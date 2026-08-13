# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Connect a megatall tower to a district cooling network and you have not simplified the design — you have replaced a plant you control with a <strong>contract you cannot renegotiate</strong>. The provider guarantees a supply temperature and a pressure; you guarantee a return temperature. That last clause is where the money is. Every kelvin of return temperature you fail to deliver inflates the flow you must contract for, and the capacity charge follows the flow: <strong>a design ΔT of 8&nbsp;K delivered as 4&nbsp;K doubles the capacity charge for exactly the same cooling.</strong> The energy transfer station is a small room with four pieces of equipment in it, and it is one of the highest-leverage designs in the building.</p>

<h2 id="why">1 · What the connection really changes</h2>
<ul class="clean">
  <li><strong>ΔT stops being an efficiency question and becomes a bill.</strong> In an in-house plant a low ΔT wastes pump energy and forces extra chillers on — bad, but internal. On a district connection it is a contractual quantity that is metered, charged and penalised.</li>
  <li><strong>You inherit somebody else's pressure.</strong> District networks run at high pressure to reach distant customers. That network pressure lands at your ETS and adds to whatever static your own building generates.</li>
  <li><strong>The interface is almost always indirect.</strong> A plate heat exchanger separates the network hydraulically from the building — mandatory in a tall building, because the network cannot be exposed to a 60&nbsp;bar building static and the building cannot be exposed to network transients.</li>
  <li><strong>And that heat exchanger costs you temperature.</strong> The approach is added to the supply temperature the provider delivers, and the building's coils must be selected for the warmer number.</li>
  <li><strong>The meter is the cash register.</strong> A BTU meter measures flow and two temperatures; at low ΔT the temperature sensors dominate the uncertainty, and the uncertainty is money.</li>
</ul>

<h2 id="int-dt">2 · Interactive: what a degraded ΔT costs</h2>
<p>District tariffs are typically split into a <strong>capacity charge</strong> — based on contracted peak capacity or peak flow — and a <strong>consumption charge</strong> on metered energy. Cooling delivered is unchanged by a poor ΔT; the <em>flow</em> to deliver it is not.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Contracted flow and capacity charge vs achieved ΔT</div>
    <div class="fsub">Q = load / (4.187·ΔT). Capacity charge is taken as proportional to contracted peak flow. Consumption is unchanged — the same cooling is delivered either way.</div>
  </div>
  <div class="chart-box"><canvas id="dtChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Peak cooling load <span id="vL">20.0 MW</span></label>
      <input type="range" id="sL" min="2" max="80" value="20" step="0.5">
      <div class="hint">Tower peak demand at the ETS (1 MW ≈ 284 TR).</div>
    </div>
    <div class="ctrl">
      <label>Design ΔT <span id="vDd">8.0 K</span></label>
      <input type="range" id="sDd" min="5" max="14" value="8" step="0.5">
      <div class="hint">The ΔT the contract is written on.</div>
    </div>
    <div class="ctrl">
      <label>Achieved ΔT <span id="vDa">6.0 K</span></label>
      <input type="range" id="sDa" min="2.5" max="14" value="6" step="0.1">
      <div class="hint">What the building actually returns. Drag it down to see the penalty.</div>
    </div>
    <div class="ctrl">
      <label>Annual capacity charge <span id="vC">4.0 M</span></label>
      <input type="range" id="sC" min="0.2" max="30" value="4" step="0.1">
      <div class="hint">Annual capacity/demand charge at the design ΔT, in your currency.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Design flow</div><div class="v" id="rQd">597 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Actual flow</div><div class="v" id="rQa">796 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Flow inflation</div><div class="v" id="rFi">33 <small>%</small></div></div>
    <div class="cell"><div class="k">Extra charge</div><div class="v" id="rEc">1.33 <small>M/yr</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">Design at 8&nbsp;K and deliver 6&nbsp;K and the contracted flow rises by <strong>33&nbsp;%</strong>; deliver 4&nbsp;K and it <strong>doubles</strong>. On a modest 4&nbsp;M annual capacity charge that is 1.33&nbsp;M a year for nothing — no extra cooling, no extra comfort, just warmer water going back. The causes are all inside your boundary and all fixable at design: three-port valves anywhere in the building, open bypasses, coils selected at a narrower ΔT than the contract, decoupler backflow, and control valves with too little authority to close properly. This is the single strongest reason to design a district-connected tower at a <strong>wide ΔT and then defend it</strong> — the same argument as in <a href="chilled-water-pumps-tall-buildings.html">chilled-water pumps</a>, but with an invoice attached.</p>

<h2 id="ets">3 · The energy transfer station</h2>
<p>An indirect ETS is deceptively simple: a plate heat exchanger, a control valve on the primary, isolation and strainers, and a meter. Each of those four is a common failure point:</p>
<ul class="clean">
  <li><strong>The heat exchanger.</strong> Sized on approach, fouling allowance and both-side pressure drops, and rated for the <em>primary</em> network pressure on one side and the building static on the other. Specify the plate material and gasket for the network's water chemistry, and provide space to open the plate pack — an exchanger that cannot be stripped will not be cleaned.</li>
  <li><strong>The primary control valve.</strong> This is the component that actually delivers your ΔT. It must have real authority against the network's differential pressure — which is large and varies with the network's own load — so it is almost always a <strong>pressure-independent control valve</strong>. An ordinary two-port valve on a district primary is the classic cause of a building that cannot hold its return temperature.</li>
  <li><strong>Strainers and filtration.</strong> The network is a shared system carrying everybody's debris. Provide a properly sized primary strainer with differential-pressure monitoring, and consider side-stream filtration; a fouled plate pack shows up first as a widening approach and then as a ΔT failure.</li>
  <li><strong>The meter.</strong> Located, installed and maintained to the standard the contract references — with the straight lengths the flow meter actually needs and the matched sensor pair in the correct pockets.</li>
</ul>

<h2 id="int-approach">4 · Interactive: the approach you pay for twice</h2>
<p>The heat exchanger's approach adds to the supply temperature the building sees, and a warmer supply means every coil in the tower must be larger to do the same job — because coil capacity follows the log-mean temperature difference, which shrinks fast as the supply warms.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Secondary supply temperature and coil area penalty vs HX approach</div>
    <div class="fsub">Secondary supply = primary supply + approach. Coil area factor taken as the inverse ratio of LMTD against a reference selection, with room air at 24 °C and off-coil at 13 °C.</div>
  </div>
  <div class="chart-box"><canvas id="apChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Primary supply temperature <span id="vPs">4.5 °C</span></label>
      <input type="range" id="sPs" min="3" max="9" value="4.5" step="0.1">
      <div class="hint">What the district network contracts to deliver at your ETS.</div>
    </div>
    <div class="ctrl">
      <label>Heat-exchanger approach <span id="vAp">1.5 K</span></label>
      <input type="range" id="sAp" min="0.3" max="4" value="1.5" step="0.1">
      <div class="hint">Closer approach = more plates and more cost, but colder secondary water.</div>
    </div>
    <div class="ctrl">
      <label>Secondary ΔT <span id="vSd">8.0 K</span></label>
      <input type="range" id="sSd" min="5" max="12" value="8" step="0.5">
      <div class="hint">Building-side design temperature difference.</div>
    </div>
    <div class="ctrl">
      <label>Reference supply <span id="vRf">6.0 °C</span></label>
      <input type="range" id="sRf" min="4" max="8" value="6" step="0.1">
      <div class="hint">The supply temperature the coils were originally selected at.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Secondary supply</div><div class="v" id="rSs">6.0 <small>°C</small></div></div>
    <div class="cell"><div class="k">Secondary return</div><div class="v" id="rSr">14.0 <small>°C</small></div></div>
    <div class="cell"><div class="k">LMTD</div><div class="v" id="rLm">8.5 <small>K</small></div></div>
    <div class="cell"><div class="k">Coil area factor</div><div class="v" id="rCa">1.00<small>×</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rAv"></span></div></div>
  </div>
</div>
<p class="fig-note">With a 4.5&nbsp;°C primary and a 1.5&nbsp;K approach the building gets <strong>6.0&nbsp;°C</strong> — exactly the reference selection, so the coils are unchanged. Loosen the approach to 3&nbsp;K to save money on plates and the secondary rises to 7.5&nbsp;°C, the LMTD shrinks, and <strong>every coil in the tower needs roughly 15&nbsp;% more area</strong> to deliver the same duty. That is the approach paid for twice: once in the exchanger you did not buy, and again in a thousand coils and the fan energy to push air through them. Buy the plates.</p>

<h2 id="int-meter">5 · Interactive: the meter is the cash register</h2>
<p>A BTU meter computes energy from a flow measurement and a temperature <em>difference</em>. Because the difference is small, the temperature sensors contribute far more uncertainty than their absolute accuracy suggests — and the smaller your ΔT, the worse it gets.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Energy metering uncertainty vs ΔT and sensor accuracy</div>
    <div class="fsub">Combined uncertainty ε = √(ε&#81;² + (√2·ε&#84;/ΔT)²). The temperature term uses a matched pair, so the two sensor errors combine in quadrature.</div>
  </div>
  <div class="chart-box"><canvas id="mtrChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Operating ΔT <span id="vMd">6.0 K</span></label>
      <input type="range" id="sMd" min="2" max="14" value="6" step="0.1">
      <div class="hint">The actual difference the meter sees, which at part load is smaller than design.</div>
    </div>
    <div class="ctrl">
      <label>Sensor pair accuracy <span id="vSe">0.10 K</span></label>
      <input type="range" id="sSe" min="0.02" max="0.5" value="0.1" step="0.01">
      <div class="hint">Matched Pt100 pairs reach 0.05 K; ordinary sensors are far worse.</div>
    </div>
    <div class="ctrl">
      <label>Flow meter accuracy <span id="vFe">1.5 %</span></label>
      <input type="range" id="sFe" min="0.2" max="5" value="1.5" step="0.1">
      <div class="hint">Electromagnetic and ultrasonic meters 0.5–2 % if installed with the right straight lengths.</div>
    </div>
    <div class="ctrl">
      <label>Annual bill <span id="vBl">10.0 M</span></label>
      <input type="range" id="sBl" min="0.5" max="60" value="10" step="0.5">
      <div class="hint">Total annual district cooling invoice, in your currency.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Temperature term</div><div class="v" id="rTe">2.36 <small>%</small></div></div>
    <div class="cell"><div class="k">Total uncertainty</div><div class="v" id="rTu">2.79 <small>%</small></div></div>
    <div class="cell"><div class="k">In money</div><div class="v" id="rMo">0.28 <small>M/yr</small></div></div>
    <div class="cell"><div class="k">At ΔT 4 K</div><div class="v" id="rM4">3.83 <small>%</small></div></div>
    <div class="cell"><div class="k">Class</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rMv"></span></div></div>
  </div>
</div>
<p class="fig-note">At a 6&nbsp;K operating ΔT with a decent 0.1&nbsp;K matched sensor pair, the metering uncertainty is about <strong>2.8&nbsp;%</strong> — on a 10&nbsp;M invoice, <strong>0.28&nbsp;M a year</strong> of pure measurement uncertainty. Let the ΔT fall to 4&nbsp;K and it rises to 3.8&nbsp;%; use ordinary 0.2&nbsp;K sensors instead of a matched pair and it roughly doubles again. Two conclusions follow, and both are cheap at design stage: specify a <strong>matched sensor pair</strong> to the standard the contract cites and install them in the correct pockets, and remember that <strong>protecting ΔT improves the accuracy of your own bill</strong> as well as its size. A meter is not a commodity item on a district connection; it is the instrument that decides what you pay for twenty years.</p>

<h2 id="pressure">6 · Pressure, transients and the interface</h2>
<ul class="clean">
  <li><strong>Rate the primary side for the network, not the building.</strong> District networks run at high pressure and are subject to transients from pumping stations kilometres away. Get the network's maximum operating and test pressures in writing and rate the primary side, the exchanger and the meter accordingly.</li>
  <li><strong>Rate the secondary side for the building's own static.</strong> In a tall tower the ETS often sits at the bottom, where the building-side static is highest — see the zoning discussion in <a href="chilled-water-pumps-tall-buildings.html">chilled-water pumps</a>.</li>
  <li><strong>Protect against transients.</strong> A large primary control valve closing quickly against a long network main is a water-hammer source; specify closure times and check them, and coordinate with the network operator.</li>
  <li><strong>Provide isolation that lets you work.</strong> Double isolation and a drain on the primary, so the ETS can be serviced without the network operator attending, and a bypass arrangement if the contract allows it.</li>
  <li><strong>Agree the boundary in writing.</strong> Who owns the meter, who owns the strainer, who may operate the primary valves, and what the response time is when the network fails — these are design-stage decisions that end up in the O&amp;M and in disputes.</li>
</ul>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Give the flow meter its straight lengths.</strong> The commonest metering error on site is an elbow immediately upstream. Reserve the upstream and downstream straight runs on the drawing and defend them in coordination — they are usually 10D and 5D but check the meter's own requirement.</li>
  <li><strong>Install the sensor pair in the specified pockets</strong>, fully immersed, with the pockets in the correct locations relative to the exchanger and the meter, and keep the pair together — a matched pair separated during installation is no longer matched.</li>
  <li><strong>Flush before the exchanger is connected.</strong> Commission the building side to a stated cleanliness standard with temporary spool pieces in place of the plate pack; a new plate pack fouled by construction debris starts life with a widened approach it never recovers from.</li>
  <li><strong>Record the approach at commissioning</strong> and trend it. A rising approach is the single best early indicator of fouling, and it will move before anyone notices a ΔT problem.</li>
  <li><strong>Commission the ΔT, not just the flow.</strong> Verify the return temperature at the ETS across the load range, and trend it against the contract from day one — the first year's data is what you will need if the ΔT clause is ever disputed.</li>
  <li><strong>Alarm on ΔT.</strong> A BMS alarm on sustained low return temperature turns a slow financial leak into an actionable event. It is one line of logic and it is almost never there.</li>
  <li><strong>Keep the plate pack accessible</strong> and record the tightened dimension of the pack; over-tightening a gasketed exchanger to stop a leak is how plates get crushed.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Design at a wide ΔT and defend it</strong> — two-port valves, no bypasses, coils selected for the contract ΔT, valve authority checked.</li>
  <li><strong>Use pressure-independent control valves</strong> on the primary and at the terminals.</li>
  <li><strong>Buy the closer approach</strong> — it is cheaper than the coil area and fan energy it saves.</li>
  <li><strong>Rate each side for its own pressure regime</strong>, with the network's figures obtained in writing.</li>
  <li><strong>Specify a matched sensor pair and a properly installed flow meter</strong>, to the standard the contract cites.</li>
  <li><strong>Reserve the meter's straight lengths</strong> on the drawing.</li>
  <li><strong>Provide strainers with DP monitoring</strong> and consider side-stream filtration.</li>
  <li><strong>Trend approach and ΔT from handover</strong>, with a BMS alarm on sustained low return temperature.</li>
  <li><strong>Write the operational boundary down</strong> — ownership, access, isolation and failure response.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A district connection converts ΔT from an efficiency metric into a <strong>contractual quantity with a price</strong>: deliver 4&nbsp;K where you promised 8&nbsp;K and the capacity charge doubles for identical cooling. So design wide, use pressure-independent valves so the return temperature is actually controlled, and buy the <strong>closer heat-exchanger approach</strong> — because the 1.5&nbsp;K you save on plates comes back as 15&nbsp;% more coil area in every room in the tower. Then treat the meter as the cash register it is: a matched sensor pair, its straight lengths reserved on the drawing, and the approach and return temperature trended and alarmed from the day the building opens.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>District Cooling Guide</em>, 2nd ed. — network design, energy transfer stations, ΔT management and customer interface.</li>
  <li>International District Energy Association (IDEA) — district cooling best practice, contracting models and delta-T requirements.</li>
  <li>EN 1434 / OIML R75 — heat and cooling meters: accuracy classes, matched temperature sensor pairs and installation requirements.</li>
  <li>Taylor, S.T. <em>Degrading Chilled Water Plant Delta-T: Causes and Mitigation</em>, ASHRAE Transactions — the mechanisms behind low-ΔT syndrome.</li>
  <li>ASHRAE <em>Handbook — HVAC Systems and Equipment</em>, District Heating and Cooling chapter; and the Heat Exchangers chapter for plate exchanger selection and fouling.</li>
  <li>Saudi Building Code <em>SBC 501</em> and the Saudi regulatory framework for district cooling services and metering.</li>
  <li>CIBSE <em>CP1 Heat Networks: Code of Practice</em> and CIBSE <em>Guide B</em> — substation design, metering and commissioning practice transferable to cooling networks.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — pressure zoning of the building side and interface location in tall buildings.</li>
</ol>

<div class="tags">#DistrictCooling #EnergyTransferStation #ETS #TallBuildings #MegatallBuildings #DeltaT #LowDeltaT #CapacityCharge #Tariff #PlateHeatExchanger #Approach #Fouling #PICV #ValveAuthority #BTUMeter #EnergyMetering #EN1434 #MatchedSensorPair #Uncertainty #Commissioning #SideStreamFiltration #WaterHammer #PressureRating #ASHRAE #IDEA #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const CP=4.187;

/* ---------- CHART 1 : delta-T penalty ---------- */
const sL=document.getElementById('sL'),sDd=document.getElementById('sDd'),
      sDa=document.getElementById('sDa'),sC=document.getElementById('sC');
const flow=(MW,dT)=>MW*1000/(CP*dT);
let dtChart=new Chart(document.getElementById('dtChart'),{
  data:{datasets:[
    {type:'line',label:'Contracted flow (L/s)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Capacity charge (× design)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your building',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:2.5,max:14,reverse:true,title:{display:true,text:'Achieved ΔT (K)  —  worse to the right',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Contracted flow (L/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Capacity charge multiplier',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updDt(){
  const L=+sL.value,dd=+sDd.value,da=+sDa.value,C=+sC.value;
  document.getElementById('vL').textContent=fmt1(L)+' MW';
  document.getElementById('vDd').textContent=fmt1(dd)+' K';
  document.getElementById('vDa').textContent=fmt1(da)+' K';
  document.getElementById('vC').textContent=fmt1(C)+' M';
  const xs=[];for(let x=2.5;x<=14;x+=0.1)xs.push(+x.toFixed(1));
  dtChart.data.datasets[0].data=xs.map(x=>({x:x,y:+flow(L,x).toFixed(1)}));
  dtChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(dd/x).toFixed(3)}));
  const Qd=flow(L,dd), Qa=flow(L,da);
  dtChart.data.datasets[2].data=[{x:da,y:+Qa.toFixed(1)}];
  dtChart.update('none');
  const infl=Qa/Qd-1;
  document.getElementById('rQd').innerHTML=fmt0(Qd)+' <small>L/s</small>';
  document.getElementById('rQa').innerHTML=fmt0(Qa)+' <small>L/s</small>';
  document.getElementById('rFi').innerHTML=fmt0(100*infl)+' <small>%</small>';
  document.getElementById('rEc').innerHTML=fmt2(C*infl)+' <small>M/yr</small>';
  const v=document.getElementById('rVd');
  if(infl<=0.02)      v.innerHTML='<span class="badge good">meeting the contract</span>';
  else if(infl<=0.20) v.innerHTML='<span class="badge warn">drifting</span>';
  else                v.innerHTML='<span class="badge bad">paying twice for nothing</span>';
}
[sL,sDd,sDa,sC].forEach(s=>s.addEventListener('input',updDt));updDt();

/* ---------- CHART 2 : approach & coil area ---------- */
const sPs=document.getElementById('sPs'),sAp=document.getElementById('sAp'),
      sSd=document.getElementById('sSd'),sRf=document.getElementById('sRf');
const T_ROOM=24, T_OFF=13;
function lmtd(sup,dT){
  const d1=T_ROOM-sup, d2=T_OFF-(sup+dT);
  if(d1<=0||d2<=0||Math.abs(d1-d2)<1e-6) return Math.max(0.1,(d1+d2)/2);
  return (d1-d2)/Math.log(d1/d2);
}
let apChart=new Chart(document.getElementById('apChart'),{
  data:{datasets:[
    {type:'line',label:'Coil area factor',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Secondary supply (°C)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your ETS',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0.3,max:4,title:{display:true,text:'Heat-exchanger approach (K)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0.8,title:{display:true,text:'Coil area factor (× reference)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',title:{display:true,text:'Secondary supply (°C)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updAp(){
  const ps=+sPs.value,ap=+sAp.value,sd=+sSd.value,rf=+sRf.value;
  document.getElementById('vPs').textContent=fmt1(ps)+' °C';
  document.getElementById('vAp').textContent=fmt1(ap)+' K';
  document.getElementById('vSd').textContent=fmt1(sd)+' K';
  document.getElementById('vRf').textContent=fmt1(rf)+' °C';
  const ref=lmtd(rf,sd);
  const xs=[];for(let x=0.3;x<=4;x+=0.05)xs.push(+x.toFixed(2));
  apChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(ref/lmtd(ps+x,sd)).toFixed(3)}));
  apChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(ps+x).toFixed(2)}));
  const sec=ps+ap, L=lmtd(sec,sd), fac=ref/L;
  apChart.data.datasets[2].data=[{x:ap,y:+fac.toFixed(3)}];
  apChart.update('none');
  document.getElementById('rSs').innerHTML=fmt1(sec)+' <small>°C</small>';
  document.getElementById('rSr').innerHTML=fmt1(sec+sd)+' <small>°C</small>';
  document.getElementById('rLm').innerHTML=fmt1(L)+' <small>K</small>';
  document.getElementById('rCa').innerHTML=fmt2(fac)+'<small>×</small>';
  const v=document.getElementById('rAv');
  if(fac<=1.03)      v.innerHTML='<span class="badge good">coils unaffected</span>';
  else if(fac<=1.15) v.innerHTML='<span class="badge warn">coils grow</span>';
  else               v.innerHTML='<span class="badge bad">buy a closer approach</span>';
}
[sPs,sAp,sSd,sRf].forEach(s=>s.addEventListener('input',updAp));updAp();

/* ---------- CHART 3 : metering uncertainty ---------- */
const sMd=document.getElementById('sMd'),sSe=document.getElementById('sSe'),
      sFe=document.getElementById('sFe'),sBl=document.getElementById('sBl');
const unc=(dT,eT,eQ)=>Math.sqrt(eQ*eQ+Math.pow(Math.SQRT2*eT/dT*100,2));
let mtrChart=new Chart(document.getElementById('mtrChart'),{
  data:{datasets:[
    {type:'line',label:'Total metering uncertainty',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Flow meter alone',data:[],borderColor:'#1b4f72',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your meter',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:2,max:14,title:{display:true,text:'Operating ΔT (K)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Energy measurement uncertainty (%)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt2(c.parsed.y)} % at ΔT ${fmt1(c.parsed.x)} K`}}}}
});
function updMtr(){
  const dT=+sMd.value,eT=+sSe.value,eQ=+sFe.value,bill=+sBl.value;
  document.getElementById('vMd').textContent=fmt1(dT)+' K';
  document.getElementById('vSe').textContent=fmt2(eT)+' K';
  document.getElementById('vFe').textContent=fmt1(eQ)+' %';
  document.getElementById('vBl').textContent=fmt1(bill)+' M';
  const xs=[];for(let x=2;x<=14;x+=0.1)xs.push(+x.toFixed(1));
  mtrChart.data.datasets[0].data=xs.map(x=>({x:x,y:+unc(x,eT,eQ).toFixed(3)}));
  mtrChart.data.datasets[1].data=xs.map(x=>({x:x,y:eQ}));
  const u=unc(dT,eT,eQ);
  mtrChart.data.datasets[2].data=[{x:dT,y:+u.toFixed(3)}];
  mtrChart.update('none');
  document.getElementById('rTe').innerHTML=fmt2(Math.SQRT2*eT/dT*100)+' <small>%</small>';
  document.getElementById('rTu').innerHTML=fmt2(u)+' <small>%</small>';
  document.getElementById('rMo').innerHTML=fmt2(bill*u/100)+' <small>M/yr</small>';
  document.getElementById('rM4').innerHTML=fmt2(unc(4,eT,eQ))+' <small>%</small>';
  const v=document.getElementById('rMv');
  if(u<=2)      v.innerHTML='<span class="badge good">tight</span>';
  else if(u<=4) v.innerHTML='<span class="badge warn">acceptable</span>';
  else          v.innerHTML='<span class="badge bad">uncertainty is costing you</span>';
}
[sMd,sSe,sFe,sBl].forEach(s=>s.addEventListener('input',updMtr));updMtr();

window.addEventListener('load',function(){try{dtChart.resize();apChart.resize();mtrChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='district-cooling-ets-tall-buildings', cat='hvac', mins=16,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='District Cooling &amp; Energy Transfer Stations for Megatall Buildings: Delta-T, Approach &amp; Metering',
    reg_title='District Cooling & Energy Transfer Stations for Megatall Buildings: Delta-T, Approach & Metering',
    reg_tag='HVAC · District Cooling · ETS',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; District Cooling &middot; Energy Transfer Station &middot; Megatall',
    desc='District cooling and energy transfer station design for megatall buildings: why a district connection turns delta-T from an efficiency metric into a contractual quantity with a price, the capacity charge penalty from a degraded return temperature, plate heat exchanger approach and the coil area it costs, pressure-independent control valves, BTU metering uncertainty and why the temperature sensors dominate at low delta-T, and the pressure interface — with three interactive charts and installation tricks.',
    og_desc='Deliver 4 K where you promised 8 K and the district cooling capacity charge doubles for identical cooling. Plus the heat-exchanger approach you pay for twice, and why the meter is the cash register.',
    ld_desc='A design-perspective guide to district cooling connections and energy transfer stations in megatall buildings: delta-T as a contractual quantity, capacity charge penalties, plate heat exchanger approach and coil area, pressure-independent control valves, energy metering uncertainty, and the pressure and transient interface.',
    img_alt='Technical cutaway of a district cooling energy transfer station at the base of a megatall tower, showing plate heat exchangers separating the district network from the building circuit, primary control valves, strainers and a BTU meter, with the building risers leaving upward',
    en_tag='HVAC &amp; Cooling &middot; District Cooling &middot; ETS &middot; Megatall',
    en_title='District Cooling &amp; Energy Transfer Stations for Megatall Buildings: Delta-T, Approach &amp; Metering',
    en_excerpt='Connecting a tower to a district network does not simplify the design &mdash; it replaces a plant you control with a contract you cannot renegotiate, and &Delta;T stops being an efficiency metric and becomes a bill. Deliver 4&nbsp;K where you promised 8&nbsp;K and the <strong>capacity charge doubles</strong> for identical cooling. The heat-exchanger approach you pay for twice (1.5&nbsp;K saved on plates comes back as 15&nbsp;% more coil area in every room), pressure-independent valves, and why at low &Delta;T the temperature sensors &mdash; not the flow meter &mdash; dominate what you pay &mdash; with three interactive charts.',
    en_search='district cooling energy transfer station ETS tall buildings megatall delta-T low delta-T return temperature capacity charge demand charge consumption charge tariff contract penalty contracted flow plate heat exchanger approach fouling plate pack gasket pressure independent control valve PICV valve authority two port three port bypass decoupler BTU meter energy meter EN 1434 OIML R75 matched sensor pair Pt100 flow meter accuracy straight lengths electromagnetic ultrasonic measurement uncertainty network pressure transient water hammer strainer side stream filtration commissioning trending alarm ASHRAE district cooling guide IDEA CIBSE CP1 MEP building services HVAC',
    ar_title='التبريد المركزي ومحطات نقل الطاقة للمباني فائقة الارتفاع: فرق الحرارة والاقتراب والعدادات',
    ar_excerpt='ربط البرج بشبكة تبريد مركزي لا يبسّط التصميم — بل يستبدل محطةً تتحكم بها بعقدٍ لا يمكنك إعادة التفاوض عليه، ويتحوّل فرق الحرارة من مؤشر كفاءة إلى فاتورة. سلّم ٤ كلفن حيث وعدت بثمانية، <strong>وتتضاعف رسوم السعة</strong> مقابل التبريد نفسه. وفرق اقتراب المبادل الذي تدفع ثمنه مرتين (توفير ١٫٥ كلفن في الصفائح يعود ١٥٪ زيادة في مساحة الملفات بكل غرفة)، والصمامات المستقلة عن الضغط، ولماذا تهيمن حساسات الحرارة — لا عداد التدفق — على ما تدفعه عند فروق الحرارة المنخفضة — مع ثلاثة رسوم تفاعلية.',
    ar_search='district cooling energy transfer station ETS delta-T capacity charge plate heat exchanger approach PICV BTU meter EN 1434 matched sensor pair uncertainty commissioning IDEA التبريد المركزي محطة نقل الطاقة المباني الشاهقة المباني فائقة الارتفاع فرق درجات الحرارة درجة حرارة العودة رسوم السعة رسوم الاستهلاك التعرفة العقد الغرامة التدفق المتعاقد عليه المبادل الحراري الصفائحي فرق الاقتراب الاتساخ حزمة الصفائح الحشية الصمام المستقل عن الضغط سلطة الصمام صمام ثنائي المسار ثلاثي المسار مسار التجاوز صمام الفصل عداد الطاقة الحرارية زوج الحساسات المتطابق دقة عداد التدفق الأطوال المستقيمة العداد الكهرومغناطيسي بالموجات فوق الصوتية عدم اليقين في القياس ضغط الشبكة العابر المطرقة المائية المصفاة الترشيح الجانبي التشغيل والاختبار التتبع الإنذار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
