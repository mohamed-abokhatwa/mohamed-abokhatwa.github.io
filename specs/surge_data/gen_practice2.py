"""
gen_practice2.py - data behind the second set of surge-analysis practice articles (s12-s19).
usage: python3 specs/surge_data/gen_practice2.py specs/surge_data [s12 s13 ...]   (writes practice2.json)

Engines: moc.py (single main, pump rundown with three torque laws, vessel, DVCM),
series_moc.py (uniform main with a vessel, valve closure), net_moc.py (tree networks: booster
stations, junction demands, branches, vessels, prescribed pump speed and valve opening).
net_moc.py reproduces moc.py on the reference main to 0.01 m (unprotected trip, pump rundown,
vessel); the check is repeated below and stored under 'checks'.
"""
import sys, json, math, os
sys.path.insert(0, sys.argv[1]); OUT = sys.argv[1]
from moc import run as mrun, Line, g
import series_moc as S
import net_moc as NM
import dgcm as DG, indep_moc as IM
from gen_datasets_helpers import dec_group, r1, r2
WANT = set(sys.argv[2:]) or {'s12', 's13', 's14', 's15', 's16', 's17', 's18', 's19'}
PATH = OUT + '/practice2.json'
D = json.load(open(PATH)) if os.path.exists(PATH) else {}
def Rk(K, dn=0.4): return K/(2*g*(math.pi*dn*dn/4)**2)
DIFF15 = dict(R_out=Rk(2.0), R_in=Rk(10.0))
W0 = 1480*2*math.pi/60
GRAD = 40.2/12000
def thorley(P_kw, N=1480): return 118*(P_kw/N)**1.48 + 1.5e7*(P_kw/N**3)**0.9556
class LCG:
    def __init__(s, seed): s.x = seed
    def u(s):
        s.x = (1103515245*s.x + 12345) % 2**31; return s.x/2**31
    def n(s):   # approximate normal (sum of 12 uniforms)
        return sum(s.u() for _ in range(12)) - 6.0

# ---------- checks: net_moc against moc ----------
def checks():
    c = {}
    dt = 12000/120/1050; net = NM.Net(dt); net.pipe('m', 'P', 'R', 12000, 1050, 0.8, 0.70, 85.0, 44.8)
    net.node('P', kind='junc'); net.node('R', kind='res', H=44.8); NM.run(net, 150); p = net.pipes['m']
    r = mrun(Line(), T=150)
    c['unprotected'] = dict(net=[r2(p.Hmin.min()), r2(p.Hmax.max())], moc=[min(r['Hmin']), max(r['Hmax'])])
    net = NM.Net(dt); net.pipe('m', 'P', 'R', 12000, 1050, 0.8, 0.70, 85.0, 44.8)
    v = dict(V0=3.5, n=1.2, Rout=Rk(2.0), Rin=Rk(10.0)); net.node('P', kind='junc', vessel=v); net.node('R', kind='res', H=44.8)
    NM.run(net, 150); p = net.pipes['m']
    c['vessel'] = dict(net=[r2(p.Hmin.min()), r2(p.Hmax.max()), r2(v['Vmax'])], ref=[4.33, 119.15, 16.17])
    return c
if 'checks' not in D or WANT >= {'s15'}:
    D['checks'] = checks(); print('checks', D['checks'], flush=True)

# ======================= s12 field validation =======================
if 's12' in WANT:
    L, HDN = 4000.0, 85.0 - GRAD*4000
    def pump(I): return dict(I=I, P0=685e3, w0=W0, Hsh=100.0, k=20/0.49, Hsuc=5.0, eta=0.80, torque_law='radial', Q_duty=0.70)
    tr = mrun(Line(L=L, H_dn=HDN, N=400, a=1000.0), T=40, pump=pump(50.0), record=(0, 200), stride=1)
    rng = LCG(20261127)
    t100 = tr['t']; p_true = tr['hist'][0]; m_true = tr['hist'][200]
    p_meas = [round(h + 0.18*rng.n(), 2) for h in p_true]; m_meas = [round(h + 0.18*rng.n(), 2) for h in m_true]
    models = []
    for a in (950.0, 1000.0, 1050.0, 1100.0):
        for I in (35.0, 44.0, 55.0):
            r = mrun(Line(L=L, H_dn=HDN, N=40, a=a), T=40, pump=pump(I), record=(0, 20), stride=1)
            models.append(dict(a=a, I=I, t=[round(x, 4) for x in r['t']], pump=r1(r['hist'][0]), mid=r1(r['hist'][20]),
                               line_min=min(r['Hmin']), line_max=max(r['Hmax'])))
            print('s12 model', a, I, models[-1]['line_min'], flush=True)
    D['s12'] = dict(L=L, x_mid=2000.0, truth=dict(a=1000.0, I=50.0, law='radial', line_min=min(tr['Hmin']), line_max=max(tr['Hmax'])),
                    t=[round(x, 4) for x in t100], pump=p_meas, mid=m_meas,
                    pump_true=[round(x, 2) for x in p_true], mid_true=[round(x, 2) for x in m_true], models=models)

# ======================= s13 sensitivity =======================
if 's13' in WANT:
    def one(a=1050.0, hf=40.2, V0=3.5, n=1.2, kfac=1.0, Q=0.70, hdn=44.8):
        v = dict(V0=V0, n=n, R_out=Rk(2.0)*kfac, R_in=Rk(10.0)*kfac)
        r = S.run([(12000.0, a)], 12000/120/a, vessel=v, T=150, H_up=hdn + hf*(Q/0.70)**2, H_dn=hdn, Q0=Q, stride=10**9)
        return dict(min=r2(r['line_min']), max=r2(r['line_max']), gas=r2(v['Vg_max']), vap=r['vapour'])
    base = one()
    PAR = [('a', 'Wave speed', 'm/s', 1050.0, 945.0, 1155.0),
           ('hf', 'Friction loss at duty', 'm', 40.2, 34.17, 46.23),
           ('V0', 'Gas volume at steady flow', 'm³', 3.5, 3.15, 3.85),
           ('n', 'Gas law exponent', '', 1.2, 1.0, 1.4),
           ('kfac', 'Connection loss (factor)', '', 1.0, 0.7, 1.3),
           ('Q', 'Flow', 'm³/s', 0.70, 0.63, 0.77),
           ('hdn', 'Delivery level (HGL)', 'm', 44.8, 41.8, 47.8)]
    sens = []
    for key, lab, unit, b0, lo, hi in PAR:
        rl = one(**{key: lo}); rh = one(**{key: hi})
        sweep = []
        for k in range(7):
            v_ = lo + (hi - lo)*k/6; rr = one(**{key: v_}); sweep.append(dict(v=round(v_, 4), min=rr['min'], max=rr['max'], gas=rr['gas']))
        sens.append(dict(key=key, label=lab, unit=unit, base=b0, lo=lo, hi=hi, at_lo=rl, at_hi=rh, sweep=sweep))
        print('s13', key, rl, rh, flush=True)
    rng = LCG(13); mc = []
    for i in range(300):
        x = {key: lo + (hi - lo)*rng.u() for key, lab, unit, b0, lo, hi in PAR}
        rr = one(**x); mc.append(dict(x={k: round(v, 4) for k, v in x.items()}, min=rr['min'], max=rr['max']))
    worst = one(a=1155.0, hf=46.23, V0=3.15, n=1.4, kfac=1.3, Q=0.77, hdn=41.8)
    D['s13'] = dict(base=base, par=sens, mc=mc, worst_all_adverse=worst)
    print('s13 worst', worst, flush=True)

# ======================= s14 forces =======================
if 's14' in WANT:
    RHO = 998.0; A = math.pi*0.8**2/4
    cases = {}
    r = mrun(Line(N=240), T=60, record=(0, 1, 2, 4), stride=1)
    cases['trip'] = dict(label='Pump trip, no protection', t=r['t'], h={0: r['hist'][0], 50: r['hist'][1], 100: r['hist'][2], 200: r['hist'][4]}, end=0)
    v = dict(V0=3.5, n=1.2, **DIFF15)
    r = S.run([(12000.0, 1050.0)], 12000/240/1050, vessel=v, T=150, record_x=(0.0, 50.0, 100.0, 200.0), stride=1)
    cases['vessel'] = dict(label='Pump trip, vessel', t=r['t'], h={0: r['hist'][0.0], 50: r['hist'][50.0], 100: r['hist'][100.0], 200: r['hist'][200.0]}, end=0)
    for Tc, key in ((0.0, 'valve0'), (5.0, 'valve5')):
        r = S.run([(12000.0, 1050.0)], 12000/240/1050, up='reservoir', H_up=85.0, valve=dict(Tc=Tc, dH0=1.0), T=60,
                  record_x=(12000.0, 11950.0, 11900.0, 11800.0), stride=1)
        cases[key] = dict(label='Line valve at 12 km closing in %g s' % Tc, t=r['t'],
                          h={0: r['hist'][12000.0], 50: r['hist'][11950.0], 100: r['hist'][11900.0], 200: r['hist'][11800.0]}, end=1)
    out = {}
    for key, c in cases.items():
        legs = {}
        for Lg in (50, 100, 200):
            F = [RHO*g*A*(c['h'][0][k] - c['h'][Lg][k])/1000.0 for k in range(len(c['t']))]
            if c['end']: F = [-f for f in F]
            Fmax = max(F); Fmin = min(F); fabs = max(abs(Fmax), abs(Fmin))
            # duration of the main pulse: time |F| stays above half its peak around the peak
            kpk = max(range(len(F)), key=lambda k: abs(F[k]))
            k0 = kpk
            while k0 > 0 and abs(F[k0-1]) >= 0.5*fabs: k0 -= 1
            k1 = kpk
            while k1 < len(F)-1 and abs(F[k1+1]) >= 0.5*fabs: k1 += 1
            td, ys = dec_group(c['t'], [F], 700)
            legs[str(Lg)] = dict(Fmax=round(Fmax, 1), Fmin=round(Fmin, 1), Fabs=round(fabs, 1), t_peak=round(c['t'][kpk], 3),
                                 pulse=round(c['t'][k1] - c['t'][k0] + (c['t'][1]-c['t'][0]), 3), t=td, F=[round(x, 1) for x in ys[0]])
        hp = max(c['h'][0])
        out[key] = dict(label=c['label'], legs=legs, hmax_end=r2(hp))
        print('s14', key, {k: (v['Fabs'], v['pulse']) for k, v in legs.items()}, flush=True)
    D['s14'] = dict(A=A, cases=out)

# ======================= s15 boosters in series =======================
if 's15' in WANT:
    P1 = 998*g*0.7*55/0.8/1e3; P2 = 998*g*0.7*45.3/0.8/1e3
    I1, I2 = thorley(P1), thorley(P2)
    def build(t1=None, t2=None, mode='inline', V1=None, V2=None, VS=None):
        net = NM.Net(100/1050)
        hA0 = 60.0; hA1 = hA0 - GRAD*8000; hB0 = hA1 + 45.3; hB1 = hB0 - GRAD*10000
        if V1 or VS:
            hJ1 = hA0 - GRAD*100; hJS = hA1 + GRAD*100
            net.pipe('A0', 'P1', 'J1', 100, 1050, 0.8, 0.70, hA0, hJ1); net.pipe('A1', 'J1', 'JS', 7800, 1050, 0.8, 0.70, hJ1, hJS)
            net.pipe('A', 'JS', 'S', 100, 1050, 0.8, 0.70, hJS, hA1)
            net.node('J1', kind='junc', vessel=(dict(V0=V1, n=1.2, Rout=Rk(2.0), Rin=Rk(10.0)) if V1 else None))
            net.node('JS', kind='junc', vessel=(dict(V0=VS, n=1.2, Rout=Rk(2.0), Rin=Rk(10.0)) if VS else None))
        else:
            net.pipe('A', 'P1', 'S', 8000, 1050, 0.8, 0.70, hA0, hA1)
        if mode == 'tank':
            if V2:
                net.pipe('B0', 'P2', 'J2', 100, 1050, 0.8, 0.70, hB0, hB0 - GRAD*100); net.pipe('B', 'J2', 'R', 9900, 1050, 0.8, 0.70, hB0 - GRAD*100, hB1)
                net.node('J2', kind='junc', vessel=dict(V0=V2, n=1.2, Rout=Rk(2.0), Rin=Rk(10.0)))
            else:
                net.pipe('B', 'P2', 'R', 10000, 1050, 0.8, 0.70, hB0, hB1)
            net.node('S', kind='res', H=hA1)
            net.node('P2', kind='pump', Hsuc=hA1, H0=60.0, k=14.7/0.49, I=I2, w0=W0, P0=P2*1e3, eta=0.8, trip_at=(t2 if t2 is not None else 1e9))
        else:
            if V2:
                net.pipe('B0', 'S2', 'J2', 100, 1050, 0.8, 0.70, hB0, hB0 - GRAD*100); net.pipe('B', 'J2', 'R', 9900, 1050, 0.8, 0.70, hB0 - GRAD*100, hB1)
                net.node('J2', kind='junc', vessel=dict(V0=V2, n=1.2, Rout=Rk(2.0), Rin=Rk(10.0)))
                bname = 'B0'
            else:
                net.pipe('B', 'S2', 'R', 10000, 1050, 0.8, 0.70, hB0, hB1); bname = 'B'
            net.node('S', kind='bnode'); net.node('S2', kind='bnode')
            net.node('BST', kind='booster', a='A', b=bname, H0=60.0, k=14.7/0.49, Kb=2.0/0.49, I=I2, w0=W0, P0=P2*1e3, eta=0.8,
                     trip_at=(t2 if t2 is not None else 1e9))
        net.node('P1', kind='pump', Hsuc=5.0, H0=70.0, k=15.0/0.49, I=I1, w0=W0, P0=P1*1e3, eta=0.8, trip_at=(t1 if t1 is not None else 1e9))
        net.node('R', kind='res', H=hB1)
        return net
    def go(T=200, **kw):
        net = build(**kw)
        bfirst = 'B0' if 'B0' in net.pipes else 'B'
        rec = [('A', net.pipes['A'].n), (bfirst, 0)]
        r = NM.run(net, T, record=rec, stride=2)
        names = [n for n in ('A0', 'A1', 'A') if n in net.pipes]; xa, mxa, mna = NM.envelope(net, names)
        namesb = [n for n in ('B0', 'B') if n in net.pipes]; xb, mxb, mnb = NM.envelope(net, namesb)
        x = xa + [8000.0 + v for v in xb]; mx = mxa + mxb; mn = mna + mnb
        suc = r['hist'][rec[0]]; dis = r['hist'][rec[1]]
        td, ys = dec_group(r['t'], [suc, dis], 320)
        vap_t = next((r['t'][k] for k, h in enumerate(suc) if h <= -9.79), None)
        return dict(A_min=r2(min(mna)), A_max=r2(max(mxa)), B_min=r2(min(mnb)), B_max=r2(max(mxb)), suc_min=r2(min(suc)), suc_max=r2(max(suc)),
                    dis_min=r2(min(dis)), dis_max=r2(max(dis)), t_vap=vap_t, t=td, suc=r1(ys[0]), dis=r1(ys[1]),
                    x=[round(v) for v in x[::2]], emax=[round(v, 1) for v in mx[::2]], emin=[round(v, 1) for v in mn[::2]],
                    gas=[round(nd['vessel']['Vmax'], 2) for nd in net.nodes.values() if nd.get('vessel')])
    sc = {}
    for key, lab, kw in (('s2', 'Booster trips, station 1 runs on', dict(t2=0.0)),
                         ('s1', 'Station 1 trips, booster runs on', dict(t1=0.0)),
                         ('both', 'Power failure at both stations', dict(t1=0.0, t2=0.0))):
        for mode in ('inline', 'tank'):
            res = go(mode=mode, **kw); res['label'] = lab; sc[key + '_' + mode] = res
            print('s15', key, mode, res['A_min'], res['A_max'], res['B_min'], res['suc_min'], res['t_vap'], flush=True)
    casc = []
    for tdl in (0.0, 2.0, 5.0, 10.0, 30.0, 1e9):
        res = go(t1=0.0, t2=tdl)
        casc.append(dict(delay=tdl, A_min=res['A_min'], B_min=res['B_min'], suc_min=res['suc_min'], dis_min=res['dis_min'], t_vap=res['t_vap'], t=res['t'], suc=res['suc'], dis=res['dis']))
        print('s15 cascade', tdl, casc[-1], flush=True)
    # decouple with a break tank, then size a vessel for each main on its own (power failure at both stations)
    def mins(V1, V2): r_ = go(t1=0.0, t2=0.0, mode='tank', V1=V1, V2=V2, T=150); return r_['A_min'], r_['B_min']
    def bis(f):
        lo, hi = 0.2, 40.0
        if not f(hi): return None
        for _ in range(12):
            m = 0.5*(lo+hi)
            if f(m): hi = m
            else: lo = m
        return round(hi + 0.05, 1)
    V1 = bis(lambda v: mins(v, None)[0] >= 3.0); print('s15 V1', V1, flush=True)
    V2 = bis(lambda v: mins(None, v)[1] >= 3.0); print('s15 V2', V2, flush=True)
    VS = None
    ves = {}
    for key, kw in (('s2', dict(t2=0.0)), ('s1', dict(t1=0.0)), ('both', dict(t1=0.0, t2=0.0))):
        res = go(mode='tank', V1=V1, V2=V2, **kw); ves[key] = res
        print('s15 vessels', key, res['A_min'], res['A_max'], res['B_min'], res['B_max'], res['gas'], flush=True)
    D['s15'] = dict(P1=round(P1), P2=round(P2), I1=round(I1, 1), I2=round(I2, 1), heads=dict(A0=60.0, A1=round(60 - GRAD*8000, 2), B0=round(60 - GRAD*8000 + 45.3, 2),
                    B1=round(60 - GRAD*8000 + 45.3 - GRAD*10000, 2)), sc=sc, cascade=casc, V1=V1, VS=VS, V2=V2, vessels=ves)

# ======================= s16 demands and branches =======================
if 's16' in WANT:
    dt = 100/1050; Rm = 40.2/0.49/12000        # main resistance per metre, head = R x Q^2
    def build(kind):
        net = NM.Net(dt)
        qd = 0.15 if kind in ('fixed', 'orifice', 'branch') else 0.0
        q2 = 0.70 - qd
        hR = 44.8; hJ = hR + Rm*6000*q2*q2; h0 = hJ + Rm*6000*0.70**2
        if kind == 'deadend':
            hK = h0 - Rm*3000*0.49
            net.pipe('m1', 'P', 'K', 3000, 1050, 0.8, 0.70, h0, hK, R=Rm); net.pipe('m1b', 'K', 'J', 3000, 1050, 0.8, 0.70, hK, hJ, R=Rm)
            net.pipe('d', 'K', 'E', 1500, 1050, 0.3, 0.0, hK, hK, R=Rm)
            net.node('K', kind='junc'); net.node('E', kind='junc')
        else:
            net.pipe('m1', 'P', 'J', 6000, 1050, 0.8, 0.70, h0, hJ, R=Rm)
        net.pipe('m2', 'J', 'R', 6000, 1050, 0.8, q2, hJ, hR, R=Rm)
        if kind == 'branch':
            hT = hJ - 6.0
            net.pipe('br', 'J', 'T', 2000, 1050, 0.4, 0.15, hJ, hT); net.node('T', kind='res', H=hT)
            net.node('J', kind='junc')
        elif kind in ('fixed', 'orifice'):
            net.node('J', kind='junc', demand=(kind, 0.15))
        else:
            net.node('J', kind='junc')
        v = dict(V0=3.5, n=1.2, Rout=Rk(2.0), Rin=Rk(10.0))
        net.node('P', kind='junc', vessel=v); net.node('R', kind='res', H=hR)
        return net, v, dict(h0=round(h0, 2), hJ=round(hJ, 2))
    res = {}
    for kind, lab in (('none', 'Offtake left out (0.70 m³/s to the end)'), ('fixed', 'Offtake as a fixed demand, 0.15 m³/s'),
                      ('orifice', 'Offtake as a pressure-dependent demand'), ('branch', 'Offtake modelled as a 2 km DN400 branch to a tank'),
                      ('deadend', 'No offtake; closed 1.5 km DN300 branch at 3 km')):
        net, v, hh = build(kind)
        rec = [('m2', 0)] + ([('d', net.pipes['d'].n)] if kind == 'deadend' else []) + ([('br', 0)] if kind == 'branch' else []) + (['J:q_now'] if kind in ('fixed', 'orifice') else [])
        r = NM.run(net, 150, record=rec, stride=2)
        names = ['m1', 'm1b', 'm2'] if kind == 'deadend' else ['m1', 'm2']
        x, mx, mn = NM.envelope(net, names)
        td, ys = dec_group(r['t'], [r['hist'][k] for k in rec], 320)
        item = dict(label=lab, line_min=r2(min(mn)), x_min=x[mn.index(min(mn))], line_max=r2(max(mx)), x_max=x[mx.index(max(mx))],
                    gas=r2(v['Vmax']), h0=hh['h0'], hJ=hh['hJ'], x=[round(q) for q in x], emax=[round(q, 1) for q in mx], emin=[round(q, 1) for q in mn],
                    t=td, J=r1(ys[0]))
        if kind == 'deadend':
            d = net.pipes['d']; item.update(dead_max=r2(float(d.Hmax[-1])), dead_min=r2(float(d.Hmin[-1])), dead=r1(ys[1]))
        if kind in ('fixed', 'orifice'):
            item['qd'] = [round(q, 4) for q in ys[-1]]
        res[kind] = item
        print('s16', kind, item['line_min'], item['x_min'], item['line_max'], item['gas'], item.get('dead_max'), flush=True)
    D['s16'] = res

# ======================= s18 normal operations =======================
if 's18' in WANT:
    dt = 100/1050; Rm = 40.2/0.49/12000
    def stop_run(Tr, vessel=False, T=200):
        net = NM.Net(dt); net.pipe('m', 'P', 'R', 12000, 1050, 0.8, 0.70, 85.0, 44.8, R=Rm)
        wf = (lambda t: max(0.0, 1.0 - t/Tr)) if Tr > 0 else (lambda t: 0.0)
        if vessel:
            net.pipe('m0', 'P', 'J', 100, 1050, 0.8, 0.70, 85.0, 85.0 - GRAD*100, R=Rm)
            net.pipes['m'] = NM.Pipe('m', 'J', 'R', 11900, 1050, 0.8, 119, 0.70, 85.0 - GRAD*100, 44.8); net.pipes['m'].R = Rm*net.pipes['m'].dx
            net.node('J', kind='junc', vessel=dict(V0=3.5, n=1.2, Rout=Rk(2.0), Rin=Rk(10.0)))
        net.node('P', kind='pump', Hsuc=5.0, H0=100.0, k=20/0.49, wfun=wf); net.node('R', kind='res', H=44.8)
        r = NM.run(net, T, record=['P:q', ('m', 0), ('m', 60 if not vessel else 59)], stride=2)
        x, mx, mn = NM.envelope(net, ['m0', 'm'] if vessel else ['m'])
        q = r['hist']['P:q']; t_stop = next((r['t'][k] for k, v in enumerate(q) if v <= 1e-6), None)
        td, ys = dec_group(r['t'], [r['hist'][('m', 0)], r['hist'][('m', 60 if not vessel else 59)], q], 300)
        return dict(Tr=Tr, line_min=r2(min(mn)), x_min=x[mn.index(min(mn))], line_max=r2(max(mx)), t_flow_stops=t_stop,
                    vap=min(mn) <= -9.79, t=td, pump=r1(ys[0]), mid=r1(ys[1]), q=[round(v, 4) for v in ys[2]])
    def start_run(Tr, mode='vfd', T=200):
        net = NM.Net(dt); net.pipe('m', 'P', 'R', 12000, 1050, 0.8, 0.0, 44.8, 44.8, R=Rm)
        if mode == 'vfd':
            net.node('P', kind='pump', Hsuc=5.0, H0=100.0, k=20/0.49, wfun=(lambda t: min(1.0, t/Tr) if Tr > 0 else 1.0))
        else:   # direct-on-line start against a pump control valve opening linearly in Tr
            K0 = 0.5/0.49
            net.node('P', kind='pump', Hsuc=5.0, H0=100.0, k=20/0.49, wfun=(lambda t: 1.0),
                     vfun=(lambda t: (K0/max(min(1.0, t/Tr), 1e-9)**2 - K0) if (Tr > 0 and t < Tr) else 0.0) if Tr > 0 else (lambda t: 0.0))
        net.node('R', kind='res', H=44.8)
        r = NM.run(net, T, record=['P:q', ('m', 0), ('m', 60)], stride=2)
        x, mx, mn = NM.envelope(net, ['m'])
        td, ys = dec_group(r['t'], [r['hist'][('m', 0)], r['hist'][('m', 60)], r['hist']['P:q']], 300)
        return dict(Tr=Tr, line_min=r2(min(mn)), line_max=r2(max(mx)), x_max=x[mx.index(max(mx))], t=td, pump=r1(ys[0]), mid=r1(ys[1]),
                    q=[round(v, 4) for v in ys[2]], q_end=round(r['hist']['P:q'][-1], 4))
    stops = [stop_run(T_) for T_ in (0.0, 10.0, 20.0, 25.0, 30.0, 35.0, 40.0, 60.0, 90.0, 120.0, 180.0, 240.0)]
    for s_ in stops: print('s18 stop', s_['Tr'], s_['line_min'], s_['line_max'], s_['t_flow_stops'], flush=True)
    starts = [start_run(T_) for T_ in (1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0)]
    for s_ in starts: print('s18 start vfd', s_['Tr'], s_['line_min'], s_['line_max'], s_['q_end'], flush=True)
    vstarts = [start_run(T_, mode='valve') for T_ in (1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0)]
    for s_ in vstarts: print('s18 start valve', s_['Tr'], s_['line_min'], s_['line_max'], s_['q_end'], flush=True)
    D['s18'] = dict(stops=stops, starts=starts, vstarts=vstarts, w_zero_flow=round(math.sqrt((44.8 - 5.0)/100.0), 4))

# ======================= s19 wastewater force main =======================
if 's19' in WANT:
    Dm, L, Q = 0.353, 3000.0, 0.18
    Kw, rho = 2.2e9, 998.0
    def ksp(E, sdr): return math.sqrt((Kw/rho)/(1 + Kw/E*(sdr - 1)))
    a = round(ksp(1.2e9, 17.0), 1)
    A = math.pi*Dm*Dm/4; v = Q/A
    hf = 0.015*L/Dm*v*v/(2*g)
    PTS = [(0, 0.0), (300, 6.0), (1800, 12.0), (2400, 9.0), (3000, 16.0)]
    def prof(x):
        for (x0, z0), (x1, z1) in zip(PTS, PTS[1:]):
            if x <= x1: return z0 + (z1 - z0)*(x - x0)/(x1 - x0)
        return PTS[-1][1]
    HDN = 16.0 + 1.0; HUP = HDN + hf
    Hp = HUP - 2.0; P = rho*g*Q*Hp/0.70/1e3; Ip = thorley(P)
    def line(): return Line(L=L, D=Dm, a=a, Q0=Q, H_up=HUP, H_dn=HDN, N=60, prof=prof)
    def pump(I): return dict(I=I, P0=P*1e3, w0=W0, Hsh=1.3*Hp, k=0.3*Hp/Q**2, Hsuc=2.0, eta=0.70, torque_law='radial', Q_duty=Q)
    cases = {}
    for key, lab, kw in (('instant', 'Pump stops at once', {}), ('inertia', 'Real rundown, %.1f kg·m²' % Ip, dict(pump=pump(Ip))),
                         ('fly', 'Rundown with 10 times the inertia', dict(pump=pump(10*Ip)))):
        r = mrun(line(), T=120, record=(0, 36), stride=1, **kw)
        td, ys = dec_group(r['t'], [r['hist'][0], r['hist'][36]], 300)
        cases[key] = dict(label=lab, line_min=min(r['Hmin'][:-1]), x_min=min(range(60), key=lambda i: r['Hmin'][i])*50, line_max=max(r['Hmax']), cav=max(r['cav_max']),
                          Hmin=r['Hmin'], Hmax=r['Hmax'], t=td, pump=r1(ys[0]), hp=r1(ys[1]))
        print('s19', key, cases[key]['line_min'], cases[key]['x_min'], cases[key]['line_max'], cases[key]['cav'], flush=True)
    lo, hi = 0.02, 10.0
    for _ in range(20):
        m = 0.5*(lo+hi)
        if min(mrun(line(), T=120, vessel=dict(V0=m, n=1.2, R_out=Rk(0.5, 0.2), R_in=Rk(0.5, 0.2)), pump=pump(Ip))['Hmin'][:-1]) >= 0.0: hi = m
        else: lo = m
    vv = dict(V0=hi, n=1.2, R_out=Rk(0.5, 0.2), R_in=Rk(0.5, 0.2)); r = mrun(line(), T=120, vessel=vv, pump=pump(Ip), record=(0, 36), stride=1)
    td, ys = dec_group(r['t'], [r['hist'][0], r['hist'][36]], 300)
    cases['vessel'] = dict(label='Vessel at the pump, %.2f m³ of gas' % hi, line_min=min(r['Hmin'][:-1]), x_min=min(range(60), key=lambda i: r['Hmin'][i])*50, line_max=max(r['Hmax']), cav=max(r['cav_max']),
                           Hmin=r['Hmin'], Hmax=r['Hmax'], t=td, pump=r1(ys[0]), hp=r1(ys[1]), gas0=round(hi, 3), gas_max=round(vv['Vg_max'], 3))
    print('s19 vessel', hi, cases['vessel']['line_min'], vv['Vg_max'], flush=True)
    base = line()
    D['s19'] = dict(a=a, D=Dm, L=L, Q=Q, v=round(v, 3), hf=round(hf, 2), HUP=round(HUP, 2), HDN=HDN, Hp=round(Hp, 2), P=round(P, 1), I=round(Ip, 2),
                    jouk=round(a*v/g, 1), pts=PTS, x=[i*50 for i in range(61)], z=[round(q, 2) for q in base.z], hgl=[round(q, 2) for q in base.H], cases=cases)

json.dump(D, open(PATH, 'w'), separators=(',', ':'))
print('written', sorted(k for k in D))
