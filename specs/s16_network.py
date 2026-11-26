# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A transient model is a simplification of the network, and the simplifications are not neutral. On the 12&nbsp;km reference main with its vessel, an offtake of 0.15&nbsp;m&sup3;/s at 6&nbsp;km changes the answer depending only on how it is drawn. As a <strong>fixed demand</strong> the line falls to <strong>+2.11&nbsp;m</strong> and fails the +3.0&nbsp;m criterion; as a <strong>pressure-dependent demand</strong> it holds +3.82&nbsp;m; as a branch pipe to a tank, +5.57&nbsp;m; left out altogether, +4.33&nbsp;m. Add a closed 1.5&nbsp;km branch to the main and the line minimum drops to <strong>+1.26&nbsp;m</strong> while the dead end goes to vapour. This article shows which network details a surge model must keep, how to model demands, and what can safely be removed.</p>

<h2 id="why">1 &middot; Why network detail matters in a transient</h2>
<p>A steady-state model only needs the network to carry the right flows at the right heads, so it tolerates heavy simplification. A transient model also needs the network to reflect, absorb and store pressure waves correctly [1][2]:</p>
<ul class="clean">
  <li><strong>Every junction reflects part of a wave</strong>, and every branch sends part of it away and back later.</li>
  <li><strong>A dead end doubles the wave</strong> that reaches it and returns it to the main, delayed by twice its travel time.</li>
  <li><strong>Demands respond to pressure.</strong> A real offtake, tap or leak draws less when the pressure falls, which damps a downsurge; a fixed-flow demand keeps drawing, which deepens it.</li>
  <li><strong>Tanks and reservoirs on branches feed water back</strong> during a downsurge and absorb it during an upsurge.</li>
</ul>
<p>The examples use the series' reference main: 12&nbsp;km of DN800 ductile iron at a wave speed of 1,050&nbsp;m/s, 0.70&nbsp;m&sup3;/s entering at the pump, a delivery reservoir at 44.8&nbsp;m, and the series vessel (3.5&nbsp;m&sup3; of gas, DN400 differential connection) protecting an instant pump stop [3]. The network solver is the same method-of-characteristics code with a vapour cavity model, verified against the series solver to 0.01&nbsp;m.</p>

<h2 id="demand">2 &middot; Fixed or pressure-dependent demand</h2>
<p>The offtake at 6&nbsp;km takes 0.15&nbsp;m&sup3;/s, leaving 0.55&nbsp;m&sup3;/s for the second half of the main. Three ways to model it are common [2][4]:</p>
<div class="eq">\[ \text{fixed: } q = q_0, \qquad \text{orifice: } q = q_0\sqrt{\frac{p}{p_0}}, \qquad \text{branch: a pipe to a tank, with its own wave speed and friction} \]</div>
<p>A fixed demand is the default in many models, because steady-state demands are usually entered that way. During a downsurge it keeps drawing 0.15&nbsp;m&sup3;/s however low the pressure falls, so the main loses water it would in reality keep. The orifice form, sized to pass \(q_0\) at the steady pressure \(p_0\), draws less as the pressure falls and more when it rises. A real offtake to a tank is a pipe, and the tank supplies water back into the main when the main falls below it.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">One network, five ways to draw it</div>
    <div class="fsub">Reference main with its vessel, instant pump stop, 150&nbsp;s. Minimum and maximum pressure head along the main. The grey lines are the envelope of the case chosen for comparison. Network MOC model, vapour cavity model, 100&nbsp;m reaches.</div>
  </div>
  <div class="chart-box"><canvas id="envChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Model</label>
      <select id="sCase">
        <option value="none">Offtake left out</option>
        <option value="fixed" selected>Offtake as a fixed demand</option>
        <option value="orifice">Offtake as a pressure-dependent demand</option>
        <option value="branch">Offtake as a 2 km DN400 branch to a tank</option>
        <option value="deadend">No offtake; closed 1.5 km DN300 branch at 3 km</option>
      </select>
      <div class="hint">Same pipes, same pump, same vessel.</div>
    </div>
    <div class="ctrl">
      <label>Compare with</label>
      <select id="sCmp">
        <option value="none">Offtake left out</option>
        <option value="fixed">Offtake as a fixed demand</option>
        <option value="orifice" selected>Offtake as a pressure-dependent demand</option>
        <option value="branch">Offtake as a branch to a tank</option>
        <option value="deadend">Closed branch at 3 km</option>
      </select>
      <div class="hint">Drawn in grey.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Lowest head on the main</div><div class="v" id="rMin">&ndash;</div></div>
    <div class="cell"><div class="k">Where</div><div class="v" id="rX" style="font-size:15px;margin-top:6px;">&ndash;</div></div>
    <div class="cell"><div class="k">Highest head</div><div class="v" id="rMax">&ndash;</div></div>
    <div class="cell"><div class="k">Vessel gas, largest</div><div class="v" id="rGas">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict at +3.0 m</div><div class="v" style="font-size:14px;margin-top:6px;" id="rVer">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The three ways of modelling the same offtake give +2.11, +3.82 and +5.57&nbsp;m: a fail, a narrow pass and a comfortable pass. The fixed demand is the most pessimistic, the branch to a tank the most favourable, because the tank feeds water back into the main at 6&nbsp;km. The orifice demand also moves the lowest point: from 4.7&nbsp;km to the pump. Leaving the offtake out (+4.33&nbsp;m) is not conservative here: it overstates the margin of the fixed-demand case by 2.2&nbsp;m.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">At the offtake</div>
    <div class="fsub">Pressure head at the offtake junction (6&nbsp;km), or at the closed branch's junction and its dead end (3&nbsp;km and 1.5&nbsp;km along the branch), with the demand drawn by the offtake where it is a demand.</div>
  </div>
  <div class="chart-box"><canvas id="jChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Model</label>
      <select id="sCase2">
        <option value="fixed" selected>Fixed demand</option>
        <option value="orifice">Pressure-dependent demand</option>
        <option value="branch">Branch to a tank</option>
        <option value="deadend">Closed branch</option>
      </select>
      <div class="hint">Right axis: demand in m³/s.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Junction: lowest</div><div class="v" id="rJm">&ndash;</div></div>
    <div class="cell"><div class="k">Demand: range</div><div class="v" id="rQr" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Dead end: highest / lowest</div><div class="v" id="rDe" style="font-size:17px;">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The pressure-dependent demand falls from 0.15 to 0.069&nbsp;m&sup3;/s as the downsurge arrives and rises to 0.18 on the return: it behaves as a small relief at the junction. The closed branch fills and empties with every reflection, and its far end goes to vapour 18&nbsp;s after the trip, while the main loses 3&nbsp;m of minimum.</p>

<h2 id="deadend">3 &middot; Dead ends and closed valves</h2>
<p>A closed branch is the clearest example of a detail that skeletonisation must keep. A wave entering it reflects from the closed end with doubled amplitude and comes back to the main after \(2L_b/a\): 2.9&nbsp;s for the 1.5&nbsp;km branch here [1][5]. The returning wave adds to the main's own transient. In our case the closed branch, carrying no flow at all, takes the main from +4.33 to +1.26&nbsp;m and its own far end to vapour. Fire mains, washout and future-connection stubs, and valves normally closed between zones are all closed branches during a transient.</p>

<h2 id="skeleton">4 &middot; What can be removed, and what cannot</h2>
<div class="tbl-wrap"><table>
  <caption>Skeletonising a network for a transient model: our rules</caption>
  <thead><tr><th>Detail</th><th>Keep or remove</th><th>Why</th></tr></thead>
  <tbody>
    <tr><td>Large offtakes and branches to tanks</td><td>Keep as pipes</td><td>They reflect, feed back and change the result (section 2)</td></tr>
    <tr><td>Closed branches, dead ends, normally closed valves</td><td>Keep</td><td>They double and return the wave (section 3)</td></tr>
    <tr><td>Small distributed demands</td><td>Lump into pressure-dependent demands at nearby nodes</td><td>Fixed demands overstate the downsurge</td></tr>
    <tr><td>Short pipes and fittings in series</td><td>Merge, keeping travel time</td><td>They force a small time step (see <a href="surge-model-time-step-convergence.html">time step</a>)</td></tr>
    <tr><td>Loops in a distribution network</td><td>Keep the main loops</td><td>A loop splits and recombines waves; a tree model can miss or exaggerate peaks</td></tr>
    <tr><td>Devices, high points and changes of section</td><td>Always keep</td><td>They are where the answer is read</td></tr>
  </tbody>
</table></div>
<p>The test of any simplification is to run the governing scenario on the detailed and the skeletonised model and compare the envelopes at the critical points [2][6]. A skeleton that changes the minimum by more than the margin describes a different system.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">The five models against the criterion</div>
    <div class="fsub">Lowest pressure head on the main, and at the dead end where there is one, for each way of modelling the network.</div>
  </div>
  <div class="chart-box" style="height:300px;"><canvas id="barChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Design minimum <span id="vCr">+3.0 m</span></label>
      <input type="range" id="sCr" min="-5" max="8" value="3" step="0.5">
      <div class="hint">Check it against the project's allowable values.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Models that pass on the main</div><div class="v" id="rN">&ndash;</div></div>
    <div class="cell"><div class="k">Spread between models</div><div class="v" id="rSp">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The spread between the five models (4.3&nbsp;m on the main) is larger than the margin of the base design (1.3&nbsp;m). The modelling choice decides the verdict.</p>

<h2 id="hammer">5 &middot; Setting it up in Bentley HAMMER</h2>
<p>Field names differ slightly between versions [7].</p>
<ol>
  <li><strong>Start from the steady-state model</strong> and decide, branch by branch, what the transient model must keep, using the table in section 4.</li>
  <li><strong>Use Skelebrator</strong> for series pipes and small branches, but lock the elements that must stay: offtakes to tanks, closed branches, devices, high points.</li>
  <li><strong>Choose the demand representation</strong> for the transient: check how your version treats junction demands during a transient run, and use a pressure-dependent form (an emitter or orifice) for offtakes that really respond to pressure. Model large offtakes as pipes to their tanks.</li>
  <li><strong>Keep normally closed valves</strong> as closed valves, so the branches behind them are dead ends in the transient.</li>
  <li><strong>Run the governing scenario on both models</strong>, the detailed and the skeleton, and compare the envelopes at the critical points before using the skeleton for the protection design.</li>
  <li><strong>Bracket the demand model</strong>: run fixed and pressure-dependent demands and report both if the verdict depends on it.</li>
</ol>

<h2 id="checklist">6 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Every large offtake</strong> modelled as a pipe to its tank, or as a pressure-dependent demand.</li>
  <li><strong>Dead ends and closed valves</strong> kept, with their branches.</li>
  <li><strong>Small demands lumped</strong> into pressure-dependent demands, not fixed flows.</li>
  <li><strong>Skeleton checked against the detailed model</strong> on the governing scenario.</li>
  <li><strong>Demand model bracketed</strong> where the verdict depends on it.</li>
  <li><strong>Loops kept</strong> in distribution networks.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><a href="surge-model-field-validation.html">Validating a surge model with a field pump-trip test</a></li>
    <li><a href="surge-sensitivity-uncertainty.html">Sensitivity and uncertainty: bounding the result</a></li>
    <li><a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip: inertia, specific speed and four-quadrant curves</a></li>
    <li><strong>Demands, branches and dead ends in a transient model</strong></li>
    <li><a href="surge-envelope-pipe-pressure-limits.html">Reading the surge envelope against the pipe's real limits</a></li>
    <li><a href="transient-forces-pipe-supports.html">Transient forces on pipe supports and bends</a></li>
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
const fmt1=v=>v.toFixed(1), fmt2=v=>v.toFixed(2), fmt3=v=>v.toFixed(3);
const sgn=(v,d)=>(v<-0.0049?'−':(v>0.0049?'+':''))+Math.abs(v).toFixed(d);
const PMIN=3.0, VAP=-9.8;
const good=t=>'<span class="badge good">'+t+'</span>', bad=t=>'<span class="badge bad">'+t+'</span>';
const hl=(v,txt,col,pos)=>({type:'line',yMin:v,yMax:v,borderColor:col,borderWidth:1.3,borderDash:[6,4],label:{display:true,content:txt,position:pos||'end',font:LBL,color:'#fff',backgroundColor:col}});
const NAMES={none:'Offtake left out',fixed:'Fixed demand',orifice:'Pressure-dependent demand',branch:'Branch to a tank',deadend:'Closed branch'};
/* ---------- CHART 1 : envelopes ---------- */
const sCase=document.getElementById('sCase'), sCmp=document.getElementById('sCmp');
const envChart=new Chart(document.getElementById('envChart'),{
  data:{datasets:[
    {type:'line',label:'Maximum (m)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.2,pointRadius:0,order:1},
    {type:'line',label:'Minimum (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:0,order:2},
    {type:'line',label:'Comparison',data:[],borderColor:'#9aa5ab',backgroundColor:'#9aa5ab',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:3},
    {type:'line',label:'Comparison min',data:[],borderColor:'#9aa5ab',backgroundColor:'#9aa5ab',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:4}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:12,title:{display:true,text:'Chainage along the main (km)',font:TTL},...AX},y:{type:'linear',min:-5,max:130,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8,filter:it=>it.datasetIndex<3}},tooltip:{filter:it=>it.datasetIndex<2,callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} km`}},
      annotation:{annotations:{p:hl(PMIN,'+3.0 m','rgba(30,132,73,0.85)','start')}}}}
});
const xy=(r,k)=>r.x.map((x,i)=>({x:x/1000,y:r[k][i]}));
function upd1(){
  const r=D[sCase.value], c=D[sCmp.value];
  envChart.data.datasets[0].data=xy(r,'emax'); envChart.data.datasets[1].data=xy(r,'emin');
  envChart.data.datasets[2].data=xy(c,'emax'); envChart.data.datasets[3].data=xy(c,'emin');
  envChart.data.datasets[2].label='Comparison: '+NAMES[sCmp.value];
  envChart.update('none');
  document.getElementById('rMin').innerHTML=sgn(r.line_min,2)+' <small>m</small>';
  document.getElementById('rX').innerHTML=r.x_min===0?'at the pump':'at '+fmt1(r.x_min/1000)+' km';
  document.getElementById('rMax').innerHTML=fmt1(r.line_max)+' <small>m</small>';
  document.getElementById('rGas').innerHTML=fmt2(r.gas)+' <small>m³</small>';
  document.getElementById('rVer').innerHTML=r.line_min>=PMIN?good('passes'):bad('fails');
}
[sCase,sCmp].forEach(s=>s.addEventListener('input',upd1));upd1();
/* ---------- CHART 2 : at the offtake ---------- */
const sCase2=document.getElementById('sCase2');
const jChart=new Chart(document.getElementById('jChart'),{
  data:{datasets:[
    {type:'line',label:'Junction (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0,yAxisID:'y'},
    {type:'line',label:'Dead end (m)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.6,pointRadius:0,yAxisID:'y'},
    {type:'line',label:'Demand (m³/s, right)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],pointRadius:0,yAxisID:'y1'}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:150,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:-15,max:130,title:{display:true,text:'Pressure head (m)',font:TTL},...AX},
            y1:{type:'linear',min:0,max:0.3,position:'right',title:{display:true,text:'Demand (m³/s)',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}},tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`demand ${fmt3(c.parsed.y)} m³/s`:`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m`}},
      annotation:{annotations:{v:hl(VAP,'vapour','rgba(192,57,43,0.85)')}}}}
});
function upd2(){
  const r=D[sCase2.value];
  jChart.data.datasets[0].data=r.t.map((t,k)=>({x:t,y:r.J[k]}));
  jChart.data.datasets[1].data=r.dead?r.t.map((t,k)=>({x:t,y:r.dead[k]})):[];
  jChart.data.datasets[2].data=r.qd?r.t.map((t,k)=>({x:t,y:r.qd[k]})):[];
  jChart.update('none');
  document.getElementById('rJm').innerHTML=sgn(Math.min(...r.J),1)+' <small>m</small>';
  document.getElementById('rQr').innerHTML=r.qd?fmt3(Math.min(...r.qd))+'–'+fmt3(Math.max(...r.qd))+' <small>m³/s</small>':'<small>no demand</small>';
  document.getElementById('rDe').innerHTML=r.dead_max!==undefined?fmt1(r.dead_max)+' / '+sgn(r.dead_min,1)+' <small>m</small>':'<small>none</small>';
}
sCase2.addEventListener('input',upd2);upd2();
/* ---------- CHART 3 : summary ---------- */
const sCr=document.getElementById('sCr');
const KEYS=['none','fixed','orifice','branch','deadend'];
const barChart=new Chart(document.getElementById('barChart'),{
  data:{labels:KEYS.map(k=>NAMES[k]),datasets:[
    {type:'bar',label:'Main: lowest (m)',data:KEYS.map(k=>D[k].line_min),backgroundColor:'#1b4f72',borderWidth:0},
    {type:'bar',label:'Dead end: lowest (m)',data:KEYS.map(k=>D[k].dead_min!==undefined?D[k].dead_min:null),backgroundColor:'#c0392b',borderWidth:0}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,indexAxis:'y',
    scales:{x:{type:'linear',min:-12,max:8,title:{display:true,text:'Lowest pressure head (m)',font:TTL},...AX},y:{...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt2(c.parsed.x)} m`}},
      annotation:{annotations:{crit:{type:'line',xMin:3,xMax:3,borderColor:'#1e8449',borderWidth:1.6,borderDash:[6,4],label:{display:true,content:'+3.0 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}}}}}}
});
function upd3(){
  const cr=+sCr.value; document.getElementById('vCr').textContent=sgn(cr,1)+' m';
  const a=barChart.options.plugins.annotation.annotations.crit; a.xMin=cr; a.xMax=cr; a.label.content=sgn(cr,1)+' m'; barChart.update('none');
  const v=KEYS.map(k=>D[k].line_min);
  document.getElementById('rN').innerHTML=v.filter(x=>x>=cr).length+' <small>of 5</small>';
  document.getElementById('rSp').innerHTML=fmt2(Math.max(...v)-Math.min(...v))+' <small>m</small>';
}
sCr.addEventListener('input',upd3);upd3();
window.addEventListener('load',function(){try{[envChart,jChart,barChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: junctions, branches, dead ends and wave reflection in networks.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: transients in distribution networks, demands and skeletonisation.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, its vessel and the verified MOC solver.</li>
  <li>Karney, B.W. &amp; McInnis, D. &ldquo;Transient analysis of water distribution systems.&rdquo; <em>Journal AWWA</em>, 82(7), 1990: demand representation and the behaviour of networks under transients.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014: branching pipes and closed branches.</li>
  <li>Jung, B.S., Boulos, P.F. &amp; Wood, D.J. &ldquo;Effect of pipeline network skeletonization on hydraulic transient simulation.&rdquo; <em>Journal of Water Resources Planning and Management</em>, 135(4), 2009: when skeletonisation changes transient results.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: Skelebrator, junction demands, emitters, valves and transient calculation options.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #NetworkModelling #Skeletonization #DemandModelling #PressureDependentDemand #DeadEnd #ClosedBranch #DistributionNetwork #SurgeVessel #BentleyHAMMER #Skelebrator #TransientAnalysis #WaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'practice2.json')))['s16']
DATA = {k: {q: v[q] for q in ('line_min', 'x_min', 'line_max', 'gas', 'x', 'emax', 'emin', 't', 'J', 'dead', 'dead_max', 'dead_min', 'qd') if q in v} for k, v in _A.items()}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='transient-model-demands-network-detail', cat='surge', mins=13,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Demands, Branches and Dead Ends in a Transient Model: What Skeletonisation Must Keep',
    reg_title='Demands, Branches and Dead Ends in a Transient Model: What Skeletonisation Must Keep',
    reg_tag='Surge Analysis · Network Detail · Demands',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Network Detail &middot; Demands',
    desc='How network detail changes a surge result: fixed against pressure-dependent demands, offtakes as branches to tanks, closed branches and dead ends, and the rules for skeletonising a model for transients, with three interactive charts and the HAMMER steps.',
    og_desc='The same 0.15 m³/s offtake on the reference main gives +2.11 m as a fixed demand (a fail), +3.82 m as a pressure-dependent demand and +5.57 m as a branch to a tank. A closed 1.5 km branch drops the main to +1.26 m and its dead end to vapour.',
    ld_desc='Network detail in hydraulic transient models: demand representation, branches to tanks, dead ends and skeletonisation rules, with the Bentley HAMMER steps.',
    img_alt='A water network drawn as an engineering schematic: a transmission main with an offtake branch to a tank, a closed valve on a dead-end branch, and pressure waves reflecting at the junctions',
    en_tag='Surge &amp; Transient Analysis &middot; Network Detail',
    en_title='Demands, Branches and Dead Ends in a Transient Model: What Skeletonisation Must Keep',
    en_excerpt='The same 0.15 m³/s offtake on the reference main gives <strong>+2.11 m</strong> as a fixed demand (a fail), <strong>+3.82 m</strong> as a pressure-dependent demand and <strong>+5.57 m</strong> as a branch to a tank. A closed 1.5 km branch carrying no flow drops the main to +1.26 m and its dead end to vapour. Demand models, branches, dead ends and skeletonisation rules, with three interactive charts.',
    en_search='transient model demands fixed demand pressure dependent demand emitter orifice offtake branch tank dead end closed valve wave reflection skeletonization Skelebrator network detail distribution network loops surge vessel water hammer Bentley HAMMER',
    ar_title='الاستهلاكات والفروع والنهايات المغلقة في نموذج الطرق المائي: ما يجب أن يبقى عند تبسيط الشبكة',
    ar_excerpt='يعطي سحب قدره ٠٫١٥ م³/ث على الخط المرجعي ضغطاً أدنى <strong>+٢٫١١ م</strong> عند نمذجته استهلاكاً ثابتاً (فشل)، و<strong>+٣٫٨٢ م</strong> عند نمذجته استهلاكاً يعتمد على الضغط، و<strong>+٥٫٥٧ م</strong> عند نمذجته فرعاً إلى خزان. وفرع مغلق طوله ١٫٥ كم يخفض الخط إلى +١٫٢٦ م. مع ثلاثة رسوم تفاعلية.',
    ar_search='نموذج الطرق المائي الاستهلاك الثابت الاستهلاك المعتمد على الضغط الفروع النهايات المغلقة انعكاس الموجة تبسيط الشبكة شبكات التوزيع خزان الحماية المطرقة المائية بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
