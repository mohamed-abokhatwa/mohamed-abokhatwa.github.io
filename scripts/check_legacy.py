#!/usr/bin/env python3
"""Verify every local reference inside legacy/ resolves to a real file."""
import os, re, sys, glob
from urllib.parse import unquote
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)

REF = re.compile(r'\b(?:src|href)="([^"]+)"|url\((["\']?)([^)"\']+)\2\)', re.I)
bad, checked = [], 0
for f in glob.glob('legacy/**/*.html', recursive=True) + glob.glob('legacy/**/*.css', recursive=True):
    base = os.path.dirname(f)
    txt = open(f, encoding='utf-8', errors='replace').read()
    for m in REF.finditer(txt):
        raw = m.group(1) or m.group(3)
        if not raw: continue
        if any(tok in raw for tok in ("'+", '"+', '${', '+r.', '+link')): continue
        if raw.startswith(('http:', 'https:', '//', 'data:', 'mailto:', 'tel:', '#', 'javascript:')):
            continue
        path = unquote(raw.split('#')[0].split('?')[0])
        if not path: continue
        target = os.path.normpath(os.path.join(base, path))
        checked += 1
        if target.endswith('/') or os.path.isdir(target):
            continue
        if not os.path.exists(target):
            if os.path.isdir(target.rstrip('/')) or os.path.exists(target + 'index.html'):
                continue
            bad.append((f, raw, target))

print(f"local references checked : {checked}")
print(f"broken                   : {len(bad)}")
seen = set()
for f, raw, t in bad:
    k = (raw, t)
    if k in seen: continue
    seen.add(k)
    print(f"  x {f}\n      {raw}  ->  {t}")
    if len(seen) > 25:
        print(f"  ... and {len(bad)-len(seen)} more"); break
sys.exit(1 if bad else 0)
