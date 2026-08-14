# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A mixed-use tower puts restaurants on the podium, a signature dining floor near the top, and staff kitchens somewhere in between — and every one of them needs a duct that runs, unbroken and uninterrupted, from the hood to the roof. That duct is lined with a combustible deposit, passes through occupied floors for hundreds of metres, and is one of the few elements in a tall building that is simultaneously a <strong>ventilation system, a fire hazard and a fire-rated compartment</strong>. It is also governed by a rule that no other duct in the building obeys: it has a <strong>minimum</strong> velocity, not just a maximum, and if the flow falls below it the grease stops travelling and starts accumulating.</p>

<h2 id="why">1 · Why a grease riser is not a duct</h2>
<ul class="clean">
  <li><strong>It carries fuel.</strong> Grease-laden vapour condenses on the duct wall. Over months it builds a layer that will sustain a fire the length of the riser, and a grease fire in a 300&nbsp;m vertical duct is exactly the vertical fire spread a tall building is designed to prevent.</li>
  <li><strong>It must be continuously welded and liquid-tight.</strong> No slip joints, no sealant-dependent seams, sloped back to the hood or to a drain point so condensate cannot pool in the run.</li>
  <li><strong>It must be enclosed in a fire-rated shaft</strong> for its full height with a rated wrap or construction, and it cannot share that shaft with anything else.</li>
  <li><strong>It has a minimum transport velocity.</strong> Codes require the air to move fast enough to keep droplets entrained — around <strong>2.5&nbsp;m/s absolute minimum</strong>, with 7.5–12.5&nbsp;m/s the practical design range. This is the constraint that makes variable-flow kitchen ventilation difficult.</li>
  <li><strong>It must be cleanable along its entire length.</strong> Access doors at every change of direction and at intervals up the riser — and in a tall building that means a cleaning route somebody has to physically reach, floor by floor, for the life of the building.</li>
</ul>

<h2 id="int-size">2 · Interactive: hood duty and riser size</h2>
<p>Exhaust rate follows the hood type and the appliance duty beneath it; the duct then follows from the transport velocity you choose.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Kitchen exhaust rate and grease riser diameter</div>
    <div class="fsub">Q = hood rate × hood length. Duct area = Q/v with v the design transport velocity; equivalent round diameter shown for a rectangular riser of the same area.</div>
  </div>
  <div class="chart-box"><canvas id="sizeChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Hood length <span id="vL">8.0 m</span></label>
      <input type="range" id="sL" min="1" max="20" value="8" step="0.5">
      <div class="hint">Total length of hood served by this riser.</div>
    </div>
    <div class="ctrl">
      <label>Hood duty rate <span id="vR">600 L/s·m</span></label>
      <input type="range" id="sR" min="200" max="1000" value="600" step="25">
      <div class="hint">Wall canopy: ~300 light, 400 medium, 600 heavy. Island canopies far higher.</div>
    </div>
    <div class="ctrl">
      <label>Transport velocity <span id="vV">10.0 m/s</span></label>
      <input type="range" id="sV" min="5" max="16" value="10" step="0.5">
      <div class="hint">Higher velocity = smaller duct but more fan energy and noise.</div>
    </div>
    <div class="ctrl">
      <label>Riser height <span id="vH">200 m</span></label>
      <input type="range" id="sH" min="20" max="600" value="200" step="10">
      <div class="hint">Hood to roof fan.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Exhaust rate</div><div class="v" id="rQ">4.80 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Duct area</div><div class="v" id="rA">0.48 <small>m²</small></div></div>
    <div class="cell"><div class="k">Round equivalent</div><div class="v" id="rD">782 <small>mm</small></div></div>
    <div class="cell"><div class="k">Riser friction</div><div class="v" id="rP">384 <small>Pa</small></div></div>
    <div class="cell"><div class="k">Shaft needed</div><div class="v" id="rS">1.2 <small>m²</small></div></div>
  </div>
</div>
<p class="fig-note">A heavy-duty 8&nbsp;m canopy needs <strong>4.8&nbsp;m³/s</strong>, which at 10&nbsp;m/s is a <strong>782&nbsp;mm</strong> round equivalent — and once wrapped, enclosed and given clearance it consumes about <strong>1.2&nbsp;m² of shaft</strong> for the full 200&nbsp;m to the roof. Push the velocity up to save shaft area and the friction climbs with the square: the same riser at 14&nbsp;m/s costs roughly twice the fan pressure. Two design consequences follow. First, <strong>the shaft must be reserved from concept</strong>, because it is unbroken and cannot be re-routed later. Second, group kitchens so they can share a riser only where a fire strategy permits it — every additional independent riser is another permanent hole through the core.</p>

<h2 id="int-turndown">3 · Interactive: the turndown trap</h2>
<p>Kitchen exhaust is the largest single air consumer in a restaurant and an obvious candidate for demand control — hoods sense cooking activity and modulate. But grease ducts have a floor below which they stop transporting, and a variable-flow system that ignores it is building a fuel load in a shaft.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Transport velocity and fan power against exhaust turndown</div>
    <div class="fsub">Velocity falls in direct proportion to flow; fan power falls with its cube. The dashed line is the code minimum transport velocity below which grease no longer stays entrained.</div>
  </div>
  <div class="chart-box"><canvas id="turnChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Design velocity <span id="vDv">10.0 m/s</span></label>
      <input type="range" id="sDv" min="5" max="16" value="10" step="0.5">
      <div class="hint">Velocity at full exhaust rate. Higher design velocity buys more turndown range.</div>
    </div>
    <div class="ctrl">
      <label>Operating turndown <span id="vT">50 %</span></label>
      <input type="range" id="sT" min="20" max="100" value="50" step="1">
      <div class="hint">Flow as a share of design under demand control.</div>
    </div>
    <div class="ctrl">
      <label>Minimum transport velocity <span id="vM">2.5 m/s</span></label>
      <input type="range" id="sM" min="1.5" max="6" value="2.5" step="0.1">
      <div class="hint">Code floor — around 2.5 m/s (500 fpm) in most jurisdictions.</div>
    </div>
    <div class="ctrl">
      <label>Fan power at design <span id="vP2">22 kW</span></label>
      <input type="range" id="sP2" min="2" max="120" value="22" step="1">
      <div class="hint">Exhaust fan absorbed power at full flow.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Velocity now</div><div class="v" id="rVn">5.0 <small>m/s</small></div></div>
    <div class="cell"><div class="k">Lowest safe turndown</div><div class="v" id="rTm">25 <small>%</small></div></div>
    <div class="cell"><div class="k">Fan power now</div><div class="v" id="rPn">2.8 <small>kW</small></div></div>
    <div class="cell"><div class="k">Power saved</div><div class="v" id="rPs">88 <small>%</small></div></div>
    <div class="cell"><div class="k">Status</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">Design at 10&nbsp;m/s and you can turn down to <strong>25&nbsp;%</strong> before the velocity reaches the 2.5&nbsp;m/s floor — and at 50&nbsp;% flow the fan is already drawing only <strong>12&nbsp;% of its design power</strong>. That is the case for demand-controlled kitchen ventilation in one line: the savings are enormous and they are available well above the safety limit. The design move that unlocks it is to <strong>choose a higher design velocity deliberately</strong>, because the turndown range you get is the ratio between design and minimum velocity. Design at 7.5&nbsp;m/s and you only reach 33&nbsp;%; design at 12.5&nbsp;m/s and you reach 20&nbsp;%. Then set the control minimum in the BMS at the velocity limit, not at the fan's minimum speed, and alarm if it is ever violated.</p>

<h2 id="int-makeup">4 · Interactive: make-up air and what a shortfall does</h2>
<p>Every cubic metre extracted must be replaced. If the dedicated make-up air is short, the kitchen draws the difference from wherever it can — the restaurant, the lobby, the lift shaft — and a tall building has a very large reservoir to be pulled from.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Make-up air shortfall and the resulting pressure</div>
    <div class="fsub">Shortfall = exhaust − dedicated make-up. Δp estimated by inverting Q = 0.83·A·√Δp — the EN 12101-6 / NFPA 92 form, with a discharge coefficient of 0.65 folded into the constant — across the kitchen&rsquo;s leakage and door openings. The make-up air load uses the dry-air mass flow at 40 °C / 55 % RH rather than a fixed density.</div>
  </div>
  <div class="chart-box"><canvas id="muChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Exhaust rate <span id="vQe">4.80 m³/s</span></label>
      <input type="range" id="sQe" min="0.5" max="20" value="4.8" step="0.1">
      <div class="hint">Total kitchen extract including hoods and general extract.</div>
    </div>
    <div class="ctrl">
      <label>Dedicated make-up <span id="vMu">85 %</span></label>
      <input type="range" id="sMu" min="40" max="100" value="85" step="1">
      <div class="hint">Tempered supply provided specifically to the kitchen.</div>
    </div>
    <div class="ctrl">
      <label>Opening leakage area <span id="vAo">0.35 m²</span></label>
      <input type="range" id="sAo" min="0.05" max="2" value="0.35" step="0.05">
      <div class="hint">Effective area of doors, hatches and gaps between kitchen and adjacent space.</div>
    </div>
    <div class="ctrl">
      <label>Door tolerance <span id="vDt">25 Pa</span></label>
      <input type="range" id="sDt" min="10" max="80" value="25" step="1">
      <div class="hint">Negative pressure at which doors become hard to use and odour control fails.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Shortfall</div><div class="v" id="rSf">0.72 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Kitchen pressure</div><div class="v" id="rDp">−6.1 <small>Pa</small></div></div>
    <div class="cell"><div class="k">Make-up needed</div><div class="v" id="rMn">4.08 <small>m³/s</small></div></div>
    <div class="cell"><div class="k">Cooling on make-up</div><div class="v" id="rCl">261 <small>kW</small></div></div>
    <div class="cell"><div class="k">Status</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rMv"></span></div></div>
  </div>
</div>
<p class="fig-note">Providing 85&nbsp;% dedicated make-up leaves a <strong>0.72&nbsp;m³/s</strong> shortfall — deliberately, so the kitchen stays slightly negative and odours do not migrate into the restaurant. With a reasonable opening area that is only a few pascals, which is exactly right. Drop the make-up to 60&nbsp;% and the kitchen goes strongly negative, doors become hard to open, the hoods lose capture because air is arriving sideways through the doorway rather than from the make-up plenum, and in a tall building the deficit is ultimately drawn down the lift shaft. Note the last readout: conditioning <strong>4&nbsp;m³/s</strong> of humid Gulf outdoor air is over <strong>260&nbsp;kW</strong> of cooling — which is why partially untempered or evaporatively cooled make-up air, delivered locally at the hood, is worth designing properly rather than dumping the whole load on the building's chilled water.</p>

<h2 id="fire">5 · Fire strategy for the riser</h2>
<ul class="clean">
  <li><strong>The hood suppression system protects the hood and the first part of the duct</strong>, not the riser. Wet-chemical systems discharge at the plenum and the duct collar; the 200&nbsp;m above them is protected by <em>construction</em> and by cleaning, not by suppression.</li>
  <li><strong>The shaft rating is the primary protection.</strong> A continuously rated enclosure or an approved duct wrap for the full height, with the rating maintained at every penetration and every access door.</li>
  <li><strong>The fan runs during a fire</strong> in most strategies, to keep the fire in the duct rather than let it spill into the hood — so the fan, its motor, its supports and its power supply must all survive the temperature. Check this explicitly; it is often assumed and rarely specified.</li>
  <li><strong>Do not fit fire dampers in a grease duct.</strong> They collect grease, they fail, and they defeat the extract when it is most needed. Protection is by enclosure, not by damping.</li>
  <li><strong>Discharge at the roof, away from intakes.</strong> High-velocity vertical discharge, well clear of any fresh-air intake, the helipad and any openable window — the dispersion check described in <a href="outdoor-air-ventilation-tall-buildings.html">outdoor air and ventilation</a> applies here more than anywhere.</li>
  <li><strong>Grease removal at the hood is what protects everything downstream.</strong> High-efficiency baffle or cartridge filters, or a UV/ozone system where the riser is long and access is hard, reduce what reaches the duct in the first place. On a 200&nbsp;m riser this is not a refinement — it is the main line of defence.</li>
</ul>

<h2 id="install">6 · Installation, cleaning &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Reserve the shaft at concept, and defend it.</strong> A grease riser cannot be re-routed, cannot share a shaft, and cannot be offset casually — every offset is a grease trap and an access door.</li>
  <li><strong>Design the cleaning route before the duct.</strong> Access doors at every change of direction and at regular intervals up the riser, each one reachable from a floor or a platform. If the cleaning contractor cannot reach an access door, that section will never be cleaned and will eventually be the fire.</li>
  <li><strong>Weld it continuously and test it.</strong> Liquid-tight, continuously welded external seams, light-tested or equivalent, with the test recorded per section as it is built — you cannot inspect it afterwards.</li>
  <li><strong>Slope the duct and provide a drain point.</strong> Horizontal runs graded back to the hood or to an accessible residue trap, never to a low point buried in a ceiling.</li>
  <li><strong>Insulate and clear the rating.</strong> Maintain the specified clearance to combustibles or the approved wrap system, and coordinate that clearance in the shaft before other trades fill it.</li>
  <li><strong>Balance the hood at the hood.</strong> Capture and containment is proved by smoke test at the hood face with the make-up running, not by measuring the duct flow — a hood can be at design flow and still fail to capture if the make-up air is arriving from the wrong direction.</li>
  <li><strong>Commission the demand control against velocity.</strong> Verify the minimum-flow setting corresponds to the code transport velocity, and prove the alarm.</li>
  <li><strong>Hand over a cleaning schedule with frequencies by duty</strong> — heavy-duty solid-fuel or wok cooking needs far more frequent cleaning than a light-duty pastry kitchen, and the schedule should name intervals and access points.</li>
</ul>

<h2 id="checklist">7 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Reserve a dedicated, unbroken, fire-rated shaft</strong> per riser at concept stage.</li>
  <li><strong>Size on hood duty, then choose the transport velocity deliberately</strong> to buy the turndown range you want.</li>
  <li><strong>Set the demand-control minimum at the velocity limit</strong>, not at the fan minimum, and alarm it.</li>
  <li><strong>Provide 80–90&nbsp;% dedicated tempered make-up</strong>, delivered so it does not disturb capture.</li>
  <li><strong>Check the kitchen&rsquo;s pressure relationship</strong> to adjacent spaces and to the building.</li>
  <li><strong>Maximise grease removal at the hood</strong> — the riser can only be protected by what never enters it.</li>
  <li><strong>Rate the enclosure for the full height</strong>; no fire dampers in the duct.</li>
  <li><strong>Confirm the fan survives fire conditions</strong>, with its power supply.</li>
  <li><strong>Design and prove the cleaning access</strong>, and issue a duty-based cleaning schedule.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A grease riser is the only duct in the building with a <strong>minimum</strong> velocity as well as a maximum, and the ratio between your design velocity and that floor is exactly the turndown you are allowed — design at 10&nbsp;m/s and demand control can take you to 25&nbsp;% flow and 12&nbsp;% fan power, which is an enormous saving available entirely within the safety limit. Everything else follows from the fact that it is a <strong>combustible-lined, unbroken, fire-rated shaft running hundreds of metres through occupied floors</strong>: reserve it at concept, remove as much grease as possible at the hood because that is the only place you can, design the cleaning access before the duct, and provide 80–90&nbsp;% tempered make-up so the hoods actually capture and the kitchen does not end up breathing through the lift shaft.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>NFPA 96 — <em>Standard for Ventilation Control and Fire Protection of Commercial Cooking Operations</em>: duct construction, transport velocity, access, clearance and cleaning.</li>
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Kitchen Ventilation chapter — hood types, exhaust rates, capture and containment, make-up air strategies.</li>
  <li>ASHRAE Standard 154 — <em>Ventilation for Commercial Cooking Operations</em>; and ASTM F1704 for hood capture and containment testing.</li>
  <li>DW/172 <em>Specification for Kitchen Ventilation Systems</em> (BESA) — UK practice on grease duct construction, access and cleaning.</li>
  <li>BS EN 16282 series — equipment for commercial kitchens: ventilation components and design.</li>
  <li>NFPA 17A — wet chemical extinguishing systems; and UL 300 for hood suppression listing.</li>
  <li>ANSI/ASHRAE/IES Standard 90.1 — kitchen exhaust energy requirements and demand-controlled kitchen ventilation provisions.</li>
  <li>Saudi Building Code <em>SBC 501</em> and <em>SBC 801</em> — mechanical and fire provisions for commercial cooking operations.</li>
</ol>

<div class="tags">#KitchenVentilation #GreaseDuct #GreaseRiser #NFPA96 #TallBuildings #MegatallBuildings #MixedUse #CommercialKitchen #Hood #CaptureAndContainment #TransportVelocity #DemandControlledKitchenVentilation #DCKV #MakeUpAir #TemperedAir #KitchenPressure #FireRatedShaft #DuctWrap #HoodSuppression #UL300 #Cleaning #AccessDoors #RoofDischarge #Dispersion #Commissioning #MEP #BuildingServices #HVAC</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const RHO=1.2;

/* ---------- CHART 1 : hood duty & riser size ---------- */
const sL=document.getElementById('sL'),sR=document.getElementById('sR'),
      sV=document.getElementById('sV'),sH=document.getElementById('sH');
const dwPa=(v,D,L,f)=>f*(L/D)*RHO*v*v/2;
let sizeChart=new Chart(document.getElementById('sizeChart'),{
  data:{datasets:[
    {type:'line',label:'Duct area (m²)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:3},
    {type:'line',label:'Riser friction (Pa)',data:[],borderColor:'#c0392b',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your riser',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:16,title:{display:true,text:'Transport velocity (m/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Duct cross-section (m²)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Riser friction (Pa)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updSize(){
  const L=+sL.value,R=+sR.value,v=+sV.value,H=+sH.value;
  document.getElementById('vL').textContent=fmt1(L)+' m';
  document.getElementById('vR').textContent=R+' L/s·m';
  document.getElementById('vV').textContent=fmt1(v)+' m/s';
  document.getElementById('vH').textContent=H+' m';
  const Q=L*R/1000;
  const area=x=>Q/x, dia=x=>Math.sqrt(4*area(x)/Math.PI);
  const fric=x=>dwPa(x,dia(x),H*1.25,0.02);
  const xs=[];for(let x=5;x<=16;x+=0.25)xs.push(+x.toFixed(2));
  sizeChart.data.datasets[0].data=xs.map(x=>({x:x,y:+area(x).toFixed(3)}));
  sizeChart.data.datasets[1].data=xs.map(x=>({x:x,y:+fric(x).toFixed(0)}));
  sizeChart.data.datasets[2].data=[{x:v,y:+area(v).toFixed(3)}];
  sizeChart.update('none');
  document.getElementById('rQ').innerHTML=fmt2(Q)+' <small>m³/s</small>';
  document.getElementById('rA').innerHTML=fmt2(area(v))+' <small>m²</small>';
  document.getElementById('rD').innerHTML=fmt0(dia(v)*1000)+' <small>mm</small>';
  document.getElementById('rP').innerHTML=fmt0(fric(v))+' <small>Pa</small>';
  document.getElementById('rS').innerHTML=fmt1(area(v)*2.5)+' <small>m²</small>';
}
[sL,sR,sV,sH].forEach(s=>s.addEventListener('input',updSize));updSize();

/* ---------- CHART 2 : turndown ---------- */
const sDv=document.getElementById('sDv'),sT=document.getElementById('sT'),
      sM=document.getElementById('sM'),sP2=document.getElementById('sP2');
let turnChart=new Chart(document.getElementById('turnChart'),{
  data:{datasets:[
    {type:'line',label:'Transport velocity (m/s)',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,yAxisID:'y',order:3},
    {type:'line',label:'Fan power (kW)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y1',order:2},
    {type:'scatter',label:'Operating point',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:20,max:100,title:{display:true,text:'Exhaust flow (% of design)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',min:0,title:{display:true,text:'Transport velocity (m/s)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,title:{display:true,text:'Fan power (kW)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      annotation:{annotations:{
        mv:{type:'line',scaleID:'y',yScaleID:'y',value:2.5,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'minimum transport velocity',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updTurn(){
  const dv=+sDv.value,t=+sT.value/100,mv=+sM.value,P=+sP2.value;
  document.getElementById('vDv').textContent=fmt1(dv)+' m/s';
  document.getElementById('vT').textContent=fmt0(t*100)+' %';
  document.getElementById('vM').textContent=fmt1(mv)+' m/s';
  document.getElementById('vP2').textContent=P+' kW';
  const xs=[];for(let x=20;x<=100;x+=1)xs.push(x);
  turnChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(dv*x/100).toFixed(2)}));
  turnChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(P*Math.pow(x/100,3)).toFixed(2)}));
  turnChart.data.datasets[2].data=[{x:t*100,y:+(dv*t).toFixed(2)}];
  turnChart.options.plugins.annotation.annotations.mv.value=mv;
  turnChart.update('none');
  const vNow=dv*t, tMin=100*mv/dv, pNow=P*Math.pow(t,3);
  document.getElementById('rVn').innerHTML=fmt1(vNow)+' <small>m/s</small>';
  document.getElementById('rTm').innerHTML=fmt0(tMin)+' <small>%</small>';
  document.getElementById('rPn').innerHTML=fmt1(pNow)+' <small>kW</small>';
  document.getElementById('rPs').innerHTML=fmt0(100*(1-Math.pow(t,3)))+' <small>%</small>';
  const v=document.getElementById('rVd');
  if(vNow<mv)          v.innerHTML='<span class="badge bad">below transport velocity</span>';
  else if(vNow<mv*1.2) v.innerHTML='<span class="badge warn">at the limit</span>';
  else                 v.innerHTML='<span class="badge good">grease stays entrained</span>';
}
[sDv,sT,sM,sP2].forEach(s=>s.addEventListener('input',updTurn));updTurn();

/* ---------- CHART 3 : make-up air ---------- */
const sQe=document.getElementById('sQe'),sMu=document.getElementById('sMu'),
      sAo=document.getElementById('sAo'),sDt=document.getElementById('sDt');
const dpFromQ=(Q,A)=>Math.pow(Q/(0.83*Math.max(A,0.01)),2);   // inverse of the EN 12101-6 / NFPA 92 form Q = 0.83·A·√Δp
let muChart=new Chart(document.getElementById('muChart'),{
  data:{datasets:[
    {type:'line',label:'Kitchen negative pressure (Pa)',data:[],borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,0.08)',borderWidth:3,pointRadius:0,fill:true,order:3},
    {type:'scatter',label:'Your design',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:40,max:100,title:{display:true,text:'Dedicated make-up air (% of exhaust)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Negative pressure in the kitchen (Pa)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      annotation:{annotations:{
        dt:{type:'line',scaleID:'y',yScaleID:'y',value:25,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'door / odour limit',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updMu(){
  const Qe=+sQe.value,mu=+sMu.value/100,A=+sAo.value,dt=+sDt.value;
  document.getElementById('vQe').textContent=fmt2(Qe)+' m³/s';
  document.getElementById('vMu').textContent=fmt0(mu*100)+' %';
  document.getElementById('vAo').textContent=fmt2(A)+' m²';
  document.getElementById('vDt').textContent=dt+' Pa';
  const xs=[];for(let x=40;x<=100;x+=1)xs.push(x);
  muChart.data.datasets[0].data=xs.map(x=>({x:x,y:+dpFromQ(Qe*(1-x/100),A).toFixed(2)}));
  const sf=Qe*(1-mu), dp=dpFromQ(sf,A);
  muChart.data.datasets[1].data=[{x:mu*100,y:+dp.toFixed(2)}];
  muChart.options.plugins.annotation.annotations.dt.value=dt;
  muChart.options.scales.y.max=Math.max(dpFromQ(Qe*0.6,A)*1.1,dt*1.5);
  muChart.update('none');
  document.getElementById('rSf').innerHTML=fmt2(sf)+' <small>m³/s</small>';
  document.getElementById('rDp').innerHTML='−'+fmt1(dp)+' <small>Pa</small>';
  document.getElementById('rMn').innerHTML=fmt2(Qe*mu)+' <small>m³/s</small>';
  document.getElementById('rCl').innerHTML=fmt0((Qe*mu/0.924)*(107-47.8))+' <small>kW</small>';   // 0.924 m³/kg dry air at 40 °C / 55 % RH
  const v=document.getElementById('rMv');
  if(dp>dt)        v.innerHTML='<span class="badge bad">too negative — capture will fail</span>';
  else if(mu>=0.98)v.innerHTML='<span class="badge warn">no negative bias — odour risk</span>';
  else             v.innerHTML='<span class="badge good">slightly negative — correct</span>';
}
[sQe,sMu,sAo,sDt].forEach(s=>s.addEventListener('input',updMu));updMu();

window.addEventListener('load',function(){try{sizeChart.resize();turnChart.resize();muChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='kitchen-exhaust-grease-risers-tall-buildings', cat='hvac', mins=14,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Kitchen Exhaust &amp; Grease Risers in Tall Buildings: Transport Velocity, Turndown &amp; Make-Up Air',
    reg_title='Kitchen Exhaust & Grease Risers in Tall Buildings: Transport Velocity, Turndown & Make-Up Air',
    reg_tag='HVAC · Kitchen Ventilation · Grease Risers',
    breadcrumb='HVAC &amp; Cooling',
    tag_line='HVAC &middot; Kitchen Ventilation &middot; Grease Risers &middot; Fire Strategy',
    desc='Kitchen exhaust and grease riser design in tall buildings: why a grease duct is the only duct with a minimum velocity as well as a maximum, hood duty and riser sizing, how design velocity sets the demand-control turndown range, make-up air and the pressure relationship that decides whether hoods capture, fire strategy for an unbroken riser through occupied floors, and cleaning access — with three interactive charts and installation tricks.',
    og_desc='A grease riser is the only duct in the building with a minimum velocity. Design at 10 m/s and demand control reaches 25 percent flow and 12 percent fan power — entirely within the safety limit.',
    ld_desc='A design-perspective guide to kitchen exhaust and grease risers in tall buildings: hood exhaust rates and duct sizing, transport velocity and demand-controlled turndown, make-up air and kitchen pressure relationships, fire strategy and shaft rating, grease removal at source, and cleaning access.',
    img_alt='Technical cutaway of a tall building showing a commercial kitchen with an extract hood on a podium level and a continuous grease riser running up a dedicated fire-rated shaft through the occupied floors to a discharge fan at roof level',
    en_tag='HVAC &amp; Cooling &middot; Kitchen Ventilation &middot; Grease Risers &middot; Fire',
    en_title='Kitchen Exhaust &amp; Grease Risers in Tall Buildings: Transport Velocity, Turndown &amp; Make-Up Air',
    en_excerpt='A mixed-use tower puts kitchens on the podium and near the crown, and every one needs a duct that runs unbroken to the roof &mdash; lined with combustible deposit, passing through occupied floors, at once a ventilation system, a fire hazard and a fire-rated compartment. It is governed by a rule no other duct obeys: a <strong>minimum</strong> velocity. Design at 10&nbsp;m/s and demand control reaches 25&nbsp;% flow and 12&nbsp;% fan power, entirely within the limit. Plus make-up air and the pressure relationship that decides whether the hoods capture at all &mdash; with three interactive charts.',
    en_search='kitchen exhaust grease duct grease riser tall buildings megatall mixed use commercial kitchen hood wall canopy island canopy capture and containment exhaust rate duty light medium heavy transport velocity minimum velocity 500 fpm demand controlled kitchen ventilation DCKV turndown fan power cube law make-up air tempered air untempered kitchen pressure negative odour migration NFPA 96 continuously welded liquid tight access doors cleaning schedule fire rated shaft duct wrap clearance to combustibles hood suppression wet chemical UL 300 no fire dampers roof discharge dispersion intake separation grease filters baffle cartridge UV ozone commissioning smoke test MEP building services HVAC',
    ar_title='شفط المطابخ ومواسير الشحوم الصاعدة في المباني الشاهقة: سرعة النقل والتخفيض وهواء التعويض',
    ar_excerpt='البرج متعدد الاستخدامات يضع مطابخ في القاعدة وقرب القمة، وكل واحد منها يحتاج مجرى هوائيًا متصلًا حتى السطح — مبطنًا برواسب قابلة للاشتعال، يمر عبر طوابق مأهولة، وهو في آنٍ واحد نظام تهوية وخطر حريق وحيز مقاوم للحريق. ويحكمه قانون لا يخضع له أي مجرى آخر: سرعة <strong>دنيا</strong>. صمّم عند ١٠ م/ث ويصل التحكم حسب الطلب إلى ٢٥٪ من التدفق و١٢٪ من قدرة المروحة، ضمن الحد الآمن تمامًا. مع هواء التعويض وعلاقة الضغط التي تحدد ما إذا كانت المظلات ستلتقط الأبخرة أصلًا — مع ثلاثة رسوم تفاعلية.',
    ar_search='kitchen exhaust grease duct riser NFPA 96 transport velocity DCKV turndown make-up air kitchen pressure fire rated shaft hood suppression cleaning access شفط المطابخ مجرى الشحوم الماسورة الصاعدة المباني الشاهقة متعدد الاستخدامات المطبخ التجاري مظلة الشفط المظلة الجدارية المظلة الجزيرة الالتقاط والاحتواء معدل الشفط الخدمة الخفيفة المتوسطة الثقيلة سرعة النقل السرعة الدنيا التحكم في تهوية المطبخ حسب الطلب التخفيض قدرة المروحة قانون التكعيب هواء التعويض الهواء المكيف ضغط المطبخ الضغط السالب انتقال الروائح اللحام المستمر محكم ضد السوائل أبواب الوصول جدول التنظيف المنور المقاوم للحريق لفائف العزل الخلوص عن المواد القابلة للاشتعال إطفاء المظلة الكيماوي الرطب عدم استخدام مخمدات الحريق التصريف من السطح التشتت فصل فتحات السحب مرشحات الشحوم الأشعة فوق البنفسجية الأوزون التشغيل والاختبار اختبار الدخان MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
