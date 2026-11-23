#!/usr/bin/env python3
"""Build ASO-GS-Mock-Polity-Defence-1.html from the Mock 01 page and a question file.

    python3 tools/build_gs_polity_defence1.py

The question file, tools/gs_polity_defence1_questions.py, defines Q (first option is the right one unless "a" is set).
Options and question order are shuffled with a fixed seed, so a rebuild gives
the same paper.
"""
import json, random, re, sys, importlib.util, collections, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "ASO-GS-Mock-Test-2027-1.html")
OUT = os.path.join(ROOT, "ASO-GS-Mock-Polity-Defence-1.html")

QFILE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "tools", "gs_polity_defence1_questions.py")
spec = importlib.util.spec_from_file_location("qs", QFILE)
qs = importlib.util.module_from_spec(spec); spec.loader.exec_module(qs)
RAW = qs.Q
assert len(RAW) == 40, len(RAW)

rng = random.Random(2027_61)

# ---- options: shuffle where the order is free, and keep the key spread even
free = [q for q in RAW if q["a"] is None]
fixed = [q for q in RAW if q["a"] is not None]
count = collections.Counter(q["a"] for q in fixed)
slots = []
for i in range(len(free)):
    j = min(range(4), key=lambda x: (count[x], rng.random()))
    count[j] += 1; slots.append(j)
rng.shuffle(slots)
for q, pos in zip(free, slots):
    right, rest = q["o"][0], q["o"][1:]
    rng.shuffle(rest)
    rest.insert(pos, right)
    q["o"], q["a"] = rest, pos

for q in RAW:
    assert len(q["o"]) == 4 and len(set(q["o"])) == 4, q["q"]
    assert 0 <= q["a"] < 4

# ---- question order: only one topic, so mix the styles (no two long styles of one kind side by side)
def ok(order):
    if not (order[0]["k"] == "one" and not order[0]["n"]): return False
    for i in range(len(order) - 1):
        a, b = order[i], order[i + 1]
        if a["s"] == b["s"]: return False
        if a["k"] == b["k"] and a["k"] != "one": return False
    return True
for _ in range(200000):
    P_ = [q for q in RAW if q["s"] == "Polity"]; D_ = [q for q in RAW if q["s"] == "Defence"]
    rng.shuffle(P_); rng.shuffle(D_)
    first_p = rng.random() < 0.5
    order = []
    for x, y in zip(P_, D_):
        order += [x, y] if first_p else [y, x]
    if ok(order): break
else:
    raise SystemExit("no order found")

Qout = [dict(s=q["s"], q=q["q"], o=q["o"], a=q["a"], e=q["e"], k=q["k"], n=q["n"], c=q["c"]) for q in order]
by = collections.Counter(q["s"] for q in Qout)
print("topics:", dict(by))
print("kinds:", dict(collections.Counter(q["k"] for q in Qout)))
print("key spread:", sorted(collections.Counter(q["a"] for q in Qout).items()))
print("news:", sum(q["n"] for q in Qout), "check:", sum(q["c"] for q in Qout))

s = open(SRC, encoding="utf-8").read()

def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:60], s.count(old))
    s = s.replace(old, new)

# ---- questions
i = s.index("var Q = ["); j = s.index("];\n(function(){", i)
s = s[:i] + "var Q = " + json.dumps(Qout, ensure_ascii=False) + s[j + 1:]

# ---- names
rep("<title>ASO GS Mock 2027</title>", "<title>ASO GS Polity and Defence Mock 01</title>")
rep("General Studies Paper I · Mock 01", "General Studies Paper I · Polity and Defence Mock 01")
rep('var SK="aso-gs-mock-2027-1";', 'var SK="aso-gs-polity-defence-1";')
rep("<h1>GS Mock 2027</h1>", "<h1>GS Polity + Defence 01</h1>")
rep('<p class="tag">100 questions built from the<br><b>2018, 2021 and 2025</b> ASO papers<br>and the news of 2026.</p>',
    '<p class="tag">40 questions on<br><b>Constitution and Defence</b><br>syllabus topics (d) and (h).</p>')

# ---- intro
a = s.index('<p class="lead dropcap">'); b = s.index('<div class="rules">')
s = s[:a] + (
 '<p class="lead dropcap">This is a short paper on two topics only: the Indian Constitution, syllabus topic (d), and Defence and Indian Armed Forces, topic (h). In the real papers these two gave 21 questions in 2018 (13 + 8), 21 in 2021 (11 + 10) and 30 in 2025 (18 + 12). They are the two steadiest scoring parts of the paper, so they deserve a test of their own. '
 'Here are 40 questions, 20 of each, and every one is the next angle of a family the examiner has already asked: schedules, amendments, offices and committees on the Polity side; exercises, operations, ranks, missiles and ships on the Defence side.</p>\n'
 '<p class="lead" style="margin-top:14px">About a fifth of the paper is news from 2025 and 2026 (the new Chief Justice, the Vice-President, Vande Mataram, the 2026 exercises, the Rafale-M deal). '
 'None of the 40 questions repeats a Polity or Defence question from GS Mock 01 to 04, the Defence Mock, GA Mock 1 or the GA Full Test. '
 'Every answer says which past question it grew from and what else to learn in that family.</p>\n')+ s[b:]

rep("<div><b>Tags</b>", '<div><b>After the test</b><span>Press “Copy answers” on the result page and paste the report into the chat. Claude will build a redo set from what you got wrong or skipped.</span></div>\n<div><b>Tags</b>')

# ---- blueprint
a = s.index('<ol class="bp">'); b = s.index("</ol>", a) + 5
rows = [("Polity", "20 questions"), ("Defence", "20 questions")]
bpr = [(6, "Parliament, President and Governor", "Rajya Sabha, ministers, pocket veto, ordinances, Article 356"),
       (6, "Rights, courts and landmark cases", "Article 21A and 32, collegium, basic structure, anti-defection"),
       (4, "Schedules, amendments and Preamble", "schedule match, amendment order, Objectives Resolution, Article 40"),
       (4, "Offices and news", "Attorney General, CJI, Vice-President, Vande Mataram"),
       (6, "Forces, ranks and awards", "Cariappa, Arjan Singh, rank match, Param Vir Chakra, forces and ministries"),
       (8, "Weapons, ships and operations", "IGMDP, Prachand, Vikramaditya, Rafale-M, Pokhran, Kargil, Sindoor"),
       (6, "Exercises and pacts", "AUSTRAHIND, KHANJAR, INDRA, Yudh Abhyas, AUKUS")]
assert sum(n for n, _, _ in bpr) == 40
bp = '<ol class="bp">' + "".join(
    '<li><span class="n">%02d</span><span>%s</span><span class="dots"></span><span class="c">%s</span></li>' % (n, k, c)
    for n, k, c in bpr) + "</ol>"
s = s[:a] + bp + s[b:]
a = s.index('<p class="src" style="margin-top:14px">The weights'); b = s.index("</p>", a) + 4
s = s[:a] + ('<p class="src" style="margin-top:14px">The weights follow the official syllabus, topic (h), and the Defence questions of 2018, 2021 and 2025. '
             'News is taken mostly from 2025 to October 2026.</p>') + s[b:]
# ---- 50-question paper: counts and time
rep("100 questions · 90 minutes · 100 marks", "40 questions · 36 minutes · 40 marks")
rep("Start exam mode · 90 min", "Start exam mode · 36 min")
rep("<span>100</span> questions", "<span>40</span> questions")
rep(">90:00<", ">36:00<")
rep("0 / 100 answered", "0 / 40 answered")
rep("DUR=90*60", "DUR=36*60")
rep("All 100 questions are answered.", "All 40 questions are answered.")
rep("net marks out of 100", "net marks out of 40")

# ---- result page: copy-answers box
rep('<div class="sec" id="r-sec"></div>',
    '<div class="send">\n<h3>Send your answers to Claude</h3>\n'
    '<p>Copy this report and paste it into the chat. It lists every wrong and skipped question with your choice and the right answer, so the next mock can bring those back.</p>\n'
    '<div class="btns"><button class="btn pri" id="b-copy">Copy answers</button><span class="cmsg" id="copy-msg" aria-live="polite"></span></div>\n'
    '<textarea id="r-copy" readonly rows="9" aria-label="Answer report"></textarea>\n</div>\n'
    '<div class="sec" id="r-sec"></div>')
rep("</style>",
    ".send{margin-top:24px;border:1px dashed var(--rule);padding:16px 16px 14px;background-color:var(--paper);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:10px 10px}\n"
    ".send h3{font-family:var(--f-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);font-weight:400}\n"
    ".send p{margin-top:8px;font-size:1rem;line-height:1.55}\n"
    ".send .btns{margin-top:12px;align-items:center}\n"
    ".send .cmsg{font-family:var(--f-mono);font-size:11px;letter-spacing:.04em;color:var(--ok)}\n"
    ".send textarea{display:block;width:100%;box-sizing:border-box;margin-top:12px;font-family:var(--f-mono);font-size:12px;line-height:1.5;border:1px solid var(--rule);background:var(--paper);color:var(--fg);padding:10px;resize:vertical;white-space:pre-wrap;overflow-wrap:anywhere}\n"
    "</style>")
for v in ("--rule", "--paper", "--grid", "--f-mono", "--blue", "--ok", "--fg"):
    assert re.search(re.escape(v) + r"\s*:", s), "missing css var " + v

rep("st.done=true; save();", "st.done=true; st.timeUp=!!timeUp; st.at=Date.now(); save();")
rep('var order=["Polity","Modern History","Defence","Environment","Economy","Odisha","Governance","World Geography","India Geography","Institutions","Science & Tech","General News"];',
    'var order=' + json.dumps([k for k, _ in rows]) + ';')
rep('    review("all"); show("s-result");\n  }',
    '    $("r-copy").value=report(r,w,s,net,by,order); $("copy-msg").textContent="";\n'
    '    review("all"); show("s-result");\n  }\n'
    '  function one(i){ return String(Q[i].q).replace(/\\s*\\n\\s*/g," / ").replace(/\\s+/g," ").trim(); }\n'
    '  function report(r,w,s,net,by,order){\n'
    '    var d=new Date(st.at||Date.now()), out=[];\n'
    '    out.push("ASO GS POLITY + DEFENCE MOCK 01 — MY ANSWERS");\n'
    '    out.push((st.mode==="exam"?"Exam mode":"Practice mode")+(st.timeUp?" (time ran out)":"")+" · "+d.toLocaleDateString("en-IN",{day:"numeric",month:"short",year:"numeric"}));\n'
    '    out.push("Net "+net.toFixed(2)+" / 40 · Right "+r+" · Wrong "+w+" · Skipped "+s);\n'
    '    out.push("Please make the next Polity, Defence or GS mock from my wrong and skipped questions.");\n'
    '    out.push("");\n'
    '    out.push("BY TOPIC (right / wrong / skipped of total)");\n'
    '    order.forEach(function(k){ var b=by[k]; if(b) out.push("- "+k+": "+b.r+" / "+b.w+" / "+b.s+" of "+b.t); });\n'
    '    var W=[],S=[],M=[],RR=[];\n'
    '    Q.forEach(function(q,i){ var a=st.ans[i]; if(a<0) S.push(i); else if(a!==q.a) W.push(i); else { RR.push(i+1); if(st.mark[i]) M.push(i); } });\n'
    '    function line(i,withPick){ var q=Q[i], a=st.ans[i], h="Q"+(i+1)+" ["+q.s+"]";\n'
    '      if(withPick) h+=" — I chose ("+L[a]+") "+q.o[a]+"; answer ("+L[q.a]+") "+q.o[q.a];\n'
    '      else h+=" — answer ("+L[q.a]+") "+q.o[q.a];\n'
    '      return h+"\\n   "+one(i); }\n'
    '    out.push(""); out.push("WRONG ("+W.length+")"); W.forEach(function(i){ out.push(line(i,true)); });\n'
    '    out.push(""); out.push("SKIPPED ("+S.length+")"); S.forEach(function(i){ out.push(line(i,false)); });\n'
    '    if(M.length){ out.push(""); out.push("RIGHT BUT MARKED FOR REVIEW — maybe guessed ("+M.length+")"); M.forEach(function(i){ out.push(line(i,false)); }); }\n'
    '    out.push(""); out.push("RIGHT ("+RR.length+"): "+(RR.join(", ")||"none"));\n'
    '    return out.join("\\n");\n'
    '  }\n'
    '  $("b-copy").onclick=function(){\n'
    '    var t=$("r-copy"), msg=$("copy-msg"), txt=t.value;\n'
    '    function fallback(){ t.focus(); t.select(); t.setSelectionRange(0,txt.length); var ok=false; try{ ok=document.execCommand("copy"); }catch(e){}\n'
    '      msg.textContent = ok ? "Copied. Paste it into the chat." : "Your browser blocked copying. The text below is selected: copy it by hand."; }\n'
    '    if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(function(){ msg.textContent="Copied. Paste it into the chat."; }, fallback); }\n'
    '    else fallback();\n'
    '  };')

# ---- footer
a = s.index("<footer>"); b = s.index("</footer>") + 9
s = s[:a] + ("<footer>OPSC ASO 2027 · GS Polity and Defence Mock 01 · built 22 Nov 2026 from the official syllabus and the 2018, 2021 and 2025 GA papers. "
             "2026 facts come from the Current Affairs 2026 manual. Questions tagged Check rest on news reports: confirm them before the exam.</footer>") + s[b:]

open(OUT, "w", encoding="utf-8").write(s)
print("wrote", OUT, len(s))
