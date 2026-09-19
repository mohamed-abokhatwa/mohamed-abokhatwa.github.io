# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Stop the pumps instantly on a 12&nbsp;km DN800 transmission main with no protection and the whole line reaches vapour; when the cavities collapse the head reaches <strong>165&ndash;190&nbsp;m</strong> against a 136&nbsp;m pipe class. Three remedies were modelled on the same pipe. A 20&nbsp;m&sup3; surge vessel holds it between <strong>+4.3&nbsp;m and 119.2&nbsp;m</strong>; a 400&nbsp;kg&middot;m&sup2; flywheel at <strong>+9.3&nbsp;m with nothing above the steady 85.0&nbsp;m</strong>, if the motor can start it. A relief valve set at 95&nbsp;m holds the pump end at about 96&nbsp;m but leaves the line at vapour and a maximum of <strong>127&ndash;143&nbsp;m</strong>, either side of the limit depending on the cavity model. The fourth device, a one-way tank, earns its place only where the profile has a knee. There is no best surge device &mdash; only the right one for a line, a load case and a site.</p>

<h2 id="load-case">1 &middot; Start from the load case, not the device</h2>
<p><em>Vessel or relief valve?</em> is the wrong first question. A surge device protects one side of the pressure wave, at one place, against one family of events, so the design starts with the load cases. In our practice, for a pumped transmission main they are:</p>
<ul class="clean">
  <li><strong>Power failure at the highest flow</strong>, all duty pumps tripping at once with nothing controlling the rundown. On most pumped mains this case sizes the protection, and it is the case used here.</li>
  <li><strong>A single pump trip and pump starts</strong>, including a restart while the column is still moving.</li>
  <li><strong>Valve closures</strong> &mdash; see <a href="water-hammer-control-valve.html">control valve water hammer</a> and <a href="control-valve-transients-hammer.html">control valve transients in HAMMER</a> &mdash; and <strong>check valve closure</strong> against reverse flow (<a href="check-valve-hammer.html">check valves and water hammer</a>).</li>
</ul>
<p>Each case produces an envelope: the highest and lowest head reached at every point on the line. The limits are fixed before any device is chosen &mdash; here +3.0&nbsp;m everywhere and the 136&nbsp;m allowable of the PN16 class, within the design-pressure framework of EN&nbsp;805 [11]. <a href="surge-scenarios-pump-stations.html">Surge scenarios in pumping stations</a> shows why the power failure usually governs, and the classical texts treat the pump trip as the defining transient of a pumping main [1][3].</p>

<h2 id="reference">2 &middot; The reference pipeline, unprotected</h2>
<p>The series uses one pipeline so that devices compare on equal terms: 12&nbsp;km of DN800 ductile iron K9 to ISO&nbsp;2531 [12], laid flat, carrying 2,520&nbsp;m&sup3;/h (0.70&nbsp;m&sup3;/s, 1.39&nbsp;m/s). With a wave speed of 1,050&nbsp;m/s the pipe period 2L/a is 22.9&nbsp;s and the Joukowsky head is 149.1&nbsp;m. The steady grade line is 85.0&nbsp;m at the pump and 44.8&nbsp;m at the delivery reservoir; any vessel gas follows a polytropic exponent of 1.2.</p>
<p>The unprotected run stops the pump instantly and shuts its check valve at once &mdash; the bounding case of a set with very little inertia. The head at the pump tries to fall by 149.1&nbsp;m, but only 94.8&nbsp;m separate the steady head from vapour. The column separates at the pump and the low-pressure wave runs the full length: <strong>the whole 12&nbsp;km reaches vapour</strong>. When the reflection returns and the cavities close, the head is thrown to <strong>165&ndash;190&nbsp;m</strong>, above 136&nbsp;m over 12.0&nbsp;km of line in one cavity model and 11.0&nbsp;km in the other.</p>
<p>A real set runs down for a moment first. In the simplified rundown model of the flywheel article, with 25&nbsp;kg&middot;m&sup2; assumed for this 685&nbsp;kW set, the pump end holds +2.5&nbsp;m but the line still reaches vapour from about 7.4 to 11.3&nbsp;km; no maximum is quoted, because that run was not repeated with the gas cavity model. That model lets a slowing pump pass some water from its suction, so it does not shrink exactly to the instant stop. Either way the bare line fails.</p>
<h3>How these numbers were produced</h3>
<p>Every transient figure in the series comes from a method-of-characteristics model with a vapour cavity model, cross-checked with a gas cavity model and an independent second code, on 120 reaches over 150&nbsp;s [1][2]. The pump boundary differs by option: the unprotected, vessel and relief-valve runs stop the pump instantly behind an ideal check valve; the flywheel runs model the rundown, because the inertia is the device. Results without cavitation are quoted to 0.1&nbsp;m. A maximum that follows a cavity collapse is quoted as a range across the two cavity models: the spike depends on how the cavity is represented, both textbook models are legitimate [9], and on the collapse peaks of this series the gas cavity model puts them between 18&nbsp;% lower and 10&nbsp;% higher than the vapour cavity model. These are not Bentley HAMMER results. They are a consistent basis for comparing devices; a project must still be analysed on its own profile in HAMMER or an equivalent tool.</p>
<div class="callout warn">
  <span class="lbl">Do not design on a collapse peak</span>
  If the answer to <em>does the pipe survive?</em> depends on which cavity model you believe, there is no design yet. Stop the column separating &mdash; protect the downsurge &mdash; and the collapse peaks never form.
</div>

<h2 id="four-options">3 &middot; Three devices, one pipeline</h2>
<p>Three devices were modelled for the same power failure, each sized or set the way a designer would specify it; the detailed articles of the series carry the derivations.</p>
<div class="tbl-wrap"><table>
  <caption>All pumps trip on the reference main, 150 s. Unprotected, vessel and relief valve: instant pump stop behind an ideal check valve; flywheel: rundown model. Minimum and maximum anywhere on the 12 km; collapse-governed maxima as a range across the two cavity models.</caption>
  <thead><tr><th>Option</th><th class="num">Line min.</th><th class="num">Line max.</th><th>+3.0 m / 136 m</th></tr></thead>
  <tbody>
    <tr><td>No protection</td><td class="num">&minus;9.8 m</td><td class="num">165&ndash;190 m</td><td>Fails both</td></tr>
    <tr><td>Air-over-water vessel: 20 m&sup3; shell, 3.5 m&sup3; gas, differential DN400</td><td class="num">+4.3 m</td><td class="num">119.2 m</td><td>Passes both</td></tr>
    <tr><td>Flywheel: 400 kg&middot;m&sup2; total</td><td class="num">+9.3 m</td><td class="num">85.0 m</td><td>Passes both</td></tr>
    <tr><td>Relief valve: DN250, set 95 m</td><td class="num">&minus;9.8 m</td><td class="num">127&ndash;143 m</td><td>Fails +3.0 m; 136 m depends on the cavity model</td></tr>
  </tbody>
</table></div>
<h3>The vessel</h3>
<p>The vessel is a source of water at the pump. Gas at 9.35&nbsp;bar abs pushes water into the line the instant the pump stops, so the column slows over tens of seconds instead of one. The 3.5&nbsp;m&sup3; of gas expands to 16.17&nbsp;m&sup3;, leaving 3.83&nbsp;m&sup3; of water in the shell, and the lowest head, +4.3&nbsp;m, is 4.3&nbsp;km out. On the return, the high-loss direction of the <a href="surge-vessel-differential-orifice.html">differential connection</a> (loss coefficient 2 out, 10 in) trims the maximum from 127.5&nbsp;m with a free connection to 119.2&nbsp;m, with the minimum almost unchanged (+4.5&nbsp;m free, +4.3&nbsp;m differential). The bare duty with a free DN400 connection is 3.08&nbsp;m&sup3; of gas expanding to 15.30&nbsp;m&sup3; in a 19.1&nbsp;m&sup3; shell; the method is in <a href="surge-vessel.html">sizing the hydropneumatic surge vessel</a>.</p>
<h3>The flywheel</h3>
<p>The flywheel keeps the pump itself delivering. The set's own inertia, taken as 25&nbsp;kg&middot;m&sup2; for a 685&nbsp;kW four-pole machine at 1,480&nbsp;rpm, is not enough: the line still reaches vapour between about 7.4 and 11.3&nbsp;km. Sixteen times that &mdash; 400&nbsp;kg&middot;m&sup2;, 4.80&nbsp;MJ at speed &mdash; holds +9.3&nbsp;m at 3.0&nbsp;km with nothing above the steady 85.0&nbsp;m, because no cavity forms to collapse. Other plausible pump torque laws move the minimum between about +7 and +9&nbsp;m, still a pass. The price is a start of about 28&nbsp;s with half the rated 4,420&nbsp;N&middot;m available (<a href="pump-inertia-flywheel-surge.html">pump inertia and the flywheel</a>).</p>
<h3>The relief valve</h3>
<p>The relief valve caps the head where it stands. Modelled as an idealised spring valve with no opening delay, it keeps the pump end within about a metre of 95&nbsp;m while discharging up to 0.416&nbsp;m&sup3;/s, 59&nbsp;% of the pumped flow &mdash; and a 95&nbsp;m set is only 10&nbsp;m above the steady head, so nuisance opening is a real risk. But a trip starts with low pressure, and the valve only opens on high. It cannot stop the line reaching vapour, and at this setting the collapse peaks form 11&ndash;12&nbsp;km out: <strong>127&ndash;143&nbsp;m</strong>, above 136&nbsp;m over 1.6&nbsp;km in the vapour cavity model and nowhere in the gas cavity model. Lowering the set point from 120 to 95&nbsp;m trims that far-field peak from 140&ndash;155&nbsp;m to 127&ndash;143&nbsp;m, but no setting tried brings it below 136&nbsp;m in both cavity models, and valve size changes nothing out on the line (<a href="surge-relief-valve-sizing.html">what a valve at the pump can protect</a>).</p>

<h2 id="int-options">4 &middot; Interactive: four options on one pipeline</h2>
<p>Each bar spans the lowest minimum to the highest maximum on the line. Where the maximum follows a cavity collapse, the paler cap is the spread between the two cavity models.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Line minimum and maximum after a pump trip, four options</div>
    <div class="fsub">Method-of-characteristics results on the reference main, 150 s; instant pump stop except the flywheel, which runs down. Solid bar: lowest minimum to highest maximum, taking the lower cavity model where they differ. Pale cap: collapse-peak range across the vapour and gas cavity models. Dashed lines: 136 m allowable, +3.0 m design minimum, vapour.</div>
  </div>
  <div class="chart-box"><canvas id="optChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Option <span id="vOpt">No protection</span></label>
      <select id="sOpt">
        <option value="0" selected>No protection</option>
        <option value="1">Surge vessel, 20 m&sup3; shell, 3.5 m&sup3; gas</option>
        <option value="2">Flywheel, 400 kg&middot;m&sup2; total</option>
        <option value="3">Relief valve DN250, set 95 m</option>
      </select>
      <div class="hint">The other options are dimmed.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Line minimum</div><div class="v" id="rOMin">&minus;9.8 <small>m</small></div></div>
    <div class="cell"><div class="k">Line maximum</div><div class="v" id="rOMax">165&ndash;190 <small>m</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;" id="rOVer"></div></div>
    <div class="cell"><div class="k">What it protects</div><div class="v" style="font-size:14px;margin-top:6px;font-weight:600;" id="rOProt">nothing</div></div>
  </div>
</div>
<p class="fig-note">At the default the unprotected line spans <strong>&minus;9.8&nbsp;m to 165&ndash;190&nbsp;m</strong>. The vessel and the flywheel bring the whole bar inside the band between +3.0&nbsp;m and 136&nbsp;m by different routes: the vessel feeds the line and absorbs the return, the flywheel never lets the column stop abruptly. The relief valve lowers the top of the bar but leaves its foot at vapour, and its cap straddles 136&nbsp;m &mdash; a verdict no designer can sign.</p>

<h2 id="int-envelopes">5 &middot; Interactive: where and when each option acts</h2>
<p>A pass or fail hides where and when the limit is approached. Switch between the envelope along the line and the head at the pump against time &mdash; the two views you read in any transient package.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Head envelopes along the line, or head at the pump against time</div>
    <div class="fsub">Pressure head above the pipe. Envelope: maximum and minimum at each of 121 nodes over 150 s; for cavitating options the maximum is drawn for both cavity models with the band between them shaded. Time: pump-end history from the vapour cavity model, sampled from t = 0.1 s, with the unprotected (instant stop) history dashed grey. The pump-end maximum beside the chart is read from the envelope, which also counts the steady head at t = 0.</div>
  </div>
  <div class="chart-box"><canvas id="envChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Option <span id="vOpt2">Relief valve</span></label>
      <select id="sOpt2">
        <option value="0">No protection</option>
        <option value="1">Surge vessel, 20 m&sup3; shell, 3.5 m&sup3; gas</option>
        <option value="2">Flywheel, 400 kg&middot;m&sup2; total</option>
        <option value="3" selected>Relief valve DN250, set 95 m</option>
      </select>
      <div class="hint">The same four cases as above.</div>
    </div>
    <div class="ctrl">
      <label>View <span id="vView">Envelope along the line</span></label>
      <select id="sView">
        <option value="0" selected>Envelope along the line</option>
        <option value="1">Head at the pump against time</option>
      </select>
      <div class="hint">Dashed grey: the steady grade line, or in the time view the unprotected history.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Line minimum</div><div class="v" style="font-size:16px;margin-top:6px;" id="rEMin">&minus;9.8 m</div></div>
    <div class="cell"><div class="k">Line maximum</div><div class="v" style="font-size:16px;margin-top:6px;" id="rEMax">127&ndash;143 m</div></div>
    <div class="cell"><div class="k">Length above 136 m</div><div class="v" style="font-size:16px;margin-top:6px;" id="rELen">1.6 / 0 km</div></div>
    <div class="cell"><div class="k">Pump-end maximum (envelope)</div><div class="v" style="font-size:16px;margin-top:6px;" id="rEPump">about 96 m</div></div>
  </div>
</div>
<p class="fig-note">The default is the relief valve. Its maximum envelope <strong>rises away from the pump and peaks 11&ndash;12&nbsp;km out</strong>, while the minimum lies on vapour for the whole 12.0&nbsp;km. The vessel's minimum dips to +4.3&nbsp;m at 4.3&nbsp;km, the flywheel's to +9.3&nbsp;m at 3.0&nbsp;km. In the time view the vessel's pump-end head bottoms out at +4.9&nbsp;m about 43&nbsp;s after the trip, while the relief valve's sits at vapour for more than 45&nbsp;s, until the columns rejoin and the valve takes the head to its set point.</p>

<h2 id="what-protects">6 &middot; What each option really protects</h2>
<p>Stripped to its physics, every device either <strong>adds water</strong> where the pressure falls, <strong>removes water</strong> where it rises, or <strong>slows the change of flow</strong> that causes both [1][2][3].</p>
<ul class="clean">
  <li><strong>Surge vessel &mdash; both sides.</strong> It adds and removes water at the pump; in our practice it is usually enough on its own on a flat or steadily rising line, though a knee or high point can make it very large. Its duty is robust: from 700 to 1,300&nbsp;m/s the required gas moves only between 3.08 and 3.19&nbsp;m&sup3;, falling to 1.99&nbsp;m&sup3; at 450&nbsp;m/s and to none at 300&nbsp;m/s (<a href="wave-speed-surge-analysis.html">wave speed</a>). The type changes the shell, not the hydraulics: a bladder vessel needs 23.2&ndash;28.4&nbsp;m&sup3; at any pre-charge from atmospheric up to 0.95 of the minimum, against 19.1&nbsp;m&sup3; air-over-water, because its gas is pre-charged below the minimum pressure (<a href="surge-vessel-type-selection.html">vessel types</a>; <a href="pre-charge-pressure.html">pre-charge and gas setting</a>). It is a pressure vessel [14], and a membrane in contact with drinking water needs potable approval [15].</li>
  <li><strong>Flywheel &mdash; both sides, by prevention.</strong> Passive, present whenever the pump turns, no controls. It needs a rundown that is a real fraction of the pipe period; on long lines the inertia outgrows what a motor can start or a shaft and bearings can carry [2][3][5].</li>
  <li><strong>Surge relief valve &mdash; upsurge, at the valve.</strong> It removes water above its set pressure, there and nowhere else. It is the right primary device where the upsurge comes first &mdash; a fast closure at the end of a gravity line &mdash; and a useful second device behind a vessel. Set pressure, overpressure and reseating are defined in ISO&nbsp;4126-1 [13].</li>
  <li><strong>Surge anticipator valve &mdash; upsurge, earlier.</strong> It opens on the initial low pressure, so it is already open when the return arrives and avoids the relief valve's lag &mdash; but it adds no water on the downsurge. It was not modelled in this series.</li>
  <li><strong>One-way surge tank &mdash; downsurge, locally.</strong> It feeds the main when the head at its connection drops below the tank level [4][7]. On a rising-profile variant of the reference main, a vessel alone needed a 104.5&nbsp;m&sup3; shell; with a tank at the knee it needed 37.8&nbsp;m&sup3;, 64&nbsp;% smaller (<a href="one-way-surge-tank-design.html">one-way tanks at the knee</a>). This flat line has no knee or high point, so a tank has nothing to do here and was not modelled on it; and alone, on the knee profile, it made the pump-end collapse worse.</li>
  <li><strong>Air valves &mdash; a complement.</strong> They admit air at a high point to hold the local pressure near atmospheric; the air must then leave without a slam, and the pocket changes the next wave [8][10]. Every main needs them for filling and draining (<a href="air-admission-networks.html">air admission in networks</a>); none should be the primary downsurge device without a model that includes them.</li>
</ul>

<h2 id="screening">7 &middot; Screening before modelling</h2>
<p>Five numbers from day-one data say how hard the problem is and which devices are worth modelling. None of them is a design.</p>
<div class="eq">\[ \begin{gathered} \Delta H = \frac{a\,v_0}{g} \qquad T_r = \frac{2L}{a} \\ 2\rho^* = \frac{a\,v_0}{g\,H_0^*} \end{gathered} \]</div>
<p>\(\Delta H\) is the head change of an abrupt stop, \(T_r\) the time for the wave to reach the far end and return, and \(2\rho^*\) Parmakian's pipeline parameter &mdash; the Joukowsky head over the absolute steady head at the pump \(H_0^*\) &mdash; used to enter the classical air-vessel charts [4][6]. On the reference line, with the nominal 0.8&nbsp;m bore:</p>
<div class="eq">\[ \begin{aligned} v_0 &= \frac{0.70}{\pi \times 0.8^2/4} = 1.393\ \text{m/s} \\ \Delta H &= \frac{1050 \times 1.393}{9.81} = 149.1\ \text{m} \\ T_r &= \frac{24\,000}{1050} = 22.9\ \text{s} \\ 2\rho^* &= \frac{149.1}{85.0+10.33} = 1.56 \end{aligned} \]</div>
<p>The fourth is a column-separation screen. On a flat line the first downsurge of an abrupt stop reaches vapour at the pump if</p>
<div class="eq">\[ \begin{aligned} \frac{a\,v_0}{g} &> h_0 + 9.8 \\ 149.1 &> 85.0 + 9.8 = 94.8\ \text{m} \quad\text{yes} \end{aligned} \]</div>
<p>with \(h_0\) the steady head above the pipe at the pump, the steady grade line less the pipe level at the discharge. That agrees with the instant-stop model. The screen assumes the pump stops much faster than 2L/a, and it only works one way: a <em>yes</em> is reliable for an abrupt stop, a <em>no</em> proves nothing. Pump inertia softens the first wave and moves separation out along the line &mdash; with the set's own 25&nbsp;kg&middot;m&sup2; the rundown model keeps the pump end at +2.5&nbsp;m while vapour forms 7.4&nbsp;km out &mdash; so for a real set a <em>yes</em> means model it, not proof of separation at the pump. At 450&nbsp;m/s the Joukowsky head is 63.9&nbsp;m and the screen says no, yet the head at the pump drops to 21.1&nbsp;m, keeps sinking as the wave travels out and the friction gradient that held the line up unwinds, and reaches vapour about 42&nbsp;s after the trip. Only at 300&nbsp;m/s does the unprotected line stay above vapour, at +5.0&nbsp;m. The fifth number screens a flywheel against the pipe period [3][5]:</p>
<div class="eq">\[ \begin{aligned} \tau &= \frac{\tfrac12\,I\,\omega_0^{\,2}}{P} \\ I = 25:\quad \tau &= 0.44\ \text{s} = 0.019\,T_r \\ I = 400:\quad \tau &= 7.01\ \text{s} = 0.31\,T_r \end{aligned} \]</div>
<p>Here \(I\) is the total rotating inertia of pump, motor and any flywheel in kg&middot;m&sup2;, \(\omega_0\) the rated speed in rad/s (1,480&nbsp;rpm = 155.0&nbsp;rad/s) and \(P\) the shaft power in W. On this line \(\tau/T_r = 0.15\) (200&nbsp;kg&middot;m&sup2;) still failed the +3.0&nbsp;m criterion and 0.31 (400&nbsp;kg&middot;m&sup2;) passed with margin &mdash; an observation on one line, not a rule. It says nothing about the start, which grows with inertia as \(t_{start} = I\,\omega_0/T_{acc}\), with \(T_{acc}\) the average torque left over to accelerate the rotor: 1.8&nbsp;s for the bare set and 28.1&nbsp;s with the flywheel, at half the rated 4,420&nbsp;N&middot;m.</p>

<h2 id="int-screening">8 &middot; Interactive: screening explorer</h2>
<p>Enter your own line. The chart plots the Joukowsky head across the range of wave speeds against the head available above vapour and above +3.0&nbsp;m; the marker is your line.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Joukowsky downsurge against the head available at the pump</div>
    <div class="fsub">Closed form: v = Q/(&pi;D&sup2;/4), &Delta;H = av/g, 2L/a, 2&rho;* = av/(gH&#8320;*) with H&#8320;* = h + 10.33 m, &tau; = &frac12;I&omega;&#8320;&sup2;/P. The separation screen assumes an abrupt stop on a flat line and is one-directional: a pass is not proof. It turns amber when the first wave would go below +3.0&nbsp;m without reaching vapour, or when &tau; exceeds 5&nbsp;% of 2L/a &mdash; our screening choice &mdash; so the rundown may prevent separation.</div>
  </div>
  <div class="chart-box"><canvas id="scrChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Length <span id="vL">12 km</span></label>
      <input type="range" id="sL" min="1" max="60" value="12" step="1">
      <div class="hint">Pump station to the first free surface.</div>
    </div>
    <div class="ctrl">
      <label>Diameter <span id="vDN">DN800</span></label>
      <select id="sDN">
        <option value="300">DN300</option><option value="400">DN400</option><option value="500">DN500</option>
        <option value="600">DN600</option><option value="700">DN700</option><option value="800" selected>DN800</option>
        <option value="900">DN900</option><option value="1000">DN1000</option><option value="1200">DN1200</option>
        <option value="1400">DN1400</option><option value="1600">DN1600</option>
      </select>
      <div class="hint">Nominal bore, as in the reference model.</div>
    </div>
    <div class="ctrl">
      <label>Flow <span id="vQ">0.70 m&sup3;/s</span></label>
      <input type="range" id="sQ" min="0.05" max="3" value="0.70" step="0.01">
      <div class="hint">Highest flow at which power can fail.</div>
    </div>
    <div class="ctrl">
      <label>Wave speed <span id="vA">1,050 m/s</span></label>
      <input type="range" id="sA" min="250" max="1400" value="1050" step="10">
      <div class="hint">Plastics sit at the low end, metals at the high end.</div>
    </div>
    <div class="ctrl">
      <label>Steady head above the pipe at the pump <span id="vH">85 m</span></label>
      <input type="range" id="sH" min="10" max="250" value="85" step="1">
      <div class="hint">Steady HGL minus pipe elevation at the discharge.</div>
    </div>
    <div class="ctrl">
      <label>Total rotating inertia <span id="vI">25 kg&middot;m&sup2;</span></label>
      <input type="range" id="sI" min="10" max="2000" value="25" step="5">
      <div class="hint">Pump, motor and any flywheel; 25 is assumed for the reference set. Use data sheets.</div>
    </div>
    <div class="ctrl">
      <label>Shaft power <span id="vP">685 kW</span></label>
      <input type="range" id="sP" min="50" max="3000" value="685" step="5">
      <div class="hint">Per pump at the duty point.</div>
    </div>
    <div class="ctrl">
      <label>Speed <span id="vN">1,480 rpm</span></label>
      <select id="sN">
        <option value="740">740 rpm</option><option value="990">990 rpm</option>
        <option value="1480" selected>1,480 rpm</option><option value="2960">2,960 rpm</option>
      </select>
      <div class="hint">Rotating energy grows with speed squared.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Velocity</div><div class="v" id="rV">1.39 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Joukowsky head</div><div class="v" id="rJ">149.1 <small>m</small></div></div>
    <div class="cell"><div class="k">2L/a</div><div class="v" id="rT">22.9 <small>s</small></div></div>
    <div class="cell"><div class="k">2&rho;*</div><div class="v" id="rRho">1.56</div></div>
    <div class="cell"><div class="k">Separation screen</div><div class="v" style="font-size:14px;margin-top:6px;" id="rSep"></div></div>
    <div class="cell"><div class="k">Rundown &tau;</div><div class="v" id="rTau">0.44 <small>s</small></div></div>
    <div class="cell"><div class="k">&tau; / (2L/a)</div><div class="v" id="rRat">0.019</div></div>
  </div>
</div>
<p class="fig-note">The defaults reproduce the reference line: <strong>1.39&nbsp;m/s, 149.1&nbsp;m, 22.9&nbsp;s, 2&rho;* = 1.56</strong>, and a red screen, because 149.1&nbsp;m exceeds the 94.8&nbsp;m above vapour. The Joukowsky line crosses the vapour line at \(a = g(h_0+9.8)/v_0\), about 670&nbsp;m/s here: a ductile iron or steel main of this size is at risk of separating on its first wave if the pump stops abruptly, and a PE main may not be &mdash; which is not the same as safe. Set the inertia to 400&nbsp;kg&middot;m&sup2; and &tau; becomes 7.01&nbsp;s, 0.31 of the period, and the screen turns amber: the rundown may prevent separation, so model it (on the reference line even 100&nbsp;kg&middot;m&sup2;, 0.077 of the period, kept the rundown model just off vapour). Stretch the line to 60&nbsp;km and the 400&nbsp;kg&middot;m&sup2; flywheel is 0.061 of a 114&nbsp;s period &mdash; the length argument against flywheels in one number.</p>

<h2 id="site-factors">9 &middot; Site and operation factors</h2>
<p>Options that both pass are separated by what the model does not see. These are engineering judgement, not rules.</p>
<ul class="clean">
  <li><strong>The critical side.</strong> If the downsurge reaches vapour, only devices that add water or slow the flow change qualify; relief and anticipator valves come after the downsurge is solved.</li>
  <li><strong>Profile and length.</strong> Knees and high points attract the minimum envelope and suit one-way tanks and air valves; a flat line spreads the problem and favours protection at the pump. Long lines push flywheels out of reach.</li>
  <li><strong>Power and starts.</strong> A weak grid means frequent trips and restarts, and a flywheel lengthens every start: confirm starting class and starts per hour with the motor manufacturer. A variable-speed drive shapes controlled stops, but on a power failure it has no supply and the pump runs down on its own inertia.</li>
  <li><strong>Operation and maintenance.</strong> Compressors and level instruments, pre-charge checks with the vessel isolated, valve function tests: choose what the operator will actually maintain (<a href="surge-analysis-risk.html">surge analysis and risk</a>). Some failures are silent whatever the device &mdash; lost gas, a ruptured bladder, a seized relief valve &mdash; so log pressures and alarm on vessel level or pre-charge (<a href="transient-analysis-scada.html">transient analysis and SCADA</a>).</li>
  <li><strong>Footprint and relative cost.</strong> In our experience valves are the smallest items, flywheels sit between, and vessel installations with compressors and civil works are the largest. The order is site-dependent, and the cheapest device that fails a limit is not an option.</li>
  <li><strong>Redundancy.</strong> With one vessel isolated for inspection, can the station still run? Split the volume or restrict pumping, and model that case.</li>
</ul>

<h2 id="int-matrix">10 &middot; Interactive: weighted decision matrix</h2>
<p>Once the model has removed the options that fail, a weighted matrix makes the remaining trade-offs explicit with client and operator. The scores are <strong>the author's engineering judgement for a typical water transmission main where a pump trip governs; rescore for your project</strong>. On every criterion 5 is the good end.</p>
__MATRIX_TABLE__
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Weighted score by option</div>
    <div class="fsub">Score = &Sigma;(weight &times; judgement score) / &Sigma; weights, on the 1&ndash;5 scale, split into the contribution of each criterion. Scores from the table above.</div>
  </div>
  <div class="chart-box"><canvas id="mtxChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Downsurge protection <span id="vW0">5</span></label>
      <input type="range" id="sW0" min="0" max="5" value="5" step="1">
      <div class="hint">Minimum envelope held above the criterion.</div>
    </div>
    <div class="ctrl">
      <label>Upsurge protection <span id="vW1">4</span></label>
      <input type="range" id="sW1" min="0" max="5" value="4" step="1">
      <div class="hint">Maximum limited at the pump and along the line.</div>
    </div>
    <div class="ctrl">
      <label>Predictability <span id="vW2">4</span></label>
      <input type="range" id="sW2" min="0" max="5" value="4" step="1">
      <div class="hint">Little dependence on collapse peaks, torque laws or settings.</div>
    </div>
    <div class="ctrl">
      <label>Ease of O&amp;M <span id="vW3">3</span></label>
      <input type="range" id="sW3" min="0" max="5" value="3" step="1">
      <div class="hint">Compressors, pre-charge checks, valve tests, sites.</div>
    </div>
    <div class="ctrl">
      <label>Low capex &amp; footprint <span id="vW4">2</span></label>
      <input type="range" id="sW4" min="0" max="5" value="2" step="1">
      <div class="hint">Relative only; no prices implied.</div>
    </div>
    <div class="ctrl">
      <label>Failure tolerance <span id="vW5">3</span></label>
      <input type="range" id="sW5" min="0" max="5" value="3" step="1">
      <div class="hint">Passive, or failure obvious and survivable.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Highest score</div><div class="v" style="font-size:15px;margin-top:6px;" id="rTop">Air-over-water vessel, 4.00</div></div>
    <div class="cell"><div class="k">Runner-up</div><div class="v" style="font-size:15px;margin-top:6px;" id="rSecond">Bladder vessel, 3.95</div></div>
    <div class="cell"><div class="k">Margin</div><div class="v" style="font-size:15px;margin-top:6px;" id="rMargin">0.05</div></div>
    <div class="cell"><div class="k">Downsurge check</div><div class="v" style="font-size:14px;margin-top:6px;" id="rDown"></div></div>
  </div>
</div>
<p class="fig-note">With the default weights the air-over-water vessel scores <strong>4.00</strong>, the bladder vessel 3.95, the one-way tank with a vessel 3.71 and the flywheel 3.62; the relief valve, anticipator valve and air valves trail at 2.19, 2.14 and 1.95. The top two are <strong>0.05 apart</strong>, and equal weights give a three-way tie at 3.67 between both vessel types and the flywheel &mdash; the matrix shows what the choice depends on; it does not make it. Now set downsurge and predictability to 0, low capex to 5, upsurge to 3, ease of O&amp;M to 2 and failure tolerance to 1: the relief valve leads at 3.82 and the downsurge check turns red. A matrix run before the hydraulic model rewards cheap devices that do not work.</p>

<h2 id="process">11 &middot; The design process, step by step</h2>
<ol>
  <li><strong>Define the load cases and limits</strong>: power failure at the highest flow, single pump trip, starts, valve and check valve closures; minimum pressure, allowable pressure of every class, vacuum rating of pipe and joints.</li>
  <li><strong>Run the unprotected model</strong> on the real profile and read both envelopes: where the minimum crosses the criterion, whether and how far the line separates.</li>
  <li><strong>Identify the critical side and location</strong> &mdash; pump end, knee, high point or the whole line.</li>
  <li><strong>Screen the options</strong> with section 7 and the profile; drop devices that cannot act on the critical side.</li>
  <li><strong>Size the survivors</strong>, one scenario each with identical run settings, until the envelopes sit inside both limits with margin.</li>
  <li><strong>Test failure and degraded cases</strong>: lost air, ruptured bladder or lost pre-charge, a relief valve that does not open, one vessel isolated, the motor maker's real inertia.</li>
  <li><strong>Test model sensitivity</strong>: wave speed range, friction method and, for anything that still cavitates, the column separation settings.</li>
  <li><strong>Specify and commission</strong>: data sheets carrying the modelled parameters, set points and alarms, a pump trip test with pressure logging, and a SCADA record.</li>
</ol>

<h2 id="hammer">12 &middot; Setting it up in Bentley HAMMER</h2>
<p>An honest comparison needs one model, one set of transient run options and one scenario per protection option, so that only the device changes between runs [16]. The general workflow is in <a href="hammer-transient-simulation-workflow.html">the HAMMER transient workflow</a> and <a href="hammer-transient-tips.html">HAMMER transient tips</a>.</p>
<ol>
  <li><strong>Base model on the real profile.</strong> Pipes with true elevations and wave speeds set with the Wave Speed Calculator (material, wall thickness, Young's modulus, Poisson's ratio, restraint condition); a Reservoir at the delivery end (<a href="boundary-conditions-reservoir-tank.html">reservoir boundary conditions</a>).</li>
  <li><strong>Pump set up for a trip.</strong> Pump trip (shut down), inertia (pump and motor) from data sheets, speed, 4-quadrant characteristic curves from the specific speed, and the pump's check valve with its closure time or delay. This models the real rundown, not the instant stop used here for the unprotected, vessel and relief-valve runs.</li>
  <li><strong>Transient run options, fixed once.</strong> A run duration of several pipe periods (the series used 150&nbsp;s, about six and a half times 2L/a); the time step computed from the shortest pipe and the wave speeds; a tight wave speed adjustment tolerance; vapour pressure and column separation enabled; one friction method for every run.</li>
  <li><strong>Unprotected scenario.</strong> In the Transient Results Viewer, plot the profile (path) from pump to reservoir with the maximum and minimum head envelopes, and time histories at the pump node and the worst points. Note where the minimum envelope sits at vapour pressure.</li>
  <li><strong>One scenario per protection option</strong>, with everything else unchanged:
    <ul>
      <li><em>Vessel:</em> a Hydropneumatic Tank at the pump discharge with initial gas volume, gas law exponent 1.2, tank volume, elevation, and inlet orifice diameter, minor loss coefficient and ratio of losses for the differential connection; for a bladder vessel, the has-bladder option and its preset gas pressure.</li>
      <li><em>Flywheel:</em> the same Pump with its inertia (pump and motor) raised by the flywheel.</li>
      <li><em>Relief valve:</em> a Surge Valve of the relief type at the discharge, with threshold pressure, time to open and to close, discharge coefficient and size; a surge anticipator variant only if it is a real candidate.</li>
      <li><em>One-way tank:</em> a one-way Surge Tank with its check valve at the knee node, with level and area, where the profile calls for it; <em>air valves:</em> Air Valve elements at the high points.</li>
    </ul>
  </li>
  <li><strong>Compare on one profile.</strong> Overlay the envelopes and tabulate each option's minimum and maximum with locations. Check a vessel's gas volume history stays inside the tank volume; for a relief valve read the pump-end history <em>and</em> the envelope along the whole line.</li>
  <li><strong>Failure scenarios</strong>: smaller initial gas volume, lost pre-charge, Surge Valve removed, one of two vessels isolated, lower-bound inertia.</li>
  <li><strong>Column separation sensitivity.</strong> For any option that still separates, rerun with changed column separation settings and wave speeds, and treat the upsurge as the range you see.</li>
  <li><strong>Other load cases</strong> for the preferred option and its runner-up; use the animation to explain the result to the operator.</li>
</ol>
<p>Field names differ slightly between HAMMER versions; follow the intent of each step.</p>

<h2 id="checklist">13 &middot; Design checklist</h2>
<ul class="clean">
  <li>Load cases agreed, including power failure at the highest flow; minimum pressure, allowable pressures and vacuum rating stated.</li>
  <li>Unprotected envelopes run on the real profile; critical side and location identified before any device is named.</li>
  <li>Screening recorded &mdash; velocity, Joukowsky head, 2L/a, 2&rho;*, the separation screen (read one way only), &tau; against 2L/a.</li>
  <li>Only devices that act on the critical side taken forward; no relief or anticipator valve offered as the answer to a downsurge.</li>
  <li>One model, one set of run options, one scenario per option, compared on the same profile.</li>
  <li>No verdict that rests on a collapse peak: anything still cavitating is redesigned or passes under every cavity setting tried.</li>
  <li>Vessel: gas history inside the shell with a water reserve, connection losses modelled both ways, pressure-vessel code, inspection access, potable approval of any membrane.</li>
  <li>Flywheel: data-sheet inertia, motor start time and starts per hour confirmed, bearings, shaft and foundation checked.</li>
  <li>Relief valve: set margin above normal operation, reseating, capacity for a large fraction of the pumped flow, and a drain to take it.</li>
  <li>One-way tank only at a knee or high point, below the lowest downstream grade line at rest; air valves modelled wherever they act.</li>
  <li>Failure cases run; alarms, pressure logging and a pump trip test written into the specification.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  On the reference 12&nbsp;km main an instant pump stop takes the whole line to vapour and the head to <strong>165&ndash;190&nbsp;m</strong>. A vessel (+4.3&nbsp;m / 119.2&nbsp;m) and a flywheel (+9.3&nbsp;m / 85.0&nbsp;m) both pass because both stop the column separating; a relief valve holds its pump end at about 96&nbsp;m but leaves the line at vapour and <strong>127&ndash;143&nbsp;m</strong>, straddling 136&nbsp;m. Choose the side of the wave first, the device second and the weights last.
</div>

<div class="callout green">
  <span class="lbl">Surge protection design series</span>
  <ol>
    <li><a href="wave-speed-surge-analysis.html">Wave speed: the number that sets the surge</a></li>
    <li><a href="surge-vessel-differential-orifice.html">The differential orifice: empty freely, refill slowly</a></li>
    <li><a href="surge-vessel-type-selection.html">Bladder, diaphragm or air-over-water vessel</a></li>
    <li><a href="one-way-surge-tank-design.html">One-way surge tanks at the knee</a></li>
    <li><a href="surge-relief-valve-sizing.html">Surge relief valves: what a valve at the pump can protect</a></li>
    <li><a href="pump-inertia-flywheel-surge.html">Pump inertia and the flywheel</a></li>
    <li><strong>Choosing surge protection on one pipeline</strong></li>
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
const LBL={size:10,family:'IBM Plex Sans'};
const TTL=t=>({display:true,text:t,font:{family:'IBM Plex Sans',size:12,weight:'600'}});
const LEG={labels:{font:{family:'IBM Plex Sans',size:11.5},usePointStyle:true,boxWidth:8}};
const ALLOW=136.0, PMIN=3.0, VAP=-9.8, G=9.81, PATM=10.33;
const sgn=v=>(v<0?'−':'+')+Math.abs(v).toFixed(1);
const badge=(c,t)=>'<span class="badge '+c+'">'+t+'</span>';
const rgba=(h,a)=>{const n=parseInt(h.slice(1),16);return 'rgba('+((n>>16)&255)+','+((n>>8)&255)+','+(n&255)+','+a+')';};
const r5=v=>5*Math.round(v/5);
/* a collapse-governed maximum is quoted as the range across the two cavity models */
function peak(a,b){
  const lo=Math.min(a,b),hi=Math.max(a,b);
  /* a range with the allowable inside it is always shown as a range, whole metres, however narrow */
  if(lo<ALLOW&&hi>ALLOW) return Math.round(lo)+'–'+Math.round(hi);
  if(hi-lo<2) return 'about '+Math.round(hi);
  return r5(lo)+'–'+r5(hi);
}
const hLine=(y,col,txt,pos)=>({type:'line',yMin:y,yMax:y,borderColor:col,borderWidth:1.5,borderDash:[6,4],
  label:{display:true,content:txt,position:pos,font:LBL,color:'#fff',backgroundColor:rgba(col,0.85),padding:{x:5,y:3}}});
const O=D.opts;
const OPTCOL=['#c0392b','#1b4f72','#1e8449','#b9770e'];

/* ---------- CHART 1 : four options on one pipeline ---------- */
const sOpt=document.getElementById('sOpt');
const PROT=['nothing: both limits fail','both sides of the wave, from the pump','both sides, by preventing separation','the pump end, on high pressure only'];
const lowMax=o=>o.maxg===null?o.max:Math.min(o.max,o.maxg);
const optChart=new Chart(document.getElementById('optChart'),{
  type:'bar',
  data:{labels:O.map(o=>o.short),
    datasets:[
      {label:'Lowest minimum to maximum, lower cavity model where they differ',data:O.map(o=>[o.min,lowMax(o)]),backgroundColor:OPTCOL.map(c=>rgba(c,0.8)),borderColor:OPTCOL.slice(),borderWidth:1.5,grouped:false,barPercentage:0.5,categoryPercentage:0.9},
      {label:'Collapse peak: range across the two cavity models',data:O.map(o=>o.maxg===null?null:[Math.min(o.max,o.maxg),Math.max(o.max,o.maxg)]),backgroundColor:OPTCOL.map(c=>rgba(c,0.4)),borderColor:OPTCOL.slice(),borderWidth:1.5,grouped:false,barPercentage:0.5,categoryPercentage:0.9}
    ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,ticks:{font:{family:'IBM Plex Sans',size:11}}},
            y:{type:'linear',min:-20,max:200,title:TTL('Pressure head above the pipe (m)'),...AX}},
    plugins:{legend:LEG,
      /* labels sit in the gaps between bars, clear of the bar ends they describe */
      annotation:{annotations:{
        lim:hLine(ALLOW,'#c0392b','PN16 allowable 136 m','50%'),
        crit:hLine(PMIN,'#1e8449','+3.0 m','75%'),
        vap:hLine(VAP,'#7f8c8d','vapour −9.8 m','50%')}},
      tooltip:{callbacks:{label:c=>{const o=O[c.dataIndex];
        if(c.datasetIndex===1) return 'collapse peak '+peak(o.max,o.maxg)+' m (cavity-model range)';
        return o.maxg===null?('minimum '+sgn(o.min)+' m, maximum '+fmt1(o.max)+' m'):('minimum '+sgn(o.min)+' m (vapour)');}}}}}
});
function updOpt(){
  const i=+sOpt.value, o=O[i];
  document.getElementById('vOpt').textContent=o.short;
  optChart.data.datasets[0].backgroundColor=OPTCOL.map((c,k)=>rgba(c,k===i?0.85:0.18));
  optChart.data.datasets[1].backgroundColor=OPTCOL.map((c,k)=>rgba(c,k===i?0.4:0.08));
  optChart.update('none');
  const minOk=o.min>=PMIN, vap=o.min<=VAP+0.01;
  document.getElementById('rOMin').innerHTML=sgn(o.min)+' <small>m</small> '+(minOk?badge('good','meets +3.0 m'):badge('bad',vap?'vapour':'below +3.0 m'));
  let maxState;
  if(o.maxg===null){
    maxState=o.max<=ALLOW?0:2;
    document.getElementById('rOMax').innerHTML=fmt1(o.max)+' <small>m</small> '+(maxState===0?badge('good','within 136 m'):badge('bad','above 136 m'));
  }else{
    const lo=Math.min(o.max,o.maxg),hi=Math.max(o.max,o.maxg);
    maxState=hi<=ALLOW?0:(lo>ALLOW?2:1);
    document.getElementById('rOMax').innerHTML=peak(o.max,o.maxg)+' <small>m</small> '+[badge('good','below 136 m in both models'),badge('warn','depends on the cavity model'),badge('bad','above 136 m in both models')][maxState];
  }
  let ver;
  if(minOk&&maxState===0) ver=badge('good','passes both limits');
  else if(!minOk&&maxState===2) ver=badge('bad','fails both limits');
  else if(!minOk&&maxState===1) ver=badge('bad','fails the minimum; maximum uncertain');
  else if(!minOk) ver=badge('bad','fails the minimum');
  else if(maxState===1) ver=badge('warn','meets the minimum; maximum depends on the cavity model');
  else ver=badge('bad','fails the maximum');
  document.getElementById('rOVer').innerHTML=ver;
  document.getElementById('rOProt').textContent=PROT[i];
}
sOpt.addEventListener('input',updOpt);updOpt();

/* ---------- CHART 2 : where and when ---------- */
const sOpt2=document.getElementById('sOpt2'), sView=document.getElementById('sView');
const KM=D.x.map(v=>v/1000);
const pts=(xs,ys)=>ys.map((y,k)=>({x:xs[k],y:y}));
const envChart=new Chart(document.getElementById('envChart'),{
  type:'line',
  data:{datasets:[
    {label:'',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.4,pointRadius:0,tension:0},
    {label:'',data:[],borderColor:'#b9770e',backgroundColor:'rgba(185,119,14,0.18)',borderWidth:2,borderDash:[6,4],pointRadius:0,fill:'-1',tension:0},
    {label:'',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,tension:0},
    {label:'',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.5,borderDash:[3,3],pointRadius:0,tension:0},
    {label:'',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.6,borderDash:[4,3],pointRadius:0,tension:0}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0,max:12,title:TTL('Chainage from the pump (km)'),...AX},
            y:{type:'linear',min:-20,max:200,title:TTL('Pressure head above the pipe (m)'),...AX}},
    plugins:{legend:{...LEG,labels:{...LEG.labels,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}},
      annotation:{annotations:{
        lim:hLine(ALLOW,'#c0392b','136 m','start'),
        crit:hLine(PMIN,'#1e8449','+3.0 m','end'),
        vap:hLine(VAP,'#7f8c8d','vapour −9.8 m','start'),
        per:{type:'line',xMin:D.period,xMax:D.period,borderColor:'#6b4f9e',borderWidth:1.5,borderDash:[4,4],display:false,
          label:{display:true,content:'2L/a = 22.9 s',position:'end',font:LBL,color:'#fff',backgroundColor:rgba('#6b4f9e',0.85),padding:{x:5,y:3}}}}},
      /* a single cavity model's collapse peak is never quoted to 0.1 m: whole metres above the design minimum */
      tooltip:{callbacks:{label:c=>{const y=c.parsed.y;return `${c.dataset.label}: ${(c.dataset.whole&&y>PMIN)?fmt0(y):fmt1(y)} m`;}}}}}
});
function updEnv(){
  const i=+sOpt2.value, view=+sView.value, o=O[i], ds=envChart.data.datasets;
  document.getElementById('vOpt2').textContent=o.short;
  document.getElementById('vView').textContent=view===0?'Envelope along the line':'Head at the pump against time';
  const cav=o.maxg!==null, ann=envChart.options.plugins.annotation.annotations;
  ds[1].whole=cav; ds[2].whole=false; ds[3].whole=false; ds[4].whole=true;
  if(view===0){
    ds[0].label=cav?'Maximum, vapour cavity model':'Maximum head'; ds[0].data=pts(KM,o.Hmax); ds[0].whole=cav;
    ds[1].label='Maximum, gas cavity model'; ds[1].data=cav?pts(KM,o.Hmaxg):[];
    ds[2].label='Minimum head'; ds[2].data=pts(KM,o.Hmin);
    ds[3].label='Steady HGL'; ds[3].data=pts(KM,D.hgl);
    ds[4].label='No protection, pump end'; ds[4].data=[];
    envChart.options.scales.x.max=12; envChart.options.scales.x.title.text='Chainage from the pump (km)';
    ann.per.display=false; ann.vap.label.position='start';
  }else{
    ds[0].label=cav?'Pump end, vapour cavity model':'Pump end'; ds[0].data=pts(D.t,o.H); ds[0].whole=cav;
    ds[1].data=[]; ds[2].data=[]; ds[3].data=[];
    ds[4].label='No protection, instant stop (vapour cavity model)'; ds[4].data=i===0?[]:pts(D.t,O[0].H);
    envChart.options.scales.x.max=150; envChart.options.scales.x.title.text='Time after the trip (s)';
    ann.per.display=true; ann.vap.label.position='end';
  }
  envChart.update('none');
  const vapLen=o.Hmin.slice(0,-1).filter(h=>h<=VAP+0.01).length*0.1;
  document.getElementById('rEMin').innerHTML=o.min<=VAP+0.01?(sgn(o.min)+' m over '+fmt1(vapLen)+' km '+badge('bad','vapour')):(sgn(o.min)+' m at '+fmt1(o.at_min/1000)+' km '+(o.min>=PMIN?badge('good','ok'):badge('bad','low')));
  const where=cav?(o.at_max===o.at_max_g?(o.at_max===0?'at the pump':fmt1(o.at_max/1000)+' km'):(fmt1(Math.min(o.at_max,o.at_max_g)/1000)+'–'+fmt1(Math.max(o.at_max,o.at_max_g)/1000)+' km')):(o.at_max===0?'at the pump':fmt1(o.at_max/1000)+' km');
  document.getElementById('rEMax').innerHTML=(cav?peak(o.max,o.maxg):fmt1(o.max))+' m, '+where;
  document.getElementById('rELen').innerHTML=cav?(fmt1(o.len136/1000)+' / '+fmt1(o.len136g/1000)+' km <small>vapour / gas model</small>'):(fmt1(o.len136/1000)+' km');
  document.getElementById('rEPump').innerHTML=cav?(peak(o.pump_max,o.pump_max_g)+' m'):(fmt1(o.pump_max)+' m');
}
[sOpt2,sView].forEach(s=>s.addEventListener('input',updEnv));updEnv();

/* ---------- CHART 3 : screening explorer ---------- */
const sL=document.getElementById('sL'),sDN=document.getElementById('sDN'),sQ=document.getElementById('sQ'),sA=document.getElementById('sA'),
      sH=document.getElementById('sH'),sI=document.getElementById('sI'),sP=document.getElementById('sP'),sN=document.getElementById('sN');
/* the wave-speed range the curve is drawn across; the y axis is scaled from it, not from the marker */
const AMIN=250, AMAX=1400;
const scrChart=new Chart(document.getElementById('scrChart'),{
  data:{datasets:[
    {type:'line',label:'Joukowsky head av/g',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.6,pointRadius:0,order:3},
    {type:'line',label:'Head above vapour, h + 9.8 m',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2,borderDash:[6,4],pointRadius:0,order:2},
    {type:'line',label:'Head above +3.0 m, h − 3.0 m',data:[],borderColor:'#1e8449',backgroundColor:'#1e8449',borderWidth:2,borderDash:[3,3],pointRadius:0,order:2},
    {type:'scatter',label:'This line',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:AMIN,max:AMAX,title:TTL('Wave speed a (m/s)'),...AX},
            y:{type:'linear',min:0,title:TTL('Head (m)'),...AX,ticks:{...AX.ticks}}},
    plugins:{legend:{...LEG,labels:{...LEG.labels,sort:(p,q)=>p.datasetIndex-q.datasetIndex}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt1(c.parsed.y)} m at ${fmt0(c.parsed.x)} m/s`}}}}
});
function updScr(){
  const L=+sL.value*1000, dn=+sDN.value, Q=+sQ.value, a=+sA.value, h=+sH.value, I=+sI.value, P=+sP.value*1000, rpm=+sN.value;
  document.getElementById('vL').textContent=fmt0(L/1000)+' km';
  document.getElementById('vDN').textContent='DN'+dn;
  document.getElementById('vQ').innerHTML=fmt2(Q)+' m&sup3;/s';
  document.getElementById('vA').textContent=fmt0(a)+' m/s';
  document.getElementById('vH').textContent=fmt0(h)+' m';
  document.getElementById('vI').innerHTML=fmt0(I)+' kg&middot;m&sup2;';
  document.getElementById('vP').textContent=fmt0(P/1000)+' kW';
  document.getElementById('vN').textContent=fmt0(rpm)+' rpm';
  const Dm=dn/1000, A=Math.PI*Dm*Dm/4, v=Q/A, J=a*v/G, Tr=2*L/a, rho=J/(h+PATM);
  const w0=rpm*2*Math.PI/60, tau=0.5*I*w0*w0/P, ratio=tau/Tr;
  const xs=[];for(let x=AMIN;x<=AMAX;x+=25)xs.push(x);
  scrChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(x*v/G).toFixed(2)}));
  scrChart.data.datasets[1].data=[{x:AMIN,y:h+9.8},{x:AMAX,y:h+9.8}];
  scrChart.data.datasets[2].data=[{x:AMIN,y:h-3.0},{x:AMAX,y:h-3.0}];
  scrChart.data.datasets[3].data=[{x:a,y:+J.toFixed(2)}];
  /* y axis: keep the whole Joukowsky curve, both limits and this line's marker in view, on a round tick step.
     The curve runs to the top of the wave-speed range, so it — not the marker — sets the scale. */
  const top=Math.max(h+9.8,J,AMAX*v/G)*1.05, steps=[10,20,25,50,100,200,250,500,1000,2000,2500,5000];
  const step=steps.find(s=>top/s<=8)||10000;
  scrChart.options.scales.y.max=Math.ceil(top/step)*step; scrChart.options.scales.y.ticks.stepSize=step;
  scrChart.update('none');
  document.getElementById('rV').innerHTML=fmt2(v)+' <small>m/s</small>'+(v>3?' '+badge('warn','high for a main'):'');
  document.getElementById('rJ').innerHTML=fmt1(J)+' <small>m</small>';
  document.getElementById('rT').innerHTML=fmt1(Tr)+' <small>s</small>';
  document.getElementById('rRho').innerHTML=fmt2(rho);
  /* the screen assumes an abrupt stop; once the rundown is a real fraction of 2L/a it no longer applies */
  const slow=ratio>=0.05;
  let sep;
  if(J>h+9.8) sep=slow?badge('warn','yes for an abrupt stop; rundown may prevent it: model it'):badge('bad','yes: vapour on the first wave of an abrupt stop');
  else if(J>h-3.0) sep=badge('warn','below +3.0 m on the first wave of an abrupt stop');
  else sep=badge('good','passes, but not proof');
  document.getElementById('rSep').innerHTML=sep;
  document.getElementById('rTau').innerHTML=fmt2(tau)+' <small>s</small>';
  document.getElementById('rRat').innerHTML=ratio<0.1?fmt3(ratio):fmt2(ratio);
}
[sL,sDN,sQ,sA,sH,sI,sP,sN].forEach(s=>s.addEventListener('input',updScr));updScr();

/* ---------- CHART 4 : weighted decision matrix ---------- */
const M=D.matrix;
const WS=[document.getElementById('sW0'),document.getElementById('sW1'),document.getElementById('sW2'),
          document.getElementById('sW3'),document.getElementById('sW4'),document.getElementById('sW5')];
const WV=[document.getElementById('vW0'),document.getElementById('vW1'),document.getElementById('vW2'),
          document.getElementById('vW3'),document.getElementById('vW4'),document.getElementById('vW5')];
/* six hexes that chart-theme.js maps to six different tokens */
const CRITCOL=['#1b4f72','#c0392b','#6b4f9e','#1e8449','#b9770e','#7f8c8d'];
const mtxChart=new Chart(document.getElementById('mtxChart'),{
  type:'bar',
  data:{labels:M.options.map(o=>o.name),
    datasets:M.criteria.map((c,k)=>({label:c,data:[],backgroundColor:CRITCOL[k],borderColor:'#fff',borderWidth:1,stack:'s'}))},
  options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0,max:5,stacked:true,title:TTL('Weighted score (1–5)'),...AX},
            y:{stacked:true,...AX,ticks:{font:{family:'IBM Plex Sans',size:11}}}},
    plugins:{legend:LEG,
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt2(c.parsed.x)}`}}}}
});
function updMtx(){
  const w=WS.map(s=>+s.value), sw=w.reduce((p,q)=>p+q,0);
  WV.forEach((el,k)=>{el.textContent=String(w[k]);});
  const tot=M.options.map(o=>sw>0?o.s.reduce((p,sc,k)=>p+w[k]*sc,0)/sw:0);
  M.criteria.forEach((c,k)=>{mtxChart.data.datasets[k].data=M.options.map(o=>sw>0?+(w[k]*o.s[k]/sw).toFixed(3):0);});
  mtxChart.update('none');
  if(sw===0){
    ['rTop','rSecond','rMargin'].forEach(id=>{document.getElementById(id).innerHTML='&mdash;';});
    document.getElementById('rDown').innerHTML=badge('warn','set at least one weight');
    return;
  }
  const ord=tot.map((v,k)=>k).sort((p,q)=>(tot[q]-tot[p])||(p-q));
  const a=ord[0], b=ord[1], mg=tot[a]-tot[b];
  document.getElementById('rTop').innerHTML=M.options[a].name+', '+fmt2(tot[a]);
  document.getElementById('rSecond').innerHTML=M.options[b].name+', '+fmt2(tot[b]);
  document.getElementById('rMargin').innerHTML=fmt2(mg)+' '+(mg<0.25?badge('warn','too close to call'):badge('good','clear'));
  const ds=M.options[a].s[0];
  document.getElementById('rDown').innerHTML=ds<=2?badge('bad','leader does not protect the downsurge'):(ds===3?badge('warn','leader protects it on short lines only'):badge('good','leader protects the downsurge'));
}
WS.forEach(s=>s.addEventListener('input',updMtx));updMtx();

window.addEventListener('load',function(){try{optChart.resize();envChart.resize();scrChart.resize();mtxChart.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993 — method of characteristics, pump trip transients, column separation and surge control devices.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014 — transients in pumping systems; air chambers, flywheels and valves as control devices.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004 — pump rundown and inertia; selecting protection for pumping mains.</li>
  <li>Parmakian, J. <em>Waterhammer Analysis</em>. Dover, 1963 — the pipeline parameter 2&rho;*, air chamber charts and surge tanks.</li>
  <li>Stephenson, D. <em>Pipeline Design for Water Engineers</em>, 3rd ed. Elsevier, 1989 — water hammer protection of pumping lines, flywheels and air vessels.</li>
  <li>Stephenson, D. &ldquo;Simple guide for design of air vessels for water hammer protection of pumping lines.&rdquo; <em>Journal of Hydraulic Engineering</em> (ASCE), 128(8), 2002 — dimensionless screening of pumping lines.</li>
  <li>Larock, B.E., Jeppson, R.W. &amp; Watters, G.Z. <em>Hydraulics of Pipeline Systems</em>. CRC Press, 2000 — transient boundary conditions for surge tanks and one-way tanks.</li>
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005 — protection strategies and the risks of air valves.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006 — vapour and gas cavity models; why collapse pressures are model-sensitive.</li>
  <li>AWWA M51 <em>Air Valves: Air-Release, Air/Vacuum, and Combination</em> — air valve functions and limitations.</li>
  <li>EN 805 <em>Water supply — Requirements for systems and components outside buildings</em> — design pressures and surge allowance.</li>
  <li>ISO 2531 <em>Ductile iron pipes, fittings, accessories and their joints for water applications</em> — the DN800 K9 pipe of the reference main.</li>
  <li>ISO 4126-1 <em>Safety devices for protection against excessive pressure — Part 1: Safety valves</em> — set pressure, overpressure and reseating.</li>
  <li>EN 13445 <em>Unfired pressure vessels</em>; ASME <em>Boiler and Pressure Vessel Code</em>, Section VIII, Division 1; Pressure Equipment Directive 2014/68/EU — surge vessels as pressure vessels.</li>
  <li>NSF/ANSI/CAN 61 <em>Drinking Water System Components — Health Effects</em> — bladder and diaphragm materials in contact with drinking water.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> product documentation and help — scenarios, protection elements, transient run options and the Transient Results Viewer.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeProtection #WaterHammer #HydraulicTransients #SurgeAnalysis #PumpTrip #PowerFailure #ColumnSeparation #VapourCavity #SurgeVessel #HydropneumaticTank #BladderVessel #Flywheel #PumpInertia #SurgeReliefValve #SurgeAnticipatorValve #OneWaySurgeTank #AirValves #Joukowsky #WaveSpeed #MethodOfCharacteristics #BentleyHAMMER #TransientModelling #DecisionMatrix #PumpingStations #TransmissionMains #DuctileIron #PipelineDesign #WaterInfrastructure</div>
"""

import json, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_D = json.load(open(os.path.join(_HERE, 'surge_data', 'datasets.json')))
_V = json.load(open(os.path.join(_HERE, 'surge_data', 'vessel_articles.json')))
_CMP = _D['compare']['rows']
_S0, _S95 = _D['srv']['cases'][0], _D['srv']['cases'][3]
_FW = _D['flywheel']['cases'][3]
_VF = _V['final']
# Maximum-head envelope of the flywheel case (I = 400 kg.m2), which datasets.json does not store. Reproduced with the audited solver,
# the same call as gen_datasets.py:
#   from moc import *; run(Line(), T=150, pump=dict(I=400, P0=685e3, w0=1480*2*pi/60, Hsh=100.0, k=20/0.49, Hsuc=5.0, eta=0.80))['Hmax']
# rounded to 0.1 m. The same run reproduces datasets.json flywheel.cases[3].Hmin exactly, and line_max 85.0 at the pump.
_FW_HMAX = [85.0, 84.7, 84.3, 84.0, 83.7, 83.3, 83.0, 82.7, 82.3, 82.0, 81.7, 81.3, 81.0, 80.7, 80.3, 80.0, 79.6, 79.3, 79.0, 78.6, 78.3,
            78.0, 77.6, 77.3, 77.0, 76.6, 76.3, 76.0, 75.6, 75.3, 75.0, 74.6, 74.3, 73.9, 73.6, 73.3, 72.9, 72.6, 72.3, 71.9, 71.6, 71.3,
            70.9, 70.6, 70.3, 69.9, 69.6, 69.2, 68.9, 68.6, 68.2, 67.9, 67.6, 67.2, 66.9, 66.8, 66.7, 66.6, 66.4, 66.3, 66.1, 66.0, 65.8,
            65.7, 65.5, 65.3, 65.2, 65.0, 64.8, 64.6, 64.4, 64.2, 64.0, 63.8, 63.6, 63.3, 63.1, 62.9, 62.6, 62.4, 62.1, 61.9, 61.6, 61.3,
            61.0, 60.7, 60.4, 60.1, 59.8, 59.5, 59.1, 58.8, 58.5, 58.1, 57.7, 57.4, 57.0, 56.6, 56.2, 55.8, 55.4, 54.9, 54.5, 54.0, 53.6,
            53.1, 52.7, 52.7, 52.7, 52.4, 51.7, 51.1, 50.4, 49.8, 49.1, 48.4, 47.7, 47.0, 46.3, 45.5, 44.8]

def _opt(short, row, Hmax, Hmaxg, Hmin, H, at_min, at_max, at_max_g, len136, len136g, pump_max, pump_max_g):
    return dict(short=short, min=row['line_min'], max=row['line_max'], maxg=row['line_max_dgcm'],
                at_min=at_min, at_max=at_max, at_max_g=at_max_g, len136=len136, len136g=len136g,
                pump_max=pump_max, pump_max_g=pump_max_g, Hmax=Hmax, Hmaxg=Hmaxg, Hmin=Hmin, H=H)

# Author's engineering judgement (1 poor - 5 good) for a typical water transmission main where a pump trip governs.
_MATRIX = dict(
    criteria=['Downsurge', 'Upsurge', 'Predictability', 'Ease of O&M', 'Low capex & footprint', 'Failure tolerance'],
    options=[
        dict(name='Air-over-water vessel', s=[5, 5, 5, 2, 2, 3],
             why='Feeds the line at once and absorbs the return; needs compressors, level control and a pressure-vessel regime.'),
        dict(name='Bladder vessel', s=[5, 5, 4, 3, 2, 3],
             why='Same hydraulics without compressors; larger shell, and a pre-charge checked only with the vessel isolated.'),
        dict(name='One-way tank with a vessel', s=[5, 4, 4, 2, 3, 3],
             why='Only at a knee or high point; shrinks the vessel but adds a second site, a refill line and a check valve.'),
        dict(name='Surge relief valve', s=[1, 3, 1, 3, 5, 2],
             why='Caps the head at the valve only; no help on the downsurge, line collapse peaks only partly reduced; needs function tests.'),
        dict(name='Surge anticipator valve', s=[1, 3, 2, 2, 4, 2],
             why='Open before the return wave, but adds no water on the downsurge; settings need careful commissioning.'),
        dict(name='Flywheel', s=[3, 4, 3, 4, 3, 5],
             why='Passive and always present; limited by line length and motor starting; sensitive to the torque law.'),
        dict(name='Air valves (complement)', s=[2, 1, 1, 3, 4, 2],
             why='Local relief at high points; admitted air must leave without a slam; never the primary device unmodelled.'),
    ])

def _matrix_table():
    # scores in a narrow table; the one-line reasons in a list below it, so nothing is clipped on a phone
    heads = ['Down', 'Up', 'Predict.', 'Ease of O&amp;M', 'Low capex', 'Fail-safe']
    rows = ''.join('    <tr><td>%s</td>%s</tr>\n' % (o['name'], ''.join('<td class="num">%d</td>' % v for v in o['s']))
                   for o in _MATRIX['options'])
    why = ''.join('  <li><strong>%s</strong> &mdash; %s</li>\n' % (o['name'], o['why'][0].lower() + o['why'][1:])
                  for o in _MATRIX['options'])
    return ('<div class="tbl-wrap"><table style="display:table">\n'
            '  <caption>Judgement scores, 1 (poor) to 5 (good): author&rsquo;s engineering judgement for a typical water transmission main; rescore for your project. '
            'Columns: downsurge, upsurge, predictability, ease of O&amp;M, low capex &amp; footprint, failure tolerance.</caption>\n'
            '  <thead><tr><th>Option</th>' + ''.join('<th class="num">%s</th>' % h for h in heads) + '</tr></thead>\n'
            '  <tbody>\n' + rows + '  </tbody>\n</table></div>\n'
            '<ul class="clean">\n' + why + '</ul>')

DATA = dict(
    x=_D['srv']['x'],
    hgl=[round(v, 1) for v in _V['steady']['hgl']],
    t=[round(v, 2) for v in _S0['t']],
    period=22.9,
    opts=[
        _opt('No protection', _CMP[0], _S0['Hmax'], _S0['Hmax_dgcm'], _S0['Hmin'], _S0['H'],
             0, _S0['at_max'], _S0['at_max_dgcm'], _S0['len_above_136'], _S0['len_above_136_dgcm'], _S0['pump_max'], _S0['pump_max_dgcm']),
        _opt('Surge vessel', _CMP[1], _VF['Hmax'], None, _VF['Hmin'], _VF['pump_H'],
             _VF['at_min'], _VF['at_max'], None, 0, None, _VF['pump']['max'], None),
        _opt('Flywheel', _CMP[2], _FW_HMAX, None, _FW['Hmin'], _FW['H'],
             _FW['at_min'], 0, None, 0, None, 85.0, None),
        _opt('Relief valve', _CMP[3], _S95['Hmax'], _S95['Hmax_dgcm'], _S95['Hmin'], _S95['H'],
             0, _S95['at_max'], _S95['at_max_dgcm'], _S95['len_above_136'], _S95['len_above_136_dgcm'], _S95['pump_max'], _S95['pump_max_dgcm']),
    ],
    matrix=dict(criteria=_MATRIX['criteria'], options=[dict(name=o['name'], s=o['s']) for o in _MATRIX['options']]),
)
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))
BODY = BODY.replace('__MATRIX_TABLE__', _matrix_table())

SPEC = dict(
    slug='choosing-surge-protection', cat='surge', mins=36,
    date_iso='2026-09-16', date_human='September 2026', date_ar='سبتمبر 2026',
    title='Choosing Surge Protection: Vessel, One-Way Tank, Relief Valve or Flywheel on the Same Pipeline',
    reg_title='Choosing Surge Protection: Vessel, One-Way Tank, Relief Valve or Flywheel on the Same Pipeline',
    reg_tag='Surge Analysis · Surge Protection · Design Decisions',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Surge Protection &middot; Design Decisions',
    desc='How to choose surge protection for a pumped water main: a surge vessel, a flywheel and a surge relief valve compared on one 12 km DN800 pipeline after a pump trip, with the one-way tank and air valves in context, screening formulas, site factors, a HAMMER procedure and four interactive charts.',
    og_desc='After an instant pump stop the unprotected 12 km DN800 main reaches vapour and 165–190 m. A 20 m³ vessel holds +4.3 m and 119.2 m, a 400 kg·m² flywheel +9.3 m and 85.0 m; a 95 m relief valve leaves the line at vapour and 127–143 m, straddling 136 m.',
    ld_desc='A design-perspective guide to choosing between surge vessels, flywheels, relief and anticipator valves, one-way tanks and air valves on one pumping main, with screening, a decision matrix and a HAMMER procedure.',
    img_alt='Dark technical cutaway of a water main on steel supports with four surge protection devices: a bladder surge vessel, a horizontal one-way tank, a pump with a large flywheel and a spring-loaded relief valve, faint line drawings behind, a tick-and-cross comparison table and a small chart of static lift against pipeline length',
    en_tag='Surge &amp; Transient Analysis &middot; Choosing Surge Protection',
    en_title='Choosing Surge Protection: Vessel, One-Way Tank, Relief Valve or Flywheel on the Same Pipeline',
    en_excerpt='On one 12 km DN800 main after an instant pump stop, a 20 m³ vessel holds the line between <strong>+4.3 m and 119.2 m</strong>; a 400 kg·m² flywheel holds +9.3 m with nothing above the steady 85.0 m, if the motor can start it; a relief valve set at 95 m caps its own pump end but leaves the line at vapour and <strong>127&ndash;143 m</strong>, straddling the 136 m limit. With no protection the line reaches vapour and <strong>165&ndash;190 m</strong>. There is no best surge device, only the right one for a given line, load case and site. The article adds screening formulas, site factors, a weighted decision matrix, a HAMMER procedure and four interactive charts.',
    en_search='choosing surge protection selection water hammer protection device comparison pump trip power failure transmission main pumping station surge vessel hydropneumatic tank air vessel air-over-water bladder vessel flywheel pump inertia rundown surge relief valve surge anticipator valve one-way surge tank air valves column separation vapour cavity collapse peak Joukowsky head wave speed 2L/a pipeline parameter Parmakian screening decision matrix weighted scoring Bentley HAMMER scenarios alternatives transient results viewer envelopes PN16 design minimum pressure ductile iron DN800 design checklist',
    ar_title='اختيار الحماية من المطرقة المائية: خزان الضغط الهوائي أم الخزان أحادي الاتجاه أم صمام تخفيف الضغط أم الحدافة على خط الأنابيب نفسه',
    ar_excerpt='على خط قطره ٨٠٠ مم وطوله ١٢ كم، وبعد التوقف الفوري للمضخات، يحفظ خزان ضغط هوائي سعته ٢٠ م³ الخط بين <strong>+٤٫٣ م و١١٩٫٢ م</strong>، وتحفظه حدافة ترفع عزم القصور الذاتي الكلي إلى ٤٠٠ كغ·م² عند +٩٫٣ م، أما صمام تخفيف الضغط المضبوط على ٩٥ م فيترك الخط عند التبخر وذروة <strong>١٢٧–١٤٣ م</strong>. ودون حماية يبلغ الخط ضغط التبخر ثم ذروة <strong>١٦٥–١٩٠ م</strong>. لا يوجد جهاز حماية أفضل على الإطلاق، بل جهاز مناسب لخط وحالة تحميل وموقع بعينها. مع مصفوفة قرار وخطوات HAMMER وأربعة رسوم تفاعلية.',
    ar_search='اختيار الحماية من الطرق المائي المطرقة المائية الموجات الانتقالية توقف المضخات انقطاع الكهرباء خط نقل المياه محطة ضخ خزان الضغط الهوائي خزان الضغط الخزان الهيدروليكي الهوائي خزان المثانة الحدافة عزم القصور الذاتي صمام تخفيف الضغط صمام تنفيس الضغط صمام استباق الموجة الخزان أحادي الاتجاه صمامات الهواء انفصال العمود المائي التجويف ضغط التبخر سرعة الموجة معادلة جوكوفسكي مصفوفة القرار برنامج هامر تحليل الموجات الانتقالية الحد الأدنى للضغط الحديد المرن',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
