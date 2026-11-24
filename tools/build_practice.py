#!/usr/bin/env python3
"""Build a question review-and-practice page (no timer, no marks) from one or more question files.

    python3 tools/build_practice.py

Reads tools/gs_history1_questions.py (set A, the original 50) and tools/gs_history2_questions.py (set B, the 100 siblings).
First option is the right one unless the question gives "a". The page shuffles the question order and the option order
EVERY time a session starts (statement codes such as "Only 1 and 2" keep their printed order).
Writes ASO-Modern-History-Practice-150.html (white-and-blue manual style, light mode only).
"""
import os, sys, json, importlib.util, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "ASO-Modern-History-Practice-150.html")
SETS = [("A", "tools/gs_history1_questions.py", "Original 50"), ("B", "tools/gs_history2_questions.py", "Siblings 100")]
KEY = "aso-history-practice-150"
FIX = [["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"],
       ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]]


def load(path):
    spec = importlib.util.spec_from_file_location("qf", os.path.join(ROOT, path))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.Q


data = []
for sid, path, _ in SETS:
    for i, q in enumerate(load(path), 1):
        a = q["a"] if q.get("a") is not None else 0
        data.append(dict(id="%s%d" % (sid, i), set=sid, q=q["q"], o=q["o"], a=a, e=q["e"], c=bool(q.get("c")),
                         fix=[str(x) for x in q["o"]] in FIX, src=q.get("src", "")))
assert all(len(d["o"]) == 4 and len(set(d["o"])) == 4 for d in data)
print("questions:", len(data), {s: sum(1 for d in data if d["set"] == s) for s, _, _ in SETS})

PAGE = r'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Modern History · Review and Practice</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=Silkscreen&display=swap" rel="stylesheet">
<style>
:root{--bg:#fbfbfb;--paper:#fff;--fg:#111;--muted:#6e6e73;--rule:#d7d7da;--grid:#eef0f6;--blue:#2b4cff;--blue-soft:#e0e6ff;--ok:#12794a;--ok-soft:#e3f4ec;--bad:#b4410b;--bad-soft:#fbeadf;
--f-serif:"EB Garamond","Iowan Old Style",Georgia,serif;--f-mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;--f-pixel:"Silkscreen","IBM Plex Mono",ui-monospace,monospace;color-scheme:light}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.7 var(--f-serif);-webkit-font-smoothing:antialiased;overflow-x:hidden}
button{font:inherit;color:inherit}
h1,h2,h3,p{margin:0}
:focus-visible{outline:2px solid var(--blue);outline-offset:3px}
.page{max-width:880px;margin:0 auto;padding:32px max(16px,env(safe-area-inset-left,0px)) 90px}
.mono,.eyebrow,.chip,.btn,.tag{font-family:var(--f-mono);text-transform:uppercase;letter-spacing:.08em}
.eyebrow{font-size:11px;color:var(--muted)}
.eyebrow b{color:var(--blue);font-weight:400}
.mast h1{font-family:var(--f-pixel);color:var(--blue);font-weight:400;font-size:clamp(2rem,7vw,3.6rem);line-height:1;letter-spacing:.02em;margin-top:8px}
.mast .sub{margin-top:12px;font-size:1.02rem}
.rule{display:flex;align-items:center;gap:14px;margin:28px 0 14px}
.rule .line{flex:1;height:1px;background:var(--fg)}
.lead::first-letter{float:left;font-size:3.6em;line-height:.82;padding:6px 8px 0 0}
.lead+.lead{margin-top:12px}
.fig{position:relative;border:1px dashed var(--rule);background-color:var(--paper);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:10px 10px;padding:18px 20px 20px 36px}
.fig .fl{position:absolute;left:10px;top:12px;font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;color:var(--muted);writing-mode:vertical-rl;transform:rotate(180deg)}
.row{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 14px}
.grp{font-family:var(--f-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-top:14px}
.chip{border:1px solid var(--rule);background:var(--paper);padding:5px 12px;font-size:11px;cursor:pointer;color:var(--fg)}
.chip[aria-pressed="true"]{border-color:var(--blue);color:var(--blue);background:var(--blue-soft)}
.chip[disabled]{opacity:.4;cursor:default}
.btn{border:1px solid var(--fg);background:var(--paper);padding:8px 16px;font-size:12px;cursor:pointer}
.btn.pri{background:var(--blue);border-color:var(--blue);color:#fff}
.btn.sm{padding:5px 12px;font-size:11px}
.btn:hover{border-color:var(--blue)}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px;align-items:center}
.note{font-size:.95rem;color:var(--muted);margin-top:10px}
[hidden]{display:none!important}

/* practice */
.bar{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);position:sticky;top:0;background:var(--bg);padding:10px 0;border-bottom:1px solid var(--rule);z-index:3}
.bar b{color:var(--fg);font-weight:500}
.prog{height:3px;background:var(--rule);margin-top:-1px}
.prog i{display:block;height:100%;background:var(--blue);width:0}
.qmeta{margin:22px 0 8px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.tag{font-size:10px;border:1px solid var(--blue);color:var(--blue);padding:0 6px;line-height:1.7}
.tag.chk{border:1px dashed var(--bad);color:var(--bad)}
.tag.src{border-color:var(--muted);color:var(--muted)}
.qtext{font-size:1.2rem;line-height:1.55;white-space:pre-line}
.opts{list-style:none;margin:16px 0 0;padding:0;display:grid;gap:10px}
.opt{display:flex;gap:12px;align-items:flex-start;width:100%;text-align:left;border:1px solid var(--rule);background:var(--paper);padding:11px 14px;cursor:pointer;line-height:1.45}
.opt .l{font-family:var(--f-mono);font-size:12px;color:var(--blue);min-width:1.4em;padding-top:2px}
.opt .t{min-width:0;overflow-wrap:anywhere}
.opt:hover:not([disabled]){border-color:var(--blue)}
.opt[disabled]{cursor:default}
.opt.right{border-color:var(--ok);background:var(--ok-soft)}
.opt.wrong{border-color:var(--bad);background:var(--bad-soft)}
.opt.right .l{color:var(--ok)}.opt.wrong .l{color:var(--bad)}
.expl{margin-top:18px;border:1px dashed var(--blue);background:var(--paper);padding:14px 18px;font-size:1rem}
.expl .v{font-family:var(--f-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:6px}
.expl .v.r{color:var(--ok)}.expl .v.w{color:var(--bad)}
.expl p+p{margin-top:8px}
.expl .k{font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-right:6px}

/* summary and review */
.big4{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:0;border-top:1px solid var(--fg);margin-top:10px}
.big4 div{padding:14px 12px 14px 0;border-bottom:1px dotted var(--muted)}
.big4 .n{font-family:var(--f-pixel);font-size:2rem;color:var(--blue);line-height:1}
.big4 .lb{font-family:var(--f-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-top:6px}
.rv details{border-bottom:1px dotted var(--muted);padding:8px 0}
.rv summary{cursor:pointer;list-style:none;display:flex;gap:10px;align-items:baseline}
.rv summary::-webkit-details-marker{display:none}
.rv summary .n{font-family:var(--f-mono);font-size:11px;color:var(--muted);min-width:3em}
.rv summary .s{white-space:pre-line;min-width:0;overflow-wrap:anywhere}
.rv .body{padding:8px 0 6px 3.4em}
.rv .a{margin:8px 0;padding:0;list-style:none;display:grid;gap:4px;font-size:.98rem}
.rv .a li{padding-left:18px;position:relative}
.rv .a li.ok{color:var(--ok);font-weight:600}
.rv .a li.ok::before{content:"\2713";position:absolute;left:0}
input.q{width:100%;border:1px solid var(--rule);background:var(--paper);padding:9px 12px;font:16px var(--f-serif);margin-top:10px}
textarea{width:100%;font:12px/1.5 var(--f-mono);border:1px solid var(--rule);background:var(--paper);padding:10px;margin-top:10px}
</style></head>
<body><main class="page">

<section id="s-start">
<header class="mast"><span class="eyebrow">General Studies Paper I · <b>Topic (c)</b></span><h1>History Practice</h1>
<p class="sub"><b>150 questions</b> on British rule and the freedom struggle: no timer, no marks, only practice and review.</p></header>

<div class="rule"><span class="eyebrow">How it works</span><span class="line"></span></div>
<p class="lead">This is a question bank, not a mock. Every time you press Start, the questions come in a new random order and the options are shuffled again, so you cannot learn the answer by its position. After each answer you see the right option and a short explanation: why it is right, the question it grew from, and the facts of the same family that are likely to come next.</p>
<p class="lead">The 150 are two sets. Set A is the original 50 most likely questions. Set B is 100 siblings: if a set A question asks when the Dandi March began, its siblings ask about the Non-Cooperation Movement, the Rowlatt Satyagraha and the Cripps Mission. Questions you miss or skip are remembered in this browser, so you can practise only those later.</p>

<div class="fig" style="margin-top:22px"><span class="fl">FIG_001</span>
<div class="grp" style="margin-top:0">Which questions</div>
<div class="row" id="set-row"></div>
<div class="grp">How many</div>
<div class="row" id="n-row"></div>
<div class="btns"><button class="btn pri" id="b-start">Start practice</button><button class="btn" id="b-review">Review all questions</button><button class="btn sm" id="b-reset">Forget my history</button></div>
<p class="note" id="st-note"></p></div>
</section>

<section id="s-prac" hidden>
<div class="bar"><span id="p-cnt"></span><span id="p-score"></span><span><button class="btn sm" id="b-end">End session</button></span></div>
<div class="prog"><i id="p-bar"></i></div>
<div class="qmeta" id="q-meta"></div>
<div class="qtext" id="q-text"></div>
<ol class="opts" id="q-opts"></ol>
<div id="q-expl"></div>
<div class="btns"><button class="btn" id="b-skip">Skip</button><button class="btn pri" id="b-next" hidden>Next →</button><span class="note" id="keys">Keys: 1–4 or A–D to answer · Enter for next · S to skip</span></div>
</section>

<section id="s-sum" hidden>
<div class="rule"><span class="eyebrow">Session finished</span><span class="line"></span></div>
<div class="big4" id="sum-big"></div>
<p class="note" id="sum-note" style="margin-top:12px"></p>
<div class="btns"><button class="btn pri" id="b-again">New random session</button><button class="btn" id="b-missed">Practise the ones I missed</button><button class="btn" id="b-copy">Copy report</button><button class="btn" id="b-home">Back to start</button><span class="note" id="copy-msg"></span></div>
<textarea id="copy-box" rows="8" readonly hidden></textarea>
<div class="rule"><span class="eyebrow">Missed and skipped in this session</span><span class="line"></span></div>
<div class="rv" id="sum-list"></div>
</section>

<section id="s-rev" hidden>
<div class="rule"><span class="eyebrow">Review all questions</span><span class="line"></span><button class="btn sm" id="b-rhome">← Back</button></div>
<div class="row" id="rv-set"></div>
<input class="q" id="rv-q" type="search" placeholder="Search a word: Gandhi, Viceroy, 1857…" aria-label="Search questions">
<p class="note" id="rv-n"></p>
<div class="rv" id="rv-list"></div>
</section>

</main>
<script>
var D = __DATA__;
var KEY = "__KEY__";
var LET = ["A","B","C","D"];
function $(id){return document.getElementById(id)}
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}return a}
function load(){try{return JSON.parse(localStorage.getItem(KEY))||{}}catch(e){return {}}}
function save(h){try{localStorage.setItem(KEY,JSON.stringify(h))}catch(e){}}
var H = load();                         // id -> {r: last result right|wrong|skip, w: times wrong, n: times seen}
var pick = {set:"all", n:0}, S = null;  // S = running session

function show(id){["s-start","s-prac","s-sum","s-rev"].forEach(function(x){$(x).hidden = x!==id}); window.scrollTo(0,0)}
function explHTML(e){
  var parts = e.split(/\s(?=(?:Grew from|Sibling of|Family):)/), out = "";
  parts.forEach(function(p){
    var m = p.match(/^(Why|Grew from|Sibling of|Family):\s*(.*)$/s);
    out += m ? '<p><span class="k">'+m[1]+'</span>'+esc(m[2])+'</p>' : '<p>'+esc(p)+'</p>';
  });
  return out;
}
function missedIds(){return D.filter(function(d){var h=H[d.id];return h && (h.r==="wrong"||h.r==="skip")}).map(function(d){return d.id})}

/* ---------- start screen ---------- */
function chips(rowId, items, key){
  var row=$(rowId); row.innerHTML="";
  items.forEach(function(it){
    var b=document.createElement("button"); b.className="chip"; b.textContent=it.t; b.disabled=!!it.off;
    b.setAttribute("aria-pressed", String(pick[key]===it.v));
    b.onclick=function(){pick[key]=it.v; drawStart()};
    row.appendChild(b);
  });
}
function poolFor(){
  var ids = pick.set==="missed" ? missedIds() : null;
  return D.filter(function(d){
    if(pick.set==="A"||pick.set==="B") return d.set===pick.set;
    if(pick.set==="missed") return ids.indexOf(d.id)>=0;
    return true;
  });
}
function drawStart(){
  var miss=missedIds().length;
  chips("set-row",[{t:"All 150",v:"all"},{t:"Set A · original 50",v:"A"},{t:"Set B · 100 siblings",v:"B"},{t:"Only my missed · "+miss,v:"missed",off:miss===0}],"set");
  var size=poolFor().length;
  chips("n-row",[{t:"All",v:0},{t:"50",v:50},{t:"25",v:25},{t:"10",v:10}],"n");
  var seen=Object.keys(H).length;
  $("st-note").textContent = size+" questions in this choice · "+seen+" of 150 seen so far · "+miss+" to revisit";
  $("b-start").disabled = size===0;
}

/* ---------- practice ---------- */
function startSession(){
  var pool=shuffle(poolFor());
  if(pick.n && pick.n<pool.length) pool=pool.slice(0,pick.n);
  if(!pool.length) return;
  S={list:pool, i:0, right:0, wrong:0, skip:0, log:[], answered:false};
  show("s-prac"); draw();
}
function view(d){                      // fresh option order every time a question is shown
  var items=d.o.map(function(t,k){return {t:t, ok:k===d.a}});
  return d.fix ? items : shuffle(items);
}
function draw(){
  var d=S.list[S.i]; S.cur={d:d, opts:view(d), done:false};
  $("p-cnt").innerHTML="Question <b>"+(S.i+1)+"</b> of <b>"+S.list.length+"</b>";
  score(); $("p-bar").style.width=(S.i/S.list.length*100)+"%";
  var m='<span class="tag">Set '+d.set+'</span>'; if(d.c) m+='<span class="tag chk">Check</span>'; if(d.src) m+='<span class="tag src">Exact repeat · '+esc(d.src)+'</span>';
  $("q-meta").innerHTML=m; $("q-text").textContent=d.q; $("q-expl").innerHTML="";
  var ol=$("q-opts"); ol.innerHTML="";
  S.cur.opts.forEach(function(o,k){
    var li=document.createElement("li"), b=document.createElement("button");
    b.className="opt"; b.innerHTML='<span class="l">'+LET[k]+'</span><span class="t">'+esc(o.t)+'</span>';
    b.onclick=function(){answer(k)}; li.appendChild(b); ol.appendChild(li);
  });
  $("b-next").hidden=true; $("b-skip").hidden=false;
  $("b-next").textContent = S.i===S.list.length-1 ? "Finish →" : "Next →";
}
function score(){$("p-score").innerHTML="<b>"+S.right+"</b> right · <b>"+S.wrong+"</b> wrong · <b>"+S.skip+"</b> skipped"}
function reveal(pickK){
  var c=S.cur, btns=document.querySelectorAll("#q-opts .opt");
  btns.forEach(function(b,k){b.disabled=true; if(c.opts[k].ok) b.classList.add("right"); else if(k===pickK) b.classList.add("wrong")});
  var verdict = pickK===null ? '<div class="v w">Skipped · the answer is shown above</div>' : (c.opts[pickK].ok ? '<div class="v r">Correct</div>' : '<div class="v w">Not this one · the right option is marked green</div>');
  $("q-expl").innerHTML='<div class="expl">'+verdict+explHTML(c.d.e)+'</div>';
  $("b-skip").hidden=true; $("b-next").hidden=false; c.done=true;
  $("b-next").scrollIntoView({block:"nearest",behavior:"smooth"});
}
function record(res){
  var d=S.cur.d, h=H[d.id]||{n:0,w:0}; h.n++; h.r=res; if(res==="wrong"||res==="skip") h.w++; H[d.id]=h; save(H);
}
function answer(k){
  var c=S.cur; if(c.done) return;
  var ok=c.opts[k].ok; if(ok) S.right++; else S.wrong++;
  S.log.push({d:c.d, pick:c.opts[k].t, res:ok?"right":"wrong"}); record(ok?"right":"wrong"); score(); reveal(k);
}
function skip(){
  var c=S.cur; if(c.done) return;
  S.skip++; S.log.push({d:c.d, pick:null, res:"skip"}); record("skip"); score(); reveal(null);
}
function next(){ if(!S.cur.done) return; S.i++; if(S.i>=S.list.length) finish(); else draw(); }
function finish(){
  show("s-sum");
  var done=S.log.length, pc=done? Math.round(S.right/done*100):0;
  $("sum-big").innerHTML=[[S.right,"right"],[S.wrong,"wrong"],[S.skip,"skipped"],[pc+"%","of answered right"]].map(function(x){return '<div><div class="n">'+x[0]+'</div><div class="lb">'+x[1]+'</div></div>'}).join("");
  var bad=S.log.filter(function(l){return l.res!=="right"});
  $("sum-note").textContent = bad.length ? bad.length+" to look at again. They are saved, so you can practise only these from the start page." : "Nothing missed in this session.";
  $("b-missed").hidden = !bad.length; $("copy-box").hidden=true; $("copy-msg").textContent="";
  $("sum-list").innerHTML = bad.map(function(l){return item(l.d, l.d.id, l.pick, false)}).join("");
}
function end(){ if(S && S.log.length) finish(); else {show("s-start"); drawStart()} }

/* ---------- lists (summary and review) ---------- */
function item(d, label, picked, open){
  var right=d.o[d.a], lis=d.o.map(function(t,k){return '<li'+(k===d.a?' class="ok"':'')+'>'+esc(t)+'</li>'}).join("");
  var pk = picked ? '<p class="note">Your pick: '+esc(picked)+'</p>' : (picked===null ? '<p class="note">Skipped</p>' : '');
  var chk = d.c ? ' <span class="tag chk">Check</span>' : '';
  return '<details'+(open?' open':'')+'><summary><span class="n">'+esc(label)+'</span><span class="s">'+esc(d.q)+chk+'</span></summary><div class="body"><ul class="a">'+lis+'</ul>'+pk+'<div class="expl">'+explHTML(d.e)+'</div></div></details>';
}
var rvSet="all";
function drawReview(){
  chips2();
  var q=$("rv-q").value.trim().toLowerCase();
  var list=D.filter(function(d){return (rvSet==="all"||d.set===rvSet) && (!q || (d.q+" "+d.o.join(" ")+" "+d.e).toLowerCase().indexOf(q)>=0)});
  $("rv-n").textContent=list.length+" of 150 questions. The green tick is the right option. Tap a question to open its explanation.";
  $("rv-list").innerHTML=list.map(function(d){return item(d, d.id, undefined, false)}).join("");
}
function chips2(){
  var row=$("rv-set"); row.innerHTML="";
  [["all","All 150"],["A","Set A · 50"],["B","Set B · 100"]].forEach(function(it){
    var b=document.createElement("button"); b.className="chip"; b.textContent=it[1]; b.setAttribute("aria-pressed",String(rvSet===it[0]));
    b.onclick=function(){rvSet=it[0]; drawReview()}; row.appendChild(b);
  });
}
function report(){
  var lines=["Modern History practice report · "+S.right+" right, "+S.wrong+" wrong, "+S.skip+" skipped"];
  S.log.filter(function(l){return l.res!=="right"}).forEach(function(l){
    lines.push("", l.d.id+" · "+(l.res==="skip"?"SKIPPED":"WRONG")+" · "+l.d.q.replace(/\n/g," / "), "  my pick: "+(l.pick||"-"), "  key: "+l.d.o[l.d.a]);
  });
  return lines.join("\n");
}

/* ---------- wire up ---------- */
$("b-start").onclick=startSession;
$("b-review").onclick=function(){show("s-rev"); drawReview()};
$("b-rhome").onclick=function(){show("s-start"); drawStart()};
$("rv-q").oninput=drawReview;
$("b-next").onclick=next; $("b-skip").onclick=skip; $("b-end").onclick=end;
$("b-again").onclick=startSession;
$("b-missed").onclick=function(){pick.set="missed"; pick.n=0; startSession()};
$("b-home").onclick=function(){show("s-start"); drawStart()};
$("b-reset").onclick=function(){ if(confirm("Forget which questions you have seen and missed?")){H={}; save(H); pick.set="all"; drawStart()} };
$("b-copy").onclick=function(){
  var t=report(), box=$("copy-box"); box.value=t; box.hidden=false;
  function done(){$("copy-msg").textContent="Copied."}
  if(navigator.clipboard&&navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done,function(){box.select()}); else {box.select(); try{document.execCommand("copy"); done()}catch(e){}}
};
document.addEventListener("keydown",function(e){
  if(e.metaKey||e.ctrlKey||e.altKey||$("s-prac").hidden) return;
  var k=e.key.toLowerCase(), idx="1234".indexOf(k); if(idx<0) idx="abcd".indexOf(k);
  if(idx>=0 && !S.cur.done){answer(idx); e.preventDefault()}
  else if((e.key==="Enter"||k==="n"||k===" ") && S.cur.done){next(); e.preventDefault()}
  else if(k==="s" && !S.cur.done){skip()}
});
drawStart();
</script></body></html>
'''

html_out = PAGE.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__KEY__", KEY)
open(OUT, "w", encoding="utf-8").write(html_out)
print("wrote", OUT, len(html_out), "bytes")
