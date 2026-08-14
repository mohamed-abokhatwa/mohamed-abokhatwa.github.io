# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Standby generators and diesel fire pumps are the systems that only matter on the day everything else has failed — and both of them run on a fuel that has to be stored in quantity, moved vertically through occupied floors, and kept ready for years without degrading. A 5&nbsp;MW generator set with 24 hours of autonomy needs <strong>26&nbsp;m³ of diesel — 22 tonnes</strong> — and if the generators sit on a high mechanical floor rather than in the basement, the transfer system has to push that fuel up a riser against <strong>25&nbsp;bar of static head at 300&nbsp;m</strong>. Every one of those facts is a fire-safety constraint before it is a mechanical one, which is why fuel systems in tall buildings are governed less by pump selection than by where the code will let you put the tank.</p>

<h2 id="why">1 · Why fuel is different from every other service</h2>
<ul class="clean">
  <li><strong>It is a fuel load inside the building.</strong> Twenty-odd tonnes of diesel is a substantial fire load with its own compartmentation, ventilation, containment and detection requirements, and its location is normally fixed by code rather than by convenience.</li>
  <li><strong>The riser is a hazard, not a utility.</strong> A fuel line running vertically through a tower must be protected, contained, monitored for leaks and capable of being isolated remotely — nothing like a water riser.</li>
  <li><strong>Quantities in occupied areas are capped.</strong> Codes limit how much fuel may sit at the equipment, which is why the system is almost always <strong>bulk storage plus small day tanks</strong> rather than one large tank at the plant.</li>
  <li><strong>It must work after years of standing still.</strong> Diesel degrades, absorbs water, and grows microbial contamination. A generator that has never failed a monthly test can still fail on fuel that has been sitting since handover.</li>
  <li><strong>Two independent duties.</strong> Standby generators and diesel fire pumps have different code bases, different autonomy requirements and, usually, must not share a fuel supply in a way that lets one exhaust the other.</li>
</ul>

<h2 id="int-storage">2 · Interactive: how much fuel, and how much it weighs</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Bulk fuel storage volume and mass vs autonomy</div>
    <div class="fsub">Consumption taken at a specific fuel rate per kWh generated, at the assumed load factor. Mass at a diesel density of 840 kg/m³. Bund volume at 110 % of the largest tank.</div>
  </div>
  <div class="chart-box"><canvas id="storChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Generator capacity <span id="vP">5.0 MW</span></label>
      <input type="range" id="sP" min="0.5" max="20" value="5" step="0.5">
      <div class="hint">Total standby generation to be sustained.</div>
    </div>
    <div class="ctrl">
      <label>Load factor <span id="vL">80 %</span></label>
      <input type="range" id="sL" min="30" max="100" value="80" step="5">
      <div class="hint">Average load during the outage. Sizing at 100 % is usually over-conservative.</div>
    </div>
    <div class="ctrl">
      <label>Specific consumption <span id="vC">0.27 L/kWh</span></label>
      <input type="range" id="sC" min="0.2" max="0.35" value="0.27" step="0.005">
      <div class="hint">Modern medium-speed diesel sets run 0.24–0.29 L/kWh at high load.</div>
    </div>
    <div class="ctrl">
      <label>Required autonomy <span id="vH">24 h</span></label>
      <input type="range" id="sH" min="4" max="96" value="24" step="2">
      <div class="hint">Set by code, by the client&rsquo;s risk appetite and by how quickly fuel can be delivered.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Consumption</div><div class="v" id="rLh">1,080 <small>L/h</small></div></div>
    <div class="cell"><div class="k">Storage volume</div><div class="v" id="rV">25.9 <small>m³</small></div></div>
    <div class="cell"><div class="k">Mass of fuel</div><div class="v" id="rM">21.8 <small>t</small></div></div>
    <div class="cell"><div class="k">Bund volume</div><div class="v" id="rB">28.5 <small>m³</small></div></div>
    <div class="cell"><div class="k">Tanker loads</div><div class="v" id="rT">0.9</div></div>
  </div>
</div>
<p class="fig-note">A 5&nbsp;MW set at 80&nbsp;% load burns <strong>1,080&nbsp;L/h</strong>, so 24 hours is <strong>25.9&nbsp;m³ and nearly 22 tonnes</strong> of fuel, in a bunded room, with a 28.5&nbsp;m³ containment. Two design points that get missed. First, the <strong>load factor matters more than the generator rating</strong> — sizing storage at 100&nbsp;% load when the real standby demand is 60&nbsp;% buys nearly double the tank for nothing. Second, look at the tanker readout: autonomy is only meaningful if fuel can actually be delivered, so the real design question is not "how many hours" but "how long until a tanker can reach the site and discharge", which in a city centre after a regional event may be considerably longer than the tank.</p>

<h2 id="int-riser">3 · Interactive: pushing fuel up the tower</h2>
<p>Generators are increasingly placed on high mechanical floors — for exhaust dispersion, for shorter electrical runs, and because basement space is scarce. That turns fuel transfer into a vertical pumping problem with a fire-safety overlay.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Fuel riser static pressure and transfer pump duty</div>
    <div class="fsub">Static pressure = ρgh at a diesel density of 840 kg/m³. Transfer pump sized to refill the day tank within a set period while the set is running at full consumption.</div>
  </div>
  <div class="chart-box"><canvas id="riserChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Generator floor height <span id="vZ">300 m</span></label>
      <input type="range" id="sZ" min="10" max="700" value="300" step="10">
      <div class="hint">Height of the generator plant above the bulk tank.</div>
    </div>
    <div class="ctrl">
      <label>Day tank capacity <span id="vD">2000 L</span></label>
      <input type="range" id="sD" min="200" max="5000" value="2000" step="100">
      <div class="hint">Often capped by code for tanks inside a building. Check the local limit before designing.</div>
    </div>
    <div class="ctrl">
      <label>Refill time <span id="vR">15 min</span></label>
      <input type="range" id="sR" min="5" max="60" value="15" step="1">
      <div class="hint">Time to refill the day tank from empty while the set runs.</div>
    </div>
    <div class="ctrl">
      <label>Consumption <span id="vQ">1080 L/h</span></label>
      <input type="range" id="sQ" min="100" max="4000" value="1080" step="20">
      <div class="hint">From the previous chart.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Static pressure</div><div class="v" id="rS">24.7 <small>bar</small></div></div>
    <div class="cell"><div class="k">Transfer duty</div><div class="v" id="rQd">9.1 <small>m³/h</small></div></div>
    <div class="cell"><div class="k">Pump power</div><div class="v" id="rPw">11.3 <small>kW</small></div></div>
    <div class="cell"><div class="k">Day tank runtime</div><div class="v" id="rRt">1.9 <small>h</small></div></div>
    <div class="cell"><div class="k">Pressure class</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rPc"></span></div></div>
  </div>
</div>
<p class="fig-note">Lifting diesel to a 300&nbsp;m mechanical floor is <strong>24.7&nbsp;bar</strong> of static pressure — a PN40 riser and PN40 valves for a flammable liquid running through occupied floors. Note the day-tank runtime: at 2,000&nbsp;L and 1,080&nbsp;L/h the set has <strong>under two hours</strong> before it needs the transfer pumps, so those pumps are as safety-critical as the generator itself and must be on the essential board, duplicated, and proven during the monthly test rather than assumed. Above about 200&nbsp;m the honest answer is often <strong>intermediate tanks at zone breaks</strong> — the same cascade logic as fire water in <a href="firefighting-tall-buildings.html">firefighting in megatall buildings</a> — which keeps every section inside a sane pressure class at the cost of more tanks to permit, bund and monitor.</p>

<h2 id="daytank">4 · Day tanks, transfer and the control that matters</h2>
<ul class="clean">
  <li><strong>Size the day tank on code first, runtime second.</strong> Many jurisdictions cap the quantity permitted at the equipment inside a building; that cap, not the runtime you would like, sets the tank.</li>
  <li><strong>Duplicate the transfer pumps and their power.</strong> Duty and standby, both on the essential supply, with automatic changeover on failure to achieve level — the failure that matters is not the pump, it is the pump that did not start.</li>
  <li><strong>Prevent overfill mechanically, not just electrically.</strong> A high-level float switch plus an independent overfill prevention device plus an overflow returning by gravity to the bulk tank. Relying on a single level probe is how a mechanical floor gets flooded with diesel.</li>
  <li><strong>Design the return leg.</strong> Engines return more fuel than they burn; the return must go somewhere thermally sensible and must not pressurise the day tank or push hot fuel back into the bulk store.</li>
  <li><strong>Fit remote isolation.</strong> A remotely operated shut-off at the bulk tank and at each floor served, operable from the fire command centre, is required by most codes and is worth having regardless.</li>
  <li><strong>Contain the riser.</strong> Double-wall pipe or a contained duct with leak detection over the full height, draining to a monitored point — a single-skin fuel line in a shaft is not acceptable in a tall building.</li>
</ul>

<h2 id="int-fire">5 · Interactive: the diesel fire pump's own fuel</h2>
<p>Diesel-driven fire pumps have their own, entirely separate rule. NFPA&nbsp;20 sizes the base tank from the engine's rated power — roughly <strong>5.07 litres per rated horsepower plus 5&nbsp;%</strong> — and that tank must be dedicated, not shared with the generators<sup class="cite">[2]</sup>.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Diesel fire pump fuel tank and run time</div>
    <div class="fsub">NFPA 20 base tank = 1 US gallon (3.785 L) per rated hp, plus 5 % for expansion and sump. Note the common slip: 5.07 L is the same rule expressed per <em>kilowatt</em>, and applying it per horsepower over-sizes the tank by a third. Confirm the exact expansion and sump allowance against the edition of NFPA 20 your project cites. Run time from the engine&rsquo;s consumption at full load.</div>
  </div>
  <div class="chart-box"><canvas id="fpChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Engine rated power <span id="vFh">300 hp</span></label>
      <input type="range" id="sFh" min="50" max="800" value="300" step="10">
      <div class="hint">Rated horsepower of the fire pump driver.</div>
    </div>
    <div class="ctrl">
      <label>Consumption <span id="vFc">0.21 L/hp·h</span></label>
      <input type="range" id="sFc" min="0.15" max="0.30" value="0.21" step="0.005">
      <div class="hint">Full-load fuel rate of the diesel driver.</div>
    </div>
    <div class="ctrl">
      <label>Required run time <span id="vFr">8 h</span></label>
      <input type="range" id="sFr" min="2" max="24" value="8" step="1">
      <div class="hint">Set by the fire strategy and the authority; 8 h is a common minimum.</div>
    </div>
    <div class="ctrl">
      <label>Number of pump sets <span id="vFn">4</span></label>
      <input type="range" id="sFn" min="1" max="10" value="4" step="1">
      <div class="hint">One per pressure zone in a zoned megatall standpipe system.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">NFPA 20 base tank</div><div class="v" id="rFb">1,192 <small>L</small></div></div>
    <div class="cell"><div class="k">Run time on base tank</div><div class="v" id="rFt">18.9 <small>h</small></div></div>
    <div class="cell"><div class="k">Needed for run time</div><div class="v" id="rFn2">504 <small>L</small></div></div>
    <div class="cell"><div class="k">Total, all sets</div><div class="v" id="rFa">4,769 <small>L</small></div></div>
    <div class="cell"><div class="k">Governing</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rFv"></span></div></div>
  </div>
</div>
<p class="fig-note">A 300&nbsp;hp fire pump driver takes a <strong>1,192&nbsp;L</strong> base tank under the NFPA&nbsp;20 rule, which at 0.21&nbsp;L/hp·h is nearly <strong>19 hours</strong> of running — far more than the eight hours the fire strategy asks for. That is deliberate: the rule is a prescriptive minimum designed to remove judgement, and in a zoned megatall with a pump set per zone it means <strong>four separate dedicated tanks totalling 4,800&nbsp;L</strong>, each with its own bund, fill point, level monitoring and weekly test regime. Do not attempt to consolidate them into one tank serving several pump rooms — the whole point of the rule is that each set is independent of every other system in the building.</p>

<h2 id="quality">6 · Fuel that has been standing for five years</h2>
<p>The commonest cause of a standby system failing is not the machine, it is the fuel. Diesel in a rarely used tank degrades in three ways at once, and all three are designed against rather than maintained against:</p>
<ul class="clean">
  <li><strong>Water accumulates</strong> from condensation in the tank headspace and from deliveries. Water at the tank bottom is where microbial growth lives. Provide a proper sump, a low-point drain that somebody can actually reach, and a water-detection alarm.</li>
  <li><strong>Microbial contamination</strong> — "diesel bug" — grows at the fuel-water interface and produces sludge that blocks filters, usually on the second or third hour of the outage rather than at start-up.</li>
  <li><strong>Oxidation and gum formation</strong>, accelerated by heat and by copper. Biodiesel blends are markedly worse: FAME content absorbs water and degrades faster, and in some regions the pump-grade fuel now contains it whether you specify it or not.</li>
  <li><strong>The design responses</strong> are a fuel polishing system that circulates and filters the bulk store on a timer, tank geometry that lets water collect where it can be drained, breather driers on the tank vents, and periodic sampling and testing written into the O&amp;M with action limits.</li>
  <li><strong>Test under load.</strong> A monthly no-load run proves the starter battery. It does not prove the fuel, the transfer pumps, the day-tank controls or the cooling — those need a periodic load-bank or building-load test, and that test is where fuel problems reveal themselves harmlessly.</li>
</ul>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Fix the tank locations with the fire engineer before the basement is laid out.</strong> Fuel room location, fire rating, ventilation, access and the tanker fill route are code-driven and almost impossible to move later.</li>
  <li><strong>Bund everything to 110&nbsp;% of the largest tank</strong>, with the bund drained to a monitored, valved point that is normally closed — an open bund drain is not a bund.</li>
  <li><strong>Put the fill point where a tanker can actually stand</strong>, with the hose run, the spill kit, the overfill alarm audible at the tanker and a lockable cap. This is coordinated with the traffic engineer, not with the plant room.</li>
  <li><strong>Double-contain and leak-detect the riser</strong> over its full height, with the interstitial space monitored and alarmed.</li>
  <li><strong>Separate fuel from everything hot and everything electrical</strong> in shafts and plant rooms, and fire-stop every penetration to the rated standard.</li>
  <li><strong>Commission the whole chain under load</strong> — bulk tank to transfer pump to day tank to engine, with level controls, overfill protection, remote isolation and the alarm path all proven, at load, not at idle.</li>
  <li><strong>Label and document the isolation points</strong> and put the fuel schematic on the wall of the fire command centre.</li>
  <li><strong>Write the fuel management regime into the O&amp;M</strong>: sampling frequency, polishing schedule, water-drain interval, action limits and who is responsible.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Establish the code constraints first</strong> — permitted quantities, tank locations, day-tank caps, separation.</li>
  <li><strong>Size storage on realistic load factor and on delivery logistics</strong>, not on generator rating alone.</li>
  <li><strong>Decide generator location knowing the fuel consequence</strong> — a high plant floor means a high-pressure fuel riser or intermediate tanks.</li>
  <li><strong>Duplicate transfer pumps on essential power</strong> with automatic changeover.</li>
  <li><strong>Provide independent overfill protection</strong> and a gravity overflow route.</li>
  <li><strong>Keep fire pump fuel entirely separate</strong> and size it to NFPA 20 per set.</li>
  <li><strong>Design for fuel quality</strong> — polishing, water drainage, breather driers, sampling.</li>
  <li><strong>Double-contain and monitor the riser</strong>, with remote isolation.</li>
  <li><strong>Commission the whole chain at load</strong> and test periodically at load thereafter.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Fuel is a <strong>fire-safety system that happens to involve pumps</strong>: 24 hours of autonomy on a 5&nbsp;MW set is 26&nbsp;m³ and 22 tonnes of diesel in a bunded, rated, ventilated room whose location the code chooses, not you. Put the generators on a high mechanical floor and the riser carries <strong>25&nbsp;bar of flammable liquid through occupied space</strong>, which means double containment, leak detection, remote isolation and — above roughly 200&nbsp;m — intermediate tanks at the zone breaks. Keep the fire pumps' fuel completely separate and size it to the prescriptive rule. And design against the thing that actually causes standby systems to fail: not the machine, but <strong>five-year-old diesel with water in the bottom of the tank</strong>, which is beaten by polishing, drainage and periodic testing under real load.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>NFPA 110 — <em>Standard for Emergency and Standby Power Systems</em>: fuel supply, day tanks, run time classes and testing regimes.</li>
  <li>NFPA 20 — <em>Standard for the Installation of Stationary Pumps for Fire Protection</em>: diesel driver fuel tank sizing, dedicated supply and weekly testing.</li>
  <li>NFPA 30 — <em>Flammable and Combustible Liquids Code</em>, and NFPA 37 for stationary combustion engines: permitted quantities, tank location, containment and separation.</li>
  <li>International Fire Code / Saudi Building Code <em>SBC 801</em> — storage of combustible liquids in buildings, fuel rooms and remote shut-off requirements.</li>
  <li>BS 5410 and the UK Oil Firing Technical Association (OFTEC) guidance — oil supply installations, bunding and fill point arrangements.</li>
  <li>EN 590 and ASTM D975 — diesel fuel specifications; and ASTM D6469 / IP guidance on microbial contamination and fuel storage stability.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — generator and fuel plant location in tall buildings.</li>
  <li>Engine manufacturers&rsquo; installation manuals — fuel supply and return temperature limits, lift limits and day tank arrangements.</li>
</ol>

<div class="tags">#FuelOil #DieselStorage #StandbyGenerators #EmergencyPower #NFPA110 #NFPA20 #NFPA30 #FirePumps #TallBuildings #MegatallBuildings #DayTank #FuelTransfer #FuelRiser #StaticHead #DoubleContainment #LeakDetection #RemoteIsolation #Bunding #Overfill #FuelPolishing #DieselBug #FuelQuality #FAME #LoadBankTesting #EssentialPower #Commissioning #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const RHO_D=840, G9=9.81;

/* ---------- CHART 1 : bulk storage ---------- */
const sP=document.getElementById('sP'),sL=document.getElementById('sL'),
      sC=document.getElementById('sC'),sH=document.getElementById('sH');
let storChart=new Chart(document.getElementById('storChart'),{
  data:{datasets:[
    {type:'line',label:'Storage volume (m³)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Fuel mass (t)',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your design',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:4,max:96,title:{display:true,text:'Required autonomy (hours)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Storage volume (m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Fuel mass (tonnes)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updStor(){
  const P=+sP.value,L=+sL.value/100,C=+sC.value,H=+sH.value;
  document.getElementById('vP').textContent=fmt1(P)+' MW';
  document.getElementById('vL').textContent=fmt0(L*100)+' %';
  document.getElementById('vC').textContent=fmt2(C)+' L/kWh';
  document.getElementById('vH').textContent=H+' h';
  const lph=P*1000*L*C;
  const vol=h=>lph*h/1000;
  const xs=[];for(let h=4;h<=96;h+=2)xs.push(h);
  storChart.data.datasets[0].data=xs.map(h=>({x:h,y:+vol(h).toFixed(2)}));
  storChart.data.datasets[1].data=xs.map(h=>({x:h,y:+(vol(h)*RHO_D/1000).toFixed(2)}));
  storChart.data.datasets[2].data=[{x:H,y:+vol(H).toFixed(2)}];
  storChart.update('none');
  const V=vol(H);
  document.getElementById('rLh').innerHTML=fmt0(lph)+' <small>L/h</small>';
  document.getElementById('rV').innerHTML=fmt1(V)+' <small>m³</small>';
  document.getElementById('rM').innerHTML=fmt1(V*RHO_D/1000)+' <small>t</small>';
  document.getElementById('rB').innerHTML=fmt1(V*1.1)+' <small>m³</small>';
  document.getElementById('rT').textContent=fmt1(V/30);
}
[sP,sL,sC,sH].forEach(s=>s.addEventListener('input',updStor));updStor();

/* ---------- CHART 2 : riser ---------- */
const sZ=document.getElementById('sZ'),sD=document.getElementById('sD'),
      sR=document.getElementById('sR'),sQ=document.getElementById('sQ');
let riserChart=new Chart(document.getElementById('riserChart'),{
  data:{datasets:[
    {type:'line',label:'Static pressure (bar)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'scatter',label:'Your generator floor',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:10,max:700,title:{display:true,text:'Generator floor above the bulk tank (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Static pressure in the fuel riser (bar)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      annotation:{annotations:{
        pn16:{type:'line',scaleID:'y',yScaleID:'y',value:16,borderColor:'#1e8449',borderWidth:1.4,borderDash:[5,4],label:{display:true,content:'PN16',position:'start',font:{size:10,family:'DM Sans'},color:'#1e8449',backgroundColor:'rgba(255,255,255,0.85)'}},
        pn40:{type:'line',scaleID:'y',yScaleID:'y',value:40,borderColor:'#b9770e',borderWidth:1.4,borderDash:[5,4],label:{display:true,content:'PN40',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updRiser(){
  const z=+sZ.value,d=+sD.value,r=+sR.value,q=+sQ.value;
  document.getElementById('vZ').textContent=z+' m';
  document.getElementById('vD').textContent=d+' L';
  document.getElementById('vR').textContent=r+' min';
  document.getElementById('vQ').textContent=q+' L/h';
  const xs=[];for(let x=10;x<=700;x+=10)xs.push(x);
  riserChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(RHO_D*G9*x/1e5).toFixed(2)}));
  const P=RHO_D*G9*z/1e5;
  riserChart.data.datasets[1].data=[{x:z,y:+P.toFixed(2)}];
  riserChart.update('none');
  const duty=d/r*60/1000+q/1000;      // m3/h to refill while consuming
  const kW=duty/3.6*(P*10.2)/(102*0.55);
  document.getElementById('rS').innerHTML=fmt1(P)+' <small>bar</small>';
  document.getElementById('rQd').innerHTML=fmt1(duty)+' <small>m³/h</small>';
  document.getElementById('rPw').innerHTML=fmt1(kW)+' <small>kW</small>';
  document.getElementById('rRt').innerHTML=fmt1(d/q)+' <small>h</small>';
  const v=document.getElementById('rPc');
  if(P<=16)      v.innerHTML='<span class="badge good">PN16 riser</span>';
  else if(P<=40) v.innerHTML='<span class="badge warn">PN40 riser</span>';
  else           v.innerHTML='<span class="badge bad">stage with intermediate tanks</span>';
}
[sZ,sD,sR,sQ].forEach(s=>s.addEventListener('input',updRiser));updRiser();

/* ---------- CHART 3 : fire pump fuel ---------- */
const sFh=document.getElementById('sFh'),sFc=document.getElementById('sFc'),
      sFr=document.getElementById('sFr'),sFn=document.getElementById('sFn');
const NFPA_L_PER_HP=3.785, NFPA_MARGIN=1.05;   // NFPA 20: 1 US gal (3.785 L) per rated hp — note 5.07 is the per-kW figure
let fpChart=new Chart(document.getElementById('fpChart'),{
  data:{datasets:[
    {type:'line',label:'NFPA 20 base tank (L)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Fuel for the required run time (L)',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your driver',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:50,max:800,title:{display:true,text:'Engine rated power (hp)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Fuel tank capacity (L)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} L at ${fmt0(c.parsed.x)} hp`}}}}
});
function updFp(){
  const hp=+sFh.value,c=+sFc.value,rt=+sFr.value,n=+sFn.value;
  document.getElementById('vFh').textContent=hp+' hp';
  document.getElementById('vFc').textContent=fmt2(c)+' L/hp·h';
  document.getElementById('vFr').textContent=rt+' h';
  document.getElementById('vFn').textContent=n;
  const base=x=>x*NFPA_L_PER_HP*NFPA_MARGIN;
  const need=x=>x*c*rt;
  const xs=[];for(let x=50;x<=800;x+=10)xs.push(x);
  fpChart.data.datasets[0].data=xs.map(x=>({x:x,y:+base(x).toFixed(0)}));
  fpChart.data.datasets[1].data=xs.map(x=>({x:x,y:+need(x).toFixed(0)}));
  fpChart.data.datasets[2].data=[{x:hp,y:+base(hp).toFixed(0)}];
  fpChart.update('none');
  const B=base(hp), N=need(hp);
  document.getElementById('rFb').innerHTML=fmt0(B)+' <small>L</small>';
  document.getElementById('rFt').innerHTML=fmt1(B/(hp*c))+' <small>h</small>';
  document.getElementById('rFn2').innerHTML=fmt0(N)+' <small>L</small>';
  document.getElementById('rFa').innerHTML=fmt0(Math.max(B,N)*n)+' <small>L</small>';
  const v=document.getElementById('rFv');
  if(B>=N) v.innerHTML='<span class="badge good">NFPA rule governs</span>';
  else     v.innerHTML='<span class="badge warn">run time governs — enlarge tank</span>';
}
[sFh,sFc,sFr,sFn].forEach(s=>s.addEventListener('input',updFp));updFp();

window.addEventListener('load',function(){try{storChart.resize();riserChart.resize();fpChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='fuel-oil-systems-tall-buildings', cat='tallmep', mins=14,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Fuel Oil Systems for Generators &amp; Fire Pumps in Megatall Buildings: Storage, Risers &amp; Fuel Quality',
    reg_title='Fuel Oil Systems for Generators & Fire Pumps in Megatall Buildings: Storage, Risers & Fuel Quality',
    reg_tag='Tall-Building Systems · Fuel Oil · Standby Power',
    breadcrumb='Tall-Building Systems',
    tag_line='Tall-Building Systems &middot; Fuel Oil &middot; Standby Generators &middot; Fire Pumps',
    desc='Fuel oil systems for standby generators and diesel fire pumps in megatall buildings: bulk storage volume and mass against realistic load factors, the static pressure in a fuel riser when generators sit on a high mechanical floor, day tanks and transfer pump duty, NFPA 20 dedicated fire pump fuel, double containment and remote isolation, and designing against the fuel degradation that actually causes standby systems to fail — with three interactive charts and installation tricks.',
    og_desc='24 hours of autonomy on a 5 MW set is 26 m3 and 22 tonnes of diesel. Put the generators on a 300 m mechanical floor and the riser carries 25 bar of flammable liquid through occupied space.',
    ld_desc='A design-perspective guide to fuel oil systems in megatall buildings: bulk storage sizing, fuel riser static pressure and staged tanks, day tanks and transfer pumps, NFPA 20 fire pump fuel provision, containment and leak detection, and fuel quality management.',
    img_alt='Technical cutaway of a megatall tower fuel system showing bulk diesel storage tanks in a bunded basement fuel room, a contained fuel riser running up the core, and a day tank feeding standby generators on a high mechanical floor',
    en_tag='Tall-Building Systems &middot; Fuel Oil &middot; Standby Power &middot; Fire Pumps',
    en_title='Fuel Oil Systems for Generators &amp; Fire Pumps in Megatall Buildings: Storage, Risers &amp; Fuel Quality',
    en_excerpt='Standby generators and diesel fire pumps only matter on the day everything else has failed &mdash; and both run on a fuel that must be stored in quantity, moved vertically through occupied floors, and kept ready for years without degrading. A 5&nbsp;MW set with 24 hours of autonomy needs <strong>26&nbsp;m&sup3; &mdash; 22 tonnes</strong> of diesel; put the generators on a 300&nbsp;m mechanical floor and the riser carries <strong>25&nbsp;bar of flammable liquid</strong> through occupied space. Plus NFPA&nbsp;20 dedicated fire pump fuel, and the five-year-old diesel that actually causes standby failures &mdash; with three interactive charts.',
    en_search='fuel oil diesel storage standby generators emergency power fire pumps tall buildings megatall NFPA 110 NFPA 20 NFPA 30 NFPA 37 bulk tank day tank permitted quantity code cap transfer pump duty standby essential power automatic changeover overfill prevention gravity overflow return leg fuel riser static pressure PN16 PN40 intermediate tanks staged double containment double wall pipe leak detection remote isolation shut off bunding 110 percent fill point tanker spill kit fuel polishing water drain breather drier microbial contamination diesel bug FAME biodiesel oxidation gum load bank testing building load test commissioning fire command centre MEP building services',
    ar_title='أنظمة الوقود للمولدات ومضخات الحريق في المباني فائقة الارتفاع: التخزين والمواسير الصاعدة وجودة الوقود',
    ar_excerpt='المولدات الاحتياطية ومضخات الحريق الديزل لا تهم إلا في اليوم الذي يفشل فيه كل شيء آخر — وكلاهما يعمل بوقود يجب تخزينه بكميات كبيرة ونقله رأسيًا عبر طوابق مأهولة وإبقاؤه جاهزًا لسنوات دون أن يتلف. مجموعة ٥ ميغاواط باستقلالية ٢٤ ساعة تحتاج <strong>٢٦ م٣ — أي ٢٢ طنًا</strong> من الديزل، وإذا وُضعت المولدات على طابق ميكانيكي بارتفاع ٣٠٠ متر فإن الماسورة الصاعدة تحمل <strong>٢٥ بارًا من سائل قابل للاشتعال</strong> عبر الفراغات المأهولة — مع ثلاثة رسوم تفاعلية.',
    ar_search='fuel oil diesel storage standby generators fire pumps NFPA 110 NFPA 20 day tank transfer pump fuel riser double containment leak detection fuel polishing diesel bug load bank testing وقود الديزل خزانات الوقود المولدات الاحتياطية الطاقة الطارئة مضخات الحريق المباني الشاهقة المباني فائقة الارتفاع الخزان الرئيسي خزان اليوم الكمية المسموحة حد الكود مضخة النقل التشغيل والاحتياطي الطاقة الأساسية التبديل التلقائي منع الفيض الفائض بالجاذبية خط العودة الماسورة الصاعدة للوقود الضغط الاستاتيكي الخزانات الوسيطة الاحتواء المزدوج الماسورة مزدوجة الجدار كشف التسرب العزل عن بعد صمام الإغلاق الحوض المانع للتسرب نقطة التعبئة الصهريج عدة الانسكاب تنقية الوقود تصريف الماء مجفف التنفيس التلوث الميكروبي حشرة الديزل وقود حيوي الأكسدة اختبار بنك الأحمال التشغيل والاختبار غرفة قيادة الحريق MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
