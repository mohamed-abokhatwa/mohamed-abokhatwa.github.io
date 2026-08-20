# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Water reuse in a tower is usually presented as a sustainability gesture and designed as an afterthought, which is why so many systems end up either starved or overflowing. It is actually a <strong>matching problem</strong>: greywater from showers, basins and laundry is roughly <strong>twice</strong> the volume that toilet flushing can absorb, so a scheme designed to flush WCs throws half its source away — while the cooling towers next door are drinking <strong>1,800&nbsp;m³ a day</strong> that the same greywater could only cover 13&nbsp;% of. Get the source and the sink matched and reuse is one of the strongest business cases in a Gulf tower. Get them mismatched and you have built a treatment plant that spends its life bypassing to drain.</p>

<h2 id="balance">1 · Start with the water balance, not the technology</h2>
<p>Every reuse scheme is defined by three quantities, and the design is simply the smallest of them:</p>
<ul class="clean">
  <li><strong>What is available.</strong> Greywater — showers, baths, basins, laundry — is typically <strong>50–55&nbsp;%</strong> of indoor demand. Kitchen waste is usually excluded as it is heavily loaded with fats and food solids and belongs with blackwater.</li>
  <li><strong>What can use it.</strong> WC flushing is around <strong>28&nbsp;%</strong> of indoor demand. Irrigation is seasonal and often small on a tower site. <strong>Cooling tower makeup</strong> is in a different league entirely and is the sink that changes the arithmetic.</li>
  <li><strong>When each happens.</strong> Greywater arrives in a morning and evening peak; flushing follows occupancy; cooling tower makeup peaks in the afternoon and runs all night in summer. The mismatch in <em>time</em> is what sizes the storage.</li>
</ul>
<p>Two other sources are usually forgotten and are worth more than they look in this climate: <strong>air-handling condensate</strong>, which in a humid Gulf summer can be substantial and is nearly distilled water, and <strong>groundwater from permanent dewatering</strong>, covered in <a href="basement-dewatering-drainage-tall-buildings.html">deep basement dewatering</a>, which in a permeable site can exceed every other source combined.</p>

<h2 id="int-balance">2 · Interactive: source, sink and the match between them</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Greywater available against the demands that can use it</div>
    <div class="fsub">Indoor demand from population and per-capita consumption, split by end use. Cooling tower makeup at 2.0 m³/h per MW of heat rejection — 1.5 of evaporation plus blowdown at four cycles of concentration, the same basis as the <a href="cooling-towers-heat-rejection-tall-buildings.html">cooling tower water balance</a>.</div>
  </div>
  <div class="chart-box"><canvas id="balChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Population <span id="vP">2000</span></label>
      <input type="range" id="sP" min="200" max="10000" value="2000" step="100">
      <div class="hint">Equivalent resident population of the tower.</div>
    </div>
    <div class="ctrl">
      <label>Per-capita demand <span id="vD">220 L/p·d</span></label>
      <input type="range" id="sD" min="80" max="400" value="220" step="10">
      <div class="hint">Gulf residential runs high; offices and hotels differ markedly.</div>
    </div>
    <div class="ctrl">
      <label>Greywater fraction <span id="vG">54 %</span></label>
      <input type="range" id="sG" min="30" max="70" value="54" step="1">
      <div class="hint">Showers, baths, basins and laundry as a share of indoor demand.</div>
    </div>
    <div class="ctrl">
      <label>Cooling rejection <span id="vC">50 MW</span></label>
      <input type="range" id="sC" min="0" max="120" value="50" step="5">
      <div class="hint">Set to zero for an air-cooled or district-cooled tower with no makeup demand.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Indoor demand</div><div class="v" id="rDm">440 <small>m³/d</small></div></div>
    <div class="cell"><div class="k">Greywater available</div><div class="v" id="rGw">238 <small>m³/d</small></div></div>
    <div class="cell"><div class="k">WC flushing demand</div><div class="v" id="rWc">123 <small>m³/d</small></div></div>
    <div class="cell"><div class="k">Tower makeup</div><div class="v" id="rTm">2,400 <small>m³/d</small></div></div>
    <div class="cell"><div class="k">Match</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rMv"></span></div></div>
  </div>
</div>
<p class="fig-note">A 2,000-person tower produces <strong>238&nbsp;m³/d</strong> of greywater against a WC flushing demand of only <strong>123&nbsp;m³/d</strong> — so a flush-only scheme discards nearly half its source, and the treatment plant is sized by the <em>sink</em>, not the source. Now bring the cooling plant in: 50&nbsp;MW of rejection needs <strong>2,400&nbsp;m³/d</strong> of makeup, which the greywater covers only 10&nbsp;% of. That is the design conclusion in both directions: <strong>in a water-cooled tower the sink is effectively unlimited</strong>, so collect every drop you can and treat to the quality the towers need; in a district-cooled or air-cooled tower the sink is small, so size on flushing plus irrigation and do not over-collect. Note also that greywater into cooling towers demands a higher treatment standard than flushing — you are creating an aerosol.</p>

<h2 id="quality">3 · Treatment: to what standard, and why that decides everything</h2>
<p>Reuse standards differ sharply by end use, and the required quality drives the entire plant selection:</p>
<ul class="clean">
  <li><strong>Irrigation, sub-surface.</strong> The least demanding. Screening, biological treatment and disinfection are typically sufficient.</li>
  <li><strong>WC flushing.</strong> Human contact is credible, so turbidity, BOD and residual disinfectant limits tighten, and colour and odour become a user-acceptance issue as much as a health one. A membrane bioreactor (MBR) is the usual answer because it produces a consistent, low-turbidity effluent in a small footprint.</li>
  <li><strong>Cooling tower makeup.</strong> The most demanding, and the one most often underestimated: the tower creates a breathable aerosol, so microbiological control is paramount, and the water chemistry must also suit the treatment programme — nutrients such as phosphorus and nitrogen left in reclaimed water feed biofilm and directly undermine the Legionella control discussed in <a href="cooling-towers-heat-rejection-tall-buildings.html">cooling towers</a>.</li>
  <li><strong>Never for potable use</strong>, and physically impossible to cross-connect: separate pipework, distinct colour coding and marking, no shared valves or hose points, and backflow protection at every interface.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Treatment plant and storage sizing</div>
    <div class="fsub">Bioreactor volume from flow and hydraulic retention time; balance storage sized to bridge the mismatch between the collection profile and the reuse profile; treated storage sized on the reuse buffer.</div>
  </div>
  <div class="chart-box"><canvas id="plantChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Design flow <span id="vQ">238 m³/d</span></label>
      <input type="range" id="sQ" min="20" max="1500" value="238" step="2">
      <div class="hint">The smaller of what you can collect and what you can use.</div>
    </div>
    <div class="ctrl">
      <label>Hydraulic retention time <span id="vH">8 h</span></label>
      <input type="range" id="sH" min="4" max="16" value="8" step="0.5">
      <div class="hint">Bioreactor HRT. MBRs run shorter than conventional activated sludge.</div>
    </div>
    <div class="ctrl">
      <label>Raw balance storage <span id="vB">6 h</span></label>
      <input type="range" id="sB" min="2" max="24" value="6" step="1">
      <div class="hint">Buffers the morning and evening greywater peaks into a steady feed.</div>
    </div>
    <div class="ctrl">
      <label>Treated storage <span id="vT">12 h</span></label>
      <input type="range" id="sT" min="4" max="48" value="12" step="1">
      <div class="hint">Buffers treated water against the reuse demand profile.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Bioreactor</div><div class="v" id="rBio">79 <small>m³</small></div></div>
    <div class="cell"><div class="k">Raw balance tank</div><div class="v" id="rRaw">60 <small>m³</small></div></div>
    <div class="cell"><div class="k">Treated tank</div><div class="v" id="rTre">119 <small>m³</small></div></div>
    <div class="cell"><div class="k">Total wet volume</div><div class="v" id="rTot">258 <small>m³</small></div></div>
    <div class="cell"><div class="k">Plant footprint</div><div class="v" id="rFp">86 <small>m²</small></div></div>
  </div>
</div>
<p class="fig-note">A 238&nbsp;m³/d plant at an 8-hour retention time is a <strong>79&nbsp;m³ bioreactor</strong>, and with raw and treated buffers the total wet volume is around <strong>258&nbsp;m³</strong> — roughly 86&nbsp;m² of plant room at 3&nbsp;m depth, plus the membranes, blowers, dosing and controls. That is a real basement room that must be found early, ventilated, drained, acoustically treated and given odour control, and it needs a maintenance route for membrane replacement. The tank sizes are dominated by the <em>buffers</em>, not the reactor — which is the practical point: <strong>storage is what makes the profiles match</strong>, and skimping on it produces a plant that alternately starves and overflows.</p>

<h2 id="int-econ">4 · Interactive: does it actually pay?</h2>
<p>Reuse has a real operating cost — energy for aeration and membranes, membrane replacement, chemicals and skilled attendance — and a scheme justified on the water tariff alone can be a net loss if that cost is ignored.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Simple payback on a greywater scheme</div>
    <div class="fsub">Net saving = reused volume × (water tariff + avoided sewerage charge − treatment operating cost). Capital scaled per m³/day of installed capacity.</div>
  </div>
  <div class="chart-box"><canvas id="econChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Reused volume <span id="vRv">238 m³/d</span></label>
      <input type="range" id="sRv" min="20" max="1500" value="238" step="2">
      <div class="hint">Volume actually displaced, not the volume collected.</div>
    </div>
    <div class="ctrl">
      <label>Water + sewerage tariff <span id="vTa">9.0 /m³</span></label>
      <input type="range" id="sTa" min="1" max="30" value="9" step="0.5">
      <div class="hint">Potable tariff plus any avoided discharge charge, in your currency.</div>
    </div>
    <div class="ctrl">
      <label>Treatment operating cost <span id="vOp">3.0 /m³</span></label>
      <input type="range" id="sOp" min="0.5" max="10" value="3" step="0.1">
      <div class="hint">Energy, membranes, chemicals and labour. MBRs are not cheap to run.</div>
    </div>
    <div class="ctrl">
      <label>Capital per m³/day <span id="vCx">4500</span></label>
      <input type="range" id="sCx" min="1000" max="12000" value="4500" step="100">
      <div class="hint">Installed cost including tanks, plant room fit-out and dual pipework.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Capital cost</div><div class="v" id="rCap">1.07 <small>M</small></div></div>
    <div class="cell"><div class="k">Net saving</div><div class="v" id="rNet">0.52 <small>M/yr</small></div></div>
    <div class="cell"><div class="k">Simple payback</div><div class="v" id="rPb">2.1 <small>yr</small></div></div>
    <div class="cell"><div class="k">Water saved</div><div class="v" id="rWs">86,870 <small>m³/yr</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rEv"></span></div></div>
  </div>
</div>
<p class="fig-note">At a combined 9 per m³ tariff and a realistic 3 per m³ operating cost, a 238&nbsp;m³/d scheme nets about <strong>0.52&nbsp;M a year</strong> against roughly <strong>1.07&nbsp;M</strong> of capital — a simple payback near <strong>2.1 years</strong>, which is genuinely good. Now drag the operating cost up to 6 and the tariff down to 4: the net saving collapses and the payback disappears entirely. <strong>The result is almost entirely a function of the local tariff</strong>, and in jurisdictions where water is heavily subsidised a reuse scheme has to be justified on resource grounds, on a green rating credit, or on resilience — not on payback. Say which one, in the design report, rather than presenting a payback that depends on a subsidy decision.</p>

<h2 id="pipework">5 · Dual pipework — where these schemes actually fail</h2>
<ul class="clean">
  <li><strong>Cross-connection is the catastrophic failure mode</strong>, and it happens during fit-out and alteration rather than at construction. Distinct pipe colour and continuous marking, different connection types where practicable, no shared valves, hose points or drain-downs, and a documented commissioning cross-connection test.</li>
  <li><strong>Label the outlets.</strong> Non-potable outlets marked in the languages the building's users and maintainers actually read, with a permanent sign not a sticker.</li>
  <li><strong>Design the top-up carefully.</strong> The treated water tank needs a potable top-up for when the reuse plant is down — and that top-up is the single most likely cross-connection in the whole building. It must be through a <strong>type AA or AB air gap</strong>, never a check valve.</li>
  <li><strong>Give the plant a bypass to drain</strong> that is automatic on out-of-spec water quality, with the reuse system reverting to potable top-up. A plant that cannot fail safely will be switched off manually and left off.</li>
  <li><strong>Monitor quality continuously</strong> — turbidity and residual disinfectant as a minimum, interlocked to the bypass, trended and alarmed.</li>
  <li><strong>Remember the reuse riser has its own pressure zoning problem</strong>, exactly as in <a href="domestic-water-tall-buildings.html">domestic water supply</a> — a third set of zones, tanks and PRVs, which is a real cost the business case must carry.</li>
</ul>

<h2 id="install">6 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Find the plant room at concept.</strong> 250&nbsp;m³ of tankage plus plant is a basement room; it cannot be squeezed in later, and it needs drainage, ventilation, odour control, acoustic treatment and a membrane replacement route.</li>
  <li><strong>Separate greywater drainage from the start.</strong> Collecting greywater means a second drainage stack system from every bathroom — decided at the earliest layout stage, impossible to retrofit, and a real coordination load in the riser shafts.</li>
  <li><strong>Exclude kitchens deliberately and physically</strong>, and put a grease interceptor on anything that might connect anyway.</li>
  <li><strong>Design for the commissioning gap.</strong> A reuse plant with no flow during a long fit-out has no biology; plan seeding, a temporary feed, or a start-up sequence timed to occupancy.</li>
  <li><strong>Trend the reuse fraction from day one</strong> — the percentage of non-potable demand actually met. It is the one number that tells you whether the scheme is working, and it is almost never measured.</li>
  <li><strong>Meter everything</strong>: raw collected, treated produced, reused delivered, potable top-up and bypass to drain. Without all five the balance cannot be closed and faults hide.</li>
  <li><strong>Write the operator competence into the O&amp;M.</strong> An MBR is a small wastewater treatment works inside a luxury building; it needs someone who understands biology, not just a facilities technician with a checklist.</li>
</ul>

<h2 id="checklist">7 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Build the water balance first</strong> — source, sink and timing — and size on the smaller of source and sink.</li>
  <li><strong>Identify the real sink.</strong> With water-cooled plant it is effectively unlimited; without it, flushing and irrigation cap the scheme.</li>
  <li><strong>Set the treatment standard by end use</strong>, with cooling tower makeup the most demanding.</li>
  <li><strong>Include condensate and dewatering</strong> as sources — both are cleaner than greywater.</li>
  <li><strong>Size the buffers, not just the reactor</strong> — storage is what matches the profiles.</li>
  <li><strong>Cost it honestly</strong> with operating cost included, and state the real justification if the payback does not stand alone.</li>
  <li><strong>Design dual pipework against cross-connection</strong>, with an air-gapped potable top-up.</li>
  <li><strong>Provide automatic bypass on out-of-spec quality</strong>, interlocked to continuous monitoring.</li>
  <li><strong>Meter all five streams</strong> and trend the reuse fraction.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Water reuse is a <strong>matching problem, not a treatment problem</strong>: greywater is about twice the volume WC flushing can absorb, so a flush-only scheme discards half its source — while a 50&nbsp;MW cooling plant next door drinks <strong>1,800&nbsp;m³ a day</strong> that the same greywater covers only 13&nbsp;% of. Find the real sink first, size on the smaller of source and sink, and put the effort into <strong>storage</strong>, because the buffers are what make the profiles meet. Then treat the two things that actually kill these schemes: an <strong>air-gapped potable top-up</strong> so the top-up is not the cross-connection, and an <strong>automatic bypass on out-of-spec quality</strong> so the plant can fail safely instead of being switched off and left off.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>WHO <em>Guidelines for the Safe Use of Wastewater, Excreta and Greywater</em>, and <em>Water Safety in Buildings</em> — health-based targets for reuse applications.</li>
  <li>BS 8525 — <em>Greywater systems</em>: design, installation, water quality and maintenance; and BS 8515 for rainwater harvesting.</li>
  <li>NSF/ANSI 350 — onsite residential and commercial water reuse treatment systems; and the International Plumbing Code / Uniform Plumbing Code non-potable water provisions.</li>
  <li>ISO 30500 and ISO 16075 — non-sewered sanitation and guidelines for treated wastewater use for irrigation.</li>
  <li>Saudi regulations on treated sewage effluent reuse and the Saudi Building Code <em>SBC 701</em> plumbing provisions, including non-potable distribution and marking.</li>
  <li>Estidama Pearl, Mostadam and LEED water efficiency credits — the rating requirements that often drive these schemes.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Water Treatment chapter, and ASHRAE 188 — implications of reclaimed water for cooling tower chemistry and Legionella risk.</li>
  <li>AWWA M14 — <em>Backflow Prevention and Cross-Connection Control</em>, for the potable top-up and interface protection.</li>
</ol>

<div class="tags">#WaterReuse #Greywater #Recycling #TallBuildings #MegatallBuildings #WaterBalance #WCFlushing #Irrigation #CoolingTowerMakeup #Condensate #GroundwaterReuse #MBR #MembraneBioreactor #Disinfection #Turbidity #DualPipework #CrossConnection #AirGap #BackflowPrevention #NonPotable #BS8525 #NSF350 #Estidama #Mostadam #LEED #WaterScarcity #Metering #Commissioning #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const WC_FRAC=0.28, TOWER_M3_PER_MW_H=2.0;   // evaporation 1.5 + blowdown at 4 cycles of concentration

/* ---------- CHART 1 : water balance ---------- */
const sP=document.getElementById('sP'),sD=document.getElementById('sD'),
      sG=document.getElementById('sG'),sC=document.getElementById('sC');
let balChart=new Chart(document.getElementById('balChart'),{
  type:'bar',
  data:{labels:['Greywater\navailable','WC flushing\ndemand','Cooling tower\nmakeup'],
    datasets:[{label:'m³/day',data:[],backgroundColor:['#1b4f72','#1e8449','#c0392b'],borderColor:'#fff',borderWidth:1}]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,ticks:{font:{family:'DM Sans',size:11}}},
            y:{type:'logarithmic',title:{display:true,text:'Volume (m³/day, log scale)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{display:false},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} m³/d`}}}}
});
function updBal(){
  const P=+sP.value,D=+sD.value,G=+sG.value/100,C=+sC.value;
  document.getElementById('vP').textContent=P;
  document.getElementById('vD').textContent=D+' L/p·d';
  document.getElementById('vG').textContent=fmt0(G*100)+' %';
  document.getElementById('vC').textContent=C+' MW';
  const dem=P*D/1000, gw=dem*G, wc=dem*WC_FRAC, mk=TOWER_M3_PER_MW_H*C*24;
  balChart.data.datasets[0].data=[+gw.toFixed(1),+wc.toFixed(1),+Math.max(mk,0.1).toFixed(1)];
  balChart.update('none');
  document.getElementById('rDm').innerHTML=fmt0(dem)+' <small>m³/d</small>';
  document.getElementById('rGw').innerHTML=fmt0(gw)+' <small>m³/d</small>';
  document.getElementById('rWc').innerHTML=fmt0(wc)+' <small>m³/d</small>';
  document.getElementById('rTm').innerHTML=fmt0(mk)+' <small>m³/d</small>';
  const sink=wc+mk, v=document.getElementById('rMv');
  if(mk>gw*2)        v.innerHTML='<span class="badge good">sink unlimited — collect everything</span>';
  else if(sink>=gw)  v.innerHTML='<span class="badge good">source is the constraint</span>';
  else               v.innerHTML='<span class="badge warn">sink limits it — do not over-collect</span>';
}
[sP,sD,sG,sC].forEach(s=>s.addEventListener('input',updBal));updBal();

/* ---------- CHART 2 : plant sizing ---------- */
const sQ=document.getElementById('sQ'),sH=document.getElementById('sH'),
      sB=document.getElementById('sB'),sT=document.getElementById('sT');
let plantChart=new Chart(document.getElementById('plantChart'),{
  data:{datasets:[
    {type:'line',label:'Total wet volume (m³)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Bioreactor only (m³)',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your plant',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:20,max:1500,title:{display:true,text:'Design flow (m³/day)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Tank volume (m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} m³ at ${fmt0(c.parsed.x)} m³/d`}}}}
});
function updPlant(){
  const Q=+sQ.value,H=+sH.value,B=+sB.value,T=+sT.value;
  document.getElementById('vQ').textContent=Q+' m³/d';
  document.getElementById('vH').textContent=fmt1(H)+' h';
  document.getElementById('vB').textContent=B+' h';
  document.getElementById('vT').textContent=T+' h';
  const bio=q=>q*H/24, raw=q=>q*B/24, tre=q=>q*T/24;
  const tot=q=>bio(q)+raw(q)+tre(q);
  const xs=[];for(let x=20;x<=1500;x+=10)xs.push(x);
  plantChart.data.datasets[0].data=xs.map(x=>({x:x,y:+tot(x).toFixed(1)}));
  plantChart.data.datasets[1].data=xs.map(x=>({x:x,y:+bio(x).toFixed(1)}));
  plantChart.data.datasets[2].data=[{x:Q,y:+tot(Q).toFixed(1)}];
  plantChart.update('none');
  document.getElementById('rBio').innerHTML=fmt0(bio(Q))+' <small>m³</small>';
  document.getElementById('rRaw').innerHTML=fmt0(raw(Q))+' <small>m³</small>';
  document.getElementById('rTre').innerHTML=fmt0(tre(Q))+' <small>m³</small>';
  document.getElementById('rTot').innerHTML=fmt0(tot(Q))+' <small>m³</small>';
  document.getElementById('rFp').innerHTML=fmt0(tot(Q)/3)+' <small>m²</small>';
}
[sQ,sH,sB,sT].forEach(s=>s.addEventListener('input',updPlant));updPlant();

/* ---------- CHART 3 : economics ---------- */
const sRv=document.getElementById('sRv'),sTa=document.getElementById('sTa'),
      sOp=document.getElementById('sOp'),sCx=document.getElementById('sCx');
let econChart=new Chart(document.getElementById('econChart'),{
  data:{datasets:[
    {type:'line',label:'Simple payback (years)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your scheme',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1,max:30,title:{display:true,text:'Water + sewerage tariff (per m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,max:40,title:{display:true,text:'Simple payback (years)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} yr at ${fmt1(c.parsed.x)}/m³`}}}}
});
function updEcon(){
  const V=+sRv.value,T=+sTa.value,O=+sOp.value,C=+sCx.value;
  document.getElementById('vRv').textContent=V+' m³/d';
  document.getElementById('vTa').textContent=fmt1(T)+' /m³';
  document.getElementById('vOp').textContent=fmt1(O)+' /m³';
  document.getElementById('vCx').textContent=C;
  const cap=V*C;
  const net=t=>V*365*(t-O);
  const pb=t=>net(t)>0?cap/net(t):NaN;
  const xs=[];for(let t=1;t<=30;t+=0.25)xs.push(+t.toFixed(2));
  econChart.data.datasets[0].data=xs.map(t=>({x:t,y:(net(t)>0?+Math.min(pb(t),40).toFixed(2):null)}));
  econChart.data.datasets[1].data=(net(T)>0)?[{x:T,y:+Math.min(pb(T),40).toFixed(2)}]:[];
  econChart.update('none');
  document.getElementById('rCap').innerHTML=fmt2(cap/1e6)+' <small>M</small>';
  document.getElementById('rNet').innerHTML=fmt2(net(T)/1e6)+' <small>M/yr</small>';
  document.getElementById('rPb').innerHTML=(net(T)>0?fmt1(pb(T)):'—')+' <small>yr</small>';
  document.getElementById('rWs').innerHTML=fmt0(V*365)+' <small>m³/yr</small>';
  const v=document.getElementById('rEv');
  if(net(T)<=0)        v.innerHTML='<span class="badge bad">operating cost exceeds tariff</span>';
  else if(pb(T)<=5)    v.innerHTML='<span class="badge good">pays back on water alone</span>';
  else if(pb(T)<=15)   v.innerHTML='<span class="badge warn">marginal — justify on resource</span>';
  else                 v.innerHTML='<span class="badge bad">not a financial case</span>';
}
[sRv,sTa,sOp,sCx].forEach(s=>s.addEventListener('input',updEcon));updEcon();

window.addEventListener('load',function(){try{balChart.resize();plantChart.resize();econChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='greywater-reuse-tall-buildings', cat='plumbing', mins=14,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Greywater &amp; Water Reuse in Megatall Buildings: Matching Source to Sink, Treatment &amp; Dual Pipework',
    reg_title='Greywater & Water Reuse in Megatall Buildings: Matching Source to Sink, Treatment & Dual Pipework',
    reg_tag='Plumbing · Water Reuse · Greywater',
    breadcrumb='Plumbing &amp; Drainage',
    tag_line='Plumbing &middot; Water Reuse &middot; Greywater &middot; Megatall Buildings',
    desc='Greywater and water reuse in megatall buildings: why reuse is a matching problem rather than a treatment problem, the water balance between greywater available and the demands that can absorb it, cooling tower makeup as the sink that changes the arithmetic, treatment standards by end use, plant and storage sizing, honest economics including operating cost, and dual pipework designed against cross-connection — with three interactive charts.',
    og_desc='Greywater is about twice the volume WC flushing can absorb, so a flush-only scheme discards half its source — while a 50 MW cooling plant next door drinks 2,400 m3 a day the same greywater covers only 10 percent of.',
    ld_desc='A design-perspective guide to greywater and water reuse in megatall buildings: water balance and source-sink matching, treatment standards by end use, membrane bioreactor and storage sizing, economics including operating cost, and dual pipework and cross-connection control.',
    img_alt='Technical cutaway of a megatall tower water reuse system showing separate greywater drainage stacks from the bathrooms, a basement membrane bioreactor treatment plant with balance and treated water tanks, and a purple non-potable riser feeding WC flushing and cooling tower makeup',
    en_tag='Plumbing &amp; Drainage &middot; Water Reuse &middot; Greywater &middot; Megatall',
    en_title='Greywater &amp; Water Reuse in Megatall Buildings: Matching Source to Sink, Treatment &amp; Dual Pipework',
    en_excerpt='Water reuse is usually presented as a sustainability gesture and designed as an afterthought, which is why so many schemes end up starved or overflowing. It is actually a <strong>matching problem</strong>: greywater is about <em>twice</em> the volume WC flushing can absorb, so a flush-only scheme throws half its source away &mdash; while the cooling towers next door drink <strong>1,800&nbsp;m&sup3; a day</strong> that the same greywater covers only 13&nbsp;% of. Treatment standards by end use, plant and storage sizing, honest economics with operating cost included, and the dual pipework that these schemes actually fail on &mdash; with three interactive charts.',
    en_search='greywater water reuse recycling tall buildings megatall water balance source sink matching indoor demand per capita showers basins laundry WC flushing irrigation cooling tower makeup condensate recovery groundwater reuse dewatering treatment standard membrane bioreactor MBR turbidity BOD disinfection residual chlorine aerosol Legionella nutrients phosphorus biofilm balance tank treated storage hydraulic retention time plant footprint odour control dual pipework purple pipe cross connection colour coding marking potable top-up air gap type AA AB backflow prevention automatic bypass out of spec quality monitoring metering reuse fraction payback operating cost tariff subsidy Estidama Mostadam LEED BS 8525 NSF 350 WHO commissioning MEP building services',
    ar_title='إعادة استخدام المياه الرمادية في المباني فائقة الارتفاع: مطابقة المصدر بالمصرف والمعالجة والشبكة المزدوجة',
    ar_excerpt='غالبًا ما تُقدَّم إعادة استخدام المياه كبادرة استدامة وتُصمَّم لاحقًا، ولهذا ينتهي كثير من الأنظمة إمّا جائعًا أو فائضًا. وهي في الحقيقة <strong>مسألة مطابقة</strong>: المياه الرمادية تبلغ نحو <em>ضعف</em> ما يمكن أن تستوعبه صناديق الطرد، فالنظام المخصص للطرد وحده يهدر نصف مصدره — بينما أبراج التبريد المجاورة تشرب <strong>١٨٠٠ متر مكعب يوميًا</strong> لا تغطي منها المياه الرمادية سوى ١٣٪. مع معايير المعالجة حسب الاستخدام، وتحجيم المحطة والتخزين، والاقتصاديات الصادقة، والشبكة المزدوجة التي تفشل فيها هذه الأنظمة فعلًا — مع ثلاثة رسوم تفاعلية.',
    ar_search='greywater water reuse recycling water balance MBR membrane bioreactor dual pipework cross connection air gap backflow potable top-up cooling tower makeup condensate BS 8525 NSF 350 Estidama Mostadam المياه الرمادية إعادة استخدام المياه إعادة التدوير المباني الشاهقة المباني فائقة الارتفاع الميزان المائي مطابقة المصدر والمصرف الطلب الداخلي نصيب الفرد الأدشاش المغاسل الغسيل صناديق الطرد الري تعويض أبراج التبريد استرجاع المياه المكثفة إعادة استخدام المياه الجوفية نزح المياه معيار المعالجة المفاعل الحيوي الغشائي العكارة الأكسجين الحيوي المطلوب التعقيم الكلور المتبقي الرذاذ الليجيونيلا المغذيات الفوسفور الغشاء الحيوي خزان الموازنة خزان المياه المعالجة زمن المكوث الهيدروليكي مساحة المحطة التحكم في الروائح الشبكة المزدوجة الماسورة البنفسجية التوصيل المتقاطع الترميز اللوني التغذية التكميلية بالمياه الصالحة الفجوة الهوائية منع الارتداد التجاوز التلقائي مراقبة الجودة العدادات نسبة إعادة الاستخدام فترة الاسترداد تكلفة التشغيل التعرفة الدعم التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
