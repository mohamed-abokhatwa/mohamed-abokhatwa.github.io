# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Refrigerant is the only fluid in the building that is dangerous, expensive, environmentally regulated and <strong>a gas and a liquid at the same time</strong> — and the last of those is what makes tall buildings hard. Water in a riser is just heavy. Refrigerant in a riser is a liquid column that boils if you let its pressure fall, an oil carrier that stops carrying if the velocity drops, and a charge that has to be small enough that if it all leaks into one room, the people in that room survive. Those three constraints — <strong>flash gas, oil return and refrigerant concentration limit</strong> — are what actually decide whether a direct-expansion system can be used in a tower at all, and they bite long before the capacity tables do.</p>

<h2 id="why">1 · Three constraints, all of them vertical</h2>
<ul class="clean">
  <li><strong>The liquid column has weight.</strong> A 100&nbsp;m vertical lift in an R-410A liquid line costs about <strong>9.3&nbsp;bar</strong> of static pressure. If the liquid arrives at the expansion device below its saturation pressure it has already flashed to gas, the device loses control and the coil starves.</li>
  <li><strong>Oil has to come home.</strong> Compressor oil circulates with the refrigerant and must be dragged back up vertical suction risers by gas velocity alone. Below a critical velocity it drains back, and the compressor eventually runs dry — a failure that appears months after handover and is always blamed on the compressor.</li>
  <li><strong>The charge is a safety limit, not a cost item.</strong> ASHRAE 15 caps the refrigerant that may be released into an occupied space by the <strong>refrigerant concentration limit</strong>. In a tower with hundreds of small rooms, the governing room is a small one — and for the newer A2L refrigerants the allowable charge is roughly a seventh of what R-410A allowed.</li>
</ul>

<h2 id="flash">2 · Static head, flash gas and the real height limit</h2>
<p>Liquid refrigerant lifted through a height \(h\) loses static pressure \( \Delta p = \rho g h\). To arrive as liquid, it must leave the condenser sub-cooled by enough that this pressure drop does not take it below saturation:</p>
<div class="eq">\[ \Delta T_{sub,\;req} \;=\; \frac{\rho\,g\,h}{(\mathrm{d}p/\mathrm{d}T)_{sat}} \]</div>
<p>For R-410A near 40&nbsp;°C the saturation curve runs at roughly 0.60&nbsp;bar/K and the liquid density is about 950&nbsp;kg/m³, so <strong>every 10&nbsp;m of lift consumes about 1.5&nbsp;K of sub-cooling</strong>. Practical systems can deliver 10–12&nbsp;K before the condenser has to be oversized or a sub-cooler added, which puts the maximum lift at roughly <strong>77&nbsp;m</strong>. That is not a manufacturer's marketing limit — it is why VRF catalogues state maximum indoor-to-outdoor height differences of 50–90&nbsp;m, and it is why a tower cannot be served by one refrigerant system from a single plant deck.</p>

<div class="callout key">
  <span class="lbl">The orientation that costs nothing</span>
  The penalty applies to <em>lifting</em> liquid. Put the condensing unit <strong>above</strong> the evaporators and the liquid line falls, gaining pressure instead of losing it — the static head now works for you, and the constraint moves to the suction riser and oil return instead. In a tower this is close to free: place the condensing plant at the top of each refrigerant zone rather than the bottom, and the flash-gas limit largely disappears. Getting this the wrong way round is one of the most common and most expensive DX layout errors in tall buildings.
</div>

<h2 id="int-flash">3 · Interactive: sub-cooling required for a liquid lift</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Sub-cooling needed to prevent flash gas vs vertical lift</div>
    <div class="fsub">ΔT = ρgh / (dp/dT)&#115;&#97;&#116;, plus the sub-cooling consumed by line friction. The dashed line is the practical sub-cooling a normal condenser can deliver; where the curve crosses it is the height limit of the system.</div>
  </div>
  <div class="chart-box"><canvas id="flashChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Vertical lift <span id="vH">60 m</span></label>
      <input type="range" id="sH" min="0" max="200" value="60" step="2">
      <div class="hint">Height the liquid line must rise from condenser to expansion device.</div>
    </div>
    <div class="ctrl">
      <label>Liquid density <span id="vRo">950 kg/m³</span></label>
      <input type="range" id="sRo" min="700" max="1300" value="950" step="10">
      <div class="hint">R-410A ≈ 950, R-134a ≈ 1150, R-32 ≈ 900 near 40 °C.</div>
    </div>
    <div class="ctrl">
      <label>Saturation slope dp/dT <span id="vSl">0.60 bar/K</span></label>
      <input type="range" id="sSl" min="0.15" max="1.0" value="0.60" step="0.01">
      <div class="hint">R-410A ≈ 0.60, R-134a ≈ 0.28, R-32 ≈ 0.62 near 40 °C.</div>
    </div>
    <div class="ctrl">
      <label>Available sub-cooling <span id="vSc">12 K</span></label>
      <input type="range" id="sSc" min="3" max="25" value="12" step="0.5">
      <div class="hint">What the condenser or a liquid sub-cooler can actually deliver.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Static pressure lost</div><div class="v" id="rDp">5.59 <small>bar</small></div></div>
    <div class="cell"><div class="k">Sub-cooling needed</div><div class="v" id="rSc">9.3 <small>K</small></div></div>
    <div class="cell"><div class="k">Max lift available</div><div class="v" id="rMx">77 <small>m</small></div></div>
    <div class="cell"><div class="k">Margin</div><div class="v" id="rMg">2.7 <small>K</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">At the default R-410A properties, a <strong>60&nbsp;m lift costs 5.6&nbsp;bar and 9.3&nbsp;K of sub-cooling</strong> against 12&nbsp;K available — a margin of only 2.7&nbsp;K before the liquid line starts producing flash gas, and that is before line friction and a hot riser shaft are counted. The limit is about <strong>77&nbsp;m</strong>. Switch to R-134a with its shallower saturation slope and heavier liquid and the picture changes completely, which is exactly why centrifugal chillers with R-134a and a water distribution system remain the default for tall buildings while DX stays a zone-by-zone solution.</p>

<h2 id="oil">4 · Oil return — the failure that arrives eighteen months late</h2>
<p>Oil leaves the compressor with the refrigerant and returns only if the suction gas moves fast enough to carry it up vertical risers. The minimum carrying velocity is roughly <strong>5–7&nbsp;m/s</strong> in a vertical suction riser, and — critically — it must be achieved at <strong>minimum load</strong>, not at design. A variable-capacity system that turns down to 25&nbsp;% has a quarter of the velocity in a riser sized for full flow.</p>
<ul class="clean">
  <li><strong>Size risers on minimum load, and size horizontal runs on pressure drop.</strong> These are different criteria and they give different diameters; the riser is nearly always smaller than the horizontal main.</li>
  <li><strong>Use a double suction riser</strong> where turndown is wide: a small riser sized for minimum load and a larger one that floods with oil at low load and takes over as flow rises. Fit the trap at the base and the connection at the top correctly — reversed, it does nothing.</li>
  <li><strong>Trap at the base of every riser</strong> and at intervals up long risers (commonly every 6–8&nbsp;m) so the oil is lifted in stages rather than as one column.</li>
  <li><strong>Slope horizontal suction lines back toward the compressor</strong> so gravity helps rather than pooling oil in a low point.</li>
  <li><strong>Do not oversize the pipe.</strong> Oversizing a suction line is not conservative — it is the direct cause of oil starvation. This is the opposite instinct to water design and it catches people out.</li>
</ul>

<h2 id="rcl">5 · Refrigerant concentration limit — the constraint that decides the system</h2>
<p>ASHRAE 15 and ISO 5149 limit the refrigerant that may enter an occupied space so that a complete leak from the system cannot produce a hazardous concentration. The rule is simple and unforgiving<sup class="cite">[1][2]</sup>:</p>
<div class="eq">\[ m_{allowable} \;=\; RCL \times V_{smallest\ occupied\ space} \]</div>
<p>The governing volume is <strong>the smallest room the system serves</strong>, not the floor area or the building. In a hotel or residential tower that is a bathroom or a small bedroom, and it is brutal: a 50&nbsp;m³ room permits 22&nbsp;kg of R-410A, 12.5&nbsp;kg of R-134a — and only <strong>3.0&nbsp;kg</strong> of R-32, because the A2L refrigerants are limited by flammability rather than toxicity. As the industry moves to lower-GWP A2L and A3 refrigerants, allowable charges fall by roughly a factor of seven, and systems that were compliant on R-410A are not on their replacement.</p>
<p>The design responses, in order of preference: <strong>reduce the charge</strong> (smaller circuits, more of them); <strong>increase the volume</strong> the leak can disperse into (permanent openings, ducted returns connecting spaces); <strong>detect and ventilate</strong> (leak detection with mechanical extract, which many codes accept as mitigation); or <strong>change the system</strong> to a chilled-water or DOAS arrangement where the refrigerant never leaves the plant room. In tall residential towers the last of these is increasingly the only compliant answer.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Allowable refrigerant charge vs smallest served room</div>
    <div class="fsub">m = RCL × V. The marker is your system charge against the room it serves. RCL from ASHRAE 34: toxicity-based for A1 refrigerants, flammability-based (a fraction of the LFL) for A2L.</div>
  </div>
  <div class="chart-box"><canvas id="rclChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Smallest room volume <span id="vV">50 m³</span></label>
      <input type="range" id="sV" min="10" max="600" value="50" step="5">
      <div class="hint">The smallest occupied space any part of the circuit serves.</div>
    </div>
    <div class="ctrl">
      <label>Refrigerant RCL <span id="vRc">0.440 kg/m³</span></label>
      <input type="range" id="sRc" min="0.02" max="0.6" value="0.44" step="0.001">
      <div class="hint">R-410A 0.44, R-134a 0.25, R-32 0.061, R-1234yf 0.058 kg/m³.</div>
    </div>
    <div class="ctrl">
      <label>System charge <span id="vCh">18 kg</span></label>
      <input type="range" id="sCh" min="1" max="200" value="18" step="1">
      <div class="hint">Total charge of the circuit that serves that room.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Allowable charge</div><div class="v" id="rAl">22.0 <small>kg</small></div></div>
    <div class="cell"><div class="k">Your charge</div><div class="v" id="rCh">18 <small>kg</small></div></div>
    <div class="cell"><div class="k">Utilisation</div><div class="v" id="rUt">82 <small>%</small></div></div>
    <div class="cell"><div class="k">Room needed</div><div class="v" id="rVn">41 <small>m³</small></div></div>
    <div class="cell"><div class="k">Compliance</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rCv"></span></div></div>
  </div>
</div>
<p class="fig-note">A 50&nbsp;m³ bedroom permits <strong>22&nbsp;kg of R-410A</strong>, so an 18&nbsp;kg circuit passes with little room to spare. Now drag the RCL down to 0.061 for R-32: the same room permits <strong>3.0&nbsp;kg</strong> and the design fails by a factor of six. That single slider is the whole refrigerant-transition problem for tall residential buildings, and it is why so many towers are moving their refrigerant into a plant room and distributing water instead.</p>

<h2 id="machinery">6 · Machinery rooms, detection and emergency ventilation</h2>
<p>Where the charge cannot be kept below the concentration limit, the refrigerant is confined to a <strong>refrigerating machinery room</strong> with its own construction, detection and ventilation requirements. ASHRAE 15 fixes the emergency ventilation rate from the largest single charge in the room<sup class="cite">[1]</sup>:</p>
<div class="eq">\[ Q \;=\; 70\,\sqrt{G} \qquad (\text{L/s},\ G\ \text{in kg}) \]</div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Machinery room emergency ventilation vs system charge</div>
    <div class="fsub">Q = 70·√G, the ASHRAE 15 emergency exhaust rate for a refrigerating machinery room, with G the largest single refrigerant charge in the room.</div>
  </div>
  <div class="chart-box"><canvas id="ventChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Largest single charge <span id="vG">500 kg</span></label>
      <input type="range" id="sG" min="20" max="3000" value="500" step="10">
      <div class="hint">Not the room total — the largest individual system.</div>
    </div>
    <div class="ctrl">
      <label>Room volume <span id="vRv">600 m³</span></label>
      <input type="range" id="sRv" min="50" max="3000" value="600" step="25">
      <div class="hint">Used here to express the rate as air changes per hour.</div>
    </div>
    <div class="ctrl">
      <label>Duct velocity <span id="vDv">10 m/s</span></label>
      <input type="range" id="sDv" min="5" max="18" value="10" step="0.5">
      <div class="hint">To size the emergency exhaust duct and its discharge.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Emergency rate</div><div class="v" id="rQ">1,565 <small>L/s</small></div></div>
    <div class="cell"><div class="k">In m³/s</div><div class="v" id="rQm">1.57 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Air changes</div><div class="v" id="rAc">9.4 <small>ACH</small></div></div>
    <div class="cell"><div class="k">Duct area</div><div class="v" id="rDa">0.16 <small>m²</small></div></div>
    <div class="cell"><div class="k">Round duct</div><div class="v" id="rDd">446 <small>mm</small></div></div>
  </div>
</div>
<p class="fig-note">A 500&nbsp;kg charge demands <strong>1,565&nbsp;L/s</strong> of emergency exhaust — about 9 air changes an hour in a 600&nbsp;m³ plant room, through a 450&nbsp;mm duct that must discharge somewhere safe and never near an air intake. Note the square root: doubling the charge only raises the rate by 41&nbsp;%, so consolidating into fewer large machines is ventilation-efficient, while the concentration limit pushes the opposite way. Detection is the other half — sensors at low level for heavier-than-air refrigerants, alarm and ventilation interlock, a purge control outside the room, and self-closing tight-fitting doors.</p>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Braze under flowing nitrogen, always.</strong> Without it the inside of the pipe oxidises and sheds scale that ends up in the expansion valves and the compressor. This is the single most-skipped and most-damaging shortcut in refrigerant pipework, and it cannot be inspected afterwards.</li>
  <li><strong>Pressure-test with nitrogen, then evacuate to a target vacuum and prove it.</strong> Triple evacuation to below 500 microns with a rise test — a vacuum that climbs is either a leak or trapped moisture, and you must know which before charging.</li>
  <li><strong>Weigh the charge in and record it.</strong> Charge by weight against the calculated value, and log the actual figure per circuit; regulatory leak-checking regimes are all based on the recorded charge.</li>
  <li><strong>Support risers for weight and for expansion.</strong> A long copper riser moves with temperature and must be anchored and guided so the movement lands in a designed loop, not on a branch tee.</li>
  <li><strong>Insulate the suction line completely, including at supports.</strong> Every uninsulated clamp on a cold suction riser inside a shaft becomes a condensation source, and in a tall shaft that water runs a long way before anyone finds it.</li>
  <li><strong>Fit isolation valves and access ports per zone</strong> so a fault does not require the whole riser to be recovered — recovery of a large charge from a tall system is a multi-day operation.</li>
  <li><strong>Commission at low load, not just at design.</strong> Oil return problems only appear at minimum capacity; run the system down to its lowest step and check compressor oil level and suction superheat there.</li>
  <li><strong>Label the charge and the leak-check regime</strong> on the plant and in the O&amp;M, with the responsible person named — this is a legal requirement in most jurisdictions and it is routinely missing.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Check the concentration limit against the smallest served room</strong>, for the refrigerant actually being installed, before selecting the system type.</li>
  <li><strong>Put condensing plant above the evaporators</strong> wherever possible so the liquid line falls.</li>
  <li><strong>Calculate the sub-cooling budget</strong> for the lift, the friction and the shaft temperature, with margin.</li>
  <li><strong>Size suction risers on minimum load</strong>, with double risers and traps where turndown is wide.</li>
  <li><strong>Never oversize suction pipework.</strong></li>
  <li><strong>Plan for the A2L transition</strong> — check whether the design still complies on the replacement refrigerant.</li>
  <li><strong>Design machinery rooms fully</strong> — construction, detection, emergency ventilation at 70√G, discharge location, purge control.</li>
  <li><strong>Specify nitrogen purge brazing, evacuation targets and weighed charging</strong> as inspected hold points.</li>
  <li><strong>Commission at minimum load</strong> and record the charge per circuit.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Refrigerant in a tower is limited by three vertical facts: <strong>a 100&nbsp;m liquid lift costs 9.3&nbsp;bar and about 15&nbsp;K of sub-cooling you do not have</strong> — so put the condensing plant on top and let the liquid fall; <strong>oil only comes back if the suction riser is sized for minimum load</strong>, which means the riser is smaller than instinct says; and <strong>the allowable charge is set by the smallest room the circuit serves</strong>, which for the incoming A2L refrigerants is roughly a seventh of what R-410A allowed. Those three, not the capacity tables, decide whether you distribute refrigerant at all — and in most megatall buildings the answer is to keep it in a plant room and distribute water.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ANSI/ASHRAE Standard 15 — <em>Safety Standard for Refrigeration Systems</em>: occupancy classification, refrigerant concentration limits, machinery room construction, detection and emergency ventilation (Q = 70√G).</li>
  <li>ANSI/ASHRAE Standard 34 — <em>Designation and Safety Classification of Refrigerants</em>: safety groups (A1, A2L, A3, B classes) and refrigerant concentration limits; and ISO 5149 for the international equivalent.</li>
  <li>ASHRAE <em>Handbook — Refrigeration</em>, System Practices for Halocarbon Refrigerants — liquid line sub-cooling, static head, suction riser sizing, double risers and oil management.</li>
  <li>ASHRAE <em>Handbook — HVAC Systems and Equipment</em>, Variable Refrigerant Flow chapter — VRF piping limits, height differences and capacity correction.</li>
  <li>EN 378 — <em>Refrigerating systems and heat pumps: safety and environmental requirements</em>; and the EU F-Gas Regulation and equivalent national regimes on charge records and leak checking.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — refrigerant distribution and plant location in tall buildings.</li>
  <li>Saudi Building Code <em>SBC 501</em> mechanical provisions and the Saudi regulations on refrigerant handling and machinery rooms.</li>
  <li>ACR/BRA and AREA industry codes of practice on brazing under nitrogen, evacuation, charging and system commissioning.</li>
</ol>

<div class="tags">#Refrigerant #DXSystems #VRF #TallBuildings #MegatallBuildings #ASHRAE15 #ASHRAE34 #RefrigerantConcentrationLimit #RCL #A2L #R410A #R32 #R134a #LowGWP #FGas #FlashGas #SubCooling #StaticHead #LiquidLine #SuctionRiser #OilReturn #DoubleRiser #MachineryRoom #LeakDetection #EmergencyVentilation #NitrogenPurge #Evacuation #Commissioning #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const G9=9.81;

/* ---------- CHART 1 : flash gas ---------- */
const sH=document.getElementById('sH'),sRo=document.getElementById('sRo'),
      sSl=document.getElementById('sSl'),sSc=document.getElementById('sSc');
const dpBar=(rho,h)=>rho*G9*h/1e5;
let flashChart=new Chart(document.getElementById('flashChart'),{
  data:{datasets:[
    {type:'line',label:'Sub-cooling required',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'scatter',label:'Your lift',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0,max:200,title:{display:true,text:'Vertical lift of the liquid line (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Sub-cooling required (K)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} K at ${fmt0(c.parsed.x)} m`}},
      annotation:{annotations:{
        av:{type:'line',scaleID:'y',yScaleID:'y',value:12,borderColor:'#1e8449',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'available sub-cooling',position:'start',font:{size:10,family:'DM Sans'},color:'#1e8449',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updFlash(){
  const h=+sH.value,rho=+sRo.value,sl=+sSl.value,sc=+sSc.value;
  document.getElementById('vH').textContent=h+' m';
  document.getElementById('vRo').textContent=rho+' kg/m³';
  document.getElementById('vSl').textContent=fmt2(sl)+' bar/K';
  document.getElementById('vSc').textContent=fmt1(sc)+' K';
  const req=x=>dpBar(rho,x)/sl;
  const xs=[];for(let x=0;x<=200;x+=2)xs.push(x);
  flashChart.data.datasets[0].data=xs.map(x=>({x:x,y:+req(x).toFixed(2)}));
  flashChart.data.datasets[1].data=[{x:h,y:+req(h).toFixed(2)}];
  flashChart.options.plugins.annotation.annotations.av.value=sc;
  flashChart.options.scales.y.max=Math.max(req(200),sc*1.3);
  flashChart.update('none');
  const maxLift=sc*sl*1e5/(rho*G9);
  document.getElementById('rDp').innerHTML=fmt2(dpBar(rho,h))+' <small>bar</small>';
  document.getElementById('rSc').innerHTML=fmt1(req(h))+' <small>K</small>';
  document.getElementById('rMx').innerHTML=fmt0(maxLift)+' <small>m</small>';
  document.getElementById('rMg').innerHTML=fmt1(sc-req(h))+' <small>K</small>';
  const v=document.getElementById('rVd'), m=sc-req(h);
  if(m<0)        v.innerHTML='<span class="badge bad">flash gas — will not work</span>';
  else if(m<3)   v.innerHTML='<span class="badge warn">no margin</span>';
  else           v.innerHTML='<span class="badge good">workable</span>';
}
[sH,sRo,sSl,sSc].forEach(s=>s.addEventListener('input',updFlash));updFlash();

/* ---------- CHART 2 : RCL ---------- */
const sV=document.getElementById('sV'),sRc=document.getElementById('sRc'),sCh=document.getElementById('sCh');
let rclChart=new Chart(document.getElementById('rclChart'),{
  data:{datasets:[
    {type:'line',label:'Allowable charge (RCL × V)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Your system charge',data:[],borderColor:'#c0392b',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your room',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:10,max:600,title:{display:true,text:'Smallest occupied room served (m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Refrigerant charge (kg)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} kg at ${fmt0(c.parsed.x)} m³`}}}}
});
function updRcl(){
  const V=+sV.value,rcl=+sRc.value,ch=+sCh.value;
  document.getElementById('vV').textContent=V+' m³';
  document.getElementById('vRc').textContent=fmt3(rcl)+' kg/m³';
  document.getElementById('vCh').textContent=ch+' kg';
  const xs=[];for(let v=10;v<=600;v+=5)xs.push(v);
  rclChart.data.datasets[0].data=xs.map(v=>({x:v,y:+(rcl*v).toFixed(2)}));
  rclChart.data.datasets[1].data=xs.map(v=>({x:v,y:ch}));
  rclChart.data.datasets[2].data=[{x:V,y:ch}];
  rclChart.options.scales.y.max=Math.max(rcl*600,ch*1.4);
  rclChart.update('none');
  const allow=rcl*V;
  document.getElementById('rAl').innerHTML=fmt1(allow)+' <small>kg</small>';
  document.getElementById('rCh').innerHTML=ch+' <small>kg</small>';
  document.getElementById('rUt').innerHTML=fmt0(100*ch/allow)+' <small>%</small>';
  document.getElementById('rVn').innerHTML=fmt0(ch/rcl)+' <small>m³</small>';
  const v=document.getElementById('rCv');
  if(ch<=allow*0.8)     v.innerHTML='<span class="badge good">compliant</span>';
  else if(ch<=allow)    v.innerHTML='<span class="badge warn">at the limit</span>';
  else                  v.innerHTML='<span class="badge bad">exceeds RCL</span>';
}
[sV,sRc,sCh].forEach(s=>s.addEventListener('input',updRcl));updRcl();

/* ---------- CHART 3 : machinery room ventilation ---------- */
const sG=document.getElementById('sG'),sRv=document.getElementById('sRv'),sDv=document.getElementById('sDv');
const emergQ=G=>70*Math.sqrt(G);
let ventChart=new Chart(document.getElementById('ventChart'),{
  data:{datasets:[
    {type:'line',label:'ASHRAE 15 emergency rate  Q = 70√G',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your plant room',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:20,max:3000,title:{display:true,text:'Largest single refrigerant charge (kg)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Emergency exhaust rate (L/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} L/s at ${fmt0(c.parsed.x)} kg`}}}}
});
function updVent(){
  const G=+sG.value,V=+sRv.value,v=+sDv.value;
  document.getElementById('vG').textContent=G+' kg';
  document.getElementById('vRv').textContent=V+' m³';
  document.getElementById('vDv').textContent=fmt1(v)+' m/s';
  const xs=[];for(let g=20;g<=3000;g+=20)xs.push(g);
  ventChart.data.datasets[0].data=xs.map(g=>({x:g,y:+emergQ(g).toFixed(0)}));
  ventChart.data.datasets[1].data=[{x:G,y:+emergQ(G).toFixed(0)}];
  ventChart.update('none');
  const Q=emergQ(G), Qm=Q/1000, area=Qm/v;
  document.getElementById('rQ').innerHTML=fmt0(Q)+' <small>L/s</small>';
  document.getElementById('rQm').innerHTML=fmt2(Qm)+' <small>m³/s</small>';
  document.getElementById('rAc').innerHTML=fmt1(Qm*3600/V)+' <small>ACH</small>';
  document.getElementById('rDa').innerHTML=fmt2(area)+' <small>m²</small>';
  document.getElementById('rDd').innerHTML=fmt0(1000*Math.sqrt(4*area/Math.PI))+' <small>mm</small>';
}
[sG,sRv,sDv].forEach(s=>s.addEventListener('input',updVent));updVent();

window.addEventListener('load',function(){try{flashChart.resize();rclChart.resize();ventChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='refrigerant-systems-tall-buildings', cat='hvac', mins=16,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Refrigerant Systems &amp; VRF in Megatall Buildings: Flash Gas, Oil Return &amp; the Concentration Limit',
    reg_title='Refrigerant Systems & VRF in Megatall Buildings: Flash Gas, Oil Return & the Concentration Limit',
    reg_tag='HVAC · Refrigerant · VRF · ASHRAE 15',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Refrigerant &middot; VRF &middot; ASHRAE 15 &middot; Megatall Buildings',
    desc='Refrigerant and VRF system design in megatall buildings: why a 100 m liquid lift costs 9.3 bar and 15 K of sub-cooling and sets the real height limit, why putting condensing plant above the evaporators removes the penalty, suction riser sizing for oil return at minimum load, the ASHRAE 15 refrigerant concentration limit set by the smallest served room and what the A2L transition does to it, and machinery room detection and emergency ventilation — with three interactive charts and installation tricks.',
    og_desc='A 100 m liquid lift costs 9.3 bar and about 15 K of sub-cooling you do not have — which is why VRF has height limits. Plus oil return at minimum load, and why A2L refrigerants cut the allowable charge by a factor of seven.',
    ld_desc='A design-perspective guide to refrigerant systems in megatall buildings: liquid line static head, flash gas and sub-cooling budgets, condensing plant orientation, suction riser sizing and oil return, ASHRAE 15 refrigerant concentration limits and the A2L transition, and machinery room detection and emergency ventilation.',
    img_alt='Technical cutaway of a megatall tower showing zoned refrigerant systems with condensing plant on mechanical floors above each zone, liquid and suction risers running down to the floors below, and a refrigerating machinery room with leak detection and emergency ventilation',
    en_tag='HVAC &amp; Cooling &middot; Refrigerant &middot; VRF &middot; ASHRAE 15',
    en_title='Refrigerant Systems &amp; VRF in Megatall Buildings: Flash Gas, Oil Return &amp; the Concentration Limit',
    en_excerpt='Refrigerant is the only fluid in the building that is a gas and a liquid at once, and that is what makes towers hard. A 100&nbsp;m liquid lift costs 9.3&nbsp;bar and about 15&nbsp;K of sub-cooling you do not have &mdash; the real reason VRF catalogues state height limits &mdash; unless you put the condensing plant above the evaporators and let the liquid fall. Suction risers sized for minimum load so the oil comes back, the ASHRAE&nbsp;15 concentration limit set by the smallest room the circuit serves, what the A2L transition does to allowable charge, and machinery room ventilation at 70&radic;G &mdash; with three interactive charts.',
    en_search='refrigerant VRF variable refrigerant flow DX direct expansion tall buildings megatall supertall high-rise flash gas sub-cooling liquid line static head vertical lift saturation slope height limit condensing unit above evaporator oil return suction riser velocity minimum load double riser oil trap pipe sizing do not oversize ASHRAE 15 ASHRAE 34 refrigerant concentration limit RCL smallest occupied space A1 A2L A3 safety group flammability LFL R410A R32 R134a R1234yf low GWP F-Gas machinery room leak detection emergency ventilation 70 root G purge control nitrogen purge brazing evacuation micron vacuum rise test weighed charge leak check register commissioning minimum load MEP building services HVAC',
    ar_title='أنظمة التبريد المباشر والـVRF في المباني فائقة الارتفاع: الغاز الوميضي وعودة الزيت وحد التركيز',
    ar_excerpt='وسيط التبريد هو المائع الوحيد في المبنى الذي يكون غازًا وسائلًا في آنٍ واحد، وهذا ما يجعل الأبراج صعبة. رفع السائل ١٠٠ متر يكلّف ٩٫٣ بار ونحو ١٥ درجة من التبريد الفائق التي لا تملكها — وهو السبب الحقيقي لحدود الارتفاع في كتالوجات الـVRF — إلا إذا وضعت وحدات التكثيف فوق وحدات التبخير وتركت السائل يهبط. تحجيم مواسير السحب على الحمل الأدنى لتعود الزيوت، وحد تركيز وسيط التبريد وفق ASHRAE 15 الذي تحدده أصغر غرفة تخدمها الدائرة، وأثر التحوّل إلى وسائط A2L على الشحنة المسموحة، وتهوية غرف المعدات — مع ثلاثة رسوم تفاعلية.',
    ar_search='refrigerant VRF DX flash gas sub-cooling liquid line static head oil return suction riser ASHRAE 15 ASHRAE 34 RCL A2L R410A R32 machinery room leak detection emergency ventilation nitrogen brazing evacuation وسيط التبريد التبريد المباشر التدفق المتغير لوسيط التبريد المباني الشاهقة المباني فائقة الارتفاع الغاز الوميضي التبريد الفائق خط السائل الضغط الاستاتيكي الرفع الرأسي ميل منحنى التشبع حد الارتفاع وحدة التكثيف فوق المبخر عودة الزيت ماسورة السحب سرعة الغاز الحمل الأدنى الماسورة المزدوجة مصيدة الزيت تحجيم المواسير عدم المبالغة في القطر حد تركيز وسيط التبريد أصغر حيز مأهول مجموعة الأمان القابلية للاشتعال الحد الأدنى للاشتعال إمكانية الاحترار العالمي المنخفضة غرفة معدات التبريد كشف التسرب التهوية الطارئة التحكم في التطهير اللحام تحت النيتروجين التفريغ اختبار الارتفاع الشحن بالوزن سجل فحص التسرب التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
