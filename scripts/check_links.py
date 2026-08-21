#!/usr/bin/env python3
"""check_links.py — every local href/src on the live site must resolve."""
import os, re, sys, glob
from urllib.parse import unquote
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)

REF = re.compile(r'\b(?:src|href)="([^"]+)"|url\((["\']?)([^)"\']+)\2\)', re.I)
SKIP = ('http:', 'https:', '//', 'data:', 'mailto:', 'tel:', '#', 'javascript:')
pages = [f for f in glob.glob('*.html') if not os.path.basename(f).startswith('._')]
pages += glob.glob('mep-course/*.html') + glob.glob('mep-course/assets/*.css') + ['style.css']

bad, checked = [], 0
for f in pages:
    base = os.path.dirname(f)
    txt = open(f, encoding='utf-8', errors='replace').read()
    for m in REF.finditer(txt):
        raw = m.group(1) or m.group(3)
        if not raw or raw.startswith(SKIP): continue
        if any(t in raw for t in ("'+", '"+', '${', '+r.', '+link')): continue
        path = unquote(raw.split('#')[0].split('?')[0])
        if not path: continue
        target = os.path.normpath(os.path.join(base, path.lstrip('/') if path.startswith('/') else path))
        checked += 1
        if os.path.exists(target) or os.path.isdir(target) or os.path.exists(os.path.join(target, 'index.html')):
            continue
        bad.append((f, raw, target))

print(f"local references checked : {checked}")
print(f"broken                   : {len(bad)}")
seen = set()
for f, raw, t in bad:
    if (raw, t) in seen: continue
    seen.add((raw, t))
    print(f"  x {f}\n      {raw}  ->  {t}")
    if len(seen) > 30: print('  ...'); break
sys.exit(1 if bad else 0)
