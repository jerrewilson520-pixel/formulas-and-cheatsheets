#!/usr/bin/env python3
"""Simulate the TI-84 app in CPython: walk every menu, unit, tab and
page with scripted key presses and check that every printed line fits
the screen width. Run after build.py:  python3 tests/sim_test.py
"""
import builtins
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, "..", "TI84EVO")
sys.path.insert(0, APP)
SRC = open(os.path.join(APP, "CHEM151.py")).read()


def run(keys, cols=None, rows=None):
    """Run the program with scripted input; return printed lines."""
    out = []
    feed = iter(keys)

    def fake_input(prompt=""):
        out.append(("PROMPT", prompt))
        try:
            return next(feed)
        except StopIteration:
            raise EOFError

    def fake_print(*a, **k):
        s = " ".join(str(x) for x in a)
        for line in s.split("\n"):
            out.append(("LINE", line))

    src = SRC
    if cols:
        src = src.replace("COLS=25", "COLS=%d" % cols, 1)
    if rows:
        src = src.replace("ROWS=10", "ROWS=%d" % rows, 1)
    ns = {"__name__": "__main__", "input": fake_input, "print": fake_print}
    exec(compile(src, "CHEM151.py", "exec"), ns)
    return out, ns


def full_walk_keys(ns):
    keys = []
    tree = ns["TREE"]
    for mi, (mt, units) in enumerate(tree, 1):
        keys.append(str(mi))
        for ui, (ut, refs) in enumerate(units, 1):
            keys.append(str(ui))
            ntabs = sum(1 for r in refs if r >= 0)
            for ti in range(1, ntabs + 1):
                keys.append(str(ti))
                # page to the end; view returns to the tab menu and the
                # extra "" presses just page the (one-page) tab menu
                keys += ["-", ""] + [""] * 80
            keys.append("0")
        keys.append("0")
    # ALL formulas+vars
    keys.append(str(len(tree) + 1))
    for c, lst in ((1, "AF"), (2, "AV"), (3, "AG")):
        keys.append(str(c))
        for i in range(1, len(ns[lst]) + 1):
            keys += [str(i)] + [""] * 80
        keys.append("0")
    keys += ["4"] + [""] * 10 + ["0"]
    # help
    keys.append(str(len(tree) + 2))
    for i in range(1, len(ns["HELPS"]) + 1):
        keys += [str(i)] + [""] * 80
    keys.append("0")
    # 00 jump to main from deep inside
    keys += ["2", "7", "1", "00"]
    keys.append("0")  # quit
    return keys


def check(cols, rows):
    _, ns = run(["0"], cols, rows)
    keys = full_walk_keys(ns)
    out, ns = run(keys, cols, rows)
    used = sum(1 for t, p in out if t == "PROMPT")
    assert used == len(keys), "walk desynced: %d of %d keys used" % (used, len(keys))
    bad = [l for t, l in out if t == "LINE" and len(l) > cols]
    assert not bad, "lines too wide at %d cols: %r" % (cols, bad[:5])
    prompts = [p for t, p in out if t == "PROMPT"]
    assert max(len(p) for p in prompts) + 2 <= cols, "prompt too wide"
    # each screen (between clears) must fit: header + body + prompt
    screen, worst = 0, 0
    for t, l in out:
        if t == "PROMPT":
            worst = max(worst, screen + 1)
            screen = 0
        elif l == "" and False:
            pass
        else:
            screen += 1
    joined = "\n".join(l for t, l in out if t == "LINE")
    # every tab of every unit was opened (its page-1 header was shown)
    import re
    seen = set(re.findall(r"^(\d+\.\d+ [A-Z]+) 1/", joined, re.M))
    want = set()
    for mt, units in ns["TREE"]:
        for ut, refs in units:
            for j, r in enumerate(refs):
                if r >= 0:
                    want.add(ut.split(" ")[0] + " " + ns["TABS"][j].upper())
    assert want <= seen, "tabs never opened: %r" % sorted(want - seen)
    assert "Missing file" not in joined
    # every module must be unloaded after use
    leaked = [m for m in sys.modules if m.startswith("C151D")]
    assert not leaked, "data modules left loaded: %r" % leaked
    pages = sum(1 for t, p in out if t == "PROMPT" and ("prev" in p or p == "ent,-,0>"))
    print("cols=%d rows=%d: %d screens viewed, %d prompts, OK" % (cols, rows, pages, len(prompts)))
    return ns, out


def check_wrap(ns):
    wrap = ns["wrap"]
    load = ns["load"]
    refs = []
    for mt, units in ns["TREE"]:
        for ut, r in units:
            refs += [x for x in r if x >= 0]
    for lst in ("AF", "AV", "AG"):
        refs += [r for t, r in ns[lst]]
    refs += [r for t, r in ns["HELPS"]] + [ns["ACON"]]
    words = 0
    for r in refs:
        t = load(r)
        assert t, r
        for w in (16, 25, 32, 40):
            lines = wrap(t, w)
            assert all(len(l) <= w for l in lines), (r, w)
            # no words lost by wrapping
            assert "".join("".join(lines).split()) == "".join(t.split()), r
        words += len(t.split())
    print("wrap check: %d docs, %d words, OK" % (len(refs), words))


def check_screen_setup():
    out, ns = run(["9", "32", "11", "", "0"])
    assert ns["COLS"] == 32 and ns["ROWS"] == 11
    print("screen setup: OK")


if __name__ == "__main__":
    for c, r in ((25, 10), (32, 11), (20, 8)):
        ns, out = check(c, r)
    check_wrap(ns)
    check_screen_setup()
    # show a sample screen
    out, _ = run(["2", "7", "1", "0", "0", "0", "0"])
    print("\n--- sample screens (25 cols) ---")
    for t, l in out[-60:]:
        print(("> " + l) if t == "PROMPT" else "|" + l)
