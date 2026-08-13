# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Thermal storage is the only way to buy cooling at one time and use it at another, and in a Gulf tower that arbitrage is worth a great deal — a 40&nbsp;MW plant shifting its peak can cut its chiller capacity by <strong>40&nbsp;%</strong> and take a real bite out of its electricity bill. But it comes with a physical constraint that decides the entire design before economics is even discussed: storing 128&nbsp;MWh as chilled water needs <strong>13,757 cubic metres of tank — nearly fourteen thousand tonnes</strong>. That does not go in a tower. As ice it is 1,538&nbsp;m³, roughly nine times more compact, and suddenly it fits in a basement. Thermal storage in a tall building is therefore an <em>ice</em> question, or it is not a question at all.</p>

<h2 id="why">1 · Why storage and towers are an awkward fit</h2>
<ul class="clean">
  <li><strong>Storage is heavy and towers hate weight.</strong> Water stores about 9.3&nbsp;kWh per tonne at an 8&nbsp;K ΔT. Any meaningful capacity is thousands of tonnes and belongs at or below grade, never up the building.</li>
  <li><strong>Latent storage is nine times denser.</strong> Ice stores its heat as a phase change at 333&nbsp;kJ/kg rather than as sensible heat over a few kelvin, which is why every space-constrained project ends up looking at it.</li>
  <li><strong>The tariff is what pays for it.</strong> The economics come from the difference between on-peak and off-peak electricity and from avoided demand charges. Where that difference is small, storage is a resilience and capacity measure rather than an energy one — and should be argued as such.</li>
  <li><strong>Making ice costs efficiency.</strong> A chiller producing −6&nbsp;°C brine instead of 6&nbsp;°C water loses roughly a quarter to a third of its COP. Storage does not save energy; it <em>moves</em> it, and it moves slightly more than it shifted.</li>
  <li><strong>It buys capacity, which in a megatall is worth more than energy.</strong> A smaller chiller plant means a smaller plant room, smaller electrical infrastructure, smaller cooling towers and less water — the compounding benefit that is usually left out of the payback calculation.</li>
</ul>

<h2 id="int-vol">2 · Interactive: how much tank, and of what</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Storage volume by medium</div>
    <div class="fsub">Sensible storage V = E/(ρ·c&#112;·ΔT); latent (ice) V = E/(h&#102;·packing). Chilled water depends entirely on the ΔT you can actually stratify; ice does not.</div>
  </div>
  <div class="chart-box"><canvas id="volChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Stored capacity <span id="vE">128 MWh</span></label>
      <input type="range" id="sE" min="5" max="400" value="128" step="1">
      <div class="hint">Cooling to be delivered from storage over the on-peak period.</div>
    </div>
    <div class="ctrl">
      <label>Chilled-water ΔT <span id="vD">8.0 K</span></label>
      <input type="range" id="sD" min="5" max="14" value="8" step="0.5">
      <div class="hint">Usable stratified difference — not the design coil ΔT. Stratified tanks rarely beat 9–10 K in practice.</div>
    </div>
    <div class="ctrl">
      <label>Ice packing factor <span id="vP">90 %</span></label>
      <input type="range" id="sP" min="60" max="100" value="90" step="1">
      <div class="hint">Usable fraction of tank volume for internal-melt ice-on-coil systems.</div>
    </div>
    <div class="ctrl">
      <label>Available plant height <span id="vHt">6.0 m</span></label>
      <input type="range" id="sHt" min="3" max="15" value="6" step="0.5">
      <div class="hint">To convert volume into the footprint you actually have to find.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Chilled water</div><div class="v" id="rVw">13,757 <small>m³</small></div></div>
    <div class="cell"><div class="k">Ice</div><div class="v" id="rVi">1,538 <small>m³</small></div></div>
    <div class="cell"><div class="k">Compactness</div><div class="v" id="rRt">8.9<small>×</small></div></div>
    <div class="cell"><div class="k">Ice footprint</div><div class="v" id="rFp">256 <small>m²</small></div></div>
    <div class="cell"><div class="k">Water footprint</div><div class="v" id="rFw">2,293 <small>m²</small></div></div>
  </div>
</div>
<p class="fig-note">128&nbsp;MWh as chilled water is <strong>13,757&nbsp;m³</strong> — a 2,293&nbsp;m² tank farm six metres deep, which is most of a basement level and fourteen thousand tonnes of structural load. As ice it is <strong>1,538&nbsp;m³</strong> and about 256&nbsp;m². That ratio is why almost every tall-building thermal store is latent rather than sensible, and it is also why the decision has to be made before the basement is designed: nobody finds 2,300&nbsp;m² of tank space in a completed scheme. Note how sensitive the water case is to the ΔT slider — a stratified tank that only achieves 6&nbsp;K instead of 9&nbsp;K is half as useful, and stratification quality is a real, and commonly disappointing, design risk.</p>

<h2 id="int-peak">3 · Interactive: what peak shaving buys</h2>
<p>With <strong>full storage</strong> the chillers do not run on-peak at all; with <strong>partial storage</strong> — almost always the right answer — the chillers run more or less continuously at a lower rating and storage covers the difference at peak.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Chiller capacity and storage size vs load factor</div>
    <div class="fsub">Partial storage: chiller sized at the daily mean load (peak × load factor); storage carries the on-peak difference. Load factor is the daily average cooling divided by the peak.</div>
  </div>
  <div class="chart-box"><canvas id="peakChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Peak cooling load <span id="vL">40 MW</span></label>
      <input type="range" id="sL" min="5" max="150" value="40" step="1">
      <div class="hint">Design day peak demand of the development.</div>
    </div>
    <div class="ctrl">
      <label>Daily load factor <span id="vLf">60 %</span></label>
      <input type="range" id="sLf" min="35" max="90" value="60" step="1">
      <div class="hint">Daily average ÷ peak. Mixed-use towers run higher than pure offices.</div>
    </div>
    <div class="ctrl">
      <label>On-peak window <span id="vOp">8 h</span></label>
      <input type="range" id="sOp" min="3" max="14" value="8" step="1">
      <div class="hint">Hours the tariff or the demand charge applies.</div>
    </div>
    <div class="ctrl">
      <label>Ice-making COP penalty <span id="vCp">28 %</span></label>
      <input type="range" id="sCp" min="10" max="45" value="28" step="1">
      <div class="hint">Efficiency lost producing ice rather than chilled water.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Chiller with TES</div><div class="v" id="rCh">24 <small>MW</small></div></div>
    <div class="cell"><div class="k">Capacity saved</div><div class="v" id="rCs">40 <small>%</small></div></div>
    <div class="cell"><div class="k">Storage needed</div><div class="v" id="rSt">128 <small>MWh</small></div></div>
    <div class="cell"><div class="k">Ice volume</div><div class="v" id="rIv">1,538 <small>m³</small></div></div>
    <div class="cell"><div class="k">Extra energy</div><div class="v" id="rEx">+9 <small>%</small></div></div>
  </div>
</div>
<p class="fig-note">A 40&nbsp;MW peak at a 60&nbsp;% load factor lets the chiller plant drop to <strong>24&nbsp;MW — 40&nbsp;% smaller</strong> — with 128&nbsp;MWh of storage covering the on-peak difference. That is a smaller plant room, smaller substation, smaller towers and less makeup water, all compounding. The honest cost is on the right: making that portion of the cooling as ice consumes roughly <strong>9&nbsp;% more energy overall</strong>, because the ice-making chillers run at a worse COP. Storage is a <em>capacity and tariff</em> measure, not an efficiency measure, and any business case that claims energy savings from the storage itself is wrong.</p>

<h2 id="int-econ">4 · Interactive: the tariff arbitrage</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Annual saving from shifting cooling off-peak</div>
    <div class="fsub">Saving = shifted energy × (on-peak rate − off-peak rate) × operating days, less the extra electricity from the ice-making COP penalty, plus any avoided demand charge.</div>
  </div>
  <div class="chart-box"><canvas id="econChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Shifted cooling per day <span id="vSh">128 MWh</span></label>
      <input type="range" id="sSh" min="10" max="400" value="128" step="2">
      <div class="hint">Cooling delivered from storage on a design day.</div>
    </div>
    <div class="ctrl">
      <label>On-peak rate <span id="vOn">0.32</span></label>
      <input type="range" id="sOn" min="0.05" max="0.8" value="0.32" step="0.01">
      <div class="hint">Electricity rate during the peak window, per kWh.</div>
    </div>
    <div class="ctrl">
      <label>Off-peak rate <span id="vOf">0.18</span></label>
      <input type="range" id="sOf" min="0.02" max="0.6" value="0.18" step="0.01">
      <div class="hint">Night rate. Where this equals the day rate, the arbitrage disappears.</div>
    </div>
    <div class="ctrl">
      <label>Operating days <span id="vDy">250</span></label>
      <input type="range" id="sDy" min="60" max="365" value="250" step="5">
      <div class="hint">Days a year the shift is actually made.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Gross arbitrage</div><div class="v" id="rGa">0.81 <small>M/yr</small></div></div>
    <div class="cell"><div class="k">COP penalty cost</div><div class="v" id="rPc">0.41 <small>M/yr</small></div></div>
    <div class="cell"><div class="k">Net saving</div><div class="v" id="rNs">0.41 <small>M/yr</small></div></div>
    <div class="cell"><div class="k">Rate ratio</div><div class="v" id="rRr">1.78<small>×</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">At a 0.32/0.18 tariff split, shifting 128&nbsp;MWh of cooling a day over 250 days moves about 23&nbsp;MWh of <em>electricity</em> a day into the night, worth <strong>0.82&nbsp;M gross</strong> — less roughly <strong>0.41&nbsp;M</strong> of extra electricity from the ice-making penalty, for a net <strong>0.41&nbsp;M a year</strong> before any avoided demand charge. Note how much of the gross the penalty eats: half of it, at this tariff. Now drag the two rates together: as the ratio falls below about 1.4 the COP penalty eats most of the benefit and the scheme has to be justified on capacity alone. <strong>Check the tariff before the tanks.</strong> And check its stability — a storage scheme is a twenty-five-year asset justified by a tariff structure that a regulator can revise in a year, which is a genuine commercial risk worth stating in the design report rather than discovering later.</p>

<h2 id="types">5 · Choosing the storage type</h2>
<ul class="clean">
  <li><strong>Stratified chilled-water tanks.</strong> Simple, no COP penalty, uses the existing chillers, and the tank can double as fire-water or resilience storage. But it is enormous, and its usable capacity depends entirely on maintaining a clean thermocline — which needs proper diffusers, low inlet velocities and a tank geometry with a decent height-to-diameter ratio. Best where land is available at grade.</li>
  <li><strong>Ice-on-coil, internal melt.</strong> The workhorse for space-constrained sites. Glycol circulates through coils in a tank, freezing water around them, then melts it from the inside. Predictable, modular, and roughly nine times denser than water. Needs a glycol loop, a heat exchanger to the building side, and chillers selected for low-temperature duty.</li>
  <li><strong>Ice harvesting and encapsulated ice.</strong> Alternatives with different discharge characteristics; encapsulated ice (nodules in a tank) packs well and suits retrofits into existing tanks.</li>
  <li><strong>Phase-change materials above 0&nbsp;°C.</strong> PCMs melting at 6–10&nbsp;°C avoid the ice-making COP penalty entirely because the chillers run at normal temperatures, at the cost of lower storage density than ice and a higher material cost. Worth evaluating where the tariff split is modest and the COP penalty would otherwise kill the scheme.</li>
</ul>

<h2 id="control">6 · Control is where storage projects fail</h2>
<p>A thermal store is only worth what its control sequence extracts. The recurring failures are all strategic rather than mechanical:</p>
<ul class="clean">
  <li><strong>Discharging too early.</strong> A store emptied by mid-afternoon leaves the chillers exposed at the real peak. The sequence must forecast the remaining day's load, not react to the current one.</li>
  <li><strong>Not filling completely.</strong> Overnight charge must be verified against inventory, not against run hours. Instrument the store for <em>state of charge</em> and trend it — a store that has been running at 70&nbsp;% charge for two years is a common and invisible failure.</li>
  <li><strong>Chiller priority confusion.</strong> Decide explicitly, in the sequence, whether chiller or storage leads at each hour and each load, and what happens on a chiller failure.</li>
  <li><strong>Ignoring the demand charge.</strong> Where the tariff has a peak-demand component, the control objective is to cap the electrical demand, not merely to shift energy — a different and more valuable optimisation.</li>
  <li><strong>No weather or occupancy forecast.</strong> Modern sequences use next-day forecast to size the overnight charge; charging fully every night on a mild day wastes the COP penalty for nothing.</li>
</ul>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Get the tank load to the structural engineer early</strong> — a full store is thousands of tonnes and its position, bearing pressure and seismic mass all affect the substructure design.</li>
  <li><strong>Insulate and vapour-seal the tank properly.</strong> A sub-zero store in a humid Gulf basement will condense and then corrode at every thermal bridge; specify the vapour barrier as carefully as the insulation and detail the supports through it.</li>
  <li><strong>Manage the glycol.</strong> Concentration, inhibitor level and compatibility with every seal and gasket in the loop, checked at commissioning and scheduled thereafter. A degraded inhibitor package turns a glycol loop into a corrosion cell.</li>
  <li><strong>Design the tank for inspection and cleaning</strong> — access, drain-down and a route to replace coils.</li>
  <li><strong>Instrument the state of charge</strong> from day one, with the sensors the control sequence actually needs, and prove the inventory calculation at commissioning by a full charge-discharge cycle against a measured load.</li>
  <li><strong>Commission across a full cycle, not a snapshot.</strong> The acceptance test is a complete charge overnight and a complete discharge over the peak, with the load simulated or real, and the results compared against the design profile.</li>
  <li><strong>Train the operator, and write the sequence down in plain language.</strong> Storage is the system most likely to be switched to manual after a handover disagreement and never switched back.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Check the tariff split and its stability</strong> before anything else; below about 1.4 the case must rest on capacity.</li>
  <li><strong>Size from a real daily load profile</strong>, not a peak and a guess at load factor.</li>
  <li><strong>Choose the medium on space and COP penalty together</strong> — ice for constrained sites, water where land allows, PCM where the tariff is thin.</li>
  <li><strong>Count the capacity savings in full</strong> — chillers, plant room, substation, towers and makeup water.</li>
  <li><strong>State the energy penalty honestly</strong> in the business case.</li>
  <li><strong>Issue the tank loads early</strong> and coordinate the substructure.</li>
  <li><strong>Design the control sequence as a deliverable</strong>, with forecast-based charging and an explicit demand-cap objective.</li>
  <li><strong>Instrument state of charge</strong> and trend it.</li>
  <li><strong>Commission a full charge-discharge cycle</strong> against a measured load.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Thermal storage in a tall building is decided by <strong>density before economics</strong>: 128&nbsp;MWh is 13,757&nbsp;m³ as chilled water and 1,538&nbsp;m³ as ice, so constrained sites store latent heat or they do not store at all — and either way it goes below grade, early, with the load issued to the structural engineer. It buys <strong>capacity</strong> — a 40&nbsp;% smaller chiller plant and everything that follows from it — and it buys <strong>tariff arbitrage</strong> &mdash; though the COP penalty eats about half the gross &mdash; but it does not buy energy: making ice costs about a quarter of your COP, so the plant uses roughly 9&nbsp;% more electricity to deliver the same cooling. Say that plainly in the business case, then win the argument on capacity and demand charge, which is where it is actually won.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Handbook — HVAC Systems and Equipment</em>, Thermal Storage chapter — sensible and latent storage media, sizing, stratification and system integration.</li>
  <li>ASHRAE <em>Design Guide for Cool Thermal Storage</em> — full and partial storage strategies, control sequences and commissioning.</li>
  <li>ANSI/ASHRAE Standard 150 — <em>Method of Testing the Performance of Cool Storage Systems</em>; and ASHRAE Guideline 4 for storage system commissioning.</li>
  <li>ASHRAE <em>District Cooling Guide</em>, 2nd ed. — thermal storage in district and campus systems, including peak-shaving economics.</li>
  <li>ANSI/ASHRAE/IES Standard 90.1 — energy modelling treatment of thermal storage and demand-limiting controls.</li>
  <li>IEA Energy Conservation through Energy Storage / Annex reports on phase-change materials and cool storage applications.</li>
  <li>Saudi Electricity Company tariff structures and the Saudi Building Code <em>SBC 501</em> — the local tariff and regulatory basis for any Gulf storage business case.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — plant location, structural interface and storage in tall buildings.</li>
</ol>

<div class="tags">#ThermalEnergyStorage #TES #IceStorage #ChilledWaterStorage #Stratification #PCM #PhaseChangeMaterial #PeakShaving #LoadShifting #DemandCharge #TariffArbitrage #TallBuildings #MegatallBuildings #Chillers #PlantCapacity #COP #Glycol #StateOfCharge #ControlSequence #ForecastControl #Commissioning #ASHRAE150 #DistrictCooling #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const CP=4.187, HFUS=333;

/* ---------- CHART 1 : storage volume ---------- */
const sE=document.getElementById('sE'),sD=document.getElementById('sD'),
      sP=document.getElementById('sP'),sHt=document.getElementById('sHt');
const volWater=(E,dT)=>E*3600/(CP*dT);
const volIce=(E,pk)=>E*3600/(HFUS*pk);
let volChart=new Chart(document.getElementById('volChart'),{
  data:{datasets:[
    {type:'line',label:'Chilled water (sensible)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Ice (latent)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.14)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your store',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:400,title:{display:true,text:'Stored cooling capacity (MWh)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Tank volume (m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} m³ for ${fmt0(c.parsed.x)} MWh`}}}}
});
function updVol(){
  const E=+sE.value,dT=+sD.value,pk=+sP.value/100,h=+sHt.value;
  document.getElementById('vE').textContent=E+' MWh';
  document.getElementById('vD').textContent=fmt1(dT)+' K';
  document.getElementById('vP').textContent=fmt0(pk*100)+' %';
  document.getElementById('vHt').textContent=fmt1(h)+' m';
  const xs=[];for(let x=5;x<=400;x+=5)xs.push(x);
  volChart.data.datasets[0].data=xs.map(x=>({x:x,y:+volWater(x,dT).toFixed(0)}));
  volChart.data.datasets[1].data=xs.map(x=>({x:x,y:+volIce(x,pk).toFixed(0)}));
  const Vw=volWater(E,dT), Vi=volIce(E,pk);
  volChart.data.datasets[2].data=[{x:E,y:+Vw.toFixed(0)}];
  volChart.update('none');
  document.getElementById('rVw').innerHTML=fmt0(Vw)+' <small>m³</small>';
  document.getElementById('rVi').innerHTML=fmt0(Vi)+' <small>m³</small>';
  document.getElementById('rRt').innerHTML=fmt1(Vw/Vi)+'<small>×</small>';
  document.getElementById('rFp').innerHTML=fmt0(Vi/h)+' <small>m²</small>';
  document.getElementById('rFw').innerHTML=fmt0(Vw/h)+' <small>m²</small>';
}
[sE,sD,sP,sHt].forEach(s=>s.addEventListener('input',updVol));updVol();

/* ---------- CHART 2 : peak shaving ---------- */
const sL=document.getElementById('sL'),sLf=document.getElementById('sLf'),
      sOp=document.getElementById('sOp'),sCp=document.getElementById('sCp');
let peakChart=new Chart(document.getElementById('peakChart'),{
  data:{datasets:[
    {type:'line',label:'Chiller capacity with TES (MW)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Storage required (MWh)',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your plant',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:35,max:90,title:{display:true,text:'Daily load factor (%)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Chiller capacity (MW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Storage (MWh)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updPeak(){
  const L=+sL.value,lf=+sLf.value/100,op=+sOp.value,cp=+sCp.value/100;
  document.getElementById('vL').textContent=L+' MW';
  document.getElementById('vLf').textContent=fmt0(lf*100)+' %';
  document.getElementById('vOp').textContent=op+' h';
  document.getElementById('vCp').textContent=fmt0(cp*100)+' %';
  const xs=[];for(let x=35;x<=90;x+=1)xs.push(x);
  peakChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(L*x/100).toFixed(2)}));
  peakChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(L*(1-x/100)*op).toFixed(1)}));
  const ch=L*lf, st=L*(1-lf)*op;
  peakChart.data.datasets[2].data=[{x:lf*100,y:+ch.toFixed(2)}];
  peakChart.update('none');
  // extra energy: the stored share is produced at a worse COP
  const share=(1-lf)*op/24/ (lf + (1-lf)*op/24) ;
  const extra=100*((1-lf)*op/(lf*24))*(1/(1-cp)-1);
  document.getElementById('rCh').innerHTML=fmt0(ch)+' <small>MW</small>';
  document.getElementById('rCs').innerHTML=fmt0(100*(1-lf))+' <small>%</small>';
  document.getElementById('rSt').innerHTML=fmt0(st)+' <small>MWh</small>';
  document.getElementById('rIv').innerHTML=fmt0(volIce(st,0.9))+' <small>m³</small>';
  document.getElementById('rEx').innerHTML='+'+fmt0(extra)+' <small>%</small>';
}
[sL,sLf,sOp,sCp].forEach(s=>s.addEventListener('input',updPeak));updPeak();

/* ---------- CHART 3 : economics ---------- */
const sSh=document.getElementById('sSh'),sOn=document.getElementById('sOn'),
      sOf=document.getElementById('sOf'),sDy=document.getElementById('sDy');
const COP_PEN=0.28, COP_BASE=5.5;
let econChart=new Chart(document.getElementById('econChart'),{
  data:{datasets:[
    {type:'line',label:'Net annual saving',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Gross arbitrage',data:[],borderColor:'#c0392b',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your scheme',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1,max:4,title:{display:true,text:'On-peak ÷ off-peak rate ratio',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',title:{display:true,text:'Annual saving (millions)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt2(c.parsed.y)} M at ratio ${fmt2(c.parsed.x)}`}}}}
});
function updEcon(){
  const sh=+sSh.value,on=+sOn.value,off=+sOf.value,dy=+sDy.value;
  document.getElementById('vSh').textContent=sh+' MWh';
  document.getElementById('vOn').textContent=fmt2(on);
  document.getElementById('vOf').textContent=fmt2(off);
  document.getElementById('vDy').textContent=dy;
  // electricity to make the shifted cooling, day vs ice COP
  const eDay=sh/COP_BASE, eIce=sh/(COP_BASE*(1-COP_PEN));
  const gross=r=>sh/COP_BASE*(off*r-off)*dy/1e6;
  const net=r=>(eDay*off*r - eIce*off)*dy/1e6*-1*-1;
  const xs=[];for(let r=1;r<=4;r+=0.05)xs.push(+r.toFixed(2));
  econChart.data.datasets[0].data=xs.map(r=>({x:r,y:+((eDay*(off*r)-eIce*off)*1000*dy/1e6).toFixed(3)}));
  econChart.data.datasets[1].data=xs.map(r=>({x:r,y:+((eDay*(off*r)-eDay*off)*1000*dy/1e6).toFixed(3)}));
  const ratio=on/off;
  const g=(eDay*on-eDay*off)*1000*dy/1e6, pen=(eIce-eDay)*off*1000*dy/1e6, n=g-pen;
  econChart.data.datasets[2].data=[{x:ratio,y:+n.toFixed(3)}];
  econChart.update('none');
  document.getElementById('rGa').innerHTML=fmt2(g)+' <small>M/yr</small>';
  document.getElementById('rPc').innerHTML=fmt2(pen)+' <small>M/yr</small>';
  document.getElementById('rNs').innerHTML=fmt2(n)+' <small>M/yr</small>';
  document.getElementById('rRr').innerHTML=fmt2(ratio)+'<small>×</small>';
  const v=document.getElementById('rVd');
  if(n<=0)          v.innerHTML='<span class="badge bad">tariff will not pay for it</span>';
  else if(ratio<1.4)v.innerHTML='<span class="badge warn">justify on capacity</span>';
  else              v.innerHTML='<span class="badge good">arbitrage works</span>';
}
[sSh,sOn,sOf,sDy].forEach(s=>s.addEventListener('input',updEcon));updEcon();

window.addEventListener('load',function(){try{volChart.resize();peakChart.resize();econChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='thermal-energy-storage-tall-buildings', cat='hvac', mins=15,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Thermal Energy Storage for Megatall Buildings: Ice vs Water, Peak Shaving &amp; the Tariff That Pays for It',
    reg_title='Thermal Energy Storage for Megatall Buildings: Ice vs Water, Peak Shaving & the Tariff That Pays for It',
    reg_tag='HVAC · Thermal Storage · Peak Shaving',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Thermal Energy Storage &middot; Ice Storage &middot; Peak Shaving',
    desc='Thermal energy storage for megatall buildings: why storage density decides the design before economics does, chilled water versus ice versus phase-change materials, partial storage peak shaving and the chiller capacity it saves, the honest energy penalty from ice-making COP, tariff arbitrage and when it stops paying, and the control sequences where storage projects actually fail — with three interactive charts and installation tricks.',
    og_desc='128 MWh is 13,757 m3 as chilled water and 1,538 m3 as ice. Storage in a tower is a density question before it is an economics question — and it buys capacity, not energy.',
    ld_desc='A design-perspective guide to thermal energy storage in megatall buildings: storage media and density, partial versus full storage, chiller capacity savings, the ice-making COP penalty, tariff arbitrage economics, control sequences and commissioning.',
    img_alt='Technical cutaway of a megatall tower basement showing large ice thermal storage tanks with internal coil bundles, connected by glycol pipework to low-temperature chillers and a plate heat exchanger serving the building chilled-water risers',
    en_tag='HVAC &amp; Cooling &middot; Thermal Storage &middot; Ice Storage &middot; Peak Shaving',
    en_title='Thermal Energy Storage for Megatall Buildings: Ice vs Water, Peak Shaving &amp; the Tariff That Pays for It',
    en_excerpt='Thermal storage is the only way to buy cooling at one time and use it at another &mdash; but in a tower a physical constraint settles the design before economics is discussed. Storing 128&nbsp;MWh as chilled water needs <strong>13,757&nbsp;m&sup3;</strong>, nearly fourteen thousand tonnes; as ice it is <strong>1,538&nbsp;m&sup3;</strong>. Partial storage cuts chiller capacity by 40&nbsp;%, the tariff arbitrage nets about 0.4&nbsp;M a year &mdash; and making ice costs about a quarter of your COP, so the plant uses 11&nbsp;% more energy. Storage buys capacity, not efficiency &mdash; with three interactive charts.',
    en_search='thermal energy storage TES cool storage ice storage chilled water storage stratified tank thermocline diffuser phase change material PCM encapsulated ice ice on coil internal melt ice harvesting tall buildings megatall peak shaving load shifting full storage partial storage load factor chiller capacity reduction plant room substation demand charge tariff arbitrage on-peak off-peak rate ratio COP penalty glycol low temperature chiller state of charge control sequence forecast based charging demand limiting commissioning charge discharge cycle ASHRAE 150 Guideline 4 structural load insulation vapour barrier condensation MEP building services HVAC',
    ar_title='التخزين الحراري للمباني فائقة الارتفاع: الثلج مقابل الماء وتقليص الذروة والتعرفة التي تدفع الثمن',
    ar_excerpt='التخزين الحراري هو الوسيلة الوحيدة لشراء التبريد في وقتٍ واستخدامه في وقتٍ آخر — لكن في الأبراج يحسم قيدٌ فيزيائي التصميم قبل مناقشة الاقتصاديات. تخزين ١٢٨ ميغاواط ساعة كماء مبرد يحتاج <strong>١٣٧٥٧ م٣</strong> أي قرابة أربعة عشر ألف طن، وكثلج يحتاج <strong>١٥٣٨ م٣</strong>. التخزين الجزئي يخفض سعة المبردات ٤٠٪، وفرق التعرفة يوفر أكثر من مليون سنويًا — وصناعة الثلج تكلّف نحو ربع معامل الأداء، فتستهلك المحطة ١١٪ طاقة أكثر. التخزين يشتري السعة لا الكفاءة — مع ثلاثة رسوم تفاعلية.',
    ar_search='thermal energy storage ice storage chilled water stratified tank PCM peak shaving load shifting partial storage COP penalty tariff arbitrage demand charge glycol state of charge ASHRAE 150 التخزين الحراري تخزين البرودة تخزين الثلج تخزين الماء المبرد الخزان الطبقي الحد الحراري الموزع مواد التغير الطوري الثلج المغلف الثلج على الملفات الذوبان الداخلي حصاد الثلج المباني الشاهقة المباني فائقة الارتفاع تقليص الذروة إزاحة الحمل التخزين الكامل التخزين الجزئي معامل الحمل تقليل سعة المبردات غرفة المعدات محطة التحويل رسوم الطلب فرق التعرفة تعرفة الذروة خارج الذروة نسبة الأسعار عقوبة معامل الأداء الجليكول المبردات منخفضة الحرارة حالة الشحن تسلسل التحكم الشحن حسب التنبؤ تحديد الطلب التشغيل والاختبار دورة الشحن والتفريغ الحمل الإنشائي العزل الحاجز البخاري التكثيف MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
