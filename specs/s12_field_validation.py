# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A surge model is a prediction until a real trip has been measured and compared with it. Done properly, the test is short and cheap: two fast pressure loggers, one deliberate pump trip and an afternoon of comparison. Done badly, it proves nothing. A SCADA historian logging once a second can miss <strong>25&nbsp;m</strong> of a 134&nbsp;m peak, and a model tuned until it matches the wrong trace hides the error it was meant to find. This article works through a pump-trip test on a 4&nbsp;km main: where to put the transducers, how fast to log, how to read the wave speed straight off the record, and how to calibrate wave speed and pump inertia against the measurement without forcing the fit. The &ldquo;measured&rdquo; traces here are synthetic: a model of the same main with a wave speed of 1,000&nbsp;m/s and an inertia of 50&nbsp;kg&middot;m&sup2;, standing in for the real pipe, with logger noise added. That lets every step be checked against a known answer.</p>

<h2 id="why-test">1 &middot; Why a test is worth the trouble</h2>
<p>Every surge model rests on inputs that are hard to know in advance: the wave speed of a buried pipe with its joints, lining and entrained air, the inertia of a motor and pump that were bought after the study, the real closure of the check valve, and the friction of a pipe in service [1][2]. The <a href="surge-sensitivity-uncertainty.html">sensitivity article</a> shows how far each one moves the answer. A field test replaces the largest of these uncertainties with a measurement. It also tells the operator that the protection works: a vessel whose gas volume has drifted, or an air valve that sticks, shows up in the first recorded trip.</p>
<p>The test main here is the 4&nbsp;km version of the series' reference line used in <a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip</a>: DN800 ductile iron, 0.70&nbsp;m&sup3;/s, 85.0&nbsp;m at the pump, a 685&nbsp;kW set at 1,480&nbsp;rpm and an ideal check valve. The design model used the catalogue wave speed (1,050&nbsp;m/s) and the correlation estimate of inertia (44&nbsp;kg&middot;m&sup2;). The &ldquo;real&rdquo; pipe has 1,000&nbsp;m/s and 50&nbsp;kg&middot;m&sup2;, a plausible gap on a real project. The design model predicts a lowest head of +1.79&nbsp;m on the line; the real one reaches +2.65&nbsp;m, and about +3.0&nbsp;m at the pump.</p>

<h2 id="instruments">2 &middot; Transducers and loggers</h2>
<ul class="clean">
  <li><strong>Where.</strong> At the pump discharge downstream of the check valve, at the vessel if there is one, at the high point or knee that governs the minimum, and at one point a known distance along the line, so the wave travel time can be measured. Two well-placed transducers beat six badly placed ones [3].</li>
  <li><strong>What.</strong> Piezoresistive pressure transducers with a range covering both vacuum and the predicted maximum (here &minus;1 to 16&nbsp;bar), mounted on a short tapping with a full-bore isolating valve, vented of air before the test.</li>
  <li><strong>How fast.</strong> Fast enough to catch the steepest change. A wave front at 1,000&nbsp;m/s passes a transducer in well under a second, and a cavity collapse in milliseconds. We log at 100&nbsp;Hz or faster, synchronised between loggers to a common clock [3][4].</li>
  <li><strong>What else.</strong> Pump speed (a tachometer or the drive's speed signal), flow before the trip, reservoir levels and the exact time of the trip.</li>
</ul>
<div class="callout warn">
  <span class="lbl">Why SCADA is not enough</span>
  A SCADA historian usually stores a value every second or slower, often averaged. Section 3 shows what that does to a peak lasting a fraction of a second. SCADA records are useful to confirm that something happened (see <a href="transient-analysis-scada.html">SCADA records in transient analysis</a>); they are not a calibration record.
</div>

<h2 id="sampling">3 &middot; Interactive: what the logging rate does to the peak</h2>
<p>The trace is the &ldquo;real&rdquo; pressure at the pump during the trip, at 100&nbsp;Hz. Choose a logging rate and a phase: where the samples happen to fall relative to the event.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">The same trip logged at different rates</div>
    <div class="fsub">Pressure head at the pump after a trip on the 4&nbsp;km main (synthetic &ldquo;real&rdquo; pipe: a = 1,000&nbsp;m/s, I = 50&nbsp;kg&middot;m&sup2;, generic radial torque law), at 100&nbsp;Hz, noise-free. Markers: the samples a slower logger would keep. Readouts: the extremes those samples report against the true ones.</div>
  </div>
  <div class="chart-box"><canvas id="sampChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Logging rate</label>
      <select id="sFs">
        <option value="1" selected>1 Hz (typical SCADA)</option>
        <option value="2">2 Hz</option>
        <option value="5">5 Hz</option>
        <option value="10">10 Hz</option>
        <option value="20">20 Hz</option>
        <option value="50">50 Hz</option>
        <option value="100">100 Hz</option>
      </select>
      <div class="hint">Samples per second.</div>
    </div>
    <div class="ctrl">
      <label>Phase of the samples <span id="vPh">0 %</span></label>
      <input type="range" id="sPh" min="0" max="99" value="0" step="1">
      <div class="hint">Where the first sample falls within one interval.</div>
    </div>
    <div class="ctrl">
      <label>Time window <span id="vWin">0–40 s</span></label>
      <select id="sWin">
        <option value="40" selected>0–40 s</option>
        <option value="12">0–12 s</option>
      </select>
      <div class="hint">Zoom in on the first two wave periods.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">True maximum</div><div class="v" id="rTmx">&ndash;</div></div>
    <div class="cell"><div class="k">Logged maximum</div><div class="v" id="rLmx">&ndash;</div></div>
    <div class="cell"><div class="k">Missed</div><div class="v" id="rMis">&ndash;</div></div>
    <div class="cell"><div class="k">Worst phase misses</div><div class="v" id="rWmis">&ndash;</div></div>
    <div class="cell"><div class="k">True / logged minimum</div><div class="v" id="rMn" style="font-size:17px;">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">At 1&nbsp;Hz the logged maximum lies anywhere between 108.8 and 134.2&nbsp;m depending on where the samples fall: up to 25&nbsp;m missed. At 10&nbsp;Hz the worst case still misses 2.5&nbsp;m; at 50&nbsp;Hz, 0.4&nbsp;m. The minimum, a slower and broader trough on this main, is caught well even at 1&nbsp;Hz (3.0 to 3.7&nbsp;m). A cavity collapse would be far sharper than either.</p>

<h2 id="wave-speed">4 &middot; Reading the wave speed off the record</h2>
<p>The simplest and most valuable number a test gives is the wave speed, and it needs no model at all. A pump trip sends a downsurge from the pump at the instant of the trip; it reaches a transducer at distance \(x\) after \(x/a\) seconds [1][5]:</p>
<div class="eq">\[ a \;=\; \frac{x}{t_{arrival} - t_{trip}}, \qquad \frac{\delta a}{a} \;\approx\; \frac{\delta t}{t_{arrival} - t_{trip}} \]</div>
<p>With a transducer 2&nbsp;km out and a logger at 100&nbsp;Hz, the timing uncertainty of one sample (0.01&nbsp;s) on a travel time of 2.0&nbsp;s is 0.5&nbsp;%. At 1&nbsp;Hz it is 50&nbsp;%: the measurement is useless. The trip time itself must be known to the same accuracy, which is why the pump-end transducer or the motor current is logged on the same clock.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Wave speed from the arrival time</div>
    <div class="fsub">Logged pressure head 2&nbsp;km from the pump (synthetic record, with logger noise of about &plusmn;0.2&nbsp;m) and at the pump, first 4&nbsp;s. Arrival: the first sample at least the threshold below the steady value. \(a = 2000/t_{arrival}\); the range comes from one sample interval of timing uncertainty.</div>
  </div>
  <div class="chart-box"><canvas id="arrChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Logging rate</label>
      <select id="sFs2">
        <option value="1">1 Hz</option>
        <option value="10">10 Hz</option>
        <option value="20">20 Hz</option>
        <option value="50">50 Hz</option>
        <option value="100" selected>100 Hz</option>
      </select>
      <div class="hint">Both loggers on one clock.</div>
    </div>
    <div class="ctrl">
      <label>Detection threshold <span id="vThr">1.0 m</span></label>
      <input type="range" id="sThr" min="0.2" max="5" value="1" step="0.1">
      <div class="hint">Above the noise, below the front.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Arrival detected</div><div class="v" id="rTa">&ndash;</div></div>
    <div class="cell"><div class="k">Wave speed</div><div class="v" id="rAe">&ndash;</div></div>
    <div class="cell"><div class="k">Range from timing</div><div class="v" id="rAr" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Design value used</div><div class="v">1,050 <small>m/s</small></div></div>
  </div>
</div>
<p class="fig-note">At 100&nbsp;Hz with a 1&nbsp;m threshold the arrival is read at about 2.0&nbsp;s and the wave speed comes out within 1&nbsp;% of the true 1,000&nbsp;m/s: 5&nbsp;% below the design value. A threshold below the noise triggers on noise; a large threshold waits for the front to deepen and reads it late, biasing the wave speed low.</p>

<h2 id="calibrate">5 &middot; Calibrating the model without forcing it</h2>
<p>With the wave speed measured, the remaining unknowns are adjusted one at a time against the whole trace, not against one peak [2][4][6]. We use the root-mean-square difference over the first 30&nbsp;s at both transducers as the measure of fit:</p>
<div class="eq">\[ \text{RMS} \;=\; \sqrt{\frac{1}{N}\sum_{k}\big(H_{model}(t_k) - H_{measured}(t_k)\big)^2} \]</div>
<p>The order matters. Fix what the test measures directly (wave speed, steady flow and heads, trip time) first. Then adjust the inputs that are genuinely uncertain and physically bounded (inertia within the range in the data sheets, the pump characteristic between neighbouring curves, the gas volume of a vessel within its level tolerance). Leave alone the things a test cannot identify, such as friction during the transient, unless the steady state is wrong.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Model against measurement</div>
    <div class="fsub">Synthetic measured record (dots, every 0.1&nbsp;s) and model (lines) at the pump and 2&nbsp;km out, for twelve combinations of wave speed and inertia. RMS over 0&ndash;30&nbsp;s at both transducers. Model: method of characteristics, vapour cavity model, generic radial torque law, 100&nbsp;m reaches.</div>
  </div>
  <div class="chart-box"><canvas id="calChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Wave speed in the model</label>
      <select id="sCa">
        <option value="950">950 m/s</option>
        <option value="1000">1,000 m/s (measured in section 4)</option>
        <option value="1050" selected>1,050 m/s (design)</option>
        <option value="1100">1,100 m/s</option>
      </select>
      <div class="hint">Set first, from the arrival time.</div>
    </div>
    <div class="ctrl">
      <label>Inertia in the model</label>
      <select id="sCi">
        <option value="35">35 kg·m²</option>
        <option value="44" selected>44 kg·m² (correlation)</option>
        <option value="55">55 kg·m²</option>
      </select>
      <div class="hint">Within the data-sheet range.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">RMS difference</div><div class="v" id="rRms">&ndash;</div></div>
    <div class="cell"><div class="k">Best of the twelve</div><div class="v" id="rBest" style="font-size:15px;margin-top:6px;">&ndash;</div></div>
    <div class="cell"><div class="k">Model: lowest head on line</div><div class="v" id="rMm">&ndash;</div></div>
    <div class="cell"><div class="k">Model: peak at the pump</div><div class="v" id="rMx">&ndash;</div></div>
    <div class="cell"><div class="k">Measured: peak at the pump</div><div class="v" id="rMeas">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The design model (1,050&nbsp;m/s, 44&nbsp;kg&middot;m&sup2;) is 12.9&nbsp;m RMS from the record: its waves arrive early and its reflections are out of step. Setting the measured 1,000&nbsp;m/s drops that to 2.6&nbsp;m with no other change. Inertia then refines it: 55&nbsp;kg&middot;m&sup2; gives 1.96&nbsp;m and 35 gives 6.7&nbsp;m, so the true value (50) is bracketed between the two better runs. No combination at 950 or 1,100&nbsp;m/s comes within 11&nbsp;m, however the inertia is set: the wave speed cannot be traded against inertia, which is why it is fixed first.</p>

<h2 id="pitfalls">6 &middot; How calibration goes wrong</h2>
<ul class="clean">
  <li><strong>Tuning to the peak.</strong> Matching one maximum by adjusting friction or wave speed can make a wrong model look right. Fit the shape and timing of the whole record.</li>
  <li><strong>Adjusting what the test cannot see.</strong> A trip that never separates the column says nothing about cavity models; a test without a vessel says nothing about its gas law.</li>
  <li><strong>Hidden air.</strong> Free air lowers the wave speed and damps the oscillation. If the measured wave speed is far below the calculated one, look for air before changing the pipe properties (see <a href="wave-speed-surge-analysis.html">wave speed</a>).</li>
  <li><strong>Different initial conditions.</strong> The test and the model must start from the same flow, heads and number of pumps running; record them.</li>
  <li><strong>Testing into danger.</strong> The test trip must be one the model already shows to be safe, with protection in service. A test of the unprotected case is never justified.</li>
</ul>

<h2 id="procedure">7 &middot; Test procedure</h2>
<ol>
  <li><strong>Agree the test with the operator</strong>: the scenario, the pass and abort criteria, who trips the pump and how, and a model run of that exact scenario showing it is safe.</li>
  <li><strong>Install and check transducers</strong>: range, zero at atmospheric, vented tappings, synchronised clocks, 100&nbsp;Hz or faster.</li>
  <li><strong>Record the steady state</strong> for several minutes: flow, heads, speed, levels, vessel level and pressure.</li>
  <li><strong>Trip the pump</strong> by opening its breaker, as a real power failure would, and keep logging until the line has settled (several minutes on a main with a vessel).</li>
  <li><strong>Read the wave speed</strong> from the arrival time (section 4) and the steady state from the pre-trip record.</li>
  <li><strong>Rerun the model</strong> with the measured steady state, then adjust the uncertain inputs within their bounds, judging each step by the RMS over the whole record.</li>
  <li><strong>Report the calibrated values</strong> and their effect on the design envelope, and keep the record for comparison after any change to the system.</li>
</ol>

<h2 id="hammer">8 &middot; Doing it in Bentley HAMMER</h2>
<p>Field names differ slightly between versions [7].</p>
<ol>
  <li><strong>Build a test scenario</strong> that matches the test exactly: the pumps running, the initial flow and levels from the pre-trip record.</li>
  <li><strong>Place report points</strong> at the transducer locations, and set the report period to every time step so the model trace has the same resolution as the logger.</li>
  <li><strong>Import or overlay the measured trace</strong> on the time-history graph of each report point (export both to a spreadsheet if your version cannot overlay).</li>
  <li><strong>Set wave speeds from the measured value</strong>, pipe by pipe or as a global factor, and check the steady state still matches.</li>
  <li><strong>Create alternatives</strong> for the uncertain inputs (inertia, specific-speed curve, vessel gas volume) and a scenario for each, and compare the RMS.</li>
  <li><strong>Carry the calibrated values back</strong> into the design scenarios and rerun the envelope.</li>
</ol>

<h2 id="checklist">9 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Test scenario modelled and shown safe</strong> before it is run.</li>
  <li><strong>Transducers at the pump, the critical point and a known distance</strong>, logging at 100&nbsp;Hz or faster on a common clock.</li>
  <li><strong>Steady state recorded</strong> before the trip and used in the model.</li>
  <li><strong>Wave speed read from the arrival time</strong>, with its timing uncertainty.</li>
  <li><strong>Calibration on the whole record</strong> (RMS), one physically bounded input at a time.</li>
  <li><strong>Calibrated values reported</strong>, with their effect on the design envelope.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><strong>Validating a surge model with a field pump-trip test</strong></li>
    <li><a href="surge-sensitivity-uncertainty.html">Sensitivity and uncertainty: bounding the result</a></li>
    <li><a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip: inertia, specific speed and four-quadrant curves</a></li>
    <li><a href="transient-model-demands-network-detail.html">Demands, branches and dead ends in a transient model</a></li>
    <li><a href="surge-envelope-pipe-pressure-limits.html">Reading the surge envelope against the pipe's real limits</a></li>
    <li><a href="transient-forces-pipe-supports.html">Transient forces on pipe supports and bends</a></li>
    <li><a href="booster-stations-series-surge.html">Booster stations in series</a></li>
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
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1), fmt2=v=>v.toFixed(2);
/* ---------- CHART 1 : logging rate ---------- */
const sFs=document.getElementById('sFs'), sPh=document.getElementById('sPh'), sWin=document.getElementById('sWin');
const T=D.t, PT=D.pump_true;
const sampChart=new Chart(document.getElementById('sampChart'),{
  data:{datasets:[
    {type:'line',label:'True pressure at the pump, 100 Hz (m)',data:T.map((t,k)=>({x:t,y:PT[k]})),borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.2,pointRadius:0,order:2},
    {type:'line',label:'Logged samples (m)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.4,pointRadius:3,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:40,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:-5,max:145,title:{display:true,text:'Pressure head at the pump (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt2(c.parsed.x)} s`}}}}
});
const sampled=(arr,step,off)=>{const o=[];for(let k=off;k<arr.length;k+=step)o.push(k);return o;};
function updSamp(){
  const fs=+sFs.value, step=Math.round(100/fs), off=Math.min(step-1,Math.floor(+sPh.value/100*step)), win=+sWin.value;
  document.getElementById('vPh').textContent=sPh.value+' %';
  document.getElementById('vWin').textContent='0–'+win+' s';
  const idx=sampled(PT,step,off);
  sampChart.data.datasets[1].data=idx.map(k=>({x:T[k],y:PT[k]}));
  sampChart.options.scales.x.max=win; sampChart.update('none');
  const tmx=Math.max(...PT), tmn=Math.min(...PT), lmx=Math.max(...idx.map(k=>PT[k])), lmn=Math.min(...idx.map(k=>PT[k]));
  let worst=0; for(let o=0;o<step;o++){const m=Math.max(...sampled(PT,step,o).map(k=>PT[k])); worst=Math.max(worst,tmx-m);}
  document.getElementById('rTmx').innerHTML=fmt1(tmx)+' <small>m</small>';
  document.getElementById('rLmx').innerHTML=fmt1(lmx)+' <small>m</small>';
  document.getElementById('rMis').innerHTML=fmt1(tmx-lmx)+' <small>m</small>';
  document.getElementById('rWmis').innerHTML=fmt1(worst)+' <small>m</small>';
  document.getElementById('rMn').innerHTML=fmt2(tmn)+' / '+fmt2(lmn)+' <small>m</small>';
}
[sFs,sPh,sWin].forEach(s=>s.addEventListener('input',updSamp));updSamp();

/* ---------- CHART 2 : arrival time ---------- */
const sFs2=document.getElementById('sFs2'), sThr=document.getElementById('sThr');
const N4=T.findIndex(t=>t>4.0);
const arrChart=new Chart(document.getElementById('arrChart'),{
  data:{datasets:[
    {type:'line',label:'Logged at 2 km (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:1.4,pointRadius:2,order:2},
    {type:'line',label:'Logged at the pump (m)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:1.2,pointRadius:0,order:3},
    {type:'scatter',label:'Arrival detected',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:4,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:0,max:90,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt2(c.parsed.y)} m at ${fmt2(c.parsed.x)} s`}},
      annotation:{annotations:{tr:{type:'line',xMin:2.0,xMax:2.0,borderColor:'#7f8c8d',borderWidth:1,borderDash:[3,3],label:{display:true,content:'x/a at 1,000 m/s',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(127,140,141,0.9)'}}}}}}
});
function updArr(){
  const fs=+sFs2.value, step=Math.round(100/fs), thr=+sThr.value;
  document.getElementById('vThr').textContent=fmt1(thr)+' m';
  const idx=sampled(D.mid,step,0).filter(k=>k<=N4);
  arrChart.data.datasets[0].data=idx.map(k=>({x:T[k],y:D.mid[k]}));
  arrChart.data.datasets[1].data=sampled(D.pump,step,0).filter(k=>k<=N4).map(k=>({x:T[k],y:D.pump[k]}));
  const h0=D.mid[0];
  const kd=sampled(D.mid,step,0).find(k=>D.mid[k]<h0-thr);
  arrChart.data.datasets[2].data=kd!==undefined?[{x:T[kd],y:D.mid[kd]}]:[];
  arrChart.update('none');
  if(kd===undefined){['rTa','rAe','rAr'].forEach(i=>document.getElementById(i).innerHTML='<small>not detected</small>');return;}
  const ta=T[kd], dt=1/fs, a=2000/ta;
  document.getElementById('rTa').innerHTML=fmt2(ta)+' <small>s</small>';
  document.getElementById('rAe').innerHTML=fmt0(a)+' <small>m/s</small>';
  document.getElementById('rAr').innerHTML=fmt0(2000/(ta+dt))+'–'+(ta-dt>0?fmt0(2000/(ta-dt)):'∞')+' <small>m/s</small>';
}
[sFs2,sThr].forEach(s=>s.addEventListener('input',updArr));updArr();

/* ---------- CHART 3 : calibration ---------- */
const sCa=document.getElementById('sCa'), sCi=document.getElementById('sCi');
const MT=[],MP=[],MM=[];for(let k=0;k<T.length;k+=10){MT.push(T[k]);MP.push(D.pump[k]);MM.push(D.mid[k]);}
function interp(ts,ys,t){let lo=0,hi=ts.length-1;if(t<=ts[0])return ys[0];if(t>=ts[hi])return ys[hi];while(hi-lo>1){const m=(lo+hi)>>1;if(ts[m]<=t)lo=m;else hi=m;}return ys[lo]+(ys[hi]-ys[lo])*(t-ts[lo])/(ts[hi]-ts[lo]);}
function rms(m){let s=0,n=0;for(let k=0;k<MT.length;k++){if(MT[k]>30)break;const a=interp(m.t,m.pump,MT[k])-MP[k],b=interp(m.t,m.mid,MT[k])-MM[k];s+=a*a+b*b;n+=2;}return Math.sqrt(s/n);}
const RM=D.models.map(m=>rms(m));
const calChart=new Chart(document.getElementById('calChart'),{
  data:{datasets:[
    {type:'scatter',label:'Measured at the pump',data:MT.map((t,k)=>({x:t,y:MP[k]})),backgroundColor:'rgba(185,119,14,0.55)',pointRadius:1.6,order:3},
    {type:'scatter',label:'Measured at 2 km',data:MT.map((t,k)=>({x:t,y:MM[k]})),backgroundColor:'rgba(27,79,114,0.55)',pointRadius:1.6,order:4},
    {type:'line',label:'Model at the pump',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2,pointRadius:0,order:1},
    {type:'line',label:'Model at 2 km',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0,order:2}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:40,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:-5,max:145,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}}}}
});
function updCal(){
  const a=+sCa.value, I=+sCi.value, i=D.models.findIndex(m=>m.a===a&&m.I===I), m=D.models[i];
  calChart.data.datasets[2].data=m.t.map((t,k)=>({x:t,y:m.pump[k]}));
  calChart.data.datasets[3].data=m.t.map((t,k)=>({x:t,y:m.mid[k]}));
  calChart.update('none');
  let b=0; RM.forEach((r,j)=>{if(r<RM[b])b=j;});
  document.getElementById('rRms').innerHTML=fmt2(RM[i])+' <small>m</small>';
  document.getElementById('rBest').innerHTML=fmt0(D.models[b].a)+' m/s, '+fmt0(D.models[b].I)+' kg·m² ('+fmt2(RM[b])+' m)';
  document.getElementById('rMm').innerHTML=(m.line_min<0?'−':'+')+fmt2(Math.abs(m.line_min))+' <small>m</small>';
  document.getElementById('rMx').innerHTML=fmt1(Math.max(...m.pump))+' <small>m</small>';
  document.getElementById('rMeas').innerHTML=fmt1(Math.max(...D.pump))+' <small>m</small>';
}
[sCa,sCi].forEach(s=>s.addEventListener('input',updCal));updCal();
window.addEventListener('load',function(){try{[sampChart,arrChart,calChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: wave propagation, pump boundary conditions and the comparison of computed and measured transients.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014: field tests, measured wave speeds and model verification.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: instrumentation for transient measurements and site testing of pumping mains.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: field verification of transient models and the value of high-speed pressure loggers.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006: measured and computed transients, and what a record can and cannot identify.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, its pump station and the verified MOC solver used for the synthetic record and the model runs.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: report points, report period, time-history graphs, alternatives and scenarios.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #FieldTest #ModelCalibration #ModelValidation #PumpTripTest #PressureTransducer #DataLogger #SamplingRate #WaveSpeed #SCADA #BentleyHAMMER #TransientAnalysis #PumpStation #TransmissionMain #WaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'practice2.json')))['s12']
DATA = {'t': _A['t'], 'pump': _A['pump'], 'mid': _A['mid'], 'pump_true': _A['pump_true'],
        'models': [{k: m[k] for k in ('a', 'I', 't', 'pump', 'mid', 'line_min')} for m in _A['models']]}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='surge-model-field-validation', cat='surge', mins=16,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Validating a Surge Model with a Field Pump-Trip Test: Loggers, Wave Speed and Calibration',
    reg_title='Validating a Surge Model with a Field Pump-Trip Test: Loggers, Wave Speed and Calibration',
    reg_tag='Surge Analysis · Field Test · Calibration',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Field Test &middot; Calibration',
    desc='How to validate a surge model with a pump-trip test: transducer positions and logging rates, what 1 Hz SCADA misses, reading the wave speed from the arrival time, and calibrating wave speed and inertia against the whole record, with three interactive charts and the HAMMER steps.',
    og_desc='Logged at 1 Hz, a pump-trip peak of 134 m can read as anything from 109 to 134 m. At 100 Hz the arrival time gives the wave speed to 1 %, and fixing it first cuts the model error from 12.9 m to 2.6 m RMS.',
    ld_desc='Field validation of a hydraulic transient model: instrumentation, logging rate, wave speed from arrival time, and calibration of wave speed and pump inertia, worked on a synthetic pump-trip record with the HAMMER steps.',
    img_alt='Field engineers at a pump station during a surge test: a pressure transducer on a tapping of the discharge main, a data logger and laptop showing a fast pressure trace, and the pipeline running into the distance',
    en_tag='Surge &amp; Transient Analysis &middot; Field Test',
    en_title='Validating a Surge Model with a Field Pump-Trip Test: Loggers, Wave Speed and Calibration',
    en_excerpt='Logged at 1 Hz, a pump-trip peak of <strong>134 m</strong> can read as anything from 109 to 134 m. At 100 Hz the arrival time 2 km out gives the wave speed to <strong>1 %</strong>, and fixing it first cuts the model error from <strong>12.9 m to 2.6 m</strong> RMS before inertia is touched. Transducers, logging rates, wave speed from the record and calibration without forcing the fit, with three interactive charts.',
    en_search='surge model validation field test pump trip test calibration pressure transducer data logger sampling rate 100 Hz SCADA 1 Hz wave speed arrival time travel time RMS fit pump inertia calibration measured transient record Bentley HAMMER report points time history water hammer transmission main',
    ar_title='التحقق من نموذج المطرقة المائية باختبار توقف مضخة ميدانياً: المسجلات وسرعة الموجة والمعايرة',
    ar_excerpt='عند تسجيل الضغط بمعدل قراءة واحدة في الثانية يمكن أن يظهر ضغط أقصى قدره <strong>١٣٤ م</strong> بأي قيمة بين ١٠٩ و١٣٤ م. وعند ١٠٠ قراءة في الثانية يعطي زمن وصول الموجة سرعتها بدقة <strong>١٪</strong>، وتثبيتها أولاً يخفض خطأ النموذج من ١٢٫٩ م إلى ٢٫٦ م. مع ثلاثة رسوم تفاعلية.',
    ar_search='التحقق من النموذج اختبار ميداني توقف المضخة معايرة النموذج حساس الضغط مسجل البيانات معدل التسجيل سرعة الموجة زمن الوصول القصور الذاتي المطرقة المائية الطرق المائي بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
