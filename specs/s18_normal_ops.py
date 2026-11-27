# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A power failure stops a pump in a second or two; a variable-speed drive can take as long as the designer asks. On the unprotected 12&nbsp;km reference main, ramping the pump to zero speed in 10&nbsp;s still takes the line to vapour; 20&nbsp;s leaves it at &minus;5.0&nbsp;m; <strong>31.2&nbsp;s</strong>, about 1.4 times 2L/a, is the shortest ramp that keeps every point at +3.0&nbsp;m or above. Starting the same pump is almost harmless here, whatever the ramp: the head never exceeds about <strong>102.5&nbsp;m</strong>, because a pump cannot deliver more than its shut-off head. This article shows how to size stop and start ramps and pump control valve times from the model, why the flow stops long before the speed reaches zero, and which interlocks to write, while remembering that none of it helps when the power fails.</p>

<h2 id="normal">1 &middot; Normal operations are surge events too</h2>
<p>A pumped main sees a few power failures a year and thousands of normal starts and stops. Each normal event is a transient, and three things make them matter [1][2]:</p>
<ul class="clean">
  <li><strong>They are recurring.</strong> On plastic pipes their pressure swings set the fatigue life (see <a href="surge-envelope-pipe-pressure-limits.html">the pipe's real limits</a>).</li>
  <li><strong>They are controllable.</strong> Their rate is a setting on a drive or a valve, so the surge study can fix it.</li>
  <li><strong>They can be worse than expected.</strong> A controlled stop that is too quick is a pump trip with extra steps.</li>
</ul>
<p>The examples use the series' reference main without protection: 12&nbsp;km DN800 ductile iron, 2L/a = 22.9&nbsp;s, a pump with a 100&nbsp;m shut-off rise above a 5&nbsp;m suction, delivering 0.70&nbsp;m&sup3;/s against a 44.8&nbsp;m reservoir [3]. The network solver prescribes the pump speed (a drive ramp) or the opening of a pump control valve; it uses a vapour cavity model and has been verified against the series solver to 0.01&nbsp;m.</p>

<h2 id="stop">2 &middot; Stopping: how long a ramp?</h2>
<p>A drive ramping the speed down linearly from full to zero over \(T_r\) decelerates the column gradually. The model gives the lowest head on the line for each ramp:</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Stop ramp against the lowest head on the line</div>
    <div class="fsub">Upper: lowest pressure head on the line for a linear speed ramp from full speed to zero, unprotected reference main, 200&ndash;250&nbsp;s runs. Points at &minus;9.8&nbsp;m are vapour. Lower: pressure head at the pump and at mid-line for the selected ramp.</div>
  </div>
  <div class="chart-box"><canvas id="stopChart"></canvas></div>
  <div class="chart-box" style="height:280px;"><canvas id="stopTr"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Ramp shown below</label>
      <select id="sTr">
        <option value="0">Instant (speed to zero at once)</option>
        <option value="1">10 s</option>
        <option value="2">20 s</option>
        <option value="3">25 s</option>
        <option value="4">30 s</option>
        <option value="5">35 s</option>
        <option value="6" selected>40 s</option>
        <option value="7">60 s</option>
        <option value="8">90 s</option>
        <option value="9">120 s</option>
        <option value="10">180 s</option>
        <option value="11">240 s</option>
      </select>
      <div class="hint">2L/a = 22.9&nbsp;s on this main.</div>
    </div>
    <div class="ctrl">
      <label>Design minimum <span id="vCr">+3.0 m</span></label>
      <input type="range" id="sCr" min="-5" max="20" value="3" step="0.5">
      <div class="hint">Check it against the project's allowable values.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Lowest head, this ramp</div><div class="v" id="rMin">&ndash;</div></div>
    <div class="cell"><div class="k">Where</div><div class="v" id="rX" style="font-size:15px;margin-top:6px;">&ndash;</div></div>
    <div class="cell"><div class="k">Highest head</div><div class="v" id="rMax">&ndash;</div></div>
    <div class="cell"><div class="k">Shortest ramp meeting the minimum</div><div class="v" id="rNeed">&ndash;</div></div>
    <div class="cell"><div class="k">As a multiple of 2L/a</div><div class="v" id="rMult">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The shortest ramp is found between the computed points by interpolation; at +3.0&nbsp;m a bisection on the model itself gives 31.2&nbsp;s. Ramps of 0 and 10&nbsp;s take the line to vapour, 20&nbsp;s to &minus;5.0&nbsp;m, 40&nbsp;s to +4.4&nbsp;m. Beyond about two minutes each extra minute buys only a few metres. The maximum never exceeds the steady 85&nbsp;m: a controlled stop of a pump with a check valve has no upsurge of its own.</p>

<h2 id="zero-flow">3 &middot; The flow stops long before the speed does</h2>
<p>A centrifugal pump cannot deliver against a head higher than its shut-off head at that speed, which falls with the square of the speed. The pump stops lifting water into the line when [4][5]</p>
<div class="eq">\[ H_{suc} + H_0\,w^2 = H_{res} \quad\Rightarrow\quad w_0 = \sqrt{\frac{H_{res} - H_{suc}}{H_0}} = \sqrt{\frac{44.8 - 5.0}{100}} = 0.631 \]</div>
<p>On a linear ramp to zero, the pump has done its useful work after the first 37&nbsp;% of the ramp: a 60&nbsp;s ramp is in effect a 22&nbsp;s deceleration of the column. Drives that ramp to a minimum speed rather than to zero, and pumps with a high static lift, make this worse. When specifying a stop ramp, think of the time from full speed to \(w_0\), not to zero; some drives allow a two-stage ramp (fast to just above \(w_0\), slow through it) for exactly this reason.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Where the pump stops delivering</div>
    <div class="fsub">Pump curves \(H = H_{suc} + H_0 w^2 - kQ^2\) at several speeds, and the system curve \(H = H_{res} + R Q^2\), with \(k\) and \(R\) set so the full-speed curve meets the system at the duty flow. The pump stops delivering at the speed whose shut-off head equals the static head.</div>
  </div>
  <div class="chart-box"><canvas id="pcChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Static head to lift <span id="vHst">39.8 m</span></label>
      <input type="range" id="sHst" min="5" max="90" value="39.8" step="0.1">
      <div class="hint">Delivery level minus suction level.</div>
    </div>
    <div class="ctrl">
      <label>Shut-off head at full speed <span id="vH0">100 m</span></label>
      <input type="range" id="sH0" min="20" max="200" value="100" step="1">
      <div class="hint">Above the suction.</div>
    </div>
    <div class="ctrl">
      <label>Duty head <span id="vHd">80 m</span></label>
      <input type="range" id="sHd" min="10" max="190" value="80" step="1">
      <div class="hint">Static head plus friction at duty.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Speed at zero flow</div><div class="v" id="rW0">&ndash;</div></div>
    <div class="cell"><div class="k">Share of a linear ramp used</div><div class="v" id="rShare">&ndash;</div></div>
    <div class="cell"><div class="k">A 60 s ramp decelerates the flow in</div><div class="v" id="rEff">&ndash;</div></div>
  </div>
</div>

<h2 id="start">4 &middot; Starting: drive ramp or pump control valve</h2>
<p>A start accelerates the column from rest. A drive ramps the speed up; a fixed-speed pump starts direct on line against a pump control valve that opens over a set time. In both cases the pump's head cannot exceed its shut-off head, 105&nbsp;m at the pump here, so the start cannot produce a maximum above that unless air or vapour is in the line. On this main both kinds of start, at every ramp or opening time from 1 to 90&nbsp;s, give a maximum of 99&ndash;102.5&nbsp;m and no fall below the static 44.8&nbsp;m [2][6].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Starting the pump into a full, still line</div>
    <div class="fsub">Pressure head at the pump and at mid-line, and the pump flow, for a drive ramp from zero to full speed or a direct-on-line start against a valve opening linearly (loss coefficient \(K_0/\tau^2\), \(K_0\) for 0.5&nbsp;m at duty). Unprotected reference main, 200&nbsp;s.</div>
  </div>
  <div class="chart-box"><canvas id="startChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Start method</label>
      <select id="sMeth">
        <option value="vfd" selected>Drive ramp</option>
        <option value="valve">Pump control valve opening</option>
      </select>
      <div class="hint">Same pump, same line.</div>
    </div>
    <div class="ctrl">
      <label>Ramp or opening time</label>
      <select id="sTs">
        <option value="0">1 s</option>
        <option value="1">5 s</option>
        <option value="2" selected>10 s</option>
        <option value="3">20 s</option>
        <option value="4">40 s</option>
        <option value="5">60 s</option>
        <option value="6">90 s</option>
      </select>
      <div class="hint">From standstill or closed.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Highest head</div><div class="v" id="rSmax">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest head</div><div class="v" id="rSmin">&ndash;</div></div>
    <div class="cell"><div class="k">Flow reaches 99 % at</div><div class="v" id="rT99">&ndash;</div></div>
    <div class="cell"><div class="k">Pump shut-off head</div><div class="v">105.0 <small>m</small></div></div>
  </div>
</div>
<p class="fig-note">The start's maximum is set by the shut-off head, not by the ramp: a slower ramp only delays the column's acceleration. The real risk at a start is elsewhere: air at high points after a drain-down (see <a href="pipeline-filling-draining-restart-surge.html">filling and restart</a>), a check valve that opens late and lets the column slam it open, or starting into a column still oscillating after the previous stop.</p>

<h2 id="interlocks">5 &middot; Settings and interlocks to write from the model</h2>
<ul class="clean">
  <li><strong>Stop ramp</strong>: at least the shortest ramp that passes, with margin (31.2&nbsp;s here; we would set 45&nbsp;s), applied to every normal stop, including stops by level control.</li>
  <li><strong>Emergency stop</strong>: a coast stop is a trip; the protection must cover it, not the ramp.</li>
  <li><strong>Start ramp or valve opening</strong>: long enough to keep starting current and air release under control; the surge seldom sets it.</li>
  <li><strong>Minimum time between a stop and the next start</strong>, long enough for the column to settle.</li>
  <li><strong>Pumps in parallel</strong>: stop and start them one at a time, with the stop ramp applying to each.</li>
  <li><strong>A power failure is not covered by any of these.</strong> The trip remains the case that sizes the protection (see <a href="choosing-surge-protection.html">choosing surge protection</a>).</li>
</ul>

<h2 id="hammer">6 &middot; Setting it up in Bentley HAMMER</h2>
<p>Field names differ slightly between versions [7].</p>
<ol>
  <li><strong>Model the controlled stop</strong> as a variable-speed pump with a speed pattern ramping from 1 to 0 over the ramp time (or the pump's own speed-controlled transient setting in your version), not as a pump shutdown, which HAMMER treats as a trip.</li>
  <li><strong>Model the start</strong> as a pump start with a speed ramp, or as a pump with a downstream control valve whose opening follows the specified time.</li>
  <li><strong>Create one scenario per ramp</strong> and use batch run to bracket the shortest ramp that passes.</li>
  <li><strong>Start from the right initial state</strong>: a full line at rest for a start, the duty point for a stop.</li>
  <li><strong>Record the recurring pressure swing</strong> at the critical points for the fatigue check of plastic pipes.</li>
  <li><strong>Write the settings into the control philosophy</strong> with the scenario that justifies each.</li>
</ol>

<h2 id="checklist">7 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Stop ramp sized</strong> from the model, with margin, and judged on the time to the zero-flow speed.</li>
  <li><strong>Start checked</strong> against the shut-off head and for air and late check valve opening.</li>
  <li><strong>Pump control valve times</strong> set from the model where valves are used.</li>
  <li><strong>Emergency stop and power failure</strong> covered by the protection, not by settings.</li>
  <li><strong>Recurring swings</strong> passed to the fatigue check.</li>
  <li><strong>Settings and interlocks</strong> written into the control philosophy.</li>
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
    <li><a href="booster-stations-series-surge.html">Booster stations in series</a></li>
    <li><strong>Pump starts, controlled stops and drive ramps</strong></li>
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
const fmt1=v=>v.toFixed(1), fmt2=v=>v.toFixed(2), fmt3=v=>v.toFixed(3);
const sgn=(v,d)=>(v<-0.0049?'−':(v>0.0049?'+':''))+Math.abs(v).toFixed(d);
const VAP=-9.8, TLA=2*12000/1050;
const hl=(v,txt,col,pos)=>({type:'line',yMin:v,yMax:v,borderColor:col,borderWidth:1.3,borderDash:[6,4],label:{display:true,content:txt,position:pos||'end',font:LBL,color:'#fff',backgroundColor:col}});
/* ---------- CHART 1 : stop ramps ---------- */
const sTr=document.getElementById('sTr'), sCr=document.getElementById('sCr');
const S=D.stops;
const stopChart=new Chart(document.getElementById('stopChart'),{
  data:{datasets:[
    {type:'line',label:'Lowest head on the line (m)',data:S.map(s=>({x:s.Tr,y:s.line_min})),borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:4,order:2},
    {type:'scatter',label:'Selected ramp',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:240,title:{display:true,text:'Stop ramp, full speed to zero (s)',font:TTL},...AX},y:{type:'linear',min:-12,max:26,title:{display:true,text:'Lowest pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${fmt2(c.parsed.y)} m for a ${fmt1(c.parsed.x)} s ramp`}},
      annotation:{annotations:{crit:hl(3,'+3.0 m','rgba(30,132,73,0.85)','start'),vap:hl(VAP,'vapour','rgba(192,57,43,0.85)'),
        tla:{type:'line',xMin:TLA,xMax:TLA,borderColor:'#6b4f9e',borderWidth:1.2,borderDash:[3,3],label:{display:true,content:'2L/a',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}}}}}
});
const stopTr=new Chart(document.getElementById('stopTr'),{
  data:{datasets:[
    {type:'line',label:'At the pump (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0},
    {type:'line',label:'At 6 km (m)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:1.6,pointRadius:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,title:{display:true,text:'Time from the start of the ramp (s)',font:TTL},...AX},y:{type:'linear',min:-15,max:95,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{vap:hl(VAP,'vapour','rgba(192,57,43,0.85)')}}}}
});
function needRamp(cr){
  if(S[0].line_min>=cr) return 0;
  for(let i=1;i<S.length;i++){ if(S[i].line_min>=cr){const a=S[i-1],b=S[i]; return a.Tr+(cr-a.line_min)*(b.Tr-a.Tr)/(b.line_min-a.line_min);} }
  return null;
}
function upd1(){
  const s=S[+sTr.value], cr=+sCr.value;
  document.getElementById('vCr').textContent=sgn(cr,1)+' m';
  const a=stopChart.options.plugins.annotation.annotations.crit; a.yMin=cr; a.yMax=cr; a.label.content=sgn(cr,1)+' m';
  stopChart.data.datasets[1].data=[{x:s.Tr,y:s.line_min}]; stopChart.update('none');
  stopTr.data.datasets[0].data=s.t.map((t,k)=>({x:t,y:s.pump[k]})); stopTr.data.datasets[1].data=s.t.map((t,k)=>({x:t,y:s.mid[k]})); stopTr.update('none');
  document.getElementById('rMin').innerHTML=sgn(s.line_min,2)+(s.vap?' <small>(vapour)</small>':' <small>m</small>');
  document.getElementById('rX').innerHTML=s.x_min===0?'at the pump':'at '+fmt1(s.x_min/1000)+' km';
  document.getElementById('rMax').innerHTML=fmt1(s.line_max)+' <small>m</small>';
  const n=needRamp(cr);
  document.getElementById('rNeed').innerHTML=n===null?'<small>more than 240 s</small>':fmt1(n)+' <small>s</small>';
  document.getElementById('rMult').innerHTML=n===null?'<small>&ndash;</small>':fmt2(n/TLA)+' <small>×</small>';
}
[sTr,sCr].forEach(s=>s.addEventListener('input',upd1));upd1();
/* ---------- CHART 2 : zero-flow speed ---------- */
const sHst=document.getElementById('sHst'), sH0=document.getElementById('sH0'), sHd=document.getElementById('sHd');
const pcChart=new Chart(document.getElementById('pcChart'),{
  data:{datasets:[]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:1.4,title:{display:true,text:'Flow as a fraction of duty',font:TTL},...AX},y:{type:'linear',min:0,title:{display:true,text:'Head above the suction (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt2(c.parsed.x)}`}}}}
});
function upd2(){
  const hst=+sHst.value, h0=+sH0.value, hd=Math.max(+sHd.value,hst+0.1);
  document.getElementById('vHst').textContent=fmt1(hst)+' m'; document.getElementById('vH0').textContent=h0+' m'; document.getElementById('vHd').textContent=fmt1(hd)+' m';
  const k=(h0-hd), R=(hd-hst); // per unit flow fraction squared
  const X=[];for(let i=0;i<=56;i++)X.push(i*0.025);
  const w0=hst<h0?Math.sqrt(hst/h0):null;
  const sets=[{type:'line',label:'System curve',data:X.map(x=>({x:x,y:hst+R*x*x})),borderColor:'#111',backgroundColor:'#111',borderWidth:2.2,pointRadius:0}];
  [[1,'#1b4f72'],[0.9,'#2e86c1'],[0.8,'#5dade2'],[0.7,'#85c1e9']].forEach(([w,c])=>sets.push({type:'line',label:'Pump at '+fmt0(w*100)+' % speed',data:X.map(x=>({x:x,y:h0*w*w-k*x*x})).filter(p=>p.y>=0),borderColor:c,backgroundColor:c,borderWidth:1.6,pointRadius:0}));
  if(w0) sets.push({type:'line',label:'Pump at zero-flow speed',data:X.map(x=>({x:x,y:h0*w0*w0-k*x*x})).filter(p=>p.y>=0),borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2,borderDash:[5,4],pointRadius:0});
  pcChart.data.datasets=sets; pcChart.options.scales.y.max=Math.ceil(h0*1.1/10)*10; pcChart.update('none');
  document.getElementById('rW0').innerHTML=w0?fmt3(w0):'<small>cannot lift at all</small>';
  document.getElementById('rShare').innerHTML=w0?fmt1(100*(1-w0))+' <small>%</small>':'&ndash;';
  document.getElementById('rEff').innerHTML=w0?fmt1(60*(1-w0))+' <small>s</small>':'&ndash;';
}
const fmt0=v=>Math.round(v).toString();
[sHst,sH0,sHd].forEach(s=>s.addEventListener('input',upd2));upd2();
/* ---------- CHART 3 : starts ---------- */
const sMeth=document.getElementById('sMeth'), sTs=document.getElementById('sTs');
const startChart=new Chart(document.getElementById('startChart'),{
  data:{datasets:[
    {type:'line',label:'At the pump (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0,yAxisID:'y'},
    {type:'line',label:'At 6 km (m)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:1.6,pointRadius:0,yAxisID:'y'},
    {type:'line',label:'Pump flow (m³/s, right)',data:[],borderColor:'#1e8449',backgroundColor:'#1e8449',borderWidth:1.6,borderDash:[5,4],pointRadius:0,yAxisID:'y1'}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:200,title:{display:true,text:'Time from the start command (s)',font:TTL},...AX},
            y:{type:'linear',min:0,max:120,title:{display:true,text:'Pressure head (m)',font:TTL},...AX},
            y1:{type:'linear',min:0,max:1.0,position:'right',title:{display:true,text:'Flow (m³/s)',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`flow ${fmt3(c.parsed.y)} m³/s`:`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m`}},
      annotation:{annotations:{so:hl(105,'shut-off head 105 m','rgba(127,140,141,0.9)','start')}}}}
});
function upd3(){
  const arr=sMeth.value==='vfd'?D.starts:D.vstarts, s=arr[+sTs.value];
  startChart.data.datasets[0].data=s.t.map((t,k)=>({x:t,y:s.pump[k]}));
  startChart.data.datasets[1].data=s.t.map((t,k)=>({x:t,y:s.mid[k]}));
  startChart.data.datasets[2].data=s.t.map((t,k)=>({x:t,y:s.q[k]}));
  startChart.update('none');
  const k99=s.q.findIndex(q=>q>=0.99*s.q_end);
  document.getElementById('rSmax').innerHTML=fmt1(s.line_max)+' <small>m</small>';
  document.getElementById('rSmin').innerHTML=fmt1(s.line_min)+' <small>m</small>';
  document.getElementById('rT99').innerHTML=k99>=0?fmt1(s.t[k99])+' <small>s</small>':'<small>not within 200 s</small>';
}
[sMeth,sTs].forEach(s=>s.addEventListener('input',upd3));upd3();
window.addEventListener('load',function(){try{[stopChart,stopTr,pcChart,startChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: pump start-up and shutdown transients, valve operation and control.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: pump starting and controlled stopping, and their effect on surge.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, its pump and the verified MOC solver.</li>
  <li>Karassik, I.J., Messina, J.P., Cooper, P. &amp; Heald, C.C. <em>Pump Handbook</em>, 4th ed. McGraw-Hill, 2008: affinity laws and the operation of variable-speed pumps against static head.</li>
  <li>Europump &amp; Hydraulic Institute. <em>Variable Speed Pumping: A Guide to Successful Applications</em>. Elsevier, 2004: minimum speed against static head and drive ramp settings.</li>
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: pump boundary conditions with prescribed speed and valve opening.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: variable-speed pumps, pump start and shutdown, valve operating rules, scenarios and batch run.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #VFD #VariableSpeedDrive #PumpStart #PumpStop #RampTime #PumpControlValve #Interlocks #ControlPhilosophy #AffinityLaws #BentleyHAMMER #TransientAnalysis #PumpStation #WaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'practice2.json')))['s18']
K1 = ('Tr', 'line_min', 'x_min', 'line_max', 'vap', 't', 'pump', 'mid')
K2 = ('Tr', 'line_min', 'line_max', 't', 'pump', 'mid', 'q', 'q_end')
DATA = {'stops': [{k: s[k] for k in K1} for s in _A['stops']], 'starts': [{k: s[k] for k in K2} for s in _A['starts']], 'vstarts': [{k: s[k] for k in K2} for s in _A['vstarts']]}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='pump-start-stop-vfd-ramp-surge', cat='surge', mins=14,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Pump Starts, Controlled Stops and Drive Ramps: Sizing Normal Operations from the Surge Model',
    reg_title='Pump Starts, Controlled Stops and Drive Ramps: Sizing Normal Operations from the Surge Model',
    reg_tag='Surge Analysis · Normal Operations · VFD',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Normal Operations &middot; VFD',
    desc='How to size stop ramps, start ramps and pump control valve times from a surge model: the lowest head against the stop ramp, the speed at which the pump stops delivering, why starts are limited by the shut-off head, and the interlocks to write, with three interactive charts and the HAMMER steps.',
    og_desc='On the unprotected 12 km main a 10 s drive stop ramp still takes the line to vapour; 31.2 s, 1.4 times 2L/a, is the shortest that keeps +3.0 m. The flow stops at 63 % speed, so a 60 s ramp decelerates the column in 22 s. Starts never exceed the 105 m shut-off head.',
    ld_desc='Normal pump operations as surge events: drive stop and start ramps, the zero-flow speed, pump control valve opening, and interlocks, worked on a 12 km main with the Bentley HAMMER steps.',
    img_alt='A pump station control room with an open variable-speed drive cabinet and a screen showing a descending ramp curve beside an oscillating pressure trace, and the pump hall visible through a large window',
    en_tag='Surge &amp; Transient Analysis &middot; Normal Operations',
    en_title='Pump Starts, Controlled Stops and Drive Ramps: Sizing Normal Operations from the Surge Model',
    en_excerpt='On the unprotected 12 km main a 10 s drive stop ramp still takes the line to vapour; <strong>31.2 s</strong>, 1.4 times 2L/a, is the shortest that keeps +3.0 m. The flow stops at <strong>63 % speed</strong>, so a 60 s ramp decelerates the column in 22 s. Starts never exceed the 105 m shut-off head. Ramps, valve times and interlocks from the model, with three interactive charts.',
    en_search='pump start stop surge VFD ramp time variable speed drive controlled stop deceleration ramp zero flow speed affinity laws shut-off head pump control valve opening time direct on line start interlocks control philosophy recurring surge fatigue Bentley HAMMER variable speed pump scenarios water hammer',
    ar_title='بدء تشغيل المضخات وإيقافها المتحكم به ومنحدرات مغيرات السرعة: ضبط التشغيل العادي من نموذج الطرق المائي',
    ar_excerpt='على الخط المرجعي غير المحمي (١٢ كم) لا يمنع منحدر إيقاف مدته ١٠ ثوانٍ وصول الخط إلى ضغط التبخر، و<strong>٣١٫٢ ثانية</strong> هي أقصر مدة تحافظ على +٣٫٠ م. ويتوقف التدفق عند <strong>٦٣٪ من السرعة</strong>، أما بدء التشغيل فلا يتجاوز ضغط الإغلاق البالغ ١٠٥ م. مع ثلاثة رسوم تفاعلية.',
    ar_search='بدء تشغيل المضخة إيقاف المضخة مغير السرعة زمن المنحدر الإيقاف المتحكم به سرعة انعدام التدفق قوانين التشابه ضغط الإغلاق صمام التحكم بالمضخة الأقفال البينية المطرقة المائية الطرق المائي بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
