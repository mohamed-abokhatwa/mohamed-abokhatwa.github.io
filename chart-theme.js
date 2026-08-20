/* ═══════════════════════════════════════════════════════════════════
   chart-theme.js — makes every Chart.js chart obey the site tokens.

   Charts used to carry a fixed palette and asked for 'DM Sans', a face
   the site never loaded, so they ignored dark mode entirely. This maps
   the legacy literals onto the Elevation 828 tokens once at init and
   again whenever the theme flips, reading the values straight from CSS.
   Load it after chart.umd.min.js and before any chart is constructed.
   ═══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var ROOT = document.documentElement;

  function boot() {
    if (typeof Chart === 'undefined' || boot.done) return;
    boot.done = true;
    run();
  }
  if (typeof Chart === 'undefined') {
    /* loaded before Chart.js: come back once it exists */
    document.addEventListener('DOMContentLoaded', boot);
    window.addEventListener('load', boot);
    return;
  }
  boot();

  function run() {
  function tok(n) { return getComputedStyle(ROOT).getPropertyValue(n).trim(); }

  /* legacy literal -> token */
  var MAP = {
    '#1b4f72': '--s2', '#2e6da4': '--s2', '#2e86c1': '--s2', '#2e7db8': '--s2',
    '#2980b9': '--s2', '#5dade2': '--s2', '#5eaadd': '--s2',
    '#e34000': '--s3', '#e67e22': '--s3',
    '#b9770e': '--warning', '#8a5700': '--warning', '#d99a3a': '--warning',
    '#8a6d3b': '--warning', '#b45309': '--warning',
    '#c0392b': '--danger', '#c42b2b': '--danger', '#e74c3c': '--danger',
    '#1e8449': '--success', '#1a7a38': '--success',
    '#5b6b7b': '--s5', '#7a848d': '--s5', '#7f8c8d': '--s5', '#5b6670': '--s5',
    '#6b4f9e': '--s4', '#7d3c98': '--s4', '#5060b0': '--s4',
    '#0071e3': '--s1',
    '#1a1d21': '--text-primary', '#6e6e73': '--text-secondary',
    '#86868b': '--text-tertiary', '#9aa7b2': '--text-tertiary',
    '#9aa4ad': '--text-tertiary', '#aaaaaa': '--text-tertiary',
    '#eef2f5': '--border', '#eef2f6': '--border', '#eeeeee': '--border',
    '#c3ccd5': '--border', '#a9cce3': '--border'
  };
  /* white only makes sense as a ring around a point */
  var RING = { '#fff': '--sheet', '#ffffff': '--sheet' };

  var COLOR_KEYS = ['borderColor', 'backgroundColor', 'pointBackgroundColor',
    'pointBorderColor', 'hoverBorderColor', 'hoverBackgroundColor', 'color'];

  function norm(c) {
    if (typeof c !== 'string') return null;
    var s = c.trim().toLowerCase();
    if (s.charAt(0) !== '#') return null;
    if (s.length === 4) s = '#' + s[1] + s[1] + s[2] + s[2] + s[3] + s[3];
    return s;
  }
  function conv(c, ring) {
    var s = norm(c);
    if (!s) return null;
    if (MAP[s]) return tok(MAP[s]) || null;
    if (ring && RING[s]) return tok(RING[s]) || null;
    return null;
  }

  /* remember the literal a chart was authored with, so flipping the theme
     always converts from the original rather than from the last result */
  function slots(chart) {
    if (chart.$themeSlots) return chart.$themeSlots;
    var out = [];
    function grab(obj, key, ring) {
      if (!obj) return;
      var v = obj[key];
      if (typeof v === 'string' && norm(v)) out.push({ o: obj, k: key, v: v, ring: !!ring });
      else if (Array.isArray(v)) {
        for (var i = 0; i < v.length; i++)
          if (typeof v[i] === 'string' && norm(v[i])) out.push({ o: v, k: i, v: v[i], ring: !!ring });
      }
    }
    (chart.data.datasets || []).forEach(function (ds) {
      COLOR_KEYS.forEach(function (k) {
        grab(ds, k, k === 'borderColor' || k === 'pointBorderColor');
      });
    });
    var sc = (chart.options && chart.options.scales) || {};
    Object.keys(sc).forEach(function (id) {
      var s = sc[id]; if (!s) return;
      grab(s.grid, 'color'); grab(s.grid, 'borderColor');
      grab(s.ticks, 'color'); grab(s.title, 'color'); grab(s.border, 'color');
    });
    var ann = chart.options && chart.options.plugins && chart.options.plugins.annotation;
    if (ann && ann.annotations) {
      Object.keys(ann.annotations).forEach(function (id) {
        var a = ann.annotations[id]; if (!a) return;
        grab(a, 'borderColor'); grab(a, 'backgroundColor'); grab(a, 'color');
        if (a.label) { grab(a.label, 'color'); grab(a.label, 'backgroundColor'); }
      });
    }
    chart.$themeSlots = out;
    return out;
  }

  function apply(chart) {
    slots(chart).forEach(function (s) {
      var c = conv(s.v, s.ring);
      if (c) s.o[s.k] = c;
    });
    if (chart.options) {
      chart.options.color = tok('--text-secondary');
      if (chart.options.plugins && chart.options.plugins.legend &&
          chart.options.plugins.legend.labels) {
        chart.options.plugins.legend.labels.color = tok('--text-secondary');
      }
    }
  }

  function defaults() {
    Chart.defaults.font.family = "'IBM Plex Sans', system-ui, -apple-system, sans-serif";
    Chart.defaults.color = tok('--text-secondary');
    Chart.defaults.borderColor = tok('--border');
    if (Chart.defaults.plugins && Chart.defaults.plugins.tooltip) {
      var t = Chart.defaults.plugins.tooltip;
      t.backgroundColor = tok('--text-primary');
      t.titleColor = tok('--bg');
      t.bodyColor  = tok('--bg');
      t.borderColor = tok('--border');
      t.titleFont = { family: "'IBM Plex Mono', monospace", size: 11, weight: '500' };
      t.bodyFont  = { family: "'IBM Plex Sans', sans-serif", size: 12 };
      t.padding = 9;
      t.cornerRadius = 2;
      t.displayColors = true;
    }
  }
  defaults();

  Chart.register({
    id: 'siteTheme',
    afterInit: function (chart) { apply(chart); }
  });

  function reskin() {
    defaults();
    var reg = Chart.instances || {};
    Object.keys(reg).forEach(function (k) {
      var c = reg[k];
      if (!c || !c.options) return;
      apply(c);
      try { c.update('none'); } catch (e) {}
    });
  }

  new MutationObserver(function (m) {
    for (var i = 0; i < m.length; i++)
      if (m[i].attributeName === 'data-theme') { reskin(); return; }
  }).observe(ROOT, { attributes: true });

  window.reskinCharts = reskin;
  /* catch any chart that was built before this file ran */
  if (document.readyState === 'complete') reskin();
  else window.addEventListener('load', reskin);
  }
})();
