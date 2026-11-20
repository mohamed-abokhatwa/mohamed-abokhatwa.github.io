# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A surge study is judged by its report, and reviewers send reports back for the same few reasons: they cannot see the model basis, the profile is missing, results are shown only at the pump, or the protection is described without the settings anyone needs to build it. Here is why the profile matters. The 12&nbsp;km reference main, with the vessel that protects it on a flat profile (3.5&nbsp;m&sup3; of gas in a 20&nbsp;m&sup3; shell), was rerun on an undulating profile with two high points. The pressure history at the pump still looks healthy, never below <strong>+4.8&nbsp;m</strong>. Along the line the pressure falls to <strong>&minus;5.8&nbsp;m</strong> at the 7.2&nbsp;km high point, and 8.5&nbsp;km of main is below the +3.0&nbsp;m criterion. A report that showed the pump history, or the envelope as head rather than pressure, would have passed it. This article sets out what we put in a surge study, how we present it, and the checklist we use when reviewing someone else's.</p>

<h2 id="purpose">1 &middot; What the report has to do</h2>
<p>A surge study supports decisions that are expensive to change later: the protection type and size, the pipe classes, the pump and valve specifications, the station layout and the operating rules [1][2]. Its report has three readers, and each needs something different.</p>
<ul class="clean">
  <li><strong>The reviewer</strong> needs to reproduce the reasoning: the model basis, the data and their sources, the assumptions, the scenarios, and evidence that the model was checked.</li>
  <li><strong>The designers and suppliers</strong> need the outputs: device sizes and settings, pressure classes, valve closure times, pump inertia requirements and interlocks.</li>
  <li><strong>The operator</strong> needs the rules: what must never be done, how to restart after a trip, how to maintain the protection.</li>
</ul>
<p>We write the report so that each reader can find their part without reading the rest, and so that every number in the conclusions can be traced back to a run.</p>

<h2 id="structure">2 &middot; The structure we use</h2>
<p>Our surge reports follow the same order on every project. The order matters: the basis and the checks come before any result, so that a reader knows what the results are worth.</p>
<div class="tbl-wrap"><table>
  <caption>Surge study report: contents and what a reviewer looks for in each part</caption>
  <thead><tr><th>Part</th><th>Contents</th><th>What the reviewer looks for</th></tr></thead>
  <tbody>
    <tr><td>Summary</td><td>System, governing event, recommended protection with sizes, key limits met, open items</td><td>One page; numbers match the body; open items are named</td></tr>
    <tr><td>System description</td><td>Route, profile, pipe materials and classes, pumps, valves, reservoirs, operating modes</td><td>A profile drawing with chainages and elevations; the weakest component classes</td></tr>
    <tr><td>Criteria</td><td>Maximum and minimum limits and their sources: EN 805 terms, product standards, owner's limits</td><td>Each limit named and referenced, in EN 805 terms where they apply [5] (see <a href="surge-envelope-pipe-pressure-limits.html">the pipe's real limits</a>)</td></tr>
    <tr><td>Model basis</td><td>Software and version, network, wave speeds, friction, pump data, valve data, cavity model, time step, run duration</td><td>The data register and assumptions register; the model checks</td></tr>
    <tr><td>Scenarios</td><td>The matrix of events, operating points and protection states</td><td>Occasional and recurring events; protection out of service; the governing case justified</td></tr>
    <tr><td>Results without protection</td><td>Envelopes and histories for the governing events</td><td>Why protection is needed, and where</td></tr>
    <tr><td>Protection design</td><td>Options compared, the selected scheme, its sizing runs</td><td>A device schedule complete enough to procure and build</td></tr>
    <tr><td>Results with protection</td><td>Envelopes along the whole line, histories at critical points, extreme tables</td><td>Pressure, not head; every high point; margins against each limit</td></tr>
    <tr><td>Sensitivity</td><td>Wave speed, pump data, device settings, model options</td><td>Whether the decision survives the uncertainty</td></tr>
    <tr><td>Operation</td><td>Interlocks, start and stop sequences, restart after a trip, maintenance of the protection</td><td>Rules an operator can follow</td></tr>
    <tr><td>Appendices</td><td>Model files, input listings, run log, data sources</td><td>Enough to rerun the study</td></tr>
  </tbody>
</table></div>

<h2 id="basis">3 &middot; Model basis: the data and assumptions registers</h2>
<p>The single most useful table in a surge report is the one that lists every input with its source and status. Reviewers trust a model whose weak points are written down, and distrust one where they have to dig for them. For the reference main at tender stage, ours reads like this:</p>
<div class="tbl-wrap"><table>
  <caption>Data and assumptions register, reference main (extract)</caption>
  <thead><tr><th>Input</th><th>Value used</th><th>Source</th><th>Status</th><th>Sensitivity tested</th></tr></thead>
  <tbody>
    <tr><td>Profile</td><td>Ground levels at 7 points, 0&ndash;12&nbsp;m</td><td>Route survey</td><td><span class="badge good">confirmed</span></td><td>&ndash;</td></tr>
    <tr><td>Pipe</td><td>DN800 ductile iron, C25 barrel, PN16 fittings</td><td>Design drawings</td><td><span class="badge good">confirmed</span></td><td>&ndash;</td></tr>
    <tr><td>Wave speed</td><td>1,050&nbsp;m/s</td><td>Korteweg, K9 wall, cement lining</td><td><span class="badge warn">calculated</span></td><td>&plusmn;10&nbsp;% (see <a href="wave-speed-surge-analysis.html">wave speed</a>)</td></tr>
    <tr><td>Friction</td><td>40.2&nbsp;m at 0.70&nbsp;m&sup3;/s</td><td>Steady-state model</td><td><span class="badge warn">calculated</span></td><td>new and aged pipe</td></tr>
    <tr><td>Pump inertia</td><td>44&nbsp;kg&middot;m&sup2; total</td><td>Correlation (HAMMER calculator)</td><td><span class="badge bad">assumed</span></td><td>25 to 88&nbsp;kg&middot;m&sup2;</td></tr>
    <tr><td>Pump characteristic</td><td>N<sub>s</sub> 46, closest library curve 25</td><td>Duty point</td><td><span class="badge bad">assumed</span></td><td>curve 94 as bracket</td></tr>
    <tr><td>Check valve</td><td>Ideal, closes at zero flow</td><td>None yet</td><td><span class="badge bad">assumed</span></td><td>real closure once selected</td></tr>
    <tr><td>Vessel gas law</td><td>Polytropic, n = 1.2</td><td>Standard practice</td><td><span class="badge warn">calculated</span></td><td>n = 1.0 and 1.4</td></tr>
    <tr><td>Cavity model</td><td>Vapour cavity; gas cavity as check</td><td>Model option</td><td><span class="badge warn">calculated</span></td><td>both models on cavitating runs</td></tr>
    <tr><td>Time step</td><td>Suggested step, length adjustment &lt; 5&nbsp;%</td><td>Model check</td><td><span class="badge good">confirmed</span></td><td>halved step</td></tr>
    <tr><td>Run duration</td><td>150&nbsp;s</td><td>Model check</td><td><span class="badge good">confirmed</span></td><td>extended to 225&nbsp;s</td></tr>
  </tbody>
</table></div>
<p>Each &ldquo;assumed&rdquo; line is an open item in the summary and, where the decision depends on it, a hold point in a specification. The model checks themselves (time step, adjustment, halved step, run duration, Joukowsky test) are set out in <a href="surge-model-time-step-convergence.html">Is your HAMMER run right?</a>, and the pump data questions in <a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip</a>.</p>

<h2 id="scenarios">4 &middot; The scenario matrix</h2>
<p>A report that runs one pump trip has not shown that the trip governs. We lay the scenarios out as a matrix of events against operating states and protection states [1][3]:</p>
<div class="tbl-wrap"><table>
  <caption>Scenario matrix for a pumped transmission main (reference main as the example)</caption>
  <thead><tr><th>Event</th><th>Type</th><th>Operating states</th><th>Protection states</th><th class="num">Runs</th></tr></thead>
  <tbody>
    <tr><td>Power failure, all pumps</td><td>occasional</td><td>maximum flow, minimum flow, maximum reservoir level</td><td>designed, vessel isolated, low gas</td><td class="num">9</td></tr>
    <tr><td>Single pump trip, others running</td><td>occasional</td><td>maximum flow</td><td>designed</td><td class="num">1</td></tr>
    <tr><td>Normal pump start</td><td>recurring</td><td>first pump, last pump</td><td>designed</td><td class="num">2</td></tr>
    <tr><td>Normal pump stop</td><td>recurring</td><td>last pump, one of several</td><td>designed</td><td class="num">2</td></tr>
    <tr><td>Line valve closure</td><td>occasional</td><td>maximum flow</td><td>designed</td><td class="num">1</td></tr>
    <tr><td>Restart after a trip</td><td>occasional</td><td>line partly drained, vessel refilling</td><td>designed</td><td class="num">1</td></tr>
    <tr><td>Sensitivity on the governing case</td><td>&ndash;</td><td>wave speed &plusmn;10&nbsp;%, inertia range, curve bracket, gas law, halved step</td><td>designed</td><td class="num">8</td></tr>
  </tbody>
</table></div>
<p>That is 24 runs for a single main. Each is a scenario in the model with a clear name, and the report says which run governs each side of the envelope and why. The scenarios themselves are described in <a href="surge-scenarios-pump-stations.html">Surge Scenarios in Pumping Stations</a>; what matters here is that the matrix appears in the report, with the run that governs each limit marked.</p>

<h2 id="present-profile">5 &middot; Presenting the envelope: pressure along the profile</h2>
<p>The envelope is the most important figure in the report and the one most often drawn badly. Three rules:</p>
<ul class="clean">
  <li><strong>Plot pressure, or plot head together with the pipe profile.</strong> A minimum HGL of +20&nbsp;m tells the reader nothing on a line with a high point at +12&nbsp;m. A pressure envelope can be read directly against the limits.</li>
  <li><strong>Show the whole line</strong>, with every high point, knee and device chainage marked, and the limits drawn on the same axes.</li>
  <li><strong>Tabulate the extremes</strong> with their chainage, time and governing scenario, so the figure does not have to be read with a ruler.</li>
</ul>
<p>Here is the reference main of the surge series [6] laid on an undulating profile (high points of 10&nbsp;m at 2.5&nbsp;km and 12&nbsp;m at 7.2&nbsp;km), run three ways.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">The same trip shown as head and as pressure</div>
    <div class="fsub">Reference main on an undulating profile, all pumps tripping. Method-of-characteristics model with a vapour cavity model, 100&nbsp;m reaches, 150&nbsp;s. Head view: HGL envelopes with the pipe profile and the steady HGL. Pressure view: pressure head envelopes with the limits. Lengths counted on the 100&nbsp;m grid.</div>
  </div>
  <div class="chart-box"><canvas id="profChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Protection</label>
      <select id="sCase">
        <option value="0">No protection</option>
        <option value="1" selected>Flat-line vessel: 3.5 m³ gas, 20 m³ shell</option>
        <option value="2">Design vessel: 7.0 m³ gas, 30 m³ shell</option>
      </select>
      <div class="hint">The second is the vessel that passes on a flat profile.</div>
    </div>
    <div class="ctrl">
      <label>View</label>
      <select id="sView">
        <option value="head">Head (HGL) with the profile</option>
        <option value="pres" selected>Pressure head</option>
      </select>
      <div class="hint">Same results, two ways of drawing them.</div>
    </div>
    <div class="ctrl">
      <label>Units</label>
      <select id="sUnit">
        <option value="m" selected>metres</option>
        <option value="bar">bar</option>
      </select>
      <div class="hint">1&nbsp;bar = 10.21&nbsp;m.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Lowest pressure</div><div class="v" id="rMin">&ndash;</div></div>
    <div class="cell"><div class="k">Where</div><div class="v" style="font-size:15px;margin-top:6px;" id="rWhere">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest at the pump</div><div class="v" id="rPump">&ndash;</div></div>
    <div class="cell"><div class="k">Highest pressure</div><div class="v" id="rMax">&ndash;</div></div>
    <div class="cell"><div class="k">Line below +3.0 m</div><div class="v" id="rLen">&ndash;</div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;" id="rVer">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">With the flat-line vessel the head view looks reassuring: the minimum HGL never falls below +4.3&nbsp;m above datum, everywhere above the pipe on the chart. The pressure view shows what the head view hides: the pressure is &minus;5.2&nbsp;m at the 2.5&nbsp;km high point and &minus;5.8&nbsp;m at 7.2&nbsp;km. Switch to the design vessel and the lowest pressure is +3.2&nbsp;m at 2.5&nbsp;km. The pump reads +12.0&nbsp;m, nearly four times as much. The maximum is 89.9&nbsp;m at the pump, well inside the 136&nbsp;m project limit, because the larger gas volume also softens the upsurge.</p>

<h2 id="present-history">6 &middot; Presenting time histories: at the critical points</h2>
<p>Time histories show how an event develops: when the minimum arrives, whether it is a single dip or a sustained low, how fast the protection responds. They belong at the points that govern, not only at the pump. We always include the pump or vessel node, every high point that comes within a few metres of the criterion, and the point of the overall minimum and maximum.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Pressure history at a chosen report point</div>
    <div class="fsub">Same runs as above. The grey trace is the pump node for comparison. 150&nbsp;s runs, traces thinned for the page; readouts from the full runs.</div>
  </div>
  <div class="chart-box"><canvas id="histChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Report point</label>
      <select id="sPt">
        <option value="1">2.5 km: first high point</option>
        <option value="2">4.5 km: low point</option>
        <option value="3" selected>7.2 km: second high point</option>
        <option value="0">0 km: pump and vessel</option>
      </select>
      <div class="hint">Chainages of the report points in the model.</div>
    </div>
    <div class="ctrl">
      <label>Protection</label>
      <select id="sCase2">
        <option value="0">No protection</option>
        <option value="1" selected>Flat-line vessel: 3.5 m³ gas</option>
        <option value="2">Design vessel: 7.0 m³ gas</option>
      </select>
      <div class="hint">As in the profile chart.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Lowest here</div><div class="v" id="rHmin">&ndash;</div></div>
    <div class="cell"><div class="k">Highest here</div><div class="v" id="rHmax">&ndash;</div></div>
    <div class="cell"><div class="k">Lowest at the pump</div><div class="v" id="rH0">&ndash;</div></div>
    <div class="cell"><div class="k">Pump history alone says</div><div class="v" style="font-size:14px;margin-top:6px;" id="rSays">&ndash;</div></div>
    <div class="cell"><div class="k">This point says</div><div class="v" style="font-size:14px;margin-top:6px;" id="rTruth">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">At 7.2&nbsp;km the flat-line vessel holds the pressure below +3.0&nbsp;m for a long stretch of the first downsurge and reaches &minus;5.8&nbsp;m. The pump history for the same run never goes below +4.8&nbsp;m. A report showing only the pump would conclude the opposite of the truth.</p>

<h2 id="device-schedule">7 &middot; The device schedule</h2>
<p>The protection must be described completely enough to be specified, procured, installed and commissioned without going back to the model. For the design vessel on this profile:</p>
<div class="tbl-wrap"><table>
  <caption>Device schedule: hydropneumatic vessel at the pump station (example)</caption>
  <thead><tr><th>Item</th><th>Value</th><th>Basis</th></tr></thead>
  <tbody>
    <tr><td>Total shell volume</td><td>30&nbsp;m&sup3;</td><td>Largest gas volume 23.5&nbsp;m&sup3;, kept below 80&nbsp;% of the shell</td></tr>
    <tr><td>Gas volume at steady flow</td><td>7.0&nbsp;m&sup3;</td><td>Smallest gas volume giving +3.0&nbsp;m everywhere is __GREQ__&nbsp;m&sup3;; rounded up</td></tr>
    <tr><td>Gas pressure at steady flow</td><td>about 9.35&nbsp;bar absolute (95.3&nbsp;m)</td><td>85.0&nbsp;m at the vessel plus atmosphere</td></tr>
    <tr><td>Water volume at steady flow</td><td>23.0&nbsp;m&sup3;</td><td>Normal operating level for the level controls</td></tr>
    <tr><td>Connection</td><td>DN400 with differential orifice</td><td>Loss coefficient 2.0 out of the vessel, 10.0 into it</td></tr>
    <tr><td>Maximum pressure at the vessel</td><td>89.9&nbsp;m (8.8&nbsp;bar)</td><td>Design trip; vessel design pressure set above it, PN16</td></tr>
    <tr><td>Level and gas controls</td><td>High, normal and low levels; compressor or gas charging</td><td>To hold 7.0&nbsp;m&sup3; within a tolerance tested in the sensitivity runs</td></tr>
    <tr><td>Air valves at 2.5 and 7.2&nbsp;km</td><td>For filling and draining</td><td>Lowest pressures in the design trip +3.2 and +7.1&nbsp;m: they do not open in the trip</td></tr>
    <tr><td>Check valve</td><td>Fast-closing, non-slam</td><td>Reverse velocity at closure to be confirmed against the selected valve</td></tr>
  </tbody>
</table></div>
<p>Each figure in the schedule should point to the run that justifies it. A schedule that gives the vessel volume without the gas volume, pressure and connection loss cannot be built to the design; the <a href="surge-vessel.html">vessel sizing article</a> and the <a href="surge-vessel-differential-orifice.html">differential orifice article</a> show how sensitive the result is to each.</p>

<h2 id="operation">8 &middot; Operating rules and interlocks</h2>
<p>The protection only works if it is in service and set correctly, so the report ends with rules that go into the operating manual and the control philosophy:</p>
<ul class="clean">
  <li><strong>Permissives:</strong> no pump may start unless the vessel is in service, with level and gas volume within limits.</li>
  <li><strong>Vessel out of service:</strong> the main may not be pumped, or may be pumped only at a reduced flow shown by a run to be safe.</li>
  <li><strong>Start and stop sequences:</strong> pumps start and stop one at a time, at least a stated interval apart, and the line valve closure time is fixed by the run that shows it safe.</li>
  <li><strong>Restart after a trip:</strong> wait until the vessel has refilled and the column has settled; for a line that has drained, follow the filling procedure.</li>
  <li><strong>Maintenance:</strong> check gas volume and connection orifice at stated intervals, and record every trip with a fast pressure logger so the model can be checked against reality.</li>
</ul>

<h2 id="review">9 &middot; The reviewer's checklist</h2>
<p>This is the list we work through when reviewing a surge study. Tick what the report you are reviewing actually contains; the chart shows which parts are weak.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Surge study review: completeness by part</div>
    <div class="fsub">Each item carries a weight of 1, or 2 for items that on their own can invalidate a conclusion (marked &#9733;). Bars show the weighted share of each part that is present. A report with any &#9733; item missing goes back, whatever its total.</div>
  </div>
  <div class="chart-box" style="height:300px;"><canvas id="revChart"></canvas></div>
  <div id="revList" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:6px 18px;margin:14px 0 4px;font-size:14px;">
__CHECKS__
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Overall</div><div class="v" id="rTot">&ndash;</div></div>
    <div class="cell"><div class="k">&#9733; items missing</div><div class="v" id="rCrit">&ndash;</div></div>
    <div class="cell"><div class="k">Weakest part</div><div class="v" style="font-size:15px;margin-top:6px;" id="rWeak">&ndash;</div></div>
    <div class="cell"><div class="k">Decision</div><div class="v" style="font-size:15px;margin-top:6px;" id="rDec">&ndash;</div></div>
  </div>
</div>
<p class="fig-note">The ticks start at what a typical first submission contains in our experience: a model description, a pump trip at the pump node and a vessel volume. That scores 17&nbsp;%, with nine of the ten starred items missing. Nothing here is saved; reload the page to start again.</p>

<h2 id="send-back">10 &middot; Why studies are sent back</h2>
<p>In our reviews the same problems come up again and again. Most concern presentation and evidence rather than hydraulics:</p>
<ul class="clean">
  <li><strong>Results only at the pump.</strong> The critical point is almost always somewhere else on the line (sections 5 and 6).</li>
  <li><strong>Head plotted without the profile</strong>, so vacuum at a high point is invisible.</li>
  <li><strong>One scenario.</strong> No single pump trip, no start or stop, no protection-out-of-service case.</li>
  <li><strong>No model checks.</strong> No time step, adjustment, halved step or run duration in the report.</li>
  <li><strong>A peak that rests on cavity collapse</strong> accepted against a pressure rating.</li>
  <li><strong>Assumed pump data presented as fact</strong>, with no range tested.</li>
  <li><strong>A vessel without its gas volume, pressure or connection loss</strong>, so it cannot be built as modelled.</li>
  <li><strong>No operating rules</strong>, leaving the protection free to be isolated.</li>
  <li><strong>Limits without sources</strong>: &ldquo;PN16&rdquo; with no statement of PFA, PMA or the owner's criteria.</li>
</ul>

<h2 id="hammer-setup">11 &middot; Getting the report out of Bentley HAMMER</h2>
<p>Field names differ slightly between versions; these follow the current documentation [4].</p>
<ol>
  <li><strong>Name scenarios and alternatives</strong> as they will appear in the report&rsquo;s scenario matrix, so every figure can carry its scenario name.</li>
  <li><strong>Define profiles</strong> along the whole main with the ground or pipe level, and plot the <strong>maximum and minimum pressure envelopes</strong> for each governing scenario.</li>
  <li><strong>Set report points</strong> at the pump, the vessel and every high point before the run, and turn on <strong>Generate Animation Data</strong>, so histories exist where they are needed.</li>
  <li><strong>Export the extremes</strong> with their locations from the transient results tables, and build the extremes table from them rather than reading graphs.</li>
  <li><strong>Copy the calculation options</strong> into the model basis: time step, adjustment, run duration, friction method and vapour pressure.</li>
  <li><strong>Keep the run log</strong> with warnings, including any wave-speed or length adjustment warning, and say in the report how each was dealt with.</li>
  <li><strong>Archive the model</strong> with the report, with a list of scenarios and the run that supports each figure.</li>
</ol>

<h2 id="checklist">12 &middot; Checklist for the author</h2>
<ul class="clean">
  <li><strong>Summary</strong> with the governing event, the protection, the margins and the open items.</li>
  <li><strong>Profile drawing</strong> and the weakest component classes.</li>
  <li><strong>Limits named and referenced</strong>, owner's criteria separated from standards.</li>
  <li><strong>Data and assumptions registers</strong>, with every assumption tested or listed as open.</li>
  <li><strong>Model checks</strong> reported.</li>
  <li><strong>Scenario matrix</strong> with the governing run marked for each limit.</li>
  <li><strong>Pressure envelopes along the whole line</strong> and histories at the critical points.</li>
  <li><strong>Device schedule</strong> complete enough to build from.</li>
  <li><strong>Sensitivity</strong> showing that the decision survives the uncertainty.</li>
  <li><strong>Operating rules</strong> and interlocks.</li>
  <li><strong>Model files</strong> archived with the report.</li>
</ul>

<div class="callout green">
  <span class="lbl">Surge analysis practice series</span>
  <ol>
    <li><a href="surge-model-time-step-convergence.html">Is your HAMMER run right? Time step, adjustment and run duration</a></li>
    <li><a href="pump-trip-data-inertia-specific-speed.html">Pump data for a pump trip: inertia, specific speed and four-quadrant curves</a></li>
    <li><a href="surge-envelope-pipe-pressure-limits.html">Reading the surge envelope against the pipe's real limits</a></li>
    <li><strong>The surge study report: what to deliver and what a reviewer checks</strong></li>
  </ol>
  The protection devices themselves are covered in the <a href="choosing-surge-protection.html">surge protection design series</a>.
</div>
"""

CHECKS = [  # (part, text, critical, ticked at start)
    ('Basis', 'Profile drawing with chainages and elevations', True, False),
    ('Basis', 'Pipe materials, classes and weakest components', False, True),
    ('Basis', 'Limits named with their sources', True, False),
    ('Model', 'Data register with sources', False, True),
    ('Model', 'Assumptions register with status', True, False),
    ('Model', 'Time step, adjustment and halved-step check', True, False),
    ('Model', 'Run duration justified', False, False),
    ('Scenarios', 'Power failure at several operating points', True, False),
    ('Scenarios', 'Protection out of service', False, False),
    ('Scenarios', 'Recurring events (starts and stops)', False, False),
    ('Results', 'Pressure envelopes along the whole line', True, False),
    ('Results', 'Histories at high points and critical points', False, True),
    ('Results', 'Extremes table with chainage, time and scenario', False, False),
    ('Results', 'No acceptance resting on a collapse peak', True, False),
    ('Devices', 'Vessel volume, gas volume and pressure', True, True),
    ('Devices', 'Connection size and losses', False, False),
    ('Devices', 'Check valve and air valve requirements', False, False),
    ('Operation', 'Interlocks and permissives', True, False),
    ('Operation', 'Start, stop and restart sequences', False, False),
    ('Operation', 'Sensitivity showing the decision holds', True, False),
]
CHECKS_HTML = '\n'.join(
    '    <label style="display:flex;gap:8px;align-items:flex-start;cursor:pointer;"><input type="checkbox" id="c%d"%s style="margin-top:3px;"> <span><strong>%s:</strong> %s%s</span></label>' % (
        i, ' checked' if t else '', p, txt, ' &#9733;' if crit else '') for i, (p, txt, crit, t) in enumerate(CHECKS))

CHARTS = r"""
const D=__DATA__;
const CK=__CHECKS__;
const FF="'IBM Plex Sans', system-ui, sans-serif";
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:FF,size:11}}};
const TTL={family:FF,size:12,weight:'600'};
const LBL={size:10,family:FF};
const LEGF={family:FF,size:11.5};
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1), fmt2=v=>v.toFixed(2);
const sgn=(v,d)=>(v<-0.0049?'−':(v>0.0049?'+':''))+Math.abs(v).toFixed(d);
const M2B=10.21, PMIN=3.0, PRJ=136.0, VAP=-9.8;
const good=t=>'<span class="badge good">'+t+'</span>', bad=t=>'<span class="badge bad">'+t+'</span>', warn=t=>'<span class="badge warn">'+t+'</span>';
const X=D.x.map(x=>x/1000);
/* ---------- CHART 1 : profile ---------- */
const sCase=document.getElementById('sCase'), sView=document.getElementById('sView'), sUnit=document.getElementById('sUnit');
const hl=(v,txt,col,pos)=>({type:'line',yMin:v,yMax:v,borderColor:col,borderWidth:1.4,borderDash:[6,4],label:{display:true,content:txt,position:pos||'end',font:LBL,color:'#fff',backgroundColor:col}});
const profChart=new Chart(document.getElementById('profChart'),{
  data:{datasets:[
    {type:'line',label:'Maximum',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,order:2},
    {type:'line',label:'Minimum',data:[],borderColor:'#b9770e',backgroundColor:'#b9770e',borderWidth:2.4,pointRadius:0,order:1},
    {type:'line',label:'Steady HGL',data:[],borderColor:'#6b4f9e',backgroundColor:'#6b4f9e',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:3},
    {type:'line',label:'Pipe profile',data:[],borderColor:'#5d4037',backgroundColor:'rgba(93,64,55,0.18)',fill:'start',borderWidth:1.6,pointRadius:0,order:4}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:12,title:{display:true,text:'Chainage from the pump station (km)',font:TTL},...AX},
            y:{type:'linear',title:{display:true,text:'',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${sUnit.value==='bar'?fmt2(c.parsed.y)+' bar':fmt1(c.parsed.y)+' m'} at ${fmt1(c.parsed.x)} km`}},
      annotation:{annotations:{}}}}
});
const lenBelow=c=>c.pmin.filter(v=>v<PMIN).length*0.1;
function updProf(){
  const c=D.cases[+sCase.value], v=sView.value, u=sUnit.value, k=u==='bar'?1/M2B:1, un=u==='bar'?'bar':'m';
  const Y=a=>a.map((q,i)=>({x:X[i],y:+(q*k).toFixed(3)}));
  if(v==='head'){
    profChart.data.datasets[0].data=Y(c.hmax); profChart.data.datasets[1].data=Y(c.hmin);
    profChart.data.datasets[2].data=Y(D.hgl); profChart.data.datasets[3].data=Y(D.z);
    profChart.data.datasets[0].label='Maximum HGL'; profChart.data.datasets[1].label='Minimum HGL';
    profChart.options.scales.y.title.text=u==='bar'?'Head above datum (bar equivalent)':'Head above datum (m)';
    profChart.options.plugins.annotation.annotations={};
  } else {
    profChart.data.datasets[0].data=Y(c.pmax); profChart.data.datasets[1].data=Y(c.pmin);
    profChart.data.datasets[2].data=[]; profChart.data.datasets[3].data=[];
    profChart.data.datasets[0].label='Maximum pressure'; profChart.data.datasets[1].label='Minimum pressure';
    profChart.options.scales.y.title.text=u==='bar'?'Pressure (bar gauge)':'Pressure head (m)';
    profChart.options.plugins.annotation.annotations={des:hl(PMIN*k,'+3.0 m','rgba(30,132,73,0.85)','start'),prj:hl(PRJ*k,'136 m project max','rgba(107,79,158,0.85)','start'),
      vap:hl(VAP*k,'vapour','rgba(192,57,43,0.85)','start')};
  }
  profChart.options.scales.y.min=-15*k; profChart.options.scales.y.max=170*k;
  profChart.update('none');
  const sh=w=>u==='bar'?sgn(w/M2B,2):sgn(w,1);
  document.getElementById('rMin').innerHTML=sh(c.line_min)+' <small>'+un+'</small>'+(c.line_min<=VAP+0.05?' <small>(vapour)</small>':'');
  document.getElementById('rWhere').innerHTML=c.line_min<=VAP+0.05?'<small>vapour over '+fmt1(c.pmin.filter(q=>q<=VAP+0.05).length*0.1)+' km</small>':(c.at_min===0?'at the pump':'at '+fmt1(c.at_min/1000)+' km');
  document.getElementById('rPump').innerHTML=sh(c.pump_min)+' <small>'+un+'</small>';
  document.getElementById('rMax').innerHTML=(u==='bar'?fmt2(c.line_max/M2B):fmt1(c.line_max))+' <small>'+un+'</small>'+(c.line_min<=VAP+0.05?' <small>(cavitating)</small>':'');
  document.getElementById('rLen').innerHTML=fmt1(lenBelow(c))+' <small>km</small>';
  document.getElementById('rVer').innerHTML=c.line_min<=VAP+0.05?bad('vapour'):(c.line_min<PMIN?bad('below +3.0 m'):(c.line_max>PRJ?warn('over 136 m'):good('meets both limits')));
}
[sCase,sView,sUnit].forEach(s=>s.addEventListener('input',updProf));updProf();

/* ---------- CHART 2 : histories ---------- */
const sPt=document.getElementById('sPt'), sCase2=document.getElementById('sCase2');
const histChart=new Chart(document.getElementById('histChart'),{
  data:{datasets:[
    {type:'line',label:'Pressure head at the report point (m)',data:[],borderColor:'#1b4f72',backgroundColor:'#1b4f72',borderWidth:2.4,pointRadius:0,order:1},
    {type:'line',label:'Pressure head at the pump (m)',data:[],borderColor:'#7f8c8d',backgroundColor:'#7f8c8d',borderWidth:1.4,borderDash:[5,4],pointRadius:0,order:2}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'nearest',axis:'x',intersect:false},
    scales:{x:{type:'linear',min:0,max:150,title:{display:true,text:'Time after the trip (s)',font:TTL},...AX},
            y:{type:'linear',min:-15,max:170,title:{display:true,text:'Pressure head (m)',font:TTL},...AX}},
    plugins:{legend:{labels:{font:LEGF,usePointStyle:true,boxWidth:8,filter:(it,d)=>d.datasets[it.datasetIndex].data.length>0}},
      tooltip:{callbacks:{label:c=>`${c.dataset.label.replace(' (m)','')}: ${fmt1(c.parsed.y)} m at ${fmt1(c.parsed.x)} s`}},
      annotation:{annotations:{des:hl(PMIN,'+3.0 m','rgba(30,132,73,0.85)','end'),vap:hl(VAP,'vapour','rgba(192,57,43,0.85)','end')}}}}
});
function updHist(){
  const c=D.cases[+sCase2.value], p=+sPt.value, h=c.hist[p], h0=c.hist[0], x=D.rec[p];
  histChart.data.datasets[0].data=c.t.map((t,k)=>({x:t,y:h[k]}));
  histChart.data.datasets[1].data=p===0?[]:c.t.map((t,k)=>({x:t,y:h0[k]}));
  histChart.data.datasets[0].label='Pressure head at '+fmt1(x/1000)+' km (m)';
  histChart.update('none');
  const ix=x/100, mn=c.pmin[ix], mx=c.pmax[ix], m0=c.pmin[0];
  document.getElementById('rHmin').innerHTML=sgn(mn,1)+' <small>m</small>';
  document.getElementById('rHmax').innerHTML=fmt1(mx)+' <small>m</small>';
  document.getElementById('rH0').innerHTML=sgn(m0,1)+' <small>m</small>';
  const say=v=>v<=VAP+0.05?bad('vapour'):(v<PMIN?bad('fails +3.0 m'):good('passes +3.0 m'));
  document.getElementById('rSays').innerHTML=say(m0);
  document.getElementById('rTruth').innerHTML=say(mn);
}
[sPt,sCase2].forEach(s=>s.addEventListener('input',updHist));updHist();

/* ---------- CHART 3 : review scorecard ---------- */
const PARTS=['Basis','Model','Scenarios','Results','Devices','Operation'];
const boxes=CK.map((c,i)=>document.getElementById('c'+i));
const revChart=new Chart(document.getElementById('revChart'),{
  data:{labels:PARTS,datasets:[{type:'bar',label:'Weighted share present (%)',data:[],backgroundColor:[],borderWidth:0}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,indexAxis:'y',
    scales:{x:{min:0,max:100,title:{display:true,text:'Weighted share of the part present (%)',font:TTL},...AX},y:{...AX}},
    plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.x)} %`}},
      annotation:{annotations:{ok:{type:'line',xMin:80,xMax:80,borderColor:'#1e8449',borderWidth:1.4,borderDash:[6,4],label:{display:true,content:'80 %',position:'start',font:LBL,color:'#fff',backgroundColor:'rgba(30,132,73,0.85)'}}}}}}
});
function updRev(){
  const w=CK.map(c=>c[2]?2:1), on=boxes.map(b=>!!b.checked);
  const share=PARTS.map(p=>{let t=0,s=0;CK.forEach((c,i)=>{if(c[0]===p){t+=w[i];if(on[i])s+=w[i];}});return 100*s/t;});
  revChart.data.datasets[0].data=share;
  revChart.data.datasets[0].backgroundColor=share.map(v=>v>=80?'#1e8449':(v>=50?'#b9770e':'#c0392b'));
  revChart.update('none');
  const tot=100*w.reduce((s,x,i)=>s+(on[i]?x:0),0)/w.reduce((s,x)=>s+x,0);
  const miss=CK.filter((c,i)=>c[2]&&!on[i]).length;
  let wi=0; share.forEach((v,i)=>{if(v<share[wi])wi=i;});
  document.getElementById('rTot').innerHTML=fmt0(tot)+' <small>%</small>';
  document.getElementById('rCrit').innerHTML=String(miss);
  document.getElementById('rWeak').innerHTML=PARTS[wi]+' ('+fmt0(share[wi])+' %)';
  document.getElementById('rDec').innerHTML=miss>0?bad('return to author'):(tot>=90?good('accept'):warn('accept with comments'));
}
boxes.forEach(b=>b.addEventListener('input',updRev));boxes.forEach(b=>b.addEventListener('change',updRev));updRev();
window.addEventListener('load',function(){try{[profChart,histChart,revChart].forEach(c=>c.resize());}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Boulos, P.F., Karney, B.W., Wood, D.J. &amp; Lingireddy, S. &ldquo;Hydraulic transient guidelines for protecting water distribution systems.&rdquo; <em>Journal AWWA</em>, 97(5), 2005: the scope of a transient study, data needs, scenarios and protection strategies.</li>
  <li>Thorley, A.R.D. <em>Fluid Transients in Pipeline Systems</em>, 2nd ed. Professional Engineering Publishing, 2004: the events to consider for pumped mains and the presentation of transient results.</li>
  <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>. Prentice Hall, 1993: transient events, boundary conditions and the method of characteristics behind the runs in this article.</li>
  <li>Bentley Systems. <em>OpenFlows HAMMER</em> documentation: scenarios and alternatives, profiles and transient envelopes, report points, animation data, results tables and calculation options.</li>
  <li>EN 805 <em>Water supply. Requirements for systems and components outside buildings</em>: the pressure terms and limits a surge report should state.</li>
  <li>Abokhatwa, M. <em>Surge protection design series</em>, abokhatwa.com, 2026: the reference main, the vessel sizing method and the verified MOC solver used for the runs in this article.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#SurgeAnalysis #WaterHammer #HydraulicTransients #SurgeStudy #TransientReport #DesignReview #EngineeringReview #BentleyHAMMER #OpenFlowsHAMMER #SurgeVessel #DeviceSchedule #AssumptionsRegister #ScenarioMatrix #PressureEnvelope #HydraulicGradeLine #PipelineProfile #HighPoint #AirValves #OperatingRules #Interlocks #PumpStation #TransmissionMain #PipelineDesign #WaterEngineering</div>
"""

import json, os
_A = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'surge_data', 'analyst.json')))['s11']
DATA = {'x': _A['x'], 'z': _A['z'], 'hgl': _A['hgl'], 'rec': _A['rec'],
        'cases': [{k: c[k] for k in ('key', 'pmax', 'pmin', 'hmax', 'hmin', 'line_min', 'at_min', 'line_max', 'pump_min', 't', 'hist')} for c in _A['cases']]}
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':'))).replace('__CHECKS__', json.dumps([[p, t, c, k] for (p, t, c, k) in CHECKS]))
BODY = BODY.replace('__CHECKS__', CHECKS_HTML).replace('__GREQ__', '%.2f' % _A['gas_required'])

SPEC = dict(
    slug='surge-study-report-review-checklist', cat='surge', mins=18,
    date_iso='2026-11-19', date_human='November 2026', date_ar='نوفمبر 2026',
    title='The Surge Study Report: What to Deliver and What a Reviewer Checks',
    reg_title='The Surge Study Report: What to Deliver and What a Reviewer Checks',
    reg_tag='Surge Analysis · Reporting · Review',
    breadcrumb='Surge &amp; Transient Analysis',
    tag_line='Surge Analysis &middot; Reporting &middot; Review',
    desc='What a surge study report must contain and how to present it: structure, data and assumptions registers, the scenario matrix, pressure envelopes along the profile, histories at critical points, a device schedule, operating rules and a reviewer checklist, with three interactive charts and the HAMMER outputs.',
    og_desc='With a vessel sized on a flat profile, the pump history of the 12 km main never falls below +4.8 m, while the 7.2 km high point reaches −5.8 m. A report that showed only the pump, or head without the profile, would have passed it.',
    ld_desc='Writing and reviewing a surge study report: contents, registers, scenarios, envelope and history presentation, device schedule, operating rules and a weighted review checklist, with the Bentley HAMMER outputs.',
    img_alt='Surge study report pages on a desk: a pipeline profile chart with two high points and pressure envelopes, a results table, a checklist with some items ticked, a red pen, a scale ruler and a laptop showing a pipe network model',
    en_tag='Surge &amp; Transient Analysis &middot; Reporting',
    en_title='The Surge Study Report: What to Deliver and What a Reviewer Checks',
    en_excerpt='With a vessel sized on a flat profile, the pump history of the 12 km main never falls below <strong>+4.8 m</strong>, while the 7.2 km high point reaches <strong>−5.8 m</strong> and 8.5 km of main is below the criterion. A report that showed only the pump, or head without the profile, would have passed it. The structure we use, the data and assumptions registers, the scenario matrix, how to present envelopes and histories, a complete device schedule, operating rules and an interactive reviewer checklist.',
    en_search='surge study report transient analysis report review checklist reviewer data register assumptions register scenario matrix pressure envelope hydraulic grade line pipeline profile high point time history report points device schedule surge vessel gas volume connection orifice operating rules interlocks permissives restart after trip sensitivity Bentley HAMMER OpenFlows scenarios alternatives profiles water hammer pump station transmission main',
    ar_title='تقرير دراسة المطرقة المائية: ما يجب تسليمه وما يراجعه المراجِع',
    ar_excerpt='مع خزان حماية صُمّم على مقطع مستوٍ، لا ينخفض الضغط عند المضخة في الخط بطول ١٢ كم عن <strong>+٤٫٨ م</strong>، بينما تصل النقطة المرتفعة عند ٧٫٢ كم إلى <strong>−٥٫٨ م</strong>. والتقرير الذي يعرض المضخة فقط، أو خط الطاقة دون المقطع الطولي، كان سيقبل هذا التصميم. هيكل التقرير، وسجلات البيانات والافتراضات، ومصفوفة السيناريوهات، وطريقة عرض الأغلفة والسجلات الزمنية، وجدول الأجهزة، وقواعد التشغيل، وقائمة مراجعة تفاعلية.',
    ar_search='تقرير دراسة المطرقة المائية الطرق المائي مراجعة الدراسة قائمة المراجعة سجل البيانات سجل الافتراضات مصفوفة السيناريوهات غلاف الضغوط خط الطاقة الهيدروليكي المقطع الطولي النقطة المرتفعة جدول الأجهزة خزان الحماية قواعد التشغيل بنتلي هامر',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
