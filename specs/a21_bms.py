# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A megatall tower has somewhere around <strong>30,000 control points</strong>. That number is not a detail — it is an architectural constraint, because the field networks that carry them do not scale gracefully. Put 500 points on a single BACnet MS/TP trunk and a full poll cycle takes <strong>3.6 seconds</strong>: fine for a room temperature, useless for a damper the fire strategy depends on, and disastrous for any control loop that needs to be stable. A 150-floor building needs on the order of <strong>ninety separate field segments</strong>, and how they are grouped, where they terminate and what rides on which one is a decision that has to be made in the concept design alongside the mechanical zoning — not left to the controls contractor after the risers are cast.</p>

<h2 id="why">1 · What makes a tower's controls different</h2>
<ul class="clean">
  <li><strong>Sheer point count.</strong> Thirty thousand points is a small industrial plant, not a building. Naming conventions, graphics, alarm philosophy and database structure all have to be designed rather than accumulated.</li>
  <li><strong>The field bus is a physical, distance-limited network.</strong> BACnet MS/TP over RS-485 has a hard device limit per segment and a shared-token bandwidth that degrades with every device added. Ethernet risers and floor-level IP controllers are what make a tower work.</li>
  <li><strong>Life-safety interfaces are real-time.</strong> Smoke control, stair pressurisation, lift recall and generator changeover cannot wait for a poll cycle, and in most codes they cannot depend on the BMS at all — they interface with it.</li>
  <li><strong>Phased handover means phased commissioning of the head end.</strong> The system must be operable, alarm-managed and trending for occupied lower floors while the upper zones are still being installed.</li>
  <li><strong>The building will outlive several generations of software.</strong> Open protocols, documented point lists and an owned database are what determine whether the system can be maintained in twenty years or has to be ripped out.</li>
</ul>

<h2 id="int-points">2 · Interactive: point count and network segmentation</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Points, devices and field network segments</div>
    <div class="fsub">BACnet MS/TP allows 32 devices per segment without repeaters (127 addresses maximum). Segment count is the minimum implied by the device count; practical designs use fewer devices per trunk to protect response time.</div>
  </div>
  <div class="chart-box"><canvas id="ptChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Floors <span id="vF">150</span></label>
      <input type="range" id="sF" min="20" max="200" value="150" step="5">
      <div class="hint">Occupied floors carrying field devices.</div>
    </div>
    <div class="ctrl">
      <label>Points per floor <span id="vP">200</span></label>
      <input type="range" id="sP" min="60" max="500" value="200" step="10">
      <div class="hint">VAV boxes, FCUs, valves, sensors, meters and lighting interfaces.</div>
    </div>
    <div class="ctrl">
      <label>Devices per floor <span id="vD">12</span></label>
      <input type="range" id="sD" min="2" max="40" value="12" step="1">
      <div class="hint">Physical controllers on the field bus.</div>
    </div>
    <div class="ctrl">
      <label>Devices per segment <span id="vS">20</span></label>
      <input type="range" id="sS" min="8" max="32" value="20" step="1">
      <div class="hint">Design limit. The code allows 32; using fewer protects the poll cycle.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Total points</div><div class="v" id="rTp">30,000</div></div>
    <div class="cell"><div class="k">Field devices</div><div class="v" id="rDv">1,800</div></div>
    <div class="cell"><div class="k">Field segments</div><div class="v" id="rSg">90</div></div>
    <div class="cell"><div class="k">Points per segment</div><div class="v" id="rPs">333</div></div>
    <div class="cell"><div class="k">Architecture</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rAv"></span></div></div>
  </div>
</div>
<p class="fig-note">A 150-floor tower at 200 points and 12 devices per floor is <strong>30,000 points on 1,800 devices</strong>, needing at least <strong>90 field segments</strong>. That is the number that decides the architecture: ninety RS-485 trunks cannot all be home-run to a basement head end, so the system becomes <strong>an IP backbone up the riser with floor- or zone-level IP controllers</strong>, each hosting a short local field bus. Design that hierarchy to match the mechanical zoning — one network zone per mechanical zone — so that a zone can be commissioned, isolated and handed over independently, which is exactly what <a href="mep-commissioning-tall-buildings.html">phased commissioning</a> requires.</p>

<h2 id="int-poll">3 · Interactive: why the field bus is the bottleneck</h2>
<p>MS/TP is a token-passing bus: every device gets the token in turn, and the time to poll everything scales linearly with what is on the trunk. That poll cycle is the response time of every control loop that crosses it.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Field bus poll cycle against points per trunk</div>
    <div class="fsub">Cycle time ≈ points × bytes per transaction × 8 / baud rate, with an allowance for token passing overhead. The dashed line is the response time your slowest acceptable control loop needs.</div>
  </div>
  <div class="chart-box"><canvas id="pollChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Points on the trunk <span id="vN">500</span></label>
      <input type="range" id="sN" min="50" max="1500" value="500" step="10">
      <div class="hint">Total points polled across all devices on one segment.</div>
    </div>
    <div class="ctrl">
      <label>Baud rate <span id="vB">76800</span></label>
      <input type="range" id="sB" min="0" max="3" value="3" step="1">
      <div class="hint">MS/TP runs at 9600, 19200, 38400 or 76800 baud. Use the highest every device supports.</div>
    </div>
    <div class="ctrl">
      <label>Bytes per transaction <span id="vBy">60</span></label>
      <input type="range" id="sBy" min="30" max="150" value="60" step="5">
      <div class="hint">Request plus response, including framing and token overhead.</div>
    </div>
    <div class="ctrl">
      <label>Required response <span id="vR">2.0 s</span></label>
      <input type="range" id="sR" min="0.2" max="10" value="2" step="0.1">
      <div class="hint">Slowest acceptable loop response on this trunk.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Poll cycle</div><div class="v" id="rPc">3.59 <small>s</small></div></div>
    <div class="cell"><div class="k">Max points allowed</div><div class="v" id="rMp">278</div></div>
    <div class="cell"><div class="k">Trunks needed</div><div class="v" id="rTn">2</div></div>
    <div class="cell"><div class="k">At 9600 baud</div><div class="v" id="rSl">28.7 <small>s</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rPv"></span></div></div>
  </div>
</div>
<p class="fig-note">Five hundred points on a 76,800-baud trunk gives a <strong>3.6-second</strong> poll cycle — acceptable for space temperature, marginal for a pressure loop, and unacceptable for anything that has to act. Drop the baud rate to 9,600, which one legacy device on the trunk can force, and the same trunk takes <strong>29 seconds</strong>: a single incompatible device destroys the performance of everything sharing the bus with it. Two rules follow. <strong>Specify the minimum baud rate every device must support</strong>, and <strong>keep life-safety and fast loops off the shared field bus entirely</strong> — hardwired or on IP, never behind a token queue.</p>

<h2 id="lifesafety">4 · The life-safety boundary</h2>
<p>The most consequential architectural decision in a tower's controls is what the BMS is <em>allowed</em> to do:</p>
<ul class="clean">
  <li><strong>Fire detection and alarm is a separate, listed system.</strong> It signals the BMS; it does not depend on it. In most codes the fire system must be able to execute its cause-and-effect matrix with the BMS entirely out of service.</li>
  <li><strong>Smoke control actuation should be hardwired or on a listed network.</strong> Damper and fan commands that form part of the fire strategy must not traverse a shared field bus whose response time depends on how many VAV boxes somebody added later.</li>
  <li><strong>The BMS provides monitoring and normal-mode control</strong>, and hands over cleanly on alarm. Design the handover explicitly, including what happens on restoration, which is the case nobody tests.</li>
  <li><strong>Lift, generator and fire pump interfaces</strong> are status-and-command boundaries with their own contractors; define every signal, its direction and its failure state in an interface matrix issued at design, not negotiated on site.</li>
  <li><strong>Security and access control interact with egress.</strong> Fail-safe versus fail-secure on every door is a life-safety decision documented in the same matrix.</li>
</ul>

<h2 id="int-trend">5 · Interactive: trending, and how much data that is</h2>
<p>A building you cannot see is a building you cannot improve. Trending is what makes every diagnostic in this whole series possible — the approach temperature in <a href="water-treatment-building-systems.html">water treatment</a>, the return temperature in <a href="district-cooling-ets-tall-buildings.html">district cooling</a>, the door differential in <a href="stack-effect-tall-buildings.html">stack effect</a> — and it has to be specified, sized and paid for.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Trend data volume by sample interval and retention</div>
    <div class="fsub">Samples = points × (60/interval) × 8760 per year; storage at the stated bytes per sample including timestamp and quality flag. Change-of-value logging reduces this substantially for slow points.</div>
  </div>
  <div class="chart-box"><canvas id="trChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Trended points <span id="vTp">30000</span></label>
      <input type="range" id="sTp" min="1000" max="60000" value="30000" step="1000">
      <div class="hint">Not every point needs trending — but every point you will ever be asked about does.</div>
    </div>
    <div class="ctrl">
      <label>Sample interval <span id="vSi">15 min</span></label>
      <input type="range" id="sSi" min="1" max="60" value="15" step="1">
      <div class="hint">15 minutes suits energy analysis; 1 minute is needed for control diagnostics.</div>
    </div>
    <div class="ctrl">
      <label>Retention <span id="vRt">10 yr</span></label>
      <input type="range" id="sRt" min="1" max="25" value="10" step="1">
      <div class="hint">Long retention is what lets you compare this summer with the first one.</div>
    </div>
    <div class="ctrl">
      <label>Bytes per sample <span id="vBs">16</span></label>
      <input type="range" id="sBs" min="8" max="64" value="16" step="1">
      <div class="hint">Value plus timestamp plus quality, before compression.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Samples per year</div><div class="v" id="rSy">1.05 <small>G</small></div></div>
    <div class="cell"><div class="k">Storage per year</div><div class="v" id="rSt">16.8 <small>GB</small></div></div>
    <div class="cell"><div class="k">Over retention</div><div class="v" id="rSr">168 <small>GB</small></div></div>
    <div class="cell"><div class="k">At 1-minute</div><div class="v" id="rS1">252 <small>GB/yr</small></div></div>
    <div class="cell"><div class="k">Assessment</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rTv"></span></div></div>
  </div>
</div>
<p class="fig-note">Thirty thousand points at fifteen-minute intervals is <strong>16.8&nbsp;GB a year</strong> — <strong>168&nbsp;GB over a ten-year retention</strong>, which is nothing. Even one-minute sampling on every point is 252&nbsp;GB a year, still trivial against the value it delivers. <strong>There is no technical reason to trend sparsely, and the usual reasons given are commercial rather than real.</strong> Specify comprehensive trending with long retention from day one, because the data you did not collect in year one is the data you will want in year five when somebody asks why the building uses more than it did. Use change-of-value logging for slow points to cut the volume without losing the record.</p>

<h2 id="metering">6 · Metering — the part that has to be designed, not added</h2>
<ul class="clean">
  <li><strong>Meter to a hierarchy that closes.</strong> Utility intake, then plant, then zone, then tenant. Every level should sum to the level above within a stated tolerance; if it does not, the discrepancy is either a meter fault or a load nobody knows about — and both are worth finding.</li>
  <li><strong>Sub-metering coverage is the single number that determines whether energy management is possible.</strong> Below about half the load metered, most consumption is unattributable and any efficiency claim is speculation.</li>
  <li><strong>Meter thermal energy as well as electricity.</strong> Cooling delivered per zone is what exposes the low-ΔT problems that this series keeps returning to, and it is what makes tenant recharging fair.</li>
  <li><strong>Match the meter to the contract.</strong> Where meters are used for billing they must meet the relevant accuracy class and be installed with the straight lengths and matched sensor pairs the standard requires — the point made in <a href="district-cooling-ets-tall-buildings.html">district cooling</a> applies to every tenant meter too.</li>
  <li><strong>Give every meter a network path and a name</strong> in the same convention as the rest of the system. A meter that has to be read by walking to it will be read once a year at best.</li>
</ul>

<h2 id="install">7 · Design, installation &amp; handover</h2>
<ul class="clean">
  <li><strong>Design the naming convention before the first controller is ordered.</strong> Building, zone, system, equipment, point — consistent, machine-parsable and documented. Thirty thousand inconsistently named points is a building that cannot be analysed, and renaming later is a project in itself.</li>
  <li><strong>Write the alarm philosophy.</strong> Priorities, routing, suppression during known conditions and a limit on the alarms an operator can receive per hour. An unmanaged system generates thousands of alarms a day and is then ignored entirely — which is worse than having none.</li>
  <li><strong>Specify open protocols and an owned database.</strong> Insist on documented point lists, exportable trend data and no proprietary lock on the graphics or the database schema. This is the clause that decides whether the system can be maintained or must be replaced.</li>
  <li><strong>Segregate the network properly</strong> — controls on their own VLAN, no direct internet exposure, remote access through a managed gateway, and a documented patching responsibility. A BMS is an OT network and should be treated as one.</li>
  <li><strong>Commission the sequences, not the points.</strong> Point-to-point checks prove wiring; only a functional test against the written sequence of operation proves control. Require the sequences as a written deliverable and test against them.</li>
  <li><strong>Hand over the model, the database and the trends</strong> — not just drawings. The single most useful handover artefact is an exportable, documented point database with a year of trend data behind it.</li>
  <li><strong>Plan for the head end to outlive its software.</strong> Budget a software refresh at ten to fifteen years and make sure the field devices will survive it.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Estimate the point count early</strong> and design the network hierarchy to match the mechanical zoning.</li>
  <li><strong>Keep field trunks short</strong> and specify a minimum baud rate for every device.</li>
  <li><strong>Keep life safety off the shared bus</strong>, with an interface matrix issued at design.</li>
  <li><strong>Design the naming convention and alarm philosophy</strong> as deliverables.</li>
  <li><strong>Trend comprehensively with long retention</strong> — the storage is trivial.</li>
  <li><strong>Meter to a hierarchy that closes</strong>, thermal as well as electrical.</li>
  <li><strong>Specify open protocols, exportable data and an owned database.</strong></li>
  <li><strong>Treat the network as OT</strong> — segregated, managed and patched.</li>
  <li><strong>Commission against written sequences</strong>, zone by zone, and hand over the database and the trends.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Thirty thousand points is a small industrial plant, and the field networks that carry them do not scale: <strong>500 points on one MS/TP trunk is a 3.6-second poll cycle</strong>, and a single legacy device forcing 9,600 baud makes it twenty-nine. So the architecture is an <strong>IP backbone with zone-level controllers whose boundaries match the mechanical zoning</strong>, life safety kept off the shared bus entirely, and short field trunks with a specified minimum baud rate. Then spend the effort on the three things that decide whether the building can be managed for sixty years: a <strong>designed naming convention</strong>, a <strong>metering hierarchy that closes</strong>, and <strong>comprehensive trending with long retention</strong> — which costs 168&nbsp;GB over a decade and is the only reason any of the diagnostics in this series are possible at all.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ANSI/ASHRAE Standard 135 — <em>BACnet: A Data Communication Protocol for Building Automation and Control Networks</em>, including MS/TP physical layer limits and device addressing.</li>
  <li>ASHRAE <em>Guideline 13 — Specifying Building Automation Systems</em>, and Guideline 36 for high-performance sequences of operation.</li>
  <li>ISO 16484 series — building automation and control systems: hardware, functions, project specification and commissioning.</li>
  <li>ANSI/ASHRAE/IES Standard 90.1 — metering, monitoring and control requirements; and ASHRAE Standard 224 / Guideline 36 for sequence standardisation.</li>
  <li>CIBSE <em>Guide H — Building Control Systems</em> and CIBSE TM39 <em>Building Energy Metering</em>.</li>
  <li>IEC 62443 — industrial communication network security, applied to building operational technology networks.</li>
  <li>EN 1434 / OIML R75 for thermal energy meters, and IEC 62053 for electricity meter accuracy classes.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — controls architecture and phased handover in tall buildings.</li>
</ol>

<div class="tags">#BMS #BuildingAutomation #Controls #BACnet #MSTP #ASHRAE135 #Guideline36 #TallBuildings #MegatallBuildings #PointCount #NetworkArchitecture #IPBackbone #PollCycle #BaudRate #LifeSafetyInterface #CauseAndEffect #InterfaceMatrix #Trending #DataRetention #ChangeOfValue #Metering #SubMetering #ThermalMetering #EN1434 #NamingConvention #AlarmPhilosophy #OTSecurity #IEC62443 #Commissioning #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};

/* ---------- CHART 1 : points & segments ---------- */
const sF=document.getElementById('sF'),sP=document.getElementById('sP'),
      sD=document.getElementById('sD'),sS=document.getElementById('sS');
let ptChart=new Chart(document.getElementById('ptChart'),{
  data:{datasets:[
    {type:'line',label:'Total points',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Field segments',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your tower',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:20,max:200,title:{display:true,text:'Floors',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Total control points',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Field network segments',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updPt(){
  const F=+sF.value,P=+sP.value,D=+sD.value,S=+sS.value;
  document.getElementById('vF').textContent=F;
  document.getElementById('vP').textContent=P;
  document.getElementById('vD').textContent=D;
  document.getElementById('vS').textContent=S;
  const xs=[];for(let x=20;x<=200;x+=5)xs.push(x);
  ptChart.data.datasets[0].data=xs.map(x=>({x:x,y:x*P}));
  ptChart.data.datasets[1].data=xs.map(x=>({x:x,y:Math.ceil(x*D/S)}));
  ptChart.data.datasets[2].data=[{x:F,y:F*P}];
  ptChart.update('none');
  const pts=F*P, dev=F*D, seg=Math.ceil(dev/S);
  document.getElementById('rTp').textContent=fmt0(pts);
  document.getElementById('rDv').textContent=fmt0(dev);
  document.getElementById('rSg').textContent=fmt0(seg);
  document.getElementById('rPs').textContent=fmt0(pts/seg);
  const v=document.getElementById('rAv');
  if(seg<=6)       v.innerHTML='<span class="badge good">flat network is viable</span>';
  else if(seg<=30) v.innerHTML='<span class="badge warn">IP backbone needed</span>';
  else             v.innerHTML='<span class="badge bad">zone controllers on an IP riser</span>';
}
[sF,sP,sD,sS].forEach(s=>s.addEventListener('input',updPt));updPt();

/* ---------- CHART 2 : poll cycle ---------- */
const sN=document.getElementById('sN'),sB=document.getElementById('sB'),
      sBy=document.getElementById('sBy'),sR=document.getElementById('sR');
const BAUDS=[9600,19200,38400,76800];
const cycle=(n,baud,by)=>n*by*8/baud*1.15;   // 15% token overhead
let pollChart=new Chart(document.getElementById('pollChart'),{
  data:{datasets:[
    {type:'line',label:'Poll cycle at your baud rate',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'At 9600 baud',data:[],borderColor:'#1b4f72',borderWidth:2.2,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your trunk',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:50,max:1500,title:{display:true,text:'Points on one field trunk',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Full poll cycle (s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt2(c.parsed.y)} s at ${fmt0(c.parsed.x)} points`}},
      annotation:{annotations:{
        req:{type:'line',scaleID:'y',yScaleID:'y',value:2,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'required response',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updPoll(){
  const n=+sN.value,bi=+sB.value,by=+sBy.value,req=+sR.value;
  const baud=BAUDS[bi];
  document.getElementById('vN').textContent=n;
  document.getElementById('vB').textContent=baud;
  document.getElementById('vBy').textContent=by;
  document.getElementById('vR').textContent=fmt1(req)+' s';
  const xs=[];for(let x=50;x<=1500;x+=10)xs.push(x);
  pollChart.data.datasets[0].data=xs.map(x=>({x:x,y:+cycle(x,baud,by).toFixed(3)}));
  pollChart.data.datasets[1].data=xs.map(x=>({x:x,y:+cycle(x,9600,by).toFixed(3)}));
  pollChart.data.datasets[2].data=[{x:n,y:+cycle(n,baud,by).toFixed(3)}];
  pollChart.options.plugins.annotation.annotations.req.value=req;
  pollChart.options.scales.y.max=Math.max(cycle(1500,baud,by)*1.05,req*2);
  pollChart.update('none');
  const t=cycle(n,baud,by);
  const maxPts=Math.floor(req*baud/(by*8*1.15));
  document.getElementById('rPc').innerHTML=fmt2(t)+' <small>s</small>';
  document.getElementById('rMp').textContent=fmt0(maxPts);
  document.getElementById('rTn').textContent=Math.max(1,Math.ceil(n/Math.max(maxPts,1)));
  document.getElementById('rSl').innerHTML=fmt1(cycle(n,9600,by))+' <small>s</small>';
  const v=document.getElementById('rPv');
  if(t<=req*0.5)   v.innerHTML='<span class="badge good">comfortable</span>';
  else if(t<=req)  v.innerHTML='<span class="badge warn">at the limit</span>';
  else             v.innerHTML='<span class="badge bad">split the trunk</span>';
}
[sN,sB,sBy,sR].forEach(s=>s.addEventListener('input',updPoll));updPoll();

/* ---------- CHART 3 : trend storage ---------- */
const sTp=document.getElementById('sTp'),sSi=document.getElementById('sSi'),
      sRt=document.getElementById('sRt'),sBs=document.getElementById('sBs');
const samplesYr=(p,iv)=>p*(60/iv)*24*365;
let trChart=new Chart(document.getElementById('trChart'),{
  data:{datasets:[
    {type:'line',label:'Storage per year (GB)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Over the retention period (GB)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your system',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:1,max:60,reverse:true,title:{display:true,text:'Sample interval (minutes)  —  finer to the right',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'logarithmic',title:{display:true,text:'Storage (GB, log scale)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} GB at ${fmt0(c.parsed.x)} min`}}}}
});
function updTr(){
  const p=+sTp.value,iv=+sSi.value,rt=+sRt.value,B=+sBs.value;
  document.getElementById('vTp').textContent=fmt0(p);
  document.getElementById('vSi').textContent=iv+' min';
  document.getElementById('vRt').textContent=rt+' yr';
  document.getElementById('vBs').textContent=B;
  const gbYr=x=>samplesYr(p,x)*B/1e9;
  const xs=[];for(let x=1;x<=60;x+=1)xs.push(x);
  trChart.data.datasets[0].data=xs.map(x=>({x:x,y:+gbYr(x).toFixed(3)}));
  trChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(gbYr(x)*rt).toFixed(3)}));
  trChart.data.datasets[2].data=[{x:iv,y:+gbYr(iv).toFixed(3)}];
  trChart.update('none');
  document.getElementById('rSy').innerHTML=fmt2(samplesYr(p,iv)/1e9)+' <small>G</small>';
  document.getElementById('rSt').innerHTML=fmt1(gbYr(iv))+' <small>GB</small>';
  document.getElementById('rSr').innerHTML=fmt0(gbYr(iv)*rt)+' <small>GB</small>';
  document.getElementById('rS1').innerHTML=fmt0(gbYr(1))+' <small>GB/yr</small>';
  const v=document.getElementById('rTv'), tb=gbYr(iv)*rt/1000;
  if(tb<1)      v.innerHTML='<span class="badge good">trivial — trend everything</span>';
  else if(tb<5) v.innerHTML='<span class="badge good">easily affordable</span>';
  else          v.innerHTML='<span class="badge warn">use change-of-value logging</span>';
}
[sTp,sSi,sRt,sBs].forEach(s=>s.addEventListener('input',updTr));updTr();

window.addEventListener('load',function(){try{ptChart.resize();pollChart.resize();trChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='bms-controls-architecture-tall-buildings', cat='tallmep', mins=14,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='BMS &amp; Controls Architecture for Megatall Buildings: Point Count, Field Networks &amp; Trending',
    reg_title='BMS & Controls Architecture for Megatall Buildings: Point Count, Field Networks & Trending',
    reg_tag='Tall-Building Systems · BMS · Controls',
    breadcrumb='Tall-Building Systems',
    tag_line='Tall-Building Systems &middot; BMS &middot; Controls &middot; Metering',
    desc='BMS and controls architecture for megatall buildings: why 30,000 points and 90 field segments force an IP backbone with zone-level controllers, how field bus poll cycles limit what can share a trunk, keeping life safety off the shared network, trend data volume and why comprehensive trending is effectively free, metering hierarchies that close, and the naming and alarm philosophy that decide whether the building can be managed — with three interactive charts.',
    og_desc='500 points on one BACnet MS/TP trunk is a 3.6-second poll cycle, and one legacy device forcing 9,600 baud makes it 29 seconds. That is why a tower needs an IP backbone with zone-level controllers.',
    ld_desc='A design-perspective guide to BMS and controls architecture in megatall buildings: point count and network segmentation, field bus poll cycle limits, the life-safety interface boundary, trend data volume and retention, metering hierarchy, naming conventions and alarm philosophy.',
    img_alt='Technical diagram of a megatall tower control network showing an IP backbone rising through the core, zone-level controllers on each mechanical floor, and short field bus trunks branching to controllers on the occupied floors',
    en_tag='Tall-Building Systems &middot; BMS &middot; Controls &middot; Metering',
    en_title='BMS &amp; Controls Architecture for Megatall Buildings: Point Count, Field Networks &amp; Trending',
    en_excerpt='A megatall tower has around <strong>30,000 control points</strong>, and the field networks that carry them do not scale gracefully. Five hundred points on one BACnet MS/TP trunk is a <strong>3.6-second poll cycle</strong>; let a single legacy device force 9,600 baud and it becomes twenty-nine. A 150-floor building needs roughly <strong>ninety field segments</strong>, which is why the architecture must be an IP backbone with zone-level controllers matching the mechanical zoning. Plus the life-safety boundary, trending that costs 168&nbsp;GB a decade, and metering hierarchies that close &mdash; with three interactive charts.',
    en_search='BMS building management system building automation controls architecture tall buildings megatall point count field devices BACnet MS/TP RS-485 segment limit 32 devices 127 addresses baud rate 9600 76800 poll cycle token passing response time IP backbone zone controller network hierarchy mechanical zoning life safety interface fire alarm cause and effect hardwired listed network smoke control damper actuation lift recall generator changeover interface matrix trending sample interval retention change of value data volume storage metering hierarchy sub-metering thermal energy meter EN 1434 tenant billing naming convention alarm philosophy alarm flood open protocol owned database OT security VLAN IEC 62443 sequence of operation Guideline 36 functional testing commissioning handover MEP building services',
    ar_title='أنظمة إدارة المباني والتحكم في المباني فائقة الارتفاع: عدد النقاط والشبكات الميدانية والتتبع',
    ar_excerpt='البرج فائق الارتفاع يحتوي على نحو <strong>٣٠٠٠٠ نقطة تحكم</strong>، والشبكات الميدانية التي تحملها لا تتوسّع بسلاسة. خمسمئة نقطة على خط BACnet MS/TP واحد تعني <strong>دورة استطلاع ٣٫١ ثانية</strong>، وإذا فرض جهاز قديم واحد سرعة ٩٦٠٠ تصبح خمسًا وعشرين ثانية. مبنى من ١٥٠ طابقًا يحتاج نحو <strong>تسعين قطاعًا ميدانيًا</strong>، ولهذا يجب أن تكون البنية شبكة IP رأسية مع متحكمات لكل منطقة تطابق التقسيم الميكانيكي — مع ثلاثة رسوم تفاعلية.',
    ar_search='BMS building automation controls BACnet MS/TP poll cycle IP backbone zone controller life safety interface trending metering sub-metering naming convention alarm philosophy OT security IEC 62443 Guideline 36 نظام إدارة المباني أتمتة المباني بنية التحكم المباني الشاهقة المباني فائقة الارتفاع عدد النقاط الأجهزة الميدانية بروتوكول باكنت الشبكة التسلسلية حد الأجهزة لكل قطاع سرعة النقل دورة الاستطلاع تمرير الرمز زمن الاستجابة الشبكة الرأسية متحكم المنطقة تسلسل الشبكة التقسيم الميكانيكي واجهة سلامة الأرواح إنذار الحريق مصفوفة السبب والنتيجة التوصيل السلكي المباشر التحكم في الدخان تشغيل المخمدات استدعاء المصاعد تبديل المولدات مصفوفة الواجهات التتبع فترة أخذ العينات مدة الاحتفاظ التسجيل عند التغير حجم البيانات التخزين تسلسل العدادات العدادات الفرعية عداد الطاقة الحرارية فوترة المستأجرين اصطلاح التسمية فلسفة الإنذارات طوفان الإنذارات البروتوكول المفتوح قاعدة البيانات المملوكة أمن الشبكات التشغيلية تسلسل التشغيل الاختبار الوظيفي التسليم MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
