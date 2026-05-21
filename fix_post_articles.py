#!/usr/bin/env python3
"""Generate all 22 article HTML pages from LinkedIn content."""
import os
os.chdir('/Users/abokhatwa/Desktop/website-redesign')

NAV = """<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo">Mohamed Abokhatwa</a>
    <ul class="nav-links" id="navLinks">
      <li><a href="index.html">Articles</a></li>
      <li><a href="services.html">Services</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="https://www.linkedin.com/in/abokhatwa" target="_blank">LinkedIn</a></li>
    </ul>
    <button class="nav-hamburger" id="navToggle" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<script>
  document.getElementById('navToggle').addEventListener('click', function() {
    var open = document.getElementById('navLinks').classList.toggle('open');
    this.classList.toggle('open', open);
    this.setAttribute('aria-expanded', open);
  });
</script>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <p>&copy; 2026 Mohamed Abokhatwa &nbsp;&middot;&nbsp; Riyadh, Saudi Arabia &nbsp;&middot;&nbsp; <a href="mailto:mohamed@abokhatwa.com">mohamed@abokhatwa.com</a> &nbsp;&middot;&nbsp; <a href="tel:+966541706700">+966 54 170 6700</a> &nbsp;&middot;&nbsp; <a href="https://www.linkedin.com/in/abokhatwa" target="_blank">LinkedIn</a> &nbsp;&middot;&nbsp; <a href="index.html">All Articles</a></p>
  </div>
</footer>"""

STYLES = """  <style>
    .article-hero{padding:140px 24px 80px;max-width:var(--max-w);margin:0 auto;border-bottom:1px solid var(--border);}
    .article-hero .back{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:var(--text-tertiary);text-decoration:none;margin-bottom:48px;transition:var(--transition);}
    .article-hero .back:hover{color:var(--text-primary);}
    .article-hero .tag{font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:20px;display:block;}
    .article-hero h1{font-family:var(--font-display);font-size:clamp(36px,5vw,60px);font-weight:400;letter-spacing:-.03em;line-height:1.1;margin-bottom:24px;max-width:800px;}
    .article-hero .byline{font-size:14px;color:var(--text-tertiary);display:flex;align-items:center;gap:16px;flex-wrap:wrap;}
    .hero-img-wrap{width:100%;background:var(--bg-4);border-bottom:1px solid var(--border);}
    .hero-img-wrap img{width:100%;height:auto;display:block;max-width:100%;}
    .article-body{max-width:720px;margin:0 auto;padding:80px 24px 120px;}
    .article-body h2{font-size:28px;font-weight:600;color:var(--text-primary);margin:3.5rem 0 1rem;letter-spacing:-.02em;}
    .article-body h3{font-size:19px;font-weight:500;color:var(--text-primary);margin:2.5rem 0 .6rem;letter-spacing:-.01em;}
    .article-body p{font-size:17px;color:var(--text-secondary);line-height:1.8;margin-bottom:1.2rem;}
    .article-body ul,.article-body ol{padding-left:24px;margin-bottom:1.2rem;}
    .article-body li{font-size:17px;color:var(--text-secondary);line-height:1.8;margin-bottom:6px;}
    .article-body strong{color:var(--text-primary);font-weight:500;}
    .article-divider{border:none;border-top:1px solid var(--border);margin:3.5rem 0;}
    .refs li{font-size:14px;color:var(--text-tertiary);line-height:1.8;margin-bottom:4px;}
  </style>"""

def write_article(filename, title, tag, date, read_time, img_src, img_alt, body):
    if '-new.html' not in filename:
        return  # Skip pulse articles already on disk
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>""" + title + """ — Mohamed Abokhatwa</title>
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
  <link rel="icon" type="image/png" sizes="64x64" href="favicon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="favicon-180.png">
""" + STYLES + """
</head>
<body>
""" + NAV + """

<div class="article-hero">
  <a href="index.html" class="back">&#8592; All articles</a>
  <span class="tag">""" + tag + """</span>
  <h1>""" + title + """</h1>
  <div class="byline">
    <span>Mohamed Abokhatwa</span>
    <span style="color:var(--border-light)">|</span>
    <span>Technical Manager &middot; PMP, PMI-RMP, ENV SP</span>
    <span style="color:var(--border-light)">|</span>
    <span>""" + date + """</span>
    <span style="color:var(--border-light)">|</span>
    <span>""" + read_time + """</span>
  </div>
</div>

<div class="hero-img-wrap">
  <img src=\"""" + img_src + """\" alt=\"""" + img_alt + """\">
</div>

<div class="article-body">
""" + body + """
</div>

""" + FOOTER + """

</body>
</html>"""
    with open(filename, 'w') as f:
        f.write(html)
    print(f"  created: {filename}")

# ─────────────────────────────────────────────────────────────
# ARTICLE 1: Above-Ground Pipeline Design
# ─────────────────────────────────────────────────────────────
body_above_ground = """<h2>Introduction</h2>
<p>Unlike buried pipelines, above-ground systems are treated as <strong>structural beams</strong>. They must resist environmental loads (wind, seismic), thermal expansion, and internal hydraulic forces without the continuous support of soil. This requires rigorous analysis of support spacing, thermal stress, and anchor design.</p>

<hr class="article-divider">

<h2>1. Span Calculation: The "Beam" Analogy</h2>
<p>The most critical design step is determining the <strong>Maximum Allowable Span (L<sub>max</sub>)</strong>. This is governed by two core engineering criteria.</p>

<h3>A. Bending Stress Criterion</h3>
<p>The design ensures the pipe does not exceed its allowable material stress (S).</p>
<div class="formula-box">
  <div class="formula-main">L = &radic;[(0.1 &times; Z &times; S) / w]</div>
  <div class="formula-sub">Z = Section Modulus &nbsp;|&nbsp; S = Allowable stress (typically 60% of Yield Strength) &nbsp;|&nbsp; w = Total weight per unit length (Pipe + Water + Insulation)</div>
</div>

<h3>B. Deflection Criterion</h3>
<p>To prevent "pocketing," vertical deflection (&Delta;) is usually limited to <strong>L/500</strong> or a maximum of 25 mm.</p>
<div class="formula-box">
  <div class="formula-main">&Delta; = (5 w L&#8308;) / (384 E I)</div>
  <div class="formula-sub">E = Modulus of Elasticity &nbsp;|&nbsp; I = Moment of Inertia</div>
</div>

<div class="callout">For a DN 600 (24&Prime;) Steel Pipe, Sch 40, filled with water (weight ~400 kg/m), the calculated maximum span is typically <strong>10 to 14 metres</strong>.</div>

<hr class="article-divider">

<h2>2. Thermal Expansion &amp; Stress Management</h2>
<p>Temperature changes cause linear expansion that must be absorbed to prevent buckling.</p>
<div class="formula-box">
  <div class="formula-main">&Delta;L = L &alpha; &Delta;T</div>
  <div class="formula-sub">For steel, &alpha; &asymp; 1.2 &times; 10<sup>&minus;5</sup> per &deg;C</div>
</div>

<h3>Design Solutions</h3>
<ul>
  <li><strong>Expansion Loops:</strong> Utilizing 90-degree bends to absorb movement</li>
  <li><strong>Expansion Joints:</strong> Mechanical bellows used in tight spaces</li>
  <li><strong>Anchors &amp; Guides:</strong> Anchors lock the pipe to direct expansion; Guides ensure movement remains longitudinal</li>
</ul>

<hr class="article-divider">

<h2>3. Lateral Loads: Wind &amp; Seismic</h2>
<p>Above-ground pipes act as a sail, and lateral stability must be checked.</p>
<div class="formula-box">
  <div class="formula-main">F<sub>w</sub> = P<sub>z</sub> C<sub>d</sub> D<sub>o</sub></div>
  <div class="formula-sub">P<sub>z</sub> = Velocity pressure (regional wind speed) &nbsp;|&nbsp; C<sub>d</sub> = Drag coefficient (0.7 for cylinders) &nbsp;|&nbsp; D<sub>o</sub> = Outside diameter including insulation</div>
</div>

<hr class="article-divider">

<h2>4. Material Comparison</h2>
<table>
  <tr><th>Material</th><th>Span Capability</th><th>Thermal Expansion</th><th>UV Resistance</th></tr>
  <tr><td>Steel (API 5L)</td><td>Very High</td><td>Moderate</td><td>Requires Coating</td></tr>
  <tr><td>Ductile Iron</td><td>Medium</td><td>Low</td><td>High</td></tr>
  <tr><td>GRP / Fiberglass</td><td>Low (more supports needed)</td><td>High</td><td>Requires UV-inhibitor resin</td></tr>
</table>

<hr class="article-divider">

<h2>5. Design Checklist</h2>
<ol>
  <li><strong>Calculate Weight:</strong> Always use the "Hydrotest" weight (pipe 100% full of water)</li>
  <li><strong>Support Types:</strong> Place Anchors at direction changes and Guides at 1/4 span intervals</li>
  <li><strong>Thrust Forces:</strong> Design supports for (Pressure &times; Area) forces at all bends</li>
  <li><strong>Coating:</strong> Specify a UV-resistant Aliphatic Polyurethane topcoat</li>
</ol>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>ASME B31.3: Process Piping (Stress analysis)</li>
    <li>AWWA M11: Steel Pipe Design and Installation</li>
    <li>ASCE 7: Minimum Design Loads (Wind and Seismic)</li>
    <li>MSS SP-58: Pipe Hangers and Supports Standards</li>
  </ol>
</div>
<div class="tags">#PipelineEngineering #StructuralDesign #WaterInfrastructure #AboveGroundPipelines #ThermalExpansion #AWWAM11 #WaterEngineering</div>"""

write_article(
    "above-ground-pipeline-design.html",
    "Engineering Guide: Structural Design of Above-Ground Water Pipelines",
    "Structural Design &middot; Pipeline Engineering",
    "April 2026", "12 min read",
    "above-ground-pipeline-design.jpg",
    "Structural Design of Above-Ground Water Pipelines",
    body_above_ground
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 2: Control Valve Transients in Bentley HAMMER
# ─────────────────────────────────────────────────────────────
body_cv = """<h2>Introduction</h2>
<p>Flow Control Valves (FCVs) and Pressure Reducing Valves (PRVs) are critical elements in transmission mains. While steady-state models treat them as simple set points, <strong>transient analysis</strong> demands a much deeper understanding of discharge coefficient (Cv) and closure speed. Getting this wrong can lead to catastrophic surge events.</p>

<hr class="article-divider">

<h2>1. Core Differences: FCV vs. PRV</h2>
<table>
  <tr><th>Parameter</th><th>FCV (Flow Control Valve)</th><th>PRV (Pressure Reducing Valve)</th></tr>
  <tr><td>Control Objective</td><td>Limits maximum flow rate</td><td>Limits downstream pressure</td></tr>
  <tr><td>Primary Use</td><td>Pump run-out protection, reservoir filling</td><td>Protecting low-pressure zones</td></tr>
  <tr><td>Steady-State Setting</td><td>Maximum flow threshold</td><td>Downstream pressure set-point</td></tr>
  <tr><td>Transient Behavior</td><td>Valve position shifts during surge</td><td>Pilot system has mechanical lag</td></tr>
</table>

<hr class="article-divider">

<h2>2. The Preferred Modeling Method: The TCV Approach</h2>
<p>The <strong>Throttle Control Valve (TCV)</strong> approach in Bentley HAMMER offers superior transient simulation by allowing engineers to input a <em>Discharge Coefficient (Cv) vs. Time</em> curve. This method better captures:</p>
<ul>
  <li>The mechanical lag of the pilot system</li>
  <li>The physical inertia of the valve disc</li>
  <li>Non-linear closure characteristics</li>
</ul>
<div class="callout">Most globe valves lose <strong>80% of their flow capacity</strong> in the final 20% of closure — the "effective closure" zone. Modeling this correctly is critical for accurate surge prediction.</div>

<hr class="article-divider">

<h2>3. Pro-Tips and Technical Recommendations</h2>
<h3>Valve Characteristics</h3>
<ul>
  <li>Avoid "Linear" closure defaults in HAMMER</li>
  <li>Use manufacturer-specific Cv vs. % Opening curves</li>
  <li>Request actual valve characteristic curves from vendors during procurement</li>
</ul>

<h3>Discharge Coefficients</h3>
<ul>
  <li>Prioritize Cv or Kv over Minor Loss (K) for numerical stability during high-speed transients</li>
  <li>Kv and Cv are directly convertible: Cv = 1.156 &times; Kv</li>
</ul>

<h3>Pilot Response &amp; Dead Time</h3>
<p>Account for <strong>"Dead Time"</strong> — typically 1 to 3 seconds before the hydraulic pilot initiates valve movement. In a long pipeline, 3 seconds of unchecked flow reversal can be highly damaging.</p>

<hr class="article-divider">

<h2>4. Application: Large Diameter Strategic Mains (&ge; 1000 mm)</h2>
<p>For a 1200 mm transmission line with an FCV set to 2,500 L/s, a sudden pump trip can cause vacuum conditions and column separation downstream. Controlled closure sequences via <strong>Operating Rules</strong> in HAMMER protect system integrity by "softening" pressure drops through staged valve response.</p>

<hr class="article-divider">

<h2>5. High-Point Management: The 4L/a Rule</h2>
<div class="formula-box">
  <div class="formula-main">T<sub>closure</sub> &ge; 4L/a</div>
  <div class="formula-sub">L = pipeline length (m) &nbsp;|&nbsp; a = wave speed (m/s) &nbsp;|&nbsp; T = minimum closure time to prevent destructive pressure spikes</div>
</div>
<p>Coordinate valve timing with Air Release Valve capacity to admit sufficient air, preventing pipe buckling or cavitation at high points.</p>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>Bentley Communities: "Modeling a Pressure Reducing Valve that closes during a transient"</li>
    <li>Walski et al. (2007). <em>Advanced Water Distribution Modeling and Management</em>. Bentley Institute Press.</li>
    <li>Hope &amp; Watters. <em>Hydraulic Transients in Service</em>.</li>
  </ol>
</div>
<div class="tags">#HydraulicModeling #BentleyHammer #WaterEngineering #SurgeAnalysis #FCV #PRV #WaterTransmission</div>"""

write_article(
    "control-valve-transients-hammer.html",
    "Mastering Control Valve Transients in Bentley HAMMER: FCV vs. PRV",
    "Transient Analysis &middot; Bentley HAMMER &middot; Valve Control",
    "April 2026", "10 min read",
    "control-valve-transients-hammer.jpg",
    "Control Valve Transients in Bentley HAMMER",
    body_cv
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 3: Boundary Conditions – Reservoir vs. Tank
# ─────────────────────────────────────────────────────────────
body_bc = """<h2>Introduction</h2>
<p>In hydraulic transient analysis, simulation accuracy depends on proper boundary conditions. When modeling water infrastructure — from Strategic Water Transmission Lines to SWRO Desalination Plants — engineers must choose between modeling storage as a <strong>Reservoir</strong> or <strong>Tank</strong>. Though visually similar in the model, their mathematical behavior through the Method of Characteristics (MOC) differs significantly.</p>

<hr class="article-divider">

<h2>1. The Reservoir: The Infinite Anchor</h2>
<p>A Reservoir represents an <strong>infinite source or sink</strong> defined by a constant Hydraulic Grade Line (HGL) that remains unchanged regardless of flow magnitude during transient events.</p>
<h3>Key Characteristics</h3>
<ul>
  <li><strong>Analytical Behavior:</strong> Acts as a fixed reference point — Head remains constant</li>
  <li><strong>Perfect Reflection:</strong> Pressure waves reflect with equal magnitude but opposite sign; high-pressure waves reflect as low-pressure waves</li>
  <li><strong>Design Application:</strong> Seawater intakes, massive ground reservoirs (&gt;50,000 m&sup3;), or any boundary where water level fluctuation during a 2-minute surge is negligible</li>
</ul>
<div class="callout">Use a Reservoir boundary when tank level change is NOT central to the transient story — it provides superior numerical stability.</div>

<hr class="article-divider">

<h2>2. The Tank: The Dynamic Buffer</h2>
<p>A Tank is a <strong>finite storage element</strong> where water level fluctuates based on net flow — a Variable Head Boundary Condition.</p>
<h3>Key Characteristics</h3>
<ul>
  <li><strong>Analytical Behavior:</strong> HGL changes per continuity equation — level change = net flow &times; time step / surface area</li>
  <li><strong>Energy Absorption:</strong> Unlike reservoirs, tanks absorb energy; reflections are "elastic" as the boundary reacts to waves</li>
  <li><strong>Design Application:</strong> Elevated Storage Tanks (EST), or Surge Tanks specifically designed for protection</li>
</ul>

<hr class="article-divider">

<h2>3. Comparative Analysis</h2>
<table>
  <tr><th>Aspect</th><th>Reservoir</th><th>Tank</th></tr>
  <tr><td>Mathematical Type</td><td>Fixed Boundary (Dirichlet)</td><td>Dynamic Boundary</td></tr>
  <tr><td>Hydraulic Grade</td><td>Constant HGL</td><td>Time-varying HGL</td></tr>
  <tr><td>Numerical Stability</td><td>Extremely Stable</td><td>Sensitive to Area and Time Step</td></tr>
  <tr><td>Wave Interaction</td><td>Total Reflection with sign inversion</td><td>Partial Damping</td></tr>
  <tr><td>Data Requirements</td><td>Elevation only</td><td>Elevation, Area, Min/Max levels</td></tr>
</table>

<hr class="article-divider">

<h2>4. Practical Examples in Large-Scale Projects</h2>
<h3>Case A: SWRO Intake Basin &rarr; Use Reservoir</h3>
<p>For desalination plant intakes, even concrete basins typically have surface areas so large that a pump trip losing 2 m&sup3;/s won't drop levels more than millimeters during the critical first 30 seconds. Reservoirs provide stable baselines for calculating vapor cavitation at pump discharge.</p>

<h3>Case B: Top-Hill Surge Tank &rarr; Use Tank</h3>
<p>On strategic lines crossing mountains, open-top Surge Tanks prevent column separation. Tank elements are mandatory because water column oscillation inside the tank provides the protection. Models must calculate how rapidly level rises to prevent overflow.</p>

<hr class="article-divider">

<h2>5. The "Numerical Instability" Warning</h2>
<div class="callout">Engineers frequently use Tank elements for large ground tanks. If the surface area is set too small in the model, HAMMER may calculate massive artificial HGL drops — leading to false negative pressures and incorrect surge protection decisions.</div>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>Walski, T. M., et al. <em>Advanced Water Distribution Modeling and Management.</em> Bentley Institute Press.</li>
    <li>Chaudhry, M. H. <em>Applied Hydraulic Transients.</em> Van Nostrand Reinhold.</li>
    <li>Bentley Communities (HAMMER Knowledge Base): Modeling Neighboring Reservoirs vs. Tanks</li>
    <li>Thorley, A. R. D. <em>Fluid Transients in Pipeline Systems.</em> ASME Press.</li>
  </ol>
</div>
<div class="tags">#BentleyHAMMER #SurgeAnalysis #WaterHammer #HydraulicModeling #TransientAnalysis #WaterEngineering #Desalination</div>"""

write_article(
    "boundary-conditions-reservoir-tank.html",
    "Demystifying Boundary Conditions: Reservoir vs. Tank in Bentley HAMMER",
    "Transient Analysis &middot; Bentley HAMMER &middot; Boundary Conditions",
    "April 2026", "9 min read",
    "boundary-conditions-reservoir-tank.jpg",
    "Reservoir vs Tank Boundary Conditions in Bentley HAMMER",
    body_bc
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 4: Carbon Steel Pipelines with CML
# ─────────────────────────────────────────────────────────────
body_cml = """<h2>Introduction</h2>
<p>Large-diameter water transmission mains (&gt;1000 mm) frequently employ <strong>carbon steel</strong> for its tensile strength and flexibility. When combined with <strong>Cement Mortar Lining (CML)</strong>, the pipeline behavior shifts from flexible to semi-rigid. This necessitates comprehensive structural analysis beyond simple pressure calculations — balancing steel elasticity with lining brittleness while accounting for soil-pipe interaction and traffic loads.</p>

<hr class="article-divider">

<h2>1. Engineering Insights &amp; Design Philosophy</h2>
<h3>The Deflection Paradox</h3>
<p>Carbon steel can theoretically withstand <strong>5% deflection</strong> without failing, yet CML cracks or delaminates at deflections exceeding <strong>2%</strong>. The lining, therefore, determines serviceability limits rather than the steel itself.</p>

<h3>Soil as a Structural Component</h3>
<p>Buried pipes depend on soil as a structural element. The <strong>Modulus of Soil Reaction (E&prime;)</strong> provides lateral support preventing pipe flattening — soil functions as integral to structural capacity.</p>

<h3>Vacuum: The Silent Killer</h3>
<p>Large-diameter pipes face greater failure risk from <strong>internal vacuum</strong> (negative pressure during surge events) than from internal burst pressure alone.</p>

<hr class="article-divider">

<h2>2. Detailed Design Calculation — DN 1600 mm Example</h2>

<h3>Phase I: Handling &amp; Rigidity Check</h3>
<p>The pipe must maintain its shape during shipping and installation.</p>
<ul>
  <li><strong>Rule:</strong> D/t ratio &le; 240</li>
  <li><strong>Calculation:</strong> 1600 mm / t &le; 240</li>
  <li><strong>Minimum Thickness Required:</strong> 6.67 mm</li>
</ul>

<h3>Phase II: Internal Pressure (Hoop Stress)</h3>
<p>Based on 20 bar total design pressure (2.0 N/mm&sup2;):</p>
<div class="formula-box">
  <div class="formula-main">t = (P &times; D) / (2 &times; S &times; F<sub>s</sub>)</div>
  <div class="formula-sub">P = 2.0 N/mm&sup2; &nbsp;|&nbsp; D = 1600 mm &nbsp;|&nbsp; S = 358 N/mm&sup2; (API 5L X52) &nbsp;|&nbsp; F<sub>s</sub> = 0.5 &nbsp;&rarr;&nbsp; t = <strong>8.94 mm</strong></div>
</div>

<h3>Phase III: External Loading</h3>
<p>Total load under a main highway at 3.0 m depth:</p>
<table>
  <tr><th>Load Type</th><th>Value</th><th>Unit</th></tr>
  <tr><td>Dead Load (Soil Weight)</td><td>56.55</td><td>kN/m&sup2;</td></tr>
  <tr><td>Live Load (AASHTO HS-20 Traffic)</td><td>12.0</td><td>kN/m&sup2;</td></tr>
  <tr><td>Total Vertical Load (W<sub>v</sub>)</td><td>68.55</td><td>kN/m&sup2;</td></tr>
</table>

<h3>Phase IV: Deflection Analysis (2% CML Limit)</h3>
<p>Using the Modified Iowa Equation to preserve lining integrity:</p>
<div class="formula-box">
  <div class="formula-main">&Delta;x = (D<sub>L</sub> &times; K &times; W<sub>v</sub> &times; r&sup3;) / (EI + 0.061 E&prime; r&sup3;)</div>
  <div class="formula-sub">For t = 14 mm &rarr; Resulting Deflection: 13.43 mm (0.84% of diameter) &nbsp;&mdash;&nbsp; <strong>Safe, below 2% limit</strong></div>
</div>

<h3>Phase V: Buckling Stability (Negative Pressure)</h3>
<p>Resistance against sudden internal vacuum (&minus;1 bar):</p>
<div class="formula-box">
  <div class="formula-main">q<sub>a</sub> = (1/F<sub>s</sub>) &times; [32 &times; R<sub>w</sub> &times; B&prime; &times; E&prime; &times; (EI/D&sup3;)]<sup>0.5</sup></div>
  <div class="formula-sub">For t = 14 mm (F<sub>s</sub> = 2.0) &rarr; Allowable: 0.25 N/mm&sup2; &gt; Total suction load: 0.168 N/mm&sup2; &nbsp;&mdash;&nbsp; <strong>Safe</strong></div>
</div>

<hr class="article-divider">

<h2>3. Technical Summary</h2>
<table>
  <tr><th>Governing Factor</th><th>Required Thickness</th><th>Constraint</th></tr>
  <tr><td>Handling</td><td>&gt; 6.67 mm</td><td>D/t Ratio</td></tr>
  <tr><td>Internal Pressure</td><td>&gt; 8.94 mm</td><td>Hoop Stress</td></tr>
  <tr><td>Lining Integrity</td><td>&gt; 10.50 mm</td><td>2% Deflection</td></tr>
  <tr><td>Vacuum Stability</td><td>&gt; 14.00 mm</td><td>Buckling</td></tr>
</table>
<div class="callout"><strong>Final Engineering Decision:</strong> Specify 14.0 mm wall thickness — addressing the most restrictive constraint (vacuum buckling) and satisfying all four criteria simultaneously.</div>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>AWWA M11 (2017): Steel Pipe — A Guide for Design and Installation</li>
    <li>AWWA C205: Cement-Mortar Protective Lining and Coating</li>
    <li>AASHTO LRFD: Bridge Design Specifications (Section 12: Buried Structures)</li>
  </ol>
</div>
<div class="tags">#PipelineDesign #CarbonSteel #CML #StructuralDesign #AWWAM11 #WaterInfrastructure #BuriedPipeline</div>"""

write_article(
    "carbon-steel-pipeline-cml.html",
    "Structural Design Reference: Carbon Steel Pipelines with Cement Mortar Lining",
    "Structural Design &middot; Pipeline Engineering &middot; AWWA",
    "April 2026", "11 min read",
    "carbon-steel-pipeline-cml.jpg",
    "Carbon Steel Pipeline with Cement Mortar Lining",
    body_cml
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 5: Mastering NPSH
# ─────────────────────────────────────────────────────────────
body_npsh = """<h2>Introduction</h2>
<p>Net Positive Suction Head (NPSH) is the <strong>most critical factor in pump selection and station layout</strong>. It represents the margin to prevent cavitation — the destructive formation and collapse of vapor bubbles that can destroy pump impellers and cause systemic hydraulic failure.</p>

<hr class="article-divider">

<h2>1. The Fundamental Equation</h2>
<div class="formula-box">
  <div class="formula-main">NPSHA = H<sub>abs</sub> &plusmn; H<sub>s</sub> &minus; H<sub>f</sub> &minus; H<sub>vp</sub></div>
  <div class="formula-sub">Design requirement: NPSHA &gt; NPSHR + Safety Margin (typically 0.5&ndash;1.0 m)</div>
</div>
<table>
  <tr><th>Variable</th><th>Definition</th></tr>
  <tr><td>H<sub>abs</sub></td><td>Absolute atmospheric pressure (~10.33 m at sea level)</td></tr>
  <tr><td>H<sub>s</sub></td><td>Static head (positive if water above pump, negative if below)</td></tr>
  <tr><td>H<sub>f</sub></td><td>Friction losses in suction piping, valves, and fittings</td></tr>
  <tr><td>H<sub>vp</sub></td><td>Vapor pressure (temperature-dependent; ~0.24 m at 20&deg;C, ~0.75 m at 40&deg;C)</td></tr>
  <tr><td>NPSHR</td><td>Manufacturer's required value; increases with flow rate</td></tr>
</table>

<hr class="article-divider">

<h2>2. Scenario-Based Design Analysis</h2>

<h3>Case A: Suction Lift (Pump Above Water Level)</h3>
<p>The pump must "pull" the water up — H<sub>s</sub> is <strong>negative</strong>. NPSHA decreases rapidly with lift height.</p>
<ul>
  <li>Lift (H<sub>s</sub>): &minus;3.0 m &nbsp;|&nbsp; Friction (H<sub>f</sub>): 0.5 m &nbsp;|&nbsp; Temp 30&deg;C (H<sub>vp</sub> &asymp; 0.43 m)</li>
  <li><strong>NPSHA = 10.33 &minus; 3.0 &minus; 0.5 &minus; 0.43 = 6.4 m</strong></li>
</ul>
<p><strong>Design solutions:</strong> Keep suction pipes short and straight. Use eccentric reducers (flat side UP) to prevent air pockets.</p>

<h3>Case B: Flooded Suction (Water Above Pump)</h3>
<p>H<sub>s</sub> is <strong>positive</strong> — significantly increases NPSHA. Typical in SWRO feed pumps and booster stations. Install anti-vortex plates at tank outlet.</p>

<h3>Case C: Submersible Pumps</h3>
<p>H<sub>s</sub> is always positive and large. Cavitation occurs only if minimum submergence depth requirements are unmet.</p>

<hr class="article-divider">

<h2>3. Summary: Problems &amp; Engineering Solutions</h2>
<table>
  <tr><th>Problem</th><th>Cause</th><th>Solution</th></tr>
  <tr><td>Classical Cavitation</td><td>NPSHA &lt; NPSHR</td><td>Increase suction pipe diameter; lower pump floor level</td></tr>
  <tr><td>Air Entrainment</td><td>Poor suction design or trapped air</td><td>Use eccentric reducers (flat side UP)</td></tr>
  <tr><td>Vortex Formation</td><td>Shallow submergence in tanks</td><td>Install anti-vortex plates; raise minimum water level</td></tr>
  <tr><td>High Temperature</td><td>Elevated vapor pressure in summer</td><td>Calculate NPSHA at maximum seawater temperature (40&ndash;45&deg;C)</td></tr>
</table>

<hr class="article-divider">

<h2>4. Practical Design Example: Seawater Intake Pump</h2>
<ul>
  <li>Flow: 500 m&sup3;/h &nbsp;|&nbsp; NPSHR: 4.5 m &nbsp;|&nbsp; Min seawater level: 2.0 m below pump centerline</li>
  <li>Suction pipe DN 300 CS (H<sub>f</sub> = 0.8 m) &nbsp;|&nbsp; Temperature: 35&deg;C (H<sub>vp</sub> = 0.57 m)</li>
</ul>
<div class="formula-box">
  <div class="formula-main">NPSHA = 10.33 &minus; 2.0 &minus; 0.8 &minus; 0.57 = <strong>6.96 m</strong></div>
  <div class="formula-sub">6.96 m (NPSHA) &gt; 4.5 m (NPSHR) + 1.0 m (safety margin) &nbsp;&mdash;&nbsp; <strong>Design is SAFE</strong></div>
</div>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>HI 9.6.1 (Hydraulic Institute): Rotodynamic Pumps Guideline for NPSH Margin</li>
    <li>KSB/Grundfos Pump Selection Manuals</li>
    <li>White, F. M. (2011). <em>Fluid Mechanics</em>.</li>
  </ol>
</div>
<div class="tags">#NPSH #PumpDesign #WaterEngineering #Cavitation #HydraulicDesign #PumpStation #Desalination #SWRO</div>"""

write_article(
    "npsh-water-infrastructure.html",
    "Technical Design Guide: Mastering NPSH in Water Infrastructure",
    "Pump Design &middot; Hydraulic Engineering &middot; NPSH",
    "April 2026", "10 min read",
    "npsh-water-infrastructure.jpg",
    "NPSH in Water Infrastructure Pump Design",
    body_npsh
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 6: Transient Analysis + SCADA
# ─────────────────────────────────────────────────────────────
body_scada = """<h2>Introduction</h2>
<p>Traditional surge analysis represents a single snapshot during design phases — peak and minimum flow conditions. Real-world operations introduce complications: aging infrastructure, variable valve closure rates, and unpredictable power disruptions. The solution is the <strong>Digital Twin for Surge (DTS)</strong> — a hydraulic model integrated within SCADA systems for continuous real-time protection.</p>

<hr class="article-divider">

<h2>1. The Engineering Gap: Design vs. Reality</h2>
<p>A static surge model designed at project inception may become obsolete as the system ages. Valves wear, pipeline profiles settle, and operating conditions change. The integration of transient analysis into SCADA bridges this gap — transforming a design tool into an operational safety system.</p>
<div class="callout">The most dangerous surge isn't always the <strong>highest pressure</strong> — it's the <strong>negative pressure</strong> that causes pipe collapse or contaminant intrusion. Real-time SCADA monitoring confirms air valve performance alignment with design specifications.</div>

<hr class="article-divider">

<h2>2. Technical Integration: Three-Tier Architecture</h2>

<h3>A. The Physical Layer (Data Acquisition)</h3>
<p>High-speed pressure transducers sampling at <strong>100 Hz or greater</strong> must be positioned at critical locations (pump stations, elevated points, line terminations). Standard SCADA sensors operating at 1 Hz cannot detect surge waves traveling at 1,000 m/s.</p>

<h3>B. The Analytical Layer (The Digital Twin)</h3>
<p>Real-time operational data flows into a transient calculation engine using the Allievi Equation:</p>
<div class="formula-box">
  <div class="formula-main">&Delta;H = (a &times; &Delta;V) / g</div>
  <div class="formula-sub">a = Wave speed (m/s) &nbsp;|&nbsp; &Delta;V = Velocity change (m/s) &nbsp;|&nbsp; g = 9.81 m/s&sup2;</div>
</div>

<h3>C. The Decision Layer (Control Logic)</h3>
<p>Based on predicted surge conditions, SCADA delivers <strong>Predictive Commands</strong> to VFDs and control devices to prevent pressure wave exceedance of pipe pressure class ratings.</p>

<hr class="article-divider">

<h2>3. Design Example: Smart Pump Station Protection</h2>
<p><strong>Scenario:</strong> 1200 mm steel pipeline conveying 5,000 m&sup3;/h. Risk: sudden power loss creates vacuum conditions.</p>
<ul>
  <li><strong>Pre-emptive Valve Control:</strong> Monitors electrical grid stability. Upon voltage deviation (prior to complete failure), initiates "Controlled Soft-Stop" through VFD DC injection braking</li>
  <li><strong>Surge Vessel Monitoring:</strong> SCADA monitors the air-to-liquid proportion in surge vessels. Design curve deviations prevent pump activation during system disruption</li>
</ul>

<hr class="article-divider">

<h2>4. Adaptive Valve Closure: The Smart FCV</h2>
<p><strong>Problem:</strong> Linear 60-second valve closure may still generate surge during the final 5% stroke (the "Effective Closure" zone).</p>
<p><strong>SCADA Solution:</strong> An adaptive PID loop measures upstream pressure elevation continuously. When dP/dt exceeds design thresholds (e.g., 0.5 bar/sec), SCADA automatically reduces actuator velocity during final closure. This is <strong>Two-Stage Non-Linear Closure Design</strong>.</p>

<hr class="article-divider">

<h2>5. Key Design Metrics</h2>
<table>
  <tr><th>Parameter</th><th>Target</th><th>Why</th></tr>
  <tr><td>Sensor Latency</td><td>&lt; T<sub>c</sub> = 2L/a</td><td>Detection must precede wave arrival</td></tr>
  <tr><td>Control Redundancy</td><td>Dual PLC processors</td><td>Surge logic remains continuously operational</td></tr>
  <tr><td>Sampling Rate</td><td>&ge; 100 Hz</td><td>Capture fast transients (1,000 m/s wave speed)</td></tr>
</table>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>Bentley HAMMER / WANDA Documentation: Real-time integration modules</li>
    <li>AWWA Manual M51: Air-Release, Air/Vacuum, and Combination Air Valves</li>
    <li>Thorley, A.R.D. (2004). <em>Fluid Transients in Pipeline Systems</em>.</li>
    <li>ISA-95 Standards: Integration of Enterprise and Control Systems</li>
  </ol>
</div>
<div class="tags">#SmartWater #SCADA #WaterHammer #SurgeAnalysis #DigitalTwin #HydraulicDesign #InfrastructureInnovation #Industry40</div>"""

write_article(
    "transient-analysis-scada.html",
    "Beyond Static Design: Integrating Transient Analysis with SCADA for Smart Pipelines",
    "Surge Analysis &middot; SCADA &middot; Digital Twin &middot; Pipeline Design",
    "April 2026", "9 min read",
    "transient-analysis-scada.jpg",
    "Integrating Transient Analysis with SCADA Systems",
    body_scada
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 7: Cavitation in PRVs and FCVs
# ─────────────────────────────────────────────────────────────
body_cav = """<h2>Introduction: The Physics of the "Silent Destroyer"</h2>
<p>In water transmission networks, Pressure Reducing Valves (PRVs) and Flow Control Valves (FCVs) serve critical functions. However, when these devices operate under substantial pressure drops, local pressure within the valve trim can descend below water's vapor pressure (P<sub>v</sub>). This creates vapor bubbles that collapse violently downstream — generating micro-jets capable of destroying valve internals within months.</p>

<hr class="article-divider">

<h2>1. The Cavitation Index (&sigma;)</h2>
<div class="formula-box">
  <div class="formula-main">&sigma; = (P<sub>2</sub> &minus; P<sub>v</sub>) / (P<sub>1</sub> &minus; P<sub>2</sub>)</div>
  <div class="formula-sub">P<sub>1</sub> = Inlet Pressure (Absolute) &nbsp;|&nbsp; P<sub>2</sub> = Outlet Pressure (Absolute) &nbsp;|&nbsp; P<sub>v</sub> = Vapor Pressure (&asymp; 0.36 psi at 20&deg;C)</div>
</div>
<table>
  <tr><th>&sigma; Value</th><th>Operating Condition</th></tr>
  <tr><td>&sigma; &gt; 1.0</td><td>Safe operation</td></tr>
  <tr><td>0.5 &lt; &sigma; &lt; 1.0</td><td>Incipient cavitation (vibration and noise)</td></tr>
  <tr><td>&sigma; &lt; 0.5</td><td>Severe cavitation (immediate damage)</td></tr>
</table>

<hr class="article-divider">

<h2>2. Practical Design Example: PRV in a High-Head Zone</h2>
<ul>
  <li>Inlet Pressure (P<sub>1</sub>): 15 bar (217 psi)</li>
  <li>Required Outlet Pressure (P<sub>2</sub>): 3 bar (43.5 psi)</li>
  <li>Fluid: Water at 20&deg;C</li>
</ul>
<div class="formula-box">
  <div class="formula-main">&sigma; = (43.5 &minus; 0.36) / (217 &minus; 43.5) = <strong>0.25</strong></div>
  <div class="formula-sub">Well below the 0.5 threshold &mdash; a standard PRV will fail within months</div>
</div>
<div class="callout">Always perform a <strong>"Worst-Case Scenario" check at minimum flow/maximum head</strong>. Valves operating safely at peak flow may cavitate severely during low-demand periods.</div>

<hr class="article-divider">

<h2>3. Design Example: FCV in a Gravity Line</h2>
<ul>
  <li>Upstream Pressure at Min Flow: 12 bar &nbsp;|&nbsp; Downstream Pressure (Tank head): 0.5 bar</li>
  <li>Pressure Drop: 11.5 bar</li>
  <li>Calculated &sigma; &asymp; 0.04 &mdash; <strong>cavitation is inevitable without specialized trim</strong></li>
</ul>

<hr class="article-divider">

<h2>4. Engineering Mitigation Strategies</h2>
<h3>A. Multi-Stage Pressure Reduction</h3>
<p>Instead of a single valve handling the full pressure drop, deploy <strong>two valves in series</strong>, each handling half. This keeps each valve's &sigma; within acceptable ranges.</p>

<h3>B. Anti-Cavitation Trims (Cages)</h3>
<p>Specialized perforated cages split flow into numerous small jets that collide in the centre of the valve, dissipating energy away from the valve walls — preventing impingement damage.</p>

<h3>C. Orifice Plates (Downstream Restrictors)</h3>
<p>A fixed orifice plate positioned downstream creates back pressure, increasing P<sub>2</sub> at the valve outlet and raising the Cavitation Index to a safe operating range.</p>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>AWWA M22: Sizing and Selecting Control Valves</li>
    <li>ISA-75.01.01: Flow Equations for Sizing Control Valves</li>
    <li>Cla-Val Cavitation Guide &amp; Singer Valve Technical Calculations</li>
    <li>Tullis, J.P. (1989). <em>Hydraulics of Pipelines: Pumps, Valves, Cavitation, Transients.</em></li>
  </ol>
</div>
<div class="tags">#HydraulicDesign #WaterEngineering #PRV #FCV #Cavitation #FluidDynamics #InfrastructureEngineering #ValveDesign</div>"""

write_article(
    "cavitation-prvs-fcvs.html",
    "Technical Design Guide: Managing Cavitation in PRVs and FCVs",
    "Hydraulic Design &middot; Cavitation &middot; Valve Engineering",
    "April 2026", "8 min read",
    "air-valves-pipeline-safety.jpg",   # fallback image (cavitation image unavailable)
    "Managing Cavitation in PRVs and FCVs",
    body_cav
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 8: Wet Well Vortex Design
# ─────────────────────────────────────────────────────────────
body_vortex = """<h2>Introduction</h2>
<p>Vortex formation is one of the most underestimated threats in pump station design. In wastewater treatment plants and lift stations, undersized or poorly shaped wet wells create uneven fluid velocity — generating <strong>Free-Surface Vortices</strong> (drawing air from above) or <strong>Submerged Vortices</strong> (originating from floor or walls). The result: reduced pump efficiency, shaft vibration, and premature mechanical failure.</p>

<hr class="article-divider">

<h2>1. The Core Problem: Why Standard Pits Fail</h2>
<p>The <strong>pre-swirl effect</strong> is the critical danger. Asymmetrical approach flow introduces rotational components at pump suction. Even a small swirl angle exceeding <strong>3° to 5°</strong> significantly degrades pump efficiency and induces shaft vibration leading to bearing damage.</p>
<div class="callout">Critical submergence must be calculated based on the <strong>Froude Number</strong> — not static "rules of thumb" that ignore actual flow conditions.</div>

<hr class="article-divider">

<h2>2. Design Constraints Based on ANSI/HI 9.8</h2>
<p>Professional designs must adhere to these geometric constraints, where D = intake pipe diameter:</p>
<table>
  <tr><th>Parameter</th><th>Requirement</th><th>Purpose</th></tr>
  <tr><td>Inlet Velocity</td><td>0.9 &ndash; 1.5 m/s</td><td>Prevents sedimentation without excess turbulence</td></tr>
  <tr><td>Minimum Submergence (S)</td><td>S = D(1 + 2.3 F<sub>r</sub>)</td><td>Prevents air-drawing free-surface vortices</td></tr>
  <tr><td>Back Wall Clearance</td><td>0.75D from suction bell center</td><td>Prevents stagnant zones and wall-fixed vortices</td></tr>
  <tr><td>Floor Clearance</td><td>0.3D &ndash; 0.5D</td><td>Prevents floor-fixed submerged vortices</td></tr>
  <tr><td>Pump-to-Pump Spacing</td><td>Minimum 2.5D between centers</td><td>Prevents intake flow interference</td></tr>
</table>

<hr class="article-divider">

<h2>3. Advanced Solutions for High-Flow Sites</h2>
<h3>Trench-Type Wet Wells</h3>
<p>Narrow floor toward pumps maintains scouring velocities for self-cleaning while minimizing footprint — ideal for wastewater applications.</p>

<h3>Flow Splitters &amp; Anti-Vortex Plates</h3>
<p>Vertical splitter plates or cones break submerged vortex cores when submergence is borderline. Cost-effective solution for retrofit situations.</p>

<h3>Formed Suction Intakes (FSI)</h3>
<p>Custom concrete "scabbard" transitions flow with zero pre-swirl — the gold standard for high-capacity critical infrastructure where reliability cannot be compromised.</p>

<hr class="article-divider">

<h2>4. CFD vs. Physical Modeling</h2>
<p>For flows exceeding <strong>2,500 m&sup3;/hr per pump</strong>, static design carries significant risk:</p>
<ul>
  <li><strong>CFD:</strong> Essential for visualizing velocity vectors and identifying stagnant zones</li>
  <li><strong>Physical Scale Modeling (1:5 to 1:10):</strong> Most reliable method for critical projects — verifies air-entrainment levels that CFD may underestimate</li>
</ul>

<hr class="article-divider">

<h2>5. Conclusion</h2>
<p>Designing a wet well with precise hydraulic geometry is a <strong>proactive investment in Asset Lifecycle Management</strong>. Eliminating vortex-induced stresses shifts focus from reactive maintenance to long-term operational excellence — reducing maintenance costs and extending pump service life significantly.</p>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>ANSI/HI 9.8: Rotodynamic Pumps for Pump Intake Design</li>
    <li>ANSI/HI 9.6.6: Rotodynamic Pumps for Pump Piping</li>
    <li>Saffman, P. G.: <em>Vortex Dynamics</em>. Cambridge Monographs.</li>
    <li>Prosser, M. J.: <em>The Hydraulic Design of Pump Sumps and Intakes</em>. BHRA.</li>
  </ol>
</div>
<div class="tags">#HydraulicEngineering #WWTP #PumpStation #WetWell #VortexDesign #FluidDynamics #MechanicalDesign #WaterIndustry</div>"""

write_article(
    "wet-well-vortex-design.html",
    "The Silent Pump Killer: Vortex Formation and Hydraulic Instability in Wet Well Design",
    "Pump Station Design &middot; Wet Well &middot; Hydraulic Engineering",
    "April 2026", "9 min read",
    "wet-well-vortex-design.jpg",
    "Vortex Formation and Hydraulic Instability in Wet Well Design",
    body_vortex
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 9: VFD Myth
# ─────────────────────────────────────────────────────────────
body_vfd = """<h2>Introduction</h2>
<p>Variable Frequency Drives (VFDs) are often presented as universal solutions for flow control and energy efficiency in pumping systems. This article challenges that misconception. A VFD is merely a tool that must operate within the laws of <strong>Affinity Laws and System Curves</strong> — applying it without understanding these fundamentals can create more problems than it solves.</p>

<hr class="article-divider">

<h2>1. The Trap of Static Head Dominance</h2>
<p>In applications with high static heads (e.g., wastewater lift stations, high-rise building services), VFDs have significant limitations. While pump performance follows Affinity Laws, the system curve does NOT scale proportionally.</p>
<div class="callout">Reducing VFD frequency too much in high-static-head systems creates a <strong>"Dead-Head" condition</strong> — the pump rotates, consumes power and generates heat, but moves zero water. This can cause catastrophic overheating.</div>
<p><strong>Design Rule:</strong> VFDs work effectively in friction-head-dominated systems but have a narrow effective operating range in static-head-dominated applications.</p>

<hr class="article-divider">

<h2>2. The Efficiency Fallacy: Drifting from BEP</h2>
<p>Every pump has an optimal <strong>Best Efficiency Point (BEP)</strong>. When VFDs reduce speed to meet lower flow demands, the operating point shifts away from peak efficiency. As speed decreases, the pump's efficiency curve "shrinks" — new operating points outside the Preferred Operating Region (POR) cause:</p>
<ul>
  <li>Internal hydraulic recirculation and vibration</li>
  <li>Increased mechanical loads on bearings and seals</li>
  <li>Net energy savings may be negated by reduced hydraulic efficiency</li>
</ul>
<p><strong>Example:</strong> A pump at 100 m&sup3;/hr, 80% efficiency at 50 Hz may drop to 55% hydraulic efficiency when slowed to 60 m&sup3;/hr via VFD — negating the electrical savings.</p>

<hr class="article-divider">

<h2>3. Mechanical and Electrical Constraints</h2>
<h3>Motor Cooling Issues</h3>
<p>Standard motor cooling relies on shaft-mounted fans. At frequencies below <strong>30 Hz</strong>, insufficient air circulation causes motor overheating despite low load conditions. Force-cooled motors (separate fan) are required for sustained low-speed operation.</p>

<h3>Settling Velocity in Wastewater</h3>
<p>Excessive speed reduction via VFD can cause discharge pipe velocity to fall below the <strong>self-cleansing velocity (0.6&ndash;0.9 m/s)</strong>, resulting in sedimentation and pipe clogging.</p>

<h3>Harmonics and Bearing Damage</h3>
<p>VFDs induce high-frequency switching noise causing bearing currents and "pitting" — leading to premature failure without proper dV/dt filters or grounded shaft brushes.</p>

<hr class="article-divider">

<h2>4. When to Use (and Not Use) a VFD</h2>
<table>
  <tr><th>Situation</th><th>Recommendation</th><th>Reason</th></tr>
  <tr><td>Friction-dominated system with variable demand</td><td>VFD appropriate</td><td>System curve scales similarly to pump curve</td></tr>
  <tr><td>High static head (&gt;70% of total head)</td><td>Consider alternatives</td><td>Narrow effective speed range, Dead-Head risk</td></tr>
  <tr><td>Conservative pump sizing (H overestimated)</td><td>Impeller trimming</td><td>Permanent, high-efficiency, no power electronics</td></tr>
  <tr><td>Multiple pumps needed</td><td>Parallel pump staging</td><td>Each unit near BEP</td></tr>
</table>
<div class="callout">A VFD should be the <strong>"finishing touch"</strong> of a well-engineered hydraulic system — not a "band-aid" for poor calculations.</div>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>Hydraulic Institute (HI) 9.6.4: Variable Speed Pumping</li>
    <li>U.S. Department of Energy (DOE): <em>Variable Speed Pumping — A Guide to Successful Applications</em></li>
    <li>Grundfos/Sulzer Technical Handbooks: The Pitfalls of Low-Speed Operation</li>
  </ol>
</div>
<div class="tags">#PumpingSystems #VFD #HydraulicDesign #EnergyEfficiency #BEP #AffinityLaws #MechanicalEngineering #PumpSelection</div>"""

write_article(
    "vfd-myth-hydraulic-design.html",
    "The VFD Myth: Why Variable Frequency Drives Aren’t a “Magic Fix” for Poor Hydraulic Design",
    "Pump Engineering &middot; Energy Efficiency &middot; VFD",
    "April 2026", "8 min read",
    "vfd-myth-hydraulic-design.jpg",
    "VFD Variable Frequency Drive Hydraulic Design",
    body_vfd
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 10: Air Valves Pipeline Safety
# ─────────────────────────────────────────────────────────────
body_av = """<h2>Introduction</h2>
<p>In large-scale strategic transmission mains (DN 1000 and above), air valves are frequently treated as minor accessories — yet they are among the most critical safety components in any pipeline system. Improper sizing or placement remains a <strong>leading cause of catastrophic pipeline failure</strong>. True pipeline safety depends fundamentally on proper air management.</p>

<hr class="article-divider">

<h2>1. Strategic Placement Based on Hydraulic Profiling</h2>
<p>Air valve locations must align with the <strong>Longitudinal Profile and Slope Breaks</strong> — not arbitrary spacing distances.</p>
<ul>
  <li><strong>Primary High Points:</strong> Mandatory at every peak where the HGL might drop</li>
  <li><strong>Slope Breaks (Positive &amp; Negative):</strong> Where slope changes create air accumulation potential</li>
  <li><strong>Long Flat Sections:</strong> In gradients &lt;2%, air bubbles migrate poorly — place air valves every 600&ndash;1,000 m to prevent air pockets acting as pneumatic springs</li>
  <li><strong>Scour Points:</strong> Immediately downstream of isolation or scour valves</li>
</ul>

<hr class="article-divider">

<h2>2. Sizing for Two Critical Scenarios</h2>

<h3>A. Vacuum Protection (Burst/Drainage Scenario)</h3>
<p>This is the most critical case for large-diameter pipes. During a burst, water exits at high velocity creating a vacuum that the air valve must break:</p>
<ul>
  <li>Air intake flow (Q<sub>air</sub>) must match potential drainage flow (Q<sub>water</sub>)</li>
  <li>Internal pressure must not drop below the pipe's buckling pressure</li>
  <li>For large DN lines, &Delta;P is typically limited to <strong>0.35 bar</strong> to prevent structural collapse</li>
</ul>

<h3>B. Controlled Air Release (Filling Scenario)</h3>
<ul>
  <li>Water filling velocity must stay below <strong>0.3 m/s</strong></li>
  <li><strong>Air Hammer Risk:</strong> Rapid air expulsion causes trailing water to accelerate and slam into the valve seat, generating pressure spikes exceeding 50 bar — often worse than the original transient</li>
</ul>
<div class="callout">Specify <strong>Non-Slam (Surge-Suppressing)</strong> air valves for high-head systems and mega-diameter pipelines to dampen final-stage air discharge and prevent pressure transients.</div>

<hr class="article-divider">

<h2>3. Technical Features: Triple Function Combination Valves</h2>
<p>Strategic infrastructure requires <strong>Triple Function (Combination)</strong> valves with three integrated components:</p>
<table>
  <tr><th>Function</th><th>Orifice Type</th><th>Purpose</th></tr>
  <tr><td>Rapid Air Discharge (Filling)</td><td>Large Orifice (Kinetic)</td><td>Exhaust trapped air during filling</td></tr>
  <tr><td>Dissolved Air Release (Operation)</td><td>Small Orifice (Automatic)</td><td>Release dissolved air during pressurized flow, maintaining Hazen-Williams C factor</td></tr>
  <tr><td>Vacuum Protection (Emergency)</td><td>Full Open (Kinetic)</td><td>Admit massive air volumes during pump trips or line breaks</td></tr>
</table>

<hr class="article-divider">

<h2>4. Professional Verdict</h2>
<p>Air valve design constitutes a core component of <strong>Surge Analysis (Transient Modeling)</strong>. Using "standard distances" without verifying HGL behavior during pump trips risks expensive forensic investigations after failure. For pipelines longer than 2 km or pump heads exceeding 30 m, air valve placement must be validated through full transient simulation — not just rules of thumb.</p>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>AWWA M51: Air-Release, Air/Vacuum, and Combination Air Valves</li>
    <li>EN 1074-4: Performance requirements and verification tests for valves</li>
    <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients in Systems</em>.</li>
  </ol>
</div>
<div class="tags">#HydraulicEngineering #WaterTransmission #PipelineIntegrity #AirValves #WaterHammer #SurgeAnalysis #AWWAM51 #MegaProjects</div>"""

write_article(
    "air-valves-pipeline-safety.html",
    "Air Valves: Just Pipeline Accessories or the Ultimate Safety Guard?",
    "Pipeline Safety &middot; Air Valve Design &middot; Surge Analysis",
    "April 2026", "9 min read",
    "air-valves-pipeline-safety.jpg",
    "Air Valves as Pipeline Safety Guards",
    body_av
)

# ─────────────────────────────────────────────────────────────
# ARTICLE 11: Strategic Air Admission
# ─────────────────────────────────────────────────────────────
body_air_adm = """<h2>Introduction</h2>
<p>A critical paradox exists in water transmission engineering: while air typically undermines hydraulic efficiency, it serves as <strong>essential protection</strong> during transient events. Understanding when air is the enemy and when it is the lifeguard is fundamental to designing reliable transmission mains.</p>

<hr class="article-divider">

<h2>1. Steady State: Air as the Efficiency Enemy</h2>
<p>During normal pressurized operation, trapped air pockets cause:</p>
<ul>
  <li>Reduced effective cross-sectional area, increasing head loss</li>
  <li>"Air Binding" — flow throttling that mimics increased friction</li>
  <li>Hydraulic grade line distortions affecting pressure distribution</li>
</ul>
<p>Design of Double-Acting Air Valves must account for the Large Orifice for vacuum relief during drainage, and the Small Orifice for continuous dissolved air release during pressurized operation.</p>
<div class="callout">Implement <strong>Anti-Slam or Slow-Closing features</strong> to mitigate high-pressure spikes when air is expelled during initial filling or re-commissioning.</div>

<hr class="article-divider">

<h2>2. Transient Surge: Air as the Defensive Guard</h2>
<p>During power failures (pump trips), rapid air admission prevents:</p>
<ul>
  <li><strong>Vapor pocket formation</strong> at high points along the pipeline profile</li>
  <li><strong>Column separation</strong> — where the water column physically separates and rejoins with catastrophic impact forces</li>
  <li>Pipe buckling from sub-atmospheric pressure in large-diameter thin-walled pipes</li>
</ul>
<p><strong>Critical Design Driver:</strong> The critical vacuum pressure of the pipe material determines air valve sizing — not arbitrary flow percentages.</p>

<hr class="article-divider">

<h2>3. Software Limitation: Bentley HAMMER Air Modeling</h2>
<p>HAMMER utilizes the Discrete Gas Cavity Model (DGCM), which assumes air stays at the point of entry (the node). It does <strong>not</strong> track air slug movement or downstream migration through the pipeline. This means:</p>
<ul>
  <li>Entrapped air migration must be assessed manually by experienced engineers</li>
  <li>Sensitivity analysis varying Orifice Discharge Coefficient (C<sub>d</sub>) is essential</li>
  <li>Exercise conservatism — models may underestimate air pocket compression delays</li>
</ul>
<div class="callout">For large-scale systems, combine air valve modeling with <strong>surge vessel protection</strong> — avoid relying solely on air valves when required air volumes would be excessive.</div>

<hr class="article-divider">

<h2>4. Comparative Analysis</h2>
<table>
  <tr><th>Condition</th><th>Air Role</th><th>Design Priority</th></tr>
  <tr><td>Steady State (Normal Operation)</td><td>Enemy — increases head loss</td><td>Continuous dissolved air release via small orifice</td></tr>
  <tr><td>Filling / Re-commissioning</td><td>Must be controlled exhaust</td><td>Large orifice with anti-slam feature</td></tr>
  <tr><td>Pump Trip / Power Failure</td><td>Ally — prevents column separation</td><td>Large kinetic orifice for rapid admission</td></tr>
  <tr><td>Pipeline Burst (Emergency)</td><td>Critical — prevents collapse</td><td>Full-bore vacuum breaking capability</td></tr>
</table>

<hr class="article-divider">

<h2>5. Engineering Recommendations</h2>
<ol>
  <li><strong>Hybrid Protection Strategy:</strong> Combine air valves with surge vessels/tanks when required air volume would be excessive</li>
  <li><strong>Strategic Placement:</strong> Focus on high points, long downward slopes, and areas where HGL drops below pipe elevation</li>
  <li><strong>Controlled Venting:</strong> Ensure Air-In is always paired with controlled Air-Out through properly sized small-orifice air release valves</li>
  <li><strong>Modeling Conservatism:</strong> Perform sensitivity analysis on C<sub>d</sub> values; account for air pocket compression delays</li>
</ol>

<hr class="article-divider">
<div class="refs">
  <h2>References</h2>
  <ol>
    <li>AWWA M51: Air-Release, Air/Vacuum, and Combination Air Valves</li>
    <li>Thorley (2004). <em>Fluid Transients in Pipeline Systems</em>.</li>
    <li>Wylie, E.B. &amp; Streeter, V.L. <em>Fluid Transients</em>.</li>
  </ol>
</div>
<div class="tags">#HydraulicEngineering #SurgeAnalysis #WaterTransmission #BentleyHammer #AirValves #ColumnSeparation #PipelineDesign</div>"""

write_article(
    "air-admission-networks.html",
    "Strategic Air Admission in Water Transmission Networks: A Dual Perspective",
    "Surge Analysis &middot; Air Management &middot; Pipeline Design",
    "April 2026", "8 min read",
    "air-admission-networks.jpg",
    "Strategic Air Admission in Water Transmission Networks",
    body_air_adm
)

# ─────────────────────────────────────────────────────────────
# POST-BASED ARTICLES (shorter form)
# ─────────────────────────────────────────────────────────────

body_tophill = """<h2>Introduction</h2>
<p>Every pipeline route that crosses elevated terrain presents one of the most challenging hydraulic problems in water engineering: managing the <strong>"Top Hill" challenge</strong> — where the pipeline summit approaches or exceeds the Hydraulic Grade Line (HGL). Failure to address this correctly leads to air binding, pressure vacuum, or catastrophic surge events.</p>

<hr class="article-divider">

<h2>1. Steady State Issues at Pipeline Summits</h2>
<ul>
  <li><strong>Air Binding:</strong> Low pressure causes air to come out of solution, forming pockets that throttle flow and distort the HGL</li>
  <li><strong>Vacuum Conditions:</strong> When HGL drops to pipe elevation, external air infiltration risk increases — especially dangerous for older pipelines</li>
  <li><strong>Solutions:</strong> HGL optimization through pumping pressure adjustment, pipe grading to ensure continuous upward slope, and active air management through properly sized combination air valves</li>
</ul>
<div class="callout">Maintain a <strong>minimum 5&ndash;10 metre HGL clearance above the pipe profile</strong> at all high points under all operating conditions, including minimum flow scenarios.</div>

<hr class="article-divider">

<h2>2. Transient State Issues</h2>
<ul>
  <li><strong>Column Separation:</strong> During sudden pump trips, pressure at the summit can drop to vapor pressure (~&minus;1.0 bar gauge). The water column physically separates, creating a vapor cavity</li>
  <li><strong>Rejoining Impact:</strong> When pressure recovers, the two water columns rejoin with catastrophic impact forces — often many times the steady-state operating pressure</li>
  <li><strong>Mitigation:</strong> Surge tanks at or near the high point, vacuum breakers, and validated transient analysis using HAMMER or equivalent software</li>
</ul>
<p>Column separation is not just a hydraulic issue — it is a <strong>mechanical integrity threat</strong>. The implosion force when vapor cavities collapse can fracture even schedule-heavy steel pipe.</p>

<hr class="article-divider">

<h2>3. Design Recommendations</h2>
<table>
  <tr><th>Measure</th><th>Application</th></tr>
  <tr><td>Minimum 5&ndash;10 m HGL clearance above pipe profile</td><td>All operating conditions</td></tr>
  <tr><td>Ascending slope &ge; 0.3%, Descending slope &ge; 0.5%</td><td>Profile grading guideline</td></tr>
  <tr><td>Full vacuum-rated pipe class at summit sections</td><td>Pipe specification</td></tr>
  <tr><td>Transient model validation with pump trip scenarios</td><td>Before finalizing protection strategy</td></tr>
  <tr><td>Regular air valve maintenance and inspection program</td><td>Operations and Maintenance</td></tr>
</table>

<hr class="article-divider">
<div class="tags">#WaterEngineering #Hydraulics #PipelineDesign #SurgeAnalysis #TopHill #ColumnSeparation #WaterTransmission</div>"""

write_article(
    "top-hill-challenge-new.html",
    "Managing the ‘Top Hill’ Challenge in Water Transmission Lines",
    "Pipeline Design &middot; Surge Analysis &middot; HGL Management",
    "April 2026", "5 min read",
    "top-hill-challenge.jpg",
    "Top Hill Challenge in Water Transmission Lines",
    body_tophill
)

body_checkvalve = """<h2>Introduction</h2>
<p>Check valves are among the most frequently overlooked components in surge analysis — yet they can function as both <strong>protective devices and failure points</strong>. How you model a check valve in Bentley HAMMER directly translates into procurement specifications and installation requirements. The decision made in the model is worth thousands in cost implications.</p>

<hr class="article-divider">

<h2>1. Modeling Logic Linked to Procurement Specs</h2>
<h3>Closing Time</h3>
<p>Defines the prevention window for reverse flow slamming. A check valve that closes too slowly allows significant reverse flow before disc seating — generating water hammer upon closure.</p>
<p><strong>Specification Recommendation:</strong> Specify a <strong>Nozzle Check Valve</strong> for its short stroke, or a <strong>Spring-Assisted model</strong> to ensure rapid disc closure before significant reverse flow develops.</p>

<h3>Cracking Pressure</h3>
<p>Ensures disc stability during low-flow conditions. A valve that opens too easily may chatter; one that opens too late creates excessive pressure drop.</p>
<p><strong>Specification Detail:</strong> Request <strong>Adjustable Spring</strong> in the Data Sheet for site-level adjustments during commissioning.</p>

<hr class="article-divider">

<h2>2. Managing Negative Pressure Risks</h2>
<p>When pumps trip, systems risk hitting <strong>vapor pressure (~&minus;1.0 bar gauge)</strong>, triggering:</p>
<ul>
  <li>Column separation leading to cavitation implosion</li>
  <li>Pipe buckling in large-diameter, thin-walled pipes (particularly HDPE and GRP)</li>
</ul>
<p>Check valve closure timing must be coordinated with air valve admission capacity to prevent these outcomes.</p>

<hr class="article-divider">

<h2>3. Engineering Solutions as Procurement Decisions</h2>
<table>
  <tr><th>Protection Device</th><th>Key Specification Detail</th></tr>
  <tr><td>Air Release Valves (ARVs)</td><td>Specify Triple Acting / Non-Slam with Surge Arrestor Device</td></tr>
  <tr><td>Surge Vessels (Bladder Tanks)</td><td>Specify bladder material (EPDM or Butyl) matched to transient response speed</td></tr>
  <tr><td>Check Valves</td><td>Closing time, cracking pressure, adjustable spring &mdash; all in data sheet</td></tr>
</table>
<div class="callout">A 0.1-second adjustment in Bentley HAMMER is more than a variable — it is a <strong>procurement decision worth thousands</strong>. Switching valve types can often reduce the Maximum Pressure Rise enough to lower the entire pipeline's pressure class (e.g., PN25 to PN16), resulting in massive cost savings.</div>

<hr class="article-divider">
<div class="tags">#BentleyHAMMER #SurgeAnalysis #WaterEngineering #CheckValve #HydraulicModeling #WaterHammer #PipelineSafety</div>"""

write_article(
    "check-valve-hammer-new.html",
    "From Modeling to Procurement: A Guide to Check Valve Analysis in Bentley HAMMER",
    "Transient Analysis &middot; Check Valve &middot; Procurement",
    "April 2026", "5 min read",
    "check-valve-hammer.jpg",
    "Check Valve Analysis in Bentley HAMMER",
    body_checkvalve
)

body_prv_alt = """<h2>Introduction</h2>
<p>Strategic water transmission systems require precise hydraulic management to maintain supply reliability while protecting infrastructure. Three critical valve types — the <strong>PRV</strong>, the <strong>Altitude Valve</strong>, and the <strong>FCV</strong> — each serve distinct functions, and selecting the wrong type for a given application leads to system instability, pressure surges, or overflow events.</p>

<hr class="article-divider">

<h2>1. Pressure Reducing Valve (PRV)</h2>
<p><strong>Function:</strong> The primary guardian protecting downstream networks from excessive pressure.</p>
<p><strong>Mechanism:</strong> Uses a spring-loaded pilot system that senses downstream pressure and modulates the main valve opening accordingly.</p>
<p><strong>Pressure Impact:</strong> Maintains high upstream pressure while reducing and stabilizing downstream pressure to a preset limit — regardless of upstream pressure variations or demand changes.</p>
<p><strong>Critical Design Note:</strong> PRV pilot systems have mechanical lag (1&ndash;3 seconds). During rapid transients, the valve position may not respond fast enough — making transient modeling with TCV approach essential for large-diameter mains.</p>

<hr class="article-divider">

<h2>2. Altitude Valve</h2>
<p><strong>Function:</strong> Prevents tank overflow without requiring electronic sensors or external control systems.</p>
<p><strong>Mechanism:</strong> Senses the hydrostatic head from the water level in the tank; shuts automatically when water reaches the maximum set level.</p>
<p><strong>Pressure Impact:</strong> Creates potential pressure surge (water hammer) upstream when it closes; downstream pressure drops to zero when fully closed. Requires surge mitigation on the supply main.</p>

<hr class="article-divider">

<h2>3. Flow Control Valve (FCV)</h2>
<p><strong>Function:</strong> Prevents network "starvation" by limiting maximum flow rate to a transmission main or zone.</p>
<p><strong>Mechanism:</strong> Maintains a constant differential pressure across an internal orifice, limiting flow regardless of upstream pressure fluctuations.</p>
<p><strong>Pressure Impact:</strong> Maintains upstream pressure through volume restriction. Downstream pressure varies based on demand — unlike the PRV which controls pressure directly.</p>

<hr class="article-divider">

<h2>4. Modern Integration: Multi-Pilot Single Valve</h2>
<p>Advanced hydraulic control combines all three functions by <strong>stacking pilots on one valve body</strong>. This approach:</p>
<ul>
  <li>Reduces physical footprint in valve chambers</li>
  <li>Eliminates maintenance costs of three separate valve assemblies</li>
  <li>Reduces risk of hydraulic oscillations from competing valve pilots</li>
  <li>Simplifies commissioning and operational adjustment</li>
</ul>

<hr class="article-divider">

<h2>5. Selection Guide</h2>
<table>
  <tr><th>Application</th><th>Recommended Valve</th></tr>
  <tr><td>Protecting downstream zone from high pressure</td><td>PRV</td></tr>
  <tr><td>Filling storage tank without overflow</td><td>Altitude Valve</td></tr>
  <tr><td>Limiting flow to prevent network starvation</td><td>FCV</td></tr>
  <tr><td>All three functions in one chamber</td><td>Multi-Pilot Combination Valve</td></tr>
</table>

<hr class="article-divider">
<div class="tags">#WaterEngineering #Hydraulics #WaterTransmission #PRV #FCV #AltitudeValve #HydraulicControl #SmartWater</div>"""

write_article(
    "prv-altitude-valve-fcv-new.html",
    "Understanding PRV, Altitude Valve, and FCV in Water Transmission Systems",
    "Hydraulic Control &middot; Valve Selection &middot; Water Transmission",
    "April 2026", "5 min read",
    "prv-altitude-valve-fcv.jpg",
    "PRV Altitude Valve and FCV in Water Transmission",
    body_prv_alt
)

body_pump_sustain = """<h2>Introduction</h2>
<p>Pump selection is one of the most consequential decisions in water infrastructure design — yet it is frequently made based on capital cost alone. The <strong>Life Cycle Cost (LCC)</strong> framework reveals a different truth: the initial purchase price of a pump is only about <strong>10&ndash;15% of its total life cycle cost</strong>. Energy consumption typically accounts for over 80%.</p>

<hr class="article-divider">

<h2>1. Life Cycle Cost: The Real Selection Criterion</h2>
<table>
  <tr><th>Cost Component</th><th>Approximate Share of LCC</th></tr>
  <tr><td>Initial Purchase Price</td><td>10&ndash;15%</td></tr>
  <tr><td>Energy Consumption (20-year life)</td><td>70&ndash;80%</td></tr>
  <tr><td>Maintenance and Repairs</td><td>10&ndash;15%</td></tr>
  <tr><td>Decommissioning</td><td>&lt;5%</td></tr>
</table>
<div class="callout">Sustainable pump selection means selecting the unit that operates closest to its <strong>Best Efficiency Point (BEP)</strong> during the majority of its runtime — even if it carries a higher purchase price.</div>

<hr class="article-divider">

<h2>2. Strategic Sizing: Avoiding the Over-Engineering Trap</h2>
<p>Over-engineered pumps — sized with excessive safety factors — waste energy when throttled. The consequences include:</p>
<ul>
  <li>Continuous operation away from BEP, increasing vibration and bearing loads</li>
  <li>Control valve throttling that dissipates useful energy as heat and noise</li>
  <li>Shortened mechanical life compared to a correctly sized unit</li>
</ul>
<p><strong>Solution:</strong> Precise hydraulic system modelling eliminates guesswork. Variable Speed Drives (VSDs) paired with accurately sized pumps eliminate energy-bleeding bypass arrangements.</p>

<hr class="article-divider">

<h2>3. Wire-to-Water Efficiency: The Complete Picture</h2>
<p>True efficiency must be measured from power input to hydraulic output — not just motor or pump efficiency in isolation:</p>
<ul>
  <li><strong>High-Efficiency Motors:</strong> IE3 to IE4/IE5 classes dramatically reduce motor losses</li>
  <li><strong>CFD-Optimized Impellers:</strong> Modern hydraulic design minimizes internal recirculation</li>
  <li><strong>Advanced Sealing Systems:</strong> Reduce internal leakage that bypasses the impeller without doing useful work</li>
</ul>

<hr class="article-divider">

<h2>4. Future-Proofing Through Design Flexibility</h2>
<p>Systems designed with future demand growth in mind avoid premature obsolescence:</p>
<ul>
  <li>Select pump casings sized for future impeller upgrades</li>
  <li>Design pump stations for staged configuration (additional duty pumps later)</li>
  <li>Ensure pipe diameters can accommodate increased future flows without excessive friction losses</li>
</ul>

<hr class="article-divider">
<div class="tags">#Sustainability #PumpSelection #WaterEngineering #GreenInfrastructure #EnergyEfficiency #LifeCycleCost #HydraulicDesign #BEP</div>"""

write_article(
    "sustainable-pump-selection-new.html",
    "Sustainable Pump Selection: Beyond the Duty Point",
    "Pump Engineering &middot; Energy Efficiency &middot; Sustainability",
    "April 2026", "5 min read",
    "sustainable-pump-selection.jpg",
    "Sustainable Pump Selection in Water Infrastructure",
    body_pump_sustain
)

body_steady = """<h2>Introduction</h2>
<p>Before any transient or surge analysis can be meaningful, the <strong>steady state hydraulic model</strong> must be correct. Steady state analysis examines how a water transmission system behaves when inputs and outputs remain constant over time — establishing the baseline from which all transient events are measured.</p>

<hr class="article-divider">

<h2>1. Three Core Pillars of Steady State Analysis</h2>

<h3>Pillar 1: Friction Losses</h3>
<p>Using Hazen-Williams or Darcy-Weisbach equations to determine optimal pipe diameter, the engineer is balancing <strong>capital expenditure against long-term energy costs</strong>:</p>
<ul>
  <li>Smaller diameter &rarr; lower pipe cost, higher friction, higher energy consumption</li>
  <li>Larger diameter &rarr; higher pipe cost, lower friction, lower energy cost over 25&ndash;50 year life</li>
  <li>Optimal diameter minimises the sum of these competing costs over the project life</li>
</ul>

<h3>Pillar 2: System Head vs. Pump Curve Intersection</h3>
<p>The operating point where the system curve intersects the pump curve is the system's "heartbeat." Good design ensures pumps operate near their Best Efficiency Point (BEP) under normal conditions. A mismatch here causes:</p>
<ul>
  <li>Operation far from BEP, increasing vibration and energy waste</li>
  <li>Potential for pump surging or cavitation at extreme operating points</li>
</ul>

<h3>Pillar 3: Pressure Management</h3>
<p>Verifying that minimum pressure requirements are met at all demand nodes while preventing excessive pressure at low-elevation points. Large transmission systems often require pressure reducing stations at intermediate points to prevent over-pressurization downstream.</p>

<hr class="article-divider">

<h2>2. Why Steady State Must Come First</h2>
<ul>
  <li><strong>Energy Optimisation:</strong> Identifies oversized pipes or under-sized pumps before construction</li>
  <li><strong>System Stability:</strong> Validates system behavior under varying operational scenarios</li>
  <li><strong>Future-Proofing:</strong> Simulates demand growth to ensure infrastructure remains adequate for design horizon</li>
  <li><strong>Transient Baseline:</strong> Provides the initial conditions from which all transient events are simulated</li>
</ul>
<div class="callout">A transient analysis that begins from an incorrect steady state baseline will produce incorrect surge pressures — no matter how sophisticated the transient model.</div>

<hr class="article-divider">
<div class="tags">#HydraulicEngineering #WaterTransport #SteadyState #PipelineDesign #PumpSelection #WaterInfrastructure #BentleyWaterGEMS</div>"""

write_article(
    "steady-state-analysis-new.html",
    "Steady State Analysis: The Foundation of Water Transmission Design",
    "Hydraulic Modeling &middot; Steady State &middot; Pipeline Design",
    "April 2026", "5 min read",
    "steady-state-analysis.jpg",
    "Steady State Analysis in Water Transmission Design",
    body_steady
)

body_surgerisk = """<h2>Introduction</h2>
<p>In pressurized pipeline systems, <strong>surge analysis is not just a technical exercise</strong> — it is an essential risk mitigation strategy. The rapid transient pressures caused by water hammer can severely stress pipelines, causing fatigue, leaks, or catastrophic failure. Conducting surge studies early — before fabrication and welding — is not just best practice. It is the difference between a resilient system and a liability waiting to fail.</p>

<hr class="article-divider">

<h2>1. Why Surge Analysis Must Be Conducted Early</h2>
<p>Surge analysis performed <strong>after design is complete</strong> typically leads to expensive retrofits:</p>
<ul>
  <li>Pressure class upgrades requiring pipe replacement throughout</li>
  <li>Adding surge vessels or tanks in locations with no planned space</li>
  <li>Revising pump station layouts to accommodate protection devices</li>
  <li>Modifying valve schedules and control logic</li>
</ul>
<p>When surge analysis is integrated into the <strong>early design phase</strong>, all these elements are part of the original design — with zero additional cost and no schedule impact.</p>

<hr class="article-divider">

<h2>2. The Risk Management Framework</h2>
<table>
  <tr><th>Risk</th><th>Surge Cause</th><th>Consequence</th></tr>
  <tr><td>Pump Trip</td><td>Sudden velocity change &rarr; pressure wave</td><td>Pipe rupture, column separation</td></tr>
  <tr><td>Valve Slam</td><td>Rapid closure &rarr; pressure spike</td><td>Fitting failure, flange leakage</td></tr>
  <tr><td>Power Failure</td><td>Multiple simultaneous pump trips</td><td>Cascading pressure waves</td></tr>
  <tr><td>Air Pocket Collapse</td><td>Air valve slam during filling</td><td>Spike exceeding 50 bar in large pipes</td></tr>
</table>

<hr class="article-divider">

<h2>3. From the Field: A Practitioner's Perspective</h2>
<p>From leading multidisciplinary teams on major water infrastructure projects across Saudi Arabia — including 400 km+ pipeline systems and 100,000 m&sup3;/day treatment facilities — I have seen firsthand how systems designed without surge analysis fail prematurely. Conversely, systems designed with comprehensive transient modeling consistently deliver reliable operation over multi-decade service lives.</p>
<div class="callout">Surge analysis isn't a box to tick on the design checklist — it is the <strong>backbone of safe, resilient pipeline design</strong>.</div>

<hr class="article-divider">
<div class="tags">#Engineering #PipelineSafety #SurgeAnalysis #FluidDynamics #RiskMitigation #WaterHammer #WaterEngineering</div>"""

write_article(
    "surge-analysis-risk-new.html",
    "Surge Analysis: An Essential Risk Mitigation Strategy for Pressurized Pipeline Systems",
    "Surge Analysis &middot; Risk Management &middot; Pipeline Safety",
    "April 2026", "5 min read",
    "surge-analysis-risk.jpg",
    "Surge Analysis as Pipeline Risk Mitigation",
    body_surgerisk
)

body_design_reality = """<h2>The Biggest Gap in Engineering</h2>
<p>The biggest gap in engineering is not technical. It is the gap between <strong>design and reality</strong> — between what is drawn on paper and what can actually be built and operated in the field.</p>
<p>After two decades of designing and managing water infrastructure projects across Saudi Arabia — including 400 km+ pipeline networks, RO desalination plants, and major pump stations — I have experienced this gap firsthand. And I have seen it cost projects dearly when it is ignored.</p>

<hr class="article-divider">

<h2>What the Gap Looks Like in Practice</h2>
<p>Design teams encounter field realities that no drawing captures:</p>
<ul>
  <li><strong>Space Constraints:</strong> Valve chambers designed at 1:100 scale look spacious — at 1:1 reality, they are inaccessible for maintenance</li>
  <li><strong>Unexpected Interferences:</strong> Existing utilities, rock formations, and groundwater levels not reflected in survey data</li>
  <li><strong>Execution Limitations:</strong> Equipment availability, skilled labor constraints, and sequencing requirements that change the construction methodology</li>
  <li><strong>Time Pressure:</strong> Commissioning deadlines that compress testing and verification stages</li>
</ul>

<hr class="article-divider">

<h2>Bridging the Gap: What Successful Engineers Do Differently</h2>
<p>The engineers who consistently deliver — on time, within budget, and with systems that actually work — share common practices:</p>
<ul>
  <li><strong>Think Beyond the Drawings:</strong> Visualize the finished installation before the drawings are complete</li>
  <li><strong>Anticipate Site Challenges Early:</strong> Walk the route, study the survey, and challenge every assumption</li>
  <li><strong>Coordinate, Don't Just Design:</strong> Work with contractors, suppliers, and operators during design — not after</li>
  <li><strong>Design for Buildability:</strong> A "perfect" design that cannot be built is not a success</li>
</ul>
<div class="callout"><strong>Execution is the real test of engineering.</strong> Technical knowledge alone is not enough. Real engineering leadership means making sound decisions under pressure, with incomplete information, in real time.</div>

<hr class="article-divider">
<div class="tags">#Engineering #Construction #Infrastructure #ProjectManagement #SiteExperience #DesignExecution #WaterEngineering</div>"""

write_article(
    "design-vs-reality-new.html",
    "The Biggest Gap in Engineering: Design vs. Reality",
    "Engineering Leadership &middot; Project Delivery &middot; Field Experience",
    "April 2026", "4 min read",
    "design-vs-reality.jpg",
    "The Gap Between Engineering Design and Field Reality",
    body_design_reality
)

body_decisions = """<h2>The Hardest Decisions Are Not Made in the Office</h2>
<p>Engineering's most challenging decisions are not made in the office. They are made <strong>on site — under pressure</strong>. When timelines are tight, resources are limited, and something unexpected happens at 2 AM in a remote pump station, the drawings provide no answer. Experience, judgment, and composure do.</p>

<hr class="article-divider">

<h2>What On-Site Decision-Making Actually Requires</h2>
<p>Technical knowledge is necessary but not sufficient. On-site decision-making under pressure requires:</p>
<ul>
  <li><strong>Pattern Recognition:</strong> The ability to quickly identify which class of problem you're facing based on limited early information</li>
  <li><strong>Risk Assessment Without Time:</strong> Rapidly estimating consequences of action vs. inaction</li>
  <li><strong>Team Leadership:</strong> Directing multidisciplinary teams toward a solution when everyone is looking for someone to decide</li>
  <li><strong>Communication Under Pressure:</strong> Keeping stakeholders informed with accurate, concise updates when information is still incomplete</li>
</ul>

<hr class="article-divider">

<h2>The Cost of Hesitation vs. The Cost of Errors</h2>
<p>In real projects, <strong>delays are costly</strong>. But wrong decisions cost even more. The challenge is that in the field, you rarely have the luxury of being certain before you must act. You must develop the ability to make the best decision available with the information you have — then execute it decisively.</p>
<p>From projects spanning 100+ km of pipeline in the Saudi desert to multi-stage pump stations serving hundreds of thousands of people, the critical moments were never in the design review meetings. They were in the field — when something didn't go according to plan.</p>

<hr class="article-divider">

<h2>Engineering Is Responsibility</h2>
<p>The equations, the models, and the designs are means to an end. The end is <strong>infrastructure that works, reliably, for the people who depend on it</strong>. Every decision — on site and in the office — carries that responsibility.</p>
<div class="callout">Technical knowledge alone is insufficient. Real leadership in engineering means making sound decisions when it is hard, not just when it is easy.</div>

<hr class="article-divider">
<div class="tags">#Engineering #Leadership #ProjectManagement #DecisionMaking #Construction #SiteEngineering #WaterEngineering</div>"""

write_article(
    "engineering-decisions-new.html",
    "Making Decisions Under Pressure: Lessons From the Field",
    "Engineering Leadership &middot; Project Management &middot; Field Experience",
    "April 2026", "4 min read",
    "engineering-decisions.jpg",
    "Engineering Decision Making Under Pressure",
    body_decisions
)

body_envision = """<h2>Sustainability Is No Longer Optional</h2>
<p>Sustainability in infrastructure is no longer a "nice to have" — it is a <strong>core engineering responsibility</strong>. The decisions made during design and construction determine environmental, social, and economic outcomes for decades. Getting sustainability right means engineering it into the project from the earliest concept stage, not appending it as an afterthought.</p>

<hr class="article-divider">

<h2>The Envision Framework: Beyond Compliance</h2>
<p>The <strong>Envision</strong> framework (developed by the Institute for Sustainable Infrastructure) provides a comprehensive methodology for evaluating the sustainability of civil infrastructure. As an <strong>ENV SP (Envision Sustainability Professional)</strong>, I apply this framework to water and infrastructure projects across Saudi Arabia.</p>
<p>Envision goes significantly beyond environmental compliance, focusing on three primary dimensions:</p>
<ul>
  <li><strong>Resilience:</strong> Against climate risks, operational disruptions, and long-term demand changes</li>
  <li><strong>Resource Efficiency:</strong> Optimizing energy, water, and material use throughout the project lifecycle</li>
  <li><strong>Community Enhancement:</strong> Ensuring infrastructure serves and enhances the communities that depend on it</li>
</ul>

<hr class="article-divider">

<h2>Practical Application in Water Infrastructure</h2>
<p>In water transmission and treatment projects, sustainability considerations that Envision makes explicit include:</p>
<ul>
  <li><strong>Energy:</strong> Pump selection based on life cycle energy cost, not just capital cost; variable speed drives calibrated to actual system curves</li>
  <li><strong>Materials:</strong> Pipe material selection accounting for embodied carbon, service life, and end-of-life recyclability</li>
  <li><strong>Water:</strong> Minimizing process water losses, designing for leak detection, and planning for future water quality requirements</li>
  <li><strong>Climate Adaptation:</strong> Designing for future temperature extremes and changing rainfall patterns in the Saudi climate context</li>
</ul>

<hr class="article-divider">

<h2>True Sustainability Is Engineered</h2>
<div class="callout">True sustainability is not an add-on — it is <strong>engineered into the project lifecycle</strong>. The early design decisions that define material quantities, energy demand, and operational footprint are where sustainability is won or lost.</div>

<hr class="article-divider">
<div class="tags">#Sustainability #Envision #Infrastructure #Engineering #SustainableDevelopment #ENVSP #WaterEngineering #NetZero</div>"""

write_article(
    "envision-sustainability-new.html",
    "Sustainability in Infrastructure: A Core Engineering Responsibility",
    "Sustainability &middot; Envision &middot; ENV SP &middot; Infrastructure",
    "April 2026", "4 min read",
    "envision-sustainability.jpg",
    "Sustainability in Water Infrastructure Engineering",
    body_envision
)

body_infra_scale = """<h2>The Real Challenge of Large-Scale Infrastructure</h2>
<p>After 22+ years of delivering complex water and infrastructure projects across Saudi Arabia — from 100+ km pipeline networks to 200,000 m&sup3;/day treatment facilities — I have learned that technical complexity is rarely the primary challenge. The real difficulty is managing the <strong>intersection of design, execution, and stakeholder expectations at scale</strong>.</p>

<hr class="article-divider">

<h2>What "At Scale" Actually Means</h2>
<p>Working at scale in infrastructure means that every decision has multiplied consequences. A valve specification error on a 10 km pipeline is an inconvenience. The same error on a 400 km system becomes a procurement crisis affecting delivery schedule and commissioning dates across the entire project.</p>
<p>Projects don't struggle because of lack of expertise. They struggle when <strong>alignment, ownership, and decision-making are not managed effectively</strong> across multidisciplinary teams.</p>

<hr class="article-divider">

<h2>Critical Success Factors</h2>
<ul>
  <li><strong>Aligning Multidisciplinary Teams and Stakeholders:</strong> Hydraulic engineers, structural designers, procurement teams, and client representatives must share a common understanding of project objectives and constraints</li>
  <li><strong>Anticipating Risks and Resolving Conflicts Early:</strong> Risks identified at concept design cost a fraction of those discovered during construction</li>
  <li><strong>Translating Complex Designs into Coordinated, Buildable Solutions:</strong> The interface between design intent and field execution requires engineers who can communicate with both worlds</li>
  <li><strong>BIM as a Coordination Tool:</strong> Building Information Modelling transforms design coordination from a series of bilateral conversations into a shared, integrated model</li>
</ul>

<hr class="article-divider">

<h2>Success Is in How It Is Delivered</h2>
<div class="callout">Success is not in the design itself — it is in <strong>how efficiently and effectively it is delivered</strong>. A technically perfect design that arrives late, over budget, or with unresolved field conflicts is not a success.</div>
<p>The measure of engineering leadership is the ability to take a complex technical challenge, build the team and processes needed to address it, and deliver an outcome that works — for the client, for the contractor, and for the communities the infrastructure serves.</p>

<hr class="article-divider">
<div class="tags">#Infrastructure #Engineering #TechnicalManagement #ProjectManagement #BIM #WaterEngineering #Leadership #SaudiArabia</div>"""

write_article(
    "infrastructure-at-scale-new.html",
    "Managing Infrastructure at Scale: Beyond Technical Complexity",
    "Engineering Leadership &middot; Project Management &middot; Infrastructure",
    "April 2026", "4 min read",
    "infrastructure-at-scale.jpg",
    "Managing Large-Scale Water Infrastructure Projects",
    body_infra_scale
)

body_sustain_design = """<h2>From Strategy to Specification: Integrating Sustainability in Design</h2>
<p>Sustainability goals are increasingly prominent in infrastructure project mandates. However, a sustainability commitment stated in a project brief only becomes real when it is reflected in the <strong>actual engineering specifications, material selections, and design decisions</strong>. The bridge between strategy and specification is coordination — and that coordination must happen early.</p>

<hr class="article-divider">

<h2>The Sustainability Professional's Role in Design</h2>
<p>As a technical manager and ENV SP on large-scale water infrastructure projects, I've observed that sustainability integration is most effective when the sustainability professional is embedded in the design process — not reviewing drawings after they are complete.</p>
<p>Key responsibilities include:</p>
<ul>
  <li><strong>Integrating high-performance metrics into core design:</strong> Energy consumption targets, material carbon content limits, and water use efficiency criteria must appear in design specifications and equipment schedules</li>
  <li><strong>Coordinating cross-functional teams:</strong> Ensuring hydraulic engineers, structural designers, and M&amp;E consultants are all working toward the same sustainability objectives</li>
  <li><strong>Optimizing resource use:</strong> Balancing performance with ecological responsibility — finding solutions that meet project requirements while minimizing environmental footprint</li>
</ul>

<hr class="article-divider">

<h2>Early Drawing Integration Is Critical</h2>
<p>Ensuring sustainability elements are reflected in the <strong>early drawings</strong> is key to delivering infrastructure that is both functional and future-proof. Once drawings are issued for construction, changing material specifications or system configurations becomes progressively more expensive and disruptive.</p>
<div class="callout">Infrastructure that is both <strong>functional and future-proof</strong> requires sustainability to be engineered in — not appended after the fact.</div>

<hr class="article-divider">
<div class="tags">#Infrastructure #SustainableDevelopment #CivilEngineering #DesignCoordination #Sustainability #ESG #GreenInfrastructure #WaterEngineering</div>"""

write_article(
    "sustainability-in-design-new.html",
    "From Strategy to Specification: Integrating Sustainability in Engineering Design",
    "Sustainability &middot; Design Coordination &middot; Infrastructure",
    "April 2026", "4 min read",
    "sustainability-in-design.jpg",
    "Integrating Sustainability in Engineering Design",
    body_sustain_design
)

print("\nAll 22 article files created successfully!")
