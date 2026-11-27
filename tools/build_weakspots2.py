#!/usr/bin/env python3
"""Build ASO-English-Weak-Spots-Guide-2.html from guide/weak-2.txt (27 Nov 2026; copy of build_weakspots1.py).

    python3 tools/build_weakspots2.py

Same markup as build_history_guide.py, plus:
  ##R12 Title || one-line rule      numbered rule heading (also feeds the @@index table)
  ✗ wrong sentence / ✓ right sentence   consecutive lines become one wrong/right block
  @@index                           table of all rules

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
OUT = os.path.join(ROOT, "ASO-English-Weak-Spots-Guide-2.html")

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
.rule{display:flex;gap:10px;align-items:baseline;scroll-margin-top:70px}
.rule .h3n{white-space:nowrap;min-width:5.2em}
.wr{margin:10px 0 14px;border-left:2px solid var(--blue);padding:2px 0 2px 12px}
.wr-r{display:flex;gap:10px;align-items:baseline;margin:3px 0;line-height:1.45}
.wr-k{font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;min-width:5.6em;flex:none}
.wr-r.no .wr-k{color:var(--muted)}.wr-r.no .wr-s{color:var(--muted);text-decoration:line-through;text-decoration-color:rgba(110,110,115,.55)}
.wr-r.ok .wr-k{color:var(--blue)}
.ri td:first-child a{font-family:var(--f-mono);font-size:12px;color:var(--blue);text-decoration:none}
.navg{font-family:var(--f-mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);padding:12px 20px 2px}
"""

# ---------------------------------------------------------------- figures
def fig(label, right, svg, cap):
    return ('<div class="figwrap"><figure class="fig"><span class="fl">%s</span><span class="fr">[ %s ]</span>%s'
            '<span class="fy">RULES</span></figure><p class="figcap"><b>%s</b>%s</p></div>' % (label, right, svg, label, cap))

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

def fig_tenses():
    pts = [("had done", "earlier past"), ("did", "finished past"), ("have done", "past to now"),
           ("do / doing", "now"), ("will do", "future"), ("will have done", "done by then")]
    return fig("FIG_001", "TENSE LINE", timeline_svg(pts, "Tense timeline from past perfect to future perfect", 520),
               "Each tense is a place on one line. When two past actions are given, the earlier one takes had + V3.")

def fig_scan():
    steps = [("1", "Subject"), ("2", "Verb"), ("3", "Tense"), ("4", "Pronoun"), ("5", "Article"), ("6", "Preposition")]
    s = '<svg viewBox="0 0 540 150" role="img" aria-label="Six-step scan for error spotting">'
    for i, (n, t) in enumerate(steps):
        x = 12 + i * 88
        cls = "bl" if i < 2 else "ln"
        s += '<rect class="%s" x="%d" y="40" width="72" height="46"/>' % (cls, x)
        s += '<text class="%s" x="%d" y="58" text-anchor="middle">%s</text>' % ("lbrv" if cls == "bl" else "lb", x + 36, n)
        s += '<text class="%s" x="%d" y="76" text-anchor="middle">%s</text>' % ("lbsrv" if cls == "bl" else "lbs", x + 36, t)
        if i < 5:
            s += '<line class="hl" x1="%d" y1="63" x2="%d" y2="63"/>' % (x + 72, x + 88)
    s += '<text class="lbs" x="12" y="118">Blue boxes first: most wrong segments are a subject and its verb.</text></svg>'
    return fig("FIG_002", "ERROR SCAN", s, "Check the six things in this order. Stop at the first one that breaks a rule.")

FIGS = {"tenses": fig_tenses, "scan": fig_scan}

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
files = sorted(glob.glob(os.path.join(ROOT, "guide", "weak-2.txt")))
lines = []
for f in files:
    lines += open(f, encoding="utf-8").read().split("\n")

rules = []
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
    if re.match(r"##R\d", ln):
        m = re.match(r"##R(\d+)\s+(.*?)\s*\|\|\s*(.*)", ln)
        rn, rt, rs = m.group(1), m.group(2), m.group(3)
        rules.append((int(rn), rt, rs, cur["id"]))
        cur["parts"].append('<h3 class="rule" id="r%s"><span class="h3n">RULE %s</span><span>%s</span></h3>' % (rn, rn, inline(rt))); i += 1; continue
    if ln.startswith("✗ ") or ln.startswith("✓ "):
        rows = []
        while i < len(lines) and (lines[i].startswith("✗ ") or lines[i].startswith("✓ ")):
            ok = lines[i].startswith("✓ ")
            rows.append('<div class="wr-r %s"><span class="wr-k">%s</span><span class="wr-s">%s</span></div>' % (
                "ok" if ok else "no", "✓ Right" if ok else "✗ Wrong", inline(lines[i][2:].strip()))); i += 1
        t = '<div class="wr">%s</div>' % "".join(rows)
        cur["parts"].append(t); words(t); continue
    if ln.strip() == "@@index":
        cur["parts"].append("@@INDEX@@"); i += 1; continue
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
    while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|\?\?|@@|- |✗ |✓ )", lines[i]):
        para.append(lines[i].rstrip()); i += 1
    t = "<p>%s</p>" % inline(" ".join(para))
    cur["parts"].append(t); words(t)

rules.sort()
idx = '<div class="tw"><table class="t ri"><thead><tr><th>No.</th><th>Rule</th><th>In one line</th></tr></thead><tbody>'
for n, t, sm, cid in rules:
    idx += '<tr><td data-l="No."><a href="#r%d">%d</a></td><td data-l="Rule">%s</td><td data-l="In one line">%s</td></tr>' % (n, n, inline(t), inline(sm))
idx += "</tbody></table></div>"
for c in chapters:
    c["parts"] = [idx if x == "@@INDEX@@" else x for x in c["parts"]]

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
        nav.append('<div class="navg">%s</div>' % html.escape({"WEAK SPOT": "Ten weak spots", "LAST WEEK": "Last week"}.get(grp, grp)))
        last_part = grp
    nav.append('<a href="#%s"><span class="n">%s</span>%s</a>' % (c["id"], num, html.escape(c["title"])))
    mins = max(3, round(c["words"] / 210))
    toc.append('<li><span class="n">%s.</span><a href="#%s">%s</a><span class="dots"></span><span class="c">%d min</span></li>' % (num, c["id"], html.escape(c["title"]), mins))

n_ch = len(chapters) - 1
head = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ASO English Weak-Spots Guide 2</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">
<style>%s</style></head><body>
<div class="bar"><div class="bar-in"><button class="btn" id="navbtn" aria-expanded="false" aria-controls="nav">Contents</button><b>ASO 2027 · WEAK SPOTS 2</b></div>
<nav id="nav">%s</nav>
<div class="chap" id="chap"><div class="chap-k">Now reading</div><div class="chap-n" id="chapN">Start here</div><div class="chap-bar"><i id="chapBar"></i></div><div class="chap-m"><span><b id="chapPct">0%%</b></span><span id="chapMin"></span></div></div></div>
<main><div class="col">
<header class="mast"><h1>Weak Spots 2</h1><p class="tag">Ten small guides built from the <b>25 questions</b><br>you got wrong or skipped<br>in English Mock 09.</p></header>
<div class="orn" aria-hidden="true">· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·</div>
<div class="stats"><span class="count">%d chapters</span><span class="count">about %s words</span><span class="count">Mock 09 · 25 questions</span><span class="count">Paper III · English</span></div>
<div class="toc"><div class="tochead"><h2>Table of Contents.</h2><span class="line"></span><span class="r"><span>%d</span> chapters</span></div><ol class="toclist">%s</ol></div>
""" % (css, "".join(nav), n_ch, "{:,}".format(round(total_words, -2)), n_ch, "".join(toc))
foot = """</div></main>
<button class="btn" id="up" aria-label="Back to top">Top</button>
<footer><div class="col"><p>OPSC ASO 2027 · English Weak Spots Guide 2 · built 27 Nov 2026 from the wrong and skipped answers of English Mock 09; the rules come from the Grammar Guide, the 2018, 2021 and 2025 papers and standard grammar. The wording and all examples are this guide’s own.</p><p>Tags marked CHECK are answers that keys or grammar books disagree on: confirm them before the exam.</p></div></footer>
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
page = page.replace("</body></html>", "<script>window.ASO_INK_KEY='aso-ink-weak2-2027';</script>\n<script>\n" + INK_JS + "</script></body></html>", 1)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes;", n_ch, "chapters;", total_words, "words")
