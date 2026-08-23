#!/usr/bin/env python3
"""
grade_photos.py - bring the site's photography onto the Elevation 828 palette.

The card thumbnails are LinkedIn infographics: bold gradients, glows, blue and
orange badges. A colour grade will not reconcile that with a mylar drawing
sheet, so the small images are mapped onto a two-colour ramp instead - ink to
mylar - which turns each one into a tonal plate that belongs to the drawing
set. The full-size hero on the article page is left in colour, because there
the diagram's blue-for-water and orange-for-hot carry meaning.

  python3 scripts/grade_photos.py thumbs/*.webp profile.jpg
  python3 scripts/grade_photos.py --check thumbs/x.webp     # writes nothing

Reversible: every input is tracked in git.
"""
import sys, os, argparse
from PIL import Image, ImageEnhance, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

INK      = (12, 26, 24)      # the palette's near-black, green-biased
MYLAR    = (233, 238, 236)   # the sheet
SAT_KEEP = 0.22              # how much of the original colour survives
STRENGTH = 0.86              # how far toward the plate

def plate(im):
    im = im.convert('RGB')
    duo  = ImageOps.colorize(ImageOps.grayscale(im), INK, MYLAR)
    base = ImageEnhance.Color(im).enhance(SAT_KEEP)
    return Image.blend(base, duo, STRENGTH)

def save_like(im, path):
    ext = os.path.splitext(path)[1].lower()
    if ext == '.webp':
        im.save(path, 'WEBP', quality=88, method=6)
    elif ext in ('.jpg', '.jpeg'):
        im.save(path, 'JPEG', quality=90, optimize=True, progressive=True)
    else:
        im.save(path)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('paths', nargs='+')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    tb = ta = 0; n = 0
    for p in a.paths:
        if not os.path.exists(p):
            print('  missing', p); continue
        b = os.path.getsize(p)
        im = plate(Image.open(p))
        if not a.check:
            save_like(im, p)
        af = os.path.getsize(p)
        tb += b; ta += af; n += 1
    print(f'  {n} files   {tb/1024:.0f} KB -> {ta/1024:.0f} KB')
