"""
gen_datasets.py — every scenario behind the seven surge-protection articles.
usage: python3 specs/surge_data/gen_datasets.py specs/surge_data   (writes datasets.json)

Main engine: moc.py (MOC + discrete vapour cavity model).  Where column separation governs a peak,
the same case is also run with dgcm.py (discrete gas cavity model, alpha0 = 1e-7, built on the
independent solver indep_moc.py) and both maxima are stored: collapse peaks are model-sensitive and
the articles quote them as a range.  All runs 150 s.
"""
import sys, json, math
sys.path.insert(0, sys.argv[1]); OUT = sys.argv[1]
from moc import *
import dgcm as DG, indep_moc as IM

ALPHA0 = 1e-7
def dec(arr, n=260):
    if len(arr) <= n: return arr
    step = len(arr)/n
    return [arr[int(i*step)] for i in range(n)]
def r1(a): return [round(v, 1) for v in a]
def r2(v): return round(v, 2)
A400 = math.pi*0.4**2/4
def Rk(K, dn=0.4): return K/(2*g*(math.pi*dn*dn/4)**2)
FREE = dict(R_out=Rk(0.5), R_in=Rk(0.5))          # "free" DN400 connection, K 0.5 both ways
DIFF15 = dict(R_out=Rk(2.0), R_in=Rk(10.0))       # differential DN400 connection, 1:5
def dg(line_kw, bc, tank=None):
    r = DG.dgcm(IM.Line(**line_kw), bc, t_end=150.0, tank=tank, alpha0=ALPHA0)
    return r
def required_gas(line_kw=None, conn=FREE, limit=3.0, T=150.0, run_kw=None, vtot_factor=None):
    """smallest steady gas volume that keeps the whole line at or above `limit` (bisection)"""
    line_kw = line_kw or {}; run_kw = run_kw or {}
    def ves(m): return dict(V0=m, n=1.2, **conn, **({'Vtot': m*vtot_factor} if vtot_factor else {}))
    lo, hi = 0.05, 80.0
    for _ in range(24):
        m = 0.5*(lo+hi); rr = run(Line(**line_kw), T=T, vessel=ves(m), **{k: (dict(v) if isinstance(v, dict) else v) for k, v in run_kw.items()})
        if min(rr['Hmin']) >= limit: hi = m
        else: lo = m
    v = ves(hi); rr = run(Line(**line_kw), T=150, vessel=v, **{k: (dict(val) if isinstance(val, dict) else val) for k, val in run_kw.items()})
    return hi, v, rr
D = {'meta': dict(engine='moc.py DVCM', check='dgcm.py DGCM alpha0=%g' % ALPHA0, T=150, N=120)}

# ---------- 1 · wave speed ----------
ws = {'cases': []}
for a in (1300, 1050, 700, 450, 300):
    r = run(Line(a=a), T=150, record=(0, 60), stride=1)
    d = dg(dict(a=float(a)), IM.StoppedPumpBC())
    needed = min(r['Hmin']) < 3.0
    if needed:
        gas, v, rv = required_gas(dict(a=a)); gas_max = r2(v['Vg_max'])
    else:
        gas, gas_max = 0.0, 0.0                     # the unprotected minimum already meets +3.0 m
    ws['cases'].append(dict(a=a, jouk=round(a*0.70/(math.pi*0.4**2)/g, 1), crit=round(2*12000/a, 1),
        unprot_min=min(r['Hmin']), unprot_max=max(r['Hmax']), unprot_max_dgcm=r2(d['lmax']),
        vapour=(min(r['Hmin']) <= -9.79), vessel_needed=needed,
        gas=r2(gas), gas_max=gas_max, vessel_total=round(gas_max/0.8, 1),
        t=dec(r['t']), pump=r1(dec(r['hist'][0])), mid=r1(dec(r['hist'][60]))))
D['wavespeed'] = ws

# ---------- 2 · differential orifice ----------
ori = {'cases': [], 'gas0': 3.5, 'vtot': 20.0, 'conn': 'DN400'}
for lab, Ko, Ki in (("Free both ways", 0.5, 0.5), ("Symmetric orifice", 25, 25), ("Differential 1:2.5", 2.0, 5.0),
                    ("Differential 1:5", 2.0, 10.0), ("Differential 1:10", 2.0, 20.0), ("Over-throttled 1:40", 2.0, 80.0)):
    ves = dict(V0=3.5, Vtot=20.0, n=1.2, R_out=Rk(Ko), R_in=Rk(Ki))
    r = run(Line(), T=150, vessel=ves, record=(0,), stride=1)
    Vg = r['extra']['Vg']; t = r['t']
    q = r['extra']['Qv']                          # solver's vessel flow (differencing the rounded gas volume is too coarse)
    ipk = Vg.index(max(Vg)); refill = None
    for i in range(ipk, len(Vg)):
        if Vg[i] <= 3.5*1.10: refill = round(t[i], 0); break
    ori['cases'].append(dict(label=lab, K_out=Ko, K_in=Ki, ratio=round(Ki/Ko, 1),
        min=min(r['Hmin']), at_min=r['i_min']*100, max=max(r['Hmax']), gas_min=r2(ves['Vg_min']), gas_max=r2(ves['Vg_max']),
        emptied=ves['emptied'], refill_s=refill, q_out_peak=round(max(q), 3), q_in_peak=round(-min(q), 3),
        t=dec(t, 300), H=r1(dec(r['hist'][0], 300)), Vg=[round(v, 2) for v in dec(Vg, 300)]))
D['orifice'] = ori

# ---------- 4 · one-way tank (knee 300 m / +30 m onto a level plateau) ----------
def prof(x): return 30.0*x/300 if x <= 300 else 30.0
KN = 3
ft = {'knee_x': 300, 'knee_z': 30.0, 'delivery_hgl': 44.8,
      'max_valid_level': round(44.8 - 30.0, 1)}      # a tank above the delivery HGL drains into the reservoir after every stop
base = Line(prof=prof)
ft['x'] = [round(i*base.dx) for i in range(base.N+1)]
ft['z'] = [round(v, 1) for v in base.z]
ft['hgl'] = [round(v, 1) for v in base.H]
ft['p_steady'] = [round(base.H[i]-base.z[i], 1) for i in range(base.N+1)]
sizing = []
for level in (None, 4.0, 8.0, 12.0, 14.0):
    run_kw = {} if level is None else {'feed': dict(node=KN, level=level, vol=800.0)}
    gas, v, rr = required_gas(dict(prof=prof), conn=DIFF15, run_kw=run_kw, vtot_factor=6.0)
    fd = rr['feed']
    sizing.append(dict(tank_level=level, gas=r2(gas), gas_max=round(v['Vg_max'], 1), total=round(v['Vg_max']/0.8, 1),
                       drew=(round(fd['vol_used'], 1) if fd else None), at_min=rr['i_min']*100,
                       line_min=min(rr['Hmin']), knee_min=rr['Hmin'][KN], pump_min=rr['Hmin'][0]))
ft['sizing'] = sizing
g_alone = sizing[0]['gas']; g_tank8 = sizing[2]['gas']
cases = [('none', 'No protection', {}),
         ('tank', 'One-way tank only (8 m)', dict(feed=dict(node=KN, level=8.0, vol=800.0))),
         ('vessel', 'Vessel alone, %.1f m3 gas' % g_alone, dict(vessel=dict(V0=g_alone, Vtot=g_alone*6, n=1.2, **DIFF15))),
         ('tank_vessel', 'Tank 8 m + vessel %.1f m3 gas' % g_tank8,
          dict(feed=dict(node=KN, level=8.0, vol=800.0), vessel=dict(V0=g_tank8, Vtot=g_tank8*6, n=1.2, **DIFF15)))]
for key, lab, kw in cases:
    r = run(Line(prof=prof), T=150, record=(0, KN, 6), stride=1, **kw)
    ves = kw.get('vessel'); fd = kw.get('feed')
    entry = dict(label=lab, Hmin=r1(r['Hmin']), Hmax=r1(r['Hmax']), line_min=min(r['Hmin']),
                 knee_min=r['Hmin'][KN], pump_min=r['Hmin'][0], line_max=max(r['Hmax']), at_min=r['i_min']*100, at_max=r['i_max']*100,
                 used=(round(fd['vol_used'], 1) if fd else None),
                 gas_max=(round(ves['Vg_max'], 1) if ves else None), emptied=(ves['emptied'] if ves else None),
                 t=dec(r['t']), knee=r1(dec(r['hist'][KN])), limb=r1(dec(r['hist'][6])), pump=r1(dec(r['hist'][0])),
                 feed=([round(v, 2) for v in dec(r['extra']['feed'])] if fd else None))
    if key in ('none', 'tank'):
        d = dg(dict(profile='knee'), IM.StoppedPumpBC(), tank=(IM.Tank(level=8.0) if key == 'tank' else None))
        entry['line_max_dgcm'] = r2(d['lmax'])
    ft[key] = entry
D['feedtank'] = ft

# ---------- 5 · surge relief valve ----------
sv = {'cases': [], 'orifice': 'DN250, Cd 0.6', 'accumulation_m': 4.0}
for Hset in (None, 120.0, 110.0, 95.0):
    srv = None if Hset is None else dict(Hset=Hset, CdA=0.6*math.pi*0.25**2/4, accum=4.0)
    r = run(Line(), T=150, srv=srv, record=(0,), stride=1)
    d = dg({}, IM.StoppedPumpBC() if Hset is None else IM.ReliefBC(Hset))
    sv['cases'].append(dict(set=Hset, pump_max=r['Hmax'][0], line_max=max(r['Hmax']), at_max=r['i_max']*100, line_min=min(r['Hmin']),
        q_peak=(round(srv['q_peak'], 3) if srv else 0.0),
        pump_max_dgcm=r2(d['n0max']), line_max_dgcm=r2(d['lmax']), at_max_dgcm=d['at'],
        len_above_136=sum(100 for h in r['Hmax'] if h > 136.0), len_above_136_dgcm=sum(100 for h in d['pmax'] if h > 136.0),
        t=dec(r['t']), H=r1(dec(r['hist'][0])), Hmax=r1(r['Hmax']), Hmin=r1(r['Hmin']), Hmax_dgcm=r1(d['pmax'])))
sv['x'] = [round(i*100) for i in range(121)]
sv['sizes'] = []
for dn in (100, 150, 200, 250, 300):
    srv = dict(Hset=95.0, CdA=0.6*math.pi*(dn/1000)**2/4, accum=4.0)
    r = run(Line(), T=150, srv=srv, record=(0,), stride=1)
    d = dg({}, IM.ReliefBC(95.0, CdAv=0.6*math.pi*(dn/1000)**2/4))
    sv['sizes'].append(dict(dn=dn, pump_max=r['Hmax'][0], line_max=max(r['Hmax']), line_min=min(r['Hmin']),
        q_peak=round(srv['q_peak'], 3), at_max=r['i_max']*100, pump_max_dgcm=r2(d['n0max']), line_max_dgcm=r2(d['lmax'])))
D['srv'] = sv

# ---------- 6 · flywheel ----------
w0 = 1480*2*math.pi/60
fw = {'cases': [], 'motor': dict(P_kW=685, rpm=1480, duty_Q=0.70, duty_H=80.0)}
for I in (25, 100, 200, 400, 800, 1600):
    pump = dict(I=I, P0=685e3, w0=w0, Hsh=100.0, k=(100-80)/0.49, Hsuc=5.0, eta=0.80)
    r = run(Line(), T=150, pump=pump, record=(0,), stride=1)
    Ek = 0.5*I*w0*w0
    ts = r['t']; ws_ = r['extra']['w']
    def w_at(T_): return round(ws_[min(range(len(ts)), key=lambda i: abs(ts[i]-T_))], 3)
    fw['cases'].append(dict(I=I, GD2=4*I, Ek_MJ=round(Ek/1e6, 2), tau_s=round(Ek/685e3, 2),
        line_min=min(r['Hmin']), at_min=r['i_min']*100, pump_min=r['Hmin'][0], line_max=max(r['Hmax']),
        w5=w_at(5.0), w10=w_at(10.0), w229=w_at(22.9),
        t=dec(r['t']), w=[round(v, 3) for v in dec(ws_)], H=r1(dec(r['hist'][0])), Hmin=r1(r['Hmin'])))
fw['x'] = [round(i*100) for i in range(121)]
D['flywheel'] = fw

# ---------- 7 · comparison on the reference system ----------
cmp = []
def rec(lab, r, note, dgmax=None):
    cmp.append(dict(option=lab, line_min=min(r['Hmin']), line_max=max(r['Hmax']), line_max_dgcm=dgmax, note=note))
rec("No protection", run(Line(), T=150), "column separation along the line; collapse peaks", r2(dg({}, IM.StoppedPumpBC())['lmax']))
ves = dict(V0=3.5, Vtot=20.0, n=1.2, **DIFF15); rec("Vessel 20 m3, 3.5 m3 gas, differential 1:5", run(Line(), T=150, vessel=ves), "protects both sides")
pump = dict(I=400, P0=685e3, w0=w0, Hsh=100.0, k=(100-80)/0.49, Hsuc=5.0, eta=0.80); rec("Flywheel I = 400 kg.m2", run(Line(), T=150, pump=pump), "rundown keeps the column moving")
rec("Relief valve DN250 set 95 m", run(Line(), T=150, srv=dict(Hset=95.0, CdA=0.6*math.pi*0.25**2/4, accum=4.0)), "pressure side only, at the valve",
    r2(dg({}, IM.ReliefBC(95.0))['lmax']))
D['compare'] = dict(rows=cmp)

json.dump(D, open(OUT+'/datasets.json', 'w'), separators=(',', ':'))
import os; print('datasets.json', os.path.getsize(OUT+'/datasets.json')//1024, 'KB')
def strip(o):
    if isinstance(o, dict): return {k: strip(v) for k, v in o.items() if not (isinstance(v, list) and len(v) > 12)}
    if isinstance(o, list): return [strip(x) for x in o]
    return o
print(json.dumps(strip(D), indent=1))
