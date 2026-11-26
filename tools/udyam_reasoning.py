"""Reasoning questions (and Maths for checking) of 2015, 2018, 2021 and 2025 from the Udyam IAS book
`udyam pyq/ASO_Reasoning_Mathematics_2015-2025.pdf` (text layer read with pypdf).
Keys and explanations are the publisher's, not OPSC's.

    from udyam_reasoning import load
    rows = load("Reasoning")   # {(year, n): dict(s, o, a, w, fig)} ; n = 1..50 inside each section
"""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "udyam pyq", "ASO_Reasoning_Mathematics_2015-2025.pdf")


def pages_text():
    import pypdf
    r = pypdf.PdfReader(PDF)
    return [(p.extract_text() or "") for p in r.pages]


def clean(pages):
    """One list of lines per document; page footers (number + t.me line) removed."""
    lines = []
    for pi, t in enumerate(pages):
        ls = t.split("\n")
        # drop the footer: "<page number>" line right before https://t.me/UDYAMIAS, and the link itself
        out = []
        for i, l in enumerate(ls):
            if l.strip().startswith("https://t.me/UDYAMIAS"):
                if out and re.fullmatch(r"\d+\s*", out[-1]): out.pop()
                continue
            out.append(l)
        lines.append(("@@PAGE %d" % (pi + 1)))
        lines.extend(out)
    return lines


def sections(lines):
    """{(year, 'Reasoning'|'Mathematics'): [lines]}"""
    res, year, sec, buf, last = {}, None, None, [], "@@PAGE 0"
    for l in lines:
        if l.startswith("@@PAGE"): last = l
        m = re.match(r"(\d{4}) ASO Reasoning and Mathematics", l)
        if m:
            year, sec = int(m.group(1)), None; continue
        m = re.match(r"[12]\. (Reasoning|Mathematics)\s*$", l)
        if m and year:
            sec = m.group(1); res[(year, sec)] = buf = [last]; continue
        if year and sec: buf.append(l)
    return res


def parse_section(ls):
    """Questions 1..50 in order. Returns {n: dict}."""
    qs, cur, n = {}, None, 0
    for l in ls:
        if l.startswith("@@PAGE"):
            if cur is not None: cur["lines"].append(l)
            continue
        m = re.match(r"%d\.(?:\s+(.*)|\s*)$" % (n + 1), l)
        if m and (cur is None or any(x.startswith("Answer") for x in cur["lines"])):
            n += 1; cur = {"n": n, "lines": []}; qs[n] = cur
            if m.group(1): cur["lines"].append(m.group(1))
            continue
        if cur is not None: cur["lines"].append(l)
    return qs


def build(q):
    pages = [l for l in q["lines"] if l.startswith("@@PAGE")]
    ls = [l for l in q["lines"] if not l.startswith("@@PAGE")]
    ai = next(i for i, l in enumerate(ls) if re.match(r"Answer\s*:", l))
    pre, post = ls[:ai], ls[ai:]
    m = re.match(r"Answer\s*:\s*([A-E])\s*-?\s*(.*)", post[0])
    ans, atext = m.group(1), m.group(2)
    # options: lines starting 'A. ' .. 'D. ' (E for figure questions)
    oi = next((i for i, l in enumerate(pre) if re.match(r"A\.\s", l) or l.strip() == "A."), None)
    stem_lines, opts = (pre, []) if oi is None else (pre[:oi], [])
    if oi is not None:
        cur = None
        for l in pre[oi:]:
            mm = re.match(r"([A-E])\.\s*(.*)", l)
            if mm and (len(opts) == ord(mm.group(1)) - 65):
                opts.append(mm.group(2)); cur = len(opts) - 1
            elif cur is not None: opts[cur] += " " + l.strip()
    stem = ""
    for l in stem_lines:
        s = l.strip()
        if not s: continue
        brk = bool(stem) and (s.startswith("(") or re.fullmatch(r"[\d ,]{8,}", s) or re.match(r"(Statements?|Conclusions?|Assertion|Reason|Directions?)\b", s))
        stem += ("\n" if brk else " " if stem else "") + s
    why = " ".join(l.strip() for l in post[1:] if l.strip())
    why = (atext + ". " + why).strip() if atext and atext.lower() not in why.lower()[:len(atext) + 2] else (why or atext)
    fig = bool(re.search(r"[Ff]igure|diagram|pattern|image", stem + " ".join(opts))) and len(opts) < 4 or any(re.fullmatch(r"Figure \d", o.strip()) for o in opts)
    return dict(s=re.sub(r"[ \t]+", " ", stem), o=[re.sub(r"\s+", " ", o).strip() for o in opts], a=ans, w=re.sub(r"\s+", " ", why), pages=[p for p in pages])


def load(section):
    lines = clean(pages_text())
    secs = sections(lines)
    out = {}
    for (y, s), ls in secs.items():
        if s != section: continue
        qs = parse_section(ls)
        for n, q in qs.items():
            out[(y, n)] = build(q)
    return out


if __name__ == "__main__":
    import sys, collections
    for sec in ("Reasoning", "Mathematics"):
        d = load(sec)
        print(sec, collections.Counter(y for y, n in d))
        bad = [(k, len(v["o"])) for k, v in d.items() if len(v["o"]) != 4]
        print("  not 4 options:", bad)
