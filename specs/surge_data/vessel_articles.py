"""
vessel_articles.py — verified results for the corrected surge-vessel.html and
pre-charge-pressure.html (same reference system and solver as the series).
usage: python3 specs/surge_data/vessel_articles.py specs/surge_data
writes vessel_articles.json
"""
import sys, json, math
sys.path.insert(0, sys.argv[1]); OUT = sys.argv[1]
from moc import *
import dgcm as DG, indep_moc as IM
_DS = json.load(open(OUT + '/datasets.json'))
_BASE = [c for c in _DS['wavespeed']['cases'] if c['a'] == 1050][0]   # MOC sizing, free DN400 connection
def dgmax(bc, **line_kw):
    r = DG.dgcm(IM.Line(**line_kw), bc, t_end=150.0, alpha0=1e-7)
    return dict(line_max=round(r['lmax'], 2), at=r['at'], pump_max=round(r['n0max'], 2), mid_max=round(r['x6000'], 2))

HMIN_LIMIT = 3.0
P0_ABS = 85.0 + HBAR            # steady gas pressure head at the tap, m abs
M_PER_BAR = 10.20

def Rk(K, dn=0.4):
    A = math.pi*dn*dn/4
    return K/(2*g*A*A)
def dec(arr, n=260):
    if len(arr) <= n: return arr
    step = len(arr)/n
    return [arr[int(i*step)] for i in range(n)]
def r1(a): return [round(v, 1) for v in a]
def conn(kind):
    return {'free':       dict(R_out=Rk(0.5), R_in=Rk(0.5)),
            'diff15':     dict(R_out=Rk(2.0), R_in=Rk(10.0)),
            'diff15_300': dict(R_out=Rk(2.0, 0.3), R_in=Rk(10.0, 0.3)),
            'diff15_250': dict(R_out=Rk(2.0, 0.25), R_in=Rk(10.0, 0.25)),
            'free_250':   dict(R_out=Rk(0.5, 0.25), R_in=Rk(0.5, 0.25))}[kind]
def vessel(V0, Vtot=1e9, n=1.2, c='free'):
    return dict(V0=V0, Vtot=Vtot, n=n, **conn(c))
def at(r, i): return dict(max=r['Hmax'][i], min=r['Hmin'][i])
def summary(r, v=None):
    d = dict(line_min=min(r['Hmin']), line_max=max(r['Hmax']),
             at_min=r['x'][r['i_min']], at_max=r['x'][r['i_max']],
             pump=at(r, 0), mid=at(r, 60), delivery=at(r, 120))
    if v is not None:
        d.update(gas_min=round(v['Vg_min'], 2), gas_max=round(v['Vg_max'], 2), emptied=v['emptied'])
    return d
def required_gas(line_kw=None, n=1.2, c='free', limit=HMIN_LIMIT, T=100):
    line_kw = line_kw or {}
    lo, hi = 0.2, 80.0
    for _ in range(22):
        m = 0.5*(lo+hi); v = vessel(m, n=n, c=c); r = run(Line(**line_kw), T=T, vessel=v)
        if min(r['Hmin']) >= limit: hi = m
        else: lo = m
    v = vessel(hi, n=n, c=c); r = run(Line(**line_kw), T=150, vessel=v)
    return dict(gas=round(hi, 2), gas_max=round(v['Vg_max'], 2), shell=round(v['Vg_max']/0.8, 1),
                line_min=min(r['Hmin']), line_max=max(r['Hmax']))

D = {}
base = Line()
D['steady'] = dict(x=[round(i*base.dx) for i in range(base.N+1)], hgl=[round(h, 2) for h in base.H],
                   P0_abs_m=round(P0_ABS, 2), P0_bar_abs=round(P0_ABS/M_PER_BAR, 2), P0_bar_g=round(85.0/M_PER_BAR, 2),
                   table=[dict(x=x, hgl=round(85.0 - 40.2*x/12000, 2), bar_abs=round((85.0 - 40.2*x/12000 + HBAR)/M_PER_BAR, 2))
                          for x in (0, 5, 50, 500, 2000, 6000, 12000)])

# ---- A. unprotected
r = run(Line(), T=150, record=(0, 60), stride=1)
D['unprotected'] = dict(**summary(r), dgcm=dgmax(IM.StoppedPumpBC()), Hmax=r1(r['Hmax']), Hmin=r1(r['Hmin']),
                        t=dec(r['t']), pump_H=r1(dec(r['hist'][0])), mid_H=r1(dec(r['hist'][60])))

# ---- B. free-connection gas sweep, no shell cap (how much gas does the line ask for?)
sweep = []
for V0 in (1.5, 2.0, 2.5, 3.08, 3.5, 4.0):
    v = vessel(V0); rr = run(Line(), T=150, vessel=v)
    sweep.append(dict(V0=V0, **{k: val for k, val in summary(rr, v).items() if k not in ('pump', 'mid', 'delivery')},
                      shell=round(v['Vg_max']/0.8, 1)))
D['gas_sweep_free'] = sweep

# ---- C. rigid-column (mass oscillation) first estimate, vessel at the pump, friction included
def rigid(V0, n=1.2, dt=0.01):
    L, A = 12000.0, math.pi*0.8**2/4
    Rt = 40.2/0.49; Q = 0.70; V = V0; Pmin = P0_ABS; Vmax = V0; t = 0
    while t < 400:
        Hv = P0_ABS*(V0/V)**n - HBAR
        dQ = (Hv - 44.8 - Rt*Q*abs(Q))*g*A/L
        Q += dQ*dt; V += Q*dt if Q > 0 else Q*dt; t += dt
        Vmax = max(Vmax, V); Pmin = min(Pmin, Hv + HBAR)
        if Q < 0 and V < V0: break
    return Vmax, Pmin - HBAR
lo, hi = 0.2, 40.0
for _ in range(40):
    m = 0.5*(lo+hi)
    if rigid(m)[1] >= HMIN_LIMIT: hi = m
    else: lo = m
vmax, pmin = rigid(hi)
ratio_abs = (P0_ABS/(HMIN_LIMIT + HBAR))**(1/1.2)
ratio_gauge = (85.0/HMIN_LIMIT)**(1/1.2)
D['estimate'] = dict(rigid_gas=round(hi, 2), rigid_gas_max=round(vmax, 2), rigid_water_out=round(vmax-hi, 2),
                     rigid_shell=round(vmax/0.8, 1), polytropic_ratio_abs=round(ratio_abs, 3), polytropic_ratio_gauge=round(ratio_gauge, 2),
                     note='rigid column ignores wave action and column separation; MOC answer is the check')

# ---- D. the old specification checked at the correct pressure (8.0 m3 shell, 4.0 m3 gas)
old = {}
for lab, c in (('free DN400', 'free'), ('DN250 connection, K 2 out / 87 in', None)):
    if c:
        v = vessel(4.0, Vtot=8.0, c=c); bc = IM.VesselBC(V0=4.0, Vtot=8.0, Kout=0.5, Kin=0.5)
    else:
        v = dict(V0=4.0, Vtot=8.0, n=1.2, R_out=Rk(2.0, 0.25), R_in=Rk(87.0, 0.25)); bc = IM.VesselBC(V0=4.0, Vtot=8.0, Kout=2.0, Kin=87.0, Dc=0.25)
    rr = run(Line(), T=150, vessel=v, record=(0,), stride=1)
    old[lab] = dict(**summary(rr, v), dgcm=dgmax(bc))
D['old_spec_check'] = old
D['old_spec_check']['isothermal_crush_if_charged_at_1.84bar'] = round(4.0*1.84/(P0_ABS/M_PER_BAR), 2)

# ---- E. iteration table and final design: 20 m3 shell, differential 1:5, DN400
iters = []
for V0, Vt, c, lab in ((2.0, 20.0, 'diff15', 'Run 1'), (2.5, 20.0, 'diff15', 'Run 2'), (3.0, 20.0, 'diff15', 'Run 3'),
                       (3.5, 20.0, 'diff15', 'Run 4 (selected)'), (3.5, 20.0, 'free', 'Run 4, free connection')):
    v = vessel(V0, Vtot=Vt, c=c); rr = run(Line(), T=150, vessel=v)
    iters.append(dict(run=lab, V0=V0, Vtot=Vt, connection=c, **summary(rr, v)))
D['iterations'] = iters
v = vessel(3.5, Vtot=20.0, c='diff15'); rr = run(Line(), T=150, vessel=v, record=(0, 60), stride=1)
D['final'] = dict(V0=3.5, Vtot=20.0, connection='DN400, K_out 2 / K_in 10', **summary(rr, v),
                  Hmax=r1(rr['Hmax']), Hmin=r1(rr['Hmin']), t=dec(rr['t']), pump_H=r1(dec(rr['hist'][0])),
                  mid_H=r1(dec(rr['hist'][60])), Vg=[round(x, 2) for x in dec(rr['extra']['Vg'])],
                  water_reserve_at_max=round(20.0 - v['Vg_max'], 2),
                  gas_pressure_bar_abs=round(P0_ABS/M_PER_BAR, 2))

# ---- F. connection size for the final vessel
cs = []
for c, lab in (('diff15', 'DN400'), ('diff15_300', 'DN300'), ('diff15_250', 'DN250')):
    v = vessel(3.5, Vtot=20.0, c=c); rr = run(Line(), T=150, vessel=v)
    s = summary(rr, v); cs.append(dict(connection=lab, line_min=s['line_min'], line_max=s['line_max'], gas_max=s['gas_max'], emptied=s['emptied']))
D['connection_size'] = cs

# ---- G. sensitivity of the required gas volume (free DN400 connection unless stated)
sens = [('Base case', {}, 1.2, 'free', 3.0),
        ('Minimum criterion +5.0 m (tighter)', {}, 1.2, 'free', 5.0),
        ('Minimum criterion +1.0 m (looser)', {}, 1.2, 'free', 1.0),
        ('Line 24 km, same end heads', dict(L=24000.0), 1.2, 'free', 3.0),
        ('Wave speed 700 m/s', dict(a=700.0), 1.2, 'free', 3.0),
        ('Wave speed 450 m/s (GRP-type pipe)', dict(a=450.0), 1.2, 'free', 3.0),
        ('Gas law exponent n = 1.0', {}, 1.0, 'free', 3.0),
        ('Gas law exponent n = 1.4', {}, 1.4, 'free', 3.0),
        ('DN250 connection, same loss coefficient', {}, 1.2, 'free_250', 3.0),
        ('Differential DN400 connection 1:5', {}, 1.2, 'diff15', 3.0)]
rows = []
for lab, kw, n, c, lim in sens:
    res = required_gas(kw, n=n, c=c, limit=lim); rows.append(dict(case=lab, **res))
b = rows[0]
for row in rows: row['shell_change_pct'] = round(100*(row['shell']/b['shell'] - 1))
r300 = run(Line(a=300.0), T=150)
rows.append(dict(case='Wave speed 300 m/s (PE-type pipe)', gas=0.0, gas_max=0.0, shell=0.0, line_min=min(r300['Hmin']),
                 line_max=max(r300['Hmax']), shell_change_pct=-100,
                 note='unprotected minimum already above +3.0 m: no vessel needed for this criterion'))
D['sensitivity'] = rows

# ---- H. pre-charge article: bladder vessel, fixed 25 m3 shell, pre-charge as a fraction of P_min abs
PMIN_ABS = HMIN_LIMIT + HBAR
bl = []
for f in (0.5, 0.7, 0.9, 1.0, 1.5, 3.0):
    Ppre = f*PMIN_ABS; V0 = 25.0*Ppre/P0_ABS
    v = vessel(V0, Vtot=25.0, c='free'); rr = run(Line(), T=150, vessel=v)
    s_ = summary(rr, v)
    bl.append(dict(fraction=f, P_pre_m_abs=round(Ppre, 2), P_pre_bar_abs=round(Ppre/M_PER_BAR, 2), V0=round(V0, 2),
                   water_at_steady=round(25.0-V0, 2), line_min=s_['line_min'], line_max=s_['line_max'],
                   gas_max=s_['gas_max'], emptied=s_['emptied'],
                   line_max_dgcm=(dgmax(IM.VesselBC(V0=V0, Vtot=25.0, Kout=0.5, Kin=0.5))['line_max'] if s_['line_min'] <= -9.79 else None),
                   vessel_min_gas_m_abs=round(P0_ABS*(V0/v['Vg_max'])**1.2, 2)))
D['bladder_fixed_shell'] = dict(shell=25.0, connection='free DN400 (K 0.5)', rows=bl)
# shell needed vs pre-charge fraction for the required 3.04 m3 at steady state (isothermal charging)
D['bladder_shell_needed'] = [dict(fraction=f, shell=round(_BASE['gas']*P0_ABS/(f*PMIN_ABS), 1)) for f in (0.5, 0.6, 0.7, 0.8, 0.9, 0.95)]

# ---- I. air-over-water, fixed 20 m3 shell, different gas settings (the water level set point)
aw = []
for V0 in (2.0, 2.5, 3.0, 3.5, 4.5, 6.0, 8.0):
    v = vessel(V0, Vtot=20.0, c='diff15'); rr = run(Line(), T=150, vessel=v, record=(0,), stride=1)
    s = summary(rr, v)
    aw.append(dict(V0=V0, gas_fraction_pct=round(100*V0/20.0), line_min=s['line_min'], line_max=s['line_max'],
                   line_max_dgcm=(dgmax(IM.VesselBC(V0=V0, Vtot=20.0, Kout=2.0, Kin=10.0))['line_max'] if s['line_min'] <= -9.79 else None),
                   gas_max=s['gas_max'], emptied=s['emptied'], water_left=round(max(0.0, 20.0-v['Vg_max']), 2),
                   t=dec(rr['t'], 200), pump_H=r1(dec(rr['hist'][0], 200))))
D['air_over_water_settings'] = dict(shell=20.0, rows=aw)
def _passes(V0):
    v = vessel(V0, Vtot=20.0, c='diff15'); rr = run(Line(), T=150, vessel=v)
    return min(rr['Hmin']) >= HMIN_LIMIT and not v['emptied']
lo, hi = 3.0, 3.5
for _ in range(18):
    m = 0.5*(lo+hi)
    if _passes(m): hi = m
    else: lo = m
w_lo = hi
lo, hi = 4.5, 8.0
for _ in range(18):
    m = 0.5*(lo+hi)
    if _passes(m): lo = m
    else: hi = m
D['air_over_water_settings']['window'] = dict(gas_min=round(w_lo, 2), gas_max=round(lo, 2),
    note='gas settings that keep +3.0 m and do not empty the 20 m3 shell; at the upper end the gas just reaches the shell volume')

# ---- J. the unit mistakes, closed form on the reference duty (water to deliver 12.21 m3, from the MOC base case)
water = _BASE['gas_max'] - _BASE['gas']
D['unit_mistakes'] = dict(water_out=round(water, 2),
    correct_abs=dict(ratio=round(ratio_abs, 3), V0=round(water/(ratio_abs-1), 2)),
    gauge_used=dict(ratio=round(ratio_gauge, 2), V0=round(water/(ratio_gauge-1), 2)),
    wrong_1_84_bar=dict(ratio=round((1.84/1.30)**(1/1.2), 3), V0=round(water/((1.84/1.30)**(1/1.2)-1), 1)))

json.dump(D, open(OUT + '/vessel_articles.json', 'w'), separators=(',', ':'))
def strip(o):
    if isinstance(o, dict): return {k: strip(v) for k, v in o.items() if not (isinstance(v, list) and len(v) > 12)}
    if isinstance(o, list): return [strip(x) for x in o]
    return o
print(json.dumps(strip(D), indent=1))
