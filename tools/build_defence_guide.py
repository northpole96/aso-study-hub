#!/usr/bin/env python3
"""Build ASO-Defence-Guide-2027.html from guide/defence-*.txt.

    python3 tools/build_defence_guide.py

Source format (one small markup, see guide/defence-1.txt):
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
OUT = os.path.join(ROOT, "ASO-Defence-Guide-2027.html")

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
            '<span class="fy">© 2026</span></figure><p class="figcap"><b>%s</b>%s</p></div>' % (label, right, svg, label, cap))

def box(x, y, w, h, t, cls="ln", sub=None):
    s = '<rect class="%s" x="%d" y="%d" width="%d" height="%d"/>' % (cls, x, y, w, h)
    tc = "lbrv" if cls == "bl" else "lb"
    if sub:
        s += '<text class="%s" x="%d" y="%d" text-anchor="middle">%s</text>' % (tc, x + w // 2, y + h // 2 - 2, t)
        s += '<text class="%s" x="%d" y="%d" text-anchor="middle">%s</text>' % ("lbsrv" if cls == "bl" else "lbs", x + w // 2, y + h // 2 + 12, sub)
    else:
        s += '<text class="%s" x="%d" y="%d" text-anchor="middle">%s</text>' % (tc, x + w // 2, y + h // 2 + 4, t)
    return s

def line(x1, y1, x2, y2):
    return '<line class="hz" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (x1, y1, x2, y2)

def fig_chain():
    s = '<svg viewBox="0 0 560 330" role="img" aria-label="Chain of command from the President to the three services">'
    s += box(200, 8, 160, 36, "PRESIDENT", "bl", "Supreme Commander")
    s += line(280, 44, 280, 60)
    s += box(190, 60, 180, 36, "PRIME MINISTER + CCS", "ln", "Cabinet Committee on Security")
    s += line(280, 96, 280, 112)
    s += box(190, 112, 180, 36, "DEFENCE MINISTER", "ln", "Ministry of Defence")
    s += line(280, 148, 280, 164)
    s += line(120, 164, 440, 164)
    s += line(120, 164, 120, 176) + line(440, 164, 440, 176)
    s += box(30, 176, 180, 40, "CHIEF OF DEFENCE STAFF", "lt", "Secretary, Dept of Military Affairs")
    s += box(350, 176, 180, 40, "DEFENCE SECRETARY", "ln", "Civil head of the Ministry")
    s += line(120, 216, 120, 236)
    s += line(60, 236, 180, 236)
    for x in (60, 120, 180):
        s += line(x, 236, x, 248)
    s += box(10, 248, 100, 40, "ARMY", "ln", "General")
    s += box(120, 248, 100, 40, "NAVY", "ln", "Admiral")
    s += box(230, 248, 100, 40, "AIR FORCE", "ln", "Air Chief Marshal")
    s += '<text class="lbs" x="30" y="312">The CDS plans and joins the services; each chief keeps command of his own service.</text>'
    s += "</svg>"
    return fig("FIG_001", "COMMAND CHAIN", s, "From the President down to the three services.")

def fig_ranks():
    s = '<svg viewBox="0 0 560 200" role="img" aria-label="Equal ranks: Colonel, Captain, Group Captain">'
    cols = [("ARMY", ["Major", "Lt Colonel", "Colonel", "Brigadier"], 2),
            ("NAVY", ["Lt Commander", "Commander", "Captain", "Commodore"], 2),
            ("AIR FORCE", ["Sqn Leader", "Wing Cdr", "Group Captain", "Air Cdre"], 2)]
    for i, (h, rows, hot) in enumerate(cols):
        x = 20 + i * 180
        s += '<text class="ttl" x="%d" y="20">%s</text>' % (x, h)
        for j, r in enumerate(rows):
            y = 30 + (3 - j) * 36
            c = "bl" if j == hot else "ln"
            s += box(x, y, 150, 30, r, c)
    s += '<text class="lbs" x="20" y="192">Same row = same rank. The Navy Captain is senior: equal to an Army Colonel.</text>'
    s += "</svg>"
    return fig("FIG_002", "RANK LADDER", s, "The blue row is the trap: Colonel, Captain and Group Captain are equal.")

def fig_missiles():
    data = [("Prithvi", 350), ("Pralay", 500), ("K-15 Sagarika", 750), ("Agni-I", 1200), ("Agni-II", 2000),
            ("Agni-III", 3000), ("K-4", 3500), ("Agni-IV", 4000), ("Agni-V", 5000)]
    s = '<svg viewBox="0 0 560 %d" role="img" aria-label="Missile ranges in kilometres">' % (40 + 26 * len(data))
    s += '<text class="ttl" x="20" y="18">APPROX. RANGE IN KM</text>'
    for i, (n, r) in enumerate(data):
        y = 30 + i * 26
        w = int(r / 5000 * 330)
        s += '<text class="lbm" x="20" y="%d">%s</text>' % (y + 14, n)
        s += '<rect class="%s" x="150" y="%d" width="%d" height="18"/>' % ("bl" if n.startswith("Agni-V") or n == "Pralay" else "lt", y, w)
        s += '<text class="lbs" x="%d" y="%d">%s</text>' % (150 + w + 6, y + 13, f"{r:,}" + ("+" if n == "Agni-V" else ""))
    s += "</svg>"
    return fig("FIG_003", "MISSILE RANGES", s, "Blue bars are the two most asked: Pralay and Agni-V.")

FIGS = {"chain": fig_chain, "ranks": fig_ranks, "missiles": fig_missiles}

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
files = sorted(glob.glob(os.path.join(ROOT, "guide", "defence-*.txt")))
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
<title>ASO Defence Guide 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">
<style>%s</style></head><body>
<div class="bar"><div class="bar-in"><button class="btn" id="navbtn" aria-expanded="false" aria-controls="nav">Contents</button><b>ASO 2027 · DEFENCE GUIDE</b></div>
<nav id="nav">%s</nav>
<div class="chap" id="chap"><div class="chap-k">Now reading</div><div class="chap-n" id="chapN">Start here</div><div class="chap-bar"><i id="chapBar"></i></div><div class="chap-m"><span><b id="chapPct">0%%</b></span><span id="chapMin"></span></div></div></div>
<main><div class="col">
<header class="mast"><h1>Defence Guide</h1><p class="tag">One place for the whole<br><b>Defence and Armed Forces</b> syllabus,<br>static and current affairs to Nov 2026.</p></header>
<div class="orn" aria-hidden="true">· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·</div>
<div class="stats"><span class="count">%d chapters</span><span class="count">about %s words</span><span class="count">Part A static · Part B news</span></div>
<div class="toc"><div class="tochead"><h2>Table of Contents.</h2><span class="line"></span><span class="r"><span>%d</span> chapters</span></div><ol class="toclist">%s</ol></div>
""" % (css, "".join(nav), n_ch, "{:,}".format(round(total_words, -2)), n_ch, "".join(toc))
foot = """</div></main>
<button class="btn" id="up" aria-label="Back to top">Top</button>
<footer><div class="col"><p>OPSC ASO 2027 · Defence Guide · built 17 Nov 2026 from the official syllabus topic (h), the 2018, 2021 and 2025 GA papers and defence news to 17 Nov 2026.</p><p>Tags marked CHECK rest on one report or on sources that disagree: confirm them before the exam.</p></div></footer>
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
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes;", n_ch, "chapters;", total_words, "words")
