# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Ask where the mechanical floors go in a megatall tower and you will get three different answers from three consultants — and none of them will be the MEP engineer's. The structural engineer wants them where the outriggers are. The fire engineer wants them where the refuge floors are. The developer wants as few as possible, because a mechanical floor is a floor nobody pays rent for. The mechanical engineer, meanwhile, has the only quantitative case in the room, and usually arrives with it too late: <strong>the spacing of the mechanical floors is what sets the vertical zone height, and the vertical zone height is what every pressure-bearing system in the building has to live inside.</strong> Get the spacing decided in the structural coordination meeting and you will spend the next four years designing around it.</p>

<h2 id="why">1 · What a mechanical floor is actually for</h2>
<p>A mechanical floor is not storage for equipment. It is a <strong>pressure break, a distribution origin and a maintenance base</strong>, and each of those has a different optimal spacing:</p>
<ul class="clean">
  <li><strong>A pressure break.</strong> Every water-bearing system — chilled water, domestic water, fire standpipe, drainage — accumulates static pressure at 0.0981&nbsp;bar per metre. A mechanical floor is where that column is interrupted with a tank, a heat exchanger or a pump set, so the equipment below it never sees more than its rating.</li>
  <li><strong>A distribution origin.</strong> Air-handling plant on a mechanical floor serves the floors above and below it, so the vertical duct only has to span half a zone rather than the whole tower. That is what keeps the riser shafts from eating the floor plate.</li>
  <li><strong>A maintenance base.</strong> Plant that cannot be reached, rigged and replaced is plant that will be run to failure. Every mechanical floor needs a route from the goods lift to every machine, and a knock-out panel or hatch big enough for the largest replaceable component.</li>
  <li><strong>A compartmentation break.</strong> Terminating shafts at mechanical floors is the single most effective control on <a href="stack-effect-tall-buildings.html">stack effect</a>, and it is also where smoke zones and fire compartments naturally align.</li>
</ul>

<h2 id="economics">2 · The area economics — and why they mislead</h2>
<p>There is a real optimisation buried here, and it is worth doing because it is so often asserted without numbers. Adding mechanical floors costs whole floors of lettable area. But it <em>saves</em> shaft area on every other floor, because a riser that only serves one zone carries a fraction of the load. With \(F\) floors of area \(A\), \(N\) mechanical floors, and a riser cross-section of \(k\) per floor served, the total area lost is approximately:</p>
<div class="eq">\[ L(N) \;=\; \underbrace{N\,A}_{\text{mechanical floors}} \;+\; \underbrace{\frac{k\,F^{2}}{2N}}_{\text{shafts on every floor}} \qquad\Longrightarrow\qquad N^{*} = F\sqrt{\frac{k}{2A}} \]</div>
<p>Run it for a real tower — 150 floors of 1,000&nbsp;m², 0.35&nbsp;m² of riser per floor served — and the optimum is <strong>two</strong> mechanical floors, costing about 2.65&nbsp;% of gross floor area. Real megatall towers have five to ten. The economics are not wrong; they are simply not the binding constraint. <strong>Mechanical floors are sited by pressure, fire and structure, and the area calculation only tells you what that decision costs.</strong> Knowing the number is still valuable: it is the difference between "we need another mechanical floor" and "another mechanical floor costs 0.7&nbsp;% of your lettable area and here is what it buys."</p>

<h2 id="int-area">3 · Interactive: the area cost of mechanical floors</h2>
<p>Set the tower and the riser intensity. The red curve is area lost to mechanical floors, the blue is area lost to shafts on every floor, and the dark curve is the total — a shallow U whose minimum is the area-optimal count. Watch how flat the bottom is: between two and four mechanical floors the total barely moves, which is exactly why other disciplines get to win this argument.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Lettable area lost vs number of mechanical floors</div>
    <div class="fsub">L(N) = N·A + k·F²/(2N). Mechanical-floor loss rises linearly; shaft loss falls as 1/N because each riser serves fewer floors. k is the riser cross-section required per floor served, covering air, water, drainage and electrical risers together.</div>
  </div>
  <div class="chart-box"><canvas id="areaChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Floors <span id="vF">150</span></label>
      <input type="range" id="sF" min="20" max="200" value="150" step="5">
      <div class="hint">Occupied floors served by the risers.</div>
    </div>
    <div class="ctrl">
      <label>Floor plate <span id="vA">1000 m²</span></label>
      <input type="range" id="sA" min="400" max="3000" value="1000" step="50">
      <div class="hint">Gross area of one typical floor.</div>
    </div>
    <div class="ctrl">
      <label>Riser area per floor served <span id="vK">0.35 m²</span></label>
      <input type="range" id="sK" min="0.1" max="1.2" value="0.35" step="0.01">
      <div class="hint">All risers combined. Central all-air systems push this up hard; floor-by-floor air handling pushes it right down.</div>
    </div>
    <div class="ctrl">
      <label>Mechanical floors <span id="vN">4</span></label>
      <input type="range" id="sN" min="1" max="16" value="4" step="1">
      <div class="hint">Marker position on the curve.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Area-optimal N</div><div class="v" id="rNo">2</div></div>
    <div class="cell"><div class="k">Loss at your N</div><div class="v" id="rLn">4,984 <small>m²</small></div></div>
    <div class="cell"><div class="k">Of gross area</div><div class="v" id="rPc">3.32 <small>%</small></div></div>
    <div class="cell"><div class="k">Cost vs optimum</div><div class="v" id="rDf">1,016 <small>m²</small></div></div>
    <div class="cell"><div class="k">Zone height</div><div class="v" id="rZh">38 <small>floors</small></div></div>
  </div>
</div>
<p class="fig-note">At the default the area optimum is <strong>two</strong> mechanical floors (2.65&nbsp;% of gross area) but four costs only 3.32&nbsp;% — about 1,000&nbsp;m² more, or roughly one extra floor's worth, spread over a 150-storey building. That is a small price for halving every pressure zone, and it is the number to bring to the coordination meeting. Now drag the riser intensity: at 1.0&nbsp;m² per floor served, typical of a fully central all-air system, the optimum moves to three and the shaft term overtakes the mechanical-floor term — which is the quantitative argument for floor-by-floor air handling.</p>

<h2 id="int-duct">4 · Interactive: why central air distribution does not scale</h2>
<p>The riser intensity above is not a constant — it is a design choice, and air is what dominates it. This shows the vertical supply-and-return duct cross-section needed as one air-handling plant serves more and more floors, against the outdoor-air-only riser that a floor-by-floor or DOAS arrangement needs instead.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Vertical duct riser area vs floors served by one plant</div>
    <div class="fsub">Q = n·A·q. Riser area = 1.8·Q/v, the 1.8 counting supply plus a return duct at 80&nbsp;% of the supply area. The blue line is the same building served by floor-by-floor air handling, where only outdoor air rides the riser — taken as 10&nbsp;% of the supply volume at two-thirds the duct velocity, since outdoor-air risers are run slower for acoustic reasons.</div>
  </div>
  <div class="chart-box"><canvas id="ductChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Floors per plant <span id="vDn">40</span></label>
      <input type="range" id="sDn" min="5" max="140" value="40" step="1">
      <div class="hint">Floors served by one central air-handling plant.</div>
    </div>
    <div class="ctrl">
      <label>Floor plate <span id="vDa">1000 m²</span></label>
      <input type="range" id="sDa" min="400" max="3000" value="1000" step="50">
      <div class="hint">Conditioned area per floor.</div>
    </div>
    <div class="ctrl">
      <label>Supply air rate <span id="vDq">1.50 L/s·m²</span></label>
      <input type="range" id="sDq" min="0.6" max="3" value="1.5" step="0.05">
      <div class="hint">Design supply airflow per square metre. Higher in dense or glazed floors.</div>
    </div>
    <div class="ctrl">
      <label>Duct velocity <span id="vDv">12 m/s</span></label>
      <input type="range" id="sDv" min="6" max="20" value="12" step="0.5">
      <div class="hint">Riser velocity. Pushing it up shrinks the shaft and costs fan power and noise.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Air volume</div><div class="v" id="rQ">60 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Riser area</div><div class="v" id="rAr">9.0 <small>m²</small></div></div>
    <div class="cell"><div class="k">Square shaft</div><div class="v" id="rSq">3.0 <small>m</small></div></div>
    <div class="cell"><div class="k">Of floor plate</div><div class="v" id="rPf">0.90 <small>%</small></div></div>
    <div class="cell"><div class="k">DOAS riser</div><div class="v" id="rDo">1.3 <small>m²</small></div></div>
  </div>
</div>
<p class="fig-note">One plant serving 40 floors needs a <strong>9&nbsp;m² riser — a 3.0&nbsp;m square shaft</strong>, running the full height of the zone. Push it to 120 floors and it becomes 27&nbsp;m², a 5.2&nbsp;m square shaft, before you have added a single water or electrical riser. Serve those same 120 floors with floor-by-floor air handling and only outdoor air rides the riser: <strong>4.0&nbsp;m²</strong>, a 2.0&nbsp;m square shaft — a seventh of the area. That is the real reason tall office towers moved to floor-by-floor AHUs — not fan energy, not control, but the fact that the vertical duct was consuming the product being sold. The counter-argument is maintenance: you have swapped four large machines in a plant room for a hundred small ones in ceilings, which is a facilities cost that lasts as long as the building.</p>

<h2 id="governing">5 · The governing constraint: whose zone height wins?</h2>
<p>Every pressure-bearing system in the tower has a maximum zone height, and they are wildly different. This is the calculation that should be done first, in one table, before the mechanical floors are located — because <strong>the shortest one governs the whole building</strong>, and it is almost never the one people expect.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Maximum vertical zone height by system</div>
    <div class="fsub">Zone height = allowable pressure / 0.0981 bar·m⁻¹. Domestic water is shown two ways: zoned on the fixture comfort window alone, and zoned on riser pipe class with floor PRVs doing the fine control. The three pipe-class bars are the raw rating over the gradient; netting off the residual each system must still hold at the top of its zone shortens them by roughly 10&nbsp;% — the domestic riser, for example, falls from 163&nbsp;m to 148&nbsp;m once a 1.5&nbsp;bar top residual is allowed for.</div>
  </div>
  <div class="chart-box"><canvas id="govChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Domestic comfort window <span id="vGw">3.5 bar</span></label>
      <input type="range" id="sGw" min="1.5" max="6" value="3.5" step="0.1">
      <div class="hint">Maximum minus minimum acceptable fixture pressure.</div>
    </div>
    <div class="ctrl">
      <label>Domestic riser class <span id="vGd">PN16</span></label>
      <input type="range" id="sGd" min="10" max="40" value="16" step="1">
      <div class="hint">With floor PRVs, the riser can run at its pipe rating.</div>
    </div>
    <div class="ctrl">
      <label>Chilled-water class <span id="vGc">PN16</span></label>
      <input type="range" id="sGc" min="10" max="40" value="16" step="1">
      <div class="hint">Rating of zone coils, valves and fittings.</div>
    </div>
    <div class="ctrl">
      <label>Standpipe rating <span id="vGf">12 bar</span></label>
      <input type="range" id="sGf" min="8" max="34" value="12" step="1">
      <div class="hint">Hose-valve and standpipe working pressure.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Governing height</div><div class="v" id="rGz">36 <small>m</small></div></div>
    <div class="cell"><div class="k">Governed by</div><div class="v" id="rGb" style="font-size:14px;margin-top:8px;">domestic comfort</div></div>
    <div class="cell"><div class="k">If PRVs at floors</div><div class="v" id="rGp">122 <small>m</small></div></div>
    <div class="cell"><div class="k">Zones in 600 m</div><div class="v" id="rGn">17</div></div>
    <div class="cell"><div class="k">With PRVs</div><div class="v" id="rGm">5</div></div>
  </div>
</div>
<p class="fig-note">The bars are not close. Chilled water at PN16 tolerates 163&nbsp;m and a standard standpipe 122&nbsp;m, but domestic water zoned on tap comfort alone tolerates just <strong>36&nbsp;m</strong> — and if you let that govern, a 600&nbsp;m tower needs seventeen mechanical levels. Break that one constraint with floor PRVs (see <a href="domestic-water-tall-buildings.html">domestic water supply</a>) and the governing system becomes the fire standpipe at 122&nbsp;m, giving five zones. <strong>One decision about tapware and PRVs changes the number of mechanical floors in the building by a factor of three.</strong> That is why this table belongs in the concept report, not the tender drawings.</p>

<h2 id="layout">6 · Laying the floor out</h2>
<ul class="clean">
  <li><strong>Start from the replacement route, not the plant.</strong> Draw the path from the goods lift to every machine, at the size of the largest indivisible component, before you place anything. If a chiller cannot be replaced without demolition, the layout has failed regardless of how efficiently it packs.</li>
  <li><strong>Give every machine its pull space.</strong> Tube-pull for shell-and-tube chillers, coil-pull and filter-face access for AHUs, shaft-withdrawal for pumps. Mark it on the drawing as reserved space and defend it in coordination — it is the first thing another trade will route through.</li>
  <li><strong>Separate wet and dry.</strong> Keep electrical rooms, generators and control panels away from and ideally above pump rooms, tanks and heat exchangers. Then bund and drain the wet side properly, with a floor gully sized for the largest credible leak and a leak-detection alarm, because the floor below is somebody's ceiling.</li>
  <li><strong>Height is the scarce dimension.</strong> Mechanical floors are usually double-height, and the coordination fight is vertical: ducts want depth, pipes want gradient, cable containment wants clearance, and the structure is deeper here because outriggers often land on the same level. Resolve the vertical stack early in the model.</li>
  <li><strong>Put the riser take-offs where the shafts actually are.</strong> A mechanical floor that requires a 30&nbsp;m horizontal run to reach its own riser has wasted the pressure break it was built to provide.</li>
  <li><strong>Design for acoustic isolation from day one.</strong> A mechanical floor sits directly under and over occupied space; see <a href="stack-effect-tall-buildings.html">the compartmentation discussion</a> for the shaft side and treat structure-borne transmission as a floor-level design problem, not an equipment selection detail.</li>
</ul>

<h2 id="coincide">7 · Making the levels coincide</h2>
<p>The cheapest mechanical floor is one that was going to exist anyway. In a well-coordinated megatall these functions are deliberately stacked on the same levels:</p>
<ul class="clean">
  <li><strong>Structural outrigger or belt-truss levels</strong> — already partially obstructed and unattractive as lettable space, and already stiff enough to carry heavy plant.</li>
  <li><strong>Refuge floors</strong> — required by code at intervals, already protected and already a shaft-compartmentation break.</li>
  <li><strong>Fire and MEP pressure zone breaks</strong> — tanks, pumps and heat exchangers for every wet system.</li>
  <li><strong>Lift zone terminations and sky lobbies</strong> — where hoistways stop and the stack-effect column is already being interrupted.</li>
  <li><strong>Façade maintenance and BMU levels</strong> — plant, davits and access already concentrated.</li>
</ul>
<p>When these coincide the tower gets its pressure breaks essentially free. When they do not — when the outriggers are at levels 30 and 90 but the water zoning wants 40 and 80 — the building pays twice, and the argument usually gets settled by whoever is furthest along in their design. That is why the MEP zoning table has to exist before the structural scheme freezes.</p>

<h2 id="install">8 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Rig the plant in before the floor above is closed.</strong> Sequence the heavy equipment deliveries against the structural programme and, where that is impossible, cast a removable slab panel or design a permanent lifting beam and hatch. Retro-fitting a 12-tonne chiller through a completed core is a demolition job.</li>
  <li><strong>Install a permanent lifting beam over every major machine</strong>, rated and certified, with the SWL painted on it. It costs almost nothing during construction and it is used for the next sixty years.</li>
  <li><strong>Set out the plinths from the riser, not the wall.</strong> Cumulative setting-out error on a mechanical floor lands on the shortest connection, which is always the one to the riser.</li>
  <li><strong>Waterproof and drain the whole floor</strong>, not just the plant rooms — tank rooms, pump rooms and heat exchanger rooms all get tanked, bunded and drained to a gully with a high-level alarm.</li>
  <li><strong>Provide dedicated plant ventilation and cooling</strong> and check it against the real heat rejection of the equipment on the floor. A mechanical floor packed with drives, transformers and pump motors is a substantial internal load, and plant rooms that run at 45&nbsp;°C halve the life of the electronics in them.</li>
  <li><strong>Photograph and scan the floor before closing ceilings.</strong> A point-cloud of every mechanical floor at completion is the single most useful handover deliverable for a building that will be modified for decades.</li>
  <li><strong>Label to a plan.</strong> Every valve, damper and machine tagged to the BMS naming convention at installation, with a laminated schematic mounted on the wall of each plant room.</li>
</ul>

<h2 id="checklist">9 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Build the zone-height table first</strong> — every pressure system, its rating, its maximum zone height; the shortest governs.</li>
  <li><strong>Decide the domestic water strategy early</strong>, because it is usually the governing constraint and it is fixable with PRVs.</li>
  <li><strong>Quantify the area cost</strong> of each additional mechanical floor and bring the number to coordination.</li>
  <li><strong>Choose the air strategy on shaft area</strong>, not on fan energy — it dominates the riser intensity.</li>
  <li><strong>Force coincidence</strong> with outriggers, refuge floors, lift zone breaks and BMU levels.</li>
  <li><strong>Lay out from the replacement route</strong>, with pull space reserved and defended.</li>
  <li><strong>Separate wet from dry</strong>, bund and drain everything, alarm the gullies.</li>
  <li><strong>Plan the rigging</strong> against the construction programme, with permanent lifting beams and hatches.</li>
  <li><strong>Ventilate and cool the plant floor</strong> for its real internal gain.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Mechanical floors are the tower's <strong>pressure breaks</strong>, and their spacing is set by whichever system has the shortest allowable zone — almost always domestic water, at 36&nbsp;m, until you break that constraint with floor PRVs and hand the job to the fire standpipe at 122&nbsp;m. The area economics say two mechanical floors; the pressure, fire and structural reality says five to ten; the useful contribution from the mechanical engineer is not the optimum but <strong>the price of each one and what it buys</strong> — brought to the table before the structural scheme freezes, because after that the zone heights are somebody else's decision and you will be designing around them for four years.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — mechanical floor location and spacing, vertical zoning strategy, plant distribution.</li>
  <li>Council on Tall Buildings and Urban Habitat (CTBUH) — technical guides on tall building services, core planning and refuge floor provision.</li>
  <li>CIBSE <em>Guide D — Transportation Systems in Buildings</em> and <em>Guide B</em> — core planning, sky lobbies and the interaction of lift zoning with plant levels.</li>
  <li>ASHRAE <em>Handbook — HVAC Systems and Equipment</em>, Air Handling and Distribution chapters — riser sizing, duct velocity and central vs decentralised air-handling arrangements.</li>
  <li>International Building Code (IBC) and Saudi Building Code <em>SBC 801</em> — refuge floor and high-rise provisions that fix candidate mechanical levels.</li>
  <li>Hydraulic Institute and ASHRAE guidance on plant room layout, equipment access and maintenance clearances.</li>
  <li>BSRIA <em>Rules of Thumb</em> (BG 9) — riser and plant space allowances for early-stage area planning.</li>
  <li>Institution of Structural Engineers / CTBUH guidance on outrigger and belt-truss levels in tall buildings, and their coordination with services floors.</li>
</ol>

<div class="tags">#MechanicalFloors #PlantRooms #TallBuildings #MegatallBuildings #SupertallBuildings #VerticalZoning #PressureZoning #RiserDesign #ShaftDesign #CorePlanning #SkyLobby #RefugeFloor #Outrigger #FloorByFloorAHU #DOAS #DuctRiser #SpacePlanning #Maintainability #Rigging #Coordination #BIM #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const BARM=0.0981;

/* ---------- CHART 1 : area economics ---------- */
const sF=document.getElementById('sF'),sA=document.getElementById('sA'),
      sK=document.getElementById('sK'),sN=document.getElementById('sN');
const lossMech=(N,A)=>N*A, lossShaft=(N,F,k)=>k*F*F/(2*N);
let areaChart=new Chart(document.getElementById('areaChart'),{
  data:{datasets:[
    {type:'line',label:'Mechanical-floor area',data:[],borderColor:'#c0392b',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:4},
    {type:'line',label:'Shaft area on all floors',data:[],borderColor:'#1b4f72',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:3},
    {type:'line',label:'Total area lost',data:[],borderColor:'#1a1d21',backgroundColor:'rgba(26,29,33,0.07)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your choice',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1,max:16,title:{display:true,text:'Number of mechanical floors',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Lettable area lost (m²)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} m² at N=${c.parsed.x}`}}}}
});
function updArea(){
  const F=+sF.value,A=+sA.value,k=+sK.value,N=+sN.value;
  document.getElementById('vF').textContent=F;
  document.getElementById('vA').textContent=A+' m²';
  document.getElementById('vK').textContent=fmt2(k)+' m²';
  document.getElementById('vN').textContent=N;
  const xs=[];for(let n=1;n<=16;n++)xs.push(n);
  areaChart.data.datasets[0].data=xs.map(n=>({x:n,y:+lossMech(n,A).toFixed(0)}));
  areaChart.data.datasets[1].data=xs.map(n=>({x:n,y:+lossShaft(n,F,k).toFixed(0)}));
  areaChart.data.datasets[2].data=xs.map(n=>({x:n,y:+(lossMech(n,A)+lossShaft(n,F,k)).toFixed(0)}));
  const Ln=lossMech(N,A)+lossShaft(N,F,k);
  areaChart.data.datasets[3].data=[{x:N,y:+Ln.toFixed(0)}];
  areaChart.update('none');
  const Nopt=Math.max(1,Math.round(F*Math.sqrt(k/(2*A))));
  const Lopt=lossMech(Nopt,A)+lossShaft(Nopt,F,k);
  document.getElementById('rNo').textContent=Nopt;
  document.getElementById('rLn').innerHTML=fmt0(Ln)+' <small>m²</small>';
  document.getElementById('rPc').innerHTML=fmt2(100*Ln/(F*A))+' <small>%</small>';
  document.getElementById('rDf').innerHTML=fmt0(Math.abs(Ln-Lopt))+' <small>m²</small>';
  document.getElementById('rZh').innerHTML=fmt0(F/N)+' <small>floors</small>';
}
[sF,sA,sK,sN].forEach(s=>s.addEventListener('input',updArea));updArea();

/* ---------- CHART 2 : duct riser ---------- */
const sDn=document.getElementById('sDn'),sDa=document.getElementById('sDa'),
      sDq=document.getElementById('sDq'),sDv=document.getElementById('sDv');
const OA_FRAC=0.10, RF=1.8;
function duct(n,A,q,v){const Q=n*A*q/1000;return {Q:Q,ar:RF*Q/v};}
let ductChart=new Chart(document.getElementById('ductChart'),{
  data:{datasets:[
    {type:'line',label:'Central all-air riser (supply + return)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Floor-by-floor AHU — outdoor air only',data:[],borderColor:'#1b4f72',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'Your plant',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:140,title:{display:true,text:'Floors served by one plant',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Vertical duct riser area (m²)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} m² at ${fmt0(c.parsed.x)} floors`}}}}
});
function updDuct(){
  const n=+sDn.value,A=+sDa.value,q=+sDq.value,v=+sDv.value;
  document.getElementById('vDn').textContent=n;
  document.getElementById('vDa').textContent=A+' m²';
  document.getElementById('vDq').textContent=fmt2(q)+' L/s·m²';
  document.getElementById('vDv').textContent=fmt1(v)+' m/s';
  const xs=[];for(let i=5;i<=140;i+=1)xs.push(i);
  ductChart.data.datasets[0].data=xs.map(i=>({x:i,y:+duct(i,A,q,v).ar.toFixed(2)}));
  ductChart.data.datasets[1].data=xs.map(i=>({x:i,y:+(RF*i*A*q*OA_FRAC/1000/(v*0.667)).toFixed(2)}));
  const r=duct(n,A,q,v);
  ductChart.data.datasets[2].data=[{x:n,y:+r.ar.toFixed(2)}];
  ductChart.update('none');
  const oa=RF*n*A*q*OA_FRAC/1000/(v*0.667);
  document.getElementById('rQ').innerHTML=fmt0(r.Q)+' <small>m³/s</small>';
  document.getElementById('rAr').innerHTML=fmt1(r.ar)+' <small>m²</small>';
  document.getElementById('rSq').innerHTML=fmt1(Math.sqrt(r.ar))+' <small>m</small>';
  document.getElementById('rPf').innerHTML=fmt2(100*r.ar/A)+' <small>%</small>';
  document.getElementById('rDo').innerHTML=fmt1(oa)+' <small>m²</small>';
}
[sDn,sDa,sDq,sDv].forEach(s=>s.addEventListener('input',updDuct));updDuct();

/* ---------- CHART 3 : governing zone height ---------- */
const sGw=document.getElementById('sGw'),sGd=document.getElementById('sGd'),
      sGc=document.getElementById('sGc'),sGf=document.getElementById('sGf');
let govChart=new Chart(document.getElementById('govChart'),{
  type:'bar',
  data:{labels:['Domestic\ncomfort window','Domestic riser\n+ floor PRVs','Chilled water','Fire standpipe'],
    datasets:[{label:'Maximum zone height (m)',data:[],backgroundColor:[],borderColor:'#fff',borderWidth:1}]},
  options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',
    scales:{x:{type:'linear',min:0,title:{display:true,text:'Maximum vertical zone height (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{...AX,ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{display:false},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.x)} m`}}}}
});
function updGov(){
  const w=+sGw.value,d=+sGd.value,c=+sGc.value,f=+sGf.value;
  document.getElementById('vGw').textContent=fmt1(w)+' bar';
  document.getElementById('vGd').textContent='PN'+d;
  document.getElementById('vGc').textContent='PN'+c;
  document.getElementById('vGf').textContent=f+' bar';
  const vals=[w/BARM,d/BARM,c/BARM,f/BARM];
  const gov=Math.min(...vals), gi=vals.indexOf(gov);
  govChart.data.datasets[0].data=vals.map(v=>+v.toFixed(0));
  govChart.data.datasets[0].backgroundColor=vals.map((v,i)=>i===gi?'#c0392b':'#1b4f72');
  govChart.update('none');
  const names=['domestic comfort','domestic riser','chilled water','fire standpipe'];
  const withPrv=Math.min(d/BARM,c/BARM,f/BARM);
  document.getElementById('rGz').innerHTML=fmt0(gov)+' <small>m</small>';
  document.getElementById('rGb').textContent=names[gi];
  document.getElementById('rGp').innerHTML=fmt0(withPrv)+' <small>m</small>';
  document.getElementById('rGn').textContent=Math.ceil(600/gov);
  document.getElementById('rGm').textContent=Math.ceil(600/withPrv);
}
[sGw,sGd,sGc,sGf].forEach(s=>s.addEventListener('input',updGov));updGov();

window.addEventListener('load',function(){try{areaChart.resize();ductChart.resize();govChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='mechanical-floors-tall-buildings', cat='tallmep', mins=17,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Mechanical Floors in Megatall Buildings: Spacing, Zone Heights, Riser Economics &amp; Layout',
    reg_title='Mechanical Floors in Megatall Buildings: Spacing, Zone Heights, Riser Economics & Layout',
    reg_tag='Tall-Building Systems · Mechanical Floors',
    breadcrumb='Tall-Building Systems',
    tag_line='Tall-Building Systems &middot; Mechanical Floors &middot; Vertical Zoning &middot; Core Planning',
    desc='Mechanical floor design in megatall buildings: what a plant level is really for, the area economics of mechanical floors versus riser shafts, why central all-air distribution does not scale, the zone-height table that decides the whole building and why domestic water usually governs it, making levels coincide with outriggers and refuge floors, layout for maintainability and rigging — with three interactive charts and installation tricks.',
    og_desc='The spacing of the mechanical floors sets the vertical zone height, and the zone height governs every pressure system in the tower. The area economics, why central air does not scale, and the one table that should exist before the structural scheme freezes.',
    ld_desc='A design-perspective guide to mechanical floors in megatall buildings: their role as pressure breaks and distribution origins, the area trade-off against riser shafts, duct riser scaling and floor-by-floor air handling, the governing zone-height calculation across systems, coincidence with structural and refuge levels, and layout for maintenance and rigging.',
    img_alt='Cutaway of a megatall tower highlighting its double-height mechanical floors at intervals up the core, each packed with air-handling plant, pumps, tanks and heat exchangers, with the riser shafts running between them',
    en_tag='Tall-Building Systems &middot; Mechanical Floors &middot; Vertical Zoning &middot; Core Planning',
    en_title='Mechanical Floors in Megatall Buildings: Spacing, Zone Heights, Riser Economics &amp; Layout',
    en_excerpt='Three consultants will tell you where the mechanical floors go, and none of them is the MEP engineer &mdash; yet their spacing sets the vertical zone height that every pressure system in the tower must live inside. The area economics of plant floors versus riser shafts, why central all-air distribution stops scaling around 40 floors, the zone-height table that decides the building (domestic water governs at 36&nbsp;m until you fix it with PRVs), making levels coincide with outriggers and refuge floors, and layout for rigging and maintenance &mdash; with three interactive charts.',
    en_search='mechanical floors plant rooms tall buildings megatall supertall high-rise vertical zoning pressure break zone height core planning riser shaft area economics lettable area gross floor area duct riser sizing central all-air floor by floor AHU DOAS outdoor air riser velocity governing constraint domestic water comfort window PRV chilled water pressure class PN16 fire standpipe rating refuge floor outrigger belt truss sky lobby lift zoning plant layout maintenance access pull space tube pull rigging lifting beam knock out panel bunding drainage leak detection plant ventilation acoustic isolation BSRIA rules of thumb coordination BIM MEP building services',
    ar_title='الطوابق الميكانيكية في المباني فائقة الارتفاع: التباعد وارتفاعات المناطق واقتصاديات المناور والتخطيط',
    ar_excerpt='ثلاثة استشاريين سيحددون مواقع الطوابق الميكانيكية، وليس بينهم مهندس الأنظمة — رغم أن تباعدها هو ما يحدد ارتفاع المنطقة الرأسية الذي يجب أن يعمل داخله كل نظام ضغط في البرج. اقتصاديات المساحة بين طوابق المعدات والمناور الرأسية، ولماذا يتوقف التوزيع الهوائي المركزي عن الجدوى عند نحو أربعين طابقًا، وجدول ارتفاعات المناطق الذي يحكم المبنى (مياه الاستخدام تحكمه عند ٣٦ مترًا حتى تُعالج بصمامات تخفيض الضغط)، ومواءمة المناسيب مع الجوائز الهيكلية وطوابق الملجأ، والتخطيط للرفع والصيانة — مع ثلاثة رسوم تفاعلية.',
    ar_search='mechanical floors plant rooms tall buildings megatall vertical zoning pressure break zone height core planning riser shaft duct sizing DOAS floor by floor AHU refuge floor outrigger sky lobby maintenance rigging BSRIA الطوابق الميكانيكية غرف المعدات المباني الشاهقة المباني فائقة الارتفاع التقسيم الرأسي فاصل الضغط ارتفاع المنطقة تخطيط النواة المنور الرأسي مساحة المناور المساحة القابلة للتأجير إجمالي المساحة تحجيم المجاري الهوائية النظام الهوائي المركزي وحدات المناولة بكل طابق هواء خارجي مخصص سرعة الهواء القيد الحاكم نافذة الضغط للأدوات الصحية صمام تخفيض الضغط درجة تحمل المياه المبردة تصنيف عمود الحريق طابق الملجأ الجائز الهيكلي بهو السماء تقسيم المصاعد تخطيط غرف المعدات مسافات الصيانة مسار سحب الأنابيب الرفع والتركيب عارضة الرفع فتحة الإدخال الحواجز المانعة للتسرب الصرف كشف التسرب تهوية غرف المعدات العزل الصوتي التنسيق MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
