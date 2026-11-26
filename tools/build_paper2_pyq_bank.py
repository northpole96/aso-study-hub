#!/usr/bin/env python3
"""ASO-Maths-PYQ-Bank.html: every Maths (Q51-100: 2015, 2018, 2021, 2025) and Reasoning (Q1-50: 2018, 2021, 2025)
question on one page, filterable by subject, year, topic and family, with search.
Reasoning 2018 and 2025 have no clean transcript (raw scans), so they show our short stems only.
Run: python3 tools/build_paper2_pyq_bank.py"""
import re, json, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/aso-mock/scripts"))
import pyq
FILES = {2015: "OPSC-ASO-2015-Maths-Paper-II.md", 2018: "OPSC-ASO-2018-Maths-Paper-II.md",
         2021: "OPSC-ASO-2021-Reasoning-Maths-Paper-II.md", 2025: "OPSC-ASO-2025-Maths-Paper-II.md"}
out, LABELS = [], {}

def parse(y, fn, lo, hi, pk, tags):
    t = open(os.path.join(ROOT, "pyq", fn), encoding="utf-8").read()
    parts = re.split(r"(?m)^\*\*(\d+)\.\*\*\s*", t)
    for i in range(1, len(parts), 2):
        n = int(parts[i]); body = parts[i + 1]
        if not lo <= n <= hi: continue
        body = re.split(r"(?m)^(?:---|## )", body)[0].strip()
        m = re.search(r"\*\*Answer:?\s*([^*]*?)\*\*\s*[—-]?\s*", body)
        ans, why, pre = "", "", body
        if m: pre = body[:m.start()].strip(); ans = m.group(1); why = body[m.end():].strip()
        o = re.search(r"(?m)^\(A\)", pre); opts = []
        if o:
            ot = pre[o.start():]; pre = pre[:o.start()].strip()
            opts = [x.strip() for x in re.split(r"\s*\((?=[A-D]\))", " " + ot) if x.strip()]
            opts = [re.sub(r"^[A-D]\)\s*", "", x) for x in opts]
        tg = tags.get((y, n), {})
        stem = re.sub(r"\s*\*\*CHECK\*\*.*", "", pre, flags=re.S).strip()
        out.append(dict(p=pk, y=y, q=n, s=stem.replace("**", ""), o=opts, a=ans, w=why.replace("**", ""), c=("CHECK" in body or "Check" in body),
                        t=pk + ":" + tg.get("topic", ""), f=tg.get("family", "").split(".", 1)[-1]))

for pk, pname, lo, hi, pre in (("m", "maths", 51, 100, "Maths · "), ("r", "reasoning", 1, 50, "Reasoning · ")):
    tags = {(r["y"], r["q"]): r for r in pyq.load(pname)}
    LABELS.update({pk + ":" + k: pre + v for k, v in pyq.topics(pname).LABEL.items()})
    for y, fn in FILES.items():
        if pk == "r" and y == 2015: continue
        if pk == "r" and y != 2021:
            for (yy, n), tg in sorted(tags.items()):
                if yy == y:
                    out.append(dict(p=pk, y=y, q=n, s=tg["stem"], o=[], a="", c=False, t=pk + ":" + tg["topic"], f=tg["family"].split(".", 1)[-1],
                                    w="Options and key are not in our files for this year (raw scan, no clean transcript). The question above is a short summary."))
            continue
        parse(y, fn, lo, hi, pk, tags)
cnt = {}
for d in out: cnt[(d["p"], d["y"])] = cnt.get((d["p"], d["y"]), 0) + 1
print(cnt, len(out))
assert cnt[("m", 2015)] == 50 and cnt[("r", 2021)] == 50 and cnt[("r", 2018)] == 50 and cnt[("r", 2025)] == 50
HTML = open(os.path.join(ROOT, "tools/paper2_pyq_bank_template.html"), encoding="utf-8").read()
open(os.path.join(ROOT, "ASO-Maths-PYQ-Bank.html"), "w", encoding="utf-8").write(
    HTML.replace("__DATA__", json.dumps(out, ensure_ascii=False)).replace("__TOPICS__", json.dumps(LABELS, ensure_ascii=False)))
print("wrote ASO-Maths-PYQ-Bank.html")
