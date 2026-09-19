# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">When the power fails, a pump does not stop at once. It coasts down on the energy in its rotating parts, and while it coasts it keeps the column moving. Make that rundown long enough and the downsurge never reaches vapour. On our 12&nbsp;km reference main the motor and pump alone, at about 25&nbsp;kg&middot;m&sup2;, protect nothing. Sixteen times that, <strong>400&nbsp;kg&middot;m&sup2; in total</strong>, keeps every point on the line at or above <strong>+9.3&nbsp;m</strong> (+7.3&nbsp;m under the least favourable torque law tried), with no upsurge above the steady 85&nbsp;m. The price comes at every start: with half of rated torque available for acceleration, the set takes <strong>28.1&nbsp;s</strong> to reach speed instead of 1.8.</p>

<h2 id="rotating-energy">1 &middot; Rotating energy as surge protection</h2>
<p>The load case that usually sizes the protection is a power failure that trips every pump at once (see <a href="surge-scenarios-pump-stations.html">Surge Scenarios in Pumping Stations</a>). The reference main for this series is a 12&nbsp;km, DN800 ductile iron K9 line [1] on a flat profile. It carries 2,520&nbsp;m&sup3;/h (1.39&nbsp;m/s) from an HGL of 85.0&nbsp;m at the pump to 44.8&nbsp;m at the reservoir, with a wave speed of 1,050&nbsp;m/s. The pipe is PN16 (136&nbsp;m allowable) [2], and the design minimum for this series is +3.0&nbsp;m. Unprotected, with the pump modelled as stopping at once, the downsurge reaches vapour (&minus;9.8&nbsp;m) along the line, and the peak when the cavities collapse is <strong>165&ndash;190&nbsp;m</strong>. That is above PN16 whichever cavity model you believe.</p>
<p>A <a href="surge-vessel.html">hydropneumatic vessel</a>, a <a href="one-way-surge-tank-design.html">one-way surge tank</a> or <a href="air-admission-networks.html">air valves</a> put water or air back into the line. A flywheel goes after the cause instead: the column is being stopped too quickly. Until the first reflection returns from the reservoir, each cubic metre per second the pump stops delivering drops the head at the pump by</p>
<div class="eq">\[ \Delta H \;=\; \frac{a}{gA}\,\Delta Q \;=\; \frac{1050}{9.81 \times 0.5027}\,\Delta Q \;=\; 212.9\ \text{m per m}^3\text{/s} \]</div>
<p>So losing all 0.70&nbsp;m&sup3;/s within 2L/a&nbsp;=&nbsp;22.9&nbsp;s would call for a 149.1&nbsp;m drop, from a head of 85&nbsp;m that can fall only 94.8&nbsp;m before it reaches vapour [3]. A pump with enough rotating mass is still delivering when the reflections come back, and the head never reaches vapour. Nothing is added to the line, there is no gas to maintain and nothing to switch on: the protection acts on every trip [4].</p>
<div class="callout key">
  <span class="lbl">What a flywheel does, and what it does not</span>
  It slows the <strong>rate at which the flow falls</strong>, which tackles the downsurge at its source. It does nothing for an upsurge caused elsewhere, it cannot help a high point that separates for its own reasons, and it makes every normal start slower and harder on the motor. In our practice, that last point decides more flywheel designs than the hydraulics does.
</div>

<h2 id="rundown-equation">2 &middot; The rundown equation: stored energy, &tau; and GD&sup2;</h2>
<p>Once the motor loses its supply, the only thing driving the pump is the kinetic energy of everything on the shaft: impeller, rotor, coupling and flywheel [3][5]:</p>
<div class="eq">\[ I\,\frac{d\omega}{dt} \;=\; -\,T, \qquad T \;=\; \frac{\rho g\,Q\,H_p}{\eta\,\omega} \;+\; T_{loss} \]</div>
<p>Here \(I\) is the total inertia on the shaft (kg&middot;m&sup2;), \(\omega\) the speed, \(Q\) and \(H_p\) the flow and head the pump is still producing, \(\eta\) its efficiency and \(T_{loss}\) the windage and friction torque. Pump head falls with the square of speed. On the model pump the zero-flow head is \(100\,w^2\) metres above a 5&nbsp;m suction, where \(w\) is the speed ratio. So once the speed has dropped by about 11&nbsp;% (\(5 + 100\,w^2 = 85\) at \(w\) = 0.89), the pump cannot hold 85&nbsp;m even at zero flow. <strong>A flywheel does not keep the pressure up. It keeps the flow going while the pressure falls.</strong></p>
<div class="eq">\[ E_k \;=\; \tfrac12\,I\,\omega_0^2, \qquad \tau \;=\; \frac{E_k}{P_0}, \qquad GD^2 \;=\; 4I \]</div>
<p>\(E_k\) is the energy stored at running speed \(\omega_0\), and \(\tau\) is how long that energy could supply the rated power \(P_0\). At a constant rated torque \(T_0 = P_0/\omega_0\), the set would stop in \(I\omega_0/T_0 = 2\tau\). In reality the torque falls with speed and the rundown tails off more slowly, but \(\tau\) still puts sets of any speed and power on one scale [6]. Parmakian's classical charts for power failure at a pump rest on the same idea, a parameter that sets the rotor's stored energy against the pipeline's wave travel time [7].</p>
<p>Many data sheets give GD&sup2;, which in kg&middot;m&sup2; is numerically \(4I\). US data sheets give WR&sup2; in lb&middot;ft&sup2;, which is \(I\) itself; multiply by 0.0421 to get kg&middot;m&sup2;. A mix-up here is a factor of four in the input that matters most.</p>

<h2 id="six-inertias">3 &middot; The model, and six inertias on the reference main</h2>
<p>The numbers come from a method-of-characteristics model with a vapour cavity model, cross-checked with a gas cavity model and an independent second code [3][8]. The pump is a screening model. None of this is Bentley HAMMER output: a project has to be run in HAMMER, or an equivalent program, on the real profile with the real pump data.</p>
<ul class="clean">
  <li><strong>Duty.</strong> 0.70&nbsp;m&sup3;/s at 80&nbsp;m pump head on a 5&nbsp;m suction, 1,480&nbsp;rpm (\(\omega_0\) = 155.0&nbsp;rad/s), efficiency 0.80. That gives 685&nbsp;kW of shaft power and a rated torque of 4,420&nbsp;N&middot;m.</li>
  <li><strong>Pump.</strong> A simplified homologous rundown [9], \(H = 100\,w^2 - 40.8\,Q^2\), with the hydraulic torque above plus windage (2&nbsp;% of rated at full speed) and an ideal non-return valve. After the valve closes we <em>assume</em> a churning torque of 45&nbsp;% of rated at full speed, scaled with \(w^2\). Speed is integrated with the trapezoidal rule.</li>
  <li><strong>Line and set.</strong> 120 reaches, 150&nbsp;s runs. The bare-set inertia of 25&nbsp;kg&middot;m&sup2; is an <em>assumption</em> for a 685&nbsp;kW four-pole set; take project values from the data sheets.</li>
</ul>
<p>HAMMER describes the pump by four-quadrant characteristics [5][10], which set the torque during the rundown. The simple torque law used here is the main uncertainty, and section 5 puts a number on it. There is also a quirk: once its head rise has fallen to zero, the slowing model pump still passes water from its 5&nbsp;m suction but takes no hydraulic torque. The bare set's speed therefore hangs at about 0.2 instead of dropping away, but only until the first reflection returns and the non-return valve closes; after that the <em>assumed</em> churning torque takes it slowly down towards zero (0.04 at 60&nbsp;s, 0.01 at 150&nbsp;s). As \(I\) falls towards zero the model does not become exactly an instantaneous stop either. Read that part of the speed trace as a feature of the torque law, not a prediction.</p>

<div class="tbl-wrap"><table>
  <caption>What each inertia stores: 685&nbsp;kW at 1,480&nbsp;rpm, 2L/a = 22.9&nbsp;s, start time with 50&nbsp;% of rated torque available for acceleration (section 8)</caption>
  <thead><tr><th class="num">Total I <span style="text-transform:none">(kg&middot;m&sup2;)</span></th><th class="num">GD&sup2; <span style="text-transform:none">(kg&middot;m&sup2;)</span></th><th class="num"><span style="text-transform:none">E<sub>k</sub></span> (MJ)</th><th class="num"><span style="text-transform:none">&tau; (s)</span></th><th class="num"><span style="text-transform:none">&tau; / (2L/a)</span></th><th class="num">Start time <span style="text-transform:none">(s)</span></th></tr></thead>
  <tbody>
    <tr><td class="num">25 (bare set)</td><td class="num">100</td><td class="num">0.30</td><td class="num">0.44</td><td class="num">0.02</td><td class="num">1.8</td></tr>
    <tr><td class="num">100</td><td class="num">400</td><td class="num">1.20</td><td class="num">1.75</td><td class="num">0.08</td><td class="num">7.0</td></tr>
    <tr><td class="num">200</td><td class="num">800</td><td class="num">2.40</td><td class="num">3.51</td><td class="num">0.15</td><td class="num">14.0</td></tr>
    <tr><td class="num"><strong>400</strong></td><td class="num">1,600</td><td class="num">4.80</td><td class="num">7.01</td><td class="num">0.31</td><td class="num">28.1</td></tr>
    <tr><td class="num">800</td><td class="num">3,200</td><td class="num">9.61</td><td class="num">14.03</td><td class="num">0.61</td><td class="num">56.1</td></tr>
    <tr><td class="num">1,600</td><td class="num">6,400</td><td class="num">19.22</td><td class="num">28.05</td><td class="num">1.23</td><td class="num">112.2</td></tr>
  </tbody>
</table></div>

<div class="tbl-wrap"><table>
  <caption>What each inertia does to the line: all pumps trip, no other protection, pressure heads above the pipe</caption>
  <thead><tr><th class="num">Total I <span style="text-transform:none">(kg&middot;m&sup2;)</span></th><th class="num">Lowest head on the line <span style="text-transform:none">(m)</span></th><th>Where</th><th class="num">Lowest head at the pump <span style="text-transform:none">(m)</span></th><th class="num">Highest head on the line <span style="text-transform:none">(m)</span></th><th class="num">Speed ratio at <span style="text-transform:none">5 / 10 / 22.9&nbsp;s</span></th></tr></thead>
  <tbody>
    <tr><td class="num">25</td><td class="num">&minus;9.8 (vapour)</td><td>7.3&ndash;11.3&nbsp;km</td><td class="num">+2.5</td><td class="num">not quoted (cavitating)</td><td class="num">0.22 / 0.22 / 0.20</td></tr>
    <tr><td class="num">100</td><td class="num">&minus;8.7</td><td>7.8&nbsp;km</td><td class="num">&minus;1.3</td><td class="num">88.2 (indicative)</td><td class="num">0.40 / 0.27 / 0.25</td></tr>
    <tr><td class="num">200</td><td class="num">&minus;1.5</td><td>5.6&nbsp;km</td><td class="num">+5.1</td><td class="num">85.0</td><td class="num">0.58 / 0.40 / 0.28</td></tr>
    <tr><td class="num"><strong>400</strong></td><td class="num"><strong>+9.3</strong></td><td>3.0&nbsp;km</td><td class="num">+10.8</td><td class="num">85.0</td><td class="num">0.73 / 0.57 / 0.37</td></tr>
    <tr><td class="num">800</td><td class="num">+17.8</td><td>at the pump</td><td class="num">+17.8</td><td class="num">85.0</td><td class="num">0.85 / 0.73 / 0.54</td></tr>
    <tr><td class="num">1,600</td><td class="num">+26.0</td><td>at the pump</td><td class="num">+26.0</td><td class="num">85.0</td><td class="num">0.92 / 0.85 / 0.70</td></tr>
  </tbody>
</table></div>

<div class="callout warn">
  <span class="lbl">Why one maximum is not quoted</span>
  With 25&nbsp;kg&middot;m&sup2; cavities form and collapse between 7.3 and 11.3&nbsp;km. The vapour cavity run shows nothing above the steady 85&nbsp;m, but collapse peaks depend on how the cavity is represented [8] (across this series the gas cavity model puts them between 18&nbsp;% lower and 10&nbsp;% higher than the vapour cavity model), and this case was not rerun with the gas cavity model, so no maximum is quoted. The 165&ndash;190&nbsp;m of section 1 does not apply either: it belongs to the pump stopping at once. The design answer is to keep the line out of vapour rather than argue about the peak. Every case from 200&nbsp;kg&middot;m&sup2; up stays clear of vapour under every torque law tried, so those results are quoted to 0.1&nbsp;m.
</div>
<p>At 100&nbsp;kg&middot;m&sup2; the line stays only 1.1&nbsp;m clear of vapour, with a small upsurge to 88.2&nbsp;m at the pump. Under the least favourable torque law tried (section 5) it reaches vapour, so treat both figures as indicative. With a short rundown the lowest point is well down the line; with a long one it moves back to the pump.</p>

<h2 id="int-rundown">4 &middot; Interactive: the rundown</h2>
<p>Pick an inertia and watch the pump slow down and the head at the pump respond. The grey traces are the bare motor and pump.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pump speed and pump-end pressure head after a power failure</div>
    <div class="fsub">Method-of-characteristics model with a vapour cavity model, 12&nbsp;km DN800, a = 1,050&nbsp;m/s, 685&nbsp;kW at 1,480&nbsp;rpm, simplified homologous rundown with an ideal non-return valve. Traces are thinned to 260 points for the page; the readouts come from the full run.</div>
  </div>
  <div class="chart-box"><canvas id="runChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Total inertia on the shaft</label>
      <select id="sCase1">
        <option value="0">25 kg&middot;m&sup2; (motor and pump only)</option>
        <option value="1">100 kg&middot;m&sup2;</option>
        <option value="2">200 kg&middot;m&sup2;</option>
        <option value="3" selected>400 kg&middot;m&sup2; (design)</option>
        <option value="4">800 kg&middot;m&sup2;</option>
        <option value="5">1,600 kg&middot;m&sup2;</option>
      </select>
      <div class="hint">Motor rotor, impeller, coupling and flywheel together.</div>
    </div>
    <div class="ctrl">
      <label>Time window <span id="vWin">90 s</span></label>
      <input type="range" id="sWin" min="10" max="150" value="90" step="5">
      <div class="hint">The vertical line is 2L/a = 22.9&nbsp;s, when the first reflection returns from the reservoir.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Inertia I</div><div class="v" id="rI">400 <small>kg&middot;m&sup2;</small></div></div>
    <div class="cell"><div class="k">GD&sup2;</div><div class="v" id="rGD">1,600 <small>kg&middot;m&sup2;</small></div></div>
    <div class="cell"><div class="k">Stored energy</div><div class="v" id="rEk">4.80 <small>MJ</small></div></div>
    <div class="cell"><div class="k"><span style="text-transform:none">&tau;</span> = E/P</div><div class="v" id="rTau">7.01 <small>s</small></div></div>
    <div class="cell"><div class="k">Lowest head on line</div><div class="v" id="rLmin">+9.3 <small>m, at 3.0 km</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;" id="rVer"><span class="badge good">meets +3.0 m</span></div></div>
    <div class="cell"><div class="k">Highest head on line</div><div class="v" id="rLmax">85.0 <small>m</small></div></div>
  </div>
</div>
<p class="fig-note">At 400&nbsp;kg&middot;m&sup2; the speed ratio is 0.73 at 5&nbsp;s, 0.57 at 10&nbsp;s and 0.37 at 2L/a. The pump-end head bottoms out at +10.8&nbsp;m just as the first reflection returns, the line never drops below +9.3&nbsp;m, and nothing rises above 85&nbsp;m. Switch to 25&nbsp;kg&middot;m&sup2;: the speed is down to 0.22 within 5&nbsp;s (where this model holds it until the first reflection returns; see section 3) and the pump-end head is below 10&nbsp;m within two seconds. The pump end holds at a few metres only because the slowing pump still passes water from its suction; meanwhile the far end of the line goes to vapour. Now try 200&nbsp;kg&middot;m&sup2;. The pump-end trace never falls below +5&nbsp;m, yet the line fails at 5.6&nbsp;km. With 800 and 1,600&nbsp;kg&middot;m&sup2; the pump-end minimum does not arrive until well after the first reflection cycle, which is why the window opens at 90&nbsp;s. <strong>Judge the design on the minimum envelope along the whole line, not on the history at the pump.</strong></p>

<h2 id="worked-example">5 &middot; Worked example: how much inertia the 12&nbsp;km main needs</h2>
<p>This is the sequence we follow on a project, run here on the reference main.</p>
<h3>Step 1: the duty and the set</h3>
<div class="eq">\[ P_0 = \frac{\rho g Q H}{\eta} = \frac{998 \times 9.81 \times 0.70 \times 80}{0.80} = 685\ \text{kW}, \qquad \omega_0 = \frac{2\pi \times 1480}{60} = 155.0\ \text{rad/s}, \qquad T_0 = \frac{P_0}{\omega_0} = 4{,}420\ \text{N m} \]</div>
<h3>Step 2: test the bare set</h3>
<p>With 25&nbsp;kg&middot;m&sup2;, \(E_k\) = &frac12; &times; 25 &times; 155.0&sup2; = 0.30&nbsp;MJ and \(\tau\) = 0.44&nbsp;s, a ratio of 0.02 to 2L/a. The speed is down to 0.22 within five seconds, and the line reaches vapour over about 4&nbsp;km, from 7.3 to 11.3&nbsp;km. <strong>The motor and pump alone protect nothing.</strong></p>
<h3>Step 3: double the inertia until the whole line passes</h3>
<p>The response is far from linear. At 100&nbsp;kg&middot;m&sup2; the lowest head is &minus;8.7&nbsp;m at 7.8&nbsp;km. At 200 the pump reads +5.1&nbsp;m, but the line reaches &minus;1.5&nbsp;m at 5.6&nbsp;km, with about 7&nbsp;km of it below +3.0&nbsp;m. At 400 the whole line holds at <strong>+9.3&nbsp;m</strong> or better, with the lowest point at 3.0&nbsp;km, and nothing rises above 85&nbsp;m. That is <strong>16 times</strong> the bare set. The true threshold lies somewhere between 200 and 400; we design at the tested value that passes with margin.</p>
<h3>Step 4: check that the answer survives the torque law</h3>
<p>The weakest assumption is the torque law, so the same rundowns were rerun under two other plausible characteristics: one that never lets the torque fall below what the shut-off head demands, and a generic radial curve (\(\beta/\alpha^2 = 0.45 + 0.75x - 0.2x^2\)). All three are in the published dataset. The tables above use the law of section 3, which is the upper end of each range rather than a bound on what another law could give. The minima moved by 2&ndash;3&nbsp;m: &minus;4.0 to &minus;1.5&nbsp;m at 200&nbsp;kg&middot;m&sup2; (failing under every law tried), +7.3 to +9.3&nbsp;m at 400 (passing under every law tried) and +23.7 to +26.0&nbsp;m at 1,600. <strong>The conclusion is robust; the decimals are not.</strong> At worst, 400&nbsp;kg&middot;m&sup2; still clears +3.0&nbsp;m by more than 4&nbsp;m.</p>
<h3>Step 5: check the pressure side, and compare</h3>
<p>The maximum is 85.0&nbsp;m: no upsurge at all, and far inside 136&nbsp;m. The reference vessel used across this site (20&nbsp;m&sup3; shell, 3.5&nbsp;m&sup3; gas, DN400 differential connection) gives +4.3&nbsp;m and 119.2&nbsp;m on the same line with the pump stopped at once, so the comparison is not strictly like for like; even at +7.3&nbsp;m the flywheel keeps more margin on the downsurge. Cost, space and operation are compared in <a href="choosing-surge-protection.html">Choosing surge protection on one pipeline</a>.</p>
<h3>Step 6: turn the inertia into steel</h3>
<p>The flywheel must add 375&nbsp;kg&middot;m&sup2;, which stores 4.50&nbsp;MJ. For a solid steel disc \(I = \tfrac12\rho\pi t\,r^4\), so at \(t\) = 120&nbsp;mm:</p>
<div class="eq">\[ r = \left(\frac{2I}{\rho\pi t}\right)^{1/4} = \left(\frac{2 \times 375}{7850\,\pi \times 0.12}\right)^{1/4} = 0.7095\ \text{m} \;\rightarrow\; 0.71\ \text{m} \]</div>
<p>At 0.71&nbsp;m the disc is 1.42&nbsp;m across and weighs 1,492&nbsp;kg. It adds 376&nbsp;kg&middot;m&sup2;, for a total of 401&nbsp;kg&middot;m&sup2;, and its rim runs at 110.0&nbsp;m/s.</p>
<h3>Step 7: price the start</h3>
<p>With 50&nbsp;% of rated torque available for acceleration (section 8), the start time rises from 1.8&nbsp;s to <strong>28.1&nbsp;s</strong>. That figure goes to the motor manufacturer before anything else is fixed.</p>
<h3>&tau; against 2L/a: a screening indicator, not a rule</h3>
<p>Protection arrived at &tau; &asymp; 7&nbsp;s, about a third of 2L/a (0.31); at 0.15 it failed. Do not turn that into a rule. The ratio a line needs depends on its profile, friction, pump curve, torque characteristic and criterion, and a knee can separate whatever the ratio. Use it only to decide whether a flywheel is worth modelling at all [6][7].</p>

<h2 id="int-inertia">6 &middot; Interactive: inertia against minimum pressure</h2>
<p>These are the six runs: minima on the line and at the pump against total inertia, with &tau; on the right-hand axis, and below them the minimum envelope along the main for the selected case. Set your own criterion.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">How much inertia is enough on the 12&nbsp;km main</div>
    <div class="fsub">Six model runs, 685&nbsp;kW at 1,480&nbsp;rpm, all pumps tripping. Upper: line and pump-end minima against total inertia (log scale). Lower: minimum pressure head along the line for the selected inertia, with the steady HGL; the thin grey lines are the other five inertias. Length below the criterion is counted on the 100&nbsp;m computational grid.</div>
  </div>
  <div class="chart-box"><canvas id="invChart"></canvas></div>
  <div class="chart-box" style="height:320px;"><canvas id="envChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Selected inertia</label>
      <select id="sCase2">
        <option value="0">25 kg&middot;m&sup2; (motor and pump only)</option>
        <option value="1">100 kg&middot;m&sup2;</option>
        <option value="2">200 kg&middot;m&sup2;</option>
        <option value="3" selected>400 kg&middot;m&sup2; (design)</option>
        <option value="4">800 kg&middot;m&sup2;</option>
        <option value="5">1,600 kg&middot;m&sup2;</option>
      </select>
      <div class="hint">Highlights the case above and draws its envelope below.</div>
    </div>
    <div class="ctrl">
      <label>Design minimum pressure head <span id="vCrit">+3.0 m</span></label>
      <input type="range" id="sCrit" min="-5" max="20" value="3" step="0.5">
      <div class="hint">+3.0&nbsp;m is the reference criterion. Owners and pipe classes differ.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Selected I</div><div class="v" id="rSel">400 <small>kg&middot;m&sup2;</small></div></div>
    <div class="cell"><div class="k"><span style="text-transform:none">&tau; / (2L/a)</span></div><div class="v" id="rRatio">0.31</div></div>
    <div class="cell"><div class="k">Lowest on line</div><div class="v" id="rLmin2">+9.3 <small>m</small></div></div>
    <div class="cell"><div class="k">Where</div><div class="v" style="font-size:15px;margin-top:6px;" id="rWhere2">at 3.0 km</div></div>
    <div class="cell"><div class="k">Lowest at pump</div><div class="v" id="rPump2">+10.8 <small>m</small></div></div>
    <div class="cell"><div class="k">Line below criterion</div><div class="v" id="rBelow">0.0 <small>km</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;" id="rVer2"><span class="badge good">meets +3.0 m</span></div></div>
    <div class="cell"><div class="k">Smallest tested I that passes</div><div class="v" id="rSmall">400 <small>kg&middot;m&sup2;</small></div></div>
  </div>
</div>
<p class="fig-note">At +3.0&nbsp;m the smallest tested inertia that passes is <strong>400&nbsp;kg&middot;m&sup2;</strong>, with &tau;/(2L/a) = 0.31. Select 200 and the two minima split apart: +5.1&nbsp;m at the pump but &minus;1.5&nbsp;m at 5.6&nbsp;km, with about 7&nbsp;km of line below the criterion. Lower the criterion to 0&nbsp;m and 400 is still needed; at &minus;1.5&nbsp;m, 200 passes. Raise it to +10&nbsp;m and the answer doubles to 800. Treat any pass by less than 2&ndash;3&nbsp;m with suspicion, since that is the spread from the torque law alone. Up to 100&nbsp;kg&middot;m&sup2; the line is at or near vapour. From there each doubling of inertia raises the line minimum by 7&ndash;11&nbsp;m (8.2&nbsp;m from 800 to 1,600), but it also doubles the start time, so every extra metre of margin costs more seconds at every start.</p>

<h2 id="flywheel-design">7 &middot; Designing the flywheel</h2>
<p>For a solid steel disc (\(\rho\) = 7,850&nbsp;kg/m&sup3;):</p>
<div class="eq">\[ m = \rho\pi r^2 t, \qquad I = \tfrac12 m r^2 = \tfrac12\rho\pi t\,r^4, \qquad \frac{E_k}{m} = \frac{(\omega_0 r)^2}{4} = \frac{v_{rim}^2}{4} \]</div>
<p>Inertia goes with the fourth power of radius. Doubling the thickness doubles both inertia and mass, while adding 19&nbsp;% to the radius doubles the inertia for only 41&nbsp;% more mass. The energy per kilogram depends only on rim speed. Rim speed sets the stress in the disc, the hub and the shaft fixing, so it is what limits the diameter, and that limit comes from the manufacturer, not from a rule of thumb.</p>

<div class="tbl-wrap"><table>
  <caption>Solid steel discs on the reference set: 1,480&nbsp;rpm, 685&nbsp;kW, bare set 25&nbsp;kg&middot;m&sup2;, start with 50&nbsp;% of rated torque available for acceleration</caption>
  <thead><tr><th>Disc <span style="text-transform:none">r &times; t</span></th><th class="num">Mass <span style="text-transform:none">(kg)</span></th><th class="num">Disc I <span style="text-transform:none">(kg&middot;m&sup2;)</span></th><th class="num">Disc GD&sup2; <span style="text-transform:none">(kg&middot;m&sup2;)</span></th><th class="num">Rim speed <span style="text-transform:none">(m/s)</span></th><th class="num">Total I <span style="text-transform:none">(kg&middot;m&sup2;)</span></th><th class="num"><span style="text-transform:none">&tau; (s)</span></th><th class="num">Start <span style="text-transform:none">(s)</span></th></tr></thead>
  <tbody>
    <tr><td>0.60&nbsp;m &times; 100&nbsp;mm</td><td class="num">888</td><td class="num">160</td><td class="num">639</td><td class="num">93.0</td><td class="num">185</td><td class="num">3.24</td><td class="num">13.0</td></tr>
    <tr><td><strong>0.71&nbsp;m &times; 120&nbsp;mm</strong> (design)</td><td class="num">1,492</td><td class="num">376</td><td class="num">1,504</td><td class="num">110.0</td><td class="num">401</td><td class="num">7.03</td><td class="num">28.1</td></tr>
    <tr><td>0.80&nbsp;m &times; 120&nbsp;mm</td><td class="num">1,894</td><td class="num">606</td><td class="num">2,424</td><td class="num">124.0</td><td class="num">631</td><td class="num">11.06</td><td class="num">44.3</td></tr>
    <tr><td>1.00&nbsp;m &times; 150&nbsp;mm</td><td class="num">3,699</td><td class="num">1,850</td><td class="num">7,398</td><td class="num">155.0</td><td class="num">1,875</td><td class="num">32.87</td><td class="num">131.5</td></tr>
  </tbody>
</table></div>

<p>In our practice, these items decide whether the flywheel gets built:</p>
<ul class="clean">
  <li><strong>Where it goes.</strong> On a horizontal set the disc sits between motor and pump, or on a second shaft extension at the motor's non-drive end, which needs a motor built for it. Either choice sets the baseplate length.</li>
  <li><strong>Bearings and shaft.</strong> Heavy discs often get pedestal bearings of their own. The added mass lowers the critical speed of the shaft line, and the set supplier has to check it.</li>
  <li><strong>Coupling.</strong> It carries flywheel torque into the pump on every trip and out of the motor on every start.</li>
  <li><strong>Guarding and balancing.</strong> The disc needs a fixed guard, dynamic balancing and a positive fixing to the shaft.</li>
  <li><strong>Vertical sets.</strong> The disc hangs on the thrust bearing. On vertical turbine and submersible pumps a flywheel is rarely practical.</li>
  <li><strong>Space and lifting.</strong> A 1.42&nbsp;m, 1.5&nbsp;tonne disc changes the crane capacity, the withdrawal space and the spacing between sets.</li>
</ul>

<h2 id="motor-start">8 &middot; The motor start penalty</h2>
<p>Whatever the flywheel gives back on a trip, the motor must put in on every start:</p>
<div class="eq">\[ t_{acc} \;=\; \frac{I\,\omega_0}{f\,T_0} \;=\; \frac{2\tau}{f} \]</div>
<p>Here \(f\) is the average fraction of rated torque left over to accelerate the rotor: motor torque minus the pump's load torque. Taking \(f\) = 0.5 is our screening <em>assumption</em>, not a motor constant. At \(f\) = 0.5 the start takes 4&tau;: <strong>1.8&nbsp;s</strong> for the bare set, 7.0&nbsp;s at 100&nbsp;kg&middot;m&sup2;, <strong>28.1&nbsp;s</strong> at 400 and 56.1&nbsp;s at 800.</p>
<ul class="clean">
  <li><strong>Rotor heating.</strong> The heat the rotor absorbs during a start grows with the energy being stored. The motor manufacturer must confirm the starting class, the permitted starts per hour and the minimum time between starts for the actual load inertia.</li>
  <li><strong>Direct-on-line starting.</strong> The starting current and the voltage dip last for the whole run-up. Stall and overcurrent protection must allow it, and any standby generator must carry it.</li>
  <li><strong>Soft starters.</strong> They cut torque along with voltage, which lowers \(f\). With a large flywheel a soft starter may not bring the set up to speed within the motor's thermal limits.</li>
  <li><strong>Variable-speed drives.</strong> A drive gives near-rated torque without inrush, so \(f\) can be higher. But the drive must be rated for the duty, a controlled stop has to dissipate the stored energy or let it coast out, and a power failure trips the set exactly as before.</li>
</ul>

<h2 id="int-calculator">9 &middot; Interactive: flywheel and motor calculator</h2>
<p>Size a disc for your own set. The chart plots &tau; and start time against total inertia, with your set marked on both lines.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Flywheel disc, stored energy and motor start time</div>
    <div class="fsub">Solid steel disc, \(\rho\) = 7,850&nbsp;kg/m&sup3;: \(m = \rho\pi r^2 t\), \(I = \tfrac12 m r^2\). \(E_k = \tfrac12 I\omega_0^2\), \(\tau = E_k/P\), start time \(= I\omega_0/(f\,T_0)\) with \(T_0 = P/\omega_0\). The green line is the &tau; at which the reference main was protected (7.0&nbsp;s at 1,480&nbsp;rpm and 685&nbsp;kW), shown as a screening marker for that main only.</div>
  </div>
  <div class="chart-box"><canvas id="flyChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Disc radius <span id="vR">0.80 m</span></label>
      <input type="range" id="sR" min="0.3" max="1.2" value="0.8" step="0.01">
      <div class="hint">Inertia goes with r&#8308;, rim speed with r.</div>
    </div>
    <div class="ctrl">
      <label>Disc thickness <span id="vTk">120 mm</span></label>
      <input type="range" id="sTk" min="0.05" max="0.30" value="0.12" step="0.01">
      <div class="hint">Inertia and mass both in proportion.</div>
    </div>
    <div class="ctrl">
      <label>Motor + pump inertia <span id="vIm">25 kg&middot;m&sup2;</span></label>
      <input type="range" id="sIm" min="5" max="100" value="25" step="1">
      <div class="hint">From the data sheets: GD&sup2; &divide; 4, or WR&sup2; (lb&middot;ft&sup2;) &times; 0.0421.</div>
    </div>
    <div class="ctrl">
      <label>Shaft power <span id="vPw">685 kW</span></label>
      <input type="range" id="sPw" min="100" max="2000" value="685" step="5">
      <div class="hint">Sets both &tau; and the rated torque.</div>
    </div>
    <div class="ctrl">
      <label>Motor speed <span id="vN">1,480 rpm</span></label>
      <select id="sN">
        <option value="740">740 rpm (8-pole, 50 Hz)</option>
        <option value="990">990 rpm (6-pole, 50 Hz)</option>
        <option value="1480" selected>1,480 rpm (4-pole, 50 Hz)</option>
        <option value="2960">2,960 rpm (2-pole, 50 Hz)</option>
      </select>
      <div class="hint">Stored energy goes with speed squared.</div>
    </div>
    <div class="ctrl">
      <label>Torque available to accelerate <span id="vTq">50 %</span></label>
      <input type="range" id="sTq" min="20" max="100" value="50" step="5">
      <div class="hint">Average motor torque minus pump load torque, as % of rated. 50&nbsp;% is our screening assumption.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Disc mass</div><div class="v" id="rDm">1,894 <small>kg</small></div></div>
    <div class="cell"><div class="k">Disc I</div><div class="v" id="rDI">606 <small>kg&middot;m&sup2;</small></div></div>
    <div class="cell"><div class="k">Total I</div><div class="v" id="rTI">631 <small>kg&middot;m&sup2;</small></div></div>
    <div class="cell"><div class="k">Total GD&sup2;</div><div class="v" id="rGD3">2,524 <small>kg&middot;m&sup2;</small></div></div>
    <div class="cell"><div class="k">Stored energy</div><div class="v" id="rEk3">7.58 <small>MJ</small></div></div>
    <div class="cell"><div class="k"><span style="text-transform:none">&tau;</span> = E/P</div><div class="v" id="rTau3">11.06 <small>s</small></div></div>
    <div class="cell"><div class="k">Start time</div><div class="v" id="rAcc">44.3 <small>s</small></div></div>
    <div class="cell"><div class="k">Rim speed</div><div class="v" id="rRim">124.0 <small>m/s</small></div></div>
  </div>
</div>
<p class="fig-note">The default disc, 0.8&nbsp;m &times; 120&nbsp;mm, weighs <strong>1,894&nbsp;kg</strong> and adds <strong>606&nbsp;kg&middot;m&sup2;</strong>. That makes 631&nbsp;kg&middot;m&sup2; in total, 7.58&nbsp;MJ stored, &tau; = 11.06&nbsp;s, a 44.3&nbsp;s start and a rim speed of 124.0&nbsp;m/s, which is more than the main needs. Drag the radius to 0.71&nbsp;m: the disc drops to 1,492&nbsp;kg and 376&nbsp;kg&middot;m&sup2;, the total is the design 401&nbsp;kg&middot;m&sup2;, and the start takes 28.1&nbsp;s. Raise the torque available to accelerate to 100&nbsp;% and the start halves to 14.1&nbsp;s. Switch to 2,960&nbsp;rpm and the same disc stores four times the energy, but its rim speed doubles to 220.1&nbsp;m/s, well beyond the 155.0&nbsp;m/s of the largest disc in section 7; get the permissible rim speed from the manufacturer.</p>

<h2 id="wrong-answer">10 &middot; When a flywheel is the wrong answer</h2>
<p>Flywheels belong on short and medium-length mains, where a modest addition of inertia buys a rundown long enough to matter over the wave period [5][6][11]. Outside that range the answer is usually something else.</p>
<ul class="clean">
  <li><strong>Long lines.</strong> The rundown a line needs grows with its wave period. Since the start time is \(2\tau/f\), a line that needs &tau; to be a sizeable fraction of 2L/a needs a start time of the same order as 2L/a. On long mains that inertia soon exceeds what a motor can accelerate within its thermal limits, or what the shaft and bearings can carry [6][11]. In our practice a <a href="surge-vessel.html">vessel</a> usually scales better.</li>
  <li><strong>Frequent starts.</strong> Every start pays the thermal price of section 8, and stations that cycle on level control use up their permitted starts.</li>
  <li><strong>Variable-speed stations.</strong> A large flywheel works against controlled ramping and adds drive duty. The drive itself does nothing for a power-failure trip, so the surge case is the same as for a fixed-speed set.</li>
  <li><strong>Knees and high points.</strong> A flywheel acts at the pump, and a knee can still separate. See <a href="one-way-surge-tank-design.html">One-way surge tanks at the knee</a>.</li>
  <li><strong>Upsurge problems.</strong> It does not help with a <a href="water-hammer-control-valve.html">valve closure</a> elsewhere on the system. It delays the flow reversal at the pump's <a href="check-valve-hammer.html">non-return valve</a>, but that valve must still close without slamming.</li>
  <li><strong>Vertical and submersible sets.</strong> There is rarely anywhere to put the disc.</li>
</ul>
<p>A <a href="surge-relief-valve-sizing.html">surge relief valve</a> covers only the pressure side. The full comparison is in <a href="choosing-surge-protection.html">Choosing surge protection on one pipeline</a>.</p>

<h2 id="hammer-setup">11 &middot; Setting it up in Bentley HAMMER</h2>
<p>This is how we check a flywheel in HAMMER [10]; the general <a href="hammer-transient-simulation-workflow.html">transient workflow</a> and <a href="hammer-transient-tips.html">common pitfalls</a> are covered separately. Field names differ slightly between HAMMER versions.</p>
<ol>
  <li><strong>Build the line and check the steady state.</strong> Model a <strong>Reservoir</strong> for the wet well, the <strong>Pump</strong>, <strong>Pipes</strong> with <strong>Junctions</strong> along the route, and a delivery <strong>Reservoir</strong> (see <a href="boundary-conditions-reservoir-tank.html">boundary conditions</a>). Set wave speeds with the <strong>Wave Speed Calculator</strong> (see <a href="wave-speed-surge-analysis.html">Wave speed</a>), and confirm the steady HGL (85.0&nbsp;m and 44.8&nbsp;m here) first.</li>
  <li><strong>Define the pump.</strong> Enter the duty, pump curve, efficiency and <strong>speed</strong> (1,480&nbsp;rpm). Select the <strong>4-quadrant characteristic curves</strong> from the specific speed closest to the real impeller, or ask the manufacturer for the complete characteristics; the rundown torque is where the answer is sensitive.</li>
  <li><strong>Enter the inertia (pump and motor)</strong> as the total on the shaft: rotor, impeller, coupling and flywheel. Check whether each value is \(I\), GD&sup2; or WR&sup2;, and whether the pump value includes the water in the impeller. Before data sheets exist, estimate the inertia from published correlations with power and speed [6], and record the estimate as an assumption.</li>
  <li><strong>Set the pump trip (shut down)</strong> at the start of the run, with every pump in the station tripping together.</li>
  <li><strong>Model the check valve on the pump</strong>, first as ideal and then with its real <strong>closure time/delay</strong>. A valve that closes slowly passes reverse flow before it seats and can then slam; check the reverse velocity at closure with the real closure time, even though the flywheel delays the reversal.</li>
  <li><strong>Set up each inertia as its own alternative and scenario</strong> (the six inertias of the tables, 25 to 1,600&nbsp;kg&middot;m&sup2;), changing nothing else, so the envelopes can be compared and the threshold bracketed.</li>
  <li><strong>Set the transient run options.</strong> Make the <strong>run duration</strong> several times 2L/a (150&nbsp;s here). Accept the <strong>time step</strong> computed from the shortest pipe and the wave speeds, and check that the <strong>wave speed adjustment tolerance</strong> has not moved any wave speed materially. Turn on <strong>vapour pressure / column separation</strong>, and keep the <strong>friction method</strong> the same in every run.</li>
  <li><strong>Read the time histories</strong> in the <strong>Transient Results Viewer</strong>: head and pump speed at the pump. A set that stops in about a second when you expected a slow rundown usually has its inertia in the wrong unit.</li>
  <li><strong>Read the profile, not the pump.</strong> Plot the <strong>profile (path)</strong> with <strong>maximum and minimum head envelopes</strong>. Check the lowest head and its chainage against +3.0&nbsp;m and the maximum against 136&nbsp;m, and use the <strong>animation</strong> to see where the minimum forms.</li>
  <li><strong>Test the sensitivity.</strong> Rerun the chosen inertia with neighbouring specific-speed characteristics, the lowest credible inertia and the wave speed range. If the minimum moves by more than your margin, the design is not yet robust.</li>
  <li><strong>Close the loop on site.</strong> In our practice a recorded trip after commissioning is the best check of the modelled inertia; see <a href="transient-analysis-scada.html">SCADA records in transient analysis</a>.</li>
</ol>

<h2 id="checklist">12 &middot; Design checklist</h2>
<ul class="clean">
  <li><strong>Model the unprotected case first</strong> with data-sheet inertia, and confirm that the downsurge is the problem.</li>
  <li><strong>Get the inertia unit right</strong> (\(I\), GD&sup2; or WR&sup2;) for the motor, the pump and the coupling.</li>
  <li><strong>Screen with E<sub>k</sub>, &tau; and &tau;/(2L/a)</strong>, and never treat the ratio as a rule.</li>
  <li><strong>Double the inertia step by step</strong> and judge each case on the minimum envelope along the whole line.</li>
  <li><strong>Bracket the torque-law uncertainty</strong>, and keep a margin larger than the spread (2&ndash;3&nbsp;m here).</li>
  <li><strong>Make sure the chosen design never reaches vapour</strong>, so that no result rests on a collapse peak.</li>
  <li><strong>Confirm the maximum</strong> against the allowable pressure, and check non-return valve closure with its real characteristic.</li>
  <li><strong>Size the disc</strong> from \(I = \tfrac12\rho\pi t r^4\), and get the permissible rim speed, balancing and shaft fixing from the manufacturer.</li>
  <li><strong>Send the total load inertia and starting method to the motor manufacturer</strong>, and get back the start time, the thermal check and the permitted starts per hour.</li>
  <li><strong>Check the electrical side</strong>: protection settings, voltage dip and any standby generator.</li>
  <li><strong>Resolve the layout</strong>: bearings, coupling, guard, baseplate, crane and withdrawal space.</li>
  <li><strong>Weigh the alternatives</strong> on the same line, including how often the station starts and the <a href="surge-analysis-risk.html">consequence of a protection failure</a>.</li>
  <li><strong>Run the final design in HAMMER</strong> on the surveyed profile, and verify it with a recorded trip.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge protection design series</span>
  <ol>
    <li><a href="wave-speed-surge-analysis.html">Wave speed: the number that sets the surge</a></li>
    <li><a href="surge-vessel-differential-orifice.html">The differential orifice: empty freely, refill slowly</a></li>
    <li><a href="surge-vessel-type-selection.html">Bladder, diaphragm or air-over-water vessel</a></li>
    <li><a href="one-way-surge-tank-design.html">One-way surge tanks at the knee</a></li>
    <li><a href="surge-relief-valve-sizing.html">Surge relief valves: what a valve at the pump can protect</a></li>
    <li><strong>Pump inertia and the flywheel</strong></li>
    <li><a href="choosing-surge-protection.html">Choosing surge protection on one pipeline</a></li>
  </ol>
  The sizing method itself is in <a href="surge-vessel.html">Sizing the Hydropneumatic Surge Vessel</a>.
</div>
"""

CHARTS = r"""
const D=__DATA__;
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const FF="'IBM Plex Sans', system-ui, sans-serif";
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:FF,size:11}}};
const TTL={family:FF,size:12,weight:'600'};
const LBL={size:10,family:FF};
const LEGF={family:FF,size:11.5};
const L2A=2*12000/1050, VAP=-9.8, PMIN=3.0;
const W0=1480*2*Math.PI/60, P0=685e3;
const C=D.cases, T=D.t, X=D.x;
const sgn1=v=>(Math.abs(v)<=0.04?'':(v<0?'&minus;':'+'))+fmt1(Math.abs(v));
const sgnT=v=>(Math.abs(v)<=0.04?'':(v<0?'−':'+'))+fmt1(Math.abs(v));
const Ek=(I,w0)=>0.5*I*w0*w0;
const isVap=c=>c.line_min<=VAP+0.05;
function whereTxt(c){
  if(isVap(c)){
    const xs=X.filter((x,i)=>c.Hmin[i]<=VAP+0.05);
    const x0=xs.length?xs[0]:c.at_min, x1=xs.length?xs[xs.length-1]:c.at_min;
    return fmt1(x0/1000)+'&ndash;'+fmt1(x1/1000)+' km';
  }
  return c.at_min===0?'at the pump':'at '+fmt1(c.at_min/1000)+' km';
}
function verdict(v,crit){
  if(v<=VAP+0.05) return '<span class="badge bad">vapour: column separation</span>';
  if(v<crit) return '<span class="badge warn">below '+sgn1(crit)+' m</span>';
  return '<span class="badge good">meets '+sgn1(crit)+' m</span>';
}

/* ---------- CHART 1 : the rundown ---------- */
const sCase1=document.getElementById('sCase1'), sWin=document.getElementById('sWin');
const xy=a=>T.map((t,k)=>({x:t,y:a[k]}));
const runChart=new Chart(document.getElementById('runChart'),{
  data:{datasets:[
    {type:'line',label:'Head at pump (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,yAxisID:'y',order:1},
    {type:'line',label:'Speed ratio (right)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.2,pointRadius:0,yAxisID:'y1',order:2},
    {type:'line',label:'Head, bare set',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.4,borderDash:[5,4],pointRadius:0,yAxisID:'y',order:3},
    {type:'line',label:'Speed, bare set',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.4,borderDash:[2,3],pointRadius:0,yAxisID:'y1',order:4}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:90,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:-20,max:100,position:'left',title:{display:true,text:'Pressure head at the pump (m)',font:TTL},grid:{color:'#eef2f5'},ticks:{font:{family:FF,size:11},stepSize:20}},
            y1:{type:'linear',min:0,max:1,position:'right',title:{display:true,text:'Speed ratio n/n₀',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11},stepSize:0.2}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:6,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}},
      tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`${c.dataset.label}: ${fmt2(c.parsed.y)}`:`${c.dataset.label}: ${fmt1(c.parsed.y)} m`}},
      annotation:{annotations:{
        pmin:{type:'line',yScaleID:'y',yMin:PMIN,yMax:PMIN,borderColor:'#1e8449',borderWidth:1.5,borderDash:[6,4],
              label:{display:true,content:'+3.0 m design minimum',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}},
        vap:{type:'line',yScaleID:'y',yMin:VAP,yMax:VAP,borderColor:'#c0392b',borderWidth:1.5,borderDash:[6,4],
              label:{display:true,content:'vapour −9.8 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(192,57,43,0.85)'}},
        tla:{type:'line',xScaleID:'x',xMin:L2A,xMax:L2A,borderColor:'#6b4f9e',borderWidth:1.5,borderDash:[4,4],
              label:{display:true,content:'2L/a = 22.9 s',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}
      }}}}
});
function updRun(){
  const i=+sCase1.value, c=C[i], win=+sWin.value;
  document.getElementById('vWin').textContent=win+' s';
  runChart.data.datasets[0].data=xy(c.H);
  runChart.data.datasets[1].data=xy(c.w);
  runChart.data.datasets[2].data=i===0?[]:xy(C[0].H);
  runChart.data.datasets[3].data=i===0?[]:xy(C[0].w);
  runChart.options.scales.x.max=win;
  runChart.update('none');
  const e=Ek(c.I,W0), tau=e/P0;
  document.getElementById('rI').innerHTML=fmt0(c.I)+' <small>kg·m²</small>';
  document.getElementById('rGD').innerHTML=fmt0(4*c.I)+' <small>kg·m²</small>';
  document.getElementById('rEk').innerHTML=fmt2(e/1e6)+' <small>MJ</small>';
  document.getElementById('rTau').innerHTML=fmt2(tau)+' <small>s</small>';
  document.getElementById('rLmin').innerHTML=sgn1(c.line_min)+' <small>m, '+whereTxt(c)+'</small>';
  document.getElementById('rVer').innerHTML=verdict(c.line_min,PMIN);
  document.getElementById('rLmax').innerHTML=isVap(c)?'<small>not quoted (cavitating)</small>':fmt1(c.line_max)+' <small>m</small>'+(c.I===100?' <small>(indicative)</small>':'');
}
[sCase1,sWin].forEach(s=>s.addEventListener('input',updRun));updRun();

/* ---------- CHART 2 : inertia against minimum pressure ---------- */
const sCase2=document.getElementById('sCase2'), sCrit=document.getElementById('sCrit');
const critAnn=()=>({type:'line',yScaleID:'y',yMin:PMIN,yMax:PMIN,borderColor:'#1e8449',borderWidth:1.5,borderDash:[6,4],
  label:{display:true,content:'design minimum +3.0 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}});
const vapAnn=()=>({type:'line',yScaleID:'y',yMin:VAP,yMax:VAP,borderColor:'#c0392b',borderWidth:1.5,borderDash:[6,4],
  label:{display:true,content:'vapour −9.8 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(192,57,43,0.85)'}});
const invChart=new Chart(document.getElementById('invChart'),{
  data:{datasets:[
    {type:'line',label:'Lowest head on the line (m)',data:C.map(c=>({x:c.I,y:c.line_min})),borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:4,yAxisID:'y',order:2},
    {type:'line',label:'Lowest head at the pump (m)',data:C.map(c=>({x:c.I,y:c.pump_min})),borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.8,borderDash:[6,4],pointRadius:3,yAxisID:'y',order:3},
    {type:'line',label:'τ = E/P (s, right axis)',data:C.map(c=>({x:c.I,y:+(Ek(c.I,W0)/P0).toFixed(3)})),borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:1.8,borderDash:[2,3],pointRadius:3,yAxisID:'y1',order:4},
    {type:'scatter',label:'Selected',data:[],backgroundColor:'#6b4f9e',borderColor:'#fff',borderWidth:2,pointRadius:8,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'logarithmic',min:15,max:2500,title:{display:true,text:'Total inertia on the shaft, I (kg·m², log scale)',font:TTL},
               grid:{color:'#eef2f5'},ticks:{font:{family:FF,size:11},callback:v=>fmt0(v)},
               afterBuildTicks:ax=>{ax.ticks=[25,50,100,200,400,800,1600].map(v=>({value:v}));}},
            y:{type:'linear',min:-15,max:30,position:'left',title:{display:true,text:'Lowest pressure head (m)',font:TTL},...AX},
            y1:{type:'linear',min:0,max:30,position:'right',title:{display:true,text:'τ (s)',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`τ ${fmt2(c.parsed.y)} s at I = ${fmt0(c.parsed.x)} kg·m²`:`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at I = ${fmt0(c.parsed.x)} kg·m²`}},
      annotation:{annotations:{crit:critAnn(),vap:vapAnn()}}}}
});
const envSets=[
  {type:'line',label:'Steady HGL (m)',data:[{x:0,y:85},{x:12,y:44.8}],borderColor:'#6b4f9e',backgroundColor:'#6b4f9e',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:3},
  {type:'line',label:'Minimum head, selected inertia (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.6,pointRadius:0,order:1}
];
for(let k=0;k<C.length-1;k++) envSets.push({type:'line',label:'Other inertias',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1,pointRadius:0,order:2});
const envChart=new Chart(document.getElementById('envChart'),{
  data:{datasets:envSets},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:12,title:{display:true,text:'Chainage from the pump station (km)',font:TTL},...AX},
            y:{type:'linear',min:-20,max:90,title:{display:true,text:'Minimum pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8,filter:it=>it.datasetIndex<=2}},
      tooltip:{filter:it=>it.datasetIndex<=1,callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} km`}},
      annotation:{annotations:{crit:critAnn(),vap:vapAnn()}}}}
});
function updInv(){
  const i=+sCase2.value, c=C[i], crit=+sCrit.value;
  document.getElementById('vCrit').textContent=sgnT(crit)+' m';
  [invChart,envChart].forEach(ch=>{
    const a=ch.options.plugins.annotation.annotations.crit;
    a.yMin=crit; a.yMax=crit; a.label.content='design minimum '+sgnT(crit)+' m';
  });
  invChart.data.datasets[3].data=[{x:c.I,y:c.line_min}];
  invChart.update('none');
  envChart.data.datasets[1].data=X.map((x,k)=>({x:x/1000,y:c.Hmin[k]}));
  let k=2;
  C.forEach((o,j)=>{if(j!==i){envChart.data.datasets[k].data=X.map((x,n)=>({x:x/1000,y:o.Hmin[n]}));k++;}});
  envChart.update('none');
  const tau=Ek(c.I,W0)/P0;
  const below=c.Hmin.filter(h=>h<crit).length*0.1;
  const ok=C.filter(o=>!isVap(o)&&o.line_min>=crit);
  document.getElementById('rSel').innerHTML=fmt0(c.I)+' <small>kg·m²</small>';
  document.getElementById('rRatio').innerHTML=fmt2(tau/L2A);
  document.getElementById('rLmin2').innerHTML=sgn1(c.line_min)+' <small>m</small>';
  document.getElementById('rWhere2').innerHTML=whereTxt(c);
  document.getElementById('rPump2').innerHTML=sgn1(c.pump_min)+' <small>m</small>';
  document.getElementById('rBelow').innerHTML=fmt1(below)+' <small>km</small>';
  document.getElementById('rVer2').innerHTML=verdict(c.line_min,crit);
  document.getElementById('rSmall').innerHTML=ok.length?fmt0(ok[0].I)+' <small>kg·m²</small>':'<small>none of the six</small>';
}
[sCase2,sCrit].forEach(s=>s.addEventListener('input',updInv));updInv();

/* ---------- CHART 3 : flywheel and motor calculator ---------- */
const sR=document.getElementById('sR'), sTk=document.getElementById('sTk'), sIm=document.getElementById('sIm'),
      sPw=document.getElementById('sPw'), sN=document.getElementById('sN'), sTq=document.getElementById('sTq');
const RHO_S=7850, TAU_REF=Ek(400,W0)/P0;
const flyChart=new Chart(document.getElementById('flyChart'),{
  data:{datasets:[
    {type:'line',label:'Start time at the chosen torque (s)',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.4,pointRadius:0,order:3},
    {type:'line',label:'τ = E/P (s)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,order:4},
    {type:'scatter',label:'Your set, start time',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1},
    {type:'scatter',label:'Your set, τ',data:[],backgroundColor:'#1b4f72',borderColor:'#fff',borderWidth:2,pointRadius:7,order:2}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:2000,title:{display:true,text:'Total inertia on the shaft, I (kg·m²)',font:TTL},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Time (s)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} s at I = ${fmt0(c.parsed.x)} kg·m²`}},
      annotation:{annotations:{
        tref:{type:'line',yMin:TAU_REF,yMax:TAU_REF,borderColor:'#1e8449',borderWidth:1.5,borderDash:[6,4],
              label:{display:true,content:'τ 7.0 s: reference main protected (screening)',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}}
      }}}}
});
function updFly(){
  const r=+sR.value, t=+sTk.value, Im=+sIm.value, P=+sPw.value*1000, N=+sN.value, f=+sTq.value/100;
  document.getElementById('vR').textContent=fmt2(r)+' m';
  document.getElementById('vTk').textContent=fmt0(t*1000)+' mm';
  document.getElementById('vIm').textContent=fmt0(Im)+' kg·m²';
  document.getElementById('vPw').textContent=fmt0(P/1000)+' kW';
  document.getElementById('vN').textContent=fmt0(N)+' rpm';
  document.getElementById('vTq').textContent=fmt0(f*100)+' %';
  const w0=N*2*Math.PI/60, m=RHO_S*Math.PI*r*r*t, Id=0.5*m*r*r, It=Id+Im;
  const e=Ek(It,w0), tau=e/P, T0=P/w0, tacc=It*w0/(f*T0), rim=w0*r;
  const xmax=Math.max(2000,Math.ceil(It*1.25/500)*500);
  const xs=[];for(let k=0;k<=40;k++)xs.push(xmax*k/40);
  flyChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(x*w0/(f*T0)).toFixed(2)}));
  flyChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(Ek(x,w0)/P).toFixed(3)}));
  flyChart.data.datasets[2].data=[{x:+It.toFixed(1),y:+tacc.toFixed(2)}];
  flyChart.data.datasets[3].data=[{x:+It.toFixed(1),y:+tau.toFixed(3)}];
  flyChart.options.scales.x.max=xmax;
  flyChart.update('none');
  document.getElementById('rDm').innerHTML=fmt0(m)+' <small>kg</small>';
  document.getElementById('rDI').innerHTML=fmt0(Id)+' <small>kg·m²</small>';
  document.getElementById('rTI').innerHTML=fmt0(It)+' <small>kg·m²</small>';
  document.getElementById('rGD3').innerHTML=fmt0(4*It)+' <small>kg·m²</small>';
  document.getElementById('rEk3').innerHTML=fmt2(e/1e6)+' <small>MJ</small>';
  document.getElementById('rTau3').innerHTML=fmt2(tau)+' <small>s</small>';
  document.getElementById('rAcc').innerHTML=fmt1(tacc)+' <small>s</small>';
  document.getElementById('rRim').innerHTML=fmt1(rim)+' <small>m/s</small>';
}
[sR,sTk,sIm,sPw,sN,sTq].forEach(s=>s.addEventListener('input',updFly));updFly();

window.addEventListener('load',function(){try{runChart.resize();invChart.resize();envChart.resize();flyChart.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ISO 2531 <em>Ductile iron pipes, fittings, accessories and their joints for water applications</em> &mdash; the DN800 K9 ductile iron pipe of the reference main.</li>
  <li>EN 805 <em>Water supply &mdash; Requirements for systems and components outside buildings</em> &mdash; design and allowable pressures, and the surge allowance the maximum is checked against.</li>
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993 &mdash; the Joukowsky relation, the method of characteristics, pump boundary conditions with rotor inertia, and the discrete vapour cavity model.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005 &mdash; overview of transient control strategies, including added pump inertia.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014 &mdash; pump rundown equations, complete (four-quadrant) pump characteristics, and flywheels as a control measure.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004 &mdash; pump trip and rundown, estimating pump and motor inertia, and where flywheels are and are not practical.</li>
  <li>Parmakian, J. <em>Waterhammer Analysis</em>. Dover, 1963 &mdash; classical charts for power failure at a pump, built on pipeline and pump inertia parameters.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006 &mdash; column separation, vapour and gas cavity models, and why collapse peaks are model-sensitive.</li>
  <li>Larock, B.E., Jeppson, R.W. &amp; Watters, G.Z. <em>Hydraulics of Pipeline Systems</em>. CRC Press, 2000 &mdash; homologous pump relations and transient pump boundary conditions.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> product documentation and help &mdash; pump inertia, pump trip, 4-quadrant characteristic curves, check valve closure, transient run options and results viewing.</li>
  <li>Stephenson, D. <em>Pipeline Design for Water Engineers</em>, 3rd ed. Elsevier, 1989 &mdash; water hammer protection of pumping lines, and the practical limits of flywheels on long mains.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #HydraulicTransients #PumpTrip #PowerFailure #PumpInertia #Flywheel #GD2 #MomentOfInertia #PumpRundown #ColumnSeparation #VapourCavity #MethodOfCharacteristics #BentleyHAMMER #OpenFlowsHAMMER #SurgeProtection #TransmissionMain #DuctileIron #PumpStation #PumpStationDesign #MotorStarting #VariableSpeedDrive #SoftStarter #FourQuadrantCharacteristics #CheckValve #TransientAnalysis #PipelineDesign #HydraulicDesign #WaterInfrastructure #WaterEngineering</div>
"""

import json, os
_D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'datasets.json')))
_F = _D['flywheel']
DATA = {
    't': _F['cases'][0]['t'],
    'x': _F['x'],
    'cases': [{k: c[k] for k in ('I', 'line_min', 'at_min', 'pump_min', 'line_max', 'w5', 'w10', 'w229', 'w', 'H', 'Hmin')}
              for c in _F['cases']],
}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='pump-inertia-flywheel-surge', cat='surge', mins=33,
    date_iso='2026-09-16', date_human='September 2026', date_ar='سبتمبر 2026',
    title='Pump Inertia and the Flywheel: When Spinning Mass Can Replace a Surge Vessel',
    reg_title='Pump Inertia and the Flywheel: When Spinning Mass Can Replace a Surge Vessel',
    reg_tag='Surge Analysis · Pump Inertia · Flywheel',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Pump Inertia &middot; Flywheel',
    desc='How added pump inertia protects a pumping main after a power failure: the rundown equation, stored energy, time constant and GD2, six inertias modelled on a 12 km DN800 main, flywheel disc sizing, the motor start penalty and a Bentley HAMMER procedure, with three interactive charts.',
    og_desc='On a 12 km DN800 main the bare motor and pump (25 kg·m²) let the line reach vapour; 400 kg·m² in total keeps it at or above +9.3 m with no upsurge above 85 m. The price: a 28.1 s motor start with half of rated torque available for acceleration.',
    ld_desc='Design guide to pump inertia and flywheels for surge protection: rundown physics, six modelled inertias on a 12 km main, flywheel disc sizing, motor start time and the Bentley HAMMER set-up.',
    img_alt='Cutaway of a centrifugal pump with a large steel flywheel between pump and motor, labelled GD², coupling and non-return valve, and an inset graph of pump speed against time with and without a flywheel',
    en_tag='Surge &amp; Transient Analysis &middot; Pump Inertia',
    en_title='Pump Inertia and the Flywheel: When Spinning Mass Can Replace a Surge Vessel',
    en_excerpt='On a 12 km DN800 main, <strong>400 kg·m² in total</strong> on the pump shaft keeps the whole line at or above <strong>+9.3 m</strong> after a power failure, with no upsurge above the steady 85 m; the bare motor and pump, at about 25 kg·m², protect nothing and the line reaches vapour. The price comes at every start: with half of rated torque available for acceleration the run-up takes <strong>28.1 s</strong>. A pump coasts down on the energy in its rotating parts, and for as long as it coasts it keeps the column moving. Six inertias modelled, the flywheel disc sized, the motor start checked, the HAMMER set-up, and three interactive charts.',
    en_search='pump inertia flywheel surge protection water hammer pump trip power failure rundown moment of inertia GD2 WR2 stored kinetic energy time constant 2L/a column separation vapour cavity downsurge transmission main ductile iron DN800 pump station design motor starting time acceleration time direct on line soft starter variable speed drive VFD four-quadrant characteristics specific speed non-return valve check valve closure Bentley HAMMER OpenFlows transient analysis method of characteristics steel disc flywheel rim speed bearings coupling surge vessel alternative',
    ar_title='القصور الذاتي للمضخة والحدّافة: متى تُغني الكتلة الدوّارة عن خزان الحماية من المطرقة المائية',
    ar_excerpt='على خط بطول ١٢ كم وقطر ٨٠٠ مم، يكفي قصور ذاتي كلي قدره <strong>٤٠٠ كغ·م²</strong> كي لا ينخفض الضغط في أي نقطة من الخط عن <strong>+٩٫٣ م</strong> بعد انقطاع الكهرباء، دون أي ارتفاع فوق ٨٥ م، في حين لا يحمي القصور الذاتي للمحرك والمضخة وحدهما (نحو ٢٥ كغ·م²) شيئاً، إذ يبلغ الخط ضغط التبخر. والثمن زمن إقلاع يبلغ <strong>٢٨٫١ ثانية</strong> عندما يتوفر للتسارع نصف العزم المقنن. فالمضخة لا تتوقف فوراً، بل تتباطأ مستهلكةً الطاقة المخزنة في أجزائها الدوّارة وتواصل دفع عمود الماء. ويتضمن المقال ثلاثة رسوم تفاعلية.',
    ar_search='الطرق المائي المطرقة المائية القصور الذاتي للمضخة عطالة المضخة الحدافة الحدّافة عزم القصور الذاتي GD2 زمن التسارع خزان الضغط الهوائي توقف المضخة انقطاع الكهرباء تباطؤ المضخة الطاقة الحركية المخزنة انفصال عمود الماء التكهف ضغط التبخر طريقة الخطوط المميزة خط نقل المياه حديد الدكتايل محطة الضخ زمن إقلاع المحرك مغير السرعة البادئ الناعم صمام عدم الرجوع خزان الحماية من الطرق المائي تحليل الموجات العابرة بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
