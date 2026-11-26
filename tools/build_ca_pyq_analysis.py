"""Build ASO-CA-PYQ-Analysis-2027.html: every current-affairs PYQ dated against its own exam, and the 2026 events.

    python3 tools/build_ca_pyq_analysis.py

Data: tools/ca_analysis_pyq.py (past questions) and tools/ca_analysis_2026.py (2026 events).
Style: the white-and-blue reference-manual look (copied from ASO-Current-Affairs-2026-Manual.html,
light mode only). Then run python3 tools/add_pen_scroll.py if the tag is missing (it is written here).
"""
import html, os, re, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ca_analysis_pyq import PAPERS, FAMS
from ca_analysis_2026 import SECTIONS, WATCH, SOURCES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "ASO-CA-PYQ-Analysis-2027.html")
FAMNAME = dict(FAMS)
EXAM27 = "2027-01"
CHECKS = []   # (where, text) collected while building

def mon(ym):
    y, m = ym.split("-"); return int(y) * 12 + int(m) - 1

def lag(p, ym):
    return mon(p["exam"]) - mon(ym) if ym and re.match(r"\d{4}-\d\d$", ym) else None

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
def ymtext(n):
    return "%s %d" % (MONTHS[n % 12], n // 12)

def inl(s, where=None):
    if "⟨CHECK" in s and where:
        CHECKS.append(where)
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"⟦(\d{4}) (Q\d+)⟧", r'<span class="yr">\1</span>\2', s)
    s = re.sub(r"⟨CHECK( [^⟩]*)?⟩", lambda m: '<span class="chk">check%s</span>' % (m.group(1) or ""), s)
    return s

# ------------------------------------------------------------------ stats
for p in PAPERS:
    p["lags"] = [lag(p, q[2]) for q in p["qs"] if lag(p, q[2]) is not None]
    p["n"] = len(p["qs"])
    p["med"] = statistics.median(p["lags"])
    p["win"] = sum(1 for l in p["lags"] if 3 <= l <= 11)
    p["newest"] = min(p["lags"])
    p["fam"] = {}
    for q in p["qs"]:
        p["fam"][q[1]] = p["fam"].get(q[1], 0) + 1
ALL_LAGS = [l for p in PAPERS for l in p["lags"]]
ALL_WIN = sum(1 for l in ALL_LAGS if 3 <= l <= 11)
P69 = sum(1 for l in ALL_LAGS if 5 <= l <= 9)

# ------------------------------------------------------------------ CSS
CSS = r"""
:root{
  --bg:#fbfbfb; --paper:#ffffff; --fg:#111111; --muted:#6e6e73; --rule:#d7d7da; --grid:#eef0f6;
  --blue:#2b4cff; --blue-soft:#e0e6ff; --on-blue:#ffffff; --warn:#b4410b;
  --f-serif:"EB Garamond","Iowan Old Style",Georgia,serif;
  --f-mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;
  --f-pixel:"Silkscreen","IBM Plex Mono",ui-monospace,monospace;
  color-scheme:light;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}*{transition:none!important}}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.8 var(--f-serif);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:var(--fg);text-decoration:underline dotted;text-decoration-color:var(--blue);text-underline-offset:3px}
a:hover{color:var(--blue)}
:focus-visible{outline:2px solid var(--blue);outline-offset:3px}
button{font:inherit;color:inherit}
h1,h2,h3{font-weight:400;margin:0;text-wrap:balance;line-height:1.25}
p{margin:0}
b,strong{font-weight:600}
.page{max-width:1200px;margin:0 auto;padding-left:max(16px, env(safe-area-inset-left,0px));padding-right:max(16px, env(safe-area-inset-right,0px));padding-block:40px 96px}
.util{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.mast{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,420px);gap:24px 48px;align-items:end;margin-top:28px}
.mast h1{font-family:var(--f-pixel);color:var(--blue);font-size:clamp(2rem,5.4vw,4rem);line-height:1;letter-spacing:.02em}
.mast .tag{text-align:right;font-size:1.02rem;line-height:1.6}
@media (max-width:820px){.mast{grid-template-columns:1fr}.mast .tag{text-align:left}}
.orn{margin-block:22px 8px;height:12px;color:var(--muted);overflow:hidden;white-space:nowrap;font-family:var(--f-mono);font-size:11px;letter-spacing:.3em;line-height:12px;opacity:.7}
.hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px 56px;align-items:start;padding-block:32px 24px}
@media (max-width:900px){.hero{grid-template-columns:1fr}}
.dropcap::first-letter{float:left;font-size:4.1em;line-height:.82;padding:6px 8px 0 0;font-weight:400}
@media (min-width:900px){.hero .lead,.sh .intro p{text-align:justify;hyphens:auto}}
.hero .lead+.lead{margin-top:16px}
.meta{margin-top:22px;display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-block;border:1px solid var(--rule);background:var(--paper);padding:2px 10px;font-family:var(--f-mono);text-transform:uppercase;letter-spacing:.08em;font-size:11px;color:var(--fg)}
.legend{display:grid;gap:6px;margin-top:20px;font-size:.95rem;color:var(--muted)}
.chk{display:inline-block;font-family:var(--f-mono);text-transform:uppercase;letter-spacing:.08em;font-size:10px;color:var(--warn);border:1px dashed currentColor;padding:0 5px;margin-left:4px;vertical-align:2px;line-height:1.7}
.yr{display:inline-block;font-family:var(--f-mono);letter-spacing:.06em;font-size:10px;color:var(--blue);border:1px solid var(--blue);padding:0 5px;margin-right:4px;vertical-align:2px;line-height:1.7;font-variant-numeric:tabular-nums}
.fig{position:relative;margin:0;border:1px dashed var(--rule);background-color:var(--paper);
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:10px 10px;padding:30px 34px}
.fig svg{display:block;width:100%;height:auto;max-width:100%}
.fl,.fr,.fy{position:absolute;font-family:var(--f-mono);text-transform:uppercase;letter-spacing:.08em;font-size:10px;color:var(--muted);writing-mode:vertical-rl;line-height:1}
.fl{left:9px;top:12px;transform:rotate(180deg)}
.fr{right:9px;top:12px}
.fy{right:9px;bottom:12px}
.fig svg .ln{fill:var(--paper);stroke:var(--blue);stroke-width:1.2;stroke-linejoin:round;stroke-linecap:round}
.fig svg .lt{fill:var(--blue-soft);stroke:var(--blue);stroke-width:1.2;stroke-linejoin:round}
.fig svg .bl{fill:var(--blue)}
.fig svg .nf{fill:none;stroke:var(--blue);stroke-width:1.2;stroke-linecap:round;stroke-linejoin:round}
.fig svg .gr{fill:none;stroke:var(--rule);stroke-width:1}
.fig svg .dt{fill:none;stroke:var(--blue);stroke-width:1;stroke-dasharray:2 3}
.fig svg .lb{font-family:var(--f-mono);font-size:8.5px;letter-spacing:.06em;fill:var(--blue)}
.fig svg .lbm{font-family:var(--f-mono);font-size:8.5px;letter-spacing:.06em;fill:var(--muted)}
.fig svg .big{font-family:var(--f-pixel);font-size:18px;fill:var(--blue)}
.fig.wide{padding:30px 40px 26px}
.fig .cap{font-size:.95rem;color:var(--muted);margin-top:10px;max-width:80ch}
.toc{padding-block:56px 24px}
.tochead{display:flex;align-items:center;gap:16px}
.tochead h2{font-size:1.25rem;white-space:nowrap}
.tochead .v{font-family:var(--f-mono);font-size:10px;color:var(--muted);align-self:flex-start}
.tochead .line{flex:1;height:1px;background:var(--fg);min-width:20px}
.tochead .r{font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase}
.tochead .r span{color:var(--blue)}
.toclist{list-style:none;margin:36px 0 0;padding:0;columns:2 340px;column-gap:56px}
.toclist li{break-inside:avoid;display:flex;align-items:baseline;gap:8px;padding:5px 0;font-size:1rem}
.toclist .n{font-family:var(--f-mono);font-size:12px;color:var(--muted);min-width:2.4em}
.toclist a{text-decoration:none}
.toclist .dots{flex:1;border-bottom:1px dotted var(--muted);transform:translateY(-4px);min-width:16px}
.toclist .c{font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;color:var(--muted);white-space:nowrap}
.part{margin-top:64px;display:flex;align-items:center;gap:14px;font-family:var(--f-mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--blue)}
.part::after{content:"";flex:1;border-bottom:2px solid var(--blue)}
section.spread{padding-block:72px 8px;scroll-margin-top:16px}
.sh{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,340px);gap:32px 56px;align-items:start}
@media (max-width:860px){.sh{grid-template-columns:1fr}.sh .fig{max-width:420px}}
.sectrule{display:flex;align-items:center;gap:14px;margin-bottom:20px}
.sectrule .line{flex:1;height:1px;background:var(--fg)}
.eyebrow{font-family:var(--f-mono);text-transform:uppercase;letter-spacing:.08em;font-size:11px;color:var(--muted)}
.eyebrow b{color:var(--blue);font-weight:400}
.sh h2{font-size:clamp(1.7rem,3vw,2.3rem);margin-top:6px}
.sh .intro{margin-top:16px;max-width:66ch}
.sh .intro p+p{margin-top:14px}
.sh .intro p:first-child::first-letter{float:left;font-size:3.6em;line-height:.82;padding:6px 8px 0 0}
h3.sub{font-family:var(--f-mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;margin:44px 0 10px;display:flex;align-items:center;gap:12px}
h3.sub::after{content:"";flex:1;border-bottom:1px dotted var(--muted)}
.prose{max-width:70ch}
.prose p+p{margin-top:12px}
.asked{margin-top:28px;border-top:1px solid var(--fg);border-bottom:1px solid var(--rule);padding-block:12px 14px}
.asked h3{font-family:var(--f-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.asked ul{margin:8px 0 0;padding:0;list-style:none;display:grid;gap:6px}
.asked li{font-size:1rem;padding-left:16px;position:relative}
.asked li::before{content:"";position:absolute;left:0;top:.75em;width:5px;height:5px;background:var(--fg)}
.method{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0;margin-top:28px;border-top:1px solid var(--fg)}
.method .m{padding:16px 18px 16px 0;min-width:0;border-bottom:1px dotted var(--muted)}
.method .m .big{font-family:var(--f-pixel);font-size:2rem;color:var(--blue);line-height:1}
.method .m p{font-size:.95rem;margin-top:8px}
.trap{margin-top:24px;max-width:80ch;border:1px dashed var(--blue);background:var(--paper);padding:14px 18px;font-size:.98rem}
.trap .tt{font-family:var(--f-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-right:6px}
.trap ul{margin:6px 0 0;padding-left:1.1em}
.trap li+li{margin-top:4px}
/* question by question */
.qlist{margin-top:14px;border-top:1px solid var(--fg)}
.qrow{display:grid;grid-template-columns:64px minmax(0,1fr) 168px;gap:4px 20px;padding:12px 0;border-bottom:1px dotted var(--muted)}
.qrow .qn{font-family:var(--f-mono);font-size:12px;letter-spacing:.04em;padding-top:3px;white-space:nowrap}
.qrow .ask{font-weight:600;line-height:1.4}
.qrow .ans{display:block;color:var(--blue);margin-top:2px;line-height:1.4}
.qrow .ans::before{content:"\2192  ";font-family:var(--f-mono);font-size:.8em}
.qrow .nt{font-size:.95rem;margin-top:6px;line-height:1.6}
.qrow .side{display:flex;flex-direction:column;gap:6px;align-items:flex-start;padding-top:3px}
.fam{font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);border:1px solid var(--rule);background:var(--paper);padding:0 6px;line-height:1.8}
.when{font-family:var(--f-mono);font-size:10.5px;letter-spacing:.03em;color:var(--fg);line-height:1.4}
.lag{font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--blue);color:var(--blue);padding:0 6px;line-height:1.8;font-variant-numeric:tabular-nums}
.lag.in{background:var(--blue);color:var(--on-blue)}
.lag.na{border-color:var(--rule);color:var(--muted)}
@media (max-width:700px){.qrow{grid-template-columns:52px minmax(0,1fr)}.qrow .side{grid-column:2;flex-direction:row;flex-wrap:wrap;align-items:center}}
/* tables */
.rows{margin-top:10px;border-top:1px solid var(--fg)}
.row{display:grid;grid-template-columns:minmax(150px,240px) minmax(0,1fr);gap:4px 24px;padding:10px 0;border-bottom:1px dotted var(--muted)}
.row>div{min-width:0}
.row>div:first-child{font-weight:600}
.row.head>div{font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:400}
.t3 .row{grid-template-columns:minmax(150px,1fr) minmax(0,1fr) minmax(0,1fr)}
@media (max-width:760px){.row,.t3 .row{grid-template-columns:1fr}.row.head{display:none}}
.famt .row{grid-template-columns:minmax(150px,1.2fr) repeat(3,minmax(0,1fr)) minmax(0,.9fr);align-items:center}
.famt .row>div:first-child{font-weight:400}
.bar{display:flex;align-items:center;gap:8px;font-family:var(--f-mono);font-size:11px;font-variant-numeric:tabular-nums}
.bar i{display:block;height:10px;background:var(--blue);min-width:1px;flex-shrink:0;width:calc(var(--w) * 90px)}
@media (max-width:760px){.bar i{width:calc(var(--w) * 36px)}}
.bar.z i{background:var(--rule)}
.famt .exp{font-family:var(--f-mono);font-size:11px;letter-spacing:.04em;color:var(--blue)}
@media (max-width:760px){.famt .row{grid-template-columns:repeat(3,minmax(0,1fr))}.famt .row>div:first-child{grid-column:1/-1;font-weight:600}.famt .row .exp{grid-column:1/-1}.famt .row.head{display:none}.famt .bar::before{content:attr(data-y);color:var(--muted);white-space:nowrap}.famt .exp::before{content:"Expect in 2027: ";color:var(--muted)}}
/* events */
.evs{margin-top:10px;border-top:1px solid var(--fg)}
.ev{display:grid;grid-template-columns:96px minmax(0,1fr) minmax(0,.62fr);gap:4px 22px;padding:12px 0;border-bottom:1px dotted var(--muted)}
.ev>div{min-width:0}
.ev .tier{font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding-top:4px;line-height:1.5}
.stars{color:var(--blue);font-family:var(--f-mono);font-size:13px;letter-spacing:.12em}
.ev .tier b{display:block;color:var(--blue);font-weight:400;font-size:13px;letter-spacing:.12em}
.ev .tt{font-weight:600;line-height:1.4}
.ev .dd{font-family:var(--f-mono);font-size:10.5px;letter-spacing:.04em;color:var(--muted);margin-top:2px}
.ev .bd{font-size:.97rem;margin-top:6px;line-height:1.65}
.ev .hk{font-size:.92rem;line-height:1.55;border-left:2px solid var(--blue);padding-left:12px;align-self:start;margin-top:4px}
.ev .hk::before{content:"EXAM HOOK";display:block;font-family:var(--f-mono);font-size:9.5px;letter-spacing:.1em;color:var(--blue)}
@media (max-width:760px){.ev{grid-template-columns:1fr}.stars{color:var(--blue);font-family:var(--f-mono);font-size:13px;letter-spacing:.12em}
.ev .tier b{display:inline;margin-right:8px}}
/* flip cards */
.likely{margin-top:40px}
.likely h3{font-family:var(--f-mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;display:flex;align-items:center;gap:12px}
.likely h3::after{content:"";flex:1;border-bottom:1px dotted var(--muted)}
.likely .hint{font-size:.9rem;color:var(--muted);margin-top:4px}
.deck{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;margin-top:14px}
.card{perspective:1000px;border:0;background:none;padding:0;cursor:pointer;text-align:left;min-height:220px;display:block;width:100%}
.card .in{position:relative;display:block;width:100%;height:100%;min-height:220px;transition:transform .5s;transform-style:preserve-3d}
.card.flip .in{transform:rotateY(180deg)}
.card .f,.card .b{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;padding:14px 16px;display:flex;flex-direction:column;gap:10px;overflow:auto}
.card .f{background-color:var(--paper);border:1px solid var(--fg);
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:10px 10px}
.card .f .n{font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.card .f .q{font-size:1.02rem;line-height:1.45;padding-bottom:18px}
.card .f::after{content:"TAP TO TURN \2192";position:absolute;left:16px;bottom:10px;font-family:var(--f-mono);font-size:9px;letter-spacing:.1em;color:var(--blue)}
.card .b{background:var(--blue);color:var(--on-blue);transform:rotateY(180deg);border:1px solid var(--blue)}
.card .b .a{font-size:1.15rem;line-height:1.35}
.card .b .x{font-size:.92rem;line-height:1.5;opacity:.92}
.card .b .yr{color:var(--on-blue);border-color:var(--on-blue)}
.card:hover .f{border-color:var(--blue)}
@media (prefers-reduced-motion: reduce){.card .in{transition:none}}
.practice{display:grid;grid-template-columns:minmax(0,440px) minmax(0,1fr);gap:32px 56px;align-items:start;margin-top:22px}
@media (max-width:800px){.practice{grid-template-columns:1fr}}
.practice .card{min-height:280px}.practice .card .in{min-height:280px}
.pbtns{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.pbtns button{border:1px solid var(--fg);background:var(--paper);padding:5px 14px;cursor:pointer;font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;border-radius:3px}
.pbtns button.pri{border-color:var(--blue);color:var(--blue)}
.pbtns button:hover{background:var(--blue-soft)}
.score{font-family:var(--f-mono);font-size:11px;letter-spacing:.06em;color:var(--muted);margin-top:10px;font-variant-numeric:tabular-nums}
.check ul{columns:2 320px;column-gap:40px;padding-left:1.1em}
.check li{break-inside:avoid;margin-bottom:6px}
.src{font-size:.9rem;color:var(--muted)}
.src ul{columns:2 320px;column-gap:28px;padding-left:1.1em}
.src li{break-inside:avoid;margin-bottom:3px;overflow-wrap:anywhere}
footer{padding-top:36px;font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.totop{position:fixed;right:calc(16px + env(safe-area-inset-right,0px));bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:20;
  font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;color:var(--blue);background:var(--paper);border:1px solid var(--blue);padding:6px 10px;border-radius:3px}
"""

# ------------------------------------------------------------------ figures
def fig(num, label, svg, year="2026", cls="", cap=""):
    c = ('<p class="cap">%s</p>' % cap) if cap else ""
    return ('<figure class="fig %s"><span class="fl">FIG_%03d</span><span class="fr">[ %s ]</span>%s%s<span class="fy">&#169; %s</span></figure>'
            % (cls, num, label, svg, c, year))

def lag_chart():
    """Dot strip: one row per paper, x = months before the exam, one dot per dated question."""
    W, X0, X1, DY = 640, 70, 600, 7.5
    def x(l): return X0 + (min(l, 26) / 26.0) * (X1 - X0)
    rows, y = [], 36
    for p in PAPERS:
        st = {}
        for l in p["lags"]:
            k = min(l, 26); st[k] = st.get(k, 0) + 1
        y += max(st.values()) * DY + 14
        rows.append((p, y)); y += 22
    top, bot = 26, y - 8
    H = bot + 74
    s = ['<svg viewBox="0 0 %d %d" role="img" aria-label="Dot chart: how many months before each exam the news happened">' % (W, H)]
    s.append('<rect class="lt" x="%.1f" y="%d" width="%.1f" height="%d" opacity=".55"/>' % (x(5), top, x(9) - x(5), bot - top))
    s.append('<text class="lb" x="%.1f" y="%d" text-anchor="middle">6 IN 10 ITEMS WERE 5–9 MONTHS OLD</text>' % ((x(5) + x(9)) / 2, top - 8))
    for l in (0, 3, 6, 9, 12, 18, 24):
        s.append('<path class="gr" d="M%.1f %d L%.1f %d"/>' % (x(l), top, x(l), bot))
    for p, base in rows:
        s.append('<path class="nf" d="M%d %d L%d %d"/>' % (X0, base, X1, base))
        s.append('<text class="lb" x="4" y="%d">%d PAPER</text>' % (base - 4, p["year"]))
        s.append('<text class="lbm" x="4" y="%d">EXAM %s</text>' % (base + 10, p["exam_text"].upper().replace(" 20", " ’")))
        stack = {}
        for l in sorted(p["lags"]):
            k = min(l, 26); stack[k] = stack.get(k, 0) + 1
            s.append('<circle class="bl" cx="%.1f" cy="%.1f" r="3.2"/>' % (x(k), base - 6 - (stack[k] - 1) * DY))
    for l in (0, 3, 6, 9, 12, 18):
        s.append('<text class="lbm" x="%.1f" y="%d" text-anchor="middle">%d</text>' % (x(l), bot + 14, l))
    s.append('<text class="lbm" x="%.1f" y="%d" text-anchor="middle">24 AND OLDER</text>' % (x(25), bot + 14))
    s.append('<text class="lbm" x="%d" y="%d" text-anchor="middle">MONTHS BEFORE THE EXAM</text>' % ((X0 + X1) // 2, bot + 28))
    L = bot + 50
    s.append('<path class="nf" d="M%d %d L%d %d"/>' % (X0, L, X1, L))
    s.append('<rect class="bl" x="%.1f" y="%d" width="%.1f" height="4"/>' % (x(5), L - 2, x(9) - x(5)))
    e = mon(EXAM27)
    for l in (0, 3, 6, 9, 12, 18, 24):
        s.append('<path class="nf" d="M%.1f %d L%.1f %d"/>' % (x(l), L - 4, x(l), L + 4))
        s.append('<text class="lb" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x(l), L + 16, ymtext(e - l).upper().replace(" 20", " ’")))
    s.append('<text class="lb" x="4" y="%d">FOR THE</text><text class="lb" x="4" y="%d">2027 EXAM</text>' % (L - 6, L + 4))
    s.append('</svg>')
    return "".join(s)

SVG = {
"clock": '''<svg viewBox="0 0 380 290" role="img" aria-label="Line drawing of a desk calendar with dots for news items and a clock">
<path class="lt" d="M60 220 L200 150 L350 225 L210 290Z"/>
<path class="ln" d="M90 200 L90 70 L220 8 L220 140Z"/><path class="ln" d="M220 140 L220 8 L330 62 L330 194Z"/><path class="ln" d="M90 200 L220 140 L330 194 L200 254Z"/>
<path class="bl" d="M90 70 L220 8 L220 28 L90 90Z"/>
<g class="nf"><path d="M104 110 L206 60"/><path d="M104 130 L206 80"/><path d="M104 150 L206 100"/><path d="M104 170 L206 120"/><path d="M130 97 L130 160"/><path d="M155 85 L155 148"/><path d="M180 73 L180 136"/></g>
<g class="bl"><circle cx="142" cy="112" r="3.5"/><circle cx="142" cy="122" r="3.5"/><circle cx="142" cy="102" r="3.5"/><circle cx="167" cy="100" r="3.5"/><circle cx="167" cy="110" r="3.5"/><circle cx="117" cy="125" r="3.5"/></g>
<circle class="ln" cx="275" cy="105" r="34"/><path class="nf" d="M275 105 L275 82 M275 105 L292 114"/><circle class="bl" cx="275" cy="105" r="2.5"/>
<text class="big" x="240" y="178">-7</text><text class="lb" x="240" y="190">MONTHS</text>
<path class="dt" d="M142 112 L142 262 L28 262"/><text class="lb" x="4" y="276">MEDIAN ≈ 7–8 MONTHS BEFORE</text>
<path class="dt" d="M300 76 L360 40"/><text class="lb" x="292" y="32">EXAM DAY</text></svg>''',
"families": '''<svg viewBox="0 0 260 210" role="img" aria-label="Two lines: defence questions rising from 5 to 14, award questions falling from 8 to 0">
<g class="gr"><path d="M40 30 L40 170"/><path d="M120 30 L120 170"/><path d="M200 30 L200 170"/><path d="M30 170 L230 170"/></g>
<path class="nf" d="M40 125 L120 105 L200 30" style="stroke-width:2.2"/><g class="bl"><circle cx="40" cy="125" r="4"/><circle cx="120" cy="105" r="4"/><circle cx="200" cy="30" r="4"/></g>
<path class="dt" d="M40 90 L120 160 L200 170" style="stroke-width:1.6"/><g class="ln"><circle cx="40" cy="90" r="4"/><circle cx="120" cy="160" r="4"/><circle cx="200" cy="170" r="4"/></g>
<text class="lb" x="150" y="22">DEFENCE 5 → 14</text><text class="lb" x="46" y="82">AWARDS 8 → 0</text>
<text class="lbm" x="28" y="186">2018</text><text class="lbm" x="108" y="186">2021</text><text class="lbm" x="188" y="186">2025</text></svg>''',
"shield": '''<svg viewBox="0 0 260 210" role="img" aria-label="Line drawing of a missile on a launcher">
<path class="lt" d="M30 170 L130 120 L235 172 L135 205Z"/>
<path class="ln" d="M70 160 L190 100 L205 108 L85 168Z"/>
<path class="ln" d="M96 140 L196 50 L208 58 L108 148Z"/><path class="bl" d="M196 50 L214 36 L208 58Z"/>
<path class="nf" d="M110 150 L120 178 M170 118 L178 146"/>
<path class="dt" d="M214 36 L240 20"/><text class="lb" x="176" y="16">SURFACE-TO-SURFACE</text>
<path class="dt" d="M90 165 L40 140"/><text class="lb" x="6" y="132">KALAM ISLAND</text>
<text class="lbm" x="6" y="196">PRALAY · 150–500 KM</text></svg>''',
"calendar": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of a calendar page with two years of themes">
<path class="ln" d="M40 30 L200 30 L200 180 L40 180Z"/><path class="bl" d="M40 30 L200 30 L200 52 L40 52Z"/>
<g class="nf"><path d="M40 82 L200 82"/><path d="M40 112 L200 112"/><path d="M40 142 L200 142"/><path d="M80 52 L80 180"/><path d="M120 52 L120 180"/><path d="M160 52 L160 180"/></g>
<rect class="lt" x="120" y="112" width="40" height="30"/><rect class="lt" x="80" y="82" width="40" height="30"/>
<text class="lb" x="208" y="100">2025</text><path class="dt" d="M120 97 L206 97"/>
<text class="lb" x="208" y="130">2026</text><path class="dt" d="M160 127 L206 127"/>
<text class="lbm" x="40" y="196">LEARN TWO YEARS OF EVERY THEME</text></svg>''',
"globe": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of a globe with summit pins">
<circle class="ln" cx="125" cy="100" r="72"/><ellipse class="nf" cx="125" cy="100" rx="30" ry="72"/><path class="nf" d="M53 100 L197 100 M64 64 L186 64 M64 136 L186 136"/>
<g class="bl"><circle cx="150" cy="78" r="4"/><circle cx="110" cy="66" r="4"/><circle cx="96" cy="112" r="4"/></g>
<path class="dt" d="M150 78 L222 48"/><text class="lb" x="176" y="42">NEW DELHI · BRICS</text>
<path class="dt" d="M110 66 L60 22"/><text class="lb" x="6" y="16">BISHKEK · SCO</text>
<path class="dt" d="M96 112 L30 176"/><text class="lb" x="6" y="190">ANTALYA · COP31</text></svg>''',
"strait": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of the Strait of Hormuz between Iran and Oman">
<path class="lt" d="M10 20 L250 20 L250 70 Q190 60 160 88 Q130 70 80 74 Q40 70 10 90Z"/>
<path class="lt" d="M110 196 L130 128 Q150 104 172 116 Q200 132 250 126 L250 196Z"/>
<path class="nf" d="M30 120 Q100 96 150 104 Q190 110 250 98"/>
<path class="dt" d="M158 90 L160 114"/><text class="lb" x="150" y="52">IRAN</text><text class="lb" x="190" y="170">OMAN</text>
<text class="lbm" x="16" y="146">PERSIAN GULF</text><text class="lbm" x="176" y="112">GULF OF OMAN</text>
<text class="lb" x="96" y="88">HORMUZ</text></svg>''',
"pillar": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of a court building">
<path class="ln" d="M40 70 L130 24 L220 70Z"/><path class="bl" d="M40 70 L220 70 L220 80 L40 80Z"/>
<g class="ln"><rect x="56" y="84" width="16" height="78"/><rect x="92" y="84" width="16" height="78"/><rect x="152" y="84" width="16" height="78"/><rect x="188" y="84" width="16" height="78"/></g>
<path class="ln" d="M30 162 L230 162 L230 176 L30 176Z"/>
<text class="big" x="114" y="130">38</text><text class="lb" x="110" y="146">JUDGES</text>
<text class="lbm" x="30" y="194">ART. 124(1) · ART. 3–4 · ART. 21</text></svg>''',
"ledger": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of a ledger with a rising line">
<path class="ln" d="M30 30 L210 30 L210 176 L30 176Z"/><g class="nf"><path d="M30 60 L210 60"/><path d="M30 90 L210 90"/><path d="M30 120 L210 120"/><path d="M30 150 L210 150"/></g>
<path class="nf" d="M44 160 L84 138 L120 146 L156 104 L196 80" style="stroke-width:2"/><g class="bl"><circle cx="196" cy="80" r="4"/></g>
<text class="lb" x="40" y="22">BASE 2022-23</text><text class="lb" x="146" y="72">REPO 5.50%</text><text class="lbm" x="30" y="194">16TH FINANCE COMMISSION · 41%</text></svg>''',
"turtle": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of an olive ridley turtle on a beach">
<path class="lt" d="M0 150 Q130 120 260 150 L260 200 L0 200Z"/>
<ellipse class="ln" cx="130" cy="110" rx="56" ry="34"/><path class="nf" d="M100 92 L130 80 L160 92 M96 120 L130 136 L164 120 M130 80 L130 136"/>
<ellipse class="ln" cx="196" cy="104" rx="16" ry="11"/><path class="ln" d="M88 132 L64 150 L92 140Z"/><path class="ln" d="M168 132 L190 152 L164 140Z"/>
<path class="dt" d="M130 76 L130 30"/><text class="lb" x="84" y="24">RUSHIKULYA · GAHIRMATHA</text>
<text class="lbm" x="6" y="194">ARRIBADA = MASS NESTING</text></svg>''',
"rocket": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of a four-stage rocket">
<path class="ln" d="M116 170 L116 60 L130 30 L144 60 L144 170Z"/><path class="bl" d="M116 120 L144 120 L144 132 L116 132Z"/>
<path class="ln" d="M100 170 L100 120 L110 108 L116 120 L116 170Z"/><path class="ln" d="M160 170 L160 120 L150 108 L144 120 L144 170Z"/>
<path class="nf" d="M116 92 L144 92"/>
<path class="dt" d="M144 126 L200 126"/><text class="lb" x="168" y="118">STAGE 3</text><text class="lbm" x="168" y="140">PSLV-C62 FAULT</text>
<path class="dt" d="M130 30 L80 16"/><text class="lb" x="12" y="14">PAYLOAD</text><text class="lbm" x="6" y="194">EOS-N1 'ANVESHA' · 12 JAN 2026</text></svg>''',
"leaf": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of a stupa and a wetland">
<path class="lt" d="M10 170 Q70 150 130 166 Q190 182 250 160 L250 196 L10 196Z"/>
<path class="ln" d="M80 140 Q80 80 130 74 Q180 80 180 140Z"/><path class="ln" d="M70 140 L190 140 L190 152 L70 152Z"/><path class="ln" d="M124 74 L124 54 L136 54 L136 74Z"/><path class="bl" d="M120 50 L140 50 L140 54 L120 54Z"/>
<text class="lb" x="150" y="40">SARNATH · 45TH</text><path class="dt" d="M136 54 L170 44"/>
<text class="lbm" x="16" y="188">RAMSAR 103 · TIGER RESERVES 58</text></svg>''',
"ranks": '''<svg viewBox="0 0 260 200" role="img" aria-label="Bar line art of India's ranks in four reports">
<g class="lt"><rect x="40" y="58" width="30" height="112"/><rect x="90" y="82" width="30" height="88"/><rect x="140" y="140" width="30" height="30"/><rect x="190" y="40" width="30" height="130"/></g>
<path class="nf" d="M30 170 L232 170"/>
<text class="lb" x="40" y="52">127</text><text class="lb" x="90" y="76">100</text><text class="lb" x="144" y="134">38</text><text class="lb" x="190" y="34">157</text>
<text class="lbm" x="34" y="184">PEACE</text><text class="lbm" x="86" y="184">HUNGER</text><text class="lbm" x="136" y="184">INNOV.</text><text class="lbm" x="186" y="184">PRESS</text></svg>''',
"medal": '''<svg viewBox="0 0 260 200" role="img" aria-label="Line drawing of a medal">
<path class="lt" d="M100 20 L130 80 L160 20 L144 20 L130 50 L116 20Z"/>
<circle class="ln" cx="130" cy="120" r="46"/><circle class="nf" cx="130" cy="120" r="34"/>
<text class="big" x="112" y="128">-8</text><text class="lb" x="190" y="110">2018: 8 QS</text><text class="lb" x="190" y="124">2025: 0</text></svg>''',
}

# ------------------------------------------------------------------ pieces
def card(tag, q, a, x):
    return ('<button class="card" type="button"><span class="in"><span class="f"><span class="n">%s</span><span class="q">%s</span></span>'
            '<span class="b"><span class="a">%s</span><span class="x">%s</span></span></span></button>' % (inl(tag), inl(q), inl(a), inl(x)))

def deck(cards, title="Likely next"):
    if not cards: return ""
    return ('<div class="likely"><h3>%s</h3><p class="hint">Tap a card to turn it over. Each one is written the way the examiner writes.</p><div class="deck">%s</div></div>'
            % (title, "".join(card(*c) for c in cards)))

def asked(items, title="Asked before"):
    return '<div class="asked"><h3>%s</h3><ul>%s</ul></div>' % (title, "".join("<li>%s</li>" % inl(i) for i in items))

def head(num, eyebrow, title, intro_html, figure, sid):
    return ('<section class="spread" id="%s"><div class="sh"><div><div class="sectrule"><span class="eyebrow">Section <b>%02d</b> · %s</span><span class="line"></span></div>'
            '<h2>%s</h2><div class="intro">%s</div></div>%s</div>' % (sid, num, eyebrow, title, intro_html, figure))

TIER = {3: ("★★★", "Very likely"), 2: ("★★", "Likely"), 1: ("★", "Possible")}
def ev(row, where):
    t, title, when, body, hook = row
    st, lab = TIER[t]
    hk = '<div class="hk">%s</div>' % inl(hook, where + ": " + title) if hook else "<div></div>"
    return ('<div class="ev"><div class="tier"><b>%s</b>%s</div><div><div class="tt">%s</div>%s<div class="bd">%s</div></div>%s</div>'
            % (st, lab, inl(title, where + ": " + title), ('<div class="dd">%s</div>' % inl(when)) if when else "", inl(body, where + ": " + title), hk))

def table3(t, where):
    h = '<div class="row head">%s</div>' % "".join("<div>%s</div>" % c for c in t["head"])
    r = "".join('<div class="row">%s</div>' % "".join("<div>%s</div>" % inl(c, where + ": " + row[0]) for c in row) for row in t["rows"])
    return '<div class="rows t3">%s%s</div>' % (h, r)

# ------------------------------------------------------------------ part 1: the papers
def lagbadge(p, ym):
    l = lag(p, ym)
    if ym == "fixed": return '<span class="lag na">fixed date</span>'
    if ym == "run": return '<span class="lag na">running story</span>'
    if l is None: return '<span class="lag na">date not traced</span>'
    return '<span class="lag%s">%d mo before</span>' % (" in" if 3 <= l <= 11 else "", l)

PAPER_TEXT = {
2018: [
 "The 2018 paper was planned for 23 December 2018 and was finally held on 20 January 2019. It had **34 news and day questions**, the most of the three papers. The clearest finding is how bunched they are: **eleven come from one month, June 2018**, seven months before the exam (Miss India, the Tribal Queen, Italy's new Prime Minister, the Global Peace Index, Oceans Day, Statistics Day, Saudi women driving, the repo rate, Mithali Raj and more).",
 "The newest items are from September 2018 (Guha's Gandhi book and the first Poshan Maah). Nothing from October 2018 to January 2019 was asked. So the paper was set roughly three months before its first planned date, and the news it used was mostly 6 to 9 months old on exam day.",
 "It was also a 'GK magazine' paper: eight questions on pageants, ambassadors, awards, books and cricket. That type has almost disappeared since. Defence had five questions, and they were simple (a conference city, a slogan, an exercise state).",
],
2021: [
 "The 2021 paper was held on 27 August 2022, a week late because of floods. Its **28 news and day questions** fall into two groups. The larger group is from **January to March 2022**, five to seven months before the exam: the budget word for crypto, Villages of Excellence, the geo-park, the Sela tunnel, the naval helicopter, Dharma Guardian, the Boltzmann Medal and the BIMSTEC summit.",
 "A smaller group is very fresh: the World Forestry Congress (May), the UN Security Council election and the DAC approval (June), and **BHASHINI (4 July 2022), only seven weeks before the exam**. So in this cycle the setter kept adding news until late. A few items were old on purpose: the 2019 Chemistry Nobel and a 2020 law in Tibet.",
 "The mix moved away from personalities towards **government initiatives** (five questions), **world bodies** (four) and **defence** (seven). The first 20 questions of the paper were a current-affairs block, but news also sat inside the defence and environment questions later in the paper.",
],
2025: [
 "The 2025 paper (Advocate General office) was held on 9 November 2025. It has **30 news and day questions**, and it is the best guide to 2027 because it is the newest. Most of its news is from January to July 2025, with the peak in **February to May**. The newest dated items are Nomadic Elephant (June) and the Pralay tests (late July); nothing from August to October 2025 was asked. So the cut-off was about three to four months before the exam.",
 "**Defence took 14 of the 30**: six exercises, three operations, a missile, an engine, a renaming, a ministry project and a world defence system. **Nine news questions were statement questions**, and in each one the false statement changed a single detail: the state (Kutul is in Chhattisgarh, not Rajasthan), the group (TRF, not Hizbul), the aircraft (MiG-29 and Jaguar, not Tejas and Rafale), the headquarters (Geneva, not Vienna), the missile type.",
 "Two items were old on purpose: the **Earth Day theme of 2024**, with the 2025 theme used as the trap, and **Operation Jindagi** (2023). Pageants, sport, books and ambassadors: zero.",
],
}

def paper_section(num, p):
    y = p["year"]
    intro = "".join("<p>%s</p>" % inl(t) for t in PAPER_TEXT[y])
    news = sum(1 for q in p["qs"])
    method = ('<div class="method">'
      '<div class="m"><div class="big">%d</div><p>news and day questions out of 100.</p></div>'
      '<div class="m"><div class="big">%g mo</div><p>median age of the dated news on exam day (%s).</p></div>'
      '<div class="m"><div class="big">%d of %d</div><p>dated items were 3 to 11 months old on exam day.</p></div>'
      '<div class="m"><div class="big">%d mo</div><p>age of the newest item. The oldest was %d months.</p></div></div>'
      % (news, p["med"], p["exam_text"], p["win"], len(p["lags"]), p["newest"], max(p["lags"])))
    rows = []
    for q in p["qs"]:
        n, fam, ym, when, ask, ans, note, chk = q
        where = "%d Q%d" % (y, n)
        rows.append('<div class="qrow"><div class="qn"><span class="yr">%d</span>Q%d</div><div><div class="ask">%s</div><span class="ans">%s</span><p class="nt">%s</p></div>'
                    '<div class="side"><span class="fam">%s</span><span class="when">%s</span>%s</div></div>'
                    % (y, n, inl(ask), inl(ans), inl(note, where + ": " + ask), FAMNAME[fam].split(",")[0], inl(when), lagbadge(p, ym)))
    hooks = "".join("<li><b>%s · %s.</b> %s</li>" % (h[0], inl(h[1]), inl(h[2], "%d %s: %s" % (y, h[0], h[1]))) for h in p["hooks"])
    figure = fig(2 + num, "%d · %s" % (y, p["code"]), lag_mini(p), str(y))
    return (head(num, "THE %d PAPER" % y, "The %d paper, question by question" % y, intro, figure, "p%d" % y) + method +
            '<h3 class="sub">Every news and day question · exam %s</h3><p class="prose" style="font-size:.95rem;color:var(--muted)">%s A filled badge means the news was 3 to 11 months old on exam day, the usual window.</p><div class="qlist">%s</div>'
            % (p["exam_text"], inl(p["exam_note"]), "".join(rows)) +
            '<div class="trap"><span class="tt">News hidden in static questions</span><ul>%s</ul></div></section>' % hooks)

def lag_mini(p):
    """Small per-paper histogram: bars of questions per month-of-age."""
    cnt = {}
    for l in p["lags"]:
        k = min(l, 24); cnt[k] = cnt.get(k, 0) + 1
    W, X0, X1, B = 260, 20, 244, 160
    def x(l): return X0 + l / 24.0 * (X1 - X0)
    s = ['<svg viewBox="0 0 %d 200" role="img" aria-label="Bars of news questions by age in months, %d paper">' % (W, p["year"])]
    s.append('<rect class="lt" x="%.1f" y="20" width="%.1f" height="%d" opacity=".5"/>' % (x(3), x(11) - x(3), B - 20))
    for k, c in sorted(cnt.items()):
        s.append('<rect class="bl" x="%.1f" y="%d" width="6" height="%d"/>' % (x(k) - 3, B - c * 10, c * 10))
        if c >= 3: s.append('<text class="lb" x="%.1f" y="%d" text-anchor="middle">%d</text>' % (x(k), B - c * 10 - 4, c))
    s.append('<path class="nf" d="M%d %d L%d %d"/>' % (X0, B, X1, B))
    for l in (0, 6, 12, 18, 24):
        s.append('<text class="lbm" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x(l), B + 14, "24+" if l == 24 else l))
    s.append('<text class="lbm" x="%d" y="%d">MONTHS BEFORE EXAM</text>' % (X0, B + 30))
    s.append('<text class="lb" x="%.1f" y="14">USUAL WINDOW 3–11</text></svg>' % x(3))
    return "".join(s)

# ------------------------------------------------------------------ the comparison and the forecast
EXPECT = {"DEF": "10–13", "DAY": "4–5", "ORG": "2–4", "GOV": "2–3", "WLD": "2–3", "ODI": "2–3", "ENV": "1–2",
          "SCI": "1–2", "CRT": "1–2", "GEO": "1", "RPT": "0–1", "ECO": "1–2", "AWD": "0–1"}

def family_table():
    mx = max(c for p in PAPERS for c in p["fam"].values())
    h = '<div class="row head"><div>Family</div>%s<div>Expect in 2027</div></div>' % "".join("<div>%d</div>" % p["year"] for p in PAPERS)
    rows = []
    for code, name in FAMS:
        cells = []
        for p in PAPERS:
            c = p["fam"].get(code, 0)
            cells.append('<div class="bar%s" data-y="%d · "><i style="--w:%.3f"></i>%d</div>' % (" z" if c == 0 else "", p["year"], c / mx if c else 0.01, c))
        rows.append('<div class="row"><div>%s</div>%s<div class="exp">%s</div></div>' % (name, "".join(cells), EXPECT[code]))
    return '<div class="rows famt">%s%s</div>' % (h, "".join(rows))

HABITS = [
 ("Change one detail in a true sentence.", "Deep Ocean Mission 'green' for blue ⟦2021 Q8⟧; Chang'e-5 'Russia' for China ⟦2021 Q11⟧; Ukraine 'fourth' for second ⟦2021 Q17⟧; WMO in 'Vienna' ⟦2025 Q5⟧; Kutul in 'Rajasthan' ⟦2025 Q29⟧; Pralay 'air-to-surface' ⟦2025 Q36⟧; Keller 'Hizbul' ⟦2025 Q50⟧; Desert Flag 'Tejas and Rafale' ⟦2025 Q73⟧. So learn every news item with its **place, partner, type and group**."),
 ("Take the wrong options from the same news story.", "The Tribal Queen runners-up ⟦2018 Q5⟧, Italy's other politicians ⟦2018 Q7⟧, the real Sea Dragon members ⟦2025 Q7⟧, Iron Dome beside Golden Dome ⟦2025 Q9⟧. Knowing the whole story, not just the answer, beats these."),
 ("Ask the year before.", "Earth Day 2024 asked in November 2025 ⟦2025 Q2⟧; the 2019 Nobel asked in 2022 ⟦2021 Q91⟧; Silkyara (2023) asked in 2025 ⟦2025 Q11⟧. For 2027, learn the 2025 themes and winners as well as 2026."),
 ("Name the meeting or the edition so the key cannot change.", "'Second bi-monthly review' ⟦2018 Q76⟧, '17th edition' ⟦2025 Q55⟧, '5th summit' ⟦2021 Q56⟧, '15th Congress' ⟦2021 Q14⟧, '21st conference' ⟦2018 Q50⟧. Learn edition numbers of the big exercises and summits."),
 ("Ask who holds a post 'now'.", "The present Air Chief ⟦2021 Q82⟧. In 2026 the CDS and all three service chiefs changed."),
 ("Ask about what is about to happen.", "Chandrayaan-2's lander, six months before launch ⟦2018 Q59⟧. For 2027: Gaganyaan G1 and Vyommitra."),
 ("Repeat a family, sometimes the same question.", "Earth Day theme ×3; Dharma Guardian ×2 (almost word for word); the forest report ×2; olive ridleys ×2; BIMSTEC ×2; Article 21 rulings ×2; operation names in 2021 and 2025."),
]

def compare_section(num):
    intro = ("<p>Put the three papers side by side and three trends stand out. <b>Defence news grew every time</b>: 5, then 7, then 14. "
             "<b>Personality news died</b>: pageants, ambassadors, awards, books and sport went from 8 questions to 1 to 0. "
             "<b>Days and themes stayed</b>: 5, 1, 5, and the Earth Day theme came all three times.</p>"
             "<p>The age of the news is steady across all three papers. Of the %d dated items, <b>%d (%d%%) were 3 to 11 months old</b> on exam day, "
             "and %d were 5 to 9 months old. Very fresh news (under two months old) came only once: BHASHINI, seven weeks before the August 2022 exam. "
             "News more than a year old comes only when it is tied to something fixed: an Article, a famous operation, a 'first', a Nobel.</p>"
             % (len(ALL_LAGS), ALL_WIN, round(100 * ALL_WIN / len(ALL_LAGS)), P69))
    figure = fig(6, "TWO TRENDS", SVG["families"], "2026")
    chart = fig(7, "DOT CHART · AGE OF THE NEWS", lag_chart(), "2026", "wide",
                "Each dot is one dated news question, placed by how many months before its own exam the news happened. The bottom line turns the same scale into months before 17 January 2027.")
    habits = "".join("<li><b>%s</b> %s</li>" % (inl(a), inl(b)) for a, b in HABITS)
    return (head(num, "ACROSS THE PAPERS", "What changed from 2018 to 2025", intro, figure, "compare") +
            '<div style="margin-top:28px">%s</div>' % chart +
            '<h3 class="sub">News questions by family</h3>%s' % family_table() +
            '<h3 class="sub">Seven habits of the examiner</h3><div class="prose"><ol>%s</ol></div></section>' % habits)

def forecast_section(num):
    intro = ("<p>The exam is on <b>17 January 2027</b> (tentative). That is the same time of year as the 2018 paper (20 January 2019), whose news peaked seven months before the exam. "
             "If the setter works the same way as in 2018 and 2025, the paper is being set now, and its news will come from about <b>February to September 2026</b>, "
             "with the most from <b>April to August 2026</b>. October and November 2026 are worth a lighter read; December 2026 is unlikely to be asked.</p>"
             "<p>Expect about <b>30 news and day questions</b>. The table above gives the expected number per family. The 2026 events in Part B are grouped the same way, "
             "and each event has a star rating: three stars for a big event in a family that is asked every year, one star for a small or uncertain item.</p>")
    figure = fig(8, "WINDOW · JAN 2027", '''<svg viewBox="0 0 260 200" role="img" aria-label="Timeline of the likely news window for the January 2027 exam">
<path class="nf" d="M14 110 L246 110"/>''' + "".join('<path class="nf" d="M%.1f 104 L%.1f 116"/>' % (14 + i * 18, 14 + i * 18) for i in range(13)) + '''
<rect class="lt" x="32" y="92" width="144" height="36"/><rect class="bl" x="68" y="98" width="90" height="24" opacity=".85"/><rect class="bl" x="230" y="94" width="8" height="32"/>
<text class="lbm" x="6" y="142">JAN 26</text><text class="lbm" x="58" y="142">APR</text><text class="lbm" x="148" y="142">AUG</text><text class="lbm" x="212" y="142">JAN 27</text>
<path class="dt" d="M112 98 L112 54"/><text class="lb" x="70" y="48">PEAK · APR–AUG 2026</text>
<path class="dt" d="M234 94 L234 70 L200 70"/><text class="lb" x="168" y="74">EXAM</text>
<path class="dt" d="M40 128 L40 170"/><text class="lb" x="10" y="184">WINDOW · FEB–SEP 2026</text></svg>''', "2027")
    five = ('<div class="method">'
            '<div class="m"><div class="big">1</div><p><b>What</b> is it, in one plain sentence (an exercise, a missile, a ruling, a scheme)?</p></div>'
            '<div class="m"><div class="big">2</div><p><b>Who</b>: which country, ministry, force or person? Who is the partner?</p></div>'
            '<div class="m"><div class="big">3</div><p><b>Where</b>: which state, city, sea or base?</p></div>'
            '<div class="m"><div class="big">4</div><p><b>Which number</b>: edition, rank, count, range, theme of which year?</p></div>'
            '<div class="m"><div class="big">5</div><p><b>The static core</b>: the Article, the treaty, the science, the founding year behind it.</p></div></div>')
    split = ('<div class="trap"><span class="tt">How to split the next seven weeks of news study</span><ul>'
             '<li><b>Defence: about a third of the time.</b> Chiefs, every exercise with its partner and place, the Odisha-coast tests, Aridhaman, Urja Suraksha, the 246 renamings.</li>'
             '<li><b>Days and themes: a sixth.</b> Make one card per day with the 2025 and 2026 themes on it.</li>'
             '<li><b>Summits, world and India news: a third together.</b> BRICS New Delhi, SCO Bishkek, COP31, the Security Council, Hormuz, new leaders, Keralam, 38 judges, budget words.</li>'
             '<li><b>Odisha, space, environment: the rest.</b> Olive ridleys, Upper Indravati, Sarnath, Ramsar 103, PSLV-C62, Artemis II.</li>'
             '<li><b>Awards, books and sport: one quick read.</b> The 2025 paper had none.</li></ul></div>')
    return (head(num, "THE FORECAST", "What to expect in January 2027", intro, figure, "forecast") +
            '<h3 class="sub">Five things to know about every news item</h3>' + five + split + "</section>")

# ------------------------------------------------------------------ part 2: 2026 events
def events_section(num, s):
    intro = "".join("<p>%s</p>" % inl(t) for t in s["intro"])
    figure = fig(num + 1, s["id"].upper() + " · 2026", SVG[s["fig"]], "2026")
    out = [head(num, s["eyebrow"].upper(), s["title"], intro, figure, s["id"]), asked(s["asked"])]
    if s.get("table"):
        out.append('<h3 class="sub">%s</h3>' % ("Themes: 2025 and 2026 side by side" if s["id"] == "days" else "India's rank, 2026"))
        out.append(table3(s["table"], s["title"]))
    for sub, rows in s["blocks"]:
        out.append('<h3 class="sub">%s</h3><div class="evs">%s</div>' % (sub, "".join(ev(r, s["title"]) for r in rows)))
    out.append(deck(s["cards"]))
    out.append("</section>")
    return "".join(out)

# ------------------------------------------------------------------ page
def build():
    secs, toc = [], []
    n = 0
    toc.append(("00", "#how", "How to read this page", "LIST"))
    for i, p in enumerate(PAPERS):
        n += 1; toc.append(("%02d" % n, "#p%d" % p["year"], "The %d paper, question by question" % p["year"], "%d QS" % len(p["qs"])))
        secs.append(paper_section(n, p))
    n += 1; toc.append(("%02d" % n, "#compare", "What changed from 2018 to 2025", "CHART")); secs.append(compare_section(n))
    n += 1; toc.append(("%02d" % n, "#forecast", "What to expect in January 2027", "PLAN")); secs.append(forecast_section(n))
    part_b_at = len(secs)
    ncards = 0
    for s in SECTIONS:
        n += 1
        k = len(s["cards"]); ncards += k
        nev = sum(len(r) for _, r in s["blocks"]) + (len(s["table"]["rows"]) if s.get("table") else 0)
        toc.append(("%02d" % n, "#" + s["id"], s["title"], "%d ITEMS" % nev))
        secs.append(events_section(n, s))
    n += 1; toc.append(("%02d" % n, "#practice", "Shuffled practice deck", "%d CARDS" % ncards))
    n += 1; toc.append(("%02d" % n, "#watch", "Still to come, and the CHECK list", "LIST"))

    totalq = sum(len(p["qs"]) for p in PAPERS)
    hero = ('<div class="hero"><div><p class="lead dropcap">I took every current-affairs question from the 2018, 2021 and 2025 General Awareness papers (%d questions in all), '
            'found when each piece of news happened, and measured how old it was on the day of its own exam. Part A goes through them one by one. It shows the pattern behind them: '
            'which kinds of news are asked, how old the news is, and the tricks the examiner uses.</p>'
            '<p class="lead">Part B uses that pattern on 2026. It lists the national and international events of January to November 2026 that fit the families the examiner asks, '
            'rates each one, explains it in plain words, and ends each section with cards written in exam style. The aim is simple: when the January 2027 paper asks a news question, '
            'you should have met that event here, together with the detail the examiner will twist.</p>'
            '<div class="meta"><span class="chip">Exam: 17 January 2027 (tentative)</span><span class="chip">News checked to 26 November 2026</span><span class="chip">%d of %d dated PYQ items were 3–11 months old</span></div>'
            '<div class="legend"><span><span class="lag in">7 mo before</span> news age on its exam day, inside the usual 3–11 month window</span>'
            '<span><span class="chk">check</span> one source only, sources disagree, or the key is ours and unsure</span>'
            '<span><span class="yr">2025</span>Q10 a past question, with its number</span>'
            '<span><span class="stars">★★★</span> very likely · <span class="stars">★★</span> likely · <span class="stars">★</span> possible</span></div></div>%s</div>'
            % (totalq, ALL_WIN, len(ALL_LAGS), fig(1, "THE NEWS CLOCK", SVG["clock"], "2026")))
    tochtml = ('<section class="toc" id="contents"><div class="tochead"><h2>Table of Contents.</h2><span class="v">V1.0</span><span class="line"></span>'
               '<span class="r">PYQs · <span>%d</span> · Cards · <span>%d</span></span></div><ol class="toclist">%s</ol></section>'
               % (totalq, ncards, "".join('<li><span class="n">%s.</span><a href="%s">%s</a><span class="dots"></span><span class="c">%s</span></li>' % t for t in toc)))
    how = ('<section class="spread" id="how"><div class="prose"><div class="sectrule"><span class="eyebrow">Section <b>00</b> · BEFORE YOU READ</span><span class="line"></span></div>'
           '<p>Read Part A once, slowly: it is the reason Part B looks the way it does. Then use Part B as a revision list. For each event, say the five facts aloud '
           '(what, who, where, which number, the static core) before you read the exam hook beside it. The cards at the end of each section and the shuffled deck test the same things.</p>'
           '<p style="margin-top:12px">Keys of past questions are ours: OPSC has published no answer key. They were checked against the Udyam IAS books and, for the news, against news reports. '
           'Where a key or a fact is still unsure it carries a <span class="chk">check</span> tag. Never treat a CHECK item as certain; tick it in your monthly magazine.</p></div></section>')
    partA = '<div class="part">Part A · The past papers</div>'
    partB = '<div class="part">Part B · The events of 2026</div>'
    practice = ('<section class="spread" id="practice"><div class="sectrule"><span class="eyebrow">Section <b>%02d</b> · PRACTICE</span><span class="line"></span></div>'
                '<h2 style="font-size:clamp(1.7rem,3vw,2.3rem)">Shuffled practice deck</h2>'
                '<div class="practice"><button class="card" id="pcard" type="button"><span class="in"><span class="f"><span class="n" id="pn"></span><span class="q" id="pq"></span></span>'
                '<span class="b"><span class="a" id="pa"></span><span class="x" id="px"></span></span></span></button>'
                '<div class="prose"><p>All %d cards from Part B in a random order. Tap the card to see the answer, then say honestly whether you knew it. Missed cards are worth writing on a slip for the last week.</p>'
                '<div class="pbtns"><button type="button" class="pri" id="pgot">Knew it</button><button type="button" id="pmiss">Missed it</button><button type="button" id="pshuf">Shuffle again</button></div>'
                '<p class="score" id="pscore"></p></div></div></section>' % (n - 1, ncards))
    seen = []
    for c in CHECKS:
        if c not in seen: seen.append(c)
    checks = "".join("<li>%s</li>" % html.escape(re.sub(r"⟨[^⟩]*⟩|\*\*|⟦|⟧", "", c).strip()[:110]) for c in seen)
    srcs = "".join(('<li><a href="%s" rel="noopener">%s</a></li>' % (html.escape(u), html.escape(t))) if u else "<li>%s</li>" % html.escape(t) for t, u in SOURCES)
    watch = ('<section class="spread" id="watch"><div class="sectrule"><span class="eyebrow">Section <b>%02d</b> · LAST WEEKS</span><span class="line"></span></div>'
             '<h2 style="font-size:clamp(1.7rem,3vw,2.3rem)">Still to come, and the CHECK list</h2>'
             '<div class="prose" style="margin-top:14px"><p>These events fall after 26 November 2026. The paper is probably set already, so they are less likely to be asked, but a late item did come in 2022 (BHASHINI, seven weeks before the exam). Write the answers on one page in the first week of January.</p></div>'
             '<div class="check"><h3 class="sub">Watch list</h3><ul>%s</ul></div>'
             '<div class="check"><h3 class="sub">Items marked CHECK (%d)</h3><ul>%s</ul></div>'
             '<div class="src"><h3 class="sub">Sources checked for this page</h3><ul>%s</ul></div></section>'
             % (n, "".join("<li>%s</li>" % inl(w) for w in WATCH), len(seen), checks, srcs))
    body = ('<div class="util"><span>OPSC ASO · General Awareness · Paper I</span><span>Edition 26 Nov 2026</span></div>'
            '<header class="mast"><h1>NEWS IN THE PAPER</h1><p class="tag">Every current-affairs question of 2018, 2021 and 2025, dated against its exam.<br><b>Then the events of 2026 that fit the pattern.</b></p></header>'
            '<div class="orn" aria-hidden="true">' + "※ " * 120 + '</div>' + hero + tochtml + how + partA + "".join(secs[:part_b_at]) + partB + "".join(secs[part_b_at:]) + practice + watch +
            '<footer>Built from the 2018, 2021 and 2025 GA papers (keys ours, no official key), the project news bank and web searches of 26 Nov 2026 · light mode only</footer>')
    js = r"""<script>
(function(){
  document.querySelectorAll('.deck .card').forEach(function(c){c.addEventListener('click',function(){c.classList.toggle('flip');});});
  var pool=[].map.call(document.querySelectorAll('.deck .card'),function(c){
    var sec=c.closest('section'); var h=sec?sec.querySelector('h2'):null;
    return {n:c.querySelector('.f .n').textContent, q:c.querySelector('.f .q').innerHTML, a:c.querySelector('.b .a').innerHTML, x:c.querySelector('.b .x').innerHTML, s:h?h.textContent:''};
  });
  var order=[],i=0,got=0,miss=0,pc=document.getElementById('pcard');
  function show(){
    var c=pool[order[i%order.length]]; pc.classList.remove('flip');
    document.getElementById('pn').textContent=c.n+' · '+c.s;
    document.getElementById('pq').innerHTML=c.q; document.getElementById('pa').innerHTML=c.a; document.getElementById('px').innerHTML=c.x;
    document.getElementById('pscore').textContent='Card '+((i%order.length)+1)+' of '+order.length+' · knew '+got+' · missed '+miss;
  }
  function shuffle(){order=pool.map(function(_,k){return k;});for(var k=order.length-1;k>0;k--){var j=Math.floor(Math.random()*(k+1));var t=order[k];order[k]=order[j];order[j]=t;}i=0;got=0;miss=0;show();}
  pc.addEventListener('click',function(){pc.classList.toggle('flip');});
  document.getElementById('pgot').addEventListener('click',function(){got++;i++;show();});
  document.getElementById('pmiss').addEventListener('click',function(){miss++;i++;show();});
  document.getElementById('pshuf').addEventListener('click',shuffle);
  shuffle();
})();
</script>"""
    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>ASO Current Affairs: PYQ Analysis and 2026 Events</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap">\n'
            '<style>%s</style>\n</head>\n<body>\n<main><div class="page">%s</div></main>\n<a class="totop" href="#contents">Contents ↑</a>\n%s\n<script src="pen-scroll.js?v=8" defer></script>\n</body>\n</html>\n'
            % (CSS, body, js))
    open(OUT, "w").write(page)
    words = len(re.sub(r"<[^>]+>", " ", re.sub(r"<(style|script|svg)[\s\S]*?</\1>", " ", page)).split())
    print("wrote %s: %d KB, about %d words, %d PYQs, %d cards, %d CHECK items" % (os.path.basename(OUT), len(page) // 1024, words, totalq, ncards, len(seen)))
    for p in PAPERS:
        print("  %d: n=%d dated=%d median=%g window=%d newest=%d fam=%s" % (p["year"], p["n"], len(p["lags"]), p["med"], p["win"], p["newest"], p["fam"]))
    print("  all: %d dated, %d in 3-11, %d in 5-9" % (len(ALL_LAGS), ALL_WIN, P69))

if __name__ == "__main__":
    build()
