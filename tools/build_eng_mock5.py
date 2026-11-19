#!/usr/bin/env python3
"""Build ASO-English-Mock-Test-2027-5.html: English Mock 05, the 'most likely' paper on the 2025 layout.
Questions: tools/eng_mock5_questions.py (first option = right answer). Layout copied from ASO-English-Mock-Test-2027-4.html
(keeps var Q, the saved ans/done state and the Copy answers report).
- fill-in block: greedy order, no two neighbours with the same label, a vocabulary question first
- jumbled sentences and paragraphs: the parts are re-lettered at random so the answer codes do not repeat
- answers are spread evenly over A, B, C, D (error-spotting segments keep their sentence order)
Run: python3 tools/build_eng_mock5.py"""
import re, json, random, sys, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import eng_mock5_questions as M
rnd = random.Random(20261119)
L = "PQRS"

def relabel(parts, right, wrongs):
    """Give the four parts new letters. Returns (stem lines, right code, wrong codes)."""
    perm = list(L); rnd.shuffle(perm)            # old letter i -> new letter perm[i]
    mp = {L[i]: perm[i] for i in range(4)}
    new_parts = [None] * 4
    for i, p in enumerate(parts): new_parts[L.index(mp[L[i]])] = p
    conv = lambda code: "".join(mp[c] for c in code)
    return new_parts, conv(right), [conv(w) for w in wrongs]

def jumble_q(parts, right, wrongs, expl, label, kind):
    for _ in range(200):
        np_, r, ws = relabel(parts, right, wrongs)
        if r not in used_codes or used_codes[r] < 1: break
    used_codes[r] = used_codes.get(r, 0) + 1
    assert len({r, *ws}) == 4, (parts, r, ws)
    head = ("Rearrange the parts P, Q, R and S to make a correct sentence:" if kind == "s"
            else "Rearrange the sentences P, Q, R and S to make a meaningful paragraph:")
    stem = head + "\n" + "\n".join("(%s) %s" % (L[i], np_[i]) for i in range(4))
    mp = dict(zip(L, [None]*4))
    for i in range(4): mp[L[i]] = L[np_.index(parts[i])]          # old letter -> new letter
    expl = re.sub(r"\b([PQRS])\b", lambda m: mp[m.group(1)], expl)
    return dict(s=label, q=stem, o=[r] + ws, e="Correct order " + r + ". " + expl)

used_codes = {}
JUMB = [jumble_q(p, r, w, e, "Sentence rearrangement", "s") for p, r, w, e in M.JUMBLE]
used_codes = {}
PARA = [jumble_q(p, r, w, e, "Paragraph ordering", "p") for p, r, w, e in M.PARA]

# greedy order for the fill-in block
pool = list(M.FILL); rnd.shuffle(pool)
fill = [next(q for q in pool if q["s"] == M.V)]; pool.remove(fill[0])
while pool:
    cnt = collections.Counter(q["s"] for q in pool)
    cands = [q for q in pool if q["s"] != fill[-1]["s"]] or pool
    q = max(cands, key=lambda q: (cnt[q["s"]], rnd.random()))   # most-left label first keeps the tail mixed
    fill.append(q); pool.remove(q)
for a, b in zip(fill, fill[1:]): assert a["s"] != b["s"]

syn = [q for q in M.VOCAB2 if q["s"] == "Synonyms"]; ant = [q for q in M.VOCAB2 if q["s"] == "Antonyms"]
vocab2 = [x for pair in zip(syn, ant) for x in pair]
ALL = fill + vocab2 + list(M.ERR) + JUMB + PARA + list(M.RC)
assert len(ALL) == 100, len(ALL)

# no repeats of earlier mocks
old = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else []
norm = lambda s: re.sub(r"[^a-z ]", "", s.lower())
oldn = {norm(s) for s in old}
import difflib
bad = False
for q in ALL:
    if norm(q["q"]) in oldn: print("REPEAT:", q["q"][:70]); bad = True
    near = [o for o in old if difflib.SequenceMatcher(None, norm(o), norm(q["q"])).ratio() > 0.8]
    if near: print("NEAR:", q["q"][:70], "|", near[0][:70])
if bad: sys.exit("exact repeats found")

# spread answers: shuffle the 94 free questions to target positions
free = [q for q in ALL if q.get("k") != "err"]
fixed = collections.Counter(q["a"] for q in ALL if q.get("k") == "err")
targets = []
for pos in range(4): targets += [pos] * (25 - fixed[pos])
rnd.shuffle(targets); assert len(targets) == len(free)
Q = []
for q in ALL:
    if q.get("k") == "err":
        o, a = q["o"], q["a"]
    else:
        right, wrong = q["o"][0], q["o"][1:]
        assert len(set(q["o"])) == 4, q["q"][:50]
        wrong = wrong[:]; rnd.shuffle(wrong)
        a = targets.pop(); o = wrong[:]; o.insert(a, right)
    Q.append({"s": q["s"], "q": q["q"], "o": o, "a": a, "e": q["e"], "k": q.get("k", "rc" if q.get("p") else "one"),
              "n": False, "c": bool(q.get("c")), "p": q.get("p", 0), "r": 0, "t": 0})
print("answer spread", collections.Counter("ABCD"[q["a"]] for q in Q))

PASS = {str(k): v for k, v in M.PASSAGES.items()}
ORDER = ["Vocabulary in context", "Tenses & conditionals", "Adjective & adverb forms", "Subject–verb agreement",
         "Connectors & inversion", "Prepositions & phrasal verbs", "Articles", "Infinitive & gerund",
         "Synonyms", "Antonyms", "Error spotting", "Sentence rearrangement", "Paragraph ordering", "Comprehension"]
cnt = collections.Counter(q["s"] for q in Q)
assert set(cnt) == set(ORDER), set(cnt) ^ set(ORDER)

h = (ROOT / "ASO-English-Mock-Test-2027-4.html").read_text()
def rep(a, b, regex=False):
    global h
    n = len(re.findall(a, h, flags=re.S)) if regex else h.count(a)
    assert n >= 1, a[:60]
    h = re.sub(a, lambda m: b, h, count=1, flags=re.S) if regex else h.replace(a, b)
rep("<title>ASO English Mock 04</title>", "<title>ASO English Mock 05</title>")
rep("OPSC ASO 2027 · Paper III (A) English · Mock 04", "OPSC ASO 2027 · Paper III (A) English · Mock 05")
rep("aso-english-mock-2027-4", "aso-english-mock-2027-5")
rep(r'<p class="tag">.*?</p></header>', '<p class="tag">Set 05 · the <b>most likely</b> paper<br>on the <b>2025</b> layout · 100 new<br>questions, each the next angle of a real one.</p></header>', True)
lead = ('<p class="lead dropcap">This mock has one goal: to ask the questions most likely to come in January 2027. It copies the 2025 paper, the newest and the first to stay fully inside the printed syllabus: a long fill-in-the-blanks block, then error spotting, jumbled sentences, jumbled paragraphs and two passages, one of them about Odisha. Every question is the next step of a question the board has already asked. 2025 asked "No sooner … than", so this mock asks "Hardly … when" and "Not until … did". 2025 asked "A number of factors have", so this mock asks "The number of accidents has". Each answer names the 2025 or 2021 question it grew from and the rest of its rule family.</p>\n'
        '<p class="lead" style="margin-top:14px">Synonyms and antonyms are named in the syllabus but were missing in 2025, after 11 questions in 2021, so six of them are carved out of the fill-in block in case they return. Narration, voice, analogies and question tags are left out: they are not in the syllabus and did not come in 2025. None of the 100 questions repeats Mocks 01 to 04.</p>')
rep(r'<p class="lead dropcap">.*?</p>\s*<p class="lead" style="margin-top:14px">.*?</p>', lead, True)
blocks = [("Fill in the blanks: vocabulary, tenses, adverbs, agreement, inversion, prepositions, articles, -ing and to", "Q1–58", 58),
          ("Synonyms and antonyms in a sentence", "Q59–64", 6), ("Spot the incorrect segment", "Q65–70", 6),
          ("Rearrange the parts into a sentence", "Q71–84", 14), ("Rearrange the sentences into a paragraph", "Q85–90", 6),
          ("Reading comprehension: AI at work · olive ridleys of Odisha", "Q91–100", 10)]
rows = "".join('<li><span class="n">%02d</span><span>%s</span><span class="dots"></span><span class="c">%s</span></li>' % (n, t, r) for t, r, n in blocks)
rep(r'<ol class="bp">.*?</ol>', '<ol class="bp">' + rows + '</ol>', True)
spread = ", ".join("%s %d" % (s.lower() if s not in ("Subject–verb agreement",) else "agreement", cnt[s]) for s in ORDER)
rep(r'<p class="src" style="margin-top:14px">.*?</p>', '<p class="src" style="margin-top:14px">Syllabus spread: ' + spread + '. The 2025 paper had vocabulary 21, adverbs and inversion 15, tenses 9, agreement 7, prepositions 6, error spotting 6, rearrangement 20 and comprehension 10.</p>', True)
rep("so you can see whether to work on vocabulary, grammar or rearrangement first.", "so you can see whether to work on vocabulary, grammar or rearrangement first.")
rep(r"<footer>.*?</footer>", "<footer>OPSC ASO 2027 · English Mock 05 · the most-likely paper, built on the 2025 Paper III (A) English and the official 2026-27 syllabus.</footer>", True)
rep('ASO ENGLISH MOCK 04 — MY ANSWERS', 'ASO ENGLISH MOCK 05 — MY ANSWERS')
rep('(q.r?" (repeat of Mock 03 Q"+q.r+")":"")+(q.t?" (same rule as Mock 03 Q"+q.t+")":"")', '(q.c?" (CHECK)":"")')
rep(r'var order=\[[^\]]*\];', 'var order=' + json.dumps(ORDER, ensure_ascii=False) + ';', True)
rep(r'var Q = \[.*?\];\n', 'var Q = ' + json.dumps(Q, ensure_ascii=False) + ';\n', True)
rep(r'var PASS = \{.*?\};\n', 'var PASS = ' + json.dumps(PASS, ensure_ascii=False) + ';\n', True)
(ROOT / "ASO-English-Mock-Test-2027-5.html").write_text(h)
print("written", len(h) // 1024, "KB;", dict(cnt))
