# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">Every mechanical floor in a tower sits directly above somebody's bedroom and directly below somebody's boardroom. The plant on it runs continuously, is bolted to a structure specifically engineered to be light and flexible, and radiates into a building where sound travels through concrete far better than through air. Yet vibration isolation is routinely specified as a line item — "spring isolators, 25&nbsp;mm deflection" — copied between projects without anybody checking the one number that decides whether it works at all. And when it is wrong the result is not slightly worse: below a critical ratio, an isolator does not reduce transmission, it <strong>amplifies</strong> it. A 6&nbsp;mm rubber pad under a 600&nbsp;rpm machine delivers 29&nbsp;% isolation; under a slower machine it makes things worse than a rigid mount.</p>

<h2 id="why">1 · Why towers are acoustically unforgiving</h2>
<ul class="clean">
  <li><strong>There is no buffer.</strong> In a low-rise building plant sits on a roof or in a basement with a car park between it and anyone who cares. On a mechanical floor there is one slab between a 150&nbsp;kW machine and a paying tenant.</li>
  <li><strong>The structure is efficient and therefore lively.</strong> Post-tensioned slabs and light long-span floors have low mass and low damping — exactly the properties that transmit structure-borne vibration well.</li>
  <li><strong>The paths multiply.</strong> Every pipe, duct, cable tray, conduit and hanger crossing from a plant room is a flanking path. The isolators can be perfect and the noise still arrives through a rigidly clamped chilled-water riser.</li>
  <li><strong>Nobody can fix it later.</strong> Once the plant is commissioned, the slab is cast and the risers are anchored, the remedies are limited, disruptive and expensive.</li>
  <li><strong>Expectations are high.</strong> Residential and hotel floors in a landmark tower are specified at NR&nbsp;25 or lower — a target that leaves almost no margin against a machine radiating 95&nbsp;dB of sound power one slab away.</li>
</ul>

<h2 id="theory">2 · The one equation that decides everything</h2>
<p>A machine on isolators is a mass on a spring. Its natural frequency depends only on how far the isolator deflects under the load:</p>
<div class="eq">\[ f_n \;=\; \frac{15.76}{\sqrt{\delta}} \quad(\text{Hz},\ \delta\ \text{in mm}), \qquad T \;=\; \frac{1}{\left|(f/f_n)^2 - 1\right|} \]</div>
<p>where \(T\) is transmissibility — the fraction of the disturbing force that reaches the structure — and \(f\) is the disturbing frequency, usually the running speed. The behaviour has three regions, and only one of them is useful:</p>
<ul class="clean">
  <li><strong>\(f/f_n < 1\)</strong> — the machine runs below resonance. The isolator does essentially nothing.</li>
  <li><strong>\(f/f_n \approx 1\)</strong> — <strong>resonance</strong>. Transmission is amplified, potentially enormously. This is where equipment shakes itself and its surroundings apart.</li>
  <li><strong>\(f/f_n > \sqrt{2}\)</strong> — isolation finally begins, and improves as the ratio grows. Practical design targets \(f/f_n \ge 3\), and \(\ge 5\) where the receiving space is sensitive.</li>
</ul>

<div class="callout warn">
  <span class="lbl">The specification that guarantees failure</span>
  Specifying an isolator by <strong>type</strong> — "neoprene pads" or "spring mounts" — instead of by <strong>static deflection</strong> is the single most common error in this field, because deflection is the only property in the equation. A 6&nbsp;mm neoprene pad has a natural frequency of 6.4&nbsp;Hz, so it needs the machine to run above 9.1&nbsp;Hz (546&nbsp;rpm) just to isolate at all, and provides only 29&nbsp;% isolation at 600&nbsp;rpm. The same pad under a 300&nbsp;rpm cooling tower gearbox sits near resonance and makes the problem worse. Always specify the minimum static deflection, and always check it against the <em>lowest</em> speed the machine will run at — which, on a variable-speed drive, is not the nameplate speed.
</div>

<h2 id="int-vib">3 · Interactive: isolation efficiency vs static deflection</h2>
<p>Set the machine speed and the isolator deflection. The curve is the fraction of vibration transmitted into the structure; the peak on the left is resonance. Note where variable-speed operation puts you — a machine isolated correctly at 1,450&nbsp;rpm may be sitting on the resonant peak at 30&nbsp;% speed.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Vibration transmissibility vs isolator static deflection</div>
    <div class="fsub">f&#110; = 15.76/√δ with δ in mm. T = √(1+(2ζr)²) ⁄ √((1−r²)²+(2ζr)²), with r = f/f&#110; and ζ the damping ratio. Isolation efficiency = (1 − T). The shaded band is the deflection range in which the <em>turndown</em> speed sits below f/f&#110; = √2 — amplification, not isolation.</div>
  </div>
  <div class="chart-box"><canvas id="vibChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Machine speed <span id="vR">1450 rpm</span></label>
      <input type="range" id="sR" min="200" max="3600" value="1450" step="10">
      <div class="hint">Disturbing frequency = speed ÷ 60. Use the lowest speed a VFD will hold.</div>
    </div>
    <div class="ctrl">
      <label>Static deflection <span id="vD">25 mm</span></label>
      <input type="range" id="sD" min="2" max="100" value="25" step="1">
      <div class="hint">The only isolator property that matters. Springs 25–75 mm; neoprene 5–10 mm.</div>
    </div>
    <div class="ctrl">
      <label>Damping ratio <span id="vZ">0.05</span></label>
      <input type="range" id="sZ" min="0.01" max="0.25" value="0.05" step="0.01">
      <div class="hint">Steel springs ≈ 0.02–0.05; neoprene ≈ 0.08–0.12. Damping limits the resonant peak but slightly worsens isolation.</div>
    </div>
    <div class="ctrl">
      <label>Turndown speed <span id="vT">40 %</span></label>
      <input type="range" id="sT" min="20" max="100" value="40" step="1">
      <div class="hint">Minimum VFD speed — checks the isolator at the machine's slowest running point.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Natural frequency</div><div class="v" id="rFn">3.15 <small>Hz</small></div></div>
    <div class="cell"><div class="k">Frequency ratio</div><div class="v" id="rRt">7.67</div></div>
    <div class="cell"><div class="k">Isolation</div><div class="v" id="rEf">97.8 <small>%</small></div></div>
    <div class="cell"><div class="k">At turndown</div><div class="v" id="rTd">87.6 <small>%</small></div></div>
    <div class="cell"><div class="k">Verdict</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rVd"></span></div></div>
  </div>
</div>
<p class="fig-note">A 1,450&nbsp;rpm pump on 25&nbsp;mm springs gives <strong>97.8&nbsp;% isolation</strong> — a frequency ratio of 7.7, comfortably clear of resonance. Drop the deflection to 6&nbsp;mm and it falls to 91.9&nbsp;%; that sounds close, but the transmitted force has nearly quadrupled. Now drag the machine speed down to 400&nbsp;rpm on the same 6&nbsp;mm pad and the ratio falls below √2 — the mount amplifies. This is exactly what happens to a variable-speed machine at low turndown, and it is why the isolator must be selected for the <strong>slowest speed the drive will hold</strong>, not the nameplate.</p>

<h2 id="paths">4 · Flanking paths — where the isolation actually leaks</h2>
<p>A perfectly isolated machine still transmits if anything rigid connects it to the structure. In order of how often they are the cause:</p>
<ul class="clean">
  <li><strong>Pipework.</strong> The largest and stiffest connection. Flexible connectors at the machine deal with the first metre; beyond that the <strong>first three to five hangers must be resiliently isolated</strong> with deflection matched to the machine's. Rigidly clamped risers carry pump vibration hundreds of metres.</li>
  <li><strong>Ductwork.</strong> Flexible connections at the fan plus resilient hangers on the first section, and — critically — no rigid contact where the duct passes through the plant room wall. Pack the penetration resiliently and seal it acoustically.</li>
  <li><strong>Conduit, cable tray and drainage.</strong> Small, stiff, easily forgotten, and often the last path left when everything else has been fixed.</li>
  <li><strong>Inertia bases short-circuited by grout or debris.</strong> A base that has been grouted solid, or that has construction rubble under it, is not isolated at all. This is astonishingly common and it is invisible once the plant room is finished.</li>
  <li><strong>Snubbers and limit stops touching in normal operation.</strong> Seismic restraints must have clearance in service; set hard against the base they are a direct rigid path.</li>
</ul>
<p>Flexible connectors deserve a warning of their own: they are for <em>vibration</em>, never for correcting misalignment, and a connector installed in tension or offset transmits more than the rigid pipe it replaced.</p>

<h2 id="int-room">5 · Interactive: plant-room level and the partition you need</h2>
<p>Equipment sound power sets the level inside the plant room; the room's absorption modifies it; and the difference between that and the target next door is the transmission loss the separating construction must deliver.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Plant-room sound pressure and required partition performance</div>
    <div class="fsub">L&#112; = L&#119; + 10·log&#8321;&#8320;(Q/4πr² + 4/R), R = Sα/(1−α). Required TL = L&#112;,&#115;&#111;&#117;&#114;&#99;&#101; − L&#112;,&#116;&#97;&#114;&#103;&#101;&#116; + 10·log&#8321;&#8320;(S&#119;&#97;&#108;&#108;/A&#114;&#111;&#111;&#109;).</div>
  </div>
  <div class="chart-box"><canvas id="acouChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Equipment sound power <span id="vLw">95 dB</span></label>
      <input type="range" id="sLw" min="75" max="120" value="95" step="1">
      <div class="hint">L&#119; of the machine. A large chiller or fan can exceed 105 dB.</div>
    </div>
    <div class="ctrl">
      <label>Plant room absorption α <span id="vAl">0.08</span></label>
      <input type="range" id="sAl" min="0.02" max="0.5" value="0.08" step="0.01">
      <div class="hint">Bare concrete ≈ 0.03–0.05; acoustically lined ≈ 0.25–0.40.</div>
    </div>
    <div class="ctrl">
      <label>Room surface area <span id="vS">400 m²</span></label>
      <input type="range" id="sS" min="100" max="2000" value="400" step="25">
      <div class="hint">Total internal surface of the plant room.</div>
    </div>
    <div class="ctrl">
      <label>Target next door <span id="vNr">NR 30</span></label>
      <input type="range" id="sNr" min="15" max="45" value="30" step="1">
      <div class="hint">NR 25 residential/hotel bedroom, NR 35 office, NR 40 circulation.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Level at 3 m</div><div class="v" id="rLp">86.2 <small>dB</small></div></div>
    <div class="cell"><div class="k">Reverberant level</div><div class="v" id="rLr">85.6 <small>dB</small></div></div>
    <div class="cell"><div class="k">Required TL</div><div class="v" id="rTl">55 <small>dB</small></div></div>
    <div class="cell"><div class="k">If lined (α 0.35)</div><div class="v" id="rTn">50 <small>dB</small></div></div>
    <div class="cell"><div class="k">Construction</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rCv"></span></div></div>
  </div>
</div>
<p class="fig-note">A 95&nbsp;dB machine in a lightly absorbent plant room produces about <strong>86&nbsp;dB</strong>, and separating that from an NR&nbsp;30 space needs roughly <strong>55&nbsp;dB</strong> of transmission loss — beyond a single blockwork wall and firmly into double-leaf or heavy composite territory. Line the plant room to α&nbsp;=&nbsp;0.35 and the requirement drops by about 6&nbsp;dB, which is often the difference between a buildable partition and an impossible one. <strong>Absorption inside the plant room is almost always cheaper than transmission loss in the wall</strong>, and it is the first move to make — but note that it does nothing at all for structure-borne transmission, which is the isolator's job.</p>

<h2 id="int-speed">6 · Interactive: variable speed as a noise control measure</h2>
<p>Slowing a fan or pump reduces its sound power steeply — roughly 50·log₁₀ of the speed ratio for a fan. This is the most under-used acoustic tool in a building, because it costs nothing once the drive is there.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Sound power and shaft power vs speed</div>
    <div class="fsub">ΔL&#119; ≈ 50·log&#8321;&#8320;(N/N&#8320;) for a fan (55 for some pump types); shaft power follows the cube law. Both fall together, which is why part-speed operation is quiet as well as cheap.</div>
  </div>
  <div class="chart-box"><canvas id="spdChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Sound power at full speed <span id="vL0">92 dB</span></label>
      <input type="range" id="sL0" min="70" max="120" value="92" step="1">
      <div class="hint">Manufacturer&rsquo;s L&#119; at design duty.</div>
    </div>
    <div class="ctrl">
      <label>Operating speed <span id="vSp">70 %</span></label>
      <input type="range" id="sSp" min="25" max="100" value="70" step="1">
      <div class="hint">Typical part-load operating point.</div>
    </div>
    <div class="ctrl">
      <label>Speed exponent <span id="vEx">50</span></label>
      <input type="range" id="sEx" min="40" max="60" value="50" step="1">
      <div class="hint">50 for most fans, 55 for some centrifugal pumps.</div>
    </div>
    <div class="ctrl">
      <label>Full-speed shaft power <span id="vP0">75 kW</span></label>
      <input type="range" id="sP0" min="5" max="400" value="75" step="5">
      <div class="hint">To show the energy saving alongside.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Sound power now</div><div class="v" id="rLn2">84.3 <small>dB</small></div></div>
    <div class="cell"><div class="k">Reduction</div><div class="v" id="rDl">7.7 <small>dB</small></div></div>
    <div class="cell"><div class="k">Shaft power</div><div class="v" id="rPw">26 <small>kW</small></div></div>
    <div class="cell"><div class="k">Power saved</div><div class="v" id="rPs">66 <small>%</small></div></div>
    <div class="cell"><div class="k">Perceived</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rPc"></span></div></div>
  </div>
</div>
<p class="fig-note">Running a fan at <strong>70&nbsp;% speed drops its sound power by 7.7&nbsp;dB</strong> — close to halving the perceived loudness — while cutting shaft power by 66&nbsp;%. That is a free acoustic result, and it argues strongly for selecting fans and pumps that will spend their lives at part speed rather than selecting tight to the duty and running them flat out. It also argues for oversizing the <em>duct</em> rather than the fan: lower velocity means less regenerated noise at every bend, damper and terminal, and regenerated noise is the one source a silencer cannot fix because it is created downstream of it.</p>

<h2 id="install">7 · Installation &amp; execution tricks</h2>
<ul class="clean">
  <li><strong>Specify by static deflection, checked at minimum speed</strong>, and require the supplier to submit the selected deflection under the actual operating weight — not the catalogue rating.</li>
  <li><strong>Inspect isolators under load, after commissioning.</strong> Measure the actual deflection of every spring; a mount that has not compressed is either wrongly selected or bottomed out, and both are common. This is a five-minute check that catches most failures.</li>
  <li><strong>Check the base is free.</strong> Walk every inertia base looking for grout bridges, packers left in, debris under the frame and snubbers touching. Photograph it before the plant room is closed.</li>
  <li><strong>Isolate the first five hangers</strong> on every pipe and duct leaving isolated plant, with the deflection reducing progressively rather than dropping to rigid at hanger two.</li>
  <li><strong>Pack and seal every penetration resiliently</strong> — and make sure the fire-stopping detail chosen is also an acoustic detail, because a rigid mortar fire-stop is a perfect sound bridge.</li>
  <li><strong>Line plant rooms before you thicken walls.</strong> Absorption is cheap, thin and effective on airborne level; use it first and size the partition on what remains.</li>
  <li><strong>Commission acoustically, and to a written criterion.</strong> Measure NR in the sensitive spaces with plant running at design and at minimum speed, at night, and record it. Without a baseline measurement every future complaint is unanswerable.</li>
  <li><strong>Watch out for tonal noise.</strong> Blade-pass and pump vane-pass frequencies are perceived far more strongly than broadband level suggests; if a tone is audible, a 3&nbsp;dB overall reduction will not fix it — the fix is speed, blade count or a tuned attenuator.</li>
</ul>

<h2 id="checklist">8 · The design &amp; installation checklist</h2>
<ul class="clean">
  <li><strong>Set acoustic criteria per space</strong> (NR/NC) at concept, and make them contractual.</li>
  <li><strong>Select isolators on static deflection</strong>, with f/f&#8345; ≥ 3 at the <em>minimum</em> operating speed.</li>
  <li><strong>Use inertia bases</strong> for pumps and close-coupled machines, sized at 1.5–2× machine mass.</li>
  <li><strong>Design every flanking path</strong> — pipes, ducts, conduit, trays, drainage, snubbers.</li>
  <li><strong>Line plant rooms</strong> and size partitions on the resulting level, with the slab and the door treated as part of the envelope.</li>
  <li><strong>Exploit part-speed operation</strong> as a design assumption, not a happy accident.</li>
  <li><strong>Keep duct and pipe velocities down</strong> near sensitive spaces to control regenerated noise.</li>
  <li><strong>Inspect deflections under load</strong> and photograph every base before closing out.</li>
  <li><strong>Measure and record NR at handover</strong>, at design and minimum speed.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  Vibration isolation is governed by one ratio — the disturbing frequency over the mount's natural frequency — and below <strong>√2</strong> the isolator amplifies rather than isolates. Specify <strong>static deflection</strong>, never isolator type, and check it at the <em>slowest</em> speed a variable-speed machine will hold, because that is where a mount selected at nameplate speed sits on the resonant peak. Then remember that the isolators are usually not the failure: the failure is a rigidly clamped riser, a grout bridge under an inertia base, or a mortar fire-stop acting as a sound bridge — so design every flanking path, line the plant room before thickening the wall, and inspect the deflections under load before the ceiling goes up.
</div>

<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>ASHRAE <em>Handbook — HVAC Applications</em>, Noise and Vibration Control chapter — transmissibility, isolator selection tables, plant room treatment and flanking paths.</li>
  <li>CIBSE <em>Guide B4 — Noise and Vibration Control for Building Services Systems</em>; and CIBSE <em>Guide A</em> for indoor design criteria.</li>
  <li>Institute of Acoustics / ANC guidance on building services noise, and BS 8233 <em>Guidance on sound insulation and noise reduction for buildings</em>.</li>
  <li>ISO 1996 and ISO 3382 series — measurement of environmental and room acoustic parameters; ISO 717 for airborne sound insulation rating.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — plant location and acoustic separation on mechanical floors.</li>
  <li>AMCA 300 / ISO 3744 — fan sound power determination; and Eurovent guidance on equipment sound data.</li>
  <li>SMACNA <em>Seismic Restraint Manual</em> — restraint and snubber arrangements compatible with vibration isolation.</li>
  <li>Beranek, L.L. &amp; Vér, I.L. <em>Noise and Vibration Control Engineering</em> — theory of isolation, structure-borne transmission and room acoustics.</li>
</ol>

<div class="tags">#VibrationIsolation #NoiseControl #Acoustics #TallBuildings #MegatallBuildings #MechanicalFloors #Transmissibility #StaticDeflection #NaturalFrequency #Resonance #InertiaBase #SpringIsolator #FlankingPath #StructureBorne #AirborneNoise #NRRating #NCRating #TransmissionLoss #PlantRoom #Silencer #RegeneratedNoise #BladePassFrequency #VFD #Commissioning #ASHRAE #CIBSE #MEP #BuildingServices</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};

/* ---------- CHART 1 : transmissibility ---------- */
const sR=document.getElementById('sR'),sD=document.getElementById('sD'),
      sZ=document.getElementById('sZ'),sT=document.getElementById('sT');
const fnat=d=>15.76/Math.sqrt(Math.max(d,0.1));
function trans(f,d,z){
  const r=f/fnat(d);
  return Math.sqrt(1+Math.pow(2*z*r,2))/Math.sqrt(Math.pow(1-r*r,2)+Math.pow(2*z*r,2));
}
let vibChart=new Chart(document.getElementById('vibChart'),{
  data:{datasets:[
    {type:'line',label:'Transmissibility at design speed',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:3},
    {type:'line',label:'At minimum (turndown) speed',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,order:2},
    {type:'scatter',label:'Your isolator',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:2,max:100,title:{display:true,text:'Isolator static deflection (mm)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'logarithmic',title:{display:true,text:'Transmissibility  (lower is better)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`T = ${c.parsed.y.toFixed(4)} at ${fmt0(c.parsed.x)} mm`}},
      annotation:{annotations:{
        amp:{type:'box',xScaleID:'x',yScaleID:'y',xMin:2,xMax:2,backgroundColor:'rgba(192,57,43,0.09)',borderWidth:0,label:{display:true,content:'amplifies',position:{x:'center',y:'start'},rotation:270,font:{size:10,family:'DM Sans'},color:'#c0392b'}},
        one:{type:'line',scaleID:'y',yScaleID:'y',value:1,borderColor:'#b9770e',borderWidth:1.6,borderDash:[5,4],label:{display:true,content:'T = 1 — no isolation',position:'start',font:{size:10,family:'DM Sans'},color:'#b9770e',backgroundColor:'rgba(255,255,255,0.85)'}}
      }}}}
});
function updVib(){
  const rpm=+sR.value,d=+sD.value,z=+sZ.value,td=+sT.value/100;
  document.getElementById('vR').textContent=rpm+' rpm';
  document.getElementById('vD').textContent=d+' mm';
  document.getElementById('vZ').textContent=fmt2(z);
  document.getElementById('vT').textContent=fmt0(td*100)+' %';
  const f=rpm/60, ft=f*td;
  const xs=[];for(let x=2;x<=100;x+=1)xs.push(x);
  vibChart.data.datasets[0].data=xs.map(x=>({x:x,y:+trans(f,x,z).toFixed(5)}));
  vibChart.data.datasets[1].data=xs.map(x=>({x:x,y:+trans(ft,x,z).toFixed(5)}));
  const T=trans(f,d,z), Tt=trans(ft,d,z);
  vibChart.data.datasets[2].data=[{x:d,y:+T.toFixed(5)}];
  const dCrit=ft>0?Math.pow(15.76*Math.SQRT2/ft,2):0;
  vibChart.options.plugins.annotation.annotations.amp.xMax=Math.max(2,Math.min(100,dCrit));
  vibChart.update('none');
  const ratio=f/fnat(d);
  document.getElementById('rFn').innerHTML=fmt2(fnat(d))+' <small>Hz</small>';
  document.getElementById('rRt').textContent=fmt2(ratio);
  document.getElementById('rEf').innerHTML=fmt1(100*(1-T))+' <small>%</small>';
  document.getElementById('rTd').innerHTML=fmt1(100*(1-Tt))+' <small>%</small>';
  const v=document.getElementById('rVd');
  if(ft/fnat(d)<1.414) v.innerHTML='<span class="badge bad">amplifies at turndown</span>';
  else if(ratio<3)     v.innerHTML='<span class="badge warn">too little deflection</span>';
  else if(ratio<5)     v.innerHTML='<span class="badge good">acceptable</span>';
  else                 v.innerHTML='<span class="badge good">good isolation</span>';
}
[sR,sD,sZ,sT].forEach(s=>s.addEventListener('input',updVib));updVib();

/* ---------- CHART 2 : room acoustics ---------- */
const sLw=document.getElementById('sLw'),sAl=document.getElementById('sAl'),
      sS=document.getElementById('sS'),sNr=document.getElementById('sNr');
function lp(Lw,r,S,a,Q){Q=Q||2;const R=S*a/(1-a);return Lw+10*Math.log10(Q/(4*Math.PI*r*r)+4/R);}
let acouChart=new Chart(document.getElementById('acouChart'),{
  data:{datasets:[
    {type:'line',label:'Sound pressure in the plant room',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,order:3},
    {type:'line',label:'Required partition transmission loss',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,order:2},
    {type:'scatter',label:'Your plant room',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:0.02,max:0.5,title:{display:true,text:'Plant room absorption coefficient α',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,title:{display:true,text:'Level / transmission loss (dB)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>`${fmt1(c.parsed.y)} dB at α = ${fmt2(c.parsed.x)}`}}}}
});
function updAcou(){
  const Lw=+sLw.value,a=+sAl.value,S=+sS.value,nr=+sNr.value;
  document.getElementById('vLw').textContent=Lw+' dB';
  document.getElementById('vAl').textContent=fmt2(a);
  document.getElementById('vS').textContent=S+' m²';
  document.getElementById('vNr').textContent='NR '+nr;
  const reqTL=(aa)=>lp(Lw,3,S,aa)-nr+10*Math.log10(20/25.0);
  const xs=[];for(let x=0.02;x<=0.5;x+=0.01)xs.push(+x.toFixed(2));
  acouChart.data.datasets[0].data=xs.map(x=>({x:x,y:+lp(Lw,3,S,x).toFixed(1)}));
  acouChart.data.datasets[1].data=xs.map(x=>({x:x,y:+reqTL(x).toFixed(1)}));
  acouChart.data.datasets[2].data=[{x:a,y:+lp(Lw,3,S,a).toFixed(1)}];
  acouChart.update('none');
  const R=S*a/(1-a);
  document.getElementById('rLp').innerHTML=fmt1(lp(Lw,3,S,a))+' <small>dB</small>';
  document.getElementById('rLr').innerHTML=fmt1(Lw+10*Math.log10(4/R))+' <small>dB</small>';
  document.getElementById('rTl').innerHTML=fmt0(reqTL(a))+' <small>dB</small>';
  document.getElementById('rTn').innerHTML=fmt0(reqTL(0.35))+' <small>dB</small>';
  const v=document.getElementById('rCv'), t=reqTL(a);
  if(t<45)      v.innerHTML='<span class="badge good">single heavy leaf</span>';
  else if(t<58) v.innerHTML='<span class="badge warn">double leaf needed</span>';
  else          v.innerHTML='<span class="badge bad">specialist construction</span>';
}
[sLw,sAl,sS,sNr].forEach(s=>s.addEventListener('input',updAcou));updAcou();

/* ---------- CHART 3 : speed vs sound power ---------- */
const sL0=document.getElementById('sL0'),sSp=document.getElementById('sSp'),
      sEx=document.getElementById('sEx'),sP0=document.getElementById('sP0');
let spdChart=new Chart(document.getElementById('spdChart'),{
  data:{datasets:[
    {type:'line',label:'Sound power (dB)',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,yAxisID:'y',order:3},
    {type:'line',label:'Shaft power (% of full)',data:[],borderColor:'#1b4f72',borderWidth:2.5,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Operating point',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:25,max:100,title:{display:true,text:'Speed (% of full)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',position:'left',title:{display:true,text:'Sound power Lᵥ (dB)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',position:'right',min:0,max:100,title:{display:true,text:'Shaft power (%)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}}}}
});
function updSpd(){
  const L0=+sL0.value,sp=+sSp.value/100,ex=+sEx.value,P0=+sP0.value;
  document.getElementById('vL0').textContent=L0+' dB';
  document.getElementById('vSp').textContent=fmt0(sp*100)+' %';
  document.getElementById('vEx').textContent=ex;
  document.getElementById('vP0').textContent=P0+' kW';
  const xs=[];for(let x=25;x<=100;x+=1)xs.push(x);
  spdChart.data.datasets[0].data=xs.map(x=>({x:x,y:+(L0+ex*Math.log10(x/100)).toFixed(2)}));
  spdChart.data.datasets[1].data=xs.map(x=>({x:x,y:+(100*Math.pow(x/100,3)).toFixed(1)}));
  const Ln=L0+ex*Math.log10(sp);
  spdChart.data.datasets[2].data=[{x:sp*100,y:+Ln.toFixed(2)}];
  spdChart.update('none');
  document.getElementById('rLn2').innerHTML=fmt1(Ln)+' <small>dB</small>';
  document.getElementById('rDl').innerHTML=fmt1(L0-Ln)+' <small>dB</small>';
  document.getElementById('rPw').innerHTML=fmt0(P0*Math.pow(sp,3))+' <small>kW</small>';
  document.getElementById('rPs').innerHTML=fmt0(100*(1-Math.pow(sp,3)))+' <small>%</small>';
  const v=document.getElementById('rPc'), d=L0-Ln;
  if(d<3)       v.innerHTML='<span class="badge warn">barely audible change</span>';
  else if(d<10) v.innerHTML='<span class="badge good">clearly quieter</span>';
  else          v.innerHTML='<span class="badge good">about half as loud</span>';
}
[sL0,sSp,sEx,sP0].forEach(s=>s.addEventListener('input',updSpd));updSpd();

window.addEventListener('load',function(){try{vibChart.resize();acouChart.resize();spdChart.resize();}catch(e){}});
"""

SPEC = dict(
    slug='vibration-noise-control-tall-buildings', cat='tallmep', mins=16,
    date_iso='2026-08-14', date_human='August 2026', date_ar='أغسطس 2026',
    title='Vibration &amp; Noise Control for MEP in Megatall Buildings: Static Deflection, Flanking Paths &amp; Plant-Room Acoustics',
    reg_title='Vibration & Noise Control for MEP in Megatall Buildings: Static Deflection, Flanking Paths & Plant-Room Acoustics',
    reg_tag='Tall-Building Systems · Vibration · Acoustics',
    breadcrumb='Tall-Building Systems',
    tag_line='Tall-Building Systems &middot; Vibration Isolation &middot; Acoustics &middot; Mechanical Floors',
    desc='Vibration and noise control for MEP plant in megatall buildings: the transmissibility equation and why an isolator below a frequency ratio of root two amplifies instead of isolating, specifying static deflection rather than isolator type and checking it at minimum VFD speed, flanking paths through pipes ducts and fire-stopping, plant-room absorption versus partition transmission loss, and variable speed as a free acoustic measure — with three interactive charts and installation tricks.',
    og_desc='Below a frequency ratio of root two an isolator amplifies rather than isolates — and a machine correctly isolated at 1,450 rpm can sit on the resonant peak at 30 percent VFD speed. Specify static deflection, not isolator type.',
    ld_desc='A design-perspective guide to vibration and noise control for building services in megatall buildings: transmissibility and static deflection, resonance and variable-speed operation, inertia bases, flanking paths, plant-room absorption and required partition transmission loss, and speed as a noise control measure.',
    img_alt='Technical cutaway of a megatall tower mechanical floor showing pumps and air-handling plant on inertia bases and spring isolators, with resiliently supported pipework and ductwork leaving the plant room above an occupied floor',
    en_tag='Tall-Building Systems &middot; Vibration &middot; Acoustics &middot; Mechanical Floors',
    en_title='Vibration &amp; Noise Control for MEP in Megatall Buildings: Static Deflection, Flanking Paths &amp; Plant-Room Acoustics',
    en_excerpt='Every mechanical floor sits directly above somebody&rsquo;s bedroom. Vibration isolation is governed by one ratio, and below &radic;2 an isolator <em>amplifies</em> rather than isolates &mdash; so a 6&nbsp;mm pad under a 600&nbsp;rpm machine gives 29&nbsp;% isolation and under anything slower makes it worse. Why you specify static deflection and never isolator type, why the check must be at minimum VFD speed, the flanking paths that leak past perfect isolators, plant-room absorption versus partition transmission loss, and variable speed as a free 8&nbsp;dB &mdash; with three interactive charts.',
    en_search='vibration isolation noise control acoustics building services MEP tall buildings megatall mechanical floors transmissibility static deflection natural frequency frequency ratio resonance amplification spring isolator neoprene pad inertia base housekeeping pad snubber seismic restraint flanking path flexible connector resilient hanger pipe riser clamping grout bridge fire stop sound bridge plant room absorption reverberant field room constant sound power sound pressure transmission loss partition double leaf NR rating NC rating regenerated noise duct velocity silencer insertion loss blade pass frequency tonal noise VFD variable speed 50 log law commissioning ASHRAE CIBSE Guide B4 BS 8233 SMACNA seismic building services',
    ar_title='التحكم في الاهتزاز والضوضاء لأنظمة الميكانيكا في المباني فائقة الارتفاع: الانحراف الاستاتيكي والمسارات الجانبية',
    ar_excerpt='كل طابق ميكانيكي يقع مباشرةً فوق غرفة نوم أحدهم. عزل الاهتزاز تحكمه نسبة واحدة، وتحت الجذر التربيعي للاثنين يقوم العازل <em>بالتضخيم</em> بدل العزل — فحشوة ٦ مم تحت ماكينة بسرعة ٦٠٠ لفة تعطي عزلًا بنسبة ٢٩٪ فقط، وتحت أي سرعة أبطأ تزيد المشكلة سوءًا. لماذا تُحدَّد المواصفة بالانحراف الاستاتيكي لا بنوع العازل، ولماذا يجب الفحص عند أدنى سرعة للمشغل، والمسارات الجانبية التي تتسرّب رغم العوازل المثالية، والامتصاص داخل غرفة المعدات مقابل عزل الجدار، والسرعة المتغيرة كمكسب مجاني بمقدار ٨ ديسيبل — مع ثلاثة رسوم تفاعلية.',
    ar_search='vibration isolation noise control acoustics MEP tall buildings transmissibility static deflection natural frequency resonance spring isolator inertia base flanking path resilient hanger plant room absorption transmission loss NR rating VFD CIBSE B4 عزل الاهتزاز التحكم في الضوضاء الصوتيات خدمات المباني المباني الشاهقة المباني فائقة الارتفاع الطوابق الميكانيكية قابلية النقل الانحراف الاستاتيكي التردد الطبيعي نسبة التردد الرنين التضخيم عازل زنبركي حشوة نيوبرين قاعدة القصور الذاتي قاعدة خرسانية مصد الاهتزاز التقييد الزلزالي المسار الجانبي الوصلة المرنة المعلاق المرن تثبيت المواسير جسر الجراوت مانع الحريق جسر صوتي امتصاص غرفة المعدات المجال المنعكس ثابت الغرفة قدرة الصوت ضغط الصوت عزل النفاذ الجدار المزدوج تصنيف الضوضاء الضوضاء المتولدة سرعة الهواء كاتم الصوت تردد مرور الريش الضوضاء النغمية المشغل متغير السرعة التشغيل والاختبار MEP خدمات المباني',
    body=BODY, charts=CHARTS,
)
