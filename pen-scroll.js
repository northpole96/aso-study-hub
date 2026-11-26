/* Pen scrolling for the whole study site (added 26 Nov 2026; widened the same day to text and links).
   A pen (stylus, drawing tablet) dragged anywhere on a page scrolls it up and down like a hand: over empty space, over text, over a
   link or a button. A tap (press and lift without moving) still clicks or places the cursor as before. Not touched: form fields,
   canvases, video, anything marked data-pen="off", Shift+drag and the pen's side button (both still select text), mouse and finger.
   Off while a page's draw mode is on. One small file, loaded by every page and injected by the hub into the pages it opens. */
(function () {
  if (window.__penScroll) return; window.__penScroll = 1;
  var TAP = 6;                                   /* px of movement before a press becomes a scroll */
  var CONTROL = 'input,select,textarea,option,video,audio,canvas,iframe,[contenteditable=""],[contenteditable="true"],[data-pen="off"]';
  var st = null, raf = 0;

  function scroller(el) {                        /* nearest ancestor that really scrolls up and down, else the page */
    for (; el && el !== document.body && el !== document.documentElement; el = el.parentElement) {
      var cs = getComputedStyle(el), oy = cs.overflowY;
      if ((oy === "auto" || oy === "scroll" || oy === "overlay") && el.scrollHeight > el.clientHeight + 1) return el;
    }
    return document.scrollingElement || document.documentElement;
  }
  function go(box, top) {                         /* straight to the spot, even where the page has scroll-behavior: smooth */
    try { box.scrollTo({ top: top, behavior: "instant" }); } catch (e) { box.scrollTop = top; }
  }
  function lock(on, o) {                          /* while scrolling, nothing gets selected */
    var s = document.documentElement.style;
    if (on) { o.prevSel = s.userSelect; o.prevWk = s.webkitUserSelect; s.userSelect = s.webkitUserSelect = "none"; var g = window.getSelection && getSelection(); if (g && g.removeAllRanges) g.removeAllRanges(); }
    else { s.userSelect = o.prevSel || ""; s.webkitUserSelect = o.prevWk || ""; }
  }
  var TAU = 340, VMAX = 4, VMIN = 0.012;          /* glide: speed fades by 1/e every 340 ms; px per ms */
  function stopFling() { cancelAnimationFrame(raf); raf = 0; }
  function fling(box, v) {                       /* keep going after the pen lifts, slow down smoothly, stop at the ends */
    stopFling();
    var pos = box.scrollTop, max = function () { return Math.max(0, box.scrollHeight - box.clientHeight); }, last = performance.now();
    v = Math.max(-VMAX, Math.min(VMAX, v));
    (function step(t) {
      var dt = Math.min(48, t - last); last = t;
      pos += v * dt; v *= Math.exp(-dt / TAU);
      var m = max(), hit = pos <= 0 || pos >= m;
      pos = Math.max(0, Math.min(m, pos)); go(box, pos);
      if (!hit && Math.abs(v) > VMIN) raf = requestAnimationFrame(step); else raf = 0;
    })(last);
  }
  ["wheel", "keydown", "touchstart"].forEach(function (n) { document.addEventListener(n, stopFling, { passive: true, capture: true }); });

  document.addEventListener("pointerdown", function (e) {
    stopFling();
    if (e.pointerType !== "pen" || e.button !== 0 || e.defaultPrevented || !e.isPrimary) return;
    if (document.body && document.body.classList.contains("drawing")) return;
    var t = e.target; if (!t || t.nodeType !== 1) return;
    if (t.closest && t.closest(CONTROL)) return;
    if (e.shiftKey) return;                                          /* Shift + drag = select text as usual */
    st = { id: e.pointerId, y: e.clientY, y0: e.clientY, x0: e.clientX, box: scroller(t), going: false, s: [] };
  }, false);

  document.addEventListener("pointermove", function (e) {
    if (!st || e.pointerId !== st.id) return;
    if (e.buttons === 0) { st = null; return; }                       /* the release was missed */
    if (!st.going) {
      if (Math.abs(e.clientY - st.y0) < TAP && Math.abs(e.clientX - st.x0) < TAP) return;
      st.going = true; lock(true, st);
    }
    var dy = e.clientY - st.y, now = performance.now();
    go(st.box, st.box.scrollTop - dy); st.y = e.clientY;
    st.s.push({ t: now, y: e.clientY });                              /* the last 100 ms of the pen's path gives the flick speed */
    while (st.s.length > 2 && now - st.s[0].t > 100) st.s.shift();
    e.preventDefault();
  }, { passive: false });

  function end(e) {
    if (!st || e.pointerId !== st.id) return;
    var s = st; st = null;
    if (s.going) {
      lock(false, s);
      if (e.type === "pointerup") { window.__penClickBlock = 1; setTimeout(function () { window.__penClickBlock = 0; }, 60); }
      var n = s.s.length, now = performance.now();
      if (e.type === "pointerup" && n > 1 && now - s.s[n - 1].t < 80) {   /* lifted while still moving = a flick */
        var span = s.s[n - 1].t - s.s[0].t;
        if (span > 8) { var v = -(s.s[n - 1].y - s.s[0].y) / span; if (Math.abs(v) > 0.1) fling(s.box, v); }
      }
    }
  }
  document.addEventListener("dragstart", function (e) { if (st) e.preventDefault(); }, true);
  document.addEventListener("pointerup", end, false);
  document.addEventListener("pointercancel", end, false);
  /* the drag must not turn into a click on whatever lies under the pen when it lifts */
  document.addEventListener("click", function (e) { if (window.__penClickBlock) { window.__penClickBlock = 0; e.preventDefault(); e.stopPropagation(); } }, true);
})();
