/* Pen-tablet drawing mode for the ASO guides.
   Ink engine ported from the draw-app project (ink-stroke.ts + ink-canvas.tsx):
   streamlined, pressure-sensitive strokes, Catmull-Rom smoothing, pen/mouse brush,
   pen-eraser end, tablet quirks (flat pressure, missed pointerup, coalesced events).
   New here: strokes are anchored to the chapter they start in and painted on tiles that scroll with the text, saved in localStorage,
   highlighter, stroke eraser, undo, clear, hide, and "touch scrolls / touch draws". */
(function () {
  "use strict";
  var KEY = window.ASO_INK_KEY || "aso-ink-" + location.pathname;

  /* ---------------- ink engine (from ink-stroke.ts) ---------------- */
  var PRESSURE_RATE = 0.275, DENSE_SPACING = 3, SAMPLE_SPACING = 0.75, WIDTH_STEP = 0.04;

  function densify(pts, emit) {
    var n = pts.length;
    function knot(a, b) { return Math.max(1e-4, Math.sqrt(Math.hypot(b.x - a.x, b.y - a.y))); }
    for (var i = 0; i < n - 1; i++) {
      var p0 = pts[Math.max(0, i - 1)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(n - 1, i + 2)];
      var steps = Math.max(1, Math.ceil(Math.hypot(p2.x - p1.x, p2.y - p1.y) / DENSE_SPACING));
      var t1 = p0 === p1 ? 1e-4 : knot(p0, p1);
      var t2 = t1 + knot(p1, p2);
      var t3 = t2 + (p3 === p2 ? 1e-4 : knot(p2, p3));
      for (var s = 1; s <= steps; s++) {
        var u = s / steps, t = t1 + (t2 - t1) * u;
        var lerp = function (a, b, ta, tb) { return ((tb - t) * a + (t - ta) * b) / (tb - ta); };
        var ax1 = lerp(p0.x, p1.x, 0, t1), ay1 = lerp(p0.y, p1.y, 0, t1);
        var ax2 = lerp(p1.x, p2.x, t1, t2), ay2 = lerp(p1.y, p2.y, t1, t2);
        var ax3 = lerp(p2.x, p3.x, t2, t3), ay3 = lerp(p2.y, p3.y, t2, t3);
        var bx1 = lerp(ax1, ax2, 0, t2), by1 = lerp(ay1, ay2, 0, t2);
        var bx2 = lerp(ax2, ax3, t1, t3), by2 = lerp(ay2, ay3, t1, t3);
        emit(lerp(bx1, bx2, t1, t2), lerp(by1, by2, t1, t2), p1.p + (p2.p - p1.p) * u);
      }
    }
  }

  function steady(input, brush, isComplete) {
    var n = input.length;
    if (n === 0) return [];
    var size = brush.size, first = input[0], firstP = first.p, i = 1, minD2 = Math.pow(size / 3, 2);
    while (i < n && Math.pow(input[i].x - first.x, 2) + Math.pow(input[i].y - first.y, 2) <= minD2) {
      firstP = Math.max(firstP, input[i].p); i++;
    }
    var out = [{ x: first.x, y: first.y, p: firstP, dist: 0, run: 0 }];
    var lag = Math.max(0.1, brush.streamline * size), px = first.x, py = first.y, run = 0, k = 1;
    function take(ix, iy, ip, exact) {
      var x = ix, y = iy;
      if (!exact) {
        var a = 1 - Math.exp(-Math.hypot(ix - px, iy - py) / lag);
        x = px + (ix - px) * a; y = py + (iy - py) * a;
      }
      if (Math.abs(x - px) < 1e-4 && Math.abs(y - py) < 1e-4) return;
      var d = Math.hypot(x - px, y - py);
      run += d;
      if (k++ < 4 && run < size) return;
      out.push({ x: x, y: y, p: ip, dist: d, run: run });
      px = x; py = y;
    }
    var kept = [first].concat(input.slice(i));
    densify(kept, function (x, y, p) { take(x, y, p, false); });
    if (isComplete && n > 1) { var last = input[n - 1]; take(last.x, last.y, last.p, true); }
    return out;
  }

  function widths(pts, brush) {
    var size = brush.size, thinning = brush.thinning, sim = brush.simulatePressure, easing = brush.easing, n = pts.length;
    function radius(p) { return Math.max(0.05, size * easing(0.5 - thinning * (0.5 - p))); }
    var total = pts[n - 1].run;
    if (!sim && total < size) {
      var max = pts.reduce(function (m, q) { return Math.max(m, q.p); }, 0.5);
      return pts.map(function () { return radius(max); });
    }
    function step(prev, q) {
      var sp = Math.min(1, q.dist / size), target = sim ? Math.min(1, 1 - sp) : q.p;
      return Math.min(1, prev + (target - prev) * sp * PRESSURE_RATE);
    }
    var prev = sim ? 0.5 : pts[0].p;
    for (var j = 0; j < n; j++) {
      var q = pts[j];
      if (q.run > size * 5) break;
      var sp = Math.min(1, q.dist / size);
      var p = sim ? Math.min(1, prev + (Math.min(1, 1 - sp) - prev) * sp * PRESSURE_RATE)
                  : Math.min(1, prev + (q.p - prev) * 0.5);
      prev += (p - prev) * 0.5;
    }
    return pts.map(function (q) { prev = step(prev, q); return radius(prev); });
  }

  function paintStroke(ctx, input, brush, isComplete) {
    var pts = steady(input, brush, isComplete);
    if (pts.length === 0) return;
    var r = widths(pts, brush);
    if (pts.length === 1) { ctx.beginPath(); ctx.arc(pts[0].x, pts[0].y, r[0], 0, Math.PI * 2); ctx.fill(); return; }
    ctx.save();
    ctx.strokeStyle = ctx.fillStyle; ctx.lineCap = "round"; ctx.lineJoin = "round";
    var runWidth = -1;
    function wOf(rad) { return Math.max(WIDTH_STEP, Math.round((2 * rad) / WIDTH_STEP) * WIDTH_STEP); }
    function begin(x, y, w) { runWidth = w; ctx.beginPath(); ctx.moveTo(x, y); }
    function end() { ctx.lineWidth = runWidth; ctx.stroke(); }
    begin(pts[0].x, pts[0].y, wOf(r[0]));
    function emit(x, y, rad) {
      var w = wOf(rad);
      ctx.lineTo(x, y);
      if (w !== runWidth) { end(); begin(x, y, w); }
    }
    function line(x0, y0, r0, x1, y1, r1) {
      var steps = Math.max(1, Math.ceil(Math.hypot(x1 - x0, y1 - y0) / SAMPLE_SPACING));
      for (var s = 1; s <= steps; s++) { var u = s / steps; emit(x0 + (x1 - x0) * u, y0 + (y1 - y0) * u, r0 + (r1 - r0) * u); }
    }
    var n = pts.length;
    function mid(i) { return { x: (pts[i].x + pts[i + 1].x) / 2, y: (pts[i].y + pts[i + 1].y) / 2, r: (r[i] + r[i + 1]) / 2 }; }
    var a = mid(0);
    line(pts[0].x, pts[0].y, r[0], a.x, a.y, a.r);
    for (var i = 1; i < n - 1; i++) {
      var c = pts[i], b = mid(i);
      var approx = Math.hypot(c.x - a.x, c.y - a.y) + Math.hypot(b.x - c.x, b.y - c.y);
      var steps = Math.max(1, Math.ceil(approx / SAMPLE_SPACING));
      for (var s = 1; s <= steps; s++) {
        var u = s / steps, w = 1 - u;
        emit(w * w * a.x + 2 * w * u * c.x + u * u * b.x, w * w * a.y + 2 * w * u * c.y + u * u * b.y,
             w * w * a.r + 2 * w * u * r[i] + u * u * b.r);
      }
      a = b;
    }
    line(a.x, a.y, a.r, pts[n - 1].x, pts[n - 1].y, r[n - 1]);
    end();
    ctx.restore();
  }

  /* ---------------- brushes (from ink-canvas.tsx) ---------------- */
  var PEN_WIDTH_SCALE = 0.54;
  function penEasing(t) { return (t * 0.65 + Math.sin((t * Math.PI) / 2) * 0.35) * PEN_WIDTH_SCALE; }
  var PEN = { size: 4.6, thinning: 0.62, streamline: 0.62, simulatePressure: false, easing: penEasing };
  var HI = { size: 18, thinning: 0, streamline: 0.35, simulatePressure: false, easing: function () { return 0.5; } };
  var PEN_PRESSURE_BOOST = 1.25, MIN_PEN_PRESSURE = 0.025, MOUSE_PRESSURE = 0.5, PEN_MIN_STEP = 1;
  var useCoalesced = !/iPad|iPhone|iPod/.test(navigator.userAgent) &&
    !(navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);

  var COLORS = [
    { n: "Black", v: "#111111" }, { n: "Blue", v: "#2b4cff" }, { n: "Red", v: "#dc2626" }, { n: "Green", v: "#15803d" },
    { n: "Yellow highlighter", v: "#ffd400", hi: 1 }, { n: "Green highlighter", v: "#3ddc84", hi: 1 }, { n: "Pink highlighter", v: "#ff6fb5", hi: 1 }
  ];

  /* ---------------- page layout + state ----------------
     The ink is painted on canvas TILES that sit inside the page (position:absolute), so they scroll
     with the text natively, in the same frame. (A fixed canvas repainted on scroll lags one frame
     behind and looks like parallax.) Only tiles near the screen exist; the rest are dropped.
     Each stroke is stored relative to the chapter <section> it starts in: x in the column's units
     (scaled when the column width changes), y from the section top. So opening a Q&A or a new
     layout moves the ink together with its chapter. */
  var col = document.querySelector("main .col") || document.body;
  var secs = [].slice.call(document.querySelectorAll("main section[id]"));
  var L = { left: 0, w: 1, tops: {}, docW: 1, docH: 1 };
  function measure() {
    var sx = window.scrollX, sy = window.scrollY, r = col.getBoundingClientRect();
    L.left = r.left + sx; L.w = Math.max(1, col.clientWidth);
    L.tops = {};
    secs.forEach(function (s) { L.tops[s.id] = s.getBoundingClientRect().top + sy; });
    L.docW = document.documentElement.clientWidth;
    L.docH = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
  }
  function topOf(s) { return s.a && L.tops[s.a] != null ? L.tops[s.a] : 0; }
  function sectionAt(pageY) {
    var best = null, bt = -1e9;
    secs.forEach(function (s) { var t = L.tops[s.id]; if (t <= pageY && t > bt) { bt = t; best = s.id; } });
    return best;
  }

  var strokes = [], undo = [], current = null, activePointer = null, lastKept = null, erasing = false, erased = [];
  var state = { on: false, color: COLORS[0].v, hi: false, eraser: false, touchDraws: false, hidden: false };
  try { var sv = JSON.parse(localStorage.getItem(KEY) || "null"); if (sv && sv.strokes) strokes = sv.strokes; if (sv && sv.touchDraws) state.touchDraws = true; } catch (e) {}

  var saveT = 0;
  function save() {
    clearTimeout(saveT);
    saveT = setTimeout(function () {
      try { localStorage.setItem(KEY, JSON.stringify({ v: 2, touchDraws: state.touchDraws, strokes: strokes })); } catch (e) {}
    }, 400);
  }

  /* ---------------- painting ---------------- */
  var TILE = 512;
  var layer = document.createElement("div");
  layer.id = "inkl"; layer.setAttribute("aria-hidden", "true");
  var live = document.createElement("canvas"), lctx = live.getContext("2d"), liveTop = 0;
  live.className = "inkt"; live.style.display = "none";
  layer.appendChild(live);
  var tmp = document.createElement("canvas"), tctx = tmp.getContext("2d");
  var tiles = {}, dpr = 1, frame = 0;

  // Paint one stroke onto canvas context c, whose top edge is at page y = top.
  function paint(c, s, top, done) {
    var k = L.w / s.w, ox = L.left, oy = topOf(s) - top;
    var pts = s.pts.map(function (q) { return { x: ox + q[0] * k, y: oy + q[1], p: s.pen && s.flat ? MOUSE_PRESSURE : q[2] }; });
    if (s.hi) {
      var cv = c.canvas;
      if (tmp.width !== cv.width || tmp.height !== cv.height) { tmp.width = cv.width; tmp.height = cv.height; }
      tctx.setTransform(1, 0, 0, 1, 0, 0); tctx.clearRect(0, 0, tmp.width, tmp.height);
      tctx.setTransform(dpr, 0, 0, dpr, 0, 0); tctx.fillStyle = s.c;
      paintStroke(tctx, pts, HI, done);
      c.save(); c.setTransform(1, 0, 0, 1, 0, 0); c.globalAlpha = 0.4; c.drawImage(tmp, 0, 0); c.restore();
    } else {
      c.setTransform(dpr, 0, 0, dpr, 0, 0); c.fillStyle = s.c;
      paintStroke(c, pts, PEN, done);
    }
  }
  function yRange(s) { var t = topOf(s); return [t + s.b[1], t + s.b[3]]; }

  function paintTile(t) {
    t.ctx.setTransform(1, 0, 0, 1, 0, 0); t.ctx.clearRect(0, 0, t.c.width, t.c.height);
    if (state.hidden) return;
    strokes.forEach(function (s) { var y = yRange(s); if (y[1] > t.top && y[0] < t.top + t.h) paint(t.ctx, s, t.top, true); });
  }
  function dropTile(i) { var t = tiles[i]; t.c.width = t.c.height = 0; t.c.remove(); delete tiles[i]; }
  function makeTile(i) {
    var top = i * TILE, h = Math.min(TILE, L.docH - top);
    if (h <= 0) return;
    var c = document.createElement("canvas");
    c.className = "inkt";
    c.style.top = top + "px"; c.style.width = L.docW + "px"; c.style.height = h + "px";
    c.width = Math.max(1, Math.round(L.docW * dpr)); c.height = Math.max(1, Math.round(h * dpr));
    var t = tiles[i] = { c: c, ctx: c.getContext("2d"), top: top, h: h };
    layer.appendChild(c); paintTile(t);
  }
  // Keep tiles from one screen above to two screens below the view; drop the rest.
  function ensureTiles() {
    var vh = window.innerHeight, sy = window.scrollY, last = Math.ceil(L.docH / TILE) - 1;
    var lo = Math.max(0, Math.floor((sy - vh) / TILE)), hi = Math.min(last, Math.floor((sy + 2 * vh) / TILE));
    Object.keys(tiles).forEach(function (i) { if (i < lo - 1 || i > hi + 1) dropTile(i); });
    for (var i = lo; i <= hi; i++) if (!tiles[i]) makeTile(i);
  }
  function repaintAll() { Object.keys(tiles).forEach(function (i) { paintTile(tiles[i]); }); }
  function rebuild() {
    dpr = window.devicePixelRatio || 1;
    Object.keys(tiles).forEach(dropTile);
    measure(); ensureTiles();
  }

  function renderLive() {
    frame = 0;
    lctx.setTransform(1, 0, 0, 1, 0, 0); lctx.clearRect(0, 0, live.width, live.height);
    if (current) paint(lctx, current.s, liveTop, false);
  }
  function request() { if (!frame) frame = requestAnimationFrame(renderLive); }
  // The stroke being drawn goes on its own canvas covering the screen at pen-down time.
  function startLive() {
    var h = Math.max(1, Math.min(window.innerHeight, L.docH - window.scrollY));
    liveTop = window.scrollY;
    live.style.top = liveTop + "px"; live.style.width = L.docW + "px"; live.style.height = h + "px";
    live.width = Math.round(L.docW * dpr); live.height = Math.round(h * dpr);
    live.style.display = "block";
  }
  function stopLive() { live.style.display = "none"; live.width = live.height = 1; }

  /* ---------------- drawing input (from ink-canvas.tsx) ---------------- */
  var input = document.createElement("div");
  input.id = "inki"; input.setAttribute("aria-hidden", "true");

  function pageOf(e, isPen, s) {
    var k = L.w / s.w;
    return [Math.round(((e.clientX + window.scrollX - L.left) / k) * 10) / 10,
      Math.round((e.clientY + window.scrollY - topOf(s)) * 10) / 10,
      isPen ? Math.round(Math.min(1, Math.max(MIN_PEN_PRESSURE, e.pressure * PEN_PRESSURE_BOOST)) * 1000) / 1000 : MOUSE_PRESSURE];
  }
  function notePressure(cur, raw) {
    if (!cur.s.pen || raw === 0) return;
    if (cur.first === null) cur.first = raw; else if (raw !== cur.first) cur.s.flat = false;
  }
  function addPoint(cur, pt) {
    var pts = cur.s.pts;
    if (cur.s.pen && lastKept && Math.hypot(pt[0] - lastKept[0], pt[1] - lastKept[1]) < PEN_MIN_STEP) { pts[pts.length - 1] = pt; return; }
    var prev = pts[pts.length - 1];
    if (prev && prev[0] === pt[0] && prev[1] === pt[1] && prev[2] === pt[2]) return;
    pts.push(pt); lastKept = pt;
  }
  function bbox(pts, pad) {
    var x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    pts.forEach(function (q) { x0 = Math.min(x0, q[0]); y0 = Math.min(y0, q[1]); x1 = Math.max(x1, q[0]); y1 = Math.max(y1, q[1]); });
    return [x0 - pad, y0 - pad, x1 + pad, y1 + pad];
  }

  // Stroke eraser: remove every stroke that has a point near the pen.
  function eraseAt(e) {
    var px = e.clientX + window.scrollX, py = e.clientY + window.scrollY, R = 14, hit = [];
    strokes.forEach(function (s) {
      var k = L.w / s.w, X = (px - L.left) / k, Y = py - topOf(s);
      if (X < s.b[0] - R || X > s.b[2] + R || Y < s.b[1] - R || Y > s.b[3] + R) return;
      var r2 = Math.pow(R / k + (s.hi ? 9 : 2), 2);
      for (var i = 0; i < s.pts.length; i++) {
        var dx = s.pts[i][0] - X, dy = s.pts[i][1] - Y;
        if (dx * dx + dy * dy <= r2) { hit.push(s); return; }
      }
    });
    if (hit.length) { strokes = strokes.filter(function (s) { return hit.indexOf(s) < 0; }); erased = erased.concat(hit); repaintAll(); }
  }

  function onDown(e) {
    if (!state.on) return;
    if (e.pointerType === "mouse" && e.button !== 0 && e.button !== 5) return;
    if (e.pointerType === "touch" && !state.touchDraws) return;
    if (activePointer !== null) endStroke(null);
    e.preventDefault();
    try { input.setPointerCapture(e.pointerId); } catch (x) {}
    activePointer = e.pointerId;
    var isPen = e.pointerType === "pen";
    // The flipped (eraser) end of a pen reports button 5 / buttons bit 32.
    erasing = state.eraser || e.button === 5 || (e.buttons & 32) === 32;
    if (erasing) { erased = []; eraseAt(e); return; }
    var s = { c: state.color, hi: state.hi ? 1 : 0, pen: isPen, flat: true, w: L.w, a: sectionAt(e.clientY + window.scrollY), pts: [], b: null };
    current = { first: null, s: s };
    s.pts.push(pageOf(e, isPen, s));
    notePressure(current, e.pressure);
    lastKept = s.pts[0];
    startLive(); request();
  }
  function onMove(e) {
    if (e.pointerId !== activePointer) return;
    if ((e.buttons & 33) === 0 && e.pointerType !== "touch") { endStroke(null); return; }   // release was missed
    if (erasing) { eraseAt(e); return; }
    if (!current) return;
    var evs = (useCoalesced && e.getCoalescedEvents && e.getCoalescedEvents()) || [];
    (evs.length ? evs : [e]).forEach(function (ev) { notePressure(current, ev.pressure); addPoint(current, pageOf(ev, current.s.pen, current.s)); });
    request();
  }
  function endStroke() {
    activePointer = null;
    if (erasing) {
      erasing = false;
      if (erased.length) { undo.push({ t: "erase", list: erased }); save(); }
      erased = []; return;
    }
    if (current) {
      var s = current.s;
      s.b = bbox(s.pts, s.hi ? 12 : 6);
      strokes.push(s); undo.push({ t: "add", s: s }); current = null;
      var y = yRange(s);
      Object.keys(tiles).forEach(function (i) { var t = tiles[i]; if (y[1] > t.top && y[0] < t.top + t.h && !state.hidden) paint(t.ctx, s, t.top, true); });
      save();
    }
    stopLive();
  }
  function onUp(e) { if (e.pointerId === activePointer) endStroke(); }

  function doUndo() {
    var a = undo.pop(); if (!a) return;
    if (a.t === "add") strokes = strokes.filter(function (s) { return s !== a.s; });
    else strokes = strokes.concat(a.list);
    repaintAll(); save();
  }
  function doClear() {
    if (!strokes.length) return;
    undo.push({ t: "erase", list: strokes }); strokes = []; repaintAll(); save();
  }

  /* ---------------- toolbar: a rail on the right edge ---------------- */
  var I = {
    pen: '<path d="M4 20l1.2-4.6L15.8 4.8a1.7 1.7 0 0 1 2.4 0l1 1a1.7 1.7 0 0 1 0 2.4L8.6 18.8z"/><path d="M14 6.6l3.4 3.4"/>',
    erase: '<path d="M8.5 19.5L3.8 14.8a1.6 1.6 0 0 1 0-2.3L12.5 3.8a1.6 1.6 0 0 1 2.3 0l5.4 5.4a1.6 1.6 0 0 1 0 2.3l-8 8z"/><path d="M8 9l7 7M8.5 19.5H20"/>',
    undo: '<path d="M9 14L4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 0 12h-3"/>',
    hand: '<path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M11 10.5V4a1.5 1.5 0 0 1 3 0v6.5"/><path d="M14 10.5V5.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-.5a6 6 0 0 1-4.8-2.4L3 15.5a1.6 1.6 0 0 1 2.5-2L8 15"/>',
    eye: '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    eyeoff: '<path d="M3 3l18 18"/><path d="M10.6 5.1A10 10 0 0 1 12 5c6.4 0 10 7 10 7a17 17 0 0 1-3 3.8M6.6 6.6A17 17 0 0 0 2 12s3.6 7 10 7a9.5 9.5 0 0 0 5.4-1.6"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>',
    trash: '<path d="M4 7h16M10 11v6M14 11v6"/><path d="M6 7l1 13h10l1-13M9 7V4h6v3"/>',
    close: '<path d="M6 6l12 12M18 6L6 18"/>'
  };
  function ic(n) { return '<svg viewBox="0 0 24 24" aria-hidden="true">' + I[n] + "</svg>"; }
  function tool(id, icon, label, title) {
    return '<button type="button" class="itool" id="' + id + '" title="' + title + '">' + ic(icon) + '<span class="il">' + label + "</span></button>";
  }

  var bar = document.createElement("div");
  bar.id = "ink"; bar.setAttribute("role", "toolbar"); bar.setAttribute("aria-label", "Drawing tools"); bar.setAttribute("aria-orientation", "vertical");
  var pens = COLORS.filter(function (c) { return !c.hi; }), his = COLORS.filter(function (c) { return c.hi; });
  function sw(list) {
    return list.map(function (c) {
      var i = COLORS.indexOf(c);
      return '<button type="button" class="isw' + (c.hi ? " hi" : "") + '" data-c="' + i + '" aria-label="' + c.n + '" title="' + c.n + '" style="--sw:' + c.v + '"></button>';
    }).join("");
  }
  bar.innerHTML =
    '<button type="button" id="inkon" class="itab" aria-pressed="false" title="Draw on the page (D)">' + ic("pen") + '<span class="iv">Draw · D</span></button>' +
    '<div class="ipanel" id="inkpanel">' +
      '<div class="ihead"><span class="ik">Ink</span><button type="button" class="ix" id="inkoff" title="Stop drawing (D)" aria-label="Stop drawing">' + ic("close") + "</button></div>" +
      '<div class="ig"><span class="ik">Pen</span><div class="isws">' + sw(pens) + "</div></div>" +
      '<div class="ig"><span class="ik">Mark</span><div class="isws">' + sw(his) + "</div></div>" +
      '<div class="ig itools">' +
        tool("inker", "erase", "Erase", "Erase whole strokes (E). The back end of a pen erases too.") +
        tool("inkun", "undo", "Undo", "Undo (Ctrl/Cmd+Z)") +
        tool("inktc", "hand", "Finger", "Pen and mouse always draw. Choose whether a finger scrolls or draws.") +
        tool("inkhd", "eye", "Hide", "Hide or show the ink") +
        tool("inkcl", "trash", "Clear", "Erase every drawing on this page") +
      "</div>" +
    "</div>";
  var $ = function (id) { return bar.querySelector("#" + id); };

  function sync() {
    document.body.classList.toggle("drawing", state.on);
    bar.classList.toggle("open", state.on);
    $("inkon").setAttribute("aria-pressed", state.on);
    $("inker").setAttribute("aria-pressed", state.eraser);
    $("inktc").setAttribute("aria-pressed", state.touchDraws);
    $("inktc").querySelector(".il").textContent = state.touchDraws ? "Finger ✎" : "Finger ↕";
    $("inkhd").setAttribute("aria-pressed", state.hidden);
    $("inkhd").innerHTML = ic(state.hidden ? "eyeoff" : "eye") + '<span class="il">' + (state.hidden ? "Show" : "Hide") + "</span>";
    [].forEach.call(bar.querySelectorAll(".isw"), function (b) {
      b.setAttribute("aria-pressed", !state.eraser && COLORS[+b.dataset.c].v === state.color);
    });
    input.style.pointerEvents = state.on ? "auto" : "none";
    input.style.touchAction = state.touchDraws ? "none" : "pan-y";
    input.style.cursor = state.on ? (state.eraser ? "cell" : "crosshair") : "";
  }
  bar.addEventListener("click", function (e) {
    var b = e.target.closest("button"); if (!b) return;
    if (b.classList.contains("isw")) { var c = COLORS[+b.dataset.c]; state.color = c.v; state.hi = !!c.hi; state.eraser = false; }
    else if (b.id === "inkon") { state.on = true; if (state.hidden) { state.hidden = false; repaintAll(); } }
    else if (b.id === "inkoff") state.on = false;
    else if (b.id === "inker") state.eraser = !state.eraser;
    else if (b.id === "inkun") doUndo();
    else if (b.id === "inkcl") doClear();
    else if (b.id === "inktc") { state.touchDraws = !state.touchDraws; save(); }
    else if (b.id === "inkhd") { state.hidden = !state.hidden; repaintAll(); }
    sync();
  });
  window.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) {
      if ((e.key === "z" || e.key === "Z") && state.on && !e.shiftKey) { e.preventDefault(); doUndo(); }
      return;
    }
    if (e.repeat || /input|textarea|select/i.test((e.target && e.target.tagName) || "")) return;
    var k = e.key.toLowerCase();
    if (k === "d") { state.on = !state.on; if (state.on && state.hidden) { state.hidden = false; repaintAll(); } sync(); }
    else if (k === "e" && state.on) { state.eraser = !state.eraser; sync(); }
  });

  /* ---------------- wire up ---------------- */
  document.body.appendChild(layer);
  document.body.appendChild(input);
  document.body.appendChild(bar);
  rebuild(); sync();
  var rT = 0;
  function relayout() { clearTimeout(rT); rT = setTimeout(rebuild, 120); }
  window.addEventListener("resize", relayout);
  // Page height changes (a Q&A opened, fonts arrived) move the chapters: re-measure and repaint.
  if (window.ResizeObserver) new ResizeObserver(relayout).observe(document.querySelector("main") || document.body);
  window.addEventListener("load", relayout);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(relayout);
  var sT = false;
  window.addEventListener("scroll", function () { if (!sT) { sT = true; requestAnimationFrame(function () { sT = false; ensureTiles(); }); } }, { passive: true });
  window.addEventListener("blur", function () { if (activePointer !== null) endStroke(); });
  input.addEventListener("pointerdown", onDown);
  // Moves and releases are heard on the whole window: pointer capture can be lost just before the
  // pen lifts (seen with UGEE tablets at the window edge) and the stroke would stay stuck.
  window.addEventListener("pointermove", onMove);
  window.addEventListener("pointerup", onUp);
  window.addEventListener("pointercancel", onUp);
})();
