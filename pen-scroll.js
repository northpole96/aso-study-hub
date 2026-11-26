/* Pen scrolling for the whole study site (added 26 Nov 2026; widened to text and links the same day; made sturdier after "inconsistent").
   A pen (stylus, drawing tablet) dragged anywhere on a page scrolls it up and down like a hand: over empty space, over text, over a
   link or a button. A tap (press and lift without moving) still clicks or places the cursor as before. Not touched: form fields,
   canvases, video, anything marked data-pen="off", Shift+drag and the pen's side button (both still select text), mouse and finger.
   Off while a page's draw mode is on. One small file, loaded by every page and injected by the hub into the pages it opens.
   Diagnosis: open any page with ?pendebug=1 to get a small badge that says what the pen is doing (?pendebug=0 hides it). */
(function () {
  if (window.__penScroll) return; window.__penScroll = 1;
  var TAP = 6;                                   /* px of movement before a press becomes a scroll */
  var CONTROL = 'input,select,textarea,option,video,audio,canvas,iframe,[contenteditable=""],[contenteditable="true"],[data-pen="off"]';
  var TAU = 340, VMAX = 4, VMIN = 0.012;          /* glide: speed fades by 1/e every 340 ms; px per ms */
  var st = null, raf = 0, locked = null, root = document.documentElement;

  /* ---------- diagnosis badge ---------- */
  var dbg = null, dn = 0;
  try {
    var q = /[?&]pendebug=(\d)/.exec(location.search);
    if (q) localStorage.setItem("aso-pen-debug", q[1]);
    if (localStorage.getItem("aso-pen-debug") === "1") dbg = true;
  } catch (e) {}
  function say(msg, type) {
    if (!dbg) return;
    var b = document.getElementById("pen-debug");
    if (!b) {
      b = document.createElement("div"); b.id = "pen-debug";
      b.style.cssText = "position:fixed;left:8px;bottom:8px;z-index:2147483647;background:#111;color:#fff;font:11px/1.4 ui-monospace,Menlo,monospace;padding:5px 9px;max-width:80vw;pointer-events:none;opacity:.92;white-space:pre-wrap";
      (document.body || root).appendChild(b);
    }
    b.textContent = "pen-scroll v4 · #" + (++dn) + " · pointer: " + (type || "?") + "\n" + msg;
  }

  /* ---------- helpers ---------- */
  function chain(el) {                           /* everything that could scroll up and down under the pen, innermost first */
    var list = [];
    for (; el && el !== document.body && el !== root; el = el.parentElement) {
      var oy = getComputedStyle(el).overflowY;
      if ((oy === "auto" || oy === "scroll" || oy === "overlay") && el.scrollHeight > el.clientHeight + 1) list.push(el);
    }
    if (document.body && document.body.scrollHeight > document.body.clientHeight + 1) list.push(document.body);
    list.push(document.scrollingElement || root);
    return list;
  }
  function go(box, top) {                         /* straight to the spot, even where the page has scroll-behavior: smooth */
    try { box.scrollTo({ top: top, behavior: "instant" }); } catch (e) { box.scrollTop = top; }
  }
  function move(list, d) {                        /* d > 0 scrolls the content down; the first box that can move takes it */
    for (var i = 0; i < list.length; i++) {
      var b = list[i], before = b.scrollTop;
      go(b, before + d);
      if (b.scrollTop !== before) return b;
    }
    return null;
  }
  function lock(on) {                             /* while scrolling, nothing gets selected */
    var s = root.style;
    if (on && !locked) {
      locked = { a: s.userSelect, b: s.webkitUserSelect }; s.userSelect = s.webkitUserSelect = "none";
      var g = window.getSelection && getSelection(); if (g && g.removeAllRanges) g.removeAllRanges();
    } else if (!on && locked) { s.userSelect = locked.a || ""; s.webkitUserSelect = locked.b || ""; locked = null; }
  }
  function stopFling() { cancelAnimationFrame(raf); raf = 0; }
  function fling(box, v) {                        /* keep going after the pen lifts, slow down smoothly, stop at the ends */
    stopFling();
    var pos = box.scrollTop, last = performance.now();
    v = Math.max(-VMAX, Math.min(VMAX, v));
    (function step(t) {
      var dt = Math.min(48, t - last); last = t;
      pos += v * dt; v *= Math.exp(-dt / TAU);
      var m = Math.max(0, box.scrollHeight - box.clientHeight), hit = pos <= 0 || pos >= m;
      pos = Math.max(0, Math.min(m, pos)); go(box, pos);
      if (!hit && Math.abs(v) > VMIN) raf = requestAnimationFrame(step); else raf = 0;
    })(last);
  }
  function release() {                            /* leave no trace: unlock selection, let go of the pointer */
    lock(false);
    if (st && st.cap) { try { root.releasePointerCapture(st.id); } catch (e) {} }
  }
  ["wheel", "keydown", "touchstart"].forEach(function (n) { document.addEventListener(n, stopFling, { passive: true, capture: true }); });
  window.addEventListener("blur", function () { if (st) { release(); st = null; } });
  document.addEventListener("visibilitychange", function () { if (document.hidden && st) { release(); st = null; } });

  /* ---------- the gesture ---------- */
  document.addEventListener("pointerdown", function (e) {
    stopFling();
    if (st) { release(); st = null; }             /* a missed release from before: start clean */
    var why = null;
    if (e.pointerType !== "pen") why = "not a pen (this one is '" + e.pointerType + "')";
    else if (e.button !== 0) why = "side button / eraser (button " + e.button + ")";
    else if (e.defaultPrevented) why = "the page handled the press itself";
    else if (!e.isPrimary) why = "second pointer";
    else if (document.body && document.body.classList.contains("drawing")) why = "draw mode is on";
    else if (e.shiftKey) why = "Shift held (select text)";
    var t = e.target;
    if (!why && (!t || t.nodeType !== 1)) why = "no element";
    if (!why && t.closest && t.closest(CONTROL)) why = "on a form field, canvas or video";
    if (why) { say("ignored: " + why, e.pointerType); return; }
    st = { id: e.pointerId, y: e.clientY, y0: e.clientY, x0: e.clientX, list: chain(t), box: null, going: false, s: [], cap: false };
    say("armed: drag to scroll (" + st.list.length + " scroll area" + (st.list.length === 1 ? "" : "s") + " here)", e.pointerType);
  }, false);

  document.addEventListener("pointermove", function (e) {
    if (!st || e.pointerId !== st.id) return;
    if (!st.going) {
      if (Math.abs(e.clientY - st.y0) < TAP && Math.abs(e.clientX - st.x0) < TAP) return;
      st.going = true; lock(true);
      try { root.setPointerCapture(e.pointerId); st.cap = true; } catch (x) {}   /* keep every move and the lift, even over a frame */
      say("scrolling", e.pointerType);
    }
    var dy = e.clientY - st.y, now = performance.now();
    st.y = e.clientY;
    var b = move(st.list, -dy); if (b) st.box = b;
    st.s.push({ t: now, y: e.clientY });          /* the last 100 ms of the pen's path gives the flick speed */
    while (st.s.length > 2 && now - st.s[0].t > 100) st.s.shift();
    e.preventDefault();
  }, { passive: false });

  function end(e) {
    if (!st || e.pointerId !== st.id) return;
    var s = st; release(); st = null;
    if (!s.going) { say(e.type === "pointercancel" ? "cancelled before moving: the browser took the pen over" : "tap (no scroll)", e.pointerType); return; }
    if (e.type === "pointerup") { window.__penClickBlock = 1; setTimeout(function () { window.__penClickBlock = 0; }, 60); }
    var n = s.s.length, now = performance.now(), flick = "";
    if (e.type === "pointerup" && s.box && n > 1 && now - s.s[n - 1].t < 80) {   /* lifted while still moving = a flick */
      var span = s.s[n - 1].t - s.s[0].t;
      if (span > 8) { var v = -(s.s[n - 1].y - s.s[0].y) / span; if (Math.abs(v) > 0.1) { fling(s.box, v); flick = " · flick " + v.toFixed(2) + " px/ms"; } }
    }
    say((e.type === "pointercancel" ? "cancelled by the browser" : "lifted") + flick, e.pointerType);
  }
  document.addEventListener("dragstart", function (e) { if (st && st.going) e.preventDefault(); }, true);
  document.addEventListener("pointerup", end, false);
  document.addEventListener("pointercancel", end, false);
  document.addEventListener("lostpointercapture", end, false);
  /* the drag must not turn into a click on whatever lies under the pen when it lifts */
  document.addEventListener("click", function (e) { if (window.__penClickBlock) { window.__penClickBlock = 0; e.preventDefault(); e.stopPropagation(); } }, true);
  if (dbg) say("ready: touch the page with the pen", "-");
})();
