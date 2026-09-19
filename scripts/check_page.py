#!/usr/bin/env python3
"""check_page.py — checks for the two hand-maintained vessel articles (surge-vessel.html,
pre-charge-pressure.html), which are edited in place rather than generated from a spec.

usage (repo root): python3 scripts/check_page.py surge-vessel.html

Validates the JSON-LD, the markup balance inside the article body, internal links, chart ids, and
runs the page's chart JavaScript against a stubbed DOM in node. Superseded figures from the
pre-2026-09 versions are allowed only inside the dated correction note.
"""
import sys, os, re, json, html, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
f = sys.argv[1]
s = open(f, encoding='utf-8').read()
fails, warns, info = [], [], []
F, W = fails.append, warns.append

a = s.find('<div class="article-body"'); b = s.find('<footer', a)
if a < 0 or b < 0: F('article-body or footer not found'); body = s
else: body = s[a:b]

for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, flags=re.S):
    try: json.loads(m.group(1))
    except Exception as e: F(f'JSON-LD does not parse: {e}')

for tag in ('div', 'p', 'ul', 'ol', 'li', 'table', 'thead', 'tbody', 'tr', 'td', 'th', 'span', 'strong', 'em', 'a', 'h2', 'h3', 'h4', 'canvas', 'select', 'label'):
    o = len(re.findall(rf'<{tag}[\s>]', body)); c = body.count(f'</{tag}>')
    if o != c: F(f'unbalanced <{tag}> in article body: {o} open vs {c} close')

note = re.search(r'<div class="[^"]*correction-note[^"]*"[^>]*>.*?</div>', body, flags=re.S)
if not note: W('no correction note (<div class="callout correction-note">) found')
scan = body.replace(note.group(0), '') if note else body
scan = re.sub(r'<script.*?</script>', '', scan, flags=re.S)
txt = html.unescape(re.sub(r'<[^>]+>', ' ', scan))
for pat, why in ((r'1\.84\s*bar', '1.84 bar outside the correction note'),
                 (r'217\.5|200\.9', 'superseded unprotected maximum'),
                 (r'128\.6|141\.2|168\.4', 'superseded iteration values'),
                 (r'\b3\.04\b|15\.25', 'superseded gas volumes (use 3.08 / 15.30)'),
                 (r'\b8\.0\s*m\s*(³|3)\b', '8.0 m³ vessel outside the correction note'),
                 (r'46\s*%', 'old 46 % penalty claim'), (r'Skulovich', 'unvetted reference'),
                 (r'steady-state mismatch warning', 'unverifiable HAMMER warning claim'),
                 (r'lorem|TODO|TBD|XXX', 'placeholder')):
    if re.search(pat, txt, re.I): F(f'banned: {why}')
for m in re.finditer(r'[−–-]\s?(\d{1,3}(?:\.\d+)?)\s*m\b', txt):
    v = float(m.group(1))
    ctx = txt[max(0, m.start()-40):m.end()+10].replace('\n', ' ')
    if v > 9.85 and not re.search(r'(km|chainage|downstream|upstream|elevation|\d\s*m\s*[−–-])', ctx):
        W(f'possible sub-vapour pressure −{v} m: "…{ctx}…"')
for m in re.finditer(r'HAMMER[^<\n]{0,60}(Results|Scenario|Iteration|Summary|Settings)', html.unescape(re.sub(r'<[^>]+>', ' ', body))):
    W(f'check wording — may present model results as HAMMER output: "{m.group(0)}"')

for href in re.findall(r'href="([^"#:]+\.html)(?:#[^"]*)?"', body):
    if not os.path.exists(href.split('?')[0]):
        F(f'broken internal link {href}')

ids = re.findall(r'\sid="([^"]+)"', s)
dup = sorted({i for i in ids if ids.count(i) > 1})
if dup: F(f'duplicate ids: {dup}')
chart_js = '\n'.join(m.group(1) for m in re.finditer(r'<script>(.*?)</script>', s, flags=re.S) if 'new Chart' in m.group(1))
canv = re.findall(r'<canvas id="([^"]+)"', s)
info.append(f'canvases {canv}, chart JS {len(chart_js)//1024} KB')
if not chart_js: F('no chart script found')
used = set(re.findall(r"getElementById\(\s*['\"]([^'\"]+)['\"]\s*\)", chart_js))
for u in used:
    if u not in ids: F(f'chart script references missing #{u}')
for c in canv:
    if c not in used and f"'{c}'" not in chart_js and f'"{c}"' not in chart_js: F(f'canvas {c} not used by chart script')
elems = {}
for m in re.finditer(r'<(input|select|canvas|span|div|td|strong|b|p)\b([^>]*)\sid="([^"]+)"([^>]*)>', s):
    tag, a1, i, a2 = m.groups(); attrs = a1 + a2
    val = re.search(r'\svalue="([^"]*)"', attrs)
    opts = re.findall(r'<option[^>]*value="([^"]*)"', s[m.end(): s.find('</select>', m.end())]) if tag == 'select' else []
    elems[i] = dict(tag=tag, value=(opts[0] if (tag == 'select' and opts and not val) else (val.group(1) if val else '')),
                    type=(re.search(r'\stype="([^"]*)"', attrs) or [None, ''])[1], options=opts,
                    min=(re.search(r'\smin="([^"]*)"', attrs) or [None, None])[1], max=(re.search(r'\smax="([^"]*)"', attrs) or [None, None])[1])
harness = r"""
const ELEMS = %s; const listeners = []; const cache = {};
function mkEl(id){ const d = ELEMS[id] || {tag:'div',value:'',type:'',options:[]};
  return {id, _d:d, tagName:d.tag.toUpperCase(), value:d.value, checked:false, style:{}, dataset:{}, textContent:'', innerHTML:'',
    classList:{add(){},remove(){},toggle(){},contains(){return false}}, options:d.options.map(v=>({value:v})),
    setAttribute(){}, getAttribute(){return null}, appendChild(){}, querySelector(){return null}, querySelectorAll(){return []},
    getContext(){return {}}, closest(){return null}, addEventListener(ev,fn){ listeners.push([this,ev,fn]); } }; }
global.window = global;
global.document = { getElementById(id){ if(!(id in ELEMS)) throw new Error('missing #'+id); return cache[id]||(cache[id]=mkEl(id)); },
  querySelector(){return null}, querySelectorAll(){return []}, addEventListener(){}, createElement(){return mkEl('__t')},
  documentElement:{getAttribute(){return null}, dataset:{}}, body:{classList:{contains(){return false}}} };
global.addEventListener = ()=>{}; global.matchMedia = ()=>({matches:false, addEventListener(){}});
global.getComputedStyle = ()=>({getPropertyValue(){return ''}}); global.localStorage = {getItem(){return null}, setItem(){}};
const charts = [];
function chk(c,w){ (c.data&&c.data.datasets||[]).forEach((ds,k)=>(ds.data||[]).forEach((p,j)=>{ const vs=(p&&typeof p==='object')?[p.x,p.y]:[p];
  vs.forEach(v=>{ if(typeof v==='number'&&!isFinite(v)) throw new Error(`non-finite in ${w} ds ${k} pt ${j}`); }); })); }
global.Chart = function(cv,cfg){ this.data=cfg.data; this.options=cfg.options||{}; this.update=()=>chk(this,cv&&cv.id); this.resize=()=>{}; this.destroy=()=>{}; charts.push(this); chk(this, cv&&cv.id); };
global.Chart.register=()=>{}; global.Chart.defaults={font:{},color:'',plugins:{legend:{labels:{}},tooltip:{}},scale:{grid:{},ticks:{}}};
try {
%s
} catch(e) { console.log('RUNTIME-FAIL initial: '+e.stack.split('\n').slice(0,3).join(' | ')); process.exit(3); }
for (const [el,ev,fn] of listeners) { const d=el._d||{}; const tr = d.tag==='select'?d.options:[d.min,d.max,d.value].filter(v=>v!=null&&v!=='');
  for (const v of tr) { el.value=String(v); try{ fn.call(el,{target:el}); }catch(e){ console.log(`RUNTIME-FAIL #${el.id}=${v}: `+e.message); process.exit(3);} } }
console.log(`RUNTIME-OK charts=${charts.length} listeners=${listeners.length}`);
""" % (json.dumps(elems), chart_js)
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as fh:
    fh.write(harness); tmp = fh.name
r = subprocess.run(['node', tmp], capture_output=True, text=True, timeout=120)
out = (r.stdout + r.stderr).strip()
if 'RUNTIME-OK' in out: info.append(out.splitlines()[-1])
else: F(out[-500:])
os.unlink(tmp)
info.append(f'body words ~{len(txt.split())}')
for m in info: print('INFO:', m)
for m in warns: print('WARN:', m)
for m in fails: print('FAIL:', m)
print('RESULT:', 'PASS' if not fails else f'{len(fails)} FAIL'); sys.exit(1 if fails else 0)
