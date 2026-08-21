#!/usr/bin/env python3
"""
gen_article.py — build a full article page from a compact spec, and wire it into
the site (registry, EN + AR index grids, category chips, sitemap).

Usage:  python3 scripts/gen_article.py specs/<name>.py

The spec module must define a dict called SPEC. See specs/_example.py.
Boilerplate (head, styles, nav, footer, newsletter) comes from scripts/_tmpl_*.html,
which were extracted from an existing published article so every page stays identical.
"""
import io, os, re, sys, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
T = lambda n: io.open(f'scripts/_tmpl_{n}.html', encoding='utf-8').read()

AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

def ar_count(n):
    """Arabic category-chip count, matching the forms already used on the site."""
    d = str(n).translate(AR_DIGITS)
    if n == 1:  return f"{d} مقالة"
    if n == 2:  return f"{d} مقالتان"
    if n <= 10: return f"{d} مقالات"
    return f"{d} مقالة"

def build_html(s):
    charts = s.get('charts', '')
    chart_libs = ''
    if charts:
        chart_libs = ('<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>\n'
                      '<script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-annotation/3.0.1/'
                      'chartjs-plugin-annotation.min.js"></script>\n<script>\n' + charts + '\n</script>\n\n')
    return (
        T('HEAD_TOP')
        + f"  <title>{s['title']} — Mohamed Abokhatwa</title>\n"
        + '    <link rel="alternate" type="application/rss+xml" title="Mohamed Abokhatwa — Engineering Insights" href="https://abokhatwa.com/feed.xml">\n'
        + '  <link rel="stylesheet" href="style.css?v=7">\n'
        + '  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png?v=2">\n'
        + '  <link rel="icon" type="image/png" sizes="64x64" href="favicon.png?v=2">\n'
        + '  <link rel="apple-touch-icon" sizes="180x180" href="favicon-180.png?v=2">\n'
        + '  <script>\n    MathJax = { tex: { inlineMath: [[\'\\\\(\', \'\\\\)\']], displayMath: [[\'\\\\[\', \'\\\\]\']] }, svg: { fontCache: \'global\' } };\n  </script>\n'
        + '  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js" id="MathJax-script" async></script>\n'
        + T('STYLE') + T('CALENDLY')
        + f'  <meta name="description" content="{s["desc"]}">\n'
        + f'  <meta property="og:title" content="{s["title"]} | Mohamed Abokhatwa">\n'
        + f'  <meta property="og:description" content="{s["og_desc"]}">\n'
        + '  <meta property="og:type" content="website">\n'
        + f'  <meta property="og:url" content="https://abokhatwa.com/{s["slug"]}.html">\n'
        + f'  <meta property="og:image" content="https://abokhatwa.com/og-{s["slug"]}.jpg">\n'
        + f'  <meta property="og:image:alt" content="{s["img_alt"]}">\n'
        + '  <meta name="twitter:card" content="summary_large_image">\n'
        + f'  <meta name="twitter:title" content="{s["title"]} | Mohamed Abokhatwa">\n'
        + f'  <meta name="twitter:description" content="{s["og_desc"]}">\n'
        + f'  <link rel="canonical" href="https://abokhatwa.com/{s["slug"]}.html">\n\n'
        + '  <script type="application/ld+json">\n{\n'
        + '  "@context": "https://schema.org",\n  "@type": "TechArticle",\n'
        + f'  "headline": "{s["title"]}",\n'
        + f'  "description": "{s["ld_desc"]}",\n'
        + f'  "image": "https://abokhatwa.com/og-{s["slug"]}.jpg",\n'
        + f'  "datePublished": "{s["date_iso"]}",\n  "dateModified": "{s["date_iso"]}",\n'
        + '  "author": { "@type": "Person", "name": "Mohamed Abokhatwa", "url": "https://abokhatwa.com/about.html" },\n'
        + '  "publisher": { "@type": "Person", "name": "Mohamed Abokhatwa" },\n'
        + f'  "mainEntityOfPage": {{ "@type": "WebPage", "@id": "https://abokhatwa.com/{s["slug"]}.html" }}\n'
        + '}\n  </script>\n</head>\n'
        + T('NAV')
        + '<div class="article-hero">\n  <a href="/" class="back">&#8592; All articles</a>\n'
        + f'  <div class="breadcrumb"><a href="/">Articles</a><span class="breadcrumb-sep">›</span><span class="breadcrumb-current">{s["breadcrumb"]}</span></div>\n'
        + f'  <span class="tag">{s["tag_line"]}</span>\n'
        + f'  <h1>{s["title"]}</h1>\n'
        + '  <div class="byline">\n    <span>Mohamed Abokhatwa</span>\n'
        + '    <span style="color:var(--border-light)">|</span>\n'
        + '    <span>Mechanical Manager &middot; MSc, PMP, PMI-RMP, Envision SP</span>\n'
        + '    <span style="color:var(--border-light)">|</span>\n'
        + f'    <span>{s["date_human"]}</span>\n'
        + '    <span style="color:var(--border-light)">|</span>\n'
        + f'    <span data-mins-fixed>{s["mins"]} min read</span>\n  </div>\n</div>\n\n'
        + '<div class="hero-img-wrap">\n'
        + f'  <img fetchpriority="high" width="1376" height="768" src="{s["slug"]}.webp" alt="{s["img_alt"]}">\n'
        + '</div>\n\n'
        + '<div class="article-body">\n' + s['body'] + '\n</div>\n\n'
        + T('FOOTER') + chart_libs + T('TAIL')
    )

def wire_site(s):
    slug, cat = s['slug'], s['cat']

    # 1 · registry (prepend, newest first)
    p = 'article-features.js'; t = io.open(p, encoding='utf-8').read()
    if f"url:'{slug}.html'" not in t:
        anchor = "  var ARTICLES = [\n"
        entry = ("    { url:'%s.html', title:'%s', cat:'%s', thumb:'%s.webp', mins:%d, tag:'%s' },\n"
                 % (slug, s['reg_title'].replace("'", "\\'"), cat, slug, s['mins'], s['reg_tag']))
        t = t.replace(anchor, anchor + entry, 1)
        io.open(p, 'w', encoding='utf-8').write(t)

    # 2 · EN + AR index: card at top of grid, chip +1, keep exactly 4 cards visible
    for idx, lang in (('index.html', 'en'), ('index-ar.html', 'ar')):
        t = io.open(idx, encoding='utf-8').read()
        if f'href="{slug}.html"' in t:
            continue
        # chip increment (create nothing — category must already exist)
        m = re.search(r'(class="cat-card"\s+data-cat="%s".*?cat-card-count">\s*)([^<]+)(</div>)' % cat, t, re.S)
        if not m:
            sys.exit(f"FATAL: category chip '{cat}' not found in {idx} — add the cat-card first")
        cur = m.group(2).strip()
        n = int(re.sub(r'\D', '', cur.translate(str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")))) + 1
        new = f"{n} article" + ("s" if n != 1 else "") if lang == 'en' else ar_count(n)
        t = t[:m.start(2)] + new + t[m.end(2):]

        if lang == 'en':
            card = ('    <a href="%s.html" class="article-card" data-cat="%s" data-search="%s">\n'
                    '      <div class="card-body">\n'
                    '        <span class="article-card-tag">%s</span>\n'
                    '        <div class="article-card-title">%s</div>\n'
                    '        <p class="article-card-excerpt">%s</p>\n'
                    '        <div class="article-card-meta">\n'
                    '          <span>%s</span>\n          <span>%d min read</span>\n'
                    '          <span class="article-card-arrow">&#8594;</span>\n'
                    '        </div>\n      </div>\n'
                    '      <div class="card-thumb">\n'
                    '        <img src="thumbs/%s.webp" width="320" height="200" alt="%s" loading="lazy">\n'
                    '      </div>\n    </a>\n\n'
                    % (slug, cat, s['en_search'], s['en_tag'], s['en_title'], s['en_excerpt'],
                       s['date_human'], s['mins'], slug, s['en_title']))
        else:
            card = ('    <a href="%s.html" class="article-card" data-cat="%s" data-search="%s">\n'
                    '      <div class="card-body">\n'
                    '        <span class="article-card-tag">%s</span>\n'
                    '        <div class="article-card-title">%s</div>\n'
                    '        <p class="article-card-excerpt">%s</p>\n'
                    '        <div class="article-card-meta">\n'
                    '          <span>%s</span><span>%s دقيقة</span>\n'
                    '          <span class="article-card-arrow">&#8592;</span>\n'
                    '        </div>\n      </div>\n'
                    '      <div class="card-thumb"><img src="thumbs/%s.webp" width="320" height="200" alt="%s" loading="lazy"></div>\n'
                    '    </a>\n\n'
                    % (slug, cat, s['ar_search'], s['en_tag'], s['ar_title'], s['ar_excerpt'],
                       s['date_ar'], str(s['mins']).translate(AR_DIGITS), slug, s['en_title']))

        gm = re.search(r'(<div class="articles-grid" id="articlesGrid">\s*\n\n?)', t)
        t = t[:gm.end(1)] + card + t[gm.end(1):]
        # demote the card that was 4th so exactly 4 stay visible
        vis = [m2 for m2 in re.finditer(r'<a href="([^"]+)" class="article-card" data-cat=', t)]
        if len(vis) > 4:
            m2 = vis[4]
            t = t[:m2.start()] + m2.group(0).replace('class="article-card"', 'class="article-card hidden-article"') + t[m2.end():]
        io.open(idx, 'w', encoding='utf-8').write(t)

    # 3 · sitemap
    p = 'sitemap.xml'; t = io.open(p, encoding='utf-8').read()
    if slug not in t:
        anchor = 'ARTICLES \u2014 TALL & MEGATALL BUILDING MEP\n  \u2550'
        j = t.find(anchor)
        k = t.index('<url>', j) if j != -1 else t.index('<url>')
        entry = ('<url>\n    <loc>https://abokhatwa.com/%s.html</loc>\n'
                 '    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n'
                 '    <priority>0.85</priority>\n  </url>\n  ' % (slug, s['date_iso']))
        io.open(p, 'w', encoding='utf-8').write(t[:k] + entry + t[k:])

def main():
    spec_path = sys.argv[1]
    name = os.path.splitext(os.path.basename(spec_path))[0]
    sp = importlib.util.spec_from_file_location(name, spec_path)
    mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    s = mod.SPEC
    out = f"{s['slug']}.html"
    io.open(out, 'w', encoding='utf-8').write(build_html(s))
    wire_site(s)
    print(f"✓ {out}  ({os.path.getsize(out)//1024} KB, cat={s['cat']}, {s['mins']} min)")

if __name__ == '__main__':
    main()
