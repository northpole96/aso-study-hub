#!/usr/bin/env python3
"""Turn the markdown / OCR sources in pyq/ into reading pages for the study hub.

Run from the ASO folder:   python3 tools/build_pages.py
It writes one .html next to each source file (pyq/NAME.md -> pyq/NAME.html).
The .md / .txt sources are never changed. Re-run after editing a source.
"""
import html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PYQ = ROOT / "pyq"

PAGES = [
    # source, short title (masthead), util line, tagline
    ("OPSC-ASO-2026-27-Official-Syllabus.md", "Official Syllabus", "Advt. No. 15 of 2026-27 · scheme and syllabus",
     "The <b>scheme and syllabus</b> of all four papers,<br>copied word for word from the official notice."),
    ("OPSC-ASO-2021-GA-Paper-I.md", "GA Paper I · 2021", "Previous year paper · General Awareness",
     "All <b>100 questions</b> of the 2021 General Awareness paper,<br>sorted by topic."),
    ("OPSC-ASO-2018-English-Paper-III.md", "English III · 2018", "Previous year paper · English",
     "The <b>English half</b> of the 2018 Paper III,<br>with worked answers and a topic map."),
    ("OPSC-ASO-2021-English-Paper-III.md", "English III · 2021", "Previous year paper · English",
     "The <b>English half</b> of the 2021 Paper III,<br>with worked answers and a topic map."),
    ("OPSC-ASO-2025-English-Paper-III.md", "English III · 2025", "Previous year paper · English",
     "The <b>English half</b> of the 2025 Paper III,<br>with worked answers and a topic map."),
    ("OPSC-ASO-2021-Reasoning-Maths-Paper-II.md", "Paper II · 2021", "Previous year paper · Reasoning and Maths",
     "All <b>100 questions</b> of the 2021 Paper II,<br>Reasoning then Maths, with worked answers."),
    ("OPSC-ASO-2018-Maths-Paper-II.md", "Maths II · 2018", "Previous year paper · Maths",
     "The <b>Maths half</b> (Q51–100) of the 2018 Paper II,<br>cleaned from OCR, CHECK tags where lost."),
    ("OPSC-ASO-2025-Maths-Paper-II.md", "Maths II · 2025", "Previous year paper · Maths",
     "The <b>Maths half</b> (Q51–100) of the 2025 Paper II,<br>cleaned from OCR, with worked answers."),
    ("English-PYQ-Breakdown-2018-2021-2025.md", "English Trend", "Three-year English breakdown",
     "How <b>2018, 2021 and 2025</b> English papers<br>map onto the official syllabus."),
    ("OPSC-ASO-2018-GA-Paper-I-OCR.txt", "GA Paper I · 2018", "Previous year paper · raw scan text",
     "The 2018 General Awareness paper as <b>raw scan text</b>.<br>Some option letters are garbled."),
    ("OPSC-ASO-2025-GA-Paper-I-OCR.txt", "GA Paper I · 2025", "Previous year paper · raw scan text",
     "The 2025 General Awareness paper as <b>raw scan text</b>.<br>Some option letters are garbled."),
]

CSS = r"""
:root{--bg:#fbfbfb;--paper:#ffffff;--fg:#111111;--muted:#6e6e73;--rule:#d7d7da;--grid:#eef0f6;--blue:#2b4cff;--blue-soft:#e0e6ff;--warn:#b4410b;
--f-serif:"EB Garamond","Iowan Old Style",Georgia,serif;--f-mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;--f-pixel:"Silkscreen","IBM Plex Mono",ui-monospace,monospace;color-scheme:light}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.75 var(--f-serif);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:var(--fg);text-decoration:underline dotted;text-decoration-color:var(--blue);text-underline-offset:3px}
a:hover{color:var(--blue)}
:focus-visible{outline:2px solid var(--blue);outline-offset:3px}
h1,h2,h3,h4{font-weight:400;margin:0;text-wrap:balance;line-height:1.25}
b,strong{font-weight:600}
code{font-family:var(--f-mono);font-size:.82em;background:var(--grid);padding:0 4px;overflow-wrap:anywhere}
.page{max-width:1100px;margin:0 auto;padding:32px max(16px,env(safe-area-inset-right,0px)) 96px max(16px,env(safe-area-inset-left,0px))}
.util{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.util a{color:var(--blue);text-decoration:none}
.mast{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,420px);gap:20px 48px;align-items:end;margin-top:28px}
.mast h1{font-family:var(--f-pixel);color:var(--blue);font-size:clamp(1.9rem,5.4vw,3.8rem);line-height:1.05;letter-spacing:.02em}
.mast .tag{text-align:right;font-size:1.02rem;line-height:1.6;margin:0}
@media (max-width:820px){.mast{grid-template-columns:1fr}.mast .tag{text-align:left}}
.orn{margin-block:22px 8px;color:var(--muted);overflow:hidden;white-space:nowrap;font-family:var(--f-mono);font-size:11px;letter-spacing:.3em;opacity:.7}
.doc{max-width:76ch}
.doc>p,.doc li{overflow-wrap:break-word}
.doc>p{margin:14px 0}
.doc>p.first::first-letter{float:left;font-size:3.8em;line-height:.82;padding:6px 8px 0 0}
.doc h2{font-size:clamp(1.5rem,3vw,2.1rem);margin:64px 0 14px;padding-top:14px;border-top:1px solid var(--fg);scroll-margin-top:60px}
.doc h3{font-family:var(--f-mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;margin:40px 0 10px;display:flex;align-items:center;gap:12px;scroll-margin-top:60px}
.doc h3::after{content:"";flex:1;border-bottom:1px dotted var(--muted)}
.doc h4{font-weight:600;margin:24px 0 6px}
.doc ul,.doc ol{padding-left:1.2em}
.doc li{margin:4px 0}
.doc blockquote{margin:18px 0;border:1px dashed var(--blue);background:var(--paper);padding:12px 16px}
.doc hr{border:0;border-top:1px dotted var(--muted);margin:32px 0}
.tbl{margin:16px 0;border-top:1px solid var(--fg)}
.tbl table{width:100%;border-collapse:collapse;font-size:.95rem;line-height:1.45;table-layout:auto}
.tbl th{font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:400;text-align:left;padding:8px 10px 8px 0;border-bottom:1px solid var(--rule)}
.tbl td{padding:8px 10px 8px 0;border-bottom:1px dotted var(--muted);vertical-align:top;overflow-wrap:anywhere}
@media (max-width:640px){
  .tbl thead{display:none}
  .tbl tr{display:block;padding:8px 0;border-bottom:1px dotted var(--muted)}
  .tbl td{display:grid;grid-template-columns:minmax(0,9em) minmax(0,1fr);gap:10px;border:0;padding:2px 0}
  .tbl td::before{content:attr(data-h);font-family:var(--f-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding-top:3px}
  .tbl td:empty{display:none}
}
.qq{scroll-margin-top:70px;margin:0;padding:14px 0;border-bottom:1px dotted var(--muted)}
.qq .qt{margin:0;font-size:1.04rem;line-height:1.55}
.qq .qn{font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;color:var(--blue);border:1px solid var(--blue);padding:0 6px;margin-right:8px;vertical-align:2px}
.qq .op{margin:6px 0 0;font-size:.98rem;line-height:1.55;color:#222}
.qq .op span{font-family:var(--f-mono);font-size:11px;color:var(--muted)}
.an{margin-top:8px;border-left:2px solid var(--blue);padding:2px 0 2px 12px;font-size:.97rem}
.an .ab{font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-right:6px}
body.hide .an{cursor:pointer;background:repeating-linear-gradient(45deg,var(--paper),var(--paper) 6px,var(--grid) 6px,var(--grid) 12px)}
body.hide .an .av{display:none}
body.hide .an::after{content:"Tap to show";font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue)}
body.hide .an.show{background:none}
body.hide .an.show .av{display:inline}
body.hide .an.show::after{content:none}
.chk{display:inline-block;font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--warn);border:1px dashed currentColor;padding:0 5px;margin:0 3px;vertical-align:2px;line-height:1.7}
.toc{padding-block:40px 8px}
.tochead{display:flex;align-items:center;gap:16px}
.tochead h2{font-size:1.25rem;white-space:nowrap}
.tochead .line{flex:1;height:1px;background:var(--fg);min-width:20px}
.tochead .r{font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}
.tochead .r span{color:var(--blue)}
.toclist{list-style:none;margin:24px 0 0;padding:0;columns:2 320px;column-gap:56px}
.toclist li{break-inside:avoid;display:flex;align-items:baseline;gap:8px;padding:4px 0;font-size:1rem;min-width:0}
.toclist .n{font-family:var(--f-mono);font-size:12px;color:var(--muted);min-width:2.2em}
.toclist a{text-decoration:none;min-width:0;overflow-wrap:anywhere}
.toclist .dots{flex:1;border-bottom:1px dotted var(--muted);transform:translateY(-4px);min-width:12px}
.toclist .c{font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;color:var(--muted);white-space:nowrap}
.bar{position:sticky;top:0;z-index:10;background:var(--bg);border-bottom:1px solid var(--rule);padding:10px 0;margin-top:20px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.btn{display:inline-block;border:1px solid var(--fg);background:var(--paper);padding:4px 12px;cursor:pointer;font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;border-radius:3px;text-decoration:none;color:var(--fg)}
.btn[aria-pressed="true"]{border-color:var(--blue);color:var(--blue);background:var(--blue-soft)}
.btn.pri{border-color:var(--blue);color:var(--blue)}
.scan{border:1px dashed var(--rule);background-color:var(--paper);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:10px 10px;padding:18px 18px;margin:12px 0 28px;position:relative}
.scan pre{margin:0;font-family:var(--f-mono);font-size:13px;line-height:1.6;white-space:pre-wrap;overflow-wrap:anywhere}
.scan .fl{position:absolute;right:6px;top:10px;writing-mode:vertical-rl;font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;color:var(--muted)}
footer{padding-top:48px;font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.totop{position:fixed;right:calc(16px + env(safe-area-inset-right,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:20;font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;color:var(--blue);background:var(--paper);border:1px solid var(--blue);padding:6px 10px;border-radius:3px}
"""

HEAD = """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="theme-color" content="#fbfbfb">
<link rel="icon" href="../icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">
<style>{css}</style>
<body>
<div class="page" id="top">
<div class="util"><a href="../index.html" target="_top">&larr; Study hub</a><span>OPSC ASO · {util}</span></div>
<header class="mast"><h1>{h1}</h1><p class="tag">{tag}</p></header>
<div class="orn" aria-hidden="true">{dots}</div>
"""

FOOT = """<footer>OPSC ASO study hub · built from <code>pyq/{src}</code> · <a href="../index.html" target="_top">back to the hub</a></footer>
</div>
<a class="totop" href="#top">Top &uarr;</a>
<script>
(function(){{var b=document.getElementById('hide');if(!b)return;
b.addEventListener('click',function(){{var on=document.body.classList.toggle('hide');b.setAttribute('aria-pressed',on);
document.querySelectorAll('.an.show').forEach(function(a){{a.classList.remove('show')}})}});
document.addEventListener('click',function(e){{var a=e.target.closest('.an');if(a&&document.body.classList.contains('hide'))a.classList.add('show')}});}})();
</script>
"""

def slug(s, seen):
    b = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", s).lower()).strip("-")[:48] or "s"
    k, i = b, 2
    while k in seen:
        k = f"{b}-{i}"; i += 1
    seen.add(k); return k

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", lambda m: "<code>" + m.group(1) + "</code>", t)
    t = re.sub(r"\*\*(Check|CHECK)\*\*", '<span class="chk">Check</span>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<i>\1</i>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    return t

def clean_src(text):
    # drop private local paths such as ~/Downloads/...
    text = re.sub(r"`~/[^`]*`", "the scanned PDF", text)
    text = re.sub(r"the user's file\s+the scanned PDF", "a scanned PDF", text)
    return text

OPT = re.compile(r"^\(A\)")
QSTART = re.compile(r"^\*\*(\d{1,3})\.\*\*\s*(.*)$")
ANS = re.compile(r"^\*\*Answer:?\s*(.*?)\*\*\s*(.*)$")

def md_to_html(text):
    lines = clean_src(text).split("\n")
    out, toc, seen = [], [], set()
    i, first_p, n_q = 0, True, 0
    cur_sec = None
    toc3, cur3 = [], None
    def opt_html(l):
        s = inline(l)
        return re.sub(r"\(([A-E])\)", r"<span>(\1)</span>", s)
    while i < len(lines):
        l = lines[i]
        s = l.strip()
        if not s:
            i += 1; continue
        if s.startswith("# ") and not out and not toc:
            i += 1; continue  # page title -> masthead
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1)); txt = inline(m.group(2))
            if lvl == 2:
                k = slug(m.group(2), seen); cur_sec = [k, txt, 0]; toc.append(cur_sec)
                out.append(f'<h2 id="{k}">{txt}</h2>')
            elif lvl == 3:
                k = slug(m.group(2), seen); out.append(f'<h3 id="{k}">{txt}</h3>')
                cur3 = [k, txt, 0]; toc3.append(cur3)
            else:
                out.append(f"<h4>{txt}</h4>")
            i += 1; continue
        if re.match(r"^-{3,}$", s):
            out.append("<hr>"); i += 1; continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip()); i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            head = cells[0]; body = [c for c in cells[1:] if not all(re.match(r"^:?-+:?$", x) for x in c if x)]
            h = '<div class="tbl"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            for r in body:
                h += "<tr>" + "".join(f'<td data-h="{html.escape(re.sub(r"[*`]", "", head[j] if j < len(head) else ""))}">{inline(c)}</td>' for j, c in enumerate(r)) + "</tr>"
            out.append(h + "</tbody></table></div>"); continue
        if s.startswith(">"):
            q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip()); i += 1
            out.append("<blockquote>" + "<br>".join(inline(x) for x in q) + "</blockquote>"); continue
        if re.match(r"^[-*] ", s):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*] ", lines[i]):
                items.append(inline(re.sub(r"^\s*[-*] ", "", lines[i]))); i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"); continue
        if re.match(r"^\d+\. ", s) and not QSTART.match(s):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                items.append(inline(re.sub(r"^\s*\d+\. ", "", lines[i]))); i += 1
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"); continue
        qm = QSTART.match(s)
        if qm:
            n_q += 1
            if cur_sec: cur_sec[2] += 1
            if cur3: cur3[2] += 1
            block = [s]; i += 1
            while i < len(lines) and lines[i].strip() and not QSTART.match(lines[i].strip()) and not lines[i].strip().startswith("#"):
                block.append(lines[i].strip()); i += 1
            qt = [qm.group(2)]; opts = []; ans = []
            for b in block[1:]:
                am = ANS.match(b)
                if am or ans:
                    if am:
                        rest = am.group(2).lstrip("—–- ").strip()
                        ans.append(f'<b class="av">{inline(am.group(1))}</b>' + (f" — {inline(rest)}" if rest else ""))
                    else:
                        ans.append(inline(b))
                elif OPT.match(b) or opts:
                    opts.append(opt_html(b))
                else:
                    qt.append(b)
            h = f'<article class="qq" id="q{qm.group(1)}"><p class="qt"><span class="qn">Q{qm.group(1)}</span>' + "<br>".join(inline(x) for x in qt if x) + "</p>"
            if opts: h += '<p class="op">' + "<br>".join(opts) + "</p>"
            if ans: h += '<div class="an"><span class="ab">Answer</span><span class="av">' + " ".join(ans) + "</span></div>"
            out.append(h + "</article>"); continue
        para = [s]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|[-*] |\d+\. |-{3,}$)", lines[i].strip()) and not QSTART.match(lines[i].strip()):
            para.append(lines[i].strip()); i += 1
        cls = ' class="first"' if first_p and not toc else ""
        if cls: first_p = False
        out.append(f"<p{cls}>" + "<br>".join(inline(x) for x in para) + "</p>")
    if len(toc) < 3 and len(toc3) >= 3:
        toc = toc3
    if len(toc) < 3 and n_q >= 20:
        nums = [int(x) for x in re.findall(r'<article class="qq" id="q(\d+)"', "\n".join(out))]
        toc = [[f"q{a}", f"Questions {a}–{min(a + 9, max(nums))}", sum(1 for x in nums if a <= x <= a + 9)] for a in range(1, max(nums) + 1, 10) if f'id="q{a}"' in "\n".join(out)]
    return "\n".join(out), toc, n_q

def ocr_to_html(text):
    pages = re.split(r"^=== PAGE (\d+)\s*$", text, flags=re.M)
    intro = pages[0].strip()
    out = [f'<p class="first">{inline(intro)} Use the clean topic-wise pages on the hub (for example Geography PYQs) where you can; this page is for checking the original wording.</p>']
    toc = []
    for k in range(1, len(pages), 2):
        n, body = pages[k], pages[k + 1].strip("\n")
        toc.append([f"p{n}", f"Page {n}", None])
        out.append(f'<h3 id="p{n}">Page {n}</h3><div class="scan"><span class="fl">SCAN_P{int(n):02d}</span><pre>{html.escape(body)}</pre></div>')
    return "\n".join(out), toc, 0

def toc_html(toc, total_label):
    if len(toc) < 2: return ""
    li = []
    for j, (k, t, c) in enumerate(toc, 1):
        cnt = f'<span class="c">{c} Q</span>' if c else ""
        li.append(f'<li><span class="n">{j:02d}</span><a href="#{k}">{t}</a><span class="dots"></span>{cnt}</li>')
    return f'<nav class="toc" aria-label="Contents"><div class="tochead"><h2>Table of Contents.</h2><span class="line"></span><span class="r">{total_label}</span></div><ol class="toclist">{"".join(li)}</ol></nav>'

def build():
    for src, h1, util, tag in PAGES:
        p = PYQ / src
        text = p.read_text(encoding="utf-8")
        if src.endswith(".txt"):
            body, toc, nq = ocr_to_html(text); label = f"<span>{len(toc)}</span> pages"
        else:
            body, toc, nq = md_to_html(text); label = f"<span>{nq}</span> questions" if nq else f"<span>{len(toc)}</span> parts"
        has_ans = 'class="an"' in body
        bar = '<div class="bar"><button class="btn" id="hide" aria-pressed="false">Hide answers</button><a class="btn" href="#top">Contents</a></div>' if has_ans else ""
        page = HEAD.format(title=f"ASO {h1}".replace(" · ", " "), css=CSS, util=util, h1=h1, tag=tag, dots="· " * 80)
        page += toc_html(toc, label) + bar + f'<main class="doc">{body}</main>' + FOOT.format(src=html.escape(src))
        dst = p.with_suffix(".html")
        dst.write_text(page, encoding="utf-8")
        print(f"{dst.relative_to(ROOT)}  {nq} q  {len(toc)} parts  answers={has_ans}")

if __name__ == "__main__":
    build()
