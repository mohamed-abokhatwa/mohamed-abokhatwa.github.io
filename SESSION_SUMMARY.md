# Website Session Summary
**Date:** 2026-05-25  
**Project:** Mohamed Abokhatwa — Water Engineering Website  
**Root:** `/Users/abokhatwa/Desktop/website-redesign/`  
**Live:** `https://abokhatwa.com`

---

## 1. Project Structure

```
website-redesign/
├── index.html            # Homepage EN — 36 articles with search/filter
├── index-ar.html         # Homepage AR — same 36 articles, Arabic UI
├── calculators.html      # 18 calculators, 9 categories (3232 lines)
├── style.css             # Shared CSS — 620 lines (includes dark mode + print)
├── theme.js              # Dark/Light mode toggle (new file)
├── article-features.js   # Shared article script: progress bar + PDF + related articles (360 lines)
├── sitemap.xml           # 44 URLs, all lastmod 2026-05-25
├── about.html / about-ar.html
├── services.html / services-ar.html
├── pipeline-checklist.html
└── [36 article .html files]
```

---

## 2. Calculators (calculators.html)

**18 calculators across 9 categories:**

| # | Category | Calculators |
|---|----------|-------------|
| 1 | Water Hammer & Surge | WH (Joukowsky), WS (Wave Speed), SV (Surge Velocity) |
| 2 | Pipeline Hydraulics | HW (Hazen-Williams), RE (Reynolds), ML (Minor Losses) |
| 3 | Pump Engineering | PP (Pump Power), NP (NPSH), BL (Bulk Modulus) |
| 4 | Manning & Open Channel | MGP (Manning Pipe), MOC (Manning Open Channel) |
| 5 | Darcy-Weisbach | DW (Darcy-Weisbach with Swamee-Jain) |
| 6 | Thrust & Structural | TH (Thrust Block) |
| 7 | Pump Affinity & Speed | AFF (Affinity Laws), NS (Specific Speed Nq) |
| 8 | Water Treatment | TNK (Tank/Reservoir Sizing), CL (Chlorine Dosing & CT) |
| 9 | Economic Optimization | EPD (Economic Pipe Diameter) |

**Hero stats corrected:** `18 Calculators · 9 Categories · SI Units`

**Key JS functions:** `calcWH, calcWS, calcSV, calcHW, calcRE, calcML, calcPP, calcNP, calcBL, calcMGP, calcMOC, calcDW, calcTH, calcAFF, calcNS, calcTNK, calcCL, calcEPD`

**DOMContentLoaded init calls all 18 functions.**

### Important JS Helper Functions
```javascript
setPrimary(id, numericValue, unit)   // sets primary result display
setText(id, string)                  // sets text of element
setPill(id, pillClass, text)         // sets status pill
fmt(value, decimals)                 // formats number
toggleFormula(id, btn)               // shows/hides formula box
toggleDiagram(id, btn)               // shows/hides diagram
```

### CSS Patterns in calculators.html
```css
/* Field input wrap */
.field { display:flex; flex-direction:column; gap:5px; min-width:0; }
.field-wrap { display:flex; align-items:center; border:1.5px solid #e5e5ea; border-radius:10px; overflow:hidden; min-width:0; }
.field-wrap input, .field-wrap select { flex:1; min-width:0; border:none; outline:none; background:transparent; padding:9px 12px; }
.field-wrap select { cursor:pointer; width:0; }

/* Category header pattern */
<div class="calc-category">
  <div class="card-icon [color]" style="width:32px;height:32px;font-size:16px;">[emoji]</div>
  <h3>[Category Name]</h3>
  <div class="calc-category-line"></div>
</div>

/* Card header pattern */
<div class="card-header">
  <div class="card-icon [color]">[emoji]</div>
  <div class="card-header-text">
    <h2>[Title]</h2>
    <p>[Subtitle]</p>
  </div>
</div>
```

---

## 3. Features Added This Session

### Feature A — Article Search & Filter (index.html + index-ar.html)
- Search input with live filtering across title, excerpt, tags
- 7 category filter chips: All · Surge & Transients · Pipeline Design · Pump Engineering · Hydraulic · Desalination · Leadership
- When filter active → shows ALL 36 articles, hides "Show More" button
- When cleared → restores default (6 visible + Show More)
- "No results" message if nothing matches
- `data-cat` and `data-search` on every article `<a>` tag
- Articles grid has `id="articlesGrid"`
- CSS: `.articles-grid.filtering .article-card { display:flex !important; }` to override `.hidden-article`
- Arabic version uses RTL search input, Arabic chip labels, bilingual `data-search` values

**JS functions:** `setCat(cat, btn)`, `filterArticles()`

### Feature B — Reading Progress Bar (all 36 articles)
- Injected by `article-features.js`
- Fixed 3px blue gradient bar at top of viewport, fills as user scrolls
- z-index: 10001

### Feature C — Reading Time Auto-Calculation (all 36 articles)
- Counts words in `.article-body`, divides by 230 wpm
- Updates the `span` containing "min read" in `.byline`

### Feature D — PDF Download Button (all 36 articles)
- Injected by `article-features.js` → `injectPdfButton()`
- Inserted as a `div.pdf-btn-wrap` AFTER the `.byline` element
- Blue outlined pill button: "⬇ Download PDF" → calls `window.print()`
- Print CSS in `style.css` hides nav, footer, FABs, related articles, newsletter, progress bar
- Dark mode variant: accent color `#2997ff`

### Feature E — Related Articles (all 36 articles)
- Injected by `article-features.js` → `renderRelated()`
- Inserted before `<footer>`
- 3-column grid (→ 2 on tablet → 1 on mobile)
- Matches by `cat` field: surge / pipeline / pumps / hydraulic / desalination / leadership
- Falls back to other categories if same-cat < 3
- All 36 articles defined in `ARTICLES` array in `article-features.js`

### Feature F — Dark / Light Mode (all 44 pages)
- `theme.js` — global toggle, saves to `localStorage('site-theme')`
- Respects `prefers-color-scheme` on first visit
- Flash prevention: inline script in `<head>` of every page:
  ```html
  <script>(function(){var t=localStorage.getItem("site-theme")||(matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light");document.documentElement.setAttribute("data-theme",t);})();</script>
  ```
- Toggle button in nav (moon → sun icon): `id="theme-toggle"` before hamburger
- Applied via `data-theme="dark"` on `<html>` element
- Dark mode colors: bg `#0e0e10`, glass `rgba(255,255,255,0.055)`, accent `#2997ff`
- Dark mode overrides: body, nav, table th/td, sim-header, callout boxes, gradients

### Feature G — Nav Updates
- `calculators.html` link added to nav of all 36 article pages
- Arabic index has `calculators.html` still missing from nav (not added — only EN articles)

### Feature H — Sitemap
- Added `calculators.html` (was missing)
- Updated all `lastmod` to `2026-05-25`
- Organized by category sections
- `changefreq` for homepage changed to `weekly`
- Total: 44 URLs

---

## 4. Shared CSS Variables (style.css :root)

```css
:root {
  --bg: #f5f5f7;          --bg-2: #fbfbfd;       --bg-3: #ffffff;    --bg-4: #ededf0;
  --border: rgba(0,0,0,0.1);                      --border-light: rgba(0,0,0,0.15);
  --glass: rgba(255,255,255,0.68);                --glass-border: rgba(255,255,255,0.88);
  --glass-hover: rgba(255,255,255,0.84);
  --shadow-glass: 0 2px 20px rgba(0,0,0,0.06)...;
  --text-primary: #1d1d1f;  --text-secondary: #6e6e73;  --text-tertiary: #86868b;
  --accent: #0071e3;
  --success: #1a7a38;  --danger: #c42b2b;  --warning: #8a5700;
  --font-display: 'DM Serif Display', Georgia, serif;
  --font-body: 'DM Sans', -apple-system, sans-serif;
  --radius: 20px;  --radius-sm: 12px;  --max-w: 980px;
  --blur: blur(20px) saturate(180%);
}

/* Dark mode overrides at :root[data-theme="dark"] */
/* Dark accent: #2997ff, bg: #0e0e10, text-primary: #f5f5f7 */
```

---

## 5. Article HTML Structure (all 36 articles)

```html
<head>
  <meta charset="UTF-8">
  <script>/* flash prevention */</script>
  <link rel="stylesheet" href="style.css">
  <style>
    .article-hero { padding:140px 24px 80px; ... }
    .article-hero .byline { display:flex; align-items:center; gap:16px; flex-wrap:wrap; }
    .article-body { max-width:720px; margin:0 auto; padding:80px 24px 120px; }
  </style>
</head>
<body>
<nav class="nav">
  <!-- nav-logo, nav-links (Articles · Calculators · Services · About · LinkedIn), theme-toggle, hamburger -->
</nav>

<div class="article-hero">
  <a href="index.html" class="back">← All articles</a>
  <span class="tag">Category · Subcategory</span>
  <h1>Title</h1>
  <div class="byline">
    <span>Mohamed Abokhatwa</span>
    <span>|</span>
    <span>Technical Manager · PMP, PMI-RMP, ENV SP</span>
    <span>|</span>
    <span>Month 2026</span>
    <span>|</span>
    <span>X min read</span>
    <!-- article-features.js injects: | [Download PDF button] -->
  </div>
  <!-- article-features.js injects: div.pdf-btn-wrap after byline -->
</div>

<div class="hero-img-wrap"><img src="article.jpg"></div>

<div class="article-body">
  <!-- content: h2, h3, p, ul, table, .callout, .formula-box, .warning-box, .danger-box -->
  <div class="tags">#Tag1 #Tag2</div>
</div>

<footer>...</footer>

<!-- article-features.js injects: section.related-articles-section before footer -->

<script src="article-features.js"></script>
<script src="theme.js"></script>
</body>
```

---

## 6. article-features.js — ARTICLES Data Array

All 36 articles defined with: `{ url, title, cat, thumb, mins, tag }`

Categories: `surge` | `pipeline` | `pumps` | `hydraulic` | `desalination` | `leadership`

Key article URLs and categories:
- `water-hammer-control-valve.html` → surge
- `surge-vessel.html` → surge  
- `pre-charge-pressure.html` → surge
- `combination-air-valves.html` → pipeline
- `above-ground-pipeline-design.html` → pipeline
- `npsh-water-infrastructure.html` → pumps
- `wet-well-vortex-design.html` → pumps
- `hydraulic-mistakes.html` → hydraulic
- `cavitation-prvs-fcvs.html` → hydraulic
- `daf-swro-pretreatment.html` → desalination
- *(+ 26 more in the array)*

---

## 7. Files Modified This Session

| File | Change |
|------|--------|
| `style.css` | Dark mode vars, toggle button, print CSS, responsive fix |
| `theme.js` | **NEW** — dark/light toggle logic |
| `article-features.js` | **NEW** — progress bar, reading time, PDF button, related articles |
| `index.html` | Search/filter UI + JS, data-cat on all cards, articlesGrid id |
| `index-ar.html` | Same as above in Arabic |
| `calculators.html` | Stats: 9→18 calculators, 4→9 categories |
| `sitemap.xml` | Added calculators.html, updated all lastmod to 2026-05-25 |
| All 36 article .html | Added: Calculators nav link, flash script, theme-toggle btn, article-features.js, theme.js |
| about/services pages | Added: flash script, theme-toggle btn, theme.js |

---

## 8. Known Pending / Possible Next Items

- Arabic article pages don't have `calculators.html` in their nav (articles link to EN page anyway)
- Dark mode not tested on calculators.html — the hero section is already dark (hardcoded gradient), rest uses CSS vars so should adapt
- `water-hammer-control-valve.html` has embedded interactive calculators (900+ lines) — these use hardcoded colors in some places that may not fully adapt to dark mode
- No Arabic versions of individual article pages (all 36 articles are English only)
- Google Search Console: submit updated sitemap after deployment
