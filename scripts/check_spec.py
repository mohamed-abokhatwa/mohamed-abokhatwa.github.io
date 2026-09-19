#!/usr/bin/env python3
"""check_spec.py — structural, link and runtime checks for an article spec (scripts/gen_article.py input).

usage (repo root): python3 scripts/check_spec.py specs/s01_wave_speed.py

Imports the spec, checks the SPEC fields, the body markup, ids, internal links, references and
citations, and then executes the chart JavaScript against a stubbed DOM in node, exercising every
control at its min, max and every select option. Exit 0 = no FAIL lines.
Deeper output checking (what the charts actually draw) is scripts/chart_probe.py.
"""
import sys, os, re, json, html, subprocess, importlib.util, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SURGE7 = ['wave-speed-surge-analysis', 'surge-vessel-differential-orifice', 'surge-vessel-type-selection',
          'one-way-surge-tank-design', 'surge-relief-valve-sizing', 'pump-inertia-flywheel-surge',
          'choosing-surge-protection']
fails, warns, info = [], [], []
def F(m): fails.append(m)
def W(m): warns.append(m)

path = sys.argv[1]
sp = importlib.util.spec_from_file_location('specmod', path)
mod = importlib.util.module_from_spec(sp)
try:
    sp.loader.exec_module(mod)
except Exception as e:
    print('FAIL: spec does not import:', repr(e)); sys.exit(1)
S = getattr(mod, 'SPEC', None)
if not isinstance(S, dict):
    print('FAIL: no SPEC dict'); sys.exit(1)

REQ = ['slug','cat','mins','date_iso','date_human','date_ar','title','reg_title','reg_tag','breadcrumb','tag_line',
       'desc','og_desc','ld_desc','img_alt','en_tag','en_title','en_excerpt','en_search','ar_title','ar_excerpt',
       'ar_search','body','charts']
for k in REQ:
    if k not in S or S[k] in (None, ''): F(f'missing SPEC field {k}')
for k in ('ar_title','ar_excerpt','ar_search'):
    if not re.search('[؀-ۿ]', S.get(k,'')): F(f'{k} has no Arabic')
for k in ('title','reg_title','reg_tag','desc','og_desc','ld_desc','img_alt','en_title','ar_title'):
    v = S.get(k,'')
    if '"' in v: F(f'{k} contains a double quote (breaks JSON-LD/attributes)')
    if "\\" in v: F(f'{k} contains a backslash')
if "'" in S.get('reg_tag',''): F("reg_tag contains a single quote")
body, charts = S.get('body',''), S.get('charts','')
surge = S.get('slug') in SURGE7

# ---- body structure
if '<p class="lead">' not in body: F('no <p class="lead">')
if '<h1' in body: F('body must not contain <h1>')
h2 = re.findall(r'<h2 id="([^"]+)">([^<]*)</h2>', body)
numbered = [int(m.group(1)) for m in (re.match(r'\s*(\d+)\s*&middot;', t) for i, t in h2) if m]
if numbered != list(range(1, len(numbered)+1)): F(f'h2 numbering not sequential: {numbered}')
if 'id="refs"' not in body or '<ol class="refs">' not in body: F('references block missing')
if '<div class="tags">' not in body: F('tags block missing')
ids = re.findall(r'\sid="([^"]+)"', body)
dup = sorted({i for i in ids if ids.count(i) > 1})
if dup: F(f'duplicate ids: {dup}')
if body.count('<div class="fig">') < 3: F(f'fewer than 3 interactive figures ({body.count(chr(60) + "div class=" + chr(34) + "fig" + chr(34) + chr(62))})')
for tag in ('div','p','ul','ol','li','table','tr','td','th','span','strong','em','a','h2','h3','select','option','label','svg'):
    o = len(re.findall(rf'<{tag}[\s>]', body)); c = body.count(f'</{tag}>')
    if o != c: F(f'unbalanced <{tag}>: {o} open vs {c} close')
if body.count('\\[') != body.count('\\]'): F('unbalanced \\[ \\]')
if body.count('\\(') != body.count('\\)'): F('unbalanced \\( \\)')
nrefs = len(re.findall(r'<li>', body[body.find('<ol class="refs">'):body.find('</ol>', body.find('<ol class="refs">'))]))
cites = [int(x) for grp in re.findall(r'\[(\d+(?:\s*[,&ndash;–-]+\s*\d+)*)\]', re.sub(r'\\\[.*?\\\]', '', body, flags=re.S)) for x in re.findall(r'\d+', grp)]
bad = sorted({c for c in cites if c < 1 or c > nrefs})
if bad: F(f'citations beyond reference list ({nrefs} refs): {bad}')
uncited = sorted(set(range(1, nrefs+1)) - set(cites))
if uncited: W(f'references never cited in text: {uncited}')

txt = html.unescape(re.sub(r'<[^>]+>', ' ', body))
if surge:
    for pat, why in ((r'1\.84\s*bar', '1.84 bar pre-charge (superseded)'),
                     (r'\b8\.0\s*m\s*(³|3)\b', '8.0 m³ vessel (superseded)'),
                     (r'217\.5|200\.9|176\.9|138\.4|120\.6', 'superseded unprotected maxima (pre-audit solver)'),
                     (r'137\.9|152\.3|149\.8', 'superseded relief-valve maxima'),
                     (r'0\.689|0\.413\b', 'superseded relief flow'),
                     (r'\b813\b|\b939\b|\b487\b|\b563\b', 'superseded Kv/Cv'),
                     (r'116\.5', 'old SRV pump max 116.5 (superseded)'),
                     (r'\b18\.9\s*m|\b16\.3\s*m|36\.2|\b24\.2\b', 'superseded bladder shell volumes'),
                     (r'\b3\.04\b|15\.25', 'superseded gas volumes (use 3.08 / 15.30)'),
                     (r'62\.7|\b20\.9\b|\b39\.0\s*m', 'superseded one-way tank numbers'),
                     (r'0\.468|0\.234\b|0\.117\b', 'superseded compressor FAD'),
                     (r'\b9\.25\b|8\.86|\b1\.57\b|17\.79', 'superseded flywheel minima'),
                     (r'lorem|TODO|TBD|XXX', 'placeholder text')):
        if re.search(pat, txt, re.I): F(f'banned: {why}')
words = len(re.sub(r'\\\[.*?\\\]', ' ', txt, flags=re.S).split())
info.append(f'words {words}, mins given {S.get("mins")}, suggested {round(words/200)}')
if words < 2000: W(f'body is short ({words} words)')

for href in re.findall(r'href="([^"#]+)(?:#[^"]*)?"', body + S.get('en_excerpt','')):
    if href.startswith(('http://','https://','mailto:')): continue
    base = href.split('?')[0]
    if base.endswith('.html') and not os.path.exists(base) and base[:-5] not in SURGE7:
        F(f'broken internal link {href}')
    if S.get('slug') and base == S['slug'] + '.html': W('links to itself')
for href in re.findall(r'href="(https?://[^"]+)"', body):
    W(f'external link (check it is real): {href}')

# ---- charts
if '__DATA__' in charts: F('__DATA__ placeholder not substituted')
used = set(re.findall(r"getElementById\(\s*'([^']+)'\s*\)", charts)) | set(re.findall(r'getElementById\(\s*"([^"]+)"\s*\)', charts))
missing = sorted(u for u in used if u not in ids)
if missing: F(f'charts reference ids not in body: {missing}')
canv = re.findall(r'<canvas id="([^"]+)"', body)
for c in canv:
    if c not in used: F(f'canvas {c} never used by charts')
for i in re.findall(r'<(?:input|select)[^>]*\sid="([^"]+)"', body):
    if i not in used: W(f'control {i} not read by charts')
if "window.addEventListener('load'" not in charts: W('no load->resize handler')
info.append(f'charts JS {len(charts)//1024} KB')

elems = {}
for m in re.finditer(r'<(input|select|canvas|span|div|td|strong|b|p)\b([^>]*)\sid="([^"]+)"([^>]*)>', body):
    tag, a1, i, a2 = m.groups(); attrs = a1 + a2
    val = re.search(r'\svalue="([^"]*)"', attrs)
    if tag == 'select':
        seg = body[m.end(): body.find('</select>', m.end())]
        opts = re.findall(r'<option[^>]*value="([^"]*)"([^>]*)>', seg)
        sel = [v for v, rest in opts if 'selected' in rest]
        v = sel[0] if sel else (opts[0][0] if opts else '')
    else:
        v = val.group(1) if val else ''
    typ = re.search(r'\stype="([^"]*)"', attrs)
    elems[i] = dict(tag=tag, value=v, type=typ.group(1) if typ else '',
                    checked=bool(re.search(r'\schecked\b', attrs)),
                    min=(re.search(r'\smin="([^"]*)"', attrs) or [None, None])[1],
                    max=(re.search(r'\smax="([^"]*)"', attrs) or [None, None])[1],
                    options=(re.findall(r'<option[^>]*value="([^"]*)"', body[m.end(): body.find('</select>', m.end())]) if tag == 'select' else []))
harness = r"""
const ELEMS = %s;
const listeners = [];
function mkEl(id){
  const d = ELEMS[id] || {tag:'div',value:'',type:'',checked:false,options:[]};
  const el = {id, tagName:d.tag.toUpperCase(), value:d.value, checked:d.checked, type:d.type,
    _d:d, style:{}, dataset:{}, classList:{add(){},remove(){},toggle(){},contains(){return false}},
    textContent:'', innerHTML:'', innerText:'', title:'', disabled:false,
    options: d.options.map(v=>({value:v})), selectedIndex: 0,
    setAttribute(){}, getAttribute(){return null}, appendChild(){}, querySelector(){return null}, querySelectorAll(){return []},
    getContext(){return {}}, parentElement:null, closest(){return null},
    addEventListener(ev, fn){ listeners.push([this, ev, fn]); } };
  return el;
}
const cache = {};
global.window = global; global.devicePixelRatio = 1;
global.document = { getElementById(id){ if(!(id in ELEMS)) throw new Error('getElementById missing #'+id); return cache[id] || (cache[id]=mkEl(id)); },
  querySelector(){return null}, querySelectorAll(){return []}, addEventListener(){}, documentElement:{getAttribute(){return null}, dataset:{}},
  body:{classList:{contains(){return false}}}, createElement(){ return mkEl('__tmp'); } };
global.addEventListener = function(){};
global.matchMedia = ()=>({matches:false, addEventListener(){}});
global.getComputedStyle = ()=>({getPropertyValue(){return ''}});
global.requestAnimationFrame = fn => 0;
const charts = [];
function checkData(cfg, where){
  (cfg.data && cfg.data.datasets || []).forEach((ds, k) => {
    (ds.data || []).forEach((p, j) => {
      const vals = (p && typeof p === 'object') ? [p.x, p.y] : [p];
      vals.forEach(v => { if (v !== null && v !== undefined && typeof v === 'number' && !isFinite(v)) throw new Error(`non-finite value in ${where} dataset ${k} point ${j}`); });
    });
  });
}
global.Chart = function(canvas, cfg){
  if (!cfg || !(cfg.type || (cfg.data && (cfg.data.datasets||[]).every(d=>d.type)))) throw new Error('Chart without type');
  this.config = cfg; this.data = cfg.data; this.options = cfg.options || {};
  this.update = () => checkData(this, canvas.id);
  this.resize = () => {}; this.destroy = () => {};
  charts.push(this);
};
global.Chart.register = () => {};
global.Chart.defaults = {font:{}, plugins:{legend:{labels:{}}, tooltip:{}}, scale:{grid:{}, ticks:{}}, color:''};
try {
%s
} catch (e) { console.log('RUNTIME-FAIL initial: ' + e.stack.split('\n').slice(0,3).join(' | ')); process.exit(3); }
let n = 0;
for (const [el, ev, fn] of listeners) {
  const d = el._d || {};
  const trials = d.tag === 'select' ? d.options : (d.type === 'checkbox' ? [true, false] : [d.min, d.max, d.value].filter(v => v !== null && v !== undefined));
  for (const v of trials) {
    if (d.type === 'checkbox') el.checked = v; else el.value = String(v);
    try { fn.call(el, {target: el}); n++; } catch (e) { console.log(`RUNTIME-FAIL on #${el.id}=${v}: ` + e.stack.split('\n').slice(0,3).join(' | ')); process.exit(3); }
  }
  if (d.tag !== 'select' && d.type !== 'checkbox') el.value = d.value;
  try { fn.call(el, {target: el}); } catch (e) {}
}
charts.forEach(c => checkData(c, 'final'));
console.log(`RUNTIME-OK charts=${charts.length} listeners=${listeners.length} calls=${n}`);
""" % (json.dumps(elems), charts)
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as fh:
    fh.write(harness); tmp = fh.name
r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
if r.returncode: F('node --check: ' + (r.stderr.strip().splitlines() or [''])[-1][:300])
else:
    r = subprocess.run(['node', tmp], capture_output=True, text=True, timeout=120)
    out = (r.stdout + r.stderr).strip()
    if 'RUNTIME-OK' in out:
        info.append(out.splitlines()[-1])
        m = re.search(r'charts=(\d+)', out)
        if m and int(m.group(1)) < 3: F(f'only {m.group(1)} Chart instances created')
    else:
        F(out[-600:])
os.unlink(tmp)

for m in info: print('INFO:', m)
for m in warns: print('WARN:', m)
for m in fails: print('FAIL:', m)
print('RESULT:', 'PASS' if not fails else f'{len(fails)} FAIL')
sys.exit(1 if fails else 0)
