# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">At tender stage a surge study rarely has a motor data sheet, a pump inertia or a complete pump characteristic, yet the pump trip that sizes the protection depends on all three. The usual answer is the correlation built into HAMMER's inertia calculator, which gives <strong>44.0&nbsp;kg&middot;m&sup2;</strong> for our 685&nbsp;kW, 1,480&nbsp;rpm set. On a 4&nbsp;km main from the same station, that estimate puts the lowest head anywhere between <strong>&minus;0.3 and +3.2&nbsp;m</strong> depending on the torque characteristic, either side of the +3.0&nbsp;m criterion. At 25&nbsp;kg&middot;m&sup2; the line fails under every characteristic we tried; at 88 it passes under all of them. On the 12&nbsp;km reference main the same uncertainty changes nothing: the line reaches vapour at any credible inertia. This article shows how to estimate the data, how to tell whether the estimate matters, and what to demand from the pump supplier.</p>

<h2 id="what-the-trip-needs">1 &middot; What the pump trip needs from the pump</h2>
<p>After a power failure the motor torque disappears and the rotating parts slow down under the torque the water still demands from the impeller [1][2]:</p>
<div class="eq">\[ I\,\frac{d\omega}{dt} \;=\; -\,T_{hyd}(\omega, Q) \;-\; T_{loss}, \qquad I = I_{motor} + I_{pump} + I_{coupling} + I_{water} \]</div>
<p>Three pieces of pump data decide how that rundown goes:</p>
<ul class="clean">
  <li><strong>The inertia \(I\)</strong> of everything on the shaft, which sets how much energy is stored and how fast it is given up.</li>
  <li><strong>The torque the pump absorbs</strong> as speed and flow fall, including the zones where flow or rotation reverse. It comes from the complete, or four-quadrant, characteristic.</li>
  <li><strong>The head the slowing pump still produces</strong>, from the same characteristic, which is what the pipeline sees.</li>
</ul>
<p>HAMMER asks for these as the pump's <strong>Inertia (Pump and Motor)</strong>, its <strong>Speed</strong> and its <strong>Specific Speed</strong>, which selects a built-in four-quadrant curve [3][4]. The <a href="hammer-transient-simulation-workflow.html">HAMMER workflow article</a> shows where they are entered. This article is about where the numbers come from when nobody has given them to you.</p>
<p>The station is the one used throughout the surge series: 0.70&nbsp;m&sup3;/s at 80&nbsp;m pump head on a 5&nbsp;m suction, 1,480&nbsp;rpm, efficiency 0.80, which gives 685&nbsp;kW of shaft power and a rated torque of 4,420&nbsp;N&middot;m. We test it on four mains of the same DN800 ductile iron line and the same friction gradient: 1, 2, 4 and 12&nbsp;km long, with 2L/a from 1.9 to 22.9&nbsp;s. The 12&nbsp;km main is the reference main of the series [5].</p>

<h2 id="estimate-inertia">2 &middot; Estimating inertia without a data sheet</h2>
<p>The correlations most programs use for a first estimate are attributed to Thorley and quoted in Wylie and Streeter [1][6]. HAMMER's <strong>Pump and Motor Inertia Calculator</strong> uses an empirical relation from Thorley, with the brake power at best efficiency and the speed as inputs [3]. With \(P\) in kW, \(N\) in rpm and \(I\) in kg&middot;m&sup2;:</p>
<div class="eq">\[ I_{motor} \;=\; 118\left(\frac{P}{N}\right)^{1.48}, \qquad I_{pump} \;=\; 1.5\times10^{7}\left(\frac{P}{N^{3}}\right)^{0.9556} \]</div>
<p>For our set:</p>
<div class="eq">\[ I_{motor} = 118\left(\frac{685}{1480}\right)^{1.48} = __IM__\ \text{kg m}^2, \qquad I_{pump} = 1.5\times10^{7}\left(\frac{685}{1480^{3}}\right)^{0.9556} = __IP__\ \text{kg m}^2 \]</div>
<p>The total is <strong>__IT__&nbsp;kg&middot;m&sup2;</strong>, of which the motor is 86&nbsp;%: the motor rotor dominates, and the impeller adds about a sixth of the motor figure here. The series so far has used 25&nbsp;kg&middot;m&sup2; as an assumed bare-set value; the correlation gives 76&nbsp;% more. Neither is wrong. A correlation fitted to a population of machines describes the population, and individual motors scatter widely around it: high-efficiency and large-frame motors carry more rotor, and some users report calculator estimates several times the maker's figure for a particular set. Treat the estimate as the centre of a range, and test the range.</p>
<div class="callout warn">
  <span class="lbl">Units: the factor-of-four trap</span>
  Data sheets give inertia as \(I\) (kg&middot;m&sup2;), as GD&sup2; (kg&middot;m&sup2;, which is \(4I\)), or as WR&sup2; or WK&sup2; (lb&middot;ft&sup2;, which is \(I\) in imperial units; multiply by 0.0421 for kg&middot;m&sup2;). A motor sheet quoting &ldquo;GD&sup2; = 176&nbsp;kg&middot;m&sup2;&rdquo; and a pump sheet quoting &ldquo;J = 6.3&nbsp;kg&middot;m&sup2;&rdquo; describe the same set as our estimate. Typing the GD&sup2; straight into the inertia field quadruples the rotor.
</div>
<p>Two more contributions are often forgotten. The water inside the impeller rotates with it and adds to the pump inertia; manufacturers state whether their figure is &ldquo;dry&rdquo; or &ldquo;wet&rdquo;. A spacer coupling on a large set can add a few percent. On a vertical turbine pump the line shaft and every bowl assembly count.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pump and motor inertia from power and speed</div>
    <div class="fsub">Thorley correlations as quoted in [1][6]: \(I_{motor} = 118(P/N)^{1.48}\), \(I_{pump} = 1.5\times10^7(P/N^3)^{0.9556}\). Total against shaft power for four synchronous speeds, log scales, with your set marked. Stored energy \(E = \tfrac12 I\omega^2\), time constant \(\tau = E/P\).</div>
  </div>
  <div class="chart-box"><canvas id="inChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Shaft power at best efficiency <span id="vP">685 kW</span></label>
      <input type="range" id="sP" min="10" max="3000" value="685" step="5">
      <div class="hint">Brake power, not motor rating.</div>
    </div>
    <div class="ctrl">
      <label>Speed</label>
      <select id="sN">
        <option value="2960">2,960 rpm (2-pole, 50 Hz)</option>
        <option value="1480" selected>1,480 rpm (4-pole, 50 Hz)</option>
        <option value="990">990 rpm (6-pole, 50 Hz)</option>
        <option value="740">740 rpm (8-pole, 50 Hz)</option>
        <option value="1780">1,780 rpm (4-pole, 60 Hz)</option>
      </select>
      <div class="hint">Running speed of the set.</div>
    </div>
    <div class="ctrl">
      <label>Uncertainty band <span id="vBand">&plusmn;50 %</span></label>
      <input type="range" id="sBand" min="10" max="100" value="50" step="5">
      <div class="hint">The range to test in the model, on either side of the estimate.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Motor</div><div class="v" id="rIm">&ndash;</div></div>
    <div class="cell"><div class="k">Pump</div><div class="v" id="rIp">&ndash;</div></div>
    <div class="cell"><div class="k">Total I</div><div class="v" id="rIt">&ndash;</div></div>
    <div class="cell"><div class="k">GD&sup2; (= 4I)</div><div class="v" id="rGD">&ndash;</div></div>
    <div class="cell"><div class="k">WR&sup2;</div><div class="v" id="rWR">&ndash;</div></div>
    <div class="cell"><div class="k"><span style="text-transform:none">&tau;</span> = E/P</div><div class="v" id="rTau">&ndash;</div></div>
    <div class="cell"><div class="k">Range to test</div><div class="v" id="rRange" style="font-size:17px;">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">At 685&nbsp;kW and 1,480&nbsp;rpm the set stores 0.53&nbsp;MJ, enough to supply rated power for 0.77&nbsp;s. Drop to 740&nbsp;rpm at the same power and the inertia rises 3.4 times, because a slower machine for the same power is a bigger machine, yet the stored energy falls by 14&nbsp;%, since it goes with the square of speed. A two-pole set at 2,960&nbsp;rpm has a third of the inertia but stores 31&nbsp;% more energy (&tau; = 1.0&nbsp;s). By the correlation, speed matters less than most engineers expect: across four speeds &tau; stays between 0.66 and 1.0&nbsp;s for this power.</p>

<h2 id="specific-speed">3 &middot; Specific speed and the four-quadrant curve</h2>
<p>During a trip the pump passes through states its catalogue curve never shows: reduced speed at normal flow, zero flow while still turning, reverse flow through a forward-turning impeller and, without a check valve, reverse rotation as a turbine. The complete characteristic covers all of them, usually in the Suter form, two functions \(W_H\) and \(W_B\) of the angle \(\theta = \arctan(\alpha/v)\), where \(\alpha\) and \(v\) are speed and flow as fractions of rated [1][2][7]. Nobody measures this for a project pump. Programs carry a small library of measured characteristics, one per specific speed, and scale them to the rated point of your pump. The specific speed tells the program which shape to borrow:</p>
<div class="eq">\[ N_s \;=\; \frac{N\sqrt{Q}}{H^{3/4}} \;=\; \frac{1480\sqrt{0.70}}{80^{3/4}} \;=\; __NS__ \quad (\text{rpm, m}^3\text{/s, m per stage}) \]</div>
<p>In US units (rpm, gpm, ft) the same pump is __NSUS__. HAMMER's documentation lists typical values with built-in curves of 25, 94 and 145 in SI units (1,280, 4,850 and 7,500 in US units), and tells the user to select the closest available setting [4]; further curves in its library come from Stepanoff and from Thorley and Chaudhry [3][8][9]. Our pump at __NS__ sits between the radial curve at 25 and the mixed-flow curve at 94, nearer the radial one. The documentation adds two points worth repeating: the error from using the wrong curve cannot be interpolated by specific speed, so it should be bracketed by running neighbouring curves, and results are less sensitive to the choice when a check valve stops reverse flow [4].</p>
<p>We cannot reproduce HAMMER's library curves here, so to show what the characteristic does we use the three rundown torque laws already used in <a href="pump-inertia-flywheel-surge.html">Pump Inertia and the Flywheel</a>: constant efficiency on the head actually produced (&ldquo;duty&rdquo;), a law that never lets the torque fall below what the shut-off head would demand (&ldquo;shut-off&rdquo;), and a generic radial characteristic \(\beta/\alpha^2 = 0.45 + 0.75x - 0.2x^2\) (&ldquo;radial&rdquo;). Each pump has an ideal check valve. These are stand-ins for the spread between real characteristics, not substitutes for them.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Specific speed and the nearest built-in characteristic</div>
    <div class="fsub">\(N_s = N\sqrt{Q}/H^{3/4}\) at best efficiency, per stage (SI: rpm, m&sup3;/s, m). US value = SI &times; 51.64. Dimensionless \(\Omega = \omega\sqrt{Q}/(gH)^{3/4}\). Markers: HAMMER's typical values 25, 94 and 145 [4].</div>
  </div>
  <div class="chart-box" style="height:200px;"><canvas id="nsChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Flow at best efficiency <span id="vQ">0.70 m³/s</span></label>
      <input type="range" id="sQ" min="0.01" max="3" value="0.7" step="0.01">
      <div class="hint">Per pump, not per station.</div>
    </div>
    <div class="ctrl">
      <label>Head at best efficiency <span id="vH">80 m</span></label>
      <input type="range" id="sH" min="5" max="300" value="80" step="1">
      <div class="hint">Total pump head.</div>
    </div>
    <div class="ctrl">
      <label>Speed <span id="vNs">1,480 rpm</span></label>
      <input type="range" id="sNs" min="500" max="3600" value="1480" step="10">
      <div class="hint">Running speed.</div>
    </div>
    <div class="ctrl">
      <label>Stages <span id="vSt">1</span></label>
      <input type="range" id="sSt" min="1" max="8" value="1" step="1">
      <div class="hint">Head is divided by the number of stages.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">N<sub>s</sub> (SI)</div><div class="v" id="rNs">&ndash;</div></div>
    <div class="cell"><div class="k">N<sub>s</sub> (US)</div><div class="v" id="rNsUS">&ndash;</div></div>
    <div class="cell"><div class="k">&Omega; (dimensionless)</div><div class="v" id="rOm">&ndash;</div></div>
    <div class="cell"><div class="k">Impeller type</div><div class="v" style="font-size:15px;margin-top:6px;" id="rType">&ndash;</div></div>
    <div class="cell"><div class="k">Closest HAMMER value</div><div class="v" id="rClose">&ndash;</div></div>
    <div class="cell"><div class="k">Bracket with</div><div class="v" style="font-size:15px;margin-top:6px;" id="rBr">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The impeller-type bands are indicative: radial below about 40 (SI), mixed flow from about 40 to 160, axial above. A multistage pump is assessed per stage, which is why a high-head multistage pump often lands at a low specific speed. When a pump falls between two library curves, run both and design to the worse.</p>

<h2 id="int-trip">4 &middot; Interactive: one trip, four mains</h2>
<p>Choose a main length, an inertia and a torque law and watch the pump slow down and the head at the pump fall. The grey trace is the same main with the pump stopping instantly, the most conservative assumption a model can make.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pump trip with no protection: speed and pump-end head</div>
    <div class="fsub">Method-of-characteristics model with a vapour cavity model, DN800 ductile iron, a = 1,050&nbsp;m/s, 0.70&nbsp;m&sup3;/s, 85.0&nbsp;m at the pump, same friction gradient on every length, 100&nbsp;m reaches (50 and 25&nbsp;m on the 2 and 1&nbsp;km mains). Ideal check valve at the pump. Readouts come from the full runs.</div>
  </div>
  <div class="chart-box"><canvas id="tripChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Main</label>
      <select id="sMain">
        <option value="0">12 km (2L/a = 22.9 s)</option>
        <option value="1" selected>4 km (2L/a = 7.6 s)</option>
        <option value="2">2 km (2L/a = 3.8 s)</option>
        <option value="3">1 km (2L/a = 1.9 s)</option>
      </select>
      <div class="hint">Same pump station, same flow and friction gradient.</div>
    </div>
    <div class="ctrl">
      <label>Total inertia</label>
      <select id="sI">
        <option value="25">25 kg&middot;m&sup2; (series assumption)</option>
        <option value="44" selected>44 kg&middot;m&sup2; (correlation estimate)</option>
        <option value="88">88 kg&middot;m&sup2; (twice the estimate)</option>
        <option value="176">176 kg&middot;m&sup2;</option>
        <option value="400">400 kg&middot;m&sup2; (with a flywheel)</option>
      </select>
      <div class="hint">Motor, pump, coupling and water.</div>
    </div>
    <div class="ctrl">
      <label>Torque characteristic</label>
      <select id="sLaw">
        <option value="radial" selected>Generic radial</option>
        <option value="duty">Constant efficiency (duty)</option>
        <option value="shutoff">Shut-off floor</option>
      </select>
      <div class="hint">Stand-ins for the spread between real four-quadrant curves.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k"><span style="text-transform:none">&tau; / (2L/a)</span></div><div class="v" id="rRat">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest head on line</div><div class="v" id="rLmin">&ndash;</div></div>
    <div class="cell"><div class="k">Where</div><div class="v" style="font-size:15px;margin-top:6px;" id="rWhere">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest at pump</div><div class="v" id="rPmin">&ndash;</div></div>
    <div class="cell"><div class="k">Highest head on line</div><div class="v" id="rLmax">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict at +3.0 m</div><div class="v" style="font-size:15px;margin-top:6px;" id="rVer">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">On the 4&nbsp;km main with the estimated 44&nbsp;kg&middot;m&sup2; and the radial law, the speed falls below half in 1.5&nbsp;s and the line bottoms out at +1.8&nbsp;m, 1.0&nbsp;km from the pump. Switch to the duty law and it passes at +3.2&nbsp;m; switch to the shut-off law and it fails at &minus;0.3&nbsp;m. On the 12&nbsp;km main every inertia up to 88&nbsp;kg&middot;m&sup2; takes the line to vapour, or within 0.1&nbsp;m of it, whatever the law: the rundown is over long before the first reflection returns at 22.9&nbsp;s. On the 1&nbsp;km main even 25&nbsp;kg&middot;m&sup2; keeps the line above +6.8&nbsp;m. The instant-stop trace shows why nobody should design a short main on that assumption: it predicts vapour and collapse peaks of 240&ndash;295&nbsp;m on the three short mains, while the estimated 44&nbsp;kg&middot;m&sup2; keeps the 1 and 2&nbsp;km lines above +5&nbsp;m under every law.</p>

<h2 id="does-it-matter">5 &middot; Does the inertia estimate matter? Look at &tau; against 2L/a</h2>
<p>The comparison that decides whether the pump data matter is the rundown time against the pipeline's wave period. The time constant \(\tau = E/P = I\omega_0^2/2P\) is 0.77&nbsp;s for the estimated set. Set against 2L/a:</p>
<div class="tbl-wrap"><table>
  <caption>Lowest head on the line (m) for three torque laws, no protection, criterion +3.0&nbsp;m. Ranges run from the least to the most favourable law</caption>
  <thead><tr><th>Main</th><th class="num">2L/a <span style="text-transform:none">(s)</span></th><th class="num"><span style="text-transform:none">&tau;/(2L/a)</span> at 44</th><th class="num">Instant stop</th><th class="num">I = 25</th><th class="num">I = 44</th><th class="num">I = 88</th><th class="num">I = 176</th></tr></thead>
  <tbody>
__TABROWS__
  </tbody>
</table></div>
<ul class="clean">
  <li><strong>Long main, small ratio (12&nbsp;km, &tau;/(2L/a) = 0.03).</strong> The pump is effectively stopped before the line knows anything about it. Inertia between 25 and 88&nbsp;kg&middot;m&sup2; changes nothing, the line reaches vapour and protection is needed. Model the real inertia anyway, but do not chase the data.</li>
  <li><strong>Middle ground (4&nbsp;km, ratio 0.10).</strong> The answer depends on both the inertia and the characteristic. At the estimate, the three laws straddle the criterion. This is where a wrong guess changes the design, and where a vendor's inertia and four-quadrant data earn their cost.</li>
  <li><strong>Short main, larger ratio (1&ndash;2&nbsp;km, ratio 0.2&ndash;0.4).</strong> Inertia alone protects the line at the estimated value. The instant-stop assumption would buy protection that is not needed.</li>
</ul>
<p>The upsurge tells the same story. On the 4&nbsp;km main the maxima stay between 129 and 135&nbsp;m for every inertia up to 88&nbsp;kg&middot;m&sup2; and every law, close to the 136&nbsp;m project limit used in this series, so the upsurge check needs the same care as the downsurge.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Minimum head against inertia, three torque laws</div>
    <div class="fsub">Same runs as above. The shaded band is the uncertainty range around the 44&nbsp;kg&middot;m&sup2; estimate; the line is the three laws' lowest result at each inertia. Points at &minus;9.8&nbsp;m are vapour. Inertia on a log scale.</div>
  </div>
  <div class="chart-box"><canvas id="sensChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Main</label>
      <select id="sMain2">
        <option value="0">12 km (2L/a = 22.9 s)</option>
        <option value="1" selected>4 km (2L/a = 7.6 s)</option>
        <option value="2">2 km (2L/a = 3.8 s)</option>
        <option value="3">1 km (2L/a = 1.9 s)</option>
      </select>
      <div class="hint">The 12 km main is the series reference.</div>
    </div>
    <div class="ctrl">
      <label>Design minimum <span id="vCrit">+3.0 m</span></label>
      <input type="range" id="sCrit" min="-5" max="15" value="3" step="0.5">
      <div class="hint">Pressure head above the pipe.</div>
    </div>
    <div class="ctrl">
      <label>Uncertainty on the estimate <span id="vBand2">&plusmn;50 %</span></label>
      <input type="range" id="sBand2" min="10" max="100" value="50" step="5">
      <div class="hint">Drawn as the shaded band.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">At 44 kg·m², worst law</div><div class="v" id="rW44">&ndash;</div></div>
    <div class="cell"><div class="k">At 44 kg·m², best law</div><div class="v" id="rB44">&ndash;</div></div>
    <div class="cell"><div class="k">Decision at the estimate</div><div class="v" style="font-size:14px;margin-top:6px;" id="rDec">&ndash;</div></div>
    <div class="cell"><div class="k">Smallest tested I passing all laws</div><div class="v" id="rSmall">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">&ldquo;Decision at the estimate&rdquo; compares the worst and best law at 44&nbsp;kg&middot;m&sup2; with the criterion: if both pass, the estimate is good enough; if both fail, protection is needed whatever the data say; if they disagree, get the data. On the 4&nbsp;km main at +3.0&nbsp;m the laws disagree. Lower the criterion to 0&nbsp;m and the decision still depends on the data. On the 12&nbsp;km main the smallest tested inertia that passes all three laws at +3.0&nbsp;m is the 400&nbsp;kg&middot;m&sup2; flywheel case.</p>

<h2 id="with-vessel">6 &middot; With a vessel: is the instant stop conservative?</h2>
<p>Many analysts model the pump as stopping instantly when sizing a vessel, on the grounds that it is conservative. On the 12&nbsp;km main we sized the vessel gas volume (differential DN400 connection, shell 5.7 times the gas, +3.0&nbsp;m everywhere) for each assumption:</p>
<div class="tbl-wrap"><table>
  <caption>Steady gas volume needed for +3.0&nbsp;m on the 12&nbsp;km main (m&sup3;), bisection to 0.01&nbsp;m&sup3;</caption>
  <thead><tr><th>Pump model</th><th class="num">Constant efficiency (duty)</th><th class="num">Generic radial</th><th class="num">Shut-off floor</th></tr></thead>
  <tbody>
__GASROWS__
  </tbody>
</table></div>
<p>With the generic radial law, real inertia saves at most 3&nbsp;% of gas. Under the two laws in which the slowing pump keeps delivering longer, the estimated set saves 15&nbsp;% and twice the estimate 32&nbsp;%. The instant stop is conservative in every case and costs up to half as much gas again (3.22 against 2.19&nbsp;m&sup3;); on a long main that is a small price for not depending on data you do not have. On short mains, where section 5 showed inertia doing most of the work, the instant stop can oversize a vessel many times over or call for one that is not needed at all, and real data pay for themselves. The same caution applies to the upsurge: the pump's rundown changes when the check valve closes and how fast the reverse flow builds, which is covered in <a href="check-valve-hammer.html">check valve slam</a>.</p>

<h2 id="reverse">7 &middot; Reverse flow, reverse rotation and the check valve</h2>
<p>Once the pump's head falls below the line head, the flow at the pump reverses. With a check valve that closes cleanly, the pump simply runs down. Without one, or with a valve that closes late, water flows back through the pump, stops it, and then drives it backwards as a turbine towards its runaway speed [1][2][7]. That is where the four-quadrant data matter most, and where results become very sensitive to the curve chosen [4]. Three practical points:</p>
<ul class="clean">
  <li><strong>Reverse rotation.</strong> Ask the manufacturer for the runaway speed in reverse at the maximum static head, and whether the pump, motor bearings and coupling may spin backwards. Some motors must not be restarted while turning backwards, which sets an interlock on the restart time.</li>
  <li><strong>Anti-reverse devices.</strong> A ratchet stops reverse rotation and turns the pump into a fixed restriction to reverse flow; the model must then treat the pump as locked, not free-wheeling.</li>
  <li><strong>Check valve timing.</strong> The inertia sets how soon the flow reverses, so it also sets the reverse velocity a slow valve meets. A larger inertia delays reversal and usually softens the slam.</li>
</ul>

<h2 id="worked-example">8 &middot; Worked example: from no data to a defensible pump model</h2>
<h3>Step 1: the duty and power</h3>
<div class="eq">\[ P = \frac{\rho g Q H}{\eta} = \frac{998 \times 9.81 \times 0.70 \times 80}{0.80} = 685\ \text{kW}, \qquad \omega_0 = \frac{2\pi \times 1480}{60} = 155.0\ \text{rad/s} \]</div>
<h3>Step 2: estimate the inertia and set a range</h3>
<p>Correlation: __IM__ + __IP__ = __IT__&nbsp;kg&middot;m&sup2;. With &plusmn;50&nbsp;% the range to test is 22&ndash;66&nbsp;kg&middot;m&sup2;. We ran 25, 44 and 88 to cover it with margin. Stored energy at the estimate: \(\tfrac12 \times 44.0 \times 155.0^2 = 0.53\) MJ; \(\tau\) = 0.77&nbsp;s.</p>
<h3>Step 3: specific speed and characteristic</h3>
<p>\(N_s\) = __NS__ (SI), a radial impeller. In HAMMER we select the closest typical value (25) and repeat the governing run with the mixed-flow curve (94) to bracket the characteristic, as the documentation advises [4].</p>
<h3>Step 4: compare &tau; with 2L/a</h3>
<p>For the 4&nbsp;km main: 0.77/7.62 = 0.10. That is in the zone where the data matter, so the trip has to be run across the whole range of inertia and characteristic, not at one point.</p>
<h3>Step 5: run the bracket and read the decision</h3>
<p>At 25&nbsp;kg&middot;m&sup2; the minimum is &minus;2.6 to +0.9&nbsp;m (fails under every law); at 44, &minus;0.3 to +3.2&nbsp;m (undecided); at 88, +4.4 to +7.5&nbsp;m (passes under every law). The design cannot be fixed on estimates.</p>
<h3>Step 6: decide</h3>
<p>Either protect the main on the conservative side (a small vessel or a flywheel, sized at 25&nbsp;kg&middot;m&sup2; and the shut-off law), or make the pump data a hold point: specify the minimum total inertia the motor and pump must provide, and require the supplier's inertia and complete characteristics before the protection is frozen. On the 4&nbsp;km main a total of 88&nbsp;kg&middot;m&sup2; passes under every law tried, so a specification can simply require it, with a small flywheel if the chosen motor falls short (see <a href="pump-inertia-flywheel-surge.html">Pump Inertia and the Flywheel</a>).</p>

<h2 id="data-request">9 &middot; What to demand in the pump specification</h2>
<p>Most surge studies stall at detailed design because the pump package arrives without the transient data. We write these into the pump and motor specification, with the surge study named as their user:</p>
<ul class="clean">
  <li><strong>Moment of inertia</strong> of the motor rotor, the pump rotor with entrained water, the coupling and any flywheel, each stated as \(I\) in kg&middot;m&sup2; (state explicitly if GD&sup2; or WR&sup2; is given).</li>
  <li><strong>Complete performance curves</strong> from shut-off to run-out at rated speed: head, power, efficiency and NPSH required, with the duty point and best efficiency point marked.</li>
  <li><strong>Specific speed and impeller type</strong>, and the complete (four-quadrant) characteristics in Suter or equivalent form where the manufacturer has them for the impeller design or a geometrically similar one.</li>
  <li><strong>Reverse running</strong>: whether reverse rotation is permitted, the runaway speed at the maximum reverse head, and the maximum time at runaway.</li>
  <li><strong>Motor starting data</strong>: the maximum load inertia the motor can accelerate, the starting time with the specified starter, and permitted starts per hour.</li>
  <li><strong>Check valve</strong> type and dynamic characteristic (reverse velocity against deceleration), from the valve manufacturer.</li>
  <li><strong>A minimum total inertia</strong>, where the surge study shows the line depends on it, as a performance requirement with a test or certificate.</li>
</ul>

<h2 id="hammer-setup">10 &middot; Setting it up in Bentley HAMMER</h2>
<p>Field names differ slightly between versions; these follow the current documentation [3][4][10].</p>
<ol>
  <li><strong>Enter the pump curve and efficiency</strong> for steady state, and confirm the duty point and power in the steady run.</li>
  <li><strong>Open the pump's transient properties</strong> and enter the <strong>Speed (Full)</strong> in rpm.</li>
  <li><strong>Inertia (Pump and Motor):</strong> enter the vendor value if you have it. If not, use the <strong>Pump and Motor Inertia Calculator</strong> with the brake power at best efficiency and the speed, and record the result as an assumption. Check whether a vendor value is \(I\), GD&sup2; or WR&sup2; before typing it in.</li>
  <li><strong>Specific Speed:</strong> calculate it per stage at best efficiency and select the closest available value. Note it in the assumptions register.</li>
  <li><strong>Pump trip:</strong> set the pump to shut down at the start of the run (all pumps together for the power-failure case), and model the check valve as described in the check valve article.</li>
  <li><strong>Make the bracket explicit:</strong> create alternatives for the low, estimated and high inertia and for the neighbouring specific-speed curve, and a scenario for each combination, changing nothing else.</li>
  <li><strong>Compare the envelopes</strong> along the whole line, and report the range. If the decision changes inside the range, say so and make the pump data a hold point.</li>
  <li><strong>Replace estimates with vendor data</strong> as soon as they arrive, rerun, and keep both runs in the report.</li>
</ol>

<h2 id="checklist">11 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Inertia source recorded</strong>: vendor (with the document) or correlation (with the inputs).</li>
  <li><strong>Units checked</strong>: \(I\), GD&sup2; or WR&sup2;, wet or dry, coupling included.</li>
  <li><strong>Range tested</strong> around any estimate, at least &plusmn;50&nbsp;%.</li>
  <li><strong>Specific speed calculated per stage</strong>, closest curve used and a neighbouring curve run as a bracket.</li>
  <li><strong>&tau;/(2L/a) worked out</strong> to judge whether the pump data matter.</li>
  <li><strong>Instant stop compared</strong> with the real rundown, and the conservative choice explained.</li>
  <li><strong>Reverse flow and rotation</strong> considered, with the check valve modelled realistically.</li>
  <li><strong>Pump data written into the specification</strong> as a hold point where the decision depends on it.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><strong>Pump data for a pump trip: inertia, specific speed and four-quadrant curves</strong></li>
    <li><a href="surge-envelope-pipe-pressure-limits.html">Reading the surge envelope against the pipe's real limits</a></li>
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
const VAP=-9.8, PMIN=3.0, G=9.81;
const Imot=(P,N)=>118*Math.pow(P/N,1.48), Ipmp=(P,N)=>1.5e7*Math.pow(P/(N*N*N),0.9556);
const w0=N=>2*Math.PI*N/60;
/* ---------- CHART 1 : inertia estimator ---------- */
const sP=document.getElementById('sP'), sN=document.getElementById('sN'), sBand=document.getElementById('sBand');
const PS=[];for(let k=0;k<=80;k++)PS.push(Math.pow(10,1+k*(Math.log10(3000)-1)/80));
const SPD=[[2960,'#c0392b'],[1480,'#1b4f72'],[990,'#b9770e'],[740,'#1e8449'],[1780,'#6b4f9e']];
const inChart=new Chart(document.getElementById('inChart'),{
  data:{datasets:SPD.map(([N,c])=>({type:'line',label:fmt0(N)+' rpm',data:PS.map(P=>({x:P,y:Imot(P,N)+Ipmp(P,N)})),borderColor:c,backgroundColor:c,borderWidth:1.8,pointRadius:0,order:3}))
    .concat([{type:'scatter',label:'Your set',data:[],backgroundColor:'#111',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1},
             {type:'line',label:'Range to test',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:3,pointRadius:3,order:2}])},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'logarithmic',min:10,max:3000,title:{display:true,text:'Shaft power at best efficiency (kW, log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[10,20,50,100,200,500,1000,2000,3000].includes(+v.toPrecision(3))?fmt0(v):''}},
            y:{type:'logarithmic',min:0.01,max:2000,title:{display:true,text:'Total inertia I (kg·m², log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[0.01,0.1,1,10,100,1000].includes(+v.toPrecision(3))?String(+v.toPrecision(3)):''}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${c.parsed.y<10?fmt2(c.parsed.y):fmt1(c.parsed.y)} kg·m² at ${fmt0(c.parsed.x)} kW`}}}}
});
function updIn(){
  const P=+sP.value, N=+sN.value, b=+sBand.value/100;
  document.getElementById('vP').textContent=fmt0(P)+' kW';
  document.getElementById('vBand').textContent='±'+fmt0(b*100)+' %';
  const im=Imot(P,N), ip=Ipmp(P,N), it=im+ip, w=w0(N), tau=0.5*it*w*w/(P*1000);
  inChart.data.datasets[5].data=[{x:P,y:it}];
  inChart.data.datasets[6].data=[{x:P,y:it*(1-b)},{x:P,y:it*(1+b)}];
  inChart.update('none');
  const f=v=>v<10?fmt2(v):fmt1(v);
  document.getElementById('rIm').innerHTML=f(im)+' <small>kg·m²</small>';
  document.getElementById('rIp').innerHTML=f(ip)+' <small>kg·m²</small>';
  document.getElementById('rIt').innerHTML=f(it)+' <small>kg·m²</small>';
  document.getElementById('rGD').innerHTML=f(4*it)+' <small>kg·m²</small>';
  document.getElementById('rWR').innerHTML=fmt0(it/0.0421)+' <small>lb·ft²</small>';
  document.getElementById('rTau').innerHTML=fmt2(tau)+' <small>s</small>';
  document.getElementById('rRange').innerHTML=f(it*(1-b))+'–'+f(it*(1+b))+' <small>kg·m²</small>';
}
[sP,sN,sBand].forEach(s=>s.addEventListener('input',updIn));updIn();

/* ---------- CHART 2 : specific speed ---------- */
const sQ=document.getElementById('sQ'), sH=document.getElementById('sH'), sNs=document.getElementById('sNs'), sSt=document.getElementById('sSt');
const HV=[25,94,145];
const nsChart=new Chart(document.getElementById('nsChart'),{
  data:{datasets:[
    {type:'scatter',label:'HAMMER typical values',data:HV.map(v=>({x:v,y:1})),backgroundColor:'#7f8c8d',borderColor:'#fff',borderWidth:2,pointRadius:8,pointStyle:'rectRot',order:2},
    {type:'scatter',label:'Your pump',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:9,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'logarithmic',min:5,max:600,title:{display:true,text:'Specific speed Ns (SI: rpm, m³/s, m), log scale',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[5,10,20,25,50,94,145,200,500].includes(+v.toPrecision(3))?String(+v.toPrecision(3)):''}},
            y:{min:0,max:2,display:false}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: Ns ${fmt1(c.parsed.x)}`}},
      annotation:{annotations:{
        rad:{type:'box',xMin:5,xMax:40,yMin:0,yMax:2,backgroundColor:'rgba(27,79,114,0.08)',borderWidth:0,label:{display:true,content:'radial',position:{x:'center',y:'start'},font:LBL,color:'#1b4f72'}},
        mix:{type:'box',xMin:40,xMax:160,yMin:0,yMax:2,backgroundColor:'rgba(185,119,14,0.08)',borderWidth:0,label:{display:true,content:'mixed flow',position:{x:'center',y:'start'},font:LBL,color:'#b9770e'}},
        axi:{type:'box',xMin:160,xMax:600,yMin:0,yMax:2,backgroundColor:'rgba(30,132,73,0.08)',borderWidth:0,label:{display:true,content:'axial',position:{x:'center',y:'start'},font:LBL,color:'#1e8449'}}
      }}}}
});
function updNs(){
  const Q=+sQ.value, H=+sH.value, N=+sNs.value, st=+sSt.value, h=H/st;
  document.getElementById('vQ').textContent=fmt2(Q)+' m³/s';
  document.getElementById('vH').textContent=fmt0(H)+' m';
  document.getElementById('vNs').textContent=fmt0(N)+' rpm';
  document.getElementById('vSt').textContent=st;
  const ns=N*Math.sqrt(Q)/Math.pow(h,0.75), om=w0(N)*Math.sqrt(Q)/Math.pow(G*h,0.75);
  nsChart.data.datasets[1].data=[{x:Math.min(600,Math.max(5,ns)),y:1}];nsChart.update('none');
  let ci=0; HV.forEach((v,i)=>{if(Math.abs(v-ns)<Math.abs(HV[ci]-ns))ci=i;});
  const br=ns<HV[0]?[HV[0]]:ns>HV[2]?[HV[2]]:HV.filter((v,i)=>i<2?(ns>=HV[i]&&ns<=HV[i+1])||(i>0&&ns>=HV[i-1]&&ns<=v):false);
  let lo=null,hi=null; for(let i=0;i<2;i++){ if(ns>=HV[i]&&ns<=HV[i+1]){lo=HV[i];hi=HV[i+1];} }
  document.getElementById('rNs').innerHTML=fmt1(ns);
  document.getElementById('rNsUS').innerHTML=fmt0(ns*51.64);
  document.getElementById('rOm').innerHTML=fmt2(om);
  document.getElementById('rType').innerHTML=ns<40?'radial':(ns<160?'mixed flow':'axial');
  document.getElementById('rClose').innerHTML=String(HV[ci]);
  document.getElementById('rBr').innerHTML=lo!==null?(lo+' and '+hi):(ns<HV[0]?'25 only: below the library':'145 only: above the library');
}
[sQ,sH,sNs,sSt].forEach(s=>s.addEventListener('input',updNs));updNs();

/* ---------- CHART 3 : trip traces ---------- */
const sMain=document.getElementById('sMain'), sI=document.getElementById('sI'), sLaw=document.getElementById('sLaw');
const tripChart=new Chart(document.getElementById('tripChart'),{
  data:{datasets:[
    {type:'line',label:'Head at the pump (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,yAxisID:'y',order:1},
    {type:'line',label:'Speed ratio (right)',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.2,pointRadius:0,yAxisID:'y1',order:2},
    {type:'line',label:'Head, instant stop',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.4,borderDash:[5,4],pointRadius:0,yAxisID:'y',order:3}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:-20,max:160,position:'left',title:{display:true,text:'Pressure head at the pump (m)',font:TTL},...AX},
            y1:{type:'linear',min:0,max:1,position:'right',title:{display:true,text:'Speed ratio n/n₀',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11},stepSize:0.2}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:6}},
      tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`${c.dataset.label}: ${fmt2(c.parsed.y)}`:`${c.dataset.label}: ${fmt1(c.parsed.y)} m`}},
      annotation:{annotations:{
        pmin:{type:'line',yScaleID:'y',yMin:PMIN,yMax:PMIN,borderColor:'#1e8449',borderWidth:1.5,borderDash:[6,4],label:{display:true,content:'+3.0 m',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}},
        vap:{type:'line',yScaleID:'y',yMin:VAP,yMax:VAP,borderColor:'#c0392b',borderWidth:1.5,borderDash:[6,4],label:{display:true,content:'vapour −9.8 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(192,57,43,0.85)'}},
        tla:{type:'line',xScaleID:'x',xMin:0,xMax:0,borderColor:'#6b4f9e',borderWidth:1.5,borderDash:[4,4],label:{display:true,content:'2L/a',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}
      }}}}
});
const isVap=c=>c.line_min<=VAP+0.05;
const verdict=(v,crit)=>v<=VAP+0.05?'<span class="badge bad">vapour</span>':(v<crit?'<span class="badge warn">below '+sgn(crit,1)+' m</span>':'<span class="badge good">meets '+sgn(crit,1)+' m</span>');
const tauOf=I=>0.5*I*w0(1480)*w0(1480)/685e3;
function updTrip(){
  const m=D.mains[+sMain.value], I=+sI.value, law=sLaw.value;
  const c=m.cases.find(q=>q.I===I&&q.law===law), c0=m.cases.find(q=>q.I===0);
  tripChart.data.datasets[0].data=c.t.map((t,k)=>({x:t,y:c.H[k]}));
  tripChart.data.datasets[1].data=c.t.map((t,k)=>({x:t,y:c.w[k]}));
  tripChart.data.datasets[2].data=c0.t.map((t,k)=>({x:t,y:c0.H[k]}));
  tripChart.options.scales.x.max=m.T;
  const a=tripChart.options.plugins.annotation.annotations.tla; a.xMin=m.tla; a.xMax=m.tla; a.label.content='2L/a = '+fmt1(m.tla)+' s';
  tripChart.update('none');
  document.getElementById('rRat').innerHTML=fmt2(tauOf(I)/m.tla);
  document.getElementById('rLmin').innerHTML=sgn(c.line_min,2)+' <small>m</small>';
  document.getElementById('rWhere').innerHTML=isVap(c)?'<small>vapour on the line</small>':(c.at_min===0?'at the pump':'at '+fmt1(c.at_min/1000)+' km');
  document.getElementById('rPmin').innerHTML=sgn(c.pump_min,2)+' <small>m</small>';
  document.getElementById('rLmax').innerHTML=isVap(c)?'<small>not quoted (cavitating)</small>':fmt1(c.line_max)+' <small>m</small>';
  document.getElementById('rVer').innerHTML=verdict(c.line_min,PMIN);
}
[sMain,sI,sLaw].forEach(s=>s.addEventListener('input',updTrip));updTrip();

/* ---------- CHART 4 : minimum against inertia ---------- */
const sMain2=document.getElementById('sMain2'), sCrit=document.getElementById('sCrit'), sBand2=document.getElementById('sBand2');
const IS=[25,44,88,176,400], LAWS=[['radial','Generic radial','#1b4f72'],['duty','Constant efficiency','#b9770e'],['shutoff','Shut-off floor','#6b4f9e']];
const sensChart=new Chart(document.getElementById('sensChart'),{
  data:{datasets:LAWS.map(([k,l,c])=>({type:'line',label:l,data:[],borderColor:c,backgroundColor:c,borderWidth:2,pointRadius:4,order:2}))
    .concat([{type:'line',label:'Worst of the three',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:1}])},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'logarithmic',min:18,max:500,title:{display:true,text:'Total inertia on the shaft (kg·m², log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[25,44,88,176,400].includes(Math.round(v))?String(Math.round(v)):''},
               afterBuildTicks:ax=>{ax.ticks=[25,44,88,176,400].map(v=>({value:v}));}},
            y:{type:'linear',min:-12,max:60,title:{display:true,text:'Lowest head on the line (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt2(c.parsed.y)} m at ${Math.round(c.parsed.x)} kg·m²`}},
      annotation:{annotations:{
        band:{type:'box',xMin:22,xMax:66,backgroundColor:'rgba(127,140,141,0.15)',borderWidth:0},
        est:{type:'line',xMin:44,xMax:44,borderColor:'#7f8c8d',borderWidth:1.2,borderDash:[3,3],label:{display:true,content:'estimate 44',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(127,140,141,0.9)'}},
        crit:{type:'line',yMin:PMIN,yMax:PMIN,borderColor:'#1e8449',borderWidth:1.5,borderDash:[6,4],label:{display:true,content:'+3.0 m',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}},
        vap:{type:'line',yMin:VAP,yMax:VAP,borderColor:'#c0392b',borderWidth:1.2,borderDash:[6,4],label:{display:true,content:'vapour',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(192,57,43,0.85)'}}
      }}}}
});
function updSens(){
  const m=D.mains[+sMain2.value], crit=+sCrit.value, b=+sBand2.value/100;
  document.getElementById('vCrit').textContent=sgn(crit,1)+' m';
  document.getElementById('vBand2').textContent='±'+fmt0(b*100)+' %';
  const val=(I,law)=>m.cases.find(q=>q.I===I&&q.law===law).line_min;
  LAWS.forEach(([k],j)=>{sensChart.data.datasets[j].data=IS.map(I=>({x:I,y:val(I,k)}));});
  sensChart.data.datasets[3].data=IS.map(I=>({x:I,y:Math.min(...LAWS.map(([k])=>val(I,k)))}));
  const A=sensChart.options.plugins.annotation.annotations;
  A.band.xMin=44*(1-b); A.band.xMax=44*(1+b); A.crit.yMin=crit; A.crit.yMax=crit; A.crit.label.content=sgn(crit,1)+' m';
  sensChart.update('none');
  const v44=LAWS.map(([k])=>val(44,k)), wo=Math.min(...v44), be=Math.max(...v44);
  const tag=v=>v<=VAP+0.05?' <small>(vapour)</small>':' <small>m</small>';
  document.getElementById('rW44').innerHTML=sgn(wo,2)+tag(wo);
  document.getElementById('rB44').innerHTML=sgn(be,2)+tag(be);
  document.getElementById('rDec').innerHTML=wo>=crit?'<span class="badge good">estimate is enough</span>':(be<crit?'<span class="badge bad">protect whatever the data</span>':'<span class="badge warn">get vendor data</span>');
  const ok=IS.filter(I=>LAWS.every(([k])=>val(I,k)>=crit));
  document.getElementById('rSmall').innerHTML=ok.length?fmt0(ok[0])+' <small>kg·m²</small>':'<small>none tested</small>';
}
[sMain2,sCrit,sBand2].forEach(s=>s.addEventListener('input',updSens));updSens();
window.addEventListener('load',function(){try{[inChart,nsChart,tripChart,sensChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: pump boundary conditions with rotor inertia, complete pump characteristics in Suter form, and inertia correlations for motors and pumps.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014: pump rundown equations, four-quadrant characteristics, reverse flow and reverse rotation.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation, &ldquo;Pump and Motor Inertia Calculator&rdquo; and pump transient properties: inertia from brake power at best efficiency and speed, using an empirical relation by Thorley.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation, &ldquo;Specific Speed&rdquo;: definition, the typical values 25, 94 and 145 (SI) with built-in curves, selecting the closest value, bracketing, and the effect of a check valve.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the 12&nbsp;km DN800 reference main, its pump station and the verified MOC solver.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: pump trip and rundown, and estimating pump and motor inertia from power and speed.</li>
  <li>Larock, B.E., Jeppson, R.W. &amp; Watters, G.Z. <em>Hydraulics of Pipeline Systems</em>. CRC Press, 2000: homologous relations and transient pump boundary conditions.</li>
  <li>Stepanoff, A.J. <em>Centrifugal and Axial Flow Pumps</em>, 2nd ed. Wiley, 1957: specific speed, impeller types and complete pump characteristics.</li>
  <li>Thorley, A.R.D. &amp; Chaudry, A. &ldquo;Pump characteristics for transient flow analysis&rdquo;: cited in the HAMMER documentation as the source of further predefined four-quadrant curves.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: data needs and pump modelling in transient studies.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #HydraulicTransients #PumpTrip #PumpInertia #MomentOfInertia #GD2 #WR2 #SpecificSpeed #FourQuadrantCurves #SuterCurves #CompletePumpCharacteristics #ReverseRotation #CheckValve #BentleyHAMMER #OpenFlowsHAMMER #PumpSpecification #PumpStation #TransmissionMain #DuctileIron #TransientAnalysis #HydraulicDesign #WaterEngineering</div>
"""

import json, os, math
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'analyst.json')))['s09']
DATA = {'mains': [dict(L=m['L'], T=m['T'], tla=m['tla'], cases=[{k: c[k] for k in ('I', 'law', 'line_min', 'at_min', 'pump_min', 'line_max', 't', 'H', 'w')} for c in m['cases']]) for m in _A['mains']]}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))
_IM = 118*(685/1480)**1.48; _IP = 1.5e7*(685/1480**3)**0.9556
_NS = 1480*math.sqrt(0.70)/80**0.75
def _sg(v): return ('+' if v >= 0 else '&minus;') + '%.1f' % abs(v)
def _rng(m, I):
    v = [c['line_min'] for c in m['cases'] if c['I'] == I]
    lo, hi = min(v), max(v)
    if hi <= -9.79: return 'vapour'
    if lo <= -9.79: return 'vapour to ' + _sg(hi)
    return _sg(lo) + ' to ' + _sg(hi)
_tau = 0.5*44.0*(2*math.pi*1480/60)**2/685e3
TABROWS = '\n'.join('    <tr><td>%s&nbsp;km</td><td class="num">%.1f</td><td class="num">%.2f</td><td class="num">%s</td><td class="num">%s</td><td class="num">%s</td><td class="num">%s</td><td class="num">%s</td></tr>' % (
    '{:,.0f}'.format(m['L']/1000), m['tla'], _tau/m['tla'], 'vapour', _rng(m, 25), _rng(m, 44), _rng(m, 88), _rng(m, 176)) for m in _A['mains'])
def _g(I, law): return next(x['gas'] for x in _A['vessel_gas'] if x['I'] == I and x['law'] == law)
GASROWS = '\n'.join(['    <tr><td>Instant stop</td><td class="num" colspan="3">%.2f</td></tr>' % _g(0, 'instant')] +
    ['    <tr><td>%s</td><td class="num">%.2f</td><td class="num">%.2f</td><td class="num">%.2f</td></tr>' % (lab, _g(I, 'duty'), _g(I, 'radial'), _g(I, 'shutoff'))
     for I, lab in ((25, 'I = 25&nbsp;kg&middot;m&sup2;'), (44, 'I = 44&nbsp;kg&middot;m&sup2; (estimate)'), (88, 'I = 88&nbsp;kg&middot;m&sup2;'))])
for k, v in {'__IM__': '%.1f' % _IM, '__IP__': '%.1f' % _IP, '__IT__': '%.1f' % (_IM + _IP), '__NS__': '%.0f' % _NS,
             '__NSUS__': '{:,.0f}'.format(round(_NS*51.64, -1)), '__TABROWS__': TABROWS, '__GASROWS__': GASROWS}.items():
    BODY = BODY.replace(k, v)

SPEC = dict(
    slug='pump-trip-data-inertia-specific-speed', cat='surge', mins=20,
    date_iso='2026-11-19', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Pump Data for a Pump Trip: Inertia, Specific Speed and Four-Quadrant Curves When the Vendor Gives You Nothing',
    reg_title='Pump Data for a Pump Trip: Inertia, Specific Speed and Four-Quadrant Curves',
    reg_tag='Surge Analysis · Pump Data · Inertia',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Pump Data &middot; Inertia',
    desc='How to model a pump trip without vendor data: inertia from the Thorley correlations behind the HAMMER calculator, units, specific speed and the four-quadrant curve, when the estimate matters (tau against 2L/a on four mains), vessel sizing with and without inertia, reverse rotation, and what to demand in the pump specification, with four interactive charts.',
    og_desc='The HAMMER inertia calculator gives 44.0 kg·m² for a 685 kW, 1,480 rpm set. On a 4 km main that estimate puts the lowest head between −0.3 and +3.2 m depending on the torque characteristic, either side of the criterion; on a 12 km main it changes nothing.',
    ld_desc='Pump data for surge analysis: estimating pump and motor inertia, specific speed and four-quadrant characteristics, testing the sensitivity on four main lengths, vessel sizing with and without inertia, and the pump data to specify, with the Bentley HAMMER settings.',
    img_alt='Cutaway of a motor and centrifugal pump set on a baseplate, with the rotor, impeller and coupling highlighted, beside a four-quadrant pump characteristic chart and a rundown curve of speed against time',
    en_tag='Surge &amp; Transient Analysis &middot; Pump Data',
    en_title='Pump Data for a Pump Trip: Inertia, Specific Speed and Four-Quadrant Curves',
    en_excerpt='The HAMMER inertia calculator gives <strong>44.0 kg·m²</strong> for our 685 kW, 1,480 rpm set. On a 4 km main that estimate puts the lowest head between <strong>−0.3 and +3.2 m</strong> depending on the torque characteristic: the design decision rests on data nobody has yet. On the 12 km reference main the same uncertainty changes nothing. How to estimate inertia and specific speed, how to tell from τ against 2L/a whether the estimate matters, whether the instant stop is conservative, and what to write into the pump specification, with four interactive charts.',
    en_search='pump trip data pump inertia motor inertia moment of inertia GD2 WR2 WK2 Thorley correlation pump and motor inertia calculator specific speed four-quadrant characteristics Suter curves complete pump characteristics reverse rotation runaway speed anti-reverse ratchet check valve instant stop conservative vessel sizing tau 2L/a rundown time constant pump specification vendor data hold point surge analysis water hammer Bentley HAMMER OpenFlows transient analysis pump station',
    ar_title='بيانات المضخة لتحليل توقفها: القصور الذاتي والسرعة النوعية والمنحنيات رباعية الأرباع',
    ar_excerpt='تعطي حاسبة القصور الذاتي في برنامج HAMMER قيمة <strong>٤٤٫٠ كغ·م²</strong> لمجموعة قدرتها ٦٨٥ كيلوواط وسرعتها ١٤٨٠ دورة في الدقيقة. وعلى خط طوله ٤ كم يجعل هذا التقدير أدنى ضغط بين <strong>−٠٫٣ و+٣٫٢ م</strong> بحسب منحنى العزم، أي على جانبي المعيار، بينما لا يغير شيئاً على الخط المرجعي بطول ١٢ كم. كيف نقدّر القصور الذاتي والسرعة النوعية، ومتى يكون التقدير مؤثراً، وما البيانات التي يجب طلبها من المورد، مع أربعة رسوم تفاعلية.',
    ar_search='بيانات المضخة توقف المضخة القصور الذاتي عزم القصور الذاتي للمحرك GD2 السرعة النوعية المنحنيات رباعية الأرباع منحنيات سوتر الدوران العكسي سرعة الجموح صمام عدم الرجوع خزان الحماية المطرقة المائية الطرق المائي تحليل الموجات العابرة مواصفات المضخة بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
