/* Shared helpers for the MEP course (Chart.js loaded per-page) */

// Global Chart.js base theme (fonts) — applied if Chart is present
window.applyChartTheme = function(){
  if(!window.Chart) return;
  Chart.defaults.font.family = "-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Roboto,Helvetica,Arial,sans-serif";
  Chart.defaults.font.size = 13;
};

// Re-colour every Chart instance for the current light/dark theme
window.themeCharts = function(){
  if(!window.Chart || !Chart.instances) return;
  var cs  = getComputedStyle(document.documentElement);
  var txt = cs.getPropertyValue('--text-primary').trim()   || '#1d1d1f';
  var mut = cs.getPropertyValue('--text-secondary').trim() || '#6e6e73';
  var grid= cs.getPropertyValue('--border').trim()         || 'rgba(0,0,0,0.1)';
  Object.values(Chart.instances).forEach(function(ch){
    var p = ch.options.plugins || {};
    if(p.title)  p.title.color = txt;
    if(p.legend){ p.legend.labels = p.legend.labels || {}; p.legend.labels.color = mut; }
    Object.values(ch.options.scales || {}).forEach(function(sc){
      sc.ticks = sc.ticks || {}; sc.ticks.color = mut;
      sc.grid  = sc.grid  || {}; sc.grid.color  = grid;
      if(sc.title) sc.title.color = mut;
    });
    ch.update('none');
  });
};

// Scroll-spy for the side nav
window.initScrollSpy = function(){
  const links = Array.from(document.querySelectorAll('.sidenav a[href^="#"]'));
  if(!links.length) return;
  const map = links.map(a=>({a, el:document.getElementById(a.getAttribute('href').slice(1))}))
                   .filter(x=>x.el);
  const obs = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        links.forEach(l=>l.classList.remove('active'));
        const hit = map.find(m=>m.el===e.target);
        if(hit) hit.a.classList.add('active');
      }
    });
  },{rootMargin:'-45% 0px -50% 0px'});
  map.forEach(m=>obs.observe(m.el));
};

document.addEventListener('DOMContentLoaded',()=>{
  window.applyChartTheme && applyChartTheme();
  window.themeCharts && themeCharts();
  window.initScrollSpy && initScrollSpy();
  // Re-theme charts whenever the site theme toggles
  if(window.Chart){
    new MutationObserver(()=>window.themeCharts && themeCharts())
      .observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  }
});
