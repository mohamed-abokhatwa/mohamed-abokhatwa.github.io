# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">The reference vessel design on the 12&nbsp;km main keeps the line at <strong>+4.33&nbsp;m</strong> against a +3.0&nbsp;m criterion: a pass, with 1.33&nbsp;m to spare. That single run assumes one wave speed, one friction, one gas volume, one gas law and one flow. Move each within a plausible range and the minimum runs from <strong>+0.29 to +8.45&nbsp;m</strong> on the gas law alone. Sample all seven together, 300 times, and <strong>31&nbsp;%</strong> of the combinations fail the criterion, while the maximum reaches 143&nbsp;m in the worst of them, above the 136&nbsp;m limit. This article shows how to find which inputs matter, how to bound the result, and how to turn a single number into a design that survives its own uncertainty.</p>

<h2 id="why">1 &middot; One run is one point in a cloud</h2>
<p>Every input to a surge model carries an uncertainty, and some carry a lot [1][2]:</p>
<ul class="clean">
  <li><strong>Wave speed:</strong> &plusmn;10&nbsp;% is common for a buried main before it is measured (see <a href="wave-speed-surge-analysis.html">wave speed</a>).</li>
  <li><strong>Friction:</strong> new pipe against pipe after years of service; &plusmn;15&nbsp;% on the head loss at duty.</li>
  <li><strong>Vessel gas volume:</strong> the level control holds it within a band, typically &plusmn;10&nbsp;% (see <a href="pre-charge-pressure.html">pre-charge pressure</a>).</li>
  <li><strong>Gas law exponent:</strong> between isothermal (1.0) and adiabatic (1.4); 1.2 is a convention, not a measurement.</li>
  <li><strong>Connection loss:</strong> &plusmn;30&nbsp;% on the loss coefficients of the vessel connection and its orifice.</li>
  <li><strong>Flow:</strong> &plusmn;10&nbsp;% on the duty, for operating points and future demand.</li>
  <li><strong>Delivery level:</strong> &plusmn;3&nbsp;m on the reservoir HGL.</li>
</ul>
<p>The base case is the vessel design of the surge series: 3.5&nbsp;m&sup3; of gas, a DN400 connection with a differential orifice (loss coefficients 2 out and 10 in), on the 12&nbsp;km DN800 ductile iron main at 0.70&nbsp;m&sup3;/s, with the pump modelled as stopping at once [3]. Every run below is a full transient run of the trip, 150&nbsp;s, with the same solver.</p>

<h2 id="tornado">2 &middot; One at a time: the tornado</h2>
<p>The first step is to move each input to the ends of its range with everything else at base, and see how far the result moves. Sorted by size, the bars form a tornado [2][4].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">What moves the result most</div>
    <div class="fsub">Reference vessel design, pump trip, 150&nbsp;s runs. Each bar spans the result with the input at the low and the high end of its range, everything else at base. Bars sorted by span. The base case is the vertical line.</div>
  </div>
  <div class="chart-box"><canvas id="torChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Result</label>
      <select id="sOut">
        <option value="min" selected>Lowest head on the line</option>
        <option value="max">Highest head on the line</option>
      </select>
      <div class="hint">The two limits are driven by different inputs.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Base case</div><div class="v" id="rBase">&ndash;</div></div>
    <div class="cell"><div class="k">Most influential</div><div class="v" id="rTop" style="font-size:15px;margin-top:6px;">&ndash;</div></div>
    <div class="cell"><div class="k">Its span</div><div class="v" id="rSpan">&ndash;</div></div>
    <div class="cell"><div class="k">Least influential</div><div class="v" id="rLow" style="font-size:15px;margin-top:6px;">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">For the minimum, the gas law exponent dominates: +8.45&nbsp;m isothermal, +0.29&nbsp;m adiabatic. Flow (+5.67 to +2.26&nbsp;m) and the gas volume tolerance (+2.68 to +5.64&nbsp;m) follow. Wave speed barely matters (+3.93 to +4.42&nbsp;m): the vessel works on the mass oscillation, not on the water hammer wave. For the maximum the order changes: the gas law and friction lead, each moving the peak by about 16&nbsp;m. One tornado per limit is needed.</p>

<h2 id="sweep">3 &middot; Shape, not only span</h2>
<p>A tornado shows the ends of each range. Sweeping an input across its range shows whether the response is linear, whether it has a threshold, and where the criterion is crossed.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">One input across its range</div>
    <div class="fsub">Seven runs across the range of the chosen input, everything else at base. Lowest head on the left axis, highest head on the right.</div>
  </div>
  <div class="chart-box"><canvas id="swChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Input</label>
      <select id="sPar">
        <option value="0">Wave speed</option>
        <option value="1">Friction loss at duty</option>
        <option value="2">Gas volume at steady flow</option>
        <option value="3" selected>Gas law exponent</option>
        <option value="4">Connection loss (factor)</option>
        <option value="5">Flow</option>
        <option value="6">Delivery level</option>
      </select>
      <div class="hint">The base value is marked.</div>
    </div>
    <div class="ctrl">
      <label>Design minimum <span id="vCr">+3.0 m</span></label>
      <input type="range" id="sCr" min="-5" max="8" value="3" step="0.5">
      <div class="hint">Check it against the project's allowable values.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Range of the input</div><div class="v" id="rRng" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest head across it</div><div class="v" id="rSwMin" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Highest head across it</div><div class="v" id="rSwMax" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Criterion met over</div><div class="v" id="rMet">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The gas law exponent moves the minimum steeply: from about 1.25 upwards the reference design falls below +3.0&nbsp;m. Gas volume is close to linear, about 0.15&nbsp;m of minimum for every 1&nbsp;% of gas, flattening at the top of the range. Friction works the other way from intuition: more friction damps the oscillation and raises the minimum. Lower the criterion to &minus;3&nbsp;m (only where the project specification and the manufacturers' ratings allow it) and every input passes across its whole range.</p>

<h2 id="together">4 &middot; All together: sampling the cloud</h2>
<p>Inputs do not wait for each other to be unfavourable. We drew 300 combinations, each input uniform within its range and independent of the others, and ran the trip for each [4][5]. Uniform sampling is deliberately plain: it says only that every value in the range is plausible, which is usually all a designer can defend.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">300 plausible versions of the same design</div>
    <div class="fsub">Distribution of the lowest head on the line over 300 runs with all seven inputs sampled uniformly within their ranges. Bins of 0.5&nbsp;m. The bars below the criterion are the share of plausible systems that fail it.</div>
  </div>
  <div class="chart-box"><canvas id="mcChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Design minimum <span id="vCr2">+3.0 m</span></label>
      <input type="range" id="sCr2" min="-5" max="8" value="3" step="0.5">
      <div class="hint">As above.</div>
    </div>
    <div class="ctrl">
      <label>Maximum limit <span id="vMx">136 m</span></label>
      <input type="range" id="sMx" min="110" max="160" value="136" step="1">
      <div class="hint">Project limit of this series.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Runs below the minimum</div><div class="v" id="rFail">&ndash;</div></div>
    <div class="cell"><div class="k">5th percentile of the minimum</div><div class="v" id="rP5">&ndash;</div></div>
    <div class="cell"><div class="k">Median of the minimum</div><div class="v" id="rP50">&ndash;</div></div>
    <div class="cell"><div class="k">Runs above the maximum limit</div><div class="v" id="rOver">&ndash;</div></div>
    <div class="cell"><div class="k">95th percentile of the maximum</div><div class="v" id="rP95">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The median of the 300 runs (+4.56&nbsp;m) is close to the base case, but 31&nbsp;% of them fall below +3.0&nbsp;m, the 5th percentile is &minus;0.43&nbsp;m and the lowest is &minus;2.91&nbsp;m. At the top, 5&nbsp;% of the runs exceed 129.8&nbsp;m and the worst reaches 143.4&nbsp;m, above the 136&nbsp;m limit. The single run said &ldquo;pass with 1.3&nbsp;m to spare&rdquo;; the cloud says the design passes in about two systems out of three.</p>

<h2 id="corner">5 &middot; From a range to a robust design</h2>
<p>Two ways to design for the cloud are common [2][5]:</p>
<ul class="clean">
  <li><strong>The corner case.</strong> Run every input at its unfavourable end together. On this main that is the high wave speed, high friction, low gas, adiabatic gas, high connection loss, high flow and low delivery level, and it gives &minus;4.85&nbsp;m. A vessel sized so that even this corner meets +3.0&nbsp;m needs <strong>5.30&nbsp;m&sup3;</strong> of gas instead of 3.5, which at the nominal inputs gives +8.84&nbsp;m. Corners are conservative, because all the inputs are rarely unfavourable at once, but they are simple and defensible.</li>
  <li><strong>A percentile.</strong> Choose the design so that, say, 95&nbsp;% of sampled systems meet the criterion. It is less conservative and needs the sampling to be repeated for each candidate size.</li>
</ul>
<p>Whichever is used, the inputs that dominate the tornado are where effort pays: here, specify the vessel's gas volume band tightly, justify the gas law with the expected rate of compression, and confirm the design flow range. Measuring the wave speed (see <a href="surge-model-field-validation.html">field validation</a>) would barely change this answer, because the vessel works on the mass oscillation; on an unprotected main or one protected by air valves, the order would be different.</p>

<div class="tbl-wrap"><table>
  <caption>Reference vessel design: the result as a single run, as a range and as a corner case</caption>
  <thead><tr><th>Basis</th><th class="num">Lowest head (m)</th><th class="num">Highest head (m)</th><th>Verdict at +3.0&nbsp;m / 136&nbsp;m</th></tr></thead>
  <tbody>
    <tr><td>Single base run</td><td class="num">+4.33</td><td class="num">119.2</td><td><span class="badge good">passes</span></td></tr>
    <tr><td>300 sampled runs, 5th / 95th percentile</td><td class="num">&minus;0.43</td><td class="num">129.8</td><td><span class="badge warn">fails 31&nbsp;% of the time</span></td></tr>
    <tr><td>Corner case, 3.5&nbsp;m&sup3; of gas</td><td class="num">&minus;4.85</td><td class="num">118.0</td><td><span class="badge bad">fails</span></td></tr>
    <tr><td>Corner case, 5.30&nbsp;m&sup3; of gas</td><td class="num">+3.00</td><td class="num">101.0</td><td><span class="badge good">passes</span></td></tr>
  </tbody>
</table></div>

<h2 id="what-to-vary">6 &middot; What to vary, and what not to</h2>
<p>Not everything in a model is uncertain in the same way, and treating every input alike blurs the answer [1][2].</p>
<ul class="clean">
  <li><strong>Physical uncertainties</strong> (wave speed, friction, inertia, gas law) belong in the ranges. Their bounds come from data, tests or the literature.</li>
  <li><strong>Operating states</strong> (flow, number of pumps, reservoir levels) are not uncertain at all: each is a separate scenario that the design must pass, not a range to be averaged over. We include them in the sampling only to see their weight, and design for each one explicitly.</li>
  <li><strong>Design choices</strong> (the criterion, the vessel size, the orifice ratio) are what the analysis is meant to fix. They are never sampled.</li>
  <li><strong>Model choices</strong> (the cavity model, the time step) are checked separately, as in <a href="surge-model-time-step-convergence.html">Is your HAMMER run right?</a>, and their effect reported alongside the range.</li>
  <li><strong>Correlated inputs</strong> should move together. Friction and the operating flow are linked through the pump curve; the gas volume and its pressure through the level control. Sampling them independently can create combinations that cannot happen.</li>
</ul>
<p>The ranges in this article are illustrative. On a project, write each one down with its source in the assumptions register (see <a href="surge-study-report-review-checklist.html">The surge study report</a>), and check the minimum used against the allowable values in the project specification and the manufacturers&rsquo; ratings.</p>

<h2 id="report">7 &middot; Reporting a range</h2>
<p>A surge report that gives one number for each limit implies a precision the model does not have. We report:</p>
<ul class="clean">
  <li>the base result, the inputs behind it, and the ranges assumed for each input with their source;</li>
  <li>the tornado for each limit, so a reviewer can see which inputs matter;</li>
  <li>the corner case or the percentile used for the design, and the margin it leaves;</li>
  <li>the inputs that should be pinned down by specification or test, because they dominate.</li>
</ul>
<p>The structure is in <a href="surge-study-report-review-checklist.html">The surge study report</a>.</p>

<h2 id="hammer">8 &middot; Running it in Bentley HAMMER</h2>
<p>Field names differ slightly between versions [6].</p>
<ol>
  <li><strong>Create one alternative per uncertain input</strong> (physical properties for wave speed and friction, initial settings for flows and levels, the hydropneumatic tank's gas volume and gas law exponent, the connection's loss coefficients), each with a low and a high version.</li>
  <li><strong>Create a scenario for each low and high</strong>, changing only that input, and use <strong>Batch Run</strong> to compute them together.</li>
  <li><strong>Tabulate the envelope extremes</strong> of each scenario from the results tables, and build the tornado from them.</li>
  <li><strong>Build the corner scenario</strong> by combining the unfavourable alternatives.</li>
  <li><strong>For sampling</strong>, script the inputs (HAMMER's programming interfaces, or export, edit and re-import the input) and collect the extremes; or sample a reduced set of inputs that the tornado shows to matter.</li>
  <li><strong>Size the protection on the chosen basis</strong>, then rerun the base and the corner with the final size.</li>
</ol>

<h2 id="checklist">9 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Range set for every uncertain input</strong>, with its source.</li>
  <li><strong>Tornado for the minimum and for the maximum</strong>, sorted by span.</li>
  <li><strong>Sweeps</strong> for the dominant inputs, looking for thresholds.</li>
  <li><strong>Combined uncertainty</strong>: corner case or sampled percentile, stated.</li>
  <li><strong>Design sized on that basis</strong>, with the margin reported.</li>
  <li><strong>Dominant inputs pinned down</strong> by specification, test or operating rule.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><a href="surge-model-field-validation.html">Validating a surge model with a field pump-trip test</a></li>
    <li><strong>Sensitivity and uncertainty: bounding the result</strong></li>
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
const sgn=(v,d)=>(v<-0.0049?'−':(v>0.0049?'+':''))+Math.abs(v).toFixed(d);
const P=D.par, B=D.base;
const fv=(p,v)=>p.key==='a'?fmt0(v)+' m/s':p.key==='Q'?fmt2(v)+' m³/s':p.key==='V0'?fmt2(v)+' m³':p.key==='hf'||p.key==='hdn'?fmt1(v)+' m':fmt2(v);
/* ---------- CHART 1 : tornado ---------- */
const sOut=document.getElementById('sOut');
const torChart=new Chart(document.getElementById('torChart'),{
  data:{labels:[],datasets:[{type:'bar',label:'Span over the input range (m)',data:[],backgroundColor:[],borderWidth:0,barPercentage:0.7}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,indexAxis:'y',
    scales:{x:{type:'linear',title:{display:true,text:'Result (m)',font:TTL},...AX},y:{...AX}},
    plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>{const r=c.raw;return `${fmt2(r[0])} to ${fmt2(r[1])} m`;}}},
      annotation:{annotations:{base:{type:'line',xMin:0,xMax:0,borderColor:'#111',borderWidth:1.4,label:{display:true,content:'base',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(17,17,17,0.8)'}},
        crit:{type:'line',xMin:3,xMax:3,borderColor:'#1e8449',borderWidth:1.2,borderDash:[5,4]}}}}}
});
function updTor(){
  const o=sOut.value, rows=P.map(p=>({lab:p.label,lo:Math.min(p.at_lo[o],p.at_hi[o]),hi:Math.max(p.at_lo[o],p.at_hi[o]),span:Math.abs(p.at_hi[o]-p.at_lo[o])}))
    .sort((a,b)=>b.span-a.span);
  torChart.data.labels=rows.map(r=>r.lab);
  torChart.data.datasets[0].data=rows.map(r=>[r.lo,r.hi]);
  torChart.data.datasets[0].backgroundColor=rows.map((r,i)=>i===0?'#c0392b':(i<3?'#b9770e':'#1b4f72'));
  const A=torChart.options.plugins.annotation.annotations; A.base.xMin=B[o]; A.base.xMax=B[o];
  A.crit.display=(o==='min'); A.crit.xMin=o==='min'?3:136; A.crit.xMax=A.crit.xMin; A.crit.display=true;
  torChart.update('none');
  document.getElementById('rBase').innerHTML=(o==='min'?sgn(B[o],2):fmt2(B[o]))+' <small>m</small>';
  document.getElementById('rTop').innerHTML=rows[0].lab;
  document.getElementById('rSpan').innerHTML=fmt2(rows[0].span)+' <small>m</small>';
  document.getElementById('rLow').innerHTML=rows[rows.length-1].lab+' ('+fmt2(rows[rows.length-1].span)+' m)';
}
sOut.addEventListener('input',updTor);updTor();

/* ---------- CHART 2 : sweep ---------- */
const sPar=document.getElementById('sPar'), sCr=document.getElementById('sCr');
const swChart=new Chart(document.getElementById('swChart'),{
  data:{datasets:[
    {type:'line',label:'Lowest head (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:4,yAxisID:'y',order:2},
    {type:'line',label:'Highest head (m, right)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.8,borderDash:[5,4],pointRadius:3,yAxisID:'y1',order:3},
    {type:'scatter',label:'Base',data:[],backgroundColor:'#111',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',title:{display:true,text:'',font:TTL},...AX},
            y:{type:'linear',min:-2,max:12,position:'left',title:{display:true,text:'Lowest head on the line (m)',font:TTL},...AX},
            y1:{type:'linear',min:95,max:135,position:'right',title:{display:true,text:'Highest head (m)',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','').replace(' (m, right)','')}: ${fmt2(c.parsed.y)} m`}},
      annotation:{annotations:{crit:{type:'line',yScaleID:'y',yMin:3,yMax:3,borderColor:'#1e8449',borderWidth:1.4,borderDash:[6,4],label:{display:true,content:'+3.0 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}}}}}}
});
function updSw(){
  const p=P[+sPar.value], cr=+sCr.value;
  document.getElementById('vCr').textContent=sgn(cr,1)+' m';
  swChart.data.datasets[0].data=p.sweep.map(s=>({x:s.v,y:s.min}));
  swChart.data.datasets[1].data=p.sweep.map(s=>({x:s.v,y:s.max}));
  swChart.data.datasets[2].data=[{x:p.base,y:B.min}];
  swChart.options.scales.x.title.text=p.label+(p.unit?' ('+p.unit+')':'');
  swChart.options.scales.x.min=p.lo; swChart.options.scales.x.max=p.hi;
  const a=swChart.options.plugins.annotation.annotations.crit; a.yMin=cr; a.yMax=cr; a.label.content=sgn(cr,1)+' m';
  swChart.update('none');
  const mins=p.sweep.map(s=>s.min), maxs=p.sweep.map(s=>s.max), ok=p.sweep.filter(s=>s.min>=cr).length;
  document.getElementById('rRng').innerHTML=fv(p,p.lo)+' to '+fv(p,p.hi);
  document.getElementById('rSwMin').innerHTML=sgn(Math.min(...mins),2)+' to '+sgn(Math.max(...mins),2)+' <small>m</small>';
  document.getElementById('rSwMax').innerHTML=fmt1(Math.min(...maxs))+' to '+fmt1(Math.max(...maxs))+' <small>m</small>';
  document.getElementById('rMet').innerHTML=ok+' <small>of 7 points</small>';
}
[sPar,sCr].forEach(s=>s.addEventListener('input',updSw));updSw();

/* ---------- CHART 3 : sampled cloud ---------- */
const sCr2=document.getElementById('sCr2'), sMx=document.getElementById('sMx');
const MN=D.mc.map(r=>r.min).sort((a,b)=>a-b), MX=D.mc.map(r=>r.max).sort((a,b)=>a-b), NR=MN.length;
const pct=(arr,p)=>{const i=(arr.length-1)*p, lo=Math.floor(i), hi=Math.ceil(i); return arr[lo]+(arr[hi]-arr[lo])*(i-lo);};
const BIN=0.5, B0=Math.floor(MN[0]/BIN)*BIN, NB=Math.ceil((MN[NR-1]-B0)/BIN)+1;
const centres=[], counts=[]; for(let k=0;k<NB;k++){centres.push(B0+BIN*(k+0.5)); counts.push(0);} MN.forEach(v=>{counts[Math.min(NB-1,Math.floor((v-B0)/BIN))]++;});
const mcChart=new Chart(document.getElementById('mcChart'),{
  data:{labels:centres.map(c=>fmt2(c)),datasets:[{type:'bar',label:'Runs',data:counts,backgroundColor:[],borderWidth:0,barPercentage:1,categoryPercentage:0.95}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{title:{display:true,text:'Lowest head on the line, bin centre (m)',font:TTL},...AX},y:{title:{display:true,text:'Number of runs (of 300)',font:TTL},...AX}},
    plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>`${c.parsed.y} runs`}}}}
});
function updMc(){
  const cr=+sCr2.value, mx=+sMx.value;
  document.getElementById('vCr2').textContent=sgn(cr,1)+' m';
  document.getElementById('vMx').textContent=mx+' m';
  mcChart.data.datasets[0].backgroundColor=centres.map(c=>c+BIN/2<=cr?'#c0392b':(c-BIN/2<cr?'#b9770e':'#1b4f72'));
  mcChart.update('none');
  const fail=MN.filter(v=>v<cr).length, over=MX.filter(v=>v>mx).length;
  document.getElementById('rFail').innerHTML=fail+' <small>('+fmt0(100*fail/NR)+' %)</small>';
  document.getElementById('rP5').innerHTML=sgn(pct(MN,0.05),2)+' <small>m</small>';
  document.getElementById('rP50').innerHTML=sgn(pct(MN,0.5),2)+' <small>m</small>';
  document.getElementById('rOver').innerHTML=over+' <small>('+fmt0(100*over/NR)+' %)</small>';
  document.getElementById('rP95').innerHTML=fmt1(pct(MX,0.95))+' <small>m</small>';
}
[sCr2,sMx].forEach(s=>s.addEventListener('input',updMc));updMc();
window.addEventListener('load',function(){try{[torChart,swChart,mcChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: uncertain inputs in transient analysis and the need for sensitivity runs.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: the influence of wave speed, friction, gas law and pump data on surge results.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, its vessel design and the verified MOC solver.</li>
  <li>Saltelli, A. et al. <em>Global Sensitivity Analysis: The Primer</em>. Wiley, 2008: one-at-a-time and sampling-based sensitivity methods.</li>
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: the transient model and the gas law of a hydropneumatic vessel.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: alternatives, scenarios, batch run and results tables.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #SensitivityAnalysis #Uncertainty #TornadoChart #MonteCarlo #RobustDesign #SurgeVessel #GasLaw #WaveSpeed #BentleyHAMMER #TransientAnalysis #TransmissionMain #WaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'practice2.json')))['s13']
DATA = {'base': {k: _A['base'][k] for k in ('min', 'max')},
        'par': [{k: p[k] for k in ('key', 'label', 'unit', 'base', 'lo', 'hi')} | {'at_lo': {'min': p['at_lo']['min'], 'max': p['at_lo']['max']},
                 'at_hi': {'min': p['at_hi']['min'], 'max': p['at_hi']['max']}, 'sweep': [{'v': s['v'], 'min': s['min'], 'max': s['max']} for s in p['sweep']]} for p in _A['par']],
        'mc': [{'min': r['min'], 'max': r['max']} for r in _A['mc']]}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='surge-sensitivity-uncertainty', cat='surge', mins=15,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Sensitivity and Uncertainty in Surge Analysis: Bounding the Result Instead of Quoting One Number',
    reg_title='Sensitivity and Uncertainty in Surge Analysis: Bounding the Result Instead of Quoting One Number',
    reg_tag='Surge Analysis · Sensitivity · Uncertainty',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Sensitivity &middot; Uncertainty',
    desc='How to bound a surge result: input ranges, a tornado chart for each limit, sweeps that reveal thresholds, 300 sampled runs of the reference vessel design, and sizing on a corner case or a percentile, with three interactive charts and the HAMMER steps.',
    og_desc='The reference vessel design passes at +4.33 m in a single run. Sample its seven uncertain inputs 300 times and 31 % of the runs fail +3.0 m; a corner-case design needs 5.30 m³ of gas instead of 3.5.',
    ld_desc='Sensitivity and uncertainty in hydraulic transient analysis: tornado charts, sweeps, sampled runs and robust sizing of a surge vessel, with the Bentley HAMMER steps.',
    img_alt='A pipeline profile on a drawing grid with a bundle of many faint surge envelopes around one bold envelope, valves along the line, and a tornado chart of horizontal bars beside it',
    en_tag='Surge &amp; Transient Analysis &middot; Sensitivity',
    en_title='Sensitivity and Uncertainty in Surge Analysis: Bounding the Result Instead of Quoting One Number',
    en_excerpt='The reference vessel design passes at <strong>+4.33 m</strong> in one run. The gas law alone moves that from +0.29 to +8.45 m, and sampling all seven uncertain inputs 300 times makes <strong>31 %</strong> of the runs fail +3.0 m. A corner-case design needs <strong>5.30 m³</strong> of gas instead of 3.5. Tornado charts for each limit, sweeps, sampled runs and how to report a range, with three interactive charts.',
    en_search='surge sensitivity analysis uncertainty tornado chart Monte Carlo sampling corner case percentile robust design surge vessel gas law exponent polytropic wave speed friction flow delivery level connection loss Bentley HAMMER alternatives scenarios batch run water hammer transient analysis',
    ar_title='الحساسية وعدم اليقين في تحليل المطرقة المائية: حصر النتيجة بدلاً من رقم واحد',
    ar_excerpt='يجتاز تصميم خزان الحماية المرجعي المعيار في تشغيل واحد بضغط أدنى <strong>+٤٫٣٣ م</strong>. لكن قانون الغاز وحده ينقل ذلك بين +٠٫٢٩ و+٨٫٤٥ م، وأخذ ٣٠٠ عينة للمدخلات السبعة يجعل <strong>٣١٪</strong> منها تفشل في المعيار. والتصميم على أسوأ الحالات يحتاج <strong>٥٫٣٠ م³</strong> من الغاز بدلاً من ٣٫٥. مع ثلاثة رسوم تفاعلية.',
    ar_search='تحليل الحساسية عدم اليقين مخطط الإعصار محاكاة مونت كارلو أسوأ الحالات التصميم المتين خزان الحماية قانون الغاز سرعة الموجة المطرقة المائية الطرق المائي بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
