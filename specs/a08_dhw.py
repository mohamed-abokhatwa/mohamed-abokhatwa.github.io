# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Domestic hot water is the only building service that can kill people through ordinary operation rather than through failure. Legionella does not need a fault, a leak or a fire — it needs lukewarm water and time, and a tall building offers both in abundance: kilometres of pipework, long branches to distant fixtures, and a system that is deliberately kept at the temperature bacteria like best somewhere between the boiler and the tap. The design problem is a genuine conflict. <strong>Hot enough to be safe is hot enough to scald</strong>, and the temperature that stops growth is the temperature that damages people. Everything else in this article follows from resolving that at the right place in the system.</p>

<h2 id="conflict">1 · The central conflict</h2>
<ul class="clean">
  <li><strong>Legionella grows between about 20 and 45&nbsp;°C</strong>, thrives around 37&nbsp;°C, and is killed progressively above 50&nbsp;°C. Below 20&nbsp;°C it is dormant.</li>
  <li><strong>Scald risk begins at about 44&nbsp;°C</strong> and becomes severe quickly: a full-thickness burn takes roughly 5 seconds at 60&nbsp;°C and about a second at 70&nbsp;°C.</li>
  <li><strong>The resolution is spatial, not thermal.</strong> Keep the <em>system</em> hot — storage at 60&nbsp;°C, return never below 55&nbsp;°C — and drop the temperature at the last possible moment with a thermostatic mixing valve immediately before the outlet. Never solve it by storing at 45&nbsp;°C.</li>
  <li><strong>The cold side matters as much.</strong> Cold water above 20&nbsp;°C is a growth medium too, and in a Gulf tower the cold riser sits in a warm shaft next to a hot one. Keeping cold water cold is a real design task, not an assumption.</li>
</ul>

<h2 id="int-kill">2 · Interactive: temperature, time and thermal disinfection</h2>
<p>Bacterial die-off is logarithmic: a <strong>D-value</strong> is the time to kill 90&nbsp;% of the population, and it falls steeply with temperature. This is why the difference between a 55&nbsp;°C and a 60&nbsp;°C return is not a 9&nbsp;% improvement but a factor of seven.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Time to disinfect vs water temperature</div>
    <div class="fsub">D(T) = 2 × 10^((60−T)/z) minutes with z ≈ 5.9 K, anchored to the widely cited values of ~2 min at 60 °C and ~100 min at 50 °C for one decimal reduction. The shaded band is the growth range.</div>
  </div>
  <div class="chart-box"><canvas id="killChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Water temperature <span id="vT">55 °C</span></label>
      <input type="range" id="sT" min="35" max="75" value="55" step="0.5">
      <div class="hint">The temperature actually achieved at the point in question — return leg, tank bottom, dead leg.</div>
    </div>
    <div class="ctrl">
      <label>Log reduction required <span id="vL">4</span></label>
      <input type="range" id="sL" min="1" max="6" value="4" step="1">
      <div class="hint">4-log (99.99 %) is a common disinfection target.</div>
    </div>
    <div class="ctrl">
      <label>z-value <span id="vZ">5.9 K</span></label>
      <input type="range" id="sZ" min="4" max="8" value="5.9" step="0.1">
      <div class="hint">Kelvin per decimal reduction. Lower z = steeper temperature sensitivity.</div>
    </div>
    <div class="ctrl">
      <label>Time available <span id="vTa">60 min</span></label>
      <input type="range" id="sTa" min="1" max="240" value="60" step="1">
      <div class="hint">Contact time at that temperature — a pasteurisation cycle, or residence in storage.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">D-value</div><div class="v" id="rD">14.1 <small>min</small></div></div>
    <div class="cell"><div class="k">Time for target</div><div class="v" id="rTt">56 <small>min</small></div></div>
    <div class="cell"><div class="k">Achieved in time</div><div class="v" id="rAc">4.3 <small>log</small></div></div>
    <div class="cell"><div class="k">At 60 °C</div><div class="v" id="rT60">8 <small>min</small></div></div>
    <div class="cell"><div class="k">Regime</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">At <strong>55&nbsp;°C</strong> a 4-log kill takes about <strong>56 minutes</strong>; at <strong>60&nbsp;°C</strong> it takes <strong>8 minutes</strong>; at 50&nbsp;°C it takes nearly seven hours; and at 46&nbsp;°C — a return leg that has sagged only a few degrees — it takes well over a day, which in a circulating system means never. That steepness is the entire reason the codes specify 60&nbsp;°C storage and a 55&nbsp;°C minimum return rather than a comfortable-sounding 50: the margin is not comfort, it is two orders of magnitude of kill rate. It is also why the number that matters is the temperature at the <em>worst</em> point in the loop, measured, not the boiler set-point.</p>

<h2 id="recirc">3 · The recirculation loop — the system's real weak point</h2>
<p>A tall building cannot wait for hot water to travel 300&nbsp;m, so the hot water circulates continuously and returns to the plant. That loop is what keeps the system safe, and it fails in ways that are invisible from the plant room:</p>
<ul class="clean">
  <li><strong>Hydraulic imbalance.</strong> Without balancing, the short and easy branches take nearly all the return flow and the long, remote branches — precisely the ones at risk — get almost none and cool below 55&nbsp;°C. <strong>Thermostatic balancing valves</strong> on every return branch, which throttle as the branch reaches temperature and so self-balance to temperature rather than to flow, are the single most effective component in the whole system.</li>
  <li><strong>Dead legs.</strong> Every length of pipe beyond the circulating loop stagnates. Codes typically limit the dead leg to a few litres or a few metres; the practical rule is to <strong>bring the circulation as close to the outlet as the layout allows</strong> and to keep the final branch short.</li>
  <li><strong>Undersized return.</strong> The return flow only has to carry the loop's heat loss, so it is small — often a fraction of a litre per second — but it must be calculated, not guessed, and it must be checked against the loss of a <em>well-insulated</em> pipe rather than a bare one.</li>
  <li><strong>Infrequently used outlets.</strong> A tall residential tower has apartments that stand empty for months. Automatic flushing on a timer, or a managed flushing regime, is part of the design, not the operation.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Recirculation heat loss and return flow</div>
    <div class="fsub">Loss = U·πD·L·ΔT; return flow = loss / (c&#112;·ΔT&#100;&#114;&#111;&#112;). The pump must deliver this flow against the loop resistance while every branch stays above 55 °C.</div>
  </div>
  <div class="chart-box"><canvas id="loopChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Loop length <span id="vLl">1200 m</span></label>
      <input type="range" id="sLl" min="100" max="3000" value="1200" step="50">
      <div class="hint">Total circulating flow-and-return pipe length in the zone.</div>
    </div>
    <div class="ctrl">
      <label>Pipe diameter <span id="vDd">65 mm</span></label>
      <input type="range" id="sDd" min="20" max="150" value="65" step="5">
      <div class="hint">Mean diameter of the circulating pipework.</div>
    </div>
    <div class="ctrl">
      <label>Insulation U-value <span id="vU">0.60 W/m²K</span></label>
      <input type="range" id="sU" min="0.2" max="3" value="0.6" step="0.05">
      <div class="hint">Per m² of pipe surface. Well-insulated ≈ 0.4–0.8; poorly lagged or bare is several times that.</div>
    </div>
    <div class="ctrl">
      <label>Permitted temperature drop <span id="vDt">5.0 K</span></label>
      <input type="range" id="sDt" min="2" max="10" value="5" step="0.5">
      <div class="hint">Flow-to-return drop. Codes require the return to stay at or above 55 °C.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Loop heat loss</div><div class="v" id="rQ">5.1 <small>kW</small></div></div>
    <div class="cell"><div class="k">Return flow</div><div class="v" id="rF">0.25 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Annual loss</div><div class="v" id="rA">45 <small>MWh</small></div></div>
    <div class="cell"><div class="k">If badly lagged</div><div class="v" id="rB">17.2 <small>kW</small></div></div>
    <div class="cell"><div class="k">Return temp OK?</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVr"></span></div></div>
  </div>
</div>
<p class="fig-note">A 1,200&nbsp;m loop of DN65 at a decent 0.6&nbsp;W/m²K loses about <strong>5.1&nbsp;kW continuously — 45&nbsp;MWh a year</strong>, and needs only <strong>0.25&nbsp;L/s</strong> of return flow to hold a 5&nbsp;K drop. Two things follow. First, the return flow is <em>tiny</em>, which is exactly why it distributes so badly without thermostatic balancing valves: at these flows a small imbalance starves a branch completely. Second, the standing loss runs 8,760 hours a year and is often larger than any efficiency measure applied to the heat source — so insulation thickness on the circulating loop is a first-order energy decision, not a detail.</p>

<h2 id="int-storage">4 · Interactive: storage versus instantaneous</h2>
<p>Hot water demand is spiky — a hotel's morning peak or a residential tower's evening peak lasts under an hour. You can meet it with raw heater capacity or with stored volume, and in a tall building the trade also involves plant space, structural weight and Legionella risk.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Heater capacity vs storage volume for the peak</div>
    <div class="fsub">Instantaneous duty = Q·c&#112;·ΔT for the full peak flow. With storage, the heater covers the sustained draw and the tank rides the peak: V = (Q − Q&#114;&#101;&#99;)·t&#112;&#101;&#97;&#107;.</div>
  </div>
  <div class="chart-box"><canvas id="storChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Peak demand <span id="vQp">8.0 L/s</span></label>
      <input type="range" id="sQp" min="0.5" max="30" value="8" step="0.5">
      <div class="hint">Simultaneous hot water draw at the peak minute for the zone.</div>
    </div>
    <div class="ctrl">
      <label>Peak duration <span id="vTp">20 min</span></label>
      <input type="range" id="sTp" min="5" max="90" value="20" step="1">
      <div class="hint">How long the peak is sustained.</div>
    </div>
    <div class="ctrl">
      <label>Temperature rise <span id="vDr">45 K</span></label>
      <input type="range" id="sDr" min="25" max="60" value="45" step="1">
      <div class="hint">Cold feed to storage temperature — 15 °C to 60 °C is typical.</div>
    </div>
    <div class="ctrl">
      <label>Heater as share of peak <span id="vSh">35 %</span></label>
      <input type="range" id="sSh" min="10" max="100" value="35" step="1">
      <div class="hint">Recovery capacity. 100 % is fully instantaneous with no storage.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Fully instantaneous</div><div class="v" id="rIn">1,507 <small>kW</small></div></div>
    <div class="cell"><div class="k">Heater with storage</div><div class="v" id="rHt">528 <small>kW</small></div></div>
    <div class="cell"><div class="k">Storage needed</div><div class="v" id="rV">6.2 <small>m³</small></div></div>
    <div class="cell"><div class="k">Tank weight</div><div class="v" id="rW">6.2 <small>t</small></div></div>
    <div class="cell"><div class="k">Turnover</div><div class="v" id="rTo">13 <small>min</small></div></div>
  </div>
</div>
<p class="fig-note">An 8&nbsp;L/s peak at a 45&nbsp;K rise is <strong>1,507&nbsp;kW</strong> if met instantaneously. Cover 35&nbsp;% of it with a <strong>528&nbsp;kW</strong> heater and ride the rest on <strong>6.2&nbsp;m³</strong> of storage — but that tank weighs 6.2&nbsp;tonnes on a mechanical floor and, crucially, it must still turn over fast enough to stay safe. The Legionella constraint pushes storage <em>down</em> while the plant-cost constraint pushes it up, and the honest answer in a tall building is usually modest storage with a generous recovery rate, kept at 60&nbsp;°C, rather than the large buffer tank that a spreadsheet optimum suggests.</p>

<h2 id="tmv">5 · Mixing valves, scald protection and the cold side</h2>
<ul class="clean">
  <li><strong>Thermostatic mixing valves belong at the outlet, not the plant.</strong> A central blending valve serving a whole floor creates a large volume of pipework at 40&nbsp;°C — the ideal growth temperature — downstream of it. Fit the TMV as close to the fixture as practicable and keep the blended dead leg to a couple of metres.</li>
  <li><strong>Specify the right TMV type</strong> and its failsafe: a valve that fails to full hot on loss of cold supply is not acceptable in a healthcare or hotel setting. Require thermal shut-off.</li>
  <li><strong>TMVs need servicing</strong> — they scale, and a scaled TMV drifts. Locate every one so it can actually be reached, and schedule them.</li>
  <li><strong>Keep the cold water cold.</strong> Insulate cold risers and, in a warm shaft, separate them from hot and heating pipework or provide a ventilated shaft. Where cold water cannot be held below 20&nbsp;°C — a real problem in Gulf towers with long horizontal runs and warm plant spaces — treat it as a risk requiring its own control measure, not as an unavoidable nuisance.</li>
  <li><strong>Do not run cold water through unventilated risers alongside heating flow and return.</strong> It is the commonest cause of warm cold-water in a tall building and it is a coordination decision made in the shaft layout.</li>
</ul>

<h2 id="install">6 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Insulate to a stated thickness and inspect it</strong> — including at valves, flanges, supports and penetrations, which are where it is always missing and where the heat actually escapes.</li>
  <li><strong>Fit a thermometer pocket on every return branch</strong> at the point it rejoins the main. Without them, proving 55&nbsp;°C at the remote branch is guesswork and every future audit is an argument.</li>
  <li><strong>Commission the loop to temperature, not to flow.</strong> Set thermostatic balancing valves, then verify the return temperature at every branch with the system at design and again at low draw-off, and record every reading against the branch reference.</li>
  <li><strong>Disinfect systematically and hold the record.</strong> Chlorination or thermal disinfection following a written procedure, with samples per zone and per riser, and the results retained — partial disinfection of a zoned system is the classic reason for a second failed clearance.</li>
  <li><strong>Flush before commissioning, and keep flushing until handover.</strong> A system that sits full and warm from practical completion to occupation is being incubated. Put a flushing regime in the handover programme with named responsibility.</li>
  <li><strong>Support and expand the hot riser properly.</strong> Hot water pipework moves substantially more than cold; provide anchors, guides and expansion devices, and check that insulation and fire-stopping accommodate the movement rather than restrain it.</li>
  <li><strong>Label the water safety plan into the O&amp;M</strong> with the temperature regime, the flushing schedule, the TMV service interval and the named responsible person.</li>
</ul>

<h2 id="checklist">7 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Store at 60&nbsp;°C, return at 55&nbsp;°C minimum, blend at the outlet</strong> — never compromise the system temperature for scald safety.</li>
  <li><strong>Thermostatic balancing valves on every return branch</strong>, and thermometer pockets to prove them.</li>
  <li><strong>Minimise dead legs</strong> and bring circulation close to the outlets.</li>
  <li><strong>Calculate the loop loss and return flow</strong> on real insulation values, and treat the standing loss as a design target.</li>
  <li><strong>Choose storage for turnover as well as for peak</strong> — small and hot beats large and tepid.</li>
  <li><strong>Keep cold water below 20&nbsp;°C</strong>, with shaft layout and insulation designed for it.</li>
  <li><strong>Plan flushing for low-occupancy outlets</strong> as a designed feature.</li>
  <li><strong>Commission to temperature and record every branch</strong>; disinfect to a written procedure per zone.</li>
  <li><strong>Issue a water safety plan</strong> with named responsibility and service intervals.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Hot water is a <strong>conflict between two temperatures</strong> — the one that kills bacteria and the one that scalds people — and it is resolved spatially, by keeping the whole system at 60&nbsp;°C and blending only at the outlet. Everything that goes wrong afterwards happens in the <strong>recirculation loop</strong>: the return flow is only a fraction of a litre per second, so without thermostatic balancing valves the long remote branches simply do not get any, sag below 55&nbsp;°C, and become the part of the system nobody measures. Put a thermometer pocket on every return branch, commission to temperature rather than flow, and remember that at 55&nbsp;°C disinfection takes an hour, at 60&nbsp;°C eight minutes, and at 46&nbsp;°C it never happens at all.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>HSE <em>ACOP L8 — Legionnaires' disease: The control of legionella bacteria in water systems</em> and HSG274 Part 2 (hot and cold water systems) — temperature regime, dead legs, monitoring and written schemes.</li>
  <li>ASHRAE Standard 188 — <em>Legionellosis: Risk Management for Building Water Systems</em>; and ASHRAE Guideline 12 for implementation detail.</li>
  <li>WHO <em>Legionella and the prevention of legionellosis</em> and <em>Water Safety in Buildings</em> — growth conditions, thermal inactivation and building water safety planning.</li>
  <li>CIBSE <em>Guide G — Public Health and Plumbing Engineering</em> and CIBSE TM13 <em>Minimising the risk of Legionnaires' disease</em>.</li>
  <li>BS 8558 and BS EN 806 — design, installation, testing and maintenance of water supply systems including disinfection procedures.</li>
  <li>BS EN 1717 and the relevant TMV standards (BS EN 1111 / 1287, NSF/ANSI / ASSE 1017 and 1070) — mixing valve performance and failsafe requirements.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Service Water Heating chapter — demand estimation, storage versus recovery sizing and recirculation design.</li>
  <li>Saudi Building Code <em>SBC 701</em> plumbing provisions; and ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em> for vertical zoning of service water heating.</li>
</ol>

<div class="tags">#DomesticHotWater #DHW #ServiceWaterHeating #Legionella #ASHRAE188 #ACOPL8 #HSG274 #TallBuildings #MegatallBuildings #Plumbing #Recirculation #ThermostaticBalancingValve #DeadLeg #TMV #ScaldProtection #ThermalDisinfection #Dvalue #Storage #InstantaneousHeating #Turnover #Insulation #StandingLoss #Flushing #WaterSafetyPlan #Commissioning #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const CP=4.187;

/* ---------- CHART 1 : thermal disinfection ---------- */
const sT=document.getElementById('sT'),sL=document.getElementById('sL'),
      sZ=document.getElementById('sZ'),sTa=document.getElementById('sTa');
const Dval=(T,z)=>2*Math.pow(10,(60-T)/z);
let killChart=new Chart(document.getElementById('killChart'),{
  data:{datasets:[
    {type:'line',label:'Time for the target log reduction',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:3},
    {type:'line',label:'D-value (one decimal reduction)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your temperature',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:35,max:75,title:{display:true,text:'Water temperature (°C)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'logarithmic',title:{display:true,text:'Time (minutes, log scale)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} min at ${fmt1(c.parsed.x)} °C`}},
      annotation:{annotations:{
        av:{type:'line',scaleID:'y',yScaleID:'y',value:60,borderColor:'#1e8449',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'time available',position:'start',font:{size:10,family:'DM Sans'},color:'#1e8449',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updKill(){
  const T=+sT.value,L=+sL.value,z=+sZ.value,ta=+sTa.value;
  document.getElementById('vT').textContent=fmt1(T)+' °C';
  document.getElementById('vL').textContent=L;
  document.getElementById('vZ').textContent=fmt1(z)+' K';
  document.getElementById('vTa').textContent=ta+' min';
  const xs=[];for(let x=35;x<=75;x+=0.5)xs.push(+x.toFixed(1));
  killChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(L*Dval(x,z)).toFixed(3)}));
  killChart.data.datasets[1].data=xs.map(x=>({x:x,y:+Dval(x,z).toFixed(3)}));
  killChart.data.datasets[2].data=[{x:T,y:+(L*Dval(T,z)).toFixed(3)}];
  killChart.options.plugins.annotation.annotations.av.value=ta;
  killChart.update('none');
  const d=Dval(T,z), need=L*d, got=ta/d;
  document.getElementById('rD').innerHTML=fmt1(d)+' <small>min</small>';
  document.getElementById('rTt').innerHTML=(need<600?fmt0(need)+' <small>min</small>':fmt1(need/60)+' <small>h</small>');
  document.getElementById('rAc').innerHTML=fmt1(got)+' <small>log</small>';
  document.getElementById('rT60').innerHTML=fmt0(L*Dval(60,z))+' <small>min</small>';
  const v=document.getElementById('rVd');
  if(T<20)       v.innerHTML='<span class="badge good">dormant — cold</span>';
  else if(T<46)  v.innerHTML='<span class="badge bad">growth range</span>';
  else if(T<55)  v.innerHTML='<span class="badge warn">slow kill only</span>';
  else           v.innerHTML='<span class="badge good">effective disinfection</span>';
}
[sT,sL,sZ,sTa].forEach(s=>s.addEventListener('input',updKill));updKill();

/* ---------- CHART 2 : recirculation loop ---------- */
const sLl=document.getElementById('sLl'),sDd=document.getElementById('sDd'),
      sU=document.getElementById('sU'),sDt=document.getElementById('sDt');
const loss=(L,D,U,dT)=>U*Math.PI*(D/1000)*L*dT;
let loopChart=new Chart(document.getElementById('loopChart'),{
  data:{datasets:[
    {type:'line',label:'Loop heat loss (kW)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Return flow (L/s)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your loop',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:100,max:3000,title:{display:true,text:'Circulating loop length (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Heat loss (kW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Return flow (L/s)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updLoop(){
  const L=+sLl.value,D=+sDd.value,U=+sU.value,dt=+sDt.value;
  document.getElementById('vLl').textContent=L+' m';
  document.getElementById('vDd').textContent=D+' mm';
  document.getElementById('vU').textContent=fmt2(U)+' W/m²K';
  document.getElementById('vDt').textContent=fmt1(dt)+' K';
  const DT=35;
  const xs=[];for(let x=100;x<=3000;x+=50)xs.push(x);
  loopChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(loss(x,D,U,DT)/1000).toFixed(3)}));
  loopChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(loss(x,D,U,DT)/(CP*1000*dt)).toFixed(4)}));
  const q=loss(L,D,U,DT);
  loopChart.data.datasets[2].data=[{x:L,y:+(q/1000).toFixed(3)}];
  loopChart.update('none');
  document.getElementById('rQ').innerHTML=fmt1(q/1000)+' <small>kW</small>';
  document.getElementById('rF').innerHTML=fmt2(q/(CP*1000*dt))+' <small>L/s</small>';
  document.getElementById('rA').innerHTML=fmt0(q*8.76/1000)+' <small>MWh</small>';
  document.getElementById('rB').innerHTML=fmt1(loss(L,D,2.0,DT)/1000)+' <small>kW</small>';
  const v=document.getElementById('rVr');
  if(dt<=5)      v.innerHTML='<span class="badge good">return stays ≥ 55 °C</span>';
  else if(dt<=7) v.innerHTML='<span class="badge warn">tight — balance carefully</span>';
  else           v.innerHTML='<span class="badge bad">return will fall below 55 °C</span>';
}
[sLl,sDd,sU,sDt].forEach(s=>s.addEventListener('input',updLoop));updLoop();

/* ---------- CHART 3 : storage vs instantaneous ---------- */
const sQp=document.getElementById('sQp'),sTp=document.getElementById('sTp'),
      sDr=document.getElementById('sDr'),sSh=document.getElementById('sSh');
let storChart=new Chart(document.getElementById('storChart'),{
  data:{datasets:[
    {type:'line',label:'Storage volume needed (m³)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Heater capacity (kW)',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your design',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:10,max:100,title:{display:true,text:'Heater capacity as a share of peak demand (%)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Storage volume (m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Heater capacity (kW)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updStor(){
  const Q=+sQp.value,tp=+sTp.value,dr=+sDr.value,sh=+sSh.value;
  document.getElementById('vQp').textContent=fmt1(Q)+' L/s';
  document.getElementById('vTp').textContent=tp+' min';
  document.getElementById('vDr').textContent=dr+' K';
  document.getElementById('vSh').textContent=sh+' %';
  const inst=Q*CP*dr;
  const vol=s=>Math.max(0,Q*(1-s/100)*tp*60/1000);
  const xs=[];for(let s=10;s<=100;s+=1)xs.push(s);
  storChart.data.datasets[0].data=xs.map(s=>({x:s,y:+vol(s).toFixed(2)}));
  storChart.data.datasets[1].data=xs.map(s=>({x:s,y:+(inst*s/100).toFixed(0)}));
  storChart.data.datasets[2].data=[{x:sh,y:+vol(sh).toFixed(2)}];
  storChart.update('none');
  const V=vol(sh);
  document.getElementById('rIn').innerHTML=fmt0(inst)+' <small>kW</small>';
  document.getElementById('rHt').innerHTML=fmt0(inst*sh/100)+' <small>kW</small>';
  document.getElementById('rV').innerHTML=fmt1(V)+' <small>m³</small>';
  document.getElementById('rW').innerHTML=fmt1(V)+' <small>t</small>';
  document.getElementById('rTo').innerHTML=(Q>0?fmt0(V*1000/Q/60):'—')+' <small>min</small>';
}
[sQp,sTp,sDr,sSh].forEach(s=>s.addEventListener('input',updStor));updStor();

window.addEventListener('load',function(){try{killChart.resize();loopChart.resize();storChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='domestic-hot-water-legionella-tall-buildings', cat='plumbing', mins=16,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Domestic Hot Water &amp; Legionella Control in Megatall Buildings: Temperature Regime, Recirculation &amp; Storage',
    reg_title='Domestic Hot Water & Legionella Control in Megatall Buildings: Temperature Regime, Recirculation & Storage',
    reg_tag='Plumbing · Hot Water · Legionella',
    breadcrumb='Plumbing &amp; Drainage',
    tag_line='Plumbing &middot; Domestic Hot Water &middot; Legionella &middot; Megatall Buildings',
    desc='Domestic hot water design in megatall buildings: the conflict between the temperature that kills Legionella and the temperature that scalds, thermal disinfection D-values and why 55 versus 60 degrees is a factor of seven, recirculation loop losses and why the tiny return flow makes thermostatic balancing valves essential, dead legs, storage versus instantaneous sizing against turnover, mixing valve placement and keeping cold water cold — with three interactive charts and installation tricks.',
    og_desc='At 55 degrees a 4-log kill takes an hour; at 60 it takes eight minutes; at 46 it never happens. Why hot water is a spatial problem, and why the recirculation return flow being a fraction of a litre per second is what makes it fail.',
    ld_desc='A design-perspective guide to domestic hot water and Legionella control in megatall buildings: thermal inactivation D-values and the temperature regime, recirculation loop heat loss and return flow, thermostatic balancing valves and dead legs, storage versus instantaneous capacity and turnover, mixing valve placement and cold water temperature control.',
    img_alt='Technical cutaway of a megatall tower&rsquo;s domestic hot water system showing calorifiers and storage on a mechanical floor, a hot flow riser and a returning recirculation riser with thermostatic balancing valves on each branch, and mixing valves close to the outlets',
    en_tag='Plumbing &amp; Drainage &middot; Hot Water &middot; Legionella &middot; Megatall',
    en_title='Domestic Hot Water &amp; Legionella Control in Megatall Buildings: Temperature Regime, Recirculation &amp; Storage',
    en_excerpt='Hot water is the only building service that can harm people through ordinary operation rather than through failure &mdash; and the design is a genuine conflict, because hot enough to be safe is hot enough to scald. At 55&nbsp;&deg;C a 4-log kill takes an hour, at 60&nbsp;&deg;C eight minutes, and at 46&nbsp;&deg;C it never happens. Why the answer is spatial rather than thermal, why a recirculation return flow of a quarter of a litre per second is what makes remote branches fail, dead legs, storage versus turnover, and keeping cold water cold in a warm shaft &mdash; with three interactive charts.',
    en_search='domestic hot water DHW service water heating Legionella legionnaires disease tall buildings megatall plumbing temperature regime 60 degrees storage 55 degrees return thermal disinfection D-value log reduction z-value growth range 20 45 scald risk thermostatic mixing valve TMV failsafe point of use recirculation loop heat loss standing loss return flow thermostatic balancing valve dynamic balancing dead leg stagnation infrequently used outlets automatic flushing storage calorifier instantaneous heater recovery rate turnover tank weight cold water below 20 shaft layout insulation thickness thermometer pocket commissioning to temperature chlorination disinfection water safety plan ACOP L8 HSG274 ASHRAE 188 CIBSE TM13 BS 8558 MEP building services',
    ar_title='المياه الساخنة ومكافحة الليجيونيلا في المباني فائقة الارتفاع: نظام الحرارة والتدوير والتخزين',
    ar_excerpt='المياه الساخنة هي الخدمة الوحيدة في المبنى التي قد تؤذي الناس أثناء التشغيل العادي لا عند العطل — والتصميم تعارضٌ حقيقي، لأن الحرارة الكافية للأمان هي نفسها الكافية للحرق. عند ٥٥ درجة يحتاج القتل بمقدار أربع مراتب لوغاريتمية إلى ساعة، وعند ٦٠ درجة إلى ثماني دقائق، وعند ٤٦ درجة لا يحدث أبدًا. لماذا يكون الحل مكانيًا لا حراريًا، ولماذا يكون تدفق العودة البالغ ربع لتر في الثانية هو سبب فشل الفروع البعيدة، والفروع الميتة، والتخزين مقابل معدل الدوران، وإبقاء المياه الباردة باردة داخل منور دافئ — مع ثلاثة رسوم تفاعلية.',
    ar_search='domestic hot water Legionella thermal disinfection D-value recirculation thermostatic balancing valve dead leg TMV storage turnover cold water ACOP L8 HSG274 ASHRAE 188 CIBSE TM13 المياه الساخنة تسخين مياه الاستخدام الليجيونيلا داء الفيالقة المباني الشاهقة المباني فائقة الارتفاع السباكة نظام درجات الحرارة التخزين عند ٦٠ العودة عند ٥٥ التعقيم الحراري قيمة الاختزال العشري المدى اللوغاريتمي نطاق النمو خطر الحروق صمام الخلط الحراري صمام الأمان عند نقطة الاستخدام دائرة التدوير الفقد الحراري الفقد الدائم تدفق العودة صمام الموازنة الحراري الفرع الميت الركود المخارج قليلة الاستخدام الغسيل التلقائي السخان التخزيني السخان اللحظي معدل الاسترداد معدل الدوران وزن الخزان المياه الباردة تحت ٢٠ تخطيط المناور سماكة العزل جيب مقياس الحرارة التشغيل والاختبار على الحرارة الكلورة التعقيم خطة سلامة المياه MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
