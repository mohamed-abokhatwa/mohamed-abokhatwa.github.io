# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">On a main that climbs out of the pump station and then runs level, the point that governs the surge protection after a power cut is not the pump but the knee, where the climb turns flat. On our 12&nbsp;km DN800 example, a surge vessel that holds the knee at +3.0&nbsp;m on its own needs <strong>43.1&nbsp;m&sup3; of gas in a 104.5&nbsp;m&sup3; shell</strong>. Put a low one-way tank at the knee, its water 8&nbsp;m above the pipe behind a check valve, and the vessel falls to <strong>15.9&nbsp;m&sup3; of gas in a 37.8&nbsp;m&sup3; shell &mdash; 64&nbsp;% smaller</strong> &mdash; for 20.7&nbsp;m&sup3; of water that the tank gives up. This article designs that pair, and shows the two ways it goes wrong: a tank set too high, and a tank asked to work alone.</p>

<h2 id="knee-weak-point">1 &middot; Why the knee is the weak point</h2>
<p>When every pump trips at once, the flow at the station stops and a low-pressure wave leaves along the main. Its size is the Joukowsky head [1]:</p>
<div class="eq">\[ \Delta H = \frac{a\,\Delta V}{g} = \frac{1050 \times 1.393}{9.81} = 149.1\ \text{m} \]</div>
<p>That is more than the 94.8&nbsp;m (85.0 + 9.8) the pump end has above vapour, so without protection the wave is cut off at vapour and the column separates. What a point on the pipe can tolerate, though, is a drop in <em>pressure</em>, and pressure is the HGL minus the pipe's own elevation:</p>
<div class="eq">\[ p(x,t) = H(x,t) - z(x) \;\geq\; +3.0\ \text{m} \]</div>
<p>Our profile climbs 30&nbsp;m in its first 300&nbsp;m and then runs level for 11.7&nbsp;km, so the steady pressure falls from 85.0&nbsp;m at the pump to 54.0&nbsp;m at the knee although the HGL has dropped only 1.0&nbsp;m. The knee has 51.0&nbsp;m to lose before it reaches the criterion; the pump end has 82.0&nbsp;m.</p>
<p>That matters most for a vessel at the pump. It fights the wave for the first seconds; after that the column slows as one mass, the HGL between the pump and the knee lies almost level, and the pressure at the knee is roughly the vessel's head minus 30&nbsp;m:</p>
<div class="eq">\[ p_{knee} \approx H_{pump} - z_{knee} \quad\Rightarrow\quad H_{pump,\,min} \approx z_{knee} + 3.0 = 33.0\ \text{m} \]</div>
<p>So the vessel must still hold about 33&nbsp;m when its gas is at its largest. In the vessel-alone run the knee touches +3.0&nbsp;m nearly two minutes after the trip, and the pump end bottoms out at +32.7&nbsp;m a few seconds later. The polytropic gas law sets the bill [2, 3]:</p>
<div class="eq">\[ P_0 V_0^{\,n} = P_{min} V_{max}^{\,n} \quad\Rightarrow\quad V_0 = \frac{\Delta V_w}{\left(P_0/P_{min}\right)^{1/n} - 1} \]</div>
<p>with \(P_0\) = 85.0 + 10.33 = 95.3&nbsp;m absolute, \(P_{min}\) = 32.7 + 10.33 = 43.0&nbsp;m absolute, \(n\) = 1.2 and \(\Delta V_w\) the water pushed into the line. While its pressure falls to less than half, the gas grows only \((95.3/43.0)^{1/1.2}\) = 1.94 times, and by then the vessel has delivered 40.5&nbsp;m&sup3;, so it needs 40.5 / 0.94 = <strong>43.1&nbsp;m&sup3; of gas</strong>. On the flat reference main, the site's reference vessel &mdash; 3.5&nbsp;m&sup3; of gas, same differential connection &mdash; holds +4.3&nbsp;m with margin to spare: a 30&nbsp;m climb in the first 300&nbsp;m has multiplied the gas more than twelve times.</p>

<h2 id="how-it-works">2 &middot; How a one-way surge tank works</h2>
<p>A one-way surge tank &mdash; the literature also calls it a feed tank or a discharge tank [4, 5] &mdash; is an unpressurised tank beside the main, connected through a check valve that opens only towards the pipe. Its surface stands \(h_T\) above the pipe. While the main's pressure there exceeds \(h_T\) the valve stays shut and the tank does nothing; once the downsurge pulls it below, the valve opens and the tank feeds the line at its own head:</p>
<div class="eq">\[ H_{knee} = z_{knee} + h_T, \qquad q_T = Q_{down} - Q_{up} \;\geq\; 0, \qquad V_{draw} = \int q_T\,dt \]</div>
<p>The knee is held at the tank level for as long as water remains. When the main recovers the valve closes, and a small refill line tops the tank up. In a method-of-characteristics model it is an interior boundary with the head fixed while the tank feeds [1, 2].</p>
<h3>Not a standpipe, and not an air valve</h3>
<p>An open surge tank is connected freely, so its surface must stand at the steady HGL &mdash; here a column 54.0&nbsp;m above the pipe, before any upsurge. The one-way tank sits far below the HGL and needs no pressure rating, but it acts at its own node: it cannot stop the first downsurge reaching the pump end, and alone it leaves the pump end at vapour, although once open its head raises the later minima on the pump side (section 8). An air valve at the knee is still worth fitting for filling, draining and venting [6], but it admits air only once the pressure falls below atmospheric, so it cannot hold +3.0&nbsp;m (see <a href="air-admission-networks.html">air admission in networks</a>).</p>
<h3>The rule that limits the tank level</h3>
<p>At rest the main settles at the level of the delivery reservoir. A tank surface above that opens its check valve and drains through the pipeline after every stop, so the level must stay below the lowest downstream HGL at rest:</p>
<div class="eq">\[ h_T \;\lt\; H_{rest} - z_{knee} = 44.8 - 30.0 = 14.8\ \text{m} \]</div>
<p>Exceed it and a rigid-column estimate with the friction below the knee gives the drain rate:</p>
<div class="eq">\[ Q_{drain} = \sqrt{\frac{z_{knee} + h_T - H_{rest}}{r}}, \qquad r = \frac{84.0 - 44.8}{0.70^2} = 80\ \text{s}^2/\text{m}^5 \]</div>
<p>A 16&nbsp;m tank would drain at \(\sqrt{1.2/80}\) = 0.12&nbsp;m&sup3;/s, indefinitely. The method-of-characteristics run drains faster while the line is still emptying and settles to 0.122&nbsp;m&sup3;/s after about ten minutes. That is a check on the arithmetic and not an independent one: the transient model carries the same lumped quadratic friction, so it must converge on the closed form.</p>

<h2 id="example">3 &middot; The example profile and the modelling basis</h2>
<p>The main is the series reference with one change of profile: 12&nbsp;km of DN800 ductile iron K9 [7] carrying 0.70&nbsp;m&sup3;/s (2,520&nbsp;m&sup3;/h, 1.39&nbsp;m/s), wave speed 1,050&nbsp;m/s, HGL 85.0&nbsp;m at the pump and 44.8&nbsp;m at the delivery reservoir, PN16, checked against 136&nbsp;m allowable (the series criterion; design pressures and the surge allowance are defined in EN 805 [8]). The ground rises 30&nbsp;m over the first 300&nbsp;m and stays level at +30&nbsp;m to the end. The load case is a power failure that trips every pump at once, the usual governing event [9] (the alternatives are compared in <a href="surge-scenarios-pump-stations.html">surge scenarios in pump stations</a>).</p>
<div class="tbl-wrap"><table>
<caption>Steady state along the knee profile at 0.70 m&sup3;/s</caption>
<thead><tr><th>Point</th><th class="num">Pipe elevation (m)</th><th class="num">HGL (m)</th><th class="num">Pressure (m)</th><th class="num">Margin to +3.0 m (m)</th></tr></thead>
<tbody>
<tr><td>Pump, 0 m</td><td class="num">0.0</td><td class="num">85.0</td><td class="num">85.0</td><td class="num">82.0</td></tr>
<tr><td>Knee, 300 m</td><td class="num">30.0</td><td class="num">84.0</td><td class="num">54.0</td><td class="num">51.0</td></tr>
<tr><td>Plateau, 600 m</td><td class="num">30.0</td><td class="num">83.0</td><td class="num">53.0</td><td class="num">50.0</td></tr>
<tr><td>Plateau, 4,400 m</td><td class="num">30.0</td><td class="num">70.3</td><td class="num">40.3</td><td class="num">37.3</td></tr>
<tr><td>Delivery reservoir, 12,000 m</td><td class="num">30.0</td><td class="num">44.8</td><td class="num">14.8</td><td class="num">11.8</td></tr>
</tbody></table></div>
<p>The transient numbers come from a method-of-characteristics model with a vapour cavity model, cross-checked with a gas cavity model and an independent second code [1, 10]: 120 reaches of 100&nbsp;m, 150&nbsp;s runs, pumps stopping instantly behind their check valves (the conservative case; see <a href="pump-inertia-flywheel-surge.html">the flywheel article</a>). The vessel has a DN400 differential connection, loss coefficient 2 out and 10 in (see <a href="surge-vessel-differential-orifice.html">the differential orifice</a>), \(n\) = 1.2, and a shell cap set well above the expansion in the model, so that it never binds; the design shell quoted throughout is the largest gas volume / 0.8. The tank is idealised: loss-free connection, constant level, 800&nbsp;m&sup3; available. Each vessel is the smallest steady gas volume, found by bisection, that keeps the whole line at +3.0&nbsp;m.</p>
<div class="callout warn">
  <span class="lbl">Where the model is uncertain, and what that means for design</span>
  Where the pressure reaches vapour the column separates, and the spike when the cavity collapses depends on how the cavity is represented. In this series the gas cavity model [10] puts those peaks between 18&nbsp;% lower and 10&nbsp;% higher than the vapour cavity model, so collapse-governed maxima are quoted as a range across both. Do not design on a collapse peak: protect the downsurge so that no cavity forms. None of these figures is HAMMER output, and a project analysis must be run in HAMMER, or an equivalent code, on the surveyed profile.
</div>

<h2 id="four-options">4 &middot; Worked example: four options on one profile</h2>
<div class="tbl-wrap"><table>
<caption>All pumps trip; minimum criterion +3.0 m; PN16 allowable 136 m</caption>
<thead><tr><th>Option</th><th class="num">Line min (m)</th><th>Where</th><th class="num">Knee min (m)</th><th class="num">Pump-end min (m)</th><th class="num">Line max (m)</th><th class="num">Tank draw (m&sup3;)</th><th class="num">Gas at max (m&sup3;)</th></tr></thead>
<tbody>
<tr><td>No protection</td><td class="num">&minus;9.8</td><td>from the pump</td><td class="num">&minus;9.8</td><td class="num">&minus;9.8</td><td class="num">about 140</td><td class="num">&ndash;</td><td class="num">&ndash;</td></tr>
<tr><td>One-way tank only, 8 m</td><td class="num">&minus;9.8</td><td>from the pump</td><td class="num">+8.0</td><td class="num">&minus;9.8</td><td class="num">160&ndash;170</td><td class="num">27.5</td><td class="num">&ndash;</td></tr>
<tr><td>Vessel alone, 43.1 m&sup3; gas</td><td class="num">+3.0</td><td>300 m, the knee</td><td class="num">+3.0</td><td class="num">+32.7</td><td class="num">85.0</td><td class="num">&ndash;</td><td class="num">83.6</td></tr>
<tr><td>Tank 8 m + vessel 15.9 m&sup3; gas</td><td class="num">+3.0</td><td>4,400 m, the plateau</td><td class="num">+8.0</td><td class="num">+33.8</td><td class="num">85.0</td><td class="num">20.7</td><td class="num">30.2</td></tr>
</tbody></table></div>
<p><strong>No protection.</strong> The line goes to vapour from the pump outwards, and the collapse peak at the pump end is about 140&nbsp;m (139&nbsp;m with the vapour cavity model, 141&nbsp;m with the gas cavity model) &mdash; above 136&nbsp;m either way.</p>
<p><strong>Vessel alone.</strong> 43.1&nbsp;m&sup3; of gas expands to 83.6&nbsp;m&sup3;, so the shell is 83.6 / 0.8 = <strong>104.5&nbsp;m&sup3;</strong>. The minimum lands on the knee and nothing rises above the steady 85.0&nbsp;m. It works; it is simply very large.</p>
<p><strong>Tank and vessel.</strong> With the knee held at +8.0&nbsp;m the vessel needs only 15.9&nbsp;m&sup3; of gas, and its pump-end minimum of +33.8&nbsp;m gives the expansion directly:</p>
<div class="eq">\[ V_{max} = 15.9 \left(\frac{95.3}{33.8 + 10.33}\right)^{1/1.2} = 30.2\ \text{m}^3, \qquad \text{shell} = \frac{30.2}{0.8} = 37.8\ \text{m}^3 \]</div>
<p>That is 1 &minus; 37.8 / 104.5 = <strong>64&nbsp;% less shell</strong>. The water accounting shows why. Alone, the vessel pushes 40.5&nbsp;m&sup3; into the line. In the pair it pushes 14.3&nbsp;m&sup3; (30.2 &minus; 15.9) and the tank supplies 20.7&nbsp;m&sup3; &mdash; 35.0&nbsp;m&sup3; in all, most of it from an open tank 8&nbsp;m above the pipe instead of from compressed gas.</p>
<p><strong>Tank alone.</strong> The knee is held at +8.0&nbsp;m, but the pump end, 300&nbsp;m down the slope behind a closed check valve, still reaches vapour and its collapse peak rises from about 140&nbsp;m to <strong>160&ndash;170&nbsp;m</strong>; the far plateau, beyond 7.4&nbsp;km, separates too. On this profile a one-way tank is never a stand-alone solution.</p>
<div class="callout key">
  <span class="lbl">What the tank buys</span>
  The tank does not replace the vessel. It takes the knee off the vessel's hands, and the vessel's critical point moves out onto the plateau.
</div>

<h2 id="int-profile">5 &middot; Interactive: the profile and the envelopes</h2>
<p>The red minimum HGL must stay above the green line (ground + 3.0&nbsp;m) everywhere; where it lies on the grey dotted line the pipe is at vapour.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Minimum and maximum HGL along the knee profile after a total pump trip</div>
    <div class="fsub">Envelopes from the method-of-characteristics runs described in section 3 (pressure envelopes plus pipe elevation). The maximum line is the vapour cavity model's envelope; where the column separates, the short amber bar at the pump end and the readout give the collapse peak as a range across both cavity models. Readouts cover the whole 12 km whatever the window.</div>
  </div>
  <div class="chart-box"><canvas id="profChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Protection option</label>
      <select id="sScn1">
        <option value="0">No protection</option>
        <option value="1">One-way tank only, 8 m</option>
        <option value="2">Vessel alone, 43.1 m³ gas</option>
        <option value="3" selected>Tank 8 m + vessel 15.9 m³ gas</option>
      </select>
      <div class="hint">Each vessel is the smallest that keeps the whole line at +3.0 m in its own case.</div>
    </div>
    <div class="ctrl">
      <label>Show the first <span id="vKm">6 km</span></label>
      <input type="range" id="sKm" min="1" max="12" value="6" step="1">
      <div class="hint">The knee is at 0.3 km; the plateau critical point with the tank is at 4.4 km.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Line minimum</div><div class="v" id="rMin1">+3.0 <small>m at 4,400 m</small></div></div>
    <div class="cell"><div class="k">Knee, 300 m</div><div class="v" id="rKnee1">+8.0 <small>m</small></div></div>
    <div class="cell"><div class="k">Pump end</div><div class="v" id="rPump1">+33.8 <small>m</small></div></div>
    <div class="cell"><div class="k">Line maximum</div><div class="v" id="rMax1">85.0 <small>m, no upsurge</small></div></div>
    <div class="cell"><div class="k">Tank draw</div><div class="v" id="rTank1">20.7 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Vessel gas max</div><div class="v" id="rGas1">30.2 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Criterion</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rOk1"></span></div></div>
  </div>
</div>
<p class="fig-note">At the default &mdash; the 8&nbsp;m tank with 15.9&nbsp;m&sup3; of vessel gas &mdash; the minimum HGL touches ground + 3.0&nbsp;m at <strong>4,400&nbsp;m</strong> on the plateau, the knee is held at +8.0&nbsp;m, the pump end at +33.8&nbsp;m, and nothing rises above 85.0&nbsp;m. Switch to the vessel alone and the critical point jumps back to the knee. Switch to the tank alone and open the window to 12&nbsp;km: the knee stands at +8.0&nbsp;m, but the red line sits on the vapour line over the first 200&nbsp;m and again beyond 7.4&nbsp;km, and the amber bar at the pump end spans 160&ndash;170&nbsp;m, through the PN16 line.</p>

<h2 id="critical-point">6 &middot; Reading it: the tank moves the critical point</h2>
<p>With the tank in place the knee cannot fall below the tank level, so the vessel's critical point moves out along the plateau to about 4.4&nbsp;km, where the tank has no say. The minimum at 4,400&nbsp;m arrives at 18.7&nbsp;s, just as the reflection from the delivery reservoir reaches it (12,000&nbsp;m out and 7,600&nbsp;m back at 1,050&nbsp;m/s). The 8&nbsp;m tank does not open until 19.3&nbsp;s, and anything it sends needs another 3.9&nbsp;s to cover the 4.1&nbsp;km. Up to 12&nbsp;m the plateau minimum has come and gone before the tank's influence arrives; at 14&nbsp;m the tank opens early enough to just catch the 4,400&nbsp;m node, which is lifted to +3.1&nbsp;m, so the critical point steps out to 4,500&nbsp;m. Either way <strong>the required steady gas is the same 15.9&nbsp;m&sup3; for every tank level from 4 to 14&nbsp;m</strong>. The vessel is now sized for the first wave on the plateau, a far smaller job than holding the knee through the slow swing that follows.</p>
<p>The second lesson is at the pump end: without the vessel, the 300&nbsp;m between the closed pump check valve and the tank becomes a short dead end in which the column still separates, which is why the tank alone makes the collapse there worse (section 4).</p>
<p>The third is that the two devices change each other's duty, so they must be modelled together [9]. The tank moves the vessel's critical point and trims its expansion; the vessel delays the moment the tank opens from 0.4&nbsp;s to 19.3&nbsp;s and cuts its draw from 27.5 to 20.7&nbsp;m&sup3;. Size either one alone and you size it for the wrong event.</p>

<h2 id="int-knee">7 &middot; Interactive: at the knee, second by second</h2>
<p>The envelopes say how low each point went; the time histories say when, and what the tank was doing.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pressure head at the knee, on the plateau and at the pump, with the cumulative tank draw</div>
    <div class="fsub">Time histories from the same runs, at the knee (300 m), on the plateau 300 m past the knee (600 m) and at the pump. Tank draw on the right axis. Minima in the readouts are the envelope values at those points, and the readouts cover the whole 150 s run whatever the window; the tank's opening time comes from the full-resolution run. The series keep the highest and lowest point of each sampling interval, so the collapse spikes are drawn; the axis is clipped at 110 m to keep the slow minima readable, and the pump-end peak beside the chart is quoted from figure 1 as a range across both cavity models. In the unprotected case only the pump trace is clipped: the knee and 600 m traces peak just below, at 108 m.</div>
  </div>
  <div class="chart-box"><canvas id="kneeChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Protection option</label>
      <select id="sScn2">
        <option value="0">No protection</option>
        <option value="1">One-way tank only, 8 m</option>
        <option value="2">Vessel alone, 43.1 m³ gas</option>
        <option value="3" selected>Tank 8 m + vessel 15.9 m³ gas</option>
      </select>
      <div class="hint">Violet dashed line: tank level at the knee (8 m). Shaded violet curve: cumulative draw, right axis.</div>
    </div>
    <div class="ctrl">
      <label>Time window <span id="vWin">150 s</span></label>
      <input type="range" id="sWin" min="10" max="150" value="150" step="5">
      <div class="hint">Close it to 30 s to see the first wave; open it to watch the slow swing.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Knee minimum</div><div class="v" id="rKnee2">+8.0 <small>m</small></div></div>
    <div class="cell"><div class="k">600 m minimum</div><div class="v" id="rLimb2">+7.2 <small>m</small></div></div>
    <div class="cell"><div class="k">Pump-end minimum</div><div class="v" id="rPump2">+33.8 <small>m</small></div></div>
    <div class="cell"><div class="k">Pump-end peak</div><div class="v" id="rPeak2">85.0 <small>m, no upsurge</small></div></div>
    <div class="cell"><div class="k">Tank opens</div><div class="v" id="rOpen2">19.3 <small>s</small></div></div>
    <div class="cell"><div class="k">Tank draw</div><div class="v" id="rDraw2">20.7 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Draw finished by</div><div class="v" id="rDone2">119 <small>s</small></div></div>
  </div>
</div>
<p class="fig-note">At the default the knee sinks from its steady 54.0&nbsp;m, reaches the tank level at about <strong>20&nbsp;s</strong> and stays at +8.0&nbsp;m while the tank feeds; 600&nbsp;m follows it down to +7.2&nbsp;m, and the pump end bottoms at +33.8&nbsp;m as the vessel's gas reaches its largest. The draw climbs to 20.7&nbsp;m&sup3; and is finished by about <strong>118&nbsp;s</strong>. Switch to the vessel alone: nothing stops the knee, which sinks slowly to +3.0&nbsp;m while the pump end falls to +32.7&nbsp;m &mdash; the slow swing the big vessel exists to carry. Switch to the tank alone: it opens within the first second and holds the knee, but the pump end sits at vapour and the tank gives 27.5&nbsp;m&sup3;.</p>

<h2 id="sizing">8 &middot; Sizing the tank and the vessel together</h2>
<p>Repeating the vessel bisection at different tank levels gives the trade-off. The draw is given at 150&nbsp;s and in full, from the same solver run continued to 600&nbsp;s.</p>
<div class="tbl-wrap"><table>
<caption>Vessel sized for +3.0 m along the whole line, with a one-way tank at the knee</caption>
<thead><tr><th>Tank level above pipe</th><th class="num">Vessel gas (m&sup3;)</th><th class="num">Gas at max (m&sup3;)</th><th class="num">Shell (m&sup3;)</th><th class="num">Draw in 150 s (m&sup3;)</th><th class="num">Complete draw (m&sup3;)</th><th>Critical point</th></tr></thead>
<tbody>
<tr><td>No tank</td><td class="num">43.1</td><td class="num">83.6</td><td class="num">104.5</td><td class="num">&ndash;</td><td class="num">&ndash;</td><td>knee, 300 m</td></tr>
<tr><td>4 m</td><td class="num">15.9</td><td class="num">32.3</td><td class="num">40.3</td><td class="num">14.0</td><td class="num">14.0</td><td>4,400 m</td></tr>
<tr><td>8 m</td><td class="num">15.9</td><td class="num">30.2</td><td class="num">37.8</td><td class="num">20.7</td><td class="num">20.7</td><td>4,400 m</td></tr>
<tr><td>12 m</td><td class="num">15.9</td><td class="num">28.3</td><td class="num">35.4</td><td class="num">30.7</td><td class="num">33.5</td><td>4,400 m</td></tr>
<tr><td>14 m</td><td class="num">15.9</td><td class="num">27.5</td><td class="num">34.4</td><td class="num">35.7</td><td class="num">51.7</td><td>4,500 m</td></tr>
<tr><td>16 m</td><td class="num" colspan="6">not valid: above the 14.8 m limit, drains at about 0.12 m&sup3;/s indefinitely</td></tr>
</tbody></table></div>
<p><strong>First, the steady gas does not change</strong> from 4 to 14&nbsp;m, for the reason given in section 6. <strong>Second, a higher tank trims the vessel only a little</strong>: the shell falls from 40.3 to 34.4&nbsp;m&sup3; because, with the knee held higher, the pump end falls less (its minimum rises from +30.5 to +39.1&nbsp;m) and the gas expands less (32.3 to 27.5&nbsp;m&sup3;). <strong>Third, a higher tank gives away much more water</strong>: 14.0 to 35.7&nbsp;m&sup3; in 150&nbsp;s, and the 12&nbsp;m and 14&nbsp;m tanks are still feeding when the run ends. Run on, their draws end at 33.5 and 51.7&nbsp;m&sup3;: a tank 0.8&nbsp;m below the drain limit keeps feeding for several minutes while the line settles towards a rest pressure just above it.</p>
<p>The design consequence is to <strong>keep the tank low</strong>, but high enough above +3.0&nbsp;m to leave room for its connection loss and its own surface falling as it feeds. On this profile 8&nbsp;m does that: 5.0&nbsp;m above the criterion, 6.8&nbsp;m below the drain limit, and a draw complete in about two minutes. That is engineering judgement, not an optimum. Apply the drain limit at the lowest operating level of the delivery reservoir, the lowest rest HGL the tank will see.</p>
<p>The tank is then sized on the complete draw, with a safety factor on the usable volume, a dead depth of water above the outlet so that the end of the draw does not pull a vortex, and a freeboard above top water level. With the top water level at \(h_T\), the outlet must still sit above the pipe:</p>
<div class="eq">\[ V_{usable} = SF \times V_{draw}, \qquad h_{water} = \frac{V_{usable}}{\pi D^2/4} + h_{dead}, \qquad H_{tank} = h_{water} + f_b \]</div>
<div class="eq">\[ z_{outlet} = h_T - h_{water} \;>\; 0, \qquad \Delta h_{surface} = \frac{V_{draw}}{\pi D^2/4} \]</div>

<h2 id="int-sizing">9 &middot; Interactive: sizing the pair</h2>
<p>Choose a tank level to see what it does to the vessel, then size the tank from the equation above.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Vessel gas, vessel shell and tank draw against tank level &mdash; and the tank that follows</div>
    <div class="fsub">Bars from the bisection sizing runs: vessel gas for a +3.0 m minimum along the whole line, shell = gas at maximum expansion / 0.8, tank draw complete (same solver run continued to 600 s). Water depth runs from the outlet, taken at the floor, to top water level; tank height adds the freeboard. Badges are engineering judgement.</div>
  </div>
  <div class="chart-box"><canvas id="sizeChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Tank level above the pipe</label>
      <select id="sLvl">
        <option value="none">No tank (vessel alone)</option>
        <option value="4">4 m</option>
        <option value="8" selected>8 m</option>
        <option value="12">12 m</option>
        <option value="14">14 m</option>
        <option value="16">16 m &mdash; above the 14.8 m limit</option>
      </select>
      <div class="hint">The water surface at rest, measured above the pipe at the knee.</div>
    </div>
    <div class="ctrl">
      <label>Safety factor on the draw <span id="vSF">2.0</span></label>
      <input type="range" id="sSF" min="1" max="3" value="2" step="0.1">
      <div class="hint">Judgement: the modelled tank is idealised, so allow for what it leaves out.</div>
    </div>
    <div class="ctrl">
      <label>Dead water above the outlet <span id="vDead">1.0 m</span></label>
      <input type="range" id="sDead" min="0.3" max="2" value="1" step="0.1">
      <div class="hint">Depth that must remain at the end of the draw; check it against the outlet size.</div>
    </div>
    <div class="ctrl">
      <label>Tank diameter <span id="vDia">5.0 m</span></label>
      <input type="range" id="sDia" min="2" max="12" value="5" step="0.5">
      <div class="hint">A wider tank falls less as it feeds and needs less depth.</div>
    </div>
    <div class="ctrl">
      <label>Freeboard above top water level <span id="vFb">0.5 m</span></label>
      <input type="range" id="sFb" min="0.3" max="1.5" value="0.5" step="0.1">
      <div class="hint">Judgement: room for the overflow and the refill inlet above top water level.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Vessel shell</div><div class="v" id="rShell3">37.8 <small>m&sup3;, &minus;64 %</small></div></div>
    <div class="cell"><div class="k">Complete draw</div><div class="v" id="rDraw3">20.7 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Usable volume</div><div class="v" id="rUse3">41.4 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Water depth</div><div class="v" id="rDepth3">3.11 <small>m</small></div></div>
    <div class="cell"><div class="k">Tank height</div><div class="v" id="rH3">3.61 <small>m</small></div></div>
    <div class="cell"><div class="k">Tank volume, floor to roof</div><div class="v" id="rVol3">70.9 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Outlet above pipe</div><div class="v" id="rOut3">4.89 <small>m</small></div></div>
    <div class="cell"><div class="k">Surface fall in the trip</div><div class="v" id="rFall3">1.05 <small>m</small></div></div>
    <div class="cell"><div class="k">Check</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rOk3"></span></div></div>
  </div>
</div>
<p class="fig-note">At the default 8&nbsp;m tank the vessel shell is <strong>37.8&nbsp;m&sup3;</strong>. With a safety factor of 2.0 on the 20.7&nbsp;m&sup3; draw, 1.0&nbsp;m of dead water, a 5.0&nbsp;m diameter and 0.5&nbsp;m of freeboard, the tank holds 41.4&nbsp;m&sup3; usable in 3.11&nbsp;m of water, stands 3.61&nbsp;m tall (70.9&nbsp;m&sup3;), and its surface falls 1.05&nbsp;m in the trip, so the knee still sees nearly 7&nbsp;m. The outlet sits 4.89&nbsp;m above the pipe: a short elevated tank, or one on higher ground beside the knee. Step through the levels: the steady gas bar does not move, the shell creeps down, the draw grows fast. At 4&nbsp;m the surface ends the trip barely above the criterion; at 14&nbsp;m a 3.0&nbsp;m diameter tank needs more water depth than the level allows, and its outlet drops below the pipe; at 16&nbsp;m the tank simply drains.</p>

<h2 id="details">10 &middot; Tank details: connection, refill, vent, water quality and interlocks</h2>
<h3>The connection and its check valve</h3>
<p>The modelled connection is loss-free; the real one is not. In the paired run the draw peaks at <strong>0.61&nbsp;m&sup3;/s</strong>, and each unit of loss coefficient costs \(v^2/2g\) of the tank's head at that flow: 0.24&nbsp;m in a DN600 connection (2.16&nbsp;m/s), 0.49&nbsp;m in a DN500 (3.11&nbsp;m/s). Take fitting coefficients from a handbook [11] and the valve's from its maker, keep the total small against the margin, and model it. The check valve must open fully on a small differential, close without slamming as the draw stops and the knee climbs back above tank level (in the paired run to no more than about 22&nbsp;m in the ten minutes after the trip), and seal tight against the 54.0&nbsp;m of the running main when the pumps restart [4] (see <a href="check-valve-hammer.html">check valves and water hammer</a>).</p>
<h3>Refill, overflow and vent</h3>
<p>Refill from the main through a small line with a float or altitude valve; refill time is \(t = V_{draw}/q\), so at 2&nbsp;L/s the 20.7&nbsp;m&sup3; draw is replaced in 2.9&nbsp;h, and the tank must be full before the pumps may restart. The overflow must pass the refill line's full-open flow at the highest main pressure (54.0&nbsp;m at the knee while pumping), not just the 2&nbsp;L/s design refill, in case the float valve fails open. The vent must pass the peak draw: the tank breathes in 0.61&nbsp;m&sup3;/s of air, and a throttled vent pulls the air space below atmospheric, lowering the effective tank level by the same amount.</p>
<h3>Water quality</h3>
<p>Between trips the tank holds stagnant drinking water. Design the turnover in &mdash; a small continuous flow through the tank, or a scheduled drain and refill &mdash; with a sampling point for chlorine residual, a cover, screened openings, a lockable hatch, and linings, coatings and valves certified for drinking-water contact [12].</p>
<h3>When the tank is out of service</h3>
<p>The pair is one system. With the tank isolated, the paired vessel in its 37.8&nbsp;m&sup3; shell <strong>empties about 51&nbsp;s after the trip</strong>; the line then separates from the pump end, the first 4.7&nbsp;km reach vapour, and every point but the delivery end falls below +3.0&nbsp;m. An emptied air-over-water vessel would also pass gas into the main, which the model does not represent. A closed isolating valve or an empty tank must therefore stop the pumps from running: in our practice a low-level switch and a limit switch on the isolating valve, interlocked with the pump starters and alarmed on SCADA (see <a href="transient-analysis-scada.html">transient analysis and SCADA</a>).</p>

<h2 id="hammer">11 &middot; Setting it up in Bentley HAMMER</h2>
<p>The general workflow is in <a href="hammer-transient-simulation-workflow.html">the HAMMER transient workflow</a> and <a href="hammer-transient-tips.html">HAMMER transient tips</a>. Field names differ slightly between HAMMER versions, so follow the intent of each step [13].</p>
<ol>
  <li><strong>Draw the real profile:</strong> Pump with its suction Reservoir, Pipes and Junctions, and a Reservoir at the delivery end at its lowest operating level (see <a href="boundary-conditions-reservoir-tank.html">reservoir and tank boundary conditions</a>). Put a node exactly at the knee (the Surge Tank in step 3). Set the Pipe wave speed field, or use the Wave Speed Calculator (see <a href="wave-speed-surge-analysis.html">wave speed</a>).</li>
  <li><strong>Pump:</strong> pump trip (shut down) at the start of the run, inertia of pump and motor, and the check valve on the pump with its closure time. A very small inertia approximates the instant stop used here.</li>
  <li><strong>Surge Tank at the knee:</strong> place a Surge Tank, set as a one-way surge tank with a check valve, as the knee node itself. Enter the tank level (8&nbsp;m above the pipe, an elevation of 38.0&nbsp;m on this profile) and the real tank area, so the surface falls as it feeds, and represent the connection loss as far as your version allows.</li>
  <li><strong>Hydropneumatic Tank at the pump:</strong> initial gas volume 15.9&nbsp;m&sup3;, gas law exponent 1.2, tank volume 37.8&nbsp;m&sup3;, elevation with the initial water level at the pipe at the pump (0.0&nbsp;m here, as the 95.3&nbsp;m absolute gas pressure assumes), inlet orifice diameter 400&nbsp;mm, minor loss coefficient 2 and ratio of losses 5. Bladder option off for an air-over-water vessel (see <a href="surge-vessel-type-selection.html">vessel type selection</a>).</li>
  <li><strong>Steady state:</strong> the Surge Tank must show no flow both while pumping (54.0&nbsp;m in the main against an 8&nbsp;m level) and at rest, with the pumps off and the delivery reservoir at its lowest level.</li>
  <li><strong>Transient run options:</strong> run duration at least 150&nbsp;s, longer if the tank is still feeding at the end; the computed time step and wave speed adjustment tolerance; vapour pressure and column separation on; your friction method.</li>
  <li><strong>One scenario per option:</strong> no protection, tank only, vessel alone, the pair at each tank level, and the pair with the tank isolated.</li>
  <li><strong>Read the results</strong> in the Transient Results Viewer: a profile (path) from pump to delivery reservoir with the maximum and minimum head envelopes against pipe elevation + 3.0&nbsp;m and + 136&nbsp;m; time histories at the knee, the first plateau node and the pump; the Surge Tank's flow and the Hydropneumatic Tank's gas volume.</li>
  <li><strong>Check:</strong> envelopes within +3.0&nbsp;m and 136&nbsp;m everywhere; largest gas volume no more than 0.8 &times; tank volume; the Surge Tank never empties and has stopped feeding before the run ends.</li>
  <li><strong>Iterate:</strong> reduce the initial gas volume until the minimum envelope just meets +3.0&nbsp;m, reset the tank volume to the largest gas volume / 0.8, rerun, and move to the next tank level.</li>
</ol>
<p>Where the unprotected or tank-only runs separate, report their maxima as ranges and never let a design depend on them (see <a href="surge-analysis-risk.html">surge analysis and risk</a>).</p>

<h2 id="checklist">12 &middot; Design checklist</h2>
<ul class="clean">
  <li><strong>Plot pressure, not only HGL,</strong> and read the steady margin to +3.0&nbsp;m wherever a climb turns flat.</li>
  <li><strong>Size the vessel alone first.</strong> If its critical point is a knee, test a one-way tank there before accepting a large vessel.</li>
  <li><strong>Respect the drain limit:</strong> tank level below the lowest rest HGL at the knee, taken at the lowest delivery reservoir level.</li>
  <li><strong>Keep the tank low, with margin</strong> for the connection loss and the surface fall; a higher tank trims the vessel slightly and costs much more water.</li>
  <li><strong>Model tank and vessel together</strong>, resize the vessel with the tank in place, and find the new critical point.</li>
  <li><strong>Never rely on the tank alone</strong> where the pump end can separate.</li>
  <li><strong>Size the tank on the complete draw</strong>, with a safety factor and dead water above the outlet.</li>
  <li><strong>Size connection, check valve and vent for the peak draw</strong>, and put the losses into the model.</li>
  <li><strong>Size the overflow for a float valve failed open</strong> at the highest main pressure, and refill before the pumps may restart.</li>
  <li><strong>Design the water quality in:</strong> turnover, sampling, screened openings, certified materials.</li>
  <li><strong>Interlock the out-of-service case</strong> and model it as a scenario: the paired vessel alone may empty.</li>
  <li><strong>Run the project analysis in HAMMER on the surveyed profile</strong> and quote collapse-governed peaks as ranges.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge protection design series</span>
  <ol>
    <li><a href="wave-speed-surge-analysis.html">Wave speed: the number that sets the surge</a></li>
    <li><a href="surge-vessel-differential-orifice.html">The differential orifice: empty freely, refill slowly</a></li>
    <li><a href="surge-vessel-type-selection.html">Bladder, diaphragm or air-over-water vessel</a></li>
    <li><strong>One-way surge tanks at the knee</strong></li>
    <li><a href="surge-relief-valve-sizing.html">Surge relief valves: what a valve at the pump can protect</a></li>
    <li><a href="pump-inertia-flywheel-surge.html">Pump inertia and the flywheel</a></li>
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
const sg1=v=>{const r=Math.round(v*10)/10;return (r<0?'&minus;':'+')+Math.abs(r).toFixed(1);};
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'IBM Plex Sans',size:11}}};
const TTL=t=>({display:true,text:t,font:{family:'IBM Plex Sans',size:12,weight:'600'}});
const LEG={labels:{font:{family:'IBM Plex Sans',size:11},usePointStyle:true,boxWidth:8}};
const ALBL=(txt,pos,col)=>({display:true,content:txt,position:pos,backgroundColor:'rgba(0,0,0,0)',color:col||'#1b4f72',font:{family:'IBM Plex Sans',size:10}});
const badge=(c,t)=>'<span class="badge '+c+'">'+t+'</span>';
const SC=[D.none,D.tank,D.vessel,D.tank_vessel];
const HAS_TANK=[false,true,false,true], TANK_LEVEL=8, KN=3, LIMB=6;
const X=D.x.map(v=>v/1000);
const ALLOW=136.0, r5=v=>5*Math.round(v/5);
/* collapse-governed peaks: the range across the vapour (DVCM) and gas (DGCM) cavity models,
   rounded to 5 m, or to whole metres where the 136 m allowable falls inside the range */
function peak(s){
  const j=Math.max(0,D.x.indexOf(s.at_max));      // compare like with like: steady PRESSURE at the node that peaks
  if(s.line_max_dgcm==null){
    return fmt1(s.line_max)+' <small>m'+(s.line_max<=D.hgl[j]-D.z[j]+0.05?', no upsurge':'')+'</small>';
  }
  const lo=Math.min(s.line_max,s.line_max_dgcm), hi=Math.max(s.line_max,s.line_max_dgcm);
  const str=lo<ALLOW&&hi>ALLOW;                   // whole metres, so the allowable's place in the range stays visible
  const a=str?Math.round(lo):r5(lo), b=str?Math.round(hi):r5(hi);
  return (a===b?'about '+fmt0(a):fmt0(a)+'&ndash;'+fmt0(b))+' <small>m</small>';
}

/* ---------- CHART 1 : profile and envelopes ---------- */
const sScn1=document.getElementById('sScn1'), sKm=document.getElementById('sKm');
const CAV=SC.map(s=>s.line_max_dgcm!=null);        // options whose column separates
const LEGF={labels:{...LEG.labels,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}};
let c1=new Chart(document.getElementById('profChart'),{
  type:'line',
  data:{datasets:[
    {label:'Ground (pipe)',data:[],borderColor:'#7f8c8d',backgroundColor:'rgba(127,140,141,0.14)',borderWidth:2,pointRadius:0,fill:'start',order:7},
    {label:'Steady HGL',data:[],borderColor:'#1b4f72',borderDash:[6,4],borderWidth:2,pointRadius:0,order:5},
    {label:'Maximum HGL (vapour cavity)',data:[],borderColor:'#b9770e',borderWidth:2.4,pointRadius:0,order:3},
    {label:'Minimum HGL',data:[],borderColor:'#c0392b',borderWidth:2.8,pointRadius:0,order:2},
    {label:'Ground + 3.0 m',data:[],borderColor:'#1e8449',borderDash:[4,3],borderWidth:1.6,pointRadius:0,order:4},
    {label:'Vapour (ground − 9.8 m)',data:[],borderColor:'#7f8c8d',borderDash:[2,3],borderWidth:1.2,pointRadius:0,order:6},
    {label:'PN16 (ground + 136 m)',data:[],borderColor:'#c0392b',borderDash:[8,4],borderWidth:1.2,pointRadius:0,order:8},
    {type:'scatter',label:'Tank water surface',data:[],backgroundColor:'#6b4f9e',borderColor:'#fff',borderWidth:2,pointRadius:7,pointStyle:'rectRot',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'nearest',intersect:false},
    scales:{x:{type:'linear',min:0,max:6,title:TTL('Chainage (km)'),...AX},
            y:{type:'linear',title:TTL('Elevation and head (m)'),...AX}},
    plugins:{legend:LEGF,
      tooltip:{callbacks:{label:c=>{
        const i=c.dataIndex;
        if(c.datasetIndex===2&&CAV[+sScn1.value]&&c.parsed.y>D.hgl[i]+0.05)
          return `Maximum HGL: about ${fmt0(Math.round(c.parsed.y/5)*5)} m (collapse peak, model-dependent; see readout)`;
        return `${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt2(c.parsed.x)} km`;
      }}},
      annotation:{annotations:{
        knee:{type:'line',xMin:0.3,xMax:0.3,borderColor:'#6b4f9e',borderWidth:1,borderDash:[3,3],label:ALBL('knee','start','#6b4f9e')},
        rng:{type:'box',xMin:0,xMax:0.1,yMin:0,yMax:0,display:false,backgroundColor:'#b9770e',borderWidth:0}
      }}}}
});
function updProf(){
  const k=+sScn1.value, s=SC[k], km=+sKm.value;
  document.getElementById('vKm').textContent=km+' km';
  const idx=D.x.map((_,i)=>i).filter(i=>X[i]<=km+1e-9);
  const mk=f=>idx.map(i=>({x:X[i],y:+f(i).toFixed(2)}));
  const hi=Math.max(s.line_max,s.line_max_dgcm==null?0:s.line_max_dgcm);
  c1.data.datasets[0].data=mk(i=>D.z[i]);
  c1.data.datasets[1].data=mk(i=>D.hgl[i]);
  c1.data.datasets[2].data=mk(i=>D.z[i]+s.Hmax[i]);
  c1.data.datasets[3].data=mk(i=>D.z[i]+s.Hmin[i]);
  c1.data.datasets[4].data=mk(i=>D.z[i]+3.0);
  c1.data.datasets[5].data=mk(i=>D.z[i]-9.8);
  c1.data.datasets[6].data=hi>ALLOW?mk(i=>D.z[i]+ALLOW):[];
  c1.data.datasets[7].data=HAS_TANK[k]?[{x:D.knee_x/1000,y:D.knee_z+TANK_LEVEL}]:[];
  const rng=c1.options.plugins.annotation.annotations.rng;   // collapse peak at the pump end, both cavity models
  rng.display=CAV[k];
  if(CAV[k]){rng.xMin=0;rng.xMax=km*0.015;rng.yMin=D.z[0]+Math.min(s.line_max,s.line_max_dgcm);rng.yMax=D.z[0]+hi;}
  c1.options.scales.x.max=km;
  c1.update('none');
  document.getElementById('rMin1').innerHTML=sg1(s.line_min)+' <small>m '+(s.at_min===0?'from the pump':'at '+fmt0(s.at_min)+' m')+'</small>';
  document.getElementById('rKnee1').innerHTML=sg1(s.knee_min)+' <small>m</small>';
  document.getElementById('rPump1').innerHTML=sg1(s.pump_min)+' <small>m</small>';
  document.getElementById('rMax1').innerHTML=peak(s);
  document.getElementById('rTank1').innerHTML=s.used==null?'&ndash;':fmt1(s.used)+' <small>m³</small>';
  document.getElementById('rGas1').innerHTML=s.gas_max==null?'&ndash;':fmt1(s.gas_max)+' <small>m³</small>';
  let b;
  if(s.line_min<=-9.79) b=badge('bad','vapour: column separation');
  else if(s.line_min<2.95) b=badge('warn','below +3.0 m');
  else if(hi>ALLOW) b=badge('warn','above the 136 m allowable');
  else b=badge('good','meets +3.0 m and PN16');
  document.getElementById('rOk1').innerHTML=b;
}
[sScn1,sKm].forEach(el=>el.addEventListener('input',updProf));updProf();

/* ---------- CHART 2 : at the knee, second by second ---------- */
const sScn2=document.getElementById('sScn2'), sWin=document.getElementById('sWin');
const YCLIP=110;                                   // a sampled trace above this is cut; the collapse peaks come from figure 1
let c2=new Chart(document.getElementById('kneeChart'),{
  type:'line',
  data:{datasets:[
    {label:'Knee (300 m)',data:[],borderColor:'#1b4f72',borderWidth:2.6,pointRadius:0,yAxisID:'y',order:1},
    {label:'Plateau (600 m)',data:[],borderColor:'#b9770e',borderWidth:2,pointRadius:0,yAxisID:'y',order:2},
    {label:'Pump end',data:[],borderColor:'#7f8c8d',borderWidth:2,pointRadius:0,yAxisID:'y',order:3},
    {label:'Tank draw (right axis)',data:[],borderColor:'#6b4f9e',backgroundColor:'rgba(107,79,158,0.12)',borderWidth:2,pointRadius:0,fill:'origin',yAxisID:'y1',order:4}
  ]},
  options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'nearest',intersect:false},
    scales:{x:{type:'linear',min:0,max:150,title:TTL('Time after the trip (s)'),...AX},
            y:{type:'linear',position:'left',title:TTL('Pressure head (m)'),...AX},
            y1:{type:'linear',position:'right',min:0,title:TTL('Tank draw (m³)'),grid:{drawOnChartArea:false},ticks:{font:{family:'IBM Plex Sans',size:11}}}},
    plugins:{legend:LEGF,
      tooltip:{callbacks:{label:c=>{
        if(c.dataset.yAxisID==='y1') return `Tank draw: ${fmt1(c.parsed.y)} m³`;
        return CAV[+sScn2.value]?`${c.dataset.label}: ${fmt0(c.parsed.y)} m (sampled)`:`${c.dataset.label}: ${fmt1(c.parsed.y)} m`;
      }}},
      annotation:{annotations:{
        crit:{type:'line',yScaleID:'y',yMin:3,yMax:3,borderColor:'#1e8449',borderWidth:1.5,borderDash:[5,4],label:{...ALBL('+3.0 m criterion','start','#1e8449'),yAdjust:9}},
        vap:{type:'line',yScaleID:'y',yMin:-9.8,yMax:-9.8,borderColor:'#7f8c8d',borderWidth:1,borderDash:[2,3],label:ALBL('vapour −9.8 m','end','#7f8c8d')},
        lvl:{type:'line',yScaleID:'y',yMin:8,yMax:8,display:true,borderColor:'#6b4f9e',borderWidth:1.2,borderDash:[6,3],label:{...ALBL('tank level 8 m','start','#6b4f9e'),yAdjust:-9}}
      }}}}
});
function updKnee(){
  const k=+sScn2.value, s=SC[k], w=+sWin.value;
  document.getElementById('vWin').textContent=w+' s';
  const idx=s.t.map((_,i)=>i).filter(i=>s.t[i]<=w+1e-9);
  const ser=a=>idx.map(i=>({x:s.t[i],y:a[i]}));
  c2.data.datasets[0].data=ser(s.knee);
  c2.data.datasets[1].data=ser(s.limb);
  c2.data.datasets[2].data=ser(s.pump);
  c2.data.datasets[3].data=s.feed?ser(s.feed):[];
  c2.options.scales.x.max=w;
  const clip=Math.max(...idx.map(i=>Math.max(s.knee[i],s.limb[i],s.pump[i])))>YCLIP;   // clip only what really runs off the top
  c2.options.scales.y.max=clip?YCLIP:undefined;
  c2.options.scales.y.title.text=clip?'Pressure head (m), clipped at '+YCLIP+' m':'Pressure head (m)';
  c2.options.scales.y1.display=HAS_TANK[k];
  c2.options.plugins.annotation.annotations.lvl.display=HAS_TANK[k];
  c2.update('none');
  document.getElementById('rKnee2').innerHTML=sg1(s.Hmin[KN])+' <small>m</small>';
  document.getElementById('rLimb2').innerHTML=sg1(s.Hmin[LIMB])+' <small>m</small>';
  document.getElementById('rPump2').innerHTML=sg1(s.Hmin[0])+' <small>m</small>';
  document.getElementById('rPeak2').innerHTML=peak(s);
  if(s.feed){
    const f=s.feed, last=f[f.length-1];
    const i1=f.findIndex(v=>v>=last-0.005);
    /* the first-supply time comes from the full-resolution run (t_open), not from the sampled series */
    const i0=f.findIndex(v=>v>0);
    const t0=(s.t_open!=null)?s.t_open:(i0<0?null:s.t[i0]);
    document.getElementById('rOpen2').innerHTML=t0==null?'&ndash;':(t0<1?fmt1(t0)+' <small>s</small>':fmt1(t0)+' <small>s</small>');
    document.getElementById('rDraw2').innerHTML=fmt1(last)+' <small>m³</small>';
    document.getElementById('rDone2').innerHTML=i1<0?'&ndash;':fmt0(s.t[i1])+' <small>s</small>';
  }else{
    ['rOpen2','rDraw2','rDone2'].forEach(id=>{document.getElementById(id).innerHTML='&ndash;';});
  }
}
[sScn2,sWin].forEach(el=>el.addEventListener('input',updKnee));updKnee();

/* ---------- CHART 3 : sizing the pair ---------- */
const sLvl=document.getElementById('sLvl'), sSF=document.getElementById('sSF'),
      sDead=document.getElementById('sDead'), sDia=document.getElementById('sDia'), sFb=document.getElementById('sFb');
const SZ=D.sizing;                               // none, 4, 8, 12, 14 m
const FINAL=[null,14.0,20.7,33.5,51.7];          // complete draw, m3: same solver run continued to 600 s
const LVL_IDX={'none':0,'4':1,'8':2,'12':3,'14':4};
const R_DRAIN=(D.hgl[KN]-D.delivery_hgl)/(0.70*0.70);   // s2/m5, friction below the knee
let SEL=2;
let c3=new Chart(document.getElementById('sizeChart'),{
  type:'bar',
  data:{labels:['No tank','Tank 4 m','Tank 8 m','Tank 12 m','Tank 14 m'],
    datasets:[
      {label:'Vessel gas, steady',data:SZ.map(r=>r.gas),backgroundColor:'#1b4f72',borderWidth:0},
      {label:'Vessel gas at maximum',data:SZ.map(r=>r.gas_max),backgroundColor:'#b9770e',borderWidth:0},
      {label:'Vessel shell',data:SZ.map(r=>r.total),backgroundColor:'#7f8c8d',borderWidth:0},
      {label:'Tank draw, complete',data:FINAL.map(v=>v==null?0:v),backgroundColor:'#6b4f9e',borderWidth:0}
    ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,ticks:{font:ctx=>({family:'IBM Plex Sans',size:11,weight:(ctx.index===SEL?'700':'400')})}},
            y:{type:'linear',min:0,title:TTL('Volume (m³)'),...AX}},
    plugins:{legend:LEG,
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m³`}},
      annotation:{annotations:{
        sel:{type:'box',xMin:1.5,xMax:2.5,backgroundColor:'#a9cce3',borderWidth:0,drawTime:'beforeDatasetsDraw'}
      }}}}
});
function updSize(){
  const v=sLvl.value, sf=+sSF.value, hd=+sDead.value, Dm=+sDia.value, fb=+sFb.value;
  document.getElementById('vSF').textContent=fmt1(sf);
  document.getElementById('vDead').textContent=fmt1(hd)+' m';
  document.getElementById('vDia').textContent=fmt1(Dm)+' m';
  document.getElementById('vFb').textContent=fmt1(fb)+' m';
  const sel=(v in LVL_IDX)?LVL_IDX[v]:-1;
  SEL=sel;
  const box=c3.options.plugins.annotation.annotations.sel;   // selected tank level: shaded band + bold label
  box.display=sel>=0; box.xMin=sel-0.5; box.xMax=sel+0.5;
  c3.update('none');
  const out=(id,h)=>{document.getElementById(id).innerHTML=h;};
  const TANK=['rUse3','rDepth3','rH3','rVol3','rOut3','rFall3'];
  if(sel<0){                                    // above the drain limit
    const lvl=+v, q=Math.sqrt(Math.max(0,D.knee_z+lvl-D.delivery_hgl)/R_DRAIN);
    out('rShell3','&ndash;'); out('rDraw3','&ndash;');
    TANK.forEach(id=>out(id,'&ndash;'));
    out('rOk3',badge('bad','above '+fmt1(D.max_valid_level)+' m: drains at about '+fmt2(q)+' m³/s'));
    return;
  }
  const r=SZ[sel], alone=SZ[0].total;
  out('rShell3',fmt1(r.total)+' <small>m³'+(sel>0?', &minus;'+fmt0(100*(1-r.total/alone))+' %':'')+'</small>');
  if(sel===0){
    ['rDraw3',...TANK].forEach(id=>out(id,'&ndash;'));
    out('rOk3',badge('warn','no tank: the vessel holds the knee'));
    return;
  }
  const lvl=+v, dr=FINAL[sel], A=Math.PI*Dm*Dm/4;
  const use=dr*sf, depth=use/A+hd, ht=depth+fb, vol=A*ht, fall=dr/A, endL=lvl-fall, zo=lvl-depth;
  out('rDraw3',fmt1(dr)+' <small>m³</small>');
  out('rUse3',fmt1(use)+' <small>m³</small>');
  out('rDepth3',fmt2(depth)+' <small>m</small>');
  out('rH3',fmt2(ht)+' <small>m</small>');
  out('rVol3',fmt1(vol)+' <small>m³</small>');
  out('rOut3',(zo<0?'&minus;':'')+fmt2(Math.abs(zo))+' <small>m</small>');
  out('rFall3',fmt2(fall)+' <small>m</small>');
  let b;
  if(lvl>=D.max_valid_level) b=badge('bad','above the drain limit');
  else if(endL<3.0) b=badge('bad','surface falls below +3.0 m');
  else if(zo<=0) b=badge('warn','outlet below the pipe: widen the tank');
  else if(lvl>=12) b=badge('warn','near the drain limit: long draw');
  else if(endL-3.0<2.0) b=badge('warn','thin margin above +3.0 m');
  else b=badge('good','shut at rest, margin kept');
  out('rOk3',b);
}
[sLvl,sSF,sDead,sDia,sFb].forEach(el=>el.addEventListener('input',updSize));updSize();

window.addEventListener('load',function(){try{c1.resize();c2.resize();c3.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993 — Joukowsky head, method of characteristics, interior boundary conditions and the discrete vapour cavity model.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014 — boundary conditions for surge tanks and air chambers, and polytropic gas behaviour.</li>
  <li>Stephenson, D. &ldquo;Simple guide for design of air vessels for water hammer protection of pumping lines.&rdquo; <em>Journal of Hydraulic Engineering</em> (ASCE), 128(8), 2002 — air vessel gas volumes, expansion and the water a vessel must supply.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004 — surge-control devices including feed tanks, and the dynamic behaviour of check valves.</li>
  <li>Stephenson, D. <em>Pipeline Design for Water Engineers</em>, 3rd ed. Elsevier, 1989 — water hammer protection of pumping lines, including discharge tanks.</li>
  <li>AWWA M51 <em>Air Valves: Air-Release, Air/Vacuum, and Combination</em> — the role and limits of air valves at high points and changes of grade.</li>
  <li>ISO 2531 <em>Ductile iron pipes, fittings, accessories and their joints for water applications</em> — the DN800 K9 pipe of the reference main.</li>
  <li>EN 805 <em>Water supply — Requirements for systems and components outside buildings</em> — design pressures, maximum design pressure and surge allowance.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005 — power failure as the governing event, selection of protection devices and analysing them as one system.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006 — vapour and gas cavity models and why collapse pressures differ between them.</li>
  <li>Idelchik, I.E. <em>Handbook of Hydraulic Resistance</em>, 3rd ed. Begell House, 1996 — loss coefficients for the tank outlet, tee and bends of the tank connection.</li>
  <li>NSF/ANSI/CAN 61 <em>Drinking Water System Components — Health Effects</em> — certification of linings, coatings and valves in contact with drinking water.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> product documentation and help — Surge Tank, Hydropneumatic Tank, pump trip, transient run options and the Transient Results Viewer.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #HydraulicTransients #OneWaySurgeTank #FeedTank #SurgeTank #SurgeVessel #HydropneumaticTank #AirVessel #PumpTrip #PowerFailure #ColumnSeparation #Downsurge #PipelineProfile #TransmissionMains #DuctileIron #MethodOfCharacteristics #BentleyHAMMER #OpenFlowsHAMMER #CheckValve #SurgeProtection #PumpStationDesign #PipelineDesign #TransientModelling #HydraulicDesign #WaterSupply #WaterEngineering</div>
"""

import json, os
_D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'datasets.json')))
_F = _D['feedtank']
_KEEP = ('label', 'Hmin', 'Hmax', 'line_min', 'knee_min', 'pump_min', 'line_max', 'line_max_dgcm',
         'at_min', 'at_max', 'used', 'gas_max', 't', 'knee', 'limb', 'pump', 'feed', 't_open')
DATA = {k: _F[k] for k in ('knee_x', 'knee_z', 'delivery_hgl', 'max_valid_level', 'x', 'z', 'hgl', 'sizing')}
for _k in ('none', 'tank', 'vessel', 'tank_vessel'):
    DATA[_k] = {f: _F[_k].get(f) for f in _KEEP}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='one-way-surge-tank-design', cat='surge', mins=33,
    date_iso='2026-09-16', date_human='September 2026', date_ar='سبتمبر 2026',
    title='One-Way Surge Tanks at the Knee: Cutting the Surge Vessel by Nearly Two-Thirds',
    reg_title='One-Way Surge Tanks at the Knee: Cutting the Surge Vessel by Nearly Two-Thirds',
    reg_tag='Surge Analysis · One-Way Surge Tank · Pipeline Profile',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; One-Way Surge Tank &middot; Pipeline Profile',
    desc='How a one-way surge tank at the knee of a rising pumping main shrinks the surge vessel at the pump: the physics, a worked 12 km DN800 example with four protection options, sizing tank and vessel together, the drain limit on tank level, tank details and the Bentley HAMMER set-up, with three interactive charts.',
    og_desc='On a 12 km DN800 main that climbs 30 m to a knee, a surge vessel alone needs a 104.5 m³ shell. An 8 m one-way tank at the knee moves the critical point onto the plateau and cuts the shell to 37.8 m³, 64 % smaller.',
    ld_desc='Design of one-way surge tanks at the knee of a pumping main: tank and vessel sized together, the drain limit on tank level, tank volume, connection, refill and vent, and the Bentley HAMMER set-up.',
    img_alt='Technical illustration on a dark navy background: a cutaway feed tank, partly filled by a refill line at the top, joined through a check valve to a pipeline climbing towards a crest, with a cyan HGL, labels for feed tank, check valve, refill line and crest, and an inset chart of the downsurge envelope along the pipeline',
    en_tag='Surge &amp; Transient Analysis &middot; One-Way Surge Tanks',
    en_title='One-Way Surge Tanks at the Knee: Cutting the Surge Vessel by Nearly Two-Thirds',
    en_excerpt='On a main that climbs and then runs level, the weak point after a pump trip is the knee where the climb turns flat. On a 12 km DN800 example, a surge vessel that holds the knee on its own needs <strong>43.1 m³ of gas in a 104.5 m³ shell</strong>. A low one-way tank at the knee, 8 m above the pipe behind a check valve, moves the vessel&rsquo;s critical point onto the plateau and cuts the shell to <strong>37.8 m³ (&minus;64 %)</strong> for <strong>20.7 m³</strong> of tank water. The drain limit on tank level, why the tank must never work alone, tank sizing and the HAMMER set-up &mdash; with three interactive charts.',
    en_search='one-way surge tank feed tank discharge tank knee rising main pipeline profile high point surge vessel hydropneumatic tank air vessel air chamber size reduction gas volume shell volume pump trip power failure downsurge column separation vapour cavity collapse DVCM DGCM method of characteristics minimum pressure criterion critical point plateau tank level drain limit delivery reservoir rest HGL tank draw volume check valve refill line float valve altitude valve vent overflow water quality turnover interlock Bentley HAMMER OpenFlows Surge Tank Hydropneumatic Tank transient envelopes DN800 ductile iron PN16 surge protection design',
    ar_title='خزانات التغذية أحادية الاتجاه عند نقطة تغيّر الميل: تقليص خزان الحماية من الطرق المائي بنحو الثلثين',
    ar_excerpt='على خط يصعد من محطة الضخ ثم يستوي، لا تكون المضخة أضعف نقطة بعد انقطاع الكهرباء، بل نقطة تغيّر الميل حيث يتحول الصعود إلى امتداد أفقي. على خط مرجعي بطول ١٢ كم وقطر DN800 يحتاج خزان الحماية الهيدروهوائي وحده إلى <strong>٤٣٫١ م³ من الغاز بسعة كلية ١٠٤٫٥ م³</strong>. ويؤدي خزان أحادي الاتجاه منخفض عند نقطة تغيّر الميل، منسوبه ٨ م فوق الأنبوب، إلى تقليص خزان الحماية إلى <strong>٣٧٫٨ م³ (أقل بنسبة ٦٤٪)</strong> مقابل <strong>٢٠٫٧ م³</strong> من الماء يمنحها الخزان. ويُشرح الحد الأعلى لمنسوب الخزان (١٤٫٨ م) حتى لا يُفرَّغ في خزان الاستلام، وخطوات الإعداد في HAMMER، مع ثلاثة رسوم تفاعلية.',
    ar_search='خزان أحادي الاتجاه خزان تغذية أحادي الاتجاه نقطة تغير الميل خط ضخ صاعد مقطع طولي خزان الحماية من الطرق المائي خزان الحماية الهيدروهوائي خزان الضغط الهوائي خزان الموازنة حجم الغاز توقف المضخات انقطاع الكهرباء الانخفاض المفاجئ للضغط انفصال العمود المائي التكهف طريقة الخطوط المميزة الحد الأدنى للضغط منسوب الخزان حد التصريف خزان الاستلام صمام عدم الرجوع خط إعادة التعبئة صمام عوامة فتحة التهوية الفائض جودة المياه برنامج HAMMER المطرقة المائية الطرق المائي تحليل المطرقة المائية حديد الدكتايل',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
