/* Pen scrolling for the whole study site (added 26 Nov 2026).
   A pen (stylus, drawing tablet) dragged over empty space scrolls the page up and down like a hand; over text, a link, a button
   or any control it behaves as before (select, click). Mouse and finger are untouched. Off while a page's draw mode is on.
   One small file, loaded by every page and injected by the hub into the pages it opens. */
(function () {
  if (window.__penScroll) return; window.__penScroll = 1;
  var TAP = 6;                                   /* px of movement before a press becomes a scroll */
  var CONTROL = 'a[href],button,input,select,textarea,summary,label,option,video,audio,canvas,iframe,[role="button"],[role="link"],[role="tab"],[contenteditable=""],[contenteditable="true"],[tabindex]:not([tabindex="-1"]),[data-pen="off"]';
  var st = null, raf = 0;

  function overGlyph(x, y) {                     /* is the pen tip on a line of text (letters or the spaces between them)? */
    var n = null, o = 0, p, r;
    if (document.caretPositionFromPoint) { p = document.caretPositionFromPoint(x, y); if (p) { n = p.offsetNode; o = p.offset; } }
    else if (document.caretRangeFromPoint) { r = document.caretRangeFromPoint(x, y); if (r) { n = r.startContainer; o = r.startOffset; } }
    if (!n || n.nodeType !== 3) return false;
    var len = n.nodeValue.length, rg = document.createRange();
    for (var i = Math.max(0, o - 1); i <= Math.min(len - 1, o); i++) {
      rg.setStart(n, i); rg.setEnd(n, i + 1);
      var rs = rg.getClientRects();
      for (var k = 0; k < rs.length; k++) { var q = rs[k]; if (x >= q.left - 1 && x <= q.right + 1 && y >= q.top - 1 && y <= q.bottom + 1) return true; }
    }
    return false;
  }
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
  function fling(box, v) {                       /* a little glide after the pen lifts */
    cancelAnimationFrame(raf); var last = performance.now();
    (function step(t) {
      var dt = t - last; last = t; go(box, box.scrollTop + v * dt); v *= Math.pow(0.0035, dt / 1000);
      if (Math.abs(v) > 0.02) raf = requestAnimationFrame(step);
    })(last);
  }

  document.addEventListener("pointerdown", function (e) {
    cancelAnimationFrame(raf);
    if (e.pointerType !== "pen" || e.button !== 0 || e.defaultPrevented || !e.isPrimary) return;
    if (document.body && document.body.classList.contains("drawing")) return;
    var t = e.target; if (!t || t.nodeType !== 1) return;
    if (t.closest && t.closest(CONTROL)) return;
    if (overGlyph(e.clientX, e.clientY)) return;
    st = { id: e.pointerId, y: e.clientY, y0: e.clientY, x0: e.clientX, box: scroller(t), going: false, t: performance.now(), v: 0 };
  }, false);

  document.addEventListener("pointermove", function (e) {
    if (!st || e.pointerId !== st.id) return;
    if (e.buttons === 0) { st = null; return; }                       /* the release was missed */
    if (!st.going) {
      if (Math.abs(e.clientY - st.y0) < TAP && Math.abs(e.clientX - st.x0) < TAP) return;
      st.going = true; lock(true, st);
    }
    var dy = e.clientY - st.y, now = performance.now(), dt = Math.max(1, now - st.t);
    go(st.box, st.box.scrollTop - dy); st.y = e.clientY;
    st.v = 0.8 * st.v + 0.2 * (-dy / dt); st.t = now;
    e.preventDefault();
  }, { passive: false });

  function end(e) {
    if (!st || e.pointerId !== st.id) return;
    var s = st; st = null;
    if (s.going) {
      lock(false, s);
      if (e.type === "pointerup") { window.__penClickBlock = 1; setTimeout(function () { window.__penClickBlock = 0; }, 60); }
      if (e.type === "pointerup" && Math.abs(s.v) > 0.15 && performance.now() - s.t < 90) fling(s.box, s.v);
    }
  }
  document.addEventListener("pointerup", end, false);
  document.addEventListener("pointercancel", end, false);
  /* the drag must not turn into a click on whatever lies under the pen when it lifts */
  document.addEventListener("click", function (e) { if (window.__penClickBlock) { window.__penClickBlock = 0; e.preventDefault(); e.stopPropagation(); } }, true);
})();
