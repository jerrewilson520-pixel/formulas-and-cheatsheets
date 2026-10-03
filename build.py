#!/usr/bin/env python3
"""Build the TI-84 Evo Python app from src/chem151_content.py.

Writes TI84EVO/CHEM151.py (the program you run) and
TI84EVO/C151Dnn.py (data files it loads one at a time, so the
calculator's small Python heap never holds the whole sheet at once).

Usage:  python3 build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))
from chem151_content import MODULES, NOTATION_KEY, FULL_TITLES  # noqa: E402

OUT = os.path.join(HERE, "TI84EVO")
COLS = 25          # default chars per printed line (safe for all models)
ROWS = 10          # default lines per screen
CHUNK = 3200       # max characters of text per data file
GLOSS_CHUNK = 1100 # max characters per glossary page
MAX_LINE = 72      # max source line length in generated files
TAB_KEYS = ("F", "V", "N", "C")


# ----------------------------------------------------------------- text
def bullets(items):
    out = []
    for it in items:
        if "\n" in it:            # a block with a heading
            if out:
                out.append("")
            out.append(it)
            out.append("")
        else:
            out.append("* " + it)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


def var_lines(vs):
    return "\n".join("* %s = %s" % (s, m) for s, m in vs)


def cheats(items):
    return "\n\n".join(items)


def tab_text(u, key):
    if key == "F":
        return bullets(u["F"])
    if key == "V":
        return var_lines(u["V"])
    if key == "N":
        return bullets(u["N"])
    return cheats(u["C"])


def code_of(u):
    return u["title"].split(" ")[0]


# ------------------------------------------------------------ doc store
class Store:
    def __init__(self):
        self.docs = []

    def add(self, text):
        self.docs.append(text)
        return len(self.docs) - 1

    def pack(self):
        """Assign docs to files. Returns (files, refs) where
        refs[doc_id] = file_no*100 + index."""
        files, refs = [[]], {}
        size = 0
        for i, t in enumerate(self.docs):
            if files[-1] and (size + len(t) > CHUNK or len(files[-1]) >= 99):
                files.append([])
                size = 0
            refs[i] = len(files) * 100 + len(files[-1])
            files[-1].append(t)
            size += len(t)
        return files, refs


def lit(s):
    """Python string literal(s) for s, split into short source lines."""
    esc = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    parts, cur = [], ""
    i = 0
    while i < len(esc):
        tok = esc[i:i + 2] if esc[i] == "\\" else esc[i]
        cur += tok
        i += len(tok)
        if len(cur) >= MAX_LINE - 8 and (tok == " " or len(cur) >= MAX_LINE - 4):
            parts.append(cur)
            cur = ""
    if cur or not parts:
        parts.append(cur)
    return "\n".join('"%s"' % p for p in parts)


def check_ascii(name, text):
    for n, line in enumerate(text.split("\n"), 1):
        for ch in line:
            if not (32 <= ord(ch) < 127):
                raise SystemExit("Non-ASCII %r in %s line %d: %s" % (ch, name, n, line))
        if "`" in line:
            raise SystemExit("Backtick in %s line %d" % (name, n))


# ------------------------------------------------------------- glossary
def sort_key(sym):
    core = sym.lstrip("<[(%#|_ ")
    return (core.lower(), sym)


def build():
    st = Store()
    tree = []          # (title, [(unit title, [ref ids])])
    all_f, all_v = [], []
    gloss = {}         # (sym, meaning) -> [unit codes]

    for mi, m in enumerate(MODULES, 1):
        if len("%d) %s" % (mi, m["title"])) > COLS:
            raise SystemExit("Module title too long: " + m["title"])
        for ui, u in enumerate(m["units"], 1):
            if len("%d) %s" % (ui, u["title"])) > COLS:
                raise SystemExit("Unit title too long: " + u["title"])
    for m in MODULES:
        units = []
        fdoc, vdoc = [], []
        for u in m["units"]:
            ids = []
            for k in TAB_KEYS:
                t = tab_text(u, k)
                if not u[k]:
                    ids.append(-1)
                else:
                    check_ascii(u["title"] + "/" + k, t)
                    ids.append(st.add(t))
            units.append((u["title"], ids))
            if u["F"]:
                fdoc.append("[" + u["title"] + "]\n" + bullets(u["F"]))
            if u["V"]:
                vdoc.append("[" + u["title"] + "]\n" + var_lines(u["V"]))
            for s, meaning in u["V"]:
                gloss.setdefault((s, meaning), []).append(code_of(u))
        tree.append((m["title"], units))
        if fdoc:
            all_f.append((m["title"], st.add("\n\n".join(fdoc))))
        if vdoc:
            all_v.append((m["title"], st.add("\n\n".join(vdoc))))

    # glossary A-Z
    entries = sorted(gloss.items(), key=lambda kv: sort_key(kv[0][0]) + (kv[0][1],))
    # group by first letter, then pack whole letters into pages
    letters = []       # [(letter, [lines])]
    for (sym, mn), codes in entries:
        L = sort_key(sym)[0][:1].upper() or "#"
        if not L.isalpha():
            L = "#"
        if not letters or letters[-1][0] != L:
            letters.append((L, []))
        letters[-1][1].append("* %s = %s [%s]" % (sym, mn, ", ".join(codes)))
    all_g, pg = [], []

    def flush():
        if pg:
            a, b = pg[0][0], pg[-1][0]
            label = a if a == b else a + " - " + b
            text = "\n\n".join("%s\n%s" % (L, "\n".join(ls)) for L, ls in pg)
            all_g.append((label, st.add(text)))
            pg[:] = []

    for L, ls in letters:
        size = sum(len(x) for _, l2 in pg for x in l2)
        if pg and size + sum(len(x) for x in ls) > GLOSS_CHUNK:
            flush()
        pg.append((L, ls))
    flush()

    consts = var_lines(MODULES[0]["units"][0]["V"]) + "\n\n" + bullets(MODULES[0]["units"][0]["N"])
    acon = st.add(consts)

    codes = [code_of(u) for m in MODULES for u in m["units"]]
    if [t.split(" ")[0] for t in FULL_TITLES] != codes:
        raise SystemExit("FULL_TITLES out of sync with units")
    about = ("ABOUT\nChem 151 Formula Sheet -- Chemical Thinking Vol. I\n\n"
             "CONTENTS (modules and units)")
    i = 0
    for m in MODULES:
        about += "\n\n" + m["full"].upper()
        for u in m["units"]:
            about += "\n* " + FULL_TITLES[i]
            i += 1
    helps = []
    for block in NOTATION_KEY[-1:] + NOTATION_KEY[:-1]:   # navigation first
        head = block.split("\n")[0]
        helps.append((head.title(), st.add(block)))
    helps.append(("About/Contents", st.add(about)))

    for i, t in enumerate(st.docs):
        check_ascii("doc %d" % i, t)

    files, refs = st.pack()
    R = lambda i: -1 if i < 0 else refs[i]

    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith(".py") and os.path.isfile(os.path.join(OUT, f)):
            os.remove(os.path.join(OUT, f))

    # data files
    names = []
    for n, docs in enumerate(files, 1):
        name = "C151D%02d" % n
        names.append(name)
        body = ["# %s: data for CHEM151. Don't run this file." % name, "D=("]
        for t in docs:
            body.append(lit(t) + ",")
        body.append(")")
        src = "\n".join(body) + "\n"
        check_ascii(name, src)
        write(name, src)

    # tree literal
    tl = ["TREE=("]
    for title, units in tree:
        tl.append("(%s,(" % pystr(title))
        for ut, ids in units:
            tl.append(" (%s,(%s))," % (pystr(ut), ",".join(str(R(i)) for i in ids)))
        tl.append(")),")
    tl.append(")")
    tl.append('ALLM=("All formulas","All variables","Glossary A-Z","Constants")')
    for var, lst in (("AF", all_f), ("AV", all_v), ("AG", all_g), ("HELPS", helps)):
        tl.append(var + "=(")
        for t, i in lst:
            tl.append(" (%s,%d)," % (pystr(t), R(i)))
        tl.append(")")
    tl.append("ACON=%d" % R(acon))

    tmpl = open(os.path.join(HERE, "src", "main_template.py")).read()
    fl = "%s..%s" % (names[0], names[-1])
    main = (tmpl.replace("@TREE@", "\n".join(tl))
                .replace("@FILES@", fl)
                .replace("@COLS@", str(COLS))
                .replace("@ROWS@", str(ROWS)))
    check_ascii("CHEM151", main)
    write("CHEM151", main)

    total = sum(len(t) for t in st.docs)
    print("docs: %d, text chars: %d, data files: %d" % (len(st.docs), total, len(files)))
    for f in sorted(x for x in os.listdir(OUT) if x.endswith(".py")):
        print("  %-12s %6d bytes" % (f, os.path.getsize(os.path.join(OUT, f))))


def pystr(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write(name, src):
    for n, line in enumerate(src.split("\n"), 1):
        if len(line) > MAX_LINE + 6:
            raise SystemExit("%s line %d too long (%d)" % (name, n, len(line)))
    with open(os.path.join(OUT, name + ".py"), "w", newline="\n") as f:
        f.write(src)


if __name__ == "__main__":
    build()
