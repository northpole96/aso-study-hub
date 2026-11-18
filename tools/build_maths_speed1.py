#!/usr/bin/env python3
"""Build ASO-Maths-Speed-1.html (26 speed, train, race and boat questions, 26 minutes) from the GS Mock 01 page and a question file.
Copied from build_maths_tw1.py on 18 Nov 2026.

    python3 tools/check_maths_speed1.py   # recomputes every answer first
    python3 tools/build_maths_speed1.py

The question file, tools/maths_speed1_questions.py, defines Q (first option is the right one unless "a" is set).
Options and question order are shuffled with a fixed seed, so a rebuild gives
the same paper.
"""
import json, random, re, sys, importlib.util, collections, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "ASO-GS-Mock-Test-2027-1.html")
OUT = os.path.join(ROOT, "ASO-Maths-Speed-1.html")

QFILE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "tools", "maths_speed1_questions.py")
spec = importlib.util.spec_from_file_location("qs", QFILE)
qs = importlib.util.module_from_spec(spec); spec.loader.exec_module(qs)
RAW = qs.Q
N = 26
assert len(RAW) == N, len(RAW)

rng = random.Random(2027_1119)

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

# ---- question order: topic blocks in syllabus order, as in the real papers; inside a block no two neighbours share a sub-type
BLOCKS = ["Speed & Time", "Trains", "Races", "Boats & Streams"]
def arrange(items):
    # greedy: always take from the biggest part left that differs from the last one (random shuffle fails with 12 of 26)
    left = collections.defaultdict(list)
    for q in items: left[q["t"]].append(q)
    for v in left.values(): rng.shuffle(v)
    o, last = [], None
    while any(left.values()):
        keys = [k for k in left if left[k] and k != last]
        if not keys: raise SystemExit("no order found")
        k = max(keys, key=lambda k: (len(left[k]), rng.random()))
        o.append(left[k].pop()); last = k
    return o
order = arrange(RAW)   # all four parts mixed, no two neighbours from one part

Qout = [dict(s=q["s"], q=q["q"], o=q["o"], a=q["a"], e=q["e"], k=q["k"], n=q["n"], c=q["c"]) for q in order]
assert len(Qout) == N
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
rep("<title>ASO GS Mock 2027</title>", "<title>ASO Speed and Trains</title>")
rep("General Studies Paper I · Mock 01", "Paper II (B) Mathematics · Speed, Trains, Races, Boats · Set 01")
rep('var SK="aso-gs-mock-2027-1";', 'var SK="aso-maths-speed-1";')
rep("<h1>GS Mock 2027</h1>", "<h1>Speed and Trains</h1>")
rep('<p class="tag">100 questions built from the<br><b>2018, 2021 and 2025</b> ASO papers<br>and the news of 2026.</p>',
    '<p class="tag">26 questions on<br><b>speed, trains, races and boats</b>,<br>every type and its twists.</p>')

# ---- intro
a = s.index('<p class="lead dropcap">'); b = s.index('<div class="rules">')
s = s[:a] + (
 '<p class="lead dropcap">Speed questions took 6 of the 50 maths questions in 2025: Robert on his cycle (Q54), two trains passing a running man (Q59, Q82), a car going 10 km/h faster (Q64) and two races (Q60, Q65). This set covers every type in the family, with the twists the examiner likes: units, average speed, late and early, chases, trains against poles, platforms and other trains, head starts, circular tracks, and boats with and against the stream.</p>\n'
 '<p class="lead" style="margin-top:14px">Three ideas solve almost all of them. Distance = speed × time. Multiply km/h by 5/18 to get metres per second. Speeds ADD when two things move towards each other and SUBTRACT when one chases the other. The four parts are mixed, so you have to spot the type yourself. Each answer names the type, shows the working, gives a shortcut and explains the trap options. Read the matching chapter of the Arithmetic Guide first if a type is new to you.</p>\n'
)+ s[b:]

a = s.index("<div><b>Tags</b>"); b = s.index("</div>", a) + 6
s = s[:a] + '<div><b>After the test</b><span>Press “Copy answers” on the result page and paste the report into the chat. Claude will build a redo set from what you got wrong or skipped.</span></div>\n<div><b>Speed</b><span>About a minute a question. If a sum is not moving, mark it and go on.</span></div>' + s[b:]
rep('<button class="btn sm" data-f="n" aria-pressed="false">2026 news</button>\n', "")

# ---- blueprint
a = s.index('<ol class="bp">'); b = s.index("</ol>", a) + 5
rows = [(k, "") for k in BLOCKS]
bpr = [(12, "Speed & Time", "units, late/early, average speed, chases · 2025 Q54, Q64"),
       (7, "Trains", "poles, platforms, men, other trains · 2025 Q59, Q82"),
       (4, "Races", "beats by, head start, circular track · 2025 Q60, Q65"),
       (3, "Boats & Streams", "downstream, upstream, there and back")]
assert sum(n for n, _, _ in bpr) == N
bp = '<ol class="bp">' + "".join(
    '<li><span class="n">%02d</span><span>%s</span><span class="dots"></span><span class="c">%s</span></li>' % (n, k, c)
    for n, k, c in bpr) + "</ol>"
s = s[:a] + bp + s[b:]
a = s.index('<p class="src" style="margin-top:14px">The weights'); b = s.index("</p>", a) + 4
s = s[:a] + ('<p class="src" style="margin-top:14px">Speed, time and distance sits under Arithmetic, topic (a) of the Paper II (B) syllabus (Advt. No. 15 of 2026-27).</p>') + s[b:]
# ---- 50-question paper: counts and time
rep("100 questions · 90 minutes · 100 marks", "26 questions · 26 minutes · 26 marks")
rep("Start exam mode · 90 min", "Start exam mode · 26 min")
rep("<span>100</span> questions", "<span>26</span> questions")
rep(">90:00<", ">26:00<")
rep("0 / 100 answered", "0 / 26 answered")
rep("DUR=90*60", "DUR=26*60")
rep("All 100 questions are answered.", "All 26 questions are answered.")
rep("net marks out of 100", "net marks out of 26")

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
    '    out.push("ASO SPEED AND TRAINS SET 01 — MY ANSWERS");\n'
    '    out.push((st.mode==="exam"?"Exam mode":"Practice mode")+(st.timeUp?" (time ran out)":"")+" · "+d.toLocaleDateString("en-IN",{day:"numeric",month:"short",year:"numeric"}));\n'
    '    out.push("Net "+net.toFixed(2)+" / 26 · Right "+r+" · Wrong "+w+" · Skipped "+s);\n'
    '    out.push("Please make the next speed set from my wrong and skipped questions.");\n'
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
s = s[:a] + ("<footer>OPSC ASO 2027 · Speed, Trains, Races, Boats · Set 01 · built 18 Nov 2026 from the official syllabus and the six speed questions of the 2025 Paper II booklet. "
             "Every answer was recomputed by a script (tools/check_maths_speed1.py).</footer>") + s[b:]

open(OUT, "w", encoding="utf-8").write(s)
print("wrote", OUT, len(s))
