# -*- coding: utf-8 -*-
BODY = r"""
<p class="lead">A litre of water arriving at a tap on the hundred-and-fiftieth floor of a Gulf tower has been made from seawater, pumped inland, and lifted six hundred metres. By the time it reaches the fixture it carries about <strong>six kilowatt-hours per cubic metre</strong> on the coast and <strong>ten inland</strong> &mdash; and the tower will evaporate several times that volume off its cooling towers without anyone recording the energy that went into making it. This is the accounting nobody does, because the desalination engineer stops at the plant fence and the building engineer starts at the site boundary.</p>

<h2 id="chain">1 &middot; The chain nobody adds up</h2>
<p>Every stage of this journey is well understood in isolation, and each has its own literature, its own specialists and its own conferences. What is missing is the sum.</p>
<ul class="clean">
  <li><strong>Desalination.</strong> A modern SWRO plant with pressure-exchanger energy recovery delivers permeate at roughly <a href="px-energy-recovery.html">3.5&nbsp;kWh/m&sup3;</a>. The same plant built in the 1990s, without recovery, took about ten.</li>
  <li><strong>Transmission.</strong> On the coast this is almost free. Inland it is the largest single term in the whole chain, and it is invisible to everyone downstream of it.</li>
  <li><strong>The building.</strong> Lifting to the top of a 600&nbsp;m tower costs about <a href="domestic-water-tall-buildings.html">2.45&nbsp;kWh/m&sup3;</a> at the pump shaft &mdash; pure physics, and the one term the MEP engineer actually controls.</li>
  <li><strong>And then it is evaporated.</strong> A 50&nbsp;MW heat-rejection plant drinks <a href="cooling-towers-heat-rejection-tall-buildings.html">2,400&nbsp;m&sup3; a day</a> in makeup. That water carries the whole chain's energy with it, into the sky, as latent heat.</li>
</ul>
<p>The reason this matters is not moral. It is that the four terms respond to completely different design decisions, they are not the same size in every city, and <strong>the cheapest term to fix is almost never the one being optimised</strong>.</p>

<h2 id="desal">2 &middot; What a cubic metre costs to make</h2>
<p>Reverse osmosis has to raise the feed above the osmotic pressure of seawater and hold it there. The ideal work is set by that pressure and the recovery ratio, and the real work is that divided by pump efficiency [1]:</p>
<div class="eq">\[ E_{RO} \;=\; \frac{P}{36\,R\,\eta}\Big(1 - \varepsilon_{ERD}\,(1-R)\Big) \;+\; E_{aux} \qquad \text{kWh/m}^3 \]</div>
<p>with \(P\) the feed pressure in bar, \(R\) the recovery fraction, \(\eta\) the high-pressure pump efficiency and \(\varepsilon_{ERD}\) the effectiveness of the energy recovery device. The bracket is the whole story of the last thirty years: the brine leaves the membrane at almost full pressure, carrying \((1-R)\) of the feed with it, and a pressure exchanger hands that energy straight back to the incoming stream at around 96&nbsp;% efficiency.</p>
<div class="callout key">
  <span class="lbl">Why the recovery ratio cuts both ways</span>
  Raising recovery reduces the volume of brine you have to pressurise, which looks like an energy saving &mdash; and it is, if there is no energy recovery device. With a pressure exchanger fitted, that brine energy was coming back anyway, so the saving largely evaporates while the fouling, scaling and osmotic pressure penalties of running at high recovery remain. This is the <a href="ro-overdesign-paradox.html">over-design paradox</a> in another guise: the lever that worked before you fitted the device stops working after you fit it.
</div>

<h2 id="int-chain">3 &middot; Interactive: the specific energy of a litre, stage by stage</h2>
<p>Set the plant, the transmission route and the tower. The bars are the four stages of the journey; the marker is the total the fixture actually receives. Then move the site from the coast to the interior and watch which term dominates.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Delivered specific energy, from seawater to the top-floor tap</div>
    <div class="fsub">RO from the equation above. Transmission and building lift both from E = h/(367&middot;&eta;), the same relation used throughout the site for pumping energy. Transmission head is static lift plus friction over the route; the building term is tower height plus a 30 m friction and residual allowance.</div>
  </div>
  <div class="chart-box"><canvas id="chainChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Feed pressure <span id="vP">60 bar</span></label>
      <input type="range" id="sP" min="45" max="80" value="60" step="1">
      <div class="hint">Membrane feed pressure. Rises with salinity, temperature and membrane age.</div>
    </div>
    <div class="ctrl">
      <label>Recovery ratio <span id="vR">45 %</span></label>
      <input type="range" id="sR" min="30" max="55" value="45" step="1">
      <div class="hint">Permeate as a share of feed. Gulf seawater rarely justifies more than about 45 %.</div>
    </div>
    <div class="ctrl">
      <label>Energy recovery device <span id="vE">96 %</span></label>
      <input type="range" id="sE" min="0" max="97" value="96" step="1">
      <div class="hint">Pressure exchanger effectiveness. Drag to zero for a plant built before they existed.</div>
    </div>
    <div class="ctrl">
      <label>Transmission head <span id="vT">55 m</span></label>
      <input type="range" id="sT" min="20" max="1400" value="55" step="5">
      <div class="hint">Static lift plus friction from the plant to the site. Coastal ≈ 55 m; Riyadh from the Gulf coast ≈ 1,200 m.</div>
    </div>
    <div class="ctrl">
      <label>Tower height <span id="vH">600 m</span></label>
      <input type="range" id="sH" min="50" max="1000" value="600" step="10">
      <div class="hint">Height the domestic riser has to serve.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Desalination</div><div class="v" id="rD">3.5 <small>kWh/m&sup3;</small></div></div>
    <div class="cell"><div class="k">Transmission</div><div class="v" id="rT">0.19 <small>kWh/m&sup3;</small></div></div>
    <div class="cell"><div class="k">Lift in the tower</div><div class="v" id="rL">2.45 <small>kWh/m&sup3;</small></div></div>
    <div class="cell"><div class="k">At the tap</div><div class="v" id="rTot">6.1 <small>kWh/m&sup3;</small></div></div>
    <div class="cell"><div class="k">Largest term</div><div class="v" style="font-size:15px;margin-top:6px;"><span id="rDom"></span></div></div>
  </div>
</div>
<p class="fig-note">At the default &mdash; a modern coastal plant, a short transmission route and a 600&nbsp;m tower &mdash; the tap receives water at about <strong>6.1&nbsp;kWh/m&sup3;</strong>, of which the building itself is responsible for 2.45. Now drag the transmission head to 1,200&nbsp;m, which is roughly what it takes to move water from the Gulf coast to the Riyadh plateau: the total becomes <strong>10.1&nbsp;kWh/m&sup3;</strong> and transmission, not desalination, becomes the largest single term in the chain. Two conclusions follow immediately. In a coastal tower the building's own lift is the biggest thing the design team controls, and it is worth the <a href="domestic-water-tall-buildings.html">zone-boosting argument</a> that halves it. In an inland tower the building's lift is a detail, and every litre not used is worth far more than the pump energy suggests &mdash; which changes the economics of reuse completely.</p>

<h2 id="evap">4 &middot; The part that is evaporated</h2>
<p>The domestic water in a tower is the small stream. The large one is condenser water, and it does not leave through a drain &mdash; it leaves as vapour. The physics is fixed: rejecting a megawatt of heat by evaporation takes about 1.5&nbsp;m&sup3; of water an hour, because that is what the latent heat of vaporisation demands. Blowdown adds to it, at a rate set by how many times you are prepared to concentrate the dissolved solids before dumping them:</p>
<div class="eq">\[ \dot{V}_{makeup} \;=\; \dot{V}_{evap}\left(1 + \frac{1}{C-1}\right), \qquad \dot{V}_{evap} \approx 1.5\,\dot{Q}_{rej}\ \ \text{m}^3\text{/h per MW} \]</div>
<p>At four cycles of concentration a 50&nbsp;MW plant needs 100&nbsp;m&sup3;/h, or 2,400&nbsp;m&sup3; a day. In the Gulf that water is desalinated, because there is no other kind. <strong>The tower is therefore boiling desalinated seawater to keep itself cool</strong>, and the energy that made that water does not appear in any building energy model, any LEED calculation or any chiller efficiency comparison.</p>

<h2 id="int-ledger">5 &middot; Interactive: the evaporation ledger</h2>
<p>This puts the two energies side by side: the electricity the chiller plant consumes, and the embodied energy of the water its cooling towers evaporate. They are not the same order of magnitude &mdash; but the second is not a rounding error either, and it is the one nobody counts.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">Chiller electricity vs the embodied energy of evaporated water</div>
    <div class="fsub">Makeup from the equation above. Embodied energy is makeup volume &times; the delivered specific energy from the previous chart. Chiller electricity from the rejected heat, taken as 1.25 &times; the cooling load, divided by the plant COP.</div>
  </div>
  <div class="chart-box"><canvas id="ledgerChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Heat rejected <span id="vMW">50 MW</span></label>
      <input type="range" id="sMW" min="5" max="200" value="50" step="5">
      <div class="hint">Total rejection at the towers, including chiller work.</div>
    </div>
    <div class="ctrl">
      <label>Cycles of concentration <span id="vC">4.0</span></label>
      <input type="range" id="sC" min="1.5" max="10" value="4" step="0.1">
      <div class="hint">Set by makeup water chemistry and the treatment programme.</div>
    </div>
    <div class="ctrl">
      <label>Delivered water energy <span id="vSec">6.1 kWh/m&sup3;</span></label>
      <input type="range" id="sSec" min="1" max="12" value="6.1" step="0.1">
      <div class="hint">From the first chart. Coastal ≈ 6; Riyadh ≈ 10; a gravity-fed mountain city ≈ 0.5.</div>
    </div>
    <div class="ctrl">
      <label>Plant COP <span id="vCOP">5.5</span></label>
      <input type="range" id="sCOP" min="3" max="8" value="5.5" step="0.1">
      <div class="hint">Chillers plus auxiliaries. A colder wet bulb buys a better number.</div>
    </div>
    <div class="ctrl">
      <label>Equivalent full-load hours <span id="vHrs">4000 h</span></label>
      <input type="range" id="sHrs" min="1000" max="8000" value="4000" step="100">
      <div class="hint">Annual operating hours at full rejection.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Makeup</div><div class="v" id="rMu">2,400 <small>m&sup3;/d</small></div></div>
    <div class="cell"><div class="k">Annual water</div><div class="v" id="rAnn">400,000 <small>m&sup3;</small></div></div>
    <div class="cell"><div class="k">Embodied in that water</div><div class="v" id="rEmb">2.45 <small>GWh</small></div></div>
    <div class="cell"><div class="k">Chiller electricity</div><div class="v" id="rChill">29.1 <small>GWh</small></div></div>
    <div class="cell"><div class="k">Water as % of plant</div><div class="v" id="rPct">8.4 <small>%</small></div></div>
  </div>
</div>
<p class="fig-note">On the coast the water a 50&nbsp;MW plant evaporates carries embodied energy equal to about <strong>8&nbsp;% of what the chillers themselves consume</strong>. Move the same building to Riyadh and two things happen at once, in opposite directions: the water becomes more expensive to deliver, pushing the embodied term to roughly <strong>14&nbsp;%</strong>, while the drier air and lower wet bulb make the chillers <em>more</em> efficient, which raises the ratio further still. <strong>The inland tower has the cheaper cooling plant and the dearer water</strong>, and a design optimisation that sees only the electricity meter will get that trade exactly backwards. This is also the honest answer to a question people expect to be alarming: the embodied water energy is not larger than the chiller load, and anyone claiming otherwise is selling something. It is roughly a tenth of it &mdash; consistently, invisibly, and for the life of the building.</p>

<h2 id="levers">6 &middot; Which levers actually move</h2>
<p>Once the ledger is written down, the design responses sort themselves by size rather than by fashion.</p>
<ul class="clean">
  <li><strong>Cycles of concentration are free energy.</strong> Going from three cycles to six removes a quarter of the makeup volume for the cost of a better treatment programme and closer monitoring. No plant, no space, no capital. It is the highest-return water measure in the building and it is usually left to whoever holds the chemicals contract.</li>
  <li><strong>Condensate is the highest-quality water in the building and it goes down the drain.</strong> A dedicated outdoor-air unit handling 10&nbsp;m&sup3;/s in Gulf summer conditions strips about <strong>15&nbsp;m&sup3; a day</strong> of distilled-grade water out of the air &mdash; produced at the point of use, on a high floor, with no chloride and no hardness. It is nearly ideal cooling-tower makeup and it needs no treatment beyond biocide.</li>
  <li><strong>Greywater is a volume play, not a quality play.</strong> As the <a href="greywater-reuse-tall-buildings.html">reuse arithmetic</a> shows, a 2,000-person tower's greywater covers only about a tenth of a 50&nbsp;MW plant's makeup &mdash; but it is the single largest recoverable stream, and in an inland city each cubic metre it displaces is worth ten kilowatt-hours rather than six.</li>
  <li><strong>Dry and hybrid coolers trade water for energy, explicitly.</strong> They raise condensing temperature and chiller power in exchange for eliminating evaporation. With the embodied energy of water written down, that trade can finally be evaluated on one axis instead of two &mdash; and in an inland Gulf city it is much closer than the usual analysis suggests.</li>
  <li><strong>Zone-boosting the domestic riser</strong> halves the building's own term, which matters most in exactly the place the other levers matter least: a coastal tower, where lift is the largest thing you control.</li>
</ul>

<h2 id="int-recovery">7 &middot; Interactive: the recovery stack</h2>
<p>Start with the makeup a plant needs and take it apart. Each measure removes a slice; what is left is the potable or treated-effluent water you actually have to buy, and the energy that came with it.</p>

<div class="fig">
  <div class="fig-head">
    <div class="ftitle">What each measure removes from the makeup bill</div>
    <div class="fsub">Cycles from the makeup equation. Condensate from the psychrometrics of the outdoor-air load, at the stated air volume and coil condition. Greywater as a share of the remaining demand. Energy is the residual volume at the delivered specific energy.</div>
  </div>
  <div class="chart-box"><canvas id="recChart"></canvas></div>
  <div class="controls">
    <div class="ctrl">
      <label>Cycles: base &rarr; improved <span id="vCy">4 &rarr; 6</span></label>
      <input type="range" id="sCy" min="4" max="10" value="6" step="0.5">
      <div class="hint">What the treatment programme can hold. The base case is four.</div>
    </div>
    <div class="ctrl">
      <label>Outdoor air handled <span id="vOA">22 m&sup3;/s</span></label>
      <input type="range" id="sOA" min="0" max="60" value="22" step="1">
      <div class="hint">Total fresh air across the tower. Sets how much condensate exists to collect.</div>
    </div>
    <div class="ctrl">
      <label>Condensate actually captured <span id="vCap">60 %</span></label>
      <input type="range" id="sCap" min="0" max="100" value="60" step="5">
      <div class="hint">Realistic capture. Floor-level units are hard to collect from; central plant is easy.</div>
    </div>
    <div class="ctrl">
      <label>Greywater available <span id="vGw">240 m&sup3;/d</span></label>
      <input type="range" id="sGw" min="0" max="800" value="240" step="10">
      <div class="hint">Treated greywater available for non-potable use.</div>
    </div>
  </div>
  <div class="readout">
    <div class="cell"><div class="k">Base makeup</div><div class="v" id="rBase">2,400 <small>m&sup3;/d</small></div></div>
    <div class="cell"><div class="k">Saved by cycles</div><div class="v" id="rCyc">240 <small>m&sup3;/d</small></div></div>
    <div class="cell"><div class="k">Condensate</div><div class="v" id="rCond">20 <small>m&sup3;/d</small></div></div>
    <div class="cell"><div class="k">Still to buy</div><div class="v" id="rBuy">1,900 <small>m&sup3;/d</small></div></div>
    <div class="cell"><div class="k">Energy avoided</div><div class="v" id="rSaved">1.1 <small>GWh/yr</small></div></div>
  </div>
</div>
<p class="fig-note">The stack is honest about proportions, and the proportions are the point. At the default, <strong>raising the cycles of concentration removes as much water as the entire greywater plant does</strong> &mdash; and it costs almost nothing in capital. Condensate is small in volume but disproportionately valuable: it is the only stream in the building that arrives cleaner than the mains supply, and capturing it well removes a treatment cost as well as a water cost. Greywater is the biggest recoverable volume and the biggest capital commitment. What remains after all three is still the majority of the bill &mdash; which is the realistic conclusion. Reuse does not make a Gulf tower water-neutral. It makes it about a fifth better, for a cost that is justified by the delivered energy behind every cubic metre rather than by the water tariff alone.</p>

<h2 id="design">8 &middot; What this changes on the drawing</h2>
<ul class="clean">
  <li><strong>Put the delivered specific energy in the design basis</strong>, not the water tariff. In a subsidised market the tariff tells you nothing about the resource, and every reuse business case built on it collapses the moment the subsidy is revised. The energy figure is physical and survives.</li>
  <li><strong>Design the condensate drainage as a collection system</strong>, not a disposal system. That is a decision about gradients, materials and a tank &mdash; taken at concept stage, worth nothing if retro-fitted, and impossible once the risers are set. It also removes the most common cause of ceiling damage in a finished tower.</li>
  <li><strong>Specify cycles of concentration as a performance requirement</strong> with a monitoring obligation, rather than leaving it as an operational habit. Write the target, the conductivity set-point and the blowdown control method into the specification.</li>
  <li><strong>Evaluate hybrid coolers on total energy</strong>, including the embodied energy of the water they save. Inland, that calculation is closer than the received wisdom.</li>
  <li><strong>Tell the client the number.</strong> A megatall in an inland Gulf city consumes, through its cooling towers alone, the desalination output of a small town. That is a fact worth putting on one slide at concept stage, because it is the only moment when the architecture can still respond to it.</li>
</ul>

<div class="callout key">
  <span class="lbl">The one-line summary</span>
  A litre reaching the top floor of a coastal Gulf tower carries about <strong>six kilowatt-hours per cubic metre</strong>; inland it carries ten, and transmission &mdash; not desalination &mdash; is the largest term. The building then evaporates several times its own drinking water off the cooling towers, carrying embodied energy equal to roughly <strong>a tenth of what the chillers consume</strong>, on nobody's energy model. The levers, in order of return, are cycles of concentration, condensate capture, greywater, and finally the pumping energy the MEP engineer usually spends all the effort on &mdash; and the order changes between the coast and the interior, which is precisely why the number belongs in the design basis rather than in a sustainability appendix.
</div>
"""

CHARTS = r"""
const fmt0=v=>Math.round(v).toLocaleString('en-US');
const fmt1=v=>v.toFixed(1);
const fmt2=v=>v.toFixed(2);
const fmt3=v=>v.toFixed(3);
const AX={grid:{color:'#eef2f5'},ticks:{font:{family:'DM Sans',size:11}}};
const LBL={size:10,family:'DM Sans'};

/* ---------- CHART 1 : the energy chain ---------- */
const sP=document.getElementById('sP'),sR=document.getElementById('sR'),
      sE=document.getElementById('sE'),sT=document.getElementById('sT'),sH=document.getElementById('sH');
const AUX=1.30, ETA_RO=0.80, ETA_TX=0.78, ETA_BLD=0.70, FRIC_BLD=30;
const lift=(h,e)=>h/(367*e);
const ro=(P,R,erd)=>P/(36*R*ETA_RO)*(1-erd*(1-R))+AUX;
let chainChart=new Chart(document.getElementById('chainChart'),{
  type:'bar',
  data:{labels:['Desalination','Transmission','Lift in the tower','Delivered at the tap'],
    datasets:[{label:'kWh/m³',data:[],backgroundColor:[],borderColor:'#fff',borderWidth:1}]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,ticks:{font:{family:'DM Sans',size:11}}},
            y:{type:'linear',min:0,title:{display:true,text:'Specific energy (kWh/m³)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{display:false},
      tooltip:{callbacks:{label:c=>`${fmt2(c.parsed.y)} kWh/m³`}}}}
});
function updChain(){
  const P=+sP.value,R=+sR.value/100,erd=+sE.value/100,T=+sT.value,H=+sH.value;
  document.getElementById('vP').textContent=P+' bar';
  document.getElementById('vR').textContent=fmt0(R*100)+' %';
  document.getElementById('vE').textContent=fmt0(erd*100)+' %';
  document.getElementById('vT').textContent=T+' m';
  document.getElementById('vH').textContent=H+' m';
  const d=ro(P,R,erd), t=lift(T,ETA_TX), b=lift(H+FRIC_BLD,ETA_BLD), tot=d+t+b;
  chainChart.data.datasets[0].data=[+d.toFixed(2),+t.toFixed(2),+b.toFixed(2),+tot.toFixed(2)];
  chainChart.data.datasets[0].backgroundColor=['#1b4f72','#b9770e','#1e8449','#c0392b'];
  chainChart.update('none');
  document.getElementById('rD').innerHTML=fmt2(d)+' <small>kWh/m³</small>';
  document.getElementById('rT').innerHTML=fmt2(t)+' <small>kWh/m³</small>';
  document.getElementById('rL').innerHTML=fmt2(b)+' <small>kWh/m³</small>';
  document.getElementById('rTot').innerHTML=fmt1(tot)+' <small>kWh/m³</small>';
  const names=['desalination','transmission','the building'], vals=[d,t,b];
  const i=vals.indexOf(Math.max(...vals));
  const cls=['badge good','badge warn','badge bad'][i];
  document.getElementById('rDom').innerHTML='<span class="'+cls+'">'+names[i]+', '+fmt0(100*vals[i]/tot)+' %</span>';
}
[sP,sR,sE,sT,sH].forEach(s=>s.addEventListener('input',updChain));updChain();

/* ---------- CHART 2 : the evaporation ledger ---------- */
const sMW=document.getElementById('sMW'),sC=document.getElementById('sC'),
      sSec=document.getElementById('sSec'),sCOP=document.getElementById('sCOP'),sHrs=document.getElementById('sHrs');
const EVAP=1.5, REJ_RATIO=1.25;
const makeup=(MW,C)=>{const E=EVAP*MW;return E+E/Math.max(C-1,0.1);};
let ledgerChart=new Chart(document.getElementById('ledgerChart'),{
  data:{datasets:[
    {type:'line',label:'Chiller electricity (GWh/yr)',data:[],borderColor:'#1b4f72',backgroundColor:'rgba(27,79,114,0.10)',borderWidth:3,pointRadius:0,fill:true,yAxisID:'y',order:4},
    {type:'line',label:'Embodied energy of evaporated water (GWh/yr)',data:[],borderColor:'#c0392b',borderWidth:3,pointRadius:0,yAxisID:'y',order:3},
    {type:'line',label:'Water as a share of plant energy (%)',data:[],borderColor:'#b9770e',borderWidth:2.2,borderDash:[6,4],pointRadius:0,yAxisID:'y1',order:2},
    {type:'scatter',label:'Your plant',data:[],backgroundColor:'#b9770e',borderColor:'#fff',borderWidth:2,pointRadius:7,yAxisID:'y',order:1}
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{type:'linear',min:5,max:200,title:{display:true,text:'Heat rejected (MW)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y:{type:'linear',min:0,position:'left',title:{display:true,text:'Annual energy (GWh)',font:{family:'DM Sans',size:12,weight:'600'}},...AX},
            y1:{type:'linear',min:0,position:'right',title:{display:true,text:'Water share of plant energy (%)',font:{family:'DM Sans',size:12,weight:'600'}},grid:{drawOnChartArea:false},ticks:{font:{family:'DM Sans',size:11}}}},
    plugins:{legend:{labels:{font:{family:'DM Sans',size:11.5},usePointStyle:true,boxWidth:8}},
      tooltip:{callbacks:{label:c=>c.dataset.yAxisID==='y1'?`${fmt1(c.parsed.y)} %`:`${fmt2(c.parsed.y)} GWh/yr`}}}}
});
function updLedger(){
  const MW=+sMW.value,C=+sC.value,sec=+sSec.value,cop=+sCOP.value,hrs=+sHrs.value;
  document.getElementById('vMW').textContent=MW+' MW';
  document.getElementById('vC').textContent=fmt1(C);
  document.getElementById('vSec').innerHTML=fmt1(sec)+' kWh/m³';
  document.getElementById('vCOP').textContent=fmt1(cop);
  document.getElementById('vHrs').textContent=hrs+' h';
  const emb=x=>makeup(x,C)*hrs*sec/1e6;
  const chl=x=>(x/REJ_RATIO)/cop*hrs/1000;
  const xs=[];for(let x=5;x<=200;x+=5)xs.push(x);
  ledgerChart.data.datasets[0].data=xs.map(x=>({x:x,y:+chl(x).toFixed(3)}));
  ledgerChart.data.datasets[1].data=xs.map(x=>({x:x,y:+emb(x).toFixed(3)}));
  ledgerChart.data.datasets[2].data=xs.map(x=>({x:x,y:+(100*emb(x)/chl(x)).toFixed(2)}));
  ledgerChart.data.datasets[3].data=[{x:MW,y:+emb(MW).toFixed(3)}];
  ledgerChart.update('none');
  const M=makeup(MW,C), ann=M*hrs, E=emb(MW), Cw=chl(MW);
  document.getElementById('rMu').innerHTML=fmt0(M*24)+' <small>m³/d</small>';
  document.getElementById('rAnn').innerHTML=fmt0(ann)+' <small>m³</small>';
  document.getElementById('rEmb').innerHTML=fmt2(E)+' <small>GWh</small>';
  document.getElementById('rChill').innerHTML=fmt1(Cw)+' <small>GWh</small>';
  document.getElementById('rPct').innerHTML=fmt1(100*E/Cw)+' <small>%</small>';
}
[sMW,sC,sSec,sCOP,sHrs].forEach(s=>s.addEventListener('input',updLedger));updLedger();

/* ---------- CHART 3 : the recovery stack ---------- */
const sCy=document.getElementById('sCy'),sOA=document.getElementById('sOA'),
      sCap=document.getElementById('sCap'),sGw=document.getElementById('sGw');
const psat=T=>0.61094*Math.exp(17.625*T/(T+243.04));
const humW=(T,rh)=>{const pw=rh*psat(T);return 0.62198*pw/(101.325-pw);};
const spVol=(T,W)=>0.287*(T+273.15)*(1+1.6078*W)/101.325;
const OA_T=40, OA_RH=0.55, COIL_T=13;
function condensate(Q){                      // m3/day from Q m3/s of outdoor air
  const Wo=humW(OA_T,OA_RH), Ws=humW(COIL_T,1.0);
  const m=Q/spVol(OA_T,Wo);
  return Math.max(0,m*(Wo-Ws))*86.4;
}
let recChart=new Chart(document.getElementById('recChart'),{
  type:'bar',
  data:{labels:['Base makeup\n(4 cycles)','Saved by\nmore cycles','Condensate\nrecovered','Greywater\napplied','Still to buy'],
    datasets:[{label:'m³/day',data:[],backgroundColor:[],borderColor:'#fff',borderWidth:1}]},
  options:{responsive:true,maintainAspectRatio:false,
    scales:{x:{...AX,ticks:{font:{family:'DM Sans',size:10.5}}},
            y:{type:'linear',min:0,title:{display:true,text:'Water (m³/day)',font:{family:'DM Sans',size:12,weight:'600'}},...AX}},
    plugins:{legend:{display:false},
      tooltip:{callbacks:{label:c=>`${fmt0(c.parsed.y)} m³/day`}}}}
});
function updRec(){
  const cy=+sCy.value,oa=+sOA.value,cap=+sCap.value/100,gw=+sGw.value;
  document.getElementById('vCy').innerHTML='4 &rarr; '+fmt1(cy);
  document.getElementById('vOA').innerHTML=oa+' m³/s';
  document.getElementById('vCap').textContent=fmt0(cap*100)+' %';
  document.getElementById('vGw').innerHTML=gw+' m³/d';
  const MW=+sMW.value, sec=+sSec.value, hrs=+sHrs.value;
  const base=makeup(MW,4)*24;
  const improved=makeup(MW,cy)*24;
  const cySave=Math.max(0,base-improved);
  const cond=Math.min(condensate(oa)*cap, improved);
  const gwUse=Math.min(gw, Math.max(0,improved-cond));
  const buy=Math.max(0,improved-cond-gwUse);
  recChart.data.datasets[0].data=[+base.toFixed(0),+cySave.toFixed(0),+cond.toFixed(0),+gwUse.toFixed(0),+buy.toFixed(0)];
  recChart.data.datasets[0].backgroundColor=['#1b4f72','#1e8449','#5eaadd','#6b4f9e','#c0392b'];
  recChart.update('none');
  const avoided=(base-buy)*365*sec/1e6;
  document.getElementById('rBase').innerHTML=fmt0(base)+' <small>m³/d</small>';
  document.getElementById('rCyc').innerHTML=fmt0(cySave)+' <small>m³/d</small>';
  document.getElementById('rCond').innerHTML=fmt0(cond)+' <small>m³/d</small>';
  document.getElementById('rBuy').innerHTML=fmt0(buy)+' <small>m³/d</small>';
  document.getElementById('rSaved').innerHTML=fmt2(avoided)+' <small>GWh/yr</small>';
}
[sCy,sOA,sCap,sGw,sMW,sC,sSec,sHrs].forEach(s=>s.addEventListener('input',updRec));updRec();

window.addEventListener('load',function(){try{chainChart.resize();ledgerChart.resize();recChart.resize();}catch(e){}});
"""

REFS = r"""
<h2 id="refs">References &amp; standards</h2>
<ol class="refs">
  <li>Voutchkov, N. <em>Desalination Engineering: Planning and Design</em> — specific energy consumption, recovery ratio and energy recovery device performance in seawater reverse osmosis.</li>
  <li>ASHRAE Handbook — <em>HVAC Systems and Equipment</em>, Cooling Towers chapter: evaporation rate, drift, blowdown and cycles of concentration.</li>
  <li>ASHRAE Handbook — <em>Fundamentals</em>, Psychrometrics chapter: moist-air properties used for the condensate calculation.</li>
  <li>International Desalination Association and Global Water Intelligence — published specific energy benchmarks for SWRO plants with and without pressure-exchanger energy recovery.</li>
  <li>Saline Water Conversion Corporation (SWCC) — Saudi water transmission system characteristics: coastal plants, inland pumping stages and delivered head to the central region.</li>
  <li>ASHRAE <em>Design Guide for Tall, Supertall, and Megatall Building Systems</em>, 2nd ed. — domestic water pumping energy and heat rejection strategy in tall buildings.</li>
  <li>Saudi Building Code SBC 501 / SBC 701 — mechanical and plumbing provisions, and Saudi Water Authority guidance on non-potable reuse for cooling tower makeup.</li>
</ol>
"""

TAGS = r"""
<div class="tags">#WaterEnergyNexus #Desalination #SWRO #EnergyRecovery #PressureExchanger #SpecificEnergy #kWhPerCubicMetre #WaterTransmission #Riyadh #Jeddah #GulfEngineering #TallBuildings #MegatallBuildings #CoolingTowers #Evaporation #Makeup #CyclesOfConcentration #Blowdown #EmbodiedEnergy #ChillerPlant #CondensateRecovery #Greywater #WaterReuse #DryCoolers #HybridCoolers #WaterConservation #Sustainability #DesignBasis #MEP #BuildingServices</div>
"""

SPEC = dict(
    slug='six-kilowatt-litre-water-energy-tall-buildings', cat='desalination', mins=18,
    date_iso='2026-08-20', date_human='August 2026', date_ar='أغسطس 2026',
    title='The Six-Kilowatt Litre: What Water Really Costs by the Time It Reaches the Top of a Gulf Tower',
    reg_title='The Six-Kilowatt Litre: What Water Really Costs by the Time It Reaches the Top of a Gulf Tower',
    reg_tag='Desalination · Water-Energy Nexus · Tall Buildings',
    breadcrumb='Desalination &amp; Water-Energy',
    tag_line='Desalination &middot; Water-Energy Nexus &middot; Cooling Towers &middot; Tall Buildings',
    desc='The full energy accounting of a litre of water from seawater to the top floor of a Gulf tower: SWRO specific energy with and without pressure-exchanger recovery, transmission head inland versus coastal, the pumping energy of height, and the embodied energy a cooling tower evaporates — with three interactive charts covering the energy chain, the evaporation ledger and the recovery stack.',
    og_desc='A litre reaching the top of a coastal Gulf tower carries about 6 kWh per cubic metre, and 10 inland where transmission beats desalination. The cooling towers then evaporate that water at an embodied energy equal to a tenth of what the chillers consume.',
    ld_desc='A design-perspective analysis of the water-energy nexus in Gulf tall buildings: desalination specific energy, transmission head, in-building pumping energy, and the embodied energy of cooling tower evaporation, with the design levers ranked by return.',
    img_alt='Technical cutaway showing the full water-energy chain in the Gulf: a seawater reverse osmosis plant on the coast, a long transmission main climbing inland, a megatall tower lifting water up its core, and a plume of vapour leaving the cooling towers on its roof',
    en_tag='Desalination &amp; Water-Energy &middot; Tall Buildings',
    en_title='The Six-Kilowatt Litre: What Water Really Costs by the Time It Reaches the Top of a Gulf Tower',
    en_excerpt='Desalination stops at the plant fence and building services start at the site boundary, so nobody adds up the whole chain. A litre reaching a top-floor tap costs about <strong>6 kWh/m³</strong> on the coast and <strong>10 inland</strong>, where transmission — not desalination — is the largest term. The tower then evaporates 2,400 m³ a day off its cooling towers, carrying embodied energy equal to roughly <strong>a tenth of the chiller plant&rsquo;s own consumption</strong> and appearing on no energy model. With three interactive charts and the levers ranked by what they actually return.',
    en_search='water energy nexus desalination SWRO specific energy consumption pressure exchanger energy recovery device PX ERD kWh per m3 recovery ratio feed pressure transmission pumping head Riyadh Jeddah Gulf tall buildings megatall domestic water lift pumping energy cooling tower makeup evaporation blowdown cycles of concentration embodied energy chiller COP condensate recovery greywater reuse dry cooler hybrid cooler water conservation sustainability design basis MEP building services',
    ar_title='اللتر بستة كيلوواط: التكلفة الحقيقية للمياه حتى تصل إلى قمة برج خليجي',
    ar_excerpt='تتوقف هندسة التحلية عند سور المحطة وتبدأ خدمات المباني عند حدود الموقع، فلا أحد يجمع السلسلة كاملة. اللتر الواصل إلى صنبور في الطابق الأخير يكلف نحو <strong>٦ ك.و.س/م³</strong> على الساحل و<strong>١٠</strong> في الداخل، حيث يتجاوز النقل التحلية. ثم يبخّر البرج ٢٤٠٠ م³ يومياً من أبراج التبريد، بطاقة كامنة تعادل نحو <strong>عُشر استهلاك محطة التبريد نفسها</strong>. مع ثلاثة رسوم تفاعلية.',
    ar_search='ترابط الماء والطاقة التحلية التناضح العكسي استهلاك الطاقة النوعي مبادل الضغط استرجاع الطاقة نسبة الاسترداد ضغط التغذية النقل الضخ الرياض جدة الخليج المباني الشاهقة المياه الصالحة للشرب رفع المياه طاقة الضخ تعويض أبراج التبريد التبخر التصريف دورات التركيز الطاقة الكامنة معامل الأداء استرجاع المكثفات إعادة استخدام المياه الرمادية المبردات الجافة الهجينة ترشيد المياه الاستدامة أساس التصميم',
    body=BODY, charts=CHARTS,
)
SPEC['body'] = BODY + REFS + TAGS
