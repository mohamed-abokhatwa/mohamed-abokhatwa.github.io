# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Once the transient model has fixed the gas duty, the vessel type looks like a procurement detail. It is not. On this series' reference main the duty is 3.08&nbsp;m&sup3; of gas at the steady HGL, expanding to 15.30&nbsp;m&sup3;. An air-over-water vessel carries that in a <strong>19.1&nbsp;m&sup3;</strong> shell; a bladder vessel pre-charged below the minimum pressure needs <strong>23.2&ndash;28.4&nbsp;m&sup3;</strong> at any pre-charge from atmospheric up to 0.95 of the minimum. The bladder saves a compressor and dissolved-air losses. You pay in shell volume, a membrane that wears, and pre-charge checks that need the vessel out of service.</p>

<h2 id="same-duty">1 &middot; Same duty, three machines</h2>
<p>When the pumps trip, a vessel's compressed gas pushes water into the line until the column turns, then takes the returning water back. The duty is a statement about gas, not steel: how much gas sits in the vessel at the steady hydraulic grade line, and how far it may expand before the pressure reaches the design minimum [1]. That is the same whichever vessel carries it. What changes is the shell, what keeps the gas there between trips, and what fails.</p>
<p>The reference system is a 12&nbsp;km DN800 ductile iron K9 main [2]: 2,520&nbsp;m&sup3;/h (1.39&nbsp;m/s), wave speed 1,050&nbsp;m/s, 85.0&nbsp;m at the pump, 44.8&nbsp;m at the delivery reservoir, PN16 with 136&nbsp;m allowable, and a +3.0&nbsp;m minimum anywhere. With all pumps tripped and no protection, the line reaches vapour and the collapse peak is 165&ndash;190&nbsp;m. A vessel at the pump with a free DN400 connection (K&nbsp;0.5) holds +3.0&nbsp;m with <strong>3.08&nbsp;m&sup3; of gas at 95.33&nbsp;m abs</strong> (9.35&nbsp;bar abs), expanding to <strong>15.30&nbsp;m&sup3;</strong>. With a 20&nbsp;% water reserve at maximum expansion, the air-over-water shell is 15.30/0.8 = 19.1&nbsp;m&sup3;. The sizing method is in <a href="surge-vessel.html">Sizing the Hydropneumatic Surge Vessel</a>; this article starts where it ends.</p>
<div class="callout key">
  <span class="lbl">Where the numbers come from</span>
  A method-of-characteristics model with a vapour cavity model, cross-checked with a gas cavity model and an independent second code. These are not HAMMER results; a project analysis must be run in HAMMER, or an equivalent, on the real profile. Collapse peaks are ranges because the spike when a cavity closes depends on how the cavity is represented [3]; on this series' cases the gas cavity model puts collapse peaks between 18&nbsp;% lower and 10&nbsp;% higher than the vapour cavity model. Never design on a collapse peak: protect the downsurge so no cavity forms. Vessel duties and protected minima involve no cavitation and are quoted to 0.1&nbsp;m or 0.01&nbsp;m&sup3;.
</div>

<h2 id="how-gas-is-held">2 &middot; How each type holds its gas</h2>
<h3>Air-over-water</h3>
<p>A pressure vessel partly filled with water, with compressed air above a free surface. Nothing separates gas from water, so the gas volume is whatever the level says it is. It needs a level transmitter, a compressor to add air, a vent to release it, and controls to hold the level in a band. Air dissolves under pressure, so top-up continues for as long as the vessel is in service [4], [5].</p>
<h3>Bladder</h3>
<p>A flexible bladder separates gas from water. Before any water enters, the gas side is charged to a pre-charge pressure and fills the whole shell. As the line comes up to pressure the bladder is squeezed into a fraction of the shell set by the ratio of pre-charge to steady pressure. No compressor, no level control, no dissolved-air loss &mdash; but the gas volume now rests on a pressure you set once, cannot see in service, and must check [5], [6].</p>
<h3>Diaphragm</h3>
<p>The same physics, with a membrane fixed across the shell instead of a bag. Diaphragm vessels are typically chosen for smaller volumes; everything said below about pre-charge applies to them too.</p>
<p>One identity ties the three together. The duty fixes a mass of gas: 3.08&nbsp;m&sup3; at 95.33&nbsp;m abs is 3.08 &times; 95.33/10.33 = <strong>28.4&nbsp;m&sup3; of free air</strong>. An air-over-water vessel stores it compressed, put there by a compressor. A bladder vessel pre-charged at atmospheric pressure needs a shell of exactly 28.4&nbsp;m&sup3;, because the shell is the container that free air is sealed into before it is squeezed. A higher pre-charge shrinks the shell in proportion; the next section is about how high it can go.</p>

<h2 id="precharge-penalty">3 &middot; The pre-charge penalty</h2>
<p>Between trips a bladder vessel's gas sits at ambient temperature, however quickly the line came up to pressure, so the steady state lies on the isotherm through the pre-charge. The expansion on a trip is faster (on the reference duty the gas reaches its largest volume about 46&nbsp;s after the trip), so design uses a polytropic exponent n = 1.2 between the isothermal and adiabatic limits [1], [4]:</p>
<div class="eq">\[ V_{shell} = V_0\,\frac{P_0}{P_{pre}}, \qquad V_{min} = V_0\left(\frac{P_0}{P_{min}}\right)^{1/n}, \qquad V_{shell,\,AOW} = \frac{V_{min}}{1-r} \]</div>
<p>All pressures are absolute: \(V_0\) is the gas at the steady pressure \(P_0\) = 95.33&nbsp;m abs, \(P_{min}\) = 3.0 + 10.33 = 13.33&nbsp;m abs, \(P_{pre}\) the pre-charge and \(r\) the air-over-water reserve. The pre-charge must stay below the lowest pressure the vessel will see, or the bladder is fully expanded, and delivering nothing, before the line reaches its minimum. Write \(P_{pre} = f\,P_{min}\) and divide the two shells:</p>
<div class="eq">\[ \frac{V_{shell,\,bladder}}{V_{shell,\,AOW}} = \frac{1-r}{f}\left(\frac{P_0}{P_{min}}\right)^{1-1/n} \]</div>
<p>The gas volume drops out. The penalty grows with the pressure ratio, so a high-head main protected to a low minimum is the worst case for a bladder: its shell is set by isothermal charging, the air-over-water shell by the smaller polytropic expansion. Here 7.15 to the power 1/6 is 1.39, so even pre-charged at the minimum itself the bladder shell is 39&nbsp;% larger than the gas at the minimum. That extra is water the bladder keeps, doing the job of the air-over-water reserve: against the air-over-water shell the penalty at f = 1 is 11&nbsp;%, and the pre-charge margin adds the rest, to 23&nbsp;% at f = 0.90. Simplified methods give the first estimate of an air vessel [7]; the transient model is the check.</p>
<div class="tbl-wrap"><table>
  <caption>Shell volume for the reference duty: 3.08 m&sup3; of gas at 95.33 m abs, minimum 13.33 m abs, n = 1.2. Air-over-water row from the transient model; bladder rows from the closed form</caption>
  <thead><tr><th>Vessel and pre-charge</th><th class="num">Pre-charge (m abs)</th><th class="num">Pre-charge (m gauge)</th><th class="num">Shell (m&sup3;)</th><th class="num">Gas at the minimum (m&sup3;)</th><th class="num">Water left at the minimum (m&sup3;)</th><th class="num">Shell vs air-over-water</th></tr></thead>
  <tbody>
    <tr><td>Air-over-water, 20 % reserve (transient model)</td><td class="num">&ndash;</td><td class="num">&ndash;</td><td class="num">19.1</td><td class="num">15.30</td><td class="num">3.8</td><td class="num">&ndash;</td></tr>
    <tr><td>Bladder, 0.60 &times; P<sub>min</sub></td><td class="num">8.00</td><td class="num">&minus;2.33</td><td class="num">36.7</td><td class="num">15.9</td><td class="num">20.8</td><td class="num">+92 %</td></tr>
    <tr><td>Bladder, atmospheric (0.775 &times; P<sub>min</sub>)</td><td class="num">10.33</td><td class="num">0.00</td><td class="num">28.4</td><td class="num">15.9</td><td class="num">12.6</td><td class="num">+49 %</td></tr>
    <tr><td>Bladder, 0.80 &times; P<sub>min</sub></td><td class="num">10.66</td><td class="num">+0.33</td><td class="num">27.5</td><td class="num">15.9</td><td class="num">11.7</td><td class="num">+44 %</td></tr>
    <tr><td>Bladder, 0.90 &times; P<sub>min</sub></td><td class="num">12.00</td><td class="num">+1.67</td><td class="num">24.5</td><td class="num">15.9</td><td class="num">8.6</td><td class="num">+28 %</td></tr>
    <tr><td>Bladder, 0.95 &times; P<sub>min</sub></td><td class="num">12.66</td><td class="num">+2.33</td><td class="num">23.2</td><td class="num">15.9</td><td class="num">7.3</td><td class="num">+21 %</td></tr>
  </tbody>
</table></div>
<p>The bladder rows use the closed-form 15.9&nbsp;m&sup3; at the minimum, slightly above the transient model's 15.30&nbsp;m&sup3;: the closed form assumes the vessel itself is drawn down to +3.0&nbsp;m, while in the model the line minimum occurs 4.6&nbsp;km out and the vessel bottoms at 13.9&nbsp;m abs (+3.6&nbsp;m). The shells follow from the 3.08&nbsp;m&sup3; and the pre-charge alone, and in the transient model the 24.5&nbsp;m&sup3; bladder vessel gives exactly the air-over-water result, +3.0&nbsp;m minimum and 130.9&nbsp;m maximum, because the bladder never reaches the shell wall.</p>
<p>Now the gauge column. Every pre-charge that meets the rule and can be set by ordinary charging lies between atmospheric (f = 0.775, the 28.4&nbsp;m&sup3; free-air shell) and 0.29&nbsp;bar&nbsp;g. The 0.60 row would need a vacuum, so with at least a 5&nbsp;% margin the practical shells run from 23.2 to 28.4&nbsp;m&sup3;, on a pre-charge that has to be exactly right. A transient study of one bladder shell at different pre-charges is in <a href="pre-charge-pressure.html">Pre-Charge Pressure</a>.</p>

<h2 id="int-shell">4 &middot; Interactive: shell volume by vessel type</h2>
<p>Each bar shows what fills the shell at the lowest pressure: expanded gas, and the water still inside. The gas at the minimum is the closed form, so at the reference duty the air-over-water shell reads 19.8&nbsp;m&sup3; rather than the transient model's 19.1&nbsp;m&sup3;, which is drawn dashed while the gas, HGL, minimum and exponent sit at the reference values. The transient model's own output is the 15.30&nbsp;m&sup3; of gas at maximum expansion, so that dashed line follows the reserve slider too: it is 15.30/(1&nbsp;&minus;&nbsp;reserve).</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Shell volume for the same gas duty: air-over-water vs bladder or diaphragm</div>
    <div class="fsub">Gas at the minimum from polytropic expansion. Bladder shell from isothermal charging to the steady HGL. Air-over-water shell = gas at the minimum / (1 &minus; reserve). Pressures absolute, atmosphere 10.33 m. Dashed line: the transient model's 15.30 m&sup3; of gas at maximum expansion divided by (1 &minus; reserve), so it moves with the reserve slider; shown only at the reference duty.</div>
  </div>
  <div class="chart-box"><canvas id="shellChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Gas at the steady HGL <span id="vV0">3.08 m&sup3;</span></label>
      <input type="range" id="sV0" min="0.5" max="10" value="3.08" step="0.01">
      <div class="hint">From the transient model. 3.08 m&sup3; is the reference duty with a free DN400 connection.</div>
    </div>
    <div class="ctrl">
      <label>Steady HGL at the vessel <span id="vHgl">85.0 m</span></label>
      <input type="range" id="sHgl" min="30" max="200" value="85" step="0.5">
      <div class="hint">Gauge head at the vessel in normal pumping. Sets P<sub>0</sub> = HGL + 10.33 m.</div>
    </div>
    <div class="ctrl">
      <label>Minimum allowed pressure <span id="vMin">+3.0 m</span></label>
      <input type="range" id="sMin" min="-5" max="20" value="3" step="0.1">
      <div class="hint">The design minimum, gauge. The vessel is assumed to be drawn down to it.</div>
    </div>
    <div class="ctrl">
      <label>Gas law exponent <span id="vN">1.20</span></label>
      <input type="range" id="sN" min="1" max="1.4" value="1.2" step="0.01">
      <div class="hint">1.0 isothermal, 1.4 adiabatic. 1.2 is the usual design value for a trip.</div>
    </div>
    <div class="ctrl">
      <label>Bladder pre-charge, fraction of P<sub>min</sub> <span id="vF">0.90</span></label>
      <input type="range" id="sF" min="0.5" max="0.98" value="0.9" step="0.01">
      <div class="hint">On absolute pressure. The margin below 1.0 is engineering judgement.</div>
    </div>
    <div class="ctrl">
      <label>Air-over-water water reserve <span id="vRes">20 %</span></label>
      <input type="range" id="sRes" min="10" max="30" value="20" step="1">
      <div class="hint">Water left at maximum expansion, so air never reaches the outlet.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Gas at the minimum</div><div class="v" id="rGmin">15.9 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Air-over-water shell</div><div class="v" id="rAow">19.8 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Bladder shell</div><div class="v" id="rBl">24.5 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Bladder penalty</div><div class="v" style="font-size:15px;margin-top:6px;" id="rPen"><span class="badge warn">+23 %</span></div></div>
    <div class="cell"><div class="k">Pre-charge</div><div class="v" id="rPre">12.00 <small>m abs (+1.67 m g)</small></div></div>
  </div>
</div>
<p class="fig-note">At the reference duty the bladder shell is <strong>24.5&nbsp;m&sup3; against 19.8&nbsp;m&sup3;</strong>: 23&nbsp;% larger on the same closed-form basis, and 28&nbsp;% larger than the transient model's 19.1&nbsp;m&sup3;. The reserves differ, though: at the minimum the bladder shell is still 35&nbsp;% water, against 20&nbsp;%. Push the pre-charge to 0.98 and the gap only narrows to 13&nbsp;%; drop it to 0.60 and the bladder shell is 85&nbsp;% larger than the air-over-water shell. Now change the system instead. Raise the steady HGL to 200&nbsp;m and the penalty grows to 41&nbsp;%. Bring it down to 30&nbsp;m with a +20&nbsp;m minimum, a low-lift main, and the bladder becomes the <em>smaller</em> vessel by 7&nbsp;%. The pressure ratio settles part of the type decision before anyone opens a catalogue.</p>

<h2 id="int-gas-path">5 &middot; Interactive: the gas path</h2>
<p>The same comparison, drawn as the gas sees it. Both axes are logarithmic, so the isothermal charge is a straight line of slope &minus;1 and the polytropic expansion a steeper one of slope &minus;n.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Gas pressure and volume through charging and a pump trip</div>
    <div class="fsub">Reference duty: 3.08 m&sup3; at 95.33 m abs, design minimum 13.33 m abs. Bladder: the pre-charge fills the shell, charging to the steady HGL is isothermal, the trip expansion is polytropic. Air-over-water: the compressor charges 3.08 m&sup3; directly, shell with a 20 % reserve. Grey dashed: expansion beyond the design minimum until the gas fills the shell.</div>
  </div>
  <div class="chart-box"><canvas id="pvChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Vessel type</label>
      <select id="sType"><option value="0">Bladder or diaphragm (pre-charged)</option><option value="1">Air-over-water (compressor)</option></select>
      <div class="hint">The hydraulic duty is identical. Only the way the gas gets there changes.</div>
    </div>
    <div class="ctrl">
      <label>Pre-charge, fraction of P<sub>min</sub> <span id="vF2">0.90</span></label>
      <input type="range" id="sF2" min="0.5" max="0.98" value="0.9" step="0.01">
      <div class="hint">Bladder and diaphragm only. Below 0.775 the pre-charge is below atmospheric.</div>
    </div>
    <div class="ctrl">
      <label>Gas law exponent <span id="vN2">1.20</span></label>
      <input type="range" id="sN2" min="1" max="1.4" value="1.2" step="0.01">
      <div class="hint">Set 1.0 to see a slow, isothermal drawdown.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Pre-charge</div><div class="v" id="rPre2">12.00 <small>m abs &middot; +0.16 bar g</small></div></div>
    <div class="cell"><div class="k">Shell</div><div class="v" id="rSh2">24.5 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Gas at the steady HGL</div><div class="v" id="rFrac2">12.6 <small>% of shell</small></div></div>
    <div class="cell"><div class="k">Gas at the minimum</div><div class="v" id="rVmin2">15.9 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Gas fills the shell at</div><div class="v" id="rWall2">7.9 <small>m abs</small></div></div>
  </div>
</div>
<p class="fig-note">The 12.00&nbsp;m abs pre-charge fills 24.5&nbsp;m&sup3;; charging squeezes it along the isotherm into <strong>12.6&nbsp;% of the shell</strong>; the trip expands it along the polytrope to 15.9&nbsp;m&sup3; at the minimum. Everything to the right of that point is shell you paid for and do not use. The dashed segment shows a fast expansion would have to reach 7.9&nbsp;m abs before the gas filled the bladder shell; for air-over-water it ends at 10.2&nbsp;m abs, where the reserve runs out. Do not count on that bladder margin. Set the exponent to 1.0 and the bladder reaches the wall exactly at the pre-charge, because in a slow drawdown the gas stays at ambient temperature &mdash; which is why we judge the pre-charge on the isothermal case, the conservative one.</p>

<h2 id="air-over-water">6 &middot; Air-over-water: compressors, level control and dissolved air</h2>
<p>An air-over-water vessel is a pressure vessel plus a small process plant, and the type decision is really about the plant:</p>
<ul class="clean">
  <li><strong>A compressor sized for recharge, not top-up.</strong> The governing duty is recharging a vessel that has lost all its air and is full of water: 28.4&nbsp;m&sup3; of free air into a vessel at 8.33&nbsp;bar&nbsp;g. Top-up for dissolved air is much smaller, but its rate depends on pressure, temperature and water surface and must come from the supplier or site records. For potable supply the air must be oil-free or filtered.</li>
  <li><strong>Level measurement the controls can trust:</strong> a transmitter over the full working range with set points for compressor start and stop, venting, high and low alarms and a low-low alarm, brought back to <a href="transient-analysis-scada.html">SCADA</a>.</li>
  <li><strong>A vent path</strong> to release air when the water level falls too low, and a strategy for gas dissolving into the water.</li>
  <li><strong>Power</strong> for compressor and instruments &mdash; remembering that a power failure is exactly the trip the vessel must ride through on the gas already inside it.</li>
</ul>
<p>The level set points are not a controls detail; they are the surge protection. On the site's reference vessel &mdash; 20&nbsp;m&sup3; shell, 3.5&nbsp;m&sup3; of gas, DN400 differential connection (K<sub>out</sub>&nbsp;2 / K<sub>in</sub>&nbsp;10), line minimum +4.3&nbsp;m and maximum 119.2&nbsp;m &mdash; the transient model holds +3.0&nbsp;m for any gas setting from <strong>3.22&nbsp;m&sup3;</strong> up to <strong>5.21&nbsp;m&sup3;</strong>, the lower end only 0.28&nbsp;m&sup3; below the design setting. Past 5.21&nbsp;m&sup3; the gas fills the shell, the vessel empties and the minimum falls below the criterion, so the window is closed at both ends. Between the design setting and that ceiling, the limit is the water reserve. The design setting expands to 16.17&nbsp;m&sup3; and leaves 3.83&nbsp;m&sup3; of water, 19&nbsp;% of the shell; keeping 15&nbsp;% caps the gas at 3.85&nbsp;m&sup3;, 10&nbsp;% at 4.28&nbsp;m&sup3;, and at 5.21&nbsp;m&sup3; no water is left. A full 20&nbsp;% would need 3.43&nbsp;m&sup3;, just under the design setting. So the band is a few tenths of a cubic metre either side: choose the reserve to protect, then set the compressor-start level and the low-gas and high-gas alarms with the transmitter accuracy and the strapping table in front of you. How the connection shapes that envelope is in <a href="surge-vessel-differential-orifice.html">the differential orifice article</a>.</p>
<p>A drained vessel is the easier case. Drain a 19.1&nbsp;m&sup3; shell with its vent open and it fills with atmospheric air that, closed and brought to the steady HGL, occupies 2.07&nbsp;m&sup3; &mdash; two-thirds of the duty. The compressor supplies only the remaining 1.01&nbsp;m&sup3; (9.3&nbsp;m&sup3; of free air).</p>

<h2 id="int-compressor">7 &middot; Interactive: keeping the air in</h2>
<p>The compressor duty is a free-air calculation: the gas at the steady pressure, scaled to atmospheric, divided by the recharge time you allow.</p>
<div class="eq">\[ V_{free} = V_0\,\frac{P_0}{P_{atm}}, \qquad FAD = \frac{V_{free}}{60\,t_{recharge}} \quad \text{(m}^3\text{/min of free air, } t \text{ in hours)} \]</div>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Compressor free air delivery against the time allowed for a full recharge</div>
    <div class="fsub">Free air: volume at atmospheric pressure (10.33 m), taken as the compressor inlet condition; temperature correction ignored. The daily top-up is an illustrative percentage of the charge, not a dissolution rate: take that from the supplier or from site records.</div>
  </div>
  <div class="chart-box"><canvas id="fadChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Gas at the steady HGL <span id="vV3">3.08 m&sup3;</span></label>
      <input type="range" id="sV3" min="0.5" max="10" value="3.08" step="0.01">
      <div class="hint">The charge the compressor must rebuild when the vessel has lost all its air.</div>
    </div>
    <div class="ctrl">
      <label>Steady HGL at the vessel <span id="vH3">85.0 m</span></label>
      <input type="range" id="sH3" min="30" max="200" value="85" step="0.5">
      <div class="hint">Higher pressure packs more free air into the same gas volume.</div>
    </div>
    <div class="ctrl">
      <label>Time allowed for a full recharge <span id="vT3">2.0 h</span></label>
      <input type="range" id="sT3" min="0.5" max="8" value="2" step="0.5">
      <div class="hint">An operating decision: how long the station can wait before it is protected again.</div>
    </div>
    <div class="ctrl">
      <label>Daily top-up, illustrative <span id="vTop">1.0 %</span></label>
      <input type="range" id="sTop" min="0" max="5" value="1" step="0.1">
      <div class="hint">Illustrative only. The real rate depends on pressure, temperature and water surface.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Free air per full recharge</div><div class="v" id="rFree">28.4 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Free air delivery</div><div class="v" id="rFad">0.237 <small>m&sup3;/min</small></div></div>
    <div class="cell"><div class="k">Daily top-up (illustrative)</div><div class="v" id="rTop">0.28 <small>m&sup3;/day</small></div></div>
    <div class="cell"><div class="k">Run time for it (illustrative)</div><div class="v" id="rRun">1.2 <small>min/day</small></div></div>
  </div>
</div>
<p class="fig-note">Recharging the reference charge of 28.4&nbsp;m&sup3; of free air in two hours takes <strong>0.237&nbsp;m&sup3;/min</strong> of free air delivery; one hour doubles it to 0.474, four hours halves it to 0.118. That is an operating decision dressed as a mechanical one: how long may the station wait, unprotected, after the vessel has lost its air? The top-up slider is deliberately illustrative; whatever the real dissolution rate, the recharge sizes the machine.</p>

<h2 id="int-gas-drift">8 &middot; Interactive: when the gas setting drifts</h2>
<p>What the level controls protect against, run through the transient model on the 20&nbsp;m&sup3; reference vessel. Each option is the gas volume the controls happened to be holding when the power failed.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Head at the pump after a trip, for different gas settings in the 20 m&sup3; vessel</div>
    <div class="fsub">Transient model, reference system, all pumps trip at t = 0. Grey dashed: the 3.5 m&sup3; design setting, shown when another setting is selected. Line minimum and maximum are for the whole line over 150 s. Where the vessel empties, vapour forms at the pump end and the maximum is given across both cavity models. Amber where the setting misses +3.0 m, or holds it with less water at maximum expansion than the design setting.</div>
  </div>
  <div class="chart-box"><canvas id="driftChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Gas volume at the steady HGL</label>
      <select id="sGas">
        <option value="0">2.00 m&sup3; (water level high)</option>
        <option value="1">2.50 m&sup3;</option>
        <option value="2">3.00 m&sup3;</option>
        <option value="3" selected>3.50 m&sup3; (design setting)</option>
        <option value="4">4.50 m&sup3;</option>
        <option value="5">6.00 m&sup3; (water level low)</option>
        <option value="6">8.00 m&sup3; (water level very low)</option>
      </select>
      <div class="hint">Too little gas is a compressor that has fallen behind. Too much is a level transmitter reading high, so the controls keep adding air.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Gas setting</div><div class="v" id="rGset">3.50 <small>m&sup3; &middot; 17.5 % of shell</small></div></div>
    <div class="cell"><div class="k">Line minimum, whole line</div><div class="v" id="rLmin4">+4.3 <small>m</small></div></div>
    <div class="cell"><div class="k">Line maximum, whole line</div><div class="v" id="rLmax4">119.2 <small>m</small></div></div>
    <div class="cell"><div class="k">Gas at maximum expansion</div><div class="v" id="rGexp4">16.17 <small>of 20 m&sup3;, 3.83 m&sup3; water left</small></div></div>
    <div class="cell"><div class="k">Status</div><div class="v" style="font-size:15px;margin-top:6px;" id="rStat4"><span class="badge good">holds +3.0 m</span></div></div>
  </div>
</div>
<p class="fig-note">At the design setting the line minimum is <strong>+4.3&nbsp;m</strong> and the gas expands to 16.17&nbsp;m&sup3;, leaving 3.83&nbsp;m&sup3; of water. Select 2.00&nbsp;m&sup3;, a compressor that has fallen behind dissolution, and the line minimum drops to <strong>&minus;3.8&nbsp;m</strong>: below the criterion, still clear of vapour. Select 4.50&nbsp;m&sup3; and the line minimum improves to +7.2&nbsp;m, but only 1.52&nbsp;m&sup3; of water is left at maximum expansion. Select 6.00&nbsp;m&sup3;, a transmitter reading high, and the vessel empties: vapour forms at the pump end and a real vessel would pass air into the main (see <a href="air-admission-networks.html">air admission</a>). The later maximum of about 96&nbsp;m comes from the returning column compressing the gas, about a minute after the cavity has closed, which is why both cavity models agree. The failures sit either side of the design setting, so an air-over-water vessel needs both a low-gas and a high-gas alarm, and both drift cases belong in the HAMMER study.</p>

<h2 id="bladder-details">9 &middot; Bladder and diaphragm details</h2>
<h3>Checking the pre-charge</h3>
<p>In service the bladder transmits the line pressure to the gas, so a gauge on the gas valve reads water pressure, not pre-charge. The pre-charge can only be measured with the water side isolated and drained to zero pressure. That takes an isolation valve, a drain, a period without protection or with a second vessel, and a low-range gauge that reads to a few hundredths of a bar (the setting is 0.16&nbsp;bar&nbsp;g) &mdash; and the reading is at whatever the ambient temperature is.</p>
<h3>Temperature</h3>
<p>The pre-charge is a fixed mass of gas, so its pressure follows absolute temperature. Set at 20&nbsp;&deg;C, a sun-exposed vessel at 45&nbsp;&deg;C reads 318.15/293.15 = 8.5&nbsp;% higher:</p>
<div class="tbl-wrap"><table>
  <caption>A pre-charge of 12.00 m abs set at 20 &deg;C, read at other gas temperatures</caption>
  <thead><tr><th>Gas temperature at the check</th><th class="num">Absolute temperature ratio</th><th class="num">Reads (m abs)</th><th class="num">Reads (bar g)</th><th class="num">Fraction of P<sub>min</sub></th></tr></thead>
  <tbody>
    <tr><td>0 &deg;C</td><td class="num">0.932</td><td class="num">11.18</td><td class="num">0.08</td><td class="num">0.84</td></tr>
    <tr><td>20 &deg;C (setting)</td><td class="num">1.000</td><td class="num">12.00</td><td class="num">0.16</td><td class="num">0.90</td></tr>
    <tr><td>35 &deg;C</td><td class="num">1.051</td><td class="num">12.61</td><td class="num">0.22</td><td class="num">0.95</td></tr>
    <tr><td>45 &deg;C</td><td class="num">1.085</td><td class="num">13.02</td><td class="num">0.26</td><td class="num">0.98</td></tr>
  </tbody>
</table></div>
<p>The trap is the correction, not the heat. A technician who finds 13.02&nbsp;m abs on a hot afternoon and bleeds the vessel back to the specified 12.00 has removed gas: back at 20&nbsp;&deg;C the pre-charge is 11.06&nbsp;m abs and the vessel carries <strong>2.84&nbsp;m&sup3;</strong> at the steady HGL instead of 3.08. In the transient model the line minimum moves from +3.0&nbsp;m to <strong>+1.8&nbsp;m</strong>. Put the reference temperature on the nameplate and a correction table in the O&amp;M manual.</p>
<h3>The membrane</h3>
<p>The bladder or diaphragm is the part that wears: it flexes on every start and trip, sits permanently in the water, and must be approved for potable use under NSF/ANSI/CAN&nbsp;61 [8] or the local equivalent. Specify replacement access (manway or flanged head, lifting points, headroom), the supplier's orientation, and a spare. Check the squeeze as well: the 12.00&nbsp;m abs pre-charge is compressed 7.9:1 into 12.6&nbsp;% of the shell in steady service, and 11.8:1 at the 130.9&nbsp;m transient peak. Confirm with the supplier the pressure ratio and smallest gas fraction the membrane allows; a low pre-charge on a high-head main can exceed them. A ruptured membrane turns the vessel into an uncontrolled air-over-water vessel, its gas dissolving with no level instrument to show it. A membrane replaced and returned to service with atmospheric air instead of the specified pre-charge holds 2.65&nbsp;m&sup3; at the steady HGL, and the transient model puts the line minimum at <strong>+0.7&nbsp;m</strong>: 1.67&nbsp;m of forgotten pre-charge costs 2.3&nbsp;m on the line.</p>
<h3>The vessel itself</h3>
<p>Every type is a pressure vessel designed, fabricated and inspected to EN&nbsp;13445 or ASME Section&nbsp;VIII Division&nbsp;1, within the Pressure Equipment Directive where it applies [9]; in-service inspection intervals come from national pressure-equipment regulations and the owner's inspection scheme, not from the surge study. The design pressure must cover the highest transient head at the vessel, and the line's design pressures should be checked in the EN&nbsp;805 sense of maximum design pressure including surge [10]. Provide isolation and a bypass, and write down what the station may do while the vessel is out: on the reference main a trip then takes the line to vapour, with a collapse peak above PN16 (see <a href="surge-analysis-risk.html">surge risk</a>). A vertical shell gives the level transmitter more travel per cubic metre; a horizontal one saves height.</p>

<h2 id="selection">10 &middot; Selection by site and duty</h2>
<p>No single criterion decides the type, and the weights depend on the site. The table gives our scores on a 1&ndash;5 scale, 5 favouring the type. They are engineering judgement, not data: re-score them for your project.</p>
<div class="tbl-wrap"><table>
  <caption>Judgement scores used in the selection figure (5 = favours the type)</caption>
  <thead><tr><th>Criterion</th><th class="num">Air-over-water</th><th class="num">Bladder</th><th class="num">Diaphragm</th><th>Reason</th></tr></thead>
  <tbody>
    <tr><td>Shell volume for the duty</td><td class="num">5</td><td class="num">3</td><td class="num">3</td><td>19.1 m&sup3; against 23.2&ndash;28.4 m&sup3; on the reference duty</td></tr>
    <tr><td>No auxiliary plant</td><td class="num">1</td><td class="num">5</td><td class="num">5</td><td>Compressor, level instruments, vent, controls and power, against none</td></tr>
    <tr><td>Holds its gas without attention</td><td class="num">2</td><td class="num">4</td><td class="num">4</td><td>Dissolved air needs top-up; a membrane separates gas from water, and losses show up at pre-charge checks</td></tr>
    <tr><td>Faults visible in service</td><td class="num">4</td><td class="num">2</td><td class="num">2</td><td>The level instrument shows lost gas in service; a lost pre-charge or torn membrane stays hidden until the next check</td></tr>
    <tr><td>Very large volumes</td><td class="num">5</td><td class="num">2</td><td class="num">1</td><td>A plain shell is limited by fabrication and transport; a membrane also by its manufacture; diaphragms usually suit smaller volumes</td></tr>
    <tr><td>Remote or unmanned site</td><td class="num">2</td><td class="num">4</td><td class="num">4</td><td>Compressors and instruments need attention and power; a membrane vessel needs periodic checks</td></tr>
  </tbody>
</table></div>
<p>Water quality is pass or fail rather than scored: wetted materials need potable approval [8], and compressor air must be oil-free or filtered. Pressure-vessel inspection applies to every type; bladders and diaphragms add membrane replacement.</p>

<h2 id="int-selection">11 &middot; Interactive: weighted selection</h2>
<p>Move the weights to describe your site. Each bar is the weighted average of the table's scores, scaled to 100 and split by criterion.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Weighted selection score by vessel type</div>
    <div class="fsub">Scores 1&ndash;5 from the table above (engineering judgement, not data). Score = 20 &times; &Sigma;(weight &times; score) / &Sigma; weight.</div>
  </div>
  <div class="chart-box"><canvas id="selChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Shell volume for the duty <span id="vw1">4</span></label>
      <input type="range" id="w1" min="0" max="5" value="4" step="1">
      <div class="hint">Space, foundations, crane and vessel cost.</div>
    </div>
    <div class="ctrl">
      <label>No auxiliary plant <span id="vw2">2</span></label>
      <input type="range" id="w2" min="0" max="5" value="2" step="1">
      <div class="hint">Compressor, instruments, controls and their power.</div>
    </div>
    <div class="ctrl">
      <label>Holds its gas without attention <span id="vw3">3</span></label>
      <input type="range" id="w3" min="0" max="5" value="3" step="1">
      <div class="hint">Dissolution, top-up and routine checks.</div>
    </div>
    <div class="ctrl">
      <label>Faults visible in service <span id="vw4">4</span></label>
      <input type="range" id="w4" min="0" max="5" value="4" step="1">
      <div class="hint">Whether lost protection shows before a trip finds it.</div>
    </div>
    <div class="ctrl">
      <label>Very large volumes <span id="vw5">4</span></label>
      <input type="range" id="w5" min="0" max="5" value="4" step="1">
      <div class="hint">How much the duty pushes toward the largest shells.</div>
    </div>
    <div class="ctrl">
      <label>Remote or unmanned site <span id="vw6">1</span></label>
      <input type="range" id="w6" min="0" max="5" value="1" step="1">
      <div class="hint">How rarely anyone is there to look after it.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Air-over-water</div><div class="v" id="rSa">73 <small>/ 100</small></div></div>
    <div class="cell"><div class="k">Bladder</div><div class="v" id="rSb">60 <small>/ 100</small></div></div>
    <div class="cell"><div class="k">Diaphragm</div><div class="v" id="rSd">56 <small>/ 100</small></div></div>
    <div class="cell"><div class="k">Leads</div><div class="v" style="font-size:15px;margin-top:6px;" id="rLead"><span class="badge good">air-over-water</span></div></div>
  </div>
</div>
<p class="fig-note">The defaults describe the reference system, a large main with a staffed pump station, where shell volume, scale and visible faults matter most: air-over-water scores <strong>73</strong>, a bladder 60, a diaphragm 56. Now describe a small unmanned booster: shell volume 2, no auxiliary plant 5, holds its gas 4, faults visible 3, large volumes 1, remote site 5. The order reverses &mdash; bladder 75, diaphragm 74, air-over-water <strong>50</strong> &mdash; and the shell penalty becomes a price worth paying on a site nobody visits every week. The matrix does not make the decision; it makes the reasons explicit enough to argue about. How the vessel compares with other devices on the same main is in <a href="choosing-surge-protection.html">Choosing surge protection on one pipeline</a>.</p>

<h2 id="hammer">12 &middot; Setting it up in Bentley HAMMER</h2>
<p>The vessel type changes only a few properties of the Hydropneumatic Tank element, and those are where the pre-charge mistakes happen [11]. Field names differ slightly between HAMMER versions. The general workflow is in <a href="hammer-transient-simulation-workflow.html">the HAMMER transient workflow</a> and <a href="hammer-transient-tips.html">HAMMER transient tips</a>.</p>
<ul class="clean">
  <li><strong>1. Steady state first.</strong> Pump with its check valve (see <a href="check-valve-hammer.html">check valves in HAMMER</a>), Pipe, and a Reservoir at the delivery end. Type 1,050&nbsp;m/s into the pipe wave speed field: it is the series' design value, 3&ndash;6&nbsp;% below the 1,080&ndash;1,117&nbsp;m/s a thin-wall (Korteweg) calculation gives for DN800 K9, for the reasons in <a href="wave-speed-surge-analysis.html">the wave speed article</a>. Confirm 85.0&nbsp;m at the pump and 44.8&nbsp;m at the reservoir.</li>
  <li><strong>2. Add a Hydropneumatic Tank</strong> at the pump discharge header at its true elevation: tank volume, gas law exponent 1.2, inlet orifice diameter 400&nbsp;mm, minor loss coefficient 0.5 and ratio of losses 1.0 for the free connection used here. The 20&nbsp;m&sup3; reference vessel's differential connection would instead take a minor loss coefficient of 2 (outflow) and a ratio of losses of 5.</li>
  <li><strong>3. Air-over-water.</strong> Bladder option off; tank volume 19.1&nbsp;m&sup3;; initial gas volume 3.08&nbsp;m&sup3;, the volume at the steady HGL that the level controls will hold.</li>
  <li><strong>4. Bladder or diaphragm.</strong> Tick has bladder; tank volume 24.5&nbsp;m&sup3;; preset gas pressure 12.00&nbsp;m abs, which is +1.67&nbsp;m gauge or 0.16&nbsp;bar&nbsp;g. Check whether your version and unit settings take it as gauge or absolute: the two differ by 10.33&nbsp;m, about six times the gauge value. Then check the gas volume at the start of the run: 24.5 &times; 12.00/95.33 = 3.08&nbsp;m&sup3;. If it is far off, suspect the pressure basis first. Near 4.36&nbsp;m&sup3;, the exponent 1.2 is being applied to the charging: confirm the gas law your version uses between preset and initial state, and if it is not isothermal adjust the preset gas pressure until the initial gas volume is 3.08&nbsp;m&sup3;.</li>
  <li><strong>5. Transient run options.</strong> Trip all pumps at t = 0; run duration at least 150&nbsp;s, several times 2L/a = 22.9&nbsp;s; time step computed from the shortest pipe and wave speeds with a tight wave speed adjustment tolerance; vapour pressure and column separation on, so a failed design shows as vapour rather than an impossible negative head.</li>
  <li><strong>6. Read the results.</strong> In the Transient Results Viewer, plot the profile (path) with maximum and minimum head envelopes against +3.0&nbsp;m and 136&nbsp;m. In the time history at the tank, the gas volume must stay below the tank volume with margin (15.30 in 19.1&nbsp;m&sup3; in our model); for a bladder, compare the lowest gas pressure with the preset gas pressure.</li>
  <li><strong>7. Failure scenarios.</strong> Air-over-water: initial gas volumes at the low-gas and high-gas alarm settings. Bladder: preset gas pressure at atmospheric (the forgotten pre-charge, +0.7&nbsp;m in our model) and a mis-adjusted hot check. Both: vessel isolated, which on the reference main is an unprotected line with a 165&ndash;190&nbsp;m collapse peak.</li>
  <li><strong>8. Record the settings</strong> behind the accepted envelope on the vessel datasheet &mdash; tank volume, initial gas volume or preset gas pressure with its basis and temperature, exponent, orifice, ratio of losses &mdash; so the equipment bought is the equipment modelled. The trip usually governs (see <a href="surge-scenarios-pump-stations.html">surge scenarios in pump stations</a>), but run the other events before accepting it.</li>
</ul>

<h2 id="checklist">13 &middot; Design checklist</h2>
<ul class="clean">
  <li><strong>State the duty as gas, in absolute pressure:</strong> gas at the steady HGL, gas at maximum expansion, minimum-pressure basis and n (here 3.08&nbsp;m&sup3; at 95.33&nbsp;m abs, 15.30&nbsp;m&sup3;, 13.33&nbsp;m abs, 1.2).</li>
  <li><strong>Size the shell per type with its basis:</strong> air-over-water from maximum expansion plus reserve; bladder or diaphragm from V<sub>0</sub>&nbsp;P<sub>0</sub>/P<sub>pre</sub>, checked for water left at the minimum.</li>
  <li><strong>Check the pressure ratio before the catalogue:</strong> a high P<sub>0</sub>/P<sub>min</sub> favours air-over-water; a low-head main with a high minimum removes most of the bladder's penalty.</li>
  <li><strong>Write the pre-charge three ways</strong> &mdash; m abs, bar g and reference temperature &mdash; with a correction table in the O&amp;M manual.</li>
  <li><strong>Keep the pre-charge below the lowest vessel pressure</strong> in every design transient, judged on the isothermal case, with a recorded margin.</li>
  <li><strong>Specify the pre-charge check:</strong> water side isolated and drained to zero pressure, a low-range gauge, an interval.</li>
  <li><strong>Membrane:</strong> potable approval (NSF/ANSI/CAN&nbsp;61 or equivalent), replacement access and lifting, orientation, spare, and the supplier's permissible ratio of operating pressure to pre-charge and smallest gas fraction (here 7.9:1 and 12.6&nbsp;% in steady service).</li>
  <li><strong>Air-over-water:</strong> compressor free air delivery for the accepted recharge time, oil-free or filtered air, transmitter range and accuracy, set points from the transient model's gas window and the water reserve you keep at maximum expansion, vent path, low-low alarm, power supply.</li>
  <li><strong>Pressure vessel:</strong> code (EN&nbsp;13445, ASME&nbsp;VIII, PED), design pressure above the highest transient head at the vessel, and whether a vacuum case applies.</li>
  <li><strong>Isolation, bypass and an operating rule</strong> for the station while the vessel is out.</li>
  <li><strong>Heat and frost:</strong> shade, insulation or trace heating where exposure would shift the pre-charge or freeze instruments.</li>
  <li><strong>Failure runs:</strong> low gas, high gas, lost pre-charge and vessel isolated, each with its envelope reported.</li>
</ul>

<div class="callout key">
  <span class="lbl">In short</span>
  The gas duty does not care which vessel you buy. Air-over-water carries it in <strong>19.1&nbsp;m&sup3;</strong>, at the price of a compressor and level controls; on the site's 20&nbsp;m&sup3; reference vessel the design gas setting is only 0.28&nbsp;m&sup3; above the loss of +3.0&nbsp;m, and the water reserve limits it from above. A bladder or diaphragm vessel needs <strong>23.2&ndash;28.4&nbsp;m&sup3;</strong> at any pre-charge between 0.95 of the minimum and atmospheric, because its shell is set by isothermal charging from a pre-charge below the minimum pressure &mdash; here under 0.29&nbsp;bar gauge, invisible in service and moving with temperature. Choose by pressure ratio, site and who will maintain it; then model each type's own failures in HAMMER.
</div>

<div class="callout green">
  <span class="lbl">Surge protection design series</span>
  <ol>
    <li><a href="wave-speed-surge-analysis.html">Wave speed: the number that sets the surge</a></li>
    <li><a href="surge-vessel-differential-orifice.html">The differential orifice: empty freely, refill slowly</a></li>
    <li><strong>Bladder, diaphragm or air-over-water vessel</strong></li>
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
const TT=t=>({display:true,text:t,font:{family:'IBM Plex Sans',size:12,weight:'600'}});
const LEG={labels:{font:{family:'IBM Plex Sans',size:11.5},usePointStyle:true,boxWidth:8}};
const LEGF={labels:{...LEG.labels,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}};
const ALBL=(txt,pos,bg)=>({display:true,content:txt,position:pos,backgroundColor:bg,color:'#fff',font:{family:'IBM Plex Sans',size:10}});
const HBAR=10.33, M_PER_BAR=10.20;
const sgn1=v=>{const s=+fmt1(v);return (s>0?'+':(s<0?'&minus;':''))+fmt1(Math.abs(v));};
const sgn2=v=>{const s=+fmt2(v);return (s>0?'+':(s<0?'&minus;':''))+fmt2(Math.abs(v));};

/* ---------- CHART 1 : shell volume by vessel type ---------- */
const sV0=document.getElementById('sV0'),sHgl=document.getElementById('sHgl'),sMin=document.getElementById('sMin'),
      sN=document.getElementById('sN'),sF=document.getElementById('sF'),sRes=document.getElementById('sRes');
function duty(V0,hgl,hmin,n,f,res){
  const P0=hgl+HBAR, Pmin=hmin+HBAR, Ppre=f*Pmin;
  const Vmin=V0*Math.pow(P0/Pmin,1/n);
  const aow=Vmin/(1-res);
  const bl=V0*P0/Ppre;
  return {P0:P0,Pmin:Pmin,Ppre:Ppre,Vmin:Vmin,aow:aow,bl:bl,pen:100*(bl/aow-1)};
}
let shellChart=new Chart(document.getElementById('shellChart'),{
  type:'bar',
  data:{labels:['Air-over-water','Bladder or diaphragm'],
    datasets:[
      {label:'Gas at the minimum pressure',data:[],backgroundColor:'#1b4f72',borderColor:'#fff',borderWidth:1,stack:'s'},
      {label:'Water still in the shell',data:[],backgroundColor:'#a9cce3',borderColor:'#fff',borderWidth:1,stack:'s'}]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,stacked:true},
            y:{...AX,stacked:true,min:0,title:TT('Volume at the minimum pressure (m³)')}},
    plugins:{legend:LEG,
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m³`}},
      annotation:{annotations:{
        moc:{type:'line',yMin:19.1,yMax:19.1,borderColor:'#c0392b',borderWidth:2,borderDash:[6,4],display:true,
             label:ALBL('Transient model, air-over-water: 19.1 m³','start','rgba(192,57,43,0.85)')}}}}}
});
function updShell(){
  const V0=+sV0.value,hgl=+sHgl.value,hmin=+sMin.value,n=+sN.value,f=+sF.value,res=+sRes.value/100;
  document.getElementById('vV0').innerHTML=fmt2(V0)+' m³';
  document.getElementById('vHgl').textContent=fmt1(hgl)+' m';
  document.getElementById('vMin').innerHTML=sgn1(hmin)+' m';
  document.getElementById('vN').textContent=fmt2(n);
  document.getElementById('vF').textContent=fmt2(f);
  document.getElementById('vRes').textContent=fmt0(res*100)+' %';
  const d=duty(V0,hgl,hmin,n,f,res);
  shellChart.data.datasets[0].data=[+d.Vmin.toFixed(3),+d.Vmin.toFixed(3)];
  shellChart.data.datasets[1].data=[+(d.aow-d.Vmin).toFixed(3),+(d.bl-d.Vmin).toFixed(3)];
  const atRef=Math.abs(V0-D.ref.gas)<1e-6&&Math.abs(hgl-85)<1e-6&&Math.abs(hmin-3)<1e-6&&Math.abs(n-1.2)<1e-6;
  const moc=D.ref.gas_max/(1-res);
  const a=shellChart.options.plugins.annotation.annotations.moc;
  a.display=atRef; a.yMin=moc; a.yMax=moc; a.label.content='Transient model, air-over-water: '+fmt1(moc)+' m³';
  shellChart.update('none');
  document.getElementById('rGmin').innerHTML=fmt1(d.Vmin)+' <small>m³</small>';
  document.getElementById('rAow').innerHTML=fmt1(d.aow)+' <small>m³</small>';
  document.getElementById('rBl').innerHTML=fmt1(d.bl)+' <small>m³</small>';
  const pen0=Math.round(d.pen);
  document.getElementById('rPen').innerHTML=pen0>0
    ? '<span class="badge warn">+'+fmt0(pen0)+' %</span>'
    : (pen0<0 ? '<span class="badge good">&minus;'+fmt0(-pen0)+' %</span>'
      : '<span class="badge good">no penalty</span>');
  const g=d.Ppre-HBAR;
  document.getElementById('rPre').innerHTML=fmt2(d.Ppre)+' <small>m abs ('+sgn2(g)+' m g'+(g<0?', below atmospheric':'')+')</small>';
}
[sV0,sHgl,sMin,sN,sF,sRes].forEach(s=>s.addEventListener('input',updShell));updShell();

/* ---------- CHART 2 : the gas path on a P-V diagram ---------- */
const sType=document.getElementById('sType'),sF2=document.getElementById('sF2'),sN2=document.getElementById('sN2');
const REF={V0:D.ref.gas,P0:85.0+HBAR,Pmin:3.0+HBAR,res:0.2};
function curve(fn,v1,v2,k){
  const pts=[];
  for(let i=0;i<=k;i++){const v=v1*Math.pow(v2/v1,i/k);pts.push({x:+v.toFixed(4),y:+fn(v).toFixed(4)});}
  return pts;
}
const LOGX=[2,3,5,10,20,30,50], LOGY=[2,5,10,20,50,100];
let pvChart=new Chart(document.getElementById('pvChart'),{
  type:'scatter',
  data:{datasets:[
    {label:'Isothermal charging',data:[],showLine:true,borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.5,pointRadius:0},
    {label:'Polytropic expansion on the trip',data:[],showLine:true,borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:3,pointRadius:0},
    {label:'Beyond the design minimum',data:[],showLine:true,borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:2,borderDash:[6,4],pointRadius:0},
    {label:'Key states',data:[],showLine:false,backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:6}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,type:'logarithmic',min:2,max:60,title:TT('Gas volume (m³, log scale)'),
               ticks:{font:{family:'IBM Plex Sans',size:11},callback:v=>LOGX.includes(v)?v:''}},
            y:{...AX,type:'logarithmic',min:2,max:150,title:TT('Gas pressure (m abs, log scale)'),
               ticks:{font:{family:'IBM Plex Sans',size:11},callback:v=>LOGY.includes(v)?v:''}}},
    plugins:{legend:LEGF,
      tooltip:{callbacks:{label:c=>(c.raw&&c.raw.lab?c.raw.lab+': ':'')+`${fmt2(c.parsed.x)} m³ at ${fmt2(c.parsed.y)} m abs`}},
      annotation:{annotations:{
        pmin:{type:'line',yMin:REF.Pmin,yMax:REF.Pmin,borderColor:'#1e8449',borderWidth:1.5,borderDash:[4,4],
              label:ALBL('Design minimum 13.33 m abs (+3.0 m)','end','rgba(30,132,73,0.85)')},
        atm:{type:'line',yMin:HBAR,yMax:HBAR,borderColor:'#7f8c8d',borderWidth:1,borderDash:[2,3],
             label:ALBL('Atmosphere','start','rgba(127,140,141,0.85)')},
        shell:{type:'line',xMin:24.5,xMax:24.5,borderColor:'#c0392b',borderWidth:2,
               label:ALBL('Shell','start','rgba(192,57,43,0.85)')}}}}}
});
function updPV(){
  const bl=(sType.value==='0'), f=+sF2.value, n=+sN2.value;
  document.getElementById('vF2').textContent=bl?fmt2(f):'not used';
  document.getElementById('vN2').textContent=fmt2(n);
  sF2.disabled=!bl;
  const V0=REF.V0,P0=REF.P0,Pmin=REF.Pmin;
  const Vmin=V0*Math.pow(P0/Pmin,1/n);
  const Ppre=f*Pmin;
  const Vsh=bl?V0*P0/Ppre:Vmin/(1-REF.res);
  const Pwall=P0*Math.pow(V0/Vsh,n);
  const poly=v=>P0*Math.pow(V0/v,n);
  pvChart.data.datasets[0].data=bl?curve(v=>Ppre*Vsh/v,Vsh,V0,40):[];
  pvChart.data.datasets[1].data=curve(poly,V0,Vmin,40);
  pvChart.data.datasets[2].data=curve(poly,Vmin,Vsh,20);
  const pts=[];
  if(bl)pts.push({x:+Vsh.toFixed(4),y:+Ppre.toFixed(4),lab:'Pre-charge fills the shell'});
  pts.push({x:V0,y:+P0.toFixed(4),lab:'Steady HGL'});
  pts.push({x:+Vmin.toFixed(4),y:+Pmin.toFixed(4),lab:'Design minimum'});
  pts.push({x:+Vsh.toFixed(4),y:+Pwall.toFixed(4),lab:bl?'Bladder reaches the shell':'Water reserve used up'});
  pvChart.data.datasets[3].data=pts;
  const sh=pvChart.options.plugins.annotation.annotations.shell;
  sh.xMin=Vsh; sh.xMax=Vsh; sh.label.content=(bl?'Bladder shell ':'Air-over-water shell ')+fmt1(Vsh)+' m³';
  pvChart.update('none');
  document.getElementById('rPre2').innerHTML=bl
    ? fmt2(Ppre)+' <small>m abs &middot; '+sgn2((Ppre-HBAR)/M_PER_BAR)+' bar g</small>'
    : 'none <small>compressor charge</small>';
  document.getElementById('rSh2').innerHTML=fmt1(Vsh)+' <small>m³</small>';
  document.getElementById('rFrac2').innerHTML=fmt1(100*V0/Vsh)+' <small>% of shell</small>';
  document.getElementById('rVmin2').innerHTML=fmt1(Vmin)+' <small>m³</small>';
  document.getElementById('rWall2').innerHTML=fmt1(Pwall)+' <small>m abs</small>';
}
[sType,sF2,sN2].forEach(s=>s.addEventListener('input',updPV));
sType.addEventListener('change',updPV);updPV();

/* ---------- CHART 3 : compressor free air delivery ---------- */
const sV3=document.getElementById('sV3'),sH3=document.getElementById('sH3'),
      sT3=document.getElementById('sT3'),sTop=document.getElementById('sTop');
let fadChart=new Chart(document.getElementById('fadChart'),{
  data:{datasets:[
    {type:'line',label:'Free air delivery for a full recharge',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',fill:true,borderWidth:3,pointRadius:0},
    {type:'scatter',label:'Your recharge time',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,type:'linear',min:0.5,max:8,title:TT('Time allowed to recharge a vessel with no air left (h)')},
            y:{...AX,type:'linear',min:0,title:TT('Compressor free air delivery (m³/min)')}},
    plugins:{legend:LEG,
      tooltip:{callbacks:{label:c=>`${fmt3(c.parsed.y)} m³/min for a ${fmt1(c.parsed.x)} h recharge`}}}}
});
function updFad(){
  const V0=+sV3.value,hgl=+sH3.value,th=+sT3.value,top=+sTop.value;
  document.getElementById('vV3').innerHTML=fmt2(V0)+' m³';
  document.getElementById('vH3').textContent=fmt1(hgl)+' m';
  document.getElementById('vT3').textContent=fmt1(th)+' h';
  document.getElementById('vTop').textContent=fmt1(top)+' %';
  const free=V0*(hgl+HBAR)/HBAR, fad=free/(60*th), daily=free*top/100;
  const xs=[];for(let x=0.5;x<=8.0001;x+=0.125)xs.push(x);
  fadChart.data.datasets[0].data=xs.map(x=>({x:+x.toFixed(3),y:+(free/(60*x)).toFixed(4)}));
  fadChart.data.datasets[1].data=[{x:th,y:+fad.toFixed(4)}];
  fadChart.update('none');
  document.getElementById('rFree').innerHTML=fmt1(free)+' <small>m³</small>';
  document.getElementById('rFad').innerHTML=fmt3(fad)+' <small>m³/min</small>';
  document.getElementById('rTop').innerHTML=fmt2(daily)+' <small>m³/day</small>';
  document.getElementById('rRun').innerHTML=fmt1(daily/fad)+' <small>min/day</small>';
}
[sV3,sH3,sT3,sTop].forEach(s=>s.addEventListener('input',updFad));updFad();

/* ---------- CHART 4 : gas setting drift in the 20 m3 reference vessel ---------- */
const sGas=document.getElementById('sGas');
const series=h=>h.map((y,i)=>({x:D.aw.t[i],y:y}));
let driftChart=new Chart(document.getElementById('driftChart'),{
  type:'line',
  data:{datasets:[
    {label:'Design setting, 3.5 m³',data:[],borderColor:'#7f8c8d',borderWidth:1.8,borderDash:[5,4],pointRadius:0},
    {label:'Selected gas setting',data:[],borderColor:'#1b4f72',borderWidth:2.5,pointRadius:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,type:'linear',min:0,max:150,title:TT('Time after the trip (s)')},
            y:{...AX,type:'linear',min:-15,max:150,title:TT('Head at the pump (m)')}},
    plugins:{legend:LEGF,
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{
        pn:{type:'line',yMin:136,yMax:136,borderColor:'#c0392b',borderWidth:2,label:ALBL('PN16 allowable 136 m','end','rgba(192,57,43,0.85)')},
        mn:{type:'line',yMin:3,yMax:3,borderColor:'#1e8449',borderWidth:1.5,borderDash:[6,4],label:ALBL('+3.0 m minimum','end','rgba(30,132,73,0.85)')},
        vap:{type:'line',yMin:-9.8,yMax:-9.8,borderColor:'#b9770e',borderWidth:1.5,borderDash:[2,3],label:ALBL('Vapour −9.8 m','start','rgba(185,119,14,0.85)')}}}}}
});
function updDrift(){
  const k=+sGas.value, r=D.aw.rows[k], ref=D.aw.rows[3];
  driftChart.data.datasets[0].data=(k===3)?[]:series(ref.h);
  driftChart.data.datasets[1].data=series(r.h);
  driftChart.data.datasets[1].label='Gas setting '+fmt2(r.V0)+' m³';
  driftChart.update('none');
  document.getElementById('rGset').innerHTML=fmt2(r.V0)+' <small>m³ &middot; '+fmt1(100*r.V0/D.aw.shell)+' % of shell</small>';
  const vap=r.lmin<=-9.79;
  document.getElementById('rLmin4').innerHTML=vap?'&minus;9.8 <small>m, vapour</small>':sgn1(r.lmin)+' <small>m</small>';
  let mx;
  if(r.lmaxd!==null){
    const lo=Math.round(Math.min(r.lmax,r.lmaxd)), hi=Math.round(Math.max(r.lmax,r.lmaxd));
    mx=(lo===hi)?'about '+hi+' <small>m, both cavity models</small>':lo+'&ndash;'+hi+' <small>m, cavity-model range</small>';
  } else { mx=fmt1(r.lmax)+' <small>m</small>'; }
  document.getElementById('rLmax4').innerHTML=mx;
  document.getElementById('rGexp4').innerHTML=fmt2(r.gmax)+' <small>of '+fmt0(D.aw.shell)+' m³, '+fmt2(r.left)+' m³ water left</small>';
  document.getElementById('rStat4').innerHTML=r.emp
    ? '<span class="badge bad">vessel empties</span>'
    : (r.lmin<3.0 ? '<span class="badge warn">below +3.0 m</span>'
      : (r.left<ref.left-1e-6 ? '<span class="badge warn">holds +3.0 m, '+fmt0(100*r.left/D.aw.shell)+' % water left</span>'
        : '<span class="badge good">holds +3.0 m</span>'));
}
sGas.addEventListener('input',updDrift);sGas.addEventListener('change',updDrift);updDrift();

/* ---------- CHART 5 : weighted selection ---------- */
const w1=document.getElementById('w1'),w2=document.getElementById('w2'),w3=document.getElementById('w3'),
      w4=document.getElementById('w4'),w5=document.getElementById('w5'),w6=document.getElementById('w6');
const WEL=[w1,w2,w3,w4,w5,w6];
const WLBL=[document.getElementById('vw1'),document.getElementById('vw2'),document.getElementById('vw3'),
            document.getElementById('vw4'),document.getElementById('vw5'),document.getElementById('vw6')];
const CRIT=[
  {name:'Shell volume',s:[5,3,3],c:'#1b4f72'},
  {name:'No auxiliary plant',s:[1,5,5],c:'#5eaadd'},
  {name:'Holds its gas',s:[2,4,4],c:'#1e8449'},
  {name:'Faults visible',s:[4,2,2],c:'#b9770e'},
  {name:'Large volumes',s:[5,2,1],c:'#6b4f9e'},
  {name:'Remote site',s:[2,4,4],c:'#7f8c8d'}];
const TYPES=['Air-over-water','Bladder','Diaphragm'];
let selChart=new Chart(document.getElementById('selChart'),{
  type:'bar',
  data:{labels:TYPES,datasets:CRIT.map(c=>({label:c.name,data:[0,0,0],backgroundColor:c.c,borderColor:'#fff',borderWidth:1,stack:'s'}))},
  options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,stacked:true,min:0,max:100,title:TT('Weighted score (out of 100)')},
            y:{...AX,stacked:true}},
    plugins:{legend:LEG,
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.x)} points`}}}}
});
function updSel(){
  const w=WEL.map(e=>+e.value);
  WLBL.forEach((el,i)=>{el.textContent=String(w[i]);});
  const sw=w.reduce((a,b)=>a+b,0);
  const tot=[0,0,0];
  CRIT.forEach((c,i)=>{
    const d=[0,1,2].map(j=>sw>0?20*w[i]*c.s[j]/sw:0);
    d.forEach((v,j)=>{tot[j]+=v;});
    selChart.data.datasets[i].data=d.map(v=>+v.toFixed(3));
  });
  selChart.update('none');
  document.getElementById('rSa').innerHTML=fmt0(tot[0])+' <small>/ 100</small>';
  document.getElementById('rSb').innerHTML=fmt0(tot[1])+' <small>/ 100</small>';
  document.getElementById('rSd').innerHTML=fmt0(tot[2])+' <small>/ 100</small>';
  const lead=document.getElementById('rLead');
  if(sw===0){lead.innerHTML='<span class="badge warn">set a weight</span>';return;}
  const order=[0,1,2].sort((a,b)=>tot[b]-tot[a]);
  const name=TYPES[order[0]].toLowerCase();
  lead.innerHTML=(tot[order[0]]-tot[order[1]]<2)
    ? '<span class="badge warn">'+name+', narrowly</span>'
    : '<span class="badge good">'+name+'</span>';
}
WEL.forEach(s=>s.addEventListener('input',updSel));updSel();

window.addEventListener('load',function(){try{shellChart.resize();pvChart.resize();fadChart.resize();driftChart.resize();selChart.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993 — method of characteristics, the air vessel boundary with a polytropic gas law, and column separation.</li>
  <li>ISO 2531 <em>Ductile iron pipes, fittings, accessories and their joints for water applications</em> — the DN800 K9 pipe of the reference system.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006 — discrete vapour and gas cavity models, and why collapse peaks depend on the cavity model.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014 — air chambers, and the gas law exponent between the isothermal and adiabatic limits.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004 — surge control devices, including gas-charged vessels of different types and their practical requirements.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005 — hydropneumatic tanks among the protection strategies for water systems, and design considerations for their use.</li>
  <li>Stephenson, D. &ldquo;Simple guide for design of air vessels for water hammer protection of pumping lines.&rdquo; <em>Journal of Hydraulic Engineering</em> (ASCE), 128(8), 2002 — closed-form first estimates of air vessel size, checked by transient analysis.</li>
  <li>NSF/ANSI/CAN 61 <em>Drinking Water System Components — Health Effects</em> — approval of membranes, linings and other wetted materials for drinking water.</li>
  <li>EN 13445 <em>Unfired pressure vessels</em>; ASME <em>Boiler and Pressure Vessel Code</em>, Section VIII, Division 1; Pressure Equipment Directive 2014/68/EU — design, fabrication and inspection of the vessel shell.</li>
  <li>EN 805 <em>Water supply — Requirements for systems and components outside buildings</em> — design pressures of the pipeline, including the surge allowance in the maximum design pressure.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> product documentation and help — the Hydropneumatic Tank element (bladder option, preset gas pressure, initial gas volume, gas law exponent, ratio of losses), transient run options and the Transient Results Viewer.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeVessel #HydropneumaticTank #BladderVessel #DiaphragmVessel #AirOverWater #SurgeProtection #WaterHammer #HydraulicTransients #PreChargePressure #PolytropicExpansion #GasLaw #AirCompressor #LevelControl #DissolvedAir #PumpTrip #PowerFailure #ColumnSeparation #TransmissionMain #DuctileIron #PumpingStation #BentleyHAMMER #OpenFlowsHAMMER #TransientAnalysis #PressureVessel #EquipmentSelection #DesignChecklist #WaterEngineering #PipelineDesign</div>
"""

import json, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_D = json.load(open(os.path.join(_HERE, 'surge_data', 'datasets.json')))
_VA = json.load(open(os.path.join(_HERE, 'surge_data', 'vessel_articles.json')))
_base = [c for c in _D['wavespeed']['cases'] if c['a'] == 1050][0]
_aw = _VA['air_over_water_settings']
DATA = {
    'ref': {'gas': _base['gas'], 'gas_max': _base['gas_max'], 'shell': _base['vessel_total']},
    'aw': {'shell': _aw['shell'],
           't': [round(x, 1) for x in _aw['rows'][0]['t']],
           'rows': [{'V0': r['V0'], 'lmin': r['line_min'], 'lmax': r['line_max'], 'lmaxd': r['line_max_dgcm'],
                     'gmax': r['gas_max'], 'emp': r['emptied'], 'left': r['water_left'], 'h': r['pump_H']}
                    for r in _aw['rows']]},
}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='surge-vessel-type-selection', cat='surge', mins=37,
    date_iso='2026-09-16', date_human='September 2026', date_ar='سبتمبر 2026',
    title='Bladder, Diaphragm or Air-over-Water: Choosing the Surge Vessel Type',
    reg_title='Bladder, Diaphragm or Air-over-Water: Choosing the Surge Vessel Type',
    reg_tag='Surge Analysis · Surge Vessel · Equipment Selection',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Surge Vessel &middot; Equipment Selection',
    desc='How to choose between bladder, diaphragm and air-over-water surge vessels for the same hydraulic duty: the pre-charge penalty on shell volume, the gas path, compressor and level-control sizing, pre-charge checks and temperature, a weighted selection matrix and the Bentley HAMMER set-up, with five interactive charts.',
    og_desc='The same 3.08 m³ gas duty on a 12 km DN800 main: an air-over-water vessel needs a 19.1 m³ shell, a bladder pre-charged below the minimum pressure 23.2 to 28.4 m³ at any practical pre-charge. Why, and when the bladder still wins.',
    ld_desc='A design comparison of bladder, diaphragm and air-over-water surge vessels on one reference pipeline: shell volume, pre-charge, compressors, level control, failure modes, selection and HAMMER set-up.',
    img_alt='Three cutaway surge vessels on a dark blue background: a bladder vessel with the water held inside a flexible bladder, a diaphragm vessel with a membrane across the shell above the water, and an air-over-water vessel with a compressor, level probes and a small chart of air volume topped up over time, with blueprint outlines of the three vessels behind',
    en_tag='Surge &amp; Transient Analysis &middot; Surge Vessel Selection',
    en_title='Bladder, Diaphragm or Air-over-Water: Choosing the Surge Vessel Type',
    en_excerpt='The gas duty is the same whichever vessel you buy: 3.08 m³ at the steady HGL, expanding to 15.30 m³ on a pump trip. An air-over-water vessel delivers it in a <strong>19.1 m³</strong> shell. A bladder or diaphragm vessel needs <strong>23.2–28.4 m³</strong> at any pre-charge from atmospheric up to 0.95 of the minimum pressure, because its shell is set by isothermal charging. That pre-charge is under 0.29 bar gauge, invisible in service and moving with temperature. Air-over-water has its own narrow margin: on the 20 m³ reference vessel used across the site, the design gas setting sits only <strong>0.28 m³</strong> above the loss of +3.0 m. With compressor sizing, a weighted selection matrix, the HAMMER set-up and five interactive charts.',
    en_search='surge vessel type selection bladder vessel diaphragm vessel air-over-water vessel hydropneumatic tank air vessel air chamber pre-charge pressure precharge gas volume shell volume polytropic expansion isothermal charging gas law exponent compressor free air delivery FAD bladder compression ratio water reserve high-gas alarm level control level transmitter dissolved air top-up membrane replacement NSF 61 pressure vessel EN 13445 ASME VIII PED pump trip power failure water hammer surge protection transmission main ductile iron DN800 Bentley HAMMER OpenFlows HAMMER Hydropneumatic Tank has bladder preset gas pressure initial gas volume ratio of losses transient analysis selection matrix design checklist',
    ar_title='مثانة أم غشاء أم هواء فوق الماء: اختيار نوع خزان الحماية من المطرقة المائية',
    ar_excerpt='الحمل الهيدروليكي واحد مهما كان نوع الخزان: <strong>٣٫٠٨ م³</strong> من الغاز عند خط الانحدار الهيدروليكي المستقر تتمدد إلى ١٥٫٣٠ م³ عند توقف المضخات. خزان الهواء فوق الماء يؤدي ذلك بغلاف سعته <strong>١٩٫١ م³</strong>، أما خزان المثانة أو الغشاء المشحون مسبقاً بضغط أقل من أدنى ضغط عابر فيحتاج <strong>٢٣٫٢–٢٨٫٤ م³</strong> لأي ضغط شحن مسبق بين الضغط الجوي و٠٫٩٥ من الحد الأدنى. نشرح السبب، وحجم الضاغط والتحكم بالمنسوب، وفحص الشحن المسبق وأثر الحرارة، ومصفوفة اختيار موزونة، وخطوات الإعداد في برنامج HAMMER، مع خمسة رسوم تفاعلية.',
    ar_search='اختيار خزان الحماية من المطرقة المائية المطرقة المائية الطرق المائي خزان الحماية خزان الضغط الهوائي خزان المثانة خزان الغشاء خزان الهواء فوق الماء الخزان الهيدروبنيوماتيكي وعاء الهواء ضغط الشحن المسبق حجم الغاز حجم الغلاف التمدد البوليتروبي الشحن متساوي الحرارة أس قانون الغازات الضاغط التحكم بالمنسوب الهواء الذائب استبدال الغشاء وعاء الضغط توقف المضخات انقطاع الكهرباء الحماية من موجات الضغط العابرة تحليل السريان العابر خط النقل حديد الدكتايل برنامج هامر مصفوفة الاختيار قائمة التحقق التصميمية',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
