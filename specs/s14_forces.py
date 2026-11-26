# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A surge program reports heads and flows; the pipe fails at its supports. When a pressure wave runs along a straight leg between two bends, the pressure at one end differs from the pressure at the other, and the difference acts on the pipe as an unbalanced axial force. On the 12&nbsp;km DN800 reference main, a line valve closed instantly at the far end loads a 50&nbsp;m above-ground leg with <strong>733&nbsp;kN</strong> for 48&nbsp;ms. Close the valve in 5&nbsp;s and the same leg sees 81&nbsp;kN. With the series vessel protecting a pump trip, the leg next to the pump sees 17&nbsp;kN. A support designed for the static thrust at a bend, or only for friction along the pipe, can take none of the first. This article shows how to turn the transient results into forces, how a support's natural frequency changes what it feels, and what to hand to the structural engineer.</p>

<h2 id="two-forces">1 &middot; Two different forces</h2>
<p>Pipe supports see two kinds of hydraulic load [1][2]:</p>
<ul class="clean">
  <li><strong>Bend thrust.</strong> At every change of direction, pressure and momentum give a resultant that a thrust block, an anchor or a restrained joint must hold. It exists in steady flow and grows with the surge pressure:
  \(F_b = 2A\left(p + \rho v^2\right)\sin(\theta/2)\).</li>
  <li><strong>Unbalanced force on a leg.</strong> In steady flow the thrusts at the two ends of a straight leg between bends cancel along its axis, apart from friction. While a wave front is inside the leg they do not: one end is at the new pressure and the other at the old. The net axial force is
  \(F_L = \rho g A\,\big(H_1(t) - H_2(t)\big)\), and it lasts as long as the front takes to cross the leg, \(L/a\) [1][3].</li>
</ul>
<p>The second is easy to miss, because a surge model draws envelopes along the line rather than differences between two points at the same instant, yet it is the load that shakes above-ground pipework off its supports, opens restrained joints and fails pipe racks in pump stations.</p>

<h2 id="bend">2 &middot; Bend thrust at the surge pressure</h2>
<p>For the reference main (DN800, \(A\) = 0.503&nbsp;m&sup2;) a 90&deg; bend carries 591&nbsp;kN at the steady 85&nbsp;m, 829&nbsp;kN at the 119&nbsp;m peak of the protected trip, and 1,322&nbsp;kN at the unprotected 190&nbsp;m. The momentum term is small at these velocities (about 1.4&nbsp;kN). Thrust blocks and anchors are designed on the maximum pressure of the envelope at that bend, which is why the envelope must be read at every bend and not only at the pump.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Bend thrust against deflection angle</div>
    <div class="fsub">\(F_b = 2A(\rho g h + \rho v^2)\sin(\theta/2)\), \(\rho\) = 998&nbsp;kg/m&sup3;. Lines for the steady pressure head and the transient maximum at the bend.</div>
  </div>
  <div class="chart-box"><canvas id="bendChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Pipe</label>
      <select id="sD">
        <option value="0.3">DN300</option>
        <option value="0.5">DN500</option>
        <option value="0.8" selected>DN800</option>
        <option value="1.2">DN1200</option>
      </select>
      <div class="hint">Internal area from the nominal diameter.</div>
    </div>
    <div class="ctrl">
      <label>Steady pressure head <span id="vHs">85 m</span></label>
      <input type="range" id="sHs" min="10" max="200" value="85" step="1">
      <div class="hint">At the bend, from the steady model.</div>
    </div>
    <div class="ctrl">
      <label>Transient maximum <span id="vHt">119 m</span></label>
      <input type="range" id="sHt" min="10" max="300" value="119" step="1">
      <div class="hint">From the envelope at the bend.</div>
    </div>
    <div class="ctrl">
      <label>Deflection <span id="vTh">90°</span></label>
      <input type="range" id="sTh" min="5" max="90" value="90" step="1">
      <div class="hint">Angle between the two legs' directions.</div>
    </div>
    <div class="ctrl">
      <label>Velocity <span id="vVv">1.39 m/s</span></label>
      <input type="range" id="sVv" min="0" max="3" value="1.39" step="0.01">
      <div class="hint">Steady.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Steady thrust</div><div class="v" id="rFs">&ndash;</div></div>
    <div class="cell"><div class="k">Transient thrust</div><div class="v" id="rFt">&ndash;</div></div>
    <div class="cell"><div class="k">Increase</div><div class="v" id="rInc">&ndash;</div></div>
    <div class="cell"><div class="k">Momentum part</div><div class="v" id="rMom">&ndash;</div></div>
  </div>
</div>

<h2 id="leg">3 &middot; Unbalanced force on a straight leg</h2>
<p>We took the transient heads at the two ends of a straight leg next to the event and formed \(F_L(t)\) for four cases on the reference main: the pump trip without protection, the pump trip with the series vessel, and a line valve at 12&nbsp;km closing instantly or in 5&nbsp;s. The model uses 50&nbsp;m reaches so the leg ends fall on nodes [4].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Unbalanced axial force on a leg next to the event</div>
    <div class="fsub">\(F_L = \rho g A (H_1 - H_2)\) from method-of-characteristics heads at the two ends of the leg, DN800, \(a\) = 1,050&nbsp;m/s, 50&nbsp;m reaches. Positive acts towards the event (the pump or the valve). Traces thinned for the page, keeping every peak.</div>
  </div>
  <div class="chart-box"><canvas id="legChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Event</label>
      <select id="sCase">
        <option value="trip">Pump trip, no protection</option>
        <option value="vessel">Pump trip, vessel</option>
        <option value="valve0" selected>Line valve closing instantly</option>
        <option value="valve5">Line valve closing in 5 s</option>
      </select>
      <div class="hint">The leg sits at the pump, or at the valve.</div>
    </div>
    <div class="ctrl">
      <label>Leg length</label>
      <select id="sLeg">
        <option value="50" selected>50 m</option>
        <option value="100">100 m</option>
        <option value="200">200 m</option>
      </select>
      <div class="hint">Between the two bends.</div>
    </div>
    <div class="ctrl">
      <label>Time window</label>
      <select id="sWin">
        <option value="all" selected>Whole run</option>
        <option value="peak">2 s around the peak</option>
      </select>
      <div class="hint">Zoom on the largest pulse.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Peak force</div><div class="v" id="rFp">&ndash;</div></div>
    <div class="cell"><div class="k">At</div><div class="v" id="rTp">&ndash;</div></div>
    <div class="cell"><div class="k">Pulse length (half height)</div><div class="v" id="rTd">&ndash;</div></div>
    <div class="cell"><div class="k">L/a</div><div class="v" id="rLa">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">An instant closure sends the full Joukowsky front (149&nbsp;m) into the leg: 733&nbsp;kN whatever the leg length, lasting \(L/a\), from 48&nbsp;ms on a 50&nbsp;m leg to 0.19&nbsp;s on a 200&nbsp;m leg. A 5&nbsp;s closure spreads the front over 5&nbsp;km of pipe, so the head difference across a leg grows with its length: 81, 153 and 273&nbsp;kN for 50, 100 and 200&nbsp;m. The unprotected pump trip peaks at 521&nbsp;kN when cavities near the pump collapse 47&nbsp;s after the trip, a load no envelope shows. The vessel keeps the leg below 30&nbsp;kN.</p>

<h2 id="dlf">4 &middot; What the support feels: dynamic load factor</h2>
<p>A support with a natural period \(T\) does not feel a short pulse as a static load. For a rectangular pulse of duration \(t_d\) applied suddenly, the peak response of a single-degree-of-freedom system, as a multiple of the static response to the same force, is [5][6]</p>
<div class="eq">\[ DLF \;=\; 2\sin\!\left(\frac{\pi t_d}{T}\right) \quad \text{for } \frac{t_d}{T} \le \tfrac12, \qquad DLF = 2 \quad \text{otherwise} \]</div>
<p>and for a load that rises over a time \(t_r\) and then stays,</p>
<div class="eq">\[ DLF \;=\; 1 + \frac{\left|\sin(\pi t_r/T)\right|}{\pi t_r/T} \]</div>
<p>A suddenly applied load that lasts longer than half the support's period doubles its effect. A pulse much shorter than the period is felt only partly. A load that builds slowly compared with the period is felt as static.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Dynamic load factor for the selected pulse</div>
    <div class="fsub">Rectangular pulse (sudden, lasting \(t_d\)) and ramp (rising over \(t_r\), then held), single degree of freedom, undamped. The marker uses the pulse length of the case selected above and the support frequency chosen here.</div>
  </div>
  <div class="chart-box"><canvas id="dlfChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Support natural frequency <span id="vFn">10 Hz</span></label>
      <input type="range" id="sFn" min="1" max="50" value="10" step="1">
      <div class="hint">From the structural engineer, for the direction of the force.</div>
    </div>
    <div class="ctrl">
      <label>Pulse shape</label>
      <select id="sShape">
        <option value="rect" selected>Sudden pulse (front crossing the leg)</option>
        <option value="ramp">Rising load (slow closure)</option>
      </select>
      <div class="hint">How the force arrives.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Support period T</div><div class="v" id="rT">&ndash;</div></div>
    <div class="cell"><div class="k">Pulse / T</div><div class="v" id="rRat">&ndash;</div></div>
    <div class="cell"><div class="k">DLF</div><div class="v" id="rDlf">&ndash;</div></div>
    <div class="cell"><div class="k">Equivalent static force</div><div class="v" id="rFeq">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">A stiff 10&nbsp;Hz support (T = 0.1&nbsp;s) under the instant-closure pulse on a 50&nbsp;m leg (48&nbsp;ms) has t<sub>d</sub>/T = 0.48 and a DLF of 2.0: the support must be designed for about 1,460&nbsp;kN. A flexible 2&nbsp;Hz support sees t<sub>d</sub>/T = 0.1 and a DLF of 0.6, but it moves a long way doing so. For the 5&nbsp;s closure most of the head rise comes in the last moments of the stroke, so the leg still sees a pulse (0.29&nbsp;s on a 50&nbsp;m leg), longer than a stiff support's period: the DLF stays at 2. The slower closure helps by making the force smaller, not the factor.</p>

<h2 id="design">5 &middot; What to hand to the structural engineer</h2>
<ul class="clean">
  <li><strong>Bend thrusts</strong> at the transient maximum pressure of each bend, with the steady value for comparison.</li>
  <li><strong>Leg force histories</strong> \(F_L(t)\) for every straight leg of above-ground or plant-room pipework next to a fast event (pump, check valve, control valve, line valve), for the governing scenarios.</li>
  <li><strong>Peak force, pulse duration and rise time</strong> for each, so a DLF can be applied, or the history itself for a time-history analysis.</li>
  <li><strong>The direction</strong> of each force along the leg, and whether it reverses (it usually does, as the wave reflects).</li>
  <li><strong>The event rate</strong>: a load that happens on every pump stop is a fatigue load for the supports, not only a strength case.</li>
</ul>
<p>The cheapest fix is usually upstream: slow the closure (see <a href="water-hammer-control-valve.html">control valve closure time</a>), protect the trip (see <a href="choosing-surge-protection.html">choosing surge protection</a>), or avoid long straight legs between bends next to fast valves. Burying or restraining the pipe moves the load into the soil and the joints, which must then be checked for it. The static design of above-ground pipe is covered in <a href="above-ground-pipeline-design.html">above-ground pipeline design</a>.</p>

<h2 id="hammer">6 &middot; Getting the forces out of Bentley HAMMER</h2>
<p>HAMMER reports heads, pressures and flows at nodes and along pipes; the force on a leg is a short calculation on two of them [7].</p>
<ol>
  <li><strong>Put nodes at every bend</strong> of the above-ground or plant-room pipework, so each straight leg is one pipe between two nodes, and give the short pipes their real lengths (see <a href="surge-model-time-step-convergence.html">time step and adjustment</a>: short pipes need care).</li>
  <li><strong>Report every time step</strong> at those nodes, so the pulse is not thinned out.</li>
  <li><strong>Export the head histories</strong> of the two end nodes of each leg, and form \(F_L(t) = \rho g A(H_1 - H_2)\) in a spreadsheet; add the bend thrusts from the maximum pressure at each bend.</li>
  <li><strong>Check the pulse is resolved</strong>: the leg must be at least one reach long, and a halved time step must not change the peak.</li>
  <li><strong>Hand over</strong> the peaks, durations, directions and histories with the scenario names.</li>
</ol>

<h2 id="checklist">7 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Bend thrusts</strong> at the transient maximum, at every bend.</li>
  <li><strong>Unbalanced forces on straight legs</strong> next to every fast event, as histories.</li>
  <li><strong>Pulse durations and rise times</strong> given, with a DLF or a time-history analysis.</li>
  <li><strong>Collapse events</strong> included where the column separates: their forces are not in any envelope.</li>
  <li><strong>Supports, anchors and restrained joints</strong> checked for the peak, the reversal and the number of events.</li>
  <li><strong>Upstream fixes considered first</strong>: closure times, protection, layout.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><a href="surge-model-field-validation.html">Validating a surge model with a field pump-trip test</a></li>
    <li><a href="surge-sensitivity-uncertainty.html">Sensitivity and uncertainty: bounding the result</a></li>
    <li><a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip: inertia, specific speed and four-quadrant curves</a></li>
    <li><a href="transient-model-demands-network-detail.html">Demands, branches and dead ends in a transient model</a></li>
    <li><a href="surge-envelope-pipe-pressure-limits.html">Reading the surge envelope against the pipe's real limits</a></li>
    <li><strong>Transient forces on pipe supports and bends</strong></li>
    <li><a href="booster-stations-series-surge.html">Booster stations in series</a></li>
    <li><a href="pump-start-stop-vfd-ramp-surge.html">Pump starts, controlled stops and drive ramps</a></li>
    <li><a href="pipeline-filling-draining-restart-surge.html">Filling, draining and restarting a transmission main</a></li>
    <li><a href="wastewater-force-main-surge.html">Surge in wastewater force mains</a></li>
    <li><a href="surge-study-report-review-checklist.html">The surge study report: what to deliver and what a reviewer checks</a></li>
  </ol>
  The protection devices themselves are covered in the <a href="choosing-surge-protection.html">surge protection design series</a>.
</div>
"""

CHARTS = r"""
const D=__DATA__;
const FF="'IBM Plex Sans', system-ui, sans-serif";
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:FF,size:11}}};
const TTL={family:FF,size:12,weight:'600'};
const LBL={size:10,family:FF};
const LEGF={family:FF,size:11.5};
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1), fmt2=v=>v.toFixed(2), fmt3=v=>v.toFixed(3);
const RHO=998, G=9.81, A_WAVE=1050;
/* ---------- CHART 1 : bend thrust ---------- */
const sD=document.getElementById('sD'), sHs=document.getElementById('sHs'), sHt=document.getElementById('sHt'), sTh=document.getElementById('sTh'), sVv=document.getElementById('sVv');
const TH=[];for(let k=0;k<=90;k+=2)TH.push(k);
const Fb=(A,h,v,th)=>2*A*(RHO*G*h+RHO*v*v)*Math.sin(th*Math.PI/360)/1000;
const bendChart=new Chart(document.getElementById('bendChart'),{
  data:{datasets:[
    {type:'line',label:'At the transient maximum (kN)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.2,pointRadius:0,order:2},
    {type:'line',label:'At the steady pressure (kN)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0,order:3},
    {type:'scatter',label:'Your bend',data:[],backgroundColor:'#111',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:90,title:{display:true,text:'Deflection angle (°)',font:TTL},...AX},y:{type:'linear',min:0,title:{display:true,text:'Resultant thrust (kN)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (kN)','')}: ${fmt0(c.parsed.y)} kN at ${c.parsed.x}°`}}}}
});
function updBend(){
  const Dm=+sD.value, A=Math.PI*Dm*Dm/4, hs=+sHs.value, ht=+sHt.value, th=+sTh.value, v=+sVv.value;
  document.getElementById('vHs').textContent=hs+' m'; document.getElementById('vHt').textContent=ht+' m';
  document.getElementById('vTh').textContent=th+'°'; document.getElementById('vVv').textContent=fmt2(v)+' m/s';
  bendChart.data.datasets[0].data=TH.map(t=>({x:t,y:Fb(A,ht,v,t)}));
  bendChart.data.datasets[1].data=TH.map(t=>({x:t,y:Fb(A,hs,v,t)}));
  bendChart.data.datasets[2].data=[{x:th,y:Fb(A,ht,v,th)}];
  bendChart.update('none');
  const fs=Fb(A,hs,v,th), ft=Fb(A,ht,v,th), fm=2*A*RHO*v*v*Math.sin(th*Math.PI/360)/1000;
  document.getElementById('rFs').innerHTML=fmt0(fs)+' <small>kN</small>';
  document.getElementById('rFt').innerHTML=fmt0(ft)+' <small>kN</small>';
  document.getElementById('rInc').innerHTML=(ft>=fs?'+':'−')+fmt0(Math.abs(100*(ft/fs-1)))+' <small>%</small>';
  document.getElementById('rMom').innerHTML=fmt2(fm)+' <small>kN</small>';
}
[sD,sHs,sHt,sTh,sVv].forEach(s=>s.addEventListener('input',updBend));updBend();

/* ---------- CHART 2 : leg force ---------- */
const sCase=document.getElementById('sCase'), sLeg=document.getElementById('sLeg'), sWin=document.getElementById('sWin');
const legChart=new Chart(document.getElementById('legChart'),{
  data:{datasets:[{type:'line',label:'Unbalanced force on the leg (kN)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.6,pointRadius:0}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,title:{display:true,text:'Time after the event starts (s)',font:TTL},...AX},y:{type:'linear',title:{display:true,text:'Force along the leg (kN)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} kN at ${fmt3(c.parsed.x)} s`}}}}
});
let CUR=null;
function updLeg(){
  const c=D.cases[sCase.value], L=sLeg.value, g=c.legs[L]; CUR=g;
  legChart.data.datasets[0].data=g.t.map((t,k)=>({x:t,y:g.F[k]}));
  const tmax=g.t[g.t.length-1];
  if(sWin.value==='peak'){legChart.options.scales.x.min=Math.max(0,g.t_peak-1); legChart.options.scales.x.max=Math.min(tmax,g.t_peak+1);}
  else {legChart.options.scales.x.min=0; legChart.options.scales.x.max=tmax;}
  const lim=Math.max(50,Math.ceil(g.Fabs*1.1/50)*50); legChart.options.scales.y.min=-lim; legChart.options.scales.y.max=lim;
  legChart.update('none');
  document.getElementById('rFp').innerHTML=fmt1(g.Fabs)+' <small>kN</small>';
  document.getElementById('rTp').innerHTML=fmt2(g.t_peak)+' <small>s</small>';
  document.getElementById('rTd').innerHTML=fmt3(g.pulse)+' <small>s</small>';
  document.getElementById('rLa').innerHTML=fmt3(+L/A_WAVE)+' <small>s</small>';
  updDlf();
}
/* ---------- CHART 3 : DLF ---------- */
const sFn=document.getElementById('sFn'), sShape=document.getElementById('sShape');
const RT=[];for(let k=1;k<=150;k++)RT.push(k*0.02);
const dRect=r=>r<=0.5?2*Math.sin(Math.PI*r):2;
const dRamp=r=>1+Math.abs(Math.sin(Math.PI*r))/(Math.PI*r);
const dlfChart=new Chart(document.getElementById('dlfChart'),{
  data:{datasets:[
    {type:'line',label:'Sudden pulse of length td',data:RT.map(r=>({x:r,y:dRect(r)})),borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2,pointRadius:0,order:2},
    {type:'line',label:'Load rising over tr, then held',data:RT.map(r=>({x:r,y:dRamp(r)})),borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0,order:3},
    {type:'scatter',label:'Selected case',data:[],backgroundColor:'#111',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:3,title:{display:true,text:'Pulse length or rise time / support period',font:TTL},...AX},y:{type:'linear',min:0,max:2.2,title:{display:true,text:'Dynamic load factor',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label}: DLF ${fmt2(c.parsed.y)} at ${fmt2(c.parsed.x)}`}}}}
});
function updDlf(){
  if(!CUR) return;
  const fn=+sFn.value, T=1/fn, td=CUR.pulse, r=td/T, rect=sShape.value==='rect';
  document.getElementById('vFn').textContent=fn+' Hz';
  const d=rect?dRect(r):dRamp(r);
  dlfChart.data.datasets[2].data=[{x:Math.min(r,3),y:d}]; dlfChart.update('none');
  document.getElementById('rT').innerHTML=fmt3(T)+' <small>s</small>';
  document.getElementById('rRat').innerHTML=fmt2(r);
  document.getElementById('rDlf').innerHTML=fmt2(d);
  document.getElementById('rFeq').innerHTML=fmt0(d*CUR.Fabs)+' <small>kN</small>';
}
[sCase,sLeg,sWin].forEach(s=>s.addEventListener('input',updLeg));[sFn,sShape].forEach(s=>s.addEventListener('input',updDlf));updLeg();
window.addEventListener('load',function(){try{[bendChart,legChart,dlfChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: unbalanced forces on pipe segments during transients and fluid-structure interaction.</li>
  <li>AWWA Manual M11 <em>Steel Pipe: A Guide for Design and Installation</em>, and AWWA Manual M41 <em>Ductile-Iron Pipe and Fittings</em>: thrust at bends and the design of restraint.</li>
  <li>Tijsseling, A.S. &ldquo;Fluid-structure interaction in liquid-filled pipe systems: a review.&rdquo; <em>Journal of Fluids and Structures</em>, 10(2), 1996: transient loads on pipe supports and their coupling with the pipe.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the 12&nbsp;km DN800 reference main, its vessel and the verified MOC solver.</li>
  <li>Biggs, J.M. <em>Introduction to Structural Dynamics</em>. McGraw-Hill, 1964: dynamic load factors for rectangular pulses and ramp loads.</li>
  <li>Chopra, A.K. <em>Dynamics of Structures</em>, 4th ed. Pearson, 2012: response of single-degree-of-freedom systems to pulse loads.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: report points, time histories and exporting results.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #PipeSupports #ThrustBlock #BendThrust #UnbalancedForce #DynamicLoadFactor #PipeStress #AboveGroundPipeline #PumpStation #FluidStructureInteraction #BentleyHAMMER #TransientAnalysis #WaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'practice2.json')))['s14']
DATA = {'cases': {k: {'legs': v['legs']} for k, v in _A['cases'].items()}}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='transient-forces-pipe-supports', cat='surge', mins=14,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Transient Forces on Pipe Supports and Bends: From HAMMER Heads to Loads the Structure Can Take',
    reg_title='Transient Forces on Pipe Supports and Bends: From HAMMER Heads to Loads the Structure Can Take',
    reg_tag='Surge Analysis · Pipe Supports · Forces',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Pipe Supports &middot; Forces',
    desc='How to turn surge results into loads: bend thrust at the transient maximum, the unbalanced force on straight legs while a wave crosses them, dynamic load factors for support frequencies, and what to hand to the structural engineer, with three interactive charts and the HAMMER steps.',
    og_desc='An instant valve closure on the DN800 reference main loads a 50 m above-ground leg with 733 kN for 48 ms; a 5 s closure gives 81 kN, and the vessel-protected pump trip 17 kN. A stiff support feels the short pulse twice over.',
    ld_desc='Transient forces in pipelines: bend thrust, unbalanced leg forces from method-of-characteristics heads, dynamic load factors, and the data structural engineers need, with the Bentley HAMMER steps.',
    img_alt='Above-ground DN800 steel pipework in a pump station with bends and pipe supports, force arrows along a straight leg and at a bend, and a sharp pressure pulse travelling along the pipe',
    en_tag='Surge &amp; Transient Analysis &middot; Pipe Supports',
    en_title='Transient Forces on Pipe Supports and Bends: From HAMMER Heads to Loads the Structure Can Take',
    en_excerpt='An instant valve closure on the DN800 reference main loads a 50 m above-ground leg with <strong>733 kN</strong> for 48 ms; a 5 s closure gives <strong>81 kN</strong>, and the vessel-protected pump trip 17 kN. A stiff support feels the short pulse twice over. Bend thrust at the surge pressure, unbalanced forces on straight legs, dynamic load factors and what to give the structural engineer, with three interactive charts.',
    en_search='transient forces pipe supports thrust block bend thrust unbalanced force straight leg wave front water hammer load dynamic load factor DLF natural frequency pipe rack above ground pipework pump station valve closure fluid structure interaction restrained joints anchor Bentley HAMMER export head history structural engineer',
    ar_title='القوى العابرة على دعامات الأنابيب والأكواع: من نتائج HAMMER إلى أحمال يتحملها المنشأ',
    ar_excerpt='إغلاق صمام فوري على الخط المرجعي (قطر ٨٠٠ مم) يحمّل جزءاً مستقيماً فوق الأرض طوله ٥٠ م بقوة <strong>٧٣٣ كيلونيوتن</strong> لمدة ٤٨ جزءاً من الألف من الثانية، بينما يعطي الإغلاق خلال ٥ ثوانٍ <strong>٨١ كيلونيوتن</strong>. قوى الأكواع وقوى الأجزاء المستقيمة ومعامل الحمل الديناميكي، مع ثلاثة رسوم تفاعلية.',
    ar_search='القوى العابرة دعامات الأنابيب كتل الدفع قوة الكوع القوة غير المتوازنة معامل الحمل الديناميكي التردد الطبيعي الأنابيب فوق الأرض محطة الضخ المطرقة المائية الطرق المائي بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
