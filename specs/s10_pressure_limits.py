# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">&ldquo;Maximum head below PN&rdquo; is how many surge results are judged, and it is too crude in both directions. On the 12&nbsp;km reference main the unprotected pump trip peaks at <strong>165&ndash;190&nbsp;m</strong> (16.1&ndash;18.6&nbsp;bar), above the 16&nbsp;bar rating of its flanged components. Yet under EN 805 and EN 545 those components may take <strong>20&nbsp;bar</strong> during a surge, so the peak itself would pass. What fails the design is the other side of the envelope: the line falls to full vacuum, beyond the <strong>&minus;0.8&nbsp;bar</strong> that pipeline components are required to withstand. This article sets the envelope against the limits that actually apply: the EN 805 pressure terms, the allowances in each pipe material's standard, collapse under vacuum, and fatigue for plastic pipes that see recurring surges.</p>

<h2 id="terms">1 &middot; The pressure terms that matter</h2>
<p>EN 805 separates what the system does from what its components can take [1]. For the system, the designer fixes:</p>
<ul class="clean">
  <li><strong>DP, design pressure:</strong> the highest steady operating pressure of the system or zone, including future developments but excluding surge.</li>
  <li><strong>MDP, maximum design pressure:</strong> DP plus surge. It is written MDPc when the surge has been calculated and MDPa when a fixed allowance is used instead; that allowance must not be less than 2&nbsp;bar.</li>
  <li><strong>STP, system test pressure:</strong> the hydrostatic test after laying. When surge is calculated, STP = MDPc + 1&nbsp;bar. When it is not, STP is the lower of 1.5 &times; MDPa and MDPa + 5&nbsp;bar.</li>
</ul>
<p>The product standards rate each component with three matching terms [1][2]:</p>
<ul class="clean">
  <li><strong>PFA, allowable operating pressure:</strong> what the component may carry continuously. It must be at least DP.</li>
  <li><strong>PMA, allowable maximum operating pressure:</strong> what it may carry for short periods, including surge. It must be at least MDP.</li>
  <li><strong>PEA, allowable site test pressure:</strong> what it may see in the hydrostatic test. It must be at least STP.</li>
</ul>
<p>For ductile iron to EN 545, PMA = 1.2 &times; PFA [2]. For flanged components the PN class sets the figures: PN10 is 10/12/17&nbsp;bar (PFA/PMA/PEA), PN16 is 16/20/25 and PN25 is 25/30/35. The pipe barrel is usually much stronger than the flanges: a DN800 pipe in class C25 has a PFA of 25&nbsp;bar. <strong>The weakest component sets the limit</strong>, and in a pumped main that is usually a valve, a flange, the vessel or an air valve, not the pipe.</p>
<div class="eq">\[ p\,[\text{bar}] \;=\; \frac{\rho g h}{10^5} \;=\; \frac{998 \times 9.81 \times h}{10^5} \;=\; \frac{h\,[\text{m}]}{10.21} \]</div>
<p>On the negative side, EN 805 and the related product standards require components to withstand a transient pressure <strong>80&nbsp;kPa below atmospheric</strong>, that is &minus;0.8&nbsp;bar or &minus;8.2&nbsp;m of water [1][3]. Full vacuum, where water boils and the column separates, is about &minus;9.8&nbsp;m at ordinary temperatures. Owners often add their own limits on top: this series uses 136&nbsp;m as a project maximum and +3.0&nbsp;m as a design minimum [4].</p>

<h2 id="reference-main">2 &middot; The reference main in EN 805 terms</h2>
<p>The reference main is a 12&nbsp;km DN800 ductile iron line with PN16 flanged valves and fittings, pumping 0.70&nbsp;m&sup3;/s at 85.0&nbsp;m at the pump [4]. The steady head at the pump is 85&nbsp;m, but against a closed line valve the pump makes its shut-off head of 105&nbsp;m (5&nbsp;m suction plus 100&nbsp;m), so we take DP = 105&nbsp;m = 10.3&nbsp;bar. With the series vessel (3.5&nbsp;m&sup3; of gas in a 20&nbsp;m&sup3; shell), the calculated maximum is 119.2&nbsp;m:</p>
<div class="tbl-wrap"><table>
  <caption>EN 805 check of the vessel-protected main, PN16 flanged components (PFA 16, PMA 20, PEA 25&nbsp;bar)</caption>
  <thead><tr><th>Term</th><th>How it is set</th><th class="num">Head <span style="text-transform:none">(m)</span></th><th class="num">bar</th><th>Component limit</th><th>Check</th></tr></thead>
  <tbody>
    <tr><td>DP</td><td>pump shut-off head</td><td class="num">105.0</td><td class="num">10.3</td><td>PFA 16.0</td><td><span class="badge good">pass</span></td></tr>
    <tr><td>MDPc</td><td>calculated maximum</td><td class="num">119.2</td><td class="num">11.7</td><td>PMA 20.0</td><td><span class="badge good">pass</span></td></tr>
    <tr><td>STP</td><td>MDPc + 1&nbsp;bar</td><td class="num">129.4</td><td class="num">12.7</td><td>PEA 25.0</td><td><span class="badge good">pass</span></td></tr>
    <tr><td>MDPa</td><td>DP + 2&nbsp;bar (if surge were not calculated)</td><td class="num">125.4</td><td class="num">12.3</td><td>PMA 20.0</td><td><span class="badge good">pass</span></td></tr>
    <tr><td>STP</td><td>lower of 1.5 MDPa and MDPa + 5&nbsp;bar</td><td class="num">176.5</td><td class="num">17.3</td><td>PEA 25.0</td><td><span class="badge good">pass</span></td></tr>
    <tr><td>Minimum</td><td>calculated lowest head</td><td class="num">+4.3</td><td class="num">+0.42</td><td>&minus;0.8&nbsp;bar</td><td><span class="badge good">pass</span></td></tr>
  </tbody>
</table></div>
<p>Two things follow. A calculated surge earns a lower test pressure: 12.7&nbsp;bar instead of 17.3, which matters on long mains where the test pressure decides section lengths and the pump size for the test. And the vessel design is limited not by the PN16 rating but by the project's own 136&nbsp;m, which is a choice about how much margin the owner wants, not a component limit. A report should say which limit it is applying and why.</p>

<h2 id="int-envelope">3 &middot; Interactive: one envelope, several limits</h2>
<p>Choose a protection case and a component class, and read the envelope against each limit. Where the peak comes from cavity collapse, two cavity models give different values, so both are drawn and both are checked [5].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Surge envelope of the reference main against component limits</div>
    <div class="fsub">12&nbsp;km DN800 ductile iron, flat profile, all pumps tripping. Maximum and minimum pressure heads from a method-of-characteristics model with a vapour cavity model; the dashed red trace is the maximum from a gas cavity model where the peak comes from cavity collapse. Lengths counted on the 100&nbsp;m grid. 1&nbsp;bar = 10.21&nbsp;m.</div>
  </div>
  <div class="chart-box"><canvas id="envChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Protection</label>
      <select id="sCase">
        <option value="0">No protection</option>
        <option value="1" selected>Vessel: 3.5 m³ gas, 20 m³ shell</option>
        <option value="2">Relief valve at 95 m, no vessel</option>
        <option value="3">Flywheel: 400 kg·m² in total</option>
      </select>
      <div class="hint">The four designs of the surge protection series.</div>
    </div>
    <div class="ctrl">
      <label>Weakest component class</label>
      <select id="sCls">
        <option value="10">PN10: PFA 10, PMA 12, PEA 17 bar</option>
        <option value="16" selected>PN16: PFA 16, PMA 20, PEA 25 bar</option>
        <option value="25">PN25 or C25 barrel: PFA 25, PMA 30, PEA 35 bar</option>
      </select>
      <div class="hint">Ductile iron to EN 545: PMA = 1.2 PFA, PEA = PMA + 5 bar.</div>
    </div>
    <div class="ctrl">
      <label>Units</label>
      <select id="sUnit">
        <option value="m" selected>metres of water</option>
        <option value="bar">bar</option>
      </select>
      <div class="hint">Gauge pressure in both.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Highest pressure</div><div class="v" id="rMax" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Against PFA</div><div class="v" style="font-size:14px;margin-top:6px;" id="rPFA">&ndash;</div></div>
    <div class="cell"><div class="k">Against PMA (MDP check)</div><div class="v" style="font-size:14px;margin-top:6px;" id="rPMA">&ndash;</div></div>
    <div class="cell"><div class="k">Against 136 m project limit</div><div class="v" style="font-size:14px;margin-top:6px;" id="rPrj">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest pressure</div><div class="v" id="rMin" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Against &minus;0.8 bar</div><div class="v" style="font-size:14px;margin-top:6px;" id="rVac">&ndash;</div></div>
    <div class="cell"><div class="k">Against +3.0 m</div><div class="v" style="font-size:14px;margin-top:6px;" id="rDes">&ndash;</div></div>
    <div class="cell"><div class="k">STP (MDPc + 1 bar)</div><div class="v" id="rSTP" style="font-size:17px;">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">With no protection the peak of 164.6&ndash;189.9&nbsp;m (16.1&ndash;18.6&nbsp;bar) exceeds PFA but stays inside the PMA of PN16 components, while the whole line goes to vapour. With the relief valve the peak along the line is 126.7&ndash;143.3&nbsp;m, inside PFA and PMA but over the project limit under one cavity model, and the line still goes to vapour. Only the vessel and the flywheel meet every limit. Switch to PN10 components and the vessel case still passes PMA (12&nbsp;bar = 122.5&nbsp;m against 119.2&nbsp;m), but with 3.3&nbsp;m to spare, which is less than the spread between cavity models on any case that cavitates.</p>
<div class="callout warn">
  <span class="lbl">Why a peak inside PMA is still not a pass</span>
  The unprotected case passes the maximum-pressure check only because the column has already separated: the peak comes from cavity collapse, its value depends on the cavity model (25&nbsp;m apart here), and the separation itself takes every point on the line to full vacuum. We never accept a maximum that depends on column separation. The line must first be kept out of vapour; only then is its maximum a number that can be checked against PMA.
</div>

<h2 id="materials">4 &middot; What each pipe material allows</h2>
<p>Each material family states its surge allowance differently. These are the rules we apply, with the references; always check the current edition and the manufacturer's own rating.</p>
<div class="tbl-wrap"><table>
  <caption>Surge allowances by material</caption>
  <thead><tr><th>Material</th><th>Standard</th><th>Maximum including surge</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>Ductile iron</td><td>EN 545 [2]</td><td>PMA = 1.2 &times; PFA</td><td>Flanged components rated by PN; the barrel class (C25, C30, C40) is usually higher.</td></tr>
    <tr><td>Ductile iron</td><td>AWWA C150 [6]</td><td>Working pressure plus a 100&nbsp;psi (6.9&nbsp;bar) surge allowance, built into the thickness design</td><td>Larger surges need a thicker class or protection.</td></tr>
    <tr><td>Steel</td><td>AWWA M11 [7]</td><td>Hoop stress under working plus transient pressure &le; 75&nbsp;% of yield</td><td>Working pressure alone is limited to 50&nbsp;% of yield.</td></tr>
    <tr><td>Polyethylene</td><td>AWWA C906, M55 [8]</td><td>Occasional surge: total &le; 2.0 &times; PC. Recurring surge: total &le; 1.5 &times; PC</td><td>PC is the pressure class; temperature derating applies.</td></tr>
    <tr><td>GRP</td><td>AWWA M45, C950 [9]</td><td>Working plus surge &le; 1.4 &times; PN</td><td>Commonly stated by manufacturers; confirm with the supplier.</td></tr>
    <tr><td>PVC-U, PVC-O</td><td>EN ISO 1452, AWWA C900 [10]</td><td>Per the class standard and the manufacturer</td><td>Recurring surges are checked for fatigue (section 6).</td></tr>
  </tbody>
</table></div>
<p>The occasional and recurring distinction runs through all of them. A power failure that trips every pump is an occasional event: a few times a year at most. A pump start or a planned stop is a recurring one: thousands of times over the life of the main. The design envelope of a surge study is usually the occasional trip, checked against PMA or its equivalent. Recurring events are smaller but far more numerous, and for plastics they are the ones that consume the pipe (section 6).</p>

<h2 id="vacuum">5 &middot; Vacuum: will the pipe collapse?</h2>
<p>A minimum envelope at vapour pressure means the pipe wall carries about one atmosphere of external pressure. For thick ductile iron that is trivial. For thin steel, GRP and plastics it is a buckling check. For a long unrestrained pipe, the elastic critical pressure is [11][12]:</p>
<div class="eq">\[ P_{cr} \;=\; \frac{2E}{1-\nu^2}\left(\frac{t}{D_m}\right)^3 \;=\; \frac{2E}{1-\nu^2}\left(\frac{1}{SDR-1}\right)^3 \]</div>
<p>where \(t\) is the wall thickness, \(D_m\) the mean diameter and SDR the outside diameter over the wall. For GRP, rated by its ring stiffness SN = \(EI/D_m^3\) in N/m&sup2;, the same expression is \(P_{cr} = 24\,SN\) per unit length. Real pipes are not perfectly round, and the ovality reduces the capacity. The factor used in the PE pipe literature for an ovality \(\delta\) is [8][12]</p>
<div class="eq">\[ f_o \;=\; \left[\frac{1-\delta}{(1+\delta)^2}\right]^3 \qquad (\delta = 0.03 \Rightarrow f_o = 0.76) \]</div>
<p>We then apply a safety factor, 2.0 in our practice for a short-term event. Surges last seconds, so the short-term modulus applies, reduced for temperature. A buried pipe is also supported by the soil, which raises its buckling resistance considerably; the unrestrained value applies above ground, in chambers and galleries, and in poorly compacted trench.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Allowable vacuum for an unsupported pipe</div>
    <div class="fsub">\(P_{allow} = f_o\,P_{cr}/SF\) with \(P_{cr} = 2E(1-\nu^2)^{-1}(SDR-1)^{-3}\), or \(24\,SN\) for GRP. Curve against SDR (or SN) for the chosen material; marker at your pipe. Full vacuum is 1.01&nbsp;bar below atmospheric; EN 805 components must withstand 0.8&nbsp;bar.</div>
  </div>
  <div class="chart-box"><canvas id="vacChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Material</label>
      <select id="sMat">
        <option value="pe" selected>PE100 (E 900 MPa, &nu; 0.45)</option>
        <option value="pvc">PVC-U (E 3,000 MPa, &nu; 0.38)</option>
        <option value="steel">Steel (E 207,000 MPa, &nu; 0.30)</option>
        <option value="grp">GRP (by stiffness class SN)</option>
      </select>
      <div class="hint">Short-term moduli at about 20&nbsp;&deg;C; use the manufacturer's value.</div>
    </div>
    <div class="ctrl">
      <label><span id="lDim">SDR</span> <span id="vDim">17</span></label>
      <input type="range" id="sDim" min="0" max="7" value="3" step="1">
      <div class="hint" id="hDim">Outside diameter over wall thickness.</div>
    </div>
    <div class="ctrl">
      <label>Modulus multiplier <span id="vE">1.00</span></label>
      <input type="range" id="sE" min="0.5" max="1.2" value="1" step="0.05">
      <div class="hint">Below 1 for higher temperature or longer load duration.</div>
    </div>
    <div class="ctrl">
      <label>Ovality <span id="vOv">3 %</span></label>
      <input type="range" id="sOv" min="0" max="8" value="3" step="0.5">
      <div class="hint">Out-of-roundness from bedding and handling.</div>
    </div>
    <div class="ctrl">
      <label>Safety factor <span id="vSF">2.0</span></label>
      <input type="range" id="sSF" min="1" max="3" value="2" step="0.1">
      <div class="hint">Our practice: 2.0 for a short-term surge.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Critical pressure</div><div class="v" id="rPcr">&ndash;</div></div>
    <div class="cell"><div class="k">Ovality factor</div><div class="v" id="rFo">&ndash;</div></div>
    <div class="cell"><div class="k">Allowable vacuum</div><div class="v" id="rPal">&ndash;</div></div>
    <div class="cell"><div class="k">Full vacuum</div><div class="v" style="font-size:14px;margin-top:6px;" id="rFull">&ndash;</div></div>
    <div class="cell"><div class="k">EN 805: &minus;0.8 bar</div><div class="v" style="font-size:14px;margin-top:6px;" id="rEN">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">PE100 SDR17 allows 2.1&nbsp;bar of vacuum with 3&nbsp;% ovality and a factor of 2, comfortably more than full vacuum. SDR26 allows only 0.55&nbsp;bar and should not be exposed to full vacuum unsupported. GRP SN5000 has a critical pressure of 1.2&nbsp;bar before any reduction, so with ovality and a factor of 2 it allows 0.46&nbsp;bar; SN10000 allows 0.92. A DN800 steel pipe (outside diameter about 0.81&nbsp;m) needs a D/t of about 120 or less to take full vacuum on these assumptions, which is 6.7&nbsp;mm of wall or more. These are the cases in which the minimum envelope, not the maximum, decides the pipe class or the protection.</p>

<h2 id="fatigue">6 &middot; Fatigue: recurring surges in plastic pipes</h2>
<p>Ductile iron and steel are rarely limited by surge fatigue in water service. PVC and PE are: each pressure cycle consumes a little of the pipe's life, and the consumption rises steeply with the size of the swing. For PVC the method recommended by the PVC pipe industry is the one developed by Folkman, used in the Uni-Bell cyclic life calculator [13]. The hoop stress amplitude and the cycles to failure are</p>
<div class="eq">\[ \sigma_{amp} \;=\; \frac{(P_{max}-P_{min})(DR-1)}{4}, \qquad N \;=\; 10^{\,-4.196\,\log_{10}\sigma_{amp} \;+\; 17.76} \]</div>
<p>with pressures and stress in psi. The cyclic life in years is \(N\) divided by the number of cycles per year. We divide the result by 2 as a design margin. The pressures come straight from the surge model: the maximum and minimum at the critical point for each recurring event (a normal start, a normal stop, a duty change), not the trip envelope.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">PVC cyclic life from the recurring surge</div>
    <div class="fsub">Folkman method as used in the Uni-Bell calculator [13]: \(\sigma_{amp} = \Delta P\,(DR-1)/4\) (psi), \(N = 10^{-4.196\log\sigma_{amp}+17.76}\). Curves: cycles to failure against the pressure swing for four DRs, log scale. Horizontal line: cycles needed for the design life with the chosen margin.</div>
  </div>
  <div class="chart-box"><canvas id="fatChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>DR</label>
      <select id="sDR">
        <option value="14">DR14</option>
        <option value="18" selected>DR18</option>
        <option value="21">DR21</option>
        <option value="25">DR25</option>
      </select>
      <div class="hint">Outside diameter over wall thickness.</div>
    </div>
    <div class="ctrl">
      <label>Maximum pressure in the cycle <span id="vPx">9.0 bar</span></label>
      <input type="range" id="sPx" min="1" max="16" value="9" step="0.5">
      <div class="hint">From the surge model at the critical point.</div>
    </div>
    <div class="ctrl">
      <label>Minimum pressure in the cycle <span id="vPn">1.5 bar</span></label>
      <input type="range" id="sPn" min="-0.8" max="10" value="1.5" step="0.1">
      <div class="hint">Gauge; negative values are below atmospheric.</div>
    </div>
    <div class="ctrl">
      <label>Cycles per day <span id="vCy">24</span></label>
      <input type="range" id="sCy" min="1" max="200" value="24" step="1">
      <div class="hint">A start and a stop are two cycles.</div>
    </div>
    <div class="ctrl">
      <label>Design life <span id="vLf">50 years</span></label>
      <input type="range" id="sLf" min="10" max="100" value="50" step="5">
      <div class="hint">With a margin of 2 on cycles.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Pressure swing</div><div class="v" id="rDP">&ndash;</div></div>
    <div class="cell"><div class="k">Stress amplitude</div><div class="v" id="rSa">&ndash;</div></div>
    <div class="cell"><div class="k">Cycles to failure</div><div class="v" id="rN">&ndash;</div></div>
    <div class="cell"><div class="k">Cyclic life</div><div class="v" id="rLife">&ndash;</div></div>
    <div class="cell"><div class="k">With margin of 2</div><div class="v" id="rLife2">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:14px;margin-top:6px;" id="rFV">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">A DR18 force main cycling between 1.5 and 9.0&nbsp;bar 24 times a day lasts about 430 years by this method, 216 with the margin. Raise the maximum to 12&nbsp;bar and drop the minimum to 0, a swing of 12&nbsp;bar, and the life falls to about 60 years, 30 with the margin: short of a 50-year design life. Because life goes with the swing to the power of about 4.2, a protection device that halves the recurring swing multiplies the life roughly eighteen times. For PE, the industry's approach is the allowance in section 4: the recurring surge is kept within a total of 1.5 &times; PC, a level at which PE4710 pipe has been shown to last millions of cycles [8].</p>

<h2 id="worked-example">7 &middot; Worked example: checking the reference main</h2>
<h3>Step 1: identify the weakest component</h3>
<p>Pipe barrel DN800 C25 (PFA 25&nbsp;bar); valves, flanges and the vessel connection PN16 (16/20/25&nbsp;bar); air valves PN16. The system is PN16.</p>
<h3>Step 2: set DP and MDP</h3>
<p>DP = 105&nbsp;m = 10.3&nbsp;bar (pump shut-off). MDPc = 119.2&nbsp;m = 11.7&nbsp;bar from the governing trip. Both within PFA 16 and PMA 20.</p>
<h3>Step 3: check the owner's criteria</h3>
<p>Maximum 119.2&nbsp;m against the 136&nbsp;m project limit: 16.8&nbsp;m of margin. Minimum +4.3&nbsp;m against +3.0&nbsp;m: 1.3&nbsp;m of margin. The line never goes below atmospheric, so the &minus;0.8&nbsp;bar requirement is not engaged.</p>
<h3>Step 4: check vacuum capacity anyway</h3>
<p>If the vessel is out of service, the line goes to vapour (section 3). Ductile iron DN800 C25 is not at risk of collapse, but any thin-walled steel spools in the station and the air valves' own ratings must be checked against full vacuum, or the operating rules must forbid running without the vessel.</p>
<h3>Step 5: set the test pressure</h3>
<p>STP = MDPc + 1&nbsp;bar = 12.7&nbsp;bar, within PEA 25. Had the surge not been calculated, the test would have been 17.3&nbsp;bar.</p>
<h3>Step 6: recurring events</h3>
<p>Ductile iron is not fatigue-limited in this service. Had the main been PVC or PE, the normal start and stop would be modelled, and their swings run through section 6.</p>

<h2 id="hammer-setup">8 &middot; Reading the limits in Bentley HAMMER</h2>
<p>HAMMER reports heads and pressures; the limits are yours to add [14]. Field names differ slightly between versions.</p>
<ol>
  <li><strong>Give every pipe its pressure rating</strong> in a user data field (PFA and PMA, or PC for plastics), and record the weakest component on each pipe, not only the barrel class.</li>
  <li><strong>Plot pressure, not head</strong>, in the profile view: maximum and minimum pressure envelopes along the path, with the ground or pipe crown profile.</li>
  <li><strong>Draw the limits on the profile</strong>: PMA, PFA, the project maximum, &minus;0.8&nbsp;bar, full vacuum and the design minimum.</li>
  <li><strong>Use colour coding</strong> on the plan to show pipes whose maximum transient pressure exceeds their PMA, or whose minimum falls below their vacuum capacity, and check every flagged pipe.</li>
  <li><strong>Check vapour pockets and cavity volumes</strong> in the results: any column separation means the maximum is model-dependent, as in the unprotected case above.</li>
  <li><strong>Model recurring events separately</strong> (normal start, normal stop, duty changes) and export the pressure range at the critical points for the fatigue check.</li>
  <li><strong>Report MDPc and STP</strong> from the governing envelope, so the test pressure can be set from the calculation.</li>
</ol>

<h2 id="checklist">9 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Weakest component identified</strong> on every part of the line: valves, flanges, vessel, air valves, fittings.</li>
  <li><strong>DP, MDP and STP stated</strong> in EN 805 terms, with the basis of DP.</li>
  <li><strong>MDP &le; PMA, DP &le; PFA, STP &le; PEA</strong> for the weakest component.</li>
  <li><strong>Owner's criteria applied</strong> separately and named as such.</li>
  <li><strong>Minimum envelope checked</strong> against &minus;0.8&nbsp;bar, full vacuum and the collapse capacity of every thin-walled pipe.</li>
  <li><strong>No acceptance resting on a collapse peak</strong>: column separation is designed out first.</li>
  <li><strong>Occasional and recurring events separated</strong>, with fatigue checked for plastic pipes.</li>
  <li><strong>Temperature derating</strong> applied to plastic pipe ratings.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip: inertia, specific speed and four-quadrant curves</a></li>
    <li><strong>Reading the surge envelope against the pipe's real limits</strong></li>
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
const M2B=10.21, VAP=-9.8, PRJ=136.0, PMIN=3.0, VAC=-0.8*M2B;
const good=t=>'<span class="badge good">'+t+'</span>', bad=t=>'<span class="badge bad">'+t+'</span>', warn=t=>'<span class="badge warn">'+t+'</span>';
/* ---------- CHART 1 : envelope against limits ---------- */
const sCase=document.getElementById('sCase'), sCls=document.getElementById('sCls'), sUnit=document.getElementById('sUnit');
const X=D.x.map(x=>x/1000);
const hl=(v,txt,col,pos)=>({type:'line',yMin:v,yMax:v,borderColor:col,borderWidth:1.4,borderDash:[6,4],label:{display:true,content:txt,position:pos||'end',font:LBL,color:'#fff',backgroundColor:col}});
const envChart=new Chart(document.getElementById('envChart'),{
  data:{datasets:[
    {type:'line',label:'Maximum, vapour cavity model',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,order:2},
    {type:'line',label:'Maximum, gas cavity model',data:[],borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.6,borderDash:[5,4],pointRadius:0,order:3},
    {type:'line',label:'Minimum',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.4,pointRadius:0,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:12,title:{display:true,text:'Chainage from the pump station (km)',font:TTL},...AX},
            y:{type:'linear',title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${sUnit.value==='bar'?fmt2(c.parsed.y)+' bar':fmt1(c.parsed.y)+' m'} at ${fmt1(c.parsed.x)} km`}},
      annotation:{annotations:{}}}}
});
function updEnv(){
  const c=D.cases[+sCase.value], pfa=+sCls.value, pma=1.2*pfa, pea=pma+5, u=sUnit.value, k=u==='bar'?1/M2B:1;
  const Y=a=>a.map((v,i)=>({x:X[i],y:+(v*k).toFixed(3)}));
  envChart.data.datasets[0].data=Y(c.Hmax);
  envChart.data.datasets[1].data=c.Hmax_dgcm?Y(c.Hmax_dgcm):[];
  envChart.data.datasets[2].data=Y(c.Hmin);
  const unit=u==='bar'?' bar':' m', fv=v=>u==='bar'?fmt1(v*k):fmt0(v*k);
  envChart.options.scales.y.min=-15*k; envChart.options.scales.y.max=Math.max(220,pma*M2B+10)*k;
  envChart.options.scales.y.title.text=u==='bar'?'Pressure (bar gauge)':'Pressure head (m)';
  envChart.options.plugins.annotation.annotations={
    pma:hl(pma*M2B*k,'PMA '+fmt0(pma)+' bar','rgba(192,57,43,0.85)'),
    pfa:hl(pfa*M2B*k,'PFA '+fmt0(pfa)+' bar','rgba(185,119,14,0.85)'),
    prj:hl(PRJ*k,'project max 136 m','rgba(107,79,158,0.85)','start'),
    des:hl(PMIN*k,'+3.0 m','rgba(30,132,73,0.85)','start'),
    vac:hl(VAC*k,'−0.8 bar','rgba(192,57,43,0.85)','start'),
  };
  envChart.update('none');
  const lo=c.line_max_dgcm!=null?Math.min(c.line_max,c.line_max_dgcm):c.line_max, hi=c.line_max_dgcm!=null?Math.max(c.line_max,c.line_max_dgcm):c.line_max;
  const show=v=>u==='bar'?fmt2(v/M2B):fmt1(v);
  document.getElementById('rMax').innerHTML=(lo!==hi?show(lo)+'–'+show(hi):show(hi))+' <small>'+unit.trim()+'</small>';
  const chk=(lim)=>hi<=lim?good('pass'):(lo>lim?bad('fails'):warn('depends on cavity model'));
  document.getElementById('rPFA').innerHTML=chk(pfa*M2B);
  document.getElementById('rPMA').innerHTML=c.line_min<=VAP+0.05?bad('not valid: column separation'):chk(pma*M2B);
  document.getElementById('rPrj').innerHTML=chk(PRJ);
  document.getElementById('rMin').innerHTML=(u==='bar'?sgn(c.line_min/M2B,2):sgn(c.line_min,1))+' <small>'+unit.trim()+'</small>'+(c.line_min<=VAP+0.05?' <small>(vapour)</small>':'');
  document.getElementById('rVac').innerHTML=c.line_min>=VAC?good('pass'):bad('fails');
  document.getElementById('rDes').innerHTML=c.line_min>=PMIN?good('pass'):bad('fails');
  const stp=hi/M2B+1;
  document.getElementById('rSTP').innerHTML=fmt1(stp)+' <small>bar</small> '+(stp<=pea?good('≤ PEA '+fmt0(pea)):bad('> PEA '+fmt0(pea)));
}
[sCase,sCls,sUnit].forEach(s=>s.addEventListener('input',updEnv));updEnv();

/* ---------- CHART 2 : vacuum collapse ---------- */
const MAT={pe:{E:900e6,nu:0.45,name:'PE100',dims:[9,11,13.6,17,21,26,33,41],def:3},
           pvc:{E:3000e6,nu:0.38,name:'PVC-U',dims:[13.6,17,21,26,33,41,51],def:3},
           steel:{E:207e9,nu:0.30,name:'Steel',dims:[50,60,70,80,90,100,110,120,135,150,175,200],def:5},
           grp:{name:'GRP',dims:[1250,2500,5000,10000,20000],def:2}};
const sMat=document.getElementById('sMat'), sDim=document.getElementById('sDim'), sE=document.getElementById('sE'), sOv=document.getElementById('sOv'), sSF=document.getElementById('sSF');
const fo=d=>Math.pow((1-d)/Math.pow(1+d,2),3);
function pcr(m,dim,em){ // Pa
  if(m==='grp') return 24*dim;
  const M=MAT[m], r=1/(dim-1); return 2*M.E*em/(1-M.nu*M.nu)*r*r*r;
}
const vacChart=new Chart(document.getElementById('vacChart'),{
  data:{datasets:[
    {type:'line',label:'Allowable vacuum (bar)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:3,order:2},
    {type:'line',label:'Critical pressure, no reduction (bar)',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:3},
    {type:'line',showLine:false,label:'Your pipe',data:[],backgroundColor:'#c0392b',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'category',title:{display:true,text:'SDR',font:TTL},...AX},
            y:{type:'logarithmic',min:0.01,max:100,title:{display:true,text:'Pressure below atmospheric (bar, log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[0.01,0.1,0.8,1,10,100].includes(+v.toPrecision(2))?String(+v.toPrecision(2)):''}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (bar)','')}: ${fmt2(c.parsed.y)} bar`}},
      annotation:{annotations:{
        full:{type:'line',yMin:1.013,yMax:1.013,borderColor:'#c0392b',borderWidth:1.5,borderDash:[6,4],label:{display:true,content:'full vacuum 1.01 bar',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(192,57,43,0.85)'}},
        en:{type:'line',yMin:0.8,yMax:0.8,borderColor:'#b9770e',borderWidth:1.2,borderDash:[3,3],label:{display:true,content:'EN 805: 0.8 bar',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(185,119,14,0.85)'}}
      }}}}
});
let lastMat=null;
function updVac(){
  const m=sMat.value, M=MAT[m];
  if(m!==lastMat){ sDim.max=String(M.dims.length-1); sDim.value=String(M.def); lastMat=m; }
  const i=Math.min(+sDim.value,M.dims.length-1), dim=M.dims[i], em=+sE.value, ov=+sOv.value/100, sf=+sSF.value;
  const lab=m==='grp'?'SN':(m==='steel'?'D/t':'SDR');
  document.getElementById('lDim').textContent=lab;
  document.getElementById('vDim').textContent=m==='grp'?fmt0(dim)+' N/m²':String(dim);
  document.getElementById('hDim').textContent=m==='grp'?'Ring stiffness class.':(m==='steel'?'Outside diameter over wall thickness.':'Outside diameter over wall thickness.');
  document.getElementById('vE').textContent=fmt2(em);
  document.getElementById('vOv').textContent=(ov*100).toFixed(1).replace('.0','')+' %';
  document.getElementById('vSF').textContent=sf.toFixed(1);
  const f=fo(ov);
  vacChart.options.scales.x.title.text=m==='grp'?'Stiffness class SN (N/m²)':(m==='steel'?'D/t':'SDR');
  vacChart.data.labels=M.dims.map(d=>m==='grp'?fmt0(d):String(d));
  vacChart.data.datasets[0].data=M.dims.map(d=>pcr(m,d,em)*f/sf/1e5);
  vacChart.data.datasets[1].data=M.dims.map(d=>pcr(m,d,em)/1e5);
  vacChart.data.datasets[2].data=M.dims.map((d,j)=>j===i?pcr(m,d,em)*f/sf/1e5:null);
  vacChart.update('none');
  const p=pcr(m,dim,em)/1e5, pa=p*f/sf;
  document.getElementById('rPcr').innerHTML=fmt2(p)+' <small>bar</small>';
  document.getElementById('rFo').innerHTML=fmt2(f);
  document.getElementById('rPal').innerHTML=fmt2(pa)+' <small>bar</small>';
  document.getElementById('rFull').innerHTML=pa>=1.013?good('withstands'):bad('collapse risk');
  document.getElementById('rEN').innerHTML=pa>=0.8?good('withstands'):bad('below requirement');
}
[sMat,sDim,sE,sOv,sSF].forEach(s=>s.addEventListener('input',updVac));updVac();

/* ---------- CHART 3 : PVC fatigue ---------- */
const sDR=document.getElementById('sDR'), sPx=document.getElementById('sPx'), sPn=document.getElementById('sPn'), sCy=document.getElementById('sCy'), sLf=document.getElementById('sLf');
const PSI=14.5038, Ncyc=(dP,DR)=>Math.pow(10,-4.196*Math.log10(dP*PSI*(DR-1)/4)+17.76);
const SW=[];for(let k=0;k<=60;k++)SW.push(0.5+k*0.25);
const fatChart=new Chart(document.getElementById('fatChart'),{
  data:{datasets:[[14,'#1e8449'],[18,'#1b4f72'],[21,'#b9770e'],[25,'#c0392b']].map(([dr,c])=>({type:'line',label:'DR'+dr,data:SW.map(s=>({x:s,y:Ncyc(s,dr)})),borderColor:c,backgroundColor:c,borderWidth:1.8,pointRadius:0,order:3}))
    .concat([{type:'scatter',label:'Your cycle',data:[],backgroundColor:'#111',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}])},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:0.5,max:15.5,title:{display:true,text:'Pressure swing Pmax − Pmin (bar)',font:TTL},...AX},
            y:{type:'logarithmic',min:1e4,max:1e10,title:{display:true,text:'Cycles to failure (log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>{const e=Math.log10(v);return Math.abs(e-Math.round(e))<1e-9?'10'+['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹','¹⁰'][Math.round(e)]:'';}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${Math.round(c.parsed.y).toExponential(2)} cycles at ${fmt2(c.parsed.x)} bar`}},
      annotation:{annotations:{need:{type:'line',yMin:1e6,yMax:1e6,borderColor:'#6b4f9e',borderWidth:1.5,borderDash:[6,4],label:{display:true,content:'needed',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}}}}}
});
function updFat(){
  const DR=+sDR.value, px=+sPx.value, pn=+sPn.value, cy=+sCy.value, lf=+sLf.value;
  document.getElementById('vPx').textContent=fmt1(px)+' bar';
  document.getElementById('vPn').textContent=sgn(pn,1)+' bar';
  document.getElementById('vCy').textContent=cy;
  document.getElementById('vLf').textContent=lf+' years';
  const dP=Math.max(0,px-pn), sa=dP*PSI*(DR-1)/4, perYr=cy*365, need=2*perYr*lf;
  const A=fatChart.options.plugins.annotation.annotations.need; A.yMin=need; A.yMax=need; A.label.content='needed for '+lf+' years with margin 2';
  fatChart.data.datasets[4].data=dP>0?[{x:dP,y:Ncyc(dP,DR)}]:[];
  fatChart.update('none');
  document.getElementById('rDP').innerHTML=fmt1(dP)+' <small>bar</small>';
  if(dP<=0){['rSa','rN','rLife','rLife2'].forEach(k=>document.getElementById(k).innerHTML='<small>no swing</small>');document.getElementById('rFV').innerHTML=warn('set Pmax above Pmin');return;}
  const N=Ncyc(dP,DR), life=N/perYr;
  document.getElementById('rSa').innerHTML=fmt0(sa)+' <small>psi</small>';
  document.getElementById('rN').innerHTML=N>=1e6?(N/1e6).toFixed(N>=1e7?0:1)+' <small>million</small>':fmt0(N);
  document.getElementById('rLife').innerHTML=life>=1000?'> 1,000 <small>years</small>':fmt0(life)+' <small>years</small>';
  document.getElementById('rLife2').innerHTML=life/2>=1000?'> 1,000 <small>years</small>':fmt0(life/2)+' <small>years</small>';
  document.getElementById('rFV').innerHTML=life/2>=lf?good('meets '+lf+' years'):bad('short of '+lf+' years');
}
[sDR,sPx,sPn,sCy,sLf].forEach(s=>s.addEventListener('input',updFat));updFat();
window.addEventListener('load',function(){try{[envChart,vacChart,fatChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>EN 805 <em>Water supply. Requirements for systems and components outside buildings</em>: DP, MDP (MDPa and MDPc), STP, the minimum 2&nbsp;bar surge allowance, the test pressure rules, and the PFA, PMA and PEA relations for components.</li>
  <li>EN 545 <em>Ductile iron pipes, fittings, accessories and their joints for water pipelines</em>: pressure classes, PMA = 1.2 PFA, and the PFA, PMA and PEA of flanged components by PN.</li>
  <li>EN 14801 <em>Conditions for pressure classification of products for water and wastewater pipelines</em>: components to withstand a transient pressure 80&nbsp;kPa below atmospheric.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, its protection cases, the 136&nbsp;m and +3.0&nbsp;m project criteria, and the verified MOC solver.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006: why collapse peaks depend on the cavity model.</li>
  <li>AWWA C150/A21.50 <em>Thickness Design of Ductile-Iron Pipe</em>: working pressure plus a 100&nbsp;psi surge allowance in the thickness design.</li>
  <li>AWWA Manual M11 <em>Steel Pipe: A Guide for Design and Installation</em>: allowable stress under working and transient pressure, and buckling of steel pipe.</li>
  <li>AWWA C906 and Manual M55 <em>PE Pipe: Design and Installation</em>; Plastics Pipe Institute guidance: pressure class, occasional surge (total 2.0 &times; PC) and recurring surge (total 1.5 &times; PC), unconstrained buckling and the ovality correction.</li>
  <li>AWWA Manual M45 <em>Fiberglass Pipe Design</em> and AWWA C950: surge allowance for GRP, with manufacturers' statements of the 1.4 &times; PN limit.</li>
  <li>EN ISO 1452 <em>Plastics piping systems for water supply: PVC-U</em>, and AWWA C900 <em>PVC pressure pipe</em>: pressure classes and temperature derating for PVC.</li>
  <li>Timoshenko, S.P. &amp; Gere, J.M. <em>Theory of Elastic Stability</em>, 2nd ed. McGraw-Hill, 1961: buckling of long thin tubes under external pressure.</li>
  <li>Plastics Pipe Institute. <em>Handbook of Polyethylene Pipe</em>, 2nd ed., 2008: design for external pressure, short-term modulus and ovality compensation.</li>
  <li>Folkman, S. &amp; Parvez, J. &ldquo;PVC pipe cyclic design method.&rdquo; ASCE Pipelines 2020; and Uni-Bell PVC Pipe Association, <em>Force Main Design Guide for PVC Pipe</em> and Cyclic-Life Calculator: stress amplitude, cycles to failure and cyclic life.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: profile envelopes, user data fields, colour coding and transient results.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #HydraulicTransients #EN805 #EN545 #PFA #PMA #PEA #DesignPressure #MaximumDesignPressure #SystemTestPressure #SurgeAllowance #VacuumCollapse #PipeBuckling #PEPipe #PVCPipe #GRPPipe #SteelPipe #DuctileIron #Fatigue #CyclicLoading #ColumnSeparation #BentleyHAMMER #PipelineDesign #WaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'analyst.json')))['s10']
DATA = {'x': _A['x'], 'cases': [{k: c[k] for k in ('key', 'Hmax', 'Hmin', 'Hmax_dgcm', 'line_max', 'line_max_dgcm', 'line_min')} for c in _A['cases']]}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='surge-envelope-pipe-pressure-limits', cat='surge', mins=17,
    date_iso='2026-11-19', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Reading the Surge Envelope Against the Pipe’s Real Limits: PFA, PMA, Vacuum and Fatigue',
    reg_title='Reading the Surge Envelope Against the Pipe’s Real Limits: PFA, PMA, Vacuum and Fatigue',
    reg_tag='Surge Analysis · Pressure Limits · EN 805',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Pressure Limits &middot; EN 805',
    desc='How to judge a surge envelope against the limits that apply: EN 805 DP, MDP and STP against PFA, PMA and PEA, surge allowances for ductile iron, steel, PE, GRP and PVC, vacuum collapse of thin-walled pipe, and fatigue of PVC under recurring surges, with three interactive charts and the HAMMER set-up.',
    og_desc='The unprotected 12 km main peaks at 165–190 m, above the 16 bar rating of its PN16 components but inside their 20 bar PMA. What fails it is the vacuum: the whole line goes beyond the −0.8 bar components must withstand.',
    ld_desc='Checking surge results against pipe limits: EN 805 and EN 545 pressure terms, material surge allowances, vacuum collapse and PVC fatigue, worked on a 12 km DN800 main with the Bentley HAMMER set-up.',
    img_alt='Pipeline profile with maximum and minimum surge pressure envelopes crossing coloured limit bands for PFA, PMA and vacuum, beside cross-sections of ductile iron, steel, PE and GRP pipes, one of them buckled inward',
    en_tag='Surge &amp; Transient Analysis &middot; Pressure Limits',
    en_title='Reading the Surge Envelope Against the Pipe’s Real Limits: PFA, PMA, Vacuum and Fatigue',
    en_excerpt='The unprotected 12 km main peaks at <strong>165–190 m</strong>, above the 16 bar rating of its PN16 components but inside the <strong>20 bar</strong> they may carry during a surge under EN 805 and EN 545. What fails it is the other side: the line goes to full vacuum, beyond the <strong>−0.8 bar</strong> components must withstand. DP, MDP and STP against PFA, PMA and PEA, the surge allowance of each material, vacuum collapse and PVC fatigue, with three interactive charts.',
    en_search='surge envelope pipe pressure limits EN 805 design pressure DP maximum design pressure MDP MDPc MDPa system test pressure STP PFA PMA PEA EN 545 ductile iron pressure class PN16 flanged components AWWA C150 surge allowance steel pipe AWWA M11 PE pipe AWWA C906 M55 occasional surge recurring surge pressure class GRP AWWA M45 1.4 PN PVC fatigue cyclic life Folkman Uni-Bell vacuum collapse buckling critical pressure ovality SDR ring stiffness SN column separation Bentley HAMMER transient analysis water hammer',
    ar_title='قراءة غلاف الضغوط العابرة مقابل الحدود الحقيقية للأنبوب: PFA وPMA والتفريغ والكلال',
    ar_excerpt='يبلغ الضغط الأقصى في الخط المرجعي غير المحمي (١٢ كم) بين <strong>١٦٥ و١٩٠ م</strong>، أي أعلى من تصنيف ١٦ بار لمكوناته، لكنه ضمن <strong>٢٠ بار</strong> المسموح بها أثناء الطرق المائي وفق EN 805 وEN 545. أما ما يُسقط التصميم فهو الجانب الآخر: يصل الخط إلى التفريغ الكامل متجاوزاً <strong>−٠٫٨ بار</strong> التي يجب أن تتحملها المكونات. ضغوط التصميم والاختبار، وسماحات المواد، وانبعاج الأنابيب تحت التفريغ، وكلال أنابيب PVC، مع ثلاثة رسوم تفاعلية.',
    ar_search='غلاف الضغوط العابرة حدود ضغط الأنابيب ضغط التصميم ضغط التصميم الأقصى ضغط اختبار النظام PFA PMA PEA حديد الدكتايل أنابيب البولي إيثيلين أنابيب PVC أنابيب الألياف الزجاجية الأنابيب الفولاذية انبعاج الأنبوب تحت التفريغ الكلال الطرق المائي المطرقة المائية انفصال عمود الماء بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
