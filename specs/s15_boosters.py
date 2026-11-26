# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">On a long carrier with an in-line booster, a trip at one station is a surge event at both. We modelled station 1 pumping 8&nbsp;km into the suction of an in-line booster that lifts the flow another 10&nbsp;km to a reservoir. If the booster trips alone, station 1 keeps pushing and the suction main rises to <strong>76&nbsp;m</strong>. If station 1 trips and the booster runs on, the booster empties its own suction main and the pressure there reaches vapour in <strong>9&nbsp;s</strong>. If both trip, both mains separate. A break tank at the booster decouples the two mains, and then each main needs only its own protection: <strong>4.2&nbsp;m&sup3;</strong> of gas at station 1 and <strong>2.8&nbsp;m&sup3;</strong> at the booster keep both lines at or above +3&nbsp;m in every trip. This article works through the scenarios, the interlocks and the choice between in-line boosting and a break tank.</p>

<h2 id="system">1 &middot; The system</h2>
<p>The carrier is DN800 ductile iron with the friction gradient of the series' reference main, 0.70&nbsp;m&sup3;/s and a wave speed of 1,050&nbsp;m/s [1]:</p>
<ul class="clean">
  <li><strong>Station 1</strong> lifts from a 5&nbsp;m suction to 60.0&nbsp;m: __P1__&nbsp;kW at 1,480&nbsp;rpm, inertia __I1__&nbsp;kg&middot;m&sup2; from the correlation (see <a href="pump-trip-data-inertia-specific-speed.html">pump data</a>).</li>
  <li><strong>Main A</strong>, 8&nbsp;km, delivers to the booster at 33.2&nbsp;m.</li>
  <li><strong>The booster</strong> adds 45.3&nbsp;m: __P2__&nbsp;kW, inertia __I2__&nbsp;kg&middot;m&sup2;, with a check valve and a bypass check valve that lets flow pass the stopped pumps when the suction pressure exceeds the discharge pressure.</li>
  <li><strong>Main B</strong>, 10&nbsp;km, delivers to a reservoir at 45.0&nbsp;m.</li>
</ul>
<p>The model is a method-of-characteristics network solver with a vapour cavity model, verified against the series solver to 0.01&nbsp;m; the pumps run down on their inertia with the constant-efficiency torque law [2][3]. The profile is flat, so heads are pressure heads.</p>

<h2 id="coupling">2 &middot; Three trips, two mains</h2>
<p>An in-line booster joins the two mains hydraulically: the flow through main A is the flow through the booster, and so through main B. Any change at either station reaches both mains [4][5].</p>
<ul class="clean">
  <li><strong>Booster trips, station 1 runs on.</strong> The flow through the booster drops, main A decelerates against a station still pumping, and the suction pressure rises until the bypass opens. Main B sees an ordinary downsurge from a stopped pump.</li>
  <li><strong>Station 1 trips, booster runs on.</strong> Main A decelerates, but the booster keeps drawing from it. Its suction pressure falls until the water column separates at the booster and the pump runs into vapour.</li>
  <li><strong>Power failure at both.</strong> Both mains decelerate at once, and the booster's own rundown pulls its suction down further while main A is already falling.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Trips at two stations in series</div>
    <div class="fsub">Upper: pressure head at the booster suction (end of main A) and discharge (start of main B). Lower: minimum and maximum envelopes along both mains, main A from 0 to 8&nbsp;km and main B from 8 to 18&nbsp;km. Network MOC model, vapour cavity model, 100&nbsp;m reaches, 200&nbsp;s.</div>
  </div>
  <div class="chart-box"><canvas id="trChart"></canvas></div>
  <div class="chart-box" style="height:300px;"><canvas id="envChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Trip</label>
      <select id="sSc">
        <option value="s2">Booster trips, station 1 runs on</option>
        <option value="s1" selected>Station 1 trips, booster runs on</option>
        <option value="both">Power failure at both stations</option>
      </select>
      <div class="hint">The three events every series system must pass.</div>
    </div>
    <div class="ctrl">
      <label>Arrangement</label>
      <select id="sAr">
        <option value="inline" selected>In-line booster, no protection</option>
        <option value="tank">Break tank at the booster, no protection</option>
        <option value="ves">Break tank, vessel at each station</option>
      </select>
      <div class="hint">The vessels are sized in section 4.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Main A: lowest</div><div class="v" id="rAmin">&ndash;</div></div>
    <div class="cell"><div class="k">Main A: highest</div><div class="v" id="rAmax">&ndash;</div></div>
    <div class="cell"><div class="k">Main B: lowest</div><div class="v" id="rBmin">&ndash;</div></div>
    <div class="cell"><div class="k">Main B: highest</div><div class="v" id="rBmax">&ndash;</div></div>
    <div class="cell"><div class="k">Booster suction reaches vapour at</div><div class="v" id="rTv">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict at +3.0 m</div><div class="v" style="font-size:14px;margin-top:6px;" id="rVer">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">In-line, the booster trip lifts the suction main to 75.7&nbsp;m while main B dips to 30.1&nbsp;m; the station 1 trip takes the booster suction to vapour after 9.0&nbsp;s; the power failure separates both mains. With a break tank, each main sees only its own station: a station 1 trip affects main A alone (&minus;9.3&nbsp;m, close to vapour), a booster trip affects main B alone (+11.9&nbsp;m). With a vessel at each station the worst minimum on either main is +3.2&nbsp;m, and the vessel's return swing lifts main B to 129.8&nbsp;m, inside the 136&nbsp;m limit of this series.</p>

<h2 id="interlock">3 &middot; The low-suction interlock</h2>
<p>Every in-line booster needs a low-suction trip, to stop it running into vapour when the supply fails. A common instinct is to delay that trip so that a brief dip does not stop the booster. The model shows what the delay does after a station 1 trip [5][6].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Station 1 trips; the booster follows after a delay</div>
    <div class="fsub">In-line arrangement, no protection. Pressure head at the booster suction and discharge for a booster trip delayed after the station 1 trip.</div>
  </div>
  <div class="chart-box"><canvas id="intChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Booster trips after</label>
      <select id="sDl">
        <option value="0">0 s (both together)</option>
        <option value="1">2 s</option>
        <option value="2">5 s</option>
        <option value="3" selected>10 s</option>
        <option value="4">30 s</option>
        <option value="5">Never (runs on)</option>
      </select>
      <div class="hint">Delay of the low-suction trip.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Suction: lowest</div><div class="v" id="rSm">&ndash;</div></div>
    <div class="cell"><div class="k">Suction at vapour from</div><div class="v" id="rSv">&ndash;</div></div>
    <div class="cell"><div class="k">Discharge: lowest</div><div class="v" id="rDm">&ndash;</div></div>
    <div class="cell"><div class="k">Main B: lowest</div><div class="v" id="rBm">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">Whatever the delay, the booster suction separates: run on, the booster drains its suction in 9&nbsp;s; trip it at once and its own rundown, combined with main A's downsurge, separates the suction after about 18&nbsp;s. Main B reaches vapour in every case in which the booster stops. The interlock protects the pump from running dry; it does not protect either main. That needs protection on the mains, which is the subject of the next section.</p>

<h2 id="protect">4 &middot; Decouple, then protect each main</h2>
<p>Protecting an in-line pair is hard because every device interacts with both stations: a vessel at station 1 cannot stop the booster drawing its suction down, and a suction-side vessel at the booster changes the discharge-side response. Our sizing runs with three vessels on the in-line arrangement (station 1, booster suction, booster discharge) did not find a combination that passed all three trips. A break tank (or a reservoir) at the booster removes the coupling: main A discharges into the tank, and the booster lifts from it [4][7]. Each main is then a single pumped main, sized as in <a href="surge-vessel.html">sizing the surge vessel</a>:</p>
<div class="tbl-wrap"><table>
  <caption>Vessels for the decoupled system, sized for the power failure at both stations (+3.0&nbsp;m everywhere), DN400 differential connections</caption>
  <thead><tr><th>Main</th><th class="num">Gas at steady flow (m&sup3;)</th><th class="num">Largest gas volume (m&sup3;)</th><th class="num">Shell at 80&nbsp;% (m&sup3;)</th><th class="num">Lowest (m)</th><th class="num">Highest (m)</th></tr></thead>
  <tbody>
__VROWS__
  </tbody>
</table></div>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Every trip against every arrangement</div>
    <div class="fsub">Lowest pressure head on each main for the three trips and three arrangements, from the same runs as above. Bars below the criterion fail it; bars at &minus;9.8&nbsp;m are vapour.</div>
  </div>
  <div class="chart-box"><canvas id="cmpChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Design minimum <span id="vCr">+3.0 m</span></label>
      <input type="range" id="sCr" min="-5" max="10" value="3" step="0.5">
      <div class="hint">Check it against the project's allowable values.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Combinations passing on both mains</div><div class="v" id="rPass">&ndash;</div></div>
    <div class="cell"><div class="k">Worst combination</div><div class="v" id="rWorst" style="font-size:15px;margin-top:6px;">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">Only the decoupled system with a vessel at each station passes all three trips at +3.0&nbsp;m. Lower the criterion to &minus;3&nbsp;m and nothing else changes: every other arrangement still reaches vapour in at least one trip.</p>

<p>The break tank brings its own costs: a structure, its overflow and level control, a second set of pumps drawing from atmospheric pressure, and the loss of the residual head at the booster (33.2&nbsp;m here), which the booster must then supply. Where the head is too valuable to break, the in-line arrangement must be protected as one system, with suction and discharge devices sized together and checked against all three trips and the interlocks, usually with more conservative devices and faster interlocks.</p>

<h2 id="practice">5 &middot; Points we check on every series system</h2>
<ul class="clean">
  <li><strong>All three trips</strong>: each station alone and both together. A power failure at one site is a common event on long carriers fed from different substations.</li>
  <li><strong>The booster suction</strong> as its own critical point, with its minimum against vapour and the pump's NPSH.</li>
  <li><strong>The bypass</strong> round an in-line booster, and its check valve, modelled; without it a stopped booster dead-ends main A.</li>
  <li><strong>Interlocks</strong> (low suction, high discharge, station-to-station signals) modelled with their real delays, and their purpose stated: protecting the pump, not the main.</li>
  <li><strong>Restarts</strong>: the order of restarting the stations, so that the booster never starts on an empty suction main.</li>
</ul>

<h2 id="hammer">6 &middot; Setting it up in Bentley HAMMER</h2>
<p>Field names differ slightly between versions [8].</p>
<ol>
  <li><strong>Model both stations and both mains</strong> in one model, with the booster's pumps, check valves and bypass explicit, and its suction node at the real elevation.</li>
  <li><strong>Give each pump its own inertia and specific speed</strong>, from data sheets or the correlation.</li>
  <li><strong>Create three trip scenarios</strong> using the pumps' shutdown settings: station 1 alone, the booster alone, both. Add delayed trips for the interlocks with the real delay times.</li>
  <li><strong>Report the booster suction and discharge</strong> as report points, and plot the profile envelopes over both mains.</li>
  <li><strong>For the decoupled option</strong>, model the break tank as a tank at its operating level, and size each main's protection with the other station running and tripped.</li>
  <li><strong>Check every combination</strong> of the final devices against all trips, and the restart order.</li>
</ol>

<h2 id="checklist">7 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Every station trip modelled alone and together</strong>, with the interlocks.</li>
  <li><strong>Booster suction checked</strong> against vapour and NPSH.</li>
  <li><strong>Bypass and check valves</strong> at the booster in the model.</li>
  <li><strong>Interlock purpose and delay</strong> stated, and not relied on for surge protection.</li>
  <li><strong>Decoupling considered</strong> (break tank or reservoir) before protecting an in-line pair as one system.</li>
  <li><strong>Protection checked against all trips</strong>, not only the one it was sized for.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><a href="surge-model-field-validation.html">Validating a surge model with a field pump-trip test</a></li>
    <li><a href="surge-sensitivity-uncertainty.html">Sensitivity and uncertainty: bounding the result</a></li>
    <li><a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip: inertia, specific speed and four-quadrant curves</a></li>
    <li><a href="transient-model-demands-network-detail.html">Demands, branches and dead ends in a transient model</a></li>
    <li><a href="surge-envelope-pipe-pressure-limits.html">Reading the surge envelope against the pipe's real limits</a></li>
    <li><a href="transient-forces-pipe-supports.html">Transient forces on pipe supports and bends</a></li>
    <li><strong>Booster stations in series</strong></li>
    <li><a href="pump-start-stop-vfd-ramp-surge.html">Pump starts, controlled stops and drive ramps</a></li>
    <li><a href="pipeline-filling-draining-restart-surge.html">Filling, draining and restarting a transmission main</a></li>
    <li><a href="wastewater-force-main-surge.html">Surge in wastewater force mains</a></li>
    <li><a href="surge-study-report-review-checklist.html">The surge study report: what to deliver and what a reviewer checks</a></li>
  </ol>
  The protection devices themselves are covered in the <a href="choosing-surge-protection.html">surge protection design series</a>.
</div>
"""

CHARTS = r"""
const D=__DATA__;
const FF="'IBM Plex Sans', system-ui, sans-serif";
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:FF,size:11}}};
const TTL={family:FF,size:12,weight:'600'};
const LBL={size:10,family:FF};
const LEGF={family:FF,size:11.5};
const fmt1=v=>v.toFixed(1), fmt2=v=>v.toFixed(2);
const sgn=(v,d)=>(v<-0.0049?'−':(v>0.0049?'+':''))+Math.abs(v).toFixed(d);
const VAP=-9.8, PMIN=3.0;
const good=t=>'<span class="badge good">'+t+'</span>', bad=t=>'<span class="badge bad">'+t+'</span>';
const hl=(v,txt,col,pos)=>({type:'line',yMin:v,yMax:v,borderColor:col,borderWidth:1.3,borderDash:[6,4],label:{display:true,content:txt,position:pos||'end',font:LBL,color:'#fff',backgroundColor:col}});
/* ---------- CHART 1 : scenarios ---------- */
const sSc=document.getElementById('sSc'), sAr=document.getElementById('sAr');
const trChart=new Chart(document.getElementById('trChart'),{
  data:{datasets:[
    {type:'line',label:'Booster suction (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0},
    {type:'line',label:'Booster discharge (m)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2,pointRadius:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:200,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},y:{type:'linear',min:-15,max:140,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{v:hl(VAP,'vapour','rgba(192,57,43,0.85)'),p:hl(PMIN,'+3.0 m','rgba(30,132,73,0.85)','start')}}}}
});
const envChart=new Chart(document.getElementById('envChart'),{
  data:{datasets:[
    {type:'line',label:'Maximum (m)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2,pointRadius:0},
    {type:'line',label:'Minimum (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:18,title:{display:true,text:'Chainage (km): main A 0–8, main B 8–18',font:TTL},...AX},y:{type:'linear',min:-15,max:140,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} km`}},
      annotation:{annotations:{v:hl(VAP,'vapour','rgba(192,57,43,0.85)'),p:hl(PMIN,'+3.0 m','rgba(30,132,73,0.85)','start'),lim:hl(136,'136 m','rgba(107,79,158,0.85)','start'),
        st:{type:'line',xMin:8,xMax:8,borderColor:'#7f8c8d',borderWidth:1.2,borderDash:[3,3],label:{display:true,content:'booster',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(127,140,141,0.9)'}}}}}}
});
const pick=()=>{const a=sAr.value, s=sSc.value; return a==='ves'?D.vessels[s]:D.sc[s+'_'+a];};
const vtxt=v=>v<=VAP+0.05?' <small>(vapour)</small>':' <small>m</small>';
function upd1(){
  const r=pick();
  trChart.data.datasets[0].data=r.t.map((t,k)=>({x:t,y:r.suc[k]}));
  trChart.data.datasets[1].data=r.t.map((t,k)=>({x:t,y:r.dis[k]}));
  trChart.update('none');
  envChart.data.datasets[0].data=r.x.map((x,k)=>({x:x/1000,y:r.emax[k]}));
  envChart.data.datasets[1].data=r.x.map((x,k)=>({x:x/1000,y:r.emin[k]}));
  envChart.update('none');
  document.getElementById('rAmin').innerHTML=sgn(r.A_min,2)+vtxt(r.A_min);
  document.getElementById('rAmax').innerHTML=fmt1(r.A_max)+' <small>m</small>';
  document.getElementById('rBmin').innerHTML=sgn(r.B_min,2)+vtxt(r.B_min);
  document.getElementById('rBmax').innerHTML=fmt1(r.B_max)+' <small>m</small>';
  document.getElementById('rTv').innerHTML=r.t_vap===null?'<small>does not</small>':fmt1(r.t_vap)+' <small>s</small>';
  const ok=r.A_min>=PMIN&&r.B_min>=PMIN;
  document.getElementById('rVer').innerHTML=ok?good('both mains pass'):bad('fails');
}
[sSc,sAr].forEach(s=>s.addEventListener('input',upd1));upd1();
/* ---------- CHART 2 : interlock delay ---------- */
const sDl=document.getElementById('sDl');
const intChart=new Chart(document.getElementById('intChart'),{
  data:{datasets:[
    {type:'line',label:'Booster suction (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0},
    {type:'line',label:'Booster discharge (m)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2,pointRadius:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:200,title:{display:true,text:'Time after station 1 trips (s)',font:TTL},...AX},y:{type:'linear',min:-15,max:90,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{v:hl(VAP,'vapour','rgba(192,57,43,0.85)'),tr:{type:'line',xMin:0,xMax:0,borderColor:'#6b4f9e',borderWidth:1.4,borderDash:[4,4],label:{display:true,content:'booster trips',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}}}}}
});
function upd2(){
  const c=D.cascade[+sDl.value];
  intChart.data.datasets[0].data=c.t.map((t,k)=>({x:t,y:c.suc[k]}));
  intChart.data.datasets[1].data=c.t.map((t,k)=>({x:t,y:c.dis[k]}));
  const a=intChart.options.plugins.annotation.annotations.tr; a.display=c.delay<1000; a.xMin=c.delay; a.xMax=c.delay;
  intChart.update('none');
  document.getElementById('rSm').innerHTML=sgn(c.suc_min,2)+vtxt(c.suc_min);
  document.getElementById('rSv').innerHTML=c.t_vap===null?'<small>does not</small>':fmt1(c.t_vap)+' <small>s</small>';
  document.getElementById('rDm').innerHTML=sgn(c.dis_min,2)+vtxt(c.dis_min);
  document.getElementById('rBm').innerHTML=sgn(c.B_min,2)+vtxt(c.B_min);
}
sDl.addEventListener('input',upd2);upd2();
/* ---------- CHART 3 : comparison ---------- */
const sCr=document.getElementById('sCr');
const COMBOS=[];[['inline','In-line'],['tank','Break tank'],['ves','Tank + vessels']].forEach(([a,al])=>[['s2','booster trips'],['s1','station 1 trips'],['both','both trip']].forEach(([s,sl])=>{
  const r=a==='ves'?D.vessels[s]:D.sc[s+'_'+a]; COMBOS.push({lab:al+', '+sl,A:r.A_min,B:r.B_min});}));
const cmpChart=new Chart(document.getElementById('cmpChart'),{
  data:{labels:COMBOS.map(c=>c.lab),datasets:[
    {type:'bar',label:'Main A lowest (m)',data:COMBOS.map(c=>c.A),backgroundColor:'#1b4f72',borderWidth:0},
    {type:'bar',label:'Main B lowest (m)',data:COMBOS.map(c=>c.B),backgroundColor:'#b9770e',borderWidth:0}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,indexAxis:'y',
    scales:{x:{type:'linear',min:-12,max:50,title:{display:true,text:'Lowest pressure head (m)',font:TTL},...AX},y:{...AX,ticks:{font:{family:FF,size:10.5}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt2(c.parsed.x)} m`}},
      annotation:{annotations:{crit:{type:'line',xMin:3,xMax:3,borderColor:'#1e8449',borderWidth:1.6,borderDash:[6,4],label:{display:true,content:'+3.0 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}}}}}}
});
function upd3(){
  const cr=+sCr.value; document.getElementById('vCr').textContent=sgn(cr,1)+' m';
  const a=cmpChart.options.plugins.annotation.annotations.crit; a.xMin=cr; a.xMax=cr; a.label.content=sgn(cr,1)+' m'; cmpChart.update('none');
  const pass=COMBOS.filter(c=>c.A>=cr&&c.B>=cr).length; let w=COMBOS[0]; COMBOS.forEach(c=>{if(Math.min(c.A,c.B)<Math.min(w.A,w.B))w=c;});
  document.getElementById('rPass').innerHTML=pass+' <small>of '+COMBOS.length+'</small>';
  document.getElementById('rWorst').innerHTML=w.lab+' ('+sgn(Math.min(w.A,w.B),1)+' m)';
}
sCr.addEventListener('input',upd3);upd3();
window.addEventListener('load',function(){try{[trChart,envChart,intChart,cmpChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, its friction gradient and the verified MOC solver.</li>
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: network characteristics, pumps in series and booster boundary conditions.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006: the vapour cavity model.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: booster stations, break tanks and the interaction of stations on long pipelines.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014: pumps in series and the response of multi-station systems.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: booster pump stations and protection strategies.</li>
  <li>Stephenson, D. <em>Pipeline Design for Water Engineers</em>, 3rd ed. Elsevier, 1989: break tanks and the hydraulic separation of pumping stages.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: pumps, check valves, pump shutdown settings, scenarios and report points.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #BoosterStation #PumpsInSeries #InlineBooster #BreakTank #PumpTrip #Interlocks #LowSuctionTrip #SurgeVessel #ColumnSeparation #BentleyHAMMER #TransmissionMain #WaterEngineering</div>
"""

import json, os, math
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'practice2.json')))['s15']
KEEP = ('A_min', 'A_max', 'B_min', 'B_max', 't_vap', 't', 'suc', 'dis', 'x', 'emax', 'emin')
DATA = {'sc': {k: {q: v[q] for q in KEEP} for k, v in _A['sc'].items()}, 'vessels': {k: {q: v[q] for q in KEEP} for k, v in _A['vessels'].items()},
        'cascade': [{q: c[q] for q in ('delay', 'suc_min', 'dis_min', 'B_min', 't_vap', 't', 'suc', 'dis')} for c in _A['cascade']]}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))
_vb = _A['vessels']['both']
VROWS = '\n'.join([
    '    <tr><td>Main A, vessel at station 1</td><td class="num">%.1f</td><td class="num">%.1f</td><td class="num">%.0f</td><td class="num">+%.2f</td><td class="num">%.1f</td></tr>' % (_A['V1'], _vb['gas'][0], math.ceil(_vb['gas'][0]/0.8), _vb['A_min'], _vb['A_max']),
    '    <tr><td>Main B, vessel at the booster discharge</td><td class="num">%.1f</td><td class="num">%.1f</td><td class="num">%.0f</td><td class="num">+%.2f</td><td class="num">%.1f</td></tr>' % (_A['V2'], _vb['gas'][1], math.ceil(_vb['gas'][1]/0.8), _vb['B_min'], _vb['B_max'])]) if True else ''
for k, v in {'__P1__': str(_A['P1']), '__P2__': str(_A['P2']), '__I1__': '%.1f' % _A['I1'], '__I2__': '%.1f' % _A['I2'], '__VROWS__': VROWS}.items():
    BODY = BODY.replace(k, v)

SPEC = dict(
    slug='booster-stations-series-surge', cat='surge', mins=14,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Booster Stations in Series: When One Trip Becomes a Surge at Both Stations',
    reg_title='Booster Stations in Series: When One Trip Becomes a Surge at Both Stations',
    reg_tag='Surge Analysis · Booster Stations · Series',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Booster Stations &middot; Series',
    desc='Surge in pumping stations in series: three trip scenarios on an in-line booster, the booster that drains its own suction main, low-suction interlocks, decoupling with a break tank and vessels sized for each main, with interactive charts and the HAMMER set-up.',
    og_desc='With an in-line booster, a station 1 trip lets the running booster drain its suction main to vapour in 9 s, and a power failure separates both mains. A break tank decouples them; 4.2 and 2.8 m³ of gas then protect each main in every trip.',
    ld_desc='Pumping stations in series: transient coupling through an in-line booster, interlocks, break-tank decoupling and vessel sizing for each main, with the Bentley HAMMER set-up.',
    img_alt='Two pumping stations on a long desert carrier, the second an in-line booster with a break tank and surge vessels, with pressure waves travelling in both directions along the pipeline between them',
    en_tag='Surge &amp; Transient Analysis &middot; Booster Stations',
    en_title='Booster Stations in Series: When One Trip Becomes a Surge at Both Stations',
    en_excerpt='With an in-line booster, a trip at either station is a surge at both. If station 1 trips and the booster runs on, it drains its own suction main to vapour in <strong>9 s</strong>; a power failure separates both mains. A break tank decouples them, and then <strong>4.2</strong> and <strong>2.8 m³</strong> of gas protect each main in every trip. Three scenarios, interlocks and the in-line or break-tank choice, with interactive charts.',
    en_search='booster stations in series in-line booster pumps in series surge pump trip break tank decoupling low suction trip interlock booster suction vapour column separation bypass check valve surge vessel each station long carrier transmission main Bentley HAMMER scenarios water hammer',
    ar_title='محطات التقوية على التوالي: حين يصبح توقف محطة واحدة طرقاً مائياً في المحطتين',
    ar_excerpt='مع محطة تقوية على الخط مباشرة، يصبح توقف أي محطة طرقاً مائياً في المحطتين. فإذا توقفت المحطة الأولى واستمرت محطة التقوية في العمل فإنها تفرغ خط السحب حتى ضغط التبخر خلال <strong>٩ ثوانٍ</strong>. وخزان القطع يفصل الخطين، فيكفي عندها <strong>٤٫٢</strong> و<strong>٢٫٨ م³</strong> من الغاز لحماية كل خط. مع رسوم تفاعلية.',
    ar_search='محطات التقوية على التوالي محطة تقوية على الخط المضخات على التوالي توقف المضخة خزان القطع إيقاف عند انخفاض ضغط السحب انفصال عمود الماء خزان الحماية خطوط النقل الطويلة المطرقة المائية بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
