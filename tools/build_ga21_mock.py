#!/usr/bin/env python3
"""Build ASO-GA-Mock-2021-Paper-I.html: the 2021 GA Paper I as a timed mock (same 100 questions, same order).
Questions: pyq/OPSC-ASO-2021-GA-Paper-I.md. Hand-made key: tools/ga21_answers.py. Layout: ASO-English-Mock-Test-2027-4.html.
Run: python3 tools/build_ga21_mock.py"""
import re, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from ga21_answers import A, SEC, ORDER
md = (ROOT / "pyq/OPSC-ASO-2021-GA-Paper-I.md").read_text()
tpl = (ROOT / "ASO-English-Mock-Test-2027-4.html").read_text()
def clean(t): return re.sub(r"\*+", "", t).replace("`", "").replace("[sic — likely Intel]", "").replace("[sic]", "").strip()
lines = md.split("\n"); i = 0; Q = []
while i < len(lines):
    m = re.match(r"^\*\*(\d{1,3})\.\*\*\s*(.*)$", lines[i].strip())
    if not m: i += 1; continue
    n = int(m.group(1)); blk = [m.group(2)]; i += 1
    while i < len(lines) and lines[i].strip() != "---" and not re.match(r"^\*\*\d{1,3}\.\*\*", lines[i].strip()):
        if lines[i].strip(): blk.append(lines[i].strip())
        i += 1
    rows = []
    for b in blk:
        if b.startswith("|"):
            cells = [c.strip() for c in b.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "): continue
            rows.append(" — ".join(cells))
        else: rows.append(b)
    # drop the table header row (List-I — List-II etc.)
    body = "\n".join(rows)
    body = re.sub(r"\n(State — Dance|List-I[^\n]* — List-II[^\n]*)\n", "\n", body)
    k = body.find("(A) ")
    assert k >= 0, n
    stem, optstr = body[:k].strip(), body[k:].replace("\n", " ")
    parts = re.split(r"\(([A-D])\) ", optstr)[1:]
    opts = [clean(parts[j+1]) for j in range(0, len(parts), 2)]
    assert len(opts) == 4, (n, opts)
    letter, expl, chk = A[n]
    q = {"s": SEC[n], "q": clean(stem), "o": opts, "a": "ABCD".index(letter), "e": expl}
    if chk: q["c"] = 1
    Q.append(q)
assert len(Q) == 100, len(Q)
h = tpl
h = h.replace("ASO English Mock 04", "ASO GA Mock · 2021 paper").replace("Paper III (A) English · Mock 04", "Paper I General Awareness · 2021 paper")
h = h.replace("aso-english-mock-2027-4", "aso-ga-mock-2021")
h = h.replace("<h1>English Mock 2027</h1>", "<h1>GA Mock 2021</h1>")
h = re.sub(r'<p class="tag">.*?</p></header>', '<p class="tag">The <b>2021</b> General Awareness paper,<br>the same 100 questions in the<br>same order, as a timed test.</p></header>', h, count=1, flags=re.S)
lead = ('<p class="lead dropcap">This is the real 2021 Paper I (General Awareness), question for question. Questions 1 to 20 are current affairs from 2022, 21 to 30 history, 31 to 51 polity and administration, 52 to 60 international bodies, 61 to 80 geography, 81 to 90 defence, 91 science and 92 to 100 environment. Take it once under exam rules to see where you stand against the paper the board actually set.</p>\n'
        '<p class="lead" style="margin-top:14px">There is no official key. The answers are worked out from standard books. About one question in four is tagged <b>Check</b>: the key may be wrong or the question itself is loose (a misprint, or two options that could both work). Do not trust a Check answer without looking it up. The 2022 current-affairs questions are old news now, so use them to learn the style, not to learn the facts.</p>')
h = re.sub(r'<p class="lead dropcap">.*?</p>\s*<p class="lead" style="margin-top:14px">.*?</p>', lambda m: lead, h, count=1, flags=re.S)
h = h.replace("so you can see whether to work on vocabulary, grammar or rearrangement first.", "so you can see which topic to work on first.")
rng = {}
for idx, q in enumerate(Q):
    rng.setdefault(q["s"], []).append(idx + 1)
def fmt(ns):
    out = []; s = p = ns[0]
    for x in ns[1:] + [None]:
        if x == p + 1 if x else False: p = x; continue
        out.append("%d–%d" % (s, p) if p > s else str(s))
        if x: s = p = x
    return ", ".join(out)
rows = "".join('<li><span class="n">%02d</span><span>%s</span><span class="dots"></span><span class="c">Q%s</span></li>' % (len(rng[s]), s, fmt(rng[s])) for s in ORDER)
h = re.sub(r'<ol class="bp">.*?</ol>', lambda m: '<ol class="bp">' + rows + '</ol>', h, count=1, flags=re.S)
h = re.sub(r'<p class="src" style="margin-top:14px">.*?</p>', '<p class="src" style="margin-top:14px">Marks: 100 questions, 100 marks, 90 minutes, minus a quarter for each wrong answer. Source: OPSC ASO 2021 Paper I, booklet A (exam held in 2022).</p>', h, count=1, flags=re.S)
h = h.replace("English Mock 04 · built on the layout of the 2021 Paper III (A) English and the official 2026-27 syllabus.", "GA Mock · the 2021 General Awareness paper, question for question.")
h = h.replace('ASO ENGLISH MOCK 04 — MY ANSWERS', 'ASO GA MOCK (2021 PAPER) — MY ANSWERS')
h = h.replace('(q.r?" (repeat of Mock 03 Q"+q.r+")":"")+(q.t?" (same rule as Mock 03 Q"+q.t+")":"")', '(q.c?" (CHECK: key not verified)":"")')
h = h.replace("""(q.r?'<span class="tag news">Repeat · M03 Q'+q.r+'</span>':'')+(q.t?'<span class="tag">Same rule · M03 Q'+q.t+'</span>':'')+""", "")
h = re.sub(r'var order=\[[^\]]*\];', lambda m: 'var order=' + json.dumps(ORDER, ensure_ascii=False) + ';', h, count=1)
h = re.sub(r'var Q = \[.*?\];\n', lambda m: 'var Q = ' + json.dumps(Q, ensure_ascii=False) + ';\n', h, count=1, flags=re.S)
h = re.sub(r'var PASS = \{.*?\};\n', 'var PASS = {};\n', h, count=1, flags=re.S)
(ROOT / "ASO-GA-Mock-2021-Paper-I.html").write_text(h)
print("written", len(h), "bytes;", sum(1 for q in Q if q.get("c")), "check-tagged")
