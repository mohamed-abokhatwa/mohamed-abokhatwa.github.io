#!/usr/bin/env python3
"""
check-articles.py — keep the article counts in sync, automatically.

Verifies that, across the site, the number of articles agrees everywhere:
  1. real article files on disk (pages containing an article body)
  2. the ARTICLES registry in article-features.js  (powers "related articles")
  3. the article cards in index.html and index-ar.html
  4. the "Browse by topic" category-count chips, per category, in both indexes

Exits 0 when everything matches, 1 (with a report) when anything drifts.
Run manually:   python3 scripts/check-articles.py
Runs automatically on every commit via .git/hooks/pre-commit.
"""
import re, sys, os, glob
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

def read(f):
    with open(f, encoding="utf-8") as fh:
        return fh.read()

# 1) real article files = pages that contain an article body
disk = sorted(f for f in glob.glob("*.html") if 'class="article-body"' in read(f))

# 2) registry urls
reg = sorted(re.findall(r"url:'([^']+)'", read("article-features.js")))

fail = []
print(f"articles on disk : {len(disk)}")
print(f"registry entries : {len(reg)}")

if set(reg) != set(disk):
    fail.append("registry out of sync with disk")
    for m in sorted(set(disk) - set(reg)):
        print(f"  ✗ missing from article-features.js: {m}")
    for m in sorted(set(reg) - set(disk)):
        print(f"  ✗ stale entry in article-features.js: {m}")

# 3) + 4) per index: grid cards (per category) vs category-count chips
for idx in ("index.html", "index-ar.html"):
    html = read(idx)
    grid = Counter(re.findall(
        r'<a href="[^"]+\.html" class="article-card[^"]*" data-cat="([a-z]+)"', html))
    total = sum(grid.values())
    chips = {cat: int(num) for cat, num in (
        (c, n.translate(AR_DIGITS)) for c, n in re.findall(
            r'class="cat-card"\s+data-cat="([a-z]+)".*?cat-card-count">\s*([0-9٠-٩]+)',
            html, re.S))}
    print(f"{idx:14s}: {total} grid cards, chips total {sum(chips.values())} {dict(sorted(chips.items()))}")

    if total != len(disk):
        fail.append(f"{idx}: {total} grid cards != {len(disk)} articles on disk")
    for cat, n in sorted(grid.items()):
        if chips.get(cat) != n:
            fail.append(f"{idx}: category '{cat}' chip={chips.get(cat)} but grid has {n}")
            print(f"  ✗ {idx}: '{cat}' chip says {chips.get(cat)}, grid has {n}")
    for cat in sorted(set(chips) - set(grid)):
        fail.append(f"{idx}: chip '{cat}'={chips[cat]} has no matching grid cards")
        print(f"  ✗ {idx}: chip '{cat}' has no articles in the grid")

if fail:
    print(f"\nFAIL — {len(fail)} issue(s); fix before committing.")
    sys.exit(1)
print(f"\n✓ all counts consistent — {len(disk)} articles everywhere.")
sys.exit(0)
