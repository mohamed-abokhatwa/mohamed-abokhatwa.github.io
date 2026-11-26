"""
net_moc.py - method-of-characteristics solver for small tree networks, written for the
surge-analysis practice articles s15 (booster stations), s16 (demands and branches) and
s18 (normal operations).

One time step for the whole network; every pipe length is chosen as a whole number of
reaches of a*dt, so no wave speed or length is adjusted. Friction is lumped per reach
(steady-state consistent). Column separation by the discrete vapour cavity model at every
interior node and at junction nodes, with upstream-side and downstream-side flows kept
apart, as in moc.py.

Node kinds
  res      fixed head
  junc     junction: any number of pipes, optional demand: ('fixed', q) or ('orifice', q0)
           (an orifice demand passes q0 at the steady head and q0*sqrt(p/p0) after)
  pump     source at the start of one pipe: suction head, shut-off head, k, and either a
           prescribed speed w(t) or a rundown with inertia (constant-efficiency torque law,
           windage, churning torque after the check valve shuts, as moc.py), ideal check valve,
           optional discharge valve opening/closing (pump control valve)
  booster  pump between the end of pipe 'a' and the start of pipe 'b', with a bypass check
           valve (loss Kb) that passes forward flow when the booster's head falls away
Validated against moc.py on the uniform 12 km reference main (see gen_practice2.py).
"""
import math
import numpy as np
g = 9.81; HV = -9.8

class Pipe:
    def __init__(s, name, n0, n1, L, a, D, n_reach, Q0, H0_start, H0_end, R=None):
        s.name, s.n0, s.n1, s.L, s.a, s.D, s.n = name, n0, n1, L, a, D, n_reach
        s.A = math.pi*D*D/4; s.B = a/(g*s.A)
        s.dx = L/n_reach
        hf = H0_start - H0_end
        if R is not None: s.R = R*s.dx            # R given per metre of pipe
        else: s.R = (hf/(Q0*abs(Q0))/n_reach) if abs(Q0) > 1e-12 else 0.0   # lumped per reach
        s.H = np.linspace(H0_start, H0_end, n_reach+1)
        s.Q = np.full(n_reach+1, float(Q0)); s.QU = s.Q.copy()
        s.cav = np.zeros(n_reach+1)
        s.z = np.zeros(n_reach+1)
        s.Hmax = s.H.copy(); s.Hmin = s.H.copy()

def reaches(L, a, dt):
    n = L/(a*dt)
    assert abs(n - round(n)) < 1e-6, 'pipe length %.3f is not a whole number of reaches (%.4f)' % (L, n)
    return int(round(n))

class Net:
    def __init__(s, dt):
        s.dt = dt; s.pipes = {}; s.nodes = {}
    def pipe(s, name, n0, n1, L, a, D, Q0, H0_start, H0_end, z=None, R=None):
        p = Pipe(name, n0, n1, L, a, D, reaches(L, a, s.dt), Q0, H0_start, H0_end, R=R)
        if z is not None: p.z = np.array([z(i*p.dx) for i in range(p.n+1)])
        s.pipes[name] = p; return p
    def node(s, name, **kw):
        s.nodes[name] = dict(kw); return s.nodes[name]

def solve_dec(fun, lo, hi):
    """root of a decreasing function between lo and hi (bisection, then a few Newton-free refinements)"""
    flo, fhi = fun(lo), fun(hi)
    if flo <= 0: return lo
    if fhi >= 0: return hi
    for _ in range(80):
        m = 0.5*(lo+hi); fm = fun(m)
        if fm > 0: lo = m
        else: hi = m
        if hi - lo < 1e-10: break
    return 0.5*(lo+hi)

def run(net, T, record=(), stride=1):
    dt = net.dt
    P = net.pipes; Nd = net.nodes
    # incidence
    inc = {k: {'in': [], 'out': []} for k in Nd}
    for p in P.values():
        inc[p.n1]['in'].append(p); inc[p.n0]['out'].append(p)
    ncav = {k: 0.0 for k in Nd}
    for k, nd in Nd.items():
        if nd['kind'] == 'pump':
            nd['w'] = 1.0; nd['closed'] = False
            if nd.get('I'):
                p = inc[k]['out'][0]
                q0 = p.Q[0]; hp = p.H[0] - nd['Hsuc']
                nd['T_prev'] = 998*g*q0*max(hp, 0)/nd['eta']/nd['w0'] + 0.02*nd['P0']/nd['w0']
        if nd['kind'] == 'booster':
            nd['w'] = 1.0
            if nd.get('I'):
                pa = P[nd['a']]; pb = P[nd['b']]
                hp = pb.H[0] - pa.H[-1]
                nd['T_prev'] = 998*g*pa.Q[-1]*max(hp, 0)/nd['eta']/nd['w0'] + 0.02*nd['P0']/nd['w0']
        if nd['kind'] == 'junc' and nd.get('demand') and nd['demand'][0] == 'orifice':
            p = (inc[k]['in'] + inc[k]['out'])[0]
            Hn = p.H[-1] if p in inc[k]['in'] else p.H[0]
            zn = p.z[-1] if p in inc[k]['in'] else p.z[0]
            nd['Cd'] = nd['demand'][1]/math.sqrt(max(Hn - zn, 1e-6))
    steps = int(round(T/dt))
    hist = {r: [] for r in record}; th = []
    for n in range(steps):
        t = (n+1)*dt
        new = {}
        # interior nodes, per pipe, with DVCM
        for p in P.values():
            H, Q, QU, R, B = p.H, p.Q, p.QU, p.R, p.B
            HP = np.empty_like(H); QP = np.empty_like(Q); QUP = np.empty_like(Q)
            if p.n > 1:
                CP = H[:-2] + B*Q[:-2] - R*Q[:-2]*np.abs(Q[:-2])
                CM = H[2:] - B*QU[2:] + R*QU[2:]*np.abs(QU[2:])
                hl = 0.5*(CP+CM); zv = p.z[1:-1] + HV
                cavn = p.cav[1:-1]
                cavmode = (cavn > 0) | (hl < zv)
                hp_ = np.where(cavmode, zv, hl)
                qu = (CP - hp_)/B; qd = (hp_ - CM)/B
                cnew = np.where(cavmode, cavn + (qd - qu)*dt, 0.0)
                collapse = cavmode & (cnew <= 0)
                hp_ = np.where(collapse, hl, hp_)
                ql = (CP - CM)/(2*B)
                qu = np.where(cavmode & ~collapse, qu, ql); qd = np.where(cavmode & ~collapse, qd, ql)
                p.cav[1:-1] = np.where(collapse, 0.0, np.maximum(cnew, 0.0))
                HP[1:-1] = hp_; QP[1:-1] = qd; QUP[1:-1] = qu
            p._CPend = H[-2] + B*Q[-2] - R*Q[-2]*abs(Q[-2])
            p._CMstart = H[1] - B*QU[1] + R*QU[1]*abs(QU[1])
            new[p.name] = (HP, QP, QUP)
        # boundary nodes
        for k, nd in Nd.items():
            kind = nd['kind']; ins = inc[k]['in']; outs = inc[k]['out']
            if kind == 'res':
                for p in ins:
                    HP, QP, QUP = new[p.name]; HP[-1] = nd['H']; QP[-1] = QUP[-1] = (p._CPend - nd['H'])/p.B
                for p in outs:
                    HP, QP, QUP = new[p.name]; HP[0] = nd['H']; QP[0] = QUP[0] = (nd['H'] - p._CMstart)/p.B
            elif kind == 'junc':
                pp = ins + outs
                zn = (ins[0].z[-1] if ins else outs[0].z[0])
                dem = nd.get('demand')
                sb = sum(1/p.B for p in pp)
                sc = sum(p._CPend/p.B for p in ins) + sum(p._CMstart/p.B for p in outs)
                def qdem(h):
                    if not dem: return 0.0
                    if dem[0] == 'fixed': return dem[1]
                    return nd['Cd']*math.sqrt(max(h - zn, 0.0))
                ves = nd.get('vessel')
                if ves is not None and 'Cg' not in ves:
                    p0 = (ins[0].H[-1] if ins else outs[0].H[0])
                    ves['Cg'] = (p0 - zn + 10.33)*ves['V0']**ves.get('n', 1.2); ves['Vg'] = ves['V0']; ves['Qv'] = 0.0; ves['Vmax'] = ves['V0']
                def qves(h):        # vessel outflow (+) at node head h, trapezoidal gas volume
                    if ves is None: return 0.0
                    nn = ves.get('n', 1.2); Vh = ves['Vg'] + 0.5*ves['Qv']*dt
                    def F(q):
                        V = max(Vh + 0.5*q*dt, 1e-6); R = ves['Rout'] if q >= 0 else ves['Rin']
                        return ves['Cg']/V**nn - 10.33 + zn - R*q*abs(q) - h
                    return solve_dec(F, -2*Vh/dt + 1e-6, 20.0)
                if (dem and dem[0] == 'orifice') or ves is not None:
                    h = solve_dec(lambda h: sc - h*sb - qdem(h) + qves(h), zn - 60, max(sc/sb, zn) + 200)
                else:
                    h = (sc - qdem(0))/sb
                hv = zn + HV
                if ncav[k] > 0 or h < hv:
                    h2 = hv
                    qin = sum((p._CPend - h2)/p.B for p in ins) + qves(h2); qout = sum((h2 - p._CMstart)/p.B for p in outs) + qdem(h2)
                    c = ncav[k] + (qout - qin)*dt
                    if c > 0: ncav[k] = c; h = h2
                    else: ncav[k] = 0.0
                for p in ins:
                    HP, QP, QUP = new[p.name]; HP[-1] = h; QP[-1] = QUP[-1] = (p._CPend - h)/p.B
                for p in outs:
                    HP, QP, QUP = new[p.name]; HP[0] = h; QP[0] = QUP[0] = (h - p._CMstart)/p.B
                nd['q_now'] = qdem(h)
                if ves is not None:
                    qv = qves(h); ves['Vg'] = ves['Vg'] + 0.5*(ves['Qv'] + qv)*dt; ves['Qv'] = qv; ves['Vmax'] = max(ves['Vmax'], ves['Vg'])
            elif kind == 'pump':
                p = outs[0]; HP, QP, QUP = new[p.name]
                cm = p._CMstart; B = p.B
                tripped = nd.get('I') and t >= nd.get('trip_at', 0.0)
                if tripped:
                    w_old = nd['w']; w = max(0.0, w_old - nd['T_prev']/(nd['I']*nd['w0'])*dt)
                elif nd.get('wfun'):
                    w = nd['wfun'](t)
                else:
                    w = 1.0; w_old = 1.0
                kv = nd['vfun'](t) if nd.get('vfun') else 0.0     # extra valve loss coefficient (head/Q^2); inf = shut
                k_tot = nd['k'] + kv
                hs = nd['Hsuc'] + nd['H0']*w*w
                q = 0.0
                if not nd['closed'] and math.isfinite(k_tot):
                    # k q^2 + B q + (cm - hs) = 0
                    disc = B*B - 4*k_tot*(cm - hs)
                    if disc > 0:
                        q = (-B + math.sqrt(disc))/(2*k_tot) if k_tot > 0 else (hs - cm)/B
                    q = max(q, 0.0)
                    if q <= 0 and tripped: nd['closed'] = True
                h = cm + B*q
                if h < p.z[0] + HV:                                 # vapour at the pump
                    h = p.z[0] + HV; q = max(0.0, (h - cm)/B)
                HP[0] = h; QP[0] = QUP[0] = q
                if nd.get('I'):
                    if not tripped: w_old = 1.0
                    hp_rise = max(0.0, nd['H0']*w*w - nd['k']*q*q)
                    om = max(w*nd['w0'], 1e-3)
                    tq = (998*g*q*hp_rise/nd['eta']/om if q > 0 else 0.0) + 0.02*nd['P0']/nd['w0']*w*w
                    if q <= 0: tq += 0.45*nd['P0']/nd['w0']*w*w
                    if tripped: w = max(0.0, w_old - 0.5*(nd['T_prev'] + tq)/(nd['I']*nd['w0'])*dt)
                    nd['T_prev'] = tq
                nd['w'] = w; nd['q'] = q
            elif kind == 'booster':
                pa, pb = P[nd['a']], P[nd['b']]
                HA, QA, QUA = new[pa.name]; HB, QB, QUB = new[pb.name]
                cp, cm = pa._CPend, pb._CMstart
                btrip = nd.get('I') and t >= nd.get('trip_at', 0.0)
                if btrip:
                    w_old = nd['w']; w = max(0.0, w_old - nd['T_prev']/(nd['I']*nd['w0'])*dt)
                elif nd.get('wfun'):
                    w = nd['wfun'](t)
                else:
                    w = 1.0; w_old = 1.0
                def hp(q):   # head across the station at flow q >= 0: pump, or the bypass if better
                    return max(nd['H0']*w*w - nd['k']*q*q, -nd['Kb']*q*q)
                def f(q): return cp - pa.B*q + hp(q) - (cm + pb.B*q)
                q = solve_dec(f, 0.0, 10.0) if f(0.0) > 0 else 0.0
                hs = cp - pa.B*q
                zs = pa.z[-1] + HV
                if ncav[k] > 0 or hs < zs:                          # suction at vapour
                    hs2 = zs
                    qa = (cp - hs2)/pa.B
                    qq = solve_dec(lambda x: hs2 + hp(x) - (cm + pb.B*x), 0.0, 10.0) if hs2 + hp(0.0) > cm else 0.0
                    c = ncav[k] + (qq - qa)*dt
                    if c > 0:
                        ncav[k] = c; hs = hs2; q_up = qa; q = qq
                    else:
                        ncav[k] = 0.0; q_up = q
                else:
                    q_up = q
                hd = cm + pb.B*q
                HA[-1] = hs; QA[-1] = q_up; QUA[-1] = q_up
                HB[0] = hd; QB[0] = QUB[0] = q
                if nd.get('I'):
                    rise = max(0.0, hd - hs)
                    om = max(w*nd['w0'], 1e-3)
                    pumping = nd['H0']*w*w - nd['k']*q*q > -nd['Kb']*q*q
                    tq = (998*g*q*rise/nd['eta']/om if (q > 0 and pumping) else 0.0) + 0.02*nd['P0']/nd['w0']*w*w
                    if btrip: w = max(0.0, w_old - 0.5*(nd['T_prev'] + tq)/(nd['I']*nd['w0'])*dt)
                    nd['T_prev'] = tq
                nd['w'] = w; nd['q'] = q; nd['hs'] = hs; nd['hd'] = hd
        # boost into place; record
        for p in P.values():
            HP, QP, QUP = new[p.name]
            # interior-node upstream-side flow at the pipe end is the arriving flow
            p.H, p.Q, p.QU = HP, QP, QUP
            np.maximum(p.Hmax, HP, out=p.Hmax); np.minimum(p.Hmin, HP, out=p.Hmin)
        if n % stride == 0:
            th.append(round(t, 4))
            for r in record:
                if isinstance(r, tuple):
                    pn, i = r; hist[r].append(float(P[pn].H[i] - P[pn].z[i]))
                else:
                    nm, attr = r.split(':'); hist[r].append(float(Nd[nm].get(attr, 0.0)))
    return dict(t=th, hist=hist)

def envelope(net, pipes=None):
    """pressure-head envelopes along the listed pipes, as (x, max, min) with x continuing from pipe to pipe"""
    xs, mx, mn = [], [], []; x0 = 0.0
    for name in pipes:
        p = net.pipes[name]
        for i in range(p.n+1):
            if xs and i == 0: continue
            xs.append(round(x0 + i*p.dx, 2)); mx.append(round(float(p.Hmax[i] - p.z[i]), 2)); mn.append(round(float(p.Hmin[i] - p.z[i]), 2))
        x0 += p.L
    return xs, mx, mn
