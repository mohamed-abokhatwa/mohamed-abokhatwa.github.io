/* Shared helpers for the MEP course (Chart.js loaded per-page) */

// Global Chart.js base theme (fonts) — applied if Chart is present
window.applyChartTheme = function(){
  if(!window.Chart) return;
  Chart.defaults.font.family = "-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Roboto,Helvetica,Arial,sans-serif";
  Chart.defaults.font.size = 13;
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

// Back-to-top button (self-contained, matches the rest of the site)
window.initBackToTop = function(){
  if(document.getElementById('back-to-top')) return;
  var btn=document.createElement('button');
  btn.id='back-to-top'; btn.setAttribute('aria-label','Back to top'); btn.title='Back to top';
  btn.innerHTML='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>';
  btn.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
  document.body.appendChild(btn);
  window.addEventListener('scroll',function(){
    var s=window.pageYOffset||document.documentElement.scrollTop, v=s>500;
    btn.style.opacity=v?'1':'0';
    btn.style.pointerEvents=v?'auto':'none';
    btn.style.transform=v?'translateX(-50%) translateY(0)':'translateX(-50%) translateY(10px)';
  },{passive:true});
};

function courseBoot(){
  try{ window.applyChartTheme && applyChartTheme(); }catch(e){}
  try{ window.initScrollSpy && initScrollSpy(); }catch(e){}
  try{ window.initBackToTop && initBackToTop(); }catch(e){}
}
// Run now if the DOM is already parsed (script loaded late), else wait.
if(document.readyState==='loading'){ document.addEventListener('DOMContentLoaded',courseBoot); }
else { courseBoot(); }
