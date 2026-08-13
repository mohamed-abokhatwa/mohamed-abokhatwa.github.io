# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A megatall tower is not a static object. It gets shorter as the concrete creeps and dries, by hundreds of millimetres over its life. Its core and its perimeter shorten by <em>different</em> amounts, so the two ends of every horizontal pipe drift apart. It leans and returns in the wind, twice a minute. And the services inside it expand and contract with their own contents — a plastic riser through 30&nbsp;K over 600&nbsp;m moves <strong>2.7 metres</strong>. None of this appears on a hydraulic calculation, none of it is in the pipe schedule, and all of it is capable of tearing a riser apart. Building movement is the quiet structural problem hidden inside every MEP package in a tall building.</p>

<h2 id="four">1 · Four movements, four different timescales</h2>
<ul class="clean">
  <li><strong>Thermal, in the service itself</strong> — minutes to hours. A chilled-water riser fills at ambient and runs at 6&nbsp;°C; a hot water riser runs at 60&nbsp;°C. The pipe changes length every time the system starts.</li>
  <li><strong>Elastic shortening of the structure</strong> — immediate, as each floor's load is applied. Largely complete before the services are installed, but not entirely.</li>
  <li><strong>Creep and shrinkage</strong> — months to decades. Concrete under sustained load keeps deforming, and it dries and shrinks. Together these dominate, and roughly <strong>a third to a half of the total happens after the pipework is fixed</strong>.</li>
  <li><strong>Wind sway and differential temperature</strong> — seconds to hours, and reversible. The tower leans, and the sunlit face grows relative to the shaded one, twisting the frame slightly.</li>
</ul>
<p>The first is the pipe moving inside a stationary building. The rest are the <em>building</em> moving around a pipe that would rather stay where it is. Both have to be designed for, and they are additive.</p>

<h2 id="int-thermal">2 · Interactive: thermal movement in the riser</h2>
<p>The classic \( \Delta L = \alpha L \Delta T\) — but in a tower \(L\) is enormous, and the coefficient depends brutally on the material you chose for reasons that had nothing to do with movement.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Thermal movement of a vertical riser</div>
    <div class="fsub">ΔL = α·L·ΔT. ΔT is measured from the installation temperature to the operating extreme — not from the design ambient. Plastics move an order of magnitude more than steel.</div>
  </div>
  <div class="chart-box"><canvas id="thermChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Riser length <span id="vL">300 m</span></label>
      <input type="range" id="sL" min="20" max="800" value="300" step="10">
      <div class="hint">Length between anchors, not the building height — anchoring is the design variable.</div>
    </div>
    <div class="ctrl">
      <label>Temperature swing <span id="vT">30 K</span></label>
      <input type="range" id="sT" min="5" max="80" value="30" step="1">
      <div class="hint">Install temperature to operating extreme. A chilled riser installed at 45 °C and run at 6 °C swings 39 K.</div>
    </div>
    <div class="ctrl">
      <label>Coefficient α <span id="vA">12.0 ×10⁻⁶</span></label>
      <input type="range" id="sA" min="10" max="160" value="12" step="1">
      <div class="hint">Steel 12, stainless 16, copper 17, PVC-U 70, PPR / PE-X ≈ 150 ×10⁻⁶ /K.</div>
    </div>
    <div class="ctrl">
      <label>Anchor spacing <span id="vS">60 m</span></label>
      <input type="range" id="sS" min="5" max="200" value="60" step="5">
      <div class="hint">Distance between fixed anchors. This is what you actually control.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Total movement</div><div class="v" id="rDl">108 <small>mm</small></div></div>
    <div class="cell"><div class="k">Per anchor bay</div><div class="v" id="rDb">21.6 <small>mm</small></div></div>
    <div class="cell"><div class="k">Anchor bays</div><div class="v" id="rNb">5</div></div>
    <div class="cell"><div class="k">Loop leg needed</div><div class="v" id="rLp">5.3 <small>m</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">A 300&nbsp;m steel riser through 30&nbsp;K moves <strong>108&nbsp;mm</strong> overall — manageable if you break it into anchor bays so each one only has to absorb about 22&nbsp;mm. Now drag the coefficient to 150 for PPR or PE-X: the same riser moves <strong>1.35&nbsp;metres</strong>, and over 600&nbsp;m it is 2.7&nbsp;m. Plastic pipe is chosen for corrosion resistance, weight and cost, and in a tall riser it brings a movement problem an order of magnitude larger than the steel it replaced. That is not an argument against it — it is an argument for designing the anchors, guides and compensators <em>as part of choosing the material</em>, rather than discovering the consequence on site.</p>

<h2 id="shortening">3 · Column shortening — the movement nobody tells you about</h2>
<p>Concrete under sustained compression keeps deforming for years, and it shrinks as it dries. The total vertical strain is the sum of three parts:</p>
<div class="eq">\[ \varepsilon_{total} \;=\; \underbrace{\frac{\sigma}{E}}_{\text{elastic}} \;+\; \underbrace{\phi\,\frac{\sigma}{E}}_{\text{creep}} \;+\; \underbrace{\varepsilon_{sh}}_{\text{shrinkage}} \]</div>
<p>with \(\phi\) the creep coefficient, typically 1.5–2.5. For a column at 10&nbsp;MPa in 35&nbsp;GPa concrete with 300&nbsp;µε of shrinkage, the total is around 1,150&nbsp;µε — and over 600&nbsp;m of building that is roughly <strong>690&nbsp;mm of vertical shortening</strong>. Structural engineers know this and compensate for most of it during construction by casting floors slightly high. What matters to the MEP engineer is the <strong>residual</strong>: the portion that occurs <em>after</em> the risers are installed and anchored, which is commonly a third to a half of the total — <strong>200 to 350&nbsp;mm on a 600&nbsp;m tower.</strong></p>

<div class="callout warn">
  <span class="lbl">The one that actually breaks things: differential shortening</span>
  The core and the perimeter columns carry different stresses, have different volume-to-surface ratios and dry at different rates, so they do <strong>not shorten by the same amount</strong>. A differential of 50–100&nbsp;mm between core and perimeter over the height of a megatall tower is normal. Every horizontal pipe, duct and cable tray that spans from the core to the façade is therefore being slowly sheared. A rigidly connected branch at the perimeter will either pull its joint apart or tear its support out of the slab, and it will do it silently over five years — long after the defects period, and it will be diagnosed as poor workmanship.
</div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Structural shortening and the part that acts on your pipework</div>
    <div class="fsub">ε = σ/E·(1+φ) + ε&#115;&#104;. The dark band is total shortening; the blue is the post-installation residual that the services actually have to absorb.</div>
  </div>
  <div class="chart-box"><canvas id="shortChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Building height <span id="vH">600 m</span></label>
      <input type="range" id="sH" min="100" max="1000" value="600" step="10">
      <div class="hint">Height over which the shortening accumulates.</div>
    </div>
    <div class="ctrl">
      <label>Sustained stress <span id="vSt">10 MPa</span></label>
      <input type="range" id="sSt" min="4" max="20" value="10" step="0.5">
      <div class="hint">Working compressive stress in the column or core wall.</div>
    </div>
    <div class="ctrl">
      <label>Creep coefficient φ <span id="vPh">2.0</span></label>
      <input type="range" id="sPh" min="1" max="3.5" value="2" step="0.1">
      <div class="hint">Higher for younger concrete at loading and for thinner sections.</div>
    </div>
    <div class="ctrl">
      <label>Post-installation share <span id="vPo">40 %</span></label>
      <input type="range" id="sPo" min="15" max="70" value="40" step="1">
      <div class="hint">Fraction of the total occurring after the risers are anchored.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Total strain</div><div class="v" id="rEp">1,157 <small>µε</small></div></div>
    <div class="cell"><div class="k">Total shortening</div><div class="v" id="rTs">694 <small>mm</small></div></div>
    <div class="cell"><div class="k">Acts on services</div><div class="v" id="rPs">278 <small>mm</small></div></div>
    <div class="cell"><div class="k">Per 40 m zone</div><div class="v" id="rPz">18.5 <small>mm</small></div></div>
    <div class="cell"><div class="k">vs thermal</div><div class="v" id="rVt">1.3<small>×</small></div></div>
  </div>
</div>
<p class="fig-note">On a 600&nbsp;m tower the structure shortens by about <strong>694&nbsp;mm</strong> in total, of which roughly <strong>278&nbsp;mm</strong> arrives after the services are fixed — about <strong>1.3 times</strong> the thermal movement of a 600&nbsp;m steel riser through 30&nbsp;K (216&nbsp;mm), and in the same direction for a chilled-water system. The two are additive and they must be summed before the compensators are sized. Note the readout per zone: even broken into 40&nbsp;m bays the structure still delivers 18&nbsp;mm of shortening into each one, on top of the thermal swing, which is why "we have expansion joints" is not the same as "we have allowed for movement".</p>

<h2 id="anchors">4 · Anchors, guides and compensators</h2>
<p>The design method is always the same three moves, in order:</p>
<ul class="clean">
  <li><strong>Decide where the pipe is <em>not</em> allowed to move</strong> — the anchors. An anchor is a structural connection carrying real force, and it must be designed and issued to the structural engineer with a load, not drawn as a bracket.</li>
  <li><strong>Force the movement into one direction</strong> — the guides. Between anchors, guides let the pipe slide axially and prevent it buckling sideways. Guide spacing comes from the buckling calculation, and the first guides either side of a compensator are much closer than the rest.</li>
  <li><strong>Give the movement somewhere to go</strong> — expansion loops, offsets, or bellows/axial compensators.</li>
</ul>
<p>Loops are preferred where space allows because they cannot fail suddenly, need no maintenance and impose only guiding forces. A guided-cantilever loop leg is roughly \( L=\sqrt{3ED\Delta/S_a}\), which for a 219&nbsp;mm riser absorbing 100&nbsp;mm needs an <strong>11.5&nbsp;m</strong> leg — usually impossible in a shaft, which is why tall risers use bellows.</p>

<div class="callout key">
  <span class="lbl">The number that surprises people: pressure thrust</span>
  A bellows does not resist pressure the way a pipe does; the pressure acting on its effective area pushes the anchors apart. For a 219&nbsp;mm bellows at 16&nbsp;bar that is about <strong>95&nbsp;kN of pressure thrust</strong>, plus the spring force of compressing it — around <strong>110&nbsp;kN total, eleven tonnes</strong>, applied to a bracket bolted to a shaft wall. Anchors either side of an unrestrained bellows are among the most heavily loaded fixings in the entire MEP installation, and they are routinely detailed as though they carried only pipe weight. Use tied or pressure-balanced bellows where the anchor cannot take the thrust, and always issue the anchor loads to the structural engineer.
</div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Expansion loop size and bellows anchor load</div>
    <div class="fsub">Loop leg L = √(3EDΔ/S&#97;) for a guided cantilever. Anchor force = pressure thrust (P·A&#101;&#102;&#102;) + bellows spring rate × movement.</div>
  </div>
  <div class="chart-box"><canvas id="anchChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Pipe outside diameter <span id="vD">219 mm</span></label>
      <input type="range" id="sD" min="50" max="600" value="219" step="5">
      <div class="hint">Riser OD. Bigger pipe needs a bigger loop and produces more thrust.</div>
    </div>
    <div class="ctrl">
      <label>Movement to absorb <span id="vM">100 mm</span></label>
      <input type="range" id="sM" min="10" max="300" value="100" step="5">
      <div class="hint">Thermal plus post-installation structural, summed.</div>
    </div>
    <div class="ctrl">
      <label>Operating pressure <span id="vP">16 bar</span></label>
      <input type="range" id="sP" min="4" max="40" value="16" step="1">
      <div class="hint">Static plus pump pressure at that point in the riser.</div>
    </div>
    <div class="ctrl">
      <label>Bellows spring rate <span id="vK">150 N/mm</span></label>
      <input type="range" id="sK" min="30" max="600" value="150" step="10">
      <div class="hint">From the bellows data sheet. Stiffer bellows load the anchor harder.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Loop leg</div><div class="v" id="rLl">11.5 <small>m</small></div></div>
    <div class="cell"><div class="k">Pressure thrust</div><div class="v" id="rPt">95 <small>kN</small></div></div>
    <div class="cell"><div class="k">Spring force</div><div class="v" id="rSf">15 <small>kN</small></div></div>
    <div class="cell"><div class="k">Anchor load</div><div class="v" id="rAl">110 <small>kN</small></div></div>
    <div class="cell"><div class="k">In tonnes</div><div class="v" id="rTn">11.2 <small>t</small></div></div>
  </div>
</div>
<p class="fig-note">A DN200 riser absorbing 100&nbsp;mm needs an <strong>11.5&nbsp;m loop leg</strong> — which does not exist in a services shaft — so it gets a bellows, and the bellows loads its anchors with <strong>110&nbsp;kN</strong>. That is over eleven tonnes on a fixing detail that is often drawn as a channel bracket. Two design responses: use <strong>tied or pressure-balanced bellows</strong> so the thrust is carried within the assembly rather than by the building, or place the anchor at a structural element that can genuinely take it and get the load formally accepted. Either way, the number has to be calculated and issued — this is the single most under-transmitted load in MEP design.</p>

<h2 id="detailing">5 · Detailing that accommodates movement</h2>
<ul class="clean">
  <li><strong>Branches from a moving riser must be flexible.</strong> Take branches off with a swing arm or an offset long enough to flex, never with a short rigid tee straight into a fixed branch. A 20&nbsp;mm riser movement against a rigid branch is a fatigue crack at the weld.</li>
  <li><strong>Slab penetrations need clearance and a movement-tolerant seal.</strong> A pipe grouted solid into a slab is an unintended anchor, and it will win against the bracket you designed. Sleeve every penetration, and choose a fire-stop that is rated <em>with</em> movement.</li>
  <li><strong>Horizontal runs from core to perimeter need articulation.</strong> This is the differential-shortening path: provide flexibility, expansion joints, or slotted supports at the perimeter end, and never fix both ends rigidly.</li>
  <li><strong>Coordinate with building movement joints.</strong> Where the structure has a movement joint, every service crossing it gets a designed flexible crossing — this is elementary and it is still missed on podium-to-tower interfaces, where the movement is largest.</li>
  <li><strong>Consider seismic and wind restraint together with expansion.</strong> These pull in opposite directions: restraint wants stiffness, expansion wants freedom. The answer is directional — restrain laterally, free axially — and a snubber that is set hard against the pipe defeats both.</li>
  <li><strong>Insulation and cladding must move too.</strong> Rigid insulation carried through a guide, or metal cladding fixed across an expansion device, transfers force and tears. Detail the insulation at every compensator explicitly.</li>
</ul>

<h2 id="install">6 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Record the installation temperature</strong> and cold-pull or pre-set every compensator to suit it. A bellows installed at neutral on a 45&nbsp;°C day and then run at 6&nbsp;°C spends its whole life at one end of its travel, halving its usable range and its fatigue life.</li>
  <li><strong>Install anchors before the pipe is filled</strong> and verify each against the design load; an anchor added later, after the riser has already found its position, does not do what the calculation assumed.</li>
  <li><strong>Check guides are actually free.</strong> Guides seized by over-tightening, by insulation packed into them or by debris are the commonest cause of a riser buckling. Inspect and record.</li>
  <li><strong>Leave the travel indicators visible.</strong> Bellows and spring supports come with position indicators — do not bury them behind cladding, and photograph their as-installed positions.</li>
  <li><strong>Survey the riser at intervals.</strong> Take datum readings at a few levels at handover and re-survey after twelve and thirty-six months; structural shortening is slow and a trend caught early is a cheap adjustment.</li>
  <li><strong>Do not weld a temporary restraint and leave it.</strong> Temporary construction restraints on risers must be removed and their removal signed off — a forgotten one is an unintended anchor at full stiffness.</li>
  <li><strong>Give the facilities team the movement drawing.</strong> Anchor and guide positions, expected travel and inspection intervals belong in the O&amp;M; without it, a future alteration will cut the riser at an anchor.</li>
</ul>

<h2 id="checklist">7 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Sum all four movements</strong> — thermal, elastic, creep-and-shrinkage residual, and sway — before sizing anything.</li>
  <li><strong>Get the post-installation shortening figure from the structural engineer</strong>, including the core-to-perimeter differential. Ask for it explicitly; it will not be offered.</li>
  <li><strong>Choose pipe material with its expansion coefficient in view</strong>, especially for plastics in tall risers.</li>
  <li><strong>Set anchors first, then guides, then compensators</strong> — in that order.</li>
  <li><strong>Calculate and issue every anchor load</strong>, including bellows pressure thrust, to the structural engineer.</li>
  <li><strong>Use tied or pressure-balanced bellows</strong> where thrust cannot be carried by the structure.</li>
  <li><strong>Articulate every core-to-perimeter run</strong> and every movement-joint crossing.</li>
  <li><strong>Sleeve penetrations</strong> with movement-rated fire-stopping; never grout a pipe solid.</li>
  <li><strong>Pre-set compensators to the recorded install temperature</strong> and verify guides are free.</li>
  <li><strong>Survey at handover and re-survey</strong> at twelve and thirty-six months.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A megatall tower shortens by roughly <strong>700&nbsp;mm</strong> over its life and about <strong>280&nbsp;mm of that lands on services already installed</strong> — comparable to the thermal movement of the same steel riser, and additive to it. Meanwhile the core and perimeter shorten by different amounts, quietly shearing every horizontal run between them. Ask the structural engineer for the post-installation and differential figures, choose pipe materials knowing that plastics move ten times as far as steel, set anchors before compensators, and above all <strong>calculate the bellows pressure thrust and issue it</strong> — because a hundred kilonewtons on a bracket detailed for pipe weight is how risers come down.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASME B31.1 <em>Power Piping</em> and B31.3 <em>Process Piping</em> — flexibility analysis, expansion stress ranges, anchor and guide design, and the guided-cantilever method.</li>
  <li>EJMA <em>Standards of the Expansion Joint Manufacturers Association</em> — bellows selection, pressure thrust, spring rates, tied and pressure-balanced arrangements.</li>
  <li>fib Model Code / EN 1992-1-1 (Eurocode 2) and ACI 209 — creep and shrinkage prediction models for concrete, and long-term deformation.</li>
  <li>CTBUH and Institution of Structural Engineers guidance on <em>column shortening in tall buildings</em>, differential shortening and construction compensation.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — riser support, movement accommodation and structural interface.</li>
  <li>CIBSE <em>Guide B</em> and BSRIA guidance on pipework support, anchors, guides and thermal movement in building services.</li>
  <li>SMACNA <em>Seismic Restraint Manual</em> — restraint arrangements compatible with thermal movement and directional freedom.</li>
  <li>Manufacturer technical data for PP-R, PE-X and PVC-U systems — expansion coefficients, support spacing and compensation detailing for plastics.</li>
</ol>

<div class="tags">#BuildingMovement #ThermalExpansion #ColumnShortening #Creep #Shrinkage #DifferentialShortening #TallBuildings #MegatallBuildings #Risers #PipeSupport #Anchors #Guides #ExpansionLoop #Bellows #ExpansionJoint #PressureThrust #EJMA #ASMEB311 #FlexibilityAnalysis #MovementJoint #SeismicRestraint #FireStopping #PPR #PEX #Commissioning #StructuralInterface #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};

/* ---------- CHART 1 : thermal movement ---------- */
const sL=document.getElementById('sL'),sT=document.getElementById('sT'),
      sA=document.getElementById('sA'),sS=document.getElementById('sS');
const dL=(a,L,dT)=>a*1e-6*L*dT*1000;   // mm
const loopLeg=(D,d)=>Math.sqrt(3*200000*D*d/100)/1000;  // m
let thermChart=new Chart(document.getElementById('thermChart'),{
  data:{datasets:[
    {type:'line',label:'Your material',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:4},
    {type:'line',label:'Carbon steel (α = 12)',data:[],borderColor:'#1b4f72',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:3},
    {type:'line',label:'PPR / PE-X (α = 150)',data:[],borderColor:'#1e8449',borderWidth:2.2,borderDash:[2,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your riser',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:20,max:800,title:{display:true,text:'Riser length (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'logarithmic',title:{display:true,text:'Thermal movement (mm, log scale)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} mm at ${fmt0(c.parsed.x)} m`}}}}
});
function updTherm(){
  const L=+sL.value,dT=+sT.value,a=+sA.value,sp=+sS.value;
  document.getElementById('vL').textContent=L+' m';
  document.getElementById('vT').textContent=dT+' K';
  document.getElementById('vA').textContent=fmt1(a)+' ×10⁻⁶';
  document.getElementById('vS').textContent=sp+' m';
  const xs=[];for(let x=20;x<=800;x+=10)xs.push(x);
  thermChart.data.datasets[0].data=xs.map(x=>({x:x,y:+dL(a,x,dT).toFixed(2)}));
  thermChart.data.datasets[1].data=xs.map(x=>({x:x,y:+dL(12,x,dT).toFixed(2)}));
  thermChart.data.datasets[2].data=xs.map(x=>({x:x,y:+dL(150,x,dT).toFixed(2)}));
  const tot=dL(a,L,dT), bay=dL(a,Math.min(sp,L),dT), n=Math.max(1,Math.ceil(L/sp));
  thermChart.data.datasets[3].data=[{x:L,y:+tot.toFixed(2)}];
  thermChart.update('none');
  document.getElementById('rDl').innerHTML=fmt0(tot)+' <small>mm</small>';
  document.getElementById('rDb').innerHTML=fmt1(bay)+' <small>mm</small>';
  document.getElementById('rNb').textContent=n;
  document.getElementById('rLp').innerHTML=fmt1(loopLeg(219,bay))+' <small>m</small>';
  const v=document.getElementById('rVd');
  if(bay<15)      v.innerHTML='<span class="badge good">absorbable in a loop</span>';
  else if(bay<50) v.innerHTML='<span class="badge warn">bellows likely needed</span>';
  else            v.innerHTML='<span class="badge bad">reduce anchor spacing</span>';
}
[sL,sT,sA,sS].forEach(s=>s.addEventListener('input',updTherm));updTherm();

/* ---------- CHART 2 : column shortening ---------- */
const sH=document.getElementById('sH'),sSt=document.getElementById('sSt'),
      sPh=document.getElementById('sPh'),sPo=document.getElementById('sPo');
const E_C=35000, SHRINK=300;
const strain=(st,ph)=>st/E_C*1e6*(1+ph)+SHRINK;
let shortChart=new Chart(document.getElementById('shortChart'),{
  data:{datasets:[
    {type:'line',label:'Total structural shortening',data:[],borderColor:'#1a1d21',backgroundColor:'rgba(26,29,33,0.07)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Acting on installed services',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.14)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your tower',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:100,max:1000,title:{display:true,text:'Building height (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Vertical shortening (mm)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} mm at ${fmt0(c.parsed.x)} m`}}}}
});
function updShort(){
  const H=+sH.value,st=+sSt.value,ph=+sPh.value,po=+sPo.value/100;
  document.getElementById('vH').textContent=H+' m';
  document.getElementById('vSt').textContent=fmt1(st)+' MPa';
  document.getElementById('vPh').textContent=fmt1(ph);
  document.getElementById('vPo').textContent=fmt0(po*100)+' %';
  const eps=strain(st,ph);
  const xs=[];for(let x=100;x<=1000;x+=10)xs.push(x);
  shortChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(eps*1e-6*x*1000).toFixed(1)}));
  shortChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(po*eps*1e-6*x*1000).toFixed(1)}));
  const tot=eps*1e-6*H*1000, act=po*tot;
  shortChart.data.datasets[2].data=[{x:H,y:+tot.toFixed(1)}];
  shortChart.update('none');
  const therm=12e-6*H*30*1000;
  document.getElementById('rEp').innerHTML=fmt0(eps)+' <small>µε</small>';
  document.getElementById('rTs').innerHTML=fmt0(tot)+' <small>mm</small>';
  document.getElementById('rPs').innerHTML=fmt0(act)+' <small>mm</small>';
  document.getElementById('rPz').innerHTML=fmt1(act*40/H)+' <small>mm</small>';
  document.getElementById('rVt').innerHTML=fmt1(act/therm)+'<small>×</small>';
}
[sH,sSt,sPh,sPo].forEach(s=>s.addEventListener('input',updShort));updShort();

/* ---------- CHART 3 : anchors & loops ---------- */
const sD=document.getElementById('sD'),sM=document.getElementById('sM'),
      sP=document.getElementById('sP'),sK=document.getElementById('sK');
const effArea=D=>Math.PI*Math.pow((D*1.25)/1000,2)/4;   // bellows effective area ~ 1.25x pipe OD
let anchChart=new Chart(document.getElementById('anchChart'),{
  data:{datasets:[
    {type:'line',label:'Anchor load (kN)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Expansion loop leg (m)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your riser',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:50,max:600,title:{display:true,text:'Pipe outside diameter (mm)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Anchor load (kN)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Loop leg (m)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updAnch(){
  const D=+sD.value,m=+sM.value,P=+sP.value,k=+sK.value;
  document.getElementById('vD').textContent=D+' mm';
  document.getElementById('vM').textContent=m+' mm';
  document.getElementById('vP').textContent=P+' bar';
  document.getElementById('vK').textContent=k+' N/mm';
  const thrust=d=>effArea(d)*P*1e5/1000;   // kN
  const xs=[];for(let x=50;x<=600;x+=10)xs.push(x);
  anchChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(thrust(x)+k*m/1000).toFixed(1)}));
  anchChart.data.datasets[1].data=xs.map(x=>({x:x,y:+loopLeg(x,m).toFixed(2)}));
  const T=thrust(D), S=k*m/1000;
  anchChart.data.datasets[2].data=[{x:D,y:+(T+S).toFixed(1)}];
  anchChart.update('none');
  document.getElementById('rLl').innerHTML=fmt1(loopLeg(D,m))+' <small>m</small>';
  document.getElementById('rPt').innerHTML=fmt0(T)+' <small>kN</small>';
  document.getElementById('rSf').innerHTML=fmt0(S)+' <small>kN</small>';
  document.getElementById('rAl').innerHTML=fmt0(T+S)+' <small>kN</small>';
  document.getElementById('rTn').innerHTML=fmt1((T+S)/9.81)+' <small>t</small>';
}
[sD,sM,sP,sK].forEach(s=>s.addEventListener('input',updAnch));updAnch();

window.addEventListener('load',function(){try{thermChart.resize();shortChart.resize();anchChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='building-movement-mep-tall-buildings', cat='tallmep', mins=16,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Building Movement &amp; MEP in Megatall Buildings: Thermal Expansion, Column Shortening &amp; Anchor Loads',
    reg_title='Building Movement & MEP in Megatall Buildings: Thermal Expansion, Column Shortening & Anchor Loads',
    reg_tag='Tall-Building Systems · Movement · Riser Support',
    breadcrumb='Tall-Building Systems',
    tag_line='Tall-Building Systems &middot; Building Movement &middot; Riser Support &middot; Anchors',
    desc='Building movement and MEP in megatall buildings: thermal expansion of risers and why plastics move ten times as far as steel, concrete creep and shrinkage shortening a tower by hundreds of millimetres with a third to a half arriving after the services are fixed, differential core-to-perimeter shortening that shears every horizontal run, expansion loop sizing, and the bellows pressure thrust that loads an anchor with eighty kilonewtons — with three interactive charts and installation tricks.',
    og_desc='A megatall tower shortens by about 700 mm over its life and 280 mm of that lands on services already installed. Plus the bellows pressure thrust that puts eight tonnes on a bracket detailed for pipe weight.',
    ld_desc='A design-perspective guide to building movement and MEP in megatall buildings: thermal expansion by material, elastic, creep and shrinkage shortening and the post-installation residual, differential core-to-perimeter shortening, anchors, guides and compensators, expansion loop sizing and bellows pressure thrust.',
    img_alt='Technical cutaway of a megatall tower services shaft showing a tall riser with fixed anchors, sliding guides and an axial bellows compensator between them, with the surrounding concrete core indicated as shortening over time',
    en_tag='Tall-Building Systems &middot; Building Movement &middot; Riser Support &middot; Anchors',
    en_title='Building Movement &amp; MEP in Megatall Buildings: Thermal Expansion, Column Shortening &amp; Anchor Loads',
    en_excerpt='A megatall tower is not a static object. It shortens by roughly <strong>700&nbsp;mm</strong> over its life as the concrete creeps and dries, and about <strong>280&nbsp;mm of that arrives after the risers are anchored</strong> &mdash; two and a half times their thermal movement, and additive to it. Core and perimeter shorten by different amounts, quietly shearing every horizontal run between them. Plus why plastic risers move ten times as far as steel, how to size an expansion loop, and the bellows pressure thrust that puts <strong>eight tonnes</strong> on a bracket detailed for pipe weight &mdash; with three interactive charts.',
    en_search='building movement thermal expansion column shortening creep shrinkage differential shortening tall buildings megatall supertall MEP risers pipe support anchors guides expansion loop guided cantilever bellows axial compensator tied bellows pressure balanced pressure thrust spring rate anchor load structural interface coefficient of expansion carbon steel stainless copper PPR PEX PVC plastics riser branch swing arm slab penetration sleeve fire stopping movement rated movement joint podium tower interface seismic restraint snubber cold pull pre-set installation temperature travel indicator survey datum EJMA ASME B31.1 Eurocode 2 ACI 209 CTBUH SMACNA commissioning building services',
    ar_title='حركة المبنى وأنظمة الميكانيكا في المباني فائقة الارتفاع: التمدد الحراري وتقاصر الأعمدة وأحمال المثبتات',
    ar_excerpt='المبنى فائق الارتفاع ليس جسمًا ساكنًا. فهو يقصر بنحو <strong>٧٠٠ ملم</strong> على مدى عمره مع زحف الخرسانة وجفافها، ويصل نحو <strong>٢٨٠ ملم من ذلك بعد تثبيت المواسير الصاعدة</strong> — أي ضعفَي ونصف حركتها الحرارية، ويُجمع معها. كما تتقاصر النواة والمحيط بمقادير مختلفة، فتقص بهدوء كل خط أفقي بينهما. ولماذا تتحرك المواسير البلاستيكية عشرة أضعاف الفولاذ، وكيف تُحسب حلقة التمدد، ودفع الضغط في المفصل المموج الذي يضع <strong>ثمانية أطنان</strong> على كتيفة صُمّمت لوزن الماسورة — مع ثلاثة رسوم تفاعلية.',
    ar_search='building movement thermal expansion column shortening creep shrinkage differential shortening risers anchors guides expansion loop bellows pressure thrust EJMA ASME B31.1 حركة المبنى التمدد الحراري تقاصر الأعمدة الزحف الانكماش التقاصر التفاضلي المباني الشاهقة المباني فائقة الارتفاع المواسير الصاعدة دعامات المواسير المثبتات الثابتة الموجهات حلقة التمدد الكابولي الموجه المفصل المموج المعوض المحوري المفصل المربوط المتوازن ضغطيًا دفع الضغط معدل الزنبرك حمل المثبت الواجهة الإنشائية معامل التمدد الفولاذ الكربوني المقاوم للصدأ النحاس البولي بروبيلين البلاستيك التفريعات ذراع التأرجح اختراق البلاطة الجلبة مانع الحريق المفصل الحركي واجهة القاعدة والبرج التقييد الزلزالي الشد البارد درجة حرارة التركيب مؤشر الحركة المسح المرجعي التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
