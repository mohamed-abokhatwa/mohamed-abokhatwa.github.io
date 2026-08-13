# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">There is one line in a tall-building chilled-water schematic that behaves completely differently from all the others, and it catches out engineers who have spent their careers on closed systems. The condenser water circuit is <strong>open</strong> — it ends in a cooling tower basin that is exposed to atmosphere — so the return column does not push back. The pump lifts the full height, every second, forever. Put the chillers in the basement and the towers on the roof of a 300&nbsp;m tower and you have just specified <strong>817&nbsp;kW of condenser pumping</strong> to move heat you could have moved for a tenth of that. This single distinction, more than any efficiency curve, is what dictates where heat rejection plant goes in a tall building — and in the Gulf it competes with a second constraint that is becoming the harder one: the towers will drink about <strong>2,400&nbsp;m³ of water a day</strong>.</p>

<h2 id="open">1 · The open-circuit trap</h2>
<p>In a closed chilled-water loop the water that goes up comes back down and the static head cancels, which is why a 600&nbsp;m tower needs only tens of metres of pump head — the argument set out in <a href="chilled-water-pumps-tall-buildings.html">chilled-water pumps</a>. A condenser water circuit ends in an open basin, so there is no returning column to balance the rising one:</p>
<div class="eq">\[ H_{CW} \;=\; \underbrace{z_{basin} - z_{pump}}_{\text{real static lift}} \;+\; h_{f} \;+\; h_{nozzle} \]</div>
<p>Every metre between the pump and the tower basin is head the pump must produce continuously. The consequences drive the whole architecture:</p>
<ul class="clean">
  <li><strong>Chillers go near their towers.</strong> Not in the basement with the towers on the roof, but on a high mechanical floor immediately below a tower deck, or paired at intermediate levels.</li>
  <li><strong>Or the circuit gets closed.</strong> A plate heat exchanger between an open tower circuit and a closed building circuit converts the problem back into a closed one — at the cost of an approach, exactly the trade described for chilled water zoning.</li>
  <li><strong>Or the towers come down.</strong> Podium-level or basement-intake towers with the chillers alongside, accepting the architectural and acoustic consequences.</li>
  <li><strong>Closed-circuit (fluid) coolers</strong> avoid the open basin entirely, at a penalty in approach and footprint.</li>
</ul>

<h2 id="int-lift">2 · Interactive: what the open circuit costs</h2>
<p>Set how far the tower basin sits above the condenser pumps. The blue curve is condenser pump power against that separation; the red line is what the same duty would cost if the circuit were closed and only friction had to be overcome.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Condenser pump power vs tower height above the pumps</div>
    <div class="fsub">Open circuit: H = static lift + friction + nozzle pressure. Closed circuit (via a plate heat exchanger): friction only. P = Q·H/(102·η).</div>
  </div>
  <div class="chart-box"><canvas id="liftChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Tower basin above pumps <span id="vZ">150 m</span></label>
      <input type="range" id="sZ" min="5" max="600" value="150" step="5">
      <div class="hint">Vertical separation between the condenser pumps and the tower basin.</div>
    </div>
    <div class="ctrl">
      <label>Condenser flow <span id="vQ">200 L/s</span></label>
      <input type="range" id="sQ" min="30" max="800" value="200" step="10">
      <div class="hint">Roughly 0.05 L/s per kW of heat rejected at a 5 K range.</div>
    </div>
    <div class="ctrl">
      <label>Friction + nozzle <span id="vF">25 m</span></label>
      <input type="range" id="sF" min="8" max="60" value="25" step="1">
      <div class="hint">Condenser, pipework, strainer and tower distribution nozzles.</div>
    </div>
    <div class="ctrl">
      <label>Pump efficiency <span id="vE">78 %</span></label>
      <input type="range" id="sE" min="55" max="88" value="78" step="1">
      <div class="hint">Wire-to-water for a large condenser pump.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Open-circuit head</div><div class="v" id="rH">175 <small>m</small></div></div>
    <div class="cell"><div class="k">Open-circuit power</div><div class="v" id="rP">440 <small>kW</small></div></div>
    <div class="cell"><div class="k">If closed via HX</div><div class="v" id="rPc">83 <small>kW</small></div></div>
    <div class="cell"><div class="k">Penalty</div><div class="v" id="rPn">357 <small>kW</small></div></div>
    <div class="cell"><div class="k">Annual penalty</div><div class="v" id="rAn">1,874 <small>MWh</small></div></div>
  </div>
</div>
<p class="fig-note">Lift the basin 150&nbsp;m above the pumps and the condenser set needs <strong>175&nbsp;m of head and 440&nbsp;kW</strong>, against 83&nbsp;kW if the same heat were moved through a closed loop — a <strong>357&nbsp;kW</strong> continuous penalty, about <strong>1,870&nbsp;MWh a year</strong> at typical run hours. That is the entire argument for putting chillers on high mechanical floors rather than in the basement, and it is why the roof-tower-basement-chiller arrangement that works perfectly in a ten-storey building is indefensible in a tower. Note the counter-argument the chart does not show: interposing a heat exchanger to close the loop costs an approach of about 1&nbsp;K on the condenser side, which is roughly a 2.5&nbsp;% chiller penalty — real, but far smaller than the pumping it saves.</p>

<h2 id="approach">3 · Approach, range and where the efficiency actually is</h2>
<p>A cooling tower is defined by two temperature differences and one ambient condition<sup class="cite">[1][2]</sup>:</p>
<ul class="clean">
  <li><strong>Range</strong> — the temperature drop across the tower, equal to the rise across the condenser. Set by the flow rate for a given load: \( \text{range} = \dot{Q}/(\dot{m}c_p)\). Typically 5–6&nbsp;K.</li>
  <li><strong>Approach</strong> — how close the leaving water gets to the ambient <strong>wet-bulb</strong> temperature. This is the tower's real performance measure, typically 3–5&nbsp;K. A closer approach means a physically larger tower, and the size grows steeply as the approach tightens; below about 2.5&nbsp;K it becomes uneconomic.</li>
  <li><strong>Wet bulb, not dry bulb.</strong> This is the number that matters, and it is where Gulf coastal sites are punished. Riyadh's summer design wet bulb is around 20&nbsp;°C despite a 44&nbsp;°C dry bulb; Jeddah's is around 29&nbsp;°C. A tower in Jeddah delivering a 4&nbsp;K approach produces 33&nbsp;°C condenser water where the same tower in Riyadh produces 24&nbsp;°C — and every one of those 9 K costs roughly 2.5&nbsp;% of chiller power.</li>
</ul>
<p>The design lever is that condenser water temperature and tower fan energy pull in opposite directions: a colder tower means a bigger, harder-working fan but a much more efficient chiller. The chiller is far larger than the fan, but fan power climbs steeply as the approach tightens, so <strong>the optimum is a real balance rather than a one-sided push</strong> — and its position is set by the fan-to-chiller power ratio, not by either machine alone. What is unambiguous is the operating case: a condenser-water reset that tracks the actual wet bulb is one of the highest-value control sequences in the plant, because for most of the year the wet bulb is far below design and the chiller will take every degree you give it.</p>

<h2 id="int-approach">4 · Interactive: approach, wet bulb &amp; total plant power</h2>
<p>Set the design wet bulb and the approach you are buying. The chart is total plant power — chiller plus tower fan — against approach, showing the optimum and how far it moves when the climate changes.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Chiller + tower fan power vs design approach</div>
    <div class="fsub">Condenser water leaving = wet bulb + approach. Chiller power scaled 2.5 % per K from a 30 °C reference; fan power scaled as (reference approach / approach)^1.6 to represent the airflow needed to close the approach.</div>
  </div>
  <div class="chart-box"><canvas id="appChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Design wet bulb <span id="vWb">29 °C</span></label>
      <input type="range" id="sWb" min="15" max="32" value="29" step="0.5">
      <div class="hint">Riyadh ≈ 20 °C, Jeddah and Doha ≈ 29 °C, London ≈ 20 °C.</div>
    </div>
    <div class="ctrl">
      <label>Approach <span id="vAp">4.0 K</span></label>
      <input type="range" id="sAp" min="2" max="9" value="4" step="0.1">
      <div class="hint">Leaving water minus wet bulb. Tighter = larger tower and bigger fan.</div>
    </div>
    <div class="ctrl">
      <label>Chiller power at reference <span id="vCh">1200 kW</span></label>
      <input type="range" id="sCh" min="200" max="4000" value="1200" step="50">
      <div class="hint">Compressor power at 30 °C entering condenser water.</div>
    </div>
    <div class="ctrl">
      <label>Fan power at 5 K approach <span id="vFn">90 kW</span></label>
      <input type="range" id="sFn" min="15" max="400" value="90" step="5">
      <div class="hint">Total tower fan power for the design airflow at a 5 K approach.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Condenser water</div><div class="v" id="rCw">33.0 <small>°C</small></div></div>
    <div class="cell"><div class="k">Chiller power</div><div class="v" id="rCp">1,290 <small>kW</small></div></div>
    <div class="cell"><div class="k">Fan power</div><div class="v" id="rFp">129 <small>kW</small></div></div>
    <div class="cell"><div class="k">Total</div><div class="v" id="rTp">1,419 <small>kW</small></div></div>
    <div class="cell"><div class="k">Optimum approach</div><div class="v" id="rOp">4.9 <small>K</small></div></div>
  </div>
</div>
<p class="fig-note">At a Jeddah wet bulb of 29&nbsp;°C, a 4&nbsp;K approach gives 33&nbsp;°C condenser water and about 1,419&nbsp;kW of combined plant power, with the optimum sitting at <strong>4.9&nbsp;K</strong>. The balance is genuine rather than one-sided: the chiller is fourteen times the size of the fan, but the fan power rises steeply as the approach tightens, so the two meet near 5&nbsp;K. What moves the answer is the <em>ratio</em> — halve the fan power and the optimum falls to 3.8&nbsp;K; double it and it climbs to 6.4&nbsp;K. Drop the wet bulb to Riyadh's 20&nbsp;°C and the whole curve falls by roughly a fifth for the same building: <strong>the same tower and the same chiller are a fundamentally different plant on the coast than they are inland.</strong> Design the tower for the site's wet bulb, not for a regional average, and reset the condenser set-point against measured wet bulb in operation.</p>

<h2 id="water">5 · Water — the constraint that is overtaking energy</h2>
<p>A cooling tower rejects heat mainly by evaporating water, and that water is consumed. The arithmetic is simple and the totals are startling<sup class="cite">[3]</sup>:</p>
<div class="eq">\[ E \approx \frac{\dot{Q}}{h_{fg}} \approx 1.5\ \text{m}^3/\text{h per MW rejected}, \qquad B = \frac{E}{\text{CoC}-1}, \qquad M = E + B \]</div>
<p>where \(E\) is evaporation, \(B\) blowdown and \(M\) makeup, and <strong>cycles of concentration</strong> (CoC) is how many times the dissolved solids are allowed to concentrate before water is dumped. A 50&nbsp;MW tower evaporates 75&nbsp;m³/h no matter what you do — that is physics — but the blowdown is entirely a water-treatment decision: at two cycles it is another 75&nbsp;m³/h, at six cycles just 15. <strong>Raising the cycles from 2 to 6 saves 1,440&nbsp;m³ a day</strong> on a single plant, which in a water-scarce region is a far more valuable saving than most energy measures.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Cooling tower makeup water vs cycles of concentration</div>
    <div class="fsub">E = 1.5 m³/h per MW rejected; B = E/(CoC−1); makeup M = E + B. Evaporation is fixed by physics; blowdown is a treatment decision.</div>
  </div>
  <div class="chart-box"><canvas id="waterChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Heat rejected <span id="vMw">50 MW</span></label>
      <input type="range" id="sMw" min="5" max="200" value="50" step="5">
      <div class="hint">Total tower duty ≈ chiller cooling × 1.25.</div>
    </div>
    <div class="ctrl">
      <label>Cycles of concentration <span id="vCo">4.0</span></label>
      <input type="range" id="sCo" min="1.5" max="10" value="4" step="0.1">
      <div class="hint">Limited by the makeup water chemistry and the treatment programme.</div>
    </div>
    <div class="ctrl">
      <label>Equivalent full-load hours <span id="vHr">4000 h</span></label>
      <input type="range" id="sHr" min="1000" max="8000" value="4000" step="100">
      <div class="hint">Annual operation at full rejection.</div>
    </div>
    <div class="ctrl">
      <label>Water tariff <span id="vTa">6.0 /m³</span></label>
      <input type="range" id="sTa" min="0.5" max="20" value="6" step="0.5">
      <div class="hint">Local potable or treated-water rate, in your currency.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Evaporation</div><div class="v" id="rEv">75 <small>m³/h</small></div></div>
    <div class="cell"><div class="k">Blowdown</div><div class="v" id="rBd">25 <small>m³/h</small></div></div>
    <div class="cell"><div class="k">Makeup</div><div class="v" id="rMu">100 <small>m³/h</small></div></div>
    <div class="cell"><div class="k">Per day</div><div class="v" id="rDay">2,400 <small>m³</small></div></div>
    <div class="cell"><div class="k">Annual cost</div><div class="v" id="rCost">2.4 <small>M</small></div></div>
  </div>
</div>
<p class="fig-note">A 50&nbsp;MW plant at four cycles consumes <strong>100&nbsp;m³/h — 2,400&nbsp;m³ a day</strong>, comparable to the domestic demand of several thousand people. Push the cycles from 2 to 6 and the makeup falls from 150 to 90&nbsp;m³/h with no change to the towers at all, purely through a better treatment programme and tighter conductivity control. In the Gulf this is where the real design conversation is heading: side-stream filtration, higher cycles, treated sewage effluent or condensate as makeup, and in some projects the decision to accept air-cooled chillers and their energy penalty rather than consume the water at all.</p>

<h2 id="placement">6 · Placement, wind and plume</h2>
<ul class="clean">
  <li><strong>Give the tower its air.</strong> Towers are volumetric air machines; they need unobstructed intake on all sides and a clear discharge path. Recirculation — hot moist discharge re-entering the intake — raises the effective wet bulb and silently destroys performance. Check separation from parapets, screens and adjacent towers, and treat architectural screening as an aerodynamic element requiring free area, not as cladding.</li>
  <li><strong>Wind at height changes the answer.</strong> A tower deck 300&nbsp;m up sits in the wind field described in <a href="outdoor-air-ventilation-tall-buildings.html">outdoor air and ventilation</a>. Cross-wind can strip the discharge plume down the leeward face, drive drift onto the façade and into intakes, and unbalance cells within a bank.</li>
  <li><strong>Drift and plume are contamination and nuisance risks.</strong> Specify high-efficiency drift eliminators (0.001&nbsp;% or better), check the plume against fresh-air intakes, helipads and openable windows, and consider plume-abated towers where visible plume is an issue.</li>
  <li><strong>Structure and access.</strong> A tower bank full of water is a heavy, dynamic, vibrating load on the highest part of the building. Coordinate the wet operating weight and the seismic and wind case with the structural engineer early, and design a maintenance route for fill replacement and motor changes at that level.</li>
  <li><strong>Freeze and shutdown.</strong> Even in the Gulf, basin heaters and a proper drain-down strategy matter for winter partial load; more importantly, plan the isolation and drain sequence for a cell taken out of service without shutting the plant.</li>
</ul>

<h2 id="legionella">7 · Water treatment and Legionella</h2>
<p>A cooling tower is a warm, aerated, nutrient-rich aerosol generator located near fresh-air intakes and public space. Control is a designed system, not a maintenance activity<sup class="cite">[4]</sup>:</p>
<ul class="clean">
  <li><strong>Design out stagnation.</strong> No dead legs, no idle standby cells left wet and unturned, and a basin arrangement that actually turns over. Rotate standby cells automatically.</li>
  <li><strong>Automate the treatment.</strong> Conductivity-controlled blowdown, proportional biocide dosing with two alternating biocides, corrosion and scale inhibitor, all monitored and trended rather than dosed on a visit schedule.</li>
  <li><strong>Side-stream filtration</strong> to remove the solids that both foul the fill and shelter organisms from biocide.</li>
  <li><strong>Sample and record.</strong> Routine dip-slides and Legionella sampling with the results trended, and a written water safety plan naming the responsible person.</li>
  <li><strong>Design for cleaning.</strong> Basins that can be drained, accessed and physically cleaned, with removable fill packs — this is the item most often designed out for space and most often needed.</li>
</ul>

<h2 id="install">8 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Set the basin level and the pump suction together.</strong> Condenser pumps need positive suction and adequate submergence; check the NPSH available at the highest basin level and, critically, at the <em>lowest</em> operating level during a rapid load change.</li>
  <li><strong>Equalise multi-cell basins properly.</strong> Under-sized equalisation lines are the classic cause of one cell overflowing while another starves and draws air.</li>
  <li><strong>Provide a proper flooded start and a drain-back volume.</strong> When the pumps stop, the water in the risers comes back; the basin must accept it without overflowing. Size the freeboard for the full drain-back, not for the static level.</li>
  <li><strong>Fit isolation, strainers and test points on every cell</strong>, and a permanent flow meter on the condenser circuit — condenser flow is the most commonly wrong and least measured number in a chiller plant.</li>
  <li><strong>Clean and passivate before handover.</strong> New galvanised towers need a controlled passivation period at moderate pH; skip it and white rust starts in the first month.</li>
  <li><strong>Do not commission on a mild day and call it done.</strong> Tower capacity is only meaningful at the design wet bulb; where that cannot be achieved, test at the achievable wet bulb and correct to design using the manufacturer's performance curves, and record both.</li>
  <li><strong>Protect the fill during construction.</strong> Construction debris and site water in a new tower ruins the fill and seeds the system biologically before it is ever handed over.</li>
</ul>

<h2 id="checklist">9 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Recognise the open circuit</strong> — locate chillers near their towers, or close the loop with a heat exchanger, and never lift condenser water hundreds of metres by default.</li>
  <li><strong>Design on the site wet bulb</strong>, and check what the approach is really worth against chiller power.</li>
  <li><strong>Optimise approach on total plant power</strong>, not on tower first cost — the answer is colder than it looks.</li>
  <li><strong>Specify condenser-water reset</strong> against measured wet bulb, with the chiller's minimum entering temperature respected.</li>
  <li><strong>Compute the water balance</strong> and design the treatment for high cycles; evaluate alternative makeup sources.</li>
  <li><strong>Give the towers air</strong> — free intake, clear discharge, screening treated aerodynamically, recirculation checked.</li>
  <li><strong>Check plume and drift</strong> against every intake, opening and helipad.</li>
  <li><strong>Design the Legionella control system</strong>, not just the dosing contract.</li>
  <li><strong>Coordinate the wet weight and dynamics</strong> with the structural engineer, and design the maintenance route.</li>
  <li><strong>Commission with correction to design wet bulb</strong>, and passivate before handover.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Condenser water is the one <strong>open</strong> circuit in the building, so the pump lifts the full height — put the chillers next to their towers or close the loop with a heat exchanger, because a 150&nbsp;m separation is a 357&nbsp;kW permanent penalty. Design the tower on the site's <strong>wet bulb</strong>, optimise the approach on chiller-plus-fan power rather than tower cost (the balance lands near 5&nbsp;K and moves with the fan-to-chiller power ratio), and treat the water balance as a first-order design output: 2,400&nbsp;m³ a day is what a 50&nbsp;MW plant drinks, and the cycles of concentration — not the towers — decide how much of that you can give back.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Handbook — HVAC Systems and Equipment</em>, Cooling Towers chapter — range, approach, wet-bulb performance and tower types.</li>
  <li>Cooling Technology Institute (CTI) ATC-105 <em>Acceptance Test Code for Water Cooling Towers</em> and CTI certification standards — performance testing and correction to design conditions.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Water Treatment chapter — cycles of concentration, blowdown, scale and corrosion control, side-stream filtration.</li>
  <li>ASHRAE Standard 188 <em>Legionellosis: Risk Management for Building Water Systems</em> and ASHRAE Guideline 12; HSE <em>ACOP L8</em> and HSG274 Part 1 for evaporative cooling systems.</li>
  <li>ANSI/ASHRAE/IES Standard 90.1 — condenser water reset, tower fan control and minimum equipment efficiency.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — heat rejection plant location and condenser water strategy in tall buildings.</li>
  <li>ASHRAE <em>Handbook — Fundamentals</em>, Climatic Design Information — design wet-bulb data by location.</li>
  <li>Saudi Building Code <em>SBC 501</em> and Saudi water regulations on cooling tower makeup, alternative water sources and discharge.</li>
</ol>

<div class="tags">#CoolingTowers #HeatRejection #CondenserWater #OpenCircuit #TallBuildings #MegatallBuildings #Chillers #WetBulb #Approach #Range #CondenserWaterReset #PlantOptimisation #WaterConsumption #CyclesOfConcentration #Blowdown #Makeup #WaterTreatment #Legionella #ASHRAE188 #Drift #Plume #Recirculation #SideStreamFiltration #Commissioning #CTI #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};

/* ---------- CHART 1 : open circuit lift ---------- */
const sZ=document.getElementById('sZ'),sQ=document.getElementById('sQ'),
      sF=document.getElementById('sF'),sE=document.getElementById('sE');
const pkW=(Q,H,e)=>Q*H/(102*e);
let liftChart=new Chart(document.getElementById('liftChart'),{
  data:{datasets:[
    {type:'line',label:'Open circuit (tower basin open to air)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Closed via plate heat exchanger',data:[],borderColor:'#1b4f72',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'Your plant',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:600,title:{display:true,text:'Tower basin above the condenser pumps (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Condenser pump shaft power (kW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} kW at ${fmt0(c.parsed.x)} m`}}}}
});
function updLift(){
  const z=+sZ.value,Q=+sQ.value,f=+sF.value,e=+sE.value/100;
  document.getElementById('vZ').textContent=z+' m';
  document.getElementById('vQ').textContent=Q+' L/s';
  document.getElementById('vF').textContent=f+' m';
  document.getElementById('vE').textContent=fmt0(e*100)+' %';
  const xs=[];for(let h=5;h<=600;h+=5)xs.push(h);
  liftChart.data.datasets[0].data=xs.map(h=>({x:h,y:+pkW(Q,h+f,e).toFixed(0)}));
  liftChart.data.datasets[1].data=xs.map(h=>({x:h,y:+pkW(Q,f+8,e).toFixed(0)}));
  const Ho=z+f, Po=pkW(Q,Ho,e), Pc=pkW(Q,f+8,e);
  liftChart.data.datasets[2].data=[{x:z,y:+Po.toFixed(0)}];
  liftChart.update('none');
  document.getElementById('rH').innerHTML=fmt0(Ho)+' <small>m</small>';
  document.getElementById('rP').innerHTML=fmt0(Po)+' <small>kW</small>';
  document.getElementById('rPc').innerHTML=fmt0(Pc)+' <small>kW</small>';
  document.getElementById('rPn').innerHTML=fmt0(Po-Pc)+' <small>kW</small>';
  document.getElementById('rAn').innerHTML=fmt0((Po-Pc)*5250/1000)+' <small>MWh</small>';
}
[sZ,sQ,sF,sE].forEach(s=>s.addEventListener('input',updLift));updLift();

/* ---------- CHART 2 : approach optimisation ---------- */
const sWb=document.getElementById('sWb'),sAp=document.getElementById('sAp'),
      sCh=document.getElementById('sCh'),sFn=document.getElementById('sFn');
const REF_CW=30, PEN=0.025, REF_AP=5, FAN_EXP=1.6;
const chillerP=(P0,cw)=>P0*(1+PEN*(cw-REF_CW));
const fanP=(F0,ap)=>F0*Math.pow(REF_AP/Math.max(ap,0.5),FAN_EXP);
let appChart=new Chart(document.getElementById('appChart'),{
  data:{datasets:[
    {type:'line',label:'Chiller power',data:[],borderColor:'#c0392b',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:4},
    {type:'line',label:'Tower fan power',data:[],borderColor:'#1e8449',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:3},
    {type:'line',label:'Total plant power',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.08)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your design',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:2,max:9,title:{display:true,text:'Design approach (K above wet bulb)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Power (kW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} kW at ${fmt1(c.parsed.x)} K`}}}}
});
function updApp(){
  const wb=+sWb.value,ap=+sAp.value,P0=+sCh.value,F0=+sFn.value;
  document.getElementById('vWb').textContent=fmt1(wb)+' °C';
  document.getElementById('vAp').textContent=fmt1(ap)+' K';
  document.getElementById('vCh').textContent=P0+' kW';
  document.getElementById('vFn').textContent=F0+' kW';
  const xs=[];for(let a=2;a<=9;a+=0.1)xs.push(+a.toFixed(1));
  const tot=a=>chillerP(P0,wb+a)+fanP(F0,a);
  appChart.data.datasets[0].data=xs.map(a=>({x:a,y:+chillerP(P0,wb+a).toFixed(0)}));
  appChart.data.datasets[1].data=xs.map(a=>({x:a,y:+fanP(F0,a).toFixed(0)}));
  appChart.data.datasets[2].data=xs.map(a=>({x:a,y:+tot(a).toFixed(0)}));
  appChart.data.datasets[3].data=[{x:ap,y:+tot(ap).toFixed(0)}];
  appChart.update('none');
  let best=xs[0];xs.forEach(a=>{if(tot(a)<tot(best))best=a;});
  document.getElementById('rCw').innerHTML=fmt1(wb+ap)+' <small>°C</small>';
  document.getElementById('rCp').innerHTML=fmt0(chillerP(P0,wb+ap))+' <small>kW</small>';
  document.getElementById('rFp').innerHTML=fmt0(fanP(F0,ap))+' <small>kW</small>';
  document.getElementById('rTp').innerHTML=fmt0(tot(ap))+' <small>kW</small>';
  document.getElementById('rOp').innerHTML=fmt1(best)+' <small>K</small>';
}
[sWb,sAp,sCh,sFn].forEach(s=>s.addEventListener('input',updApp));updApp();

/* ---------- CHART 3 : water ---------- */
const sMw=document.getElementById('sMw'),sCo=document.getElementById('sCo'),
      sHr=document.getElementById('sHr'),sTa=document.getElementById('sTa');
const EVAP=1.5;   // m3/h per MW rejected
let waterChart=new Chart(document.getElementById('waterChart'),{
  data:{datasets:[
    {type:'line',label:'Makeup water',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Evaporation (fixed by physics)',data:[],borderColor:'#c0392b',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your plant',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1.5,max:10,title:{display:true,text:'Cycles of concentration',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Water rate (m³/h)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} m³/h at ${fmt1(c.parsed.x)} cycles`}}}}
});
function updWater(){
  const MW=+sMw.value,co=+sCo.value,hr=+sHr.value,ta=+sTa.value;
  document.getElementById('vMw').textContent=MW+' MW';
  document.getElementById('vCo').textContent=fmt1(co);
  document.getElementById('vHr').textContent=hr+' h';
  document.getElementById('vTa').textContent=fmt1(ta)+' /m³';
  const E=EVAP*MW;
  const xs=[];for(let c=1.5;c<=10;c+=0.1)xs.push(+c.toFixed(1));
  waterChart.data.datasets[0].data=xs.map(c=>({x:c,y:+(E+E/(c-1)).toFixed(1)}));
  waterChart.data.datasets[1].data=xs.map(c=>({x:c,y:+E.toFixed(1)}));
  const B=E/(co-1), M=E+B;
  waterChart.data.datasets[2].data=[{x:co,y:+M.toFixed(1)}];
  waterChart.update('none');
  document.getElementById('rEv').innerHTML=fmt0(E)+' <small>m³/h</small>';
  document.getElementById('rBd').innerHTML=fmt0(B)+' <small>m³/h</small>';
  document.getElementById('rMu').innerHTML=fmt0(M)+' <small>m³/h</small>';
  document.getElementById('rDay').innerHTML=fmt0(M*24)+' <small>m³</small>';
  document.getElementById('rCost').innerHTML=fmt1(M*hr*ta/1e6)+' <small>M</small>';
}
[sMw,sCo,sHr,sTa].forEach(s=>s.addEventListener('input',updWater));updWater();

window.addEventListener('load',function(){try{liftChart.resize();appChart.resize();waterChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='cooling-towers-heat-rejection-tall-buildings', cat='hvac', mins=18,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Cooling Towers &amp; Heat Rejection in Megatall Buildings: The Open Circuit, Wet-Bulb Approach &amp; the Water Balance',
    reg_title='Cooling Towers & Heat Rejection in Megatall Buildings: The Open Circuit, Wet-Bulb Approach & the Water Balance',
    reg_tag='HVAC · Cooling Towers · Heat Rejection',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Cooling Towers &middot; Heat Rejection &middot; Megatall Buildings',
    desc='Cooling tower and heat rejection design in megatall buildings: why the condenser water circuit is open so the pump lifts the full height, where that puts the chillers, approach and wet-bulb optimisation against combined chiller and fan power, the water balance and cycles of concentration that decide makeup consumption, plume drift and recirculation at height, and Legionella control — with three interactive charts and installation tricks.',
    og_desc='Condenser water is the one open circuit in the building — a 150 m separation between chillers and towers is a 377 kW permanent penalty. Plus wet-bulb approach optimisation and the 2,400 m3 a day a 50 MW plant drinks.',
    ld_desc='A design-perspective guide to cooling towers and heat rejection in megatall buildings: open versus closed condenser circuits and plant location, approach and wet-bulb optimisation on total plant power, cooling tower water balance and cycles of concentration, placement, wind, plume and drift, and Legionella risk management.',
    img_alt='Technical cutaway of a megatall tower showing cooling towers on a high plant deck with chillers on the mechanical floor immediately below, condenser water risers connecting them, and the tower discharge plume being carried by the wind',
    en_tag='HVAC &amp; Cooling &middot; Cooling Towers &middot; Heat Rejection &middot; Megatall',
    en_title='Cooling Towers &amp; Heat Rejection in Megatall Buildings: The Open Circuit, Wet-Bulb Approach &amp; the Water Balance',
    en_excerpt='One line in a tall-building chilled-water schematic behaves completely differently from all the others: the condenser circuit is <em>open</em>, so the return column never pushes back and the pump lifts the full height forever. Put the chillers in the basement and the towers on a 300&nbsp;m roof and that is 817&nbsp;kW of pumping. Approach and wet-bulb optimisation against combined chiller and fan power, why the optimum is colder than the specification says, the water balance that has a 50&nbsp;MW plant drinking 2,400&nbsp;m&sup3; a day, plume and recirculation at height, and Legionella control &mdash; with three interactive charts.',
    en_search='cooling towers heat rejection condenser water tall buildings megatall supertall open circuit closed circuit static lift plate heat exchanger chiller location mechanical floor fluid cooler approach range wet bulb design wet bulb condenser water reset chiller efficiency penalty tower fan power optimisation evaporation blowdown cycles of concentration makeup water balance side stream filtration treated sewage effluent water scarcity drift eliminator plume abatement recirculation intake obstruction wind at height structural wet weight basin equalisation drain back freeboard NPSH submergence passivation white rust Legionella ASHRAE 188 HSG274 CTI ATC-105 commissioning MEP building services HVAC',
    ar_title='أبراج التبريد وطرد الحرارة في المباني فائقة الارتفاع: الدائرة المفتوحة ودرجة البصيلة الرطبة وميزان المياه',
    ar_excerpt='هناك خط واحد في مخطط المياه المبردة يتصرّف تصرّفًا مختلفًا تمامًا عن بقية الخطوط: دائرة مياه المكثف <em>مفتوحة</em>، فلا يوجد عمود عائد يدفع للخلف، والمضخة ترفع كامل الارتفاع إلى الأبد. ضع المبردات في القبو والأبراج على سطح مبنى بارتفاع ٣٠٠ متر وستحتاج ٨١٧ كيلوواط للضخ. تحسين فرق الاقتراب ودرجة البصيلة الرطبة مقابل قدرة المبرد والمروحة معًا، ولماذا يكون الحل الأمثل أبرد ممّا تنصّ عليه المواصفات، وميزان المياه الذي يجعل محطة ٥٠ ميغاواط تستهلك ٢٤٠٠ متر مكعب يوميًا، والعمود المتصاعد وإعادة السحب على الارتفاعات، ومكافحة الليجيونيلا — مع ثلاثة رسوم تفاعلية.',
    ar_search='cooling towers heat rejection condenser water open circuit chiller location approach wet bulb condenser water reset evaporation blowdown cycles of concentration makeup drift plume recirculation Legionella ASHRAE 188 CTI أبراج التبريد طرد الحرارة مياه المكثف المباني الشاهقة المباني فائقة الارتفاع الدائرة المفتوحة الدائرة المغلقة الرفع الاستاتيكي المبادل الحراري الصفائحي موقع المبردات الطابق الميكانيكي المبرد المغلق فرق الاقتراب المدى الحراري البصيلة الرطبة درجة التصميم إعادة ضبط حرارة المكثف كفاءة المبرد قدرة مروحة البرج التحسين التبخر التصريف دورات التركيز مياه التعويض ميزان المياه الترشيح الجانبي مياه الصرف المعالجة ندرة المياه مانع الرذاذ تخفيف العمود المتصاعد إعادة السحب الرياح على الارتفاع الوزن التشغيلي معادلة الأحواض الارتداد المائي الحيز الحر صافي ضغط الشفط الموجب التخميل الصدأ الأبيض الليجيونيلا التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
