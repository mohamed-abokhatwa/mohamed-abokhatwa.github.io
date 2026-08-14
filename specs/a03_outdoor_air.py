# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Outdoor air is the one thing a tall building cannot manufacture. Everything else — cooling, heat, water, power — can be generated, stored or zoned. Fresh air has to be captured from a moving atmosphere, at a height where that atmosphere is doing something very different from what it does at ground level, and then dragged through a filter bank and up a shaft to a hundred floors of people. In a megatall tower the ventilation system is fighting three things at once: <strong>wind pressures that exceed the fan's own static</strong>, an outdoor state that in a coastal Gulf summer carries more than twice the enthalpy of the air being thrown away, and a filtration duty that quietly consumes more fan energy over a year than the fan was ever sized to notice.</p>

<h2 id="why">1 · Why outdoor air is different up there</h2>
<ul class="clean">
  <li><strong>The wind is a pressure source, not a breeze.</strong> Wind speed grows with height as a power law, and dynamic pressure grows with its square. At 600&nbsp;m a wind that is a mild 10&nbsp;m/s at street level produces a windward-to-leeward pressure difference across the tower of about <strong>600&nbsp;Pa</strong> — larger than the external static of many air-handling units. An intake that is not designed for it will be over-pressurised, reversed, or both, depending on the hour.</li>
  <li><strong>Intake location cannot be an afterthought.</strong> At height, the choices are few: the façade, a mechanical floor louvre, or the roof. Each has a different relationship with the wind, with the exhaust discharges, and with the plume from cooling towers and generators.</li>
  <li><strong>The outdoor state is not the same air you left downstairs.</strong> Temperature falls roughly 6.5&nbsp;°C per kilometre, particulate loading falls markedly above the street canyon, and humidity behaves differently near a coast. On a 600&nbsp;m tower those are small but real differences, and they push in the designer's favour — a rare thing.</li>
  <li><strong>Stack effect is superimposed on everything.</strong> The ventilation system does not operate in a neutral building; it operates inside the pressure regime described in <a href="stack-effect-tall-buildings.html">stack effect</a>. Supply and extract balance that works in the shoulder season can invert in winter or in a Gulf summer.</li>
  <li><strong>Fresh air is the dominant latent load.</strong> In a humid coastal climate the outdoor air is where nearly all the dehumidification energy goes, which makes energy recovery not a refinement but a primary design decision.</li>
</ul>

<h2 id="wind">2 · Wind pressure at the intake</h2>
<p>Wind speed increases with height through the atmospheric boundary layer, conventionally modelled as a power law, and the pressure it exerts on a façade is the dynamic pressure modified by a surface pressure coefficient<sup class="cite">[1][2]</sup>:</p>
<div class="eq">\[ V(z) = V_{10}\left(\frac{z}{10}\right)^{\alpha}, \qquad p = C_p\,\tfrac{1}{2}\rho V(z)^2 \]</div>
<p>with \(\alpha\) about 0.14 in open terrain and 0.25–0.33 in a city, \(C_p\) roughly <strong>+0.8 on the windward face</strong> and <strong>−0.5 to −0.7 on the leeward and side faces</strong>. The consequences for a façade intake are severe and asymmetric: on the windward side the wind <em>helps</em> the intake and over-ventilates, while a relief or exhaust louvre on the same face may reverse; on the leeward side the negative pressure fights the fan and starves it.</p>

<div class="callout warn">
  <span class="lbl">The failure that looks like a controls problem</span>
  A tower with façade intakes on more than one orientation, all connected to a common plenum, has built a <strong>wind-driven short circuit</strong>. On a windy day the windward louvre pressurises the plenum and air pours <em>out</em> of the leeward louvre without ever passing a coil. Outdoor-air flow measurement reads correctly at the fan and the floors are still starved. The fix is architectural — separate plenums per orientation, or an intake on one orientation only, or a roof intake — and it cannot be commissioned away.
</div>

<h2 id="int-wind">3 · Interactive: wind pressure on the intake</h2>
<p>Set the site wind and terrain and read the pressure the intake will actually see, up the height of the tower, against the external static the fan was sized for.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Wind pressure at a façade intake vs height</div>
    <div class="fsub">V(z) = V&#8321;&#8320;·(z/10)^α, p = C&#112;·½ρV², ρ = 1.2 kg/m³. Windward C&#112; = +0.8, leeward C&#112; = −0.5. The dashed line is the fan external static for comparison.</div>
  </div>
  <div class="chart-box"><canvas id="windChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Wind speed at 10 m <span id="vV">10 m/s</span></label>
      <input type="range" id="sV" min="2" max="25" value="10" step="0.5">
      <div class="hint">A representative windy-day speed, not the structural design gust.</div>
    </div>
    <div class="ctrl">
      <label>Terrain exponent α <span id="vAl">0.25</span></label>
      <input type="range" id="sAl" min="0.1" max="0.4" value="0.25" step="0.01">
      <div class="hint">0.14 open coast, 0.25 suburban, 0.33 dense city.</div>
    </div>
    <div class="ctrl">
      <label>Intake height <span id="vZ">600 m</span></label>
      <input type="range" id="sZ" min="20" max="1000" value="600" step="10">
      <div class="hint">Height of the louvre above grade.</div>
    </div>
    <div class="ctrl">
      <label>Fan external static <span id="vFs">400 Pa</span></label>
      <input type="range" id="sFs" min="100" max="1200" value="400" step="25">
      <div class="hint">What the AHU was selected to overcome.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Wind at intake</div><div class="v" id="rV">27.8 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Windward</div><div class="v" id="rWw">+372 <small>Pa</small></div></div>
    <div class="cell"><div class="k">Leeward</div><div class="v" id="rLw">−232 <small>Pa</small></div></div>
    <div class="cell"><div class="k">Across building</div><div class="v" id="rAc">604 <small>Pa</small></div></div>
    <div class="cell"><div class="k">vs fan static</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">A 10&nbsp;m/s street-level wind — an ordinary day, not a storm — becomes <strong>27.8&nbsp;m/s at 600&nbsp;m</strong> and produces <strong>+372&nbsp;Pa windward and −232&nbsp;Pa leeward</strong>, a difference of 604&nbsp;Pa across the building. Against a 400&nbsp;Pa fan that is not a correction, it is the dominant term: the same unit is wildly over-supplied on one face and cannot deliver on the other. Design intakes for the pressure they will actually see, use motorised rather than gravity dampers where reversal is credible, and give each orientation its own plenum and its own flow measurement.</p>

<h2 id="location">4 · Choosing the intake and discharge strategy</h2>
<ul class="clean">
  <li><strong>Mechanical-floor louvres.</strong> The default: intake and discharge on the plant levels, which puts them at the pressure break and keeps duct runs short. Separate intake and exhaust by orientation and by height, and never place them on the same face without checking the re-entrainment geometry against the prevailing wind.</li>
  <li><strong>Roof intake.</strong> Cleanest air and the most predictable pressure field, but it commits the building to a full-height outdoor-air riser and it puts the intake in the same airspace as cooling tower plume, generator exhaust and helipad operations.</li>
  <li><strong>Separation from discharges is a dispersion calculation, not a rule of thumb.</strong> Cooling tower drift, generator and boiler flues, kitchen exhaust and toilet extract all need a stack-height and separation assessment; ASHRAE gives the geometric method and dispersion modelling is warranted where the plume is significant.<sup class="cite">[3]</sup></li>
  <li><strong>Louvre free area is not the louvre size.</strong> Weather louvres run 40–60&nbsp;% free area, and rain-defence louvres less; size on the free area and hold face velocity down (typically below 2–2.5&nbsp;m/s) or the louvre becomes both a water entry point and a noise source.</li>
  <li><strong>Plan for sand and salt.</strong> In the Gulf both are design conditions rather than exceptions: pre-filters ahead of the fine stage, accessible wash-down at the louvre, and corrosion-resistant coil and casing specification.</li>
</ul>

<h2 id="int-recovery">5 · Interactive: what energy recovery is worth in your climate</h2>
<p>Outdoor air must be dragged from its own state to the supply state, and the air being exhausted is already most of the way there. A total-enthalpy device — a wheel or a membrane exchanger — recovers both heat and moisture, and its value depends entirely on how far apart the two air streams are. In a dry inland climate that gap is modest. On a humid coast it is enormous.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Total-enthalpy recovery from outdoor air</div>
    <div class="fsub">h = 1.006·T + W(2501 + 1.86·T), with W from temperature and relative humidity. Load = ṁ·Δh and recovered load = ṁ·Δh·ε against exhaust air at 24 °C / 50 % RH, with the dry-air mass flow ṁ = Q/v taken from the moist-air specific volume rather than a fixed density — at 40 °C that alone is a 10 % correction.</div>
  </div>
  <div class="chart-box"><canvas id="ervChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Outdoor temperature <span id="vOt">40 °C</span></label>
      <input type="range" id="sOt" min="25" max="50" value="40" step="0.5">
      <div class="hint">Summer design dry-bulb.</div>
    </div>
    <div class="ctrl">
      <label>Outdoor relative humidity <span id="vOr">55 %</span></label>
      <input type="range" id="sOr" min="5" max="90" value="55" step="1">
      <div class="hint">Riyadh ≈ 15 % at peak; Jeddah, Dubai and Doha ≈ 50–60 %.</div>
    </div>
    <div class="ctrl">
      <label>Outdoor air volume <span id="vOq">10.0 m³/s</span></label>
      <input type="range" id="sOq" min="1" max="40" value="10" step="0.5">
      <div class="hint">Total fresh air for the zone or tower.</div>
    </div>
    <div class="ctrl">
      <label>Recovery effectiveness ε <span id="vEf">70 %</span></label>
      <input type="range" id="sEf" min="0" max="85" value="70" step="1">
      <div class="hint">Total-enthalpy wheels reach 70–80 %; plate and membrane devices less.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Outdoor enthalpy</div><div class="v" id="rHo">107 <small>kJ/kg</small></div></div>
    <div class="cell"><div class="k">Enthalpy gap</div><div class="v" id="rDh">59 <small>kJ/kg</small></div></div>
    <div class="cell"><div class="k">Untreated OA load</div><div class="v" id="rL0">642 <small>kW</small></div></div>
    <div class="cell"><div class="k">Recovered</div><div class="v" id="rRe">449 <small>kW</small></div></div>
    <div class="cell"><div class="k">Chiller saved</div><div class="v" id="rTr">128 <small>TR</small></div></div>
  </div>
</div>
<p class="fig-note">The regional split is stark. At <strong>Jeddah</strong> conditions (40&nbsp;°C, 55&nbsp;%) the outdoor air carries 107&nbsp;kJ/kg against 48&nbsp;kJ/kg leaving the building — a <strong>59&nbsp;kJ/kg</strong> gap, so 10&nbsp;m³/s of fresh air is a 642&nbsp;kW load and a 70&nbsp;% wheel recovers <strong>449&nbsp;kW</strong>, about 128 tons of chiller you never have to buy or run. Drag the humidity down to 15&nbsp;% for <strong>Riyadh</strong> and the outdoor air ends up <em>drier</em> than the air leaving the building: the gap collapses to about 10&nbsp;kJ/kg, the load to 113&nbsp;kW and the recovery to 79&nbsp;kW. Same building, same wheel, under a fifth of the benefit — which is why energy recovery is close to mandatory on the coast and a genuine cost-benefit question inland. Note also what this says about leakage: in Jeddah every extra litre of uncontrolled infiltration costs nearly six times what it costs in Riyadh.</p>

<h2 id="int-filter">6 · Interactive: the quiet cost of filtration</h2>
<p>Filters are specified on capture efficiency and forgotten. Their pressure drop, however, runs 8,760 hours a year and rises as they load. Over a filter's life the fan spends far more energy pushing through it than the filter itself costs.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Fan energy to overcome filtration</div>
    <div class="fsub">P = Q·Δp/η&#102;&#97;&#110;. The curve is annual energy against the average pressure drop over the filter's life — roughly midway between clean and change-out.</div>
  </div>
  <div class="chart-box"><canvas id="filtChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Air volume <span id="vFq">10.0 m³/s</span></label>
      <input type="range" id="sFq" min="1" max="40" value="10" step="0.5">
      <div class="hint">Airflow through the filter bank.</div>
    </div>
    <div class="ctrl">
      <label>Average pressure drop <span id="vFd">175 Pa</span></label>
      <input type="range" id="sFd" min="40" max="400" value="175" step="5">
      <div class="hint">Mean over the life. A clean ePM1 60 % filter starts near 100 Pa and is changed near 250.</div>
    </div>
    <div class="ctrl">
      <label>Fan + drive efficiency <span id="vFe">65 %</span></label>
      <input type="range" id="sFe" min="40" max="80" value="65" step="1">
      <div class="hint">Total, including motor and drive.</div>
    </div>
    <div class="ctrl">
      <label>Annual run hours <span id="vFh">6000 h</span></label>
      <input type="range" id="sFh" min="2000" max="8760" value="6000" step="100">
      <div class="hint">Central plant in a mixed-use tower runs most of the year.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Fan power</div><div class="v" id="rFp">2.7 <small>kW</small></div></div>
    <div class="cell"><div class="k">Annual energy</div><div class="v" id="rFe">16,154 <small>kWh</small></div></div>
    <div class="cell"><div class="k">If 50 Pa lower</div><div class="v" id="rFl">11,538 <small>kWh</small></div></div>
    <div class="cell"><div class="k">Saving</div><div class="v" id="rFs">4,615 <small>kWh</small></div></div>
    <div class="cell"><div class="k">Across 20 AHUs</div><div class="v" id="rF20">92 <small>MWh</small></div></div>
  </div>
</div>
<p class="fig-note">One AHU at 10&nbsp;m³/s and a 175&nbsp;Pa average filter loss spends about <strong>16,150&nbsp;kWh a year</strong> just on filtration. Specify a deeper filter with more media area for the same efficiency class — dropping the average by 50&nbsp;Pa — and you save 4,615&nbsp;kWh on that one unit, <strong>92&nbsp;MWh across twenty units</strong>, every year, for nothing but a slightly deeper filter housing decided at design stage. Depth is the cheapest energy measure in an air system, and it is only available before the AHU is ordered.</p>

<h2 id="strategy">7 · Ventilation strategy: DOAS and the case for separating jobs</h2>
<p>The dominant modern arrangement in tall buildings is to <strong>separate ventilation from cooling</strong>: a dedicated outdoor-air system conditions and dehumidifies fresh air centrally and delivers it at neutral or slightly cool temperature, while sensible cooling is handled locally by fan-coils, chilled beams or floor AHUs. The advantages compound in a tower:</p>
<ul class="clean">
  <li><strong>The riser carries only fresh air</strong> — roughly a tenth of the air volume of an all-air system, which is the shaft-area argument made in <a href="mechanical-floors-tall-buildings.html">mechanical floors</a>.</li>
  <li><strong>Ventilation is measurable and guaranteed.</strong> Fresh air is delivered by a dedicated path with its own flow measurement, rather than being a fraction of a variable supply that falls with load.</li>
  <li><strong>Dehumidification is done once, properly.</strong> The DOAS coil handles the latent load at a deep dew point; the local units run dry and stay clean.</li>
  <li><strong>Demand control actually works.</strong> CO₂ sensing modulates a stream that is only fresh air, so the response is direct and the savings real.</li>
</ul>
<p>The counterweight is that a DOAS makes the outdoor-air riser a single point of failure and demands rigorous air balancing, because there is no large recirculating stream to hide errors in.</p>

<h2 id="install">8 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Measure outdoor air where it can be measured.</strong> Fit a proper airflow measuring station in a straight duct section on the fresh-air path of every AHU, not a differential-pressure guess across a damper. Without it, ventilation compliance is an assertion.</li>
  <li><strong>Motorise the intake and relief dampers</strong> where wind reversal is credible, with end-switch proving, and interlock them with the fan so a stopped unit is not a wind-driven hole in the façade.</li>
  <li><strong>Drain every louvre plenum.</strong> Rain and wash-down water will get in; give it a bunded, drained, corrosion-protected floor with a trapped outlet, and check the trap depth against the plenum pressure — a shallow trap on a negative plenum simply blows dry.</li>
  <li><strong>Set the filter change-out on pressure, not on a calendar</strong>, with a differential-pressure switch and a BMS trend on every bank. Changing early wastes filters; changing late wastes far more in fan energy.</li>
  <li><strong>Seal the AHU and the ductwork to a stated class.</strong> At the pressures a tall building generates, casing and duct leakage is not a rounding error; specify the leakage class, test it, and reject on the test.</li>
  <li><strong>Commission across seasons and across wind.</strong> Ventilation rates verified on a still day in March tell you very little; re-verify on a windy day and in the design season, and record the outdoor conditions alongside every reading.</li>
  <li><strong>Protect the coils during construction.</strong> Running AHUs for temporary conditioning without construction filters is how a tower starts life with a fouled coil and a permanent capacity deficit.</li>
</ul>

<h2 id="checklist">9 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Calculate the wind pressure at every intake and discharge</strong>, on every orientation, and design the dampers and plenums for it.</li>
  <li><strong>Never share a plenum across orientations</strong> without a means of preventing wind-driven short-circuit.</li>
  <li><strong>Do the separation and dispersion assessment</strong> for towers, flues, kitchen and toilet exhaust against every intake.</li>
  <li><strong>Evaluate total-enthalpy recovery on real local psychrometrics</strong> — it is transformative on a humid coast and marginal inland.</li>
  <li><strong>Specify filters on depth and life-cycle pressure drop</strong>, not on capture class alone.</li>
  <li><strong>Separate ventilation from cooling</strong> where the shaft area or the latent load justifies it.</li>
  <li><strong>Measure the outdoor air</strong> with a real flow station on every unit.</li>
  <li><strong>Design for sand, salt and wash-down</strong> at every louvre.</li>
  <li><strong>Commission in wind and in season</strong>, recording outdoor conditions with every result.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  At 600&nbsp;m an ordinary day produces <strong>600&nbsp;Pa across the building</strong> — more than the fan's own static — so intake location, damper selection and plenum separation are ventilation design, not architectural detailing. Recover the outdoor air's enthalpy where the climate is humid, because on the coast fresh air is most of the latent load and a wheel is worth well over a hundred tons of chiller; specify filters on depth rather than class, because their pressure drop runs all year; and separate ventilation from cooling so the riser carries a tenth of the air and the fresh air is something you can actually measure.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Handbook — Fundamentals</em>, Airflow Around Buildings and Climatic Design Information chapters — boundary-layer wind profiles, pressure coefficients and design weather data.</li>
  <li>EN 1991-1-4 (Eurocode 1, wind actions) and ASCE 7 — wind speed profiles, terrain categories and external pressure coefficients.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Building Air Intake and Exhaust Design — separation distances, plume dispersion and re-entrainment geometry.</li>
  <li>ANSI/ASHRAE Standard 62.1 — <em>Ventilation for Acceptable Indoor Air Quality</em>: outdoor air rates, intake location and demand-controlled ventilation.</li>
  <li>ANSI/ASHRAE/IES Standard 90.1 — energy recovery requirements, fan power limits and filtration allowances.</li>
  <li>ISO 16890 / EN 779 — air filter classification (ePM1, ePM2.5, ePM10) and test methods; and Eurovent guidance on filter life-cycle energy.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — outdoor air strategy, riser planning and intake location in tall buildings.</li>
  <li>CIBSE <em>Guide B2 — Ventilation and Ductwork</em>; and Saudi Building Code <em>SBC 501</em> mechanical provisions.</li>
</ol>

<div class="tags">#Ventilation #OutdoorAir #FreshAir #IAQ #TallBuildings #MegatallBuildings #WindPressure #PressureCoefficient #BoundaryLayer #AirIntake #Louvre #EnergyRecovery #EnthalpyWheel #ERV #DOAS #Dehumidification #Psychrometrics #Filtration #ISO16890 #FanEnergy #ASHRAE62 #ASHRAE901 #DemandControlledVentilation #Commissioning #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const RHO=1.2;

/* ---------- CHART 1 : wind at intake ---------- */
const sV=document.getElementById('sV'),sAl=document.getElementById('sAl'),
      sZ=document.getElementById('sZ'),sFs=document.getElementById('sFs');
const CPW=0.8, CPL=-0.5;
const vAt=(v10,a,z)=>v10*Math.pow(Math.max(z,1)/10,a);
let windChart=new Chart(document.getElementById('windChart'),{
  data:{datasets:[
    {type:'line',label:'Windward (Cₚ +0.8)',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:3},
    {type:'line',label:'Leeward (Cₚ −0.5)',data:[],borderColor:'#1b4f72',borderWidth:3,pointRadius:0,order:2},
    {type:'scatter',label:'Your intake',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',title:{display:true,text:'Pressure on the louvre (Pa)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Height above grade (m)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.x)} Pa at ${fmt0(c.parsed.y)} m`}},
      annotation:{annotations:{
        fs:{type:'line',scaleID:'x',value:0,borderColor:'#b9770e',borderWidth:1.5,borderDash:[5,4],label:{display:true,content:'fan static',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updWind(){
  const v10=+sV.value,a=+sAl.value,z=+sZ.value,fs=+sFs.value;
  document.getElementById('vV').textContent=fmt1(v10)+' m/s';
  document.getElementById('vAl').textContent=fmt2(a);
  document.getElementById('vZ').textContent=z+' m';
  document.getElementById('vFs').textContent=fs+' Pa';
  const ys=[];for(let h=10;h<=1000;h+=10)ys.push(h);
  windChart.data.datasets[0].data=ys.map(h=>({x:+(CPW*0.5*RHO*Math.pow(vAt(v10,a,h),2)).toFixed(0),y:h}));
  windChart.data.datasets[1].data=ys.map(h=>({x:+(CPL*0.5*RHO*Math.pow(vAt(v10,a,h),2)).toFixed(0),y:h}));
  const v=vAt(v10,a,z), q=0.5*RHO*v*v;
  windChart.data.datasets[2].data=[{x:+(CPW*q).toFixed(0),y:z}];
  const span=Math.max(CPW*q*1.15,fs*1.15,60);
  windChart.options.scales.x.min=-span; windChart.options.scales.x.max=span;
  windChart.options.scales.y.max=1000;
  windChart.options.plugins.annotation.annotations.fs.value=fs;
  windChart.update('none');
  document.getElementById('rV').innerHTML=fmt1(v)+' <small>m/s</small>';
  document.getElementById('rWw').innerHTML='+'+fmt0(CPW*q)+' <small>Pa</small>';
  document.getElementById('rLw').innerHTML=fmt0(CPL*q)+' <small>Pa</small>';
  document.getElementById('rAc').innerHTML=fmt0((CPW-CPL)*q)+' <small>Pa</small>';
  const e=document.getElementById('rVd'), r=(CPW*q)/fs;
  if(r<0.25)      e.innerHTML='<span class="badge good">minor</span>';
  else if(r<0.75) e.innerHTML='<span class="badge warn">significant</span>';
  else            e.innerHTML='<span class="badge bad">wind dominates the fan</span>';
}
[sV,sAl,sZ,sFs].forEach(s=>s.addEventListener('input',updWind));updWind();

/* ---------- CHART 2 : enthalpy recovery ---------- */
const sOt=document.getElementById('sOt'),sOr=document.getElementById('sOr'),
      sOq=document.getElementById('sOq'),sEf=document.getElementById('sEf');
const enth=(T,W)=>1.006*T+W*(2501+1.86*T);
function humRatio(T,rh,P){P=P||101.325;const pws=0.61094*Math.exp(17.625*T/(T+243.04));const pw=rh*pws;return 0.62198*pw/(P-pw);}
const specVol=(T,W)=>0.287*(T+273.15)*(1+1.6078*W)/101.325;   // m³ per kg dry air
const H_RET=enth(24,humRatio(24,0.50));
let ervChart=new Chart(document.getElementById('ervChart'),{
  data:{datasets:[
    {type:'line',label:'Untreated outdoor-air load',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:3},
    {type:'line',label:'Load after recovery',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your climate',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:90,title:{display:true,text:'Outdoor relative humidity (%)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Outdoor-air cooling load (kW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} kW at ${fmt0(c.parsed.x)} % RH`}}}}
});
function updErv(){
  const T=+sOt.value,rh=+sOr.value/100,Q=+sOq.value,ef=+sEf.value/100;
  document.getElementById('vOt').textContent=fmt1(T)+' °C';
  document.getElementById('vOr').textContent=fmt0(rh*100)+' %';
  document.getElementById('vOq').textContent=fmt1(Q)+' m³/s';
  document.getElementById('vEf').textContent=fmt0(ef*100)+' %';
  const xs=[];for(let r=5;r<=90;r+=1)xs.push(r);
  const load=r=>{const W=humRatio(T,r/100);return Math.max(0,(Q/specVol(T,W))*(enth(T,W)-H_RET));};
  ervChart.data.datasets[0].data=xs.map(r=>({x:r,y:+load(r).toFixed(0)}));
  ervChart.data.datasets[1].data=xs.map(r=>({x:r,y:+(load(r)*(1-ef)).toFixed(0)}));
  const Wo=humRatio(T,rh), ho=enth(T,Wo), dh=ho-H_RET, L0=Math.max(0,(Q/specVol(T,Wo))*dh), rec=L0*ef;
  ervChart.data.datasets[2].data=[{x:rh*100,y:+L0.toFixed(0)}];
  ervChart.update('none');
  document.getElementById('rHo').innerHTML=fmt0(ho)+' <small>kJ/kg</small>';
  document.getElementById('rDh').innerHTML=fmt0(dh)+' <small>kJ/kg</small>';
  document.getElementById('rL0').innerHTML=fmt0(L0)+' <small>kW</small>';
  document.getElementById('rRe').innerHTML=fmt0(rec)+' <small>kW</small>';
  document.getElementById('rTr').innerHTML=fmt0(rec/3.517)+' <small>TR</small>';
}
[sOt,sOr,sOq,sEf].forEach(s=>s.addEventListener('input',updErv));updErv();

/* ---------- CHART 3 : filtration ---------- */
const sFq=document.getElementById('sFq'),sFd=document.getElementById('sFd'),
      sFe=document.getElementById('sFe'),sFh=document.getElementById('sFh');
let filtChart=new Chart(document.getElementById('filtChart'),{
  data:{datasets:[
    {type:'line',label:'Annual filtration energy',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your bank',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:40,max:400,title:{display:true,text:'Average filter pressure drop (Pa)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Annual fan energy for filtration (kWh)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} kWh at ${fmt0(c.parsed.x)} Pa`}}}}
});
function updFilt(){
  const Q=+sFq.value,dp=+sFd.value,eta=+sFe.value/100,hrs=+sFh.value;
  document.getElementById('vFq').textContent=fmt1(Q)+' m³/s';
  document.getElementById('vFd').textContent=dp+' Pa';
  document.getElementById('vFe').textContent=fmt0(eta*100)+' %';
  document.getElementById('vFh').textContent=hrs+' h';
  const kwh=d=>Q*d/1000/eta*hrs;
  const xs=[];for(let d=40;d<=400;d+=5)xs.push(d);
  filtChart.data.datasets[0].data=xs.map(d=>({x:d,y:+kwh(d).toFixed(0)}));
  filtChart.data.datasets[1].data=[{x:dp,y:+kwh(dp).toFixed(0)}];
  filtChart.update('none');
  const e0=kwh(dp), e1=kwh(Math.max(40,dp-50));
  document.getElementById('rFp').innerHTML=fmt1(Q*dp/1000/eta)+' <small>kW</small>';
  document.getElementById('rFe').innerHTML=fmt0(e0)+' <small>kWh</small>';
  document.getElementById('rFl').innerHTML=fmt0(e1)+' <small>kWh</small>';
  document.getElementById('rFs').innerHTML=fmt0(e0-e1)+' <small>kWh</small>';
  document.getElementById('rF20').innerHTML=fmt0(20*(e0-e1)/1000)+' <small>MWh</small>';
}
[sFq,sFd,sFe,sFh].forEach(s=>s.addEventListener('input',updFilt));updFilt();

window.addEventListener('load',function(){try{windChart.resize();ervChart.resize();filtChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='outdoor-air-ventilation-tall-buildings', cat='hvac', mins=17,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Outdoor Air &amp; Ventilation in Megatall Buildings: Wind Pressure, Intake Strategy, Energy Recovery &amp; Filtration',
    reg_title='Outdoor Air & Ventilation in Megatall Buildings: Wind Pressure, Intake Strategy, Energy Recovery & Filtration',
    reg_tag='HVAC · Ventilation · Outdoor Air',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Ventilation &middot; Outdoor Air &middot; Megatall Buildings',
    desc='Outdoor air and ventilation design in megatall buildings: how wind pressure at height exceeds the fan external static and short-circuits shared plenums, intake and discharge location and dispersion, what total-enthalpy recovery is really worth in a humid coastal versus dry inland climate, the annual fan energy hidden in filter pressure drop, and the case for separating ventilation from cooling — with three interactive charts and installation tricks.',
    og_desc='At 600 m an ordinary 10 m/s wind produces 600 Pa across the building — more than the fan static. Plus what an enthalpy wheel is worth in Jeddah versus Riyadh, and the annual energy hiding in your filter bank.',
    ld_desc='A design-perspective guide to outdoor air and ventilation in megatall buildings: boundary-layer wind pressure at intakes, plenum and damper strategy, intake and exhaust separation, total-enthalpy recovery evaluated on real psychrometrics, filtration pressure drop and fan energy, and dedicated outdoor-air systems.',
    img_alt='Technical cutaway of a megatall tower&rsquo;s ventilation system showing outdoor-air intake louvres on a mechanical floor, wind pressure acting on the windward and leeward faces, an energy recovery wheel and filter bank inside the air-handling plant, and the fresh-air riser feeding the floors',
    en_tag='HVAC &amp; Cooling &middot; Ventilation &middot; Outdoor Air &middot; Megatall',
    en_title='Outdoor Air &amp; Ventilation in Megatall Buildings: Wind Pressure, Intake Strategy, Energy Recovery &amp; Filtration',
    en_excerpt='Outdoor air is the one thing a tall building cannot manufacture &mdash; it has to be captured from a moving atmosphere that behaves very differently at 600&nbsp;m. Why an ordinary 10&nbsp;m/s street wind becomes 600&nbsp;Pa across the building and short-circuits any shared intake plenum, how to place intakes and discharges, what a total-enthalpy wheel is actually worth in Jeddah versus Riyadh (three times the difference), the annual fan energy hidden in filter pressure drop, and the case for separating ventilation from cooling &mdash; with three interactive charts.',
    en_search='outdoor air ventilation fresh air tall buildings megatall supertall high-rise indoor air quality IAQ wind pressure boundary layer power law terrain exponent pressure coefficient windward leeward air intake louvre free area face velocity plenum short circuit motorised damper reversal exhaust discharge separation dispersion re-entrainment plume cooling tower drift generator flue energy recovery enthalpy wheel ERV HRV effectiveness latent load psychrometrics humidity ratio dehumidification DOAS dedicated outdoor air system demand controlled ventilation CO2 filtration ISO 16890 ePM1 MERV pressure drop filter depth fan energy leakage class commissioning ASHRAE 62.1 90.1 sand salt corrosion MEP building services HVAC',
    ar_title='الهواء الخارجي والتهوية في المباني فائقة الارتفاع: ضغط الرياح ومواقع السحب واسترجاع الطاقة والفلترة',
    ar_excerpt='الهواء النقي هو الشيء الوحيد الذي لا يستطيع المبنى تصنيعه — بل يجب التقاطه من غلافٍ جويٍّ يتصرّف على ارتفاع ٦٠٠ متر تصرّفًا مختلفًا تمامًا. لماذا تتحوّل رياح عادية بسرعة ١٠ م/ث عند مستوى الشارع إلى ٦٠٠ باسكال عبر المبنى فتُحدث دائرة قِصر في أي غرفة سحب مشتركة، وكيف تُوضع فتحات السحب والطرد، وكم تساوي عجلة استرجاع الطاقة الكلية في جدة مقابل الرياض (الفارق ثلاثة أضعاف)، وطاقة المراوح السنوية المختبئة في فقد ضغط الفلاتر، ومبرّر فصل التهوية عن التبريد — مع ثلاثة رسوم تفاعلية.',
    ar_search='outdoor air ventilation fresh air tall buildings megatall wind pressure boundary layer pressure coefficient intake louvre plenum damper exhaust separation dispersion energy recovery enthalpy wheel ERV DOAS filtration ISO 16890 fan energy ASHRAE 62.1 الهواء الخارجي التهوية الهواء النقي المباني الشاهقة المباني فائقة الارتفاع جودة الهواء الداخلي ضغط الرياح الطبقة الحدية معامل الضغط الجهة المواجهة للريح الجهة الخلفية فتحة السحب الشيش المساحة الحرة سرعة الوجه غرفة التجميع دائرة القصر المخمدات المحركة انعكاس التدفق فتحة الطرد مسافة الفصل تشتت العادم إعادة السحب عمود برج التبريد عادم المولدات استرجاع الطاقة عجلة الإنثالبي كفاءة الاسترجاع الحمل الكامن الخواص السيكرومترية نسبة الرطوبة إزالة الرطوبة نظام الهواء الخارجي المخصص التهوية حسب الطلب ثاني أكسيد الكربون الفلترة عمق الفلتر فقد الضغط طاقة المروحة فئة التسرب التشغيل والاختبار الرمال الأملاح التآكل MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
