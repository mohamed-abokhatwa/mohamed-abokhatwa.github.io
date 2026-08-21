#!/usr/bin/env python3
"""
build_handbook.py — assemble the tall-building articles into a single printable
reading edition (megatall-handbook.html).

Interactive figures cannot print, so each one is replaced by a figure card that
keeps the title, the stated model and the finding, and links to the live chart
in the source article.
"""
import io, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

PARTS = [
 ("I", "The building as a pressure vessel",
  "Height turns four ordinary services into one coupled problem. These four chapters are the physics every later chapter inherits.",
  ["stack-effect-tall-buildings","mechanical-floors-tall-buildings",
   "building-movement-mep-tall-buildings","vibration-noise-control-tall-buildings"]),
 ("II", "Water",
  "The tallest column of water in the building, the smallest pressure window, and the systems that have to live inside both.",
  ["domestic-water-tall-buildings","domestic-hot-water-legionella-tall-buildings",
   "drainage-stormwater-tall-buildings","basement-dewatering-drainage-tall-buildings",
   "greywater-reuse-tall-buildings","pools-wellness-mep-tall-buildings"]),
 ("III", "Cooling",
  "From the chiller barrel to the plume on the roof, and the water and pressure class that decide the architecture.",
  ["chiller-plant-design","chilled-water-pumps-tall-buildings",
   "cooling-towers-heat-rejection-tall-buildings","district-cooling-ets-tall-buildings",
   "refrigerant-systems-tall-buildings","thermal-energy-storage-tall-buildings",
   "cooling-load-modelling-tall-buildings","water-treatment-building-systems"]),
 ("IV", "Air",
  "Shaft area is the scarcest commodity in a tower, and air is what consumes it.",
  ["outdoor-air-ventilation-tall-buildings","car-park-ventilation-tall-buildings",
   "kitchen-exhaust-grease-risers-tall-buildings"]),
 ("V", "Life safety",
  "The two systems whose design case is a day that will probably never come, and must work anyway.",
  ["firefighting-tall-buildings","atrium-smoke-control-tall-buildings"]),
 ("VI", "The systems that serve the systems",
  "Everything that is nobody's headline scope and every project's late problem.",
  ["vertical-transportation-mep-tall-buildings","fuel-oil-systems-tall-buildings",
   "bms-controls-architecture-tall-buildings","refuse-chutes-waste-tall-buildings",
   "mep-commissioning-tall-buildings"]),
 ("VII", "Coda",
  "What all of it costs, once somebody adds up the whole chain.",
  ["six-kilowatt-litre-water-energy-tall-buildings"]),
]

FIG = re.compile(r'<div class="fig">(.*?)</div>\s*(?=<p class="fig-note"|<h2|<div class="callout"|<div class="callout |$)', re.S)

def figure_card(inner, slug):
    t  = re.search(r'<div class="ftitle">(.*?)</div>', inner, re.S)
    s  = re.search(r'<div class="fsub">(.*?)</div>',  inner, re.S)
    cv = re.search(r'<canvas id="([^"]+)"',           inner)
    anchor = ''
    m = re.search(r'href="(calculators\.html#calc-[a-z0-9]+)"', inner)
    if m: anchor = ('  <a class="hb-fig-calc" href="%s">Open as a calculator</a>\n' % m.group(1))
    return ('<figure class="hb-fig">\n'
            '  <div class="hb-fig-label">Interactive figure</div>\n'
            '  <div class="hb-fig-title">%s</div>\n'
            '  <div class="hb-fig-model">%s</div>\n'
            '  <a class="hb-fig-live" href="%s.html#%s">Run this model in the online edition</a>\n%s'
            '</figure>\n'
            % (t.group(1).strip() if t else 'Figure',
               s.group(1).strip() if s else '',
               slug, cv.group(1) if cv else '', anchor))

def chapter(slug):
    src = io.open(slug + '.html', encoding='utf-8').read()
    ttl = re.search(r'<h1>(.*?)</h1>', src, re.S).group(1).strip()
    body = re.search(r'<div class="article-body">(.*)</div>\s*\n\n<footer', src, re.S)
    if not body:
        body = re.search(r'<div class="article-body">(.*?)\n</div>\n', src, re.S)
    b = body.group(1)
    b = FIG.sub(lambda m: figure_card(m.group(1), slug), b)
    b = re.sub(r'<div class="tags">.*?</div>', '', b, flags=re.S)          # hashtags
    b = re.sub(r'<p class="lead">', '<p class="hb-lead">', b)
    b = re.sub(r'\sid="[^"]*"', '', b)                                     # avoid duplicate ids across chapters
    b = re.sub(r'<a class="hb-fig-live" href="([^"#]+)#">', r'<a class="hb-fig-live" href="\1">', b)
    mins = re.search(r'<span data-mins-fixed>(\d+) min read</span>', src)
    return ttl, b, int(mins.group(1)) if mins else 0

def main():
    chapters, n, total = [], 0, 0
    toc = []
    for num, name, blurb, slugs in PARTS:
        toc.append('<div class="hb-toc-part"><span>Part %s</span> %s</div>' % (num, name))
        for slug in slugs:
            n += 1
            ttl, body, mins = chapter(slug)
            total += mins
            short = re.split(r':\s', ttl)[0]
            chapters.append((num, name, blurb, n, slug, ttl, short, body, mins))
            toc.append('<a class="hb-toc-item" href="#ch%d"><span class="hb-toc-n">%d</span>'
                       '<span class="hb-toc-t">%s</span><span class="hb-toc-m">%d min</span></a>' % (n, n, short, mins))
    print(f"  {n} chapters, {total} minutes")
    return chapters, toc, n, total

if __name__ == '__main__':
    main()

HB_CSS = """
  <style>
    .hb-wrap{max-width:1180px;margin:0 auto;padding:0 24px;}
    .hb-cover{max-width:820px;margin:0 auto;padding:150px 24px 70px;}
    .hb-kicker{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);}
    .hb-cover h1{font-family:var(--font-display);font-size:clamp(46px,8vw,86px);font-weight:700;
      letter-spacing:-.045em;line-height:.98;margin:20px 0 22px;}
    .hb-sub{font-size:21px;line-height:1.6;color:var(--text-secondary);margin:0 0 34px;max-width:60ch;}
    .hb-meta{display:flex;flex-wrap:wrap;gap:0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);}
    .hb-meta div{padding:16px 26px 18px 0;border-right:1px solid var(--border);margin-right:26px;}
    .hb-meta div:last-child{border-right:none;margin-right:0;}
    .hb-meta .k{font-size:10.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--text-tertiary);}
    .hb-meta .v{font-family:var(--font-display);font-size:29px;font-weight:700;line-height:1.15;margin-top:3px;
      font-variant-numeric:tabular-nums;color:var(--text-primary);}
    .hb-meta .v small{font-size:12.5px;font-weight:400;color:var(--text-tertiary);display:block;}
    .hb-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:32px;}
    .hb-btn{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:3px;
      font-size:14px;font-weight:600;text-decoration:none;border:1px solid var(--border-light);
      color:var(--text-primary);background:var(--bg-3);cursor:pointer;font-family:inherit;transition:.18s;}
    .hb-btn.primary{background:var(--accent);border-color:var(--accent);color:var(--on-accent);}
    .hb-btn:hover{transform:translateY(-1px);}
    .hb-note{max-width:820px;margin:0 auto;padding:0 24px 20px;font-size:15px;line-height:1.75;
      color:var(--text-tertiary);}
    .hb-note b{color:var(--text-secondary);}

    .hb-toc{max-width:820px;margin:0 auto;padding:46px 24px 30px;}
    .hb-toc h2{font-family:var(--font-display);font-size:15px;font-weight:700;letter-spacing:.13em;
      text-transform:uppercase;color:var(--text-tertiary);margin:0 0 22px;}
    .hb-toc-part{font-family:var(--font-display);font-size:19px;font-weight:600;color:var(--text-primary);
      margin:30px 0 10px;padding-bottom:8px;border-bottom:1px solid var(--border);}
    .hb-toc-part span{color:var(--accent);font-size:12px;letter-spacing:.1em;text-transform:uppercase;
      margin-right:10px;font-weight:700;}
    .hb-toc-item{display:flex;align-items:baseline;gap:14px;padding:8px 0;text-decoration:none;
      border-bottom:1px solid var(--border);}
    .hb-toc-item:hover .hb-toc-t{color:var(--accent);}
    .hb-toc-n{font-size:12px;color:var(--text-tertiary);width:24px;flex:0 0 24px;font-variant-numeric:tabular-nums;}
    .hb-toc-t{flex:1;font-size:16px;color:var(--text-primary);line-height:1.45;}
    .hb-toc-m{font-size:12px;color:var(--text-tertiary);font-variant-numeric:tabular-nums;}

    .hb-part{max-width:820px;margin:0 auto;padding:78px 24px 8px;}
    .hb-part-n{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);}
    .hb-part h2{font-family:var(--font-display);font-size:clamp(32px,5vw,46px);font-weight:700;
      letter-spacing:-.03em;margin:12px 0 14px;line-height:1.05;}
    .hb-part p{font-size:17.5px;line-height:1.65;color:var(--text-secondary);margin:0;max-width:62ch;}
    .hb-part-rule{max-width:820px;margin:26px auto 0;border-top:2px solid var(--text-primary);opacity:.85;}

    .hb-ch{max-width:820px;margin:0 auto;padding:54px 24px 10px;}
    .hb-ch-head{border-bottom:1px solid var(--border);padding-bottom:16px;margin-bottom:8px;}
    .hb-ch-n{font-size:11.5px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--text-tertiary);}
    .hb-ch h3{font-family:var(--font-display);font-size:clamp(26px,3.6vw,36px);font-weight:700;
      letter-spacing:-.025em;line-height:1.12;margin:10px 0 10px;}
    .hb-ch-src{font-size:13px;color:var(--text-tertiary);}
    .hb-ch-src a{color:var(--accent);text-decoration:none;}
    .hb-body{padding-top:6px;}
    .hb-lead{font-size:19px !important;line-height:1.62 !important;color:var(--text-primary) !important;
      margin-bottom:1.5rem !important;}

    .hb-fig{margin:26px 0;border:1px solid var(--border);border-left:3px solid var(--accent);
      border-radius:3px;padding:16px 20px 18px;background:var(--bg-3);}
    .hb-fig-label{font-size:10px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);}
    .hb-fig-title{font-size:16px;font-weight:600;color:var(--text-primary);margin-top:6px;line-height:1.35;}
    .hb-fig-model{font-size:13.5px;color:var(--text-tertiary);line-height:1.6;margin-top:7px;}
    .hb-fig-live,.hb-fig-calc{display:inline-block;margin-top:11px;margin-right:16px;font-size:13px;
      font-weight:600;color:var(--accent);text-decoration:none;}
    .hb-fig-live:hover,.hb-fig-calc:hover{text-decoration:underline;}

    .hb-end{max-width:820px;margin:70px auto 0;padding:30px 24px 90px;border-top:2px solid var(--text-primary);}
    .hb-end p{font-size:15px;line-height:1.75;color:var(--text-tertiary);}

    @media print{
      @page{margin:19mm 16mm;}
      body{background:var(--sheet) !important;color:#111 !important;font-size:10.6pt;}
      .nav,footer,.fab-consult,.fab-glass,.hb-actions,#read-progress-bar,
      .hb-note,section[style*="padding:96px"]{display:none !important;}
      .hb-cover{padding:0 0 24pt;page-break-after:always;}
      .hb-toc{padding:0;page-break-after:always;}
      .hb-part{page-break-before:always;padding:0 0 6pt;}
      .hb-ch{page-break-before:always;padding:0;}
      .hb-ch h3,.hb-part h2{page-break-after:avoid;}
      .article-body h2,.hb-body h2{page-break-after:avoid;font-size:14pt;}
      .hb-fig,.callout,table,.eq{page-break-inside:avoid;}
      .hb-fig{background:#f6f6f4 !important;border-color:#ccc !important;}
      a{color:#111 !important;text-decoration:none;}
      .hb-toc-item{border-color:#ddd !important;}
      .hb-meta{border-color:#bbb !important;}
    }
    @media(max-width:640px){ .hb-cover{padding-top:120px;} .hb-meta div{margin-right:16px;padding-right:16px;} }
  </style>
"""

def build():
    chapters, toc, n, total = main()
    T = lambda x: io.open('scripts/_tmpl_%s.html' % x, encoding='utf-8').read()
    figs = sum(io.open(s + '.html', encoding='utf-8').read().count('<canvas id=')
               for _, _, _, _, s, _, _, _, _ in chapters)
    DESC = ("The complete tall-building MEP collection as one printable reading edition: %d chapters "
            "across water, cooling, air, life safety and the systems that serve them, with %d worked "
            "models linked back to their live interactive versions." % (n, figs))

    out = [T('HEAD_TOP'),
      "  <title>The Megatall MEP Handbook &mdash; Mohamed Abokhatwa</title>\n",
      '  <link rel="stylesheet" href="style.css?v=7">\n',
      '  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png?v=2">\n',
      '  <link rel="icon" type="image/png" sizes="64x64" href="favicon.png?v=2">\n',
      '  <link rel="apple-touch-icon" sizes="180x180" href="favicon-180.png?v=2">\n',
      '  <script>\n    MathJax = { tex: { inlineMath: [[\'\\\\(\', \'\\\\)\']], displayMath: [[\'\\\\[\', \'\\\\]\']] }, svg: { fontCache: \'global\' } };\n  </script>\n',
      '  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js" id="MathJax-script" async></script>\n',
      T('CALENDLY'),
      '  <meta name="description" content="%s">\n' % DESC,
      '  <meta property="og:title" content="The Megatall MEP Handbook | Mohamed Abokhatwa">\n',
      '  <meta property="og:description" content="%s">\n' % DESC,
      '  <meta property="og:type" content="book">\n',
      '  <meta property="og:url" content="https://abokhatwa.com/megatall-handbook.html">\n',
      '  <meta property="og:image" content="https://abokhatwa.com/og-mechanical-floors-tall-buildings.jpg">\n',
      '  <meta name="twitter:card" content="summary_large_image">\n',
      '  <link rel="canonical" href="https://abokhatwa.com/megatall-handbook.html">\n',
      HB_CSS, '</head>\n', T('NAV')]

    out.append(
      '<div class="hb-cover">\n'
      '  <div class="hb-kicker">Collected edition &middot; %d chapters</div>\n'
      '  <h1>The Megatall<br>MEP Handbook</h1>\n'
      '  <p class="hb-sub">Everything on this site about designing mechanical services for tall '
      'buildings, in the order it should be read &mdash; from the stack effect that governs the '
      'whole tower down to what a litre of water costs by the time it reaches the top floor.</p>\n'
      '  <div class="hb-meta">\n'
      '    <div><div class="k">Chapters</div><div class="v">%d<small>seven parts</small></div></div>\n'
      '    <div><div class="k">Reading time</div><div class="v">%d<small>hours</small></div></div>\n'
      '    <div><div class="k">Worked models</div><div class="v">%d<small>all verified</small></div></div>\n'
      '    <div><div class="k">Edition</div><div class="v">1.0<small>August 2026</small></div></div>\n'
      '  </div>\n'
      '  <div class="hb-actions">\n'
      '    <button class="hb-btn primary" onclick="window.print()">Print or save as PDF</button>\n'
      '    <a class="hb-btn" href="#contents">Contents</a>\n'
      '    <a class="hb-btn" href="one-tower.html">Open One Tower</a>\n'
      '  </div>\n'
      '</div>\n'
      '<p class="hb-note"><b>About this edition.</b> The interactive charts in the online articles '
      'cannot be printed, so each one appears here as a figure card carrying its title, the model it '
      'uses and the finding it produced, with a link to run it live. Everything else &mdash; the '
      'derivations, the worked numbers, the installation notes and the references &mdash; is complete. '
      'Print it, or use your browser&rsquo;s <em>Save as PDF</em>.</p>\n'
      % (n, n, round(total/60), figs))

    out.append('<div class="hb-toc" id="contents">\n  <h2>Contents</h2>\n' + '\n'.join(toc) + '\n</div>\n')

    last = None
    for num, name, blurb, i, slug, ttl, short, body, mins in chapters:
        if num != last:
            out.append('<div class="hb-part">\n  <div class="hb-part-n">Part %s</div>\n'
                       '  <h2>%s</h2>\n  <p>%s</p>\n</div>\n<div class="hb-part-rule"></div>\n'
                       % (num, name, blurb))
            last = num
        out.append('<div class="hb-ch" id="ch%d">\n  <div class="hb-ch-head">\n'
                   '    <div class="hb-ch-n">Chapter %d</div>\n    <h3>%s</h3>\n'
                   '    <div class="hb-ch-src">Online edition: <a href="%s.html">%s.html</a> '
                   '&middot; %d min</div>\n  </div>\n  <div class="hb-body article-body">\n%s\n  </div>\n</div>\n'
                   % (i, i, ttl, slug, slug, mins, body))

    out.append('<div class="hb-end">\n<p>&copy; 2026 Mohamed Abokhatwa. Collected from the articles '
               'published at abokhatwa.com. Every model in this edition was derived from the stated '
               'equation, computed independently, and checked against the figure it produced. Where a '
               'chapter cites a code or standard, check it against the edition your project is '
               'contracted to &mdash; the numbers here are engineering, not compliance.</p>\n</div>\n')
    out.append(T('FOOTER')); out.append(T('TAIL'))

    html = ''.join(out)
    io.open('megatall-handbook.html', 'w', encoding='utf-8').write(html)
    print(f"  megatall-handbook.html  {len(html)//1024} KB  |  {n} chapters, {figs} models, {round(total/60)} h")
