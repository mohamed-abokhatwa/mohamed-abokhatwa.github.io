# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Every megatall tower sits on a deep basement, and every deep basement sits below the water table. That creates two problems that behave nothing like each other. One is <strong>flow</strong>: how much water arrives, which depends almost entirely on the ground and barely at all on the building — the same 20&nbsp;m excavation takes <strong>3&nbsp;L/s</strong> in silt and <strong>326&nbsp;L/s</strong> in sand and gravel, a factor of a hundred set by a soil parameter the MEP engineer does not control. The other is <strong>pressure</strong>: a water table 30&nbsp;m above the slab pushes up at <strong>294&nbsp;kPa</strong> — thirty tonnes on every square metre — and that is a structural decision the drainage design must be coordinated with, not a pumping problem at all.</p>

<h2 id="two">1 · Two strategies, decided by somebody else</h2>
<p>Before any pump is sized, the project has chosen one of two fundamentally different approaches, usually on structural and geotechnical advice:</p>
<ul class="clean">
  <li><strong>Tanked (fully waterproofed).</strong> The basement is a sealed box designed to resist the full hydrostatic uplift and lateral pressure. No permanent dewatering. The structure carries everything, the waterproofing must be perfect for the life of the building, and the MEP scope reduces to handling leakage, groundwater ingress at joints and the internal drainage.</li>
  <li><strong>Drained (under-slab drainage with permanent pumping).</strong> A drainage layer beneath the slab relieves the pressure, and pumps run forever to keep the water down. Structural cost falls sharply; in exchange the building acquires a <strong>permanent, safety-critical pumping system</strong> that must never fail, with all the redundancy, power and maintenance obligations that implies.</li>
</ul>
<p>The choice is a whole-life trade between concrete and pumps, and the MEP engineer's job is to make the second half of that trade honest — because the pumping obligation is routinely under-stated at the point the decision is made. A drained basement means N+1 pumps on essential power, alarmed, tested, and maintained for sixty years, plus the energy, plus the consequence of a failure that floods the plant rooms containing the building's entire mechanical and electrical infrastructure.</p>

<h2 id="int-inflow">2 · Interactive: how much water actually arrives</h2>
<p>Steady seepage into an excavation is governed by Darcy's law. Using the classical unconfined-flow approximation with Sichardt's radius of influence:</p>
<div class="eq">\[ Q \;\approx\; \frac{\pi k H^{2}}{\ln(R/r)}, \qquad R \approx 3000\,H\sqrt{k} \]</div>
<p>with \(k\) the permeability (m/s), \(H\) the drawdown, \(r\) the equivalent excavation radius and \(R\) the radius of influence. Note where the sensitivity lies: \(Q\) is <em>linear</em> in \(k\), and \(k\) ranges over six orders of magnitude between clay and gravel.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Steady groundwater inflow vs soil permeability</div>
    <div class="fsub">Q = πkH²/ln(R/r) with R = 3000·H·√k (Sichardt). An estimating tool for the order of magnitude — a real scheme needs a pumping test and a geotechnical model, not this curve.</div>
  </div>
  <div class="chart-box"><canvas id="flowChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Permeability k <span id="vK">1.0e-4 m/s</span></label>
      <input type="range" id="sK" min="-7" max="-2" value="-4" step="0.05">
      <div class="hint">Clay 1e-9, silt 1e-6, fine sand 1e-4, sand &amp; gravel 1e-3 to 1e-2 m/s.</div>
    </div>
    <div class="ctrl">
      <label>Drawdown <span id="vH">20 m</span></label>
      <input type="range" id="sH" min="3" max="45" value="20" step="1">
      <div class="hint">Water table down to the underside of the slab.</div>
    </div>
    <div class="ctrl">
      <label>Excavation radius <span id="vR">40 m</span></label>
      <input type="range" id="sR" min="10" max="120" value="40" step="5">
      <div class="hint">Equivalent radius of the basement footprint.</div>
    </div>
    <div class="ctrl">
      <label>Design factor <span id="vF">2.0×</span></label>
      <input type="range" id="sF" min="1" max="4" value="2" step="0.1">
      <div class="hint">Allowance for heterogeneity, fissures and the difference between theory and ground.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Theoretical inflow</div><div class="v" id="rQ">46 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Design inflow</div><div class="v" id="rQd">93 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Per day</div><div class="v" id="rDay">8,020 <small>m³</small></div></div>
    <div class="cell"><div class="k">Radius of influence</div><div class="v" id="rRi">600 <small>m</small></div></div>
    <div class="cell"><div class="k">Regime</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">The chart is a warning as much as a calculator. A 20&nbsp;m drawdown over a 40&nbsp;m radius takes about <strong>3&nbsp;L/s in silt and 326&nbsp;L/s in sand and gravel</strong> — the same building, the same excavation, a hundredfold difference driven by a parameter that is measured, not designed. Two consequences: never size a permanent dewatering system from a soil description, only from a <strong>pumping test</strong>; and note the radius of influence, which at high permeability reaches kilometres — permanent dewatering in a permeable aquifer draws down neighbouring ground, and settlement of adjacent structures is a real and litigated risk that belongs in the design discussion.</p>

<h2 id="int-uplift">3 · Interactive: uplift, and why the drainage layer exists</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Hydrostatic uplift on the basement slab</div>
    <div class="fsub">u = ρgh. Net uplift is the water pressure less the weight of the slab and the permanent load above it; the balance is what a drainage layer removes, or what the structure and anchors must resist.</div>
  </div>
  <div class="chart-box"><canvas id="upChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Water above slab <span id="vHu">20 m</span></label>
      <input type="range" id="sHu" min="2" max="45" value="20" step="1">
      <div class="hint">Design water table above the underside of the base slab.</div>
    </div>
    <div class="ctrl">
      <label>Slab thickness <span id="vT">2.0 m</span></label>
      <input type="range" id="sT" min="0.5" max="5" value="2" step="0.1">
      <div class="hint">Base slab / raft thickness.</div>
    </div>
    <div class="ctrl">
      <label>Permanent load above <span id="vG">60 kPa</span></label>
      <input type="range" id="sG" min="0" max="400" value="60" step="10">
      <div class="hint">Dead load of basement structure and any tower load reaching this point.</div>
    </div>
    <div class="ctrl">
      <label>Drainage relief <span id="vD">0 %</span></label>
      <input type="range" id="sD" min="0" max="100" value="0" step="1">
      <div class="hint">Pressure relieved by an under-slab drainage layer with permanent pumping.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Uplift pressure</div><div class="v" id="rU">196 <small>kPa</small></div></div>
    <div class="cell"><div class="k">Resisting load</div><div class="v" id="rRe">108 <small>kPa</small></div></div>
    <div class="cell"><div class="k">Net uplift</div><div class="v" id="rN">88 <small>kPa</small></div></div>
    <div class="cell"><div class="k">Per 1000 m²</div><div class="v" id="rTn">9,000 <small>t</small></div></div>
    <div class="cell"><div class="k">Status</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rSt"></span></div></div>
  </div>
</div>
<p class="fig-note">Twenty metres of water above the slab is <strong>196&nbsp;kPa</strong>. Against a 2&nbsp;m raft and 60&nbsp;kPa of load above, the net uplift is <strong>88&nbsp;kPa</strong> — which over a 1,000&nbsp;m² footprint is <strong>9,000 tonnes</strong> trying to lift the building. That is resisted by thickening the raft, by tension piles or anchors, or by <em>removing the pressure altogether</em> with an under-slab drainage layer. Drag the relief slider and watch the net uplift fall to nothing: that is exactly what a drained basement buys, and exactly why its pumps are structural elements in everything but name. A drained basement whose pumps fail does not merely flood — it can float.</p>

<div class="callout warn">
  <span class="lbl">The consequence that is never in the pump schedule</span>
  In a drained basement the dewatering pumps are not a plumbing utility; they are <strong>part of the structural load path</strong>. Their failure mode is not "wet floor" but progressive re-pressurisation of the under-slab drainage layer, and the building's entire electrical intake, chiller plant, fire pumps and transformers are usually in the lowest basement, directly in the path. Design them accordingly: duty/standby/standby on separate boards, at least one pump on essential power with the changeover tested, high-level alarms to a permanently manned point, and — because a pump that has never run will not run — automatic duty rotation. Then write the failure consequence into the O&amp;M so nobody quietly economises on the maintenance contract in year twelve.
</div>

<h2 id="int-sump">4 · Interactive: sump sizing and the energy of depth</h2>
<p>Sump design is the same cycle-time problem as any wet well: too small and the pumps short-cycle and burn out, too large and the water stagnates. The classic result is that the active volume needed is greatest when the inflow is <em>half</em> the pump capacity.</p>
<div class="eq">\[ V_{active} \;=\; \frac{Q_{pump}\,T_{min}}{4} \]</div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Sump active volume and pumping energy</div>
    <div class="fsub">V = Q·T/4 for the worst-case inflow of half the pump rate. Energy from E = H/(367·η) with H the lift from sump to discharge plus friction.</div>
  </div>
  <div class="chart-box"><canvas id="sumpChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Pump capacity <span id="vQp">40 L/s</span></label>
      <input type="range" id="sQp" min="5" max="200" value="40" step="5">
      <div class="hint">One duty pump. Size for the design inflow with standby equal.</div>
    </div>
    <div class="ctrl">
      <label>Maximum starts <span id="vS">10 /h</span></label>
      <input type="range" id="sS" min="4" max="30" value="10" step="1">
      <div class="hint">From the motor manufacturer. Larger motors permit fewer starts.</div>
    </div>
    <div class="ctrl">
      <label>Basement depth <span id="vDp">25 m</span></label>
      <input type="range" id="sDp" min="5" max="50" value="25" step="1">
      <div class="hint">Sump invert to discharge level.</div>
    </div>
    <div class="ctrl">
      <label>Pump efficiency <span id="vE">65 %</span></label>
      <input type="range" id="sE" min="40" max="80" value="65" step="1">
      <div class="hint">Wire-to-water for a submersible drainage pump.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Active volume</div><div class="v" id="rV">3.6 <small>m³</small></div></div>
    <div class="cell"><div class="k">Total head</div><div class="v" id="rH">40 <small>m</small></div></div>
    <div class="cell"><div class="k">Shaft power</div><div class="v" id="rP">24 <small>kW</small></div></div>
    <div class="cell"><div class="k">Specific energy</div><div class="v" id="rSe">0.168 <small>kWh/m³</small></div></div>
    <div class="cell"><div class="k">Annual at 50 % duty</div><div class="v" id="rAn">106 <small>MWh</small></div></div>
  </div>
</div>
<p class="fig-note">A 40&nbsp;L/s duty pump at ten starts an hour needs <strong>3.6&nbsp;m³ of active volume</strong> — and lifting from 25&nbsp;m costs <strong>0.168&nbsp;kWh/m³</strong>, which running at half duty all year is about <strong>106&nbsp;MWh</strong>. Two design points follow. Raise the permitted starts and the sump shrinks, but check it against the motor rather than assuming; and note that the specific energy is modest per cubic metre but the volumes in a permeable site are enormous — at 326&nbsp;L/s the same 25&nbsp;m lift is a continuous 130&nbsp;kW load, which belongs in the building's energy model and its essential-power sizing, not in a footnote.</p>

<h2 id="drainage">5 · The rest of the basement drainage</h2>
<p>Groundwater is only one of the inflows a deep basement has to handle, and the others arrive suddenly:</p>
<ul class="clean">
  <li><strong>Ramp and vehicle entrance water.</strong> The single largest transient inflow. Size the ramp channel and its sump for the design storm falling on the whole ramp catchment plus the wash-off from vehicles, and provide a physical high point at the top of the ramp so a surcharged street cannot run in.</li>
  <li><strong>Sprinkler and firefighting water.</strong> A design discharge in a basement produces a very large flow with nowhere to go. Codes and insurers increasingly require the drainage to handle a defined firefighting flow for a defined duration — check the number and design for it, because it usually exceeds every other case.</li>
  <li><strong>Plant room leakage and washdown.</strong> Bunded, drained plant rooms with alarmed gullies, discharging to a sump that is not the groundwater sump.</li>
  <li><strong>Separate the streams.</strong> Groundwater is clean and can often be discharged directly or reused; car park and ramp water carries oil and silt and needs interception; foul drainage must be separately pumped and must never be able to back up into either. Three systems, three sumps, no cross-connections.</li>
  <li><strong>Oil interception and silt traps</strong> on the car park system, sized and — critically — accessible for the regular emptying they need.</li>
  <li><strong>Backflow protection on every discharge.</strong> A public sewer that surcharges in a storm will drive water down into the lowest point of the building, which is where all the plant is. Non-return devices, anti-flood valves and a discharge point above the surcharge level where possible.</li>
</ul>

<h2 id="reuse">6 · Groundwater as a resource</h2>
<p>In a water-scarce region, pumping thousands of cubic metres a day of clean groundwater to waste is difficult to defend. Depending on quality and local regulation it can serve cooling tower makeup — where <a href="cooling-towers-heat-rejection-tall-buildings.html">a 50&nbsp;MW plant drinks 2,400&nbsp;m³ a day</a> — or irrigation, water features or toilet flushing through a treatment train. Three cautions: test the quality properly (deep groundwater is often saline or high in sulphates and can be aggressive to both plant and concrete); confirm abstraction and discharge consents, which in many jurisdictions are the binding constraint rather than the engineering; and design the reuse so the dewatering function is never compromised by a fault in the reuse system — the pumps must always be able to discharge to waste.</p>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Insist on a pumping test, not a borehole description.</strong> Permeability inferred from soil classification can be an order of magnitude out, and the system is linear in it.</li>
  <li><strong>Design the transition from temporary to permanent dewatering</strong> as a deliberate operation. Construction dewatering runs for years; the permanent system takes over at a moment when the basement is full of finished plant, and that handover is a high-risk event that needs a method statement.</li>
  <li><strong>Make the sumps maintainable.</strong> Guide rails and lifting chains on submersible pumps so a pump can be withdrawn without entry, a permanent lifting point above each, and access covers sized for the pump — not for the man.</li>
  <li><strong>Treat sumps as confined spaces</strong> in the design: ventilation, gas monitoring where foul is involved, and a maintenance procedure that does not require entry for routine work.</li>
  <li><strong>Alarm at three levels</strong> — high, high-high and pump-fail — to a permanently manned location, and prove the alarm path at commissioning rather than the alarm contact.</li>
  <li><strong>Rotate duty automatically</strong> and log run hours per pump; a standby that has sat idle for two years is not a standby.</li>
  <li><strong>Protect the plant rooms.</strong> Raise plinths for electrical and control equipment in the lowest basement, provide a bunded threshold at plant room doors, and locate transformers and switchgear above the credible flood level where the layout allows it.</li>
  <li><strong>Record the as-built drainage layer.</strong> Under-slab drainage cannot be inspected; its layout, outlets and rodding points must be documented at construction or they are lost forever.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Establish tanked or drained early</strong>, and make the whole-life pumping obligation explicit in that decision.</li>
  <li><strong>Size from a pumping test</strong>, with a design factor for heterogeneity.</li>
  <li><strong>Check the radius of influence</strong> and the settlement risk to neighbours.</li>
  <li><strong>Coordinate uplift with the structural engineer</strong> and confirm what the drainage layer is assumed to relieve.</li>
  <li><strong>Design the pumps as safety-critical</strong> — duty/standby/standby, essential power, tested changeover, automatic rotation, three-level alarms.</li>
  <li><strong>Separate groundwater, car park and foul</strong> into three systems with no cross-connection.</li>
  <li><strong>Design for the firefighting discharge case</strong>, which often governs.</li>
  <li><strong>Protect against sewer surcharge</strong> on every discharge.</li>
  <li><strong>Evaluate groundwater reuse</strong>, subject to quality and consents, without compromising the dewatering duty.</li>
  <li><strong>Plan the temporary-to-permanent handover</strong> and protect the plant rooms with plinths and thresholds.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A deep basement has a <strong>flow problem and a pressure problem</strong>, and they are answered differently. The flow is set almost entirely by the ground — a hundredfold range between silt and gravel — so it is measured with a pumping test, never estimated from a soil description. The pressure is set by the water table, and at 20&nbsp;m it is <strong>9,000 tonnes of uplift on a 1,000&nbsp;m² raft</strong>, which the project either resists structurally or relieves with an under-slab drainage layer. Choose the second and the dewatering pumps become <strong>structural elements</strong>: duty/standby/standby, essential power, alarmed to a manned point, rotated automatically and maintained for sixty years — because they are protecting the room that contains the entire building's plant, and a drained basement whose pumps stop does not just flood.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>CIRIA C750 <em>Groundwater control: design and practice</em> — dewatering design, permeability, radius of influence and settlement effects.</li>
  <li>CIRIA C515 / C760 and BS 8102 <em>Code of practice for protection of below ground structures against water from the ground</em> — tanked, drained and integral protection, and grades of waterproofing.</li>
  <li>Powers, J.P. et&nbsp;al. <em>Construction Dewatering and Groundwater Control</em> — theory and practice of seepage estimation and system design.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em> and CIBSE <em>Guide G</em> — basement drainage, sump design and pumped drainage systems.</li>
  <li>BS EN 12056-4 and BS EN 752 — wastewater lifting plants and drain and sewer systems outside buildings, including surcharge protection.</li>
  <li>NFPA 13 / NFPA 20 and insurer guidance (FM Global) — drainage provision for sprinkler and firefighting discharge in basements.</li>
  <li>Hydraulic Institute ANSI/HI 9.8 <em>Rotodynamic Pumps for Pump Intake Design</em> — sump geometry, submergence and approach conditions; see also <a href="wet-well-vortex-design.html">wet well vortex design</a>.</li>
  <li>Saudi Building Code <em>SBC 701</em> and local abstraction and discharge regulations governing groundwater reuse.</li>
</ol>

<div class="tags">#BasementDrainage #Dewatering #GroundwaterControl #DeepBasement #TallBuildings #MegatallBuildings #Permeability #Darcy #RadiusOfInfluence #Settlement #HydrostaticUplift #TankedBasement #DrainedBasement #UnderSlabDrainage #TensionPiles #SumpDesign #ActiveVolume #CycleTime #SubmersiblePumps #EssentialPower #DutyStandby #SewerSurcharge #BackflowProtection #OilInterceptor #GroundwaterReuse #CIRIA #BS8102 #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const G9=9.81;

/* ---------- CHART 1 : inflow ---------- */
const sK=document.getElementById('sK'),sH=document.getElementById('sH'),
      sR=document.getElementById('sR'),sF=document.getElementById('sF');
const sichardt=(H,k)=>3000*H*Math.sqrt(k);
function inflow(k,H,r){
  const R=Math.max(sichardt(H,k),r*1.5);
  return Math.PI*k*H*H/Math.log(R/r);   // m3/s
}
let flowChart=new Chart(document.getElementById('flowChart'),{
  data:{datasets:[
    {type:'line',label:'Design inflow (with factor)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Theoretical inflow',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your site',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'logarithmic',min:1e-7,max:1e-2,title:{display:true,text:'Permeability k (m/s, log scale)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'logarithmic',title:{display:true,text:'Inflow (L/s, log scale)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} L/s at k = ${c.parsed.x.toExponential(1)}`}}}}
});
function updFlow(){
  const k=Math.pow(10,+sK.value),H=+sH.value,r=+sR.value,f=+sF.value;
  document.getElementById('vK').textContent=k.toExponential(1)+' m/s';
  document.getElementById('vH').textContent=H+' m';
  document.getElementById('vR').textContent=r+' m';
  document.getElementById('vF').textContent=fmt1(f)+'×';
  const xs=[];for(let e=-7;e<=-2;e+=0.1)xs.push(Math.pow(10,+e.toFixed(2)));
  flowChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(inflow(x,H,r)*1000*f).toFixed(3)}));
  flowChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(inflow(x,H,r)*1000).toFixed(3)}));
  const q=inflow(k,H,r)*1000;
  flowChart.data.datasets[2].data=[{x:k,y:+(q*f).toFixed(3)}];
  flowChart.update('none');
  document.getElementById('rQ').innerHTML=fmt0(q)+' <small>L/s</small>';
  document.getElementById('rQd').innerHTML=fmt0(q*f)+' <small>L/s</small>';
  document.getElementById('rDay').innerHTML=fmt0(q*f*86.4)+' <small>m³</small>';
  document.getElementById('rRi').innerHTML=fmt0(sichardt(H,k))+' <small>m</small>';
  const v=document.getElementById('rVd');
  if(q*f<10)       v.innerHTML='<span class="badge good">modest — routine sump</span>';
  else if(q*f<100) v.innerHTML='<span class="badge warn">significant permanent duty</span>';
  else             v.innerHTML='<span class="badge bad">major — reconsider tanking</span>';
}
[sK,sH,sR,sF].forEach(s=>s.addEventListener('input',updFlow));updFlow();

/* ---------- CHART 2 : uplift ---------- */
const sHu=document.getElementById('sHu'),sT=document.getElementById('sT'),
      sG=document.getElementById('sG'),sD=document.getElementById('sD');
const CONC=24;   // kN/m3
let upChart=new Chart(document.getElementById('upChart'),{
  data:{datasets:[
    {type:'line',label:'Uplift pressure',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:4},
    {type:'line',label:'Resisting load',data:[],borderColor:'#1e8449',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:3},
    {type:'line',label:'Net uplift',data:[],borderColor:'#1b4f72',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'Your basement',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:2,max:45,title:{display:true,text:'Water table above the slab (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',title:{display:true,text:'Pressure (kPa)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} kPa at ${fmt0(c.parsed.x)} m`}}}}
});
function updUp(){
  const h=+sHu.value,t=+sT.value,g=+sG.value,d=+sD.value/100;
  document.getElementById('vHu').textContent=h+' m';
  document.getElementById('vT').textContent=fmt1(t)+' m';
  document.getElementById('vG').textContent=g+' kPa';
  document.getElementById('vD').textContent=fmt0(d*100)+' %';
  const resist=t*CONC+g;
  const xs=[];for(let x=2;x<=45;x+=1)xs.push(x);
  upChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(G9*x*(1-d)).toFixed(1)}));
  upChart.data.datasets[1].data=xs.map(x=>({x:x,y:+resist.toFixed(1)}));
  upChart.data.datasets[2].data=xs.map(x=>({x:x,y:+Math.max(0,G9*x*(1-d)-resist).toFixed(1)}));
  const up=G9*h*(1-d), net=Math.max(0,up-resist);
  upChart.data.datasets[3].data=[{x:h,y:+up.toFixed(1)}];
  upChart.update('none');
  document.getElementById('rU').innerHTML=fmt0(up)+' <small>kPa</small>';
  document.getElementById('rRe').innerHTML=fmt0(resist)+' <small>kPa</small>';
  document.getElementById('rN').innerHTML=fmt0(net)+' <small>kPa</small>';
  document.getElementById('rTn').innerHTML=fmt0(net*1000/9.81)+' <small>t</small>';
  const v=document.getElementById('rSt');
  if(net<=0)      v.innerHTML='<span class="badge good">self-weight sufficient</span>';
  else if(net<50) v.innerHTML='<span class="badge warn">thicken raft or anchor</span>';
  else            v.innerHTML='<span class="badge bad">major uplift — drain or anchor</span>';
}
[sHu,sT,sG,sD].forEach(s=>s.addEventListener('input',updUp));updUp();

/* ---------- CHART 3 : sump & energy ---------- */
const sQp=document.getElementById('sQp'),sS=document.getElementById('sS'),
      sDp=document.getElementById('sDp'),sE=document.getElementById('sE');
const FRIC=15;
let sumpChart=new Chart(document.getElementById('sumpChart'),{
  data:{datasets:[
    {type:'line',label:'Active volume (m³)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Shaft power (kW)',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your sump',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:200,title:{display:true,text:'Pump capacity (L/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Sump active volume (m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Shaft power (kW)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updSump(){
  const Q=+sQp.value,st=+sS.value,dp=+sDp.value,e=+sE.value/100;
  document.getElementById('vQp').textContent=Q+' L/s';
  document.getElementById('vS').textContent=st+' /h';
  document.getElementById('vDp').textContent=dp+' m';
  document.getElementById('vE').textContent=fmt0(e*100)+' %';
  const H=dp+FRIC;
  const vol=q=>q*3600/(4*st)/1000;
  const pw=q=>q*H/(102*e);
  const xs=[];for(let x=5;x<=200;x+=5)xs.push(x);
  sumpChart.data.datasets[0].data=xs.map(x=>({x:x,y:+vol(x).toFixed(2)}));
  sumpChart.data.datasets[1].data=xs.map(x=>({x:x,y:+pw(x).toFixed(1)}));
  sumpChart.data.datasets[2].data=[{x:Q,y:+vol(Q).toFixed(2)}];
  sumpChart.update('none');
  const se=H/(367*e);
  document.getElementById('rV').innerHTML=fmt1(vol(Q))+' <small>m³</small>';
  document.getElementById('rH').innerHTML=fmt0(H)+' <small>m</small>';
  document.getElementById('rP').innerHTML=fmt0(pw(Q))+' <small>kW</small>';
  document.getElementById('rSe').innerHTML=fmt3(se)+' <small>kWh/m³</small>';
  document.getElementById('rAn').innerHTML=fmt0(pw(Q)*0.5*8760/1000)+' <small>MWh</small>';
}
[sQp,sS,sDp,sE].forEach(s=>s.addEventListener('input',updSump));updSump();

window.addEventListener('load',function(){try{flowChart.resize();upChart.resize();sumpChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='basement-dewatering-drainage-tall-buildings', cat='plumbing', mins=15,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Deep Basement Dewatering &amp; Drainage for Megatall Buildings: Inflow, Uplift &amp; Safety-Critical Pumps',
    reg_title='Deep Basement Dewatering & Drainage for Megatall Buildings: Inflow, Uplift & Safety-Critical Pumps',
    reg_tag='Plumbing · Dewatering · Basement Drainage',
    breadcrumb='Plumbing &amp; Drainage',
    tag_line='Plumbing &middot; Dewatering &middot; Basement Drainage &middot; Megatall Buildings',
    desc='Deep basement dewatering and drainage for megatall buildings: the hundredfold range in groundwater inflow set by permeability rather than by the building, tanked versus drained basements, hydrostatic uplift and why a drained basement makes its pumps structural elements, sump sizing and cycle time, the firefighting discharge case, separation of groundwater car park and foul streams, and groundwater reuse — with three interactive charts and installation tricks.',
    og_desc='The same 20 m excavation takes 3 L/s in silt and 326 L/s in sand and gravel. And 20 m of water above the slab is 9,000 tonnes of uplift on a 1,000 m2 raft — which is why a drained basement makes its pumps structural elements.',
    ld_desc='A design-perspective guide to deep basement dewatering and drainage in megatall buildings: seepage estimation and permeability sensitivity, tanked versus drained strategies, hydrostatic uplift, safety-critical pump design, sump sizing, drainage stream separation and groundwater reuse.',
    img_alt='Technical cutaway of a deep basement beneath a megatall tower showing the water table above the base slab, an under-slab drainage layer, collector pipework running to a sump with submersible pumps, and the discharge rising to grade',
    en_tag='Plumbing &amp; Drainage &middot; Dewatering &middot; Basement &middot; Megatall',
    en_title='Deep Basement Dewatering &amp; Drainage for Megatall Buildings: Inflow, Uplift &amp; Safety-Critical Pumps',
    en_excerpt='Every megatall tower sits on a deep basement below the water table, and that creates two problems that behave nothing like each other. The <strong>flow</strong> is set almost entirely by the ground &mdash; the same 20&nbsp;m excavation takes 3&nbsp;L/s in silt and <strong>326&nbsp;L/s</strong> in sand and gravel. The <strong>pressure</strong> is set by the water table: 20&nbsp;m above the slab is <strong>9,000 tonnes</strong> of uplift on a 1,000&nbsp;m&sup2; raft. Choose a drained basement to relieve it and the dewatering pumps become structural elements protecting the room that holds all the building&rsquo;s plant &mdash; with three interactive charts.',
    en_search='basement dewatering groundwater control deep basement tall buildings megatall permeability Darcy seepage Sichardt radius of influence pumping test settlement neighbouring structures tanked basement drained basement BS 8102 waterproofing grades under slab drainage layer hydrostatic uplift buoyancy tension piles anchors raft thickness sump design active volume cycle time starts per hour submersible pump guide rail duty standby essential power alarm levels duty rotation confined space ramp water firefighting discharge sprinkler drainage oil interceptor silt trap foul separation sewer surcharge backflow anti-flood valve groundwater reuse cooling tower makeup abstraction consent CIRIA C750 commissioning MEP building services',
    ar_title='نزح المياه الجوفية وصرف الأقبية العميقة في المباني فائقة الارتفاع: التدفق والطفو والمضخات الحرجة',
    ar_excerpt='كل برج فائق الارتفاع يقوم على قبو عميق تحت منسوب المياه الجوفية، وهذا يخلق مشكلتين لا تتشابهان إطلاقًا. <strong>التدفق</strong> تحدده الأرض وحدها تقريبًا — الحفر نفسه بعمق ٢٠ مترًا يستقبل ٣ لتر/ث في الطمي و<strong>٣٢٦ لتر/ث</strong> في الرمل والحصى. و<strong>الضغط</strong> يحدده منسوب المياه: عشرون مترًا فوق البلاطة تعني <strong>٩٠٠٠ طن</strong> من قوة الطفو على لبشة مساحتها ١٠٠٠ م². واختيار القبو المصرَّف لتخفيفها يجعل مضخات النزح عناصر إنشائية تحمي الغرفة التي تضم كل معدات المبنى — مع ثلاثة رسوم تفاعلية.',
    ar_search='basement dewatering groundwater control deep basement permeability seepage uplift tanked drained BS 8102 sump submersible pump duty standby sewer surcharge groundwater reuse CIRIA نزح المياه الجوفية التحكم في المياه الجوفية القبو العميق المباني الشاهقة المباني فائقة الارتفاع النفاذية قانون دارسي الترشح نصف قطر التأثير اختبار الضخ هبوط المنشآت المجاورة القبو المحكم القبو المصرَّف العزل المائي طبقة الصرف تحت البلاطة الضغط الهيدروستاتيكي قوة الطفو خوازيق الشد المراسي سماكة اللبشة تصميم بئر التجميع الحجم الفعال زمن الدورة عدد مرات التشغيل المضخة الغاطسة قضبان التوجيه التشغيل والاحتياطي الطاقة الأساسية مستويات الإنذار تدوير التشغيل الحيز المحصور مياه المنحدر تصريف مياه الإطفاء الرشاشات فاصل الزيوت مصيدة الطمي فصل الصرف الصحي ارتداد المجاري صمام منع الفيضان إعادة استخدام المياه الجوفية تعويض أبراج التبريد تصاريح السحب MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
