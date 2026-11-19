"""
gen_analyst.py — data behind the four surge-analysis practice articles (s08–s11).
usage: python3 specs/surge_data/gen_analyst.py specs/surge_data   (writes analyst.json; needs numpy)

s08 model check : time-step / wave-speed adjustment on a realistic pipe list (series_moc.py, an
                  independent numpy solver that reproduces moc.py to 0.01 m on the uniform main),
                  grid convergence and run duration on the reference main, Joukowsky test model.
s09 pump data   : pump-trip rundowns (moc.py) for four main lengths, six inertias, three torque laws;
                  vessel gas required on the 12 km main against the inertia assumption.
s10 limits      : envelopes of four protection cases on the reference main.
s11 report      : the reference main on an undulating profile, unprotected / 3.5 m3 vessel / design vessel.
"""
import sys, json, math
sys.path.insert(0, sys.argv[1]); OUT = sys.argv[1]
from moc import run, Line, g
import series_moc as S
import dgcm as DG, indep_moc as IM
from gen_datasets_helpers import dec_group, r1, r2
def Rk(K, dn=0.4): return K/(2*g*(math.pi*dn*dn/4)**2)
DIFF15 = dict(R_out=Rk(2.0), R_in=Rk(10.0))
W0 = 1480*2*math.pi/60
D = {}

# ======================= s08 · is the run right? =======================
ST, DI = 1150.0, 1050.0
RAW = [('P-1', 'Pump discharge spool', 6.5, ST), ('P-2', 'Discharge header', 11.0, ST), ('P-3', 'Header to vessel tee and meter', 18.4, ST),
       ('P-4', 'Flowmeter spool', 2.4, ST), ('P-5', 'Meter to station boundary valve', 27.7, ST),
       ('P-6', 'Field main', 486.0, DI), ('P-7', 'Field main', 1212.5, DI), ('P-8', 'Field main', 834.6, DI),
       ('P-9', 'Washout chamber spool', 3.2, DI), ('P-10', 'Field main', 1560.2, DI), ('P-11', 'Road crossing (steel sleeve)', 41.0, ST),
       ('P-12', 'Field main', 922.8, DI), ('P-13', 'Field main', 1407.3, DI), ('P-14', 'Air valve tee spool', 5.6, DI),
       ('P-15', 'Field main', 2015.0, DI), ('P-16', 'Field main', 1175.9, DI), ('P-17', 'Field main to reservoir', 2269.9, DI)]
CLEAN = [('P-1', 'Station pipework, P-1 to P-5 merged', 66.0, ST), ('P-6', 'Field main', 486.0, DI), ('P-7', 'Field main', 1212.5, DI),
         ('P-8', 'Field main with P-9 merged', 837.8, DI), ('P-10', 'Field main', 1560.2, DI), ('P-11', 'Road crossing (steel sleeve)', 41.0, ST),
         ('P-12', 'Field main', 922.8, DI), ('P-13', 'Field main with P-14 merged', 1412.9, DI), ('P-15', 'Field main', 2015.0, DI),
         ('P-16', 'Field main', 1175.9, DI), ('P-17', 'Field main to reservoir', 2269.9, DI)]
assert abs(sum(p[2] for p in RAW) - 12000) < 1e-6 and abs(sum(p[2] for p in CLEAN) - 12000) < 1e-6
pp = lambda M: [(p[2], p[3]) for p in M]
a = {'raw': [list(p) for p in RAW], 'clean': [list(p) for p in CLEAN]}
DTS = (0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002)
a['adj_check'] = {m: {mode: {str(dt): S.adjust_stats(pp(M), dt, mode) for dt in DTS + (0.001, 0.03, 0.0035)}
                       for mode in ('length', 'wave')} for m, M in (('raw', RAW), ('clean', CLEAN))}
ref = S.run(pp(RAW), 0.0005, 'wave', vessel=dict(V0=3.5, n=1.2, **DIFF15), T=150, stride=10**9)
a['ref'] = dict(dt=0.0005, line_min=r2(ref['line_min']), x_min=round(ref['x_min']), line_max=r2(ref['line_max']),
                gas_max=r2(ref['vessel']['Vg_max']), reaches=ref['N'])
res = []
for m, M in (('raw', RAW), ('clean', CLEAN)):
    for mode in ('length', 'wave'):
        for dt in DTS:
            v = dict(V0=3.5, n=1.2, **DIFF15)
            r = S.run(pp(M), dt, mode, vessel=v, T=150, stride=10**9)
            st = S.adjust_stats(pp(M), dt, mode)
            res.append(dict(model=m, mode=mode, dt=dt, line_min=r2(r['line_min']), x_min=round(r['x_min']), line_max=r2(r['line_max']),
                            gas_max=r2(v['Vg_max']), vapour=r['vapour'], reaches=r['N'], max_adj=round(st['max']*100, 1)))
            print('s08', m, mode, dt, res[-1]['line_min'], res[-1]['line_max'], flush=True)
a['results'] = res
grid = []
for N in (30, 60, 120, 240, 480, 960):
    v = dict(V0=3.5, Vtot=20.0, n=1.2, **DIFF15); rv = run(Line(N=N), T=150, vessel=v)
    p = dict(I=400, P0=685e3, w0=W0, Hsh=100.0, k=(100-80)/0.49, Hsuc=5.0, eta=0.80); rp = run(Line(N=N), T=150, pump=p)
    ru = run(Line(N=N), T=150)
    d = DG.dgcm(IM.Line(N=N), IM.StoppedPumpBC(), t_end=150.0, alpha0=1e-7)
    grid.append(dict(N=N, dx=round(12000/N, 1), dt=round(12000/N/1050, 4),
                     ves_min=min(rv['Hmin']), ves_xmin=round(rv['i_min']*12000/N), ves_max=max(rv['Hmax']), ves_gas=r2(v['Vg_max']),
                     fly_min=min(rp['Hmin']), fly_xmin=round(rp['i_min']*12000/N),
                     un_max=max(ru['Hmax']), un_max_dgcm=r2(d['lmax'])))
    print('grid', grid[-1], flush=True)
a['grid'] = grid
v = dict(V0=3.5, n=1.2, **DIFF15)
r = S.run([(12000.0, 1050.0)], 12000/1200/1050, vessel=v, T=400, record_x=(0.0, 6000.0), stride=1)
fm, fM = r['env_min'][-1], r['env_max'][-1]
t_min = next(r['t'][k] for k in range(len(r['t'])) if r['env_min'][k] <= fm + 0.005)
t_max = next(r['t'][k] for k in range(len(r['t'])) if r['env_max'][k] >= fM - 0.005)
td, ys = dec_group(r['t'], [r['hist'][0.0], r['hist'][6000.0], r['env_min'], r['env_max']], 520)
a['duration'] = dict(t=td, pump=r1(ys[0]), mid=r1(ys[1]), env_min=[round(x, 2) for x in ys[2]], env_max=[round(x, 2) for x in ys[3]],
                     final_min=r2(fm), final_max=r2(fM), t_min=round(t_min, 1), t_max=round(t_max, 1), gas_max=r2(v['Vg_max']))
jk = []
for Tc in (0.0, 5.0):
    r = S.run([(12000.0, 1050.0)], 12000/1200/1050, up='reservoir', H_up=85.0, valve=dict(Tc=Tc, dH0=1.0), T=60, record_x=(12000.0, 6000.0), stride=1)
    h = r['hist'][12000.0]; t = r['t']
    i5 = min(range(len(t)), key=lambda q: abs(t[q] - (Tc + 0.1)))
    td, ys = dec_group(t, [h, r['hist'][6000.0]], 300)
    jk.append(dict(Tc=Tc, h_first=r2(h[0]), h_after=r2(h[i5]), peak=r2(max(h)), t_peak=round(t[h.index(max(h))], 2),
                   t=td, valve=r1(ys[0]), mid=r1(ys[1])))
a['joukowsky'] = dict(steady_valve=45.8, theory=r2(1050*(0.70/(math.pi*0.4**2))/g), cases=jk)
D['s08'] = a

# ======================= s09 · pump data =======================
LAWS = ('duty', 'radial', 'shutoff')
IS = (0, 25, 44, 88, 176, 400)
b = {'thorley': dict(P=685.0, N=1480, Im=round(118*(685/1480)**1.48, 2), Ip=round(1.5e7*(685/1480**3)**0.9556, 2)), 'mains': []}
for L, N, T in ((12000.0, 120, 150.0), (4000.0, 40, 60.0), (2000.0, 40, 40.0), (1000.0, 40, 30.0)):
    Hdn = 85.0 - 40.2*L/12000
    main = dict(L=L, Hdn=round(Hdn, 2), T=T, tla=round(2*L/1050, 2), cases=[])
    for I in IS:
        for law in (LAWS if I > 0 else ('instant',)):
            kw = {}
            if I > 0: kw['pump'] = dict(I=I, P0=685e3, w0=W0, Hsh=100.0, k=(100-80)/0.49, Hsuc=5.0, eta=0.80, torque_law=law, Q_duty=0.70)
            r = run(Line(L=L, H_dn=Hdn, N=N), T=T, record=(0,), stride=1, **kw)
            ser = [r['hist'][0]] + ([r['extra']['w']] if I > 0 else [])
            td, ys = dec_group(r['t'], ser, 240)
            vap = min(r['Hmin']) <= -9.79
            main['cases'].append(dict(I=I, law=law, line_min=min(r['Hmin']), at_min=round(r['i_min']*L/N), pump_min=r['Hmin'][0],
                                      line_max=max(r['Hmax']), vapour=vap, t=td, H=r1(ys[0]), w=([round(x, 3) for x in ys[1]] if I > 0 else None)))
        print('s09', L, I, flush=True)
    b['mains'].append(main)
def req_gas(I, law):
    lo, hi = 0.05, 10.0
    for _ in range(22):
        m = 0.5*(lo+hi); kw = dict(vessel=dict(V0=m, Vtot=m*20/3.5, n=1.2, **DIFF15))
        if I > 0: kw['pump'] = dict(I=I, P0=685e3, w0=W0, Hsh=100.0, k=(100-80)/0.49, Hsuc=5.0, eta=0.80, torque_law=law, Q_duty=0.70)
        if min(run(Line(), T=150, **kw)['Hmin']) >= 3.0: hi = m
        else: lo = m
    return round(hi, 2)
b['vessel_gas'] = [dict(I=I, law=law, gas=req_gas(I, law)) for I in (0, 25, 44, 88) for law in ((LAWS) if I > 0 else ('instant',))]
print('s09 gas', b['vessel_gas'], flush=True)
D['s09'] = b

# ======================= s10 · limits =======================
DS = json.load(open(OUT + '/datasets.json'))
sv = DS['srv']['cases']
un = sv[0]; rv95 = sv[3]
v = dict(V0=3.5, Vtot=20.0, n=1.2, **DIFF15); rves = run(Line(), T=150, vessel=v)
p = dict(I=400, P0=685e3, w0=W0, Hsh=100.0, k=(100-80)/0.49, Hsuc=5.0, eta=0.80); rfly = run(Line(), T=150, pump=p)
c = {'x': [i*100 for i in range(121)], 'cases': [
    dict(key='none', label='No protection', Hmax=un['Hmax'], Hmin=un['Hmin'], Hmax_dgcm=un['Hmax_dgcm'], line_max=un['line_max'], line_max_dgcm=un['line_max_dgcm'], line_min=un['line_min']),
    dict(key='vessel', label='Vessel, 3.5 m3 gas in a 20 m3 shell', Hmax=[r2(x) for x in rves['Hmax']], Hmin=[r2(x) for x in rves['Hmin']], Hmax_dgcm=None,
         line_max=max(rves['Hmax']), line_max_dgcm=None, line_min=min(rves['Hmin'])),
    dict(key='srv', label='Relief valve set at 95 m, no vessel', Hmax=rv95['Hmax'], Hmin=rv95['Hmin'], Hmax_dgcm=rv95['Hmax_dgcm'],
         line_max=rv95['line_max'], line_max_dgcm=rv95['line_max_dgcm'], line_min=rv95['line_min']),
    dict(key='fly', label='Flywheel, 400 kg.m2 in total', Hmax=[r2(x) for x in rfly['Hmax']], Hmin=[r2(x) for x in rfly['Hmin']], Hmax_dgcm=None,
         line_max=max(rfly['Hmax']), line_max_dgcm=None, line_min=min(rfly['Hmin']))]}
D['s10'] = c

# ======================= s11 · report =======================
PTS = [(0, 0.0), (600, 4.0), (2500, 10.0), (4500, 3.0), (7200, 12.0), (9000, 6.0), (10800, 9.0), (12000, 5.0)]
def prof(x):
    for (x0, z0), (x1, z1) in zip(PTS, PTS[1:]):
        if x <= x1: return z0 + (z1-z0)*(x-x0)/(x1-x0)
    return PTS[-1][1]
REC = (0, 25, 45, 72, 120)
base = Line(prof=prof)
d = dict(pts=PTS, x=[i*100 for i in range(121)], z=[round(v, 2) for v in base.z], hgl=[round(v, 2) for v in base.H], rec=[k*100 for k in REC], cases=[])
lo, hi = 0.5, 40.0
for _ in range(22):
    m = 0.5*(lo+hi)
    if min(run(Line(prof=prof), T=150, vessel=dict(V0=m, Vtot=1e9, n=1.2, **DIFF15))['Hmin']) >= 3.0: hi = m
    else: lo = m
d['gas_required'] = round(hi, 3)
for key, label, ves in (('none', 'No protection', None), ('v35', 'Flat-line vessel: 3.5 m3 gas, 20 m3 shell', dict(V0=3.5, Vtot=20.0, n=1.2, **DIFF15)),
                        ('v70', 'Design vessel: 7.0 m3 gas, 30 m3 shell', dict(V0=7.0, Vtot=30.0, n=1.2, **DIFF15))):
    r = run(Line(prof=prof), T=150, vessel=ves, record=REC, stride=1)
    td, ys = dec_group(r['t'], [r['hist'][k] for k in REC], 300)
    zz = base.z
    d['cases'].append(dict(key=key, label=label, pmax=r['Hmax'], pmin=r['Hmin'],
                           hmax=[r2(r['Hmax'][i] + zz[i]) for i in range(121)], hmin=[r2(r['Hmin'][i] + zz[i]) for i in range(121)],
                           line_min=min(r['Hmin']), at_min=r['i_min']*100, line_max=max(r['Hmax']), at_max=r['i_max']*100,
                           pump_min=r['Hmin'][0], gas_max=(r2(ves['Vg_max']) if ves else None), emptied=(ves['emptied'] if ves else None),
                           t=td, hist=[r1(y) for y in ys]))
    print('s11', key, d['cases'][-1]['line_min'], d['cases'][-1]['at_min'], d['cases'][-1]['line_max'], flush=True)
D['s11'] = d
json.dump(D, open(OUT + '/analyst.json', 'w'), separators=(',', ':'))
print('written')
