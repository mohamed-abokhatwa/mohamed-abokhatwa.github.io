# Website Modifications — Performance Pass (3 July 2026)

Published live in commit `bcbb894` (reapplied as `e573da9`) on abokhatwa.com.
**Zero visual change** — design, text, and layout are untouched on every page.

## 1. Chart.js no longer blocks page rendering — 21 pages
The `Chart.js` and `chartjs-plugin-annotation` scripts were loaded in the
`<head>`, delaying first paint. They now load at the bottom of the page,
just before the chart initialisation code.
- 14 article pages (chiller plant, NRW, pressure/DMA, pump curves, etc.)
- All 7 MEP course modules

## 2. Calendly stylesheet no longer blocks rendering — 73 pages
`widget.css` from assets.calendly.com was a render-blocking stylesheet on
every page. It now loads asynchronously (`media="print"` + `onload`) and
applies once ready. The "Book a Consultation" popup works unchanged.

## 3. Real thumbnails for homepage cards — index.html, index-ar.html
Card thumbnails (displayed at 160×100) were loading the full 1376×768
hero images. A new `thumbs/` folder holds 50 WebP thumbnails at 320×200:
- Homepage image payload: **4.9 MB → 604 KB** (−88%)
- `width`/`height` attributes added (no layout shift)
- One card on the Arabic homepage loaded its image from an external
  CloudFront URL — replaced with the local image.

## 4. Image dimensions and priorities — 60 pages
- `width`/`height` added to 98 images → no layout jumping while loading
- `fetchpriority="high"` on 45 article hero images → hero paints first
- Below-fold content images remain lazy-loaded

## 5. Head hints — all 74 pages
- `preconnect` to googletagmanager.com, cdnjs.cloudflare.com and
  assets.calendly.com (only where each is actually used)
- `theme-color` metas for light (#f5f5f7) and dark (#0e0e10) so mobile
  browser chrome matches the site theme

## Verification done before publishing
- All charts render on article and course pages, no console errors
- Homepage and Arabic homepage load correctly with thumbnails
- Article-count guard (`scripts/check-articles.py`) passes: 51 everywhere
- Live checks after deploy: thumbnails serve (HTTP 200), async Calendly
  and theme-color present on live pages

## Note on git history
GitHub Pages' deploy service failed transiently several times on 3 July
(their side — proven by a revert test). History therefore contains two
empty trigger commits plus a revert/reapply pair; the final deployed
state is exactly the performance pass described above.
