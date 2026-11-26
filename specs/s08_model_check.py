# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A transient model can be wrong in ways that no error message reports. We built the 12&nbsp;km reference main the way it usually arrives from a GIS import, with a 2.4&nbsp;m flowmeter spool and four other short pipes. We then ran it with a custom 0.1&nbsp;s time step and HAMMER-style wave-speed adjustment. It reported a maximum head of <strong>90.0&nbsp;m</strong>; the converged answer is <strong>119.3&nbsp;m</strong>. At 0.05&nbsp;s the same model put the line minimum at +1.4&nbsp;m, below the +3.0&nbsp;m design minimum used in this series, when the true value is +4.3&nbsp;m, a pass. And a 90&nbsp;s run of the correct model reports no upsurge at all, because the 119&nbsp;m peak does not arrive until <strong>101&nbsp;s</strong> after the trip. This article sets out the five checks we make before any surge result leaves the office, with the numbers that show why each one matters.</p>

<h2 id="five-checks">1 &middot; Five checks before you believe a transient run</h2>
<p>The reference main for the surge series is a 12&nbsp;km, DN800 ductile iron line carrying 0.70&nbsp;m&sup3;/s (1.39&nbsp;m/s) from an HGL of 85.0&nbsp;m at the pump to 44.8&nbsp;m at the reservoir. The wave speed is 1,050&nbsp;m/s, so 2L/a = 22.9&nbsp;s. Protection is a hydropneumatic vessel at the pump with 3.5&nbsp;m&sup3; of gas in a 20&nbsp;m&sup3; shell and a DN400 differential connection (see <a href="surge-vessel.html">Sizing the Hydropneumatic Surge Vessel</a>). Converged, this design keeps the line at or above <strong>+4.26&nbsp;m</strong> (lowest at 4.3&nbsp;km), with a maximum of <strong>119.3&nbsp;m</strong> at the pump, against a design minimum of +3.0&nbsp;m and a project limit of 136&nbsp;m.</p>
<div class="callout key">
  <span class="lbl">Which design minimum?</span>
  The minimum pressure is a project criterion, set by the owner or the designer, not a physical limit. This series uses +3.0&nbsp;m: the line stays above atmospheric with a margin, so no air is drawn in at joints or air valves and the model's uncertainty is covered. Many owners and consultants accept a sub-atmospheric minimum instead, commonly around &minus;3&nbsp;m (&minus;0.3&nbsp;bar). That is defensible when the pipe, joints and fittings are rated for it (EN 805 asks components to withstand &minus;0.8&nbsp;bar, or &minus;8.2&nbsp;m), when the 6.8&nbsp;m left before vapour at &minus;9.8&nbsp;m covers the model's uncertainty, and when every air valve that will open below atmospheric is in the model and sized for the air it admits. Both criteria can be right, but neither is a default to copy: <strong>the minimum you design to must be checked against the allowable values that apply to your project</strong>. That means the project specification, the owner&rsquo;s or utility&rsquo;s standards, and the manufacturers&rsquo; vacuum ratings for the pipe, joints, gaskets, valves and air valves. If any of them is stricter, it governs. Once the minimum is fixed, what matters is the margin between the computed minimum and the chosen one. A numerical error eats that margin whichever criterion you use. The chart in section 5 lets you set your own (see also <a href="surge-envelope-pipe-pressure-limits.html">the pipe's real limits</a>).
</div>
<p>Every number in this article comes from two method-of-characteristics codes written independently for this series: the solver behind the <a href="choosing-surge-protection.html">surge protection series</a> and a new multi-pipe solver that reproduces it to 0.01&nbsp;m on the uniform main [1][2]. Neither is Bentley HAMMER, but the time-step and adjustment logic follows the HAMMER documentation [3][4], so the effects shown here are the ones a HAMMER user meets. The five checks are:</p>
<ol>
  <li><strong>The steady state.</strong> Flows, HGL at both ends and the pump duty point match the hydraulic design before anything is tripped.</li>
  <li><strong>The time step and the adjustment it forces.</strong> One time step serves the whole model, so every pipe's length or wave speed is bent to fit it. Sections 2 to 6 cover this.</li>
  <li><strong>Grid convergence.</strong> Halving the time step should leave the answer unchanged (section 7).</li>
  <li><strong>Run duration.</strong> The envelope must stop changing well before the run ends (section 8).</li>
  <li><strong>A hand check.</strong> A test case whose answer is known, such as the Joukowsky rise for a fast valve closure, must come out right (section 9).</li>
</ol>
<div class="callout key">
  <span class="lbl">The reviewer's question</span>
  &ldquo;How do you know this number is right?&rdquo; A surge report that cannot answer it with the time step, the adjustments, a halved-step rerun and a run duration has not been checked, whatever software produced it. The <a href="surge-study-report-review-checklist.html">surge study report</a> article lists where each of these goes in the deliverable.
</div>

<h2 id="why-adjust">2 &middot; Why one time step forces an adjustment</h2>
<p>The method of characteristics moves along lines on which a pressure wave travels one reach in one time step. Each pipe <em>i</em> is cut into \(n_i\) reaches of length \(\Delta x_i = a_i\,\Delta t\), and that only works if its length is a whole number of reaches [1][5]:</p>
<div class="eq">\[ n_i \;=\; \frac{L_i}{a_i\,\Delta t} \quad\text{must be an integer} \;\ge 1 \]</div>
<p>With dozens of pipes of arbitrary length and several wave speeds, no practical \(\Delta t\) satisfies every pipe exactly. HAMMER therefore rounds each \(n_i\) and changes either the pipe's length or its wave speed so the rounded value fits [3][4]:</p>
<div class="eq">\[ \text{Adjust length: } L_i' = n_i\,a_i\,\Delta t \qquad\qquad \text{Adjust wave speed: } a_i' = \frac{L_i}{n_i\,\Delta t} \]</div>
<p>In both modes the wave takes \(n_i\,\Delta t\) to cross the pipe instead of \(L_i/a_i\). The difference lies in what else changes. Adjusting the length keeps the pipe's impedance \(a/gA\), so each metre per second of flow change still produces the right head change, but the pipe holds a different volume of water. Adjusting the wave speed keeps the volume but changes the impedance: a pipe whose wave speed is cut from 1,150 to 24&nbsp;m/s responds to a flow change with 2&nbsp;% of the head it should, and behaves like a small soft accumulator.</p>
<p>HAMMER shows the result in its <strong>Transient Time Step Options</strong> dialog: the time step, and the <strong>Max</strong>, <strong>Mean</strong> and <strong>RMS Adjustment</strong> over all pipes, in absolute terms or as a percentage. <strong>Length</strong> is the default adjustment; wave speed is offered as faster and acceptable for slow mass oscillations [3]. When the adjustment is too large HAMMER warns that the approximation &ldquo;deviates excessively from the entered values&rdquo;, and suggests lengthening short pipes, subdividing long ones or raising the <strong>Max Adjustment</strong> value [3]. The documentation says plainly that there is no hard rule for how much adjustment is acceptable, and that users should test the sensitivity of their results [4]. The rest of this article is that test, on one model.</p>
<div class="callout warn">
  <span class="lbl">The tempting shortcut</span>
  Raising <strong>Max Adjustment</strong> until the warning goes away, or typing in a larger <strong>Custom Time Step</strong> to make a big model run faster, is exactly how the results in section 5 were produced. Both are legitimate settings. Neither is safe without the checks that follow.
</div>

<h2 id="as-imported">3 &middot; The model as it arrives</h2>
<p>A model built from a GIS export or a station layout drawing carries every fitting that was drawn as a pipe. Ours has five pieces of steel station pipework between the pump and the boundary valve (one of them a 2.4&nbsp;m magnetic flowmeter spool), a 3.2&nbsp;m spool at a washout chamber, a 5.6&nbsp;m spool at an air valve tee and a 41&nbsp;m steel road crossing, among ten long ductile iron pipes. The total is still 12,000&nbsp;m. The steel station pipework is thicker-walled, so we give it 1,150&nbsp;m/s.</p>

<div class="tbl-wrap"><table>
  <caption>The as-imported model, and what two time steps do to it in each adjustment mode (adjustment as a percentage of the entered value)</caption>
  <thead><tr><th>Pipe</th><th>Description</th><th class="num">L <span style="text-transform:none">(m)</span></th><th class="num">a <span style="text-transform:none">(m/s)</span></th><th class="num">Travel time <span style="text-transform:none">(s)</span></th><th class="num">n at 0.1&nbsp;s</th><th class="num">Length adj. at 0.1&nbsp;s</th><th class="num">Wave speed adj. at 0.1&nbsp;s</th><th class="num">n at 0.005&nbsp;s</th></tr></thead>
  <tbody>
__RAWROWS__
  </tbody>
</table></div>
<p>At 0.1&nbsp;s the flowmeter spool, whose true travel time is 2.1&nbsp;ms, has to become one reach of 0.1&nbsp;s. Adjusting length turns 2.4&nbsp;m of pipe into 115&nbsp;m; adjusting wave speed turns 1,150&nbsp;m/s into 24&nbsp;m/s. The long pipes barely move. The <strong>Mean</strong> and <strong>RMS</strong> figures look alarming only because a handful of short pipes dominate them, which is the first lesson: <strong>read the adjustment pipe by pipe, not as one number</strong>.</p>

<h2 id="int-adjust">4 &middot; Interactive: the adjustment for any time step</h2>
<p>Choose the model and the adjustment mode and move the time step. The chart shows the largest adjustment in the model over the whole range of time steps for both modes; the table lists every pipe at the selected step. The readouts are the three figures HAMMER reports.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Time step against the adjustment it forces</div>
    <div class="fsub">\(n_i = \max(1, \mathrm{round}(L_i/a_i\Delta t))\). Length mode: \((n_i a_i\Delta t - L_i)/L_i\). Wave speed mode: \((L_i/n_i\Delta t - a_i)/a_i\). Max, mean and RMS of the absolute values over all pipes, unweighted. Log scales on both axes.</div>
  </div>
  <div class="chart-box"><canvas id="adjChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Model</label>
      <select id="sModel">
        <option value="raw" selected>As imported: 17 pipes, shortest 2.4 m</option>
        <option value="clean">Cleaned: 11 pipes, shortest 41 m</option>
      </select>
      <div class="hint">Section 6 explains how the short pipes were merged.</div>
    </div>
    <div class="ctrl">
      <label>Adjust</label>
      <select id="sMode">
        <option value="length" selected>Length (HAMMER default)</option>
        <option value="wave">Wave speed</option>
      </select>
      <div class="hint">The table and readouts follow this choice.</div>
    </div>
    <div class="ctrl">
      <label>Time step <span id="vDt">0.1 s</span></label>
      <input type="range" id="sDt" min="0" max="16" value="14" step="1">
      <div class="hint">From 0.001 to 0.2&nbsp;s.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Max adjustment</div><div class="v" id="rMax">&ndash;</div></div>
    <div class="cell"><div class="k">Mean adjustment</div><div class="v" id="rMean">&ndash;</div></div>
    <div class="cell"><div class="k">RMS adjustment</div><div class="v" id="rRms">&ndash;</div></div>
    <div class="cell"><div class="k">Worst pipe</div><div class="v" style="font-size:15px;margin-top:6px;" id="rWorst">&ndash;</div></div>
    <div class="cell"><div class="k">Reaches in the model</div><div class="v" id="rReach">&ndash;</div></div>
    <div class="cell"><div class="k">Run effort vs 0.1 s</div><div class="v" id="rCost">&ndash;</div></div>
  </div>
  <div class="tbl-wrap" style="margin-top:14px;"><table>
    <thead><tr><th>Pipe</th><th class="num">L <span style="text-transform:none">(m)</span></th><th class="num">a <span style="text-transform:none">(m/s)</span></th><th class="num">n</th><th class="num">Modelled <span style="text-transform:none">L / a</span></th><th class="num">Adjustment</th></tr></thead>
    <tbody id="adjRows"></tbody>
  </table></div>
</div>
<p class="fig-note">On the as-imported model the largest adjustment never falls below 5&nbsp;% in either mode, even at 0.001&nbsp;s with 11,421 reaches for a 12&nbsp;km main. The cleaned model gets below 5&nbsp;% at 0.005&nbsp;s with 2,284 reaches, and below 1.1&nbsp;% at 0.002&nbsp;s. The curves are saw-toothed: a slightly <em>larger</em> step can need less adjustment than a smaller one, because what matters is how close each \(L_i/a_i\Delta t\) falls to a whole number. Run effort is the number of reaches times the number of steps, relative to the same model at 0.1&nbsp;s.</p>

<h2 id="effect">5 &middot; What the adjustment does to the answer</h2>
<p>We ran the vessel-protected trip on both models at seven time steps in both modes, 150&nbsp;s each, and compared every result with a reference run of the as-imported model at 0.0005&nbsp;s (22,850 reaches, largest adjustment __REFADJ__&nbsp;%). The reference gives +4.26&nbsp;m at 4.3&nbsp;km, a maximum of 119.27&nbsp;m and a peak gas volume of 16.19&nbsp;m&sup3;. The cleaned model at 0.0005&nbsp;s agrees to 0.01&nbsp;m.</p>

<div class="tbl-wrap"><table>
  <caption>Vessel-protected pump trip on the as-imported model. Reference: +4.26&nbsp;m minimum, 119.27&nbsp;m maximum</caption>
  <thead><tr><th class="num">&Delta;t <span style="text-transform:none">(s)</span></th><th class="num">Reaches</th><th class="num">Min, length adj. <span style="text-transform:none">(m)</span></th><th class="num">Max, length adj. <span style="text-transform:none">(m)</span></th><th class="num">Min, wave speed adj. <span style="text-transform:none">(m)</span></th><th class="num">Max, wave speed adj. <span style="text-transform:none">(m)</span></th></tr></thead>
  <tbody>
__RESROWS__
  </tbody>
</table></div>

<p>Four things stand out.</p>
<ul class="clean">
  <li><strong>The errors go both ways.</strong> At 0.1&nbsp;s, wave-speed adjustment reports a maximum of 90.0&nbsp;m, 29&nbsp;m low, and a minimum of +4.9&nbsp;m, 0.7&nbsp;m better than the truth. The soft spools near the pump absorb the upsurge. At 0.05&nbsp;s the same mode puts the minimum at +1.4&nbsp;m near 0.9&nbsp;km: against the +3.0&nbsp;m minimum, a design that passes is reported as failing. With a &minus;3&nbsp;m criterion this case would still pass, but the error is the same 2.8&nbsp;m, and it would flip any design whose true minimum lay within 2.8&nbsp;m of that criterion.</li>
  <li><strong>Length adjustment fails more gently here.</strong> It keeps every pipe's impedance, so its errors come from the extra water and travel time. At 0.1&nbsp;s it reads 121.4&nbsp;m and +3.6&nbsp;m, conservative on both sides, but still 0.7&nbsp;m out on a 1.3&nbsp;m margin.</li>
  <li><strong>At 0.005&nbsp;s and below both modes agree with the reference</strong> to within 0.1&nbsp;m on both extremes. Even then the worst adjusted pipe, now a chamber spool changed by 24&nbsp;%, still moves the peak at the pump by 0.08&nbsp;m in wave-speed mode.</li>
  <li><strong>At 0.2&nbsp;s the model says there is no problem at all.</strong> Wave-speed adjustment reports a maximum of 85.0&nbsp;m, the steady head, and a minimum of +12.4&nbsp;m. Length adjustment at the same step reports +2.6&nbsp;m, a failure. Neither number has anything to do with the real main.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">The same trip, the same model, different time steps</div>
    <div class="fsub">Vessel-protected pump trip, 150&nbsp;s runs. Upper: highest head on the line. Lower: lowest pressure head on the line. Dashed lines are the 0.0005&nbsp;s reference run of the as-imported model (+4.26&nbsp;m and 119.27&nbsp;m). Time step on a log scale.</div>
  </div>
  <div class="chart-box" style="height:300px;"><canvas id="resMaxChart"></canvas></div>
  <div class="chart-box" style="height:300px;"><canvas id="resMinChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Model</label>
      <select id="sModel2">
        <option value="raw" selected>As imported: 17 pipes</option>
        <option value="clean">Cleaned: 11 pipes</option>
      </select>
      <div class="hint">Both adjustment modes are drawn.</div>
    </div>
    <div class="ctrl">
      <label>Time step for the readouts</label>
      <select id="sDt2">
        <option value="0">0.2 s</option>
        <option value="1" selected>0.1 s</option>
        <option value="2">0.05 s</option>
        <option value="3">0.02 s</option>
        <option value="4">0.01 s</option>
        <option value="5">0.005 s</option>
        <option value="6">0.002 s</option>
      </select>
      <div class="hint">Readouts for the length (L) and wave speed (a) modes.</div>
    </div>
    <div class="ctrl">
      <label>Design minimum <span id="vCrit2">+3.0 m</span></label>
      <input type="range" id="sCrit2" min="-5" max="5" value="3" step="0.5">
      <div class="hint">+3.0&nbsp;m in this series; many owners accept about &minus;3&nbsp;m.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Max adjustment, L / a</div><div class="v" id="rAdj2" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Highest head, L / a</div><div class="v" id="rMax2" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Error on the max, L / a</div><div class="v" id="rEmax2" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest head, L / a</div><div class="v" id="rMin2" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Error on the min, L / a</div><div class="v" id="rEmin2" style="font-size:17px;">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict at the minimum, L / a</div><div class="v" style="font-size:14px;margin-top:6px;" id="rVer2">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">Switch to the cleaned model and the spread collapses: at 0.1&nbsp;s the maximum is within 1.2&nbsp;m of the reference in both modes, and from 0.05&nbsp;s down every result is within 0.15&nbsp;m. At 0.1&nbsp;s the cleaned model in wave-speed mode still drops the minimum to +3.4&nbsp;m near 1&nbsp;km, because the 41&nbsp;m road crossing is then one reach with its wave speed cut by 64&nbsp;% and the 66&nbsp;m station pipe by 43&nbsp;%. At 0.2&nbsp;s even the cleaned model fails in wave-speed mode (&minus;0.4&nbsp;m). A large custom time step is the first thing we look for in someone else's run.</p>

<h2 id="clean-model">6 &middot; Cleaning the model: what to merge and what to keep</h2>
<p>The cure for adjustment is rarely a smaller time step. On a large network that multiplies run time, and HAMMER's documentation itself points to lengthening short pipes, subdividing long ones and using Skelebrator to remove short pipes [3][4]. We merged five things:</p>
<ul class="clean">
  <li><strong>Station pipework</strong> P-1 to P-5 became one 66.0&nbsp;m steel pipe. Where merged pipes have different wave speeds, keep the travel time: \(a_{eq} = \sum L_i \big/ \sum (L_i/a_i)\). Where they have different bores, keep the volume and the impedance as far as you can, and keep the station in detail if a check valve or the vessel connection sits inside it.</li>
  <li><strong>Chamber spools</strong> (P-9, P-14) were added to the neighbouring field pipe. A washout or air valve node must stay where the device is; only the spool goes.</li>
  <li><strong>The road crossing</strong> stayed at 41&nbsp;m: it is long enough to be a few reaches and its wave speed is genuinely different.</li>
</ul>
<p>Some things must never be merged away, whatever they do to the time step: a dead-end branch (it reflects the wave and doubles the pressure at its end), a closed valve, the node of any protection device, a high point or a change of gradient on the profile, and any pipe where the diameter changes enough to change the impedance. When in doubt, keep the pipe and reduce the time step for that run only.</p>
<div class="callout green">
  <span class="lbl">Our working rule</span>
  We clean the model until the largest adjustment is a few percent on every pipe longer than about two reaches, and then prove the time step by halving it (section 7). We read the adjustment pipe by pipe: on the cleaned model at 0.05&nbsp;s, a 40&nbsp;% length change on the 41&nbsp;m road crossing moved the answer by 0.14&nbsp;m at most, while a 98&nbsp;% wave-speed change on a 2.4&nbsp;m spool beside the pump moved the maximum by 29&nbsp;m.
</div>

<h2 id="convergence">7 &middot; Halve the step: grid convergence on the uniform main</h2>
<p>Even with no adjustment at all, a coarse grid smears steep wave fronts and moves the extremes. On the uniform reference main, where any \(\Delta t = 12{,}000/(1{,}050\,N)\) fits exactly, we ran three cases at six grid sizes: the vessel design, the 400&nbsp;kg&middot;m&sup2; flywheel of <a href="pump-inertia-flywheel-surge.html">Pump Inertia and the Flywheel</a>, and the unprotected trip, whose peak comes from cavity collapse.</p>

<div class="tbl-wrap"><table>
  <caption>Grid convergence on the uniform 12&nbsp;km main, 150&nbsp;s runs</caption>
  <thead><tr><th class="num">Reaches N</th><th class="num">&Delta;x <span style="text-transform:none">(m)</span></th><th class="num">&Delta;t <span style="text-transform:none">(s)</span></th><th class="num">Vessel: min <span style="text-transform:none">(m)</span></th><th class="num">Vessel: max <span style="text-transform:none">(m)</span></th><th class="num">Flywheel: min <span style="text-transform:none">(m)</span></th><th class="num">Unprotected max, vapour cavity <span style="text-transform:none">(m)</span></th><th class="num">Unprotected max, gas cavity <span style="text-transform:none">(m)</span></th></tr></thead>
  <tbody>
__GRIDROWS__
  </tbody>
</table></div>
<p>The two protected cases converge cleanly. From the coarsest grid to the finest, the vessel minimum falls by __VDROP__&nbsp;m, and every halving halves the change (0.16, 0.08, 0.04, 0.02, 0.01&nbsp;m), which is first-order behaviour. A model at 0.38&nbsp;s would report +4.57&nbsp;m and overstate the margin above +3.0&nbsp;m by a quarter. The flywheel minimum hardly moves (0.08&nbsp;m). The collapse peak behaves differently: the vapour cavity model settles at 189&ndash;190&nbsp;m, while the gas cavity model wanders between __DGLO__ and __DGHI__&nbsp;m with no trend. Collapse peaks do not converge the way a single-phase result does, which is why this series quotes them as a range and designs to keep the line out of vapour [6][7].</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Does the answer stop moving when the step is halved?</div>
    <div class="fsub">Uniform reference main, N = 30 to 960 reaches (\(\Delta t\) = 0.38 to 0.012&nbsp;s). Upper: the two protected minima. Lower: the unprotected maximum in the two cavity models. Grid on a log scale.</div>
  </div>
  <div class="chart-box" style="height:300px;"><canvas id="gridMinChart"></canvas></div>
  <div class="chart-box" style="height:300px;"><canvas id="gridMaxChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Your run</label>
      <select id="sGrid">
        <option value="0" selected>N = 30, &Delta;t = 0.381 s</option>
        <option value="1">N = 60, &Delta;t = 0.190 s</option>
        <option value="2">N = 120, &Delta;t = 0.095 s</option>
        <option value="3">N = 240, &Delta;t = 0.048 s</option>
        <option value="4">N = 480, &Delta;t = 0.024 s</option>
        <option value="5">N = 960, &Delta;t = 0.012 s</option>
      </select>
      <div class="hint">The readouts compare it with the run at half the step (twice the reaches).</div>
    </div>
    <div class="ctrl">
      <label>Tolerance on a halving <span id="vTol">0.10 m</span></label>
      <input type="range" id="sTol" min="0.02" max="0.5" value="0.1" step="0.02">
      <div class="hint">How much change you will accept before trusting the run.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Vessel min, this run</div><div class="v" id="rG1">&ndash;</div></div>
    <div class="cell"><div class="k">At half the step</div><div class="v" id="rG2">&ndash;</div></div>
    <div class="cell"><div class="k">Change on halving</div><div class="v" id="rG3">&ndash;</div></div>
    <div class="cell"><div class="k">Extrapolated value</div><div class="v" id="rG4">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;" id="rG5">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The extrapolated value assumes first-order convergence: \(H_\infty \approx 2H_{2N} - H_N\). From every grid, even N = 30 (0.38&nbsp;s), the extrapolation lands within 0.01&nbsp;m of the finest run. With a 0.10&nbsp;m tolerance the vessel minimum is converged from N = 60. Select N = 960 and there is no finer run to compare with, which is the honest position for any production model: the last halving is the evidence.</p>
<p>In HAMMER this check is two runs: the time step HAMMER suggests, and the same scenario with <strong>Use Custom Time Step?</strong> checked and half that value. The documentation recommends the same kind of test with a very small step [4]. Compare the minimum and maximum envelopes at the critical points, not only at the pump.</p>

<h2 id="duration">8 &middot; Run duration: the peak that arrives at 101 seconds</h2>
<p>A pump trip on a long main with a vessel is a slow event. The first downsurge is over in one wave cycle, but the column then swings back and forth between the vessel and the reservoir with a period set by the gas volume and the length of the line, much longer than 2L/a. On the reference main the lowest head is reached at __TMIN__&nbsp;s. The highest head, 119.2&nbsp;m at the pump, comes at <strong>__TMAX__&nbsp;s</strong> on the return swing, more than four times 2L/a. The <a href="hammer-transient-simulation-workflow.html">HAMMER workflow article</a> on this site uses 90&nbsp;s as an example duration; on this main a 90&nbsp;s run would report a maximum of 85.0&nbsp;m, the steady head, and miss the upsurge entirely.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">What a run of a given length would report</div>
    <div class="fsub">Vessel-protected pump trip on the uniform reference main, 400&nbsp;s at \(\Delta t\) = 0.0095&nbsp;s. Head at the pump and at mid-line (6&nbsp;km); the shaded area is the part of the event a run of the chosen length never sees. The dashed traces are the line envelope as it builds up.</div>
  </div>
  <div class="chart-box"><canvas id="durChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Run duration <span id="vDur">90 s</span></label>
      <input type="range" id="sDur" min="20" max="400" value="90" step="5">
      <div class="hint">2L/a = 22.9&nbsp;s. The vertical line marks the end of the run.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Duration / (2L/a)</div><div class="v" id="rD1">&ndash;</div></div>
    <div class="cell"><div class="k">Reported min</div><div class="v" id="rD2">&ndash;</div></div>
    <div class="cell"><div class="k">Reported max</div><div class="v" id="rD3">&ndash;</div></div>
    <div class="cell"><div class="k">Max missed by</div><div class="v" id="rD4">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;" id="rD5">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The minimum is captured from __TMINR__&nbsp;s onwards; the maximum needs __TMAXR__&nbsp;s. Between 102 and 400&nbsp;s nothing changes, so 150&nbsp;s (6.6 &times; 2L/a) is enough here. On a main protected by air valves, a one-way tank or a flywheel the governing peak can come later still, after a cavity has grown and collapsed or a tank has drained.</p>
<p>Our rule: run at least long enough to see the first full swing of the slowest oscillation in the system, then extend the run by half and confirm that neither envelope moves. If the maximum or minimum occurs in the last quarter of the run, the run is too short.</p>

<h2 id="hand-check">9 &middot; Hand checks the model must pass</h2>
<p>Before trusting a model of a real system, we run a test scenario whose answer we already know. The cleanest is the Joukowsky test: replace the pump with a reservoir at the duty head, put a valve at the far end, and close it faster than 2L/a. The head at the valve must jump by [1][5]</p>
<div class="eq">\[ \Delta H \;=\; \frac{a\,\Delta V}{g} \;=\; \frac{1050 \times 1.3926}{9.81} \;=\; __JTH__\ \text{m} \]</div>
<p>Our test model holds 45.8&nbsp;m at the valve in steady flow (1.0&nbsp;m across the open valve).</p>
<div class="tbl-wrap"><table>
  <caption>Joukowsky test on the uniform main: valve at 12&nbsp;km closing linearly, reservoir at 85.0&nbsp;m upstream</caption>
  <thead><tr><th>Check</th><th class="num">Hand value</th><th class="num">Model</th><th>Comment</th></tr></thead>
  <tbody>
__JROWS__
  </tbody>
</table></div>
<p>The rise above the Joukowsky value is line packing: as the front runs upstream it meets water at progressively higher head, and the water still flowing towards the valve behind it keeps packing the line, so the head at the valve keeps climbing until the reflection returns [1][8]. On a long, high-friction main it is a real part of the peak. If the first rise in your model is a few percent off \(a\Delta V/g\), look at the adjusted wave speeds before anything else.</p>
<p>Three more checks take minutes:</p>
<ul class="clean">
  <li><strong>Steady state.</strong> The initial HGL along the profile matches the hydraulic model, every pump sits at its duty point, and no air valve or relief valve is open at time zero.</li>
  <li><strong>Travel time.</strong> A disturbance at the pump must reach chainage \(x\) at \(x/a\): 5.71&nbsp;s to mid-line here. Place a report point there and look at the trace.</li>
  <li><strong>Energy.</strong> With friction on, every oscillation must decay. An oscillation that grows or does not die away points to a boundary or device input error.</li>
</ul>

<h2 id="hammer-setup">10 &middot; Setting it up in Bentley HAMMER</h2>
<p>Field names differ slightly between HAMMER versions; these follow the current documentation [3][4][9].</p>
<ol>
  <li><strong>Compute the steady state first</strong> and compare it with the design model: flows, pump duty points and the HGL at the ends of the main (85.0&nbsp;m and 44.8&nbsp;m here).</li>
  <li><strong>Clean the model for transients.</strong> Merge station pipework, chamber spools and other short pipes as in section 6, or use <strong>Skelebrator</strong>, but keep every device node, dead end, closed valve and high point.</li>
  <li><strong>Open Transient Time Step Options</strong> and read the suggested <strong>Time Step</strong> and the <strong>Max</strong>, <strong>Mean</strong> and <strong>RMS Adjustment</strong>. Set <strong>Adjustment Type</strong> to relative so the figures are percentages, and sort the pipe adjustments to find the worst pipes.</li>
  <li><strong>Leave Adjust on Length</strong> unless you have a reason to change it, and do not raise <strong>Max Adjustment</strong> just to clear the warning. If the warning appears, fix the short pipes it points to.</li>
  <li><strong>Set the run duration</strong> in time, not time steps, and make it at least 6&ndash;7 &times; 2L/a for a pumped main with a vessel. Extend it by half once and confirm that the envelopes do not change.</li>
  <li><strong>Choose report points</strong> at the pump, at the vessel, at every high point and knee, and at mid-line, and turn on <strong>Generate Animation Data</strong> so the profile envelopes can be checked along the whole line.</li>
  <li><strong>Run the halved step:</strong> check <strong>Use Custom Time Step?</strong>, enter half the suggested value, and rerun the governing scenario. Record both results in the report.</li>
  <li><strong>Run the Joukowsky test</strong> once per model as a separate scenario, with the pump replaced by a reservoir and a valve closing in a fraction of 2L/a at the far end.</li>
  <li><strong>Record everything</strong>: time step, adjustment mode, max/mean/RMS adjustment, the worst pipes, the halved-step result and the run duration, in the model basis of the report.</li>
</ol>

<h2 id="checklist">11 &middot; Checklist</h2>
<ul class="clean">
  <li><strong>Steady state matches the design model</strong> before any transient run.</li>
  <li><strong>Short pipes merged</strong> where they carry no device, dead end, high point or change of section.</li>
  <li><strong>Adjustment read pipe by pipe</strong>, with the worst pipes named and their effect understood.</li>
  <li><strong>Max Adjustment left at a value you can defend</strong>, never raised only to clear a warning.</li>
  <li><strong>Halved time step run</strong> on the governing scenario, with the change in minimum and maximum recorded.</li>
  <li><strong>Collapse peaks quoted as a range</strong>, and the design judged on keeping the line out of vapour.</li>
  <li><strong>Run duration</strong> long enough that neither envelope changes when it is extended by half.</li>
  <li><strong>Joukowsky test and travel-time check</strong> passed by the model.</li>
  <li><strong>Envelopes read along the whole line</strong>, not only at the pump.</li>
  <li><strong>All of the above written into the report</strong> (see <a href="surge-study-report-review-checklist.html">The Surge Study Report</a>).</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><strong>Is your HAMMER run right? Time step, adjustment and run duration</strong></li>
    <li><a href="surge-model-field-validation.html">Validating a surge model with a field pump-trip test</a></li>
    <li><a href="surge-sensitivity-uncertainty.html">Sensitivity and uncertainty: bounding the result</a></li>
    <li><a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip: inertia, specific speed and four-quadrant curves</a></li>
    <li><a href="transient-model-demands-network-detail.html">Demands, branches and dead ends in a transient model</a></li>
    <li><a href="surge-envelope-pipe-pressure-limits.html">Reading the surge envelope against the pipe's real limits</a></li>
    <li><a href="transient-forces-pipe-supports.html">Transient forces on pipe supports and bends</a></li>
    <li><a href="booster-stations-series-surge.html">Booster stations in series</a></li>
    <li><a href="pump-start-stop-vfd-ramp-surge.html">Pump starts, controlled stops and drive ramps</a></li>
    <li><a href="pipeline-filling-draining-restart-surge.html">Filling, draining and restarting a transmission main</a></li>
    <li><a href="wastewater-force-main-surge.html">Surge in wastewater force mains</a></li>
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
const pct=v=>(v>=100?fmt0(v):v>=10?fmt1(v):fmt2(v))+' %';
const PMIN=3.0, PMAX=136.0;
const DTS=[0.001,0.0015,0.002,0.003,0.004,0.005,0.0075,0.01,0.015,0.02,0.03,0.04,0.05,0.075,0.1,0.15,0.2];
function disc(pipes,dt,mode){
  return pipes.map(p=>{const L=p[2],a=p[3];const n=Math.max(1,Math.round(L/(a*dt)));
    const adj=mode==='length'?(n*a*dt-L)/L:(L/(n*dt)-a)/a;
    return {id:p[0],desc:p[1],L:L,a:a,n:n,Lm:mode==='length'?n*a*dt:L,am:mode==='length'?a:L/(n*dt),adj:adj};});
}
function stats(pipes,dt,mode){
  const d=disc(pipes,dt,mode), ab=d.map(p=>Math.abs(p.adj));
  let w=0; ab.forEach((v,i)=>{if(v>ab[w])w=i;});
  return {d:d,max:ab[w],mean:ab.reduce((s,v)=>s+v,0)/ab.length,rms:Math.sqrt(ab.reduce((s,v)=>s+v*v,0)/ab.length),
          worst:w,reaches:d.reduce((s,p)=>s+p.n,0)};
}
/* ---------- CHART 1 : adjustment calculator ---------- */
const sModel=document.getElementById('sModel'), sMode=document.getElementById('sMode'), sDt=document.getElementById('sDt');
const GRID=[];for(let k=0;k<=240;k++)GRID.push(Math.pow(10,-3+k*(Math.log10(0.2)+3)/240));
const adjChart=new Chart(document.getElementById('adjChart'),{
  data:{datasets:[
    {type:'line',label:'Max adjustment, length mode',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0,order:3},
    {type:'line',label:'Max adjustment, wave speed mode',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2,pointRadius:0,order:4},
    {type:'scatter',label:'Selected',data:[],backgroundColor:'#6b4f9e',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'logarithmic',min:0.001,max:0.2,title:{display:true,text:'Time step Δt (s, log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2].includes(+v.toPrecision(3))?String(+v.toPrecision(3)):''}},
            y:{type:'logarithmic',min:0.1,max:20000,title:{display:true,text:'Largest adjustment in the model (%, log scale)',font:TTL},grid:{color:'#eef2f5'},
               ticks:{font:{family:FF,size:11},callback:v=>[0.1,1,10,100,1000,10000].includes(+v.toPrecision(3))?fmt0(v)+(v<1?'':'')+' %':''}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${pct(c.parsed.y)} at Δt ${c.parsed.x.toPrecision(3)} s`}},
      annotation:{annotations:{five:{type:'line',yMin:5,yMax:5,borderColor:'#1e8449',borderWidth:1.2,borderDash:[6,4],
        label:{display:true,content:'5 %',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}}}}}}
});
function updAdj(){
  const M=D.pipes[sModel.value], mode=sMode.value, dt=DTS[+sDt.value];
  document.getElementById('vDt').textContent=dt+' s';
  adjChart.data.datasets[0].data=GRID.map(t=>({x:t,y:Math.max(0.1,100*stats(M,t,'length').max)}));
  adjChart.data.datasets[1].data=GRID.map(t=>({x:t,y:Math.max(0.1,100*stats(M,t,'wave').max)}));
  const s=stats(M,dt,mode);
  adjChart.data.datasets[2].data=[{x:dt,y:Math.max(0.1,100*s.max)}];
  adjChart.update('none');
  document.getElementById('rMax').innerHTML=pct(100*s.max);
  document.getElementById('rMean').innerHTML=pct(100*s.mean);
  document.getElementById('rRms').innerHTML=pct(100*s.rms);
  const w=s.d[s.worst];
  document.getElementById('rWorst').innerHTML=w.id+' ('+fmt1(w.L)+' m)';
  document.getElementById('rReach').innerHTML=fmt0(s.reaches);
  const s0=stats(M,0.1,mode);
  document.getElementById('rCost').innerHTML=fmt0((s.reaches/dt)/(s0.reaches/0.1))+' <small>×</small>';
  document.getElementById('adjRows').innerHTML=s.d.map(p=>'<tr><td>'+p.id+'</td><td class="num">'+p.L.toLocaleString('en-US',{minimumFractionDigits:1,maximumFractionDigits:1})+
    '</td><td class="num">'+fmt0(p.a)+'</td><td class="num">'+fmt0(p.n)+'</td><td class="num">'+(mode==='length'?fmt1(p.Lm)+' m':fmt0(p.am)+' m/s')+
    '</td><td class="num">'+(p.adj>=0?'+':'−')+pct(Math.abs(100*p.adj))+'</td></tr>').join('');
}
[sModel,sMode,sDt].forEach(s=>s.addEventListener('input',updAdj));updAdj();

/* ---------- CHART 2 : results against the time step ---------- */
const sModel2=document.getElementById('sModel2'), sDt2=document.getElementById('sDt2');
const R=D.results, REF=D.ref, RDT=[0.2,0.1,0.05,0.02,0.01,0.005,0.002];
const pick=(m,mode)=>RDT.map(dt=>R.find(r=>r.model===m&&r.mode===mode&&r.dt===dt));
const xLog={type:'logarithmic',min:0.0015,max:0.25,reverse:true,title:{display:true,text:'Time step Δt (s, log scale, finer to the right)',font:TTL},grid:{color:'#eef2f5'},
  ticks:{font:{family:FF,size:11},callback:v=>[0.002,0.005,0.01,0.02,0.05,0.1,0.2].includes(+v.toPrecision(3))?String(+v.toPrecision(3)):''}};
function mkRes(cv,key,ref,ymin,ymax,ylab,extra){
  return new Chart(cv,{
    data:{datasets:[
      {type:'line',label:'Adjust length',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:4,order:2},
      {type:'line',label:'Adjust wave speed',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.2,pointRadius:4,order:3},
      {type:'scatter',label:'Selected step',data:[],backgroundColor:'#6b4f9e',borderColor:'#fff',borderWidth:2,pointRadius:8,order:1}
    ]},
    options:{responsive:true,maintainAspectRatio:false,animation:false,
      scales:{x:xLog,y:{type:'linear',min:ymin,max:ymax,title:{display:true,text:ylab,font:TTL},...AX}},
      plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},
        tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt2(c.parsed.y)} m at Δt ${c.parsed.x} s`}},
        annotation:{annotations:Object.assign({ref:{type:'line',yMin:ref,yMax:ref,borderColor:'#7f8c8d',borderWidth:1.5,borderDash:[6,4],
          label:{display:true,content:'reference '+fmt2(ref)+' m',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(127,140,141,0.9)'}}},extra||{})}}}
  });
}
const resMax=mkRes(document.getElementById('resMaxChart'),'line_max',REF.line_max,80,130,'Highest head on the line (m)');
const resMin=mkRes(document.getElementById('resMinChart'),'line_min',REF.line_min,-6,14,'Lowest head on the line (m)',
  {crit:{type:'line',yMin:PMIN,yMax:PMIN,borderColor:'#1e8449',borderWidth:1.5,borderDash:[2,3],
    label:{display:true,content:'+3.0 m design minimum',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}}});
const sCrit2=document.getElementById('sCrit2');
const badge=(v,c)=>v>=c?'<span class="badge good">pass</span>':'<span class="badge bad">fail</span>';
function updRes(){
  const m=sModel2.value, i=+sDt2.value, L=pick(m,'length'), A=pick(m,'wave'), crit=+sCrit2.value;
  document.getElementById('vCrit2').textContent=sgn(crit,1)+' m';
  const ca=resMin.options.plugins.annotation.annotations.crit; ca.yMin=crit; ca.yMax=crit; ca.label.content=sgn(crit,1)+' m design minimum';
  resMax.data.datasets[0].data=L.map(r=>({x:r.dt,y:r.line_max}));
  resMax.data.datasets[1].data=A.map(r=>({x:r.dt,y:r.line_max}));
  resMin.data.datasets[0].data=L.map(r=>({x:r.dt,y:r.line_min}));
  resMin.data.datasets[1].data=A.map(r=>({x:r.dt,y:r.line_min}));
  resMax.data.datasets[2].data=[{x:L[i].dt,y:L[i].line_max},{x:A[i].dt,y:A[i].line_max}];
  resMin.data.datasets[2].data=[{x:L[i].dt,y:L[i].line_min},{x:A[i].dt,y:A[i].line_min}];
  resMax.update('none');resMin.update('none');
  const PP=D.pipes[m];
  document.getElementById('rAdj2').innerHTML=pct(100*stats(PP,RDT[i],'length').max)+' / '+pct(100*stats(PP,RDT[i],'wave').max);
  document.getElementById('rMax2').innerHTML=fmt1(L[i].line_max)+' / '+fmt1(A[i].line_max)+' <small>m</small>';
  document.getElementById('rEmax2').innerHTML=sgn(L[i].line_max-REF.line_max,1)+' / '+sgn(A[i].line_max-REF.line_max,1)+' <small>m</small>';
  document.getElementById('rMin2').innerHTML=sgn(L[i].line_min,2)+' / '+sgn(A[i].line_min,2)+' <small>m</small>';
  document.getElementById('rEmin2').innerHTML=sgn(L[i].line_min-REF.line_min,2)+' / '+sgn(A[i].line_min-REF.line_min,2)+' <small>m</small>';
  document.getElementById('rVer2').innerHTML=badge(L[i].line_min,crit)+' '+badge(A[i].line_min,crit);
}
[sModel2,sDt2,sCrit2].forEach(s=>s.addEventListener('input',updRes));updRes();

/* ---------- CHART 3 : grid convergence ---------- */
const G=D.grid, sGrid=document.getElementById('sGrid'), sTol=document.getElementById('sTol');
const xN={type:'logarithmic',min:24,max:1200,title:{display:true,text:'Reaches N on the 12 km main (log scale)',font:TTL},grid:{color:'#eef2f5'},
  ticks:{font:{family:FF,size:11},callback:v=>[30,60,120,240,480,960].includes(Math.round(v))?String(Math.round(v)):''},
  afterBuildTicks:ax=>{ax.ticks=[30,60,120,240,480,960].map(v=>({value:v}));}};
const gMin=new Chart(document.getElementById('gridMinChart'),{
  data:{datasets:[
    {type:'line',label:'Vessel: lowest head (m)',data:G.map(r=>({x:r.N,y:r.ves_min})),borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.2,pointRadius:4,yAxisID:'y',order:2},
    {type:'line',label:'Flywheel: lowest head (m, right)',data:G.map(r=>({x:r.N,y:r.fly_min})),borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.2,pointRadius:4,yAxisID:'y1',order:3},
    {type:'scatter',label:'Your run',data:[],backgroundColor:'#6b4f9e',borderColor:'#fff',borderWidth:2,pointRadius:8,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:xN,y:{type:'linear',min:4.0,max:5.0,position:'left',title:{display:true,text:'Vessel case (m)',font:TTL},...AX},
            y1:{type:'linear',min:9.0,max:10.0,position:'right',title:{display:true,text:'Flywheel case (m)',font:TTL},grid:{drawOnChartArea:false},ticks:{font:{family:FF,size:11}}}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','').replace(' (m, right)','')}: ${fmt2(c.parsed.y)} m at N = ${Math.round(c.parsed.x)}`}}}}
});
const gMax=new Chart(document.getElementById('gridMaxChart'),{
  data:{datasets:[
    {type:'line',label:'Unprotected max, vapour cavity model (m)',data:G.map(r=>({x:r.N,y:r.un_max})),borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:2.2,pointRadius:4,order:2},
    {type:'line',label:'Unprotected max, gas cavity model (m)',data:G.map(r=>({x:r.N,y:r.un_max_dgcm})),borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:2.2,borderDash:[6,4],pointRadius:4,order:3}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:xN,y:{type:'linear',min:150,max:200,title:{display:true,text:'Highest head on the line (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at N = ${Math.round(c.parsed.x)}`}},
      annotation:{annotations:{lim:{type:'line',yMin:163.4,yMax:163.4,borderColor:'#6b4f9e',borderWidth:1.2,borderDash:[4,4],
        label:{display:true,content:'PN16 rating ≈ 163 m',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}}}}}}
});
function updGrid(){
  const i=+sGrid.value, tol=+sTol.value, r=G[i], f=G[i+1];
  document.getElementById('vTol').textContent=fmt2(tol)+' m';
  gMin.data.datasets[2].data=[{x:r.N,y:r.ves_min}];gMin.update('none');
  document.getElementById('rG1').innerHTML=sgn(r.ves_min,2)+' <small>m</small>';
  if(!f){
    ['rG2','rG3','rG4'].forEach(k=>document.getElementById(k).innerHTML='<small>no finer run</small>');
    document.getElementById('rG5').innerHTML='<span class="badge warn">halve once more to prove it</span>';return;
  }
  const ch=f.ves_min-r.ves_min, ex=2*f.ves_min-r.ves_min;
  document.getElementById('rG2').innerHTML=sgn(f.ves_min,2)+' <small>m</small>';
  document.getElementById('rG3').innerHTML=sgn(ch,2)+' <small>m</small>';
  document.getElementById('rG4').innerHTML=sgn(ex,2)+' <small>m</small>';
  document.getElementById('rG5').innerHTML=Math.abs(ch)<=tol+1e-9?'<span class="badge good">converged within '+fmt2(tol)+' m</span>':'<span class="badge warn">not converged: halve again</span>';
}
[sGrid,sTol].forEach(s=>s.addEventListener('input',updGrid));updGrid();

/* ---------- CHART 4 : run duration ---------- */
const U=D.duration, sDur=document.getElementById('sDur'), TLA=2*12000/1050;
const durChart=new Chart(document.getElementById('durChart'),{
  data:{datasets:[
    {type:'line',label:'Head at the pump (m)',data:U.t.map((t,k)=>({x:t,y:U.pump[k]})),borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2,pointRadius:0,order:3},
    {type:'line',label:'Head at 6 km (m)',data:U.t.map((t,k)=>({x:t,y:U.mid[k]})),borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:1.6,pointRadius:0,order:4},
    {type:'line',label:'Line maximum so far (m)',data:U.t.map((t,k)=>({x:t,y:U.env_max[k]})),borderColor:'#c0392b',backgroundColor:'#c0392b',borderWidth:1.4,borderDash:[6,4],pointRadius:0,order:2},
    {type:'line',label:'Line minimum so far (m)',data:U.t.map((t,k)=>({x:t,y:U.env_min[k]})),borderColor:'#1e8449',backgroundColor:'#1e8449',borderWidth:1.4,borderDash:[6,4],pointRadius:0,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:400,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:0,max:130,title:{display:true,text:'Head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8}},tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{
        unseen:{type:'box',xMin:90,xMax:400,backgroundColor:'rgba(127,140,141,0.13)',borderWidth:0},
        end:{type:'line',xMin:90,xMax:90,borderColor:'#6b4f9e',borderWidth:1.6,label:{display:true,content:'end of run',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(107,79,158,0.85)'}},
        tla:{type:'line',xMin:TLA,xMax:TLA,borderColor:'#7f8c8d',borderWidth:1,borderDash:[3,3],label:{display:true,content:'2L/a',position:'end',font:LBL,color:'#fff',backgroundColor:'rgba(127,140,141,0.9)'}}
      }}}}
});
function updDur(){
  const T=+sDur.value; document.getElementById('vDur').textContent=T+' s';
  const A=durChart.options.plugins.annotation.annotations; A.unseen.xMin=T; A.end.xMin=T; A.end.xMax=T; durChart.update('none');
  let k=0; for(let j=0;j<U.t.length;j++){ if(U.t[j]<=T+1e-9) k=j; }
  const mn=U.env_min[k], mx=U.env_max[k], miss=U.final_max-mx;
  document.getElementById('rD1').innerHTML=fmt1(T/TLA)+' <small>×</small>';
  document.getElementById('rD2').innerHTML=sgn(mn,2)+' <small>m</small>';
  document.getElementById('rD3').innerHTML=fmt1(mx)+' <small>m</small>';
  document.getElementById('rD4').innerHTML=fmt1(Math.max(0,miss))+' <small>m</small>';
  document.getElementById('rD5').innerHTML=(miss<=0.05&&mn<=U.final_min+0.05)?'<span class="badge good">full envelope captured</span>':
    (mn>U.final_min+0.05?'<span class="badge bad">misses the minimum</span>':'<span class="badge bad">misses the maximum</span>');
}
sDur.addEventListener('input',updDur);updDur();
window.addEventListener('load',function(){try{[adjChart,resMax,resMin,gMin,gMax,durChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: the method of characteristics, the Courant condition, interpolation and wave-speed adjustment, and the Joukowsky relation.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, the vessel design and the verified MOC solver used throughout this article.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation, &ldquo;Transient Time Step Options Dialog Box&rdquo;: time step, Max, Mean and RMS Adjustment, Adjust (Length or Wave speed), Adjustment Type, Use Custom Time Step and the excessive-adjustment warning.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation, &ldquo;Selection of the Time Step&rdquo;: why the time step forces adjustments, the absence of a fixed limit, and sensitivity testing with a smaller step.</li>
  <li>Chaudhry, M.H. <em>Applied Hydraulic Transients</em>, 3rd ed. Springer, 2014: discretisation of pipe networks, wave-speed adjustment and the accuracy of characteristic methods.</li>
  <li>Bergant, A., Simpson, A.R. &amp; Tijsseling, A.S. &ldquo;Water hammer with column separation: a historical review.&rdquo; <em>Journal of Fluids and Structures</em>, 22(2), 2006: vapour and gas cavity models and why collapse peaks depend on the model and the grid.</li>
  <li>Simpson, A.R. &amp; Bergant, A. &ldquo;Numerical comparison of pipe-column-separation models.&rdquo; <em>Journal of Hydraulic Engineering</em>, 120(3), 1994: grid sensitivity of the discrete vapour cavity model.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: line packing and the effect of friction on the transient peak.</li>
  <li>Karney, B.W. &amp; Ghidaoui, M.S. &ldquo;Flexible discretization algorithm for fixed-grid MOC in pipelines.&rdquo; <em>Journal of Hydraulic Engineering</em>, 123(11), 1997: the errors introduced by wave-speed adjustment and interpolation, and ways to limit them.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #HydraulicTransients #BentleyHAMMER #OpenFlowsHAMMER #TimeStep #WaveSpeedAdjustment #CourantCondition #MethodOfCharacteristics #GridConvergence #ModelVerification #RunDuration #Joukowsky #LinePacking #ColumnSeparation #SurgeVessel #PumpTrip #TransmissionMain #DuctileIron #PumpStation #TransientAnalysis #HydraulicModelling #Skeletonization #PipelineDesign #WaterEngineering</div>
"""

import json, os, math
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'analyst.json')))['s08']
DATA = {'pipes': {'raw': _A['raw'], 'clean': _A['clean']}, 'results': _A['results'], 'ref': _A['ref'], 'grid': _A['grid'],
        'duration': {k: _A['duration'][k] for k in ('t', 'pump', 'mid', 'env_min', 'env_max', 'final_min', 'final_max', 't_min', 't_max')}}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

def _row(p):
    import math
    L, a = p[2], p[3]
    n1 = max(1, int(math.floor(L/(a*0.1) + 0.5))); n2 = max(1, int(math.floor(L/(a*0.005) + 0.5)))
    la = (n1*a*0.1 - L)/L*100; wa = (L/(n1*0.1) - a)/a*100
    f = lambda v: ('+' if v >= 0 else '&minus;') + ('{:,.0f}'.format(abs(v)) if abs(v) >= 100 else '%.1f' % abs(v)) + '&nbsp;%'
    return ('    <tr><td>%s</td><td>%s</td><td class="num">%s</td><td class="num">%s</td><td class="num">%.4f</td><td class="num">%d</td>'
            '<td class="num">%s</td><td class="num">%s</td><td class="num">%s</td></tr>') % (
        p[0], p[1], '{:,.1f}'.format(L), '{:,.0f}'.format(a), L/a, n1, f(la), f(wa), '{:,}'.format(n2))
RAWROWS = '\n'.join(_row(p) for p in _A['raw'])
def _sg(v): return ('+' if v >= 0 else '&minus;') + '%.2f' % abs(v)
RESROWS = '\n'.join('    <tr><td class="num">%s</td><td class="num">%s</td><td class="num">%s</td><td class="num">%.2f</td><td class="num">%s</td><td class="num">%.2f</td></tr>' % (
    dt, '{:,}'.format(L['reaches']), _sg(L['line_min']), L['line_max'], _sg(W['line_min']), W['line_max'])
    for dt in (0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002)
    for L in [next(r for r in _A['results'] if r['model'] == 'raw' and r['mode'] == 'length' and r['dt'] == dt)]
    for W in [next(r for r in _A['results'] if r['model'] == 'raw' and r['mode'] == 'wave' and r['dt'] == dt)])
GRIDROWS = '\n'.join('    <tr><td class="num">%d</td><td class="num">%.0f</td><td class="num">%.3f</td><td class="num">%s</td><td class="num">%.2f</td><td class="num">%s</td><td class="num">%.1f</td><td class="num">%.1f</td></tr>' % (
    r['N'], r['dx'], r['dt'], _sg(r['ves_min']), r['ves_max'], _sg(r['fly_min']), r['un_max'], r['un_max_dgcm']) for r in _A['grid'])
J0, J5 = _A['joukowsky']['cases']
JTH = _A['joukowsky']['theory']
JROWS = '\n'.join([
    '    <tr><td>Rise at the valve, instant closure (first step)</td><td class="num">%.1f&nbsp;m</td><td class="num">%.1f&nbsp;m</td><td>from 45.8&nbsp;m to %.1f&nbsp;m in one step</td></tr>' % (JTH, J0['h_first'] - 45.8, J0['h_first']),
    '    <tr><td>Head at the valve, 5&nbsp;s closure, just after closure</td><td class="num">about %.0f&nbsp;m</td><td class="num">%.1f&nbsp;m</td><td>closure well inside 2L/a, so the full Joukowsky rise plus a little line packing</td></tr>' % (45.8 + JTH, J5['h_after']),
    '    <tr><td>Peak at the valve, instant closure</td><td class="num">&ge; %.1f&nbsp;m</td><td class="num">%.1f&nbsp;m at %.1f&nbsp;s</td><td>Joukowsky plus line packing, just before the reflection returns at 2L/a = 22.9&nbsp;s</td></tr>' % (45.8 + JTH, J0['peak'], J0['t_peak']),
    '    <tr><td>Peak at the valve, 5&nbsp;s closure</td><td class="num">&ge; %.1f&nbsp;m</td><td class="num">%.1f&nbsp;m at %.1f&nbsp;s</td><td>slightly lower and later: the rise is built over 5&nbsp;s instead of in one step</td></tr>' % (45.8 + JTH, J5['peak'], J5['t_peak'])])
DU = _A['duration']
REPL = {'__RAWROWS__': RAWROWS, '__RESROWS__': RESROWS, '__GRIDROWS__': GRIDROWS, '__JROWS__': JROWS, '__JTH__': '%.1f' % JTH,
        '__REFADJ__': '%.1f' % max(abs((L/(max(1, math.floor(L/(a*0.0005) + 0.5))*0.0005) - a)/a)*100 for (_i, _d, L, a) in _A['raw']),
        '__VDROP__': '%.2f' % (_A['grid'][0]['ves_min'] - _A['grid'][-1]['ves_min']),
        '__DGLO__': '%.0f' % min(r['un_max_dgcm'] for r in _A['grid']), '__DGHI__': '%.0f' % max(r['un_max_dgcm'] for r in _A['grid']),
        '__TMIN__': '%.1f' % DU['t_min'], '__TMAX__': '%.0f' % DU['t_max'], '__TMINR__': '%.0f' % (DU['t_min'] + 0.4), '__TMAXR__': '%.0f' % (DU['t_max'] + 0.4)}
for k, v in REPL.items():
    BODY = BODY.replace(k, v)

SPEC = dict(
    slug='surge-model-time-step-convergence', cat='surge', mins=23,
    date_iso='2026-11-19', date_human='November 2026', date_ar='نوفمبر 2026',
    title='Is Your HAMMER Run Right? Time Step, Wave-Speed Adjustment, Convergence and Run Duration',
    reg_title='Is Your HAMMER Run Right? Time Step, Wave-Speed Adjustment, Convergence and Run Duration',
    reg_tag='Surge Analysis · Model Checking · Time Step',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Model Checking &middot; Time Step',
    desc='How to check a surge model before trusting it: why one time step forces length or wave-speed adjustments, what they did to a 12 km DN800 main, cleaning short pipes, halving the step, run duration and the Joukowsky test, with four interactive charts and the Bentley HAMMER settings.',
    og_desc='On a 12 km DN800 main with a 2.4 m meter spool, a 0.1 s time step with wave-speed adjustment reported a 90 m maximum against a converged 119.3 m, and a 90 s run missed the upsurge entirely because it arrives at 101 s.',
    ld_desc='Checking a hydraulic transient model: time step and wave-speed or length adjustment, model cleaning, grid convergence, run duration and the Joukowsky test, worked on a 12 km DN800 main with the Bentley HAMMER settings.',
    img_alt='Pump station and a long blue transmission main in a desert trench, with short spools and a valve chamber near the station, a fading grid of characteristic lines above the pipe, and a stopwatch',
    en_tag='Surge &amp; Transient Analysis &middot; Model Checking',
    en_title='Is Your HAMMER Run Right? Time Step, Wave-Speed Adjustment, Convergence and Run Duration',
    en_excerpt='A 12 km DN800 main imported with a <strong>2.4 m flowmeter spool</strong>, run at 0.1 s with wave-speed adjustment, reported a maximum of <strong>90.0 m</strong>; the converged answer is <strong>119.3 m</strong>. At 0.05 s it turned a passing design into a failing one, and a 90 s run missed the upsurge completely because it arrives at 101 s. The five checks we make before any surge result leaves the office: adjustment pipe by pipe, cleaning the model, halving the step, run duration and the Joukowsky test, with four interactive charts and the HAMMER settings.',
    en_search='surge model verification HAMMER time step wave speed adjustment length adjustment Max Adjustment Mean RMS Transient Time Step Options custom time step Courant condition method of characteristics grid convergence halve time step run duration envelope Joukowsky test line packing short pipes skeletonization Skelebrator model cleaning flowmeter spool column separation collapse peak vapour cavity gas cavity transient analysis pump trip surge vessel 12 km DN800 ductile iron Bentley OpenFlows HAMMER',
    ar_title='هل نتائج HAMMER صحيحة؟ الخطوة الزمنية وتعديل سرعة الموجة والتقارب ومدة التشغيل',
    ar_excerpt='خط بطول ١٢ كم وقطر ٨٠٠ مم أُدخل إلى النموذج ومعه وصلة عداد بطول <strong>٢٫٤ م</strong>، وعند تشغيله بخطوة زمنية ٠٫١ ثانية مع تعديل سرعة الموجة أعطى ضغطاً أقصى قدره <strong>٩٠٫٠ م</strong>، بينما القيمة الصحيحة <strong>١١٩٫٣ م</strong>. وعند ٠٫٠٥ ثانية حوّل تصميماً ناجحاً إلى تصميم فاشل، كما أن تشغيلاً مدته ٩٠ ثانية لم يلتقط الارتفاع الأقصى لأنه يصل بعد ١٠١ ثانية. خمس مراجعات نجريها قبل اعتماد أي نتيجة، مع أربعة رسوم تفاعلية وإعدادات برنامج HAMMER.',
    ar_search='التحقق من نموذج المطرقة المائية الطرق المائي الخطوة الزمنية تعديل سرعة الموجة تعديل الطول شرط كورانت طريقة الخطوط المميزة تقارب الشبكة مدة التشغيل معادلة جوكوفسكي الأنابيب القصيرة تبسيط النموذج انفصال عمود الماء خزان الحماية توقف المضخة بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
