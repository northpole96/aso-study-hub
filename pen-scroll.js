/* Pen scrolling for the whole study site (v5, 26 Nov 2026).
   A pen (stylus, drawing tablet) dragged anywhere on a page scrolls it up and down like a hand: over empty space, text, links and
   buttons. A tap still clicks or places the cursor. A flick keeps the page gliding and it slows down smoothly.
   Not touched: form fields, canvases, video, [data-pen="off"], Shift+drag (selects text), the pen's side button, finger. Off in draw mode.

   Why v5. Chrome on a Mac learns that the pointer is a pen only from the tablet's "proximity" message, sent when the pen comes into
   range or when the browser becomes the active app again. A page that is reloaded while the pen hovers starts out believing the pen is
   a mouse (pointerType "mouse") until the next such message: that is the "does not work after refresh, works after switching apps and
   back" the user saw. So once this browser has seen a real pen (remembered in localStorage "aso-pen-seen"), a left-button drag that
   Chrome calls "mouse" is treated as the pen too. Side effect: a mouse or trackpad click-drag also scrolls instead of selecting; Shift+drag
   or a double click still selects. Turn that part off with ?penmouse=0 (back on with ?penmouse=1).
   Diagnosis: ?pendebug=1 shows a badge at the bottom left (?pendebug=0 hides it). */
(function () {
  if (window.__penScroll) return; window.__penScroll = 5;
  var TAP = 6;                                    /* px of movement before a press becomes a scroll */
  var CONTROL = 'input,select,textarea,option,video,audio,canvas,iframe,[contenteditable=""],[contenteditable="true"],[data-pen="off"]';
  var TAU = 325, VMAX = 4.5, VMIN = 0.01;          /* glide: speed fades by 1/e every 325 ms; speeds in px per ms */
  var root = document.documentElement, st = null, fl = 0, locked = null;

  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  var q = /[?&]pendebug=(\d)/.exec(location.search); if (q) ls("aso-pen-debug", q[1]);
  q = /[?&]penmouse=(\d)/.exec(location.search); if (q) ls("aso-pen-mouse", q[1]);
  var dbg = ls("aso-pen-debug") === "1";
  var penSeen = ls("aso-pen-seen") === "1", mouseAsPen = ls("aso-pen-mouse") !== "0";

  var dn = 0;
  function say(msg, e) {
    if (!dbg) return;
    var b = document.getElementById("pen-debug");
    if (!b) {
      b = document.createElement("div"); b.id = "pen-debug";
      b.style.cssText = "position:fixed;left:8px;bottom:8px;z-index:2147483647;background:#111;color:#fff;font:11px/1.45 ui-monospace,Menlo,monospace;padding:5px 9px;max-width:86vw;pointer-events:none;opacity:.92;white-space:pre-wrap";
      (document.body || root).appendChild(b);
    }
    b.textContent = "pen-scroll v5 · #" + (++dn) + " · pointer: " + (e ? e.pointerType : "-") + (e && e.pointerType === "pen" ? " · pressure " + (e.pressure || 0).toFixed(2) : "") +
      "\npen seen in this browser: " + (penSeen ? "yes" : "no") + " · mouse drags as pen: " + (penSeen && mouseAsPen ? "on" : "off") + "\n" + msg;
  }
  function learn(e) { if (e.pointerType === "pen" && !penSeen) { penSeen = true; ls("aso-pen-seen", "1"); say("a pen was seen; remembered", e); } }
  document.addEventListener("pointermove", learn, true);
  document.addEventListener("pointerover", learn, true);

  /* ---------- scrolling helpers ---------- */
  function chain(el) {                            /* every box under the pen that can scroll up and down, innermost first */
    var list = [];
    for (; el && el !== document.body && el !== root; el = el.parentElement) {
      var oy = getComputedStyle(el).overflowY;
      if ((oy === "auto" || oy === "scroll" || oy === "overlay") && el.scrollHeight > el.clientHeight + 1) list.push(el);
    }
    if (document.body && document.body.scrollHeight > document.body.clientHeight + 1) list.push(document.body);
    list.push(document.scrollingElement || root);
    return list;
  }
  function go(box, top) { try { box.scrollTo({ top: top, behavior: "instant" }); } catch (e) { box.scrollTop = top; } }
  function canMove(list, d) {                     /* which box would move for a push of d (d > 0 = content goes up) */
    for (var i = 0; i < list.length; i++) {
      var b = list[i], m = b.scrollHeight - b.clientHeight;
      if ((d > 0 && b.scrollTop < m - 0.5) || (d < 0 && b.scrollTop > 0.5)) return b;
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

  /* ---------- the glide after a flick ---------- */
  function stopFling() { if (fl) { cancelAnimationFrame(fl); fl = 0; } }
  function fling(box, v) {
    stopFling();
    var pos = box.scrollTop, last = performance.now();
    v = Math.max(-VMAX, Math.min(VMAX, v));
    function step(t) {
      var dt = Math.min(40, Math.max(0, t - last)); last = t;
      pos += v * dt; v *= Math.exp(-dt / TAU);
      var m = Math.max(0, box.scrollHeight - box.clientHeight), hit = pos <= 0 || pos >= m;
      pos = Math.max(0, Math.min(m, pos)); go(box, Math.round(pos * 2) / 2);
      fl = (!hit && Math.abs(v) > VMIN) ? requestAnimationFrame(step) : 0;
    }
    fl = requestAnimationFrame(step);
  }
  ["wheel", "keydown", "touchstart"].forEach(function (n) { document.addEventListener(n, stopFling, { passive: true, capture: true }); });

  /* ---------- the drag: pen moves are gathered and applied once per frame, so the page moves smoothly ---------- */
  var pend = 0, frame = 0;
  function flush() {
    frame = 0; if (!st || !pend) return;
    var d = pend; pend = 0;
    var b = canMove(st.list, d) || st.box;
    if (b) { go(b, b.scrollTop + d); st.box = b; }
  }
  function release(o) {                          /* st is already cleared when this runs, so a late lostpointercapture is ignored */
    lock(false); pend = 0; if (frame) { cancelAnimationFrame(frame); frame = 0; }
    if (o && o.cap) { o.cap = false; try { root.releasePointerCapture(o.id); } catch (e) {} }
  }
  function drop() { var o = st; st = null; release(o); }
  window.addEventListener("blur", function () { if (st) drop(); });

  document.addEventListener("pointerdown", function (e) {
    stopFling();
    if (st) drop();
    var why = null, asMouse = false;
    if (e.pointerType === "pen") learn(e);
    else if (e.pointerType === "mouse" && penSeen && mouseAsPen) asMouse = true;
    else why = e.pointerType === "mouse" ? (penSeen ? "mouse drags as pen are off (?penmouse=1)" : "Chrome says mouse and no pen has been seen in this browser yet: move the pen out of range and back once")
                                         : "not a pen ('" + e.pointerType + "')";
    if (!why && e.button !== 0) why = "side button / eraser / right click (button " + e.button + ")";
    if (!why && e.defaultPrevented) why = "the page handled the press itself";
    if (!why && !e.isPrimary) why = "second pointer";
    if (!why && document.body && document.body.classList.contains("drawing")) why = "draw mode is on";
    if (!why && (e.shiftKey || e.altKey || e.metaKey || e.ctrlKey)) why = "a modifier key is held (Shift = select text)";
    var t = e.target;
    if (!why && (!t || t.nodeType !== 1)) why = "no element";
    if (!why && t.closest && t.closest(CONTROL)) why = "on a form field, canvas or video";
    if (why) { say("ignored: " + why, e); return; }
    st = { id: e.pointerId, y: e.clientY, y0: e.clientY, x0: e.clientX, list: chain(t), box: null, going: false, s: [{ t: e.timeStamp, y: e.clientY }], cap: false, mouse: asMouse };
    say("armed" + (asMouse ? " (Chrome calls it a mouse; treated as the pen)" : "") + ": drag to scroll", e);
  }, false);

  document.addEventListener("pointermove", function (e) {
    if (!st || e.pointerId !== st.id) return;
    if (!(e.buttons & 1)) { drop(); return; }          /* the tip is up: the release was missed */
    if (!st.going) {
      if (Math.abs(e.clientY - st.y0) < TAP && Math.abs(e.clientX - st.x0) < TAP) return;
      st.box = canMove(st.list, st.y0 - e.clientY);
      if (!st.box) { say("nothing here can scroll that way: left alone", e); st = null; return; }
      st.going = true; lock(true);
      try { root.setPointerCapture(e.pointerId); st.cap = true; } catch (x) {}
      st.y = st.y0;                                                    /* count the first few px too, so the page keeps up with the pen */
      say("scrolling", e);
    }
    var evs = (e.getCoalescedEvents && e.getCoalescedEvents()) || []; if (!evs.length) evs = [e];
    for (var i = 0; i < evs.length; i++) st.s.push({ t: evs[i].timeStamp || e.timeStamp, y: evs[i].clientY });
    while (st.s.length > 3 && e.timeStamp - st.s[0].t > 150) st.s.shift();
    pend += st.y - e.clientY; st.y = e.clientY; st.lastT = e.timeStamp;
    if (!frame) frame = requestAnimationFrame(flush);
    e.preventDefault();
  }, { passive: false });

  function speed(s, tEnd) {                         /* px per ms over the last stretch of the stroke; picks the faster of two windows */
    function over(win) {
      var i = s.length - 1; if (i < 1) return 0;
      var j = i; while (j > 0 && s[i].t - s[j - 1].t <= win) j--;
      var dt = s[i].t - s[j].t; return dt >= 8 ? (s[j].y - s[i].y) / dt : 0;
    }
    var a = over(60), b = over(130);
    return Math.abs(a) > Math.abs(b) ? a : b;
  }
  function end(e) {
    if (!st || e.pointerId !== st.id) return;
    var s = st; if (s.going) flush(); st = null; release(s);
    if (!s.going) { say(e.type === "pointercancel" ? "cancelled before moving: the browser took the pen" : "tap (no scroll)", e); return; }
    if (e.type === "lostpointercapture") return;
    if (e.type === "pointerup") { window.__penClickBlock = 1; setTimeout(function () { window.__penClickBlock = 0; }, 80); }
    var gap = e.timeStamp - (s.lastT || 0), v = speed(s.s), note;
    if (e.type === "pointerup" && s.box && gap < 140 && Math.abs(v) > 0.08) { fling(s.box, v); note = "flick " + v.toFixed(2) + " px/ms → gliding"; }
    else note = "no glide (speed " + v.toFixed(2) + " px/ms, pen was still for " + Math.round(gap) + " ms before lifting)";
    say((e.type === "pointercancel" ? "cancelled by the browser · " : "lifted · ") + note, e);
  }
  document.addEventListener("dragstart", function (e) { if (st) e.preventDefault(); }, true);
  document.addEventListener("pointerup", end, false);
  document.addEventListener("pointercancel", end, false);
  document.addEventListener("lostpointercapture", end, false);
  /* after a drag, the lift must not click whatever lies under the pen */
  document.addEventListener("click", function (e) { if (window.__penClickBlock) { window.__penClickBlock = 0; e.preventDefault(); e.stopPropagation(); } }, true);
  if (dbg) say("ready: touch the page with the pen", null);
})();
