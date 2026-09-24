# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Two towers of identical height and identical total area can have completely different cooling loads, different plant, different riser strategies and different economics — because one has a 30&nbsp;m floor plate and the other a 60&nbsp;m one. The slender tower carries <strong>twice as much façade per square metre of floor</strong>, which makes it an <strong>envelope-driven building</strong> where 60&nbsp;% of the load comes through the glass; the wide one is internally driven, where the people, lights and equipment dominate. Almost every subsequent decision — where the plant goes, whether perimeter systems are needed, how the zones are controlled, what the diversity is — follows from which of those two buildings you are designing, and it is decided by the architect's massing long before the first load calculation.</p>

<h2 id="geometry">1 · Geometry is the load</h2>
<p>For a square floor plate of side \(s\) and floor-to-floor height \(h\), the façade area per unit of floor area is simply:</p>
<div class="eq">\[ \frac{A_{façade}}{A_{floor}} = \frac{4sh}{s^2} = \frac{4h}{s} \]</div>
<p>It depends on the <em>plate size</em>, not on the building height at all. A 30&nbsp;m plate at 4&nbsp;m floor-to-floor carries <strong>0.53&nbsp;m² of façade per m² of floor</strong>; a 60&nbsp;m plate carries <strong>0.27</strong>. That single ratio decides the character of the building:</p>
<ul class="clean">
  <li><strong>Slender towers are envelope-dominated.</strong> Solar and conduction gains scale with that ratio, so they peak sharply with orientation and time of day, they vary enormously between façades, and they demand perimeter treatment and orientation-based zoning.</li>
  <li><strong>Wide-plate towers are internally dominated.</strong> Lights, equipment and people dominate, loads are steadier, deep space needs cooling all year even in winter, and simultaneous heating and cooling on the same floor becomes a real design problem.</li>
  <li><strong>Residential and hotel towers are almost always slender</strong> — because every room needs a window — which is why they behave so differently from offices and why office rules of thumb mislead badly when applied to them.</li>
</ul>

<h2 id="int-geom">2 · Interactive: envelope versus internal load</h2>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Load split by floor plate size</div>
    <div class="fsub">Façade ratio = 4h/s for a square plate. Envelope load = ratio × (U·ΔT + SHGC · solar · sunlit fraction); internal load from lighting, equipment and occupancy densities.</div>
    <a class="calc-link" href="calculators.html#calc-clr"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h2M12 10h2M16 10h.01M8 14h2M12 14h2M16 14h.01M8 18h6"/></svg>Open Cooling load as a calculator</a>
  </div>
  <div class="chart-box"><canvas id="geoChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Floor plate side <span id="vS">45 m</span></label>
      <input type="range" id="sS" min="18" max="90" value="45" step="1">
      <div class="hint">Square-equivalent side. Slender residential plates are 20–35 m; office plates 40–60 m.</div>
    </div>
    <div class="ctrl">
      <label>Glazing U-value <span id="vU">1.80 W/m²K</span></label>
      <input type="range" id="sU" min="0.8" max="3.5" value="1.8" step="0.05">
      <div class="hint">Whole-façade average including frames and spandrel.</div>
    </div>
    <div class="ctrl">
      <label>Solar heat gain coefficient <span id="vG">0.25</span></label>
      <input type="range" id="sG" min="0.1" max="0.6" value="0.25" step="0.01">
      <div class="hint">Effective SHGC of the glazing system including shading.</div>
    </div>
    <div class="ctrl">
      <label>Internal gain density <span id="vI">35 W/m²</span></label>
      <input type="range" id="sI" min="15" max="80" value="35" step="1">
      <div class="hint">Lighting plus equipment plus people. Trading floors and data-rich offices far higher.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Façade ratio</div><div class="v" id="rFr">0.356 <small>m²/m²</small></div></div>
    <div class="cell"><div class="k">Envelope load</div><div class="v" id="rEn">35 <small>W/m²</small></div></div>
    <div class="cell"><div class="k">Internal load</div><div class="v" id="rIn">35 <small>W/m²</small></div></div>
    <div class="cell"><div class="k">Envelope share</div><div class="v" id="rSh">50 <small>%</small></div></div>
    <div class="cell"><div class="k">Character</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rCh"></span></div></div>
  </div>
</div>
<p class="fig-note">At a 45&nbsp;m plate the two halves are almost exactly balanced. Slide down to a 30&nbsp;m residential plate and the envelope takes <strong>60&nbsp;%</strong>; slide up to 60&nbsp;m and it falls to <strong>43&nbsp;%</strong>. These are different buildings. The slender one wants perimeter fan-coils or an active façade, tight orientation zoning, and a plant sized for a sharp, orientation-dependent peak. The wide one wants deep-plan air distribution, year-round cooling in the core, and careful attention to simultaneous heating and cooling. <strong>Applying the wrong template is the most consequential early error in tall-building HVAC</strong>, and the two templates are separated by nothing more than a dimension on the architect's plan.</p>

<h2 id="height">3 · What actually changes with height</h2>
<p>Height itself changes less than people expect, but what it does change is systematic:</p>
<ul class="clean">
  <li><strong>Shading disappears.</strong> Near grade a tower is shaded by its neighbours for much of the day; above the urban canopy it is not. The upper third of a tower can receive close to <strong>twice the solar gain</strong> of the lower third on the same orientation, for identical glass — and that is a zoning decision, not a glazing one.</li>
  <li><strong>Air temperature falls slightly</strong> — roughly 0.65&nbsp;°C per 100&nbsp;m — which very marginally helps.</li>
  <li><strong>Wind increases sharply</strong>, raising the external film coefficient and therefore the conduction gain, and driving the infiltration described in <a href="stack-effect-tall-buildings.html">stack effect</a>.</li>
  <li><strong>Infiltration becomes a real load</strong> rather than a rounding error, and it is <em>not</em> uniform — it is concentrated below the neutral plane in winter and above it in a Gulf summer.</li>
  <li><strong>Occupancy patterns differ by zone, but the chilled-water peaks mostly do not.</strong> Offices, hotel rooms and residences keep different hours, and a hotel's busiest evening or a residence's late-night occupancy is real. On chilled water in a Gulf summer, though, all three draw their peak in the same afternoon: offices between 14:00 and 15:00, hotel rooms and residences between 16:00 and 17:00, because sun on glass, infiltration and outdoor air dominate each of them. Section&nbsp;4 shows how much diversity that leaves.</li>
</ul>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Solar gain by height, for the same façade</div>
    <div class="fsub">Unshaded fraction rises through the urban canopy and saturates above it. Gain shown relative to a fully exposed façade at the same orientation.</div>
  </div>
  <div class="chart-box"><canvas id="solChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Surrounding building height <span id="vNh">60 m</span></label>
      <input type="range" id="sNh" min="10" max="200" value="60" step="5">
      <div class="hint">Typical height of the neighbouring urban fabric.</div>
    </div>
    <div class="ctrl">
      <label>Street width ratio <span id="vW">1.2</span></label>
      <input type="range" id="sW" min="0.3" max="4" value="1.2" step="0.1">
      <div class="hint">Street width ÷ neighbour height. Wider streets mean less shading low down.</div>
    </div>
    <div class="ctrl">
      <label>Peak solar on façade <span id="vSo">500 W/m²</span></label>
      <input type="range" id="sSo" min="200" max="900" value="500" step="10">
      <div class="hint">Peak incident irradiance on the design orientation.</div>
    </div>
    <div class="ctrl">
      <label>Your floor height <span id="vZ">400 m</span></label>
      <input type="range" id="sZ" min="5" max="700" value="400" step="5">
      <div class="hint">Height of the floor being assessed.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Unshaded fraction</div><div class="v" id="rUf">1.00</div></div>
    <div class="cell"><div class="k">Solar on this floor</div><div class="v" id="rSf">500 <small>W/m²</small></div></div>
    <div class="cell"><div class="k">At level 5</div><div class="v" id="rS5">200 <small>W/m²</small></div></div>
    <div class="cell"><div class="k">Top vs bottom</div><div class="v" id="rRt">2.5<small>×</small></div></div>
    <div class="cell"><div class="k">Zoning</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rZv"></span></div></div>
  </div>
</div>
<p class="fig-note">The same glass, the same orientation, and a <strong>2.5× difference in peak solar gain</strong> between the podium floors and the crown. Designing every floor to the same W/m² therefore over-sizes the bottom of the tower and under-sizes the top — and because plant is zoned vertically anyway, the fix is nearly free: <strong>apply different load densities to different vertical zones</strong>, and check the shading with a real solar study rather than a rule of thumb. Note also that the shading benefit at low level is a <em>borrowed</em> benefit; it disappears if the neighbouring site is redeveloped taller, which on a prime site over a sixty-year life is not a remote possibility.</p>

<h2 id="int-diversity">4 · Interactive: how much diversity a mixed-use tower really has</h2>
<div class="callout warn"><span class="lbl">Corrected September 2026</span>An earlier version of this section said a mixed-use tower could be sized at 0.5&ndash;0.6 of its connected load, and showed a 50&nbsp;MW connected load becoming a 30&nbsp;MW plant. That model applied occupancy diversity to the whole load, including the weather-driven part, which does not diversify. The section, the chart and the summary have been rebuilt on the hourly block calculation in the companion article, <a href="chilled-water-diversity-megatall.html">Chilled-Water Diversity in Megatall Towers</a>. For a Gulf mixed-use tower the figure is about <strong>0.86</strong>.</div>
<p>Connected load is the sum of every zone's own peak. The simultaneous load, the <strong>block load</strong>, is the highest hour of their sum, and it is always less, because not everything peaks in the same hour. The block load is the number the codes size equipment on. ASHRAE 90.1 (&sect;6.4.2.1) and the Saudi Building Code (SBC&nbsp;501, &sect;312.1) require system design loads to be calculated to ANSI/ASHRAE/ACCA Standard&nbsp;183. In practice that means an hour-by-hour calculation using the load methods of the ASHRAE <em>Fundamentals</em> handbook. How far the block falls below the connected load depends on what drives the load:</p>
<ul class="clean">
  <li><strong>Weather-driven load</strong> means solar gain, conduction, infiltration and outdoor air at its design rate. It gets <strong>no usage diversity</strong>. The sun reaches every west-facing floor at the same moment, whether the rooms are let or not. Its only diversity is <em>time</em>: east and west façades peak hours apart.</li>
  <li><strong>Usage-driven load</strong> means people, lighting, equipment, demand-controlled ventilation and process loads. It is statistical. Not every room is let and not every desk is busy, and the effect grows with the number of independent units. Measured office equipment runs at about 60&ndash;75&nbsp;% of its peak draw at the design hour (Wilkins &amp; Hosni, <em>ASHRAE Journal</em>, 2011). ASHRAE research project RP-1093 built a library of lighting and equipment diversity factors from metered office buildings for exactly this use.</li>
</ul>
<p>In a glass tower in a hot climate, more than half of the connected load is weather-driven. That is why the tower's diversity is much smaller than a rule of thumb built on occupancy alone would suggest.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Simultaneous versus connected load, split by what drives it</div>
    <div class="fsub">Tower coincidence = w&middot;c<sub>w</sub> + (1&minus;w)&middot;[u&#8734; + (1&minus;u&#8734;)/&radic;n]. Only the usage-driven share falls as the number of independent zones grows. The weather-driven share stays at its time coincidence however many floors are added. The load axis runs to the connected load, so the right-hand scale reads the tower coincidence directly. The defaults reproduce the hour-by-hour coastal Gulf tower in the companion article.</div>
    <a class="calc-link" href="calculators.html#calc-clr"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h2M12 10h2M16 10h.01M8 14h2M12 14h2M16 14h.01M8 18h6"/></svg>Open Cooling load as a calculator</a>
  </div>
  <div class="chart-box"><canvas id="divChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Independent zones <span id="vN">60</span></label>
      <input type="range" id="sN" min="1" max="200" value="60" step="1">
      <div class="hint">Groups whose usage is genuinely independent: tenancies, hotel room blocks, apartment floors.</div>
    </div>
    <div class="ctrl">
      <label>Weather-driven share <span id="vWs">0.56</span></label>
      <input type="range" id="sWs" min="0.2" max="0.8" value="0.56" step="0.01">
      <div class="hint">Envelope, solar, infiltration and design ventilation as a share of the connected load. Companion model: 0.56 for a coastal Gulf tower, 0.51 inland.</div>
    </div>
    <div class="ctrl">
      <label>Time coincidence of weather load <span id="vCw">0.91</span></label>
      <input type="range" id="sCw" min="0.8" max="1" value="0.91" step="0.01">
      <div class="hint">East and west façades peak hours apart, and that is all the diversity these loads get. Companion model: 0.91 coastal, 0.87 inland.</div>
    </div>
    <div class="ctrl">
      <label>Usage asymptote <span id="vDa">0.76</span></label>
      <input type="range" id="sDa" min="0.4" max="1" value="0.76" step="0.01">
      <div class="hint">What a very large group of people-driven loads averages at the tower&rsquo;s peak hour. Measured office equipment gives 0.60&ndash;0.75; lighting and people run higher.</div>
    </div>
    <div class="ctrl">
      <label>Connected load <span id="vC">50 MW</span></label>
      <input type="range" id="sC" min="5" max="150" value="50" step="1">
      <div class="hint">Sum of every zone&rsquo;s individual peak.</div>
    </div>
    <div class="ctrl">
      <label>Redundancy <span id="vR">N+1</span></label>
      <input type="range" id="sR" min="0" max="3" value="1" step="1">
      <div class="hint">Standby units added to a six-unit duty set.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Tower coincidence</div><div class="v" id="rDf">0.858</div></div>
    <div class="cell"><div class="k">Simultaneous peak</div><div class="v" id="rSp">42.9 <small>MW</small></div></div>
    <div class="cell"><div class="k">Capacity avoided</div><div class="v" id="rAv">7.1 <small>MW</small></div></div>
    <div class="cell"><div class="k">Installed with N+1</div><div class="v" id="rIc">50.0 <small>MW</small></div></div>
    <div class="cell"><div class="k">vs connected load</div><div class="v" id="rVn">0 <small>%</small></div></div>
    <div class="cell"><div class="k">A blanket 0.55 would be</div><div class="v" id="rBl">36 <small>% short</small></div></div>
  </div>
</div>
<p class="fig-note">With the defaults, the tower coincidence is about <strong>0.86</strong>, so a 50&nbsp;MW connected load is a <strong>43&nbsp;MW</strong> plant. N+1 on a six-unit set brings the installed capacity back to roughly the connected load. In a hot climate, <strong>diversity pays for the standby chiller; it does not halve the plant</strong>. A blanket 0.55 applied to this tower would leave the plant <strong>36&nbsp;% short</strong> on the design day. Lower the weather-driven share, as in a cooler climate or a building dominated by people and equipment, and the figure moves down. It moves slowly, though, because the usage-driven share also has its own floor. Take too much diversity and the plant is short on the first hot afternoon. Take none and the plant is about 17&nbsp;% larger than it needs to be.</p>
<div class="callout key"><span class="lbl">Where the 0.86 comes from</span>No standard or handbook publishes a single diversity figure for a mixed-use tower, and one that did would be wrong for most towers. The 0.86 is the result of the calculation the codes require: an hour-by-hour block load in the manner of ANSI/ASHRAE/ACCA Standard&nbsp;183 and the ASHRAE <em>Fundamentals</em> load chapter, as required for equipment sizing by ASHRAE 90.1 &sect;6.4.2.1 and SBC&nbsp;501 &sect;312.1. It was run for an illustrative 128-floor Gulf tower with retail, offices, a hotel, residences and an observation deck. Every input is stated in the <a href="chilled-water-diversity-megatall.html">companion article</a>, and the full model is published as <a href="specs/diversity_data/model.py">source code</a> that anyone can rerun or change. The usage diversity inside it is kept within measured evidence: the office equipment diversity from ASHRAE-sponsored measurements, and the RP-1093 library of lighting and equipment diversity factors. Coastal Gulf gives <strong>0.858</strong>, and inland Gulf, drier with a wider daily swing, <strong>0.837</strong>. For your own tower, the number to use is the one your own hourly block calculation gives, written into the design basis with its assumptions.</div>

<h2 id="modelling">5 · Modelling a tower honestly</h2>
<ul class="clean">
  <li><strong>Zone by orientation and by height</strong>, not by floor. A 150-storey model with every floor represented is unmanageable and no more accurate; a model with representative floors per vertical zone and per orientation captures what matters.</li>
  <li><strong>Include the stack effect.</strong> Most whole-building models treat infiltration as a constant air change rate, which is exactly wrong for a tower — infiltration is concentrated at the base in winter and at the top in a Gulf summer, and it is one of the largest single loads. Use a model that couples airflow to the thermal simulation, or at least apply a height-varying infiltration profile.</li>
  <li><strong>Model the real occupancy schedules per use</strong>, because the usage-driven part of the diversity is a scheduling result. A mixed-use tower modelled with one office schedule throughout will get the peak hour, and therefore the block, wrong.</li>
  <li><strong>Calibrate the glazing model against the actual specification</strong>, including frames, spandrel panels and the shading that is actually built rather than the shading that is rendered.</li>
  <li><strong>Test the model's sensitivity</strong> to the three parameters that dominate: SHGC, internal gain density and infiltration. If the answer swings wildly on any of them, that is where the design effort belongs.</li>
  <li><strong>Do not confuse peak sizing with energy.</strong> Peak sizing sets the plant; annual simulation sets the running cost and the control strategy. They are different exercises with different assumptions, and using peak-day assumptions for an annual model is a common and expensive error.</li>
</ul>

<h2 id="install">6 · From model to plant — the practical steps</h2>
<ul class="clean">
  <li><strong>Write down the diversity you took and why.</strong> The single most useful line in a design report is an explicit statement of the assumed diversity, the basis for it and what would invalidate it. The basis should be an hourly block calculation, not a percentage. It is also the line that protects you if the building's use changes.</li>
  <li><strong>Give each vertical zone its own load density.</strong> Solar-driven differences of 2× between bottom and top are real and free to exploit, because the plant is zoned anyway.</li>
  <li><strong>Separate the perimeter from the core in the control strategy</strong>, even where a single system serves both — they peak at different times and in opposite directions.</li>
  <li><strong>Design for turndown, not just for peak.</strong> A plant sized on a diversified peak spends its life well below it; staging, minimum flows and low-load stability matter more than the last percent of full-load efficiency.</li>
  <li><strong>Leave space for a future tenant load.</strong> A trading floor, a kitchen or a data room appearing mid-life is normal in a landmark tower; leaving riser and plant capacity for it is far cheaper than adding it later.</li>
  <li><strong>Re-run the model at the end of design</strong> against the specification that was actually procured, not the one that was assumed at concept — the glazing and the lighting density both routinely change.</li>
  <li><strong>Compare against measured data at handover</strong> and keep the model. A calibrated model is the tool that answers every future question about the building, and it is almost always thrown away.</li>
</ul>

<h2 id="checklist">7 · The design &amp; modelling checklist</h2>
<ul class="clean">
  <li><strong>Establish the façade ratio first</strong> — it tells you whether the building is envelope- or internally-driven and which template applies.</li>
  <li><strong>Zone by orientation and by height</strong>, with different load densities per vertical zone.</li>
  <li><strong>Run a real solar study</strong> including the surrounding fabric and the risk of it changing.</li>
  <li><strong>Couple infiltration to stack effect</strong> rather than assuming a uniform air change rate.</li>
  <li><strong>Take diversity from an hourly block calculation</strong> with use-specific schedules, applying usage diversity only to people-driven loads, and state it explicitly.</li>
  <li><strong>Test sensitivity</strong> to SHGC, internal gains and infiltration.</li>
  <li><strong>Size on the diversified simultaneous peak</strong> with a stated redundancy.</li>
  <li><strong>Design for turndown</strong> and leave capacity for future tenant loads.</li>
  <li><strong>Re-run against the procured specification</strong> and calibrate against measured data at handover.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A tower's cooling load is decided by a dimension on the architect's plan: <strong>façade per unit floor area is 4h/s</strong>, so a 30&nbsp;m plate is 60&nbsp;% envelope-driven and a 60&nbsp;m plate is 43&nbsp;% — two different buildings needing two different HVAC templates. Height changes less than expected but changes it systematically: shading disappears, so the crown can see <strong>2.5× the solar gain</strong> of the podium for identical glass, which is free to exploit because the plant is zoned vertically anyway. Diversity is real, but it is smaller than the rule of thumb. In a Gulf glass tower more than half of the connected load is driven by the weather and peaks together, so a mixed-use tower's block load is about <strong>0.86 of connected, not 0.55</strong>. It is enough to pay for the standby chiller, not to halve the plant. Take it from an hourly block calculation to Standard&nbsp;183, not from a blanket percentage, and <strong>write it down explicitly</strong>, because it is the assumption most likely to be quietly invalidated by a change of tenant.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Handbook — Fundamentals</em>: Nonresidential Cooling and Heating Load Calculations (Radiant Time Series), Fenestration, and Climatic Design Information.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — load characteristics, vertical zoning and diversity in tall buildings.</li>
  <li>CIBSE <em>Guide A — Environmental Design</em> and CIBSE TM52 / TM54 — load calculation, design criteria and operational energy prediction.</li>
  <li>ANSI/ASHRAE Standard 140 — <em>Method of Test for Evaluating Building Performance Simulation Software</em>; and ASHRAE Guideline 14 for model calibration against measured data.</li>
  <li>ANSI/ASHRAE/IES Standard 90.1, Appendix G — whole-building performance modelling protocol; and Estidama / Mostadam / LEED energy modelling requirements.</li>
  <li>ASHRAE <em>Handbook — Fundamentals</em>, Ventilation and Infiltration chapter — stack-driven infiltration in tall buildings and its coupling to thermal load.</li>
  <li>CTBUH technical guidance on façade performance and solar exposure in tall buildings.</li>
  <li>Saudi Building Code <em>SBC 601</em> (energy conservation) and <em>SBC 501</em> — envelope and mechanical requirements for the region; SBC 501 &sect;312.1 requires system design loads to be determined to ASHRAE/ACCA Standard 183.</li>
  <li>ANSI/ASHRAE/ACCA Standard 183, <em>Peak Cooling and Heating Load Calculations in Buildings Except Low-Rise Residential Buildings</em> — the design load procedure required for equipment sizing by ASHRAE 90.1 &sect;6.4.2.1.</li>
  <li>Wilkins, C.K. and Hosni, M.H. &ldquo;Plug Load Design Factors.&rdquo; <em>ASHRAE Journal</em> 53(5), May 2011, pp.&nbsp;30&ndash;34 — measured diversity of office equipment (75&nbsp;% for computers, 60&nbsp;% for monitors) and design load factors.</li>
  <li>Abushakra, B., Haberl, J.S. and Claridge, D.E. &ldquo;Overview of Existing Literature on Diversity Factors and Schedules for Energy and Cooling Load Calculations.&rdquo; <em>ASHRAE Transactions</em> 110(1), 2004 (ASHRAE RP-1093) — lighting and equipment diversity factors from metered office buildings.</li>
  <li>Abokhatwa, M. <a href="chilled-water-diversity-megatall.html">Chilled-Water Diversity in Megatall Towers</a>, 2026, with the hourly block model published as <a href="specs/diversity_data/model.py">source code</a> — the calculation behind the 0.86 used here.</li>
</ol>

<div class="tags">#CoolingLoad #LoadCalculation #EnergyModelling #BuildingSimulation #TallBuildings #MegatallBuildings #FacadeRatio #FloorPlate #EnvelopeDriven #InternallyDriven #SHGC #Glazing #SolarGain #Shading #UrbanCanopy #Diversity #SimultaneousLoad #ConnectedLoad #MixedUse #PlantSizing #Redundancy #Turndown #Infiltration #StackEffect #ASHRAE140 #Guideline14 #Calibration #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const FH=4.0, DT=20, SUNLIT=0.5;

/* ---------- CHART 1 : envelope vs internal ---------- */
const sS=document.getElementById('sS'),sU=document.getElementById('sU'),
      sG=document.getElementById('sG'),sI=document.getElementById('sI');
const SOLAR=500;
const facRatio=s=>4*FH/s;
let geoChart=new Chart(document.getElementById('geoChart'),{
  data:{datasets:[
    {type:'line',label:'Envelope load (W/m²)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'line',label:'Internal load (W/m²)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your building',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:18,max:90,title:{display:true,text:'Floor plate side (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Cooling load (W per m² of floor)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} W/m² at ${fmt0(c.parsed.x)} m plate`}}}}
});
function updGeo(){
  const s=+sS.value,U=+sU.value,G=+sG.value,I=+sI.value;
  document.getElementById('vS').textContent=s+' m';
  document.getElementById('vU').textContent=fmt2(U)+' W/m²K';
  document.getElementById('vG').textContent=fmt2(G);
  document.getElementById('vI').textContent=I+' W/m²';
  const env=x=>facRatio(x)*(U*DT+G*SOLAR*SUNLIT);
  const xs=[];for(let x=18;x<=90;x+=1)xs.push(x);
  geoChart.data.datasets[0].data=xs.map(x=>({x:x,y:+env(x).toFixed(1)}));
  geoChart.data.datasets[1].data=xs.map(x=>({x:x,y:I}));
  geoChart.data.datasets[2].data=[{x:s,y:+env(s).toFixed(1)}];
  geoChart.update('none');
  const E=env(s), share=100*E/(E+I);
  document.getElementById('rFr').innerHTML=fmt3(facRatio(s))+' <small>m²/m²</small>';
  document.getElementById('rEn').innerHTML=fmt0(E)+' <small>W/m²</small>';
  document.getElementById('rIn').innerHTML=fmt0(I)+' <small>W/m²</small>';
  document.getElementById('rSh').innerHTML=fmt0(share)+' <small>%</small>';
  const v=document.getElementById('rCh');
  if(share>=58)      v.innerHTML='<span class="badge bad">envelope-driven</span>';
  else if(share>=45) v.innerHTML='<span class="badge warn">balanced</span>';
  else               v.innerHTML='<span class="badge good">internally driven</span>';
}
[sS,sU,sG,sI].forEach(s=>s.addEventListener('input',updGeo));updGeo();

/* ---------- CHART 2 : solar by height ---------- */
const sNh=document.getElementById('sNh'),sW=document.getElementById('sW'),
      sSo=document.getElementById('sSo'),sZ=document.getElementById('sZ');
function unshaded(z,nh,wr){
  // simple geometric model: fully shaded below the height at which the sun clears the opposite block
  const zFull=nh*(1-Math.min(wr,1)*0.6);       // height at which shading has largely gone
  if(z>=nh) return 1.0;
  const f=0.4+0.6*Math.min(1,Math.max(0,(z-zFull)/Math.max(nh-zFull,1)));
  return Math.min(1,Math.max(0.3,f));
}
let solChart=new Chart(document.getElementById('solChart'),{
  data:{datasets:[
    {type:'line',label:'Solar gain on the façade (W/m²)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your floor',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',
    scales:{x:{type:'linear',min:0,title:{display:true,text:'Peak solar gain on the façade (W/m²)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Height above grade (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.x)} W/m² at ${fmt0(c.parsed.y)} m`}}}}
});
function updSol(){
  const nh=+sNh.value,wr=+sW.value,So=+sSo.value,z=+sZ.value;
  document.getElementById('vNh').textContent=nh+' m';
  document.getElementById('vW').textContent=fmt1(wr);
  document.getElementById('vSo').textContent=So+' W/m²';
  document.getElementById('vZ').textContent=z+' m';
  const ys=[];for(let y=5;y<=700;y+=5)ys.push(y);
  solChart.data.datasets[0].data=ys.map(y=>({x:+(So*unshaded(y,nh,wr)).toFixed(0),y:y}));
  const f=unshaded(z,nh,wr);
  solChart.data.datasets[1].data=[{x:+(So*f).toFixed(0),y:z}];
  solChart.options.scales.x.max=So*1.1;
  solChart.update('none');
  const low=So*unshaded(20,nh,wr);
  document.getElementById('rUf').textContent=fmt2(f);
  document.getElementById('rSf').innerHTML=fmt0(So*f)+' <small>W/m²</small>';
  document.getElementById('rS5').innerHTML=fmt0(low)+' <small>W/m²</small>';
  document.getElementById('rRt').innerHTML=fmt1(So*f/Math.max(low,1))+'<small>×</small>';
  const v=document.getElementById('rZv'), r=So*f/Math.max(low,1);
  if(r<1.3)      v.innerHTML='<span class="badge good">uniform — one density</span>';
  else if(r<2.0) v.innerHTML='<span class="badge warn">zone by height</span>';
  else           v.innerHTML='<span class="badge bad">large variation — zone by height</span>';
}
[sNh,sW,sSo,sZ].forEach(s=>s.addEventListener('input',updSol));updSol();

/* ---------- CHART 3 : diversity, split by what drives the load ---------- */
const sN=document.getElementById('sN'),sWs=document.getElementById('sWs'),sCw=document.getElementById('sCw'),
      sDa=document.getElementById('sDa'),sC=document.getElementById('sC'),sR=document.getElementById('sR');
const usageF=(n,a)=>a+(1-a)/Math.sqrt(Math.max(n,1));
const coinc=(n,w,cw,a)=>w*cw+(1-w)*usageF(n,a);
const BLANKET=0.55;
let divChart=new Chart(document.getElementById('divChart'),{
  data:{datasets:[
    {type:'line',label:'Weather-driven part (MW)',data:[],borderColor:'#b9770e',backgroundColor:'rgba(185,119,14,0.16)',borderWidth:2,pointRadius:0,fill:'origin',yAxisID:'y',order:5},
    {type:'line',label:'Simultaneous load (MW)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.12)',borderWidth:3,pointRadius:0,fill:'-1',yAxisID:'y',order:4},
    {type:'line',label:'Blanket 0.55 (MW)',data:[],borderColor:'#7f8c8d',borderWidth:1.5,borderDash:[3,3],pointRadius:0,fill:false,yAxisID:'y',order:3},
    {type:'scatter',label:'Your tower',data:[],backgroundColor:'#1b4f72',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,animation:false,
    scales:{x:{type:'linear',min:1,max:200,title:{display:true,text:'Independent zones',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Load (MW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,max:1,title:{display:true,text:'Fraction of connected load',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updDiv(){
  const n=+sN.value,w=+sWs.value,cw=+sCw.value,a=+sDa.value,C=+sC.value,R=+sR.value;
  document.getElementById('vN').textContent=n;
  document.getElementById('vWs').textContent=fmt2(w);
  document.getElementById('vCw').textContent=fmt2(cw);
  document.getElementById('vDa').textContent=fmt2(a);
  document.getElementById('vC').textContent=C+' MW';
  document.getElementById('vR').textContent=R===0?'N':'N+'+R;
  const xs=[];for(let x=1;x<=200;x+=1)xs.push(x);
  divChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(C*w*cw).toFixed(2)}));
  divChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(C*coinc(x,w,cw,a)).toFixed(2)}));
  divChart.data.datasets[2].data=[{x:1,y:C*BLANKET},{x:200,y:C*BLANKET}];
  const d=coinc(n,w,cw,a), sim=C*d;
  divChart.data.datasets[3].data=[{x:n,y:+sim.toFixed(2)}];
  divChart.options.scales.y.max=C;
  divChart.update('none');
  const nUnits=6, inst=sim*(1+R/nUnits), vs=100*(inst/C-1), short=100*(1-BLANKET/d);
  document.getElementById('rDf').textContent=fmt3(d);
  document.getElementById('rSp').innerHTML=fmt1(sim)+' <small>MW</small>';
  document.getElementById('rAv').innerHTML=fmt1(C-sim)+' <small>MW</small>';
  document.getElementById('rIc').innerHTML=fmt1(inst)+' <small>MW</small>';
  document.getElementById('rVn').innerHTML=(Math.round(vs)>0?'+':Math.round(vs)<0?'−':'')+fmt0(Math.abs(vs))+' <small>%</small>';
  document.getElementById('rBl').innerHTML=short>0.5?fmt0(short)+' <small>% short</small>':fmt0(-short)+' <small>% over</small>';
}
[sN,sWs,sCw,sDa,sC,sR].forEach(s=>s.addEventListener('input',updDiv));updDiv();

window.addEventListener('load',function(){try{geoChart.resize();solChart.resize();divChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='cooling-load-modelling-tall-buildings', cat='hvac', mins=15,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Cooling Load &amp; Energy Modelling for Megatall Buildings: Façade Ratio, Solar by Height &amp; Diversity',
    reg_title='Cooling Load & Energy Modelling for Megatall Buildings: Façade Ratio, Solar by Height & Diversity',
    reg_tag='HVAC · Cooling Load · Energy Modelling',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Cooling Load &middot; Energy Modelling &middot; Diversity',
    desc='Cooling load and energy modelling for megatall buildings: why the floor plate dimension decides whether the tower is envelope-driven or internally driven, what actually changes with height including the loss of shading and a doubling of solar gain at the crown, how much diversity a mixed-use tower really has once weather-driven and usage-driven loads are separated, and how to model a tower honestly including stack-driven infiltration — with three interactive charts.',
    og_desc='A 30 m floor plate is 60 percent envelope-driven; a 60 m plate is 43 percent. Two different buildings needing two different HVAC templates, separated by nothing more than a dimension on the architect plan.',
    ld_desc='A design-perspective guide to cooling load and energy modelling in megatall buildings: facade-to-floor area ratio and load character, solar gain variation with height and shading, load diversity split into weather-driven and usage-driven parts with block-load plant sizing, and modelling practice including stack-coupled infiltration and calibration.',
    img_alt='Technical illustration comparing a slender tower with a small floor plate against a wider tower of the same height, with solar gain indicated on their facades and the difference in envelope area per floor made visible',
    en_tag='HVAC &amp; Cooling &middot; Cooling Load &middot; Modelling &middot; Diversity',
    en_title='Cooling Load &amp; Energy Modelling for Megatall Buildings: Façade Ratio, Solar by Height &amp; Diversity',
    en_excerpt='Two towers of identical height can have completely different cooling loads, plant and economics &mdash; because one has a 30&nbsp;m floor plate and the other a 60&nbsp;m one. The slender tower carries twice the fa&ccedil;ade per square metre of floor and is <strong>60&nbsp;% envelope-driven</strong>; the wide one is internally driven at 43&nbsp;%. Plus what really changes with height (the crown sees <strong>2.5&times;</strong> the solar gain of the podium for identical glass), and why a Gulf mixed-use tower&rsquo;s block load is about <strong>0.86</strong> of its connected load, not the 0.55 often assumed &mdash; with three interactive charts.',
    en_search='cooling load calculation energy modelling building simulation tall buildings megatall facade ratio floor plate slender wide envelope driven internally driven glazing U-value SHGC solar heat gain coefficient shading urban canopy solar gain by height orientation zoning perimeter core simultaneous heating and cooling diversity factor connected load simultaneous load mixed use office hotel residential schedules plant sizing redundancy N+1 turndown part load stack effect infiltration coupled airflow thermal simulation ASHRAE 140 Guideline 14 calibration Appendix G radiant time series CIBSE TM54 sensitivity analysis future tenant load MEP building services HVAC',
    ar_title='حساب أحمال التبريد والنمذجة للمباني فائقة الارتفاع: نسبة الواجهة والإشعاع مع الارتفاع والتزامن',
    ar_excerpt='برجان بالارتفاع نفسه قد يختلفان تمامًا في أحمال التبريد والمعدات والاقتصاديات — لأن أحدهما بمسطح طابق ٣٠ مترًا والآخر ٦٠ مترًا. البرج النحيل يحمل ضعف مساحة الواجهة لكل متر مربع من الأرضية ويكون <strong>محكومًا بالغلاف بنسبة ٦٠٪</strong>، بينما الواسع محكوم بالأحمال الداخلية عند ٤٣٪. مع ما يتغير فعلًا مع الارتفاع (القمة ترى <strong>٢٫٥ ضعف</strong> الإشعاع الشمسي مقارنة بالقاعدة للزجاج نفسه)، ولماذا يبلغ الحمل المتزامن لبرج متعدد الاستخدامات في الخليج نحو <strong>٠٫٨٦</strong> من الحمل الموصول، لا ٠٫٥٥ كما يُفترض غالبًا — مع ثلاثة رسوم تفاعلية.',
    ar_search='cooling load energy modelling facade ratio floor plate envelope driven internally driven SHGC solar gain shading diversity factor simultaneous load mixed use plant sizing stack effect infiltration ASHRAE 140 calibration حساب أحمال التبريد نمذجة الطاقة محاكاة المباني المباني الشاهقة المباني فائقة الارتفاع نسبة الواجهة مسطح الطابق البرج النحيل البرج الواسع محكوم بالغلاف محكوم بالأحمال الداخلية معامل انتقال الحرارة معامل الكسب الشمسي التظليل المظلة الحضرية الكسب الشمسي مع الارتفاع التوجيه تقسيم المناطق المحيط والنواة التدفئة والتبريد المتزامنان معامل التزامن الحمل الموصول الحمل المتزامن الاستخدام المختلط المكاتب الفنادق السكني جداول الإشغال تحجيم المحطة الاحتياطية التشغيل الجزئي تأثير المدخنة تسرب الهواء المحاكاة المقترنة المعايرة تحليل الحساسية أحمال المستأجرين المستقبلية MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
