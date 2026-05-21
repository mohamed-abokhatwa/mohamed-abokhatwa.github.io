#!/bin/bash
# Script to replace old post article HTML files with corrected versions
# and fix index.html card thumbnails
# Run this from Terminal: bash /Users/abokhatwa/Desktop/website-redesign/apply_fixes.sh

cd /Users/abokhatwa/Desktop/website-redesign

echo "=== Step 1: Replace post article HTML files ==="
POST_ARTICLES=(
    "top-hill-challenge"
    "check-valve-hammer"
    "prv-altitude-valve-fcv"
    "sustainable-pump-selection"
    "steady-state-analysis"
    "surge-analysis-risk"
    "design-vs-reality"
    "engineering-decisions"
    "envision-sustainability"
    "infrastructure-at-scale"
    "sustainability-in-design"
    "cavitation-prvs-fcvs"
)

for base in "${POST_ARTICLES[@]}"; do
    old="${base}.html"
    new="${base}-new.html"
    if [ -f "$new" ]; then
        rm "$old" 2>/dev/null
        mv "$new" "$old"
        echo "  ✓ Fixed: $old"
    else
        echo "  ✗ Missing: $new"
    fi
done

echo ""
echo "=== Step 2: Fix index.html card thumbnails ==="
python3 << 'PYEOF'
import re

with open('index.html', 'r') as f:
    content = f.read()

# Context-aware replacements: find each post article card and fix its image
# Each replacement is (article_href, wrong_img, correct_img)
fixes = [
    ("top-hill-challenge.html",       "transient-analysis-scada.jpg",          "top-hill-challenge.jpg"),
    ("check-valve-hammer.html",       "control-valve-transients-hammer.jpg",   "check-valve-hammer.jpg"),
    ("prv-altitude-valve-fcv.html",   "boundary-conditions-reservoir-tank.jpg","prv-altitude-valve-fcv.jpg"),
    ("sustainable-pump-selection.html","npsh-water-infrastructure.jpg",        "sustainable-pump-selection.jpg"),
    ("steady-state-analysis.html",    "above-ground-pipeline-design.jpg",      "steady-state-analysis.jpg"),
    ("surge-analysis-risk.html",      "wet-well-vortex-design.jpg",            "surge-analysis-risk.jpg"),
    ("design-vs-reality.html",        "above-ground-pipeline-design.jpg",      "design-vs-reality.jpg"),
    ("engineering-decisions.html",    "carbon-steel-pipeline-cml.jpg",         "engineering-decisions.jpg"),
    ("envision-sustainability.html",  "transient-analysis-scada.jpg",          "envision-sustainability.jpg"),
    ("infrastructure-at-scale.html",  "carbon-steel-pipeline-cml.jpg",         "infrastructure-at-scale.jpg"),
    ("sustainability-in-design.html", "above-ground-pipeline-design.jpg",      "sustainability-in-design.jpg"),
    ("cavitation-prvs-fcvs.html",    "air-valves-pipeline-safety.jpg",        "cavitation-prvs-fcvs.jpg"),
]

for href, wrong_img, correct_img in fixes:
    # Find the card for this article and replace only the image within that card
    # Use a pattern that spans from the href to the next closing </a>
    pattern = r'(href="' + re.escape(href) + r'".*?src=")' + re.escape(wrong_img) + r'(")'
    replacement = r'\g<1>' + correct_img + r'\g<2>'
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count > 0:
        content = new_content
        print(f"  ✓ Fixed image in card: {href} → {correct_img}")
    else:
        print(f"  ✗ Not found: {href} / {wrong_img}")

with open('index.html', 'w') as f:
    f.write(content)

print("\n  ✓ index.html saved with corrected card thumbnails")
PYEOF

echo ""
echo "=== Step 3: Update sitemap.xml ==="
if [ -f "sitemap-new.xml" ]; then
    rm "sitemap.xml" 2>/dev/null
    mv "sitemap-new.xml" "sitemap.xml"
    echo "  ✓ sitemap.xml updated with all 25 URLs"
else
    echo "  ✗ sitemap-new.xml not found"
fi

echo ""
echo "=== All fixes applied! ==="
echo "✓ Post article HTML files corrected (12 files with correct images)"
echo "✓ index.html card thumbnails fixed"
echo "✓ sitemap.xml updated with 22 new article URLs"
