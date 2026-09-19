# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A surge relief valve at the pump discharge is the cheapest-looking answer to a pump-trip upsurge, and on the 12&nbsp;km DN800 reference main it caps its own connection well. Set at 95&nbsp;m &mdash; lower than a station could hold in service, so a best case &mdash; it holds the pump end at <strong>96.3&nbsp;m</strong> where the unprotected line reaches 165&ndash;190&nbsp;m. Everywhere else, the main still falls to vapour pressure from end to end, and the peak along the line remains <strong>127&ndash;143&nbsp;m</strong> depending on how the cavity is modelled &mdash; straddling the 136&nbsp;m PN16 allowable. On a line that separates, the valve belongs behind the real protection, not in front of it.</p>

<h2 id="purpose">1 &middot; What a relief valve is for</h2>
<p>A surge relief valve (SRV) is a normally closed valve that opens when the pressure at its connection exceeds a set point, and discharges to atmosphere or a sump. It acts on <strong>high pressure only</strong>, so it cannot put water into a line whose pressure is falling, and <strong>at its own connection only</strong>, reaching the rest of the line only through the waves that node sends out [1, 2].</p>
<p>A <a href="surge-vessel.html">hydropneumatic vessel</a> feeds the downsurge and absorbs the upsurge; a <a href="pump-inertia-flywheel-surge.html">flywheel</a> keeps the column moving; a <a href="one-way-surge-tank-design.html">one-way surge tank</a> feeds a high point. The relief valve is only a pressure cap, so the design question is not whether it can cap the pump end but <strong>where the pressures that exceed the pipe rating are generated</strong> [3]. On a line that separates, most of those places are far from the pump.</p>

<h2 id="mechanism">2 &middot; Where the upsurge on a pump trip comes from</h2>
<p>Every head change in a transient is tied to a flow change by the Joukowsky relation, with the pipe&rsquo;s characteristic impedance \(B\):</p>
<div class="eq">\[ \Delta H \;=\; \frac{a}{g\,A}\,\Delta Q \;=\; B\,\Delta Q, \qquad B \;=\; \frac{1050}{9.81 \times 0.5027} \;=\; 212.9\ \text{s/m}^2 \]</div>
<p>On the reference main &mdash; 12&nbsp;km of DN800 ductile iron K9 to ISO 2531 [4], wave speed 1,050&nbsp;m/s, 0.70&nbsp;m&sup3;/s at 1.39&nbsp;m/s, flat profile &mdash; stopping the full flow is worth \(B \times 0.70\) = 149.1&nbsp;m, but only 85.0 + 9.8 = 94.8&nbsp;m is available above vapour at the pump. When every pump trips, the pump end drops straight to &minus;9.8&nbsp;m and the whole line is at vapour within 11.4&nbsp;s. Then, in the vapour cavity model:</p>
<ul class="clean">
  <li><strong>0&ndash;25&nbsp;s.</strong> A large cavity opens at the pump and small ones along the line; the small ones close as the reflection returns from the <a href="boundary-conditions-reservoir-tank.html">delivery reservoir</a>.</li>
  <li><strong>47&nbsp;s.</strong> The column, running back at about 0.50&nbsp;m&sup3;/s, closes the pump cavity against the shut check valve: \(B \times 0.50\) lifts the pump end from &minus;9.8&nbsp;m to about 97&nbsp;m in one step.</li>
  <li><strong>47&ndash;58&nbsp;s.</strong> That front runs down the line and stops about 0.47&nbsp;m&sup3;/s of the flow coming back out of the reservoir, adding about 100&nbsp;m to the 44.8&nbsp;m already there. <strong>The far-end peak is generated 11&ndash;12&nbsp;km from the pump.</strong></li>
  <li><strong>47&ndash;68&nbsp;s.</strong> Later waves keep arriving at the pump, and its head climbs steadily to about 142&nbsp;m &mdash; the climb that opens a 110&nbsp;m valve at about 49&nbsp;s and a 120&nbsp;m valve at about 54&nbsp;s.</li>
  <li><strong>69&nbsp;s.</strong> Reflections reach the closed check valve, which doubles them [5]: the unprotected pump-end peak of 165&ndash;190&nbsp;m.</li>
</ul>
<h3>Why collapse peaks are quoted as ranges</h3>
<p>The results come from a method-of-characteristics model with a vapour cavity model, cross-checked with a gas cavity model and an independent second code (120 reaches, 150&nbsp;s runs). They are not HAMMER output; a project analysis must be run in HAMMER, or an equivalent package, on the real profile. Maxima that follow a collapse are quoted as a range across the two models, because the spike depends on how the cavity is represented: one closes a concentrated cavity in an instant, the other cushions the closure with a trace of free gas [1, 6]. Here the gas cavity model gives line maxima 10&ndash;13&nbsp;% lower, an undersized valve&rsquo;s pump-end peak about a fifth lower, and peak relief flows 33&ndash;44&nbsp;% lower at the three settings modelled &mdash; though only about a tenth lower for that undersized valve. A finer grid does not close the gap: at 95&nbsp;m the line maximum moves by less than 1&nbsp;m between 60 and 240 reaches, against about 17&nbsp;m between the two models.</p>

<h2 id="model">3 &middot; Worked example: one valve, four settings</h2>
<p>The valve is a spring-loaded relief valve on the pump discharge header, downstream of the check valves, discharging to atmosphere. It opens in proportion to the head above its set point and reaches full lift at an overpressure of 4&nbsp;m. The discharge law, the usual form of a valve boundary in a characteristics model [7], is</p>
<div class="eq">\[ Q_r \;=\; C_d\,A\;\min\!\left(1,\;\frac{h - H_s}{\Delta h_{op}}\right)\sqrt{2 g h}, \qquad h > H_s \]</div>
<p>with \(h\) the head at the valve, \(H_s\) the set head, \(\Delta h_{op}\) = 4&nbsp;m and \(C_d A\) for DN250 at \(C_d\) = 0.6. Three idealisations matter, and a project model must replace each: <strong>all pumps stop instantly</strong> behind an ideal check valve, with no rundown (the bounding case for the downsurge; a real rundown changes when and how hard the column returns); <strong>the valve has no dynamics</strong> &mdash; no opening delay, closing time or blowdown (section 9); and the nominal bore is taken as the flow area.</p>
<p>Three settings are modelled: 120&nbsp;m, 110&nbsp;m and 95&nbsp;m. Read 95&nbsp;m, only 10&nbsp;m above the steady head, as the best case for the valve rather than a usable setting: it is below the shut-off head of the series&rsquo; model pump, so the valve would open in service (section 9).</p>
<div class="tbl-wrap"><table>
  <caption>DN250 relief valve at the pump, all pumps tripped. Results without collapse to 0.1&nbsp;m; collapse-driven maxima as a range across the vapour and gas cavity models.</caption>
  <thead><tr><th>Set head</th><th class="num">Pump-end max, vapour / gas model (m)</th><th class="num">Line max (m)</th><th class="num">Length above 136&nbsp;m, vapour / gas (km)</th><th class="num">Line min (m)</th><th class="num">Peak relief flow, vapour / gas (m&sup3;/s)</th></tr></thead>
  <tbody>
    <tr><td>No valve</td><td class="num">165&ndash;190 (collapse range)</td><td class="num">165&ndash;190</td><td class="num">12.0 / 11.0</td><td class="num">&minus;9.8</td><td class="num">&ndash;</td></tr>
    <tr><td>120&nbsp;m</td><td class="num">120.9 / 120.5</td><td class="num">140&ndash;155</td><td class="num">11.9 / 3.9</td><td class="num">&minus;9.8</td><td class="num">0.319 / 0.179</td></tr>
    <tr><td>110&nbsp;m</td><td class="num">111.0 / 110.6</td><td class="num">133&ndash;151</td><td class="num">10.0 / 0</td><td class="num">&minus;9.8</td><td class="num">0.359 / 0.220</td></tr>
    <tr><td>95&nbsp;m (best case)</td><td class="num">96.3 / 95.9</td><td class="num">127&ndash;143</td><td class="num">1.6 / 0</td><td class="num">&minus;9.8</td><td class="num">0.416 / 0.280</td></tr>
  </tbody>
</table></div>
<p>The valve does its own job in every case, holding the pump end within 1.3&nbsp;m of the set point. It does nothing for the minimum, &minus;9.8&nbsp;m throughout. The line maximum falls with the set point but never clearly below 136&nbsp;m: over it under both models at 120&nbsp;m, model-dependent at 110&nbsp;m and 95&nbsp;m. The peak relief flow at 95&nbsp;m, 0.416&nbsp;m&sup3;/s in the vapour cavity model, is <strong>59&nbsp;% of the pumped flow</strong>.</p>

<h2 id="int-pump">4 &middot; Interactive: the pump end, second by second</h2>
<p>Pick a setting and watch the head at the valve; the faint trace is the same trip with no valve.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pressure head at the pump discharge after all pumps trip</div>
    <div class="fsub">Vapour cavity model time history; instant stop of all pumps; DN250 relief valve, C<sub>d</sub> 0.6, full lift at set + 4 m, no opening delay. The line maximum readout spans both cavity models; the line minimum is the lowest head anywhere on the main.</div>
  </div>
  <div class="chart-box"><canvas id="pumpChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Relief valve setting <span id="v1">set 95 m</span></label>
      <select id="s1">
        <option value="0">No valve</option>
        <option value="1">Set 120 m</option>
        <option value="2">Set 110 m</option>
        <option value="3" selected>Set 95 m (best case)</option>
      </select>
      <div class="hint">Steady head at the pump 85.0 m; PN16 allowable 136 m.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Pump-end max</div><div class="v" id="rP1">96.3 <small>m (gas model 95.9)</small></div></div>
    <div class="cell"><div class="k">Line max, two models</div><div class="v" id="rL1">127&ndash;143 <small>m</small></div><div id="bL1" style="margin-top:6px;"><span class="badge warn">depends on the cavity model</span></div></div>
    <div class="cell"><div class="k">Line min</div><div class="v" id="rM1">&minus;9.8 <small>m</small></div><div id="bM1" style="margin-top:6px;"><span class="badge bad">vapour: column separation</span></div></div>
    <div class="cell"><div class="k">Peak relief flow</div><div class="v" id="rQ1">0.416 <small>m&sup3;/s (gas model 0.280)</small></div></div>
    <div class="cell"><div class="k">Valve first opens</div><div class="v" id="rO1">47 <small>s</small></div></div>
  </div>
</div>
<p class="fig-note">At 95&nbsp;m the pump end sits at vapour for 47&nbsp;s; the valve opens the instant the cavity closes and holds 95.0&ndash;95.7&nbsp;m. At 69&nbsp;s, where the unprotected trace spikes to about 190&nbsp;m (165&ndash;190&nbsp;m across the two cavity models), the valve opens further and the head reaches <strong>96.3&nbsp;m</strong>. At 110&nbsp;m and 120&nbsp;m it opens part-way up the climb after the collapse. Every setting gives the same pattern: an excellent result at the valve in this no-delay model, &minus;9.8&nbsp;m on the line, and a line maximum the valve cannot settle.</p>

<h2 id="envelopes">5 &middot; Why the line still fails &mdash; or might not</h2>
<p>The valve removes the doubling at the check valve, which lowers the envelope near the pump: at 6&nbsp;km the maximum falls from 150&ndash;160&nbsp;m unprotected to 120&ndash;130&nbsp;m at a 95&nbsp;m setting. The far end is governed by the front that left the pump at 47&nbsp;s at about 97&nbsp;m &mdash; barely touched by a 95&nbsp;m valve, and untouched by a 110&nbsp;m or 120&nbsp;m valve that has not yet opened. In the vapour cavity model the 120&nbsp;m envelope matches the unprotected one from 8.0&nbsp;km onwards, and the 110&nbsp;m envelope from 10.7&nbsp;km.</p>
<p>Then comes the model question. At 95&nbsp;m the vapour cavity model peaks at 11.9&nbsp;km and leaves the last 1.6&nbsp;km above 136&nbsp;m; the gas cavity model peaks lower, at 11.1&nbsp;km, and leaves none. Honestly quoted, the line maximum is <strong>127&ndash;143&nbsp;m</strong>, with 136&nbsp;m inside the range. Higher settings only lengthen the stretch over the allowable (table 1).</p>
<div class="callout warn">
  <span class="lbl">Not a design</span>
  A scheme whose compliance hangs on the least certain number in transient analysis is not a design. Accept the 95&nbsp;m valve because the gas cavity model shows 127&nbsp;m, and a modelling option has chosen the pipe class &mdash; at a setting the station could not hold. Every high head on the line still comes from a column stopped after separation [6, 8]. Protect the downsurge, and the upsurge becomes a clean, well-predicted wave.
</div>
<h3>Why a lower set point cannot fix it</h3>
<p>The set point cannot go below the pumps&rsquo; shut-off head plus a margin (section 9), and the governing front leaves the pump at about 97&nbsp;m: \(B\) times the returning flow, counted up from vapour pressure. A relief valve set at or above that head barely touches it. Near the reservoir the same front is counted up from 44.8&nbsp;m, which is why the envelope <em>rises</em> towards the delivery end. Only a device that stops the column separating removes the returning flow; a valve already open when it returns might discharge part of it (the anticipator, section 9).</p>

<h2 id="int-line">6 &middot; Interactive: along the line</h2>
<p>The shaded band between the two maximum envelopes is the part of the answer that belongs to the cavity model rather than to the valve.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Maximum and minimum head envelopes along the 12 km main</div>
    <div class="fsub">Maximum envelopes from the vapour and gas cavity models, minimum envelope from the vapour cavity model, DN250 relief valve at the pump. The grey line is the vapour-model maximum with no valve.</div>
  </div>
  <div class="chart-box"><canvas id="lineChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Relief valve setting <span id="v2">set 95 m</span></label>
      <select id="s2">
        <option value="0">No valve</option>
        <option value="1">Set 120 m</option>
        <option value="2">Set 110 m</option>
        <option value="3" selected>Set 95 m (best case)</option>
      </select>
      <div class="hint">Lengths count each 100 m reach whose maximum exceeds 136 m.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Above 136 m, vapour model</div><div class="v" id="rA2">1.6 <small>km</small></div><div id="bA2" style="margin-top:6px;"><span class="badge bad">over the allowable</span></div></div>
    <div class="cell"><div class="k">Above 136 m, gas model</div><div class="v" id="rB2">0.0 <small>km</small></div><div id="bB2" style="margin-top:6px;"><span class="badge good">within the allowable</span></div></div>
    <div class="cell"><div class="k">Line max</div><div class="v" id="rX2">127&ndash;143 <small>m</small></div></div>
    <div class="cell"><div class="k">Peak location, vapour / gas</div><div class="v" id="rW2">11.9 / 11.1 <small>km</small></div></div>
    <div class="cell"><div class="k">Max at 6 km</div><div class="v" id="rC2">120&ndash;130 <small>m</small></div></div>
  </div>
</div>
<p class="fig-note">At 95&nbsp;m the upper edge of the band crosses 136&nbsp;m over the last stretch before the reservoir and the lower edge does not; step through the settings to see the lengths in table 1 build up. Against the grey unprotected line, the valve pulls the envelope down near the pump and leaves the far end alone. The minimum envelope never moves.</p>

<h2 id="sizing">7 &middot; Sizing the valve: flow first, then bore</h2>
<p>A relief valve is sized for a flow, and the flow is a transient result: at the 95&nbsp;m setting, 0.416&nbsp;m&sup3;/s in the vapour cavity model and 0.280&nbsp;m&sup3;/s in the gas cavity model. The peak is collapse-driven too, so size for the larger.</p>
<h3>A first estimate before the model</h3>
<p>Without the valve the waves lift the pump end to the unprotected peak \(H_u\); with the valve open near \(H_s\), the flow behind the difference has to leave through it:</p>
<div class="eq">\[ Q_r \;\approx\; \frac{H_u - H_s}{B} \;=\; \frac{(165\ \text{to}\ 190) - 95}{212.9} \;=\; 0.33\ \text{to}\ 0.45\ \text{m}^3/\text{s} \]</div>
<p>The model gives 0.280&ndash;0.416&nbsp;m&sup3;/s. The estimate runs 7&ndash;17&nbsp;% high because each discharge weakens the waves that follow &mdash; the right side to err on when choosing sizes to model.</p>
<h3>Capacity at full lift, K<sub>v</sub> and C<sub>v</sub></h3>
<p>Full lift is reached at the set head plus the overpressure, so the capacity at full lift, discharging to atmosphere, is</p>
<div class="eq">\[ Q_{cap} \;=\; C_d\,A\,\sqrt{2 g \left(H_s + \Delta h_{op}\right)} \]</div>
<p>&mdash; 1.298&nbsp;m&sup3;/s for DN250 at a 95&nbsp;m set head and \(C_d\) = 0.6, with the other sizes in the table. Manufacturers usually quote a flow coefficient, so convert the required flow at the set pressure, 95&nbsp;m or 9.32&nbsp;bar:</p>
<div class="eq">\[ K_v \;=\; \frac{Q\ [\text{m}^3/\text{h}]}{\sqrt{\Delta p\ [\text{bar}]}} \;=\; \frac{0.416 \times 3600}{\sqrt{9.32}} \;=\; 491\ \text{m}^3/\text{h}, \qquad C_v \;=\; 1.156\,K_v \;=\; 567 \]</div>
<p>The same law gives the head at the valve, \(h = H_s + \Delta h_{op}\,Q_r / (C_d A \sqrt{2gh})\): 96.3&nbsp;m for DN250, 97.0&nbsp;m for DN200 and 98.5&nbsp;m for DN150 at the flows the model computes &mdash; its pump-end maxima to 0.1&nbsp;m. Once the valve is big enough, its own characteristic sets the pump-end result.</p>
<div class="tbl-wrap"><table>
  <caption>Valve size sweep at a 95&nbsp;m set head, C<sub>d</sub> 0.6, full lift at 99&nbsp;m; capacity against a required 416&nbsp;L/s. Collapse-driven maxima as a range across the two cavity models.</caption>
  <thead><tr><th>Valve</th><th class="num">Capacity at full lift (L/s)</th><th class="num">Capacity &divide; required</th><th class="num">Peak relief flow, vapour / gas (L/s)</th><th class="num">Pump-end max, vapour / gas (m)</th><th class="num">Line max (m)</th></tr></thead>
  <tbody>
    <tr><td>DN100</td><td class="num">208</td><td class="num">0.50</td><td class="num">242 / 219</td><td class="num">110&ndash;135 (collapse range)</td><td class="num">127&ndash;143</td></tr>
    <tr><td>DN150</td><td class="num">467</td><td class="num">1.12</td><td class="num">407 / 274</td><td class="num">98.5 / 97.4</td><td class="num">127&ndash;143</td></tr>
    <tr><td>DN200</td><td class="num">831</td><td class="num">2.00</td><td class="num">413 / 278</td><td class="num">97.0 / 96.4</td><td class="num">127&ndash;143</td></tr>
    <tr><td>DN250</td><td class="num">1,298</td><td class="num">3.12</td><td class="num">416 / 280</td><td class="num">96.3 / 95.9</td><td class="num">127&ndash;143</td></tr>
    <tr><td>DN300</td><td class="num">1,869</td><td class="num">4.49</td><td class="num">418 / 281</td><td class="num">95.9 / 95.6</td><td class="num">127&ndash;143</td></tr>
  </tbody>
</table></div>
<p>DN100 is undersized: its capacity at full lift is half the requirement, and it passes 242&nbsp;L/s only because the pump end climbs to 110&ndash;135&nbsp;m, a collapse-driven range again because the valve has lost control. From DN150 up the pump end is controlled, and each size step buys less than 1.5&nbsp;m. DN150 works near full lift, with no margin for a lower installed discharge coefficient or a slower valve, so in our judgement DN200 or DN250 is the choice. The last column never moves: <strong>the line maximum is indifferent to the size of the valve</strong>.</p>
<h3>The discharge side</h3>
<p>At 0.416&nbsp;m&sup3;/s a DN250 outlet runs at 8.5&nbsp;m/s, and the model discharges 3.3&ndash;4.4&nbsp;m&sup3; per trip at 95&nbsp;m (vapour and gas cavity models) &mdash; one event, not a sump volume. The discharge pipe must not throttle the valve, the sump or return must take the peak flow and repeated trips without backing up, and a valve venting at over 9&nbsp;bar needs a splash guard and safe access [3, 9].</p>

<h2 id="int-size">8 &middot; Interactive: sizing the valve</h2>
<p>The left axis carries the transient sweep at 95&nbsp;m; the right axis carries the capacity at full lift for your inputs, against the flow you require.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Relief valve size: capacity, flow coefficients and the transient sweep</div>
    <div class="fsub">Left axis: maximum heads from the transient sweep at set 95 m, C<sub>d</sub> 0.6; circles vapour cavity model, triangles gas cavity model. Right axis: capacity at full lift C<sub>d</sub>A&radic;(2g(H<sub>s</sub> + 4 m)) for your inputs, the required flow, and the sweep&rsquo;s peak relief flows. K<sub>v</sub> at the set pressure; head at the valve from the proportional-lift law with 4 m overpressure.</div>
  </div>
  <div class="chart-box"><canvas id="sizeChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Valve size <span id="vDN">DN250</span></label>
      <select id="sDN">
        <option value="100">DN100</option>
        <option value="150">DN150</option>
        <option value="200">DN200</option>
        <option value="250" selected>DN250</option>
        <option value="300">DN300</option>
      </select>
      <div class="hint">Nominal bore taken as the flow area.</div>
    </div>
    <div class="ctrl">
      <label>Set head <span id="vHs">95 m</span></label>
      <input type="range" id="sHs" min="80" max="140" value="95" step="1">
      <div class="hint">Steady head at the pump 85.0 m, pumps&rsquo; shut-off head 105 m; set point plus the 4 m overpressure must stay under the 136 m allowable. The transient sweep stays at 95 m.</div>
    </div>
    <div class="ctrl">
      <label>Discharge coefficient <span id="vCd">0.60</span></label>
      <input type="range" id="sCd" min="0.4" max="0.8" value="0.6" step="0.01">
      <div class="hint">Use the installed value, with inlet and outlet pipework.</div>
    </div>
    <div class="ctrl">
      <label>Required flow <span id="vQr">0.416 m&sup3;/s</span></label>
      <input type="range" id="sQr" min="0.1" max="1" value="0.416" step="0.001">
      <div class="hint">Default: peak relief flow from the transient model, DN250 at 95 m, vapour cavity model.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Capacity at full lift</div><div class="v" id="rCap">1.298 <small>m&sup3;/s</small></div></div>
    <div class="cell"><div class="k">K<sub>v</sub> required</div><div class="v" id="rKv">491 <small>m&sup3;/h</small></div></div>
    <div class="cell"><div class="k">C<sub>v</sub> required</div><div class="v" id="rCv">567 <small>US</small></div></div>
    <div class="cell"><div class="k">Capacity &divide; required</div><div class="v" id="rRat">3.12 <small>&times;</small></div><div id="bRat" style="margin-top:6px;"><span class="badge good">adequate</span></div></div>
    <div class="cell"><div class="k">Head at the valve</div><div class="v" id="rHv">96.3 <small>m, lift 32 %</small></div><div id="bHv" style="margin-top:6px;"><span class="badge warn">below the pumps&rsquo; 105 m shut-off head</span></div></div>
    <div class="cell"><div class="k">First estimate of flow</div><div class="v" id="rEst">0.33&ndash;0.45 <small>m&sup3;/s</small></div></div>
  </div>
</div>
<p class="fig-note">At the defaults the valve has <strong>1.298&nbsp;m&sup3;/s at full lift, 3.12 times the requirement</strong>, and settles at 96.3&nbsp;m, a third of the way to full lift. At DN150 the ratio falls to 1.12 and the head rises to 98.6&nbsp;m, nearly wide open; at a discharge coefficient of 0.45, DN150 is no longer enough. Raising the set head lowers the first estimate but not the sweep, which stays at 95&nbsp;m; how the set point moves the line maximum is in figure 2 and table 1 (127&ndash;143&nbsp;m at 95&nbsp;m, 140&ndash;155&nbsp;m at 120&nbsp;m).</p>

<h2 id="setpoint">9 &middot; Set pressure, reseating and the anticipator</h2>
<h3>Choosing the set point</h3>
<p>Too high a set point exposes more of the line (table 1). Too low, and the valve opens in service: it must clear a second pump starting, a control valve moving and, above all, a delivery valve closed against running pumps, which takes the pump end to the shut-off head. The model pump of the pump inertia article in this series has a zero-flow head of 105&nbsp;m (100&nbsp;m above a 5&nbsp;m suction), so a 95&nbsp;m valve would discharge whenever the flow was throttled below about 0.50&nbsp;m&sup3;/s. In our judgement a setting that clears 105&nbsp;m with the valve&rsquo;s tolerance is nearer 110&ndash;120&nbsp;m, which leaves 10.0&ndash;11.9&nbsp;km above 136&nbsp;m in the vapour cavity model (none to 3.9&nbsp;km in the gas cavity model). In our practice the set point comes from a run of the <a href="surge-scenarios-pump-stations.html">normal operating events</a> &mdash; their highest head plus the set-point tolerance &mdash; and the trip is rerun at that setting.</p>
<p>ISO 4126-1 supplies the vocabulary [10]. The <strong>overpressure</strong> is the rise above set pressure needed for full lift (4&nbsp;m here); the <strong>reseating pressure</strong> is where the valve closes again, and the difference from the set pressure is the <strong>blowdown</strong> &mdash; too long and the valve dumps water after the transient, too short and it chatters. On the pipe side, EN 805 distinguishes the design pressure from the maximum design pressure, which adds a surge allowance [11]: set point plus overpressure must not exceed the maximum design pressure, and nor may the maximum envelope anywhere along the line.</p>
<h3>Spring-loaded or pilot-operated</h3>
<p>A direct-acting valve holds its disc shut with a spring; a pilot-operated valve uses a small pilot, sensing line pressure, to control the chamber above the main valve &mdash; conceptually, simplicity against closer control of set point and closing speed [2, 3]. Neither opens instantly, and here the valve first opens at the worst moment: at 95&nbsp;m on the cavity collapse itself, a step of about 106&nbsp;m in one time step; at 110&nbsp;m and 120&nbsp;m part-way up the climb that follows. Without the valve the pump end rises from 96.5&nbsp;m at the collapse to 102.3&nbsp;m by 48&nbsp;s and 109.0&nbsp;m by 49&nbsp;s, so a valve that takes a second or two to open lets the head run up that climb and sends a higher front towards the far end. Model the manufacturer&rsquo;s opening and closing times before relying on any number here.</p>
<h3>The surge anticipator valve</h3>
<p>A surge anticipator valve (SAV) opens on the initial <em>low</em> pressure after a trip, so it is already open when the return wave arrives, and then closes slowly [2, 12]. That removes the opening-time problem, but it neither prevents separation nor feeds the downsurge. Being open when the column returns, it may lower the collapse front that governs the far-end peak; that has to be shown by modelling it, including its behaviour while its connection is below atmospheric pressure &mdash; the question behind <a href="air-admission-networks.html">air admission</a>. <strong>No anticipator was modelled here.</strong></p>

<h2 id="where">10 &middot; Where a relief valve is the right answer</h2>
<p>None of this makes the SRV a bad device, only one with a narrow job. In our judgement it fits in three places, and fails in a fourth:</p>
<ul class="clean">
  <li><strong>Where the downsurge stays above vapour.</strong> With a low velocity, a slow rundown or a protected downsurge, the upsurge is the returning wave at the <a href="check-valve-hammer.html">check valve</a>, and a relief valve there caps it where it is generated.</li>
  <li><strong>Upstream of a closing valve on a gravity line</strong>, where the closure generates the upsurge: slow the closure first and keep the relief valve as the backstop (<a href="water-hammer-control-valve.html">control valve closure</a>, <a href="control-valve-transients-hammer.html">control valve transients in HAMMER</a>).</li>
  <li><strong>Behind a vessel, as a backstop</strong> that caps the pump header if the vessel is isolated, short of gas or wrongly charged. It must stay shut while the vessel works, so here it would sit above the vessel&rsquo;s 119.2&nbsp;m line maximum, at 120&nbsp;m say &mdash; and with the vessel out of service the line would still see 140&ndash;155&nbsp;m (section 3). The vessel&rsquo;s availability is the real protection; record it in the <a href="surge-analysis-risk.html">surge risk review</a>.</li>
  <li><strong>Not as the primary pump-trip protection on a line that separates</strong>, like this one [9, 12].</li>
</ul>
<div class="tbl-wrap"><table>
  <caption>All pumps tripped on the reference main: what each option does to the envelope. Collapse-driven maxima as a range across the two cavity models.</caption>
  <thead><tr><th>Option</th><th class="num">Line min (m)</th><th class="num">Line max (m)</th><th>What it protects</th></tr></thead>
  <tbody>
    <tr><td>No protection</td><td class="num">&minus;9.8</td><td class="num">165&ndash;190</td><td>Nothing: column separation along the line</td></tr>
    <tr><td>Relief valve DN250, set 95&nbsp;m (best case)</td><td class="num">&minus;9.8</td><td class="num">127&ndash;143</td><td>The pressure side, at the valve</td></tr>
    <tr><td>Flywheel, total I = 400&nbsp;kg&middot;m&sup2;</td><td class="num">+9.3</td><td class="num">85.0</td><td>Both sides, by keeping the column moving</td></tr>
    <tr><td>Vessel 20&nbsp;m&sup3;, 3.5&nbsp;m&sup3; gas, <a href="surge-vessel-differential-orifice.html">differential DN400 connection</a></td><td class="num">+4.3</td><td class="num">119.2</td><td>Both sides, at the pump</td></tr>
  </tbody>
</table></div>
<p>The two options that stop the column separating remove the collapse upsurge and keep the maximum within the rating (119.2&nbsp;m and 85.0&nbsp;m). That is the argument of this series in one table, worked through in <a href="choosing-surge-protection.html">choosing surge protection on one pipeline</a>.</p>

<h2 id="hammer">11 &middot; Setting it up in Bentley HAMMER</h2>
<p>Field names differ slightly between HAMMER versions, so read them as descriptions of intent [13]. The <a href="hammer-transient-simulation-workflow.html">HAMMER transient workflow</a> and <a href="hammer-transient-tips.html">HAMMER transient tips</a> cover the general run set-up.</p>
<ol>
  <li><strong>Build and check the steady state.</strong> Reservoir, Pump, Pipe and delivery Reservoir on the real profile, with each Pipe&rsquo;s wave speed from the Wave Speed Calculator (<a href="wave-speed-surge-analysis.html">wave speed</a>).</li>
  <li><strong>Define the trip.</strong> On the Pump: a pump trip (shut down) at time zero, pump and motor inertia from the datasheets, 4-quadrant characteristic curves (from specific speed if the manufacturer&rsquo;s are not available), and the check valve on the pump with its closure time or delay.</li>
  <li><strong>Run it unprotected</strong> for several times 2L/a (150&nbsp;s here, against 22.9&nbsp;s), with the computed time step, a tight wave speed adjustment tolerance and vapour pressure / column separation on. Read the profile (path) with maximum and minimum head envelopes: if the line reaches vapour, the relief valve is not the primary device.</li>
  <li><strong>Fix the threshold pressure from normal operation.</strong> Run a pump start, a controlled stop, control valve movements and a delivery valve closed against running pumps. Set the threshold (set) pressure above the highest head at the pump discharge node by the valve&rsquo;s set-point tolerance.</li>
  <li><strong>Add the Surge Valve</strong> at the pump discharge node, downstream of the check valves, as a surge relief valve: the threshold pressure from step 4, size and discharge coefficient, and time to open and time to close (or the opening and closing characteristics) from the manufacturer. An instantaneous opening is only a bounding sensitivity, and this article&rsquo;s figures come from a different model, so do not expect to reproduce them. Rerun the step 4 events with the valve in place and confirm it stays shut.</li>
  <li><strong>Build the comparisons.</strong> At least three valve sizes around the first estimate from section 7 as separate scenarios, with any higher set points as alternatives above the step 4 value.</li>
  <li><strong>Read the pump end.</strong> In the Transient Results Viewer, plot the time history at the valve node: the head should stay within the overpressure of the set point. Note when the valve first opens and, if your version reports it, the peak discharge.</li>
  <li><strong>Read the whole line.</strong> Plot the profile (path) envelopes for every scenario, check the maximum against the pipe rating along the full length, and use the animation to see where the high heads are generated.</li>
  <li><strong>Check the minimum separately.</strong> The relief valve does nothing for the downsurge; the minimum envelope must meet the design minimum (+3.0&nbsp;m here) by other means, or every maximum on the line is a collapse result.</li>
  <li><strong>Test whether the verdict holds.</strong> Rerun any scenario that separates with different column separation settings. If the verdict against the pipe rating changes, the protection must change. A finer time step checks convergence but will not remove the cavity-model uncertainty.</li>
</ol>

<h2 id="checklist">12 &middot; Design checklist</h2>
<ul class="clean">
  <li><strong>Run the trip unprotected first.</strong> If the line reaches vapour, a relief valve is not the primary protection.</li>
  <li><strong>Set the valve from a normal-operations run</strong>, above every normal event and the pumps&rsquo; shut-off head plus tolerance, then rerun the trip.</li>
  <li><strong>Size for flow.</strong> Screen with \((H_u - H_s)/B\), then take the peak relief flow under the harsher cavity model.</li>
  <li><strong>Choose a size that controls the pump end with margin</strong> at the installed discharge coefficient, not the smallest that reaches full lift, and give the manufacturer K<sub>v</sub> or C<sub>v</sub> at the set pressure.</li>
  <li><strong>Model the manufacturer&rsquo;s</strong> set-point tolerance, overpressure, reseating pressure and opening and closing times &mdash; the first opening can coincide with a cavity collapse.</li>
  <li><strong>Read the whole-line envelopes</strong>, quote collapse-driven maxima as a range, and reject any scheme whose compliance depends on the cavity model.</li>
  <li><strong>Design the discharge</strong> &mdash; drain, sump or return, splash protection, access &mdash; for the peak flow and repeated events.</li>
  <li><strong>Record the residual risk</strong> in the <a href="surge-analysis-risk.html">surge risk review</a>, and hand the settings and their reasons to operations so nobody raises the set point to stop a nuisance discharge (<a href="transient-analysis-scada.html">transients and SCADA</a>).</li>
</ul>

<div class="callout key">
  <span class="lbl">In summary</span>
  Even in the best case, set at 95&nbsp;m, a DN250 relief valve holds the pump end at <strong>96.3&nbsp;m</strong> and discharges 0.280&ndash;0.416&nbsp;m&sup3;/s at its peak. It does nothing for the downsurge: the line still reaches vapour from end to end, and its peak is <strong>127&ndash;143&nbsp;m</strong>, either side of the 136&nbsp;m allowable depending on the cavity model. Size it for flow, set it from normal operation, and use it where the pressure is generated at the valve &mdash; or behind a device that stops the column separating.
</div>

<div class="callout green">
  <span class="lbl">Surge protection design series</span>
  <ol>
    <li><a href="wave-speed-surge-analysis.html">Wave speed: the number that sets the surge</a></li>
    <li><a href="surge-vessel-differential-orifice.html">The differential orifice: empty freely, refill slowly</a></li>
    <li><a href="surge-vessel-type-selection.html">Bladder, diaphragm or air-over-water vessel</a></li>
    <li><a href="one-way-surge-tank-design.html">One-way surge tanks at the knee</a></li>
    <li><strong>Surge relief valves: what a valve at the pump can protect</strong></li>
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
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'IBM Plex Sans',size:11}}};
const TT={font:{family:'IBM Plex Sans',size:12,weight:'600'}};
const LEG={labels:{font:{family:'IBM Plex Sans',size:11},usePointStyle:true,boxWidth:8}};
const G=9.81, LIM=136, PMIN=3.0, HV=-9.8, HSS=85.0, HSHUT=105.0;
const B=1050/(G*Math.PI*0.8*0.8/4);            /* pipe impedance a/(gA), s/m2 */
const ACC=D.acc;                                  /* overpressure to full lift, m */
const pts=(xs,ys)=>xs.map((x,i)=>({x:x,y:ys[i]}));
const neg=v=>(v<0?'&minus;':'')+fmt1(Math.abs(v));
const lbl=(txt,pos,col)=>({display:true,content:txt,position:pos,color:col,backgroundColor:'rgba(255,255,255,0.85)',font:{size:10,family:'IBM Plex Sans'}});
const hline=(y,col,dash,txt,pos)=>({type:'line',yMin:y,yMax:y,borderColor:col,borderWidth:1.5,borderDash:dash,label:lbl(txt,pos,col)});
/* collapse-driven maxima: a range across the two cavity models, rounded to 5 m, but to whole metres when the 136 m limit falls inside the range */
function rng(a,b){const lo=Math.min(a,b),hi=Math.max(a,b);
  if(lo<=LIM&&hi>=LIM)return Math.round(lo)+'&ndash;'+Math.round(hi);
  return (5*Math.round(lo/5))+'&ndash;'+(5*Math.round(hi/5));}
function verdict(a,b){const lo=Math.min(a,b),hi=Math.max(a,b);
  if(hi<=LIM)return '<span class="badge good">below 136 m in both models</span>';
  if(lo>LIM)return '<span class="badge bad">above 136 m in both models</span>';
  return '<span class="badge warn">depends on the cavity model</span>';}
function minBadge(m){
  if(m<=HV+0.01)return '<span class="badge bad">vapour: column separation</span>';
  if(m<PMIN)return '<span class="badge warn">below +3.0 m</span>';
  return '<span class="badge good">meets +3.0 m</span>';}
const maxOf=a=>a.reduce((m,v)=>v>m?v:m,-1e9);
const minOf=a=>a.reduce((m,v)=>v<m?v:m,1e9);

/* ---------- CHART 1 : the pump end, second by second ---------- */
const s1=document.getElementById('s1');
let c1=new Chart(document.getElementById('pumpChart'),{
  type:'line',
  data:{datasets:[
    {label:'No valve',data:[],borderColor:'rgba(127,140,141,0.55)',borderWidth:1.3,pointRadius:0,tension:0},
    {label:'Relief valve set 95 m',data:[],borderColor:'#1b4f72',borderWidth:2.4,pointRadius:0,tension:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:150,title:{display:true,text:'Time after the trip (s)',...TT},...AX},
            y:{type:'linear',min:-25,max:200,title:{display:true,text:'Pressure head at the pump (m)',...TT},...AX,ticks:{stepSize:25,font:{family:'IBM Plex Sans',size:11}}}},
    plugins:{legend:{labels:{...LEG.labels,filter:(it,d)=>!(it.datasetIndex===0&&!d.datasets[0].data.length)}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{
        pn:hline(LIM,'#c0392b',[6,4],'PN16 allowable 136 m','start'),
        set:hline(95,'#b9770e',[6,4],'set 95 m','end'),
        ss:hline(HSS,'#7f8c8d',[2,3],'steady 85.0 m','start'),
        vap:hline(HV,'#6b4f9e',[2,3],'vapour -9.8 m','start')
      }}}}
});
function upd1(){
  const c=D.cases[+s1.value];
  document.getElementById('v1').textContent=c.set?('set '+c.set+' m'):'no valve';
  c1.data.datasets[0].data=c.set?pts(D.t,D.cases[0].H):[];
  c1.data.datasets[1].data=pts(D.t,c.H);
  c1.data.datasets[1].label=c.set?('Relief valve set '+c.set+' m'):'No valve';
  const an=c1.options.plugins.annotation.annotations;
  an.set.display=!!c.set;
  if(c.set){an.set.yMin=c.set;an.set.yMax=c.set;an.set.label.content='set '+c.set+' m';}
  c1.update('none');
  document.getElementById('rP1').innerHTML=c.set?(fmt1(c.pmax)+' <small>m (gas model '+fmt1(c.pmaxg)+')</small>')
                                                 :(rng(c.pmax,c.pmaxg)+' <small>m, collapse peak</small>');
  const lv=maxOf(c.Hv), lg=maxOf(c.Hg);
  document.getElementById('rL1').innerHTML=rng(lv,lg)+' <small>m</small>';
  document.getElementById('bL1').innerHTML=verdict(lv,lg);
  const mn=minOf(c.Hmin);
  document.getElementById('rM1').innerHTML=neg(mn)+' <small>m</small>';
  document.getElementById('bM1').innerHTML=minBadge(mn);
  document.getElementById('rQ1').innerHTML=c.set?(fmt3(c.q)+' <small>m³/s (gas model '+fmt3(c.qg)+')</small>'):'&ndash; <small>no valve</small>';
  document.getElementById('rO1').innerHTML=!c.set?'&ndash; <small>no valve</small>'
    :(c.topen>0?fmt0(c.topen)+' <small>s</small>':'&ndash; <small>stays shut</small>');
}
s1.addEventListener('input',upd1);upd1();

/* ---------- CHART 2 : along the line ---------- */
const s2=document.getElementById('s2');
const XK=D.x.map(x=>x/1000);
let c2=new Chart(document.getElementById('lineChart'),{
  type:'line',
  data:{datasets:[
    {label:'Max, vapour cavity model',data:[],borderColor:'#c0392b',borderWidth:2.4,pointRadius:0,fill:false,order:1},
    {label:'Max, gas cavity model',data:[],borderColor:'#b9770e',borderWidth:2,borderDash:[6,4],pointRadius:0,fill:'-1',backgroundColor:'rgba(185,119,14,0.14)',order:2},
    {label:'Min, vapour cavity model',data:[],borderColor:'#1b4f72',borderWidth:2.2,pointRadius:0,fill:false,order:3},
    {label:'Max with no valve',data:[],borderColor:'rgba(127,140,141,0.6)',borderWidth:1.3,pointRadius:0,fill:false,order:4}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:12,title:{display:true,text:'Chainage from the pump (km)',...TT},...AX},
            y:{type:'linear',min:-25,max:200,title:{display:true,text:'Pressure head (m)',...TT},...AX,ticks:{stepSize:25,font:{family:'IBM Plex Sans',size:11}}}},
    plugins:{legend:{labels:{...LEG.labels,filter:(it,d)=>!(it.datasetIndex===3&&!d.datasets[3].data.length)}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} km`}},
      annotation:{annotations:{
        pn:hline(LIM,'#c0392b',[6,4],'PN16 allowable 136 m','start'),
        mn:hline(PMIN,'#1e8449',[6,4],'design minimum +3.0 m','end'),
        vap:hline(HV,'#6b4f9e',[2,3],'vapour -9.8 m','start')
      }}}}
});
function upd2(){
  const c=D.cases[+s2.value], u=D.cases[0];
  document.getElementById('v2').textContent=c.set?('set '+c.set+' m'):'no valve';
  c2.data.datasets[0].data=pts(XK,c.Hv);
  c2.data.datasets[1].data=pts(XK,c.Hg);
  c2.data.datasets[2].data=pts(XK,c.Hmin);
  c2.data.datasets[3].data=c.set?pts(XK,u.Hv):[];
  c2.update('none');
  const la=c.Hv.filter(h=>h>LIM).length*100, lb=c.Hg.filter(h=>h>LIM).length*100;
  const bl=l=>l>0?'<span class="badge bad">over the allowable</span>':'<span class="badge good">within the allowable</span>';
  document.getElementById('rA2').innerHTML=fmt1(la/1000)+' <small>km</small>';
  document.getElementById('bA2').innerHTML=bl(la);
  document.getElementById('rB2').innerHTML=fmt1(lb/1000)+' <small>km</small>';
  document.getElementById('bB2').innerHTML=bl(lb);
  const lv=maxOf(c.Hv), lg=maxOf(c.Hg);
  document.getElementById('rX2').innerHTML=rng(lv,lg)+' <small>m</small>';
  document.getElementById('rW2').innerHTML=fmt1(D.x[c.Hv.indexOf(lv)]/1000)+' / '+fmt1(D.x[c.Hg.indexOf(lg)]/1000)+' <small>km</small>';
  const i6=D.x.indexOf(6000);
  document.getElementById('rC2').innerHTML=rng(c.Hv[i6],c.Hg[i6])+' <small>m</small>';
}
s2.addEventListener('input',upd2);upd2();

/* ---------- CHART 3 : sizing the valve ---------- */
const sDN=document.getElementById('sDN'),sHs=document.getElementById('sHs'),
      sCd=document.getElementById('sCd'),sQr=document.getElementById('sQr');
const areaDN=dn=>Math.PI*Math.pow(dn/1000,2)/4;
const capAt=(dn,Hs,Cd)=>Cd*areaDN(dn)*Math.sqrt(2*G*(Hs+ACC));   /* full lift is reached at Hs + overpressure */
function headAtValve(dn,Hs,Cd,Q){            /* h = Hs + acc * Q/(CdA sqrt(2gh)); null if full lift cannot pass Q */
  const CdA=Cd*areaDN(dn);
  if(Q>capAt(dn,Hs,Cd))return null;
  let h=Hs+ACC;
  for(let k=0;k<80;k++)h=Hs+ACC*Math.min(1,Q/(CdA*Math.sqrt(2*G*h)));
  return h;
}
const SZ=D.sizes, HU_V=D.cases[0].pmax, HU_G=D.cases[0].pmaxg;
let c3=new Chart(document.getElementById('sizeChart'),{
  type:'line',
  data:{datasets:[
    {label:'Pump end · vapour',data:pts(SZ.map(s=>s.dn),SZ.map(s=>s.pmax)),borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:3,pointStyle:'circle',yAxisID:'y'},
    {label:'Pump end · gas',data:pts(SZ.map(s=>s.dn),SZ.map(s=>s.pmaxg)),borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:1.8,borderDash:[6,4],pointRadius:3,pointStyle:'triangle',yAxisID:'y'},
    {label:'Line max · vapour',data:pts(SZ.map(s=>s.dn),SZ.map(s=>s.lmax)),borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.2,pointRadius:3,pointStyle:'circle',yAxisID:'y'},
    {label:'Line max · gas',data:pts(SZ.map(s=>s.dn),SZ.map(s=>s.lmaxg)),borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.8,borderDash:[6,4],pointRadius:3,pointStyle:'triangle',yAxisID:'y'},
    {label:'Capacity',data:[],borderColor:'#1e8449',backgroundColor:'#1e8449',borderWidth:2.2,pointRadius:0,pointStyle:'line',yAxisID:'y1'},
    {label:'Q required',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.6,borderDash:[3,3],pointRadius:0,pointStyle:'line',yAxisID:'y1'},
    {label:'Q relief · vapour',data:pts(SZ.map(s=>s.dn),SZ.map(s=>s.q)),borderColor:'#6b4f9e',backgroundColor:'#6b4f9e',showLine:false,pointRadius:5,pointStyle:'circle',yAxisID:'y1'},
    {label:'Q relief · gas',data:pts(SZ.map(s=>s.dn),SZ.map(s=>s.qg)),borderColor:'#6b4f9e',backgroundColor:'#6b4f9e',showLine:false,pointRadius:5,pointStyle:'triangle',yAxisID:'y1'}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:75,max:325,afterBuildTicks:ax=>{ax.ticks=[100,150,200,250,300].map(v=>({value:v}));},ticks:{font:{family:'IBM Plex Sans',size:11},callback:v=>'DN'+v},grid:{color:'#eef2f5'},title:{display:true,text:'Relief valve size',...TT}},
            y:{type:'linear',min:40,max:160,position:'left',title:{display:true,text:'Max head at 95 m set (m)',...TT},...AX,ticks:{stepSize:20,font:{family:'IBM Plex Sans',size:11}}},
            y1:{type:'linear',min:0,position:'right',title:{display:true,text:'Flow (m³/s)',...TT},grid:{drawOnChartArea:false},ticks:{font:{family:'IBM Plex Sans',size:11}}}},
    onResize:(ch,sz)=>{const lb=ch.options.plugins.legend.labels,narrow=sz.width<480;lb.font.size=narrow?10:11;lb.boxWidth=narrow?5:8;lb.padding=narrow?5:10;},
    plugins:{legend:{labels:{font:{family:'IBM Plex Sans',size:(window.innerWidth||800)<520?10:11},usePointStyle:true,boxWidth:(window.innerWidth||800)<520?5:8,padding:(window.innerWidth||800)<520?5:10}},
      tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`${c.dataset.label}: ${fmt3(c.parsed.y)} m³/s`:`${c.dataset.label}: ${fmt1(c.parsed.y)} m`}},
      annotation:{annotations:{
        pn:{type:'line',yScaleID:'y',yMin:LIM,yMax:LIM,borderColor:'#c0392b',borderWidth:1.5,borderDash:[6,4],label:lbl('136 m','start','#c0392b')},
        sel:{type:'line',xMin:250,xMax:250,borderColor:'#6b4f9e',borderWidth:1.5,borderDash:[4,4],label:lbl('DN250','end','#6b4f9e')}
      }}}}
});
function upd3(){
  const dn=+sDN.value, Hs=+sHs.value, Cd=+sCd.value, Q=+sQr.value;
  document.getElementById('vDN').textContent='DN'+dn;
  document.getElementById('vHs').textContent=Hs+' m';
  document.getElementById('vCd').textContent=fmt2(Cd);
  document.getElementById('vQr').innerHTML=fmt3(Q)+' m³/s';
  const xs=[];for(let d=100;d<=300;d+=5)xs.push(d);
  c3.data.datasets[4].data=xs.map(d=>({x:d,y:+capAt(d,Hs,Cd).toFixed(4)}));
  c3.data.datasets[5].data=[{x:100,y:Q},{x:300,y:Q}];
  for(let k=0;k<4;k++)c3.data.datasets[k].pointRadius=SZ.map(s=>s.dn===dn?7:3);
  const an=c3.options.plugins.annotation.annotations;
  an.sel.xMin=dn;an.sel.xMax=dn;an.sel.label.content='DN'+dn;
  c3.update('none');
  const cap=capAt(dn,Hs,Cd), Kv=Q*3600/Math.sqrt(Hs*0.0981), ratio=cap/Q;
  document.getElementById('rCap').innerHTML=fmt3(cap)+' <small>m³/s</small>';
  document.getElementById('rKv').innerHTML=fmt0(Kv)+' <small>m³/h</small>';
  document.getElementById('rCv').innerHTML=fmt0(1.156*Kv)+' <small>US</small>';
  document.getElementById('rRat').innerHTML=(Math.abs(ratio-1)<0.01?ratio.toFixed(3):fmt2(ratio))+' <small>&times;</small>';
  let b;
  if(ratio<1)b='<span class="badge bad">undersized</span>';
  else if(ratio<1.5)b='<span class="badge warn">tight: near full lift</span>';
  else if(ratio<=4)b='<span class="badge good">adequate</span>';
  else b='<span class="badge warn">large margin: small working lift</span>';
  document.getElementById('bRat').innerHTML=b;
  const h=headAtValve(dn,Hs,Cd,Q);
  document.getElementById('rHv').innerHTML=h===null?'full lift <small>cannot pass it</small>'
    :(fmt1(h)+' <small>m, lift '+fmt0(100*(h-Hs)/ACC)+' %</small>');
  let hb;
  if(Hs+ACC>LIM)hb='<span class="badge bad">set + overpressure above the 136 m allowable</span>';
  else if(Hs<HSS)hb='<span class="badge bad">below the 85.0 m steady head: opens in service</span>';
  else if(Hs<HSHUT)hb='<span class="badge warn">below the pumps&rsquo; 105 m shut-off head</span>';
  else hb='<span class="badge good">clears the shut-off head and the allowable</span>';
  document.getElementById('bHv').innerHTML=hb;
  const lo=Math.max(0,(HU_G-Hs)/B), hi=Math.max(0,(HU_V-Hs)/B);
  document.getElementById('rEst').innerHTML=fmt2(lo)+'&ndash;'+fmt2(hi)+' <small>m³/s</small>';
}
[sDN,sHs,sCd,sQr].forEach(s=>s.addEventListener('input',upd3));upd3();

window.addEventListener('load',function(){try{c1.resize();c2.resize();c3.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993 — method of characteristics, pump and valve boundary conditions, column separation and the discrete vapour and gas cavity models.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014 — surge relief valves, surge anticipator valves and their representation in transient models.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004 — surge control devices, relief valve types and practical application on pumping mains.</li>
  <li>ISO 2531 <em>Ductile iron pipes, fittings, accessories and their joints for water applications</em> — the K9 ductile iron main of the reference system.</li>
  <li>Parmakian, J. <em>Waterhammer Analysis</em>. Dover, 1963 — pump discharge lines after power failure, the returning wave at a closed check valve, and relief valves.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006 — why cavity collapse peaks depend on the cavity model, and the vapour and gas cavity models compared.</li>
  <li>Larock, B.E., Jeppson, R.W. &amp; Watters, G.Z. <em>Hydraulics of Pipeline Systems</em>. CRC Press, 2000 — valve discharge boundaries and orifice-type discharge laws in characteristics models.</li>
  <li>Swaffield, J.A. &amp; Boldy, A.P. <em>Pressure Surge in Pipe and Duct Systems</em>. Avebury Technical, 1993 — pressure surge following column separation and the limits of local pressure relief.</li>
  <li>Stephenson, D. <em>Pipeline Design for Water Engineers</em>, 3rd ed. Elsevier, 1989 — protection of pumping lines, where relief valves suit and where they do not, and discharge arrangements.</li>
  <li>ISO 4126-1 <em>Safety devices for protection against excessive pressure — Part 1: Safety valves</em> — terminology: set pressure, overpressure, reseating pressure and blowdown.</li>
  <li>EN 805 <em>Water supply — Requirements for systems and components outside buildings</em> — design pressure, maximum design pressure including surge, and the surge allowance.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005 — surge relief and surge anticipating valves among the protection options, and their limits.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> product documentation and help — Surge Valve, Pump and Pipe properties, transient run options and the Transient Results Viewer.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeReliefValve #SurgeAnticipatorValve #WaterHammer #HydraulicTransients #SurgeAnalysis #PumpTrip #PumpStations #ColumnSeparation #VapourCavity #CavityCollapse #MethodOfCharacteristics #Joukowsky #TransmissionMains #DuctileIron #PN16 #ReliefValveSizing #FlowCoefficient #Kv #Cv #SetPressure #Blowdown #BentleyHAMMER #OpenFlowsHAMMER #SurgeProtection #HydropneumaticTank #PipelineDesign #WaterSupply #EN805 #TransientModelling</div>
"""

import json, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_D = json.load(open(os.path.join(_HERE, 'surge_data', 'datasets.json')))
_S = _D['srv']

# Maximum-head envelopes at 0.01 m for the four srv settings: vapour cavity model (moc.py) and gas cavity model
# (dgcm.py, alpha0 1e-7), reproduced with the srv block of gen_datasets.py. datasets.json stores them at 0.1 m;
# the length above 136 m is counted at 0.01 m exactly as gen_datasets.py counts len_above_136, so the chart
# needs this precision (four nodes sit at 136.0 m after rounding). Checked against datasets.json below.
_ENV2 = {
    'none': ([189.92,189.73,189.54,189.35,189.16,188.97,166.24,166.12,165.93,165.81,165.62,165.5,165.31,165.19,164.99,164.87,164.68,164.56,164.36,164.24,164.04,163.92,163.72,163.6,163.4,163.27,163.14,163.02,162.89,162.76,162.64,162.51,162.38,162.25,162.12,161.99,161.86,161.73,161.6,161.46,161.33,161.2,161.06,160.93,160.79,160.66,160.52,160.38,160.25,160.11,159.97,159.83,159.69,159.55,159.41,159.27,159.12,158.98,158.84,158.69,158.55,158.4,158.25,158.11,157.96,157.81,157.66,157.51,157.36,157.2,157.05,156.9,156.74,156.59,156.43,156.27,156.12,155.96,155.8,155.64,155.48,155.31,155.15,154.99,154.82,154.65,154.49,154.32,154.15,153.98,153.81,153.64,153.46,153.29,153.11,152.94,152.76,152.58,152.4,152.22,152.03,151.85,151.67,151.48,151.29,151.1,150.91,150.72,150.53,150.33,150.14,148.09,147.61,147.14,146.67,146.21,145.76,145.31,144.86,144.42,44.8],
           [164.55,163.71,163.33,162.62,161.92,161.28,160.86,161.7,160.97,160.46,159.9,160.74,159.9,159.64,160.49,158.32,159.07,158.78,159.17,160.01,157.96,158.71,158.5,158.88,159.72,157.67,158.42,157.96,158.45,158.54,157.4,158.16,157.34,157.97,157.21,156.14,156.99,156.17,154.18,153.99,154.48,154.72,154.16,153.79,153.51,153.26,153.04,152.85,153.18,153.13,152.83,152.57,152.48,152.47,152.07,151.78,151.53,151.29,151.09,151.25,150.99,150.66,150.38,150.15,149.95,149.76,149.56,149.37,149.19,149,148.8,148.63,148.48,148.31,148.32,148.45,148.94,148.64,148.29,147.6,146.87,146.96,146.95,146.84,146.41,146.65,146.86,147.01,147.32,147.82,147.39,146.99,146.44,146.06,145.51,145.11,144.69,144.05,143.48,142.97,142.45,141.88,141.44,140.69,139.98,139.32,138.82,138.25,137.38,135.95,136.13,130.14,130.33,121.51,122.27,122.83,122.24,121.51,122.32,118.21,44.8]),
    '120': ([120.89,142.81,143.02,143.22,143.42,143.63,143.83,143.96,144.16,144.3,144.5,144.64,144.84,144.98,145.18,145.32,145.53,145.67,145.87,146.02,146.22,146.36,146.57,146.71,146.87,147.01,147.15,147.29,147.43,147.57,147.71,147.86,148,148.14,148.28,148.43,148.57,148.72,148.87,149.01,149.16,149.31,149.45,149.6,149.75,149.9,150.05,150.2,150.35,150.51,150.66,150.81,150.96,151.12,151.27,151.43,151.59,151.74,151.9,152.06,152.22,152.38,152.54,152.71,152.87,153.03,153.2,153.36,153.53,153.7,153.87,154.03,154.2,154.37,154.55,154.72,154.89,155.07,155.24,155.42,155.48,155.31,155.15,154.99,154.82,154.65,154.49,154.32,154.15,153.98,153.81,153.64,153.46,153.29,153.11,152.94,152.76,152.58,152.4,152.22,152.03,151.85,151.67,151.48,151.29,151.1,150.91,150.72,150.53,150.33,150.14,148.09,147.61,147.14,146.67,146.21,145.76,145.31,144.86,144.42,44.8],
           [120.5,122.07,122.9,123.28,123.53,123.76,124.02,124.26,124.59,125.22,125.67,126.14,126.55,126.95,127.3,127.59,127.34,126.76,126.43,125.98,125.78,126.12,126.49,126.96,127.51,127.79,128.31,128.64,128.73,128.07,128.1,128.1,128.26,128.46,128.69,128.88,129.08,129.27,129.46,129.64,129.84,130.03,130.2,130.5,130.81,131.08,130.92,131.13,131.36,131.62,132.01,132.32,132.33,132.55,132.77,132.99,133.16,133.32,133.46,133.45,133.38,133.73,134.29,134.6,134.37,133.84,134.06,134.25,134.78,135.35,135.85,136.36,136.92,137.36,138.1,138.41,138.4,137.73,137.22,136.65,136.17,136.33,136.5,136.63,136.72,136.83,137,137.24,137.52,137.83,137.9,138,138.17,138.45,138.76,139.02,139.11,139.1,138.99,138.49,138.73,138.94,139.17,139.67,139.98,139.32,138.82,138.25,137.38,135.95,136.13,130.14,130.33,120.98,121.3,121.73,122.24,118.65,117.7,118.21,44.8]),
    '110': ([111.04,132.68,132.89,133.09,133.3,133.51,133.72,133.86,134.06,134.2,134.41,134.55,134.76,134.9,135.11,135.26,135.46,135.61,135.82,135.96,136.17,136.32,136.53,136.67,136.84,136.99,137.13,137.28,137.42,137.57,137.72,137.86,138.01,138.16,138.31,138.46,138.61,138.76,138.91,139.06,139.21,139.36,139.51,139.67,139.82,139.97,140.13,140.28,140.44,140.6,140.75,140.91,141.07,141.23,141.39,141.55,141.71,141.87,142.03,142.19,142.36,142.52,142.69,142.85,143.02,143.19,143.36,143.53,143.7,143.87,144.04,144.21,144.39,144.56,144.74,144.91,145.09,145.27,145.45,145.63,145.81,145.99,146.17,146.35,146.54,146.72,146.91,147.1,147.29,147.48,147.67,147.86,148.05,148.25,148.44,148.64,148.84,149.04,149.24,149.44,149.64,149.84,150.05,150.26,150.47,150.68,150.83,150.72,150.53,150.33,150.14,148.09,147.61,147.14,146.67,146.21,145.76,145.31,144.86,144.42,44.8],
           [110.64,112.21,113.03,113.41,113.66,113.9,114.22,114.75,115.5,116.01,116.57,117.1,117.58,117.99,118.61,119.07,119.54,119.95,120.36,120.71,120.99,121.05,121.34,118.84,118.98,119.19,119.53,119.9,120.37,120.93,121.22,121.73,122.06,122.08,122.41,121.83,121.45,121.58,121.76,121.96,122.15,122.34,122.55,122.76,122.96,123.15,123.38,123.66,123.99,124.26,124.26,124.55,124.55,124.81,125.1,125.51,125.52,125.61,125.88,126.18,126.24,125.91,126.16,126.33,126.59,126.87,127.24,127.82,127.58,127.08,127.46,127.47,127.68,127.92,128.39,129.08,129.74,130.23,130.8,131.65,131.64,129.55,130.09,129.33,129.3,129.67,129.84,130.02,130.18,130.25,130.36,130.51,130.75,131.1,131.17,131.27,131.44,131.7,132.04,132.3,132.4,132.39,132.3,132.46,132.65,132.62,132.5,132.78,133.28,133,133.18,130.14,130.33,120.98,121.3,121.73,122.24,118.65,117.7,118.21,44.8]),
    '95': ([96.3,117.42,117.64,117.86,118.07,118.29,118.5,118.65,118.87,119.02,119.23,119.38,119.6,119.75,119.97,120.12,120.33,120.49,120.71,120.86,121.08,121.24,121.45,121.61,121.79,121.94,122.1,122.25,122.41,122.56,122.72,122.87,123.03,123.19,123.35,123.5,123.66,123.82,123.98,124.14,124.3,124.46,124.62,124.78,124.94,125.11,125.27,125.43,125.6,125.76,125.93,126.09,126.26,126.43,126.59,126.76,126.93,127.1,127.27,127.44,127.61,127.78,127.96,128.13,128.3,128.48,128.65,128.83,129.01,129.19,129.36,129.54,129.72,129.91,130.09,130.27,130.46,130.64,130.83,131.01,131.2,131.39,131.58,131.77,131.96,132.15,132.34,132.54,132.73,132.93,133.13,133.33,133.52,133.73,133.93,134.13,134.33,134.54,134.74,134.95,135.16,135.37,135.58,135.79,136.01,136.22,138.44,138.93,139.41,139.89,140.36,140.83,141.29,141.75,142.21,142.43,142.65,142.87,143.08,143.3,44.8],
           [95.88,102.56,103.45,104.03,104.55,105.23,105.96,106.73,107.18,107.76,108.29,108.81,109.4,110.05,110.49,110.89,111.45,111.84,112.4,112.8,113.24,113.5,113.94,112.14,112.42,111.6,111.77,111.96,112.17,112.41,113.07,113.77,114.13,114.46,114.82,115.13,114.48,114.51,114.51,114.68,114.84,115.02,115.22,115.42,115.61,115.81,116.01,116.21,116.42,116.66,116.94,117.27,117.55,117.39,117.6,117.84,118.12,118.4,118.81,118.83,118.92,119.19,119.49,119.56,119.22,119.42,119.65,119.91,120.46,120.57,121.15,120.91,120.39,120.62,120.81,121.02,121.26,121.54,121.78,122.63,124.33,124.32,125.01,125.01,122.1,121.89,122.3,122.58,122.92,123.13,123.27,123.37,123.48,123.66,123.9,124.15,124.51,124.57,124.68,124.85,125.12,125.46,125.72,125.82,125.82,125.71,124.65,125.12,125.55,126.05,126.23,126.73,124.55,120.98,121.3,121.73,122.24,118.65,117.7,118.21,44.8]),
}
# First instant the valve passes flow, s, from moc.py rerun unchanged at stride=1 (dt = 12000/120/1050 = 0.095238 s):
# the first step whose head at node 0 reaches the set point, which is also the first step with srv q_peak > 0.
# datasets.json stores the history decimated 6:1, so reading the opening off DATA.t/case.H is up to 0.6 s late
# (it gives 47.3 / 49.6 / 54.9 s); the guard below keeps these values tied to that series.
_TOPEN = {'none': 0.0, '120': 54.476, '110': 49.429, '95': 46.857}

# Peak relief flow in the gas cavity model (dgcm.py ReliefBC.qr_peak), m3/s: by setting (DN250) and by size (set 95 m).
_QDG = {'none': 0.0000, '120': 0.1788, '110': 0.2203, '95': 0.2802}
_QDG_SIZE = {100: 0.2187, 150: 0.2740, 200: 0.2782, 250: 0.2802, 300: 0.2813}

_KEYS = ['none', '120', '110', '95']
_bad = []
for _k, _c in zip(_KEYS, _S['cases']):
    _v, _g = _ENV2[_k]
    if len(_v) != len(_c['Hmax']) or any(abs(a - b) > 0.06 for a, b in zip(_v, _c['Hmax'])): _bad.append(_k + ' vapour')
    if len(_g) != len(_c['Hmax_dgcm']) or any(abs(a - b) > 0.06 for a, b in zip(_g, _c['Hmax_dgcm'])): _bad.append(_k + ' gas')
    if sum(100 for h in _v if h > 136.0) != _c['len_above_136'] or sum(100 for h in _g if h > 136.0) != _c['len_above_136_dgcm']:
        _bad.append(_k + ' length above 136 m')
    if _c['set']:
        _td = next((_t for _t, _h in zip(_c['t'], _c['H']) if _h >= _c['set']), None)
        if _td is None or not (_TOPEN[_k] <= _td < _TOPEN[_k] + 0.8): _bad.append(_k + ' opening time')
if _bad:
    raise ValueError('s05_relief_valve: embedded solver values no longer match datasets.json srv (%s); rerun the srv block of gen_datasets.py' % ', '.join(_bad))

DATA = dict(
    t=_S['cases'][0]['t'], x=_S['x'], acc=_S['accumulation_m'],
    cases=[dict(set=_c['set'], pmax=_c['pump_max'], pmaxg=_c['pump_max_dgcm'], q=_c['q_peak'], qg=_QDG[_k], topen=_TOPEN[_k],
                H=_c['H'], Hmin=_c['Hmin'], Hv=_ENV2[_k][0], Hg=_ENV2[_k][1])
           for _k, _c in zip(_KEYS, _S['cases'])],
    sizes=[dict(dn=_s['dn'], pmax=_s['pump_max'], pmaxg=_s['pump_max_dgcm'], lmax=_s['line_max'], lmaxg=_s['line_max_dgcm'],
                q=_s['q_peak'], qg=_QDG_SIZE[_s['dn']])
           for _s in _S['sizes']],
)
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='surge-relief-valve-sizing', cat='surge', mins=32,
    date_iso='2026-09-16', date_human='September 2026', date_ar='سبتمبر 2026',
    title='Surge Relief Valve Sizing: What a Valve at the Pump Can and Cannot Protect',
    reg_title='Surge Relief Valve Sizing: What a Valve at the Pump Can and Cannot Protect',
    reg_tag='Surge Analysis · Surge Relief Valve · Pump Stations',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Surge Relief Valve &middot; Pump Stations',
    desc='How to size a surge relief valve at a pump station, and what it can and cannot protect: pump-trip column separation, collapse peaks under two cavity models, relief flow, capacity at full lift, Kv and Cv, set pressure and reseating, and the HAMMER set-up, worked on a 12 km DN800 main with three interactive charts.',
    og_desc='Set at 95 m, a best case, a DN250 relief valve holds the pump end of a 12 km DN800 main at 96.3 m. The line still reaches vapour end to end and peaks at 127–143 m depending on the cavity model, straddling the 136 m PN16 limit.',
    ld_desc='A design guide to surge relief valves on pumping mains: where pump-trip upsurges are generated, how to size relief flow, capacity and Kv, how to choose the set point, and how to model the valve in HAMMER.',
    img_alt='Cutaway of a pilot-operated surge relief valve on a pipe tee, water flowing out of the side discharge, with labelled pilot, set pressure, disc and discharge on a dark blue background',
    en_tag='Surge &amp; Transient Analysis &middot; Surge Relief Valves',
    en_title='Surge Relief Valve Sizing: What a Valve at the Pump Can and Cannot Protect',
    en_excerpt='A relief valve at the pump caps the pressure where it is installed, and on a 12 km DN800 main it does that well: even in the best case, set at 95 m, below the shut-off head of the pumps, it holds the pump end at <strong>96.3 m</strong>. But after a pump trip the line still reaches vapour from end to end, and the peak out along the line is <strong>127–143 m</strong> depending on the cavity model — straddling the 136 m PN16 allowable. The valve must pass <strong>0.416 m³/s</strong>, 59 % of the pumped flow. Relief flow, capacity at full lift, Kv and Cv, set pressure and reseating, where a relief valve is the right answer, and the HAMMER set-up, with three interactive charts.',
    en_search='surge relief valve sizing SRV surge anticipator valve SAV pump trip power failure water hammer upsurge downsurge column separation vapour cavity collapse discrete vapour cavity model discrete gas cavity model method of characteristics Joukowsky characteristic impedance relief flow capacity at full lift discharge coefficient Kv Cv flow coefficient set pressure overpressure reseating pressure shut-off head opening time blowdown spring loaded pilot operated relief valve pump station check valve transmission main DN800 ductile iron K9 PN16 136 m allowable maximum head envelope minimum head envelope Bentley HAMMER Surge Valve threshold pressure time to open surge protection hydropneumatic vessel flywheel EN 805 ISO 4126-1',
    ar_title='تحديد مقاس صمام تخفيف الضغط على خطوط الضخ: ما الذي يحميه صمام عند المضخة وما لا يحميه',
    ar_excerpt='يحدّ صمام تخفيف الضغط من ارتفاع الضغط في موضع تركيبه فقط. على خط نقل بطول ١٢ كم وقطر DN800، يُبقي الصمام المضبوط على ٩٥ م أقصى ضغط عند المضخة في حدود <strong>٩٦٫٣ م</strong>، وهذه أفضل الحالات لأن ٩٥ م أدنى من ضاغط المضخات عند التدفق الصفري. ومع ذلك يبلغ الخط ضغط التبخر على امتداده كله بعد توقف المضخات، وتصل الذروة على طول الخط إلى <strong>١٢٧–١٤٣ م</strong> بحسب نموذج التجويف، أي على جانبي حد ١٣٦ م لفئة PN16. ويُحدَّد مقاس الصمام لتدفق <strong>٠٫٤١٦ م³/ث</strong> (ذروة نموذج تجويف البخار، مقابل ٠٫٢٨٠ في نموذج التجويف الغازي)، أي ٥٩٪ من التدفق المضخوخ. مع ثلاثة رسوم تفاعلية وخطوات النمذجة في HAMMER.',
    ar_search='صمام تخفيف الضغط صمام تنفيس الضغط الطرق المائي صمام استباق التضاغط المطرقة المائية الظواهر العابرة توقف المضخات انقطاع الكهرباء انفصال عمود الماء تجويف البخار انهيار التجويف طريقة الخصائص معادلة جوكوفسكي تدفق التنفيس السعة عند الفتح الكامل معامل التصريف معامل التدفق ضغط الضبط ضغط إعادة الإغلاق محطات الضخ صمام عدم الرجوع خط نقل حديد الدكتايل غلاف الضغط الأقصى حماية المطرقة المائية خزان الحماية الهيدروهوائي خزان الضغط الهوائي ضاغط الإغلاق زمن الفتح الحدافة',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
