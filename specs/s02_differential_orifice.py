# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A surge vessel is specified by its gas volume, but whether that gas protects the pipeline is decided by the short pipe joining the vessel to the main. On the downsurge the vessel must discharge with as little loss as possible, because every bit of flow the connection holds back leaves as downsurge in the line. On the return, the water flowing back into the vessel carries the energy that becomes the upsurge, so that is the direction to throttle. On a 12&nbsp;km DN800 main with a 20&nbsp;m&sup3; vessel holding 3.5&nbsp;m&sup3; of gas, a differential connection (outflow K&nbsp;2, inflow K&nbsp;10) in place of a free one cuts the maximum from <strong>127.5&nbsp;m to 119.2&nbsp;m</strong> while the minimum moves only from +4.5&nbsp;m to <strong>+4.3&nbsp;m</strong>. A symmetric K&nbsp;25 orifice, a plate of about 210&nbsp;mm both ways, drops the line to <strong>&minus;4.5&nbsp;m</strong>.</p>

<h2 id="connection">1 &middot; The connection is part of the vessel</h2>
<p>Vessel data sheets list volumes and pressures; the connection appears as a nozzle size. Hydraulically that is backwards. The gas volume sets how much water the vessel <em>can</em> give. The connection decides how fast it gives it and how fast it takes it back, and those two rates set the two ends of the transient envelope.</p>

<h3>The reference system</h3>
<p>Every number here comes from one pipeline: a 12&nbsp;km DN800 ductile iron K9 main [1], laid flat, carrying 2,520&nbsp;m&sup3;/h (0.70&nbsp;m&sup3;/s, 1.39&nbsp;m/s) at a wave speed of 1,050&nbsp;m/s, with the grade line at 85.0&nbsp;m at the pump and 44.8&nbsp;m at delivery. The pipe class is PN16 with 136&nbsp;m allowable (design pressure terms as in [2]); the design minimum is +3.0&nbsp;m anywhere; 2L/a is 22.9&nbsp;s and a&middot;v/g is 149.1&nbsp;m. The load case is every pump tripping at once on a power failure (see <a href="surge-scenarios-pump-stations.html">which surge scenario governs</a>).</p>
<p>Unprotected, the downsurge reaches vapour (&minus;9.8&nbsp;m) and the collapse peak is <strong>165&ndash;190&nbsp;m</strong>, above PN16 either way. With a free DN400 connection the vessel needs 3.08&nbsp;m&sup3; of gas at the steady grade line, expanding to 15.30&nbsp;m&sup3;, in a 19.1&nbsp;m&sup3; shell with a 20&nbsp;% water reserve. The site's reference vessel carries <strong>3.5&nbsp;m&sup3; of gas in a 20&nbsp;m&sup3; shell</strong> (sizing method in <a href="surge-vessel.html">Sizing the Hydropneumatic Surge Vessel</a>, its gas setting in <a href="pre-charge-pressure.html">pre-charge pressure</a>). The extra gas expands further in almost the same shell and leaves 18&ndash;19&nbsp;% water (section&nbsp;4), just under that reserve. Only the connection changes here.</p>

<h3>How the numbers were produced</h3>
<p>The results come from a method-of-characteristics model with a vapour cavity model, cross-checked with a gas cavity model and an independent second code [3][4]: 120 reaches, 150&nbsp;s runs, polytropic gas with n&nbsp;=&nbsp;1.2, separate outflow and inflow coefficients, and an instantaneous pump stop behind an ideal check valve, a conservative idealisation for the downsurge. Where a line reaches vapour, the collapse peak depends on how the cavity is represented, and in our runs the gas cavity model puts collapse peaks between 18&nbsp;% lower and 10&nbsp;% higher than the vapour cavity model, so never design to rely on a collapse peak; protect the downsurge. <strong>None of the six connection cases here reaches vapour</strong>, so no result below carries that uncertainty: minima and maxima are quoted to 0.1&nbsp;m and gas volumes to 0.01&nbsp;m&sup3;. They are not Bentley HAMMER output; a project needs its own analysis in HAMMER, or an equivalent program, on the real profile [5].</p>

<h2 id="directions">2 &middot; What the connection does in each direction</h2>
<h3>Outflow: the vessel must replace the pump at once</h3>
<p>At the trip the pumps stop delivering 0.70&nbsp;m&sup3;/s. Whatever the vessel cannot supply immediately is a flow change at the pump end, and it leaves as a downsurge wave [3][6]:</p>
<div class="eq">\[ \Delta H = \frac{a}{g\,A}\,\Delta Q, \qquad \frac{a}{g\,A} = \frac{1050}{9.81 \times 0.5027} = 212.9\ \text{s/m}^2 \]</div>
<p>Stopping all 0.70&nbsp;m&sup3;/s gives the 149.1&nbsp;m Joukowsky head; every 0.1&nbsp;m&sup3;/s the connection holds back sends 21.3&nbsp;m of downsurge into the main. A connection loss is exactly that hold-back. In the first tenth of a second the head in the main at the vessel connection falls to 83.2&nbsp;m with the free connection, 81.0&nbsp;m with an outflow K of 2, and <strong>57.7&nbsp;m</strong> with a symmetric K of 25. The gas then keeps feeding the line and reaches its largest volume about 46&nbsp;s after the trip, close to 4L/a (35&nbsp;s behind the symmetric orifice).</p>

<h3>Inflow: the returning column winds up the gas spring</h3>
<p>Then the flow reverses. The column of about 6,000&nbsp;m&sup3; of water in the main swings back towards the pump and compresses the gas, and with nothing to absorb its energy it overshoots: the gas is squeezed below its steady 3.5&nbsp;m&sup3;, and the pressure at that instant is the pump-end maximum, 127.5&nbsp;m at 2.57&nbsp;m&sup3; about 100&nbsp;s after the trip with the free connection. An inflow loss turns part of that energy into turbulence in the connection instead.</p>

<div class="callout key">
  <span class="lbl">Causality does half the design for you</span>
  The outflow loss acts from the first instant and alone governs the downsurge. The inflow loss can do nothing until the flow reverses: in the four differential cases below, with the same outflow coefficient and inflow coefficients from 5 to 80, the head and gas volume at the vessel are <strong>identical until the flow reverses, about 46&nbsp;s after the trip</strong>. The two coefficients are separate design variables, and a symmetric orifice forces you to set them equal.
</div>

<h2 id="equations">3 &middot; The equations behind the connection</h2>
<p>Three relations describe the vessel end of the line [3][6][7]. The first is the connection loss, using the velocity in the connection bore of area \(A_c\) and a coefficient for each direction:</p>
<div class="eq">\[ H_{node} = H_{gas} - K_{out}\,\frac{Q^2}{2g\,A_c^{2}} \ \ \text{(outflow)}, \qquad H_{node} = H_{gas} + K_{in}\,\frac{Q^2}{2g\,A_c^{2}} \ \ \text{(inflow)} \]</div>
<p>The second is the polytropic gas law, with n&nbsp;=&nbsp;1.2 lying between isothermal and adiabatic behaviour [6][8], in absolute heads, with H<sub>0</sub> the steady pressure head above the vessel's water surface (the grade line minus that surface's elevation: 85.0&nbsp;m here, with the surface at the pipe datum), so the steady gas pressure is 85.0&nbsp;+&nbsp;10.33&nbsp;=&nbsp;95.3&nbsp;m abs (9.35&nbsp;bar abs):</p>
<div class="eq">\[ H_{gas}(V) = \big(H_0 + H_{atm}\big)\left(\frac{V_0}{V}\right)^{n} - H_{atm} \]</div>
<p>The third follows from the other two. When the gas volume is at its minimum, the flow through the connection is momentarily zero, so there is no loss and the head in the main at the connection equals the gas pressure. <strong>The pump-end maximum is the gas law evaluated at the smallest gas volume.</strong> With a small outflow loss, the lowest head at the vessel is the same law at the largest volume:</p>
<div class="eq">\[ H_{max} \approx H_{gas}\big(V_{min}\big), \qquad H_{min,\,vessel} \approx H_{gas}\big(V_{max}\big) \]</div>
<p>The relation is exact in the model: the smallest gas volumes give the simulated 119.2&nbsp;m (1:5) and 127.5&nbsp;m (free). From the rounded volumes in the table, 2.71 and 2.57&nbsp;m&sup3;, it gives 119.3 and 127.8&nbsp;m, since near 2.6&nbsp;m&sup3; the gas head moves about 63&nbsp;m per m&sup3;. At the other end, 16.17&nbsp;m&sup3; gives 4.9&nbsp;m, the lowest head at the vessel in the differential cases. Behind the symmetric orifice the relation breaks: the head in the main drops to &minus;3.4&nbsp;m at 22.9&nbsp;s (2L/a) while the gas pressure is still about +9.3&nbsp;m. The difference is the orifice.</p>
<p>Air-chamber methods [9] and simplified sizing guides [10][11] give the gas volume. The ratio \(r = K_{in}/K_{out}\) is chosen on top of it.</p>

<h2 id="six-cases">4 &middot; Six connections on one pipeline</h2>
<p>K values are referred to the DN400 velocity and cover the whole connection: entry, tee, isolating valve and any check valve or plate. The free connection is an idealised plain branch; the symmetric orifice is a plate with no bypass; the differential cases hold a realistic outflow K of 2 and throttle the inflow progressively harder.</p>
<div class="tbl-wrap"><table><caption>Six connections on the reference vessel (20 m&sup3; shell, 3.5 m&sup3; gas, DN400, n = 1.2), all pumps tripped, 150 s. Minimum and maximum are the envelope along the whole 12 km.</caption>
<thead><tr><th>Connection</th><th class="num">K out</th><th class="num">K in</th><th class="num">Ratio</th><th class="num">Line min (m)</th><th class="num">At (km)</th><th class="num">Line max (m)</th><th class="num">Gas min&ndash;max (m&sup3;)</th><th class="num">Gas back within 10&nbsp;% (s)</th></tr></thead>
<tbody>
<tr><td>Free both ways</td><td class="num">0.5</td><td class="num">0.5</td><td class="num">1</td><td class="num">+4.5</td><td class="num">1.4</td><td class="num">127.5</td><td class="num">2.57&ndash;16.36</td><td class="num">88</td></tr>
<tr><td>Symmetric orifice</td><td class="num">25</td><td class="num">25</td><td class="num">1</td><td class="num">&minus;4.5</td><td class="num">3.6</td><td class="num">103.1</td><td class="num">3.03&ndash;14.08</td><td class="num">85</td></tr>
<tr><td>Differential 1:2.5</td><td class="num">2</td><td class="num">5</td><td class="num">2.5</td><td class="num">+4.3</td><td class="num">4.3</td><td class="num">123.0</td><td class="num">2.65&ndash;16.17</td><td class="num">89</td></tr>
<tr><td>Differential 1:5</td><td class="num">2</td><td class="num">10</td><td class="num">5</td><td class="num">+4.3</td><td class="num">4.3</td><td class="num">119.2</td><td class="num">2.71&ndash;16.17</td><td class="num">90</td></tr>
<tr><td>Differential 1:10</td><td class="num">2</td><td class="num">20</td><td class="num">10</td><td class="num">+4.3</td><td class="num">4.3</td><td class="num">112.3</td><td class="num">2.84&ndash;16.17</td><td class="num">91</td></tr>
<tr><td>Over-throttled 1:40</td><td class="num">2</td><td class="num">80</td><td class="num">40</td><td class="num">+4.3</td><td class="num">4.3</td><td class="num">85.6</td><td class="num">3.48&ndash;16.17</td><td class="num">102</td></tr>
</tbody></table></div>
<p>No connection empties the vessel: 16.36&nbsp;m&sup3; of gas leaves 3.64&nbsp;m&sup3; of water in the 20&nbsp;m&sup3; shell (18&nbsp;%), and 16.17&nbsp;m&sup3; leaves 3.83&nbsp;m&sup3; (19&nbsp;%), both just under the 20&nbsp;% reserve of the sizing basis. The last column is the time from the trip until the gas first returns within 10&nbsp;% of its steady 3.5&nbsp;m&sup3;. It indexes how quickly the vessel refills after the first swing; every case is still oscillating at 150&nbsp;s.</p>

<h2 id="int-trial">5 &middot; Interactive: the connection on trial</h2>
<p>Pick a connection and a second one to compare it with. The readouts give the envelope along the whole line, which is where the criteria apply.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Head in the main at the vessel connection, and gas volume, after all pumps trip</div>
    <div class="fsub">Method-of-characteristics results on the reference system (12 km DN800, a = 1,050 m/s), vessel 20 m&sup3; with 3.5 m&sup3; of gas, DN400 connection, n = 1.2. Solid lines: the selected connection; dashed: the comparison. The gas axis tops out at the 20 m&sup3; shell. Line minimum and maximum are the envelope over all 12 km; the loss is K<sub>in</sub>&middot;(Q/A)&sup2;/2g across the whole connection at the peak return flow.</div>
  </div>
  <div class="chart-box"><canvas id="trialChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Connection</label>
      <select id="sCase"><option value="0">Free both ways (K 0.5 / 0.5)</option><option value="1">Symmetric orifice (K 25 / 25)</option><option value="2">Differential 1:2.5 (K 2 / 5)</option><option value="3" selected>Differential 1:5 (K 2 / 10)</option><option value="4">Differential 1:10 (K 2 / 20)</option><option value="5">Over-throttled 1:40 (K 2 / 80)</option></select>
      <div class="hint">Outflow / inflow loss coefficients, referred to the DN400 bore.</div>
    </div>
    <div class="ctrl">
      <label>Compare with</label>
      <select id="sCmp"><option value="none">No comparison</option><option value="0" selected>Free both ways (K 0.5 / 0.5)</option><option value="1">Symmetric orifice (K 25 / 25)</option><option value="2">Differential 1:2.5 (K 2 / 5)</option><option value="3">Differential 1:5 (K 2 / 10)</option><option value="4">Differential 1:10 (K 2 / 20)</option><option value="5">Over-throttled 1:40 (K 2 / 80)</option></select>
      <div class="hint">Drawn dashed; the readout gives the change in line maximum.</div>
    </div>
    <div class="ctrl">
      <label>Time window <span id="vWin">150 s</span></label>
      <input type="range" id="sWin" min="30" max="150" value="150" step="5">
      <div class="hint">Shorten it to see the first seconds, when only the outflow loss acts.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Line minimum</div><div class="v" id="rMin">+4.3 <small>m at 4.3 km</small></div></div>
    <div class="cell"><div class="k">Line maximum</div><div class="v" id="rMax">119.2 <small>m</small></div></div>
    <div class="cell"><div class="k">Against the limits</div><div class="v" style="font-size:15px;margin-top:6px;" id="rStat"><span class="badge good">meets +3.0 m and 136 m</span></div></div>
    <div class="cell"><div class="k">Maximum vs compared</div><div class="v" id="rDmax">&minus;8.3 <small>m</small></div></div>
    <div class="cell"><div class="k">Gas volume</div><div class="v" id="rGas">2.71&ndash;16.17 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Gas back within 10&nbsp;%</div><div class="v" id="rRefill">90 <small>s</small></div></div>
    <div class="cell"><div class="k">Connection loss at peak return flow</div><div class="v" id="rDhin">5.2 <small>m</small></div></div>
  </div>
</div>
<p class="fig-note">At the default, 1:5 is set against the free connection. Until the flow reverses at about 46&nbsp;s the two stay within 2.2&nbsp;m; then the 1:5 gas is squeezed to 2.71&nbsp;m&sup3; instead of 2.57&nbsp;m&sup3; and the maximum is <strong>119.2&nbsp;m, 8.3&nbsp;m lower</strong>, with the minimum at +4.3&nbsp;m and 5.2&nbsp;m lost across the connection at peak return flow. Pick the symmetric orifice: the head in the main drops from 85.0 to 57.7&nbsp;m in the first tenth of a second, the gas expands only to 14.08&nbsp;m&sup3;, and the line minimum falls to <strong>&minus;4.5&nbsp;m</strong> at 3.6&nbsp;km, which makes its 103.1&nbsp;m maximum worthless. Shorten the window to 30&nbsp;s to see that first drop.</p>

<h2 id="reading">6 &middot; Reading the results: outflow sets the minimum, inflow sets the maximum</h2>
<h3>The minimum belongs to the outflow path</h3>
<p>Every connection with K<sub>out</sub>&nbsp;=&nbsp;2 has the same minimum, +4.3&nbsp;m at 4.3&nbsp;km, whatever its inflow coefficient; a seventh run with K&nbsp;2 both ways gives the same. The free connection reaches +4.5&nbsp;m at 1.4&nbsp;km, so a realistic outflow path costs 0.2&nbsp;m. The symmetric orifice reaches &minus;4.5&nbsp;m at 3.6&nbsp;km: 7.5&nbsp;m short of +3.0&nbsp;m and below atmospheric, though not at vapour.</p>
<p>The minimum is out along the line: about 4.9&nbsp;m at the vessel itself in the differential cases, and about half a metre lower kilometres away. The vessel protects the line through the flow it supplies, so check the whole profile [12]. Nor does the loss come off the minimum one for one: the symmetric orifice loses 26.4&nbsp;m across the connection at peak outflow, passing 0.572&nbsp;m&sup3;/s where the free connection passes 0.691&nbsp;m&sup3;/s, and the minimum falls by 9.0&nbsp;m. The missing flow is the damage.</p>
<div class="tbl-wrap"><table><caption>Flow out of the vessel and the loss it causes: &Delta;h = K&middot;(Q/A)&sup2;/2g in the DN400 bore at each case's peak outflow, in the first time step, from the vessel flow computed by the solver (0.681 m&sup3;/s is 5.42 m/s).</caption>
<thead><tr><th>Connection</th><th class="num">K out</th><th class="num">Peak outflow (m&sup3;/s)</th><th class="num">&Delta;h out at peak (m)</th><th class="num">Line min (m)</th></tr></thead>
<tbody>
<tr><td>Free both ways</td><td class="num">0.5</td><td class="num">0.691</td><td class="num">0.8</td><td class="num">+4.5</td></tr>
<tr><td>Symmetric orifice</td><td class="num">25</td><td class="num">0.572</td><td class="num">26.4</td><td class="num">&minus;4.5</td></tr>
<tr><td>Differential 1:2.5, 1:5, 1:10 and 1:40</td><td class="num">2</td><td class="num">0.681</td><td class="num">3.0</td><td class="num">+4.3</td></tr>
</tbody></table></div>

<h3>The maximum belongs to the inflow path</h3>
<p>With the outflow held at K&nbsp;2, the maximum falls as the inflow is throttled: 125.4&nbsp;m with K&nbsp;2 both ways (the seventh run), 123.0&nbsp;m at 1:2.5, 119.2&nbsp;m at 1:5, 112.3&nbsp;m at 1:10 and 85.6&nbsp;m at 1:40, while the gas minimum rises from 2.65 to 3.48&nbsp;m&sup3;. The free connection already clears 136&nbsp;m on this flat line, so the gain is margin: 1:5 takes 8.3&nbsp;m off its maximum, 6.3&nbsp;m from the ratio and 2.0&nbsp;m from raising both coefficients from 0.5 to 2. In our practice that margin is worth having, because it absorbs what analysis cannot pin down: the wave speed achieved (see <a href="wave-speed-surge-analysis.html">wave speed</a>), the gas actually held in service, and pump and valve behaviour at the trip.</p>

<h3>The over-throttled limit</h3>
<p>At 1:40 the upsurge has almost gone, 85.6&nbsp;m against a steady 85.0&nbsp;m. But the gas returns within 10&nbsp;% at 102&nbsp;s instead of 88&ndash;91&nbsp;s, and the loss across the connection at peak return flow is 22.9&nbsp;m. The practical limits are the jet velocity (14.2&nbsp;m/s through the plate sized in section&nbsp;8), cavitation and noise at the plate, erosion, and slower recovery before a second event such as a restart attempt.</p>
<div class="callout warn">
  <span class="lbl">There is no standard ratio</span>
  The ratio is a design choice for one line, vessel and load case, not a constant to copy. On this system 1:5 is the reference design because it puts the maximum 16.8&nbsp;m under the allowable for 5.2&nbsp;m lost across the connection at peak return flow; 1:10 buys another 6.9&nbsp;m of margin for 9.3&nbsp;m. A steeper profile, a smaller gas volume or a different trip sequence moves every one of these numbers, so run the sweep on your own model.
</div>

<h2 id="int-ratio">7 &middot; Interactive: minimum and maximum across the connections</h2>
<p>Each bar runs from the line minimum to the line maximum for one connection. Set your own limits and add a series showing what each connection costs.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Line envelope for each connection against your limits</div>
    <div class="fsub">Same runs as the chart above. Blue bars meet both limits; red bars fail at least one. The extra series uses the right-hand axis: time until the gas is back within 10 % of its steady volume, the gas volume range, or the loss across the connection at peak return flow, K<sub>in</sub>&middot;(Q/A)&sup2;/2g in the DN400 bore.</div>
  </div>
  <div class="chart-box"><canvas id="envChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Design minimum <span id="vLo">+3.0 m</span></label>
      <input type="range" id="sLo" min="0" max="6" value="3" step="0.1">
      <div class="hint">Lowest head allowed anywhere on the line; +3.0 m on the reference system.</div>
    </div>
    <div class="ctrl">
      <label>Allowable maximum <span id="vHi">136 m</span></label>
      <input type="range" id="sHi" min="80" max="150" value="136" step="1">
      <div class="hint">PN16 allowable is 136 m. Lower it to hold a margin.</div>
    </div>
    <div class="ctrl">
      <label>Extra series</label>
      <select id="sExtra"><option value="refill" selected>Time until gas is back within 10 %</option><option value="loss">Connection loss at peak return flow</option><option value="gas">Gas volume range</option><option value="none">None</option></select>
      <div class="hint">What each connection costs.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Connections passing</div><div class="v" id="rPass">5 <small>of 6</small></div></div>
    <div class="cell"><div class="k">Lowest maximum meeting both limits</div><div class="v" id="rBest">85.6 <small>m, Over-throttled 1:40</small></div></div>
    <div class="cell"><div class="k">Failing on minimum / maximum</div><div class="v" id="rFail">1 / 0</div></div>
    <div class="cell"><div class="k">Extra series range</div><div class="v" id="rExtra">85&ndash;102 <small>s</small></div></div>
  </div>
</div>
<p class="fig-note">At +3.0&nbsp;m and 136&nbsp;m five of the six connections pass, and the lowest maximum meeting both limits is 85.6&nbsp;m at 1:40. The extra series is the reason not to stop there: the refill time rises from 90&nbsp;s at 1:5 to 102&nbsp;s at 1:40, and the loss across the connection at peak return flow (switch the series) from 5.2&nbsp;m to 22.9&nbsp;m. Raise the minimum to +4.4&nbsp;m and every connection with K<sub>out</sub>&nbsp;2 fails while the free one passes. Pull the allowable down to 110&nbsp;m and only 1:40 survives.</p>

<h2 id="sizing">8 &middot; Sizing the orifice plate</h2>
<p>Once the model has fixed the inflow coefficient, the plate is sized from a standard relation. For a thin, sharp-edged orifice in a straight pipe at high Reynolds number, Idelchik gives the loss referred to the pipe velocity, with \(\beta = d/D\) [13]:</p>
<div class="eq">\[ K_{or} = \frac{\left(1 + 0.707\sqrt{1-\beta^{2}} - \beta^{2}\right)^{2}}{\beta^{4}}, \qquad \Delta h = K\,\frac{v^{2}}{2g} \]</div>
<p>The sensitivity to the bore is extreme: &beta;&nbsp;0.3 gives 309.9, 0.4 gives 86.5, 0.5 gives 29.7, 0.6 gives 11.2, 0.7 gives 4.29 and 0.8 gives 1.50.</p>
<div class="callout warn">
  <span class="lbl">Where the plate sits changes its coefficient</span>
  The relation is for a plate in a straight spool with enough pipe after it for the jet to re-expand and recover pressure; the &minus;&beta;&sup2; term is that recovery. A plate or flap discharging straight into the vessel shell recovers none: without the term, \(\left(1 + 0.707\sqrt{1-\beta^{2}}\right)^{2}/\beta^{4}\) gives 14.7 at &beta;&nbsp;0.635 instead of 8.0 (including the exit loss the fittings K would otherwise count), so the same K<sub>in</sub> needs a larger bore. Size such a plate, and any proprietary fitting, from the manufacturer's tested coefficient for the installed geometry.
</div>

<h3>Worked example: the DN400 connection</h3>
<p>Take the plate in a straight DN400 spool of the branch and the fittings as K&nbsp;&asymp;&nbsp;2 both ways, the outflow coefficient of the differential cases. Bypassed on outflow, the plate supplies the rest of the inflow coefficient, K<sub>or</sub>&nbsp;=&nbsp;K<sub>in</sub>&nbsp;&minus;&nbsp;2:</p>
<div class="tbl-wrap"><table><caption>Orifice plates for the four differential connections: plate in a straight DN400 spool, fittings K 2; bore velocity Q/(&pi;d&sup2;/4) and loss across the whole connection at each case's own peak inflow, from the vessel flow computed by the solver.</caption>
<thead><tr><th>Connection</th><th class="num">Target K in</th><th class="num">Orifice K</th><th class="num">&beta;</th><th class="num">Bore d (mm)</th><th class="num">Peak inflow (m&sup3;/s)</th><th class="num">Bore velocity (m/s)</th><th class="num">Connection loss on return (m)</th></tr></thead>
<tbody>
<tr><td>Differential 1:2.5</td><td class="num">5</td><td class="num">3</td><td class="num">0.736</td><td class="num">294</td><td class="num">0.416</td><td class="num">6.1</td><td class="num">2.8</td></tr>
<tr><td>Differential 1:5</td><td class="num">10</td><td class="num">8</td><td class="num">0.635</td><td class="num">254</td><td class="num">0.403</td><td class="num">7.9</td><td class="num">5.2</td></tr>
<tr><td>Differential 1:10</td><td class="num">20</td><td class="num">18</td><td class="num">0.551</td><td class="num">220</td><td class="num">0.380</td><td class="num">10.0</td><td class="num">9.3</td></tr>
<tr><td>Over-throttled 1:40</td><td class="num">80</td><td class="num">78</td><td class="num">0.409</td><td class="num">164</td><td class="num">0.298</td><td class="num">14.2</td><td class="num">22.9</td></tr>
</tbody></table></div>
<p>The bore velocity is the mean through the hole; the jet contracts after the plate, so the vena contracta is faster still. Tolerance matters: a 250&nbsp;mm bore gives K<sub>in</sub>&nbsp;10.8 and 258&nbsp;mm gives 9.3, so &plusmn;4&nbsp;mm moves the coefficient by 7&ndash;8&nbsp;%. Specify the bore from the coefficient and make the plate replaceable. And a symmetric K&nbsp;25 is only an orifice K of 23, &beta;&nbsp;0.526, a bore of about 210&nbsp;mm: a modest-looking plate that took the minimum from the +4.3&nbsp;m of the K&nbsp;2 fittings alone to &minus;4.5&nbsp;m.</p>

<h2 id="int-orifice">9 &middot; Interactive: orifice sizing</h2>
<p>Choose the connection, the fittings loss and the plate, and decide what the outflow passes through. The readouts include the coefficients re-referred to the plate bore, for entry into a model.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Orifice loss coefficient against bore ratio, with your connection</div>
    <div class="fsub">Idelchik's thin sharp-edged orifice in a pipe, referred to the connection velocity. Inflow path = fittings + plate. Outflow path = fittings only (plate bypassed), the same plate both ways, or fittings + a fixed restriction. Losses are K&middot;(Q/A)&sup2;/2g at the flows you set. The ratio badge refers to the range modelled here, not a general rule; &Delta;h out is flagged above the 3.0 m of the K 2 outflow path modelled, because it sets the minimum.</div>
  </div>
  <div class="chart-box"><canvas id="orfChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Connection <span id="vDN">DN400</span></label>
      <select id="sDN"><option value="300">DN300</option><option value="400" selected>DN400</option><option value="500">DN500</option></select>
      <div class="hint">The bore every coefficient is referred to.</div>
    </div>
    <div class="ctrl">
      <label>Fittings K <span id="vFit">2.0</span></label>
      <input type="range" id="sFit" min="0" max="4" value="2" step="0.1">
      <div class="hint">Entry, tee, isolating valve and open check valve or flap, both directions.</div>
    </div>
    <div class="ctrl">
      <label>Inflow plate &beta; <span id="vBin">0.635 &middot; 254 mm</span></label>
      <input type="range" id="sBin" min="0.3" max="0.9" value="0.6354" step="0.0001">
      <div class="hint">Bore divided by the connection diameter.</div>
    </div>
    <div class="ctrl">
      <label>Outflow path</label>
      <select id="sOut"><option value="full" selected>Plate bypassed: fittings only</option><option value="sym">Same plate both ways</option><option value="0.8">Fixed restriction &beta; 0.8</option><option value="0.7">Fixed restriction &beta; 0.7</option><option value="0.6">Fixed restriction &beta; 0.6</option></select>
      <div class="hint">What the water passes through when the vessel discharges.</div>
    </div>
    <div class="ctrl">
      <label>Peak outflow <span id="vQo">0.681 m&sup3;/s</span></label>
      <input type="range" id="sQo" min="0.1" max="1.2" value="0.681" step="0.001">
      <div class="hint">From the vessel flow history; 0.681 with the K 2 outflow path on the reference system.</div>
    </div>
    <div class="ctrl">
      <label>Peak inflow <span id="vQi">0.403 m&sup3;/s</span></label>
      <input type="range" id="sQi" min="0.1" max="1" value="0.403" step="0.001">
      <div class="hint">From the vessel flow history; 0.403 for the 1:5 connection.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">K out</div><div class="v" id="rKo">2.0</div></div>
    <div class="cell"><div class="k">K in</div><div class="v" id="rKi">10.0</div></div>
    <div class="cell"><div class="k">Ratio K in / K out</div><div class="v" id="rRat">5.0 <span class="badge good">inside the 1:2.5&ndash;1:10 modelled</span></div></div>
    <div class="cell"><div class="k">&Delta;h out at peak</div><div class="v" id="rDho">3.0 <small>m</small></div></div>
    <div class="cell"><div class="k">&Delta;h in at peak</div><div class="v" id="rDhi">5.2 <small>m</small></div></div>
    <div class="cell"><div class="k">Bore velocity</div><div class="v" id="rBore">7.9 <small>m/s in a 254 mm bore</small></div></div>
    <div class="cell"><div class="k">K out / K in referred to the bore</div><div class="v" id="rRef">0.33 / 1.63</div></div>
  </div>
</div>
<p class="fig-note">At the default (DN400, fittings K&nbsp;2, a &beta;&nbsp;0.635 plate in a straight spool bypassed on outflow, the reference peak flows) the calculator gives K<sub>out</sub>&nbsp;2.0, K<sub>in</sub>&nbsp;10.0 and a ratio of 5.0: the 1:5 connection, losing 3.0&nbsp;m at 0.681&nbsp;m&sup3;/s out and 5.2&nbsp;m at 0.403&nbsp;m&sup3;/s back, through a 254&nbsp;mm bore at 7.9&nbsp;m/s. Switch the outflow to the same plate both ways and the ratio collapses to 1.0, with 15.0&nbsp;m lost on outflow at the same flow. Bypass the plate again and change to DN300: the ratio does not move, but the losses become 9.5&nbsp;m out, which is flagged, and 16.6&nbsp;m in, with 14.1&nbsp;m/s through the bore. Back at DN400, set &beta; to 0.409 and the peak inflow to 0.298&nbsp;m&sup3;/s to reproduce the over-throttled row of the table.</p>

<h2 id="arrangements">10 &middot; Physical arrangements and details</h2>
<h3>Three ways to build a differential connection</h3>
<ul class="clean">
  <li><strong>(a) A check valve with an orifice bypass.</strong> A full-bore check valve in the main branch opens towards the main, so the vessel discharges through the whole connection. On reversal it closes and the water returns through a smaller bypass carrying the orifice. The check valve's fully open loss counts in K<sub>out</sub>. The worked plates in section&nbsp;8 sit in the DN400 branch. In a bypass, take &beta; on the bypass bore and multiply the bypass pipe, fittings and plate coefficients by (400/d<sub>bypass</sub>)<sup>4</sup> to refer them to DN400: a DN200 bypass with fittings K&nbsp;2 already contributes 32, three times the whole 1:5 target.</li>
  <li><strong>(b) A single differential orifice fitting.</strong> A hinged flap or plate with a bore in it swings clear on outflow and seats on the return. It is compact, but it is a moving part that must close cleanly at every reversal, and at the vessel nozzle its jet discharges into the shell (section&nbsp;8).</li>
  <li><strong>(c) A nozzle-shaped outflow path with a sharp-edged inflow path.</strong> No moving parts, but the achievable ratio is limited by the geometry and has to be shown by test data for that fitting, not assumed.</li>
</ul>

<h3>The check valve or flap must not slam</h3>
<p>In (a) and (b) the moving element closes as the flow reverses. If it is still open when the returning column arrives, the column shuts it, and the slam puts a pressure spike into exactly the place the design was meant to calm. Choose a fast-closing, non-slam type and model its closure; see <a href="check-valve-hammer.html">check valve slam and water hammer</a>.</p>

<h3>Cavitation, jet velocity and erosion at the plate</h3>
<p>The return flow does not peak when the vessel is nearly full. In these runs it peaks about 74&nbsp;s after the trip, with the gas still expanded to 8.4&ndash;10.1&nbsp;m&sup3; in the differential cases and the gas pressure on the vessel side of the plate at only about 16&ndash;23&nbsp;m. A useful screen compares the absolute head behind the plate with the loss:</p>
<div class="eq">\[ \sigma = \frac{H_{down,\,abs} - H_{vap,\,abs}}{\Delta h_{in}} \]</div>
<p>With the vapour head at 0.53&nbsp;m abs and the whole connection loss as &Delta;h<sub>in</sub>, which overstates the plate's own share (80&nbsp;% of K<sub>in</sub> at 1:5, 97.5&nbsp;% at 1:40) and so errs on the safe side, the index at peak return flow is about 6 at 1:5, 3 at 1:10 and 1 at 1:40, where the loss is close to the whole absolute pressure behind the plate. Whether a plate cavitates depends on its geometry and must come from test data, but in our judgement a falling index is a warning in itself. The jet leaves the bore at 7.9&nbsp;m/s at 1:5 and 14.2&nbsp;m/s at 1:40, so keep it off the shell and away from the water surface where the level is measured.</p>

<h3>Nozzle size, isolation and records</h3>
<p>The coefficients are referred to the connection bore, so the bore is part of the loss: at 0.681&nbsp;m&sup3;/s, K&nbsp;2 costs 3.0&nbsp;m in DN400, 9.5&nbsp;m in DN300 and 1.2&nbsp;m in DN500, since at fixed K and flow the loss varies as 1/D<sup>4</sup>. The isolating valve sits in the outflow path too, so make it full bore, locked open, with its loss counted in K<sub>out</sub>. Confirm and record the plate bore at installation. Plates and coatings in contact with drinking water need approval [14], the shell and nozzles follow the project's pressure vessel code [15], and pipeline design pressures follow [2].</p>

<h2 id="hammer">11 &middot; Setting it up in Bentley HAMMER</h2>
<p>This procedure reproduces the comparison on a project model. Field names differ slightly between HAMMER versions; the intent of each step does not [5]. For the wider workflow see <a href="hammer-transient-simulation-workflow.html">the HAMMER transient simulation workflow</a> and <a href="hammer-transient-tips.html">HAMMER transient tips</a>.</p>
<ol>
  <li><strong>Build and check the steady state:</strong> Pump, Pipe and Reservoir on the real profile, each Pipe's wave speed from the Wave Speed Calculator. Confirm the grade line at the pump and at delivery.</li>
  <li><strong>Place a Hydropneumatic Tank</strong> downstream of the pump check valves: elevation, tank volume (20&nbsp;m&sup3;), initial gas volume (3.5&nbsp;m&sup3;), gas law exponent (1.2), and &ldquo;has bladder&rdquo; off for an air-over-water vessel (other types: <a href="surge-vessel-type-selection.html">vessel type selection</a>).</li>
  <li><strong>Describe the connection.</strong> Inlet orifice diameter: the bore the coefficients are referred to (400&nbsp;mm). Minor loss coefficient: the outflow coefficient (2). Ratio of losses: inflow loss over outflow loss (5, giving K<sub>in</sub>&nbsp;10). To enter the plate bore instead, re-refer both with \(K_d = K_D\,\beta^{4}\): 0.33 and 1.63 for the 254&nbsp;mm plate, ratio still 5. Use coefficients for the installed geometry (section&nbsp;8).</li>
  <li><strong>Prove the direction of the ratio.</strong> Run ratio 1 and ratio 5 with the same minor loss coefficient. Acting on inflow, the ratio leaves the minimum alone and lowers the maximum (125.4&nbsp;m to 119.2&nbsp;m here, section&nbsp;6); if the minimum moves, invert the entry.</li>
  <li><strong>Set the pump trip</strong> at time zero with the real pump and motor inertia and the pump check valve closure. This article used an instantaneous stop behind an ideal check valve, a conservative idealisation for the downsurge; real inertia and valve closure can move the maximum either way, so repeat the comparison with them (see <a href="pump-inertia-flywheel-surge.html">pump inertia</a>).</li>
  <li><strong>Set the transient run options:</strong> a run duration that covers the recompression and the start of the second swing (150&nbsp;s here, about six and a half times 2L/a), the computed time step, a small wave speed adjustment tolerance, vapour pressure and column separation on, one friction method throughout.</li>
  <li><strong>Run one scenario per connection:</strong> free, symmetric, three or four ratios with your real outflow coefficient, and one over-throttled case.</li>
  <li><strong>Read the results.</strong> In the Transient Results Viewer, plot the profile (path) with maximum and minimum head envelopes against +3.0&nbsp;m and the pipe class; read the time history at the tank for head, gas volume and flow, and compute &Delta;h&nbsp;=&nbsp;K&middot;v&sup2;/2g at the peak flows.</li>
  <li><strong>Check the vessel never empties and keeps its reserve:</strong> the largest gas volume against the tank volume, and the water left against the project's criterion (3.83&nbsp;m&sup3;, 19&nbsp;%, at 1:5). An empty shell lets air into the main (see <a href="air-admission-networks.html">air admission</a>).</li>
  <li><strong>Close with the gas-law check:</strong> with H<sub>0</sub> the steady pressure head above the vessel's water surface, \((H_0 + H_{atm})(V_0/V_{min})^{n} - H_{atm}\) should match the maximum grade line at the tank less that surface's elevation, once the change in water level is allowed for (in the model used here it is exact). If not, suspect the tank data before trusting the envelope.</li>
</ol>

<h2 id="checklist">12 &middot; Design checklist</h2>
<ul class="clean">
  <li><strong>Treat the connection as part of the vessel:</strong> K<sub>out</sub>, K<sub>in</sub>, their reference diameter and the arrangement go on the data sheet and in the surge report.</li>
  <li><strong>Size the outflow path first:</strong> full bore, short, few fittings, isolating valve locked open. Confirm the minimum with the real K<sub>out</sub>.</li>
  <li><strong>Never throttle the outflow to cure an upsurge.</strong> A symmetric K&nbsp;25 turned the free connection's +4.5&nbsp;m into &minus;4.5&nbsp;m.</li>
  <li><strong>Choose K<sub>in</sub> from a sweep:</strong> the smallest ratio that meets the allowable with the margin your uncertainties call for (see <a href="surge-analysis-risk.html">surge analysis and risk</a>).</li>
  <li><strong>Run the gas-law check</strong> H<sub>max</sub>&nbsp;&asymp;&nbsp;H<sub>gas</sub>(V<sub>min</sub>) on every run, with both heads measured from the vessel's water surface.</li>
  <li><strong>Check the plate:</strong> a coefficient for where it is installed, bore velocity, loss against the absolute pressure behind it at peak return flow, noise, erosion; replaceable, bore recorded.</li>
  <li><strong>Check recovery</strong> against the earliest credible restart or second trip; slow refill is the price of heavy throttling.</li>
  <li><strong>Check the moving parts</strong> close at reversal without slamming, and that the vessel keeps the project's water reserve at maximum gas volume.</li>
  <li><strong>Keep model coefficients consistent</strong> with the diameter entered, and prove the direction of the ratio of losses; check the minimum along the whole profile, not just at the vessel.</li>
  <li><strong>Verify on site:</strong> measure the installed bore and log vessel level and pressure through the first trips (see <a href="transient-analysis-scada.html">transient analysis with SCADA data</a>).</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge protection design series</span>
  <ol>
    <li><a href="wave-speed-surge-analysis.html">Wave speed: the number that sets the surge</a></li>
    <li><strong>The differential orifice: empty freely, refill slowly</strong></li>
    <li><a href="surge-vessel-type-selection.html">Bladder, diaphragm or air-over-water vessel</a></li>
    <li><a href="one-way-surge-tank-design.html">One-way surge tanks at the knee</a></li>
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
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'IBM Plex Sans',size:11}}};
const TTL=t=>({display:true,text:t,font:{family:'IBM Plex Sans',size:12,weight:'600'}});
const G=9.81, MINUS='−';
const sgn=v=>{const r=Math.round(v*10)/10;return (r>0?'+':(r<0?MINUS:''))+fmt1(Math.abs(r));};
const fmtK=k=>k>=1?fmt1(k):fmt2(k);
const badge=(cls,txt)=>'<span class="badge '+cls+'">'+txt+'</span>';
const lossK=(K,q,A)=>K*Math.pow(q/A,2)/(2*G);          // head loss K v^2/2g, v = q/A
const lineAnn=(v,col,txt,pos)=>({type:'line',scaleID:'y',value:v,borderColor:col,borderWidth:1.4,borderDash:[6,4],
  label:{display:true,content:txt,position:pos||'start',font:{size:10,family:'IBM Plex Sans'},color:col,backgroundColor:'rgba(255,255,255,0.85)'}});
const nonEmpty=(it,d)=>(d.datasets[it.datasetIndex].data||[]).some(p=>p!==null);
const C=D.cases, T=D.t;
const AC=Math.PI*0.4*0.4/4;                             // DN400 connection bore, m2
const H0=85.0;                                          // steady head at the pump end, m
const SHORT=['Free','Symmetric','1:2.5','1:5','1:10','1:40'];
const NARROW=(window.innerWidth||1024)<640;

/* ---------- CHART 1 : the connection on trial ---------- */
const sCase=document.getElementById('sCase'),sCmp=document.getElementById('sCmp'),sWin=document.getElementById('sWin');
let trialChart=new Chart(document.getElementById('trialChart'),{
  type:'line',
  data:{datasets:[
    {label:'Head in the main at the vessel',data:[],borderColor:'#1b4f72',borderWidth:2.4,pointRadius:0,yAxisID:'y',order:1},
    {label:'Gas volume',data:[],borderColor:'#b9770e',borderWidth:2.2,pointRadius:0,yAxisID:'y1',order:2},
    {label:'Compared: head',data:[],borderColor:'#7f8c8d',borderWidth:1.6,borderDash:[5,4],pointRadius:0,yAxisID:'y',order:3},
    {label:'Compared: gas',data:[],borderColor:'#6b4f9e',borderWidth:1.4,borderDash:[5,4],pointRadius:0,yAxisID:'y1',order:4}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:150,title:TTL('Time after the trip (s)'),...AX},
            y:{type:'linear',min:-10,max:140,position:'left',title:TTL('Head in the main at the vessel (m)'),...AX},
            y1:{type:'linear',min:0,max:20,position:'right',title:TTL('Gas volume (m³)'),grid:{drawOnChartArea:false},ticks:{font:{family:'IBM Plex Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'IBM Plex Sans',size:11},usePointStyle:true,boxWidth:8,filter:nonEmpty}},
      tooltip:{callbacks:{title:it=>it.length?fmt1(it[0].parsed.x)+' s':'',
        label:c=>c.dataset.yAxisID==='y1'?`${c.dataset.label}: ${fmt2(c.parsed.y)} m³`:`${c.dataset.label}: ${fmt1(c.parsed.y)} m`}},
      annotation:{annotations:{
        pn:lineAnn(136,'#c0392b','PN16 allowable 136 m','end'),
        ss:lineAnn(85,'#7f8c8d','Steady 85.0 m','end'),
        mn:lineAnn(3,'#1e8449','+3.0 m minimum','end')
      }}}}
});
function updTrial(){
  const c=C[+sCase.value], w=+sWin.value, k=sCmp.value;
  const cc=(k==='none')?null:C[+k];
  document.getElementById('vWin').textContent=w+' s';
  // the stored series start one time step after the trip; prepend the steady state at t = 0
  const pts=(a,y0)=>{const o=[{x:0,y:y0}];for(let i=0;i<T.length;i++){if(T[i]<=w+0.5)o.push({x:T[i],y:a[i]});}return o;};
  const ds=trialChart.data.datasets;
  ds[0].data=pts(c.H,H0);  ds[0].label='Head: '+c.label;
  ds[1].data=pts(c.Vg,D.gas0); ds[1].label='Gas: '+c.label;
  ds[2].data=cc?pts(cc.H,H0):[];  ds[2].label='Head: '+(cc?cc.label:'');
  ds[3].data=cc?pts(cc.Vg,D.gas0):[]; ds[3].label='Gas: '+(cc?cc.label:'');
  trialChart.options.scales.x.max=w;
  trialChart.update('none');
  const okMin=c.min>=3.0, okMax=c.max<=136.0;
  document.getElementById('rMin').innerHTML=sgn(c.min)+' <small>m at '+fmt1(c.at_min/1000)+' km</small>';
  document.getElementById('rMax').innerHTML=fmt1(c.max)+' <small>m</small>';
  document.getElementById('rStat').innerHTML=(okMin&&okMax)?badge('good','meets +3.0 m and 136 m')
      :(!okMin?badge('bad','minimum below +3.0 m'):badge('bad','maximum above 136 m'));
  document.getElementById('rDmax').innerHTML=cc?sgn(c.max-cc.max)+' <small>m</small>':'&ndash;';
  document.getElementById('rGas').innerHTML=fmt2(c.gas_min)+'&ndash;'+fmt2(c.gas_max)+' <small>m³</small>'+(c.emptied?' '+badge('bad','emptied'):'');
  document.getElementById('rRefill').innerHTML=fmt0(c.refill_s)+' <small>s</small>';
  document.getElementById('rDhin').innerHTML=fmt1(lossK(c.K_in,c.q_in_peak,AC))+' <small>m</small>';
}
[sCase,sCmp,sWin].forEach(s=>s.addEventListener('input',updTrial));updTrial();

/* ---------- CHART 2 : envelope across the connections ---------- */
const sLo=document.getElementById('sLo'),sHi=document.getElementById('sHi'),sExtra=document.getElementById('sExtra');
const EXTRA={
  refill:{label:'Gas back within 10 % (s)',axis:'Time after the trip (s)',max:120,val:c=>c.refill_s,show:v=>fmt0(v),unit:'s'},
  loss:{label:'Connection loss at peak return (m)',axis:'Connection loss on return (m)',max:30,val:c=>lossK(c.K_in,c.q_in_peak,AC),show:v=>fmt1(v),unit:'m'},
  gas:{label:'Gas volume, min to max (m³)',axis:'Gas volume (m³)',max:20,unit:'m³'}
};
let envChart=new Chart(document.getElementById('envChart'),{
  data:{labels:C.map((c,i)=>[SHORT[i]||c.label,'K '+c.K_out+'/'+c.K_in]),
    datasets:[
      {type:'bar',label:'Meets both limits',data:[],backgroundColor:'rgba(27,79,114,0.55)',borderColor:'#1b4f72',borderWidth:1.5,yAxisID:'y',skipNull:true,barPercentage:0.7,categoryPercentage:0.8,order:3},
      {type:'bar',label:'Fails a limit',data:[],backgroundColor:'rgba(192,57,43,0.45)',borderColor:'#c0392b',borderWidth:1.5,yAxisID:'y',skipNull:true,barPercentage:0.7,categoryPercentage:0.8,order:3},
      {type:'bar',label:'Gas volume, min to max (m³)',data:[],backgroundColor:'rgba(185,119,14,0.35)',borderColor:'#b9770e',borderWidth:1.2,yAxisID:'y1',skipNull:true,barPercentage:0.7,categoryPercentage:0.8,order:2},
      {type:'line',label:'Gas back within 10 % (s)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2,pointRadius:5,pointHoverRadius:6,yAxisID:'y1',order:1}
    ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{...AX,ticks:{font:{family:'IBM Plex Sans',size:NARROW?9.5:10.5},autoSkip:false,maxRotation:NARROW?50:0,minRotation:NARROW?50:0}},
            y:{type:'linear',min:-10,max:150,position:'left',title:TTL('Line head, minimum to maximum (m)'),...AX},
            y1:{type:'linear',min:0,max:120,position:'right',display:true,title:TTL('Time after the trip (s)'),grid:{drawOnChartArea:false},ticks:{font:{family:'IBM Plex Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'IBM Plex Sans',size:11},usePointStyle:true,boxWidth:8,filter:nonEmpty}},
      tooltip:{callbacks:{title:it=>it.length?C[it[0].dataIndex].label:'',label:c=>{const r=c.raw;
        if(Array.isArray(r)) return c.dataset.yAxisID==='y1'?`Gas ${fmt2(r[0])}–${fmt2(r[1])} m³`:`Line ${sgn(r[0])} m to ${fmt1(r[1])} m`;
        return `${c.dataset.label}: ${fmt1(c.parsed.y)}`;}}},
      annotation:{annotations:{
        lo:lineAnn(3,'#1e8449','Design minimum +3.0 m','start'),
        hi:lineAnn(136,'#c0392b','Allowable 136 m','start'),
        ss:lineAnn(85,'#7f8c8d','Steady 85.0 m','end')
      }}}}
});
function updEnv(){
  const lo=+sLo.value, hi=+sHi.value, ex=sExtra.value;
  document.getElementById('vLo').textContent=sgn(lo)+' m';
  document.getElementById('vHi').textContent=fmt0(hi)+' m';
  const okMin=C.map(c=>c.min>=lo), okMax=C.map(c=>c.max<=hi);
  const pass=C.map((c,i)=>okMin[i]&&okMax[i]);
  const ds=envChart.data.datasets;
  ds[0].data=C.map((c,i)=>pass[i]?[c.min,c.max]:null);
  ds[1].data=C.map((c,i)=>pass[i]?null:[c.min,c.max]);
  const E=EXTRA[ex], y1=envChart.options.scales.y1;
  if(ex==='gas'){ds[2].data=C.map(c=>[c.gas_min,c.gas_max]);ds[3].data=[];}
  else if(ex==='none'||!E){ds[2].data=[];ds[3].data=[];}
  else{ds[2].data=[];ds[3].data=C.map(c=>+E.val(c).toFixed(2));ds[3].label=E.label;}
  y1.display=!!E;
  if(E){y1.max=E.max;y1.title.text=E.axis;}
  const an=envChart.options.plugins.annotation.annotations;
  an.lo.value=lo; an.lo.label.content='Design minimum '+sgn(lo)+' m';
  an.hi.value=hi; an.hi.label.content='Allowable '+fmt0(hi)+' m';
  envChart.update('none');
  const nP=pass.filter(Boolean).length;
  document.getElementById('rPass').innerHTML=nP+' <small>of '+C.length+'</small>';
  let best=null; C.forEach((c,i)=>{if(pass[i]&&(best===null||c.max<best.max))best=c;});
  document.getElementById('rBest').innerHTML=best?fmt1(best.max)+' <small>m, '+best.label+'</small>':badge('bad','none passes');
  const fMin=okMin.filter(v=>!v).length, fMax=C.filter((c,i)=>okMin[i]&&!okMax[i]).length;
  document.getElementById('rFail').innerHTML=fMin+' / '+fMax;
  let rng='&ndash;';
  if(ex==='gas'){rng=fmt2(Math.min(...C.map(c=>c.gas_min)))+'&ndash;'+fmt2(Math.max(...C.map(c=>c.gas_max)))+' <small>m³</small>';}
  else if(E){const v=C.map(E.val);rng=E.show(Math.min(...v))+'&ndash;'+E.show(Math.max(...v))+' <small>'+E.unit+'</small>';}
  document.getElementById('rExtra').innerHTML=rng;
}
[sLo,sHi,sExtra].forEach(s=>s.addEventListener('input',updEnv));updEnv();

/* ---------- CHART 3 : orifice sizing ---------- */
const sDN=document.getElementById('sDN'),sFit=document.getElementById('sFit'),sBin=document.getElementById('sBin'),
      sOut=document.getElementById('sOut'),sQo=document.getElementById('sQo'),sQi=document.getElementById('sQi');
const KOR=b=>Math.pow(1+0.707*Math.sqrt(1-b*b)-b*b,2)/Math.pow(b,4);   // Idelchik, thin sharp-edged orifice, pipe velocity
const BET=[];for(let i=0;i<=60;i++)BET.push(+(0.30+0.01*i).toFixed(2));
const WORKED=[{x:0.736,y:5},{x:0.635,y:10},{x:0.551,y:20},{x:0.409,y:80}];
let orfChart=new Chart(document.getElementById('orfChart'),{
  type:'scatter',
  data:{datasets:[
    {type:'line',label:'Plate alone (Idelchik)',data:BET.map(b=>({x:b,y:+KOR(b).toFixed(3)})),borderColor:'#1b4f72',borderWidth:2.4,pointRadius:0,order:4},
    {type:'line',label:'Inflow path: fittings + plate',data:[],borderColor:'#5eaadd',borderWidth:2,borderDash:[6,4],pointRadius:0,order:3},
    {type:'scatter',label:'Worked plates (fittings K 2)',data:WORKED,backgroundColor:'#7f8c8d',borderColor:'#fff',borderWidth:1.5,pointRadius:5,order:2},
    {type:'scatter',label:'Your inflow path',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1},
    {type:'scatter',label:'Your outflow restriction',data:[],backgroundColor:'#1e8449',borderColor:'#fff',borderWidth:2,pointRadius:7,pointStyle:'rectRot',order:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0.3,max:0.9,title:TTL('Bore ratio β = d / D'),...AX},
            y:{type:'logarithmic',min:0.1,max:1000,title:TTL('Loss coefficient K (connection velocity)'),...AX}},
    plugins:{legend:{labels:{font:{family:'IBM Plex Sans',size:11},usePointStyle:true,boxWidth:8,filter:nonEmpty}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: β ${fmt3(c.parsed.x)}, K ${fmtK(c.parsed.y)}`}},
      annotation:{annotations:{
        ko:{type:'line',scaleID:'y',value:2,borderColor:'#1e8449',borderWidth:1.4,borderDash:[6,4],
            label:{display:true,content:'K out 2.0',position:'end',font:{size:10,family:'IBM Plex Sans'},color:'#1e8449',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updOrf(){
  const Dm=+sDN.value/1000, fit=+sFit.value, bi=+sBin.value, mode=sOut.value, qo=+sQo.value, qi=+sQi.value;
  const A=Math.PI*Dm*Dm/4, d=bi*Dm;
  const Kin=fit+KOR(bi);
  let Kout, bo=null;
  if(mode==='full'){Kout=fit;}
  else if(mode==='sym'){Kout=Kin;bo=bi;}
  else{bo=+mode;Kout=fit+KOR(bo);}
  const ratio=Kout>0?Kin/Kout:Infinity;
  const dho=lossK(Kout,qo,A), dhi=lossK(Kin,qi,A), vb=qi/(Math.PI*d*d/4), b4=Math.pow(bi,4);
  document.getElementById('vDN').textContent='DN'+sDN.value;
  document.getElementById('vFit').textContent=fmt1(fit);
  document.getElementById('vBin').textContent=fmt3(bi)+' · '+fmt0(d*1000)+' mm';
  document.getElementById('vQo').textContent=fmt3(qo)+' m³/s';
  document.getElementById('vQi').textContent=fmt3(qi)+' m³/s';
  const ds=orfChart.data.datasets;
  ds[1].data=BET.map(b=>({x:b,y:+(fit+KOR(b)).toFixed(3)}));
  ds[3].data=[{x:bi,y:+Kin.toFixed(3)}];
  ds[4].data=(bo!==null)?[{x:bo,y:+Kout.toFixed(3)}]:[];
  const ko=orfChart.options.plugins.annotation.annotations.ko;
  ko.value=Math.max(Kout,0.1); ko.label.content='K out '+fmtK(Kout);
  orfChart.update('none');
  const outHigh=dho>3.05;                               // the K 2 outflow path modelled loses 3.0 m at 0.681 m3/s
  let rb;
  if(!isFinite(ratio)) rb=badge('warn','no outflow loss entered');
  else if(ratio<1.25) rb=badge('warn','no differential');
  else if(ratio<2.45) rb=badge('warn','weaker than the 1:2.5 modelled');
  else if(ratio<=10.5) rb=outHigh?badge('warn','ratio modelled, outflow loss is not'):badge('good','inside the 1:2.5–1:10 modelled');
  else if(ratio<39.5) rb=badge('warn','beyond 1:10: check recovery and plate');
  else rb=badge('warn','as steep as the over-throttled 1:40');
  document.getElementById('rKo').innerHTML=fmtK(Kout);
  document.getElementById('rKi').innerHTML=fmtK(Kin);
  document.getElementById('rRat').innerHTML=(isFinite(ratio)?fmt1(ratio):'∞')+' '+rb;
  document.getElementById('rDho').innerHTML=fmt1(dho)+' <small>m</small>'+(outHigh?' '+badge('warn','above the 3.0 m modelled: check the minimum'):'');
  document.getElementById('rDhi').innerHTML=fmt1(dhi)+' <small>m</small>';
  document.getElementById('rBore').innerHTML=fmt1(vb)+' <small>m/s in a '+fmt0(d*1000)+' mm bore</small>';
  document.getElementById('rRef').innerHTML=fmt2(Kout*b4)+' / '+fmt2(Kin*b4);
}
[sDN,sFit,sBin,sOut,sQo,sQi].forEach(s=>s.addEventListener('input',updOrf));updOrf();

window.addEventListener('load',function(){try{trialChart.resize();envChart.resize();orfChart.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ISO 2531 <em>Ductile iron pipes, fittings, accessories and their joints for water applications</em> — pipe classes and wall thickness of the DN800 K9 reference main.</li>
  <li>EN 805 <em>Water supply — Requirements for systems and components outside buildings</em> — design pressure terminology, including the maximum design pressure with its allowance for surge.</li>
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993 — method of characteristics, the air chamber boundary with an orifice loss, and column separation.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006 — vapour and gas cavity models, and why collapse peaks depend on the model.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> product documentation and help — Hydropneumatic Tank properties (inlet orifice diameter, minor loss coefficient, ratio of losses), transient run options and the Transient Results Viewer.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014 — air chambers on pumping mains, polytropic gas behaviour and the pump-end boundary.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004 — surge suppression devices, including air vessels.</li>
  <li>Larock, B.E., Jeppson, R.W. &amp; Watters, G.Z. <em>Hydraulics of Pipeline Systems</em>. CRC Press, 2000 — accumulator boundary conditions and the gas law in transient models.</li>
  <li>Parmakian, J. <em>Waterhammer Analysis</em>. Dover, 1963 — classical graphical analysis of air chambers on pump discharge lines.</li>
  <li>Stephenson, D. &ldquo;Simple guide for design of air vessels for water hammer protection of pumping lines.&rdquo; <em>Journal of Hydraulic Engineering</em> (ASCE), 128(8), 2002 — simplified sizing of air vessels on pumping lines.</li>
  <li>Stephenson, D. <em>Pipeline Design for Water Engineers</em>, 3rd ed. Elsevier, 1989 — pumping main design, including water hammer protection with air vessels.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005 — checking protection over the whole system and selecting hydropneumatic tanks.</li>
  <li>Idelchik, I.E. <em>Handbook of Hydraulic Resistance</em>, 3rd ed. Begell House, 1996 — loss coefficient of a thin sharp-edged orifice in a pipe.</li>
  <li>NSF/ANSI/CAN 61 <em>Drinking Water System Components — Health Effects</em> — approval of plates, coatings and internals in contact with drinking water.</li>
  <li>EN 13445 <em>Unfired pressure vessels</em>; ASME <em>Boiler and Pressure Vessel Code</em>, Section VIII, Division 1; Pressure Equipment Directive 2014/68/EU — design and conformity of the vessel shell and nozzles.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeVessel #DifferentialOrifice #WaterHammer #HydraulicTransients #SurgeProtection #HydropneumaticTank #AirVessel #OrificePlate #HeadLoss #Idelchik #PumpTrip #Downsurge #Upsurge #ColumnSeparation #MethodOfCharacteristics #BentleyHAMMER #OpenFlowsHAMMER #TransmissionMains #DuctileIron #PumpStations #PipelineDesign #CheckValves #SurgeAnalysis #TransientAnalysis #HydraulicDesign #WaterSupply #WaterEngineering #WaterInfrastructure</div>
"""

import json, os
_D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'datasets.json')))
_O = _D['orifice']
DATA = {
    't': _O['cases'][0]['t'],
    'gas0': _O['gas0'], 'vtot': _O['vtot'],
    'cases': [{k: c[k] for k in ('label', 'K_out', 'K_in', 'ratio', 'min', 'at_min', 'max', 'gas_min', 'gas_max',
                                 'emptied', 'refill_s', 'q_out_peak', 'q_in_peak', 'H', 'Vg')} for c in _O['cases']],
}
# Peak vessel flows come from moc.py's own vessel flow Qv (datasets.json q_out_peak / q_in_peak).
assert {c['label']: (c['q_out_peak'], c['q_in_peak']) for c in DATA['cases']}['Differential 1:5'] == (0.681, 0.403), 'dataset peak flows changed: update the prose'
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='surge-vessel-differential-orifice', cat='surge', mins=36,
    date_iso='2026-09-16', date_human='September 2026', date_ar='سبتمبر 2026',
    title='The Differential Orifice: Why a Surge Vessel Should Empty Freely and Refill Slowly',
    reg_title='The Differential Orifice: Why a Surge Vessel Should Empty Freely and Refill Slowly',
    reg_tag='Surge Analysis · Surge Vessel · Orifice Design',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Surge Vessel &middot; Orifice Design',
    desc='How the connection between a surge vessel and the main sets both ends of the transient envelope: why outflow loss deepens the downsurge and throttled inflow cuts the upsurge, six connections compared on a 12 km DN800 main, orifice plate sizing, the HAMMER set-up, and three interactive charts.',
    og_desc='On a 12 km DN800 main with a 20 m³ vessel, a K 2 outflow / K 10 inflow connection cuts the maximum from 127.5 m to 119.2 m while the minimum moves only from +4.5 m to +4.3 m. A symmetric K 25 orifice drops the line to −4.5 m.',
    ld_desc='A design guide to the differential orifice on a surge vessel: loss and gas-law equations, six connections simulated on a reference main, plate sizing from the Idelchik formula, and the HAMMER set-up.',
    img_alt='Cutaway render of a vertical pipe teeing into a branch fitted with an orifice plate and a small bypass check valve, labelled free outflow and throttled return, with a vessel line drawing and two decaying pressure traces inset',
    en_tag='Surge &amp; Transient Analysis &middot; Differential Orifice',
    en_title='The Differential Orifice: Why a Surge Vessel Should Empty Freely and Refill Slowly',
    en_excerpt='On a 12 km DN800 main with a 20 m³ vessel carrying 3.5 m³ of gas, a K 2 outflow / K 10 inflow connection in place of a free one cuts the maximum from <strong>127.5 m to 119.2 m</strong> while the minimum moves only from +4.5 m to <strong>+4.3 m</strong>; a symmetric K 25 orifice sends the line to <strong>−4.5 m</strong>. The pipe between a surge vessel and the main is a design element, not a fitting: flow the connection holds back becomes downsurge, and the water flowing back into the vessel is the energy that makes the upsurge. Six connections compared, the orifice plate sized from the Idelchik formula, the HAMMER set-up and three interactive charts.',
    en_search='differential orifice surge vessel connection hydropneumatic tank air vessel air chamber orifice plate inflow outflow loss coefficient ratio of losses throttled return free outflow bypass check valve flap downsurge upsurge pump trip power failure water hammer transient analysis method of characteristics column separation gas law polytropic exponent Idelchik orifice loss beta ratio bore velocity cavitation erosion vessel nozzle DN400 DN800 ductile iron transmission main PN16 Bentley HAMMER OpenFlows inlet orifice diameter minor loss coefficient surge protection design checklist',
    ar_title='الفتحة التفاضلية: لماذا ينبغي أن يَفرغ خزان الحماية الهيدروهوائي بحرية ويمتلئ ببطء',
    ar_excerpt='على خط بقطر ٨٠٠ مم وطول ١٢ كم مع خزان سعته ٢٠ م³، يؤدي استبدال الوصلة الحرة بوصلة تفاضلية (معامل الفاقد ٢ للخروج و١٠ للدخول) إلى خفض الضغط الأقصى من <strong>١٢٧٫٥ م إلى ١١٩٫٢ م</strong>، بينما لا يتغير الحد الأدنى إلا من +٤٫٥ م إلى <strong>+٤٫٣ م</strong>، في حين تُهبط الفتحة المتماثلة (K ٢٥) الضغط في الخط إلى <strong>−٤٫٥ م</strong>. فالوصلة بين خزان الحماية والخط الرئيسي عنصر تصميمي وليست مجرد قطعة تركيب: التدفق الذي تحجزه يعمّق انخفاض الضغط في الخط، والماء العائد إلى الخزان هو الطاقة التي تصنع ارتفاع الضغط. ويتضمن المقال ثلاثة رسوم تفاعلية وخطوات النمذجة في HAMMER.',
    ar_search='الفتحة التفاضلية المطرقة المائية خزان حماية هيدروهوائي خزان الحماية الهيدروهوائي خزان الضغط الهوائي خزان الحماية من الطرق المائي وعاء الهواء لوح الفتحة المعايرة لوحة الفتحة نسبة الفواقد فاقد الضغط معامل الفاقد التدفق الداخل التدفق الخارج صمام عدم الرجوع توقف المضخات انقطاع الكهرباء انخفاض الضغط ارتفاع الضغط التحليل العابر طريقة الخصائص انفصال عمود الماء قانون الغاز خط نقل المياه حديد الدكتايل تصميم الحماية من المطرقة المائية',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
