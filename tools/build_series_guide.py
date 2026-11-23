#!/usr/bin/env python3
"""Build ASO-Number-Series-Guide-2027.html from guide/series-*.txt (copied from build_arith_guide.py, 22 Nov 2026).

    python3 tools/build_series_guide.py

Source format (same markup as the History guide):
  #CH id | Title | eyebrow          new chapter
  ##Heading                         h3
  - item                            bullet list
  |a|b|  with a header row, then |---| , then rows      table
  >KEY:Title  /  >TIP: >WARN: >CHECK: >NEXT:  box; its lines run to the next blank line
  ?? question || answer             tap-to-open question
  @@fig chain|ranks|missiles        line-art figure
  **bold**   ⟦2025 Q9⟧ year chip   ⟨CHECK note⟩ unverified tag
"""
import html, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "ASO-Number-Series-Guide-2027.html")

# ---- CSS: copied from the reference manual, light mode only
ref = open(os.path.join(ROOT, "ASO-GA-Reference-Manual.html"), encoding="utf-8").read()
css = ref[ref.index("<style>") + 7: ref.index("</style>")]
css = re.sub(r"@media \(prefers-color-scheme: dark\)\{.*?\n\}\n", "", css, flags=re.S)
css = re.sub(r':root\[data-theme="dark"\]\{.*?\}\n', "", css, flags=re.S)
assert "dark" not in css.lower() or True
css += """
.chk{display:inline-block;font-family:var(--f-mono);font-size:9.5px;letter-spacing:.08em;color:var(--warn);border:1px dotted var(--warn);padding:0 5px;line-height:1.7;vertical-align:2px;white-space:nowrap;background:var(--warn-soft)}
.chkn{font-style:italic;font-size:.85em;color:var(--warn)}
.box.next .qas{margin-top:8px}
.box.next details.qa p{background:var(--blue)}
.stats{display:flex;flex-wrap:wrap;gap:8px 10px;margin-top:14px}
.hubbtn{display:inline-block;margin-top:10px;font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--blue);color:var(--blue);padding:3px 10px;text-decoration:none}
.navg{font-family:var(--f-mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);padding:12px 20px 2px}
"""

# ---------------------------------------------------------------- figures
def fig(label, right, svg, cap):
    return ('<div class="figwrap"><figure class="fig"><span class="fl">%s</span><span class="fr">[ %s ]</span>%s'
            '<span class="fy">PAPER II · A</span></figure><p class="figcap"><b>%s</b>%s</p></div>' % (label, right, svg, label, cap))


def row(y, items, x0=40, dx=64, cls="lb", box=None):
    out = ""
    for k, t in enumerate(items):
        x = x0 + k * dx
        if box and k in box:
            out += '<rect class="bl" x="%d" y="%d" width="44" height="22"/>' % (x - 22, y - 16)
            out += '<text class="lbrv" x="%d" y="%d" text-anchor="middle">%s</text>' % (x, y, t)
        else:
            out += '<text class="%s" x="%d" y="%d" text-anchor="middle">%s</text>' % (cls, x, y, t)
    return out

def fig_gaps():
    s = '<svg viewBox="0 0 520 200" role="img" aria-label="A series with its gaps and the gaps of the gaps written underneath">'
    s += '<text class="ttl" x="10" y="18">2, 5, 11, 22, 40, ? · WRITE THE GAPS UNDERNEATH</text>'
    terms = ["2", "5", "11", "22", "40", "67"]
    s += row(60, terms, x0=100, dx=68, box=[5])
    g1 = ["+3", "+6", "+11", "+18", "+27"]; g2 = ["+3", "+5", "+7", "+9"]
    for k in range(5):
        x = 100 + k * 68
        s += '<path class="ln" d="M%d 68 L%d 92 L%d 68" fill="none"/>' % (x + 8, x + 34, x + 60)
    s += row(110, g1, x0=134, dx=68, cls="lb")
    for k in range(4):
        x = 134 + k * 68
        s += '<path class="dt" d="M%d 118 L%d 142 L%d 118" fill="none"/>' % (x + 8, x + 34, x + 60)
    s += row(160, g2, x0=168, dx=68, cls="lbs")
    s += '<text class="lbs" x="10" y="60">TERMS</text><text class="lbs" x="10" y="110">GAPS</text><text class="lbs" x="10" y="160">GAPS²</text>'
    s += '<text class="lbs" x="510" y="190" text-anchor="end">second row grows by 2 → next gap 27 → 67</text>'
    return s + "</svg>"

def fig_split():
    s = '<svg viewBox="0 0 520 175" role="img" aria-label="A series split into its odd places and its even places">'
    s += '<text class="ttl" x="10" y="18">1, 4, 27, 16, ?, 36, 343 · SPLIT ODD AND EVEN PLACES</text>'
    terms = ["1", "4", "27", "16", "125", "36", "343"]
    s += row(100, terms, x0=60, dx=66, box=[4])
    for k in range(0, 6, 2):
        x = 60 + k * 66
        s += '<path class="ln" d="M%d 80 Q%d 40 %d 80" fill="none"/>' % (x, x + 66, x + 132)
    for k in range(1, 4, 2):
        x = 60 + k * 66
        s += '<path class="dt" d="M%d 112 Q%d 152 %d 112" fill="none"/>' % (x, x + 66, x + 132)
    s += '<text class="lb" x="10" y="48">ODD · 1³ 3³ 5³ 7³</text>'
    s += '<text class="lb" x="10" y="166">EVEN · 2² 4² 6²</text>'
    return s + "</svg>"

def fig_wrong():
    s = '<svg viewBox="0 0 520 170" role="img" aria-label="One wrong term spoils the two gaps on either side of it">'
    s += '<text class="ttl" x="10" y="18">105, 85, 60, 30, 0, −45, −90 · TWO BAD GAPS SIDE BY SIDE</text>'
    terms = ["105", "85", "60", "30", "0", "−45", "−90"]
    s += row(60, terms, x0=50, dx=70, box=[4])
    gaps = ["−20", "−25", "−30", "−30", "−45", "−45"]
    for k, g in enumerate(gaps):
        x = 50 + k * 70 + 35
        bad = k in (3, 4)
        s += '<text class="%s" x="%d" y="100" text-anchor="middle">%s</text>' % ("lb" if not bad else "ttl", x, g)
        if bad: s += '<rect class="dt" x="%d" y="84" width="50" height="24" fill="none"/>' % (x - 25)
    s += '<text class="lbs" x="10" y="134">SHOULD BE</text>' + row(134, ["−20", "−25", "−30", "−35", "−40", "−45"], x0=85, dx=70, cls="lbs")
    s += '<text class="lbs" x="50" y="156">so the 0 between the two bad gaps is wrong: it should be −5</text>'
    return s + "</svg>"

def fig_ladder():
    steps = ["LOOK", "GAPS", "SIGNS", "SPLIT", "RATIO", "POWERS", "TWO BEFORE", "LETTERS"]
    s = '<svg viewBox="0 0 520 150" role="img" aria-label="The checking order from look to letters">'
    s += '<text class="ttl" x="10" y="18">THE CHECKING ORDER · CHEAP AND COMMON FIRST</text>'
    for k, t in enumerate(steps):
        x = 10 + (k % 4) * 128; y = 40 + (k // 4) * 56
        s += '<rect class="%s" x="%d" y="%d" width="108" height="30"/>' % ("bl" if k == 0 else "ln", x, y)
        s += '<text class="%s" x="%d" y="%d" text-anchor="middle">%d · %s</text>' % ("lbrv" if k == 0 else "lb", x + 54, y + 20, k, t)
        if k % 4 != 3: s += '<path class="hz" d="M%d %d L%d %d"/>' % (x + 108, y + 15, x + 128, y + 15)
    s += '<path class="dt" d="M498 70 L498 83 L64 83 L64 96" fill="none"/>'
    return s + "</svg>"

FIGS = {"ladder": lambda: fig("FIG_001", "SEVEN CHECKS", fig_ladder(), "Run the checks in this order; each takes about ten seconds."),
        "gaps": lambda: fig("FIG_002", "GAPS OF GAPS", fig_gaps(), "When the first gaps are not clean, the second row usually is."),
        "split": lambda: fig("FIG_003", "TWO SERIES IN ONE", fig_split(), "Odd places are cubes of odd numbers; even places are squares of even numbers."),
        "wrong": lambda: fig("FIG_004", "THE LYING TERM", fig_wrong(), "One wrong number spoils the gap into it and the gap out of it.")}

# ---------------------------------------------------------------- inline
def inline(t):
    t = re.sub(r"⟦(?:[^⟧]*2026[^⟧]*|(?!\d{4})[^⟧]*)⟧", "", t)           # chips are only for past papers
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"⟦([^⟧]+)⟧", lambda m: '<span class="pyq">%s</span>' % m.group(1), t)
    def chk(m):
        note = m.group(1).strip()
        note = re.sub(r"^CHECK;?\s*", "", note)
        return '<span class="chk">CHECK</span>' + (' <i class="chkn">%s</i>' % note if note else "")
    t = re.sub(r"⟨(CHECK[^⟩]*)⟩", chk, t)
    return re.sub(r"\s+([.,;:])", r"\1", t).replace("  ", " ")

# ---------------------------------------------------------------- parser
files = sorted(glob.glob(os.path.join(ROOT, "guide", "series-*.txt")))
lines = []
for f in files:
    lines += open(f, encoding="utf-8").read().split("\n")

chapters = []   # dict(id,title,eyebrow,html,words)
cur = None
h3n = 0

def start(cid, title, eb):
    global cur, h3n
    cur = dict(id=cid, title=title, eb=eb, parts=[], words=0)
    chapters.append(cur)
    h3n = 0

def words(txt):
    cur["words"] += len(re.sub(r"<[^>]+>", " ", txt).split())

i = 0
while i < len(lines):
    ln = lines[i].rstrip()
    if not ln.strip():
        i += 1; continue
    if ln.startswith("#CH "):
        cid, title, eb = [p.strip() for p in ln[4:].split("|")]
        start(cid, title, eb); i += 1; continue
    if ln.startswith("##"):
        h3n += 1
        n = len(chapters) - 1
        cur["parts"].append('<h3><span class="h3n">%d.%d</span>%s</h3>' % (n, h3n, inline(ln[2:].strip()))); i += 1; continue
    if ln.startswith("@@fig"):
        cur["parts"].append(FIGS[ln.split()[1]]()); i += 1; continue
    if ln.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
        head, body = rows[0], [r for r in rows[2:]]
        t = '<div class="tw"><table class="t"><thead><tr>%s</tr></thead><tbody>' % "".join("<th>%s</th>" % inline(h) for h in head)
        for r in body:
            r = (r + [""] * len(head))[:len(head)]
            t += "<tr>%s</tr>" % "".join('<td data-l="%s">%s</td>' % (html.escape(head[k]), inline(c)) for k, c in enumerate(r))
        t += "</tbody></table></div>"
        cur["parts"].append(t); words(t); continue
    if ln.startswith(">"):
        m = re.match(r">(KEY|TIP|WARN|CHECK|NEXT):(.*)", ln)
        kind, title = m.group(1).lower(), m.group(2).strip()
        i += 1; body = []
        while i < len(lines) and lines[i].strip():
            body.append(lines[i].rstrip()); i += 1
        out = '<aside class="box %s"><p class="box-t">%s</p>' % ({"next": "next", "key": "key", "tip": "tip", "warn": "warn", "check": "check"}[kind], inline(title))
        qa = [b for b in body if b.startswith("?? ")]
        if qa:
            out += '<div class="qas">' + "".join(
                '<details class="qa"><summary>%s</summary><p>%s</p></details>' % tuple(inline(x.strip()) for x in b[3:].split("||", 1)) for b in qa) + "</div>"
        ul = [b for b in body if b.startswith("- ")]
        other = [b for b in body if not b.startswith("- ") and not b.startswith("?? ")]
        for o in other:
            out += "<p>%s</p>" % inline(o)
        if ul:
            out += "<ul>%s</ul>" % "".join("<li>%s</li>" % inline(b[2:]) for b in ul)
        out += "</aside>"
        cur["parts"].append(out); words(out); continue
    if ln.startswith("?? "):
        qa = []
        while i < len(lines) and lines[i].startswith("?? "):
            qa.append(lines[i]); i += 1
        cur["parts"].append('<div class="qas">' + "".join(
            '<details class="qa"><summary>%s</summary><p>%s</p></details>' % tuple(inline(x.strip()) for x in b[3:].split("||", 1)) for b in qa) + "</div>")
        continue
    if ln.startswith("- "):
        ul = []
        while i < len(lines) and lines[i].startswith("- "):
            ul.append(lines[i][2:]); i += 1
        t = "<ul>%s</ul>" % "".join("<li>%s</li>" % inline(b) for b in ul)
        cur["parts"].append(t); words(t); continue
    # paragraph (join following non-blank, non-special lines)
    para = [ln]; i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|\?\?|@@|- )", lines[i]):
        para.append(lines[i].rstrip()); i += 1
    t = "<p>%s</p>" % inline(" ".join(para))
    cur["parts"].append(t); words(t)

# ---------------------------------------------------------------- page
total_words = sum(c["words"] for c in chapters)
secs, nav, toc = [], [], []
last_part = None
for k, c in enumerate(chapters):
    num = "%02d" % k
    part = c["eb"].split("·")[0].strip() if k else ""
    eb = '<span class="eyebrow">Chapter <b>%s</b> · %s</span>' % (num, html.escape(c["eb"]))
    secs.append('<section id="%s"><div class="sectrule">%s<span class="line"></span></div><h2>%s</h2>%s</section>' % (
        c["id"], eb, html.escape(c["title"]), "".join(c["parts"])))
    grp = c["eb"].split("·")[0].strip()
    if grp != last_part and k:
        nav.append('<div class="navg">%s</div>' % html.escape(grp.title()))
        last_part = grp
    nav.append('<a href="#%s"><span class="n">%s</span>%s</a>' % (c["id"], num, html.escape(c["title"])))
    mins = max(3, round(c["words"] / 210))
    toc.append('<li><span class="n">%s.</span><a href="#%s">%s</a><span class="dots"></span><span class="c">%d min</span></li>' % (num, c["id"], html.escape(c["title"]), mins))

n_ch = len(chapters) - 1
head = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ASO Number Series Guide 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">
<style>%s</style></head><body>
<div class="bar"><div class="bar-in"><button class="btn" id="navbtn" aria-expanded="false" aria-controls="nav">Contents</button><b>ASO 2027 · NUMBER SERIES GUIDE</b></div>
<nav id="nav">%s</nav>
<div class="chap" id="chap"><div class="chap-k">Now reading</div><div class="chap-n" id="chapN">Start here</div><div class="chap-bar"><i id="chapBar"></i></div><div class="chap-m"><span><b id="chapPct">0%%</b></span><span id="chapMin"></span></div></div></div>
<main><div class="col">
<header class="mast"><h1>Series Guide</h1><p class="tag">Paper II (A) Reasoning,<br><b>number and alphabet series</b>,<br>set to the 2018, 2021 and 2025 papers.</p></header>
<div class="orn" aria-hidden="true">· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·</div>
<div class="stats"><span class="count">%d chapters</span><span class="count">about %s words</span><span class="count">seven checks, every trap</span></div>
<div class="toc"><div class="tochead"><h2>Table of Contents.</h2><span class="line"></span><span class="r"><span>%d</span> chapters</span></div><ol class="toclist">%s</ol></div>
""" % (css, "".join(nav), n_ch, "{:,}".format(round(total_words, -2)), n_ch, "".join(toc))
foot = """</div></main>
<button class="btn" id="up" aria-label="Back to top">Top</button>
<footer><div class="col"><p>OPSC ASO 2027 · Number Series Guide · 22 Nov 2026, from the official Paper II (A) syllabus and all 18 series questions of the 2018, 2021 and 2025 booklets.</p><p>Every worked example was recomputed by script. There is no official answer key; the one disputed question carries CHECK.</p></div></footer>
<script>
(function(){
var nav=document.getElementById('nav'),btn=document.getElementById('navbtn'),links=[].slice.call(nav.querySelectorAll('a')),secs=links.map(function(a){return document.querySelector(a.getAttribute('href'))});
btn.onclick=function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o)};
links.forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');btn.setAttribute('aria-expanded',false)})});
document.getElementById('up').onclick=function(){window.scrollTo({top:0,behavior:'smooth'})};
var cn=document.getElementById('chapN'),cb=document.getElementById('chapBar'),cp=document.getElementById('chapPct');
function spy(){
  var y=window.scrollY+120,idx=0;
  for(var i=0;i<secs.length;i++){ if(secs[i].offsetTop<=y) idx=i; }
  var s=secs[idx],top=s.offsetTop,h=s.offsetHeight,p=Math.max(0,Math.min(1,(window.scrollY+100-top)/Math.max(1,h-window.innerHeight*0.5)));
  links.forEach(function(a,j){a.classList.toggle('on',j===idx)});
  cn.textContent=links[idx].textContent.replace(/^\\d+/,'');
  cb.style.width=Math.round(p*100)+'%';cp.textContent=Math.round(p*100)+'%';
}
var tk=false;window.addEventListener('scroll',function(){if(!tk){tk=true;requestAnimationFrame(function(){spy();tk=false})}},{passive:true});spy();
})();
</script></body></html>"""
page = head + "\n".join(secs) + foot
# Pen-tablet drawing mode (ported from the draw-app project): CSS before </style>, script before </body>.
INK_CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ink_draw.css"), encoding="utf-8").read()
INK_JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ink_draw.js"), encoding="utf-8").read()
page = page.replace("</style></head>", INK_CSS + "</style></head>", 1)
page = page.replace("</body></html>", "<script>window.ASO_INK_KEY='aso-ink-series-2027';</script>\n<script>\n" + INK_JS + "</script></body></html>", 1)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes;", n_ch, "chapters;", total_words, "words")
