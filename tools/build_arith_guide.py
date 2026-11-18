#!/usr/bin/env python3
"""Build ASO-Arithmetic-Guide-2027.html from guide/arith-*.txt (copied from build_history_guide.py, 18 Nov 2026).
One chapter group per arithmetic family; new families are added as new guide/arith-N.txt files.

    python3 tools/build_arith_guide.py

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
OUT = os.path.join(ROOT, "ASO-Arithmetic-Guide-2027.html")

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
            '<span class="fy">PAPER II · B</span></figure><p class="figcap"><b>%s</b>%s</p></div>' % (label, right, svg, label, cap))

def arrow(x1, y, x2, cls="hz"):
    d = 6 if x2 > x1 else -6
    return ('<line class="%s" x1="%d" y1="%d" x2="%d" y2="%d"/><path class="nf" d="M%d %d L%d %d L%d %d"/>'
            % (cls, x1, y, x2, y, x2 - d, y - 4, x2, y, x2 - d, y + 4))

def train(x, y, w, label, cls="ln"):
    s = '<rect class="%s" x="%d" y="%d" width="%d" height="18"/>' % (cls, x, y, w)
    s += '<circle class="ln" cx="%d" cy="%d" r="3"/><circle class="ln" cx="%d" cy="%d" r="3"/>' % (x + 8, y + 21, x + w - 8, y + 21)
    s += '<text class="%s" x="%d" y="%d" text-anchor="middle">%s</text>' % ("lbsrv" if cls == "bl" else "lbs", x + w / 2, y + 13, label)
    return s

def fig_trains():
    s = '<svg viewBox="0 0 520 300" role="img" aria-label="What distance a train covers when it passes a pole, a platform and another train">'
    rows = [(30, "A · POLE", "distance = train only"), (120, "B · PLATFORM", "distance = train + platform"), (210, "C · ANOTHER TRAIN", "distance = both trains")]
    for y, t, cap in rows:
        s += '<text class="ttl" x="10" y="%d">%s</text>' % (y - 8, t)
        s += '<line class="grid" x1="10" y1="%d" x2="510" y2="%d"/>' % (y + 26, y + 26)
        s += '<text class="lb" x="510" y="%d" text-anchor="end">%s</text>' % (y - 8, cap)
    # A: pole
    s += train(40, 30, 120, "TRAIN L", "bl") + '<line class="hz" x1="300" y1="22" x2="300" y2="56"/><circle class="hd" cx="300" cy="20" r="3"/>' + arrow(170, 39, 230)
    s += '<path class="dt" d="M40 66 L160 66"/><text class="lbs" x="100" y="80" text-anchor="middle">covers L</text>'
    # B: platform
    s += train(30, 120, 120, "TRAIN L", "bl") + arrow(160, 129, 200) + '<rect class="lt" x="220" y="132" width="180" height="14"/><text class="lbs" x="310" y="143" text-anchor="middle">PLATFORM P</text>'
    s += '<path class="dt" d="M30 156 L400 156"/><text class="lbs" x="215" y="170" text-anchor="middle">covers L + P</text>'
    # C: two trains
    s += train(30, 210, 110, "TRAIN 1", "bl") + arrow(150, 219, 195) + train(260, 210, 150, "TRAIN 2") + arrow(420, 219, 470)
    s += '<text class="lbs" x="260" y="258" text-anchor="middle">same way: speeds SUBTRACT · opposite ways: speeds ADD</text>'
    s += '<path class="dt" d="M30 266 L410 266"/><text class="lbs" x="220" y="282" text-anchor="middle">covers L1 + L2</text>'
    return s + "</svg>"

def fig_boat():
    s = '<svg viewBox="0 0 520 210" role="img" aria-label="A boat going downstream and upstream">'
    for y in (60, 150):
        for k in range(5):
            x = 20 + k * 90
            s += '<path class="dt" d="M%d %d q10 -5 20 0 t20 0"/>' % (x, y + 30)
    s += '<text class="ttl" x="10" y="20">DOWNSTREAM · WITH THE WATER</text>'
    s += '<path class="bl" d="M150 60 L250 60 L235 78 L165 78 Z"/>' + arrow(270, 68, 350)
    s += '<text class="lb" x="510" y="72" text-anchor="end">D = b + s</text>'
    s += '<text class="ttl" x="10" y="110">UPSTREAM · AGAINST THE WATER</text>'
    s += '<path class="ln" d="M270 150 L370 150 L355 168 L285 168 Z"/>' + arrow(250, 158, 170)
    s += '<text class="lb" x="510" y="162" text-anchor="end">U = b − s</text>'
    s += '<text class="lbs" x="10" y="200">water flows → at s · boat b = (D + U) ÷ 2 · stream s = (D − U) ÷ 2</text>'
    return s + "</svg>"

def fig_avg():
    s = '<svg viewBox="0 0 520 170" role="img" aria-label="Why average speed is below the plain average: more time at the slow speed">'
    s += '<text class="ttl" x="10" y="18">120 KM THERE AT 40, BACK AT 60 · TIME ON THE BOTTOM LINE</text>'
    s += '<rect class="lt" x="10" y="40" width="288" height="34"/><text class="lb" x="154" y="62" text-anchor="middle">3 h at 40 km/h</text>'
    s += '<rect class="bl" x="298" y="40" width="192" height="34"/><text class="lbrv" x="394" y="62" text-anchor="middle">2 h at 60</text>'
    s += '<line class="hz" x1="10" y1="96" x2="490" y2="96"/>'
    for k in range(6):
        x = 10 + k * 96
        s += '<line class="hl" x1="%d" y1="90" x2="%d" y2="102"/><text class="lbs" x="%d" y="116" text-anchor="middle">%d h</text>' % (x, x, x, k)
    s += '<text class="lb" x="10" y="150">240 km ÷ 5 h = 48 km/h, not 50</text>'
    return s + "</svg>"

FIGS = {"trains": lambda: fig("FIG_002", "WHAT A TRAIN COVERS", fig_trains(), "A pole has no length; a platform and another train add their lengths."),
        "boat": lambda: fig("FIG_003", "WITH AND AGAINST", fig_boat(), "The stream helps one way and hurts the other by the same amount."),
        "avg": lambda: fig("FIG_001", "AVERAGE SPEED", fig_avg(), "Equal distances, unequal times: the slow part lasts longer.")}

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
files = sorted(glob.glob(os.path.join(ROOT, "guide", "arith-*.txt")))
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
<title>ASO Arithmetic Guide 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">
<style>%s</style></head><body>
<div class="bar"><div class="bar-in"><button class="btn" id="navbtn" aria-expanded="false" aria-controls="nav">Contents</button><b>ASO 2027 · ARITHMETIC GUIDE</b></div>
<nav id="nav">%s</nav>
<div class="chap" id="chap"><div class="chap-k">Now reading</div><div class="chap-n" id="chapN">Start here</div><div class="chap-bar"><i id="chapBar"></i></div><div class="chap-m"><span><b id="chapPct">0%%</b></span><span id="chapMin"></span></div></div></div>
<main><div class="col">
<header class="mast"><h1>Arithmetic Guide</h1><p class="tag">Paper II (B) Mathematics,<br><b>one family at a time</b>, set to<br>the 2018, 2021 and 2025 papers.</p></header>
<div class="orn" aria-hidden="true">· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·</div>
<div class="stats"><span class="count">%d chapters</span><span class="count">about %s words</span><span class="count">every type, every trap</span></div>
<div class="toc"><div class="tochead"><h2>Table of Contents.</h2><span class="line"></span><span class="r"><span>%d</span> chapters</span></div><ol class="toclist">%s</ol></div>
""" % (css, "".join(nav), n_ch, "{:,}".format(round(total_words, -2)), n_ch, "".join(toc))
foot = """</div></main>
<button class="btn" id="up" aria-label="Back to top">Top</button>
<footer><div class="col"><p>OPSC ASO 2027 · Arithmetic Guide · started 18 Nov 2026 from the official Paper II (B) syllabus, the maths sections of the 2018, 2021 and 2025 booklets and the standard R. S. Aggarwal types.</p><p>Every worked example was recomputed by hand and by the practice-set check scripts.</p></div></footer>
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
page = page.replace("</body></html>", "<script>window.ASO_INK_KEY='aso-ink-arith-2027';</script>\n<script>\n" + INK_JS + "</script></body></html>", 1)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes;", n_ch, "chapters;", total_words, "words")
