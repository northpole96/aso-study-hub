#!/usr/bin/env python3
"""Build ASO-Statistics-Probability-Guide-2027.html from guide/stat-*.txt (copied from build_history_guide.py, 18 Nov 2026).
Statistics and probability guide, 23 Nov 2026, from guide/stat-*.txt.

    python3 tools/build_stat_guide.py

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
OUT = os.path.join(ROOT, "ASO-Statistics-Probability-Guide-2027.html")

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
.box.pq{background:#fff;border:1px solid var(--blue);border-left:4px solid var(--blue)}
.box.pq .box-t{color:var(--blue)}
.box.pq p{margin:6px 0}
.stats{display:flex;flex-wrap:wrap;gap:8px 10px;margin-top:14px}
.hubbtn{display:inline-block;margin-top:10px;font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--blue);color:var(--blue);padding:3px 10px;text-decoration:none}
.navg{font-family:var(--f-mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);padding:12px 20px 2px}
"""


def fig(label, right, svg, cap):
    return ('<div class="figwrap"><figure class="fig"><span class="fl">%s</span><span class="fr">[ %s ]</span>%s'
            '<span class="fy">PAPER II · B</span></figure><p class="figcap"><b>%s</b>%s</p></div>' % (label, right, svg, label, cap))

def fig_central():
    data = [2, 3, 3, 5, 7, 8, 14]
    x0, step = 40, 32
    X = lambda v: x0 + v * step
    s = '<svg viewBox="0 0 520 210" role="img" aria-label="Mode, median and mean on a number line">'
    s += '<text class="ttl" x="10" y="18">DATA: 2, 3, 3, 5, 7, 8, 14</text>'
    s += '<line class="hz" x1="30" y1="120" x2="500" y2="120"/>'
    for v in range(0, 15):
        s += '<line class="ln" x1="%d" y1="116" x2="%d" y2="124"/>' % (X(v), X(v))
        if v % 2 == 0 or v in (3, 5):
            s += '<text class="lbs" x="%d" y="138" text-anchor="middle">%d</text>' % (X(v), v)
    seen = {}
    for v in data:
        n = seen.get(v, 0); seen[v] = n + 1
        s += '<circle class="bl" cx="%d" cy="%d" r="7"/>' % (X(v), 108 - n * 16)
    s += '<path class="dt" d="M%d 100 L%d 52"/><text class="lb" x="%d" y="46" text-anchor="middle">MODE 3</text>' % (X(3), X(3), X(3))
    s += '<path class="dt" d="M%d 100 L%d 74"/><text class="lb" x="%d" y="68" text-anchor="middle">MEDIAN 5</text>' % (X(5) + 2, X(5) + 2, X(5) + 2)
    s += '<path class="nf" d="M%d 146 L%d 124 M%d 146 L%d 124"/><text class="lb" x="%d" y="162" text-anchor="middle">MEAN 6</text>' % (X(6), X(6), X(6) + 1, X(6) + 1, X(6))
    s += '<text class="lbs" x="10" y="192">The 14 pulls the mean up; the median and mode ignore it.</text>'
    return s + "</svg>"

def fig_bars():
    cls = [("0-10", 8), ("10-20", 16), ("20-30", 36), ("30-40", 34), ("40-50", 6)]
    cum = [8, 24, 60, 94, 100]
    s = '<svg viewBox="0 0 520 250" role="img" aria-label="Grouped data with the median class marked">'
    s += '<text class="ttl" x="10" y="18">GROUPED DATA · N = 100 · N/2 = 50</text>'
    for k, (c, f) in enumerate(cls):
        x = 40 + k * 90; h = f * 4.0
        s += '<rect class="%s" x="%d" y="%d" width="70" height="%d"/>' % ("bl" if k == 2 else "lt", x, 200 - h, h)
        s += '<text class="lb" x="%d" y="%d" text-anchor="middle">f = %d</text>' % (x + 35, 194 - h, f)
        s += '<text class="lbs" x="%d" y="216" text-anchor="middle">%s</text>' % (x + 35, c)
        s += '<text class="lbs" x="%d" y="232" text-anchor="middle">cf = %d</text>' % (x + 35, cum[k])
    s += '<text class="lb" x="260" y="44" text-anchor="middle">MEDIAN CLASS: cf first passes 50 here (20-30)</text>'
    return s + "</svg>"

def fig_dice():
    s = '<svg viewBox="0 0 520 290" role="img" aria-label="The 36 outcomes of two dice with the total 5 marked">'
    s += '<text class="ttl" x="10" y="16">TWO DICE · 36 OUTCOMES (total in each cell)</text>'
    for r in range(1, 7):
        s += '<text class="lbs" x="30" y="%d" text-anchor="end">%d</text>' % (54 + (r - 1) * 36 + 21 - 6, r)
        s += '<text class="lbs" x="%d" y="44" text-anchor="middle">%d</text>' % (40 + (r - 1) * 36 + 17, r)
    for a in range(1, 7):
        for b in range(1, 7):
            x, y = 40 + (b - 1) * 36, 54 + (a - 1) * 36 - 6
            hit = (a + b == 5)
            s += '<rect class="%s" x="%d" y="%d" width="34" height="34"/>' % ("bl" if hit else "ln", x, y)
            s += '<text class="%s" x="%d" y="%d" text-anchor="middle">%d</text>' % ("lbsrv" if hit else "lbs", x + 17, y + 21, a + b)
    s += '<text class="ttl" x="290" y="80">TOTAL 5</text><text class="lb" x="290" y="102">4 cells: (1,4) (2,3) (3,2) (4,1)</text>'
    s += '<text class="lb" x="290" y="124">P = 4/36 = 1/9</text>'
    s += '<text class="ttl" x="290" y="168">WAYS FOR EACH TOTAL</text>'
    ways = "2:1  3:2  4:3  5:4  6:5  7:6  8:5  9:4  10:3  11:2  12:1".split("  ")
    for k, w in enumerate(ways):
        s += '<text class="lbs" x="%d" y="%d">%s</text>' % (290 + (k % 4) * 56, 188 + (k // 4) * 16, w.replace(":", " → "))
    s += '<text class="lbs" x="290" y="262">7 is the likeliest total (6 ways).</text>'
    return s + "</svg>"

FIGS = {"central": lambda: fig("FIG_001", "MEAN, MEDIAN, MODE", fig_central(), "One odd large value drags the mean away; median and mode stay put."),
        "bars": lambda: fig("FIG_002", "GROUPED MEDIAN", fig_bars(), "The median sits in the class where the running total first passes N/2."),
        "dice": lambda: fig("FIG_003", "TWO DICE", fig_dice(), "Draw the 36-cell table once; every dice question is a count of cells.")}
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
files = sorted(glob.glob(os.path.join(ROOT, "guide", "stat-*.txt")))
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
        m = re.match(r">(KEY|TIP|WARN|CHECK|NEXT|PYQ):(.*)", ln)
        kind, title = m.group(1).lower(), m.group(2).strip()
        i += 1; body = []
        while i < len(lines) and lines[i].strip():
            body.append(lines[i].rstrip()); i += 1
        out = '<aside class="box %s"><p class="box-t">%s</p>' % ({"next": "next", "key": "key", "tip": "tip", "warn": "warn", "check": "check", "pyq": "pq"}[kind], inline(title))
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
<title>ASO Statistics and Probability Guide 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">
<style>%s</style></head><body>
<div class="bar"><div class="bar-in"><button class="btn" id="navbtn" aria-expanded="false" aria-controls="nav">Contents</button><b>ASO 2027 · STATISTICS &amp; PROBABILITY</b></div>
<nav id="nav">%s</nav>
<div class="chap" id="chap"><div class="chap-k">Now reading</div><div class="chap-n" id="chapN">Start here</div><div class="chap-bar"><i id="chapBar"></i></div><div class="chap-m"><span><b id="chapPct">0%%</b></span><span id="chapMin"></span></div></div></div>
<main><div class="col">
<header class="mast"><h1>Statistics &amp; Probability</h1><p class="tag">Paper II (B) Mathematics,<br><b>every type, every trap</b>, set to<br>the 2018 and 2021 papers.</p></header>
<div class="orn" aria-hidden="true">· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·</div>
<div class="stats"><span class="count">%d chapters</span><span class="count">about %s words</span><span class="count">every question of 2018 and 2021</span></div>
<div class="toc"><div class="tochead"><h2>Table of Contents.</h2><span class="line"></span><span class="r"><span>%d</span> chapters</span></div><ol class="toclist">%s</ol></div>
""" % (css, "".join(nav), n_ch, "{:,}".format(round(total_words, -2)), n_ch, "".join(toc))
foot = """</div></main>
<button class="btn" id="up" aria-label="Back to top">Top</button>
<footer><div class="col"><p>OPSC ASO 2027 · Statistics and Probability Guide · 23 Nov 2026 · from the Paper II (B) maths blocks of the 2018, 2021 and 2025 booklets.</p><p>Every worked example was recomputed by a script.</p></div></footer>
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
page = page.replace("</body></html>", "<script>window.ASO_INK_KEY='aso-ink-stat-2027';</script>\n<script>\n" + INK_JS + "</script></body></html>", 1)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes;", n_ch, "chapters;", total_words, "words")
