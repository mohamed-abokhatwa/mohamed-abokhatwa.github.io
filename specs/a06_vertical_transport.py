# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">The lifts are somebody else's package. The vertical transportation consultant sizes them, a specialist contractor installs them, and the mechanical engineer's name appears nowhere on the drawings. Yet the lift installation is simultaneously the tower's <strong>largest concentrated heat source outside the plant rooms</strong>, its <strong>dominant chimney</strong>, a <strong>piston that generates hundreds of pascals</strong> every time a car moves at speed, and — in a fire — a protected escape route that only works if a pressurisation system nobody has coordinated is holding the right pressure across doors that are already fighting the stack effect. Almost every one of those is an MEP responsibility, and almost every one is discovered late.</p>

<h2 id="interfaces">1 · The four interfaces that matter</h2>
<ul class="clean">
  <li><strong>Heat.</strong> Machine rooms and machine-room-less (MRL) drive cabinets reject the losses of very large motors. A bank of eight high-rise lifts can dump <strong>over 100&nbsp;kW</strong> into a small room at the top of a zone — a room that is often unconditioned in the concept design because nobody asked.</li>
  <li><strong>Air.</strong> The hoistway is the tallest, smoothest, warmest shaft in the building and therefore the principal path for <a href="stack-effect-tall-buildings.html">stack effect</a>. Whether it is vented, sealed or pressurised is an MEP decision with consequences for the whole tower.</li>
  <li><strong>Pressure transients.</strong> A car moving at 10&nbsp;m/s in a close-fitting shaft is a piston. The pressure it generates ahead of and behind it can reach <strong>160&nbsp;Pa or more</strong>, and it lands on top of the stack pressure that is already there.</li>
  <li><strong>Fire.</strong> Fire-service and occupant-evacuation lifts require pressurised, protected shafts and lobbies with guaranteed power — the life-safety half of the problem covered in <a href="firefighting-tall-buildings.html">firefighting in megatall buildings</a>.</li>
</ul>

<h2 id="heat">2 · Machine room heat — the load nobody scheduled</h2>
<p>A lift motor does not consume its rated power continuously; it draws heavily on acceleration and up-travel, regenerates on down-travel with a full car, and idles between trips. The heat rejected into the machine space is the system loss multiplied by the duty:</p>
<div class="eq">\[ \dot{Q}_{room} \;=\; n\,P_{motor}\,(1-\eta_{sys})\,f_{duty} \]</div>
<p>with \(\eta_{sys}\) the combined motor, drive and gear efficiency and \(f_{duty}\) the fraction of time under load through the design hour. For eight lifts of 150&nbsp;kW at 80&nbsp;% system efficiency and a 45&nbsp;% duty that is <strong>108&nbsp;kW</strong> into one room. Three consequences follow immediately:</p>
<ul class="clean">
  <li><strong>It needs mechanical cooling, not ventilation.</strong> Lift equipment is typically limited to about 35–40&nbsp;°C ambient, and drives derate or trip above it. Outside-air ventilation cannot hold that in a Gulf summer, so the machine room needs a dedicated cooling system on essential power.</li>
  <li><strong>It must not fail.</strong> If the machine-room cooling trips, the lifts trip — which in a megatall building is an evacuation problem, not a comfort complaint. N+1 cooling and essential-power supply are proportionate.</li>
  <li><strong>Regenerative drives change the number.</strong> Drives that return energy to the building rather than burning it in a resistor bank cut both the room's heat load and the tower's energy bill; the trade is harmonic distortion and a grid connection that will accept export.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Lift machine-room heat gain and cooling duty</div>
    <div class="fsub">Q = n·P·(1−η)·f. Regenerative drives are credited with returning a share of the loss to the building rather than to the room. The dashed line is the cooling you have installed.</div>
  </div>
  <div class="chart-box"><canvas id="heatChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Lifts in the group <span id="vN">8</span></label>
      <input type="range" id="sN" min="1" max="16" value="8" step="1">
      <div class="hint">Cars sharing one machine room or drive space.</div>
    </div>
    <div class="ctrl">
      <label>Motor rating each <span id="vP">150 kW</span></label>
      <input type="range" id="sP" min="15" max="400" value="150" step="5">
      <div class="hint">High-rise gearless machines are large — 100–250 kW is common.</div>
    </div>
    <div class="ctrl">
      <label>System efficiency <span id="vEf">80 %</span></label>
      <input type="range" id="sEf" min="60" max="95" value="80" step="1">
      <div class="hint">Motor, drive and rope losses combined.</div>
    </div>
    <div class="ctrl">
      <label>Peak duty fraction <span id="vDu">45 %</span></label>
      <input type="range" id="sDu" min="10" max="80" value="45" step="1">
      <div class="hint">Share of the design hour under load. Morning up-peak is the case.</div>
    </div>
    <div class="ctrl">
      <label>Regenerative recovery <span id="vRg">0 %</span></label>
      <input type="range" id="sRg" min="0" max="45" value="0" step="1">
      <div class="hint">Share of the loss returned to the building instead of the room.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Heat to room</div><div class="v" id="rQ">108 <small>kW</small></div></div>
    <div class="cell"><div class="k">Cooling duty</div><div class="v" id="rTr">31 <small>TR</small></div></div>
    <div class="cell"><div class="k">Per lift</div><div class="v" id="rPl">13.5 <small>kW</small></div></div>
    <div class="cell"><div class="k">Air at 8 K rise</div><div class="v" id="rAf">11.2 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">Eight 150&nbsp;kW machines produce <strong>108&nbsp;kW</strong> — about 31 tons of cooling in a room the size of a large apartment, on the highest occupied level of a zone where getting chilled water to it is least convenient. Trying to remove it with outside air needs <strong>11&nbsp;m³/s at an 8&nbsp;K rise</strong>, which in a 45&nbsp;°C ambient does not produce a 35&nbsp;°C room at all. Add regenerative drives at 30&nbsp;% recovery and the room load drops to about 76&nbsp;kW while the recovered energy goes back into the building. The number to take away is that this room is a <em>plant room</em> with a chilled-water requirement, not a cupboard with a wall fan.</p>

<h2 id="piston">3 · Piston effect — the transient nobody models</h2>
<p>A lift car nearly fills its shaft. When it moves, the air ahead must escape through the annular gap around the car and through door leakage, and the resulting pressure is roughly<sup class="cite">[3]</sup>:</p>
<div class="eq">\[ \Delta p \;\approx\; \tfrac{1}{2}\rho\,K\left(v\,\frac{A_{car}}{A_{shaft}-A_{car}}\right)^{2} \]</div>
<p>The blockage ratio is what makes this severe. At 60&nbsp;% blockage a car at 10&nbsp;m/s drives air through the annulus at 15&nbsp;m/s and generates around <strong>160&nbsp;Pa</strong>; tighten the shaft to 75&nbsp;% blockage and the same car produces over 600&nbsp;Pa. This pressure is <em>transient</em> and <em>additive</em> — it arrives on top of the stack pressure already across the landing doors, and it is the reason lift doors on the low floors of a tall zone in winter misbehave intermittently rather than consistently.</p>
<ul class="clean">
  <li><strong>Give the shaft free area.</strong> Blockage ratio is the dominant variable, and it is fixed by the architect and the lift consultant when the shaft is dimensioned. A slightly larger shaft is enormously cheaper than the noise and door problems it prevents.</li>
  <li><strong>Vent between shafts, not to the building.</strong> Inter-shaft openings within a lift bank let the air displaced by a rising car be taken by the shaft of a descending one, cancelling much of the pressure. This is very effective and it is a coordination item, not a product.</li>
  <li><strong>Aerodynamic car shrouds</strong> on the fastest lifts reduce both the pressure and the noise; above about 7&nbsp;m/s they are standard on serious installations.</li>
  <li><strong>Do not solve it with a permanent shaft vent.</strong> That fixes the piston effect and dramatically worsens the stack effect, as set out in <a href="stack-effect-tall-buildings.html">stack effect</a> — it drags the neutral plane to the roof and lands the whole stack pressure on the entrance lobby.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Piston-effect pressure vs car speed and shaft blockage</div>
    <div class="fsub">Δp = ½ρK(v·B/(1−B))², B = car area / shaft area, K ≈ 1.2 for the annulus and door leakage path. The dashed line is the pressure at which lift landing doors typically start to misbehave.</div>
  </div>
  <div class="chart-box"><canvas id="pistonChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Car speed <span id="vV">10.0 m/s</span></label>
      <input type="range" id="sV" min="1" max="18" value="10" step="0.5">
      <div class="hint">Megatall shuttle lifts reach 10–20 m/s.</div>
    </div>
    <div class="ctrl">
      <label>Blockage ratio <span id="vB">0.60</span></label>
      <input type="range" id="sB" min="0.25" max="0.85" value="0.6" step="0.01">
      <div class="hint">Car cross-section ÷ shaft cross-section. The single most powerful variable.</div>
    </div>
    <div class="ctrl">
      <label>Loss coefficient K <span id="vK">1.20</span></label>
      <input type="range" id="sK" min="0.6" max="2.5" value="1.2" step="0.05">
      <div class="hint">Depends on the annulus, door gaps and any inter-shaft venting.</div>
    </div>
    <div class="ctrl">
      <label>Door tolerance <span id="vDt">60 Pa</span></label>
      <input type="range" id="sDt" min="25" max="150" value="60" step="5">
      <div class="hint">Differential at which landing doors start to bind or reopen.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Annulus velocity</div><div class="v" id="rVa">15.0 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Piston pressure</div><div class="v" id="rDp">162 <small>Pa</small></div></div>
    <div class="cell"><div class="k">Max speed OK</div><div class="v" id="rVm">6.1 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Blockage for OK</div><div class="v" id="rBm">0.48</div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rPv"></span></div></div>
  </div>
</div>
<p class="fig-note">A 10&nbsp;m/s car at 60&nbsp;% blockage produces <strong>162&nbsp;Pa</strong>, comfortably past the point where landing doors bind — and that is before any stack pressure is added. Hold the same speed and open the shaft out to 48&nbsp;% blockage and the pressure falls inside tolerance. The chart's real message is the exponent: pressure goes as the <em>square</em> of both speed and the blockage function, so the shaft dimension chosen in the concept design is worth far more than anything the MEP engineer can add later.</p>

<h2 id="pressurisation">4 · Hoistway and lobby pressurisation</h2>
<p>Fire-service lifts, occupant-evacuation lifts and, increasingly, all lifts in a tall building require the shaft or its lobby to be held at positive pressure so smoke cannot enter. The airflow follows from the leakage area and the pressure to be held:</p>
<div class="eq">\[ Q \;=\; C_d\,A_{leak}\sqrt{\frac{2\,\Delta p}{\rho}} \]</div>
<p>A hoistway is leaky: every landing door is a large gap, and there are as many of them as there are floors. One square metre of effective leakage area at 50&nbsp;Pa needs about <strong>9&nbsp;m³/s</strong> — a substantial fan and a substantial shaft to feed it. The design difficulties are the same ones the stack-effect article sets out, sharpened:</p>
<ul class="clean">
  <li><strong>The pressure budget is tiny.</strong> The system must hold enough pressure to exclude smoke, but landing doors and adjacent stair doors must still work; the stack effect has usually spent most of the allowance before the fan starts.</li>
  <li><strong>Inject at multiple levels.</strong> A single injection point at the top or bottom of a 600&nbsp;m shaft cannot produce a uniform profile against the shaft's own stack gradient.</li>
  <li><strong>Relieve the doors-closed case.</strong> With every door shut, a fan sized for the doors-open case will over-pressurise; barometric or modulating relief is required.</li>
  <li><strong>Pressurise the lobby as an alternative.</strong> Pressurising protected lobbies rather than the shafts is often easier to control, uses less air, and puts the pressure where the smoke barrier actually is.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Hoistway pressurisation airflow vs leakage area</div>
    <div class="fsub">Q = 0.83·A·√Δp — the EN 12101-6 / NFPA 92 form, with a discharge coefficient of 0.65 folded into the constant — applied to effective leakage area. An open landing door is taken as 2.0 m² of free area. Landing-door leakage dominates and scales with the number of floors served.</div>
  </div>
  <div class="chart-box"><canvas id="pressChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Floors served <span id="vFl">60</span></label>
      <input type="range" id="sFl" min="5" max="150" value="60" step="1">
      <div class="hint">Landing doors on the shaft.</div>
    </div>
    <div class="ctrl">
      <label>Leakage per door <span id="vAd">0.020 m²</span></label>
      <input type="range" id="sAd" min="0.005" max="0.06" value="0.02" step="0.001">
      <div class="hint">Effective leakage area of one landing door assembly.</div>
    </div>
    <div class="ctrl">
      <label>Design pressure <span id="vDp">50 Pa</span></label>
      <input type="range" id="sDp" min="12" max="60" value="50" step="1">
      <div class="hint">NFPA 92 minimum 12.5 Pa sprinklered; EN 12101-6 Class B ≈ 50 Pa.</div>
    </div>
    <div class="ctrl">
      <label>Open doors allowance <span id="vOd">2</span></label>
      <input type="range" id="sOd" min="0" max="4" value="2" step="1">
      <div class="hint">Doors assumed open simultaneously in the design case.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Closed-door leakage</div><div class="v" id="rAl">1.20 <small>m²</small></div></div>
    <div class="cell"><div class="k">Flow, doors closed</div><div class="v" id="rQc">7.0 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Flow, doors open</div><div class="v" id="rQo">30.5 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Fan duct at 12 m/s</div><div class="v" id="rDa">2.5 <small>m²</small></div></div>
    <div class="cell"><div class="k">Turndown needed</div><div class="v" id="rTd">4.3<small>×</small></div></div>
  </div>
</div>
<p class="fig-note">Sixty landing doors at 0.02&nbsp;m² each give <strong>1.2&nbsp;m² of leakage</strong> and need <strong>7.0&nbsp;m³/s</strong> just to hold 50&nbsp;Pa with everything shut — rising to <strong>30.5&nbsp;m³/s</strong> if the same 50&nbsp;Pa has to be held with two doors open. That <strong>4.3:1 turndown</strong> between the two design cases is the whole control problem: a fan big enough for the open-door case will destroy the closed-door case unless relief or variable speed is provided, and a fan sized for the closed-door case simply fails when the fire service opens a door. One caveat that decides how much air you actually buy: the codes do not require full pressure to be held with a door open. EN 12101-6 and NFPA 92 set the open-door case as a <em>velocity</em> through the opening — typically 0.75–2&nbsp;m/s — which is a fraction of the air needed to hold 50&nbsp;Pa. Establish with the authority which criterion applies before selecting the fan, then specify and commission both cases explicitly.</p>

<h2 id="install">5 · Installation, coordination &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Get the machine-room cooling into the concept design.</strong> The single most common failure on this interface is a lift machine room with no chilled water route, discovered when the risers are already cast. Put it on the zone schematic at concept stage with its load, its N+1 requirement and its essential-power supply.</li>
  <li><strong>Never route anything else through a hoistway.</strong> Codes prohibit it and it is still attempted — no pipework, no cabling, no drainage other than what serves the lift itself.</li>
  <li><strong>Drain the pit, and think about where the water comes from.</strong> Pits flood from sprinkler discharge, washdown and groundwater. Provide a drained, pumped pit with an oil separator, and coordinate the sprinkler and shunt-trip arrangement so power is isolated before water is discharged into a shaft with live equipment.</li>
  <li><strong>Fire-stop the landing door surrounds and the shaft penetrations</strong> to the rated standard — they are both a fire barrier and the leakage area in the pressurisation calculation, so a poor installation fails twice.</li>
  <li><strong>Coordinate the shunt trip, the fire alarm and the lift controller</strong> as one sequence, and test it as one sequence. Phase 1 recall, Phase 2 fire-service operation, machine-room cooling status and pressurisation start-up all interact.</li>
  <li><strong>Measure the real door differential at commissioning</strong>, at the top and bottom of every zone, with the pressurisation running and with it off, and in the design season. The stack article's recommendation for permanent differential-pressure sensors applies here more than anywhere.</li>
  <li><strong>Check harmonics from the drives.</strong> A bank of large regenerative drives is a significant harmonic source close to sensitive equipment; specify the limits and the mitigation with the electrical engineer rather than accepting the lift supplier's default.</li>
  <li><strong>Plan the rope and machine replacement route</strong> at the machine room, with a certified lifting beam — the same discipline as any other plant room.</li>
</ul>

<h2 id="checklist">6 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Schedule the machine-room heat load</strong> per group, with cooling on essential power and N+1 where lift availability is critical.</li>
  <li><strong>Evaluate regenerative drives</strong> for both room load and building energy, with the harmonic consequence priced.</li>
  <li><strong>Fix the shaft blockage ratio early</strong> — it is the dominant piston-effect variable and it belongs in the concept dialogue with the VT consultant.</li>
  <li><strong>Provide inter-shaft venting within lift banks</strong> rather than venting shafts to atmosphere.</li>
  <li><strong>Design pressurisation for both the doors-open and doors-closed cases</strong>, with multi-level injection and relief.</li>
  <li><strong>Do not vent hoistways permanently</strong> — coordinate with the stack-effect strategy.</li>
  <li><strong>Drain and protect the pit</strong>, and coordinate sprinkler discharge with power isolation.</li>
  <li><strong>Fire-stop landing surrounds</strong> to both the fire rating and the assumed leakage area.</li>
  <li><strong>Test the whole fire sequence end to end</strong>, and measure real door differentials in season.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  The lift package is not an MEP scope, but four of its consequences are: a machine room that is really a <strong>108&nbsp;kW plant room</strong> needing chilled water on essential power; a hoistway that is the building's <strong>principal chimney</strong> and must not be solved with a permanent vent; a car that at 10&nbsp;m/s and 60&nbsp;% blockage generates <strong>160&nbsp;Pa</strong> of piston pressure on top of the stack effect, fixed far more cheaply by shaft dimension than by any equipment; and a pressurisation system with a <strong>3.6:1 turndown</strong> between its two code design cases. Get all four onto the zone schematic at concept stage, because every one of them is cast into the core.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>CIBSE <em>Guide D — Transportation Systems in Buildings</em> — lift heat gains, machine room environment, shaft design and interfaces with building services.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — lift machine room cooling, hoistway pressurisation and stack-effect interaction.</li>
  <li>Klote, J.H. &amp; Milke, J.A. <em>Handbook of Smoke Control Engineering</em> (ASHRAE/SFPE/ICC) — elevator piston effect, hoistway pressurisation and door forces.</li>
  <li>NFPA 92 — <em>Standard for Smoke Control Systems</em>: pressurisation design cases, doors-open criteria and relief requirements; and EN 12101-6 for pressure differential systems.</li>
  <li>EN 81-20 / EN 81-50 and ASME A17.1 — lift safety requirements including machine room environment, pit drainage and firefighter lift provisions.</li>
  <li>ISO 25745 — energy performance of lifts, including regenerative drive assessment and duty categories.</li>
  <li>Council on Tall Buildings and Urban Habitat (CTBUH) — tall building vertical transportation strategy, sky lobbies and lift zoning.</li>
  <li>International Building Code (IBC) and Saudi Building Code <em>SBC 801</em> — fire-service access lifts, occupant evacuation elevators and hoistway protection.</li>
</ol>

<div class="tags">#VerticalTransportation #Lifts #Elevators #TallBuildings #MegatallBuildings #MachineRoom #MRL #HeatGain #RegenerativeDrive #PistonEffect #Hoistway #ShaftDesign #BlockageRatio #StackEffect #Pressurisation #NFPA92 #EN121016 #FirefighterLift #OccupantEvacuationElevator #PitDrainage #ShuntTrip #Harmonics #Coordination #Commissioning #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const RHO=1.2;

/* ---------- CHART 1 : machine room heat ---------- */
const sN=document.getElementById('sN'),sP=document.getElementById('sP'),
      sEf=document.getElementById('sEf'),sDu=document.getElementById('sDu'),sRg=document.getElementById('sRg');
const roomQ=(n,P,e,d,r)=>n*P*(1-e)*d*(1-r);
let heatChart=new Chart(document.getElementById('heatChart'),{
  data:{datasets:[
    {type:'line',label:'Heat rejected to the machine room',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'With regenerative recovery',data:[],borderColor:'#1b4f72',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'Your group',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1,max:16,title:{display:true,text:'Lifts in the group',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Heat to the machine room (kW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} kW with ${fmt0(c.parsed.x)} lifts`}}}}
});
function updHeat(){
  const n=+sN.value,P=+sP.value,e=+sEf.value/100,d=+sDu.value/100,r=+sRg.value/100;
  document.getElementById('vN').textContent=n;
  document.getElementById('vP').textContent=P+' kW';
  document.getElementById('vEf').textContent=fmt0(e*100)+' %';
  document.getElementById('vDu').textContent=fmt0(d*100)+' %';
  document.getElementById('vRg').textContent=fmt0(r*100)+' %';
  const xs=[];for(let i=1;i<=16;i++)xs.push(i);
  heatChart.data.datasets[0].data=xs.map(i=>({x:i,y:+roomQ(i,P,e,d,0).toFixed(1)}));
  heatChart.data.datasets[1].data=xs.map(i=>({x:i,y:+roomQ(i,P,e,d,r).toFixed(1)}));
  const Q=roomQ(n,P,e,d,r);
  heatChart.data.datasets[2].data=[{x:n,y:+Q.toFixed(1)}];
  heatChart.update('none');
  document.getElementById('rQ').innerHTML=fmt0(Q)+' <small>kW</small>';
  document.getElementById('rTr').innerHTML=fmt0(Q/3.517)+' <small>TR</small>';
  document.getElementById('rPl').innerHTML=fmt1(Q/n)+' <small>kW</small>';
  document.getElementById('rAf').innerHTML=fmt1(Q/(1.2*1.005*8))+' <small>m³/s</small>';
  const v=document.getElementById('rVd');
  if(Q<20)       v.innerHTML='<span class="badge good">ventilation may suffice</span>';
  else if(Q<60)  v.innerHTML='<span class="badge warn">dedicated cooling</span>';
  else           v.innerHTML='<span class="badge bad">plant room — chilled water + N+1</span>';
}
[sN,sP,sEf,sDu,sRg].forEach(s=>s.addEventListener('input',updHeat));updHeat();

/* ---------- CHART 2 : piston effect ---------- */
const sV=document.getElementById('sV'),sB=document.getElementById('sB'),
      sK=document.getElementById('sK'),sDt=document.getElementById('sDt');
const annV=(v,B)=>v*B/(1-B);
const piston=(v,B,K)=>0.5*RHO*K*Math.pow(annV(v,B),2);
let pistonChart=new Chart(document.getElementById('pistonChart'),{
  data:{datasets:[
    {type:'line',label:'At your blockage ratio',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'At 40 % blockage (open shaft)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your car',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1,max:18,title:{display:true,text:'Car speed (m/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Piston pressure (Pa)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} Pa at ${fmt1(c.parsed.x)} m/s`}},
      annotation:{annotations:{
        dt:{type:'line',scaleID:'y',yScaleID:'y',value:60,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'door tolerance',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updPiston(){
  const v=+sV.value,B=+sB.value,K=+sK.value,dt=+sDt.value;
  document.getElementById('vV').textContent=fmt1(v)+' m/s';
  document.getElementById('vB').textContent=fmt2(B);
  document.getElementById('vK').textContent=fmt2(K);
  document.getElementById('vDt').textContent=dt+' Pa';
  const xs=[];for(let s2=1;s2<=18;s2+=0.25)xs.push(+s2.toFixed(2));
  pistonChart.data.datasets[0].data=xs.map(s2=>({x:s2,y:+piston(s2,B,K).toFixed(0)}));
  pistonChart.data.datasets[1].data=xs.map(s2=>({x:s2,y:+piston(s2,0.40,K).toFixed(0)}));
  const dp=piston(v,B,K);
  pistonChart.data.datasets[2].data=[{x:v,y:+dp.toFixed(0)}];
  pistonChart.options.plugins.annotation.annotations.dt.value=dt;
  pistonChart.options.scales.y.max=Math.max(piston(18,B,K)*0.55,dt*3);
  pistonChart.update('none');
  const vmax=Math.sqrt(2*dt/(RHO*K))*(1-B)/B;
  const bmax=1/(1+v/Math.sqrt(2*dt/(RHO*K)));
  document.getElementById('rVa').innerHTML=fmt1(annV(v,B))+' <small>m/s</small>';
  document.getElementById('rDp').innerHTML=fmt0(dp)+' <small>Pa</small>';
  document.getElementById('rVm').innerHTML=fmt1(vmax)+' <small>m/s</small>';
  document.getElementById('rBm').textContent=fmt2(bmax);
  const e=document.getElementById('rPv');
  if(dp<=dt*0.6)     e.innerHTML='<span class="badge good">within tolerance</span>';
  else if(dp<=dt)    e.innerHTML='<span class="badge warn">marginal</span>';
  else               e.innerHTML='<span class="badge bad">doors will misbehave</span>';
}
[sV,sB,sK,sDt].forEach(s=>s.addEventListener('input',updPiston));updPiston();

/* ---------- CHART 3 : hoistway pressurisation ---------- */
const sFl=document.getElementById('sFl'),sAd=document.getElementById('sAd'),
      sDp=document.getElementById('sDp'),sOd=document.getElementById('sOd');
const OPEN_A=2.0;   // m2 free area of one open landing door (1.0 x 2.1 m)
const flow=(A,dp)=>0.83*A*Math.sqrt(dp);   // EN 12101-6 / NFPA 92 form, Cd 0.65 folded into the 0.83
let pressChart=new Chart(document.getElementById('pressChart'),{
  data:{datasets:[
    {type:'line',label:'Doors closed',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'With design doors open',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'Your shaft',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:150,title:{display:true,text:'Floors served by the shaft',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Pressurisation airflow (m³/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} m³/s at ${fmt0(c.parsed.x)} floors`}}}}
});
function updPress(){
  const F=+sFl.value,Ad=+sAd.value,dp=+sDp.value,od=+sOd.value;
  document.getElementById('vFl').textContent=F;
  document.getElementById('vAd').textContent=fmt3(Ad)+' m²';
  document.getElementById('vDp').textContent=dp+' Pa';
  document.getElementById('vOd').textContent=od;
  const xs=[];for(let f=5;f<=150;f+=1)xs.push(f);
  pressChart.data.datasets[0].data=xs.map(f=>({x:f,y:+flow(f*Ad,dp).toFixed(2)}));
  pressChart.data.datasets[1].data=xs.map(f=>({x:f,y:+flow(f*Ad+od*OPEN_A,dp).toFixed(2)}));
  const Ac=F*Ad, Qc=flow(Ac,dp), Qo=flow(Ac+od*OPEN_A,dp);
  pressChart.data.datasets[2].data=[{x:F,y:+Qc.toFixed(2)}];
  pressChart.update('none');
  document.getElementById('rAl').innerHTML=fmt2(Ac)+' <small>m²</small>';
  document.getElementById('rQc').innerHTML=fmt1(Qc)+' <small>m³/s</small>';
  document.getElementById('rQo').innerHTML=fmt1(Qo)+' <small>m³/s</small>';
  document.getElementById('rDa').innerHTML=fmt1(Qo/12)+' <small>m²</small>';
  document.getElementById('rTd').innerHTML=fmt1(Qo/Qc)+'<small>×</small>';
}
[sFl,sAd,sDp,sOd].forEach(s=>s.addEventListener('input',updPress));updPress();

window.addEventListener('load',function(){try{heatChart.resize();pistonChart.resize();pressChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='vertical-transportation-mep-tall-buildings', cat='tallmep', mins=16,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Lifts &amp; MEP in Megatall Buildings: Machine-Room Heat, Piston Effect &amp; Hoistway Pressurisation',
    reg_title='Lifts & MEP in Megatall Buildings: Machine-Room Heat, Piston Effect & Hoistway Pressurisation',
    reg_tag='Tall-Building Systems · Lifts · MEP Interfaces',
    breadcrumb='Tall-Building Systems',
    tag_line='Tall-Building Systems &middot; Vertical Transportation &middot; MEP Interfaces',
    desc='The MEP interfaces of vertical transportation in megatall buildings: lift machine-room heat gain and why it is a plant room needing chilled water on essential power, regenerative drives, piston effect pressure from high-speed cars and why shaft blockage ratio dominates it, hoistway and lobby pressurisation and the turndown between the doors-open and doors-closed design cases, pit drainage and fire sequence coordination — with three interactive charts and installation tricks.',
    og_desc='A bank of eight lifts dumps 108 kW into a room nobody scheduled, a 10 m/s car generates 162 Pa of piston pressure on top of the stack effect, and hoistway pressurisation has a 3.6:1 turndown between its two code cases.',
    ld_desc='A design-perspective guide to the MEP interfaces of lifts in megatall buildings: machine-room heat gain and cooling, regenerative drives, piston effect and shaft blockage ratio, hoistway and lobby pressurisation design cases, pit drainage, shunt trip and fire sequence coordination.',
    img_alt='Technical cutaway of a megatall tower&rsquo;s lift core showing a high-speed car in its hoistway with air displaced around it, the machine room above with its drives and cooling plant, and pressurisation ductwork injecting into the shaft at several levels',
    en_tag='Tall-Building Systems &middot; Lifts &middot; MEP Interfaces &middot; Megatall',
    en_title='Lifts &amp; MEP in Megatall Buildings: Machine-Room Heat, Piston Effect &amp; Hoistway Pressurisation',
    en_excerpt='The lifts are somebody else&rsquo;s package, yet four of their consequences are squarely MEP. A bank of eight machines dumps <strong>108&nbsp;kW</strong> into a room that is usually unconditioned in the concept design; the hoistway is the building&rsquo;s dominant chimney; a car at 10&nbsp;m/s and 60&nbsp;% blockage generates <strong>160&nbsp;Pa</strong> of piston pressure on top of the stack effect, fixed far more cheaply by shaft dimension than by equipment; and pressurisation has a <strong>3.6:1 turndown</strong> between its doors-open and doors-closed cases &mdash; with three interactive charts.',
    en_search='vertical transportation lifts elevators MEP interface tall buildings megatall supertall machine room heat gain MRL machine room less drive cabinet motor losses duty cycle regenerative drive harmonics essential power N+1 cooling chilled water ambient limit derating piston effect blockage ratio car speed annulus velocity shaft dimension inter-shaft venting aerodynamic shroud landing door differential stack effect hoistway pressurisation lobby pressurisation NFPA 92 EN 12101-6 doors open doors closed turndown relief damper multi-level injection firefighter lift occupant evacuation elevator pit drainage sump oil separator sprinkler shunt trip phase 1 recall fire alarm interface commissioning CIBSE Guide D EN 81-20 ASME A17.1 ISO 25745 MEP building services',
    ar_title='المصاعد وأنظمة الميكانيكا في المباني فائقة الارتفاع: حرارة غرفة الماكينة وتأثير المكبس وتضغيط البئر',
    ar_excerpt='المصاعد حزمة عمل تخصّ غيرك، لكن أربعًا من نتائجها تقع مباشرة على مهندس الأنظمة. مجموعة من ثمانية مصاعد تطرح <strong>١٠٨ كيلوواط</strong> في غرفة لا تُكيَّف عادةً في التصميم المبدئي؛ وبئر المصعد هو المدخنة الرئيسية للمبنى؛ وكابينة بسرعة ١٠ م/ث ونسبة انسداد ٦٠٪ تولّد <strong>١٦٠ باسكال</strong> من ضغط المكبس فوق تأثير المدخنة، وعلاجه بأبعاد البئر أرخص بكثير من أي معدات؛ ولنظام التضغيط نسبة تخفيض <strong>٣٫٦:١</strong> بين حالتَي الأبواب المفتوحة والمغلقة — مع ثلاثة رسوم تفاعلية.',
    ar_search='vertical transportation lifts elevators MEP machine room heat regenerative drive piston effect blockage ratio hoistway pressurisation NFPA 92 EN 12101-6 pit drainage shunt trip CIBSE Guide D EN 81-20 المصاعد النقل الرأسي واجهات الأنظمة الميكانيكية المباني الشاهقة المباني فائقة الارتفاع غرفة الماكينة الكسب الحراري المصاعد بدون غرفة ماكينة خزانة المشغل فواقد المحرك دورة التشغيل المشغل المسترجع للطاقة التوافقيات الكهربائية الطاقة الأساسية التبريد الاحتياطي المياه المبردة حد درجة الحرارة المحيطة خفض القدرة تأثير المكبس نسبة الانسداد سرعة الكابينة سرعة الحلقة أبعاد البئر التهوية بين الآبار الغطاء الانسيابي فرق الضغط على باب الطابق تأثير المدخنة تضغيط بئر المصعد تضغيط الردهة الأبواب المفتوحة الأبواب المغلقة نسبة التخفيض مخمد التنفيس الحقن متعدد المستويات مصعد رجال الإطفاء مصعد إخلاء الشاغلين صرف حفرة المصعد فاصل الزيت الرشاش قطع التغذية استدعاء المرحلة الأولى واجهة إنذار الحريق التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
