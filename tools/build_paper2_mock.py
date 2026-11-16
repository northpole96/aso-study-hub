#!/usr/bin/env python3
"""Build ASO-Reasoning-Maths-Mock-2021-Paper-II.html: the 2021 Paper II as a timed mock.
Questions come from pyq/OPSC-ASO-2021-Reasoning-Maths-Paper-II.md; figure crops from a folder of PNGs
(argument 1: folder holding q8.png, q9.png ...). Layout is copied from ASO-English-Mock-Test-2027-4.html.
Run: python3 tools/build_paper2_mock.py <crop folder>"""
import re, sys, json, base64, subprocess, tempfile, os, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
md = (ROOT / "pyq/OPSC-ASO-2021-Reasoning-Maths-Paper-II.md").read_text()
tpl = (ROOT / "ASO-English-Mock-Test-2027-4.html").read_text()
crops = Path(sys.argv[1])

SEC = {}
for name, nums in {
 "Coding and decoding": [2,15,17,21,34,35,44], "Direction sense": [14,36,37], "Blood relations": [16,18,19,20,45],
 "Ranking and dictionary order": [1,13,38,42], "Number series": [30,31,32], "Number relation": [10,43],
 "Arithmetic reasoning": [6,7,11,12,24,28,50], "Analogy and odd one out": [22,23,25,29,33,41],
 "Cubes and dice": [3,4,5,9,39,40], "Counting figures": [8,26,27,49], "Mirror and water images": [46,47,48],
 "Arithmetic": list(range(51,64))+[68,78,82,93], "Algebra": [64,65,66,67]+list(range(69,78))+[83],
 "Probability": [79,80,81,84,85,89,90,91,92], "Mensuration": [86,87,88], "Statistics": list(range(94,101))}.items():
    for n in nums: SEC[n] = name
ORDER = ["Coding and decoding","Direction sense","Blood relations","Ranking and dictionary order","Number series","Number relation",
 "Arithmetic reasoning","Analogy and odd one out","Cubes and dice","Counting figures","Mirror and water images",
 "Arithmetic","Algebra","Probability","Mensuration","Statistics"]
GUESS = {8:"B",9:"C",26:"C",30:"B",39:"C",42:"B",47:"A",49:"D",77:"B"}   # no verified key: best guesses, tagged Check
IMGQ = {8,9,26,27,39,40,46,47,48,49}

def clean(t): return re.sub(r"\*\*", "", t).replace("`", "").strip()
lines = md.split("\n"); i = 0; dirs = []; Q = []; PASS = {}
while i < len(lines):
    s = lines[i].strip()
    if s.startswith("Directions (Q"):
        m = re.search(r"Nos?\. (\d+)(?: to |, | & )(\d+)", s); a, b = int(m.group(1)), int(m.group(2))
        dirs.append((a, b, "d%d" % a, re.sub(r"^Directions \(Q\. Nos\.? [^)]*\):\s*", "", s)))
    m = re.match(r"^\*\*(\d{1,3})\.\*\*\s*(.*)$", s)
    if m:
        n = int(m.group(1)); blk = [m.group(2)]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^\*\*\d{1,3}\.\*\*", lines[i].strip()): blk.append(lines[i].strip()); i += 1
        txt = [b for b in blk if not b.startswith("**Answer")]; ans = [b for b in blk if b.startswith("**Answer")][0]
        body = " ".join(txt)
        k = body.rfind("(A) ")
        if k < 0: sys.exit("no options q%d" % n)
        stem, optstr = body[:k].strip(), body[k:]
        parts = re.split(r"\(([A-D])\) ", optstr)[1:]
        opts = [parts[j+1].strip() for j in range(0, len(parts), 2)]
        assert len(opts) == 4, (n, opts)
        am = re.match(r"\*\*Answer:\s*(\S+?)\*\*\s*(?:—\s*)?(.*)$", ans); letter, expl = am.group(1), clean(am.group(2))
        chk = "Check" in ans or letter == "—"
        if letter == "—":
            letter = GUESS[n]; expl = ("No verified key. I could not solve this from the scan. The marked answer is only a best guess, so treat this question as unscored. " + re.sub(r"^Check — ", "", expl)).strip()
        expl = re.sub(r"^Check — ", "", expl).replace("Check — ", "")
        q = {"s": SEC[n], "q": clean(stem), "o": [clean(o) for o in opts], "a": "ABCD".index(letter), "e": expl}
        if chk: q["c"] = 1
        if n in IMGQ: q["i"] = "q%d" % n
        for a0, b0, key, dt in dirs:
            if a0 <= n <= b0: q["p"] = key; PASS[key] = clean(dt)
        Q.append(q); continue
    i += 1
assert len(Q) == 100, len(Q)

IMG = {}
for n in IMGQ:
    jp = tempfile.mktemp(suffix=".jpg")
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "70", str(crops / ("q%d.png" % n)), "--out", jp], check=True, capture_output=True)
    IMG["q%d" % n] = "data:image/jpeg;base64," + base64.b64encode(open(jp, "rb").read()).decode(); os.unlink(jp)

h = tpl
h = h.replace("ASO English Mock 04", "ASO Paper II Mock · 2021 paper").replace("Paper III (A) English · Mock 04", "Paper II Reasoning and Maths · 2021 paper")
h = h.replace("aso-english-mock-2027-4", "aso-paper2-mock-2021")
h = h.replace("<h1>English Mock 2027</h1>", "<h1>Paper II Mock 2021</h1>")
h = re.sub(r'<p class="tag">.*?</p></header>', '<p class="tag">The <b>2021</b> Reasoning and Maths paper,<br>the same 100 questions in the<br>same order, as a timed test.</p></header>', h, count=1, flags=re.S)
lead = ('<p class="lead dropcap">This is the real 2021 Paper II, question for question. Questions 1 to 50 are Reasoning and Mental Ability. Questions 51 to 100 are Maths. Take it once under exam rules to see where you stand against the paper the board actually set. Question 10 and question 43 are the same question; the booklet printed it twice, and it is kept twice here.</p>\n'
        '<p class="lead" style="margin-top:14px">There is no official key. The answers are worked out by hand. Nine questions (8, 9, 26, 30, 39, 42, 47, 49 and 77) could not be solved with confidence, because they depend on a crowded figure or have a faulty option list. Their marked answer is a guess and they carry a <b>Check</b> tag, so do not trust them. Figures are cropped from the scan.</p>')
h = re.sub(r'<p class="lead dropcap">.*?</p>\s*<p class="lead" style="margin-top:14px">.*?</p>', lambda m: lead, h, count=1, flags=re.S)
h = h.replace("so you can see whether to work on vocabulary, grammar or rearrangement first.", "so you can see which Reasoning or Maths topic to work on first.")
h = h.replace("Claude will build a redo set from the questions you got wrong or skipped.", "Claude will build a redo set from the questions you got wrong or skipped.")
bp = [("Coding, direction sense, relations","1–2, 14–21, 34–37, 44–45"),]
rows = ""; 
groups = [("Reasoning and Mental Ability: coding, directions, relations, ranking, series, puzzles, cubes, figures and mirror images", "Q1–50", 50), ("Arithmetic: fractions, percent, profit, interest, work, speed, averages", "Q51–63, 68, 78, 82, 93", 19), ("Algebra: quadratics, equations, matrices, progressions", "Q64–77, 83", 15), ("Probability and mensuration", "Q79–92", 14), ("Statistics: mean, median, deviations", "Q94–100", 7)]
rows = "".join('<li><span class="n">%02d</span><span>%s</span><span class="dots"></span><span class="c">%s</span></li>' % (c, t, r) for t, r, c in groups)
h = re.sub(r'<ol class="bp">.*?</ol>', lambda m: '<ol class="bp">' + rows + '</ol>', h, count=1, flags=re.S)
h = re.sub(r'<p class="src" style="margin-top:14px">.*?</p>', '<p class="src" style="margin-top:14px">Marks: 100 questions, 100 marks, 90 minutes, minus a quarter for each wrong answer. Source: OPSC ASO 2021 Paper II, booklet BH-2A/21.</p>', h, count=1, flags=re.S)
h = h.replace("English Mock 04 · built on the layout of the 2021 Paper III (A) English and the official 2026-27 syllabus.", "Paper II Mock · the 2021 Reasoning and Maths paper, question for question.")
h = h.replace('ASO ENGLISH MOCK 04 — MY ANSWERS', 'ASO PAPER II MOCK (2021 PAPER) — MY ANSWERS')
h = h.replace('(q.r?" (repeat of Mock 03 Q"+q.r+")":"")+(q.t?" (same rule as Mock 03 Q"+q.t+")":"")', '(q.c?" (CHECK: key not verified)":"")')
h = re.sub(r'var order=\[[^\]]*\];', 'var order=' + json.dumps(ORDER, ensure_ascii=False) + ';', h, count=1)
h = re.sub(r'var Q = \[.*?\];\n', lambda m: 'var Q = ' + json.dumps(Q, ensure_ascii=False) + ';\n', h, count=1, flags=re.S)
h = re.sub(r'var PASS = \{.*?\};\n', lambda m: 'var PASS = ' + json.dumps(PASS, ensure_ascii=False) + ';\nvar IMG = ' + json.dumps(IMG) + ';\n', h, count=1, flags=re.S)
h = h.replace('<div class="qtext" id="q-text"></div>', '<div class="qtext" id="q-text"></div>\n<div id="q-img" class="qimg"></div>', 1)
h = h.replace('"Passage "+q.p+" · read it, then answer"', '"Directions · read them, then answer"')
h = h.replace('$("q-text").textContent=q.q;', '$("q-text").textContent=q.q; $("q-img").innerHTML=q.i?\'<img alt="Figure for question \'+(i+1)+\'" src="\'+IMG[q.i]+\'">\':"";', 1)
h = h.replace("</style>", ".qimg{margin:6px 0 14px}.qimg:empty{display:none}.qimg img{display:block;max-width:100%;height:auto;border:1px dashed var(--rule,#d7d7da);background:#fff;padding:6px}\n.rvq .qimg img{max-width:340px}\n</style>", 1)
h = h.replace('esc(q.s)+\'</span>\'', 'esc(q.s)+\'</span>\'', 1)
(ROOT / "ASO-Paper-II-Mock-2021.html").write_text(h)
print("written", len(h), "bytes;", sum(1 for q in Q if q.get("c")), "check-tagged")
