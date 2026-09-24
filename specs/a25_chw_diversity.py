# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Every megatall project reaches the same argument sooner or later: <em>how much diversity do we take on the chilled water?</em> One side wants a single percentage for the tower, another wants one per use, and the pump, heat-exchanger and chiller schedules quietly end up on different bases. The argument never closes because it is about the wrong thing. Diversity is not a number you choose once; it is a result that changes at every level of the system. We built an hour-by-hour model of a mixed-use Gulf tower (offices, hotel, residences, retail, a ballroom and an observation deck) to show where it really comes from. The plant needs <strong>0.86</strong> of the sum of terminal peaks. Almost all of that saving sits <strong>inside each floor and inside each use</strong>, and a blanket 0.70 would leave the plant <strong>19&nbsp;% short</strong> on the design day.</p>

<h2 id="terms">1 &middot; Two words for one idea, and two ideas under one word</h2>
<p>Half of the disputes about diversity are about vocabulary. Electrical engineering, where the terms come from, defines the <strong>diversity factor</strong> as the sum of the individual maximum demands divided by the maximum demand of the group, a number of one or more [1]. HVAC engineers usually mean its reciprocal, the <strong>coincidence</strong> or <strong>simultaneity factor</strong>, a number of one or less:</p>
<div class="eq">\[ DF = \frac{\sum_i \hat{q}_i}{\max_t \sum_i q_i(t)} \;\ge 1, \qquad CF = \frac{1}{DF} = \frac{\max_t \sum_i q_i(t)}{\sum_i \hat{q}_i} \;\le 1 \]</div>
<p>where \(q_i(t)\) is the load of zone \(i\) at hour \(t\) and \(\hat{q}_i\) is that zone's own peak. "Take 80&nbsp;% diversity" can mean a factor of 0.80 or of 1.25, so a design basis that does not say which is not a design basis. This article quotes the coincidence factor throughout and calls it that.</p>
<p>The second problem is that two physically different effects hide under the one word:</p>
<ul class="clean">
  <li><strong>Time diversity</strong> is deterministic. The east façade peaks in the morning and the west in the afternoon; offices peak at mid-afternoon and retail in the evening. It needs no factor at all: it falls out of adding the hourly loads together, which is exactly what a block-load calculation does [2, 3].</li>
  <li><strong>Usage diversity</strong> is statistical. Not every hotel room is let, not every apartment has its cooker on, not every tenant fills the floor. It applies only to loads that depend on people and their equipment, and it grows with the number of independent units in the group.</li>
</ul>
<p>Weather-driven loads, meaning solar gain, conduction, infiltration and outdoor air at its design rate, have <strong>no usage diversity</strong>. The sun reaches every floor of the west façade at the same moment, whether the rooms behind it are let or not.</p>

<h2 id="tower">2 &middot; The tower we modelled</h2>
<p>The example is a mixed-use megatall on the Gulf coast. It has a retail podium, a ballroom and dining level, forty office floors, thirty hotel floors, fifty residential floors and an observation deck, with 243,500&nbsp;m&sup2; of conditioned floor. Every floor is split into four perimeter zones and a core. For each zone the model builds a 24-hour design-day load from four sources:</p>
<ul class="clean">
  <li><strong>Envelope</strong>: the sun position is computed for the site latitude on 21 July, run through a simple clear-sky model onto each façade and a radiant time lag, then conduction and infiltration are added.</li>
  <li><strong>Internal</strong>: people, lights and equipment, on a schedule specific to each use.</li>
  <li><strong>Ventilation</strong>: outdoor air cooled from the outdoor to the room enthalpy.</li>
  <li><strong>Process</strong>: 900&nbsp;kW that never switches off (IT, telecom, lift machine and electrical rooms).</li>
</ul>
<p>The coastal design day peaks at 42&nbsp;&deg;C with a humidity ratio of 20.5&nbsp;g/kg, which keeps the outdoor enthalpy above 85&nbsp;kJ/kg all night. A second, inland climate (45.5&nbsp;&deg;C, 8&nbsp;g/kg) is included for comparison. The design-day inputs are illustrative; a project must use its own ASHRAE climatic design data [4].</p>
<div class="tbl-wrap"><table>
  <caption>The example programme. Unit counts set the statistical usage diversity; the mean usage and its spread are stated assumptions a project should replace with its own.</caption>
  <thead><tr><th>Use</th><th class="num">Floors</th><th class="num">Area (m&sup2;)</th><th>Load peaks around</th><th class="num">Independent units</th><th class="num">Mean usage at peak</th></tr></thead>
  <tbody>
    <tr><td>Retail podium</td><td class="num">4</td><td class="num">28,000</td><td>18:00&ndash;19:00 (evening crowds)</td><td class="num">160</td><td class="num">0.90</td></tr>
    <tr><td>Ballroom, meeting and dining</td><td class="num">2</td><td class="num">6,000</td><td>Lunch and dinner events</td><td class="num">1 (an event)</td><td class="num">1.00</td></tr>
    <tr><td>Offices</td><td class="num">40</td><td class="num">88,000</td><td>14:00&ndash;15:00</td><td class="num">160 tenancies</td><td class="num">0.85</td></tr>
    <tr><td>Hotel guest rooms</td><td class="num">30</td><td class="num">48,000</td><td>16:00&ndash;17:00 on the chilled water</td><td class="num">900 rooms</td><td class="num">0.85</td></tr>
    <tr><td>Residences</td><td class="num">50</td><td class="num">70,000</td><td>16:00&ndash;17:00 on the chilled water</td><td class="num">400 apartments</td><td class="num">0.75</td></tr>
    <tr><td>Observation deck and entertainment</td><td class="num">2</td><td class="num">3,500</td><td>16:00&ndash;20:00 (sunset visitors)</td><td class="num">1 (a crowd)</td><td class="num">1.00</td></tr>
    <tr><td>Process (IT, telecom, lift and electrical rooms)</td><td class="num">&ndash;</td><td class="num">&ndash;</td><td>Constant</td><td class="num">&ndash;</td><td class="num">1.00</td></tr>
  </tbody>
</table></div>
<p>Note the hotel rooms and the residences. Their occupants are home in the evening, yet their <em>chilled-water</em> peak falls at 16:00&ndash;17:00. On a Gulf façade the sun on the west glass and the round-the-clock outdoor air outweigh the evening rise in people and cooking. This is the first thing a schedule-only argument gets wrong.</p>

<h2 id="int-day">3 &middot; Interactive: the tower, hour by hour</h2>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Tower chilled-water load on the design day, stacked by use</div>
    <div class="fsub">Each band is one use with all its floors: envelope + usage-diversified internal gains + ventilation. The upper dashed line is the connected load (every terminal and ventilation unit at its own peak). The lower dashed line is the sum of each use's own peak. The marker is the tower block, the load the plant actually meets.</div>
  </div>
  <div class="chart-box"><canvas id="dayChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Climate</label>
      <select id="sCl"><option value="coastal" selected>Coastal Gulf (humid)</option><option value="inland">Inland Gulf (dry)</option></select>
      <div class="hint">Humid coastal air keeps the ventilation load high all night; dry inland air does not.</div>
    </div>
    <div class="ctrl">
      <label>Residential mean usage <span id="vMr">0.75</span></label>
      <input type="range" id="sMr" min="0.4" max="1" value="0.75" step="0.01">
      <div class="hint">Average share of full internal gain across the apartments at their peak hour. Vacant or seasonal units pull it down.</div>
    </div>
    <div class="ctrl">
      <label>Hotel occupancy at peak <span id="vMh">0.85</span></label>
      <input type="range" id="sMh" min="0.4" max="1" value="0.85" step="0.01">
      <div class="hint">Design occupancy of the guest rooms.</div>
    </div>
    <div class="ctrl">
      <label>Office usage <span id="vMo">0.85</span></label>
      <input type="range" id="sMo" min="0.5" max="1" value="0.85" step="0.01">
      <div class="hint">Average share of full occupancy and equipment across the tenancies.</div>
    </div>
    <div class="ctrl">
      <label>Statistical confidence <span id="vZ">1.65</span></label>
      <input type="range" id="sZ" min="0" max="2.33" value="1.65" step="0.01">
      <div class="hint">z in the usage allowance: 0 takes the mean, 1.65 covers 95&nbsp;% of days, 2.33 covers 99&nbsp;%.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Connected</div><div class="v" id="rConn">24,346 <small>kW</small></div></div>
    <div class="cell"><div class="k">Tower block</div><div class="v" id="rBlk">21,043 <small>kW</small></div></div>
    <div class="cell"><div class="k">Block hour</div><div class="v" id="rHr">14&ndash;15 <small>h</small></div></div>
    <div class="cell"><div class="k">Coincidence</div><div class="v" id="rCf">0.86</div></div>
    <div class="cell"><div class="k">Night minimum</div><div class="v" id="rMin">0.37 <small>of peak</small></div></div>
  </div>
</div>
<p class="fig-note">At the defaults the coastal tower peaks at 14:00&ndash;15:00 with 21,043&nbsp;kW, against a connected load of 24,346&nbsp;kW: a coincidence factor of 0.86, or 86&nbsp;W/m&sup2; against 100 (41&nbsp;m&sup2; per ton of refrigeration). Drop the residential usage to 0.40, an extreme that treats most apartments as empty, and the block falls only from 21,043 to 20,834&nbsp;kW, 1&nbsp;%, because the residences' envelope and outdoor air do not care whether anyone is home. The night minimum of 0.37 of the peak is the turndown the plant must handle in summer, before winter lowers it further.</p>

<h2 id="where">4 &middot; Where the diversity actually comes from</h2>
<p>Follow the load up the system, from the terminals to the plant, and record the coincident peak at each level. Each row below is what equipment at that level has to be sized for, and each is smaller than the one above it:</p>
<div class="tbl-wrap"><table>
  <caption>Coastal climate, default assumptions. Coincidence is relative to the connected load in the first row.</caption>
  <thead><tr><th>Level</th><th class="num">Load (kW)</th><th class="num">Coincidence</th><th>What is sized on it</th></tr></thead>
  <tbody>
    <tr><td>Every terminal and ventilation unit at its own peak (connected)</td><td class="num">24,346</td><td class="num">1.000</td><td>Fan-coil units, VAV boxes, chilled beams, fresh-air units, their control valves and branch pipes</td></tr>
    <tr><td>Sum of floor blocks</td><td class="num">22,692</td><td class="num">0.932</td><td>Floor AHU coils, floor branch mains</td></tr>
    <tr><td>Sum of use blocks</td><td class="num">22,060</td><td class="num">0.906</td><td>Risers serving one use</td></tr>
    <tr><td>Sum of hydraulic-zone blocks</td><td class="num">21,446</td><td class="num">0.881</td><td>Zone pumps; heat exchangers (see section 9 for the cascade)</td></tr>
    <tr><td>Tower block</td><td class="num">21,043</td><td class="num">0.864</td><td>Chillers, primary pumps, heat rejection, district-cooling contract</td></tr>
  </tbody>
</table></div>
<p>The largest single step, 6.8&nbsp;%, comes inside one floor: its four façades peak at different hours. Look at one office floor:</p>
<div class="tbl-wrap"><table>
  <caption>One office floor (2,200&nbsp;m&sup2;), coastal design day. Every terminal is sized at its own peak, with no factor.</caption>
  <thead><tr><th>Zone</th><th class="num">Area (m&sup2;)</th><th class="num">Own peak (kW)</th><th class="num">W/m&sup2;</th><th>Peak hour</th></tr></thead>
  <tbody>
    <tr><td>North perimeter</td><td class="num">211</td><td class="num">23.7</td><td class="num">112</td><td>15:00&ndash;16:00</td></tr>
    <tr><td>East perimeter</td><td class="num">211</td><td class="num">33.5</td><td class="num">159</td><td>09:00&ndash;10:00</td></tr>
    <tr><td>South perimeter</td><td class="num">211</td><td class="num">23.4</td><td class="num">111</td><td>13:00&ndash;14:00</td></tr>
    <tr><td>West perimeter</td><td class="num">211</td><td class="num">35.3</td><td class="num">167</td><td>16:00&ndash;17:00</td></tr>
    <tr><td>Core</td><td class="num">1,356</td><td class="num">48.8</td><td class="num">36</td><td>Flat from 09:00</td></tr>
    <tr><td>Floor ventilation</td><td class="num">&ndash;</td><td class="num">68.7</td><td class="num">&ndash;</td><td>13:00&ndash;14:00</td></tr>
    <tr><td><strong>Sum of peaks / floor block</strong></td><td class="num">2,200</td><td class="num"><strong>233.5 / 219.4</strong></td><td class="num">&ndash;</td><td>Block at 14:00&ndash;15:00</td></tr>
  </tbody>
</table></div>
<p>The east fan coils must deliver their 159&nbsp;W/m&sup2; at nine in the morning and the west ones their 167 at four in the afternoon. A single "diversity" applied to the terminals would short one of them. The floor as a whole, however, never needs more than 219.4&nbsp;kW. That 0.94 is the orientation diversity, and it is free.</p>
<p>The next step, from floors to uses, is the statistical one: 160 office tenancies do not all run at full density on the same afternoon, and 400 apartments do not all cook at once. The steps after that, between uses and between hydraulic zones, are small: 2.5&nbsp;% and 1.7&nbsp;% of the connected load. That is the finding that surprises people. <strong>In a hot climate, mixing uses buys little chilled-water diversity</strong>, because the loads that dominate (sun on glass, outdoor air, infiltration) peak together across every use within the same afternoon hours.</p>
<div class="callout key"><span class="lbl">Why not 0.55?</span>A figure of 0.5&ndash;0.6 for a mixed-use tower is often quoted, including in the simple model in our own <a href="cooling-load-modelling-tall-buildings.html">cooling-load article</a>. There the coincidence approaches an asymptote as the number of independently-peaking zones grows. That shape is right for the <em>usage-driven</em> share of the load and wrong for the weather-driven share, which does not become independent however many floors you add. In this tower the weather-driven share is large, so the tower lands at 0.86, not 0.6. In a cooler climate, or in a building where people and equipment dominate, the true figure moves down, but it has to be shown by calculation, not assumed.</div>

<h2 id="int-levels">5 &middot; Interactive: diversity, level by level</h2>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">How the coincident load falls as the system aggregates</div>
    <div class="fsub">"Levels" shows the load at each level of the hierarchy as a share of the connected load. "Uses" compares, for each use, its connected load, its own block (all its floors at its own peak hour) and what it contributes at the tower's peak hour. The last of these is the only honest meaning of a per-use factor. Default usage assumptions.</div>
  </div>
  <div class="chart-box"><canvas id="lvlChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Climate</label>
      <select id="sCl2"><option value="coastal" selected>Coastal Gulf (humid)</option><option value="inland">Inland Gulf (dry)</option></select>
      <div class="hint">The same tower in two climates.</div>
    </div>
    <div class="ctrl">
      <label>View</label>
      <select id="sView"><option value="levels" selected>Levels, terminal to plant</option><option value="uses">Uses at the tower's peak hour</option></select>
      <div class="hint">Switch between the aggregation cascade and the per-use contributions.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k" id="kL1">Within the floor</div><div class="v" id="rL1">&minus;6.8 <small>%</small></div></div>
    <div class="cell"><div class="k" id="kL2">Within each use</div><div class="v" id="rL2">&minus;2.6 <small>%</small></div></div>
    <div class="cell"><div class="k" id="kL3">Between uses and zones</div><div class="v" id="rL3">&minus;4.2 <small>%</small></div></div>
    <div class="cell"><div class="k" id="kL4">Tower coincidence</div><div class="v" id="rL4">0.864</div></div>
  </div>
</div>
<p class="fig-note">The first three readouts are percentage points of the connected load removed at each stage, so they add up to one minus the tower coincidence. Inland the tower coincidence drops to 0.845, since the dry night air takes the ventilation load away after dark, yet the ranking holds: most of the saving is inside floors and inside uses. In the "Uses" view the retail podium contributes only 0.74 of its connected load at the tower's peak, because the crowds arrive after 18:00. The ballroom contributes all of its load, because a full event at the design hour is exactly what it is designed for.</p>

<h2 id="percent">6 &middot; One percentage for the tower, or one per use?</h2>
<p>Neither, as an <em>input</em>. Both are legitimate as a <em>check</em>, once the block calculation exists.</p>
<p>A single percentage for the tower is a result: here it is 0.864, and it applies to one thing only, the plant, against the connected load. Applying it anywhere else is an error. On the terminals it undersizes every fan coil by 14&nbsp;%. On a heat exchanger it assumes diversity between zones that, in this tower, do not have any (section 9).</p>
<p>Per-use percentages are also results, and they depend on the whole mix, not just on the use:</p>
<div class="tbl-wrap"><table>
  <caption>Coastal climate, default assumptions. "At tower peak" is each use's load during the tower's peak hour (14:00&ndash;15:00).</caption>
  <thead><tr><th>Use</th><th class="num">Connected (kW)</th><th class="num">Own block (kW)</th><th>Own peak hour</th><th class="num">At tower peak (kW)</th><th class="num">Factor at tower peak</th></tr></thead>
  <tbody>
    <tr><td>Retail podium</td><td class="num">3,542</td><td class="num">3,240</td><td>18:00&ndash;19:00</td><td class="num">2,626</td><td class="num">0.74</td></tr>
    <tr><td>Ballroom, meeting and dining</td><td class="num">1,802</td><td class="num">1,798</td><td>14:00&ndash;15:00</td><td class="num">1,798</td><td class="num">1.00</td></tr>
    <tr><td>Offices</td><td class="num">9,338</td><td class="num">8,385</td><td>14:00&ndash;15:00</td><td class="num">8,385</td><td class="num">0.90</td></tr>
    <tr><td>Hotel guest rooms</td><td class="num">3,088</td><td class="num">2,710</td><td>16:00&ndash;17:00</td><td class="num">2,594</td><td class="num">0.84</td></tr>
    <tr><td>Residences</td><td class="num">4,672</td><td class="num">4,038</td><td>16:00&ndash;17:00</td><td class="num">3,938</td><td class="num">0.84</td></tr>
    <tr><td>Observation deck</td><td class="num">1,004</td><td class="num">989</td><td>16:00&ndash;17:00</td><td class="num">802</td><td class="num">0.80</td></tr>
    <tr><td>Process</td><td class="num">900</td><td class="num">900</td><td>Constant</td><td class="num">900</td><td class="num">1.00</td></tr>
    <tr><td><strong>Tower</strong></td><td class="num"><strong>24,346</strong></td><td class="num">&ndash;</td><td>14:00&ndash;15:00</td><td class="num"><strong>21,043</strong></td><td class="num"><strong>0.86</strong></td></tr>
  </tbody>
</table></div>
<p>Two things follow. First, a "residential factor of 0.84" is not a property of residences. Move the tower to a climate where the offices peak later, add a mall that peaks at noon, or let the hotel become serviced apartments, and every number in the last column changes. Borrowing these factors from another project is the usual source of error.</p>
<p>Second, look at what the common rules of thumb do to the plant. The tower needs 21,043&nbsp;kW:</p>
<div class="tbl-wrap"><table>
  <caption>The plant on different bases, coastal climate. Shortfall and excess are relative to the simulated block.</caption>
  <thead><tr><th>Basis</th><th class="num">Plant (kW)</th><th class="num">Against the block</th></tr></thead>
  <tbody>
    <tr><td>Sum of every terminal peak (no diversity)</td><td class="num">24,346</td><td class="num">+16&nbsp;% oversized</td></tr>
    <tr><td>Simulated block</td><td class="num">21,043</td><td class="num">&ndash;</td></tr>
    <tr><td>Blanket 0.70 &times; connected</td><td class="num">17,042</td><td class="num">19&nbsp;% short</td></tr>
    <tr><td>Blanket 0.60 &times; connected</td><td class="num">14,608</td><td class="num">31&nbsp;% short</td></tr>
  </tbody>
</table></div>
<div class="callout warn"><span class="lbl">The asymmetry</span>An oversized plant costs money and part-load efficiency. An undersized one fails on the hottest afternoons, in front of the client. Error in both directions is common, but only one of them is discovered in operation. That is why the block has to be calculated and written down, not negotiated.</div>

<h2 id="stat">7 &middot; The statistics of usage diversity</h2>
<p>Where diversity is genuinely statistical, it follows the arithmetic of adding independent random loads. If each of \(n\) units has a mean usage \(m\) at the peak hour, as a fraction of its full internal gain, and a spread \(s\) between units, the group's design usage at a confidence \(z\) is:</p>
<div class="eq">\[ f(n) = \min\!\left(1,\; m + z\,\frac{s}{\sqrt{n}}\right) \]</div>
<p>A single room gets \(f = 1\): its terminal must cope with it full. As \(n\) grows the factor falls towards the mean \(m\), quickly at first and then slowly. For the 400 apartments, with \(m\) = 0.75 and \(s\) = 0.30 at 95&nbsp;% confidence, it is 0.925 for one floor of eight and 0.775 for the whole residential block. The formula applies to <em>internal and occupancy-driven</em> load only, and it assumes the units are independent. A national holiday, Ramadan evenings or a stadium event on the television correlate them, and the diversity disappears; this is why the confidence matters.</p>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Statistical usage factor against the number of independent units</div>
    <div class="fsub">f(n) = min(1, m + z&middot;s/&radic;n) on the internal load. Markers show one apartment, one residential floor (8), one hydraulic zone of residences (240) and all of them (400). Log scale on the number of units.</div>
  </div>
  <div class="chart-box"><canvas id="statChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Mean usage m <span id="vM3">0.75</span></label>
      <input type="range" id="sM3" min="0.3" max="1" value="0.75" step="0.01">
      <div class="hint">The asymptote: what a very large group averages at the peak hour.</div>
    </div>
    <div class="ctrl">
      <label>Spread between units s <span id="vS3">0.30</span></label>
      <input type="range" id="sS3" min="0" max="0.5" value="0.3" step="0.01">
      <div class="hint">Standard deviation of one unit's usage. Hotel rooms, which are let or not, are high.</div>
    </div>
    <div class="ctrl">
      <label>Confidence z <span id="vZ3">1.65</span></label>
      <input type="range" id="sZ3" min="0" max="2.33" value="1.65" step="0.01">
      <div class="hint">1.65 is 95&nbsp;%, 2.33 is 99&nbsp;% of design days.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">One unit</div><div class="v" id="rF1">1.00</div></div>
    <div class="cell"><div class="k">One floor (8)</div><div class="v" id="rF8">0.925</div></div>
    <div class="cell"><div class="k">One zone (240)</div><div class="v" id="rF240">0.782</div></div>
    <div class="cell"><div class="k">All (400)</div><div class="v" id="rF400">0.775</div></div>
  </div>
</div>
<p class="fig-note">Set the spread to zero and the curve collapses onto the mean: nothing random, nothing statistical to claim. Push the confidence to 2.33 and a floor of eight apartments is back at 0.997, practically no diversity. This is why terminals, floor branches and single-use AHUs see almost none of it, and why the plant sees the most.</p>

<h2 id="components">8 &middot; What each component is sized on</h2>
<p>The rule behind the whole table fits in one sentence. <strong>A component is sized on the coincident peak of everything it serves, at that group's own worst hour.</strong> A terminal serves one zone, so it takes that zone's peak. A plant serves the tower, so it takes the tower block. Everything in between takes the block of its own group. Diversity is never applied as a factor to a component; it appears because the group is larger.</p>
<div class="tbl-wrap"><table>
  <caption>Sizing basis by component. Values are for the example tower, coastal climate.</caption>
  <thead><tr><th>Component</th><th>Sized on</th><th>Diversity</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td>Fan coil, VAV box, chilled beam, room unit</td><td>Its zone's own peak (hour and month)</td><td>None</td><td>West office perimeter 35.3&nbsp;kW at 16:00&ndash;17:00</td></tr>
    <tr><td>Control valve and branch pipe to one terminal</td><td>The terminal's design flow</td><td>None</td><td>Selected on the coil flow, not on a share of it</td></tr>
    <tr><td>Fresh-air unit / dedicated outdoor air system</td><td>Design ventilation at the peak outdoor enthalpy [10]</td><td>None, unless demand-controlled</td><td>68.7&nbsp;kW per office floor at 13:00&ndash;14:00</td></tr>
    <tr><td>Floor AHU (VAV, several zones)</td><td>Block of its zones; fan airflow on the block, boxes on zone peaks</td><td>Orientation only</td><td>219.4&nbsp;kW against 233.5 summed</td></tr>
    <tr><td>Process cooling (IT, telecom, lift rooms)</td><td>The heat load, 24/7</td><td>None; standby units carry no load</td><td>900&nbsp;kW constant</td></tr>
    <tr><td>Floor branch main</td><td>Floor block flow</td><td>Orientation</td><td>0.94 of the terminal flows on an office floor</td></tr>
    <tr><td>Riser</td><td>Block of the floors it serves, plus a stated allowance for change of use</td><td>Statistical, growing with floors</td><td>Residential riser near 0.86 of connected</td></tr>
    <tr><td>Zone (secondary) pumps</td><td>Block flow of the zone at the <em>achieved</em> &Delta;T</td><td>Only with two-way valves</td><td>Zone 1: 13,709&nbsp;kW, 0.88 of connected</td></tr>
    <tr><td>Pressure-break heat exchangers</td><td>Block of every zone above, in a cascade, at their coincident hour</td><td>Only between zones that peak at different hours</td><td>HX-A 7,737&nbsp;kW = sum of the three zones above it</td></tr>
    <tr><td>Chillers and primary pumps</td><td>Tower block + pump heat + distribution gains, then redundancy</td><td>The full tower coincidence</td><td>21,043&nbsp;kW block</td></tr>
    <tr><td>Cooling towers</td><td>Chiller duty plus compressor work</td><td>As the plant</td><td>Follows the chillers, no further factor</td></tr>
    <tr><td>District-cooling contract and energy transfer station</td><td>Tower block plus an explicit margin</td><td>As the plant; the network's own diversity is the provider's [11]</td><td>The contracted capacity is billed; see <a href="district-cooling-ets-tall-buildings.html">district cooling</a></td></tr>
    <tr><td>Thermal energy storage</td><td>The ton-hours under the design-day curve, not the peak</td><td>Not applicable</td><td>347.7&nbsp;MWh (98,860 ton-hours) a day, load factor 0.69; see <a href="thermal-energy-storage-tall-buildings.html">storage</a></td></tr>
  </tbody>
</table></div>
<p>Two rows in that table cause most of the site problems: the pumps and the heat exchangers.</p>
<p><strong>Pumps only get diversity from two-way valves.</strong> A terminal with a three-way valve draws its full design flow whether it is loaded or not. A circuit full of them has a constant flow equal to the sum of the terminal flows, whatever the load does. Size those pumps on the block and they are short from the day they start [5]. Diversity on the flow requires variable flow at the terminals.</p>
<p><strong>Pumps are sized on flow, not on load.</strong> Flow is load divided by \(\rho c_p \Delta T\), and the \(\Delta T\) that matters is the one the system achieves at the peak, not the one on the schedule [6]:</p>
<div class="eq">\[ \dot V = \frac{Q}{\rho\, c_p\, \Delta T} \qquad 21{,}043\ \text{kW at } 8\ \text{K} \rightarrow 628\ \text{L/s}; \quad \text{at } 6\ \text{K} \rightarrow 837\ \text{L/s} \;(+33\,\%) \]</div>
<p>A 25&nbsp;% loss of \(\Delta T\) at the peak costs a third more flow, more than the entire diversity taken between the uses and the zones. If the pumps and risers were cut to the diversified flow at the design \(\Delta T\), they are the first thing to run out.</p>

<h2 id="int-plant">9 &middot; Interactive: from the block to the plant, the pumps and the heat exchangers</h2>
<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Plant capacity on different bases, and the flows behind it</div>
    <div class="fsub">Bars: the chiller plant sized four ways, against the simulated block (dashed). The selected basis is the block plus losses and the margin policy you set. Readouts: the selected plant, what is installed with one standby chiller, the primary flow at the design and the achieved &Delta;T, and the duty of the lowest heat exchanger in the cascade.</div>
  </div>
  <div class="chart-box"><canvas id="plantChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Climate</label>
      <select id="sCl4"><option value="coastal" selected>Coastal Gulf (humid)</option><option value="inland">Inland Gulf (dry)</option></select>
      <div class="hint">Default usage assumptions for the block.</div>
    </div>
    <div class="ctrl">
      <label>Pump heat and distribution gains <span id="vLoss">3 %</span></label>
      <input type="range" id="sLoss" min="0" max="6" value="3" step="0.5">
      <div class="hint">Added once, at the plant.</div>
    </div>
    <div class="ctrl">
      <label>Margin per stage <span id="vMg">10 %</span></label>
      <input type="range" id="sMg" min="0" max="15" value="10" step="1">
      <div class="hint">The safety margin each designer adds.</div>
    </div>
    <div class="ctrl">
      <label>Stages that add their own margin <span id="vSt">1</span></label>
      <input type="range" id="sSt" min="1" max="4" value="1" step="1">
      <div class="hint">1 = one margin, at the plant. 3 = load calculation, coil and plant each add theirs.</div>
    </div>
    <div class="ctrl">
      <label>Design &Delta;T <span id="vDt">8 K</span></label>
      <input type="range" id="sDt" min="5" max="10" value="8" step="0.5">
      <div class="hint">Chilled-water temperature difference on the schedule.</div>
    </div>
    <div class="ctrl">
      <label>&Delta;T achieved at peak <span id="vDa">8 K</span></label>
      <input type="range" id="sDa" min="4" max="10" value="8" step="0.5">
      <div class="hint">What the coils actually return. Degraded &Delta;T raises the flow for the same load.</div>
    </div>
    <div class="ctrl">
      <label>Duty chillers (plus one standby) <span id="vN">4</span></label>
      <input type="range" id="sN" min="2" max="6" value="4" step="1">
      <div class="hint">Equal units, N+1.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Selected plant</div><div class="v" id="rDuty">23,842 <small>kW</small></div></div>
    <div class="cell"><div class="k">Installed N+1</div><div class="v" id="rInst">5 &times; 5,961 <small>kW</small></div></div>
    <div class="cell"><div class="k">Against the block</div><div class="v" id="rOver">+13 <small>%</small></div></div>
    <div class="cell"><div class="k">Flow at design / achieved &Delta;T</div><div class="v" id="rFlow">711 / 647 <small>L/s</small></div></div>
    <div class="cell"><div class="k">HX-A duty</div><div class="v" id="rHx">7,737 <small>kW</small></div></div>
  </div>
</div>
<p class="fig-note">With 3&nbsp;% for pump heat and distribution gains and one 10&nbsp;% margin at the plant, the plant is 23,842&nbsp;kW, 13&nbsp;% above the block: a defensible, stated allowance. Let three designers each add their 10&nbsp;% and the same plant is 28,849&nbsp;kW, 37&nbsp;% above the block, more than the 24,346&nbsp;kW of having taken no diversity at all. Margins compound; diversity does not rescue them. Lower the achieved &Delta;T to 6&nbsp;K and the primary flow the load needs rises to 862&nbsp;L/s, above what pumps sized at the design &Delta;T deliver.</p>

<h3>The heat-exchanger cascade</h3>
<p>Megatall chilled water is broken into pressure zones by plate heat exchangers, and in a cascade each exchanger feeds the zone above it through the next one [7]. That changes the question. HX-A does not serve "Zone 2". It serves Zones 2, 3 and 4 together, so its duty is the coincident block of all three:</p>
<div class="tbl-wrap"><table>
  <caption>Coastal climate. Flows at an 8&nbsp;K secondary &Delta;T.</caption>
  <thead><tr><th>Exchanger</th><th>Serves</th><th class="num">Coincident block (kW)</th><th class="num">Sum of zone peaks (kW)</th><th class="num">Flow (L/s)</th></tr></thead>
  <tbody>
    <tr><td>HX-A</td><td>Zones 2, 3, 4</td><td class="num">7,737</td><td class="num">7,737</td><td class="num">231</td></tr>
    <tr><td>HX-B</td><td>Zones 3, 4</td><td class="num">5,027</td><td class="num">5,027</td><td class="num">150</td></tr>
    <tr><td>HX-C</td><td>Zone 4</td><td class="num">2,604</td><td class="num">2,604</td><td class="num">78</td></tr>
  </tbody>
</table></div>
<p>The block equals the sum: hotel rooms, residences and the deck all peak together at 16:00&ndash;17:00, so there is no diversity to take <em>between</em> the cascaded zones. Their diversity is already inside each zone, in the statistics of their rooms and apartments. An exchanger sized on the sum of its zones' blocks, times a further tower factor, is short. Each stage also adds its approach temperature, so the top zone receives the warmest water; its coils need the capacity, but that is a coil selection question, not a diversity one. The hydraulics are in <a href="chilled-water-pumps-tall-buildings.html">chilled-water pumps in megatall buildings</a>.</p>

<h2 id="traps">10 &middot; The traps that cancel diversity on site</h2>
<ul class="clean">
  <li><strong>Three-way valves or bypasses</strong> at terminals make the flow constant. Keep three-way valves only where a minimum flow is needed, at the ends of mains, and count their flow.</li>
  <li><strong>Degraded &Delta;T</strong> from dirty coils, oversized valves, open bypasses or coils selected for too small a \(\Delta T\) raises the flow for the same load [6]. Design for it, commission against it, and size pumps and mains on the \(\Delta T\) you will actually achieve.</li>
  <li><strong>Stacked margins.</strong> 10&nbsp;% in the load calculation, 10&nbsp;% on the coil schedule and 10&nbsp;% on the plant is 33&nbsp;%, before any redundancy [12]. One margin, in one place, written down.</li>
  <li><strong>Standby counted as load.</strong> A standby CRAC unit, AHU or pump adds capacity, not chilled-water demand. Count duty units only in the load, and add redundancy after the block.</li>
  <li><strong>Morning pull-down.</strong> Offices whose AHUs are switched off overnight start with the stored heat of the fabric and furniture. In a tower whose hotel and residences keep the plant running, the start-up load lands on top of an already high base. Check the 07:00&ndash;09:00 hours of the block profile, not just the afternoon.</li>
  <li><strong>Turndown.</strong> A plant sized on a diversified peak spends most of its life far below it: 0.37 of the peak at 04:00 on the coastal design day, 0.27 inland, less in winter. Chiller sizes, minimum flows and staging must be chosen for that, not just for the peak [8].</li>
  <li><strong>Change of use.</strong> Diversity is a property of the schedules. A hotel floor that becomes serviced apartments, or an office tenant that adds a trading floor, changes it. Risers and exchangers need a stated allowance for that; do not rely on diversity to absorb it.</li>
</ul>

<h2 id="basis">11 &middot; Writing it into the design basis</h2>
<p>The argument with the designer ends when the diversity is a documented calculation rather than a percentage. What to require:</p>
<ul class="clean">
  <li><strong>An hourly block load report</strong>, to ASHRAE Standard 183 and the load chapter of the Fundamentals handbook, as ASHRAE 90.1 requires for system sizing [2, 3, 9]. It must give the peak and its hour for every zone, floor, use, riser, hydraulic zone, heat exchanger and the plant. Coincident peaks, not sums.</li>
  <li><strong>The schedules and usage assumptions per use</strong>: occupancy, lighting, equipment and ventilation hours, plus the mean usage and the number of units behind every statistical factor.</li>
  <li><strong>One table of margins</strong>: where each margin is added, how large it is and why. Nothing hidden in "the load calc includes 10&nbsp;%".</li>
  <li><strong>The sizing basis per component</strong>, as in section 8, including the \(\Delta T\) the pumps and risers are sized for.</li>
  <li><strong>The sensitivity</strong>: what the block becomes if the hotel runs at 100&nbsp;%, if a use changes, if the achieved \(\Delta T\) is 2&nbsp;K lower.</li>
</ul>
<div class="callout green"><span class="lbl">A basis statement you can use</span>"Terminal units, their valves and branches are selected on each zone's own peak with no diversity. Air-handling units, floor mains, risers, zone pumps and heat exchangers are sized on the coincident block of the zones they serve, at that group's own peak hour, from the hourly load calculation. Heat exchangers in the cascade carry the block of every zone above them. Usage diversity is applied to internal and occupancy-driven loads only, using the unit counts and assumptions in Appendix X; no diversity is applied to envelope or design ventilation loads. The central plant is sized on the tower block of X&nbsp;kW, plus Y&nbsp;% for pump heat and distribution gains and a single design margin of Z&nbsp;%, with N+1 redundancy. Pumps and risers are sized for an achieved &Delta;T of W&nbsp;K."</div>

<h2 id="checklist">12 &middot; Design checklist</h2>
<ul class="clean">
  <li>State which convention "diversity" means in the project (a diversity or a coincidence factor) and use one.</li>
  <li>Run an hourly block load with use-specific schedules; never derive the plant from a blanket percentage.</li>
  <li>Size every terminal, valve and one-terminal branch on its own zone peak, with no factor.</li>
  <li>Size every shared component on the coincident block of what it serves, at that group's own worst hour.</li>
  <li>Apply statistical usage diversity only to internal and occupancy-driven loads, scaled by the number of independent units, at a stated confidence.</li>
  <li>Take no usage diversity on envelope, infiltration or design ventilation; take none on event spaces or process loads.</li>
  <li>Size cascaded heat exchangers on the coincident block of every zone above them.</li>
  <li>Use two-way valves if you want flow diversity, and size pumps and mains for the achieved &Delta;T.</li>
  <li>Put one margin in one place and write it down; add redundancy after the block.</li>
  <li>Check turndown at the night and winter minimum, and the morning start-up hours.</li>
  <li>Record the sensitivity to change of use and keep a stated allowance on risers and exchangers.</li>
  <li>In the transient and energy models, use the same schedules as the sizing model, so the diversity you took is the diversity you operate.</li>
</ul>
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>IEEE Std 141 (<em>IEEE Recommended Practice for Electric Power Distribution for Industrial Plants</em>): definitions of demand, diversity and coincidence factors, from which the HVAC usage is borrowed.</li>
  <li>ASHRAE Handbook &mdash; <em>Fundamentals</em>, Nonresidential Cooling and Heating Load Calculations: zone peak versus block load, the radiant time series method and hourly schedules.</li>
  <li>ANSI/ASHRAE/ACCA Standard 183, <em>Peak Cooling and Heating Load Calculations in Buildings Except Low-Rise Residential Buildings</em>: the procedure for design peak and block loads.</li>
  <li>ASHRAE Handbook &mdash; <em>Fundamentals</em>, Climatic Design Information: design-day dry-bulb, daily range and humidity used to build the hourly outdoor conditions.</li>
  <li>ASHRAE Handbook &mdash; <em>HVAC Systems and Equipment</em>, Hydronic Heating and Cooling: variable-flow systems, two-way and three-way valves, pipe and pump sizing.</li>
  <li>Taylor, S.T. &ldquo;Degrading Chilled Water Plant Delta-T: Causes and Mitigation.&rdquo; <em>ASHRAE Transactions</em> 108(1), 2002: the causes and cost of low &Delta;T and its effect on flow and pumping.</li>
  <li>ASHRAE, <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed.: vertical zoning, heat-exchanger pressure breaks and load characteristics in tall buildings.</li>
  <li>ASHRAE Handbook &mdash; <em>HVAC Applications</em>, Tall Buildings: system arrangements, stack effect and part-load operation in tall buildings.</li>
  <li>ANSI/ASHRAE/IES Standard 90.1, <em>Energy Standard for Sites and Buildings Except Low-Rise Residential Buildings</em>: system design loads calculated to Standard 183 for equipment sizing.</li>
  <li>ANSI/ASHRAE Standard 62.1, <em>Ventilation and Acceptable Indoor Air Quality</em>: design ventilation rates and demand-controlled ventilation.</li>
  <li>ASHRAE, <em>District Cooling Guide</em>: building connections, contracted capacity and network diversity between buildings.</li>
  <li>CIBSE Guide A, <em>Environmental Design</em>: thermal design, plant sizing and design margins.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#ChilledWater #Diversity #DiversityFactor #CoincidenceFactor #SimultaneityFactor #BlockLoad #PeakLoad #CoolingLoad #LoadCalculation #ASHRAE183 #RadiantTimeSeries #MixedUse #MegatallBuildings #TallBuildings #HotelHVAC #ResidentialHVAC #FanCoilUnits #AHU #DOAS #HeatExchangers #PressureZoning #ChilledWaterPumps #DeltaT #LowDeltaT #ChillerPlant #DistrictCooling #ThermalEnergyStorage #DesignMargins #GulfEngineering #MEP #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'IBM Plex Sans',size:11}}};
const TT={display:true,font:{family:'IBM Plex Sans',size:12,weight:'600'}};
const LEG={labels:{font:{family:'IBM Plex Sans',size:11},usePointStyle:true,boxWidth:8}};
const LBL={size:10,family:'IBM Plex Sans'};
const D=__DATA__;
const ORDER=['process','office','retail','hotel_public','hotel_rooms','residential','observation'];
const COL={process:'#7f8c8d',office:'#1b4f72',retail:'#b9770e',hotel_public:'#c0392b',hotel_rooms:'#6b4f9e',residential:'#1e8449',observation:'#5eaadd'};
const FILL={process:'rgba(127,140,141,0.35)',office:'rgba(27,79,114,0.35)',retail:'rgba(185,119,14,0.35)',hotel_public:'rgba(192,57,43,0.35)',hotel_rooms:'rgba(107,79,158,0.35)',residential:'rgba(30,132,73,0.35)',observation:'rgba(94,170,221,0.35)'};
const hrs=h=>(h<10?'0':'')+h+':00';

/* usage-diversified hourly load of every use, all its floors, kW */
function uf(f,m,z){ if(f.units<=1||f.s===0) return 1; return Math.min(1,m+z*f.s/Math.sqrt(f.units)); }
function model(cl,P){
  const C=D[cl], out={};
  Object.keys(C.f).forEach(k=>{ const f=C.f[k]; const m=(P.m[k]!==undefined)?P.m[k]:f.m; const u=uf(f,m,P.z);
    out[k]=f.env.map((e,i)=>e+u*f.int[i]+(f.vo?u:1)*f.vent[i]); });
  out.process=new Array(24).fill(C.process);
  const tower=out.process.map((_,i)=>ORDER.reduce((a,k)=>a+out[k][i],0));
  const peak=Math.max(...tower), hour=tower.indexOf(peak);
  const zone=z=>out.process.map((_,i)=>D.zones[z].parts.reduce((a,p)=>a+out[p[0]][i]*p[1],0)+(z===0?C.process:0));
  const Z=[0,1,2,3].map(zone);
  const hx=[1,2,3].map(j=>Math.max(...Z[0].map((_,i)=>Z.slice(j).reduce((a,s)=>a+s[i],0))));
  return {out,tower,peak,hour,min:Math.min(...tower),Z,hx};
}
const DEF={m:{},z:1.65};

/* ---------- CHART 1 : the tower hour by hour ---------- */
const sCl=document.getElementById('sCl'), sMr=document.getElementById('sMr'), sMh=document.getElementById('sMh'),
      sMo=document.getElementById('sMo'), sZ=document.getElementById('sZ');
const dayChart=new Chart(document.getElementById('dayChart'),{
  type:'line',
  data:{labels:[...Array(24).keys()].map(h=>h+1),
    datasets:ORDER.map((k,j)=>({label:k,data:[],borderColor:COL[k],backgroundColor:FILL[k],borderWidth:1.2,pointRadius:0,fill:j===0?'origin':'-1',stack:'s'}))},
  options:{responsive:true,maintainAspectRatio:false,animation:false,interaction:{mode:'index',intersect:false},
    scales:{x:{...AX,title:{...TT,text:'Hour ending (solar time)'}},
            y:{...AX,stacked:true,min:0,title:{...TT,text:'Chilled-water load (kW)'}}},
    plugins:{legend:{...LEG,position:'bottom'},
      tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${fmt0(c.parsed.y)} kW`}},
      annotation:{annotations:{
        conn:{type:'line',scaleID:'y',value:0,borderColor:'#c0392b',borderWidth:1.5,borderDash:[6,4],label:{display:true,content:'',position:'start',font:LBL,color:'#c0392b',backgroundColor:'rgba(255,255,255,0.8)'}},
        sumu:{type:'line',scaleID:'y',value:0,borderColor:'#b9770e',borderWidth:1.5,borderDash:[3,3],label:{display:true,content:'',position:'end',font:LBL,color:'#b9770e',backgroundColor:'rgba(255,255,255,0.8)'}},
        pk:{type:'point',xValue:0,yValue:0,radius:6,backgroundColor:'#1a1d21',borderColor:'#ffffff',borderWidth:2}
      }}}}
});
function updDay(){
  const cl=sCl.value, P={m:{residential:+sMr.value,hotel_rooms:+sMh.value,office:+sMo.value},z:+sZ.value};
  document.getElementById('vMr').textContent=fmt2(+sMr.value);
  document.getElementById('vMh').textContent=fmt2(+sMh.value);
  document.getElementById('vMo').textContent=fmt2(+sMo.value);
  document.getElementById('vZ').textContent=fmt2(+sZ.value);
  const M=model(cl,P), C=D[cl];
  const labs={process:'Process',office:'Offices',retail:'Retail',hotel_public:'Ballroom and dining',hotel_rooms:'Hotel rooms',residential:'Residences',observation:'Observation deck'};
  ORDER.forEach((k,j)=>{ dayChart.data.datasets[j].data=M.out[k].map(v=>+v.toFixed(1)); dayChart.data.datasets[j].label=labs[k]; });
  const sumUse=ORDER.reduce((a,k)=>a+Math.max(...M.out[k]),0);
  const A=dayChart.options.plugins.annotation.annotations;
  A.conn.value=C.connected; A.conn.label.content='connected '+fmt0(C.connected)+' kW';
  A.sumu.value=sumUse; A.sumu.label.content='sum of use peaks '+fmt0(sumUse)+' kW';
  A.pk.xValue=M.hour; A.pk.yValue=M.peak;
  dayChart.options.scales.y.max=Math.ceil(C.connected*1.08/2000)*2000;
  dayChart.update('none');
  document.getElementById('rConn').innerHTML=fmt0(C.connected)+' <small>kW</small>';
  document.getElementById('rBlk').innerHTML=fmt0(M.peak)+' <small>kW</small>';
  document.getElementById('rHr').innerHTML=M.hour+'&ndash;'+(M.hour+1)+' <small>h</small>';
  document.getElementById('rCf').textContent=fmt2(M.peak/C.connected);
  document.getElementById('rMin').innerHTML=fmt2(M.min/M.peak)+' <small>of peak</small>';
}
[sCl,sMr,sMh,sMo,sZ].forEach(el=>el.addEventListener('input',updDay)); updDay();

/* ---------- CHART 2 : diversity level by level ---------- */
const sCl2=document.getElementById('sCl2'), sView=document.getElementById('sView');
const lvlChart=new Chart(document.getElementById('lvlChart'),{
  type:'bar',
  data:{labels:[],datasets:[]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,indexAxis:'y',
    scales:{x:{...AX,min:0,title:{...TT,text:''}},y:{...AX,ticks:{font:{family:'IBM Plex Sans',size:10.5}}}},
    plugins:{legend:{...LEG,position:'bottom'},tooltip:{callbacks:{label:c=>`${c.dataset.label}: ${sView.value==='levels'?fmt3(c.parsed.x):fmt0(c.parsed.x)+' kW'}`}}}}
});
function updLvl(){
  const cl=sCl2.value, C=D[cl], v=sView.value;
  if(v==='levels'){
    const L=C.levels, c0=L[0][1];
    lvlChart.data.labels=['Terminals at own peak (connected)','Sum of floor blocks','Sum of use blocks','Sum of zone blocks','Tower block (plant)'];
    lvlChart.data.datasets=[{label:'Share of connected load',data:L.map(x=>+(x[1]/c0).toFixed(3)),backgroundColor:['#7f8c8d','#5eaadd','#6b4f9e','#b9770e','#1b4f72'],borderWidth:0}];
    lvlChart.options.scales.x.min=0.6; lvlChart.options.scales.x.max=1.0;
    lvlChart.options.scales.x.title.text='Coincident load / connected load';
    const d1=(L[0][1]-L[1][1])/c0, d2=(L[1][1]-L[2][1])/c0, d3=(L[2][1]-L[4][1])/c0;
    document.getElementById('kL1').textContent='Within the floor';
    document.getElementById('kL2').textContent='Within each use';
    document.getElementById('kL3').textContent='Between uses and zones';
    document.getElementById('kL4').textContent='Tower coincidence';
    document.getElementById('rL1').innerHTML='&minus;'+fmt1(100*d1)+' <small>%</small>';
    document.getElementById('rL2').innerHTML='&minus;'+fmt1(100*d2)+' <small>%</small>';
    document.getElementById('rL3').innerHTML='&minus;'+fmt1(100*d3)+' <small>%</small>';
    document.getElementById('rL4').textContent=fmt3(L[4][1]/c0);
  } else {
    const keys=['retail','hotel_public','office','hotel_rooms','residential','observation'];
    const names={retail:'Retail',hotel_public:'Ballroom and dining',office:'Offices',hotel_rooms:'Hotel rooms',residential:'Residences',observation:'Observation deck'};
    lvlChart.data.labels=keys.map(k=>names[k]);
    lvlChart.data.datasets=[
      {label:'Connected',data:keys.map(k=>C.f[k].connected),backgroundColor:'#a9cce3',borderWidth:0},
      {label:'Own block',data:keys.map(k=>C.f[k].block),backgroundColor:'#5eaadd',borderWidth:0},
      {label:"At the tower's peak hour",data:keys.map(k=>C.f[k].at_peak),backgroundColor:'#1b4f72',borderWidth:0}];
    lvlChart.options.scales.x.min=0; lvlChart.options.scales.x.max=undefined;
    lvlChart.options.scales.x.title.text='kW';
    const fac=k=>C.f[k].at_peak/C.f[k].connected;
    document.getElementById('kL1').textContent='Retail at tower peak';
    document.getElementById('kL2').textContent='Residences at tower peak';
    document.getElementById('kL3').textContent='Hotel rooms at tower peak';
    document.getElementById('kL4').textContent='Offices at tower peak';
    document.getElementById('rL1').textContent=fmt2(fac('retail'));
    document.getElementById('rL2').textContent=fmt2(fac('residential'));
    document.getElementById('rL3').textContent=fmt2(fac('hotel_rooms'));
    document.getElementById('rL4').textContent=fmt2(fac('office'));
  }
  lvlChart.update('none');
}
[sCl2,sView].forEach(el=>el.addEventListener('input',updLvl)); updLvl();

/* ---------- CHART 3 : statistical usage factor ---------- */
const sM3=document.getElementById('sM3'), sS3=document.getElementById('sS3'), sZ3=document.getElementById('sZ3');
const NS=[]; for(let e=0;e<=3.0001;e+=0.05) NS.push(Math.round(Math.pow(10,e)*100)/100);
const statChart=new Chart(document.getElementById('statChart'),{
  type:'scatter',
  data:{datasets:[
    {type:'line',label:'Usage factor f(n)',data:[],borderColor:'#1b4f72',borderWidth:2.5,pointRadius:0,showLine:true},
    {type:'line',label:'Mean m (large-group limit)',data:[],borderColor:'#b9770e',borderWidth:1.5,borderDash:[5,4],pointRadius:0,showLine:true},
    {type:'scatter',label:'Apartment, floor, zone, all residences',data:[],backgroundColor:'#c0392b',borderColor:'#ffffff',borderWidth:2,pointRadius:6}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{...AX,type:'logarithmic',min:1,max:1000,title:{...TT,text:'Number of independent units n'}},
            y:{...AX,min:0.3,max:1.05,title:{...TT,text:'Share of full internal load'}}},
    plugins:{legend:{...LEG,position:'bottom'},tooltip:{callbacks:{label:c=>`n = ${fmt0(c.parsed.x)}: ${fmt3(c.parsed.y)}`}}}}
});
function updStat(){
  const m=+sM3.value, s=+sS3.value, z=+sZ3.value;
  document.getElementById('vM3').textContent=fmt2(m);
  document.getElementById('vS3').textContent=fmt2(s);
  document.getElementById('vZ3').textContent=fmt2(z);
  const f=n=>n<=1?1:Math.min(1,m+z*s/Math.sqrt(n));
  statChart.data.datasets[0].data=NS.map(n=>({x:n,y:+f(n).toFixed(4)}));
  statChart.data.datasets[1].data=[{x:1,y:m},{x:1000,y:m}];
  statChart.data.datasets[2].data=[1,8,240,400].map(n=>({x:n,y:+f(n).toFixed(4)}));
  statChart.options.scales.y.min=Math.min(0.3,Math.floor(m*10)/10-0.05);
  statChart.update('none');
  document.getElementById('rF1').textContent=fmt2(f(1));
  document.getElementById('rF8').textContent=fmt3(f(8));
  document.getElementById('rF240').textContent=fmt3(f(240));
  document.getElementById('rF400').textContent=fmt3(f(400));
}
[sM3,sS3,sZ3].forEach(el=>el.addEventListener('input',updStat)); updStat();

/* ---------- CHART 4 : from block to plant ---------- */
const sCl4=document.getElementById('sCl4'), sLoss=document.getElementById('sLoss'), sMg=document.getElementById('sMg'),
      sSt=document.getElementById('sSt'), sDt=document.getElementById('sDt'), sDa=document.getElementById('sDa'), sN=document.getElementById('sN');
const RHO_CP=4.19;
const plantChart=new Chart(document.getElementById('plantChart'),{
  type:'bar',
  data:{labels:['Selected basis','No diversity (sum of peaks)','Blanket 0.70 x connected','Blanket 0.60 x connected'],
    datasets:[{label:'Chiller plant (kW)',data:[],backgroundColor:['#1b4f72','#7f8c8d','#b9770e','#c0392b'],borderWidth:0}]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,indexAxis:'y',
    scales:{x:{...AX,min:0,title:{...TT,text:'Plant capacity (kW)'}},y:{...AX}},
    plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.x)} kW`}},
      annotation:{annotations:{blk:{type:'line',scaleID:'x',value:0,borderColor:'#1e8449',borderWidth:2,borderDash:[6,4],
        label:{display:true,content:'',position:'end',font:LBL,color:'#1e8449',backgroundColor:'rgba(255,255,255,0.8)'}}}}}}
});
function updPlant(){
  const cl=sCl4.value, C=D[cl], M=model(cl,DEF);
  const loss=+sLoss.value/100, mg=+sMg.value/100, st=+sSt.value, dT=+sDt.value, dA=+sDa.value, n=+sN.value;
  document.getElementById('vLoss').textContent=fmt1(+sLoss.value).replace('.0','')+' %';
  document.getElementById('vMg').textContent=sMg.value+' %';
  document.getElementById('vSt').textContent=st;
  document.getElementById('vDt').textContent=fmt1(dT).replace('.0','')+' K';
  document.getElementById('vDa').textContent=fmt1(dA).replace('.0','')+' K';
  document.getElementById('vN').textContent=n;
  const duty=M.peak*(1+loss)*Math.pow(1+mg,st), unit=duty/n;
  plantChart.data.datasets[0].data=[duty,C.connected,0.70*C.connected,0.60*C.connected].map(v=>+v.toFixed(0));
  const A=plantChart.options.plugins.annotation.annotations.blk; A.value=M.peak; A.label.content='block '+fmt0(M.peak)+' kW';
  plantChart.update('none');
  document.getElementById('rDuty').innerHTML=fmt0(duty)+' <small>kW</small>';
  document.getElementById('rInst').innerHTML=(n+1)+' &times; '+fmt0(unit)+' <small>kW</small>';
  const over=100*(duty/M.peak-1);
  document.getElementById('rOver').innerHTML=(over>=0?'+':'&minus;')+fmt0(Math.abs(over))+' <small>%</small>';
  const qDesign=duty/(RHO_CP*dT), qNeed=M.peak*(1+loss)/(RHO_CP*dA);
  document.getElementById('rFlow').innerHTML=fmt0(qDesign)+' / '+fmt0(qNeed)+' <small>L/s</small>'+(qNeed>qDesign?' <span class="badge bad">short</span>':'');
  document.getElementById('rHx').innerHTML=fmt0(M.hx[0])+' <small>kW</small>';
}
[sCl4,sLoss,sMg,sSt,sDt,sDa,sN].forEach(el=>el.addEventListener('input',updPlant)); updPlant();

window.addEventListener('load',function(){try{dayChart.resize();lvlChart.resize();statChart.resize();plantChart.resize();}catch(e){}});
"""

import json, os
_M = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diversity_data', 'model.json')))
_I = _M['inputs']
DATA = {'zones': [dict(key=z['key'], parts=[[k, s] for k, s in z['parts']]) for z in _I['zones']]}
for _cl in ('coastal', 'inland'):
    _c = _M[_cl]
    DATA[_cl] = dict(
        connected=_c['connected'], process=_c['process'],
        levels=_c['levels'],
        f={k: dict(env=v['env'], int=v['internal_raw'], vent=v['vent_raw'], vo=_I['funcs'][k]['vent_occ'],
                   m=_I['funcs'][k]['m'], s=_I['funcs'][k]['s'], units=v['units'],
                   connected=v['connected'], block=v['func_block_peak'], at_peak=v['at_tower_peak'])
           for k, v in _c['functions'].items()})
CHARTS = CHARTS.replace('__DATA__', json.dumps(DATA, separators=(',', ':')))

SPEC = dict(
    slug='chilled-water-diversity-megatall', cat='hvac', mins=30,
    date_iso='2026-09-24', date_human='September 2026', date_ar='سبتمبر 2026',
    title='Chilled-Water Diversity in Megatall Towers: Peak or Block, Per Use or Per Tower, and Which Components Get It',
    reg_title='Chilled-Water Diversity in Megatall Towers: Peak or Block, Per Use or Per Tower, and Which Components Get It',
    reg_tag='HVAC · Chilled Water · Diversity',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Chilled Water &middot; Diversity &middot; Megatall Buildings',
    desc='How much diversity to take on chilled water in a mixed-use megatall: diversity versus coincidence factor, time versus usage diversity, an hour-by-hour Gulf tower model, what each component is sized on from fan coils to heat exchangers and chillers, and four interactive charts.',
    og_desc='An hour-by-hour model of a mixed-use Gulf megatall: the plant needs 0.86 of the sum of terminal peaks, almost all of the diversity sits inside floors and uses, and a blanket 0.70 leaves the plant 19 % short.',
    ld_desc='A design-perspective guide to chilled-water diversity in mixed-use megatall towers: definitions, block versus peak loads, statistical usage diversity, sizing basis by component, heat-exchanger cascades and design margins.',
    img_alt='Cutaway of a tapered mixed-use tower on a blueprint grid, its west half in warm afternoon sun and its east half in blue shade, with chilled-water risers through the core, heat exchangers on three mechanical floors, two chillers in the basement plant and visitors on the observation deck, and translucent load curves rising behind it',
    en_tag='HVAC &amp; Cooling &middot; Chilled Water',
    en_title='Chilled-Water Diversity in Megatall Towers: Peak or Block, Per Use or Per Tower, and Which Components Get It',
    en_excerpt='One percentage for the tower or one per use? Neither, as an input. An hour-by-hour model of a mixed-use Gulf megatall shows the plant needs <strong>0.86</strong> of the sum of terminal peaks, that almost all of the diversity sits inside each floor and each use rather than between hotel, residences and offices, and that a blanket 0.70 leaves the plant <strong>19&nbsp;% short</strong>. Fan coils take their own peak; shared components take the block of what they serve; cascaded heat exchangers carry every zone above them, here with <strong>no diversity between zones</strong>. With four interactive charts.',
    en_search='chilled water diversity factor coincidence factor simultaneity factor block load peak load sum of peaks cooling load calculation ASHRAE 183 radiant time series hourly load profile mixed use tower megatall supertall hotel residential office retail ballroom observation deck fan coil unit FCU VAV AHU DOAS fresh air unit riser heat exchanger pressure break cascade secondary pumps primary pumps chiller plant sizing cooling tower district cooling contracted capacity thermal energy storage design margin safety factor stacked margins redundancy N+1 two-way valve three-way valve variable flow low delta T degraded delta T turndown Gulf coastal humid inland MEP HVAC design basis',
    ar_title='معامل التنوع في المياه المبرّدة للأبراج فائقة الارتفاع: الحمل الأقصى أم الحمل المتزامن، ولكل استخدام أم للبرج كله، وأي المعدات تستحقه',
    ar_excerpt='نسبة واحدة للبرج أم نسبة لكل استخدام؟ لا هذه ولا تلك كمُدخل. نموذج ساعي لبرج خليجي متعدد الاستخدامات يبيّن أن المحطة تحتاج <strong>٠٫٨٦</strong> من مجموع أحمال الوحدات الطرفية القصوى، وأن معظم التنوع يقع داخل كل طابق وكل استخدام لا بين الفندق والسكن والمكاتب، وأن نسبة ثابتة قدرها ٠٫٧٠ تجعل المحطة ناقصة <strong>١٩٪</strong> في يوم التصميم. وحدات ملف المروحة تُصمَّم على حملها الأقصى، والمعدات المشتركة على الحمل المتزامن لما تخدمه، والمبادلات المتتالية تحمل كل المناطق فوقها <strong>دون تنوع بينها</strong>. مع أربعة رسوم تفاعلية.',
    ar_search='معامل التنوع معامل التزامن المياه المبرّدة الحمل الأقصى الحمل المتزامن حساب أحمال التبريد الأبراج فائقة الارتفاع المباني متعددة الاستخدامات فندق سكني مكاتب تجزئة قاعة احتفالات وحدات ملف المروحة وحدات مناولة الهواء وحدات الهواء النقي الصاعد المبادل الحراري كسر الضغط المضخات الثانوية المضخات الأولية محطة التبريد أبراج التبريد تبريد المناطق القدرة التعاقدية تخزين الطاقة الحرارية هامش الأمان الاحتياطي فرق درجة الحرارة الصمامات ثنائية الاتجاه الخليج',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
