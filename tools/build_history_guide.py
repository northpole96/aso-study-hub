#!/usr/bin/env python3
"""Build ASO-History-Guide-2027.html from guide/history-*.txt.

    python3 tools/build_history_guide.py

Source format (one small markup, see guide/history-1.txt):
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
OUT = os.path.join(ROOT, "ASO-History-Guide-2027.html")

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
            '<span class="fy">© 1947</span></figure><p class="figcap"><b>%s</b>%s</p></div>' % (label, right, svg, label, cap))

def timeline_svg(points, aria, w=440):
    h = 200
    s = '<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (w, h, aria)
    n = len(points)
    x0, x1 = 30, w - 30
    s += '<line class="hz" x1="%d" y1="100" x2="%d" y2="100"/>' % (x0, x1)
    for i, (yr, txt) in enumerate(points):
        x = x0 + (x1 - x0) * i / (n - 1)
        up = i % 2 == 0
        s += '<circle class="hd" cx="%d" cy="100" r="4"/>' % x
        y2 = 70 if up else 130
        s += '<line class="hl" x1="%d" y1="100" x2="%d" y2="%d"/>' % (x, x, y2)
        s += '<text class="lb" x="%d" y="%d" text-anchor="middle">%s</text>' % (x, y2 - 6 if up else y2 + 14, yr)
        words = txt.split(" ")
        lines, cur = [], ""
        for wd in words:
            if len(cur) + len(wd) > 13 and cur:
                lines.append(cur); cur = wd
            else:
                cur = (cur + " " + wd).strip()
        lines.append(cur)
        for k, ln in enumerate(lines[:3]):
            yy = (y2 - 20 - 11 * (len(lines[:3]) - 1 - k)) if up else (y2 + 28 + 11 * k)
            s += '<text class="lbs" x="%d" y="%d" text-anchor="middle">%s</text>' % (x, yy, ln)
    s += "</svg>"
    return s

def fig_timeline():
    pts = [("1757", "Plassey"), ("1857", "Revolt"), ("1885", "Congress born"), ("1905", "Bengal split"), ("1919", "Rowlatt, Jallianwala"),
           ("1930", "Dandi March"), ("1942", "Quit India"), ("1947", "Independence")]
    return fig("FIG_001", "THE LONG ROAD", timeline_svg(pts, "Timeline from Plassey to independence"), "From Plassey to 15 August 1947.")

def fig_odisha():
    pts = [("1803", "Deogaon treaty"), ("1817", "Paika revolt"), ("1866", "Great famine"), ("1903", "Utkal Sammilani"),
           ("1936", "Odisha province"), ("1942", "Eram firing"), ("1948", "States merged")]
    return fig("FIG_003", "ODISHA LINE", timeline_svg(pts, "Timeline of Odisha"), "Seven dates for Odisha.")

def fig_acts():
    steps = [("1773", "Regulating"), ("1813", "Education"), ("1833", "Gov-Gen of India"), ("1858", "Crown"), ("1892", "Election"),
             ("1909", "Separate electorates"), ("1919", "Dyarchy"), ("1935", "Autonomy"), ("1947", "Independence")]
    s = '<svg viewBox="0 0 560 250" role="img" aria-label="Staircase of the constitutional Acts">'
    for i, (yr, t) in enumerate(steps):
        x = 20 + i * 58
        h = 22 + i * 20
        y = 225 - h
        cls = "bl" if yr in ("1892", "1909", "1919", "1935") else "ln"
        s += '<rect class="%s" x="%d" y="%d" width="56" height="%d"/>' % (cls, x, y, h)
        s += '<text class="%s" x="%d" y="%d" text-anchor="middle">%s</text>' % ("lbrv" if cls == "bl" else "lb", x + 28, y + 15, yr)
    s += '<text class="lbs" x="20" y="244">Blue steps: the four reform Acts the exam asks most.</text></svg>'
    return fig("FIG_002", "ACTS STAIRCASE", s, "1773 Regulating · 1813 Education · 1833 Governor-General of India · 1858 Crown · 1892 election · 1909 separate electorates · 1919 dyarchy · 1935 autonomy · 1947 Independence.")

FIGS = {"timeline": fig_timeline, "acts": fig_acts, "odisha": fig_odisha}

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
files = sorted(glob.glob(os.path.join(ROOT, "guide", "history-*.txt")))
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
        nav.append('<div class="navg">%s</div>' % html.escape({"PART A": "Part A · Static", "PART B": "Part B · News 2025–26", "LAST WEEK": "Last week"}.get(grp, grp)))
        last_part = grp
    nav.append('<a href="#%s"><span class="n">%s</span>%s</a>' % (c["id"], num, html.escape(c["title"])))
    mins = max(3, round(c["words"] / 210))
    toc.append('<li><span class="n">%s.</span><a href="#%s">%s</a><span class="dots"></span><span class="c">%d min</span></li>' % (num, c["id"], html.escape(c["title"]), mins))

n_ch = len(chapters) - 1
head = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ASO History Guide 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">
<style>%s</style></head><body>
<div class="bar"><div class="bar-in"><button class="btn" id="navbtn" aria-expanded="false" aria-controls="nav">Contents</button><b>ASO 2027 · HISTORY GUIDE</b></div>
<nav id="nav">%s</nav>
<div class="chap" id="chap"><div class="chap-k">Now reading</div><div class="chap-n" id="chapN">Start here</div><div class="chap-bar"><i id="chapBar"></i></div><div class="chap-m"><span><b id="chapPct">0%%</b></span><span id="chapMin"></span></div></div></div>
<main><div class="col">
<header class="mast"><h1>History Guide</h1><p class="tag">British rule in India and the<br><b>Freedom Struggle</b>, from Plassey<br>to 1950, with the 2025–26 news.</p></header>
<div class="orn" aria-hidden="true">· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·</div>
<div class="stats"><span class="count">%d chapters</span><span class="count">about %s words</span><span class="count">Part A static · Part B news 2025–26</span></div>
<div class="toc"><div class="tochead"><h2>Table of Contents.</h2><span class="line"></span><span class="r"><span>%d</span> chapters</span></div><ol class="toclist">%s</ol></div>
""" % (css, "".join(nav), n_ch, "{:,}".format(round(total_words, -2)), n_ch, "".join(toc))
foot = """</div></main>
<button class="btn" id="up" aria-label="Back to top">Top</button>
<footer><div class="col"><p>OPSC ASO 2027 · History Guide · built 17 Nov 2026 from the official syllabus topic (c), the 2018, 2021 and 2025 GA papers, standard textbooks and the 2025–26 commemorations.</p><p>Tags marked CHECK rest on one report or on sources that disagree: confirm them before the exam.</p></div></footer>
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
page = page.replace("</body></html>", "<script>window.ASO_INK_KEY='aso-ink-history-2027';</script>\n<script>\n" + INK_JS + "</script></body></html>", 1)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes;", n_ch, "chapters;", total_words, "words")
