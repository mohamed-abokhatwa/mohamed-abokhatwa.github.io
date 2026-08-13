# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Water treatment is the last line item in the tender, the first thing value-engineered out, and the only system in the building whose neglect degrades <em>every other system simultaneously</em>. A millimetre of scale on a condenser tube is not a maintenance issue — it is a <strong>25&nbsp;% increase in chiller power</strong> for the same cooling, invisible on every gauge, arriving so slowly that nobody notices the building got worse. Meanwhile the corrosion nobody measured is taking wall thickness off risers that were designed to last sixty years and are buried in a core that will never be opened.</p>

<h2 id="three">1 · Three problems, one system</h2>
<ul class="clean">
  <li><strong>Scale.</strong> Calcium and magnesium salts precipitate on the hottest surfaces — condenser tubes, heat exchanger plates. Scale is an excellent insulator, and it lands exactly where heat transfer matters most.</li>
  <li><strong>Corrosion.</strong> Oxygen, dissolved solids, pH excursions and galvanic couples remove metal. In a closed chilled-water system the oxygen should be consumed early and the system should then be almost inert; in an open condenser system corrosion is continuous and must be inhibited chemically for the whole life of the plant.</li>
  <li><strong>Biofouling.</strong> Biofilm insulates like scale, shelters corrosion beneath it, and in an open cooling tower is a public-health matter — the Legionella control discussed in <a href="cooling-towers-heat-rejection-tall-buildings.html">cooling towers</a>. A biofilm a fraction of a millimetre thick has a thermal resistance comparable to several millimetres of scale.</li>
</ul>
<p>These interact. Scale shelters bacteria; biofilm creates the local chemistry that drives pitting; corrosion products become the suspended solids that foul the exchangers. Treating one and ignoring the others does not work, which is why a treatment programme is a system rather than a dosing pump.</p>

<h2 id="int-fouling">2 · Interactive: what fouling actually costs</h2>
<p>A fouling layer adds a thermal resistance in series with the tube wall. The temperature penalty it produces is simply that resistance multiplied by the heat flux, and the chiller pays for it in condensing temperature:</p>
<div class="eq">\[ \Delta T_{approach} \;=\; R_f \cdot \frac{q}{A}, \qquad R_f = \frac{t_{scale}}{k_{scale}} \]</div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Chiller power penalty vs scale thickness</div>
    <div class="fsub">R&#102; = t/k with k ≈ 2.0 W/m·K for calcium carbonate; approach penalty = R&#102; × heat flux; chiller power penalty taken at a rate per kelvin of condensing temperature. The dashed line is the ASHRAE design fouling allowance.</div>
  </div>
  <div class="chart-box"><canvas id="foulChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Scale thickness <span id="vT">0.50 mm</span></label>
      <input type="range" id="sT" min="0" max="2" value="0.5" step="0.01">
      <div class="hint">Deposit on the condenser tube. A visible film is already 0.1–0.3 mm.</div>
    </div>
    <div class="ctrl">
      <label>Scale conductivity k <span id="vK">2.0 W/m·K</span></label>
      <input type="range" id="sK" min="0.5" max="3" value="2" step="0.1">
      <div class="hint">Calcium carbonate ≈ 2.0–2.9; silica and biofilm far lower, so they hurt more per millimetre.</div>
    </div>
    <div class="ctrl">
      <label>Condenser heat flux <span id="vQ">20 kW/m²</span></label>
      <input type="range" id="sQ" min="8" max="40" value="20" step="1">
      <div class="hint">Heat transferred per square metre of tube. Higher flux means fouling hurts more.</div>
    </div>
    <div class="ctrl">
      <label>Chiller penalty rate <span id="vP">2.5 %/K</span></label>
      <input type="range" id="sP" min="1.5" max="4" value="2.5" step="0.1">
      <div class="hint">Compressor power increase per kelvin of raised condensing temperature.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Fouling resistance</div><div class="v" id="rRf">0.00025 <small>m²K/W</small></div></div>
    <div class="cell"><div class="k">Approach penalty</div><div class="v" id="rDt">5.0 <small>K</small></div></div>
    <div class="cell"><div class="k">Chiller power</div><div class="v" id="rPw">+12.5 <small>%</small></div></div>
    <div class="cell"><div class="k">On 1,200 kW</div><div class="v" id="rKw">150 <small>kW</small></div></div>
    <div class="cell"><div class="k">Condition</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">Half a millimetre of scale — a deposit you would describe as "a bit of a film" — raises the condensing approach by <strong>5&nbsp;K</strong> and the chiller's power by <strong>12.5&nbsp;%</strong>. On a 1,200&nbsp;kW compressor that is 150&nbsp;kW, continuously, for as long as the scale is there. Take it to a full millimetre and the penalty is 25&nbsp;%. Now compare that with the cost of a treatment programme, which is a rounding error beside it. Note the conductivity slider: <strong>silica scale and biofilm conduct far worse than calcium carbonate</strong>, so a thin biofilm can cost more than a much thicker layer of hard scale — which is why microbiological control is an energy measure and not only a health one.</p>

<h2 id="int-filtration">3 · Interactive: side-stream filtration</h2>
<p>Suspended solids — airborne dust scrubbed out by the cooling tower, corrosion products, biological debris — settle in low-velocity areas, foul exchangers and shelter bacteria from biocide. Filtering the whole flow is uneconomic; filtering a <strong>side stream</strong> continuously is not.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Side-stream filtration: turnover and filter size</div>
    <div class="fsub">Filter flow = a percentage of the main circulating flow. Turnover time = system volume ÷ filter flow — the time for a volume equal to the whole system to have passed through the filter once.</div>
  </div>
  <div class="chart-box"><canvas id="filtChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Main circulating flow <span id="vFm">200 L/s</span></label>
      <input type="range" id="sFm" min="20" max="800" value="200" step="10">
      <div class="hint">Condenser or chilled water circulation rate.</div>
    </div>
    <div class="ctrl">
      <label>Side-stream fraction <span id="vSs">5 %</span></label>
      <input type="range" id="sSs" min="1" max="15" value="5" step="1">
      <div class="hint">Typical practice is 3–10 %. Tower basins and dusty sites need the upper end.</div>
    </div>
    <div class="ctrl">
      <label>System volume <span id="vV">400 m³</span></label>
      <input type="range" id="sV" min="30" max="3000" value="400" step="10">
      <div class="hint">Total water in the circuit including tower basins and any storage.</div>
    </div>
    <div class="ctrl">
      <label>Filter cut point <span id="vC">10 µm</span></label>
      <input type="range" id="sC" min="1" max="100" value="10" step="1">
      <div class="hint">Sand filters ≈ 10–20 µm; centrifugal separators only ~40 µm and above.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Filter flow</div><div class="v" id="rFf">10.0 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Turnover time</div><div class="v" id="rTo">11.1 <small>h</small></div></div>
    <div class="cell"><div class="k">Turnovers per day</div><div class="v" id="rTd">2.2</div></div>
    <div class="cell"><div class="k">Filter pump power</div><div class="v" id="rFp">3.8 <small>kW</small></div></div>
    <div class="cell"><div class="k">Assessment</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rFv"></span></div></div>
  </div>
</div>
<p class="fig-note">A 5&nbsp;% side stream on a 200&nbsp;L/s condenser circuit is a <strong>10&nbsp;L/s filter</strong> turning the system over roughly <strong>twice a day</strong> — enough to hold suspended solids down and to keep biocide effective, for about 3.8&nbsp;kW. The cut point matters as much as the flow: a centrifugal separator removes sand and heavy grit but passes the fine particles that actually foul plates and shelter biofilm, so a separator is a pre-filter, not a filtration strategy. Take the suction from the point where solids collect — the <strong>tower basin sweep</strong> or the sump — rather than from a convenient tee on a clean main, which filters water that was already clean.</p>

<h2 id="int-corrosion">4 · Interactive: corrosion and asset life</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Wall loss and remaining life vs corrosion rate</div>
    <div class="fsub">Uniform corrosion at a constant rate. 1 mil per year (mpy) = 0.0254 mm/yr. Pitting is far more dangerous than uniform loss and is not represented here — a low average rate can still perforate a pipe.</div>
  </div>
  <div class="chart-box"><canvas id="corrChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Corrosion rate <span id="vCr">2.0 mpy</span></label>
      <input type="range" id="sCr" min="0.2" max="20" value="2" step="0.1">
      <div class="hint">Coupon-measured. Under 1 mpy excellent, 1–3 acceptable, over 5 a failing programme.</div>
    </div>
    <div class="ctrl">
      <label>Available wall <span id="vW">3.0 mm</span></label>
      <input type="range" id="sW" min="0.5" max="8" value="3" step="0.1">
      <div class="hint">Corrosion allowance before the pipe reaches its minimum thickness.</div>
    </div>
    <div class="ctrl">
      <label>Design life <span id="vDl">60 yr</span></label>
      <input type="range" id="sDl" min="20" max="80" value="60" step="5">
      <div class="hint">Intended service life of the pipework.</div>
    </div>
    <div class="ctrl">
      <label>Pitting factor <span id="vPf">4×</span></label>
      <input type="range" id="sPf" min="1" max="12" value="4" step="0.5">
      <div class="hint">Ratio of deepest pit to average loss. Under-deposit and microbiologically influenced corrosion push this high.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Uniform rate</div><div class="v" id="rMm">0.051 <small>mm/yr</small></div></div>
    <div class="cell"><div class="k">Life, uniform</div><div class="v" id="rLu">59 <small>yr</small></div></div>
    <div class="cell"><div class="k">Life with pitting</div><div class="v" id="rLp">15 <small>yr</small></div></div>
    <div class="cell"><div class="k">Loss by design life</div><div class="v" id="rLo">3.0 <small>mm</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rCv"></span></div></div>
  </div>
</div>
<p class="fig-note">At a respectable 2&nbsp;mpy the uniform wall loss uses the whole 3&nbsp;mm allowance in about <strong>59 years</strong> — apparently fine for a 60-year building. Apply a pitting factor of four, which is entirely normal under deposits or where microbiologically influenced corrosion is present, and the first perforation arrives in <strong>15 years</strong>. That gap is the reason coupon monitoring alone is not enough: an <em>average</em> rate says nothing about the deepest pit, and it is the deepest pit that floods the floor. Measure corrosion with coupons, but control it by removing what makes pits — oxygen, deposits and biofilm — rather than by watching a number.</p>

<h2 id="closed">5 · Closed systems: different problem, worse neglect</h2>
<p>Chilled-water and heating circuits are closed, so the received wisdom is that they need little attention. That is true only if they were commissioned properly and have stayed closed:</p>
<ul class="clean">
  <li><strong>Every make-up event is a fresh dose of oxygen.</strong> A closed system that is quietly topping up is not closed — it has a leak, and it is being continuously re-oxygenated. Meter the make-up and alarm on abnormal consumption; it is the single most useful instrument on a closed system and it costs almost nothing.</li>
  <li><strong>Pre-commission cleaning is not optional.</strong> New systems contain mill scale, flux, jointing compound, swarf and construction debris. Flushing, chemical cleaning and passivation to a stated standard, with a cleanliness acceptance test, is what determines whether the system spends its life clean or spends it fouling.</li>
  <li><strong>Dose the inhibitor and then prove it.</strong> Inhibitor depletes; test it at least twice a year and re-dose. A closed system dosed once at handover and never checked is an untreated system after five years.</li>
  <li><strong>Provide dosing pots, sample points and coupon stations</strong> on every closed circuit, positioned where someone can actually reach them. Their absence is why the testing never happens.</li>
  <li><strong>Watch dissimilar metals.</strong> Steel, copper, stainless and aluminium in one circuit is a galvanic problem that inhibitors must be selected to cover — aluminium in particular restricts the chemistry available.</li>
  <li><strong>Air separation and pressurisation are corrosion controls</strong>, not comfort items — see the point-of-no-pressure-change discussion in <a href="chilled-water-pumps-tall-buildings.html">chilled-water pumps</a>.</li>
</ul>

<h2 id="open">6 · Open systems: the chemistry that decides the water bill</h2>
<p>Cooling tower chemistry sets both the fouling risk and the water consumption, and the two pull in opposite directions. Running at higher <strong>cycles of concentration</strong> saves large volumes of water — the calculation in <a href="cooling-towers-heat-rejection-tall-buildings.html">cooling towers</a> — but concentrates the very ions that scale. What makes high cycles possible is the treatment programme:</p>
<ul class="clean">
  <li><strong>Scale inhibitors and dispersants</strong> that keep calcium in solution well past its natural saturation, monitored by a saturation index rather than by hardness alone.</li>
  <li><strong>Conductivity-controlled blowdown</strong>, so the cycles are actually held rather than assumed, with the conductivity probe cleaned and calibrated on a schedule.</li>
  <li><strong>Two alternating biocides</strong> — typically an oxidising and a non-oxidising — dosed proportionally to makeup rather than on a timer, to prevent resistant populations establishing.</li>
  <li><strong>Pre-treatment of the makeup</strong> where the source is hard or high in silica: softening or reverse osmosis on the makeup can raise achievable cycles dramatically and pay for itself in water alone, which in the Gulf is often the strongest argument available.</li>
  <li><strong>Automated monitoring with remote alarms</strong>, because the failure mode of a manual programme is a missed visit that nobody notices for a month.</li>
</ul>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Write pre-commission cleaning into the contract with an acceptance standard</strong> — a stated cleanliness level and a witnessed test, not "flush until clear".</li>
  <li><strong>Fit the sample points, coupon racks and dosing pots at construction.</strong> Retrofitting them into a live system is expensive and therefore never happens, which is why so many systems are unmonitorable.</li>
  <li><strong>Meter make-up water on every closed circuit</strong> and trend it on the BMS with an alarm. This single measure catches leaks, failed seals and open bypasses years before they become failures.</li>
  <li><strong>Do not leave a new system full and stagnant.</strong> A tower commissioned early and then left standing for eighteen months during fit-out will be biologically established before anyone occupies the building; either circulate and treat it or drain it.</li>
  <li><strong>Passivate new galvanised towers</strong> at controlled pH before normal operation, or white rust starts in the first weeks.</li>
  <li><strong>Take the side-stream suction from the dirt.</strong> Basin sweep piping or a sump draw-off, not a convenient tee.</li>
  <li><strong>Keep strainer differential pressure on the BMS</strong> — a rising strainer DP is the earliest and cheapest indication of a fouling problem anywhere in the circuit.</li>
  <li><strong>Trend the approach on every heat exchanger and condenser.</strong> Fouling is invisible on a temperature gauge but obvious in a widening approach, and it is the measurement that turns treatment from an act of faith into engineering.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Treat water treatment as an energy system</strong> — quantify the fouling penalty in kilowatts and put it in the business case.</li>
  <li><strong>Specify pre-commission cleaning and passivation</strong> to a standard with a witnessed acceptance test.</li>
  <li><strong>Design in the monitoring</strong> — sample points, coupon racks, dosing pots, make-up meters, strainer DP, approach trending.</li>
  <li><strong>Size side-stream filtration at 3–10&nbsp;%</strong> with a real cut point, drawn from where solids collect.</li>
  <li><strong>Set the cycles of concentration from the makeup chemistry</strong>, and evaluate makeup pre-treatment against the water saving.</li>
  <li><strong>Automate dosing and blowdown</strong> with remote monitoring and alarms.</li>
  <li><strong>Check the metallurgy</strong> for galvanic couples and select inhibitors accordingly.</li>
  <li><strong>Protect closed systems from oxygen</strong> — leak-free, correctly pressurised, air-separated, make-up metered.</li>
  <li><strong>Hand over a water safety and treatment plan</strong> with named responsibility, test frequencies and action limits.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Water treatment is not a maintenance contract, it is an <strong>energy and asset-life system</strong>: half a millimetre of scale costs <strong>12.5&nbsp;% of your chiller power</strong> continuously and a full millimetre costs 25&nbsp;%, while a pitting factor of four turns a comfortable 59-year corrosion allowance into a 15-year one. Everything that makes it work has to be designed in rather than bolted on — sample points, coupon racks, dosing pots, a metered make-up on every closed circuit, side-stream filtration drawn from where the dirt actually is, and <strong>trended approach temperatures</strong>, which are the only way anyone will ever notice that the building is quietly getting worse.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Water Treatment chapter — scale, corrosion, biological control, cycles of concentration and side-stream filtration.</li>
  <li>ASHRAE Standard 188 and Guideline 12 — building water system risk management; HSE <em>ACOP L8</em> and HSG274 Part 1 for evaporative cooling systems.</li>
  <li>BSRIA <em>BG 29 Pre-Commission Cleaning of Pipework Systems</em> — cleaning stages, chemical cleaning, passivation and cleanliness acceptance criteria.</li>
  <li>NACE / AMPP standards on corrosion monitoring, coupon testing and microbiologically influenced corrosion.</li>
  <li>ASHRAE <em>Handbook — Fundamentals</em> and TEMA — fouling factors and their effect on heat exchanger performance.</li>
  <li>CIBSE <em>Guide B</em> and <em>Commissioning Code W</em> — water distribution systems, cleanliness and commissioning.</li>
  <li>Cooling Technology Institute guidance on tower water chemistry, blowdown control and basin cleanliness.</li>
  <li>Saudi Building Code <em>SBC 501</em> and local regulations on cooling tower water, blowdown discharge and alternative makeup sources.</li>
</ol>

<div class="tags">#WaterTreatment #Scale #Corrosion #Biofouling #Legionella #FoulingFactor #ChillerEfficiency #CondenserApproach #SideStreamFiltration #CyclesOfConcentration #Blowdown #Inhibitor #Biocide #PreCommissionCleaning #BSRIABG29 #Passivation #WhiteRust #Coupons #Pitting #MIC #ClosedSystems #MakeUpMetering #ApproachTrending #TallBuildings #MegatallBuildings #ASHRAE188 #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const fmt5=v=>v.toFixed(5);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};

/* ---------- CHART 1 : fouling penalty ---------- */
const sT=document.getElementById('sT'),sK=document.getElementById('sK'),
      sQ=document.getElementById('sQ'),sP=document.getElementById('sP');
const ASHRAE_RF=0.000044;
let foulChart=new Chart(document.getElementById('foulChart'),{
  data:{datasets:[
    {type:'line',label:'Chiller power penalty (%)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'scatter',label:'Your condition',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0,max:2,title:{display:true,text:'Scale thickness on the tube (mm)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Chiller power penalty (%)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`+${fmt1(c.parsed.y)} % at ${fmt2(c.parsed.x)} mm`}},
      annotation:{annotations:{
        des:{type:'line',scaleID:'x',xScaleID:'x',value:0.088,borderColor:'#1e8449',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'ASHRAE design allowance',position:'end',font:{size:10,family:'DM Sans'},color:'#1e8449',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updFoul(){
  const t=+sT.value,k=+sK.value,q=+sQ.value*1000,p=+sP.value;
  document.getElementById('vT').textContent=fmt2(t)+' mm';
  document.getElementById('vK').textContent=fmt1(k)+' W/m·K';
  document.getElementById('vQ').textContent=fmt0(q/1000)+' kW/m²';
  document.getElementById('vP').textContent=fmt1(p)+' %/K';
  const rf=x=>x/1000/k;
  const pen=x=>rf(x)*q*p;
  const xs=[];for(let x=0;x<=2;x+=0.02)xs.push(+x.toFixed(2));
  foulChart.data.datasets[0].data=xs.map(x=>({x:x,y:+pen(x).toFixed(2)}));
  foulChart.data.datasets[1].data=[{x:t,y:+pen(t).toFixed(2)}];
  foulChart.options.plugins.annotation.annotations.des.value=ASHRAE_RF*k*1000;
  foulChart.update('none');
  document.getElementById('rRf').innerHTML=fmt5(rf(t))+' <small>m²K/W</small>';
  document.getElementById('rDt').innerHTML=fmt1(rf(t)*q)+' <small>K</small>';
  document.getElementById('rPw').innerHTML='+'+fmt1(pen(t))+' <small>%</small>';
  document.getElementById('rKw').innerHTML=fmt0(1200*pen(t)/100)+' <small>kW</small>';
  const v=document.getElementById('rVd');
  if(rf(t)<=ASHRAE_RF)   v.innerHTML='<span class="badge good">within design allowance</span>';
  else if(pen(t)<10)     v.innerHTML='<span class="badge warn">clean it</span>';
  else                   v.innerHTML='<span class="badge bad">costing serious energy</span>';
}
[sT,sK,sQ,sP].forEach(s=>s.addEventListener('input',updFoul));updFoul();

/* ---------- CHART 2 : side-stream filtration ---------- */
const sFm=document.getElementById('sFm'),sSs=document.getElementById('sSs'),
      sV=document.getElementById('sV'),sC=document.getElementById('sC');
let filtChart=new Chart(document.getElementById('filtChart'),{
  data:{datasets:[
    {type:'line',label:'Turnover time (h)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Filter flow (L/s)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your system',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1,max:15,title:{display:true,text:'Side-stream fraction (% of main flow)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Turnover time (hours)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Filter flow (L/s)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updFilt(){
  const Fm=+sFm.value,ss=+sSs.value,V=+sV.value,cut=+sC.value;
  document.getElementById('vFm').textContent=Fm+' L/s';
  document.getElementById('vSs').textContent=ss+' %';
  document.getElementById('vV').textContent=V+' m³';
  document.getElementById('vC').textContent=cut+' µm';
  const ff=x=>Fm*x/100;
  const to=x=>V*1000/ff(x)/3600;
  const xs=[];for(let x=1;x<=15;x+=0.25)xs.push(+x.toFixed(2));
  filtChart.data.datasets[0].data=xs.map(x=>({x:x,y:+to(x).toFixed(2)}));
  filtChart.data.datasets[1].data=xs.map(x=>({x:x,y:+ff(x).toFixed(2)}));
  filtChart.data.datasets[2].data=[{x:ss,y:+to(ss).toFixed(2)}];
  filtChart.update('none');
  const f=ff(ss), T=to(ss);
  document.getElementById('rFf').innerHTML=fmt1(f)+' <small>L/s</small>';
  document.getElementById('rTo').innerHTML=fmt1(T)+' <small>h</small>';
  document.getElementById('rTd').innerHTML=fmt1(24/T);
  document.getElementById('rFp').innerHTML=fmt1(f*25/(102*0.65))+' <small>kW</small>';
  const v=document.getElementById('rFv');
  if(cut>25)        v.innerHTML='<span class="badge warn">separator only — fines pass</span>';
  else if(24/T<1)   v.innerHTML='<span class="badge warn">slow turnover</span>';
  else              v.innerHTML='<span class="badge good">effective</span>';
}
[sFm,sSs,sV,sC].forEach(s=>s.addEventListener('input',updFilt));updFilt();

/* ---------- CHART 3 : corrosion ---------- */
const sCr=document.getElementById('sCr'),sW=document.getElementById('sW'),
      sDl=document.getElementById('sDl'),sPf=document.getElementById('sPf');
const MPY=0.0254;
let corrChart=new Chart(document.getElementById('corrChart'),{
  data:{datasets:[
    {type:'line',label:'Life, uniform corrosion',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Life with pitting',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'Your system',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0.2,max:20,title:{display:true,text:'Corrosion rate (mils per year)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'logarithmic',title:{display:true,text:'Years to lose the corrosion allowance',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} yr at ${fmt1(c.parsed.x)} mpy`}},
      annotation:{annotations:{
        dl:{type:'line',scaleID:'y',yScaleID:'y',value:60,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'design life',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updCorr(){
  const cr=+sCr.value,w=+sW.value,dl=+sDl.value,pf=+sPf.value;
  document.getElementById('vCr').textContent=fmt1(cr)+' mpy';
  document.getElementById('vW').textContent=fmt1(w)+' mm';
  document.getElementById('vDl').textContent=dl+' yr';
  document.getElementById('vPf').textContent=fmt1(pf)+'×';
  const lifeU=x=>w/(x*MPY);
  const lifeP=x=>w/(x*MPY*pf);
  const xs=[];for(let x=0.2;x<=20;x+=0.2)xs.push(+x.toFixed(1));
  corrChart.data.datasets[0].data=xs.map(x=>({x:x,y:+lifeU(x).toFixed(1)}));
  corrChart.data.datasets[1].data=xs.map(x=>({x:x,y:+lifeP(x).toFixed(1)}));
  corrChart.data.datasets[2].data=[{x:cr,y:+lifeP(cr).toFixed(1)}];
  corrChart.options.plugins.annotation.annotations.dl.value=dl;
  corrChart.update('none');
  document.getElementById('rMm').innerHTML=fmt3(cr*MPY)+' <small>mm/yr</small>';
  document.getElementById('rLu').innerHTML=fmt0(lifeU(cr))+' <small>yr</small>';
  document.getElementById('rLp').innerHTML=fmt0(lifeP(cr))+' <small>yr</small>';
  document.getElementById('rLo').innerHTML=fmt1(Math.min(w,cr*MPY*dl))+' <small>mm</small>';
  const v=document.getElementById('rCv');
  if(lifeP(cr)>=dl)      v.innerHTML='<span class="badge good">meets design life</span>';
  else if(lifeP(cr)>=dl/2)v.innerHTML='<span class="badge warn">short of design life</span>';
  else                   v.innerHTML='<span class="badge bad">premature failure likely</span>';
}
[sCr,sW,sDl,sPf].forEach(s=>s.addEventListener('input',updCorr));updCorr();

window.addEventListener('load',function(){try{foulChart.resize();filtChart.resize();corrChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='water-treatment-building-systems', cat='hvac', mins=15,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Water Treatment for Building HVAC Systems: What Fouling Really Costs, Filtration &amp; Corrosion Life',
    reg_title='Water Treatment for Building HVAC Systems: What Fouling Really Costs, Filtration & Corrosion Life',
    reg_tag='HVAC · Water Treatment · Fouling',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Water Treatment &middot; Fouling &middot; Corrosion',
    desc='Water treatment for building HVAC systems from a design perspective: the chiller power penalty from scale and biofilm, side-stream filtration sizing and turnover, corrosion rates, pitting factors and real asset life, closed-system oxygen control and make-up metering, open-system chemistry and cycles of concentration, and the monitoring that has to be designed in rather than bolted on — with three interactive charts and installation tricks.',
    og_desc='Half a millimetre of scale costs 12.5 percent of your chiller power, continuously. And a pitting factor of four turns a comfortable 59-year corrosion allowance into a 15-year one.',
    ld_desc='A design-perspective guide to water treatment in building HVAC systems: fouling resistance and its chiller power penalty, side-stream filtration, corrosion rates and pitting, closed-system oxygen and make-up control, cooling tower chemistry and cycles of concentration, and designed-in monitoring.',
    img_alt='Technical cutaway of a chiller plant room water treatment installation showing dosing pots and chemical dosing pumps, a side-stream sand filter with its own pump, coupon and sample stations on the pipework, and a condenser tube section revealing scale build-up',
    en_tag='HVAC &amp; Cooling &middot; Water Treatment &middot; Fouling &middot; Corrosion',
    en_title='Water Treatment for Building HVAC Systems: What Fouling Really Costs, Filtration &amp; Corrosion Life',
    en_excerpt='Water treatment is the last line in the tender, the first thing value-engineered out, and the only system whose neglect degrades every other system at once. Half a millimetre of scale &mdash; what you would call &ldquo;a bit of a film&rdquo; &mdash; raises the condensing approach by 5&nbsp;K and the chiller&rsquo;s power by <strong>12.5&nbsp;%</strong>, continuously, invisibly. Meanwhile a pitting factor of four turns a comfortable 59-year corrosion allowance into <strong>15 years</strong>. Side-stream filtration, closed-system oxygen control, cooling tower chemistry, and the monitoring that must be designed in &mdash; with three interactive charts.',
    en_search='water treatment building HVAC chilled water condenser water scale corrosion biofouling biofilm Legionella fouling factor thermal resistance condenser approach chiller power penalty heat flux calcium carbonate silica scale side stream filtration sand filter centrifugal separator cut point turnover time basin sweep corrosion rate mils per year mpy coupon monitoring pitting factor microbiologically influenced corrosion MIC under deposit closed system oxygen make-up metering leak detection pre-commission cleaning BSRIA BG29 chemical cleaning passivation white rust galvanic dissimilar metals inhibitor depletion dosing pot sample point cycles of concentration blowdown conductivity control oxidising non-oxidising biocide makeup pre-treatment softening reverse osmosis strainer differential pressure approach trending ASHRAE 188 commissioning MEP building services',
    ar_title='معالجة المياه لأنظمة التكييف في المباني: ما يكلفه الاتساخ فعلًا والترشيح وعمر التآكل',
    ar_excerpt='معالجة المياه هي آخر بند في المناقصة، وأول ما يُحذف عند خفض التكاليف، وهي النظام الوحيد الذي يؤدي إهماله إلى تدهور كل الأنظمة الأخرى في آنٍ واحد. نصف ملليمتر من الترسبات — ما قد تصفه بأنه «طبقة رقيقة» — يرفع فرق الاقتراب في المكثف ٥ درجات وقدرة المبرد <strong>١٢٫٥٪</strong>، باستمرار وبلا أن يلاحظه أحد. وفي الوقت نفسه، معامل تنقر مقداره أربعة يحوّل احتياطي تآكل يكفي ٥٩ عامًا إلى <strong>١٥ عامًا</strong>. مع الترشيح الجانبي والتحكم في الأكسجين وكيمياء أبراج التبريد — مع ثلاثة رسوم تفاعلية.',
    ar_search='water treatment HVAC scale corrosion biofouling fouling factor condenser approach chiller penalty side stream filtration coupon pitting MIC closed system make-up metering pre-commission cleaning BSRIA BG29 passivation cycles of concentration blowdown biocide معالجة المياه أنظمة التكييف المياه المبردة مياه المكثف الترسبات التآكل الاتساخ الحيوي الأغشية الحيوية الليجيونيلا معامل الاتساخ المقاومة الحرارية فرق الاقتراب عقوبة قدرة المبرد الفيض الحراري كربونات الكالسيوم ترسبات السيليكا الترشيح الجانبي المرشح الرملي الفاصل الطرد المركزي حجم الاحتجاز زمن الدوران كنس حوض البرج معدل التآكل الملي في السنة كوبونات المراقبة معامل التنقر التآكل الميكروبي التآكل تحت الرواسب النظام المغلق الأكسجين عداد مياه التعويض كشف التسرب التنظيف قبل التشغيل التنظيف الكيميائي التخميل الصدأ الأبيض التآكل الجلفاني المعادن المختلفة استنفاد المثبط وعاء الجرعات نقطة أخذ العينات دورات التركيز التصريف التحكم في التوصيلية المبيدات المؤكسدة وغير المؤكسدة معالجة مياه التعويض التليين التناضح العكسي فرق ضغط المصفاة تتبع فرق الاقتراب MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
