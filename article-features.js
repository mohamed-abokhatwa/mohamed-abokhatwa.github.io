/* article-features.js — Reading Progress Bar + Reading Time + Related Articles
   Include this script in every article page (before </body>) */

(function () {
  'use strict';

  /* ─────────────────────────────────────────────────────────────
     1.  ARTICLES DATA
     ───────────────────────────────────────────────────────────── */
  var ARTICLES = [
    { url:'water-hammer-control-valve.html',       title:'Effect of Control Valve Closure Time on Water Hammer Intensity',                                          cat:'surge',       thumb:'water_hammer_control_valve_v2.png',   mins:15, tag:'Transient Analysis · Water Hammer' },
    { url:'combination-air-valves.html',           title:'Design Criteria for Combination Air Valves in Long-Distance Transmission Mains',                          cat:'pipeline',    thumb:'combination_air_valves_design_criteria.png', mins:14, tag:'Transmission Pipeline · Air Management' },
    { url:'surge-vessel.html',                     title:'Sizing the Hydropneumatic Surge Vessel in Water Transmission Pipelines',                                  cat:'surge',       thumb:'https://d8j0ntlcm91z4.cloudfront.net/user_3DrcxvLSmsv5g8tPL57WIum7RP6/hf_20260517_194531_a798e431-c75a-4a41-b7b3-146f9a1a846d.png', mins:10, tag:'Surge Analysis · Hydraulic Design' },
    { url:'hydraulic-mistakes.html',               title:'Common Mistakes in Hydraulic Modeling of Water Transmission Networks',                                    cat:'hydraulic',   thumb:'hydraulic_modeling_mistakes.png',     mins:8,  tag:'Hydraulic Modeling · Pipeline Design' },
    { url:'pre-charge-pressure.html',              title:'The Pre-Charge Pressure of the Surge Vessel — How One Number Changes Everything',                         cat:'surge',       thumb:'IMG_4656.PNG',                        mins:12, tag:'Surge Analysis · Surge Vessel Design' },
    { url:'above-ground-pipeline-design.html',     title:'Engineering Guide: Structural Design of Above-Ground Water Pipelines',                                   cat:'pipeline',    thumb:'above-ground-pipeline-design.jpg',    mins:12, tag:'Structural Design · Pipeline Engineering' },
    { url:'control-valve-transients-hammer.html',  title:'Mastering Control Valve Transients in Bentley HAMMER: FCV vs. PRV',                                      cat:'surge',       thumb:'control-valve-transients-hammer.jpg', mins:10, tag:'Transient Analysis · Bentley HAMMER' },
    { url:'boundary-conditions-reservoir-tank.html',title:'Demystifying Boundary Conditions: Reservoir vs. Tank in Bentley HAMMER',                                cat:'surge',       thumb:'boundary-conditions-reservoir-tank.jpg',mins:9, tag:'Transient Analysis · Bentley HAMMER' },
    { url:'carbon-steel-pipeline-cml.html',        title:'Structural Design Reference: Carbon Steel Pipelines with Cement Mortar Lining',                          cat:'pipeline',    thumb:'carbon-steel-pipeline-cml.jpg',      mins:11, tag:'Structural Design · Pipeline Engineering' },
    { url:'npsh-water-infrastructure.html',        title:'Technical Design Guide: Mastering NPSH in Water Infrastructure',                                         cat:'pumps',       thumb:'npsh-water-infrastructure.jpg',       mins:10, tag:'Pump Design · NPSH' },
    { url:'transient-analysis-scada.html',         title:'Beyond Static Design: Integrating Transient Analysis with SCADA for Smart Pipelines',                    cat:'surge',       thumb:'transient-analysis-scada.jpg',        mins:9,  tag:'SCADA · Digital Twin · Surge Analysis' },
    { url:'cavitation-prvs-fcvs.html',             title:'Technical Design Guide: Managing Cavitation in PRVs and FCVs',                                           cat:'hydraulic',   thumb:'cavitation-prvs-fcvs.jpg',            mins:8,  tag:'Hydraulic Design · Cavitation' },
    { url:'wet-well-vortex-design.html',           title:'The Silent Pump Killer: Vortex Formation and Hydraulic Instability in Wet Well Design',                  cat:'pumps',       thumb:'wet-well-vortex-design.jpg',          mins:9,  tag:'Pump Station Design · Wet Well' },
    { url:'vfd-myth-hydraulic-design.html',        title:"The VFD Myth: Why Variable Frequency Drives Aren't a 'Magic Fix' for Poor Hydraulic Design",             cat:'pumps',       thumb:'vfd-myth-hydraulic-design.jpg',       mins:8,  tag:'Pump Engineering · VFD' },
    { url:'air-valves-pipeline-safety.html',       title:'Air Valves: Just Pipeline Accessories or the Ultimate Safety Guard?',                                    cat:'pipeline',    thumb:'air-valves-pipeline-safety.jpg',      mins:9,  tag:'Pipeline Safety · Air Valve Design' },
    { url:'air-admission-networks.html',           title:'Strategic Air Admission in Water Transmission Networks: A Dual Perspective',                             cat:'surge',       thumb:'air-admission-networks.jpg',          mins:8,  tag:'Surge Analysis · Air Management' },
    { url:'top-hill-challenge.html',               title:'Managing the "Top Hill" Challenge in Water Transmission Lines',                                          cat:'pipeline',    thumb:'top-hill-challenge.jpg',              mins:5,  tag:'Pipeline Design · Surge Analysis' },
    { url:'check-valve-hammer.html',               title:'From Modeling to Procurement: A Guide to Check Valve Analysis in Bentley HAMMER',                        cat:'surge',       thumb:'check-valve-hammer.jpg',              mins:5,  tag:'Transient Analysis · Check Valve' },
    { url:'prv-altitude-valve-fcv.html',           title:'Understanding PRV, Altitude Valve, and FCV in Water Transmission Systems',                               cat:'hydraulic',   thumb:'prv-altitude-valve-fcv.jpg',          mins:5,  tag:'Hydraulic Control · Valve Selection' },
    { url:'sustainable-pump-selection.html',       title:'Sustainable Pump Selection: Beyond the Duty Point',                                                      cat:'pumps',       thumb:'sustainable-pump-selection.jpg',      mins:5,  tag:'Pump Engineering · Energy Efficiency' },
    { url:'steady-state-analysis.html',            title:'Steady State Analysis: The Foundation of Water Transmission Design',                                     cat:'hydraulic',   thumb:'steady-state-analysis.jpg',           mins:5,  tag:'Hydraulic Modeling · Steady State' },
    { url:'surge-analysis-risk.html',              title:'Surge Analysis: An Essential Risk Mitigation Strategy for Pressurized Pipelines',                        cat:'surge',       thumb:'surge-analysis-risk.jpg',             mins:5,  tag:'Surge Analysis · Risk Management' },
    { url:'design-vs-reality.html',                title:'The Biggest Gap in Engineering: Design vs. Reality',                                                     cat:'leadership',  thumb:'design-vs-reality.jpg',               mins:4,  tag:'Engineering Leadership · Field Experience' },
    { url:'engineering-decisions.html',            title:'Making Decisions Under Pressure: Lessons From the Field',                                                cat:'leadership',  thumb:'engineering-decisions.jpg',           mins:4,  tag:'Engineering Leadership · Project Management' },
    { url:'envision-sustainability.html',          title:'Sustainability in Infrastructure: A Core Engineering Responsibility',                                    cat:'leadership',  thumb:'envision-sustainability.jpg',         mins:4,  tag:'Sustainability · Envision' },
    { url:'infrastructure-at-scale.html',          title:'Managing Infrastructure at Scale: Beyond Technical Complexity',                                          cat:'leadership',  thumb:'infrastructure-at-scale.jpg',         mins:4,  tag:'Engineering Leadership · Infrastructure' },
    { url:'sustainability-in-design.html',         title:'From Strategy to Specification: Integrating Sustainability in Engineering Design',                       cat:'leadership',  thumb:'sustainability-in-design.jpg',        mins:4,  tag:'Sustainability · Design Coordination' },
    { url:'daf-swro-pretreatment.html',            title:'Technical Deep-Dive: Designing DAF for Large-Scale SWRO Pre-treatment',                                  cat:'desalination',thumb:'daf-swro-pretreatment.jpg',           mins:10, tag:'Desalination · DAF · SWRO' },
    { url:'mega-swro-engineering.html',            title:'The Engineering of Scale: Why Standard Design Is Not Enough for Mega SWRO Plants',                       cat:'desalination',thumb:'mega-swro-engineering.jpg',          mins:8,  tag:'Desalination · SWRO · Scale Engineering' },
    { url:'swro-pretreatment-dilemma.html',        title:'Design Reference: The Strategic Dilemma in SWRO Pre-treatment',                                          cat:'desalination',thumb:'swro-pretreatment-dilemma.jpg',       mins:9,  tag:'Desalination · SWRO · UF' },
    { url:'ro-overdesign-paradox.html',            title:'The Over-Design Paradox: Are Your Safety Margins Actually Killing Your RO Plant?',                       cat:'desalination',thumb:'ro-overdesign-paradox.jpg',          mins:7,  tag:'Desalination · RO · Design Philosophy' },
    { url:'chlorine-swro-disinfection.html',       title:'The Chlorine Journey: Disinfection Science in SWRO Plants',                                              cat:'desalination',thumb:'chlorine-swro-disinfection.jpg',     mins:3,  tag:'Desalination · SWRO · Chlorination' },
    { url:'offshore-intake-design.html',           title:'Offshore Seawater Intake Design: Six Core Engineering Principles',                                       cat:'desalination',thumb:'offshore-intake-design.jpg',          mins:3,  tag:'Desalination · Intake Design · Offshore' },
    { url:'ph-management-swro.html',               title:'pH Management: The Hidden Key to Sustainable SWRO Operation',                                            cat:'desalination',thumb:'ph-management-swro.jpg',              mins:3,  tag:'Desalination · SWRO · pH' },
    { url:'onshore-intake-design.html',            title:'Onshore Intake Design: Bridging Hydraulic Theory and Field Reality',                                     cat:'desalination',thumb:'onshore-intake-design.jpg',          mins:3,  tag:'Desalination · Intake Design · Onshore' },
    { url:'px-energy-recovery.html',               title:'PX Technology: How Energy Recovery Transformed Desalination Economics',                                  cat:'desalination',thumb:'px-energy-recovery.jpg',              mins:3,  tag:'Desalination · Energy Recovery · PX' }
  ];

  /* ─────────────────────────────────────────────────────────────
     2.  READING PROGRESS BAR
     ───────────────────────────────────────────────────────────── */
  function initProgressBar() {
    var bar = document.createElement('div');
    bar.id = 'read-progress-bar';
    bar.setAttribute('role', 'progressbar');
    bar.setAttribute('aria-label', 'Reading progress');
    bar.style.cssText = [
      'position:fixed',
      'top:0',
      'left:0',
      'height:3px',
      'width:0%',
      'background:linear-gradient(90deg,#0071e3 0%,#5b9cf6 100%)',
      'z-index:10001',
      'border-radius:0 2px 2px 0',
      'transition:width 0.08s linear',
      'pointer-events:none'
    ].join(';');
    document.body.insertBefore(bar, document.body.firstChild);

    window.addEventListener('scroll', function () {
      var scrollTop  = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight  = Math.max(
        document.body.scrollHeight,
        document.documentElement.scrollHeight
      ) - window.innerHeight;
      var pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
      bar.style.width = pct + '%';
    }, { passive: true });
  }

  /* ─────────────────────────────────────────────────────────────
     3.  READING TIME (auto-compute from article-body)
     ───────────────────────────────────────────────────────────── */
  function updateReadingTime() {
    var body = document.querySelector('.article-body');
    if (!body) return;
    var words = (body.innerText || body.textContent || '').trim().split(/\s+/).length;
    var mins  = Math.max(1, Math.ceil(words / 230));
    // Find the span in .byline that contains "min read" and update it
    var byline = document.querySelector('.byline');
    if (!byline) return;
    var spans = byline.querySelectorAll('span');
    for (var i = 0; i < spans.length; i++) {
      if (spans[i].textContent.indexOf('min read') !== -1) {
        spans[i].textContent = mins + ' min read';
        return;
      }
    }
  }

  /* ─────────────────────────────────────────────────────────────
     4.  RELATED ARTICLES
     ───────────────────────────────────────────────────────────── */
  function getRelated() {
    var page = window.location.pathname.split('/').pop() || '';
    var current = null;
    for (var i = 0; i < ARTICLES.length; i++) {
      if (ARTICLES[i].url === page) { current = ARTICLES[i]; break; }
    }
    if (!current) return [];

    // Same category first, then fallback to any
    var same = [];
    var other = [];
    for (var j = 0; j < ARTICLES.length; j++) {
      if (ARTICLES[j].url === page) continue;
      if (ARTICLES[j].cat === current.cat) same.push(ARTICLES[j]);
      else other.push(ARTICLES[j]);
    }
    // Shuffle same-cat picks slightly (deterministic by title length so it's stable)
    same.sort(function(a, b){ return (a.mins - b.mins) || a.title.length - b.title.length; });
    var picks = same.slice(0, 3);
    if (picks.length < 3) picks = picks.concat(other.slice(0, 3 - picks.length));
    return picks.slice(0, 3);
  }

  function renderRelated() {
    var articles = getRelated();
    if (!articles.length) return;

    var html = [
      '<section class="related-articles-section">',
      '  <div class="related-articles-inner">',
      '    <div class="related-articles-header">',
      '      <span class="related-eyebrow">Continue Reading</span>',
      '      <h2 class="related-title">Related Articles</h2>',
      '    </div>',
      '    <div class="related-grid">'
    ];

    articles.forEach(function (a) {
      var thumbSrc = a.thumb.indexOf('http') === 0 ? a.thumb : a.thumb;
      html.push(
        '<a href="' + a.url + '" class="related-card">',
        '  <div class="related-thumb">',
        '    <img src="' + thumbSrc + '" alt="' + a.title.replace(/"/g, '&quot;') + '" loading="lazy" onerror="this.parentElement.style.display=\'none\'">',
        '  </div>',
        '  <div class="related-card-body">',
        '    <span class="related-tag">' + a.tag + '</span>',
        '    <div class="related-card-title">' + a.title + '</div>',
        '    <div class="related-meta">' + a.mins + ' min read &nbsp;&#8594;</div>',
        '  </div>',
        '</a>'
      );
    });

    html.push('    </div>', '  </div>', '</section>');

    // Insert before footer
    var footer = document.querySelector('footer');
    if (footer) {
      footer.insertAdjacentHTML('beforebegin', html.join('\n'));
    }
  }

  /* ─────────────────────────────────────────────────────────────
     4b. PDF DOWNLOAD BUTTON
     ───────────────────────────────────────────────────────────── */
  function injectPdfButton() {
    var byline = document.querySelector('.byline');
    if (!byline) return;

    var wrap = document.createElement('div');
    wrap.className = 'pdf-btn-wrap';

    var btn = document.createElement('button');
    btn.className = 'pdf-btn';
    btn.setAttribute('aria-label', 'Download as PDF');
    btn.title = 'Save or print this article as PDF';
    btn.innerHTML =
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/>' +
      '<polyline points="7 10 12 15 17 10"/>' +
      '<line x1="12" y1="15" x2="12" y2="3"/>' +
      '</svg> Download PDF';
    btn.onclick = function () { window.print(); };

    wrap.appendChild(btn);
    // Insert after byline
    byline.parentNode.insertBefore(wrap, byline.nextSibling);
  }

  /* ─────────────────────────────────────────────────────────────
     5.  CSS
     ───────────────────────────────────────────────────────────── */
  function injectCSS() {
    var style = document.createElement('style');
    style.textContent = [
      /* Related articles section */
      '.related-articles-section{',
      '  padding:60px 24px 80px;',
      '  background:var(--bg-2,#f5f5f7);',
      '  border-top:1px solid var(--border,rgba(0,0,0,0.08));',
      '}',
      '.related-articles-inner{',
      '  max-width:var(--max-w,1100px);',
      '  margin:0 auto;',
      '}',
      '.related-articles-header{ margin-bottom:36px; }',
      '.related-eyebrow{',
      '  display:block;',
      '  font-size:11px;',
      '  font-weight:600;',
      '  letter-spacing:0.1em;',
      '  text-transform:uppercase;',
      '  color:var(--accent,#0071e3);',
      '  margin-bottom:10px;',
      '}',
      '.related-title{',
      '  font-size:clamp(24px,3vw,34px);',
      '  font-weight:600;',
      '  letter-spacing:-0.02em;',
      '  color:var(--text-primary,#1d1d1f);',
      '  margin:0;',
      '}',
      '.related-grid{',
      '  display:grid;',
      '  grid-template-columns:repeat(3,1fr);',
      '  gap:16px;',
      '}',
      '.related-card{',
      '  display:flex;',
      '  flex-direction:column;',
      '  background:var(--glass,rgba(255,255,255,0.72));',
      '  backdrop-filter:var(--blur,blur(20px));',
      '  -webkit-backdrop-filter:var(--blur,blur(20px));',
      '  border:1px solid var(--glass-border,rgba(255,255,255,0.5));',
      '  border-radius:var(--radius,16px);',
      '  box-shadow:var(--shadow-glass,0 4px 24px rgba(0,0,0,0.06));',
      '  text-decoration:none;',
      '  overflow:hidden;',
      '  transition:transform 0.2s ease, box-shadow 0.2s ease;',
      '}',
      '.related-card:hover{',
      '  transform:translateY(-3px);',
      '  box-shadow:0 12px 36px rgba(0,0,0,0.12);',
      '}',
      '.related-thumb{',
      '  width:100%;',
      '  height:140px;',
      '  overflow:hidden;',
      '  background:var(--bg-4,#e8e8ed);',
      '  flex-shrink:0;',
      '}',
      '.related-thumb img{',
      '  width:100%;',
      '  height:100%;',
      '  object-fit:cover;',
      '  display:block;',
      '  filter:grayscale(80%);',
      '  opacity:0.85;',
      '  transition:filter 0.35s ease, opacity 0.35s ease;',
      '}',
      '.related-card:hover .related-thumb img{',
      '  filter:grayscale(0%);',
      '  opacity:1;',
      '}',
      '.related-card-body{',
      '  padding:20px 20px 20px;',
      '  flex:1;',
      '  display:flex;',
      '  flex-direction:column;',
      '  gap:8px;',
      '}',
      '.related-tag{',
      '  font-size:10px;',
      '  font-weight:600;',
      '  letter-spacing:0.08em;',
      '  text-transform:uppercase;',
      '  color:var(--text-tertiary,#aeaeb2);',
      '}',
      '.related-card-title{',
      '  font-size:15px;',
      '  font-weight:600;',
      '  color:var(--text-primary,#1d1d1f);',
      '  line-height:1.4;',
      '  letter-spacing:-0.01em;',
      '  flex:1;',
      '}',
      '.related-meta{',
      '  font-size:13px;',
      '  color:var(--accent,#0071e3);',
      '  font-weight:500;',
      '  margin-top:4px;',
      '}',
      /* PDF button */
      '.pdf-btn-wrap{ margin-top:20px; }',
      '.pdf-btn{',
      '  display:inline-flex;',
      '  align-items:center;',
      '  gap:7px;',
      '  padding:9px 20px;',
      '  border-radius:980px;',
      '  border:1.5px solid rgba(0,113,227,0.35);',
      '  background:rgba(0,113,227,0.06);',
      '  font-size:13px;',
      '  font-weight:600;',
      '  color:#0071e3;',
      '  cursor:pointer;',
      '  font-family:inherit;',
      '  transition:all 0.2s;',
      '  letter-spacing:-0.01em;',
      '}',
      '.pdf-btn:hover{',
      '  border-color:#0071e3;',
      '  background:rgba(0,113,227,0.12);',
      '  transform:translateY(-1px);',
      '  box-shadow:0 4px 14px rgba(0,113,227,0.2);',
      '}',
      ':root[data-theme="dark"] .pdf-btn{',
      '  color:#2997ff;',
      '  border-color:rgba(41,151,255,0.35);',
      '  background:rgba(41,151,255,0.08);',
      '}',
      ':root[data-theme="dark"] .pdf-btn:hover{',
      '  border-color:#2997ff;',
      '  background:rgba(41,151,255,0.15);',
      '}',
      /* Responsive */
      '@media(max-width:768px){',
      '  .related-grid{ grid-template-columns:1fr; gap:12px; }',
      '  .related-articles-section{ padding:48px 20px 60px; }',
      '  .related-thumb{ height:110px; }',
      '}',
      '@media(min-width:769px) and (max-width:1024px){',
      '  .related-grid{ grid-template-columns:repeat(2,1fr); }',
      '}'
    ].join('\n');
    document.head.appendChild(style);
  }

  /* ─────────────────────────────────────────────────────────────
     6.  INIT
     ───────────────────────────────────────────────────────────── */
  function init() {
    injectCSS();
    initProgressBar();
    updateReadingTime();
    injectPdfButton();
    renderRelated();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
