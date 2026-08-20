/* ═══════════════════════════════════════════════════════════════════
   elevation.js — the survey rail.

   The page is a section through a tower. Scrolling descends it; every
   element carrying data-elev docks at the elevation it names, and the
   instrument reads the real conditions at that height:

     static head    h x 0.0981                        bar
     stack pressure 3460 (1/To - 1/Ti) h              Pa
     wind speed     v10 (h/10)^0.14                   m/s

   Colours are read from the CSS tokens, so it follows the theme.
   Activates only on pages that contain .el-rail.
   ═══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var rail = document.querySelector('.el-rail');
  if (!rail) return;
  var cv = rail.querySelector('canvas');
  if (!cv || !cv.getContext) return;

  var $ = function (i) { return document.getElementById(i); };
  var ctx = cv.getContext('2d');
  var ROOT = document.documentElement;
  var BAR = 0.0981, TI = 22, ETA = 0.70, FLOOR = 4.2;
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var S = { H: 828, PN: 16, PM: 1.5, PF: 12, zd: 147.8, zf: 122.3, zg: 122.3, nz: 7,
            To: 5, elev: 828, tgt: 828, scale: 0.18, datumY: 320,
            anchors: [], run: false, idle: 0 };

  var pal = {};
  function readPal() {
    var c = getComputedStyle(ROOT);
    var g = function (n) { return c.getPropertyValue(n).trim(); };
    pal = { ink: g('--ink'), ink2: g('--ink-2'), ink3: g('--ink-3'),
            rule: g('--rule'), water: g('--water'), fire: g('--fire'),
            air: g('--air'), sheet: g('--sheet') };
  }
  function rgba(hex, a) {
    hex = (hex || '#000').replace('#', '');
    if (hex.length === 3) hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
    var n = parseInt(hex, 16);
    return 'rgba(' + ((n >> 16) & 255) + ',' + ((n >> 8) & 255) + ',' + (n & 255) + ',' + a + ')';
  }

  function staticBar(e) { return Math.max(0, e) * BAR; }
  function stackPa(e, To) { return 3460 * (1 / (To + 273.15) - 1 / (TI + 273.15)) * Math.max(0, e); }
  function windMs(e) { return 8 * Math.pow(Math.max(e, 10) / 10, 0.14); }
  function liftKWh(H) { return H / (367 * ETA); }

  function computeAnchors() {
    var els = [].slice.call(document.querySelectorAll('[data-elev]'));
    S.anchors = els.map(function (el) {
      var off = el.dataset.anchorOff !== undefined ? +el.dataset.anchorOff
              : (el.classList.contains('dock') ? 34 : 110);
      var r = el.getBoundingClientRect();
      return { el: el, y: r.top + window.pageYOffset + off, e: parseFloat(el.dataset.elev) };
    }).sort(function (a, b) { return a.y - b.y; });
    /* pin the top so the page opens at exactly its first elevation */
    if (S.anchors.length) S.anchors[0].y = S.datumY;
  }
  function elevAt(y) {
    var a = S.anchors, i = 0;
    if (!a.length) return S.H;
    while (i < a.length - 2 && y >= a[i + 1].y) i++;
    var p = a[i], q = a[i + 1] || a[i];
    var dy = Math.max(1, q.y - p.y);
    return p.e - (y - p.y) * ((p.e - q.e) / dy);
  }

  function halfFrac(e) {
    var H = S.H;
    if (e <= 0) return 1.14;
    if (e > H) return 0;
    var r = e / H, f = 1 - 0.50 * Math.pow(r, 1.4);
    if (r > 0.88) f = Math.max(0.05, f * (1 - (r - 0.88) / 0.12 * 0.82));
    return Math.max(0.05, f);
  }

  function drawRail() {
    var w = cv.clientWidth, h = cv.clientHeight;
    if (w < 12 || h < 12) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    if (cv.width !== Math.round(w * dpr)) { cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);

    var sc = S.scale, eD = S.elev, yD = S.datumY;
    var yAt = function (e) { return yD - (e - eD) / sc; };
    var eAt = function (y) { return eD + (yD - y) * sc; };
    var eTop = eAt(0), eBot = eAt(h);
    var narrow = w < 96;
    var rtl = (document.documentElement.getAttribute('dir') === 'rtl');
    var gut = narrow ? 20 : 54;
    var bx0 = rtl ? 5 : gut, bx1 = rtl ? w - gut : w - 5;
    var cx = (bx0 + bx1) / 2, half = (bx1 - bx0) / 2;
    var clampX = function (x) { return Math.max(1, Math.min(w - 1, x)); };
    var e, yy, hf;

    /* soil below grade */
    var y0 = yAt(0);
    if (y0 < h) {
      ctx.save();
      ctx.beginPath(); ctx.rect(0, Math.max(0, y0), w, h - Math.max(0, y0)); ctx.clip();
      ctx.fillStyle = rgba(pal.ink, 0.035); ctx.fillRect(0, Math.max(0, y0), w, h);
      ctx.strokeStyle = rgba(pal.ink, 0.06); ctx.lineWidth = 1;
      for (var gx = -h; gx < w + h; gx += 9) { ctx.beginPath(); ctx.moveTo(gx, h); ctx.lineTo(gx + h, 0); ctx.stroke(); }
      ctx.restore();
    }

    /* tower */
    ctx.beginPath();
    var started = false;
    for (yy = -20; yy <= h + 20; yy += 4) {
      e = eAt(yy); if (e > S.H || e < -34) continue;
      hf = halfFrac(e) * half;
      if (!started) { ctx.moveTo(clampX(cx - hf), yy); started = true; }
      else ctx.lineTo(clampX(cx - hf), yy);
    }
    for (yy = h + 20; yy >= -20; yy -= 4) {
      e = eAt(yy); if (e > S.H || e < -34) continue;
      hf = halfFrac(e) * half;
      ctx.lineTo(clampX(cx + hf), yy);
    }
    if (started) {
      ctx.closePath();
      ctx.fillStyle = rgba(pal.ink, 0.05); ctx.fill();
      ctx.strokeStyle = rgba(pal.ink, 0.55); ctx.lineWidth = 1; ctx.stroke();
    }

    /* floor slabs */
    if (FLOOR / sc > 4.5) {
      ctx.strokeStyle = rgba(pal.ink, 0.13); ctx.lineWidth = 1;
      var f0 = Math.floor(Math.max(-30, eBot) / FLOOR) * FLOOR;
      for (var fe = f0; fe <= Math.min(eTop, S.H); fe += FLOOR) {
        if (fe < -30) continue;
        hf = halfFrac(fe) * half; if (hf <= 1) continue;
        var fy = Math.round(yAt(fe)) + 0.5;
        if (fy < -2 || fy > h + 2) continue;
        ctx.beginPath(); ctx.moveTo(clampX(cx - hf), fy); ctx.lineTo(clampX(cx + hf), fy); ctx.stroke();
      }
    }

    /* mechanical bands at every zone break, plus roof plant */
    var breaks = [], k;
    for (k = 1; k * S.zg < S.H; k++) breaks.push(k * S.zg);
    var occ = S.H * 0.90;
    breaks.push(occ - 6);
    for (k = 0; k < breaks.length; k++) {
      var be = breaks[k];
      if (be > eTop + 20 || be < eBot - 20) continue;
      var byT = yAt(be + 4.2), byB = yAt(be - 4.2);
      hf = halfFrac(be) * half;
      ctx.save();
      ctx.beginPath(); ctx.rect(clampX(cx - hf), byT, 2 * hf, Math.max(2, byB - byT)); ctx.clip();
      ctx.fillStyle = rgba(pal.ink, 0.10); ctx.fillRect(0, byT, w, byB - byT);
      ctx.strokeStyle = rgba(pal.ink, 0.30); ctx.lineWidth = 1;
      for (var mx = cx - hf - 14; mx < cx + hf + 14; mx += 5) {
        ctx.beginPath(); ctx.moveTo(mx, byB); ctx.lineTo(mx + 14, byT); ctx.stroke();
      }
      ctx.restore();
      ctx.strokeStyle = rgba(pal.ink, 0.45); ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(clampX(cx - hf), Math.round(byT) + 0.5); ctx.lineTo(clampX(cx + hf), Math.round(byT) + 0.5); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(clampX(cx - hf), Math.round(byB) + 0.5); ctx.lineTo(clampX(cx + hf), Math.round(byB) + 0.5); ctx.stroke();
    }

    /* risers, following the taper, with a PRV at every break */
    var rw = Math.max(5, half * 0.30);
    var offAt = function (ee) { return Math.min(rw, halfFrac(ee) * half * 0.55); };
    [[-1, pal.water], [1, pal.fire]].forEach(function (pair) {
      var sgn = pair[0], col = pair[1];
      ctx.strokeStyle = rgba(col, 0.9); ctx.lineWidth = 1.6;
      ctx.beginPath();
      var open = false;
      for (var ry = -8; ry <= h + 8; ry += 3) {
        var re = eAt(ry);
        if (re > occ || re < -26) { open = false; continue; }
        var ox = offAt(re);
        if (ox < 2.5) { open = false; continue; }
        var rx = cx + sgn * ox;
        if (!open) { ctx.moveTo(rx, ry); open = true; } else ctx.lineTo(rx, ry);
      }
      ctx.stroke();
      for (var b = 0; b < breaks.length - 1; b++) {
        var be2 = breaks[b], by = yAt(be2);
        if (by < -14 || by > h + 14) continue;
        var ox2 = offAt(be2); if (ox2 < 2.5) continue;
        var px = cx + sgn * ox2;
        ctx.fillStyle = rgba(col, 0.95);
        ctx.beginPath(); ctx.moveTo(px - 4, by - 6); ctx.lineTo(px + 4, by - 6); ctx.lineTo(px, by); ctx.closePath(); ctx.fill();
        ctx.beginPath(); ctx.moveTo(px - 4, by + 6); ctx.lineTo(px + 4, by + 6); ctx.lineTo(px, by); ctx.closePath(); ctx.fill();
      }
    });

    /* roof tank */
    var te = occ + 8;
    if (te < eTop + 30 && te > eBot - 10) {
      hf = halfFrac(te) * half;
      var tw = Math.max(7, hf * 0.85);
      ctx.strokeStyle = rgba(pal.water, 0.9); ctx.lineWidth = 1.2;
      ctx.fillStyle = rgba(pal.water, 0.22);
      var ty = yAt(te + 7), th = Math.max(4, yAt(te - 7) - ty);
      ctx.fillRect(cx - tw, ty, tw * 2, th); ctx.strokeRect(cx - tw, ty, tw * 2, th);
    }

    /* grade */
    if (y0 > -10 && y0 < h + 10) {
      ctx.strokeStyle = rgba(pal.ink, 0.85); ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.moveTo(0, Math.round(y0) + 0.5); ctx.lineTo(w, Math.round(y0) + 0.5); ctx.stroke();
    }

    /* survey scale */
    ctx.font = '500 9px "IBM Plex Mono", monospace';
    ctx.textBaseline = 'middle';
    var minor = 10, e0 = Math.ceil(eBot / minor) * minor;
    for (var t2 = e0; t2 <= eTop; t2 += minor) {
      var ty2 = Math.round(yAt(t2)) + 0.5;
      if (ty2 < 8 || ty2 > h - 4) continue;
      var major = (Math.round(t2) % 50 === 0);
      ctx.strokeStyle = rgba(pal.ink, major ? 0.5 : 0.22);
      ctx.lineWidth = 1;
      var tx0 = rtl ? w - 6 : 6, tx1 = rtl ? w - (major ? 20 : 13) : (major ? 20 : 13);
      ctx.beginPath(); ctx.moveTo(tx0, ty2); ctx.lineTo(tx1, ty2); ctx.stroke();
      if (major && !narrow) {
        ctx.fillStyle = rgba(pal.ink3, 0.95);
        ctx.textAlign = rtl ? 'right' : 'left';
        ctx.fillText((t2 > 0 ? '+' : '') + t2, rtl ? w - 24 : 24, ty2);
        ctx.textAlign = 'left';
      }
    }

    /* the datum */
    var dy = Math.round(yD) + 0.5;
    ctx.strokeStyle = rgba(pal.fire, 0.9); ctx.lineWidth = 1.2;
    ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(0, dy); ctx.lineTo(w, dy); ctx.stroke();
    ctx.setLineDash([]);
  }

  function set(id, html) { var el = $(id); if (el) el.innerHTML = html; }
  function setT(id, txt) { var el = $(id); if (el) el.textContent = txt; }

  function updateCluster() {
    var e = S.elev, sb = staticBar(e);
    setT('r-elev', (e >= 0 ? '' : '−') + Math.abs(e).toFixed(0));
    set('r-static', sb.toFixed(1) + '<small>bar</small>');
    var b1 = $('b-static'); if (b1) b1.style.width = Math.min(100, sb / (S.H * BAR) * 100) + '%';

    if (e > S.H + 1 || e < 0) {
      setT('r-zn', '—'); set('r-zone', '—');
      var b0 = $('b-zone'); if (b0) b0.style.width = '0%';
    } else {
      var zn = Math.min(S.nz, Math.floor(e / S.zg) + 1);
      var res = (e - (zn - 1) * S.zg) * BAR;
      setT('r-zn', zn);
      set('r-zone', res.toFixed(1) + '<small>bar</small>');
      var b2 = $('b-zone'); if (b2) b2.style.width = Math.min(100, res / (S.zg * BAR) * 100) + '%';
    }
    var sp = stackPa(e, S.To);
    set('r-stack', (sp >= 0 ? '↑' : '↓') + ' ' + Math.abs(sp).toFixed(0) + '<small>Pa</small>');
    set('r-wind', e < 0 ? '—' : windMs(e).toFixed(1) + '<small>m/s</small>');
  }

  function calc() {
    var h = $('s-h'), pn = $('s-pn'), pm = $('s-pm'), pf = $('s-pf');
    if (!h) return;
    S.H = +h.value; S.PN = +pn.value; S.PM = +pm.value; S.PF = +pf.value;
    S.zd = Math.max(5, (S.PN - S.PM) / BAR);
    S.zf = S.PF / BAR;
    S.zg = Math.min(S.zd, S.zf);
    S.nz = Math.max(1, Math.ceil(S.H / S.zg));

    setT('v-h', S.H); setT('v-pn', S.PN); setT('v-pm', S.PM.toFixed(1)); setT('v-pf', S.PF);
    set('o-base', (S.H * BAR).toFixed(1) + '<small>bar</small>');
    set('o-zd', S.zd.toFixed(0) + '<small>m</small>');
    set('o-zf', S.zf.toFixed(0) + '<small>m</small>');
    set('o-zg', S.zg.toFixed(0) + '<small>m</small>');
    setT('o-nz', S.nz);
    set('o-e', liftKWh(S.H).toFixed(2) + '<small>kWh/m&sup3;</small>');

    var rows = [], i;
    for (i = S.nz; i >= 1; i--) {
      var lo = (i - 1) * S.zg, hi = Math.min(S.H, i * S.zg);
      rows.push({ i: i, lo: lo, hi: hi, bar: (hi - lo) * BAR });
    }
    var show = rows.length > 7 ? rows.slice(0, 3).concat([null]).concat(rows.slice(-2)) : rows;
    var zb = $('zbar');
    if (zb) zb.innerHTML = show.map(function (r) {
      if (!r) return '<div class="el-z-gap">&#8942;</div>';
      return '<div class="' + (r.i === 1 ? 'g' : '') + '"><span>Z' + r.i + '&nbsp;&nbsp;' +
             r.lo.toFixed(0) + '&#8211;' + r.hi.toFixed(0) + '&thinsp;m</span><span>' +
             r.bar.toFixed(1) + '&thinsp;bar</span></div>';
    }).join('');

    var head = Math.abs(S.zd - S.zf), note;
    var ar = (document.documentElement.getAttribute('lang') || '').indexOf('ar') === 0;
    if (S.zf < S.zd - 0.5) {
      note = ar
        ? 'الحاكم هو عمود الحريق عند PN' + S.PF + '، ولدى عمود المياه ' + head.toFixed(0) +
          ' مترًا من الطاقة غير المستغلة — رفع رتبته لا يفيد قبل رفع رتبة عمود الحريق معه. ' +
          S.nz + ' نطاقات، أي ' + (S.nz - 1) + ' طوابق ميكانيكية وسيطة إضافة إلى دور السطح.'
        : 'Governed by the fire standpipe at PN' + S.PF + '. The domestic riser carries ' +
          head.toFixed(0) + ' m of unused headroom — raising its class buys nothing until the ' +
          'standpipe class rises with it. ' + S.nz + ' zones, so ' + (S.nz - 1) +
          ' intermediate mechanical levels plus roof plant.';
    } else if (S.zd < S.zf - 0.5) {
      note = ar
        ? 'الحاكم هو عمود المياه عند PN' + S.PN + ' بضغط متبقٍّ ' + S.PM.toFixed(1) +
          ' بار، ولعمود الحريق ' + head.toFixed(0) + ' متر من الطاقة. تقع الخزانات وصمامات تخفيض الضغط كل ' +
          S.zg.toFixed(0) + ' متر — ' + S.nz + ' نطاقات إجمالًا.'
        : 'Governed by the domestic riser at PN' + S.PN + ' with ' + S.PM.toFixed(1) +
          ' bar residual. The standpipe has ' + head.toFixed(0) +
          ' m of headroom. Break tanks and PRVs land every ' + S.zg.toFixed(0) +
          ' m — ' + S.nz + ' zones in all.';
    } else {
      note = ar
        ? 'ينكسر العمودان عند المنسوب نفسه، وهذا هو الحل الأكفأ: دور ميكانيكي واحد يخدمهما. ' +
          S.nz + ' نطاقات عند ' + S.zg.toFixed(0) + ' متر.'
        : 'Both risers break at the same level, which is the efficient answer: one mechanical ' +
          'floor serves both. ' + S.nz + ' zones at ' + S.zg.toFixed(0) + ' m.';
    }
    setT('calc-note', note);
    wake();
  }

  var docks = [].slice.call(document.querySelectorAll('.dock'));
  var lastH = 0, lastVH = 0;

  function render() {
    updateCluster();
    drawRail();
    for (var i = 0; i < docks.length; i++) {
      var r = docks[i].getBoundingClientRect();
      var on = Math.abs((r.top + 34) - S.datumY) < 64;
      if (on !== docks[i].classList.contains('at')) docks[i].classList.toggle('at', on);
    }
  }
  function retarget() {
    var dh = document.body.scrollHeight, vh = vpH();
    if (dh !== lastH || vh !== lastVH) { lastH = dh; lastVH = vh; layout(true); }
    S.tgt = elevAt(window.pageYOffset + S.datumY);
  }
  function frame() {
    S.elev += (S.tgt - S.elev) * 0.16;
    render();
    if (Math.abs(S.tgt - S.elev) > 0.03 || S.idle-- > 0) requestAnimationFrame(frame);
    else S.run = false;
  }
  function wake() {
    retarget();
    if (RM || document.hidden) { S.elev = S.tgt; render(); return; }
    S.idle = 20;
    if (!S.run) { S.run = true; requestAnimationFrame(frame); }
  }

  function vpH() { return window.innerHeight || ROOT.clientHeight || 800; }
  function layout(quiet) {
    var vh = vpH();
    S.datumY = Math.round(Math.max(190, vh * 0.42));
    S.scale = 148 / Math.max(320, vh);
    var dl = document.querySelector('.el-datum');
    if (dl) dl.style.top = S.datumY + 'px';
    var cl = document.querySelector('.el-cluster');
    if (cl) cl.style.top = window.innerWidth > 760 ? Math.round(S.datumY - 128) + 'px' : '';
    computeAnchors();
    lastH = document.body.scrollHeight; lastVH = vh;
    if (!quiet) wake();
  }

  var seg = document.querySelector('.el-seg');
  if (seg) seg.addEventListener('click', function (ev) {
    var b = ev.target.closest('button'); if (!b) return;
    S.To = +b.dataset.to;
    [].slice.call(this.querySelectorAll('button')).forEach(function (x) {
      x.setAttribute('aria-pressed', String(x === b));
    });
    wake();
  });
  ['s-h', 's-pn', 's-pm', 's-pf'].forEach(function (id) {
    var el = $(id); if (el) el.addEventListener('input', calc);
  });
  window.addEventListener('scroll', wake, { passive: true });
  window.addEventListener('resize', layout);
  new MutationObserver(function (m) {
    for (var i = 0; i < m.length; i++)
      if (m[i].attributeName === 'data-theme') { readPal(); wake(); return; }
  }).observe(ROOT, { attributes: true });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { layout(); });
  window.addEventListener('load', function () { layout(); });

  readPal(); layout(); calc();
  window.elevationRail = { S: S, layout: layout, render: render, elevAt: elevAt, calc: calc,
                           set: function (e) { S.tgt = e; S.elev = e; render(); } };
})();
