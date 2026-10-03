# CHEM151: Chem 151 Formula Sheet
# Chemical Thinking Vol. I
# For TI-84 Evo / TI-84 Plus CE Python.
# Also needs the data files @FILES@
# Run CHEM151. Type a number then [enter].
# [enter]=next page  -=prev page
# 0=back  00=main menu  [on]=quit
#
# Screen size. Change here, or use Screen
# setup in the app (saved in list CHEMS).
COLS=@COLS@
ROWS=@ROWS@

import gc
try:
  import sys
except:
  sys=None
try:
  from ti_system import disp_clr as _dc
except:
  _dc=None
try:
  from ti_system import recall_list,store_list
  _s=recall_list("CHEMS")
  if 16<=int(_s[0])<=60 and 5<=int(_s[1])<=30:
    COLS=int(_s[0])
    ROWS=int(_s[1])
except:
  pass

TABS=("Formulas","Variables","Notes","Cheats")
@TREE@

def clr():
  if _dc:
    try:
      _dc()
      return
    except:
      pass
  print("\n"*ROWS)

def ask(p):
  try:
    return input(p).strip()
  except EOFError:
    return "0"

def cut(s):
  if len(s)>COLS:
    return s[:COLS]
  return s

def brk(s,h,w):
  # where to split a too-long formula: after an
  # operator with the fewest open brackets
  k=w-1
  bd=99
  d=0
  bar=0
  for i in range(h,w):
    c=s[i]
    if c in "([":
      d+=1
    elif c in ")]":
      d-=1
    elif c=="|":
      bar=1-bar
    elif i>h+2 and (c in "/*+=," or (c=="-" and s[i-1]!="^")):
      if d+bar<=bd:
        bd=d+bar
        k=i
  return k

def wrap(t,w):
  out=[]
  for p in t.split("\n"):
    h=2
    i=p.find(". ")
    if 0<i<3 and p[:i].isdigit():
      h=i+2
    if h>w-4:
      h=0
    cur=None
    pad=""
    for wd in p.split(" "):
      if not wd:
        continue
      if cur is not None and len(cur)+1+len(wd)<=w:
        cur=cur+" "+wd
        continue
      if cur is not None:
        out.append(cur)
        pad=" "*h
      cur=pad+wd
      while len(cur)>w:
        k=brk(cur,h,w)
        out.append(cur[:k+1])
        cur=" "*h+cur[k+1:]
    if cur is None:
      cur=""
    out.append(cur)
  return out

def load(r):
  nm="C151D"+str(r//100//10)+str(r//100%10)
  gc.collect()
  try:
    m=__import__(nm)
  except ImportError:
    clr()
    print(cut("Missing file "+nm))
    print("Send all C151D files")
    print("to the calculator.")
    ask("[enter]")
    return None
  t=m.D[r%100]
  del m
  if sys:
    try:
      del sys.modules[nm]
    except:
      pass
  gc.collect()
  return t

def view(title,r):
  t=load(r)
  if t is None:
    return 0
  L=wrap(t,COLS)
  t=None
  n=ROWS-2
  if n<1:
    n=1
  np=(len(L)+n-1)//n
  if np<1:
    np=1
  p=0
  while True:
    clr()
    pg=" "+str(p+1)+"/"+str(np)
    print(title[:COLS-len(pg)]+pg)
    for s in L[p*n:p*n+n]:
      print(s)
    if COLS<25:
      k=ask("ent,-,0>")
    elif p<np-1:
      k=ask("ent:next -:prev 0:back>")
    else:
      k=ask("ent/0:back -:prev>")
    if k=="":
      if p<np-1:
        p+=1
      else:
        return 0
    elif k=="-":
      if p>0:
        p-=1
    elif k=="0":
      return 0
    elif k=="00":
      return 2
    elif k.isdigit():
      v=int(k)-1
      if 0<=v<np:
        p=v

def menu(title,items,top=False):
  n=ROWS-2
  if n<1:
    n=1
  np=(len(items)+n-1)//n
  p=0
  while True:
    clr()
    print(cut(title))
    for i in range(p*n,min(len(items),p*n+n)):
      print(cut(str(i+1)+") "+items[i]))
    if top:
      q="#,0:quit"
    else:
      q="#,0:back"
    if np>1:
      q=q+",ent:more"
    k=ask(q+">")
    if k=="":
      p=(p+1)%np
    elif k=="-":
      p=(p-1)%np
    elif k=="0":
      return -1
    elif k=="00":
      return -2
    elif k.isdigit():
      v=int(k)-1
      if 0<=v<len(items):
        return v

def unit(u):
  name=u[0]
  code=name.split(" ")[0]
  refs=u[1]
  lab=[]
  rr=[]
  for j in range(4):
    if refs[j]>=0:
      lab.append(TABS[j])
      rr.append(refs[j])
  while True:
    c=menu(name,lab)
    if c==-1:
      return 0
    if c==-2:
      return 2
    if view(code+" "+lab[c].upper(),rr[c])==2:
      return 2

def module(m):
  us=m[1]
  names=[u[0] for u in us]
  while True:
    c=menu(m[0],names)
    if c==-1:
      return 0
    if c==-2:
      return 2
    if unit(us[c])==2:
      return 2

def docs(title,lst):
  names=[d[0] for d in lst]
  while True:
    c=menu(title,names)
    if c==-1:
      return 0
    if c==-2:
      return 2
    if view(names[c],lst[c][1])==2:
      return 2

def allfv():
  while True:
    c=menu("ALL FORMULAS+VARS",ALLM)
    if c==-1:
      return 0
    if c==-2:
      return 2
    if c==0:
      r=docs("All formulas",AF)
    elif c==1:
      r=docs("All variables",AV)
    elif c==2:
      r=docs("Glossary A-Z",AG)
    else:
      r=view("CONSTANTS",ACON)
    if r==2:
      return 2

def num(p,lo,hi,d):
  k=ask(p)
  try:
    v=int(k)
  except:
    return d
  if v<lo or v>hi:
    return d
  return v

def screen():
  global COLS,ROWS
  clr()
  print("....5....10...15...20...25...30...35...40")
  print("Number at the right edge")
  print("of the line above, minus 1")
  print("= chars per line.")
  COLS=num("Chars/line ("+str(COLS)+")?",16,60,COLS)
  ROWS=num("Lines/screen ("+str(ROWS)+")?",5,30,ROWS)
  try:
    store_list("CHEMS",[COLS,ROWS])
  except:
    pass
  clr()
  for i in range(ROWS-1):
    print(str(i+1)+" "+"#"*(COLS-len(str(i+1))-1))
  ask("All on screen? [enter]")

def main():
  items=[m[0] for m in TREE]
  items=items+["ALL Formulas+Vars","Notation key/Help","Screen setup"]
  nm=len(TREE)
  while True:
    c=menu("CHEM 151 FORMULAS",items,True)
    if c==-1:
      clr()
      return
    if c==-2:
      continue
    if c<nm:
      module(TREE[c])
    elif c==nm:
      allfv()
    elif c==nm+1:
      docs("Notation key/Help",HELPS)
    else:
      screen()

main()
