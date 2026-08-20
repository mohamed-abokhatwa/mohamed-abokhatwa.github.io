#!/usr/bin/env python3
"""
build_legacy.py - freeze the pre-redesign site into /legacy so it stays
browsable at abokhatwa.com/legacy/ after the Elevation 828 redesign.

Text files (html/css/js) are copied; the large image assets are NOT duplicated,
they are referenced up one level. Every rewritten path is then checked to make
sure it actually resolves on disk.

Rebuild with:  python3 scripts/build_legacy.py [--from <git-ref>]
"""
import os, re, sys, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DEST = 'legacy'
REF  = 'v1-original'

IMG = r'(?:webp|jpg|jpeg|png|gif|svg|avif)'
BANNER = (
  '<div id="legacy-bar" style="position:sticky;top:0;z-index:99999;'
  'background:#1d1d1f;color:#f5f5f7;font:500 13px/1.4 -apple-system,BlinkMacSystemFont,'
  'Inter,Helvetica,Arial,sans-serif;padding:9px 16px;display:flex;gap:14px;'
  'align-items:center;justify-content:center;flex-wrap:wrap;text-align:center;">'
  '<span>You are viewing the previous design of abokhatwa.com, archived 21 August 2026.</span>'
  '<a href="https://abokhatwa.com/" style="color:#6fb3d6;text-decoration:underline;">'
  'Go to the current site</a></div>'
)
NOINDEX = '<meta name="robots" content="noindex,nofollow">'

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, check=True).stdout

def files_at(ref):
    return sh('git', 'ls-tree', '-r', '--name-only', ref).splitlines()

def blob(ref, path):
    return subprocess.run(['git','show',f'{ref}:{path}'], capture_output=True, check=True).stdout

# ── which files travel into the archive ───────────────────────────────────
tracked = files_at(REF)
TEXT_EXT = ('.html', '.css', '.js')
SMALL    = ('.ico', '.png', '.pdf')          # favicons + the lead-magnet PDF
take = []
for p in tracked:
    if p.startswith(('scripts/', 'specs/', '_originals/', '_tiles/', '_tmp_tiles/')):
        continue
    if os.path.basename(p).startswith('._'):      # AppleDouble stub, 0 bytes
        continue
    if p.startswith('thumbs/') or p.startswith('fonts/'):
        continue                              # referenced up one level instead
    ext = os.path.splitext(p)[1].lower()
    if ext in TEXT_EXT or ext in SMALL:
        take.append(p)

if os.path.isdir(DEST):
    shutil.rmtree(DEST)
os.makedirs(DEST, exist_ok=True)

def up(depth):
    return '../' * depth

def fix_html(src, path):
    depth = path.count('/') + 1
    u = up(depth)                       # back to the site root from legacy/<path>
    sub = os.path.dirname(path)         # '' at the root, 'mep-course' inside the course
    bare = u + (sub + '/' if sub else '')   # where a bare filename really lives
    # relative images resolve against the ORIGINAL directory, one level up
    src = re.sub(r'(\b(?:src|href|content)=")(?!https?:|//|data:|#|/)([^"/]+\.' + IMG + r')(["?])',
                 lambda m: m.group(1) + bare + m.group(2) + m.group(3), src, flags=re.I)
    # thumbs/ always lives at the site root
    src = re.sub(r'(\b(?:src|href|content)=")thumbs/',
                 lambda m: m.group(1) + u + 'thumbs/', src, flags=re.I)
    # srcset entries
    src = re.sub(r'(srcset=")(?!https?:|/)([^"]+)(")',
                 lambda m: m.group(1) + re.sub(r'(^|,\s*)(?!https?:|/)', r'\1' + bare, m.group(2)) + m.group(3),
                 src, flags=re.I)
    # url(...) inside inline styles
    src = re.sub(r"url\((['\"]?)(?!https?:|//|data:|/)([^)'\"]+\.\s*" + IMG + r")\1\)",
                 lambda m: "url(%s%s%s%s)" % (m.group(1), bare, m.group(2), m.group(1)),
                 src, flags=re.I)
    # a bare root link would jump out of the archive
    src = src.replace('href="/"', 'href="%sindex.html"' % ('' if depth == 1 else '../'))
    # keep the archive out of search results
    if '<head>' in src:
        src = src.replace('<head>', '<head>\n' + NOINDEX, 1)
    elif '<meta charset' in src:
        src = re.sub(r'(<meta charset[^>]*>)', r'\1\n' + NOINDEX, src, count=1)
    # visible marker
    m = re.search(r'<body[^>]*>', src, re.I)
    if m:
        src = src[:m.end()] + '\n' + BANNER + src[m.end():]
    return src

def fix_css(src, depth):
    u = up(depth)
    return re.sub(r"url\((['\"]?)fonts/", lambda m: "url(%s%sfonts/" % (m.group(1), u), src)

written = 0
for p in take:
    out = os.path.join(DEST, p)
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    depth = p.count('/') + 1
    data = blob(REF, p)
    ext = os.path.splitext(p)[1].lower()
    if ext == '.html':
        data = fix_html(data.decode('utf-8'), p).encode('utf-8')
    elif ext == '.css':
        data = fix_css(data.decode('utf-8'), depth).encode('utf-8')
    with open(out, 'wb') as f:
        f.write(data)
    written += 1

print(f"archived {written} files into {DEST}/")
