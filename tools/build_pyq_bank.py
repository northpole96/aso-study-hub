#!/usr/bin/env python3
"""ASO-PYQ-Bank.html: every past question of every paper on one filterable page.

Papers (syllabus order): General Awareness (Paper I), Reasoning and Maths (Paper II), English and Odia (Paper III).
Years: 2018, 2021, 2025 for all papers; 2015 for Maths only.
Filters in the page: paper, year, section (topic), family, search, only CHECK.

Sources: the tagged data of the aso-mock skill (topic, family, GA/Odia text and keys) and the transcripts in pyq/
(Maths, Reasoning 2021, English: text, options, key and notes). Reasoning 2018 and 2025 have no clean transcript, so they
show our short stems only. Keys are mine (or the Udyam book's for Odia), not OPSC's.

Run: python3 tools/build_pyq_bank.py
"""
import re, json, sys, os, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/aso-mock/scripts"))
import pyq

PAPERS = [("ga", "General Awareness", "GA", "Paper I"), ("re", "Reasoning", "RE", "Paper II (A)"),
          ("ma", "Maths", "MA", "Paper II (B)"), ("en", "English", "EN", "Paper III (A)"), ("od", "Odia", "OD", "Paper III (B)")]
SKILL_NAME = {"ga": "ga", "re": "reasoning", "ma": "maths", "en": "english", "od": "odia"}
out, LABELS, PASSAGES = [], {}, []
warn = []


def mod(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def clean_stem(s):
    s = re.sub(r"\s*\*\*CHECK\*\*.*", "", s, flags=re.S)
    lines = []
    for ln in s.split("\n"):
        if re.fullmatch(r"\|[-| :]+\|", ln.strip()): continue
        if ln.strip().startswith("|"):
            ln = " · ".join(c.strip() for c in ln.strip().strip("|").split("|") if c.strip())
        lines.append(ln)
    return "\n".join(lines).replace("**", "").strip()


def split_opts(pre):
    """(stem, [A, B, C, D]) from the text before the answer line."""
    o = re.search(r"(?m)^\(A\)", pre)
    if not o: return pre.strip(), []
    ot = pre[o.start():]; stem = pre[:o.start()]
    opts = [x.strip() for x in re.split(r"\s*\((?=[A-D]\))", " " + ot) if x.strip()]
    opts = [re.sub(r"\s+", " ", re.sub(r"^[A-D]\)\s*", "", x)).strip() for x in opts]
    if len(opts) != 4: return pre.strip(), []   # options lost or only described (e.g. "(A)-(D) four versions")
    return stem, opts


def blocks(path, lo, hi):
    """{n: body} from a transcript; the first block of each number inside lo..hi wins."""
    t = open(path, encoding="utf-8").read()
    parts = re.split(r"(?m)^\*\*(\d+)\.\*\*\s*", t)
    res = {}
    for i in range(1, len(parts), 2):
        n = int(parts[i])
        if not lo <= n <= hi or n in res: continue
        res[n] = re.split(r"(?m)^(?:---|#{2,3} |> )", parts[i + 1])[0].strip()
    return res


def passages(path):
    """[(lo, hi, text)] from '### Passage (Q91–95)' + blockquote."""
    t = open(path, encoding="utf-8").read(); res = []
    for m in re.finditer(r"(?m)^###\s*Passage[^\n]*?\(Q?(\d+)\s*[–-]\s*(\d+)\)[^\n]*\n+((?:>[^\n]*\n?)+)", t):
        ls = [l[1:].strip() for l in m.group(3).splitlines()]
        txt = re.sub(r"\n{3,}", "\n\n", "\n".join(ls)).strip().replace("**", "")
        res.append((int(m.group(1)), int(m.group(2)), txt))
    return res


def add_passage(y, lo, hi, txt, bag):
    PASSAGES.append(txt); bag[(y, lo, hi)] = len(PASSAGES) - 1


def fam(f): return f.split(".", 1)[-1]


# ---------------------------------------------------------------- Maths and Reasoning 2021 (Paper II transcripts)
P2FILES = {2015: "OPSC-ASO-2015-Maths-Paper-II.md", 2018: "OPSC-ASO-2018-Maths-Paper-II.md",
           2021: "OPSC-ASO-2021-Reasoning-Maths-Paper-II.md", 2025: "OPSC-ASO-2025-Maths-Paper-II.md"}


def parse_p2(y, fn, lo, hi, pk, tags):
    for n, body in sorted(blocks(os.path.join(ROOT, "pyq", fn), lo, hi).items()):
        m = re.search(r"\*\*Answer:?\s*([^*]*?)\*\*\s*[—-]?\s*", body)
        ans, why, pre = "", "", body
        if m: pre = body[:m.start()].strip(); ans = m.group(1); why = body[m.end():].strip()
        stem, opts = split_opts(pre)
        tg = tags.get((y, n), {})
        out.append(dict(p=pk, y=y, q=n, s=clean_stem(stem), o=opts, a=ans, w=why.replace("**", ""),
                        c=("CHECK" in body or "Check" in body), t=pk + ":" + tg.get("topic", ""), f=fam(tg.get("family", ""))))


for pk, name, lo, hi in (("ma", "maths", 51, 100), ("re", "reasoning", 1, 50)):
    tags = {(r["y"], r["q"]): r for r in pyq.load(name)}
    LABELS.update({pk + ":" + k: v for k, v in pyq.topics(name).LABEL.items()})
    for y, fn in P2FILES.items():
        if pk == "re" and y == 2015: continue
        if pk == "re" and y != 2021:   # raw scans only: our short stems, no options, no key
            for (yy, n), tg in sorted(tags.items()):
                if yy == y:
                    out.append(dict(p=pk, y=y, q=n, s=tg["stem"], o=[], a="", c=False, t=pk + ":" + tg["topic"], f=fam(tg["family"]),
                                    w="Options and key are not in our files for this year (raw scan, no clean transcript). The question above is a short summary."))
            continue
        parse_p2(y, fn, lo, hi, pk, tags)

# ---------------------------------------------------------------- General Awareness (data files + the 2021 key)
LABELS.update({"ga:" + k: v for k, v in pyq.topics("ga").LABEL.items()})
key21 = mod(os.path.join(ROOT, "tools", "ga21_answers.py")).A
for r in pyq.load("ga"):
    a, why, c = r["ans"], "", bool(r["check"])
    if r["y"] == 2021:
        why = key21[r["q"]][1]
    if a not in ("A", "B", "C", "D"):
        a, why = "", "No usable key for this question (scan unclear or question dropped)."
    out.append(dict(p="ga", y=r["y"], q=r["q"], s=re.sub(r"\s+", " ", r["stem"]).strip() if "\n" not in r["stem"] else r["stem"],
                    o=r["opts"], a=a, w=why, c=c, t="ga:" + r["topic"], f=fam(r["family"])))

# ---------------------------------------------------------------- English (transcripts; family tags from the data file)
LABELS.update({"en:" + k: v for k, v in pyq.topics("english").LABEL.items()})
ENF = {2018: "OPSC-ASO-2018-English-Paper-III.md", 2021: "OPSC-ASO-2021-English-Paper-III.md", 2025: "OPSC-ASO-2025-English-Paper-III.md"}
etags = {(r["y"], r["q"]): r for r in pyq.load("english")}
pg = {}
for y, fn in ENF.items():
    path = os.path.join(ROOT, "pyq", fn)
    for lo, hi, txt in passages(path): add_passage(y, lo, hi, txt, pg)
    for n, body in sorted(blocks(path, 1, 100).items()):
        m = re.search(r"\*\*Answer:?\s*([^*]*?)\*\*\s*[—-]?\s*", body)
        pre, raw, why = body, "", ""
        if m: pre = body[:m.start()]; raw = m.group(1).strip(); why = body[m.end():].strip()
        stem, opts = split_opts(pre)
        tg = etags[(y, n)]
        a = raw if re.fullmatch(r"[A-D]", raw) else tg["ans"]
        if a not in ("A", "B", "C", "D"): a = ""
        if a and a != tg["ans"]: warn.append("English %s Q%s: transcript key %r, data key %r" % (y, n, raw, tg["ans"]))
        if not re.fullmatch(r"[A-D]", raw): why = ("Answer given in the transcript: " + raw + " " + why).strip()
        c = bool(re.search(r"\*\*Check|CHECK|\bCheck:", why + " " + raw))
        g = next((v for (yy, lo, hi), v in pg.items() if yy == y and lo <= n <= hi), None)
        e = dict(p="en", y=y, q=n, s=clean_stem(stem), o=opts, a=a, w=why.replace("**", ""), c=c, t="en:" + tg["topic"], f=fam(tg["family"]))
        if g is not None: e["g"] = g
        out.append(e)

# ---------------------------------------------------------------- Odia (data file; notes from the local transcripts)
LABELS.update({"od:" + k: v for k, v in pyq.topics("odia").LABEL.items()})
om = mod(os.path.join(ROOT, ".claude/skills/aso-mock/data/odia.py"))
notes = {}
for y in (2018, 2021, 2025):
    t = open(os.path.join(ROOT, "pyq", "OPSC-ASO-%d-Odia-Paper-III.md" % y), encoding="utf-8").read()
    parts = re.split(r"(?m)^\*\*(\d+)\.\*\*\s*", t)
    for i in range(1, len(parts), 2):
        n = int(parts[i])
        if (y, n) in notes: continue
        nt = [l[1:].strip() for l in parts[i + 1].splitlines() if l.startswith(">")]
        notes[(y, n)] = " ".join(nt)
opg = {}
for (lo, hi), txt in om.PASSAGES.items(): add_passage(2025, lo, hi, txt, opg)
for r in pyq.load("odia"):
    y, n, a = r["y"], r["q"], r["ans"]
    nv = n in om.NV.get(y, []) or a not in ("A", "B", "C", "D")
    why = notes.get((y, n), "")
    why_c = om.CHECK_WHY.get((y, n), "")
    if why_c: why = (why + " CHECK: " + why_c).strip()
    if nv: why = ("Not valued: OPSC dropped this question. " + why).strip()
    e = dict(p="od", y=y, q=n, s=r["stem"], o=r["opts"], a="" if nv else a, w=why, c=bool(r["check"]) or bool(why_c),
             t="od:" + r["topic"], f=fam(r["family"]))
    if nv: e["nv"] = 1
    g = next((v for (yy, lo, hi), v in opg.items() if yy == y and lo <= n <= hi), None)
    if g is not None: e["g"] = g
    out.append(e)

# ---------------------------------------------------------------- order and checks
PO = {p[0]: i for i, p in enumerate(PAPERS)}
out.sort(key=lambda d: (PO[d["p"]], d["y"], d["q"]))
cnt = {}
for d in out: cnt[(d["p"], d["y"])] = cnt.get((d["p"], d["y"]), 0) + 1
want = {("ga", 2018): 100, ("ga", 2021): 100, ("ga", 2025): 100, ("re", 2018): 50, ("re", 2021): 50, ("re", 2025): 50,
        ("ma", 2015): 50, ("ma", 2018): 50, ("ma", 2021): 50, ("ma", 2025): 50,
        ("en", 2018): 100, ("en", 2021): 100, ("en", 2025): 100, ("od", 2018): 100, ("od", 2021): 100, ("od", 2025): 100}
assert cnt == want, (cnt, want)
assert len({(d["p"], d["y"], d["q"]) for d in out}) == len(out)
for d in out:
    assert d["t"] in LABELS, (d["p"], d["y"], d["q"], d["t"])
    assert d["s"], (d["p"], d["y"], d["q"], "empty stem")
bad = [(d["p"], d["y"], d["q"], len(d["o"])) for d in out if d["p"] in ("ga", "en", "od") and len(d["o"]) != 4]
nokey = [(d["p"], d["y"], d["q"]) for d in out if d["p"] in ("ga", "en", "od", "ma") and d["o"] and not d["a"] and not d.get("nv")]
print("counts", {k[0] + str(k[1]): v for k, v in cnt.items()}, "total", len(out))
print("not 4 options:", bad)
print("options but no key:", nokey)
print("key mismatches:", *warn, sep="\n  ")

# ---------------------------------------------------------------- page
JS = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
HTML = open(os.path.join(ROOT, "tools/pyq_bank_template.html"), encoding="utf-8").read()
HTML = (HTML.replace("__DATA__", JS(out)).replace("__TOPICS__", JS(LABELS)).replace("__PASSAGES__", JS(PASSAGES))
        .replace("__PAPERS__", JS([[k, n, s, w] for k, n, s, w in PAPERS])))
open(os.path.join(ROOT, "ASO-PYQ-Bank.html"), "w", encoding="utf-8").write(HTML)
print("wrote ASO-PYQ-Bank.html", len(HTML) // 1024, "KB")
