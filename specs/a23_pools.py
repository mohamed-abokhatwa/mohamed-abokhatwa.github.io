# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Every megatall tower has a pool, and increasingly it is on the roof — an infinity edge at three hundred metres with a view. That single architectural decision transforms an ordinary building service into one of the hardest loads in the building, because evaporation depends on <strong>air movement</strong>, and at 300&nbsp;m there is a great deal of it. The same 400&nbsp;m² of water that evaporates quietly indoors loses <strong>384&nbsp;kg an hour</strong> on an exposed rooftop in Gulf conditions — a <strong>262&nbsp;kW</strong> latent load and <strong>9&nbsp;m³ a day</strong> of makeup water, permanently, on the highest and least accessible part of the building.</p>

<h2 id="why">1 · Why a pool in a tower is different</h2>
<ul class="clean">
  <li><strong>Evaporation is wind-driven, and the wind is what changes with height.</strong> A rooftop pool sits in the boundary-layer profile described in <a href="outdoor-air-ventilation-tall-buildings.html">outdoor air and ventilation</a>, where the wind is several times the street-level speed.</li>
  <li><strong>The water is a structural load.</strong> A 400&nbsp;m² pool 1.6&nbsp;m deep is <strong>640 tonnes</strong> of water on the top of the tower, plus the tank, plus the dynamic sloshing load when the building sways.</li>
  <li><strong>The plant is far from the pool.</strong> Filtration, heating and dosing need a plant room; putting it at roof level costs prime area, and putting it lower means a very tall circulation loop with its own static pressure and its own hydraulic problems.</li>
  <li><strong>Everything is inaccessible.</strong> Chemical delivery, filter media replacement and backwash disposal all have to happen at the top of a 300&nbsp;m building, through the goods lift, forever.</li>
  <li><strong>The safety case is unforgiving.</strong> Recirculation and disinfection are public-health systems: a failure is an outbreak, not a comfort complaint.</li>
</ul>

<h2 id="int-evap">2 · Interactive: evaporation, and what the wind does to it</h2>
<p>Evaporation from a pool follows the vapour-pressure difference between the water surface and the air, enhanced by air movement<sup class="cite">[1]</sup>:</p>
<div class="eq">\[ \dot m = \frac{A}{Y}\,(p_w - p_a)\,(0.089 + 0.0782\,V) \]</div>
<p>with \(\dot m\) in kg/s, \(A\) the water surface area, \(Y\) the latent heat of vaporisation (≈2,454&nbsp;kJ/kg), \(p_w\) the saturation pressure at the water temperature, \(p_a\) the actual vapour pressure of the air, and \(V\) the air velocity over the surface. The velocity term is the one that matters here: going from a still indoor 0.1&nbsp;m/s to an exposed rooftop 3&nbsp;m/s multiplies the coefficient by <strong>more than three</strong>.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pool evaporation and latent load</div>
    <div class="fsub">ASHRAE evaporation correlation. Latent load = ṁ·Y; makeup water is the same mass flow. Air velocity is the value at the water surface, not the free-stream wind speed — a windbreak reduces it substantially.</div>
  </div>
  <div class="chart-box"><canvas id="evChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Water surface area <span id="vA">400 m²</span></label>
      <input type="range" id="sA" min="20" max="1200" value="400" step="10">
      <div class="hint">Free water surface, including any spa and reflecting pools on the same system.</div>
    </div>
    <div class="ctrl">
      <label>Water temperature <span id="vTw">30 °C</span></label>
      <input type="range" id="sTw" min="24" max="40" value="30" step="0.5">
      <div class="hint">Leisure pools 28–30 °C; spas 36–40 °C evaporate far harder.</div>
    </div>
    <div class="ctrl">
      <label>Air temperature <span id="vTa">40 °C</span></label>
      <input type="range" id="sTa" min="18" max="48" value="40" step="1">
      <div class="hint">Ambient at the pool deck.</div>
    </div>
    <div class="ctrl">
      <label>Relative humidity <span id="vRh">30 %</span></label>
      <input type="range" id="sRh" min="10" max="90" value="30" step="1">
      <div class="hint">Dry air evaporates far more. Coastal Jeddah is humid; Riyadh is not.</div>
    </div>
    <div class="ctrl">
      <label>Air velocity at the surface <span id="vV">3.0 m/s</span></label>
      <input type="range" id="sV" min="0.05" max="6" value="3" step="0.05">
      <div class="hint">Indoor still air ≈ 0.1; a screened terrace ≈ 1; an exposed roof at 300 m far more.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Evaporation</div><div class="v" id="rEv">384 <small>kg/h</small></div></div>
    <div class="cell"><div class="k">Latent load</div><div class="v" id="rLl">262 <small>kW</small></div></div>
    <div class="cell"><div class="k">Makeup water</div><div class="v" id="rMu">9.2 <small>m³/d</small></div></div>
    <div class="cell"><div class="k">If sheltered to 0.5 m/s</div><div class="v" id="rSh">104 <small>kW</small></div></div>
    <div class="cell"><div class="k">Exposure</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rEx"></span></div></div>
  </div>
</div>
<p class="fig-note">A 400&nbsp;m² rooftop pool in dry 40&nbsp;°C air at 3&nbsp;m/s evaporates <strong>384&nbsp;kg/h</strong> — a <strong>262&nbsp;kW</strong> load and <strong>9.2&nbsp;m³ a day</strong> of treated makeup water hauled to the top of the tower. Now drag the velocity down to 0.5&nbsp;m/s, which is what a properly designed <strong>windbreak or recessed pool surround</strong> achieves: the load falls to about <strong>104&nbsp;kW</strong>, a 60&nbsp;% reduction, for architecture rather than plant. That is the single highest-value intervention available, and it has to be argued at concept design because it is a form decision. A <strong>pool cover at night</strong> is the second: covering for eight hours cuts daily evaporation by roughly a third at no capital cost beyond the cover itself.</p>

<h2 id="int-turnover">3 · Interactive: turnover, filtration and the plant</h2>
<p>Water quality is maintained by continuously recirculating the whole volume through filtration and disinfection. The <strong>turnover period</strong> — the time to pass a volume equal to the pool through the plant — is set by code and by bather load, and it sizes everything downstream.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Circulation flow, filter area and pump duty</div>
    <div class="fsub">Flow = pool volume ÷ turnover period. Filter area = flow ÷ design filtration velocity. Pump duty from flow and the circuit head including filter, heater, strainer and any static lift to a remote plant room.</div>
  </div>
  <div class="chart-box"><canvas id="turnChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Pool volume <span id="vVo">640 m³</span></label>
      <input type="range" id="sVo" min="20" max="2000" value="640" step="10">
      <div class="hint">Surface area × average depth, plus balance tank.</div>
    </div>
    <div class="ctrl">
      <label>Turnover period <span id="vT">4 h</span></label>
      <input type="range" id="sT" min="0.5" max="10" value="4" step="0.5">
      <div class="hint">Public leisure pools 3–4 h; spas 10–20 min; private pools up to 8 h.</div>
    </div>
    <div class="ctrl">
      <label>Filtration velocity <span id="vFv">25 m/h</span></label>
      <input type="range" id="sFv" min="10" max="50" value="25" step="1">
      <div class="hint">Sand filters run 25–37 m/h. Lower velocity filters better and needs more area.</div>
    </div>
    <div class="ctrl">
      <label>Circuit head <span id="vHd">18 m</span></label>
      <input type="range" id="sHd" min="8" max="120" value="18" step="1">
      <div class="hint">Filter, heater, strainer and pipework, plus any lift to a plant room on another level.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Circulation flow</div><div class="v" id="rQ">160 <small>m³/h</small></div></div>
    <div class="cell"><div class="k">In L/s</div><div class="v" id="rLs">44 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Filter area</div><div class="v" id="rFa">6.4 <small>m²</small></div></div>
    <div class="cell"><div class="k">Pump shaft power</div><div class="v" id="rPw">11.2 <small>kW</small></div></div>
    <div class="cell"><div class="k">Backwash flow</div><div class="v" id="rBw">288 <small>m³/h</small></div></div>
  </div>
</div>
<p class="fig-note">A 640&nbsp;m³ pool on a four-hour turnover needs <strong>160&nbsp;m³/h — 44&nbsp;L/s</strong> circulating continuously, through <strong>6.4&nbsp;m²</strong> of filter, for about 11&nbsp;kW of pump power running 8,760 hours a year. Two design traps sit in the readouts. The <strong>backwash flow is far larger than the circulation flow</strong> — typically 45&nbsp;m/h against 25 — so the backwash pipework, the waste drain and the balance tank must be sized for it, not for normal operation. And note the head slider: if the plant room is on a different level from the pool, the circuit becomes a tall open loop, the pump has to lift the water, and the pump power multiplies. <strong>Put the plant room on the same level as the pool</strong> if the architecture allows it.</p>

<h2 id="water">4 · Water treatment, and why the balance tank matters</h2>
<ul class="clean">
  <li><strong>The balance tank is the system.</strong> It absorbs displaced water when bathers enter, receives the deck-level and infinity-edge overflow, provides the pump suction and takes the makeup. Undersize it and the pump loses suction, the edge stops flowing and the surface skimming fails. Size it for the displacement of the design bather load plus the surge volume of the overflow channel plus a working depth — never as a minimum sump.</li>
  <li><strong>Infinity edges multiply the balance duty.</strong> A weir edge is a continuous overflow, which is excellent for surface skimming and demands a much larger catchment channel, a larger balance tank and a larger circulation rate than a skimmer pool. It is an architectural feature with a real hydraulic consequence.</li>
  <li><strong>Disinfection is dual.</strong> A residual disinfectant (chlorine or bromine) throughout the water, plus supplementary treatment — commonly UV or ozone — to control chlorine-resistant organisms and to reduce combined chlorine. UV in particular reduces the chloramines responsible for the smell and eye irritation that people wrongly attribute to "too much chlorine".</li>
  <li><strong>Automate and monitor.</strong> Continuous pH and free-chlorine measurement with proportional dosing and an interlock that stops bathing on out-of-range readings. Manual dosing on a rooftop pool at 300&nbsp;m will not happen reliably.</li>
  <li><strong>Handle the chemicals safely.</strong> Segregated, ventilated, bunded chemical storage with incompatible chemicals separated, and a delivery route that does not pass through occupied space — a real constraint when the plant is on the roof.</li>
  <li><strong>Spas are a category of their own.</strong> High temperature, high aeration and high bather density mean turnover periods measured in minutes, aggressive disinfection demand and the highest Legionella risk in the building — treat a spa as a separate system, never as an appendage to the pool.</li>
</ul>

<h2 id="heat">5 · Heating, and where the energy actually goes</h2>
<p>For a heated pool, <strong>evaporation is typically 60–70&nbsp;% of the total heat loss</strong> — more than conduction, radiation and makeup heating combined. Three consequences follow, and they are all cheap:</p>
<ul class="clean">
  <li><strong>A cover is the single most effective measure.</strong> It stops evaporation almost completely while in place; even overnight-only use is a large annual saving.</li>
  <li><strong>Shelter the water surface.</strong> The velocity term in the evaporation equation is the design variable you can most easily change.</li>
  <li><strong>Do not overheat.</strong> Each degree of water temperature raises the saturation pressure and therefore the evaporation; a pool run 2&nbsp;K warmer than necessary costs far more than 2&nbsp;K of sensible heating.</li>
  <li><strong>Recover the heat.</strong> An indoor pool hall's dehumidification plant should be a heat-pump dehumidifier returning the latent heat to the water — the load is large, constant and at a useful temperature, which is close to an ideal heat-pump duty. Backwash and drainage heat recovery are worth checking too.</li>
</ul>
<p>In a Gulf tower the more common case is the opposite: an outdoor pool that needs <em>cooling</em> in summer to stay comfortable, which is a genuine chilled-water load, and heating only in the short winter. Design for both and confirm which governs.</p>

<h2 id="int-struct">6 · Interactive: the load on the roof</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pool mass and sloshing allowance at the top of a tower</div>
    <div class="fsub">Static mass from volume; dynamic allowance as a fraction of static representing the sloshing (convective) mass excited by building sway. Indicative only — a real design needs a fluid-structure assessment.</div>
  </div>
  <div class="chart-box"><canvas id="stChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Pool area <span id="vSa">400 m²</span></label>
      <input type="range" id="sSa" min="20" max="1200" value="400" step="10">
      <div class="hint">Plan area of the pool tank.</div>
    </div>
    <div class="ctrl">
      <label>Average depth <span id="vDp">1.6 m</span></label>
      <input type="range" id="sDp" min="0.4" max="3" value="1.6" step="0.1">
      <div class="hint">Mean water depth across the tank.</div>
    </div>
    <div class="ctrl">
      <label>Sloshing allowance <span id="vSl">15 %</span></label>
      <input type="range" id="sSl" min="0" max="40" value="15" step="1">
      <div class="hint">Share of the water mass participating dynamically under building sway.</div>
    </div>
    <div class="ctrl">
      <label>Structure allowance <span id="vSt">40 %</span></label>
      <input type="range" id="sSt" min="10" max="120" value="40" step="5">
      <div class="hint">Tank, finishes and surround as a share of the water mass.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Water mass</div><div class="v" id="rWm">640 <small>t</small></div></div>
    <div class="cell"><div class="k">Sloshing mass</div><div class="v" id="rSm">96 <small>t</small></div></div>
    <div class="cell"><div class="k">Total dead load</div><div class="v" id="rTl">896 <small>t</small></div></div>
    <div class="cell"><div class="k">Load intensity</div><div class="v" id="rLi">22.0 <small>kPa</small></div></div>
    <div class="cell"><div class="k">vs office floor</div><div class="v" id="rVo">7.3<small>×</small></div></div>
  </div>
</div>
<p class="fig-note">A 400&nbsp;m² pool at 1.6&nbsp;m mean depth is <strong>640 tonnes of water</strong> and, with the tank and surround, close to <strong>900 tonnes</strong> at roof level — a load intensity of <strong>22&nbsp;kPa</strong>, roughly <strong>seven times</strong> a normal office floor. It also sits at the point of maximum building sway, so a share of that water is a dynamic mass moving with the structure. Two things follow that the MEP engineer must actually do: issue the <strong>full operating mass including the balance tank</strong> to the structural engineer early, and note that a pool near the top of a tower interacts with the building's dynamics — in some towers deliberately, as a tuned sloshing damper, which is only possible if the interaction is recognised at concept rather than discovered in commissioning.</p>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Waterproof the tank as a structure, not a finish.</strong> A pool over occupied space is a tanking problem; specify the membrane, the movement joints and a leak-detection layer, and test-fill and monitor before finishes go on.</li>
  <li><strong>Test-fill and hold.</strong> A recorded 7-day static level test before tiling is the only reliable proof; a leak found afterwards means demolishing the finish.</li>
  <li><strong>Size the balance tank properly</strong> and give it level control, overflow and an air gap on the makeup — the same air-gap rule as in <a href="greywater-reuse-tall-buildings.html">water reuse</a>.</li>
  <li><strong>Design the backwash disposal.</strong> A 288&nbsp;m³/h backwash into a drain sized for 160&nbsp;m³/h floods the plant room; check the drain, the route and any dilution or neutralisation the discharge consent requires.</li>
  <li><strong>Plan chemical delivery to the roof</strong> — route, lift capacity, spill containment and a store that meets separation requirements. This is a logistics design task, not a note on a drawing.</li>
  <li><strong>Provide plant access and replacement routes</strong> for filter media, pumps and the dehumidifier, and remember the goods lift is the only way up.</li>
  <li><strong>Commission the water chemistry before opening</strong>, with a microbiological clearance, and set the interlocks that stop bathing on out-of-range readings.</li>
  <li><strong>Meter the makeup water.</strong> On a rooftop pool the makeup meter is the leak detector — a step change in daily makeup is the earliest sign of a tank leak, which over occupied space is the failure that matters most.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Calculate evaporation at the real surface air velocity</strong>, not at an indoor default.</li>
  <li><strong>Shelter the surface and provide a cover</strong> — the two cheapest load reductions available.</li>
  <li><strong>Set the turnover from the code and the bather load</strong>, and size filters, backwash and balance tank from it.</li>
  <li><strong>Put the plant room on the pool level</strong> where possible; otherwise account for the lift in the pump duty.</li>
  <li><strong>Size the balance tank for displacement plus surge</strong>, especially with an infinity edge.</li>
  <li><strong>Treat spas as separate systems</strong> with their own turnover and disinfection.</li>
  <li><strong>Automate dosing with interlocks</strong> and continuous monitoring.</li>
  <li><strong>Issue the full operating mass early</strong> and discuss sloshing with the structural engineer.</li>
  <li><strong>Design backwash disposal, chemical logistics and plant access</strong> as real constraints.</li>
  <li><strong>Test-fill, meter the makeup and commission the chemistry</strong> before anyone swims.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A rooftop pool turns an ordinary building service into one of the tower's largest loads, because evaporation scales with <strong>air velocity</strong> and a roof at 300&nbsp;m is a windy place: 400&nbsp;m² of water loses <strong>384&nbsp;kg/h and 262&nbsp;kW</strong> exposed, against about 104&nbsp;kW sheltered. <strong>Shelter and a cover are worth more than any plant you can buy</strong>, and both are concept-stage architectural decisions. Then size the balance tank for displacement plus surge rather than as a sump, size the drain for the <strong>backwash</strong> rather than the circulation, keep the plant on the pool's own level so the circuit is not a tall open loop, and issue the <strong>900-tonne operating mass</strong> to the structural engineer before the roof is designed rather than after.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Natatoriums chapter — pool evaporation correlation, dehumidification, air distribution and heat recovery.</li>
  <li>PWTAG <em>Swimming Pool Water: Treatment and Quality Standards for Pools and Spas</em> — turnover periods, filtration velocities, disinfection and monitoring.</li>
  <li>BS EN 15288-1 and -2 — swimming pools: safety requirements for design and for operation; and ISO 20380 for pool water treatment plant.</li>
  <li>WHO <em>Guidelines for Safe Recreational Water Environments, Volume 2: Swimming Pools and Similar Environments</em>.</li>
  <li>ANSI/APSP/ICC standards for public and residential pools and spas; and the International Swimming Pool and Spa Code.</li>
  <li>HSE <em>HSG282</em> — control of Legionella and other infectious agents in spa pool systems.</li>
  <li>CIBSE <em>Guide G</em> and SPATA design standards — pool hall services, balance tanks and plant sizing.</li>
  <li>Saudi Building Code <em>SBC 701</em> and local health authority requirements for public pools and water features.</li>
</ol>

<div class="tags">#SwimmingPools #Natatorium #RooftopPool #InfinityEdge #Spa #Wellness #TallBuildings #MegatallBuildings #Evaporation #LatentLoad #PoolCover #Windbreak #Turnover #Filtration #SandFilter #Backwash #BalanceTank #Disinfection #Chlorine #UV #Ozone #Chloramines #Legionella #HSG282 #PWTAG #HeatPumpDehumidifier #StructuralLoad #Sloshing #Waterproofing #Commissioning #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const Y_LAT=2454;
const psat=T=>0.61094*Math.exp(17.625*T/(T+243.04));

/* ---------- CHART 1 : evaporation ---------- */
const sA=document.getElementById('sA'),sTw=document.getElementById('sTw'),
      sTa=document.getElementById('sTa'),sRh=document.getElementById('sRh'),sV=document.getElementById('sV');
function evap(A,Tw,Ta,rh,V){
  const dp=Math.max(psat(Tw)-rh*psat(Ta),0);
  return (A/Y_LAT)*dp*(0.089+0.0782*V);   // kg/s
}
let evChart=new Chart(document.getElementById('evChart'),{
  data:{datasets:[
    {type:'line',label:'Latent load (kW)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Makeup water (m³/day)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your pool',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0.05,max:6,title:{display:true,text:'Air velocity over the water surface (m/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Latent load (kW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Makeup water (m³/day)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updEv(){
  const A=+sA.value,Tw=+sTw.value,Ta=+sTa.value,rh=+sRh.value/100,V=+sV.value;
  document.getElementById('vA').textContent=A+' m²';
  document.getElementById('vTw').textContent=fmt1(Tw)+' °C';
  document.getElementById('vTa').textContent=Ta+' °C';
  document.getElementById('vRh').textContent=fmt0(rh*100)+' %';
  document.getElementById('vV').textContent=fmt2(V)+' m/s';
  const xs=[];for(let x=0.05;x<=6;x+=0.05)xs.push(+x.toFixed(2));
  evChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(evap(A,Tw,Ta,rh,x)*Y_LAT).toFixed(1)}));
  evChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(evap(A,Tw,Ta,rh,x)*86.4).toFixed(2)}));
  const w=evap(A,Tw,Ta,rh,V);
  evChart.data.datasets[2].data=[{x:V,y:+(w*Y_LAT).toFixed(1)}];
  evChart.update('none');
  const sheltered=evap(A,Tw,Ta,rh,0.5)*Y_LAT;
  document.getElementById('rEv').innerHTML=fmt0(w*3600)+' <small>kg/h</small>';
  document.getElementById('rLl').innerHTML=fmt0(w*Y_LAT)+' <small>kW</small>';
  document.getElementById('rMu').innerHTML=fmt1(w*86.4)+' <small>m³/d</small>';
  document.getElementById('rSh').innerHTML=fmt0(sheltered)+' <small>kW</small>';
  const v=document.getElementById('rEx');
  if(V<=0.5)      v.innerHTML='<span class="badge good">sheltered</span>';
  else if(V<=1.5) v.innerHTML='<span class="badge warn">partly exposed</span>';
  else            v.innerHTML='<span class="badge bad">exposed — shelter it</span>';
}
[sA,sTw,sTa,sRh,sV].forEach(s=>s.addEventListener('input',updEv));updEv();

/* ---------- CHART 2 : turnover ---------- */
const sVo=document.getElementById('sVo'),sT=document.getElementById('sT'),
      sFv=document.getElementById('sFv'),sHd=document.getElementById('sHd');
const BACKWASH_V=45;
let turnChart=new Chart(document.getElementById('turnChart'),{
  data:{datasets:[
    {type:'line',label:'Circulation flow (m³/h)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Pump shaft power (kW)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your pool',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0.5,max:10,reverse:true,title:{display:true,text:'Turnover period (h)  —  faster to the right',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Circulation flow (m³/h)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Pump shaft power (kW)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updTurn(){
  const V=+sVo.value,T=+sT.value,fv=+sFv.value,H=+sHd.value;
  document.getElementById('vVo').textContent=V+' m³';
  document.getElementById('vT').textContent=fmt1(T)+' h';
  document.getElementById('vFv').textContent=fv+' m/h';
  document.getElementById('vHd').textContent=H+' m';
  const Q=t=>V/t;
  const kW=t=>Q(t)/3.6*H/(102*0.70);
  const xs=[];for(let t=0.5;t<=10;t+=0.1)xs.push(+t.toFixed(1));
  turnChart.data.datasets[0].data=xs.map(t=>({x:t,y:+Q(t).toFixed(1)}));
  turnChart.data.datasets[1].data=xs.map(t=>({x:t,y:+kW(t).toFixed(2)}));
  turnChart.data.datasets[2].data=[{x:T,y:+Q(T).toFixed(1)}];
  turnChart.update('none');
  const q=Q(T), fa=q/fv;
  document.getElementById('rQ').innerHTML=fmt0(q)+' <small>m³/h</small>';
  document.getElementById('rLs').innerHTML=fmt0(q/3.6)+' <small>L/s</small>';
  document.getElementById('rFa').innerHTML=fmt1(fa)+' <small>m²</small>';
  document.getElementById('rPw').innerHTML=fmt1(kW(T))+' <small>kW</small>';
  document.getElementById('rBw').innerHTML=fmt0(fa*BACKWASH_V)+' <small>m³/h</small>';
}
[sVo,sT,sFv,sHd].forEach(s=>s.addEventListener('input',updTurn));updTurn();

/* ---------- CHART 3 : structural load ---------- */
const sSa=document.getElementById('sSa'),sDp=document.getElementById('sDp'),
      sSl=document.getElementById('sSl'),sSt=document.getElementById('sSt');
const OFFICE_KPA=3.0;
let stChart=new Chart(document.getElementById('stChart'),{
  data:{datasets:[
    {type:'line',label:'Total dead load (t)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Water only (t)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your pool',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:20,max:1200,title:{display:true,text:'Pool plan area (m²)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Mass at roof level (tonnes)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} t at ${fmt0(c.parsed.x)} m²`}}}}
});
function updSt(){
  const A=+sSa.value,d=+sDp.value,sl=+sSl.value/100,st=+sSt.value/100;
  document.getElementById('vSa').textContent=A+' m²';
  document.getElementById('vDp').textContent=fmt1(d)+' m';
  document.getElementById('vSl').textContent=fmt0(sl*100)+' %';
  document.getElementById('vSt').textContent=fmt0(st*100)+' %';
  const water=a=>a*d;                 // tonnes (1 m3 = 1 t)
  const total=a=>water(a)*(1+st);
  const xs=[];for(let x=20;x<=1200;x+=10)xs.push(x);
  stChart.data.datasets[0].data=xs.map(x=>({x:x,y:+total(x).toFixed(0)}));
  stChart.data.datasets[1].data=xs.map(x=>({x:x,y:+water(x).toFixed(0)}));
  stChart.data.datasets[2].data=[{x:A,y:+total(A).toFixed(0)}];
  stChart.update('none');
  const W=water(A), T=total(A), kpa=T*9.81/A;
  document.getElementById('rWm').innerHTML=fmt0(W)+' <small>t</small>';
  document.getElementById('rSm').innerHTML=fmt0(W*sl)+' <small>t</small>';
  document.getElementById('rTl').innerHTML=fmt0(T)+' <small>t</small>';
  document.getElementById('rLi').innerHTML=fmt1(kpa)+' <small>kPa</small>';
  document.getElementById('rVo').innerHTML=fmt1(kpa/OFFICE_KPA)+'<small>×</small>';
}
[sSa,sDp,sSl,sSt].forEach(s=>s.addEventListener('input',updSt));updSt();

window.addEventListener('load',function(){try{evChart.resize();turnChart.resize();stChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='pools-wellness-mep-tall-buildings', cat='plumbing', mins=14,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Pools &amp; Wellness MEP in Megatall Buildings: Rooftop Evaporation, Turnover &amp; the Load on the Roof',
    reg_title='Pools & Wellness MEP in Megatall Buildings: Rooftop Evaporation, Turnover & the Load on the Roof',
    reg_tag='Plumbing · Pools · Wellness',
    breadcrumb='Plumbing &amp; Drainage',
    tag_line='Plumbing &middot; Pools &middot; Wellness &middot; Rooftop Amenities',
    desc='Pool and wellness MEP design in megatall buildings: why evaporation scales with air velocity and a rooftop pool at 300 m loses five times what an indoor one does, shelter and covers as the highest-value interventions, turnover periods and filtration and backwash sizing, balance tanks and infinity edges, disinfection and spa risk, heating and heat recovery, and the 900-tonne operating mass at roof level — with three interactive charts.',
    og_desc='A 400 m2 rooftop pool in exposed Gulf conditions loses 384 kg an hour — a 262 kW latent load and 9 m3 a day of makeup. Shelter it to 0.5 m/s and that falls to 104 kW, for architecture rather than plant.',
    ld_desc='A design-perspective guide to pools and wellness facilities in megatall buildings: evaporation and latent load, shelter and covers, turnover and filtration sizing, backwash and balance tanks, infinity edges, disinfection and spa risk, heating and heat recovery, and structural load at roof level.',
    img_alt='Technical cutaway of a rooftop infinity pool on a megatall tower showing the overflow channel and balance tank below deck, the filtration and dosing plant room alongside, and wind flowing across the exposed water surface',
    en_tag='Plumbing &amp; Drainage &middot; Pools &middot; Wellness &middot; Rooftop',
    en_title='Pools &amp; Wellness MEP in Megatall Buildings: Rooftop Evaporation, Turnover &amp; the Load on the Roof',
    en_excerpt='Every megatall tower has a pool, and increasingly it is on the roof &mdash; which transforms an ordinary building service into one of the hardest loads in the building, because evaporation depends on <strong>air movement</strong> and at 300&nbsp;m there is a great deal of it. The same 400&nbsp;m&sup2; of water loses <strong>384&nbsp;kg an hour</strong> exposed: a <strong>262&nbsp;kW</strong> latent load and 9&nbsp;m&sup3; a day of makeup. Shelter it and that falls to 104&nbsp;kW &mdash; architecture beating plant. Plus turnover, backwash, balance tanks, spa risk and the 900-tonne mass at roof level &mdash; with three interactive charts.',
    en_search='swimming pool wellness spa MEP tall buildings megatall rooftop infinity edge evaporation ASHRAE correlation vapour pressure air velocity wind boundary layer latent load makeup water pool cover windbreak shelter water temperature turnover period circulation flow filtration velocity sand filter filter area backwash flow disposal balance tank displacement surge bather load skimmer deck level overflow disinfection chlorine bromine residual UV ozone chloramines combined chlorine automatic dosing pH interlock spa Legionella HSG282 PWTAG heat pump dehumidifier heat recovery structural load sloshing dynamic mass tuned sloshing damper waterproofing tanking test fill leak detection makeup metering chemical storage plant access commissioning MEP building services',
    ar_title='المسابح ومرافق الاستجمام في المباني فائقة الارتفاع: التبخر على الأسطح ومعدل الدوران والحمل الإنشائي',
    ar_excerpt='كل برج فائق الارتفاع فيه مسبح، وغالبًا على السطح — وهذا يحوّل خدمة عادية إلى واحد من أصعب الأحمال في المبنى، لأن التبخر يعتمد على <strong>حركة الهواء</strong>، وعلى ارتفاع ٣٠٠ متر يوجد الكثير منها. المساحة نفسها البالغة ٤٠٠ م٢ تفقد <strong>٣٨٤ كجم في الساعة</strong> عند التعرض: حمل كامن قدره <strong>٢٦٢ كيلوواط</strong> و٩ أمتار مكعبة يوميًا من مياه التعويض. احمِ السطح وينخفض إلى ١٠١ كيلوواط — العمارة تتفوق على المعدات. مع معدل الدوران والغسيل العكسي وخزان الموازنة ومخاطر الجاكوزي والكتلة البالغة ٩٠٠ طن على السطح — مع ثلاثة رسوم تفاعلية.',
    ar_search='swimming pool spa wellness rooftop infinity edge evaporation latent load pool cover turnover filtration backwash balance tank disinfection UV ozone Legionella HSG282 PWTAG structural load sloshing waterproofing المسابح حمامات السباحة الجاكوزي مرافق الاستجمام المباني الشاهقة المباني فائقة الارتفاع مسبح السطح الحافة اللانهائية التبخر معادلة أشري ضغط البخار سرعة الهواء الرياح الطبقة الحدية الحمل الكامن مياه التعويض غطاء المسبح مصد الرياح الحماية درجة حرارة الماء فترة الدوران معدل التدوير سرعة الترشيح المرشح الرملي مساحة المرشح تدفق الغسيل العكسي التخلص من مياه الغسيل خزان الموازنة الإزاحة الطفرة حمل المستحمين المكشطة التصريف المحيطي التعقيم الكلور البروم المتبقي الأشعة فوق البنفسجية الأوزون الكلورامين الجرعات التلقائية الأس الهيدروجيني التعشيق الليجيونيلا مضخة حرارية لإزالة الرطوبة استرجاع الحرارة الحمل الإنشائي الترنح الكتلة الديناميكية مخمد الترنح المضبوط العزل المائي اختبار الملء كشف التسرب عداد مياه التعويض تخزين الكيماويات الوصول للمعدات التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
