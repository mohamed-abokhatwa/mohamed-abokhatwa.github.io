# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A wastewater force main looks forgiving: a PE pipe with a wave speed near <strong>270&nbsp;m/s</strong> turns a full stop at 1.84&nbsp;m/s into a Joukowsky drop of only <strong>50.5&nbsp;m</strong>, a quarter of what ductile iron would see. But force mains run at low pressure, with small pumps and little inertia, and that 50&nbsp;m is more than the 39&nbsp;m the pump holds. On our 3&nbsp;km DN400 example, the pump's real rundown (2.9&nbsp;kg&middot;m&sup2;) changes nothing: the line goes to vapour at the pump. Ten times that inertia still lets the high point at 1.8&nbsp;km separate. A vessel with <strong>4.3&nbsp;m&sup3;</strong> of gas keeps the line above atmospheric, and then has to live with sewage. This article covers the hydraulics that set wastewater surge apart, the protection options and their trade-offs, the cycle counts that make fatigue matter, and how to model it in HAMMER.</p>

<h2 id="different">1 &middot; What is different about sewage</h2>
<ul class="clean">
  <li><strong>Plastic pipes and low wave speeds.</strong> PE and PVC force mains have wave speeds of 250&ndash;450&nbsp;m/s, and dissolved and entrained gas lowers them further [1][2].</li>
  <li><strong>Low heads.</strong> Force mains lift a few tens of metres, so a moderate downsurge is enough to reach vapour.</li>
  <li><strong>Small, low-inertia pumps,</strong> often submersible, that stop almost at once.</li>
  <li><strong>Gas.</strong> Hydrogen sulfide and other gases collect at high points, and the air valves that release them must be sewage types that will not foul.</li>
  <li><strong>Solids.</strong> They limit what can be put in the line: small orifices clog, and vessels and check valves must tolerate rags and grit.</li>
  <li><strong>Many cycles.</strong> Pumps start and stop on wet-well level, many times an hour, every day.</li>
</ul>

<h2 id="wave-speed">2 &middot; Wave speed and Joukowsky in plastic pipe</h2>
<p>For a thin-walled pipe anchored against axial movement, the wave speed is [1][3]</p>
<div class="eq">\[ a \;=\; \sqrt{\frac{K/\rho}{1 + \dfrac{K}{E}\,(SDR-1)}}, \qquad \Delta H = \frac{a\,v}{g} \]</div>
<p>For PE100 at SDR17, with a short-term modulus of 1.2&nbsp;GPa at about 20&nbsp;&deg;C, this gives __A__&nbsp;m/s, and a stop from __V__&nbsp;m/s gives __J__&nbsp;m. The modulus of PE falls with temperature and load duration, so the wave speed in a warm sewer is lower still; take the manufacturer's dynamic modulus, and bracket it (see <a href="surge-sensitivity-uncertainty.html">sensitivity</a> and <a href="wave-speed-surge-analysis.html">wave speed</a>, which also covers gas content).</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Wave speed and stopping surge by pipe material</div>
    <div class="fsub">\(a = \sqrt{(K/\rho)/(1 + (K/E)(SDR-1))}\) with \(K\) = 2.2&nbsp;GPa, \(\rho\) = 998&nbsp;kg/m&sup3;, no free gas. Curves against SDR for PE100 and PVC-U at the chosen moduli; ductile iron (K9-type wall, \(E\) = 170&nbsp;GPa, D/e about 60) shown as a reference line.</div>
  </div>
  <div class="chart-box"><canvas id="aChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Material</label>
      <select id="sMat">
        <option value="pe" selected>PE100</option>
        <option value="pvc">PVC-U</option>
      </select>
      <div class="hint">For the readouts.</div>
    </div>
    <div class="ctrl">
      <label>SDR <span id="vSdr">17</span></label>
      <input type="range" id="sSdr" min="0" max="6" value="3" step="1">
      <div class="hint">Outside diameter over wall thickness.</div>
    </div>
    <div class="ctrl">
      <label>PE modulus <span id="vEpe">1.20 GPa</span></label>
      <input type="range" id="sEpe" min="0.6" max="1.6" value="1.2" step="0.05">
      <div class="hint">Short-term, at operating temperature.</div>
    </div>
    <div class="ctrl">
      <label>Velocity stopped <span id="vVel">1.84 m/s</span></label>
      <input type="range" id="sVel" min="0.5" max="3" value="1.84" step="0.01">
      <div class="hint">Pump stopping at once.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Wave speed</div><div class="v" id="rA">&ndash;</div></div>
    <div class="cell"><div class="k">Joukowsky a·v/g</div><div class="v" id="rJ">&ndash;</div></div>
    <div class="cell"><div class="k">Ductile iron, same velocity</div><div class="v" id="rJdi">&ndash;</div></div>
    <div class="cell"><div class="k">2L/a for 3 km</div><div class="v" id="rTla">&ndash;</div></div>
  </div>
</div>

<h2 id="example">3 &middot; The example force main</h2>
<p>A wet well with its water level 2&nbsp;m above the pump lifts 0.18&nbsp;m&sup3;/s through 3&nbsp;km of PE100 SDR17 DN400 (353&nbsp;mm bore) to a discharge manhole whose water level is at 17.0&nbsp;m. The main rises to 6&nbsp;m in its first 300&nbsp;m, to a high point of 12&nbsp;m at 1.8&nbsp;km, dips to 9&nbsp;m and climbs to 16&nbsp;m at the manhole. Friction at a Darcy factor of 0.015 is __HF__&nbsp;m, so the pump delivers __HP__&nbsp;m (__P__&nbsp;kW at 1,480&nbsp;rpm, inertia __I__&nbsp;kg&middot;m&sup2; from the correlation in <a href="pump-trip-data-inertia-specific-speed.html">pump data</a>). The steady pressure is 39&nbsp;m at the pump, 13.8&nbsp;m at the high point and 2.9&nbsp;m just before the manhole. Every point except the manhole itself sits below the discharge level once the pumps stop, so the line stays full at rest. Because the pressure near the outlet is only 2.9&nbsp;m in normal running, the design criterion here is no sub-atmospheric pressure (0&nbsp;m) rather than +3&nbsp;m; as always, check it against the project specification and the manufacturers' ratings.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pump trip on the force main</div>
    <div class="fsub">Method-of-characteristics model with a vapour cavity model, a = __A__&nbsp;m/s, 50&nbsp;m reaches, 120&nbsp;s. Pressure head envelopes along the main, with the steady pressure. The outlet manhole is the last point.</div>
  </div>
  <div class="chart-box"><canvas id="fmChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Case</label>
      <select id="sCase">
        <option value="instant">Pump stops at once</option>
        <option value="inertia" selected>Real rundown, 2.9 kg·m²</option>
        <option value="fly">Rundown with 10 times the inertia</option>
        <option value="vessel">Vessel at the pump</option>
      </select>
      <div class="hint">Ideal check valve at the pump in every case.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Lowest pressure</div><div class="v" id="rMin">&ndash;</div></div>
    <div class="cell"><div class="k">Where</div><div class="v" id="rX" style="font-size:15px;margin-top:6px;">&ndash;</div></div>
    <div class="cell"><div class="k">Highest pressure</div><div class="v" id="rMax">&ndash;</div></div>
    <div class="cell"><div class="k">Largest vapour cavity</div><div class="v" id="rCav">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict at 0 m</div><div class="v" style="font-size:14px;margin-top:6px;" id="rVer">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">Stopping at once, the pump end goes to vapour and the cavity collapse lifts the peak to 54.5&nbsp;m. The real rundown barely helps: vapour at the pump, a peak of 40.7&nbsp;m. Ten times the inertia moves the trouble to the high point (vapour at 1.75&nbsp;km). The vessel, __G0__&nbsp;m&sup3; of gas growing to __GM__&nbsp;m&sup3;, keeps every point at or above atmospheric, the lowest being the high point.</p>

<h2 id="protection">4 &middot; Protection options for sewage</h2>
<div class="tbl-wrap"><table>
  <caption>Surge protection on wastewater force mains: what works and what it costs</caption>
  <thead><tr><th>Option</th><th>Effect on the downsurge</th><th>Wastewater concerns</th></tr></thead>
  <tbody>
    <tr><td>Sewage air valves at high points</td><td>Admit air to stop separation at the high points; cushion the collapse</td><td>Must be sewage types with long bodies and anti-fouling; need maintenance; release odour; the air admitted must be expelled slowly</td></tr>
    <tr><td>Added inertia (flywheel)</td><td>Slows the stop; on short mains can avoid separation</td><td>Rarely practical on submersible pumps; ten times the inertia was not enough here</td></tr>
    <tr><td>Hydropneumatic vessel (air-over-water)</td><td>Supplies water at the pump; keeps the whole line up</td><td>Solids and grease in the vessel, H<sub>2</sub>S in the gas space, level instruments fouling; needs flushing and inspection</td></tr>
    <tr><td>Bladder vessel</td><td>Same, with the gas separated from the sewage</td><td>Bladder material must resist sewage; the connection must not trap solids</td></tr>
    <tr><td>Larger, slower pumps or a drive ramp</td><td>Controlled stops become harmless (see <a href="pump-start-stop-vfd-ramp-surge.html">normal operations</a>)</td><td>Does nothing for a power failure</td></tr>
    <tr><td>Stronger pipe class</td><td>Accepts the maximum; may tolerate vacuum (see <a href="surge-envelope-pipe-pressure-limits.html">pipe limits</a>)</td><td>Column separation still happens; collapse peaks are model-dependent</td></tr>
  </tbody>
</table></div>
<p>In our practice, sewage air valves at the high points with a stronger pipe class are the usual answer on short force mains, and a vessel only where the separation is severe or long-lasting. Vessels on sewage are avoided where possible because of the maintenance they demand, not because they do not work hydraulically [4][5].</p>

<h2 id="cycles">5 &middot; Cycles: why fatigue matters on force mains</h2>
<p>A wet well controlled on level can start and stop its pumps several times an hour. Each start and each stop is a pressure cycle, and on plastic pipe the number of cycles sets the life (see <a href="surge-envelope-pipe-pressure-limits.html">the pipe's real limits</a>). For PVC the Folkman method gives the cycles to failure from the stress amplitude [6]:</p>
<div class="eq">\[ \sigma_{amp} = \frac{(P_{max}-P_{min})(DR-1)}{4}, \qquad N = 10^{\,-4.196\log_{10}\sigma_{amp} + 17.76} \]</div>
<p>For PE the industry approach is to keep the recurring total pressure within 1.5 times the pressure class [7].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pump cycles and pipe life</div>
    <div class="fsub">Cycles per year from the starts per hour (a start and a stop are two cycles). PVC: Folkman cyclic life, divided by 2 as a margin. PE: recurring maximum against 1.5 &times; PC. Pressures in bar gauge; 1&nbsp;bar = 10.21&nbsp;m.</div>
  </div>
  <div class="chart-box"><canvas id="cyChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Starts per hour <span id="vSph">6</span></label>
      <input type="range" id="sSph" min="1" max="15" value="6" step="1">
      <div class="hint">Per pump, at peak inflow.</div>
    </div>
    <div class="ctrl">
      <label>Recurring maximum <span id="vPx">4.0 bar</span></label>
      <input type="range" id="sPx" min="1" max="10" value="4" step="0.1">
      <div class="hint">From the model, at the critical point.</div>
    </div>
    <div class="ctrl">
      <label>Recurring minimum <span id="vPn">−0.9 bar</span></label>
      <input type="range" id="sPn" min="-0.95" max="3" value="-0.9" step="0.05">
      <div class="hint">Vapour is about −0.96 bar.</div>
    </div>
    <div class="ctrl">
      <label>PVC DR <span id="vDr">18</span></label>
      <input type="range" id="sDr" min="0" max="3" value="1" step="1">
      <div class="hint">14, 18, 21 or 25.</div>
    </div>
    <div class="ctrl">
      <label>PE pressure class <span id="vPc">10 bar</span></label>
      <input type="range" id="sPc" min="6" max="16" value="10" step="1">
      <div class="hint">PN of the PE pipe.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Cycles per year</div><div class="v" id="rCy">&ndash;</div></div>
    <div class="cell"><div class="k">PVC cycles to failure</div><div class="v" id="rN">&ndash;</div></div>
    <div class="cell"><div class="k">PVC life with margin 2</div><div class="v" id="rLife">&ndash;</div></div>
    <div class="cell"><div class="k">PE: max against 1.5 PC</div><div class="v" style="font-size:14px;margin-top:6px;" id="rPe">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">Six starts an hour around the clock is 105,000 cycles a year, more than a water transmission main sees in a decade. With the example's unprotected stop (about 4.0&nbsp;bar at the pump down to vapour), PVC DR18 has a cyclic life of about 107 years with the margin of 2, and PE PN10 is far inside 1.5 &times; PC. Life falls with roughly the fourth power of the swing: at 10 starts an hour the same pipe gives 64 years, and a 7&nbsp;bar swing at six starts an hour gives 24.</p>

<h2 id="hammer">6 &middot; Modelling it in Bentley HAMMER</h2>
<p>Field names differ slightly between versions [8].</p>
<ol>
  <li><strong>Model the wet well</strong> as a reservoir or tank at its lowest operating level, which gives the lowest pressures, and repeat at the highest.</li>
  <li><strong>Set the wave speed</strong> from the pipe's dynamic modulus and SDR with the Wave Speed Calculator, and bracket it for temperature and gas.</li>
  <li><strong>Enter the pump's own inertia</strong>; submersible sets are often an order of magnitude below dry-well sets of the same power.</li>
  <li><strong>Model the discharge manhole</strong> as a reservoir at its water level, and check that no part of the main sits above it, or the line will drain at rest.</li>
  <li><strong>Add sewage air valves</strong> as air valve elements at every high point, with the manufacturer's inflow and outflow orifices, and check that they do not admit air during normal operation.</li>
  <li><strong>Run the trip and the normal stop</strong>, and export the recurring pressure range at the critical points for the fatigue check.</li>
  <li><strong>Check the check valve</strong> on each pump against slam with its dynamic characteristic (see <a href="check-valve-hammer.html">check valve slam</a>), since sewage check valves are often slow-closing swing types.</li>
</ol>

<h2 id="checklist">7 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Wave speed</strong> from the dynamic modulus, bracketed for temperature and gas.</li>
  <li><strong>Pump inertia</strong> from the real (often submersible) set.</li>
  <li><strong>Profile against the discharge level</strong>, so the line stays full at rest.</li>
  <li><strong>Criterion stated</strong> and checked against the specification and the manufacturers' ratings.</li>
  <li><strong>Protection chosen with maintenance in mind</strong>: sewage air valves, pipe class, vessel only where needed.</li>
  <li><strong>Cycles counted</strong> and the fatigue checked for plastic pipe.</li>
  <li><strong>Check valves</strong> checked for slam.</li>
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
    <li><a href="transient-forces-pipe-supports.html">Transient forces on pipe supports and bends</a></li>
    <li><a href="booster-stations-series-surge.html">Booster stations in series</a></li>
    <li><a href="pump-start-stop-vfd-ramp-surge.html">Pump starts, controlled stops and drive ramps</a></li>
    <li><a href="pipeline-filling-draining-restart-surge.html">Filling, draining and restarting a transmission main</a></li>
    <li><strong>Surge in wastewater force mains</strong></li>
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
const sgn=(v,d)=>(v<-0.0049?'−':(v>0.0049?'+':''))+Math.abs(v).toFixed(d);
const G=9.81, KW=2.2e9, RHO=998, VAP=-9.8, M2B=10.21;
const good=t=>'<span class="badge good">'+t+'</span>', bad=t=>'<span class="badge bad">'+t+'</span>';
const hl=(v,txt,col,pos)=>({type:'line',yMin:v,yMax:v,borderColor:col,borderWidth:1.3,borderDash:[6,4],label:{display:true,content:txt,position:pos||'end',font:LBL,color:'#fff',backgroundColor:col}});
const aOf=(E,sdr)=>Math.sqrt((KW/RHO)/(1+KW/E*(sdr-1)));
/* ---------- CHART 1 : wave speed ---------- */
const SDRS=[11,13.6,17,21,26,33,41], sMat=document.getElementById('sMat'), sSdr=document.getElementById('sSdr'), sEpe=document.getElementById('sEpe'), sVel=document.getElementById('sVel');
const SX=[];for(let k=0;k<=60;k++)SX.push(9+k*0.55);
const A_DI=aOf(170e9,61);
const aChart=new Chart(document.getElementById('aChart'),{
  data:{datasets:[
    {type:'line',label:'PE100',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:0,order:2},
    {type:'line',label:'PVC-U (E 3.0 GPa)',data:SX.map(s=>({x:s,y:aOf(3.0e9,s)})),borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2,pointRadius:0,order:3},
    {type:'scatter',label:'Your pipe',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:9,max:42,title:{display:true,text:'SDR',font:TTL},...AX},y:{type:'linear',min:0,max:1300,title:{display:true,text:'Wave speed (m/s)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt0(c.parsed.y)} m/s at SDR ${fmt1(c.parsed.x)}`}},
      annotation:{annotations:{di:hl(A_DI,'ductile iron ≈ '+Math.round(A_DI)+' m/s','rgba(127,140,141,0.9)','start')}}}}
});
function upd1(){
  const pe=sMat.value==='pe', sdr=SDRS[+sSdr.value], E=pe?(+sEpe.value)*1e9:3.0e9, v=+sVel.value;
  document.getElementById('vSdr').textContent=String(sdr); document.getElementById('vEpe').textContent=fmt2(+sEpe.value)+' GPa'; document.getElementById('vVel').textContent=fmt2(v)+' m/s';
  aChart.data.datasets[0].data=SX.map(s=>({x:s,y:aOf((+sEpe.value)*1e9,s)})); aChart.data.datasets[0].label='PE100 (E '+fmt2(+sEpe.value)+' GPa)';
  const a=aOf(E,sdr); aChart.data.datasets[2].data=[{x:sdr,y:a}]; aChart.update('none');
  document.getElementById('rA').innerHTML=fmt0(a)+' <small>m/s</small>';
  document.getElementById('rJ').innerHTML=fmt1(a*v/G)+' <small>m</small>';
  document.getElementById('rJdi').innerHTML=fmt0(A_DI*v/G)+' <small>m</small>';
  document.getElementById('rTla').innerHTML=fmt1(6000/a)+' <small>s</small>';
}
[sMat,sSdr,sEpe,sVel].forEach(s=>s.addEventListener('input',upd1));upd1();
/* ---------- CHART 2 : force main ---------- */
const sCase=document.getElementById('sCase'), X=D.x.map(x=>x/1000), STEADY=D.hgl.map((h,i)=>h-D.z[i]);
const fmChart=new Chart(document.getElementById('fmChart'),{
  data:{datasets:[
    {type:'line',label:'Maximum (m)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2,pointRadius:0},
    {type:'line',label:'Minimum (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:0},
    {type:'line',label:'Steady (m)',data:X.map((x,i)=>({x:x,y:STEADY[i]})),borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.2,borderDash:[5,4],pointRadius:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:3,title:{display:true,text:'Chainage from the pump (km)',font:TTL},...AX},y:{type:'linear',min:-12,max:60,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt2(c.parsed.x)} km`}},
      annotation:{annotations:{z:hl(0,'atmospheric','rgba(30,132,73,0.85)','start'),v:hl(VAP,'vapour','rgba(192,57,43,0.85)'),
        hp:{type:'line',xMin:1.8,xMax:1.8,borderColor:'#6b4f9e',borderWidth:1,borderDash:[3,3],label:{display:true,content:'high point',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}}}}}
});
function upd2(){
  const c=D.cases[sCase.value];
  fmChart.data.datasets[0].data=X.map((x,i)=>({x:x,y:c.Hmax[i]})); fmChart.data.datasets[1].data=X.map((x,i)=>({x:x,y:c.Hmin[i]})); fmChart.update('none');
  document.getElementById('rMin').innerHTML=sgn(c.line_min,2)+(c.line_min<=VAP+0.05?' <small>(vapour)</small>':' <small>m</small>');
  document.getElementById('rX').innerHTML=c.x_min===0?'at the pump':'at '+fmt2(c.x_min/1000)+' km';
  document.getElementById('rMax').innerHTML=fmt1(c.line_max)+' <small>m</small>';
  document.getElementById('rCav').innerHTML=fmt3(c.cav)+' <small>m³</small>';
  document.getElementById('rVer').innerHTML=c.line_min>=-0.005?good('no vacuum'):bad('vacuum on the line');
}
sCase.addEventListener('input',upd2);upd2();
/* ---------- CHART 3 : cycles ---------- */
const sSph=document.getElementById('sSph'), sPx=document.getElementById('sPx'), sPn=document.getElementById('sPn'), sDr=document.getElementById('sDr'), sPc=document.getElementById('sPc');
const DRS=[14,18,21,25], PSI=14.5038;
const Ncyc=(dp,dr)=>Math.pow(10,-4.196*Math.log10(dp*PSI*(dr-1)/4)+17.76);
const SPH=[];for(let k=1;k<=15;k++)SPH.push(k);
const cyChart=new Chart(document.getElementById('cyChart'),{
  data:{datasets:[
    {type:'line',label:'PVC life with margin 2 (years)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.2,pointRadius:3,order:2},
    {type:'scatter',label:'Your station',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:1,max:15,title:{display:true,text:'Starts per hour',font:TTL},...AX},y:{type:'logarithmic',min:1,max:100000,title:{display:true,text:'PVC cyclic life (years, log scale)',font:TTL},grid:{color:'#eef2f5'},
      ticks:{font:{family:FF,size:11},callback:v=>[1,10,100,1000,10000,100000].includes(v)?fmt0(v):''}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} years at ${c.parsed.x} starts per hour`}},
      annotation:{annotations:{life:{type:'line',yMin:50,yMax:50,borderColor:'#6b4f9e',borderWidth:1.2,borderDash:[4,4],label:{display:true,content:'50-year design life',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}}}}}
});
function upd3(){
  const sph=+sSph.value, px=+sPx.value, pn=+sPn.value, dr=DRS[+sDr.value], pc=+sPc.value;
  document.getElementById('vSph').textContent=sph; document.getElementById('vPx').textContent=fmt1(px)+' bar';
  document.getElementById('vPn').textContent=sgn(pn,2)+' bar'; document.getElementById('vDr').textContent=dr; document.getElementById('vPc').textContent=pc+' bar';
  const dp=Math.max(0.01,px-pn), cyc=sph*2*24*365, N=Ncyc(dp,dr);
  cyChart.data.datasets[0].data=SPH.map(s=>({x:s,y:Math.max(1,N/(s*2*24*365)/2)}));
  cyChart.data.datasets[1].data=[{x:sph,y:Math.max(1,N/cyc/2)}]; cyChart.update('none');
  document.getElementById('rCy').innerHTML=fmt0(cyc);
  document.getElementById('rN').innerHTML=N>=1e6?(N/1e6).toFixed(1)+' <small>million</small>':fmt0(N);
  document.getElementById('rLife').innerHTML=N/cyc/2>=1000?'> 1,000 <small>years</small>':fmt0(N/cyc/2)+' <small>years</small>';
  document.getElementById('rPe').innerHTML=px<=1.5*pc?good(fmt1(px)+' ≤ '+fmt1(1.5*pc)+' bar'):bad(fmt1(px)+' > '+fmt1(1.5*pc)+' bar');
}
[sSph,sPx,sPn,sDr,sPc].forEach(s=>s.addEventListener('input',upd3));upd3();
window.addEventListener('load',function(){try{[aChart,fmChart,cyChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: wave speed in thin-walled and plastic pipes, and the Joukowsky relation.</li>
  <li>Plastics Pipe Institute. <em>Handbook of Polyethylene Pipe</em>, 2nd ed., 2008: dynamic modulus and wave speed of PE pipe, and surge in PE systems.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: wave speeds, pumped sewage mains and air valves.</li>
  <li>Water Environment Federation. <em>Design of Wastewater and Stormwater Pumping Stations</em> (MOP FD-4) and Jones, G.M. et al. <em>Pumping Station Design</em>, 3rd ed. Butterworth-Heinemann, 2006: force main design, surge control and air valves for wastewater.</li>
  <li>AWWA Manual M51 <em>Air Valves</em>: air valves for wastewater service.</li>
  <li>Folkman, S. &amp; Parvez, J. &ldquo;PVC pipe cyclic design method.&rdquo; ASCE Pipelines 2020; Uni-Bell PVC Pipe Association, <em>Force Main Design Guide for PVC Pipe</em> and Cyclic-Life Calculator.</li>
  <li>AWWA C906 and Manual M55 <em>PE Pipe: Design and Installation</em>: recurring surge allowance of 1.5 &times; PC.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: wave speed calculator, air valve elements, pumps and check valves.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #Wastewater #ForceMain #SewagePumping #PEPipe #PVCPipe #WaveSpeed #SewageAirValve #ColumnSeparation #Fatigue #PumpCycles #SurgeVessel #BentleyHAMMER #WastewaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'practice2.json')))['s19']
DATA = {'x': _A['x'], 'z': _A['z'], 'hgl': _A['hgl'], 'cases': {k: {q: v[q] for q in ('line_min', 'x_min', 'line_max', 'cav', 'Hmin', 'Hmax')} for k, v in _A['cases'].items()}}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))
_v = _A['cases']['vessel']
for k, v in {'__A__': '%.0f' % _A['a'], '__V__': '%.2f' % _A['v'], '__J__': '%.1f' % _A['jouk'], '__HF__': '%.1f' % _A['hf'], '__HP__': '%.1f' % _A['Hp'],
             '__P__': '%.0f' % _A['P'], '__I__': '%.1f' % _A['I'], '__G0__': '%.2f' % _v['gas0'], '__GM__': '%.2f' % _v['gas_max']}.items():
    BODY = BODY.replace(k, v)

SPEC = dict(
    slug='wastewater-force-main-surge', cat='surge', mins=14,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Surge in Wastewater Force Mains: Plastic Pipe, Low Heads, Sewage Air Valves and Thousands of Cycles',
    reg_title='Surge in Wastewater Force Mains: Plastic Pipe, Low Heads, Sewage Air Valves and Thousands of Cycles',
    reg_tag='Surge Analysis · Wastewater · Force Mains',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Wastewater &middot; Force Mains',
    desc='Surge in wastewater force mains: wave speed in PE and PVC, a 3 km DN400 PE force main tripped with and without inertia and a vessel, protection options for sewage, the cycle counts of level-controlled pumps and their fatigue effect, and the HAMMER set-up, with three interactive charts.',
    og_desc='On a 3 km DN400 PE force main the Joukowsky drop is only 50.5 m, yet the line goes to vapour at the pump; ten times the pump inertia still lets the high point separate. A vessel with 4.3 m³ of gas keeps it above atmospheric.',
    ld_desc='Wastewater force main surge: plastic pipe wave speed, pump trip with low inertia, protection choices for sewage, cycle counts and fatigue, with the Bentley HAMMER set-up.',
    img_alt='A wastewater pumping station with submersible pumps in a wet well, a PE force main rising over a high point with a sewage air valve, and a discharge manhole at the end',
    en_tag='Surge &amp; Transient Analysis &middot; Wastewater',
    en_title='Surge in Wastewater Force Mains: Plastic Pipe, Low Heads, Sewage Air Valves and Thousands of Cycles',
    en_excerpt='On a 3 km DN400 PE force main the Joukowsky drop is only <strong>50.5 m</strong>, a quarter of ductile iron, yet the line goes to vapour at the pump: the pump holds only 39 m. Ten times the inertia still lets the high point separate; a vessel with <strong>4.3 m³</strong> of gas keeps it above atmospheric. Wave speed, protection for sewage, 105,000 cycles a year and fatigue, with three interactive charts.',
    en_search='wastewater force main surge sewage pumping station PE pipe PVC pipe wave speed Joukowsky submersible pump low inertia column separation high point sewage air valve hydrogen sulfide surge vessel bladder flywheel pump cycles starts per hour fatigue cyclic life Folkman PE recurring surge 1.5 PC Bentley HAMMER water hammer',
    ar_title='الطرق المائي في خطوط ضخ الصرف الصحي: أنابيب بلاستيكية وضغوط منخفضة وصمامات هواء للصرف وآلاف الدورات',
    ar_excerpt='في خط ضخ صرف صحي من البولي إيثيلين بطول ٣ كم وقطر ٤٠٠ مم لا يتجاوز هبوط جوكوفسكي <strong>٥٠٫٥ م</strong>، ومع ذلك يصل الخط إلى ضغط التبخر عند المضخة لأن ضغط التشغيل لا يتجاوز ٣٩ م. وخزان حماية بحجم غاز <strong>٤٫٣ م³</strong> يبقي الخط فوق الضغط الجوي. مع ثلاثة رسوم تفاعلية.',
    ar_search='الطرق المائي خطوط ضخ الصرف الصحي محطة ضخ الصرف أنابيب البولي إيثيلين أنابيب PVC سرعة الموجة المضخات الغاطسة انفصال عمود الماء صمامات هواء الصرف الصحي خزان الحماية عدد دورات التشغيل الكلال بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
