# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Fire water has to reach the top floor once, on the worst day of the building's life. Domestic water has to reach it <em>every time somebody opens a tap</em>, at a pressure that is neither a dribble nor a jet, for sixty years. That second requirement is far harder, and it is governed by a constraint fire systems never face: the acceptable pressure window at a tap is only about <strong>3.5&nbsp;bar wide</strong>, which is worth just 36 metres of building. A megatall tower is therefore not a four-zone problem like the standpipe — it is a seventeen-zone problem, unless you design your way out of it. On top of that sits a second, quieter error: almost every tall residential tower in the world is sized by a 1940 method that over-predicts peak demand by a factor of three.</p>

<h2 id="why">1 · Why domestic water in a megatall is a different problem</h2>
<ul class="clean">
  <li><strong>The pressure window is tiny.</strong> A tap needs roughly <strong>1.0–1.5&nbsp;bar</strong> flowing to work properly, and codes cap static pressure at a fixture at about <strong>4.5–5.5&nbsp;bar</strong> to prevent noise, splashing, seal wear and burst flexible connectors. That window is worth about 36&nbsp;m of height — around ten storeys.</li>
  <li><strong>Demand is probabilistic, not additive.</strong> Nobody flushes every toilet at once. The whole design rests on a statistical estimate of simultaneous use, and the traditional estimate is badly out of date for modern low-flow fittings.</li>
  <li><strong>Water quality degrades with residence time.</strong> Large break tanks high in a tower can hold water for days. Chlorine decays, temperature drifts into the growth range, and a storage strategy sized purely for resilience becomes a public-health liability.</li>
  <li><strong>Every fixture is a potential cross-connection.</strong> With hundreds of metres of head available, a backflow event does not trickle — it drives.</li>
  <li><strong>The energy is real.</strong> Lifting water 600&nbsp;m costs about <strong>2.4&nbsp;kWh/m³</strong> at the pump shaft — roughly five times the specific energy of a typical municipal distribution system, for the last 600&nbsp;m of a journey that may have started 400&nbsp;km away.</li>
</ul>
<p>The static-pressure physics is the same \(p=\rho g h\) that drives <a href="firefighting-tall-buildings.html">fire standpipe zoning</a>; what changes is the ceiling. Fire equipment tolerates 12–24&nbsp;bar. A shower mixer tolerates five.</p>

<h2 id="demand">2 · Estimating demand — and why Hunter over-sizes your tower</h2>
<p>Roy Hunter's 1940 fixture-unit method is still the default in most codes. It models each fixture as an on/off process, assigns weighted <strong>water supply fixture units (WSFU)</strong>, and reads a design flow off an empirical curve<sup class="cite">[1][2]</sup>. It was a brilliant piece of work — calibrated against the fixtures of 1940, which used a 20-litre flush, an unrestricted 15&nbsp;L/min tap and no aerators at all.</p>
<p>Modern fittings use a 4.5-litre dual flush, 6&nbsp;L/min aerated taps and 9&nbsp;L/min showers. The fixtures changed by a factor of three; the curve did not. The modern replacement — the basis of the IAPMO Water Demand Calculator and of EN 806 / DIN 1988-300 style methods — treats simultaneous use as a <strong>binomial process</strong><sup class="cite">[3]</sup>:</p>
<div class="eq">\[ Q_{design} \;=\; n\,p\,q_f \;+\; z\,q_f\sqrt{n\,p\,(1-p)} \]</div>
<p>with \(n\) fixtures, \(p\) the probability any one is in use at the peak minute, \(q_f\) the flow of one fixture and \(z\) the confidence multiplier (1.96 for the 97.5th percentile). The first term is the average demand; the second is the statistical peak above it. Note what happens as \(n\) grows: the mean scales with \(n\) but the peak term only with \(\sqrt{n}\), so <strong>the bigger the tower, the smoother the demand</strong> — the exact opposite of what a per-fixture allowance implies.</p>

<h2 id="int-demand">3 · Interactive: Hunter vs the probabilistic method</h2>
<p>Set the size of the tower and the fixture assumptions. The red curve is the classic Hunter fixture-unit estimate; the blue curve is the binomial estimate for the same building. The gap between them is pipe, pump and plant you may be buying for nothing.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Peak domestic demand — Hunter fixture units vs binomial probability</div>
    <div class="fsub">Hunter fitted to the published flush-tank curve as Q(gpm) = 1.968·WSFU^0.6746 (reproduces 44 gpm at 100 WSFU and 208 gpm at 1000). Binomial: Q = n·p·q&#102; + 1.96·q&#102;·√(n·p·(1−p)).</div>
  </div>
  <div class="chart-box"><canvas id="demandChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Dwelling units <span id="vU">250</span></label>
      <input type="range" id="sU" min="20" max="1200" value="250" step="10">
      <div class="hint">Apartments or equivalent occupancies served by the riser.</div>
    </div>
    <div class="ctrl">
      <label>WSFU per unit <span id="vW">6.0</span></label>
      <input type="range" id="sW" min="2" max="14" value="6" step="0.5">
      <div class="hint">Fixture units per dwelling, from the code schedule. Drives the Hunter curve only.</div>
    </div>
    <div class="ctrl">
      <label>Fixtures per unit <span id="vF">5.0</span></label>
      <input type="range" id="sF" min="2" max="12" value="5" step="0.5">
      <div class="hint">Physical fixture count. Drives the binomial estimate only.</div>
    </div>
    <div class="ctrl">
      <label>Fixture in-use probability p <span id="vP">0.020</span></label>
      <input type="range" id="sP" min="0.005" max="0.08" value="0.02" step="0.001">
      <div class="hint">Chance one fixture is running at the peak minute. Residential ≈ 0.01–0.03; hotels and offices higher.</div>
    </div>
    <div class="ctrl">
      <label>Flow per fixture <span id="vQf">0.15 L/s</span></label>
      <input type="range" id="sQf" min="0.06" max="0.35" value="0.15" step="0.01">
      <div class="hint">0.15 L/s = 9 L/min, a modern aerated tap or low-flow shower.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Hunter</div><div class="v" id="rHu">17.2 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Binomial</div><div class="v" id="rBi">5.2 <small>L/s</small></div></div>
    <div class="cell"><div class="k">Over-prediction</div><div class="v" id="rRt">3.3<small>×</small></div></div>
    <div class="cell"><div class="k">Riser bore · Hunter</div><div class="v" id="rDh">105 <small>mm</small></div></div>
    <div class="cell"><div class="k">Riser bore · binomial</div><div class="v" id="rDb">58 <small>mm</small></div></div>
  </div>
</div>
<p class="fig-note">A 250-unit tower comes out at <strong>17.2&nbsp;L/s</strong> on Hunter and <strong>5.2&nbsp;L/s</strong> on the binomial method — a factor of <strong>3.3</strong>. That propagates into roughly double the riser diameter, a pump set three times too large running permanently at the wrong end of its curve, and a storage volume that turns over so slowly the water goes stale. Note also the shape: the two curves diverge as the building grows, because Hunter never learned that large populations average out. Codes still mandate Hunter in many jurisdictions — so calculate both, size the pipe to the code, and size the <em>pumps and storage</em> to reality, with the calculation on record.</p>

<h2 id="zoning">4 · Pressure zoning — the 36-metre problem</h2>
<p>Zoning domestic water is arithmetic. If the highest fixture in a zone needs \(p_{min}\) and the lowest may not exceed \(p_{max}\), then the tallest possible zone is:</p>
<div class="eq">\[ H_{zone} \;=\; \frac{p_{max}-p_{min}}{0.0981} \qquad \text{(m, bar)} \]</div>
<p>With a 1.5&nbsp;bar minimum and a 5.0&nbsp;bar maximum that is <strong>35.7&nbsp;m — about ten storeys</strong>. A 600&nbsp;m tower would need <strong>seventeen</strong> pressure zones, each with its own tank or pump set. Nobody builds that. The way out is to separate the two constraints:</p>
<ul class="clean">
  <li><strong>Let the riser carry high pressure, and break it at the floor.</strong> Run the riser at its pipe rating (PN16 with a 1.5&nbsp;bar top residual → 148&nbsp;m of column) and fit a <strong>floor or apartment pressure-reducing valve</strong> on each branch. The riser zone is now set by pipe class, not by tap comfort: five zones instead of seventeen. The PRVs become the most safety-critical, most numerous, least-maintained components in the building — which is the trade you are making.</li>
  <li><strong>Use PRV cascades within a zone.</strong> Intermediate PRVs every few floors on the riser, each dropping the pressure back into the window, with the branch pressure checked at the top <em>and</em> bottom fixture of every PRV group.</li>
  <li><strong>Exploit gravity down-feed.</strong> Feeding down from a high tank gives the top floors of the zone the low pressure they need naturally, with the highest pressures at the bottom of the down-feed where PRVs are easiest to group.</li>
</ul>

<div class="callout warn">
  <span class="lbl">The two-fixture check that catches most defects</span>
  For every PRV group, check <strong>both</strong> ends: the <em>highest</em> fixture at design flow (does it still make \(p_{min}\) with the friction loss and the PRV's own fall-off?) and the <em>lowest</em> fixture at zero flow (does the static, with the PRV at its no-flow set-point, stay under \(p_{max}\)?). A PRV set to satisfy one end almost always violates the other, and the failure is silent: the top floor complains about the shower, the bottom floor quietly destroys its flexible hoses. Schedule both numbers, for every group, on the drawing.
</div>

<h2 id="int-zoning">5 · Interactive: the pressure window and how many zones it costs</h2>
<p>Set the acceptable fixture pressure window and the riser pipe class. The chart shows the pressure profile up the tower for two strategies: zoning purely on tap comfort, and zoning the riser on pipe class with floor PRVs doing the fine control. The shaded band is the acceptable fixture window.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Domestic riser pressure profile — comfort zoning vs riser zoning with floor PRVs</div>
    <div class="fsub">Static pressure p = 0.0981·h below each zone's supply point. Zone height = (p&#109;&#97;&#120; − p&#109;&#105;&#110;)/0.0981 for comfort zoning, and (PN &minus; p&#109;&#105;&#110;)/0.0981 for riser zoning, so the pipe reaches exactly its rating at the foot of the zone. Dashed lines are the fixture pressure limits.</div>
  </div>
  <div class="chart-box"><canvas id="zoneChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Tower height <span id="vH">600 m</span></label>
      <input type="range" id="sH" min="50" max="1000" value="600" step="10">
      <div class="hint">Height served by the domestic riser.</div>
    </div>
    <div class="ctrl">
      <label>Minimum fixture pressure <span id="vPn">1.5 bar</span></label>
      <input type="range" id="sPn" min="0.5" max="3" value="1.5" step="0.1">
      <div class="hint">Flowing pressure needed at the highest tap or mixer.</div>
    </div>
    <div class="ctrl">
      <label>Maximum fixture pressure <span id="vPx">5.0 bar</span></label>
      <input type="range" id="sPx" min="3" max="8" value="5" step="0.1">
      <div class="hint">Code cap at the lowest fixture. UPC 5.5 bar; many designers hold 4.5.</div>
    </div>
    <div class="ctrl">
      <label>Riser pressure class <span id="vPN">PN16</span></label>
      <input type="range" id="sPN" min="10" max="40" value="16" step="1">
      <div class="hint">Rating of the riser pipe and fittings (bar).</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Comfort zone height</div><div class="v" id="rZc">36 <small>m</small></div></div>
    <div class="cell"><div class="k">Zones · comfort only</div><div class="v" id="rNc">17</div></div>
    <div class="cell"><div class="k">Zones · riser + PRVs</div><div class="v" id="rNr">5</div></div>
    <div class="cell"><div class="k">Floor PRV groups</div><div class="v" id="rPrv">17</div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">The default case is stark: a 3.5&nbsp;bar comfort window is worth <strong>36&nbsp;m</strong>, so a 600&nbsp;m tower needs <strong>17</strong> tank-and-pump zones if the riser itself must stay inside the window. Zone the riser on PN16 instead and it falls to <strong>5</strong> — but you have now committed to roughly <strong>seventeen PRV groups</strong> per riser, one for every comfort-window's worth of height, every one of which must be scheduled, set, tested and maintained. Widen the window by a single bar and you save two or three zones; that is why the choice of tapware, and its permitted maximum pressure, is a decision the mechanical engineer should be making early rather than inheriting late.</p>

<h2 id="architecture">6 · Supply architectures</h2>
<ul class="clean">
  <li><strong>Gravity down-feed from high-level tanks.</strong> Transfer pumps lift water to tanks at the top of each zone or at the roof; the zones are fed downward by gravity through PRVs. Reliable — it keeps working through a pump or power failure, and the tank rides out demand peaks so the pumps see a smooth duty. The cost is structural (tanks high in a tower are heavy), spatial, and energetic, because every litre is lifted to the top whether it is used on floor 10 or floor 100.</li>
  <li><strong>Zone-boosted (direct) pumping.</strong> A pump set per zone draws from a lower break tank and boosts only that zone. No high-level storage, much less structural load, and each litre is lifted only as far as it actually goes — roughly half the energy of a roof-tank scheme. In exchange the system depends entirely on pumps and power, so redundancy and standby generation become part of the water strategy.</li>
  <li><strong>Cascade / series transfer.</strong> Ground tank → mid-level tank → upper tank, each stage lifting one zone height, exactly as in the fire system. Keeps every pump and pipe inside its pressure class and gives each stage a guaranteed suction source. Note carefully: <strong>cascading saves pressure class, not energy</strong> — the water still ends up at the same height, so the ρgh is unchanged.</li>
  <li><strong>Hydropneumatic / variable-speed boosters.</strong> Multi-pump variable-speed sets on a small pressure vessel, holding a set-point. Compact and responsive; the vessel exists to stop the pumps hunting on tiny demands, not to store water.</li>
</ul>

<h2 id="int-energy">7 · Interactive: the energy cost of height</h2>
<p>Pumping water up a tower is one of the few building loads that is pure physics — you cannot design it away, only avoid wasting it. This compares lifting every litre to a roof tank against boosting each litre only to its own zone.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Specific pumping energy — roof-tank gravity vs zone-boosted</div>
    <div class="fsub">E (kWh/m³) = H/(367·η). Roof-tank lifts every litre the full height; zone-boosted lifts to a mean height of H/2 for demand spread uniformly up the tower. Both include a friction and residual allowance.</div>
  </div>
  <div class="chart-box"><canvas id="energyChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Tower height <span id="veH">600 m</span></label>
      <input type="range" id="seH" min="50" max="1000" value="600" step="10">
      <div class="hint">Marker position on the curves.</div>
    </div>
    <div class="ctrl">
      <label>Daily demand <span id="veV">150 m³/d</span></label>
      <input type="range" id="seV" min="20" max="800" value="150" step="10">
      <div class="hint">Average daily potable consumption of the tower.</div>
    </div>
    <div class="ctrl">
      <label>Pump efficiency <span id="veE">70 %</span></label>
      <input type="range" id="seE" min="45" max="85" value="70" step="1">
      <div class="hint">Wire-to-water. Small boosters are often far worse than the catalogue suggests.</div>
    </div>
    <div class="ctrl">
      <label>Friction + residual <span id="veF">30 m</span></label>
      <input type="range" id="seF" min="10" max="80" value="30" step="1">
      <div class="hint">Added to the lift in both schemes.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Gravity scheme</div><div class="v" id="reG">2.45 <small>kWh/m³</small></div></div>
    <div class="cell"><div class="k">Zone-boosted</div><div class="v" id="reB">1.28 <small>kWh/m³</small></div></div>
    <div class="cell"><div class="k">Annual · gravity</div><div class="v" id="reAG">134 <small>MWh</small></div></div>
    <div class="cell"><div class="k">Annual · boosted</div><div class="v" id="reAB">70 <small>MWh</small></div></div>
    <div class="cell"><div class="k">Saving</div><div class="v" id="reS">48 <small>%</small></div></div>
  </div>
</div>
<p class="fig-note">At 600&nbsp;m the roof-tank scheme costs about <strong>2.45&nbsp;kWh/m³</strong> and the zone-boosted scheme about <strong>1.28</strong> — roughly <strong>half</strong>, because demand is spread up the tower and the average litre only travels half way. For a 150&nbsp;m³/day tower that is around 64&nbsp;MWh a year. It is not a reason to abandon gravity feed, whose reliability and peak-smoothing are worth a great deal; it <em>is</em> a reason to stop lifting everything to the roof by default, and to consider a hybrid — gravity for the upper zones and direct boosting for the lower ones, which is what most well-engineered megatall towers actually do.</p>

<h2 id="storage">8 · Storage, turnover and water quality</h2>
<p>Storage in a tall building is sized by three competing requirements, and the third is usually forgotten:</p>
<ul class="clean">
  <li><strong>Resilience</strong> — hours of supply if the town main fails. Drives volume up.</li>
  <li><strong>Peak smoothing and pump duty</strong> — enough buffer that the transfer pumps run steadily rather than chasing demand. Drives volume up.</li>
  <li><strong>Turnover and water quality</strong> — drives volume <em>down</em>. Chlorine residual decays exponentially; at typical temperatures a residual is largely gone within 2–3 days. Storage sized for a generous four-day outage is storage that delivers biologically active water on a normal Tuesday.</li>
</ul>
<p>Design for a <strong>turnover of roughly one day</strong> across the whole storage chain, and get resilience from redundancy and multiple incoming connections rather than from volume. Compartment every tank into at least two cells so one can be cleaned without shutting the tower down, arrange inlets and outlets diagonally opposite so the tank actually flushes instead of short-circuiting, and never let a tank become a plug-flow dead volume with the inlet next to the outlet. Where residence time cannot be avoided, re-chlorinate or fit UV at the tank outlet and monitor the residual continuously.</p>

<h2 id="backflow">9 · Backflow, cross-connection and material selection</h2>
<ul class="clean">
  <li><strong>Protect by hazard category, at every zone boundary.</strong> An air gap (AA/AB) at the break tank is the only absolute protection and should be the primary barrier at the building inlet. Below that, RPZ valves for high-hazard connections — cooling towers, irrigation with fertiliser injection, water features, chemical dosing — and double check valves for lower-hazard ones. In a tower the risk is amplified: a burst on a low floor can pull a substantial vacuum on the riser above it.</li>
  <li><strong>Fit vacuum breakers at the top of every riser.</strong> When a riser drains, it will try to siphon; without a vacuum breaker it pulls back through fixtures.</li>
  <li><strong>Choose pipe for the pressure class <em>and</em> the water.</strong> Copper, stainless and PPR/PEX all behave differently at 16&nbsp;bar and at 60&nbsp;°C. Watch velocity limits for erosion-corrosion in copper (keep below ~1.5&nbsp;m/s on hot recirculation), and check that plastic system pressure ratings are stated <em>at the operating temperature</em>, not at 20&nbsp;°C — the de-rating is severe.</li>
  <li><strong>Separate the fire and domestic storage, or prove the turnover.</strong> Shared tanks look efficient and create a large stagnant fire reserve inside the potable system.</li>
</ul>

<h2 id="hammer">10 · Transients in tall risers</h2>
<p>A 600&nbsp;m riser full of water is a substantial mass, and domestic systems are full of fast-closing devices — solenoid valves, ceramic-disc taps, washing machines. The Joukowsky pressure rise for an instantaneous stop is \( \Delta p = \rho a \Delta v\); with a wave speed of about 1,200&nbsp;m/s in steel, a 1&nbsp;m/s velocity change gives roughly <strong>12&nbsp;bar</strong> on top of whatever static pressure is already there. On a low floor of a tall zone that is enough to exceed the pipe rating<sup class="cite">[6]</sup>. Provide arrestors at fast-acting fixtures and at the ends of long branches, slow the closure of solenoid and motorised valves, and check the pump check-valve arrangement on trip. The full treatment of the physics is in <a href="water-hammer-control-valve.html">valve closure and water hammer</a>.</p>

<h2 id="install">11 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Schedule every PRV with two numbers</strong> — set-point at design flow and expected static at the lowest fixture — and commission against both. Record the as-set values; the single most useful document for the facilities team over the building's life.</li>
  <li><strong>Fit isolation and a strainer upstream of every PRV</strong>, with a test point either side. A PRV you cannot isolate is a PRV nobody will ever service.</li>
  <li><strong>Support the riser for weight and movement.</strong> A full DN150 riser is roughly 40&nbsp;kg per metre with its water; over 150&nbsp;m of zone that is six tonnes hanging on the shaft steel. Add thermal and structural movement and the anchor and guide design becomes a structural submission, not a bracket schedule.</li>
  <li><strong>Chlorinate and flush systematically, bottom-up, and sample per zone.</strong> Partial disinfection of a zoned system is the classic reason a tower fails its microbiological clearance twice.</li>
  <li><strong>Pressure-test by zone, at zone rating</strong> — testing the whole riser at the highest zone's pressure is how PN10 branch work gets destroyed before handover.</li>
  <li><strong>Meter every zone.</strong> Zone-level metering is what turns an unexplained consumption rise into a located leak, and it costs almost nothing at construction. The rationale is the same as in <a href="non-revenue-water-leakage.html">non-revenue water</a>: you cannot manage losses you cannot see.</li>
  <li><strong>Prove the transfer control logic on site</strong> — level switches, pump duty rotation, low-level cut-out, and the alarm on tank overflow. Overflowing a tank on level 90 is an expensive way to discover a float switch was wired inverted.</li>
</ul>

<h2 id="checklist">12 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Calculate demand twice</strong> — code method for compliance, probabilistic method for reality; size pumps and storage on the second.</li>
  <li><strong>Fix the pressure window early</strong> — agree the tapware maximum with the architect; it decides the zoning.</li>
  <li><strong>Zone the riser on pipe class and control at the floor</strong>, unless the tower is short enough to zone on comfort alone.</li>
  <li><strong>Check both ends of every PRV group</strong> — highest fixture flowing, lowest fixture static.</li>
  <li><strong>Choose the architecture on energy and reliability together</strong> — hybrid gravity/boosted is usually the honest answer.</li>
  <li><strong>Size storage for one-day turnover</strong>, get resilience from redundancy, compartment every tank.</li>
  <li><strong>Protect against backflow by hazard at every boundary</strong>, with air gaps at the inlet and vacuum breakers at riser tops.</li>
  <li><strong>Assess transients</strong> — arrestors, slow closure, and a check on the pump trip case.</li>
  <li><strong>Commission on paper first</strong> — PRV schedules, zone test pressures, disinfection plan and zone metering, all issued before anyone opens a valve.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Domestic water in a megatall is governed by a <strong>3.5&nbsp;bar comfort window worth only 36&nbsp;m of building</strong>, so either you build seventeen zones or you zone the riser on pipe class and control pressure at the floor with PRVs you then have to schedule, test and maintain. Size the demand probabilistically rather than with a 1940 curve that over-predicts by three, keep storage turning over in about a day instead of hoarding it, boost each litre only as far as it actually travels, and check both the top and the bottom fixture of every pressure group — because in this system the complaint from the penthouse and the burst hose in the basement have the same root cause.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Hunter, R.B. <em>Methods of Estimating Loads in Plumbing Systems</em>, National Bureau of Standards Report BMS65 (1940) — the origin of the fixture-unit method.</li>
  <li>Uniform Plumbing Code (UPC) / International Plumbing Code (IPC) — fixture-unit schedules, maximum and minimum fixture pressures, PRV requirements; and the Saudi Building Code <em>SBC 701</em> plumbing provisions.</li>
  <li>IAPMO <em>Water Demand Calculator</em> and its supporting research (Buchberger et&nbsp;al.) — probabilistic peak demand for modern low-flow fixtures; and DIN 1988-300 / EN 806-3 sizing methods.</li>
  <li>CIBSE <em>Guide G — Public Health and Plumbing Engineering</em>; and the Institute of Plumbing <em>Plumbing Engineering Services Design Guide</em>.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — vertical zoning of domestic water, storage location and transfer strategies.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Service Water Heating and Water Distribution chapters; and AWWA M14 <em>Backflow Prevention and Cross-Connection Control</em>.</li>
  <li>BS 8558 / BS EN 806 — design, installation, testing and maintenance of services supplying water for domestic use, including disinfection.</li>
  <li>WHO <em>Water Safety in Buildings</em> — storage turnover, residual management and microbiological risk in building water systems.</li>
</ol>

<div class="tags">#DomesticWater #PotableWater #Plumbing #TallBuildings #MegatallBuildings #PressureZoning #PRV #BoosterPumps #HunterCurve #WaterDemandCalculator #FixtureUnits #WaterStorage #Turnover #Backflow #CrossConnection #Legionella #WaterHammer #SpecificEnergy #GravityFeed #Hydropneumatic #WaterQuality #Commissioning #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const BARM=0.0981;

/* ---------- CHART 1 : demand ---------- */
const HU_A=1.968, HU_B=0.6746, GPM=0.0630902;      // fitted Hunter curve, gpm -> L/s
const hunter=w=>GPM*HU_A*Math.pow(Math.max(w,1),HU_B);
const binom=(n,p,qf)=>n*p*qf+1.96*qf*Math.sqrt(n*p*(1-p));
const bore=q=>1000*Math.sqrt(4*(q/1000)/(Math.PI*2.0));   // mm at 2.0 m/s
const sU=document.getElementById('sU'),sW=document.getElementById('sW'),sF=document.getElementById('sF'),
      sP=document.getElementById('sP'),sQf=document.getElementById('sQf');
let demandChart=new Chart(document.getElementById('demandChart'),{
  data:{datasets:[
    {type:'line',label:'Hunter fixture-unit method',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:3},
    {type:'line',label:'Binomial probability method',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your tower',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:20,max:1200,title:{display:true,text:'Dwelling units served',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Peak design flow (L/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} L/s at ${fmt0(c.parsed.x)} units`}}}}
});
function updDemand(){
  const U=+sU.value,W=+sW.value,F=+sF.value,p=+sP.value,qf=+sQf.value;
  document.getElementById('vU').textContent=U;
  document.getElementById('vW').textContent=fmt1(W);
  document.getElementById('vF').textContent=fmt1(F);
  document.getElementById('vP').textContent=fmt3(p);
  document.getElementById('vQf').textContent=fmt2(qf)+' L/s';
  const xs=[];for(let u=20;u<=1200;u+=10)xs.push(u);
  demandChart.data.datasets[0].data=xs.map(u=>({x:u,y:+hunter(u*W).toFixed(2)}));
  demandChart.data.datasets[1].data=xs.map(u=>({x:u,y:+binom(u*F,p,qf).toFixed(2)}));
  const h=hunter(U*W), b=binom(U*F,p,qf);
  demandChart.data.datasets[2].data=[{x:U,y:+h.toFixed(2)}];
  demandChart.update('none');
  document.getElementById('rHu').innerHTML=fmt1(h)+' <small>L/s</small>';
  document.getElementById('rBi').innerHTML=fmt1(b)+' <small>L/s</small>';
  document.getElementById('rRt').innerHTML=fmt1(h/b)+'<small>×</small>';
  document.getElementById('rDh').innerHTML=fmt0(bore(h))+' <small>mm</small>';
  document.getElementById('rDb').innerHTML=fmt0(bore(b))+' <small>mm</small>';
}
[sU,sW,sF,sP,sQf].forEach(s=>s.addEventListener('input',updDemand));updDemand();

/* ---------- CHART 2 : zoning ---------- */
const sH=document.getElementById('sH'),sPn=document.getElementById('sPn'),
      sPx=document.getElementById('sPx'),sPN=document.getElementById('sPN');
let zoneChart=new Chart(document.getElementById('zoneChart'),{
  data:{datasets:[
    {type:'line',label:'Comfort zoning (tank per zone)',data:[],borderColor:'#c0392b',borderWidth:2.5,pointRadius:0,order:3},
    {type:'line',label:'Riser zoning + floor PRVs',data:[],borderColor:'#1b4f72',borderWidth:3,pointRadius:0,order:2}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0,title:{display:true,text:'Static pressure in the riser (bar)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Height above grade (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.x)} bar at ${fmt0(c.parsed.y)} m`}},
      annotation:{annotations:{
        lo:{type:'line',scaleID:'x',xScaleID:'x',value:0,borderColor:'#1e8449',borderWidth:1.4,borderDash:[5,4],label:{display:true,content:'min',position:'start',font:{size:10,family:'DM Sans'},color:'#1e8449',backgroundColor:'rgba(255,255,255,0.85)'}},
        hi:{type:'line',scaleID:'x',xScaleID:'x',value:0,borderColor:'#b9770e',borderWidth:1.4,borderDash:[5,4],label:{display:true,content:'max',position:'end',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function saw(H,zh,top){const d=[];const n=Math.ceil(H/zh);
  for(let k=0;k<n;k++){const b=k*zh,t=Math.min((k+1)*zh,H);
    d.push({x:+(top+(t-b)*BARM).toFixed(2),y:+b.toFixed(0)});
    d.push({x:+top.toFixed(2),y:+t.toFixed(0)});}
  return d;}
function updZone(){
  const H=+sH.value,pn=+sPn.value,px=+sPx.value,PN=+sPN.value;
  document.getElementById('vH').textContent=H+' m';
  document.getElementById('vPn').textContent=fmt1(pn)+' bar';
  document.getElementById('vPx').textContent=fmt1(px)+' bar';
  document.getElementById('vPN').textContent='PN'+PN;
  const zc=Math.max(1,(px-pn))/BARM, zr=Math.max(1,(PN-pn))/BARM;
  zoneChart.data.datasets[0].data=saw(H,zc,pn);
  zoneChart.data.datasets[1].data=saw(H,zr,pn);
  zoneChart.options.scales.x.max=Math.max(PN*1.08,px*1.15);
  zoneChart.options.scales.y.max=H;
  const an=zoneChart.options.plugins.annotation.annotations;
  an.lo.value=pn; an.lo.label.content=pn.toFixed(1)+' bar min';
  an.hi.value=px; an.hi.label.content=px.toFixed(1)+' bar max';
  zoneChart.update('none');
  const nc=Math.ceil(H/zc), nr=Math.ceil(H/zr);
  document.getElementById('rZc').innerHTML=fmt0(zc)+' <small>m</small>';
  document.getElementById('rNc').textContent=nc;
  document.getElementById('rNr').textContent=nr;
  document.getElementById('rPrv').textContent=nc;
  const v=document.getElementById('rVd');
  if(px<=pn) v.innerHTML='<span class="badge bad">no usable window</span>';
  else if(nc<=3) v.innerHTML='<span class="badge good">comfort zoning is viable</span>';
  else if(nr<=6) v.innerHTML='<span class="badge warn">riser zoning + PRVs needed</span>';
  else v.innerHTML='<span class="badge bad">many zones either way</span>';
}
[sH,sPn,sPx,sPN].forEach(s=>s.addEventListener('input',updZone));updZone();

/* ---------- CHART 3 : energy ---------- */
const seH=document.getElementById('seH'),seV=document.getElementById('seV'),
      seE=document.getElementById('seE'),seF=document.getElementById('seF');
const spec=(lift,eta)=>lift/(367*eta);
let energyChart=new Chart(document.getElementById('energyChart'),{
  data:{datasets:[
    {type:'line',label:'Roof-tank gravity (lift all to top)',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:3},
    {type:'line',label:'Zone-boosted (lift to mean height)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your tower',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:50,max:1000,title:{display:true,text:'Tower height (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Specific pumping energy (kWh/m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt2(c.parsed.y)} kWh/m³ at ${fmt0(c.parsed.x)} m`}}}}
});
function updEnergy(){
  const H=+seH.value,V=+seV.value,eta=+seE.value/100,fr=+seF.value;
  document.getElementById('veH').textContent=H+' m';
  document.getElementById('veV').textContent=V+' m³/d';
  document.getElementById('veE').textContent=(eta*100).toFixed(0)+' %';
  document.getElementById('veF').textContent=fr+' m';
  const xs=[];for(let h=50;h<=1000;h+=10)xs.push(h);
  energyChart.data.datasets[0].data=xs.map(h=>({x:h,y:+spec(h+fr,eta).toFixed(3)}));
  energyChart.data.datasets[1].data=xs.map(h=>({x:h,y:+spec(h/2+fr,eta).toFixed(3)}));
  const g=spec(H+fr,eta), b=spec(H/2+fr,eta);
  energyChart.data.datasets[2].data=[{x:H,y:+g.toFixed(3)}];
  energyChart.update('none');
  const yr=V*365;
  document.getElementById('reG').innerHTML=fmt2(g)+' <small>kWh/m³</small>';
  document.getElementById('reB').innerHTML=fmt2(b)+' <small>kWh/m³</small>';
  document.getElementById('reAG').innerHTML=fmt0(yr*g/1000)+' <small>MWh</small>';
  document.getElementById('reAB').innerHTML=fmt0(yr*b/1000)+' <small>MWh</small>';
  document.getElementById('reS').innerHTML=fmt0(100*(1-b/g))+' <small>%</small>';
}
[seH,seV,seE,seF].forEach(s=>s.addEventListener('input',updEnergy));updEnergy();

window.addEventListener('load',function(){try{demandChart.resize();zoneChart.resize();energyChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='domestic-water-tall-buildings', cat='plumbing', mins=18,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Domestic Water Supply in Megatall Buildings: Demand, Pressure Zoning, PRVs &amp; the Energy of Height',
    reg_title='Domestic Water Supply in Megatall Buildings: Demand, Pressure Zoning, PRVs & the Energy of Height',
    reg_tag='Plumbing · Domestic Water · Tall Buildings',
    breadcrumb='Plumbing &amp; Drainage',
    tag_line='Plumbing &middot; Domestic Water &middot; Pressure Zoning &middot; Megatall Buildings',
    desc='Domestic water supply in megatall buildings from a design perspective: why Hunter fixture units over-predict peak demand by three times, the 3.5 bar fixture pressure window that is worth only 36 m of building, riser zoning on pipe class with floor PRVs, gravity down-feed vs zone-boosted pumping and the energy of height, storage turnover and water quality, backflow protection and transients — with three interactive charts, worked numbers and installation tricks.',
    og_desc='The comfort window at a tap is 3.5 bar — worth 36 m of tower. Why that forces seventeen pressure zones unless you zone the riser on pipe class, why Hunter over-sizes by 3x, and what height really costs in kWh/m3 — in three interactive charts.',
    ld_desc='A design-perspective guide to domestic water supply in megatall buildings: probabilistic vs fixture-unit demand estimation, the fixture pressure window and vertical zoning, floor PRVs, gravity vs boosted architectures and specific pumping energy, storage turnover, backflow protection and transients.',
    img_alt='Technical cutaway of a megatall tower&rsquo;s domestic water system showing break tanks and booster pump sets at intervals up the core, a supply riser divided into pressure zones, and floor-level pressure-reducing valve groups serving the apartments',
    en_tag='Plumbing &amp; Drainage &middot; Domestic Water &middot; Pressure Zoning &middot; Megatall',
    en_title='Domestic Water Supply in Megatall Buildings: Demand, Pressure Zoning, PRVs &amp; the Energy of Height',
    en_excerpt='Fire water reaches the top floor once; domestic water has to reach it every time somebody opens a tap. The pressure window at a fixture is only 3.5&nbsp;bar wide &mdash; worth 36&nbsp;m of building &mdash; so a 600&nbsp;m tower needs seventeen zones unless you zone the riser on pipe class and control at the floor. Why the 1940 Hunter curve over-predicts modern demand by three times, gravity down-feed vs zone-boosted pumping and what height costs in kWh/m&sup3;, storage turnover and water quality, backflow and transients &mdash; with three interactive charts and installation tricks.',
    en_search='domestic water potable water supply tall buildings megatall supertall high-rise plumbing demand estimation Hunter curve fixture units WSFU water supply fixture unit binomial probability IAPMO water demand calculator DIN 1988 EN 806 simultaneous demand diversity pressure zoning fixture pressure window minimum flowing pressure maximum static pressure PRV pressure reducing valve floor PRV riser zoning pipe class PN16 break tank transfer pump booster pump hydropneumatic variable speed gravity down-feed roof tank cascade series pumping specific energy kWh per m3 storage turnover water quality chlorine residual stagnation compartmented tank backflow prevention cross connection air gap RPZ vacuum breaker water hammer Joukowsky arrestor disinfection zone metering commissioning MEP building services',
    ar_title='إمداد المياه في المباني فائقة الارتفاع: الطلب وتقسيم الضغط وصمامات تخفيض الضغط وثمن الارتفاع',
    ar_excerpt='مياه الحريق تصل إلى الطابق الأخير مرة واحدة، أما مياه الاستخدام فيجب أن تصل كلما فُتح صنبور. نافذة الضغط المقبولة عند نقطة الاستخدام لا تتجاوز ٣٫٥ بار — أي ما يعادل ٣٦ مترًا من ارتفاع المبنى — فيحتاج برج ٦٠٠ متر إلى سبعة عشر منطقة ضغط ما لم تُقسّم المواسير الصاعدة حسب درجة تحمّلها وتُضبط الضغوط عند الأدوار. ولماذا يبالغ منحنى هَنتر لعام ١٩٤٠ في تقدير الطلب ثلاثة أضعاف، والتغذية بالجاذبية مقابل الضخ لكل منطقة وثمن الارتفاع بالكيلوواط ساعة لكل متر مكعب، ودوران التخزين وجودة المياه، والارتداد العكسي والمطرقة المائية — مع ثلاثة رسوم تفاعلية وحِيَل التنفيذ.',
    ar_search='domestic water potable supply tall buildings megatall plumbing Hunter fixture units binomial IAPMO water demand calculator pressure zoning PRV break tank booster pump gravity roof tank specific energy storage turnover backflow air gap RPZ water hammer المياه الصالحة للشرب إمداد المياه المباني الشاهقة المباني فائقة الارتفاع السباكة تقدير الطلب منحنى هنتر وحدات التجهيزات الصحية الاحتمال الثنائي حاسبة الطلب على المياه الطلب المتزامن معامل التزامن تقسيم الضغط الرأسي نافذة الضغط الضغط الأدنى الضغط الأقصى صمام تخفيض الضغط صمامات الأدوار درجة تحمل الماسورة خزان الفصل مضخة النقل مضخة التعزيز الضغط الهوائي متغير السرعة التغذية بالجاذبية خزان السطح الضخ المتتالي الطاقة النوعية دوران التخزين جودة المياه الكلور المتبقي الركود الخزان المقسم منع الارتداد العكسي التوصيل المتقاطع الفجوة الهوائية كاسر التفريغ المطرقة المائية جوكوفسكي ممتص الصدمات التعقيم عدادات المناطق التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
