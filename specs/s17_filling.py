# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">More transmission mains are damaged while they are being filled or restarted than during the pump trip their surge study was written for. On the 12&nbsp;km reference main, filling at 0.3&nbsp;m/s means a closing air valve stops the column with a Joukowsky rise of <strong>32&nbsp;m</strong>; at 2&nbsp;m/s the same closure gives <strong>214&nbsp;m</strong>, above the line's 136&nbsp;m limit. Opening a filling valve fully from a 40&nbsp;m head into a 1&nbsp;km leg that holds 50&nbsp;m of trapped air drives that pocket to <strong>279&nbsp;m</strong>, seven times the driving head. Throttle the same fill to 0.3&nbsp;m/s and the pocket peaks at <strong>40.5&nbsp;m</strong>. This article sets out the physics, the rates and the air valve checks that keep filling, draining and restarting inside the limits, and what a full-pipe surge program such as HAMMER can and cannot show.</p>

<h2 id="why">1 &middot; Why filling is a surge event</h2>
<p>A pipe being filled is not full, and a pipe being drained is not empty. Both contain moving water and moving air, and air behaves very differently from water: it is 800 times lighter, a thousand times more compressible, and it escapes through an orifice far faster than water can follow it. Three mechanisms cause most of the damage [1][2][3]:</p>
<ul class="clean">
  <li><strong>Air valve slam.</strong> While air is leaving through a large orifice, the water behind it can reach high velocity. When the water arrives at the valve, the float shuts and the column stops abruptly.</li>
  <li><strong>Trapped air compressed by an accelerating column.</strong> A pocket that cannot escape acts as a spring. A column started suddenly from a high head overshoots and squeezes the pocket to several times the driving head.</li>
  <li><strong>Restarting into a partly drained line.</strong> After a trip or a drain-down, voids at high points refill at the full velocity of a running pump.</li>
</ul>
<p>The reference main of the surge series is a 12&nbsp;km DN800 ductile iron line with a wave speed of 1,050&nbsp;m/s, a steady HGL of 85.0&nbsp;m at the pump and a 136&nbsp;m project limit [4]. It holds 6,032&nbsp;m&sup3; of water.</p>

<h2 id="slam">2 &middot; Filling velocity and air valve slam</h2>
<p>When the water reaches an air valve, the float closes and the column that was moving at velocity \(v\) stops in a time much shorter than the wave travel time. The head rise is the Joukowsky value [5]:</p>
<div class="eq">\[ \Delta H \;=\; \frac{a\,v}{g}, \qquad 0.3\ \text{m/s:}\ \frac{1050 \times 0.3}{9.81} = 32.1\ \text{m}, \qquad 2.0\ \text{m/s:}\ 214.1\ \text{m} \]</div>
<p>The velocity that matters is the velocity of the water arriving at the valve, and while air is leaving freely that is close to the filling velocity. In a plastic pipe with a wave speed near 300&nbsp;m/s, the same velocities give 9.2 and 61.2&nbsp;m. The commonly quoted filling limit of about 0.3&nbsp;m/s (1&nbsp;ft/s), found in AWWA guidance on air valves, keeps the slam of a ductile iron main near 30&nbsp;m [1].</p>
<p>The other half of the check is the air valve itself. During filling, the free-air flow out of the valve equals the water flow in. Through an orifice the air needs a pressure difference to leave, and isentropic orifice flow gives [6]</p>
<div class="eq">\[ \dot m \;=\; C_d A\,p_0\sqrt{\frac{2\gamma}{(\gamma-1)RT_0}\left[\left(\frac{p}{p_0}\right)^{2/\gamma}-\left(\frac{p}{p_0}\right)^{(\gamma+1)/\gamma}\right]} \]</div>
<p>with \(C_d\) = 0.6, \(\gamma\) = 1.4 and the pressure ratio no lower than the critical 0.528, beyond which the flow is choked. Filling the reference main at 0.3&nbsp;m/s pushes 0.151&nbsp;m&sup3;/s of air out. A DN100 large orifice passes that at 0.006&nbsp;bar; a DN50 orifice needs 0.10&nbsp;bar with the air leaving at 77&nbsp;m/s. Too small an orifice slows the fill; too large an orifice on a fast fill lets the column accelerate into the valve. That is why anti-slam and two-stage air valves throttle the last of the air, and why the filling rate, not the valve size alone, sets the slam [1][7].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Filling rate, slam and the air the valves must pass</div>
    <div class="fsub">Slam head \(\Delta H = a v/g\) against filling velocity for the chosen wave speed, with ductile iron (1,050&nbsp;m/s) and PE (300&nbsp;m/s) for comparison. Air exhaust pressure from isentropic orifice flow, \(C_d\) = 0.6, 20&nbsp;&deg;C. 1&nbsp;bar = 10.21&nbsp;m.</div>
  </div>
  <div class="chart-box"><canvas id="slamChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Pipe</label>
      <select id="sDN">
        <option value="0.3">DN300</option>
        <option value="0.5">DN500</option>
        <option value="0.8" selected>DN800</option>
        <option value="1.2">DN1200</option>
      </select>
      <div class="hint">Internal diameter taken as the nominal.</div>
    </div>
    <div class="ctrl">
      <label>Filling velocity <span id="vV">0.30 m/s</span></label>
      <input type="range" id="sV" min="0.1" max="2" value="0.3" step="0.05">
      <div class="hint">Water velocity in the pipe while it fills.</div>
    </div>
    <div class="ctrl">
      <label>Wave speed <span id="vA">1,050 m/s</span></label>
      <input type="range" id="sA" min="200" max="1300" value="1050" step="10">
      <div class="hint">See the <a href="wave-speed-surge-analysis.html">wave speed article</a>.</div>
    </div>
    <div class="ctrl">
      <label>Section length <span id="vLs">12.0 km</span></label>
      <input type="range" id="sLs" min="0.5" max="30" value="12" step="0.5">
      <div class="hint">Between isolating valves.</div>
    </div>
    <div class="ctrl">
      <label>Air valve large orifice</label>
      <select id="sOr">
        <option value="50">DN50</option>
        <option value="80">DN80</option>
        <option value="100" selected>DN100</option>
        <option value="150">DN150</option>
        <option value="200">DN200</option>
      </select>
      <div class="hint">Effective orifice of the valve(s) venting the section.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Filling flow</div><div class="v" id="rQ">&ndash;</div></div>
    <div class="cell"><div class="k">Time to fill</div><div class="v" id="rT">&ndash;</div></div>
    <div class="cell"><div class="k">Slam head a·v/g</div><div class="v" id="rS">&ndash;</div></div>
    <div class="cell"><div class="k">Air exhaust pressure</div><div class="v" id="rDp">&ndash;</div></div>
    <div class="cell"><div class="k">Air speed in orifice</div><div class="v" id="rVo">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:14px;margin-top:6px;" id="rVer">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The verdict compares the slam head, added to the static head of a filled line at rest (44.8&nbsp;m here), with the 136&nbsp;m project limit, and flags an air exhaust pressure above 0.1&nbsp;bar. Filling the reference main at 0.3&nbsp;m/s takes 11.1&nbsp;hours; at 1&nbsp;m/s it takes 3.3&nbsp;hours, but the slam is 107&nbsp;m. Shorter sections between valves let each fill faster at the same velocity, because the time is set by the volume, not by the rate limit.</p>

<h2 id="pocket">3 &middot; Trapped air: the pocket that becomes a spring</h2>
<p>Where air cannot escape, for example at a high point with no air valve or a closed valve at the end of a section, the arriving column compresses it. Treating the water as a rigid column, which is valid while the pocket is large compared with the elastic storage of the pipe, gives a pair of equations that every analyst should be able to solve by hand [2][8][9]:</p>
<div class="eq">\[ \frac{dv}{dt} \;=\; \frac{g}{L_c}\left(H_R - H_p - K\frac{v|v|}{2g}\right) - \frac{f\,v|v|}{2D}, \qquad \frac{dV}{dt} = -A\,v, \qquad H_p V^{n} = H_{atm}V_0^{\,n} \]</div>
<p>Heads are absolute: \(H_R\) is the driving head plus the atmosphere (10.33&nbsp;m), \(H_p\) the pocket pressure, \(L_c\) the column length, \(K\) the loss coefficient of the filling valve or throttle, and \(n\) the gas law exponent. The pocket starts at atmospheric pressure with the column at rest.</p>
<p>Take a 1&nbsp;km DN800 leg filled from a 40&nbsp;m head through a valve opened fully, with 50&nbsp;m of pipe (25&nbsp;m&sup3;) of trapped air at its closed end. The column accelerates to <strong>3.76&nbsp;m/s</strong>, overshoots, and the pocket peaks at <strong>278.5&nbsp;m</strong> gauge 19&nbsp;s after opening: seven times the driving head and twice the project limit of this series. A throttle sized for a steady filling velocity of 0.3&nbsp;m/s keeps the column near that velocity, and the pocket rises slowly to 40.5&nbsp;m, barely above the driving head.</p>

<div class="tbl-wrap"><table>
  <caption>Filling a 1&nbsp;km DN800 leg from 40&nbsp;m against 50&nbsp;m of trapped air, rigid-column model, n = 1.2, f = 0.015</caption>
  <thead><tr><th>Filling valve</th><th class="num">Valve loss K</th><th class="num">Peak column velocity (m/s)</th><th class="num">Peak pocket pressure (m)</th><th class="num">Time to peak (s)</th></tr></thead>
  <tbody>
__THROTTLE__
  </tbody>
</table></div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Filling against a trapped air pocket</div>
    <div class="fsub">Rigid water column, polytropic pocket, filling valve loss \(K\) set for the chosen steady velocity (fully open: \(K\) = 1). Upper: pocket pressure and column velocity against time. Lower: the first peak against pocket size for the same settings, with the water hammer value \(a v_{max}/g\) (\(a\) = 1,050&nbsp;m/s) at the velocity reached. Pocket size on a log scale. RK4 integration, 5&nbsp;ms step.</div>
  </div>
  <div class="chart-box"><canvas id="pockChart"></canvas></div>
  <div class="chart-box" style="height:300px;"><canvas id="peakChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Driving head <span id="vH">40 m</span></label>
      <input type="range" id="sH" min="10" max="100" value="40" step="5">
      <div class="hint">Gauge, at the pocket's elevation.</div>
    </div>
    <div class="ctrl">
      <label>Column length <span id="vL">1,000 m</span></label>
      <input type="range" id="sL" min="100" max="5000" value="1000" step="100">
      <div class="hint">Water accelerating behind the pocket.</div>
    </div>
    <div class="ctrl">
      <label>Trapped air, as pipe length <span id="vP">50 m</span></label>
      <input type="range" id="sP" min="0" max="20" value="12" step="1">
      <div class="hint">From 1 to 500&nbsp;m of pipe.</div>
    </div>
    <div class="ctrl">
      <label>Filling valve</label>
      <select id="sK">
        <option value="0" selected>Fully open</option>
        <option value="2">Throttled for 2.0 m/s</option>
        <option value="1">Throttled for 1.0 m/s</option>
        <option value="0.5">Throttled for 0.5 m/s</option>
        <option value="0.3">Throttled for 0.3 m/s</option>
      </select>
      <div class="hint">\(K = 2gH/v^2 - fL/D - 1\), at least 1.</div>
    </div>
    <div class="ctrl">
      <label>Pipe</label>
      <select id="sD2">
        <option value="0.3">DN300</option>
        <option value="0.5">DN500</option>
        <option value="0.8" selected>DN800</option>
        <option value="1.2">DN1200</option>
      </select>
      <div class="hint">Friction factor 0.015.</div>
    </div>
    <div class="ctrl">
      <label>Gas law exponent</label>
      <select id="sN">
        <option value="1.0">1.0 (isothermal)</option>
        <option value="1.2" selected>1.2</option>
        <option value="1.4">1.4 (adiabatic)</option>
      </select>
      <div class="hint">A fast compression is close to adiabatic.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Peak pocket pressure</div><div class="v" id="rPk">&ndash;</div></div>
    <div class="cell"><div class="k">Times the driving head</div><div class="v" id="rRat">&ndash;</div></div>
    <div class="cell"><div class="k">Time to peak</div><div class="v" id="rTp">&ndash;</div></div>
    <div class="cell"><div class="k">Peak column velocity</div><div class="v" id="rVm">&ndash;</div></div>
    <div class="cell"><div class="k">Water hammer at that velocity</div><div class="v" id="rJk">&ndash;</div></div>
    <div class="cell"><div class="k">Against 136 m</div><div class="v" style="font-size:14px;margin-top:6px;" id="rV2">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">Shrink the pocket and the rigid-column peak keeps rising: 398.5&nbsp;m for 20&nbsp;m of air and 521.1&nbsp;m for 2&nbsp;m. Those small-pocket numbers are not real. A small pocket stops the column within a few metres, at a low velocity, and the elasticity of the water and the pipe then limits the peak to about the water hammer value at that velocity (97&nbsp;m for the 2&nbsp;m pocket). The two curves cross near 30&nbsp;m of air on this leg, and that is where the worst real peaks occur: the pocket is small enough to stop the column hard and large enough to let it reach speed first. Use the lower curve as a screening value, and an elastic model with a gas pocket (section 6) for design.</p>

<h2 id="drain">4 &middot; Draining: let the air in</h2>
<p>Draining reverses the problem. Water leaving through a washout must be replaced by air entering through the air valves at the high points, or the pressure there falls towards vacuum and the column separates. The same orifice equation, with atmospheric air flowing into a pipe below atmospheric pressure, sizes the inflow. Draining the reference main through a washout at 0.10&nbsp;m&sup3;/s needs 0.10&nbsp;m&sup3;/s of free air at the high points: a DN50 orifice admits 0.19&nbsp;m&sup3;/s at 0.2&nbsp;bar of vacuum, a DN100 admits 0.76. The same inflow capacity protects the line when a pump trip separates the column, which is the case air valves are usually sized for [1][10].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Air inflow capacity against vacuum</div>
    <div class="fsub">Free air (m&sup3;/s at atmospheric pressure, 20&nbsp;&deg;C) entering through a sharp orifice, isentropic, \(C_d\) = 0.6, choked below an absolute pressure ratio of 0.528 (vacuum above 0.47&nbsp;bar). The horizontal line is the air demand and the vertical line the vacuum you will accept.</div>
  </div>
  <div class="chart-box"><canvas id="airChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Air demand <span id="vQa">0.10 m³/s</span></label>
      <input type="range" id="sQa" min="0.01" max="1.5" value="0.1" step="0.01">
      <div class="hint">Drain flow, or the rate a separating column draws air in.</div>
    </div>
    <div class="ctrl">
      <label>Vacuum accepted <span id="vVac">0.20 bar</span></label>
      <input type="range" id="sVac" min="0.02" max="0.6" value="0.2" step="0.01">
      <div class="hint">EN 805 components withstand 0.8&nbsp;bar.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Smallest orifice that admits it</div><div class="v" id="rOr">&ndash;</div></div>
    <div class="cell"><div class="k">Its capacity at that vacuum</div><div class="v" id="rCap">&ndash;</div></div>
    <div class="cell"><div class="k">DN100 capacity</div><div class="v" id="rC100">&ndash;</div></div>
    <div class="cell"><div class="k">Vacuum a DN100 needs</div><div class="v" id="rVac100">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">Capacity rises steeply at first and then flattens: once the vacuum passes 0.47&nbsp;bar the flow is choked and more vacuum admits no more air. Manufacturers publish tested curves for their valves, which include the body and float losses; use those for the final selection, and this chart to see whether the demand is in the right range [1][7].</p>

<h2 id="restart">5 &middot; Restarting after a trip or a drain-down</h2>
<p>After a power failure the column may have separated at high points, and after a long stop the line may have drained partly through leaks, washouts or air valves. Restarting a pump at full speed into such a line repeats sections 2 and 3 at pump velocity: the column runs into the voids at 1&ndash;2&nbsp;m/s, and the air valves at the high points close on it. Our restart procedure:</p>
<ul class="clean">
  <li><strong>Wait for the line to settle</strong> after a trip: the vessel refilled, cavities collapsed, air valves closed. On the reference main the column swings for several minutes (see <a href="surge-model-time-step-convergence.html">run duration</a>).</li>
  <li><strong>Refill slowly first</strong> where the line may have drained: a bypass round the pump, the pump at minimum speed on its drive, or the pump control valve held at a small opening, with the filling velocity kept near 0.3&nbsp;m/s until the high points have vented.</li>
  <li><strong>Interlock the restart</strong>: no full-speed start until pressure at the high points is positive, and a minimum time after any trip.</li>
  <li><strong>Check the air valves</strong> after every drain-down, since a stuck float turns a vented high point into a trapped pocket.</li>
</ul>

<h2 id="hammer">6 &middot; What HAMMER can and cannot show</h2>
<p>HAMMER, like other full-pipe method-of-characteristics programs, assumes every pipe is full of liquid along its length. It cannot simulate an empty pipe filling, a stratified flow running down a slope, or air travelling along the pipe [11]. It can model gas at nodes, and that covers most of what a designer needs:</p>
<ol>
  <li><strong>Air valves</strong> at high points, with their inflow and outflow orifice sizes and, for triple-acting or anti-slam valves, the switching settings. Use them to check slam on restart and the vacuum during a trip.</li>
  <li><strong>A trapped pocket at a node</strong>, represented by a small gas volume (for example a vessel element at the high point with no connection loss) at its expected size and pressure. Run the restart with that pocket in place to get an elastic answer for section 3.</li>
  <li><strong>The restart itself</strong>: a pump start with the real ramp or valve opening (see <a href="pump-start-stop-vfd-ramp-surge.html">normal operations</a>) into a line whose initial condition has the pockets in place.</li>
  <li><strong>The filling procedure</strong> is then checked by hand with the rigid-column model of section 3 and the slam limit of section 2, and written into the operating manual with rates, valve sequences and hold points.</li>
</ol>

<h2 id="checklist">7 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Filling velocity set</strong> (about 0.3&nbsp;m/s unless a calculation supports more), and the slam head checked against the pipe's limits.</li>
  <li><strong>Air valves sized for exhaust during filling and inflow during draining</strong>, with the manufacturer's tested curves.</li>
  <li><strong>Anti-slam or two-stage valves</strong> where filling or restart velocities cannot be kept low.</li>
  <li><strong>Every high point vented</strong>, or the trapped pocket checked with the rigid-column model and an elastic model.</li>
  <li><strong>Filling valve or bypass sized as a throttle</strong>, not opened fully against a closed or air-filled section.</li>
  <li><strong>Restart procedure</strong> with a settling time, a slow refill and an interlock on high-point pressure.</li>
  <li><strong>Procedure in the operating manual</strong>, with rates, sequences and hold points.</li>
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
    <li><a href="pump-start-stop-vfd-ramp-surge.html">Pump starts, controlled stops and drive ramps</a></li>
    <li><strong>Filling, draining and restarting a transmission main</strong></li>
    <li><a href="wastewater-force-main-surge.html">Surge in wastewater force mains</a></li>
    <li><a href="surge-study-report-review-checklist.html">The surge study report: what to deliver and what a reviewer checks</a></li>
  </ol>
  The protection devices themselves are covered in the <a href="choosing-surge-protection.html">surge protection design series</a>.
</div>
"""

CHARTS = r"""
const FF="'IBM Plex Sans', system-ui, sans-serif";
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:FF,size:11}}};
const TTL={family:FF,size:12,weight:'600'};
const LBL={size:10,family:FF};
const LEGF={family:FF,size:11.5};
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1), fmt2=v=>v.toFixed(2), fmt3=v=>v.toFixed(3);
const G=9.81, HA=10.33, M2B=10.21, PRJ=136.0, STATIC=44.8;
const good=t=>'<span class="badge good">'+t+'</span>', bad=t=>'<span class="badge bad">'+t+'</span>', warn=t=>'<span class="badge warn">'+t+'</span>';
/* isentropic orifice: free-air m3/s through an orifice of d mm at a pressure difference dp (bar) */
function airQ(dmm,dp,inflow){
  const A=Math.PI*Math.pow(dmm/1000,2)/4, gam=1.4, R=287, T0=293.15, pa=101325, Cd=0.6;
  const p0=inflow?pa:pa+dp*1e5, p=inflow?pa-dp*1e5:pa;
  const r=Math.max(p/p0,0.5283);
  const m=Cd*A*p0*Math.sqrt(2*gam/((gam-1)*R*T0)*(Math.pow(r,2/gam)-Math.pow(r,(gam+1)/gam)));
  return m/(pa/(R*T0));
}
function dpFor(dmm,Q,inflow,cap){ // smallest dp (bar) passing Q, or null if more than cap
  if(airQ(dmm,cap,inflow)<Q) return null;
  let lo=0,hi=cap; for(let k=0;k<60;k++){const m=(lo+hi)/2; if(airQ(dmm,m,inflow)>=Q) hi=m; else lo=m;} return hi;
}
/* ---------- CHART 1 : slam and air exhaust ---------- */
const sDN=document.getElementById('sDN'), sV=document.getElementById('sV'), sA=document.getElementById('sA'), sLs=document.getElementById('sLs'), sOr=document.getElementById('sOr');
const VS=[];for(let k=0;k<=40;k++)VS.push(k*0.05);
const slamChart=new Chart(document.getElementById('slamChart'),{
  data:{datasets:[
    {type:'line',label:'Slam head, chosen wave speed (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,order:2},
    {type:'line',label:'Ductile iron, 1,050 m/s',data:VS.map(v=>({x:v,y:1050*v/G})),borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.2,borderDash:[5,4],pointRadius:0,order:3},
    {type:'line',label:'PE, 300 m/s',data:VS.map(v=>({x:v,y:300*v/G})),borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:1.2,borderDash:[5,4],pointRadius:0,order:4},
    {type:'scatter',label:'Your fill',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:2,title:{display:true,text:'Water velocity arriving at the air valve (m/s)',font:TTL},...AX},
            y:{type:'linear',min:0,max:280,title:{display:true,text:'Head rise when the float closes (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt2(c.parsed.x)} m/s`}},
      annotation:{annotations:{lim:{type:'line',yMin:PRJ-STATIC,yMax:PRJ-STATIC,borderColor:'#c0392b',borderWidth:1.4,borderDash:[6,4],
        label:{display:true,content:'136 m limit less 44.8 m static',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(192,57,43,0.85)'}}}}}}
});
function updSlam(){
  const D=+sDN.value, v=+sV.value, a=+sA.value, Ls=+sLs.value*1000, d=+sOr.value;
  document.getElementById('vV').textContent=fmt2(v)+' m/s';
  document.getElementById('vA').textContent=fmt0(a)+' m/s';
  document.getElementById('vLs').textContent=fmt1(Ls/1000)+' km';
  const A=Math.PI*D*D/4, Q=A*v, T=A*Ls/Q/3600, dH=a*v/G;
  slamChart.data.datasets[0].data=VS.map(x=>({x:x,y:a*x/G}));
  slamChart.data.datasets[3].data=[{x:v,y:dH}];
  slamChart.update('none');
  const dp=dpFor(d,Q,false,1.0), vo=Q/(Math.PI*Math.pow(d/1000,2)/4);
  document.getElementById('rQ').innerHTML=fmt3(Q)+' <small>m³/s</small>';
  document.getElementById('rT').innerHTML=fmt1(T)+' <small>h</small>';
  document.getElementById('rS').innerHTML=fmt1(dH)+' <small>m</small>';
  document.getElementById('rDp').innerHTML=dp===null?'<small>more than 1 bar</small>':fmt3(dp)+' <small>bar</small>';
  document.getElementById('rVo').innerHTML=fmt0(vo)+' <small>m/s</small>';
  const peak=STATIC+dH;
  document.getElementById('rVer').innerHTML=(peak>PRJ?bad('slam exceeds 136 m'):good('slam within 136 m'))+' '+((dp===null||dp>0.1)?warn('orifice small'):'');
}
[sDN,sV,sA,sLs,sOr].forEach(s=>s.addEventListener('input',updSlam));updSlam();

/* ---------- CHART 2 : trapped pocket, rigid column ---------- */
const sH=document.getElementById('sH'), sL=document.getElementById('sL'), sP=document.getElementById('sP'), sK=document.getElementById('sK'), sD2=document.getElementById('sD2'), sN=document.getElementById('sN');
const PL=[1,2,3,5,7,10,15,20,25,30,40,50,60,80,100,125,150,200,250,350,500];
function pocket(Hg,L,D,Lp,n,vt,firstPeakOnly,Tend){
  const f=0.015, A=Math.PI*D*D/4, V0=A*Lp, HR=Hg+HA, dt=0.005;
  const K=vt>0?Math.max(1,2*G*Hg/(vt*vt)-f*L/D-1):1;
  let v=0,V=V0,t=0,pk=HA,tpk=0,vmax=0; const ts=[],ps=[],vs=[];
  const der=(v,V)=>{const Lc=L+(V0-V)/A, Hp=HA*Math.pow(V0/V,n); return [(G/Lc)*(HR-Hp-K*v*Math.abs(v)/(2*G))-f*v*Math.abs(v)/(2*D), -A*v];};
  let k=0, falling=0;
  while(t<Tend-1e-12){
    const k1=der(v,V),k2=der(v+0.5*dt*k1[0],V+0.5*dt*k1[1]),k3=der(v+0.5*dt*k2[0],V+0.5*dt*k2[1]),k4=der(v+dt*k3[0],V+dt*k3[1]);
    v+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6; V+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6; t+=dt; k++;
    const Hp=HA*Math.pow(V0/V,n); if(v>vmax)vmax=v;
    if(Hp>pk){pk=Hp;tpk=t;falling=0;} else if(firstPeakOnly && Hp<pk-0.5) {falling++; if(falling>40) break;}
    if(!firstPeakOnly && k%40===0){ts.push(+t.toFixed(2));ps.push(+(Hp-HA).toFixed(2));vs.push(+v.toFixed(3));}
  }
  return {peak:pk-HA,t:tpk,vmax:vmax,K:K,ts,ps,vs};
}
const pockChart=new Chart(document.getElementById('pockChart'),{
  data:{datasets:[
    {type:'line',label:'Pocket pressure (m, gauge)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.2,pointRadius:0,yAxisID:'y',order:1},
    {type:'line',label:'Column velocity (m/s, right)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:1.8,pointRadius:0,yAxisID:'y1',order:2}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:200,title:{display:true,text:'Time after the filling valve opens (s)',font:TTL},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Pocket pressure (m, gauge)',font:TTL},...AX},
            y1:{type:'linear',position:'right',title:{display:true,text:'Column velocity (m/s)',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`velocity ${fmt2(c.parsed.y)} m/s`:`pocket ${fmt1(c.parsed.y)} m`}},
      annotation:{annotations:{drv:{type:'line',yScaleID:'y',yMin:40,yMax:40,borderColor:'#7f8c8d',borderWidth:1.2,borderDash:[4,4],label:{display:true,content:'driving head',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(127,140,141,0.9)'}}}}}}
});
const peakChart=new Chart(document.getElementById('peakChart'),{
  data:{datasets:[
    {type:'line',label:'Rigid-column peak (m)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.2,pointRadius:2,order:2},
    {type:'line',label:'Water hammer a·vmax/g (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:1.8,borderDash:[5,4],pointRadius:2,order:3},
    {type:'scatter',label:'Your pocket',data:[],backgroundColor:'#111',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'logarithmic',min:1,max:500,title:{display:true,text:'Trapped air, as metres of pipe (log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[1,2,5,10,20,50,100,200,500].includes(+v.toPrecision(3))?String(+v.toPrecision(3)):''}},
            y:{type:'linear',min:0,title:{display:true,text:'First peak (m, gauge)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt0(c.parsed.x)} m of air`}},
      annotation:{annotations:{lim:{type:'line',yMin:PRJ,yMax:PRJ,borderColor:'#6b4f9e',borderWidth:1.2,borderDash:[4,4],label:{display:true,content:'136 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}}}}}
});
function updPock(){
  const Hg=+sH.value, L=+sL.value, Lp=PL[+sP.value], vt=+sK.value, D=+sD2.value, n=+sN.value;
  document.getElementById('vH').textContent=Hg+' m';
  document.getElementById('vL').textContent=fmt0(L)+' m';
  document.getElementById('vP').textContent=Lp+' m';
  const r=pocket(Hg,L,D,Lp,n,vt,false,200);
  pockChart.data.datasets[0].data=r.ts.map((t,k)=>({x:t,y:r.ps[k]}));
  pockChart.data.datasets[1].data=r.ts.map((t,k)=>({x:t,y:r.vs[k]}));
  const an=pockChart.options.plugins.annotation.annotations.drv; an.yMin=Hg; an.yMax=Hg;
  pockChart.update('none');
  const sw=PL.map(lp=>{const q=pocket(Hg,L,D,lp,n,vt,true,200);return {lp:lp,pk:q.peak,j:1050*q.vmax/G};});
  peakChart.data.datasets[0].data=sw.map(s=>({x:s.lp,y:s.pk}));
  peakChart.data.datasets[1].data=sw.map(s=>({x:s.lp,y:s.j}));
  peakChart.data.datasets[2].data=[{x:Lp,y:r.peak}];
  peakChart.update('none');
  document.getElementById('rPk').innerHTML=fmt1(r.peak)+' <small>m</small>';
  document.getElementById('rRat').innerHTML=fmt2(r.peak/Hg)+' <small>×</small>';
  document.getElementById('rTp').innerHTML=fmt1(r.t)+' <small>s</small>';
  document.getElementById('rVm').innerHTML=fmt2(r.vmax)+' <small>m/s</small>';
  document.getElementById('rJk').innerHTML=fmt1(1050*r.vmax/G)+' <small>m</small>';
  document.getElementById('rV2').innerHTML=Math.min(r.peak,1050*r.vmax/G)>PRJ?bad('screening value above 136 m'):good('screening value within 136 m');
}
[sH,sL,sP,sK,sD2,sN].forEach(s=>s.addEventListener('input',updPock));updPock();

/* ---------- CHART 3 : air inflow ---------- */
const sQa=document.getElementById('sQa'), sVac=document.getElementById('sVac');
const ORF=[[50,'#c0392b'],[80,'#b9770e'],[100,'#1b4f72'],[150,'#1e8449'],[200,'#6b4f9e']];
const DPS=[];for(let k=0;k<=60;k++)DPS.push(k*0.01);
const airChart=new Chart(document.getElementById('airChart'),{
  data:{datasets:ORF.map(([d,c])=>({type:'line',label:'DN'+d,data:DPS.map(p=>({x:p,y:airQ(d,p,true)})),borderColor:c,backgroundColor:c,borderWidth:2,pointRadius:0}))},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0,max:0.6,title:{display:true,text:'Vacuum in the pipe (bar below atmospheric)',font:TTL},...AX},
            y:{type:'logarithmic',min:0.01,max:5,title:{display:true,text:'Free air admitted (m³/s, log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[0.01,0.03,0.1,0.3,1,3].includes(+v.toPrecision(2))?String(+v.toPrecision(2)):''}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt3(c.parsed.y)} m³/s at ${fmt2(c.parsed.x)} bar`}},
      annotation:{annotations:{
        dem:{type:'line',yMin:0.1,yMax:0.1,borderColor:'#111',borderWidth:1.4,borderDash:[6,4],label:{display:true,content:'air demand',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(17,17,17,0.8)'}},
        vac:{type:'line',xMin:0.2,xMax:0.2,borderColor:'#7f8c8d',borderWidth:1.2,borderDash:[3,3]},
        chk:{type:'line',xMin:0.4717,xMax:0.4717,borderColor:'#c0392b',borderWidth:1,borderDash:[2,3],label:{display:true,content:'choked',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(192,57,43,0.85)'}}
      }}}}
});
function updAir(){
  const Q=+sQa.value, vac=+sVac.value;
  document.getElementById('vQa').textContent=fmt2(Q)+' m³/s';
  document.getElementById('vVac').textContent=fmt2(vac)+' bar';
  const A=airChart.options.plugins.annotation.annotations; A.dem.yMin=Q; A.dem.yMax=Q; A.vac.xMin=vac; A.vac.xMax=vac; airChart.update('none');
  const ok=ORF.map(o=>o[0]).find(d=>airQ(d,vac,true)>=Q);
  document.getElementById('rOr').innerHTML=ok?'DN'+ok:'<small>more than DN200</small>';
  document.getElementById('rCap').innerHTML=ok?fmt3(airQ(ok,vac,true))+' <small>m³/s</small>':'<small>&ndash;</small>';
  document.getElementById('rC100').innerHTML=fmt3(airQ(100,vac,true))+' <small>m³/s</small>';
  const need=dpFor(100,Q,true,0.6);
  document.getElementById('rVac100').innerHTML=need===null?'<small>beyond choking</small>':fmt3(need)+' <small>bar</small>';
}
[sQa,sVac].forEach(s=>s.addEventListener('input',updAir));updAir();
window.addEventListener('load',function(){try{[slamChart,pockChart,peakChart,airChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>AWWA Manual M51 <em>Air Valves: Air-Release, Air/Vacuum, and Combination</em>: air valve types, sizing for filling, draining and column separation, and filling rates.</li>
  <li>Martin, C.S. &ldquo;Entrapped air in pipelines.&rdquo; <em>Proc. 2nd International Conference on Pressure Surges</em>, BHRA, 1976: rigid-column analysis of air pockets compressed by an accelerating column.</li>
  <li>Lingireddy, S., Wood, D.J. &amp; Zloczower, N. &ldquo;Pressure surges in pipeline systems resulting from air releases.&rdquo; <em>Journal AWWA</em>, 96(7), 2004: surges caused by air release and air valve closure.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the 12&nbsp;km DN800 reference main.</li>
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: the Joukowsky relation, rigid-column theory and gas pockets.</li>
  <li>Shapiro, A.H. <em>The Dynamics and Thermodynamics of Compressible Fluid Flow</em>, Vol. 1. Ronald Press, 1953: isentropic flow through an orifice and choking.</li>
  <li>EN 1074-4 <em>Valves for water supply: air valves</em>: performance requirements and testing of air valves.</li>
  <li>Zhou, F., Hicks, F.E. &amp; Steffler, P.M. &ldquo;Transient flow in a rapidly filling horizontal pipe containing trapped air.&rdquo; <em>Journal of Hydraulic Engineering</em>, 128(6), 2002: experiments and models of pocket pressure, and the pocket sizes that give the worst peaks.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: rigid-column analysis and filling transients.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: air valves as transient protection.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: air valve elements and gas volumes at nodes in a full-pipe transient model.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #PipelineFilling #PipelineDraining #AirValves #AirValveSlam #TrappedAir #AirPocket #RigidColumn #FillingRate #Commissioning #PumpRestart #AntiSlamAirValve #AWWAM51 #BentleyHAMMER #TransmissionMain #DuctileIron #PipelineDesign #WaterEngineering</div>
"""

import math, os, sys
sys.path.insert(0, os.path.expanduser('~/site-work/tools/analyst'))
def _pocket(vt):
    g = 9.81; Ha = 10.33; Hg, L, D, Lp, f, n = 40.0, 1000.0, 0.8, 50.0, 0.015, 1.2
    A = math.pi*D*D/4; V0 = A*Lp; HR = Hg + Ha; dt = 0.002
    K = 1.0 if not vt else max(1.0, 2*g*Hg/vt**2 - f*L/D - 1.0)
    v = 0.0; V = V0; t = 0.0; pk = Ha; tpk = 0.0; vmax = 0.0
    def der(v, V):
        Lc = L + (V0 - V)/A; Hp = Ha*(V0/V)**n
        return (g/Lc)*(HR - Hp - K*v*abs(v)/(2*g)) - f*v*abs(v)/(2*D), -A*v
    while t < 200 - 1e-12:
        k1 = der(v, V); k2 = der(v + 0.5*dt*k1[0], V + 0.5*dt*k1[1]); k3 = der(v + 0.5*dt*k2[0], V + 0.5*dt*k2[1]); k4 = der(v + dt*k3[0], V + dt*k3[1])
        v += dt*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6; V += dt*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6; t += dt
        Hp = Ha*(V0/V)**n; vmax = max(vmax, v)
        if Hp > pk: pk = Hp; tpk = t
    return K, vmax, pk - Ha, tpk
THROTTLE = '\n'.join('    <tr><td>%s</td><td class="num">%s</td><td class="num">%.2f</td><td class="num">%.1f</td><td class="num">%.1f</td></tr>' % (
    lab, '{:,.0f}'.format(K), vm, pk, tp) for lab, (K, vm, pk, tp) in
    (('Fully open', _pocket(None)), ('Throttled for 2.0&nbsp;m/s', _pocket(2.0)), ('Throttled for 1.0&nbsp;m/s', _pocket(1.0)),
     ('Throttled for 0.5&nbsp;m/s', _pocket(0.5)), ('Throttled for 0.3&nbsp;m/s', _pocket(0.3))))
BODY = BODY.replace('__THROTTLE__', THROTTLE)

SPEC = dict(
    slug='pipeline-filling-draining-restart-surge', cat='surge', mins=18,
    date_iso='2026-11-27', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Filling, Draining and Restarting a Transmission Main: Air Valve Slam, Trapped Air and Safe Rates',
    reg_title='Filling, Draining and Restarting a Transmission Main: Air Valve Slam, Trapped Air and Safe Rates',
    reg_tag='Surge Analysis · Filling · Air Valves',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Filling &middot; Air Valves',
    desc='The surge risks of filling, draining and restarting a pipeline: air valve slam against filling velocity, trapped air compressed by an accelerating column, air valve capacity for exhaust and inflow, restart after a trip, and what a full-pipe program such as HAMMER can show, with three interactive charts.',
    og_desc='Filling the 12 km reference main at 2 m/s makes a closing air valve slam at 214 m; at 0.3 m/s it is 32 m. Opening a filling valve fully from 40 m into a 1 km leg with 50 m of trapped air drives the pocket to 279 m; throttled to 0.3 m/s it peaks at 40.5 m.',
    ld_desc='Filling, draining and restarting a transmission main: air valve slam, rigid-column trapped air analysis, air valve exhaust and inflow capacity, restart procedure and HAMMER modelling, with interactive charts.',
    img_alt='A transmission main being filled: water advancing along a pipeline towards an air valve at a high point, with air escaping from the valve and a trapped air pocket at a closed section shown in cutaway',
    en_tag='Surge &amp; Transient Analysis &middot; Filling',
    en_title='Filling, Draining and Restarting a Transmission Main: Air Valve Slam, Trapped Air and Safe Rates',
    en_excerpt='Filling the 12 km reference main at 2 m/s makes a closing air valve slam at <strong>214 m</strong>; at 0.3 m/s it is <strong>32 m</strong>. Opening a filling valve fully from 40 m into a 1 km leg holding 50 m of trapped air drives the pocket to <strong>279 m</strong>, seven times the driving head; throttled to 0.3 m/s it peaks at 40.5 m. Slam, trapped air, air valve capacity, restart after a trip and what HAMMER can and cannot model, with three interactive charts.',
    en_search='pipeline filling draining restart surge air valve slam filling velocity 0.3 m/s trapped air pocket rigid column entrapped air compression air valve sizing exhaust inflow orifice isentropic choked flow vacuum draining washout anti-slam two stage air valve restart after pump trip commissioning AWWA M51 EN 1074-4 HAMMER air valve transmission main ductile iron water hammer',
    ar_title='ملء خطوط النقل وتفريغها وإعادة تشغيلها: صدمة صمامات الهواء والهواء المحبوس والمعدلات الآمنة',
    ar_excerpt='ملء الخط المرجعي (١٢ كم) بسرعة ٢ م/ث يجعل إغلاق صمام الهواء يرفع الضغط بمقدار <strong>٢١٤ م</strong>، بينما لا يتجاوز <strong>٣٢ م</strong> عند ٠٫٣ م/ث. وفتح صمام الملء بالكامل من ارتفاع ٤٠ م على جزء طوله ١ كم يحبس ٥٠ م من الهواء يضغط الجيب الهوائي إلى <strong>٢٧٩ م</strong>، أي سبعة أضعاف الضغط الدافع، بينما لا يتجاوز ٤٠٫٥ م عند خنق الملء إلى ٠٫٣ م/ث. مع ثلاثة رسوم تفاعلية.',
    ar_search='ملء الأنابيب تفريغ الأنابيب إعادة التشغيل صدمة صمام الهواء سرعة الملء الهواء المحبوس الجيب الهوائي نموذج العمود الصلب تصميم صمامات الهواء التفريغ المطرقة المائية الطرق المائي خطوط النقل بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
