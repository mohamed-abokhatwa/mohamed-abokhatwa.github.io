# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Every surge model of a pumping main starts with one number typed into every pipe: the wave speed. It sets the Joukowsky head, the 2L/a clock and whether the water column separates. On a 12&nbsp;km DN800 ductile iron main, taking it from 1,050 down to 700&nbsp;m/s cuts the Joukowsky head from <strong>149.1 to 99.4&nbsp;m</strong> and the unprotected peak from 165&ndash;190&nbsp;m to 140&ndash;150&nbsp;m. Yet the air-over-water vessel that holds the line above +3.0&nbsp;m only moves from <strong>3.08 to 3.19&nbsp;m&sup3; of gas</strong>. This article explains why, where that stops being true, and how to choose and test the number.</p>

<h2 id="first-input">1 &middot; Why wave speed is the first input</h2>
<p>When pumps with little inertia trip, the flow at the pump stops almost at once. The pressure change that follows travels along the main at the wave speed \(a\), and both its size and its timing follow directly from that speed [1, 2, 5, 8]:</p>
<div class="eq">\[ \Delta H = \frac{a\,\Delta V}{g}, \qquad T_r = \frac{2L}{a} \]</div>
<p>The Joukowsky head \(\Delta H\) applies when the velocity changes faster than a wave can reach the far end and come back. That round trip, \(2L/a\), is the clock that every valve closure, pump rundown and relief-valve opening is judged against [3].</p>
<p>The reference main for this series is 12&nbsp;km of DN800 ductile iron K9 carrying 0.70&nbsp;m&sup3;/s (2,520&nbsp;m&sup3;/h) at 1.39&nbsp;m/s, with the HGL at 85.0&nbsp;m at the pump and 44.8&nbsp;m at the delivery reservoir. It is PN16 with 136&nbsp;m allowable, and the design minimum is +3.0&nbsp;m. With a = 1,050&nbsp;m/s:</p>
<ul class="clean">
  <li><strong>The Joukowsky head is 149.1&nbsp;m</strong> (1,050 &times; 1.393 / 9.81, with the unrounded velocity). The pump end has only 85.0 + 9.8 = <strong>94.8&nbsp;m</strong> of head above vapour, so an instant stop takes it straight to vapour.</li>
  <li><strong>2L/a is 22.9&nbsp;s</strong>: the time before anything at the reservoir end can affect the pump.</li>
  <li><strong>The peak is 165&ndash;190&nbsp;m.</strong> Once the column has separated, the peak comes from the cavity closing, not from Joukowsky, and it is above PN16 in either cavity model.</li>
</ul>
<div class="callout key">
  <span class="lbl">The design point</span>
  Get the wave speed right for peaks, pipe class, timing and column separation. Do not expect a more refined value to shrink the vessel on steel or ductile iron: from 700 to 1,300&nbsp;m/s the gas needed stays at <strong>3.08&ndash;3.19&nbsp;m&sup3;</strong>. Only flexible pipe changes it: 1.99&nbsp;m&sup3; at 450&nbsp;m/s, and no vessel at 300&nbsp;m/s. Never carry a wave speed from one material to another. Collapse peaks depend on how the cavity is modelled [7], so in our practice they are quoted as a range.
</div>

<h2 id="korteweg">2 &middot; What sets it: the water, the wall and the restraint</h2>
<p>Wave speed is a balance between how much the water compresses and how much the pipe wall stretches. For a thin-walled elastic pipe, the Korteweg formula with the Wylie &amp; Streeter restraint factor is [1, 2]:</p>
<div class="eq">\[ a=\sqrt{\dfrac{K/\rho}{1+\dfrac{K\,D}{E\,e}\,c_1}} \]</div>
<p>Here \(K\) = 2.19&nbsp;GPa is the bulk modulus of water, \(\rho\) = 998&nbsp;kg/m&sup3;, \(D\) the diameter (the nominal diameter here, which for PE is the outside diameter, so D/e is the SDR), \(e\) the wall thickness and \(E\) the Young&rsquo;s modulus of the wall. The restraint factor \(c_1\) depends on how the pipe is held along its length and on its Poisson&rsquo;s ratio \(\mu\):</p>
<ul class="clean">
  <li><strong>Anchored at the upstream end only:</strong> \(1-\mu/2\).</li>
  <li><strong>Anchored throughout against axial movement:</strong> \(1-\mu^2\).</li>
  <li><strong>Expansion joints throughout:</strong> 1.</li>
</ul>
<p>On its own, \(\sqrt{K/\rho}\) = 1,481&nbsp;m/s is the speed of sound in water, which no pipe can exceed. The wall term \(KD/(Ee)\) compares how much the pipe stretches with how much the water compresses. It is 0.88 for DN800 ductile iron, where the two share the job, and 33.8 for PE100 SDR17 of the same size, where the wall does nearly all of it.</p>
<h3>Worked example: the DN800 K9 pipe</h3>
<p>ISO 2531 gives the nominal wall of a K-class ductile iron pipe as \(e = k\,(0.5 + 0.001\,DN)\)&nbsp;mm, with \(k\) the class number [14]. DN800 K9 therefore has e = 9 &times; 1.3 = <strong>11.7&nbsp;mm</strong> (D/e = 68.4). With E = 170&nbsp;GPa and &mu; = 0.28:</p>
<div class="tbl-wrap"><table><caption>Korteweg wave speed, DN800 K9 ductile iron (D = 800 mm, e = 11.7 mm)</caption><thead><tr><th>Restraint condition</th><th class="num">c&#8321;</th><th class="num">a (m/s)</th><th class="num">Above 1,050 m/s by</th></tr></thead><tbody>
<tr><td>Anchored at the upstream end only</td><td class="num">0.860</td><td class="num">1,117</td><td class="num">6.4 %</td></tr>
<tr><td>Anchored throughout</td><td class="num">0.922</td><td class="num">1,101</td><td class="num">4.8 %</td></tr>
<tr><td>Expansion joints throughout</td><td class="num">1.000</td><td class="num">1,080</td><td class="num">2.9 %</td></tr>
</tbody></table></div>
<p>The series uses <strong>a = 1,050&nbsp;m/s</strong>, 3&ndash;6&nbsp;% below these values. That choice is design judgement, not a formula result: an allowance for traces of air and for the joints, which the thin-wall formula does not see. Also in our judgement, socket-and-spigot ductile iron is closest to the expansion-joint case, and buried welded steel to anchored throughout.</p>

<h2 id="int-calculator">3 &middot; Interactive: wave speed calculator</h2>
<p>Choose a pipe, then change its geometry, modulus and restraint. The curves show Korteweg wave speed against D/e for the current material under all three restraint conditions. The marker is your pipe.</p>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Korteweg wave speed by material, geometry and restraint</div>
    <div class="fsub">Thin-wall Korteweg formula, K = 2.19 GPa, &rho; = 998 kg/m&sup3;. Joukowsky head at the reference 1.39 m/s; 2L/a on the reference 12 km. Presets reproduce the materials table.</div>
  </div>
  <div class="chart-box"><canvas id="waveChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Pipe</label>
      <select id="sPre">
        <option value="0" selected>Ductile iron DN800 K9</option>
        <option value="1">Steel DN800, e = 10 mm</option>
        <option value="2">Steel DN2000, e = 20 mm</option>
        <option value="3">GRP DN800, e = 16 mm</option>
        <option value="4">HDPE PE100 DN800 SDR17</option>
        <option value="5">PVC DN300, e = 11.7 mm</option>
        <option value="6">Custom (use the sliders)</option>
      </select>
      <div class="hint">Sets D, e, E and &mu;. Moving a slider makes it a custom pipe.</div>
    </div>
    <div class="ctrl">
      <label>Restraint</label>
      <select id="sRes">
        <option value="0">Anchored at the upstream end only</option>
        <option value="1">Anchored throughout</option>
        <option value="2" selected>Expansion joints throughout</option>
      </select>
      <div class="hint">In our judgement: socket joints are closest to expansion joints; welded and buried, to anchored throughout.</div>
    </div>
    <div class="ctrl">
      <label>Diameter D <span id="vDia">800 mm</span></label>
      <input type="range" id="sDia" min="100" max="2500" value="800" step="10">
      <div class="hint">Nominal diameter.</div>
    </div>
    <div class="ctrl">
      <label>Wall thickness e <span id="vWall">11.7 mm</span></label>
      <input type="range" id="sWall" min="2" max="80" value="11.7" step="0.1">
      <div class="hint">K-class wall for ductile iron; D/SDR for plastics.</div>
    </div>
    <div class="ctrl">
      <label>Young&rsquo;s modulus E <span id="vMod">170 GPa</span></label>
      <input type="range" id="sMod" min="-0.3" max="2.35" value="2.2304489" step="any">
      <div class="hint">Log scale, 0.5&ndash;220 GPa. Short-term value for plastics; hoop value for GRP.</div>
    </div>
    <div class="ctrl">
      <label>Poisson&rsquo;s ratio &mu; <span id="vPoi">0.28</span></label>
      <input type="range" id="sPoi" min="0.2" max="0.5" value="0.28" step="0.01">
      <div class="hint">About 0.3 for metals; up to 0.45 for PE.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Wave speed</div><div class="v" id="rWa">1,080 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Joukowsky, 1.39 m/s</div><div class="v" id="rWj">153.3 <small>m</small></div></div>
    <div class="cell"><div class="k">2L/a on 12 km</div><div class="v" id="rWt">22.2 <small>s</small></div></div>
    <div class="cell"><div class="k">Wall term KD/Ee</div><div class="v" id="rWw">0.88</div></div>
    <div class="cell"><div class="k">Difference from 1,050 m/s</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rWd"><span class="badge good">+2.9 %</span></span></div></div>
  </div>
</div>
<p class="fig-note">The default, DN800 K9 with expansion joints, gives <strong>1,080&nbsp;m/s</strong>, a Joukowsky head of 153.3&nbsp;m and 2L/a of 22.2&nbsp;s, which is 2.9&nbsp;% above the design value. Steel DN800 gives 1,094&nbsp;m/s: the higher modulus is mostly cancelled by the thinner wall. HDPE PE100 SDR17 gives <strong>251&nbsp;m/s</strong>, a Joukowsky head of 35.6&nbsp;m and a 95.6&nbsp;s round trip. For the metals, a 10&nbsp;% error in E moves a by about 2.5&nbsp;%. For PE and GRP the same error moves it by about 5&nbsp;%, because a then varies almost as \(\sqrt{E}\), and in our experience a plastic&rsquo;s modulus is seldom known that closely.</p>

<h2 id="materials">4 &middot; Materials, and where the numbers come from</h2>
<div class="tbl-wrap"><table><caption>Korteweg wave speed by material and restraint</caption><thead><tr><th>Pipe</th><th class="num">E (GPa)</th><th class="num">&mu;</th><th class="num">D (mm)</th><th class="num">e (mm)</th><th class="num">Anchored upstream (m/s)</th><th class="num">Anchored throughout (m/s)</th><th class="num">Expansion joints (m/s)</th></tr></thead><tbody>
<tr><td>Ductile iron DN800 K9</td><td class="num">170</td><td class="num">0.28</td><td class="num">800</td><td class="num">11.7</td><td class="num">1,117</td><td class="num">1,101</td><td class="num">1,080</td></tr>
<tr><td>Steel DN800</td><td class="num">210</td><td class="num">0.30</td><td class="num">800</td><td class="num">10</td><td class="num">1,133</td><td class="num">1,117</td><td class="num">1,094</td></tr>
<tr><td>Steel DN2000</td><td class="num">210</td><td class="num">0.30</td><td class="num">2,000</td><td class="num">20</td><td class="num">1,079</td><td class="num">1,061</td><td class="num">1,036</td></tr>
<tr><td>GRP DN800</td><td class="num">11</td><td class="num">0.25</td><td class="num">800</td><td class="num">16</td><td class="num">475</td><td class="num">461</td><td class="num">448</td></tr>
<tr><td>HDPE PE100 DN800 SDR17</td><td class="num">1.1</td><td class="num">0.45</td><td class="num">800</td><td class="num">47.1</td><td class="num">284</td><td class="num">280</td><td class="num">251</td></tr>
<tr><td>PVC DN300</td><td class="num">3.0</td><td class="num">0.40</td><td class="num">300</td><td class="num">11.7</td><td class="num">371</td><td class="num">362</td><td class="num">334</td></tr>
</tbody></table></div>
<ul class="clean">
  <li><strong>Ductile iron.</strong> The wall comes from the ISO 2531 K-class rule [14], and the modulus is well known. The cement-mortar lining adds some stiffness the formula ignores. In our judgement it is not worth taking credit for.</li>
  <li><strong>Steel.</strong> D/e is what matters. DN2000 with a 20&nbsp;mm wall gives 1,061&nbsp;m/s anchored throughout, against 1,117&nbsp;m/s for DN800 with a 10&nbsp;mm wall. AWWA M11 covers surge in steel pipe design [11].</li>
  <li><strong>GRP.</strong> The hoop modulus depends on the laminate, so the 11&nbsp;GPa here is only an illustration. Use the manufacturer&rsquo;s value for the actual pipe [12].</li>
  <li><strong>PE and PVC.</strong> Use the short-term modulus, because a surge lasts seconds. The modulus falls as temperature rises, so the same line has a lower wave speed in summer. SDR17 pipe (D/e = 17) is thicker than the thin-wall formula strictly covers; restraint factors for thick-walled pipe are in [1, 2]. The diameter convention matters too: with the bore (705.8&nbsp;mm) instead of the outside diameter, the same pipe gives 267 rather than 251&nbsp;m/s with expansion joints, so state which you used. Wall thicknesses follow ISO 4427-2 and ISO 1452-2 [14], and AWWA M55 covers surge in PE pipe [13].</li>
  <li><strong>Mixed or encased lines.</strong> A concrete surround, a sleeve, or a PE section inside a ductile iron main changes the wave speed locally. Model each section as its own pipe. An averaged value hides the reflections at each change.</li>
</ul>

<h2 id="air">5 &middot; Air: the largest uncertainty</h2>
<p>The Korteweg formula assumes water with no free gas in it. Real mains carry some: air released from solution as the pressure falls, air drawn in at the pump suction, and air let in by air valves during the downsurge [15]. The simplified isothermal form given by Wylie &amp; Streeter [1] uses \(a_0\) for the wave speed without air, \(\alpha\) for the volume fraction of free gas at the local absolute pressure \(p\), and \(n\) for the gas exponent:</p>
<div class="eq">\[ a=\Big[\rho\Big(\frac{1}{\rho\, a_0^2}+\frac{\alpha}{n\,p}\Big)\Big]^{-1/2} \]</div>
<p>The gas term is divided by the pressure, so free air has its biggest effect at low pressure, which is exactly where the downsurge happens [2, 6]. A fixed quantity of gas also expands as the pressure falls (isothermally, \(\alpha\,p\) stays constant), so the effect at low pressure is stronger still. The table holds \(\alpha\) at the stated pressure:</p>
<div class="tbl-wrap"><table><caption>Wave speed with free air, a&#8320; = 1,050 m/s, isothermal (n = 1), &alpha; at the stated pressure, m/s</caption><thead><tr><th>Free air by volume</th><th class="num">2 bar abs</th><th class="num">5 bar abs</th><th class="num">10 bar abs</th></tr></thead><tbody>
<tr><td>0.1 %</td><td class="num">412</td><td class="num">587</td><td class="num">725</td></tr>
<tr><td>0.5 %</td><td class="num">197</td><td class="num">303</td><td class="num">412</td></tr>
<tr><td>1 %</td><td class="num">140</td><td class="num">219</td><td class="num">303</td></tr>
<tr><td>2 %</td><td class="num">100</td><td class="num">157</td><td class="num">219</td></tr>
</tbody></table></div>
<p>One-tenth of one per cent of free air at 2&nbsp;bar abs takes away <strong>61&nbsp;% of the wave speed</strong>. Compressed to 10&nbsp;bar abs, the same gas is only 0.02&nbsp;% of the volume and the wave speed recovers to about 950&nbsp;m/s, which is why the high-pressure part of a transient travels close to the pipe&rsquo;s own wave speed. Carried the other way, 0.1&nbsp;% at the steady 9.35&nbsp;bar abs at the pump becomes about 0.7&nbsp;% at the +3.0&nbsp;m limit, where the wave speed is about 134&nbsp;m/s. The low-pressure phase, which is the one a surge vessel exists to control, may travel far more slowly, and it is the part of the model we know least about [3]. How air valves let air into a line is covered in <a href="air-admission-networks.html">air admission in networks</a>.</p>

<h2 id="int-air">6 &middot; Interactive: free air and pressure</h2>
<p>Set the free-air fraction, the wave speed without air and the gas exponent. The red curve is your case. The faint curves show 0.1, 0.5, 1 and 2&nbsp;% air at the same a&#8320; and n.</p>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Wave speed of water with free air against absolute pressure</div>
    <div class="fsub">Simplified Wylie &amp; Streeter form, &rho; = 998 kg/m&sup3;, log pressure scale. Each curve holds &alpha;, the free-gas fraction at the local pressure, constant. Vertical lines: steady HGL at the pump (95.3 m abs, 9.35 bar abs) and the +3.0 m design minimum (13.33 m abs, 1.31 bar abs).</div>
  </div>
  <div class="chart-box"><canvas id="airChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Free air by volume <span id="vAl">0.10 %</span></label>
      <input type="range" id="sAl" min="0" max="3" value="0.1" step="0.01">
      <div class="hint">Undissolved gas as a fraction of volume at each pressure.</div>
    </div>
    <div class="ctrl">
      <label>Wave speed without air a&#8320; <span id="vA0">1,050 m/s</span></label>
      <input type="range" id="sA0" min="300" max="1400" value="1050" step="10">
      <div class="hint">About 1,050 for ductile iron; about 335&ndash;475 for PVC and GRP. PE (about 250&ndash;285) lies just below the range.</div>
    </div>
    <div class="ctrl">
      <label>Gas exponent n <span id="vN">1.00</span></label>
      <input type="range" id="sN" min="1" max="1.4" value="1" step="0.05">
      <div class="hint">1.0 isothermal; 1.4 adiabatic.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">At 2 bar abs</div><div class="v" id="rA2">412 <small>m/s</small></div></div>
    <div class="cell"><div class="k">At 5 bar abs</div><div class="v" id="rA5">587 <small>m/s</small></div></div>
    <div class="cell"><div class="k">At 10 bar abs</div><div class="v" id="rA10">725 <small>m/s</small></div></div>
    <div class="cell"><div class="k">At the +3.0 m limit, same &alpha;</div><div class="v" id="rAlim">342 <small>m/s</small></div></div>
    <div class="cell"><div class="k">At the limit, gas taken from 9.35 bar abs</div><div class="v" id="rAfix">134 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Lost at 2 bar abs</div><div class="v" id="rAloss">61 <small>%</small></div></div>
  </div>
</div>
<p class="fig-note">With 0.1&nbsp;% free air and a&#8320; = 1,050&nbsp;m/s, the curve gives 412, 587 and 725&nbsp;m/s at 2, 5 and 10&nbsp;bar abs, and <strong>342&nbsp;m/s</strong> at the +3.0&nbsp;m limit with the same &alpha;. The next readout follows a fixed quantity of gas instead: 0.1&nbsp;% at the steady 9.35&nbsp;bar abs leaves only <strong>134&nbsp;m/s</strong> at the limit. Raising n to 1.2 only lifts the 2&nbsp;bar value to 444&nbsp;m/s; cutting the air to 0.01&nbsp;% brings it back to 843&nbsp;m/s.</p>

<h2 id="surge-sensitivity">7 &middot; What wave speed does to the surge on a 12 km main</h2>
<p>To isolate its effect, we ran the reference main at five wave speeds (1,300, 1,050, 700, 450 and 300&nbsp;m/s) and changed nothing else: same bore, friction and HGL, all pumps stopping instantly with the check valve closing at once, and no protection. The low values are a sensitivity test on this main, not a model of a plastic line, which would have its own bore, friction and rating. The vessel columns give the smallest air-over-water vessel at the pump, with a free DN400 connection (K 0.5), that keeps the whole line at or above +3.0&nbsp;m. The shell is the gas at maximum expansion divided by 0.8, a 20&nbsp;% water reserve.</p>
<div class="tbl-wrap"><table><caption>Pump trip on the 12 km DN800 main at five wave speeds</caption><thead><tr><th class="num">a (m/s)</th><th class="num">Joukowsky (m)</th><th class="num">2L/a (s)</th><th>Unprotected minimum</th><th>Unprotected peak, both cavity models</th><th class="num">Gas at steady HGL (m&sup3;)</th><th class="num">Gas at maximum expansion (m&sup3;)</th><th class="num">Shell (m&sup3;)</th></tr></thead><tbody>
<tr><td class="num">1,300</td><td class="num">184.5</td><td class="num">18.5</td><td>&minus;9.8 m (vapour)</td><td>190&ndash;210 m</td><td class="num">3.11</td><td class="num">16.00</td><td class="num">20.0</td></tr>
<tr><td class="num">1,050</td><td class="num">149.1</td><td class="num">22.9</td><td>&minus;9.8 m (vapour)</td><td>165&ndash;190 m</td><td class="num">3.08</td><td class="num">15.30</td><td class="num">19.1</td></tr>
<tr><td class="num">700</td><td class="num">99.4</td><td class="num">34.3</td><td>&minus;9.8 m (vapour)</td><td>140&ndash;150 m</td><td class="num">3.19</td><td class="num">15.32</td><td class="num">19.1</td></tr>
<tr><td class="num">450</td><td class="num">63.9</td><td class="num">53.3</td><td>&minus;9.8 m (vapour)</td><td>85&ndash;90 m</td><td class="num">1.99</td><td class="num">10.15</td><td class="num">12.7</td></tr>
<tr><td class="num">300</td><td class="num">42.6</td><td class="num">80.0</td><td>+5.0 m (no separation)</td><td>85 m (steady; no upsurge)</td><td class="num">not needed</td><td class="num">&ndash;</td><td class="num">&ndash;</td></tr>
</tbody></table></div>
<p>The runs use a method-of-characteristics model with a vapour cavity model (120 reaches, 150&nbsp;s), cross-checked with a gas cavity model and an independent second code [1, 4, 7]. They are not Bentley HAMMER results; a project analysis must be run in HAMMER, or an equivalent, on the real profile. What they show reliably is the trend.</p>
<h3>Joukowsky is not the peak once the column separates</h3>
<p>At 1,050&nbsp;m/s the Joukowsky head is 149.1&nbsp;m but the peak is <strong>165&ndash;190&nbsp;m</strong>. The pump end drops to vapour and a cavity opens, which in the model stays open for about 47&nbsp;s, roughly two round trips. When returning water closes it, the collapse spike adds to the returning wave. Peaks fall with wave speed, as the table shows, but none can be read from Joukowsky.</p>
<h3>Why the peak is a range</h3>
<p>The collapse spike depends on how the cavity is represented. Against the vapour cavity model, the gas cavity model [7] puts these peaks between 13&nbsp;% lower and 10&nbsp;% higher, and the collapse peaks across this series between 18&nbsp;% lower and 10&nbsp;% higher, so neither is simply conservative. The design answer is not to pick a model but to stop relying on the collapse peak: protect the downsurge so the column does not separate [10].</p>
<h3>450 m/s: separation below the Joukowsky threshold</h3>
<p>The Joukowsky head is 63.9&nbsp;m, well under the 94.8&nbsp;m available, yet the line reaches vapour. The trip drops the pump head to 21.1&nbsp;m, and the head then keeps falling as the line drains toward the reservoir, reaching vapour after about 42&nbsp;s, before the reflection returns at 53.3&nbsp;s. The collapse adds little: 85&ndash;90&nbsp;m against a steady 85.0&nbsp;m.</p>
<h3>300 m/s: no separation</h3>
<p>The first drop takes the pump end to 42.4&nbsp;m, as Joukowsky predicts, and the head then drains to <strong>+5.0&nbsp;m</strong> just before the reflection arrives at 80.0&nbsp;s. There is no separation and no upsurge, and +3.0&nbsp;m is met without protection. Joukowsky&rsquo;s separation test happens to give the right answer here, but its minimum is 37&nbsp;m too high: the drain-down takes the pump end to +5.0&nbsp;m, only 2&nbsp;m above the criterion. Only the model shows that.</p>
<div class="callout warn">
  <span class="lbl">Do not design to a collapse peak</span>
  At 1,050&nbsp;m/s the two cavity models are 25&nbsp;m apart. Check the pipe class against the whole range, and keep the minimum envelope at or above the +3.0&nbsp;m design minimum, well clear of vapour. See <a href="surge-analysis-risk.html">surge analysis and risk</a>.
</div>

<h2 id="int-surge">8 &middot; Interactive: the surge at five wave speeds</h2>
<p>Choose a wave speed and a location. The dark trace is the unprotected pressure head from the vapour cavity model. The faint dashed trace is the 1,050&nbsp;m/s case at the same point. The peak readout covers both cavity models.</p>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Unprotected pump trip on the 12 km DN800 main: pressure head against time</div>
    <div class="fsub">Method of characteristics with a vapour cavity model; instant stop of all pumps; only the wave speed changes. Gas and shell: smallest free-connection vessel holding the line at or above +3.0 m.</div>
  </div>
  <div class="chart-box"><canvas id="surgeChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Wave speed</label>
      <select id="sCase">
        <option value="0">1,300 m/s: high sensitivity value</option>
        <option value="1" selected>1,050 m/s: reference design value</option>
        <option value="2">700 m/s: low sensitivity value</option>
        <option value="3">450 m/s: GRP-like flexibility</option>
        <option value="4">300 m/s: PE-like flexibility</option>
      </select>
      <div class="hint">Bore, friction and HGL stay those of the DN800 main.</div>
    </div>
    <div class="ctrl">
      <label>Location</label>
      <select id="sLoc">
        <option value="pump" selected>At the pump</option>
        <option value="mid">Mid-line, 6 km</option>
      </select>
      <div class="hint">Steady head 85.0 m at the pump, 64.9 m at 6 km. The readouts are for the whole line.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Joukowsky a&middot;v/g</div><div class="v" id="rSj">149.1 <small>m</small></div></div>
    <div class="cell"><div class="k">2L/a</div><div class="v" id="rSt">22.9 <small>s</small></div></div>
    <div class="cell"><div class="k">Line minimum</div><div class="v" id="rSm">&minus;9.8 <small>m</small> <span class="badge bad">vapour</span></div></div>
    <div class="cell"><div class="k">Line peak, both models</div><div class="v" id="rSp">165&ndash;190 <small>m</small> <span class="badge bad">above PN16</span></div></div>
    <div class="cell"><div class="k">Gas: steady &rarr; max</div><div class="v" id="rSg">3.08 &rarr; 15.30 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Vessel shell</div><div class="v" id="rSv">19.1 <small>m&sup3;</small></div></div>
  </div>
</div>
<p class="fig-note">Step from 1,050 down to 700&nbsp;m/s: the spikes and the peak readout shrink, while the gas readout barely moves. At 450 and 300&nbsp;m/s the spikes go and the vessel shrinks or disappears. On the 6&nbsp;km trace the peak is 150&ndash;160&nbsp;m, against 165&ndash;190&nbsp;m for the whole line. The 300&nbsp;m/s run covers under two round trips; run on to 320&nbsp;s, the pump head peaks at 70.6&nbsp;m and never exceeds the steady 85.0&nbsp;m.</p>

<h2 id="vessel">9 &middot; Why the vessel barely moves, and when it does</h2>
<h3>Worked example: the vessel at 1,050 m/s</h3>
<p>The sizing criterion is the smallest gas volume, in a vessel at the pump with a free DN400 connection, that keeps the whole line at or above +3.0&nbsp;m. The gas starts at 85.0 + 10.33 = 95.3&nbsp;m abs (9.35&nbsp;bar abs) and expands with n = 1.2:</p>
<div class="eq">\[ p\,V^{\,n} = \text{const} \quad\Rightarrow\quad p = 95.3\left(\frac{3.08}{15.30}\right)^{1.2} = 13.9\ \text{m abs} \]</div>
<p>The model gives <strong>3.08&nbsp;m&sup3;</strong> of gas at the steady HGL, expanding to <strong>15.30&nbsp;m&sup3;</strong> at 13.9&nbsp;m abs (about +3.6&nbsp;m gauge). The gas does not fall to +3.0&nbsp;m itself: the governing minimum is along the line, 4.6&nbsp;km from the pump in this run, not at the vessel. The vessel has delivered 12.2&nbsp;m&sup3; of water, and the shell is 15.30 / 0.8 = <strong>19.1&nbsp;m&sup3;</strong>. The method is in <a href="surge-vessel.html">Sizing the Hydropneumatic Surge Vessel</a> and Stephenson&rsquo;s simple guide [9]. The site&rsquo;s reference vessel (20&nbsp;m&sup3; shell, 3.5&nbsp;m&sup3; gas, differential DN400 connection with K 2 out and K 10 in) holds +4.3&nbsp;m minimum and 119.2&nbsp;m maximum; <a href="surge-vessel-differential-orifice.html">article 2</a> explains the orifice.</p>
<h3>The column&rsquo;s momentum does not depend on wave speed</h3>
<p>Across the stiff range the water delivered hardly changes: 12.9&nbsp;m&sup3; at 1,300&nbsp;m/s, 12.2 at 1,050 and 12.1 at 700, then 8.2 at 450. The vessel is feeding a slowing column, 6,032&nbsp;m&sup3; of water at 1.39&nbsp;m/s, whose momentum is</p>
<div class="eq">\[ M = \rho\,L\,A\,v = \rho\,L\,Q = 998 \times 12{,}000 \times 0.70 = 8.38\ \text{MN}\,\text{s} \]</div>
<p>The wave speed is not in it. What a changes on a stiff pipe is the pressure history along the line: the Joukowsky head, the timing and the collapse peaks in the table above.</p>
<h3>What does change: the water stored in the line</h3>
<p>Wave speed does set how much water the line stores per metre of head, in the stretch of the wall and the compression of the water:</p>
<div class="eq">\[ C = \frac{g\,A\,L}{a^{2}} \]</div>
<p>C is 0.054&nbsp;m&sup3; per metre at 1,050&nbsp;m/s and 0.658&nbsp;m&sup3;/m at 300&nbsp;m/s, <strong>12.25 times more</strong>. A flexible pipe gives water back from its own wall as the pressure falls, feeding the column from inside the line. At 700&nbsp;m/s storage is 2.25 times the 1,050&nbsp;m/s value and the vessel does not move. At 450&nbsp;m/s it is 5.44 times, and the gas drops 35&nbsp;% to 1.99&nbsp;m&sup3;. At 300&nbsp;m/s the line needs no vessel. Treat this qualitatively: the head does not fall evenly along the line, so C times the head drop is not the water delivered.</p>
<ul class="clean">
  <li><strong>Steel and ductile iron:</strong> refine the wave speed for pressures, pipe class and timing, not for vessel volume. Here the gas varies by less than 4&nbsp;% from 700 to 1,300&nbsp;m/s, and 700&nbsp;m/s needs the most.</li>
  <li><strong>A plastic wave speed on a steel or ductile iron main is the dangerous mistake.</strong> At 450&nbsp;m/s this main&rsquo;s vessel comes out 35&nbsp;% too small and the peak 85&ndash;90&nbsp;m instead of 165&ndash;190&nbsp;m.</li>
  <li><strong>A steel wave speed on a plastic line is also wrong.</strong> It overstates the Joukowsky head and the peaks, but it shortens 2L/a, so a closure that is rapid on the real pipe looks slow. In our judgement, from the trend of these runs, it also overstates the vessel. Size a plastic line with its own wave speed and its own model.</li>
</ul>

<h2 id="int-storage">10 &middot; Interactive: vessel volume against line storage</h2>
<p>Move the wave speed and choose which vessel quantity to plot. The blue points are the five model runs; the thin dashed segment down to zero at 300&nbsp;m/s only joins two runs and is not a computed size. The dashed amber curve is \(gAL/a^2\), calculated at any wave speed.</p>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Vessel volume and line storage against wave speed</div>
    <div class="fsub">Vessel points from the method-of-characteristics runs in section 7 (zero at 300 m/s, where none is needed). Storage C = gAL/a&sup2; for the whole 12 km line, A = 0.5027 m&sup2;.</div>
  </div>
  <div class="chart-box"><canvas id="vesChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Wave speed <span id="vAv">1,050 m/s</span></label>
      <input type="range" id="sAv" min="250" max="1400" value="1050" step="10">
      <div class="hint">Storage and timing are calculated at any value; vessel data exist at five wave speeds.</div>
    </div>
    <div class="ctrl">
      <label>Vessel quantity</label>
      <select id="sQty">
        <option value="0" selected>Gas at the steady HGL</option>
        <option value="1">Gas at maximum expansion</option>
        <option value="2">Shell volume (20 % water reserve)</option>
      </select>
      <div class="hint">All three stay flat across the stiff-pipe range.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Joukowsky a&middot;v/g</div><div class="v" id="rVj">149.1 <small>m</small></div></div>
    <div class="cell"><div class="k">2L/a</div><div class="v" id="rVt">22.9 <small>s</small></div></div>
    <div class="cell"><div class="k">Line storage C</div><div class="v" id="rVc">0.054 <small>m&sup3;/m</small></div></div>
    <div class="cell"><div class="k">Storage vs 1,050 m/s</div><div class="v" id="rVr">1.00 <small>&times;</small></div></div>
    <div class="cell"><div class="k">Nearest computed vessel</div><div class="v" style="font-size:15px;margin-top:6px;" id="rVn">1,050 m/s: 3.08 m&sup3;</div></div>
  </div>
</div>
<p class="fig-note">Compare the two curves. Storage grows as 1/a&sup2;, but across the steel and ductile iron range it stays small and the vessel line stays flat; the vessel only falls once storage has grown several times over, at 450&nbsp;m/s and below. Switch to shell volume and the shape is the same.</p>

<h2 id="bracketing">11 &middot; Design practice: choosing the wave speed and testing both sides</h2>
<p>The wave speed in a design basis should be traceable back to its source. In our practice that means three steps:</p>
<ul class="clean">
  <li><strong>Calculate.</strong> Apply Korteweg with the actual wall class or SDR, the right modulus (short-term at the operating temperature for plastics, hoop modulus for GRP), and the restraint that matches how the pipe is jointed and laid.</li>
  <li><strong>Reduce, and label it as judgement.</strong> Take a modest allowance for air and joints. For this main that gives 1,050&nbsp;m/s.</li>
  <li><strong>Test both sides.</strong> In our judgement, run a deliberately high and a deliberately low value as uniform sensitivity cases. For this main we used 1,300&nbsp;m/s, about 16&nbsp;% above the highest Korteweg value for DN800 K9 (1,117&nbsp;m/s), and 700&nbsp;m/s, two-thirds of the design value. One wave speed per pipe cannot reproduce the local slowdown that free air causes at low pressure (section 5), so the low run is a sensitivity test, not a model of the air. Do not go lower to size a vessel down: on this stiff main 450&nbsp;m/s cuts the computed gas to 1.99&nbsp;m&sup3;, 35&nbsp;% short of what 1,050&nbsp;m/s needs. For plastics, vary the modulus with temperature.</li>
</ul>
<div class="tbl-wrap"><table><caption>Which end of the range governs each check, on the reference main</caption><thead><tr><th>Check</th><th>End that governs</th><th>On this main</th></tr></thead><tbody>
<tr><td>Peak pressure and pipe class</td><td>High a</td><td>190&ndash;210 m at 1,300 m/s; 165&ndash;190 m at 1,050 m/s</td></tr>
<tr><td>Joukowsky head for a fast stop or valve slam</td><td>High a</td><td>184.5 m at 1,300 m/s; 149.1 m at 1,050 m/s</td></tr>
<tr><td>Maximum with a free-connection vessel in place</td><td>High a</td><td>140.9 m at 1,300 m/s; 130.9 m at 1,050 m/s (each with the gas sized for that wave speed)</td></tr>
<tr><td>Vessel gas for the downsurge</td><td>Not consistent; check both</td><td>3.19 m&sup3; at 700, 3.11 at 1,300, 3.08 at 1,050 m/s</td></tr>
<tr><td>Whether a closure counts as rapid (shorter than 2L/a)</td><td>Low a (longer 2L/a)</td><td>34.3 s at 700 m/s; 22.9 s at 1,050 m/s</td></tr>
<tr><td>Whether an unprotected line separates</td><td>Not settled by Joukowsky</td><td>Vapour at every wave speed down to 450 m/s</td></tr>
</tbody></table></div>
<p>The value that is conservative for peak pressure is not the one that is conservative for the downsurge, so no single &ldquo;safe&rdquo; wave speed exists. EN 805 includes surge in the maximum design pressure [16]: check the pipe class against the high-wave-speed envelope, collapse peaks as a range, and timing decisions at both ends; see <a href="check-valve-hammer.html">check valve slam</a>, <a href="water-hammer-control-valve.html">control valve closure</a> and <a href="surge-scenarios-pump-stations.html">surge scenarios in pumping stations</a>.</p>

<h2 id="hammer">12 &middot; Setting it up in Bentley HAMMER</h2>
<p>The order we work in on a pumping main [17]: set the wave speed deliberately, check what the program actually used, and run the high and low cases beside the design case.</p>
<ol>
  <li><strong>Split the line wherever the wave speed changes.</strong> Model from the Pump, with its Check Valve, to the delivery Reservoir, starting a new Pipe at every change of material, diameter, wall class or restraint.</li>
  <li><strong>Use the Wave Speed Calculator on each Pipe.</strong> Enter the pipe material, wall thickness (11.7&nbsp;mm for DN800 K9), Young&rsquo;s modulus, Poisson&rsquo;s ratio and the support/restraint condition, and check the result against a hand Korteweg value (1,080&ndash;1,117&nbsp;m/s for DN800 K9).</li>
  <li><strong>Enter the design value in the wave speed field</strong> (1,050&nbsp;m/s here), record why, and use it on every Pipe of the same construction.</li>
  <li><strong>Define the load case.</strong> On each Pump set a pump trip (shut down) at time zero, with pump and motor inertia, speed, the 4-quadrant characteristic curves and the check valve closure time or delay. No protection in the first run. The runs in this article stop the pumps instantly, which is the severe bound; with the real inertia HAMMER will show a milder first drop, so do not expect to reproduce the section 7 table.</li>
  <li><strong>Set the transient run options.</strong> Run duration of several round trips (150&nbsp;s is about 6.6 times 2L/a here). The time step is computed from the shortest pipe and the wave speeds. Set the wave speed adjustment tolerance, turn on vapour pressure / column separation, and choose the friction method.</li>
  <li><strong>Check the adjusted wave speeds</strong> against those you entered, on every Pipe. Short station pipes are where large adjustments usually appear, or they force a very small time step. In our judgement, do not coarsen the time step or loosen the wave speed adjustment tolerance so far that the main line&rsquo;s wave speed drifts by more than a few per cent.</li>
  <li><strong>Read the envelopes.</strong> In the Transient Results Viewer, plot the profile (path) with maximum and minimum head envelopes, add time histories at the pump discharge and mid-line, and use the animation to see where cavities form and collapse. Check the minimum against +3.0&nbsp;m and vapour, the maximum against 136&nbsp;m. This reference main is flat; on a real profile, subtract the pipe elevation from the head (or plot pressure) before making those comparisons.</li>
  <li><strong>Run the low and high wave speeds</strong> (700 and 1,300&nbsp;m/s here), compare envelopes with the design run, and record which run governs each check.</li>
  <li><strong>Be wary of collapse-governed maxima.</strong> Where the minimum sits at vapour, the maximum also depends on the column separation settings. Do not let the pipe class rest on it.</li>
  <li><strong>Size the protection, then rerun the range.</strong> Add a Hydropneumatic Tank at the pump (initial gas volume, gas law exponent 1.2, inlet orifice diameter, minor loss coefficient, ratio of losses, tank volume). Size it at the design wave speed, then rerun at 700 and 1,300&nbsp;m/s and confirm at each that the minimum envelope stays at or above +3.0&nbsp;m, the maximum at or below 136&nbsp;m, and the gas at maximum expansion leaves the intended water reserve; size to the governing run. Here the free-connection vessel sized at 1,050&nbsp;m/s (3.08&nbsp;m&sup3;) lets the line fall to +2.6&nbsp;m at 700&nbsp;m/s and +2.9&nbsp;m at 1,300&nbsp;m/s, so 700&nbsp;m/s sets the gas (3.19&nbsp;m&sup3;), and at 1,300&nbsp;m/s a free connection lets the maximum reach 140.9&nbsp;m even with 3.11&nbsp;m&sup3;. The site&rsquo;s reference vessel, with its differential connection, stays within both limits at all three wave speeds (minimum +3.9 to +4.3&nbsp;m, maximum 98.5 to 128.6&nbsp;m).</li>
</ol>
<p>Field names differ slightly between HAMMER versions; follow the intent of each step. The wider sequence is in <a href="hammer-transient-simulation-workflow.html">the HAMMER transient workflow</a> and <a href="hammer-transient-tips.html">HAMMER transient tips</a>.</p>

<h2 id="checklist">13 &middot; Design checklist</h2>
<ul class="clean">
  <li><strong>Calculate a for every material</strong> with Korteweg: actual wall class or SDR, the right modulus, a stated restraint condition.</li>
  <li><strong>Record the design value</strong> in the design basis, with the allowance below Korteweg labelled as judgement.</li>
  <li><strong>Compare Joukowsky with the head above vapour.</strong> For a fast (low-inertia) stop, larger means expect separation; smaller proves nothing (this main separates at 450&nbsp;m/s, and drains to +5.0&nbsp;m at 300&nbsp;m/s).</li>
  <li><strong>Run a high and a low wave speed</strong> and record which governs the peak and which the vessel.</li>
  <li><strong>Check the pipe class against the high-a envelope</strong>, with collapse-governed peaks as a range across both cavity models.</li>
  <li><strong>Expect no vessel saving</strong> from refining a on steel or ductile iron, and recheck the vessel at both ends of the range: minimum, maximum and water reserve.</li>
  <li><strong>Give every plastic line or section its own wave speed</strong>, and never put a plastic value on a steel or ductile iron main.</li>
  <li><strong>Check timing against 2L/a at both ends:</strong> check valve closure, valve stroke, relief valve opening.</li>
  <li><strong>Keep the line out of the low pressures</strong> where air valves open and gas comes out of solution; that is where a is least certain.</li>
  <li><strong>In HAMMER, confirm the adjusted wave speeds</strong> and run for several round trips.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge protection design series</span>
  <ol>
    <li><strong>Wave speed: the number that sets the surge</strong></li>
    <li><a href="surge-vessel-differential-orifice.html">The differential orifice: empty freely, refill slowly</a></li>
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
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'IBM Plex Sans',size:11}}};
const TT={font:{family:'IBM Plex Sans',size:12,weight:'600'}};
const LBL={size:10,family:'IBM Plex Sans'};
const LEG={labels:{font:{family:'IBM Plex Sans',size:11.5},usePointStyle:true,boxWidth:8}};
const D=__DATA__;
const G=9.81, KW=2.19e9, RHO=998, LEN=12000, AREF=Math.PI*0.8*0.8/4, V0=0.70/AREF;
const jouk=a=>a*V0/G, trip=a=>2*LEN/a;
const kortDe=(De,Epa,c1)=>Math.sqrt((KW/RHO)/(1+KW*De/Epa*c1));
const c1Of=(r,mu)=>r===0?1-mu/2:(r===1?1-mu*mu:1);
/* label chips take the figure ground (--sheet) at every update, so they follow a theme flip */
const SHEET=()=>{try{return getComputedStyle(document.documentElement).getPropertyValue('--sheet').trim()||'#ffffff';}catch(e){return '#ffffff';}};
const LBLBG={id:'lblbg',beforeUpdate(ch){try{const an=ch.options.plugins.annotation.annotations,bg=SHEET();
  Object.keys(an).forEach(k=>{if(an[k]&&an[k].label)an[k].label.backgroundColor=bg;});}catch(e){}}};
const note=(txt,col,pos)=>({display:true,content:txt,position:pos||'start',font:LBL,color:col,backgroundColor:'transparent'});

/* ---------- CHART 1 : Korteweg wave speed calculator ---------- */
const PRE=[{E:170,mu:0.28,D:800,e:11.7},{E:210,mu:0.30,D:800,e:10},{E:210,mu:0.30,D:2000,e:20},
           {E:11,mu:0.25,D:800,e:16},{E:1.1,mu:0.45,D:800,e:47.1},{E:3.0,mu:0.40,D:300,e:11.7}];
const sPre=document.getElementById('sPre'),sRes=document.getElementById('sRes'),sDia=document.getElementById('sDia'),
      sWall=document.getElementById('sWall'),sMod=document.getElementById('sMod'),sPoi=document.getElementById('sPoi');
let waveChart=new Chart(document.getElementById('waveChart'),{
  plugins:[LBLBG],
  data:{datasets:[
    {type:'line',label:'Anchored upstream',data:[],borderColor:'#1e8449',borderWidth:1.5,pointRadius:0,order:4},
    {type:'line',label:'Anchored throughout',data:[],borderColor:'#6b4f9e',borderWidth:1.5,pointRadius:0,order:3},
    {type:'line',label:'Expansion joints',data:[],borderColor:'#1b4f72',borderWidth:1.5,pointRadius:0,order:2},
    {type:'scatter',label:'Your pipe',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'logarithmic',min:10,max:200,title:{display:true,text:'Diameter / wall thickness, D/e',...TT},...AX},
            y:{type:'linear',min:0,max:1600,title:{display:true,text:'Wave speed a (m/s)',...TT},...AX}},
    plugins:{legend:{...LEG,reverse:true},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt0(c.parsed.y)} m/s at D/e = ${fmt1(c.parsed.x)}`}},
      annotation:{annotations:{
        des:{type:'line',scaleID:'y',value:1050,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:note('reference design value 1,050 m/s','#b9770e','start')},
        wat:{type:'line',scaleID:'y',value:Math.sqrt(KW/RHO),borderColor:'#7f8c8d',borderWidth:1.2,borderDash:[3,3],label:note('water alone, 1,481 m/s','#7f8c8d','end')}
      }}}}
});
function updWave(){
  const Dmm=+sDia.value, emm=+sWall.value, mu=+sPoi.value, r=+sRes.value;
  const E=+Math.pow(10,+sMod.value).toPrecision(3);
  document.getElementById('vDia').textContent=fmt0(Dmm)+' mm';
  document.getElementById('vWall').textContent=fmt1(emm)+' mm';
  document.getElementById('vMod').textContent=(E>=10?fmt0(E):fmt1(E))+' GPa';
  document.getElementById('vPoi').textContent=fmt2(mu);
  const De=Dmm/emm, Epa=E*1e9;
  const xmin=Math.min(10,De/1.3), xmax=Math.max(200,De*1.3);
  const xs=[];for(let i=0;i<=80;i++)xs.push(xmin*Math.pow(xmax/xmin,i/80));
  for(let k=0;k<3;k++){
    waveChart.data.datasets[k].data=xs.map(x=>({x:+x.toFixed(3),y:+kortDe(x,Epa,c1Of(k,mu)).toFixed(1)}));
    waveChart.data.datasets[k].borderWidth=(k===r)?3.5:1.5;
  }
  const a=kortDe(De,Epa,c1Of(r,mu));
  waveChart.data.datasets[3].data=[{x:+De.toFixed(3),y:+a.toFixed(1)}];
  waveChart.options.scales.x.min=xmin; waveChart.options.scales.x.max=xmax;
  waveChart.update('none');
  document.getElementById('rWa').innerHTML=fmt0(a)+' <small>m/s</small>';
  document.getElementById('rWj').innerHTML=fmt1(jouk(a))+' <small>m</small>';
  document.getElementById('rWt').innerHTML=fmt1(trip(a))+' <small>s</small>';
  document.getElementById('rWw').innerHTML=fmt2(KW*De/Epa);
  const pct=100*(a-1050)/1050, ap=Math.abs(pct);
  const cls=ap<=10?'badge good':(ap<=25?'badge warn':'badge bad');
  const txt=(pct>=0?'+':'−')+fmt1(ap)+' %'+(ap>25?' — a different pipe':'');
  document.getElementById('rWd').innerHTML='<span class="'+cls+'">'+txt+'</span>';
}
sPre.addEventListener('input',function(){
  const k=+sPre.value;
  if(k<PRE.length){const p=PRE[k];sDia.value=p.D;sWall.value=p.e;sMod.value=Math.log10(p.E);sPoi.value=p.mu;}
  updWave();
});
[sDia,sWall,sMod,sPoi].forEach(s=>s.addEventListener('input',function(){sPre.value='6';updWave();}));
sRes.addEventListener('input',updWave);
updWave();

/* ---------- CHART 2 : free air ---------- */
const sAl=document.getElementById('sAl'),sA0=document.getElementById('sA0'),sN=document.getElementById('sN');
const aAir=(al,pPa,a0,n)=>al<=0?a0:1/Math.sqrt(RHO*(1/(RHO*a0*a0)+al/(n*pPa)));
const P_SS=9.35, P_LIM=13.33*0.0981;     // bar abs: steady HGL at the pump, +3.0 m design minimum
const REFAL=[0.001,0.005,0.01,0.02];
let airChart=new Chart(document.getElementById('airChart'),{
  plugins:[LBLBG],
  data:{datasets:[
    {type:'line',label:'0.1 %',data:[],borderColor:'#5eaadd',borderWidth:1.2,borderDash:[4,3],pointRadius:0,order:6},
    {type:'line',label:'0.5 %',data:[],borderColor:'#6b4f9e',borderWidth:1.2,borderDash:[4,3],pointRadius:0,order:5},
    {type:'line',label:'1 %',data:[],borderColor:'#1e8449',borderWidth:1.2,borderDash:[4,3],pointRadius:0,order:4},
    {type:'line',label:'2 %',data:[],borderColor:'#7f8c8d',borderWidth:1.2,borderDash:[4,3],pointRadius:0,order:3},
    {type:'line',label:'Your air content',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'2, 5 and 10 bar abs',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:6,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'logarithmic',min:1,max:20,title:{display:true,text:'Absolute pressure (bar abs)',...TT},...AX},
            y:{type:'linear',min:0,max:1500,title:{display:true,text:'Wave speed a (m/s)',...TT},...AX}},
    plugins:{legend:{...LEG,reverse:true},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt0(c.parsed.y)} m/s at ${fmt2(c.parsed.x)} bar abs`}},
      annotation:{annotations:{
        lim:{type:'line',scaleID:'x',value:P_LIM,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:note('+3.0 m limit','#b9770e','start')},
        ss:{type:'line',scaleID:'x',value:P_SS,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:note('steady HGL at pump','#b9770e','start')}
      }}}}
});
function updAir(){
  const al=+sAl.value/100, a0=+sA0.value, n=+sN.value;
  document.getElementById('vAl').textContent=fmt2(al*100)+' %';
  document.getElementById('vA0').textContent=fmt0(a0)+' m/s';
  document.getElementById('vN').textContent=fmt2(n);
  const ps=[];for(let i=0;i<=80;i++)ps.push(Math.pow(20,i/80));
  REFAL.forEach((r,k)=>{airChart.data.datasets[k].data=ps.map(p=>({x:+p.toFixed(4),y:+aAir(r,p*1e5,a0,n).toFixed(1)}));});
  airChart.data.datasets[4].data=ps.map(p=>({x:+p.toFixed(4),y:+aAir(al,p*1e5,a0,n).toFixed(1)}));
  airChart.data.datasets[5].data=[2,5,10].map(p=>({x:p,y:+aAir(al,p*1e5,a0,n).toFixed(1)}));
  airChart.update('none');
  const a2=aAir(al,2e5,a0,n);
  document.getElementById('rA2').innerHTML=fmt0(a2)+' <small>m/s</small>';
  document.getElementById('rA5').innerHTML=fmt0(aAir(al,5e5,a0,n))+' <small>m/s</small>';
  document.getElementById('rA10').innerHTML=fmt0(aAir(al,10e5,a0,n))+' <small>m/s</small>';
  document.getElementById('rAlim').innerHTML=fmt0(aAir(al,P_LIM*1e5,a0,n))+' <small>m/s</small>';
  const alFix=al*Math.pow(P_SS/P_LIM,1/n);                // same gas carried from 9.35 bar abs down to the limit (p V^n const)
  document.getElementById('rAfix').innerHTML=fmt0(aAir(alFix,P_LIM*1e5,a0,n))+' <small>m/s</small>';
  document.getElementById('rAloss').innerHTML=fmt0(100*(1-a2/a0))+' <small>%</small>';
}
[sAl,sA0,sN].forEach(s=>s.addEventListener('input',updAir));updAir();

/* ---------- CHART 3 : the surge at five wave speeds (MOC) ---------- */
const sCase=document.getElementById('sCase'),sLoc=document.getElementById('sLoc');
const CS=D.ws, REF=CS[1];
const r5=v=>5*Math.round(v/5);
let surgeChart=new Chart(document.getElementById('surgeChart'),{
  plugins:[LBLBG],
  data:{datasets:[
    {type:'line',label:'a = 1,050 m/s (reference)',data:[],borderColor:'#7f8c8d',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:2},
    {type:'line',label:'Selected case, vapour cavity model',data:[],borderColor:'#1b4f72',borderWidth:2.2,pointRadius:0,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0,max:150,title:{display:true,text:'Time after the trip (s)',...TT},...AX},
            y:{type:'linear',min:-20,max:220,title:{display:true,text:'Pressure head (m)',...TT},...AX}},
    plugins:{legend:{...LEG,labels:{...LEG.labels,filter:(it,d)=>(d.datasets[it.datasetIndex].data||[]).length>0}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{
        pn:{type:'line',scaleID:'y',value:136,borderColor:'#c0392b',borderWidth:1.6,borderDash:[5,4],label:note('PN16 allowable 136 m','#c0392b','end')},
        mn:{type:'line',scaleID:'y',value:3,borderColor:'#1e8449',borderWidth:1.6,borderDash:[5,4],label:note('+3.0 m design minimum','#1e8449','end')},
        vp:{type:'line',scaleID:'y',value:-9.8,borderColor:'#6b4f9e',borderWidth:1.6,borderDash:[5,4],label:note('vapour −9.8 m','#6b4f9e','start')},
        tr:{type:'line',scaleID:'x',value:trip(1050),borderColor:'#b9770e',borderWidth:1.2,borderDash:[3,3],label:note('2L/a','#b9770e','start')}
      }}}}
});
function peakRange(c){
  const lo=Math.min(c.unprot_max,c.unprot_max_dgcm), hi=Math.max(c.unprot_max,c.unprot_max_dgcm);
  const a=r5(lo), b=r5(hi);
  if(!c.vapour) return fmt0(a)+' <small>m</small> <span class="badge good">steady, no upsurge</span>';
  const txt=(a===b?fmt0(a):fmt0(a)+'–'+fmt0(b))+' <small>m</small> ';
  if(lo>136) return txt+'<span class="badge bad">above PN16</span>';
  if(hi>136) return txt+'<span class="badge warn">depends on the model</span>';
  return txt+'<span class="badge good">below PN16</span>';
}
function updSurge(){
  const c=CS[+sCase.value]||REF, loc=(sLoc.value==='mid')?'mid':'pump';
  const H0=(loc==='mid')?64.9:85.0;                       // steady head before the trip
  const pts=cs=>[{x:0,y:H0}].concat(cs.t.map((t,i)=>({x:t,y:cs[loc][i]})));
  surgeChart.data.datasets[1].data=pts(c);
  surgeChart.data.datasets[1].label='a = '+fmt0(c.a)+' m/s, vapour cavity model';
  surgeChart.data.datasets[0].data=(c.a===1050)?[]:pts(REF);
  const an=surgeChart.options.plugins.annotation.annotations.tr;
  an.value=trip(c.a); an.label.content='2L/a = '+fmt1(trip(c.a))+' s';
  surgeChart.update('none');
  document.getElementById('rSj').innerHTML=fmt1(jouk(c.a))+' <small>m</small>';
  document.getElementById('rSt').innerHTML=fmt1(trip(c.a))+' <small>s</small>';
  document.getElementById('rSm').innerHTML=c.vapour
    ? '−9.8 <small>m</small> <span class="badge bad">vapour</span>'
    : (c.unprot_min>=0?'+':'−')+fmt1(Math.abs(c.unprot_min))+' <small>m</small> <span class="badge '+(c.unprot_min>=3?'good">meets +3.0 m':'warn">below +3.0 m')+'</span>';
  document.getElementById('rSp').innerHTML=peakRange(c);
  document.getElementById('rSg').innerHTML=c.vessel_needed
    ? fmt2(c.gas)+' → '+fmt2(c.gas_max)+' <small>m³</small>'
    : '<span class="badge good">not needed</span>';
  document.getElementById('rSv').innerHTML=c.vessel_needed?fmt1(c.vessel_total)+' <small>m³</small>':'– <small>m³</small>';
}
[sCase,sLoc].forEach(s=>s.addEventListener('input',updSurge));updSurge();

/* ---------- CHART 4 : vessel volume against line storage ---------- */
const sAv=document.getElementById('sAv'),sQty=document.getElementById('sQty');
const QK=['gas','gas_max','vessel_total'], QN=['Gas at steady HGL','Gas at maximum expansion','Vessel shell'], QMAX=[4,18,22];
const A_ROUND=0.5027;                                   // m², the bore area as quoted in the text
const storage=a=>G*A_ROUND*LEN/(a*a);
const SORTED=CS.slice().sort((p,q)=>p.a-q.a);
let vesChart=new Chart(document.getElementById('vesChart'),{
  plugins:[LBLBG],
  data:{datasets:[
    {type:'line',label:'Gas at steady HGL (MOC runs)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.5,pointRadius:5,yAxisID:'y',order:2,
     segment:{borderDash:ctx=>(ctx&&ctx.p0&&ctx.p0.parsed&&ctx.p0.parsed.x<400)?[4,4]:undefined,
              borderWidth:ctx=>(ctx&&ctx.p0&&ctx.p0.parsed&&ctx.p0.parsed.x<400)?1.2:undefined}},
    {type:'line',label:'Line storage gAL/a²',data:[],borderColor:'#b9770e',borderWidth:2.2,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:3},
    {type:'scatter',label:'Selected wave speed',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y1',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:250,max:1400,title:{display:true,text:'Wave speed a (m/s)',...TT},...AX},
            y:{type:'linear',position:'left',min:0,max:4,title:{display:true,text:'Vessel volume (m³)',...TT},...AX},
            y1:{type:'linear',position:'right',min:0,max:1,title:{display:true,text:'Line storage (m³ per m of head)',...TT},grid:{drawOnChartArea:false},ticks:{font:{family:'IBM Plex Sans',size:11}}}},
    plugins:{legend:LEG,
      tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`${fmt3(c.parsed.y)} m³/m at ${fmt0(c.parsed.x)} m/s`:`${fmt2(c.parsed.y)} m³ at ${fmt0(c.parsed.x)} m/s`}},
      annotation:{annotations:{
        av:{type:'line',scaleID:'x',value:1050,borderColor:'#c0392b',borderWidth:1.2,borderDash:[3,3]}
      }}}}
});
function updVes(){
  const a=+sAv.value, q=+sQty.value||0;
  document.getElementById('vAv').textContent=fmt0(a)+' m/s';
  vesChart.data.datasets[0].data=SORTED.map(c=>({x:c.a,y:c[QK[q]]}));
  vesChart.data.datasets[0].label=QN[q]+' (MOC runs)';
  vesChart.options.scales.y.max=QMAX[q];
  const xs=[];for(let x=250;x<=1400;x+=10)xs.push(x);
  vesChart.data.datasets[1].data=xs.map(x=>({x:x,y:+storage(x).toFixed(4)}));
  vesChart.data.datasets[2].data=[{x:a,y:+storage(a).toFixed(4)}];
  vesChart.options.plugins.annotation.annotations.av.value=a;
  vesChart.update('none');
  document.getElementById('rVj').innerHTML=fmt1(jouk(a))+' <small>m</small>';
  document.getElementById('rVt').innerHTML=fmt1(trip(a))+' <small>s</small>';
  document.getElementById('rVc').innerHTML=fmt3(storage(a))+' <small>m³/m</small>';
  document.getElementById('rVr').innerHTML=fmt2(storage(a)/storage(1050))+' <small>×</small>';
  let near=SORTED[0];SORTED.forEach(c=>{if(Math.abs(c.a-a)<Math.abs(near.a-a))near=c;});
  const val=near.vessel_needed?((q===2?fmt1(near[QK[q]]):fmt2(near[QK[q]]))+' m³'):'not needed';
  document.getElementById('rVn').innerHTML=fmt0(near.a)+' m/s: '+val;
}
[sAv,sQty].forEach(s=>s.addEventListener('input',updVes));updVes();

window.addEventListener('load',function(){try{waveChart.resize();airChart.resize();surgeChart.resize();vesChart.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993 — Korteweg wave speed with restraint factors, wave speed with free gas, method of characteristics, vapour cavity model.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014 — wave speed in thin- and thick-walled pipe, free gas, Joukowsky head.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004 — pump trip transients, round-trip time, uncertainty of wave speed with entrained air.</li>
  <li>Larock, B.E., Jeppson, R.W. &amp; Watters, G.Z. <em>Hydraulics of Pipeline Systems</em>. CRC Press, 2000 — method-of-characteristics implementation and pump boundaries.</li>
  <li>Parmakian, J. <em>Waterhammer Analysis</em>. Dover, 1963 — the Joukowsky relation and pump-trip waterhammer.</li>
  <li>Swaffield, J.A. &amp; Boldy, A.P. <em>Pressure Surge in Pipe and Duct Systems</em>. Avebury Technical, 1993 — surge propagation and the effect of free air on wave speed.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006 — vapour and gas cavity models and the sensitivity of collapse pressures.</li>
  <li>Stephenson, D. <em>Pipeline Design for Water Engineers</em>, 3rd ed. Elsevier, 1989 — water hammer in pumping main design.</li>
  <li>Stephenson, D. &ldquo;Simple guide for design of air vessels for water hammer protection of pumping lines.&rdquo; <em>Journal of Hydraulic Engineering</em> (ASCE), 128(8), 2002 — air vessel sizing.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005 — transient analysis and protection practice.</li>
  <li>AWWA M11 <em>Steel Pipe — A Guide for Design and Installation</em> — surge in steel pipe design.</li>
  <li>AWWA M45 <em>Fiberglass Pipe Design</em> — surge in GRP pipe design.</li>
  <li>AWWA M55 <em>PE Pipe — Design and Installation</em> — surge in polyethylene pipe design.</li>
  <li>ISO 2531 <em>Ductile iron pipes, fittings, accessories and their joints for water applications</em>; ISO 4427-2 <em>Polyethylene (PE) pipes for water supply</em>; ISO 1452-2 <em>PVC-U pipes for water supply</em> — K-class and SDR wall thicknesses.</li>
  <li>AWWA M51 <em>Air Valves: Air-Release, Air/Vacuum, and Combination</em> — air admission during transients.</li>
  <li>EN 805 <em>Water supply — Requirements for systems and components outside buildings</em> — maximum design pressure including surge.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> product documentation and help — Wave Speed Calculator, wave speed adjustment, column separation, Hydropneumatic Tank, Transient Results Viewer.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#WaveSpeed #SurgeAnalysis #WaterHammer #HydraulicTransients #Joukowsky #Korteweg #PumpTrip #ColumnSeparation #VapourCavity #MethodOfCharacteristics #SurgeVessel #AirVessel #HydropneumaticTank #DuctileIron #SteelPipe #GRP #HDPE #PVC #EntrainedAir #FreeAir #TransmissionMains #PumpingMains #PipeClass #SensitivityAnalysis #BentleyHAMMER #OpenFlowsHAMMER #EN805 #WaterInfrastructure #PipelineDesign</div>
"""

import json, os
_D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'datasets.json')))
DATA = {'ws': _D['wavespeed']['cases']}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='wave-speed-surge-analysis', cat='surge', mins=37,
    date_iso='2026-09-16', date_human='September 2026', date_ar='سبتمبر 2026',
    title='Wave Speed in Surge Analysis: The Number That Sets the Surge but Barely Moves the Surge Vessel',
    reg_title='Wave Speed in Surge Analysis: The Number That Sets the Surge but Barely Moves the Surge Vessel',
    reg_tag='Surge Analysis · Wave Speed · Pipe Materials',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Wave Speed &middot; Pipe Materials',
    desc='How wave speed sets the Joukowsky head, the 2L/a timing, column separation and peak pressure on a 12 km DN800 pumping main, and why the surge vessel barely changes on ductile iron or steel: Korteweg by material and restraint, free air, cavity-model ranges, a Bentley HAMMER procedure and four interactive charts.',
    og_desc='On a 12 km DN800 ductile iron main, wave speed moves the Joukowsky head from 99.4 to 184.5 m and the unprotected peak from 140–150 to 190–210 m, yet the surge vessel gas stays at 3.08–3.19 m³ from 700 to 1,300 m/s.',
    ld_desc='A design guide to wave speed in surge analysis: Korteweg by pipe material and restraint, free air, pump-trip results at five wave speeds, why vessel size barely changes on stiff pipe, and a HAMMER procedure.',
    img_alt='Illustration of a sectioned transmission pipeline on a dark blue background: glowing pressure wave fronts travel through the water past a cluster of air bubbles at a joint, with steel, ductile iron, GRP and HDPE wall sections above and an inset graph of wave speed falling as entrained air rises',
    en_tag='Surge &amp; Transient Analysis &middot; Wave Speed',
    en_title='Wave Speed in Surge Analysis: The Number That Sets the Surge but Barely Moves the Surge Vessel',
    en_excerpt='On a 12 km DN800 ductile iron main, cutting the wave speed from 1,050 to 700 m/s drops the Joukowsky head from <strong>149.1 to 99.4 m</strong> and the unprotected peak from 165–190 m to 140–150 m, yet the air-over-water vessel needed to hold +3.0 m barely moves: <strong>3.08 to 3.19 m³</strong> of gas from 700 to 1,300 m/s. Only flexible pipe changes that, with <strong>1.99 m³ at 450 m/s</strong> and no vessel at 300 m/s. Wave speed still sets the Joukowsky head, the 2L/a clock and whether the column separates. Covers Korteweg by material and restraint, free air, cavity-model ranges and a HAMMER procedure, with four interactive charts.',
    en_search='wave speed pressure wave celerity surge analysis water hammer hydraulic transients Joukowsky head Korteweg formula pipe restraint factor anchored expansion joints Poisson ratio Young modulus bulk modulus ductile iron K9 wall thickness ISO 2531 steel pipe GRP HDPE PE100 SDR17 PVC short-term modulus entrained air free gas wave speed reduction 2L/a round trip time pump trip power failure column separation vapour cavity model DVCM gas cavity model DGCM collapse peak method of characteristics MOC surge vessel air vessel hydropneumatic tank gas volume pipe capacitance line storage momentum sensitivity analysis bracketing pipe class PN16 EN 805 Bentley HAMMER Wave Speed Calculator wave speed adjustment tolerance time step transient results viewer envelopes',
    ar_title='سرعة الموجة في تحليل المطرقة المائية: الرقم الذي يحدد ذروة الضغط ولا يكاد يغيّر خزان الحماية',
    ar_excerpt='على خط ناقل بطول ١٢ كم وقطر ٨٠٠ مم من حديد الدكتايل، يؤدي خفض سرعة الموجة من ١٠٥٠ إلى ٧٠٠ م/ث إلى خفض ضاغط جوكوفسكي من <strong>١٤٩٫١ إلى ٩٩٫٤ م</strong>، بينما يبقى حجم الغاز اللازم في خزان الحماية بين <strong>٣٫٠٨ و٣٫١٩ م³</strong> لسرعات بين ٧٠٠ و١٣٠٠ م/ث. لا يصغر الخزان إلا عندما تنخفض السرعة إلى قيم الأنابيب عالية المرونة: <strong>١٫٩٩ م³</strong> عند ٤٥٠ م/ث. وتبقى سرعة الموجة حاسمة لضاغط جوكوفسكي وزمن ذهاب الموجة وإيابها وحدوث انفصال العمود المائي. مع أربعة رسوم تفاعلية وخطوات النمذجة في HAMMER.',
    ar_search='سرعة الموجة سرعة انتشار موجة الضغط تحليل الطرق المائي المطرقة المائية الظواهر العابرة ضاغط جوكوفسكي معادلة كورتيفيغ تثبيت الأنبوب وصلات التمدد نسبة بواسون معامل المرونة معامل الانضغاط حديد الدكتايل الحديد المرن الصلب الألياف الزجاجية البولي إيثيلين عالي الكثافة بي في سي الهواء المحتبس الغاز الحر توقف المضخات انقطاع الكهرباء انفصال العمود المائي تجويف البخار نموذج التجويف الغازي طريقة الخطوط المميزة خزان الحماية خزان الحماية الهيدروهوائي خزان الضغط الهوائي الخزان الهوائي حجم الغاز تخزين الخط كمية الحركة تحليل الحساسية فئة الضغط PN16 برنامج HAMMER حاسبة سرعة الموجة خطوط النقل الرئيسية',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
