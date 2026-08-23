/* route.js - the homepage sheet: the main in profile, the tower in elevation.
   Generated from design-samples/sea-to-828.html by scripts/mk_route.py */
(function(){
'use strict';
if(!document.querySelector('.rt-sheet')) return;

'use strict';
var $=function(i){return document.getElementById(i);};
var G=9.81, L_KM=42, COVER=1.5, TWL=196, D=1.2, C_HW=130, ETA_M=0.82;
var A=Math.PI*D*D/4, Q=1.2;
var BAR=0.0981, TI=22, ETA_T=0.70, H_TOWER=828, PN=16, PMIN=1.5, PF=12;
var A_WAVE=1000;
var RM=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* -- phase 1: the main --------------------------------------- */
var CP=[[0,4],[2,16],[6,44],[11,70],[17,116],[22,160],[28,198],[33,172],[37,182],[42,185]];
function ground(x){
  if(x<=CP[0][0]) return CP[0][1];
  for(var i=0;i<CP.length-1;i++){
    var a=CP[i],b=CP[i+1];
    if(x>=a[0]&&x<=b[0]){var t=(x-a[0])/(b[0]-a[0]); t=t*t*(3-2*t); return a[1]+(b[1]-a[1])*t;}
  }
  return CP[CP.length-1][1];
}
function pipe(x){ return ground(x)-COVER; }
var VEL=Q/A;
var HF=10.67*(L_KM*1000)*Math.pow(Q,1.852)/(Math.pow(C_HW,1.852)*Math.pow(D,4.87));
function hgl(x){ return TWL+HF*(1-x/L_KM); }
var DH0=A_WAVE*VEL/G;
function envMin(x){ return hgl(x)-DH0*(1-x/L_KM); }
function envMax(x){ return hgl(x)+DH0*(1-x/L_KM); }
var E_MAIN=(hgl(0)-ground(0))/(367*ETA_M);

/* -- phase 2: the tower -------------------------------------- */
var ZD=(PN-PMIN)/BAR, ZF=PF/BAR, ZG=Math.min(ZD,ZF), NZ=Math.ceil(H_TOWER/ZG);
function staticBar(e){ return Math.max(0,e)*BAR; }
function stackPa(e){ return 3460*(1/(5+273.15)-1/(TI+273.15))*Math.max(0,e); }
function windMs(e){ return 8*Math.pow(Math.max(e,10)/10,0.14); }
function liftKWh(h){ return h/(367*ETA_T); }
function halfFrac(e){
  if(e<=0) return 1.14;
  if(e>H_TOWER) return 0;
  var r=e/H_TOWER, f=1-0.50*Math.pow(r,1.4);
  if(r>0.88) f=Math.max(0.05,f*(1-(r-0.88)/0.12*0.82));
  return Math.max(0.05,f);
}

/* -- one journey position: p in [0,1] along, [1,2] up -------- */
var S={p:0,tgt:0,run:false,idle:0,anchors:[]};
function pToCh(p){ return Math.max(0,Math.min(1,p))*L_KM; }
function pToEl(p){ return Math.max(0,Math.min(1,p-1))*H_TOWER; }

var pal={};
function readPal(){
  var c=getComputedStyle(document.documentElement), g=function(n){return c.getPropertyValue(n).trim();};
  pal={ink:g('--ink'),ink3:g('--ink-3'),rule:g('--rule'),water:g('--water'),
       air:g('--air'),fire:g('--fire'),danger:g('--danger'),sheet:g('--sheet')};
}
function rgba(hex,al){
  hex=(hex||'#000').replace('#','');
  if(hex.length===3) hex=hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
  var n=parseInt(hex,16);
  return 'rgba('+((n>>16)&255)+','+((n>>8)&255)+','+(n&255)+','+al+')';
}

/* -- the sheet: two views, one grade line -------------------- */
var cv=$('rt-canvas'), ctx=cv.getContext('2d');
function draw(){
  var w=cv.clientWidth, h=cv.clientHeight;
  if(w<40||h<40) return;
  var dpr=Math.min(window.devicePixelRatio||1,2);
  if(cv.width!==Math.round(w*dpr)){cv.width=Math.round(w*dpr);cv.height=Math.round(h*dpr);}
  ctx.setTransform(dpr,0,0,dpr,0,0);
  ctx.clearRect(0,0,w,h);

  var padT=14, padB=24, split=Math.round(w*0.70);
  var gy = h-padB;                         /* the shared grade line */
  var inA = S.p < 1;

  /* ---------- left view: the main in profile ---------- */
  var ax0=42, ax1=split-16;
  var atop=Math.max(hgl(0),envMax(0))+14, abot=-6;
  var AX=function(km){ return ax0+(km/L_KM)*(ax1-ax0); };
  var AY=function(m){ return gy-((m-abot)/(atop-abot))*(gy-padT); };
  var N=200,i,km;

  ctx.globalAlpha = inA ? 1 : 0.55;
  ctx.font='500 9px "IBM Plex Mono", monospace'; ctx.textBaseline='middle';
  ctx.textAlign='right';
  for(var lv=0; lv<=Math.ceil(atop/100)*100; lv+=100){
    var ly=AY(lv); if(ly<padT-2||ly>gy+2) continue;
    ctx.strokeStyle=rgba(pal.ink,0.09); ctx.lineWidth=1;
    ctx.beginPath(); ctx.moveTo(ax0,Math.round(ly)+0.5); ctx.lineTo(ax1,Math.round(ly)+0.5); ctx.stroke();
    ctx.fillStyle=rgba(pal.ink3,0.95); ctx.fillText(lv,ax0-6,ly);
  }
  ctx.textAlign='center';
  for(km=0;km<=L_KM;km+=10){
    ctx.fillStyle=rgba(pal.ink3,0.95); ctx.fillText(km,AX(km),gy+13);
  }
  /* ground */
  ctx.beginPath(); ctx.moveTo(AX(0),AY(ground(0)));
  for(i=1;i<=N;i++){km=L_KM*i/N; ctx.lineTo(AX(km),AY(ground(km)));}
  ctx.lineTo(ax1,gy); ctx.lineTo(ax0,gy); ctx.closePath();
  ctx.save(); ctx.clip();
  ctx.fillStyle=rgba(pal.ink,0.075); ctx.fillRect(ax0,padT,ax1-ax0,gy-padT);
  ctx.strokeStyle=rgba(pal.ink,0.11); ctx.lineWidth=1;
  for(var gx=ax0-h;gx<ax1+h;gx+=9){ctx.beginPath();ctx.moveTo(gx,gy);ctx.lineTo(gx+h,padT);ctx.stroke();}
  ctx.restore();
  ctx.beginPath(); ctx.moveTo(AX(0),AY(ground(0)));
  for(i=1;i<=N;i++){km=L_KM*i/N; ctx.lineTo(AX(km),AY(ground(km)));}
  ctx.strokeStyle=rgba(pal.ink,0.7); ctx.lineWidth=1.3; ctx.stroke();
  /* separation reach */
  var run=null;
  for(i=0;i<=N;i++){
    km=L_KM*i/N; var bad=envMin(km)<pipe(km);
    if(bad&&run===null) run=km;
    if((!bad||i===N)&&run!==null){
      ctx.fillStyle=rgba(pal.danger,0.12);
      ctx.fillRect(AX(run),padT,Math.max(2,AX(km)-AX(run)),gy-padT); run=null;
    }
  }
  function polyA(fn,col,dash){
    ctx.beginPath();
    for(var k=0;k<=N;k++){var q=L_KM*k/N; var yy=AY(fn(q)); if(k===0)ctx.moveTo(AX(q),yy); else ctx.lineTo(AX(q),yy);}
    ctx.setLineDash(dash||[]); ctx.strokeStyle=col; ctx.lineWidth=1.15; ctx.stroke(); ctx.setLineDash([]);
  }
  polyA(envMax,rgba(pal.air,0.7),[4,3]);
  polyA(envMin,rgba(pal.danger,0.8),[4,3]);
  polyA(pipe,rgba(pal.ink,0.5),[6,3]);
  ctx.beginPath();
  for(i=0;i<=N;i++){km=L_KM*i/N; var hy=AY(hgl(km)); if(i===0)ctx.moveTo(AX(km),hy); else ctx.lineTo(AX(km),hy);}
  ctx.strokeStyle=pal.water; ctx.lineWidth=1.8; ctx.stroke();
  ctx.globalAlpha=1;

  /* ---------- divider + the site ---------- */
  ctx.strokeStyle=rgba(pal.ink,0.22); ctx.lineWidth=1;
  ctx.beginPath(); ctx.moveTo(split-4,padT-6); ctx.lineTo(split-4,gy+8); ctx.stroke();
  /* the shared grade line runs across both views */
  ctx.strokeStyle=rgba(pal.ink,0.85); ctx.lineWidth=1.6;
  ctx.beginPath(); ctx.moveTo(ax0,Math.round(gy)+0.5); ctx.lineTo(w-10,Math.round(gy)+0.5); ctx.stroke();

  /* ---------- right view: the tower in elevation ---------- */
  var bx0=split+16, bx1=w-14;
  var bcx=(bx0+bx1)/2;
  /* a tower has to read as a tower: cap its half-width so the elevation
     stays slender whatever the panel is doing */
  var bhalf=Math.min((bx1-bx0)/2, 44);
  var BY=function(m){ return gy-(m/(H_TOWER*1.05))*(gy-padT); };
  ctx.globalAlpha = inA ? 0.55 : 1;
  ctx.textAlign='left';
  for(var el=0; el<=800; el+=200){
    var ey=BY(el); if(ey<padT-2) continue;
    ctx.strokeStyle=rgba(pal.ink,0.09);
    ctx.beginPath(); ctx.moveTo(bx0,Math.round(ey)+0.5); ctx.lineTo(bx1,Math.round(ey)+0.5); ctx.stroke();
    ctx.fillStyle=rgba(pal.ink3,0.95); ctx.fillText(el, bx1+2>w-4 ? bx0-2 : bx1-22, ey);
  }
  /* silhouette */
  ctx.beginPath();
  var started=false, e2, hf2;
  for(var yy2=padT-4; yy2<=gy; yy2+=3){
    e2=(gy-yy2)/(gy-padT)*(H_TOWER*1.05);
    if(e2>H_TOWER) continue;
    hf2=halfFrac(e2)*bhalf;
    if(!started){ctx.moveTo(bcx-hf2,yy2);started=true;} else ctx.lineTo(bcx-hf2,yy2);
  }
  for(var yy3=gy; yy3>=padT-4; yy3-=3){
    e2=(gy-yy3)/(gy-padT)*(H_TOWER*1.05);
    if(e2>H_TOWER) continue;
    hf2=halfFrac(e2)*bhalf;
    ctx.lineTo(bcx+hf2,yy3);
  }
  if(started){
    ctx.closePath();
    ctx.fillStyle=rgba(pal.ink,0.075); ctx.fill();
    ctx.strokeStyle=rgba(pal.ink,0.6); ctx.lineWidth=1.2; ctx.stroke();
  }
  /* mechanical bands at every zone break */
  ctx.font='500 8.5px "IBM Plex Mono", monospace'; ctx.textAlign='left'; ctx.textBaseline='middle';
  for(var z=1; z*ZG<H_TOWER; z++){
    var be=z*ZG, byT=BY(be+9), byB=BY(be-9), hb=halfFrac(be)*bhalf;
    ctx.fillStyle=rgba(pal.ink,0.16);
    ctx.fillRect(bcx-hb,byT,2*hb,Math.max(1.5,byB-byT));
    ctx.strokeStyle=rgba(pal.ink,0.16); ctx.lineWidth=1;
    ctx.beginPath(); ctx.moveTo(bcx+hb+3,Math.round(BY(be))+0.5); ctx.lineTo(bcx+hb+22,Math.round(BY(be))+0.5); ctx.stroke();
    ctx.fillStyle=rgba(pal.ink3,0.9);
    ctx.fillText('Z'+(z+1)+'  '+Math.round(be)+' m', bcx+hb+26, BY(be));
  }
  ctx.textBaseline='middle';
  /* the two risers */
  [[-1,pal.water],[1,pal.fire]].forEach(function(pr){
    ctx.strokeStyle=rgba(pr[1],0.9); ctx.lineWidth=1.4;
    ctx.beginPath(); var open=false;
    for(var ry=gy; ry>=padT-4; ry-=3){
      var re=(gy-ry)/(gy-padT)*(H_TOWER*1.05);
      if(re>H_TOWER*0.9){open=false;continue;}
      var ox=Math.min(bhalf*0.3, halfFrac(re)*bhalf*0.55);
      if(ox<2){open=false;continue;}
      var rx=bcx+pr[0]*ox;
      if(!open){ctx.moveTo(rx,ry);open=true;} else ctx.lineTo(rx,ry);
    }
    ctx.stroke();
  });
  ctx.globalAlpha=1;

  /* ---------- the marker ---------- */
  ctx.fillStyle=pal.fire; ctx.strokeStyle=rgba(pal.fire,0.9); ctx.lineWidth=1.2;
  ctx.setLineDash([3,3]);
  if(inA){
    var mx=AX(pToCh(S.p));
    ctx.beginPath(); ctx.moveTo(Math.round(mx)+0.5,padT-6); ctx.lineTo(Math.round(mx)+0.5,gy); ctx.stroke();
    ctx.setLineDash([]);
    ctx.beginPath(); ctx.moveTo(mx-4,padT-6); ctx.lineTo(mx+4,padT-6); ctx.lineTo(mx,padT); ctx.closePath(); ctx.fill();
    ctx.beginPath(); ctx.arc(mx,AY(hgl(pToCh(S.p))),3.2,0,6.2832); ctx.fillStyle=pal.water; ctx.fill();
  } else {
    var my=BY(pToEl(S.p));
    ctx.beginPath(); ctx.moveTo(bx0-8,Math.round(my)+0.5); ctx.lineTo(bx1,Math.round(my)+0.5); ctx.stroke();
    ctx.setLineDash([]);
    ctx.beginPath(); ctx.moveTo(bx0-8,my-4); ctx.lineTo(bx0-8,my+4); ctx.lineTo(bx0-3,my); ctx.closePath(); ctx.fill();
  }
  ctx.setLineDash([]);

  /* view labels */
  ctx.font='500 9px "IBM Plex Mono", monospace'; ctx.textAlign='left';
  ctx.fillStyle=rgba(pal.ink3,0.9);
  ctx.fillText('THE MAIN  -  CHAINAGE km', ax0, padT-4);
  ctx.fillText('THE TOWER  -  ELEVATION m', bx0, padT-4);
}

/* -- readouts ------------------------------------------------ */
function set(id,h){var e=$(id); if(e) e.innerHTML=h;}
function txt(id,s){var e=$(id); if(e) e.textContent=s;}
function f(n,d){return (Math.round(n*Math.pow(10,d))/Math.pow(10,d)).toFixed(d);}

/* the Arabic page uses the same engine, so the labels live here */
var AR=(document.documentElement.getAttribute('lang')||'').indexOf('ar')===0;
var T={
  km:      AR?'\u00a0\u0643\u0645':'\u00a0km',
  mAGL:    AR?'\u00a0\u0645':'\u00a0m AGL',
  transmission: AR?'\u062e\u0637 \u0627\u0644\u0646\u0642\u0644':'Transmission',
  inTower: AR?'\u062f\u0627\u062e\u0644 \u0627\u0644\u0628\u0631\u062c':'In the tower',
  ground:  AR?'\u0645\u0646\u0633\u0648\u0628 \u0627\u0644\u0623\u0631\u0636':'Ground',
  hgl:     AR?'\u0627\u0644\u062e\u0637 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u0644\u064a\u0643\u064a':'Hydraulic grade',
  head:    AR?'\u0636\u0627\u063a\u0637 \u0627\u0644\u0636\u063a\u0637':'Pressure head',
  gauge:   AR?'= \u0628\u0627\u0631':'= gauge',
  minTrip: AR?'\u0627\u0644\u0623\u062f\u0646\u0649 \u0639\u0646\u062f \u0627\u0644\u0641\u0635\u0644':'Min on trip',
  energy:  AR?'\u0627\u0644\u0637\u0627\u0642\u0629 \u062d\u062a\u0649 \u0627\u0644\u0622\u0646':'Energy so far',
  zone:    AR?'\u0627\u0644\u0646\u0637\u0627\u0642':'Zone',
  ofN:     AR?' \u0645\u0646 ':' of ',
  unbroken:AR?'\u0627\u0633\u062a\u0627\u062a\u064a\u0643\u064a \u062f\u0648\u0646 \u0642\u0637\u0639':'Static if unbroken',
  inZone:  AR?'\u0627\u0633\u062a\u0627\u062a\u064a\u0643\u064a \u062f\u0627\u062e\u0644 \u0627\u0644\u0646\u0637\u0627\u0642':'Static in zone',
  stack:   AR?'\u0636\u063a\u0637 \u0627\u0644\u0645\u062f\u062e\u0646\u0629':'Stack \u0394p',
  wind:    AR?'\u0633\u0631\u0639\u0629 \u0627\u0644\u0631\u064a\u0627\u062d':'Wind',
  m:       AR?'\u0645':'m',
  bar:     AR?'\u0628\u0627\u0631':'bar'
};
function readout(){
  var inA=S.p<1;
  var ph=$('r-phase');
  if(inA){
    var x=pToCh(S.p), g=ground(x), h=hgl(x), head=h-pipe(x), mn=envMin(x);
    txt('r-pos',f(x,1)); txt('r-unit',T.km);
    ph.textContent=T.transmission; ph.className='rt-ph';
    txt('k1',T.ground); set('r-a',Math.round(g)+'<small>'+T.m+'</small>');
    txt('k2',T.hgl); set('r-b',Math.round(h)+'<small>'+T.m+'</small>');
    txt('k3',T.head); set('r-c',Math.round(head)+'<small>'+T.m+'</small>');
    txt('k4',T.gauge); set('r-d',f(head*BAR,1)+'<small>'+T.bar+'</small>');
    txt('k5',T.minTrip); set('r-e',Math.round(mn)+'<small>'+T.m+'</small>');
    $('r-e').className='rt-v '+(mn<pipe(x)?'rt-v-danger':'rt-v-water');
    txt('k6',T.energy); set('r-f',f(E_MAIN*(x/L_KM),2)+'<small>kWh/m&sup3;</small>');
  } else {
    var e=pToEl(S.p), sb=staticBar(e);
    var zn=Math.min(NZ,Math.floor(e/ZG)+1), res=(e-(zn-1)*ZG)*BAR;
    txt('r-pos',Math.round(e)); txt('r-unit',T.mAGL);
    ph.textContent=T.inTower; ph.className='rt-ph rt-b';
    txt('k1',T.zone); set('r-a',zn+T.ofN+NZ);
    txt('k2',T.unbroken); set('r-b',f(sb,1)+'<small>'+T.bar+'</small>');
    txt('k3',T.inZone); set('r-c',f(res,1)+'<small>'+T.bar+'</small>');
    txt('k4',T.stack); set('r-d',Math.round(stackPa(e))+'<small>Pa</small>');
    txt('k5',T.wind); set('r-e',f(windMs(e),1)+'<small>m/s</small>');
    $('r-e').className='rt-v rt-v-air';
    txt('k6',T.energy); set('r-f',f(E_MAIN+liftKWh(e),2)+'<small>kWh/m&sup3;</small>');
  }
}

/* -- mapping ------------------------------------------------- */
function vpH(){ return window.innerHeight||document.documentElement.clientHeight||800; }
function parseAt(v){
  var m=/^(ch|el):(-?[\d.]+)$/.exec((v||'').trim());
  if(!m) return 0;
  return m[1]==='ch' ? (+m[2])/L_KM : 1+(+m[2])/H_TOWER;
}
function computeAnchors(){
  S.anchors=[].slice.call(document.querySelectorAll('[data-at]')).map(function(el){
    var off=el.classList.contains('rt-dock')?34:110;
    return {y:el.getBoundingClientRect().top+window.pageYOffset+off, p:parseAt(el.dataset.at)};
  }).sort(function(a,b){return a.y-b.y;});
  if(S.anchors.length) S.anchors[0].y=Math.round(vpH()*0.34);
}
function pAt(y){
  var a=S.anchors,i=0;
  if(!a.length) return 0;
  while(i<a.length-2&&y>=a[i+1].y) i++;
  var q=a[i], r=a[i+1]||a[i], dy=Math.max(1,r.y-q.y);
  return q.p+(y-q.y)*((r.p-q.p)/dy);
}

var docks=[].slice.call(document.querySelectorAll('.rt-dock'));
var lastH=0,lastV=0;
function render(){
  readout(); draw();
  var dY=Math.round(vpH()*0.34);
  for(var i=0;i<docks.length;i++){
    var r=docks[i].getBoundingClientRect();
    var on=Math.abs((r.top+34)-dY)<64;
    if(on!==docks[i].classList.contains('at')) docks[i].classList.toggle('at',on);
  }
}
function retarget(){
  var dh=document.body.scrollHeight, vh=vpH();
  if(dh!==lastH||vh!==lastV){lastH=dh;lastV=vh;layout(true);}
  S.tgt=pAt(window.pageYOffset+Math.round(vh*0.34));
}
function frame(){
  S.p+=(S.tgt-S.p)*0.16;
  render();
  if(Math.abs(S.tgt-S.p)>0.0002||S.idle-->0) requestAnimationFrame(frame);
  else S.run=false;
}
function wake(){
  retarget();
  if(RM||document.hidden){S.p=S.tgt;render();return;}
  S.idle=20;
  if(!S.run){S.run=true;requestAnimationFrame(frame);}
}
function layout(quiet){
  computeAnchors(); lastH=document.body.scrollHeight; lastV=vpH();
  if(!quiet) wake();
}


new MutationObserver(function(m){
  for(var i=0;i<m.length;i++) if(m[i].attributeName==='data-theme'){ readPal(); wake(); return; }
}).observe(document.documentElement,{attributes:true});
window.addEventListener('scroll',wake,{passive:true});
window.addEventListener('resize',function(){layout();});
if(document.fonts&&document.fonts.ready) document.fonts.ready.then(function(){layout();});
window.addEventListener('load',function(){layout();});

readPal(); layout();
window.route={S:S,layout:layout,render:render,pAt:pAt,ground:ground,pipe:pipe,hgl:hgl,
  envMin:envMin,staticBar:staticBar,stackPa:stackPa,windMs:windMs,liftKWh:liftKWh,
  E_MAIN:E_MAIN,ZG:ZG,NZ:NZ,VEL:VEL,HF:HF,DH0:DH0,
  set:function(p){S.tgt=p;S.p=p;render();}};
})();
