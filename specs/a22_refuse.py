# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A refuse chute is the only system in a tall building deliberately designed to drop objects hundreds of metres in free fall. A five-kilogram bag reaches terminal velocity of about <strong>28.6&nbsp;m/s — 103&nbsp;km/h</strong> — and it gets to 87&nbsp;% of that within the first sixty metres, so a 600&nbsp;m chute and a 60&nbsp;m chute deliver almost identical impact: roughly <strong>2,000 joules</strong>, arriving repeatedly, at the bottom of a shaft that runs the full height of the building. That shaft is simultaneously a fire path, an odour path and — because it is warm, vertical and hundreds of metres tall — a chimney developing <strong>200&nbsp;Pa</strong> of its own stack pressure. It is also, invariably, the last riser to be coordinated.</p>

<h2 id="why">1 · Four problems in one shaft</h2>
<ul class="clean">
  <li><strong>Impact.</strong> The energy arriving at the base is set by terminal velocity, not by building height, and it must be absorbed by something designed for it rather than by the floor slab.</li>
  <li><strong>Fire.</strong> A vertical shaft full of combustible material connecting every floor is exactly the vertical fire spread compartmentation exists to prevent, and every hopper door is a penetration of a fire-rated enclosure.</li>
  <li><strong>Odour and hygiene.</strong> The chute's own stack effect drives air — and everything in it — upward, out through hopper doors on the upper floors. This is the same physics as <a href="stack-effect-tall-buildings.html">stack effect</a> and it is solved the same way: by controlling the pressure regime, not by sealing harder.</li>
  <li><strong>Noise.</strong> A bag at 100&nbsp;km/h in a steel tube adjacent to bedrooms is a serious acoustic problem, and it arrives at night.</li>
</ul>

<h2 id="int-impact">2 · Interactive: how fast, and how hard</h2>
<p>A falling bag accelerates until drag balances weight. Integrating the equation of motion gives the velocity after a drop \(h\):</p>
<div class="eq">\[ v_t = \sqrt{\frac{2mg}{\rho\,C_d A}}, \qquad v(h) = v_t\sqrt{1-e^{-2gh/v_t^{2}}} \]</div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Bag velocity and impact energy against drop height</div>
    <div class="fsub">Free fall with quadratic drag, C&#100; ≈ 1.0 for a tumbling bag, air density 1.2 kg/m³. Impact energy = ½mv². The dashed line is terminal velocity.</div>
  </div>
  <div class="chart-box"><canvas id="impChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Bag mass <span id="vM">5.0 kg</span></label>
      <input type="range" id="sM" min="1" max="20" value="5" step="0.5">
      <div class="hint">Typical domestic bag; commercial and hotel waste is heavier.</div>
    </div>
    <div class="ctrl">
      <label>Frontal area <span id="vA">0.10 m²</span></label>
      <input type="range" id="sA" min="0.03" max="0.35" value="0.10" step="0.01">
      <div class="hint">A tumbling bag presents a varying area; heavier, denser bags present less per kilogram.</div>
    </div>
    <div class="ctrl">
      <label>Drop height <span id="vH">200 m</span></label>
      <input type="range" id="sH" min="5" max="600" value="200" step="5">
      <div class="hint">Highest hopper to the base of the chute.</div>
    </div>
    <div class="ctrl">
      <label>Drag coefficient <span id="vC">1.00</span></label>
      <input type="range" id="sC" min="0.6" max="1.6" value="1.0" step="0.05">
      <div class="hint">Higher for a loose, tumbling bag; lower for a dense compact one.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Terminal velocity</div><div class="v" id="rVt">28.6 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Velocity at impact</div><div class="v" id="rVi">28.5 <small>m/s</small></div></div>
    <div class="cell"><div class="k">In km/h</div><div class="v" id="rKh">103 <small>km/h</small></div></div>
    <div class="cell"><div class="k">Impact energy</div><div class="v" id="rEi">2,027 <small>J</small></div></div>
    <div class="cell"><div class="k">Reaches 90 % at</div><div class="v" id="rH9">69 <small>m</small></div></div>
  </div>
</div>
<p class="fig-note">The curve flattens fast: a bag reaches <strong>90&nbsp;% of terminal velocity within about 70&nbsp;metres</strong>, so everything above that height is hydraulically identical. A 600&nbsp;m chute is not six times worse than a 100&nbsp;m one — it is <em>the same</em>, which is genuinely good news and means the base detail is a standard problem rather than a megatall one. What it must handle is around <strong>2,000&nbsp;J per bag</strong>, repeatedly: that requires a designed <strong>speed-reduction or shock-absorbing base</strong> — a discharge chamber with a sacrificial impact plate, a compactor hopper designed for the energy, or an in-chute retarding device — not a bin sitting on a slab. Note the mass slider: hotel and commercial waste at 10&nbsp;kg per bag more than doubles the energy.</p>

<h2 id="int-storage">3 · Interactive: what arrives at the bottom, and where it goes</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Waste volume and storage room sizing</div>
    <div class="fsub">Mass from population and per-capita generation; volume from bulk density, which compaction changes by a factor of three or more. Store sized on collection interval plus a contingency.</div>
  </div>
  <div class="chart-box"><canvas id="volChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Population <span id="vP">2000</span></label>
      <input type="range" id="sP" min="200" max="10000" value="2000" step="100">
      <div class="hint">Residents plus staff plus an allowance for visitors.</div>
    </div>
    <div class="ctrl">
      <label>Generation rate <span id="vG">1.8 kg/p·d</span></label>
      <input type="range" id="sG" min="0.5" max="4" value="1.8" step="0.1">
      <div class="hint">Gulf residential runs high; hotels higher again.</div>
    </div>
    <div class="ctrl">
      <label>Bulk density <span id="vD">120 kg/m³</span></label>
      <input type="range" id="sD" min="60" max="600" value="120" step="10">
      <div class="hint">Loose bagged waste 100–150; compacted 350–500 kg/m³.</div>
    </div>
    <div class="ctrl">
      <label>Collection interval <span id="vI">2 days</span></label>
      <input type="range" id="sI" min="1" max="7" value="2" step="1">
      <div class="hint">Plus contingency for missed collections and public holidays.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Mass per day</div><div class="v" id="rKg">3,600 <small>kg/d</small></div></div>
    <div class="cell"><div class="k">Volume per day</div><div class="v" id="rVd">30.0 <small>m³/d</small></div></div>
    <div class="cell"><div class="k">Store volume</div><div class="v" id="rSv">60 <small>m³</small></div></div>
    <div class="cell"><div class="k">Room area</div><div class="v" id="rRa">20 <small>m²</small></div></div>
    <div class="cell"><div class="k">If compacted 4:1</div><div class="v" id="rCv">15 <small>m³</small></div></div>
  </div>
</div>
<p class="fig-note">Two thousand people generate <strong>3.6 tonnes and 30&nbsp;m³ a day</strong> loose — a 60&nbsp;m³ store for a two-day collection interval, which at 3&nbsp;m clear is 20&nbsp;m² <em>of bin space alone</em>, before circulation, before the compactor, before the recycling streams and before a vehicle can turn. <strong>Compaction is what makes this fit</strong>: at 4:1 the same store is 15&nbsp;m³. But a compactor is a powered machine in a wet, corrosive room with its own noise, power, drainage, maintenance access and a bin-change operation that must not block the chute — and it needs a control interlock so the chute cannot discharge onto a machine mid-cycle or into a missing bin.</p>

<h2 id="odour">4 · The chute as a chimney</h2>
<p>The chute is warm, vertical and connects every floor to a refuse room — the ideal conditions for the stack effect described elsewhere in this series. A 400&nbsp;m chute only 15&nbsp;K warmer than outside develops around <strong>208&nbsp;Pa</strong>, all of it pushing air, odour and airborne material <em>up</em> and out through the hopper doors of the upper floors. The controls are all pressure controls:</p>
<ul class="clean">
  <li><strong>Extract at the top, mechanically.</strong> A continuously running extract fan at the chute head holds the whole shaft at negative pressure relative to the lobbies, so air moves into the chute at every hopper rather than out of it. This is the primary control and everything else supports it.</li>
  <li><strong>Make-up at the bottom.</strong> The extract needs a designed air path in at the refuse room, or the fan simply pulls harder on the hopper doors and the negative pressure collapses.</li>
  <li><strong>Self-closing, gasketed hopper doors</strong> with an interlock so only one can be open at a time on a given riser — which also prevents a bag being dropped onto somebody loading below.</li>
  <li><strong>Wash-down and drainage.</strong> Chutes need periodic cleaning; provide a wash-down head at the top, a drained base and a gully in the refuse room connected to the foul system with a trap that will not dry out.</li>
  <li><strong>Do not rely on sealing alone.</strong> A 200&nbsp;Pa driving pressure will find every gasket; the answer is to reverse the pressure, not to fight it.</li>
</ul>

<h2 id="fire">5 · Fire strategy</h2>
<ul class="clean">
  <li><strong>The shaft is a fire-rated enclosure</strong> for its full height, with the rating maintained at every hopper door and every penetration.</li>
  <li><strong>Sprinkler protection inside the chute</strong> — typically at the top, at the discharge and at intervals — with the discharge draining safely rather than flooding the refuse room's electrical equipment.</li>
  <li><strong>Hopper doors are fire doors.</strong> Self-closing, rated, and with a fusible or automatic closing arrangement at the discharge so a fire in the refuse room cannot propagate up the shaft.</li>
  <li><strong>The refuse room is a high fire load</strong> in its own right: separately compartmented, sprinklered, with detection and with a ventilation strategy that does not feed a fire.</li>
  <li><strong>Interlock the chute on alarm.</strong> A fire condition should close the discharge and lock the hopper doors — a chute left open during a fire is an open vertical path.</li>
</ul>

<h2 id="int-noise">6 · Interactive: the noise problem</h2>
<p>A bag impacting at 100&nbsp;km/h in a steel tube radiates structure-borne noise into every wall the chute touches. Because the chute is usually in the core, those walls are usually apartment walls.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Impact noise and the benefit of isolating the chute</div>
    <div class="fsub">Radiated level scaled from impact energy on a logarithmic basis, then reduced by the enclosure and by resilient mounting. The dashed line is a typical night-time bedroom criterion.</div>
  </div>
  <div class="chart-box"><canvas id="noiChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Impact energy <span id="vE">2000 J</span></label>
      <input type="range" id="sE" min="200" max="6000" value="2000" step="50">
      <div class="hint">From the first chart.</div>
    </div>
    <div class="ctrl">
      <label>Enclosure reduction <span id="vR">30 dB</span></label>
      <input type="range" id="sR" min="10" max="60" value="30" step="1">
      <div class="hint">Blockwork or double-skin shaft construction around the chute.</div>
    </div>
    <div class="ctrl">
      <label>Resilient mounting <span id="vI2">8 dB</span></label>
      <input type="range" id="sI2" min="0" max="20" value="8" step="1">
      <div class="hint">Isolating the chute from the shaft wall breaks the structure-borne path.</div>
    </div>
    <div class="ctrl">
      <label>Night criterion <span id="vN">NR 25</span></label>
      <input type="range" id="sN" min="15" max="40" value="25" step="1">
      <div class="hint">Bedroom target at night. Impact noise is judged far more harshly than steady noise.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Source level</div><div class="v" id="rLs">93 <small>dB</small></div></div>
    <div class="cell"><div class="k">After enclosure</div><div class="v" id="rLe">63 <small>dB</small></div></div>
    <div class="cell"><div class="k">After isolation</div><div class="v" id="rLi">55 <small>dB</small></div></div>
    <div class="cell"><div class="k">Above criterion</div><div class="v" id="rLo">30 <small>dB</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rNv"></span></div></div>
  </div>
</div>
<p class="fig-note">The model here is indicative rather than predictive — real impact noise needs measurement or a manufacturer's data — but the <em>ranking</em> is not in doubt, and it makes the design point: enclosure alone does not get there, and <strong>the structure-borne path through the chute's fixings is what actually reaches the bedroom</strong>. Resiliently mount the chute within its shaft, do not let it touch a party wall, and — most effectively of all — <strong>locate it away from bedrooms in the first place</strong>, which is a core-planning decision made long before anyone calculates a decibel. The same principle as in <a href="vibration-noise-control-tall-buildings.html">vibration and noise control</a>: the flanking path beats the barrier.</p>

<h2 id="streams">7 · Recycling, and the multi-stream problem</h2>
<p>A single chute delivers a single mixed stream, which is increasingly unacceptable and in many jurisdictions non-compliant. The options each carry a design consequence:</p>
<ul class="clean">
  <li><strong>Multiple chutes.</strong> Simplest and most reliable, and the most expensive in core area — two or three full-height rated shafts instead of one.</li>
  <li><strong>A single chute with a diverter</strong> at the base, selected by the user at the hopper. Saves shaft space but introduces a mechanism at the bottom of a 300&nbsp;m drop, and depends entirely on users selecting correctly.</li>
  <li><strong>Chute for general waste plus room-level collection</strong> for recyclables. Pragmatic and common, but it moves the problem into the operations budget and requires storage on every floor or a portering regime.</li>
  <li><strong>Vacuum waste collection.</strong> Pneumatic transport from chute bases to a central terminal, avoiding vehicle movements through the podium entirely. Genuinely elegant on a large mixed-use development, high capital cost, high energy, and it needs a level of maintenance capability that must be verified before it is specified.</li>
</ul>
<p>Whichever is chosen, decide it at concept stage. Adding a second full-height rated shaft to a tower after the core is set is not a variation; it is a redesign.</p>

<h2 id="install">8 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Reserve the shaft and the refuse room at concept</strong>, including the vehicle access, turning and bin-presentation route, which is a traffic-engineering constraint as much as an MEP one.</li>
  <li><strong>Specify a designed discharge arrangement</strong> — impact absorption, a bin that cannot be missing, and an interlock that stops discharge during a bin change.</li>
  <li><strong>Run the extract fan continuously</strong> and prove the negative pressure at the top and bottom hopper at commissioning, not just the fan's flow rate.</li>
  <li><strong>Detail the acoustic isolation of the chute from the shaft</strong> explicitly, and check on site that no fixing bridges it — this is the same grout-bridge failure as under an inertia base.</li>
  <li><strong>Provide wash-down and drainage</strong> at the top and the base, with a trapped, primed gully.</li>
  <li><strong>Commission the fire interlocks</strong> — hopper locking, discharge closure and sprinkler operation — as part of the integrated systems test, not as a separate contractor's demonstration.</li>
  <li><strong>Write the cleaning and maintenance regime into the O&amp;M</strong> with intervals, and design the access it needs — a chute that cannot be cleaned becomes the source of the odour complaint the extract system is blamed for.</li>
</ul>

<h2 id="checklist">9 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Decide the waste strategy at concept</strong> — number of streams, chute count, vacuum or conventional.</li>
  <li><strong>Design the discharge for the impact energy</strong>, which is set by terminal velocity, not by height.</li>
  <li><strong>Size the store on real generation rates</strong> and a realistic collection interval, with compaction if the room will not otherwise fit.</li>
  <li><strong>Hold the chute at negative pressure</strong> with continuous top extract and a designed make-up path.</li>
  <li><strong>Rate the shaft for its full height</strong>, with rated self-closing hopper doors and in-chute sprinklers.</li>
  <li><strong>Interlock on fire alarm</strong> and prove it in the integrated test.</li>
  <li><strong>Isolate the chute acoustically</strong> and keep it away from bedrooms.</li>
  <li><strong>Provide wash-down, drainage and cleaning access.</strong></li>
  <li><strong>Coordinate the vehicle route and bin presentation</strong> with the traffic strategy.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A refuse chute reaches <strong>90&nbsp;% of terminal velocity in the first 70 metres</strong>, so a megatall chute is no worse than a mid-rise one — but it delivers about <strong>2,000&nbsp;J per bag</strong> into a base detail that must be designed for it rather than left as a bin on a slab. The two problems that are genuinely worse with height are the chute's own <strong>stack effect</strong> — 200&nbsp;Pa pushing odour out of the upper hoppers, beaten by continuous top extract holding the shaft negative, never by better gaskets — and the <strong>structure-borne noise</strong> of a bag at 100&nbsp;km/h in a steel tube in the core, beaten by resilient mounting and, far better, by not putting the chute next to bedrooms. Decide the number of streams at concept, because a second full-height rated shaft is a redesign, not a variation.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>BS 5906 — <em>Waste management in buildings: Code of practice</em>: chute design, storage sizing, generation rates and collection.</li>
  <li>NFPA 82 — <em>Standard on Incinerators and Waste and Linen Handling Systems and Equipment</em>: chute construction, fire rating, sprinkler protection and discharge arrangements.</li>
  <li>International Building Code and Saudi Building Code <em>SBC 801</em> — rubbish and linen chute provisions, shaft enclosure and access room requirements.</li>
  <li>CIBSE <em>Guide G — Public Health and Plumbing Engineering</em> — refuse systems, chute ventilation and refuse room services.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em> and CIBSE <em>Guide B2</em> — extract ventilation and odour control for waste handling areas.</li>
  <li>BS 8233 and CIBSE <em>Guide B4</em> — noise criteria and structure-borne transmission relevant to chute location and isolation.</li>
  <li>Manufacturer design guidance for refuse chutes, retarding devices, diverters and compactors, and for pneumatic (vacuum) waste collection systems.</li>
  <li>Local municipality waste regulations governing stream separation, storage and collection access.</li>
</ol>

<div class="tags">#RefuseChute #WasteManagement #TallBuildings #MegatallBuildings #TerminalVelocity #ImpactEnergy #DischargeDesign #Compactor #WasteStorage #BulkDensity #StackEffect #OdourControl #NegativePressure #TopExtract #HopperDoor #FireRatedShaft #NFPA82 #BS5906 #InChuteSprinkler #FireInterlock #StructureBorneNoise #ResilientMounting #RecyclingStreams #VacuumWasteCollection #CorePlanning #Commissioning #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const RHO=1.2, G9=9.81;

/* ---------- CHART 1 : impact ---------- */
const sM=document.getElementById('sM'),sA=document.getElementById('sA'),
      sH=document.getElementById('sH'),sC=document.getElementById('sC');
const vTerm=(m,A,Cd)=>Math.sqrt(2*m*G9/(RHO*Cd*A));
const vAt=(h,m,A,Cd)=>{const vt=vTerm(m,A,Cd);return vt*Math.sqrt(1-Math.exp(-2*G9*h/(vt*vt)));};
let impChart=new Chart(document.getElementById('impChart'),{
  data:{datasets:[
    {type:'line',label:'Velocity (m/s)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Impact energy (J)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your chute',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:600,title:{display:true,text:'Drop height (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Velocity (m/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Impact energy (J)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      annotation:{annotations:{
        vt:{type:'line',scaleID:'y',yScaleID:'y',value:28.6,borderColor:'#1e8449',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'terminal velocity',position:'end',font:{size:10,family:'DM Sans'},color:'#1e8449',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updImp(){
  const m=+sM.value,A=+sA.value,H=+sH.value,Cd=+sC.value;
  document.getElementById('vM').textContent=fmt1(m)+' kg';
  document.getElementById('vA').textContent=fmt2(A)+' m²';
  document.getElementById('vH').textContent=H+' m';
  document.getElementById('vC').textContent=fmt2(Cd);
  const vt=vTerm(m,A,Cd);
  const xs=[];for(let x=5;x<=600;x+=5)xs.push(x);
  impChart.data.datasets[0].data=xs.map(x=>({x:x,y:+vAt(x,m,A,Cd).toFixed(2)}));
  impChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(0.5*m*Math.pow(vAt(x,m,A,Cd),2)).toFixed(0)}));
  const v=vAt(H,m,A,Cd);
  impChart.data.datasets[2].data=[{x:H,y:+v.toFixed(2)}];
  impChart.options.plugins.annotation.annotations.vt.value=vt;
  impChart.options.scales.y.max=vt*1.15;
  impChart.update('none');
  // height at which 90% of terminal is reached
  const h90=-vt*vt/(2*G9)*Math.log(1-0.81);
  document.getElementById('rVt').innerHTML=fmt1(vt)+' <small>m/s</small>';
  document.getElementById('rVi').innerHTML=fmt1(v)+' <small>m/s</small>';
  document.getElementById('rKh').innerHTML=fmt0(v*3.6)+' <small>km/h</small>';
  document.getElementById('rEi').innerHTML=fmt0(0.5*m*v*v)+' <small>J</small>';
  document.getElementById('rH9').innerHTML=fmt0(h90)+' <small>m</small>';
}
[sM,sA,sH,sC].forEach(s=>s.addEventListener('input',updImp));updImp();

/* ---------- CHART 2 : waste volume ---------- */
const sP=document.getElementById('sP'),sG=document.getElementById('sG'),
      sD=document.getElementById('sD'),sI=document.getElementById('sI');
let volChart=new Chart(document.getElementById('volChart'),{
  data:{datasets:[
    {type:'line',label:'Store volume (m³)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'If compacted 4:1',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your building',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:200,max:10000,title:{display:true,text:'Population served',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Refuse store volume (m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} m³ for ${fmt0(c.parsed.x)} people`}}}}
});
function updVol(){
  const P=+sP.value,G=+sG.value,D=+sD.value,I=+sI.value;
  document.getElementById('vP').textContent=P;
  document.getElementById('vG').textContent=fmt1(G)+' kg/p·d';
  document.getElementById('vD').textContent=D+' kg/m³';
  document.getElementById('vI').textContent=I+' days';
  const store=p=>p*G/D*I;
  const xs=[];for(let x=200;x<=10000;x+=100)xs.push(x);
  volChart.data.datasets[0].data=xs.map(x=>({x:x,y:+store(x).toFixed(1)}));
  volChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(store(x)/4).toFixed(1)}));
  volChart.data.datasets[2].data=[{x:P,y:+store(P).toFixed(1)}];
  volChart.update('none');
  const kg=P*G, V=store(P);
  document.getElementById('rKg').innerHTML=fmt0(kg)+' <small>kg/d</small>';
  document.getElementById('rVd').innerHTML=fmt1(kg/D)+' <small>m³/d</small>';
  document.getElementById('rSv').innerHTML=fmt0(V)+' <small>m³</small>';
  document.getElementById('rRa').innerHTML=fmt0(V/3)+' <small>m²</small>';
  document.getElementById('rCv').innerHTML=fmt0(V/4)+' <small>m³</small>';
}
[sP,sG,sD,sI].forEach(s=>s.addEventListener('input',updVol));updVol();

/* ---------- CHART 3 : noise ---------- */
const sE=document.getElementById('sE'),sR=document.getElementById('sR'),
      sI2=document.getElementById('sI2'),sN=document.getElementById('sN');
const srcLevel=E=>60+10*Math.log10(Math.max(E,1));   // indicative scaling from impact energy
let noiChart=new Chart(document.getElementById('noiChart'),{
  data:{datasets:[
    {type:'line',label:'Level at the bedroom (dB)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Enclosure only, no isolation',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your design',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:200,max:6000,title:{display:true,text:'Impact energy (J)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',title:{display:true,text:'Level at the receiver (dB)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      annotation:{annotations:{
        cr:{type:'line',scaleID:'y',yScaleID:'y',value:25,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'night criterion',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updNoi(){
  const E=+sE.value,R=+sR.value,I=+sI2.value,N=+sN.value;
  document.getElementById('vE').textContent=E+' J';
  document.getElementById('vR').textContent=R+' dB';
  document.getElementById('vI2').textContent=I+' dB';
  document.getElementById('vN').textContent='NR '+N;
  const xs=[];for(let x=200;x<=6000;x+=50)xs.push(x);
  noiChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(srcLevel(x)-R-I).toFixed(1)}));
  noiChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(srcLevel(x)-R).toFixed(1)}));
  noiChart.data.datasets[2].data=[{x:E,y:+(srcLevel(E)-R-I).toFixed(1)}];
  noiChart.options.plugins.annotation.annotations.cr.value=N;
  noiChart.update('none');
  const Ls=srcLevel(E), Le=Ls-R, Li=Le-I;
  document.getElementById('rLs').innerHTML=fmt0(Ls)+' <small>dB</small>';
  document.getElementById('rLe').innerHTML=fmt0(Le)+' <small>dB</small>';
  document.getElementById('rLi').innerHTML=fmt0(Li)+' <small>dB</small>';
  document.getElementById('rLo').innerHTML=fmt0(Math.max(0,Li-N))+' <small>dB</small>';
  const v=document.getElementById('rNv');
  if(Li<=N)        v.innerHTML='<span class="badge good">meets the criterion</span>';
  else if(Li<=N+10)v.innerHTML='<span class="badge warn">close — isolate further</span>';
  else             v.innerHTML='<span class="badge bad">relocate away from bedrooms</span>';
}
[sE,sR,sI2,sN].forEach(s=>s.addEventListener('input',updNoi));updNoi();

window.addEventListener('load',function(){try{impChart.resize();volChart.resize();noiChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='refuse-chutes-waste-tall-buildings', cat='plumbing', mins=14,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Refuse Chutes &amp; Waste Handling in Megatall Buildings: Impact Energy, Odour Control &amp; Noise',
    reg_title='Refuse Chutes & Waste Handling in Megatall Buildings: Impact Energy, Odour Control & Noise',
    reg_tag='Plumbing · Refuse Chutes · Waste',
    breadcrumb='Plumbing &amp; Drainage',
    tag_line='Plumbing &middot; Refuse Chutes &middot; Waste Handling &middot; Megatall Buildings',
    desc='Refuse chute and waste handling design in megatall buildings: terminal velocity and the impact energy the discharge must absorb, why a 600 m chute is no worse than a 70 m one, waste generation and store sizing with compaction, the chute as a chimney driving odour out of upper hoppers and the continuous top extract that beats it, fire rating and interlocks, structure-borne noise, and multi-stream recycling options — with three interactive charts.',
    og_desc='A five-kilogram bag hits terminal velocity of 103 km/h and reaches 90 percent of it in the first 70 metres — so a 600 m chute is no worse than a mid-rise one, but it delivers 2,000 J per bag into a base detail that must be designed for it.',
    ld_desc='A design-perspective guide to refuse chutes and waste handling in megatall buildings: falling-bag terminal velocity and impact energy, discharge design, waste store sizing and compaction, chute stack effect and odour control, fire rating and interlocks, acoustic isolation and recycling stream strategy.',
    img_alt='Technical cutaway of a megatall tower refuse chute showing hopper doors on successive floors, a bag falling inside the shaft, an extract fan at the chute head drawing air upward, and a discharge chamber with compactor and bins in the basement refuse room',
    en_tag='Plumbing &amp; Drainage &middot; Refuse Chutes &middot; Waste &middot; Megatall',
    en_title='Refuse Chutes &amp; Waste Handling in Megatall Buildings: Impact Energy, Odour Control &amp; Noise',
    en_excerpt='A refuse chute is the only system in a tall building deliberately designed to drop objects hundreds of metres in free fall. A five-kilogram bag reaches <strong>103&nbsp;km/h</strong> and gets to 90&nbsp;% of terminal velocity in the first 70&nbsp;metres &mdash; so a 600&nbsp;m chute is no worse than a mid-rise one, but it delivers <strong>2,000&nbsp;J per bag</strong> into a base detail that must be designed for it. Plus the chute as a 200&nbsp;Pa chimney pushing odour out of the upper hoppers, fire interlocks, and the structure-borne noise of a bag at 100&nbsp;km/h beside a bedroom &mdash; with three interactive charts.',
    en_search='refuse chute waste handling tall buildings megatall terminal velocity drag impact energy discharge chamber shock absorber retarding device compactor waste generation rate bulk density loose compacted store sizing collection interval refuse room vehicle access chute stack effect odour control negative pressure continuous top extract make-up air hopper door self closing gasketed interlock fire rated shaft NFPA 82 BS 5906 in-chute sprinkler fusible link fire alarm interlock structure borne noise resilient mounting acoustic isolation bedroom criterion recycling streams multiple chutes diverter vacuum waste collection pneumatic core planning wash down drainage commissioning MEP building services',
    ar_title='مزالق النفايات وإدارة المخلفات في المباني فائقة الارتفاع: طاقة الارتطام والتحكم في الروائح والضوضاء',
    ar_excerpt='مزلق النفايات هو النظام الوحيد في المبنى الشاهق المصمَّم عمدًا لإسقاط أجسام مئات الأمتار في سقوط حر. كيس بوزن خمسة كيلوغرامات يبلغ <strong>١٠٣ كم/س</strong> ويصل إلى ٩٠٪ من السرعة النهائية خلال أول سبعين مترًا — فمزلق بطول ٦٠٠ متر ليس أسوأ من مزلق في مبنى متوسط، لكنه يوصل <strong>٢٠٠٠ جول لكل كيس</strong> إلى تفصيلة قاعدة يجب تصميمها لذلك. مع المزلق كمدخنة بضغط ٢٠٠ باسكال تدفع الروائح خارج الفتحات العلوية، وتعشيق الحريق، وضوضاء كيس بسرعة ١٠٠ كم/س بجوار غرفة نوم — مع ثلاثة رسوم تفاعلية.',
    ar_search='refuse chute waste handling terminal velocity impact energy compactor store sizing stack effect odour control negative pressure hopper door fire rated NFPA 82 BS 5906 sprinkler structure borne noise vacuum waste collection مزلق النفايات إدارة المخلفات المباني الشاهقة المباني فائقة الارتفاع السرعة النهائية مقاومة الهواء طاقة الارتطام غرفة التفريغ ممتص الصدمات جهاز التبطيء الكابسة معدل توليد النفايات الكثافة الظاهرية السائبة المضغوطة تحجيم غرفة التخزين فترة الجمع غرفة النفايات وصول المركبات تأثير المدخنة في المزلق التحكم في الروائح الضغط السالب الشفط العلوي المستمر هواء التعويض باب الإلقاء ذاتي الإغلاق محكم الإغلاق التعشيق المنور المقاوم للحريق الرشاش داخل المزلق الوصلة المنصهرة تعشيق إنذار الحريق الضوضاء المنتقلة عبر الهيكل التركيب المرن العزل الصوتي معيار غرف النوم مسارات إعادة التدوير المزالق المتعددة المحوّل الجمع بالتفريغ الهوائي تخطيط النواة الغسيل والصرف التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
