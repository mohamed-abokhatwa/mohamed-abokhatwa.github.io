#!/usr/bin/env python3
"""chart_probe.py — run an article spec's chart code headlessly and record every output.

usage (repo root):  python3 scripts/chart_probe.py specs/s01_wave_speed.py out.json [--points N]

Records, for the default state and for every control swept one at a time (range: min, interior
points on the step grid, max, default; select: every option; checkbox: both states):
  - every text/innerHTML write to non-control elements (readouts, labels, badges, hints)
  - every Chart instance: type, axis titles/min/max/type, annotation values and label text,
    and each dataset (label, type, point count, x/y range, first/last points, a sample of points)
Also lists the equations in the article body (display and inline MathJax) and the controls.

Needs node. Writes nothing into the repo; the JSON goes where you point it.
"""
import sys, os, re, json, html, subprocess, tempfile, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
spec_path, out_path = sys.argv[1], sys.argv[2]
NPTS = int(sys.argv[sys.argv.index('--points') + 1]) if '--points' in sys.argv else 40

sp = importlib.util.spec_from_file_location('probe_spec', spec_path)
mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
S = mod.SPEC; body = S['body']; charts = S['charts']

def strip(x): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()
equations = {
    'display': [m.group(1).strip() for m in re.finditer(r'\\\[(.*?)\\\]', body, flags=re.S)],
    'inline': [m.group(1).strip() for m in re.finditer(r'\\\((.*?)\\\)', body, flags=re.S)],
}

controls = []
elems = {}
for m in re.finditer(r'<(input|select|canvas|span|div|td|strong|b|p|small|em|li|h3|h4)\b([^>]*)\sid="([^"]+)"([^>]*)>', body):
    tag, a1, i, a2 = m.groups(); attrs = a1 + a2
    g = lambda k: (re.search(r'\s%s="([^"]*)"' % k, attrs) or [None, None])[1]
    d = dict(tag=tag, value=g('value') or '', type=g('type') or '', checked=bool(re.search(r'\schecked\b', attrs)))
    if tag == 'select':
        seg = body[m.end(): body.find('</select>', m.end())]
        opts = re.findall(r'<option([^>]*)value="([^"]*)"([^>]*)>(.*?)</option>', seg, flags=re.S)
        d['options'] = [[v, strip(lab)] for pre, v, post, lab in opts]
        sel = [v for pre, v, post, lab in opts if 'selected' in pre + post]
        d['value'] = sel[0] if sel else (opts[0][1] if opts else '')
    if tag == 'input':
        d.update(min=g('min'), max=g('max'), step=g('step'))
    elems[i] = d
    if tag in ('input', 'select'):
        lab = re.search(r'<label[^>]*>(.*?)</label>\s*(?:<[^>]+>\s*)*?<%s[^>]*id="%s"' % (tag, re.escape(i)), body, flags=re.S)
        controls.append(dict(id=i, **d, label=strip(lab.group(1)) if lab else ''))

def sweep_values(c):
    if c['tag'] == 'select': return [o[0] for o in c.get('options', [])]
    if c['type'] == 'checkbox': return ['__on__', '__off__']
    try:
        lo, hi = float(c['min']), float(c['max']); st = float(c['step']) if c['step'] not in (None, '', 'any') else None
    except Exception:
        return [c['value']]
    vals = [lo, lo + (hi - lo) * 0.25, lo + (hi - lo) * 0.5, lo + (hi - lo) * 0.75, hi]
    if st:
        vals = [round(round((v - lo) / st) * st + lo, 10) for v in vals]
    out = []
    for v in vals + ([float(c['value'])] if c['value'] not in ('', None) else []):
        s = ('%.10g' % v)
        if s not in out: out.append(s)
    return out

harness = r"""
const ELEMS = %(elems)s;
const CONTROLS = %(controls)s;
const SWEEP = %(sweep)s;
const NPTS = %(npts)d;
const listeners = []; const cache = {}; const writes = {};
function strip(s){ return String(s).replace(/<[^>]+>/g,' ').replace(/&nbsp;/g,' ').replace(/&minus;/g,'−').replace(/&middot;/g,'·').replace(/&sup3;/g,'³').replace(/&sup2;/g,'²').replace(/&amp;/g,'&').replace(/\s+/g,' ').trim(); }
function mkEl(id){
  const d = ELEMS[id] || {tag:'div',value:'',type:'',checked:false,options:[]};
  const el = {id, _d:d, tagName:(d.tag||'div').toUpperCase(), type:d.type, checked:!!d.checked, style:{}, dataset:{},
    classList:{_s:new Set(), add(...a){a.forEach(x=>this._s.add(x))}, remove(...a){a.forEach(x=>this._s.delete(x))}, toggle(x,f){ if(f===undefined? !this._s.has(x) : f) this._s.add(x); else this._s.delete(x);}, contains(x){return this._s.has(x)}},
    options:(d.options||[]).map(o=>({value:o[0], text:o[1], textContent:o[1]})), selectedIndex:0, disabled:false, title:'',
    setAttribute(k,v){ this['_attr_'+k]=v; }, getAttribute(k){ return this['_attr_'+k]||null; }, appendChild(){}, removeChild(){},
    querySelector(){return null}, querySelectorAll(){return []}, getContext(){return {}}, closest(){return null},
    addEventListener(ev, fn){ listeners.push([this, ev, fn]); } };
  let _v = d.value; Object.defineProperty(el, 'value', {get(){return _v}, set(v){_v=String(v);}, enumerable:true});
  Object.defineProperty(el, 'valueAsNumber', {get(){return parseFloat(_v)}, enumerable:true});
  let _t = '', _h = '';
  Object.defineProperty(el, 'textContent', {get(){return _t}, set(v){_t=String(v); _h=String(v); writes[id]=strip(v);}, enumerable:true});
  Object.defineProperty(el, 'innerText', {get(){return _t}, set(v){_t=String(v); _h=String(v); writes[id]=strip(v);}, enumerable:true});
  Object.defineProperty(el, 'innerHTML', {get(){return _h}, set(v){_h=String(v); _t=strip(v); writes[id]=strip(v);}, enumerable:true});
  if (d.tag==='select') { const i=(d.options||[]).findIndex(o=>o[0]===d.value); el.selectedIndex=i<0?0:i; }
  return el;
}
global.window = global; global.devicePixelRatio = 1;
global.document = { getElementById(id){ if(!(id in ELEMS)) throw new Error('getElementById missing #'+id); return cache[id]||(cache[id]=mkEl(id)); },
  querySelector(){return null}, querySelectorAll(){return []}, addEventListener(){}, createElement(){ return mkEl('__tmp'); },
  documentElement:{getAttribute(){return 'light'}, dataset:{}, style:{}}, body:{classList:{contains(){return false}}} };
global.addEventListener = function(){};
global.matchMedia = ()=>({matches:false, addEventListener(){}, addListener(){}});
global.getComputedStyle = ()=>({getPropertyValue(){return ''}});
global.requestAnimationFrame = fn => 0; global.localStorage = {getItem(){return null}, setItem(){}};
const charts = [];
global.Chart = function(canvas, cfg){ this.canvas = canvas; this.config = cfg; this.data = cfg.data; this.options = cfg.options || {}; this.update = ()=>{}; this.resize = ()=>{}; this.destroy = ()=>{}; charts.push(this); };
global.Chart.register = () => {}; global.Chart.defaults = {font:{}, plugins:{legend:{labels:{}}, tooltip:{}}, scale:{grid:{}, ticks:{}}, color:''};
function num(v){ return (typeof v==='number' && isFinite(v)) ? +v.toPrecision(6) : v; }
function pt(p, i){ if (p && typeof p==='object') return [num(p.x), num(p.y)]; return [i, num(p)]; }
function snapChart(c){
  const o = c.options || {}; const sc = o.scales || {}; const axes = {};
  Object.keys(sc).forEach(k=>{ const a=sc[k]||{}; axes[k]={type:a.type, min:num(typeof a.min==='function'?'fn':a.min), max:num(typeof a.max==='function'?'fn':a.max), title:a.title&&a.title.text, position:a.position}; });
  const ann = {}; try { const A = o.plugins.annotation.annotations; Object.keys(A||{}).forEach(k=>{ const a=A[k]; if(!a) return; ann[k]={type:a.type, value:num(a.value), xMin:num(a.xMin), xMax:num(a.xMax), yMin:num(a.yMin), yMax:num(a.yMax), scaleID:a.scaleID, display:a.display, label:a.label&&(Array.isArray(a.label.content)?a.label.content.join(' / '):a.label.content), label_display:a.label&&a.label.display}; }); } catch(e){}
  const ds = ((c.data&&c.data.datasets)||[]).map(d=>{
    const pts = (d.data||[]).map(pt);
    const ys = pts.map(p=>p[1]).filter(v=>typeof v==='number'); const xs = pts.map(p=>p[0]).filter(v=>typeof v==='number');
    const bad = (d.data||[]).filter(p=>{ const v=(p&&typeof p==='object')?[p.x,p.y]:[p]; return v.some(z=>typeof z==='number' && !isFinite(z)); }).length;
    const step = Math.max(1, Math.ceil(pts.length/NPTS));
    return {label:d.label, type:d.type||c.config.type, hidden:!!d.hidden, yAxisID:d.yAxisID, n:pts.length, nonFinite:bad,
      xRange: xs.length?[Math.min(...xs), Math.max(...xs)]:null, yRange: ys.length?[Math.min(...ys), Math.max(...ys)]:null,
      first: pts[0]||null, last: pts[pts.length-1]||null, sample: pts.filter((p,i)=>i%%step===0) };
  });
  return {canvas:c.canvas&&c.canvas.id, type:c.config.type, labels:(c.data&&c.data.labels)||null, axes, annotations:ann, datasets:ds};
}
function snapshot(){ return {readouts: Object.assign({}, writes), charts: charts.map(snapChart)}; }
function fire(el){ listeners.filter(l=>l[0]===el).forEach(([e,ev,fn])=>{ fn.call(e,{target:e, type:ev}); }); }
const result = {errors:[]};
try {
%(charts)s
} catch (e) { result.errors.push('initial: '+e.stack.split('\n').slice(0,3).join(' | ')); }
result.default = snapshot();
result.sweeps = [];
for (const c of CONTROLS) {
  const el = document.getElementById(c.id);
  const d0 = el.value, c0 = el.checked;
  for (const v of (SWEEP[c.id]||[])) {
    if (v==='__on__') el.checked = true; else if (v==='__off__') el.checked = false; else { el.value = v; if (c.tag==='select') el.selectedIndex = Math.max(0,(c.options||[]).findIndex(o=>o[0]===v)); }
    try { fire(el); result.sweeps.push({control:c.id, label:c.label, value:v, state:snapshot()}); }
    catch (e) { result.errors.push(`${c.id}=${v}: `+e.stack.split('\n').slice(0,3).join(' | ')); }
  }
  el.value = d0; el.checked = c0; if (c.tag==='select') el.selectedIndex = Math.max(0,(c.options||[]).findIndex(o=>o[0]===d0));
  try { fire(el); } catch(e) {}
}
result.listeners = listeners.map(l=>l[0].id+':'+l[1]);
process.stdout.write(JSON.stringify(result));
""" % dict(elems=json.dumps(elems), controls=json.dumps(controls), sweep=json.dumps({c['id']: sweep_values(c) for c in controls}),
           npts=NPTS, charts=charts)

with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as fh:
    fh.write(harness); tmp = fh.name
r = subprocess.run(['node', '--max-old-space-size=2048', tmp], capture_output=True, text=True, timeout=300)
os.unlink(tmp)
if r.returncode != 0 or not r.stdout.startswith('{'):
    print('HARNESS FAILED', r.stderr[-2000:]); sys.exit(2)
res = json.loads(r.stdout)
res['spec'] = spec_path; res['slug'] = S['slug']; res['controls'] = controls; res['equations'] = equations
json.dump(res, open(out_path, 'w'), indent=1, ensure_ascii=False)
print(f"{S['slug']}: {len(controls)} controls, {len(res['sweeps'])} swept states, {len(res['default']['charts'])} charts, "
      f"{len(res['default']['readouts'])} readouts, {len(equations['display'])}+{len(equations['inline'])} equations, errors={len(res['errors'])}")
for e in res['errors']: print('  ERROR', e)
