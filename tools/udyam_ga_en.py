"""GA and English questions of 2015, 2018, 2021, 2025 from the Udyam IAS books (text layer read with pypdf).
Keys are the publisher's, not OPSC's.   load("ga") / load("en") -> {(year, k): dict(s, o, a, w, bookno)}  (k = order in the book, NOT the paper number; match by text)   (a may be 'Unresolved')"""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = {"ga": "Udyam_ASO_All_400_Questions_and_Solutions.pdf", "en": "Udyam_ASO_English_PYQs_2015-2025.pdf"}
HEAD = {"ga": r"(\d{4}) ASO General Awareness", "en": r"(\d{4}) ASO English"}

def lines_of(kind):
    import pypdf
    r = pypdf.PdfReader(os.path.join(ROOT, "udyam pyq", PDF[kind])); out = []
    for t in (p.extract_text() or "" for p in r.pages):
        ls = t.split("\n"); keep = []
        for l in ls:
            if l.strip().startswith("https://t.me/UDYAMIAS"):
                if keep and re.fullmatch(r"\d+\s*", keep[-1]): keep.pop()
                continue
            keep.append(l)
        out.extend(keep)
    return out

def load(kind):
    ls, year, res, cur = lines_of(kind), None, {}, None
    seen = set(); sec = None
    for l in ls:
        m = re.match(HEAD[kind], l.strip())
        if m: year = int(m.group(1)); cur = None; continue
        if year is None: continue
        hm = re.match(r"(\d{1,2}\.\d{1,2})\s+[A-Z]", l.strip())
        if hm and (cur is None or cur['done']): sec = hm.group(1)
        m = re.match(r"(\d{1,3})\.\s+(\S.*)$", l) or re.match(r"(\d{1,3})\.\s*()$", l)
        if m and (cur is None or cur["done"]) and 1 <= int(m.group(1)) <= 100:
            n = int(m.group(1)); idx = sum(1 for k in res if k[0] == year) + 1
            cur = res[(year, idx)] = dict(lines=[m.group(2)] if m.group(2) else [], done=False, y=year, n=n, bookno=n, sec=sec); continue
        if cur is not None:
            cur["lines"].append(l)
            if re.match(r"Answer\s*:", l): cur["done"] = True; cur["ai"] = len(cur["lines"]) - 1
    for k, c in res.items():
        L = c["lines"]; ai = c.get("ai")
        if ai is None: c.update(a=None, s=" ".join(L), o=[], w=""); continue
        pre, post = L[:ai], L[ai:]
        oi = next((i for i, x in enumerate(pre) if re.match(r"A\.\s", x) or x.strip() == "A."), None)
        stem = " ".join(x.strip() for x in (pre if oi is None else pre[:oi]))
        opts = []
        if oi is not None:
            cu = None
            for x in pre[oi:]:
                mm = re.match(r"([A-E])\.\s*(.*)", x)
                if mm and len(opts) == ord(mm.group(1)) - 65: opts.append(mm.group(2)); cu = len(opts) - 1
                elif cu is not None: opts[cu] += " " + x.strip()
        m = re.match(r"Answer\s*:\s*([A-E])\b\s*-?\s*(.*)", post[0])
        a = m.group(1) if m else "Unresolved"
        c.update(a=a, s=re.sub(r"\s+", " ", stem), o=[re.sub(r"\s+", " ", o).strip() for o in opts], w=re.sub(r"\s+", " ", " ".join(x.strip() for x in post)))
    return res

if __name__ == "__main__":
    import collections
    for k in ("ga", "en"):
        d = load(k); print(k, sorted(collections.Counter(y for y, n in d).items()), "no answer:", [x for x, v in d.items() if v["a"] is None][:10],
              "unresolved:", [x for x, v in d.items() if v["a"] == "Unresolved"], "not4:", [x for x, v in d.items() if len(v["o"]) != 4][:12])
