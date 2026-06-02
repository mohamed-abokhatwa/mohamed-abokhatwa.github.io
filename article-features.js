/* article-features.js — Progress Bar · Reading Time · Related Articles
                         Back-to-Top · LinkedIn Share · GA4 Event Tracking
   Include this script in every article page (before </body>) */

(function () {
  'use strict';

  /* ─────────────────────────────────────────────────────────────
     1.  ARTICLES DATA
     ───────────────────────────────────────────────────────────── */
  var ARTICLES = [
    { url:'hammer-transient-tips.html',             title:'Tips for Using HAMMER to Understand Interesting Transient Results',                                       cat:'surge',       thumb:'hammer-transient-tips.webp',           mins:12, tag:'Transient Analysis · Bentley HAMMER' },
    { url:'water-hammer-control-valve.html',       title:'Effect of Control Valve Closure Time on Water Hammer Intensity',                                          cat:'surge',       thumb:'water_hammer_control_valve_v2.webp',   mins:15, tag:'Transient Analysis · Water Hammer' },
    { url:'combination-air-valves.html',           title:'Design Criteria for Combination Air Valves in Long-Distance Transmission Mains',                          cat:'pipeline',    thumb:'combination_air_valves_design_criteria.webp', mins:14, tag:'Transmission Pipeline · Air Management' },
    { url:'surge-vessel.html',                     title:'Sizing the Hydropneumatic Surge Vessel in Water Transmission Pipelines',                                  cat:'surge',       thumb:'surge-vessel.webp',                    mins:10, tag:'Surge Analysis · Hydraulic Design' },
    { url:'hydraulic-mistakes.html',               title:'Common Mistakes in Hydraulic Modeling of Water Transmission Networks',                                    cat:'hydraulic',   thumb:'hydraulic_modeling_mistakes.webp',     mins:8,  tag:'Hydraulic Modeling · Pipeline Design' },
    { url:'pre-charge-pressure.html',              title:'The Pre-Charge Pressure of the Surge Vessel — How One Number Changes Everything',                         cat:'surge',       thumb:'IMG_4656.webp',                        mins:12, tag:'Surge Analysis · Surge Vessel Design' },
    { url:'above-ground-pipeline-design.html',     title:'Engineering Guide: Structural Design of Above-Ground Water Pipelines',                                   cat:'pipeline',    thumb:'above-ground-pipeline-design.webp',    mins:12, tag:'Structural Design · Pipeline Engineering' },
    { url:'control-valve-transients-hammer.html',  title:'Mastering Control Valve Transients in Bentley HAMMER: FCV vs. PRV',                                      cat:'surge',       thumb:'control-valve-transients-hammer.webp', mins:10, tag:'Transient Analysis · Bentley HAMMER' },
    { url:'boundary-conditions-reservoir-tank.html',title:'Demystifying Boundary Conditions: Reservoir vs. Tank in Bentley HAMMER',                               cat:'surge',       thumb:'boundary-conditions-reservoir-tank.webp',mins:9, tag:'Transient Analysis · Bentley HAMMER' },
    { url:'carbon-steel-pipeline-cml.html',        title:'Structural Design Reference: Carbon Steel Pipelines with Cement Mortar Lining',                          cat:'pipeline',    thumb:'carbon-steel-pipeline-cml.webp',      mins:11, tag:'Structural Design · Pipeline Engineering' },
    { url:'npsh-water-infrastructure.html',        title:'Technical Design Guide: Mastering NPSH in Water Infrastructure',                                         cat:'pumps',       thumb:'npsh-water-infrastructure.webp',       mins:10, tag:'Pump Design · NPSH' },
    { url:'transient-analysis-scada.html',         title:'Beyond Static Design: Integrating Transient Analysis with SCADA for Smart Pipelines',                    cat:'surge',       thumb:'transient-analysis-scada.webp',        mins:9,  tag:'SCADA · Digital Twin · Surge Analysis' },
    { url:'cavitation-prvs-fcvs.html',             title:'Technical Design Guide: Managing Cavitation in PRVs and FCVs',                                           cat:'hydraulic',   thumb:'cavitation-prvs-fcvs.webp',            mins:8,  tag:'Hydraulic Design · Cavitation' },
    { url:'wet-well-vortex-design.html',           title:'The Silent Pump Killer: Vortex Formation and Hydraulic Instability in Wet Well Design',                  cat:'pumps',       thumb:'wet-well-vortex-design.webp',          mins:9,  tag:'Pump Station Design · Wet Well' },
    { url:'vfd-myth-hydraulic-design.html',        title:"The VFD Myth: Why Variable Frequency Drives Aren't a 'Magic Fix' for Poor Hydraulic Design",             cat:'pumps',       thumb:'vfd-myth-hydraulic-design.webp',       mins:8,  tag:'Pump Engineering · VFD' },
    { url:'air-valves-pipeline-safety.html',       title:'Air Valves: Just Pipeline Accessories or the Ultimate Safety Guard?',                                    cat:'pipeline',    thumb:'air-valves-pipeline-safety.webp',      mins:9,  tag:'Pipeline Safety · Air Valve Design' },
    { url:'air-admission-networks.html',           title:'Strategic Air Admission in Water Transmission Networks: A Dual Perspective',                             cat:'surge',       thumb:'air-admission-networks.webp',          mins:8,  tag:'Surge Analysis · Air Management' },
    { url:'top-hill-challenge.html',               title:'Managing the "Top Hill" Challenge in Water Transmission Lines',                                          cat:'pipeline',    thumb:'top-hill-challenge.webp',              mins:5,  tag:'Pipeline Design · Surge Analysis' },
    { url:'check-valve-hammer.html',               title:'From Modeling to Procurement: A Guide to Check Valve Analysis in Bentley HAMMER',                        cat:'surge',       thumb:'check-valve-hammer.webp',              mins:5,  tag:'Transient Analysis · Check Valve' },
    { url:'prv-altitude-valve-fcv.html',           title:'Understanding PRV, Altitude Valve, and FCV in Water Transmission Systems',                               cat:'hydraulic',   thumb:'prv-altitude-valve-fcv.webp',          mins:5,  tag:'Hydraulic Control · Valve Selection' },
    { url:'sustainable-pump-selection.html',       title:'Sustainable Pump Selection: Beyond the Duty Point',                                                      cat:'pumps',       thumb:'sustainable-pump-selection.webp',      mins:5,  tag:'Pump Engineering · Energy Efficiency' },
    { url:'steady-state-analysis.html',            title:'Steady State Analysis: The Foundation of Water Transmission Design',                                     cat:'hydraulic',   thumb:'steady-state-analysis.webp',           mins:5,  tag:'Hydraulic Modeling · Steady State' },
    { url:'surge-analysis-risk.html',              title:'Surge Analysis: An Essential Risk Mitigation Strategy for Pressurized Pipelines',                        cat:'surge',       thumb:'surge-analysis-risk.webp',             mins:5,  tag:'Surge Analysis · Risk Management' },
    { url:'design-vs-reality.html',                title:'The Biggest Gap in Engineering: Design vs. Reality',                                                     cat:'leadership',  thumb:'design-vs-reality.webp',               mins:4,  tag:'Engineering Leadership · Field Experience' },
    { url:'engineering-decisions.html',            title:'Making Decisions Under Pressure: Lessons From the Field',                                                cat:'leadership',  thumb:'engineering-decisions.webp',           mins:4,  tag:'Engineering Leadership · Project Management' },
    { url:'envision-sustainability.html',          title:'Sustainability in Infrastructure: A Core Engineering Responsibility',                                    cat:'leadership',  thumb:'envision-sustainability.webp',         mins:4,  tag:'Sustainability · Envision' },
    { url:'infrastructure-at-scale.html',          title:'Managing Infrastructure at Scale: Beyond Technical Complexity',                                          cat:'leadership',  thumb:'infrastructure-at-scale.webp',         mins:4,  tag:'Engineering Leadership · Infrastructure' },
    { url:'sustainability-in-design.html',         title:'From Strategy to Specification: Integrating Sustainability in Engineering Design',                       cat:'leadership',  thumb:'sustainability-in-design.webp',        mins:4,  tag:'Sustainability · Design Coordination' },
    { url:'daf-swro-pretreatment.html',            title:'Technical Deep-Dive: Designing DAF for Large-Scale SWRO Pre-treatment',                                  cat:'desalination',thumb:'daf-swro-pretreatment.webp',           mins:10, tag:'Desalination · DAF · SWRO' },
    { url:'mega-swro-engineering.html',            title:'The Engineering of Scale: Why Standard Design Is Not Enough for Mega SWRO Plants',                       cat:'desalination',thumb:'mega-swro-engineering.webp',          mins:8,  tag:'Desalination · SWRO · Scale Engineering' },
    { url:'swro-pretreatment-dilemma.html',        title:'Design Reference: The Strategic Dilemma in SWRO Pre-treatment',                                          cat:'desalination',thumb:'swro-pretreatment-dilemma.webp',       mins:9,  tag:'Desalination · SWRO · UF' },
    { url:'ro-overdesign-paradox.html',            title:'The Over-Design Paradox: Are Your Safety Margins Actually Killing Your RO Plant?',                       cat:'desalination',thumb:'ro-overdesign-paradox.webp',          mins:7,  tag:'Desalination · RO · Design Philosophy' },
    { url:'chlorine-swro-disinfection.html',       title:'The Chlorine Journey: Disinfection Science in SWRO Plants',                                              cat:'desalination',thumb:'chlorine-swro-disinfection.webp',     mins:3,  tag:'Desalination · SWRO · Chlorination' },
    { url:'offshore-intake-design.html',           title:'Offshore Seawater Intake Design: Six Core Engineering Principles',                                       cat:'desalination',thumb:'offshore-intake-design.webp',          mins:3,  tag:'Desalination · Intake Design · Offshore' },
    { url:'ph-management-swro.html',               title:'pH Management: The Hidden Key to Sustainable SWRO Operation',                                            cat:'desalination',thumb:'ph-management-swro.webp',              mins:3,  tag:'Desalination · SWRO · pH' },
    { url:'onshore-intake-design.html',            title:'Onshore Intake Design: Bridging Hydraulic Theory and Field Reality',                                     cat:'desalination',thumb:'onshore-intake-design.webp',          mins:3,  tag:'Desalination · Intake Design · Onshore' },
    { url:'px-energy-recovery.html',               title:'PX Technology: How Energy Recovery Transformed Desalination Economics',                                  cat:'desalination',thumb:'px-energy-recovery.webp',              mins:3,  tag:'Desalination · Energy Recovery · PX' }
  ];

  /* ─────────────────────────────────────────────────────────────
     2.  GA4 EVENT HELPER
     ───────────────────────────────────────────────────────────── */
  function trackEvent(name, params) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', name, params || {});
    }
  }

  /* ─────────────────────────────────────────────────────────────
     3.  READING PROGRESS BAR  +  article_read_complete event
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
      'background:var(--accent,#0071e3)',
      'z-index:10001',
      'border-radius:0 2px 2px 0',
      'transition:width 0.08s linear',
      'pointer-events:none'
    ].join(';');
    document.body.insertBefore(bar, document.body.firstChild);

    var readFired = false;

    window.addEventListener('scroll', function () {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight = Math.max(
        document.body.scrollHeight,
        document.documentElement.scrollHeight
      ) - window.innerHeight;
      var pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
      bar.style.width = pct + '%';

      // Fire once when reader reaches 90%
      if (!readFired && pct >= 90) {
        readFired = true;
        trackEvent('article_read_complete', {
          page_title: document.title,
          page_path: window.location.pathname
        });
      }
    }, { passive: true });
  }

  /* ─────────────────────────────────────────────────────────────
     4.  READING TIME (auto-compute from article-body)
     ───────────────────────────────────────────────────────────── */
  function updateReadingTime() {
    var body = document.querySelector('.article-body');
    if (!body) return;
    var words = (body.innerText || body.textContent || '').trim().split(/\s+/).length;
    var mins  = Math.max(1, Math.ceil(words / 230));
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
     5.  RELATED ARTICLES
     ───────────────────────────────────────────────────────────── */
  function getRelated() {
    var page = window.location.pathname.split('/').pop() || '';
    var current = null;
    for (var i = 0; i < ARTICLES.length; i++) {
      if (ARTICLES[i].url === page) { current = ARTICLES[i]; break; }
    }
    if (!current) return [];

    var same = [];
    var other = [];
    for (var j = 0; j < ARTICLES.length; j++) {
      if (ARTICLES[j].url === page) continue;
      if (ARTICLES[j].cat === current.cat) same.push(ARTICLES[j]);
      else other.push(ARTICLES[j]);
    }
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
      var safeTitle = a.title.replace(/"/g, '&quot;').replace(/'/g, '&#39;');
      html.push(
        '<a href="' + a.url + '" class="related-card" ' +
          'onclick="if(window.gtag)window.gtag(\'event\',\'related_article_click\',{item_id:\'' + a.url + '\',page_path:window.location.pathname})">',
        '  <div class="related-thumb">',
        '    <img src="' + a.thumb + '" alt="' + safeTitle + '" loading="lazy" onerror="this.parentElement.style.display=\'none\'">',
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

    var footer = document.querySelector('footer');
    if (footer) {
      footer.insertAdjacentHTML('beforebegin', html.join('\n'));
    }
  }

  /* ─────────────────────────────────────────────────────────────
     6.  ARTICLE ACTIONS  —  PDF download  +  LinkedIn share
     ───────────────────────────────────────────────────────────── */
  function injectArticleActions() {
    var byline = document.querySelector('.byline');
    if (!byline) return;

    var pageUrl  = window.location.href;
    var liUrl    = 'https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(pageUrl);
    var safePath = window.location.pathname.replace(/'/g, '');

    var wrap = document.createElement('div');
    wrap.className = 'article-actions-wrap';

    // PDF button
    var pdfBtn = document.createElement('button');
    pdfBtn.className = 'pdf-btn';
    pdfBtn.setAttribute('aria-label', 'Download as PDF');
    pdfBtn.title = 'Save or print this article as PDF';
    pdfBtn.innerHTML =
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/>' +
        '<polyline points="7 10 12 15 17 10"/>' +
        '<line x1="12" y1="15" x2="12" y2="3"/>' +
      '</svg> Download PDF';
    pdfBtn.addEventListener('click', function () {
      trackEvent('pdf_download', { page_title: document.title, page_path: window.location.pathname });
      window.print();
    });

    // LinkedIn share button
    var liBtn = document.createElement('a');
    liBtn.href = liUrl;
    liBtn.target = '_blank';
    liBtn.rel = 'noopener';
    liBtn.className = 'share-btn-li';
    liBtn.setAttribute('aria-label', 'Share on LinkedIn');
    liBtn.innerHTML =
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">' +
        '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>' +
      '</svg> Share on LinkedIn';
    liBtn.addEventListener('click', function () {
      trackEvent('share', {
        method: 'linkedin',
        content_type: 'article',
        item_id: window.location.pathname
      });
    });

    wrap.appendChild(pdfBtn);
    wrap.appendChild(liBtn);

    // Insert the action row right after the byline
    byline.parentNode.insertBefore(wrap, byline.nextSibling);
  }

  /* ─────────────────────────────────────────────────────────────
     7.  BACK-TO-TOP BUTTON
     ───────────────────────────────────────────────────────────── */
  function initBackToTop() {
    var btn = document.createElement('button');
    btn.id = 'back-to-top';
    btn.setAttribute('aria-label', 'Back to top');
    btn.title = 'Back to top';
    btn.innerHTML =
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">' +
        '<polyline points="18 15 12 9 6 15"/>' +
      '</svg>';

    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
      trackEvent('back_to_top', { page_path: window.location.pathname });
    });

    document.body.appendChild(btn);

    window.addEventListener('scroll', function () {
      var scrolled = window.pageYOffset || document.documentElement.scrollTop;
      var visible  = scrolled > 500;
      btn.style.opacity       = visible ? '1' : '0';
      btn.style.pointerEvents = visible ? 'auto' : 'none';
      btn.style.transform     = visible
        ? 'translateX(-50%) translateY(0)'
        : 'translateX(-50%) translateY(10px)';
    }, { passive: true });
  }

  /* ─────────────────────────────────────────────────────────────
     8.  FAB TRACKING  —  WhatsApp + Book Consultation clicks
     ───────────────────────────────────────────────────────────── */
  function initFabTracking() {
    // FABs are injected inline in HTML; wait briefly for DOM readiness
    setTimeout(function () {
      var waFab = document.querySelector('.fab-wa');
      if (waFab) {
        waFab.addEventListener('click', function () {
          trackEvent('whatsapp_click', { page_path: window.location.pathname });
        });
      }
      var consultFab = document.querySelector('.fab-consult');
      if (consultFab) {
        consultFab.addEventListener('click', function () {
          trackEvent('consultation_click', { page_path: window.location.pathname });
        });
      }
    }, 200);
  }

  /* ─────────────────────────────────────────────────────────────
     9.  CSS
     ───────────────────────────────────────────────────────────── */
  function injectCSS() {
    var style = document.createElement('style');
    style.textContent = [

      /* ── Related articles ── */
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
      '  padding:20px;',
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

      /* ── Article actions row (PDF + LinkedIn share) ── */
      '.article-actions-wrap{',
      '  margin-top:20px;',
      '  display:flex;',
      '  gap:10px;',
      '  flex-wrap:wrap;',
      '  align-items:center;',
      '}',

      /* PDF button */
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

      /* LinkedIn share button */
      '.share-btn-li{',
      '  display:inline-flex;',
      '  align-items:center;',
      '  gap:7px;',
      '  padding:9px 20px;',
      '  border-radius:980px;',
      '  border:1.5px solid rgba(0,119,181,0.35);',
      '  background:rgba(0,119,181,0.06);',
      '  font-size:13px;',
      '  font-weight:600;',
      '  color:#0077b5;',
      '  cursor:pointer;',
      '  font-family:inherit;',
      '  text-decoration:none;',
      '  transition:all 0.2s;',
      '  letter-spacing:-0.01em;',
      '}',
      '.share-btn-li:hover{',
      '  border-color:#0077b5;',
      '  background:rgba(0,119,181,0.12);',
      '  transform:translateY(-1px);',
      '  box-shadow:0 4px 14px rgba(0,119,181,0.2);',
      '}',
      ':root[data-theme="dark"] .share-btn-li{',
      '  color:#70b5d9;',
      '  border-color:rgba(112,181,217,0.35);',
      '  background:rgba(112,181,217,0.08);',
      '}',
      ':root[data-theme="dark"] .share-btn-li:hover{',
      '  border-color:#70b5d9;',
      '  background:rgba(112,181,217,0.15);',
      '}',

      /* ── Back-to-top button ── */
      '#back-to-top{',
      '  position:fixed;',
      '  bottom:2rem;',
      '  left:50%;',
      '  transform:translateX(-50%) translateY(10px);',
      '  width:44px;',
      '  height:44px;',
      '  border-radius:50%;',
      '  background:var(--bg-primary,#fff);',
      '  border:1.5px solid var(--border,rgba(0,0,0,0.1));',
      '  box-shadow:0 4px 20px rgba(0,0,0,0.12),0 1px 4px rgba(0,0,0,0.06);',
      '  color:var(--text-primary,#1d1d1f);',
      '  cursor:pointer;',
      '  display:flex;',
      '  align-items:center;',
      '  justify-content:center;',
      '  z-index:9998;',
      '  opacity:0;',
      '  pointer-events:none;',
      '  transition:opacity 0.25s ease, transform 0.25s ease, box-shadow 0.2s ease;',
      '}',
      '#back-to-top:hover{',
      '  box-shadow:0 8px 28px rgba(0,0,0,0.18);',
      '  transform:translateX(-50%) translateY(-2px) !important;',
      '}',
      ':root[data-theme="dark"] #back-to-top{',
      '  background:var(--bg-primary,#1d1d1f);',
      '  border-color:rgba(255,255,255,0.15);',
      '  box-shadow:0 4px 20px rgba(0,0,0,0.4);',
      '}',

      /* ── Table of Contents (collapsible, all screen sizes) ── */
      '#article-toc{ display:none; }',   /* desktop sidebar disabled */
      '.toc-list{',
      '  list-style:none;',
      '  padding:0;',
      '  margin:0;',
      '  display:flex;',
      '  flex-direction:column;',
      '  gap:2px;',
      '}',
      '.toc-list a{',
      '  display:flex;',
      '  align-items:baseline;',
      '  gap:8px;',
      '  padding:6px 8px;',
      '  border-radius:8px;',
      '  font-size:13px;',
      '  line-height:1.4;',
      '  color:var(--text-secondary,#6e6e73);',
      '  text-decoration:none;',
      '  transition:background 0.15s, color 0.15s;',
      '}',
      '.toc-list a:hover{',
      '  background:var(--bg-4,#ededf0);',
      '  color:var(--text-primary,#1d1d1f);',
      '}',
      '.toc-list a.active{',
      '  background:rgba(0,113,227,0.08);',
      '  color:var(--accent,#0071e3);',
      '  font-weight:600;',
      '}',
      '.toc-num{',
      '  font-size:11px;',
      '  font-weight:700;',
      '  color:var(--accent,#0071e3);',
      '  min-width:16px;',
      '  flex-shrink:0;',
      '}',
      /* Collapsible TOC — always visible */
      '#article-toc-mobile{',
      '  margin-bottom:2rem;',
      '  border:1px solid var(--border,rgba(0,0,0,0.08));',
      '  border-radius:14px;',
      '  overflow:hidden;',
      '}',
      '.toc-mobile-toggle{',
      '  width:100%;',
      '  display:flex;',
      '  align-items:center;',
      '  gap:8px;',
      '  padding:14px 16px;',
      '  background:var(--bg-2,#fbfbfd);',
      '  border:none;',
      '  color:var(--text-primary,#1d1d1f);',
      '  font-size:13px;',
      '  font-weight:600;',
      '  font-family:inherit;',
      '  cursor:pointer;',
      '  text-align:left;',
      '}',
      '.toc-chevron{ margin-left:auto; transition:transform 0.2s; }',
      '#article-toc-mobile.open .toc-chevron{ transform:rotate(180deg); }',
      '.toc-mobile-list{',
      '  display:none;',
      '  padding:8px 12px 12px;',
      '  background:var(--bg-2,#fbfbfd);',
      '  border-top:1px solid var(--border,rgba(0,0,0,0.06));',
      '}',
      '#article-toc-mobile.open .toc-mobile-list{ display:flex; }',

      /* ── Inline CTA ── */
      '.inline-cta{',
      '  display:flex;',
      '  align-items:flex-start;',
      '  gap:16px;',
      '  background:rgba(0,113,227,0.05);',
      '  border:1px solid rgba(0,113,227,0.15);',
      '  border-left:4px solid var(--accent,#0071e3);',
      '  border-radius:0 14px 14px 0;',
      '  padding:20px 24px;',
      '  margin:2.5rem 0;',
      '}',
      ':root[data-theme="dark"] .inline-cta{',
      '  background:rgba(41,151,255,0.06);',
      '  border-color:rgba(41,151,255,0.18);',
      '  border-left-color:#2997ff;',
      '}',
      '.inline-cta-icon{ color:var(--accent,#0071e3); flex-shrink:0; display:flex; align-items:center; }',
      '.inline-cta-icon svg{ width:22px; height:22px; }',
      '.inline-cta-title{',
      '  font-size:15px;',
      '  font-weight:700;',
      '  color:var(--text-primary,#1d1d1f);',
      '  margin-bottom:6px;',
      '  letter-spacing:-0.01em;',
      '}',
      '.inline-cta-text{',
      '  font-size:14px;',
      '  color:var(--text-secondary,#6e6e73);',
      '  line-height:1.6;',
      '  margin-bottom:14px;',
      '}',
      '.inline-cta-btn{',
      '  display:inline-flex;',
      '  align-items:center;',
      '  gap:6px;',
      '  padding:9px 20px;',
      '  background:var(--accent,#0071e3);',
      '  color:#fff !important;',
      '  border-radius:980px;',
      '  font-size:13px;',
      '  font-weight:600;',
      '  text-decoration:none;',
      '  transition:opacity 0.2s, transform 0.2s;',
      '}',
      '.inline-cta-btn:hover{ opacity:0.88; transform:translateY(-1px); }',

      /* ── Copy buttons ── */
      '.copy-btn{',
      '  display:inline-flex;',
      '  align-items:center;',
      '  justify-content:center;',
      '  width:22px;',
      '  height:22px;',
      '  border-radius:6px;',
      '  border:1px solid var(--border,rgba(0,0,0,0.1));',
      '  background:var(--bg-3,#fff);',
      '  color:var(--text-tertiary,#86868b);',
      '  cursor:pointer;',
      '  font-size:11px;',
      '  opacity:0;',
      '  margin-left:8px;',
      '  transition:opacity 0.15s, background 0.15s, color 0.15s;',
      '  vertical-align:middle;',
      '  flex-shrink:0;',
      '}',
      'li:hover .copy-btn{ opacity:1; }',
      '.copy-btn.copied{',
      '  background:rgba(52,199,89,0.1);',
      '  border-color:rgba(52,199,89,0.4);',
      '  color:#34c759;',
      '  opacity:1;',
      '}',

      /* ── Responsive ── */
      '@media(max-width:768px){',
      '  .related-grid{ grid-template-columns:1fr; gap:12px; }',
      '  .related-articles-section{ padding:48px 20px 60px; }',
      '  .related-thumb{ height:110px; }',
      '  .pdf-btn,.share-btn-li{ padding:8px 16px; font-size:12px; }',
      '  .inline-cta{ flex-direction:column; gap:10px; padding:16px; }',
      '}',
      '@media(min-width:769px) and (max-width:1024px){',
      '  .related-grid{ grid-template-columns:repeat(2,1fr); }',
      '}'

    ].join('\n');
    document.head.appendChild(style);
  }

  /* ─────────────────────────────────────────────────────────────
     10.  TABLE OF CONTENTS
     ───────────────────────────────────────────────────────────── */
  function buildTOC() {
    var body = document.querySelector('.article-body');
    if (!body) return;
    var headings = body.querySelectorAll('h2');
    if (headings.length < 3) return;

    // Assign IDs to headings
    var items = [];
    headings.forEach(function (h, i) {
      if (!h.id) h.id = 'section-' + (i + 1);
      items.push({ id: h.id, text: h.textContent.trim() });
    });

    var listHTML = items.map(function (item, i) {
      return '<li><a href="#' + item.id + '" data-toc-id="' + item.id + '">' +
               '<span class="toc-num">' + (i + 1) + '</span>' +
               '<span class="toc-text">' + item.text + '</span>' +
             '</a></li>';
    }).join('');

    // Collapsible TOC at top of article (all screen sizes)
    var mobileToc = document.createElement('nav');
    mobileToc.id = 'article-toc-mobile';
    mobileToc.setAttribute('aria-label', 'Article sections');
    mobileToc.innerHTML =
      '<button class="toc-mobile-toggle" aria-expanded="false" ' +
        'onclick="var o=this.parentElement.classList.toggle(\'open\');this.setAttribute(\'aria-expanded\',o)">' +
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>' +
        ' Table of Contents' +
        '<svg class="toc-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>' +
      '</button>' +
      '<ol class="toc-list toc-mobile-list">' + listHTML + '</ol>';
    body.insertBefore(mobileToc, body.firstChild);

    // Highlight active section on scroll
    var allTocLinks = document.querySelectorAll('[data-toc-id]');
    window.addEventListener('scroll', function () {
      var scrollY = window.pageYOffset + 140;
      var activeId = null;
      headings.forEach(function (h) {
        if (h.offsetTop <= scrollY) activeId = h.id;
      });
      allTocLinks.forEach(function (a) {
        a.classList.toggle('active', a.getAttribute('data-toc-id') === activeId);
      });
    }, { passive: true });
  }

  /* ─────────────────────────────────────────────────────────────
     11.  INLINE CONSULTATION CTA
     ───────────────────────────────────────────────────────────── */
  function injectInlineCTA() {
    var body = document.querySelector('.article-body');
    if (!body) return;
    var headings = body.querySelectorAll('h2');
    if (headings.length < 2) return;

    // Insert before the 3rd heading (or last if fewer)
    var targetIdx = Math.min(2, headings.length - 1);
    var target = headings[targetIdx];

    var cta = document.createElement('div');
    cta.className = 'inline-cta';
    cta.innerHTML =
      '<div class="inline-cta-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12.5 7.5L3 21l2-5.5A8.5 8.5 0 1 1 21 11.5z"/></svg></div>' +
      '<div class="inline-cta-body">' +
        '<div class="inline-cta-title">Need expert input on this?</div>' +
        '<div class="inline-cta-text">I work with engineering teams on hydraulic design, surge analysis, and SWRO projects. Happy to review your design or answer specific questions.</div>' +
        '<a href="#" class="inline-cta-btn" ' +
          'onclick="if(typeof Calendly!==\'undefined\'){Calendly.initPopupWidget({url:\'https://calendly.com/mohamed-abokhatwa/30min\'});}else{window.open(\'https://calendly.com/mohamed-abokhatwa/30min\',\'_blank\');}' +
          'if(window.gtag)gtag(\'event\',\'consultation_click\',{source:\'inline_cta\',page_path:window.location.pathname});return false;">' +
          'Book a Free Consultation' +
        '</a>' +
      '</div>';

    target.parentNode.insertBefore(cta, target);
  }

  /* ─────────────────────────────────────────────────────────────
     12.  COPY BUTTONS on list items
     ───────────────────────────────────────────────────────────── */
  function initCopyButtons() {
    var body = document.querySelector('.article-body');
    if (!body) return;
    if (!navigator.clipboard) return;

    var items = body.querySelectorAll('li');
    items.forEach(function (li) {
      var btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.setAttribute('aria-label', 'Copy');
      btn.title = 'Copy to clipboard';
      btn.innerHTML = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>';
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        e.preventDefault();
        // Get text without the copy button's own text
        var text = Array.from(li.childNodes)
          .filter(function (n) { return n !== btn; })
          .map(function (n) { return n.textContent; })
          .join('').trim();
        navigator.clipboard.writeText(text).then(function () {
          btn.innerHTML = '✓';
          btn.classList.add('copied');
          setTimeout(function () {
            btn.innerHTML = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012 2v1"/></svg>';
            btn.classList.remove('copied');
          }, 1800);
        }).catch(function () {});
      });
      li.appendChild(btn);
    });
  }

  /* ─────────────────────────────────────────────────────────────
     13.  INIT
     ───────────────────────────────────────────────────────────── */
  function init() {
    injectCSS();
    initProgressBar();
    updateReadingTime();
    injectArticleActions();
    buildTOC();
    injectInlineCTA();
    initCopyButtons();
    renderRelated();
    initBackToTop();
    initFabTracking();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
