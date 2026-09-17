"""
moc.py — method-of-characteristics transient solver for the surge series.
Reference system: 12 km, DN800 ductile iron, Q0 = 2520 m3/h, a = 1050 m/s, HGL 85.0 m at the pump,
44.8 m at delivery, flat profile at z = 0 unless a profile is given.
Boundaries: upstream pump (instant stop + ideal check valve, or a simplified homologous rundown with
inertia), hydropneumatic vessel with asymmetric connection loss and a shell cap, spring relief valve,
all solved together at node 0 with a vapour cavity between the sources and the pipe; one-way feed
tank at an interior node; downstream constant-head reservoir.
Column separation by the discrete vapour cavity model (DVCM, Wylie & Streeter 1993; Bergant, Simpson &
Tijsseling 2006), with the upstream-side and downstream-side flows kept distinct at cavity nodes.
Audited against an independent clean-room implementation (indep_moc.py). Collapse-governed peaks are
model-sensitive: dgcm.py gives the discrete gas cavity model for comparison.
"""
import math, json
g = 9.81
HV = -9.8          # vapour head relative to local elevation, gauge (m)
HBAR = 10.33       # atmospheric head (m)

class Line:
    def __init__(s, L=12000.0, D=0.80, a=1050.0, Q0=0.70, H_up=85.0, H_dn=44.8,
                 N=120, prof=None):
        s.L, s.D, s.a, s.Q0, s.N = L, D, a, Q0, N
        s.A = math.pi*D*D/4
        s.dx = L/N; s.dt = s.dx/a
        s.B = a/(g*s.A)
        hf = H_up - H_dn
        s.R = hf/(Q0*Q0)/N                       # lumped per reach
        s.z = [prof(i*s.dx) if prof else 0.0 for i in range(N+1)]
        s.H = [H_up - hf*i/N for i in range(N+1)]
        s.Q = [Q0]*(N+1)
        s.H_dn = H_dn

def run(line, T=90.0, vessel=None, pump=None, srv=None, feed=None, record=(0,), stride=2):
    L = line; N = L.N; dt = L.dt; B = L.B; R = L.R
    H, Q, z = L.H[:], L.Q[:], L.z
    steps = int(round(T/dt))
    hist = {k: [] for k in record}; t_hist = []; extra = {'Vg':[], 'Qv':[], 'w':[], 'feed':[]}
    Hmax = H[:]; Hmin = H[:]
    cav = [0.0]*(N+1)   # vapour cavity volume per node (fresh for every run)
    cav0 = 0.0          # vapour cavity at the upstream boundary (pump / vessel node)
    cav_lost = 0.0      # cavity volume deleted by the collapse rule (DVCM mass defect, m3)
    cav_max = [0.0]*(N+1)
    # vessel state
    if vessel:
        nn = vessel.get('n',1.2); zl = vessel.get('zl',0.0); Vtot = vessel.get('Vtot', 1e9)
        Rv_out = vessel.get('R_out', 0.0); Rv_in = vessel.get('R_in', 0.0)
        Vg = vessel['V0']; Habs0 = H[0] - z[0] - zl + HBAR
        Cg = Habs0 * Vg**nn
        Qv = 0.0
        vessel['Vg_min'] = Vg; vessel['Vg_max'] = Vg; vessel['Vtot'] = Vtot; vessel['emptied']=False
    # pump state (reset: a dict reused from an earlier run must not start with its check valve shut)
    if pump:
        w = 1.0      # normalised speed
        pump['closed'] = False
        # shaft torque at t = 0 (motor torque lost at t = 0+): hydraulic at the duty point + windage
        T_prev = 998*g*Q[0]*max(0.0, H[0] - z[0] - pump['Hsuc'])/max(pump['eta'],0.3)/pump['w0'] + pump.get('T_loss',0.02)*pump['P0']/pump['w0']
    if srv:
        srv['q_peak'] = 0.0
    if feed:
        feed['vol_used'] = 0.0; feed['open'] = False
    Qc = Q[:]           # flow on the UPSTREAM side of each node (differs from Q only at cavity / feed-tank nodes)
    for n in range(steps):
        t = (n+1)*dt
        HP = [0.0]*(N+1); QP = [0.0]*(N+1)
        Qo = Qc[:]      # upstream-side flows from the previous step (the C- characteristic arrives on that side)
        # interior nodes with DVCM
        for i in range(1, N):
            CP = H[i-1] + B*Q[i-1] - R*Q[i-1]*abs(Q[i-1])
            CM = H[i+1] - B*Qo[i+1] + R*Qo[i+1]*abs(Qo[i+1])
            if feed and i == feed['node']:
                lvl = z[i] + feed['level']
                h_try = 0.5*(CP+CM)
                room = feed['vol'] - feed['vol_used']
                if h_try < lvl and room > 0.0:
                    q_net = min(2.0*(lvl - h_try)/B, room/dt)   # tank supply = q_dn - q_up, capped by what is left
                    HP[i] = h_try + 0.5*B*q_net                # = lvl unless the tank runs dry in this step
                    if HP[i] < z[i] + HV:                      # ran dry and the node reaches vapour
                        HP[i] = z[i] + HV
                        cav[i] += ((2*HP[i] - CP - CM)/B - q_net)*dt
                    q_up = (CP - HP[i])/B; q_dn = (HP[i] - CM)/B
                    feed['vol_used'] += q_net*dt
                    QP[i] = q_dn
                    Qc[i] = q_up
                    continue
            if cav[i] > 0.0 or 0.5*(CP+CM) < z[i] + HV:
                HP[i] = z[i] + HV
                q_up = (CP - HP[i])/B        # arriving from upstream
                q_dn = (HP[i] - CM)/B        # leaving downstream
                cav[i] += (q_dn - q_up)*dt
                if cav[i] <= 0.0:
                    cav_lost += cav[i] - (q_dn - q_up)*dt
                    cav[i] = 0.0
                    HP[i] = 0.5*(CP+CM); QP[i] = (CP-CM)/(2*B); Qc[i] = QP[i]
                else:
                    QP[i] = q_dn; Qc[i] = q_up
            else:
                HP[i] = 0.5*(CP+CM); QP[i] = (CP-CM)/(2*B); Qc[i] = QP[i]
        # downstream reservoir
        CP = H[N-1] + B*Q[N-1] - R*Q[N-1]*abs(Q[N-1])
        HP[N] = L.H_dn; QP[N] = (CP - HP[N])/B; Qc[N] = QP[N]
        # ---- upstream boundary, node 0: ONE implicit solve for pump + vessel + relief valve + vapour cavity ----
        # pipe side (C-): q0 = (h - CM)/B.  Sources at node head h: pump through its check valve, vessel (trapezoidal
        # gas volume, asymmetric loss, shell cap), minus relief discharge.  Cavity between the sources and the pipe:
        # head held at vapour, cav0 += (q0 - sources)*dt; when that is <= 0 the cavity collapses and the node takes
        # the liquid solution (same DVCM rule as the interior nodes).
        if pump:                                 # rotor predictor: node 0 is solved with the end-of-step speed
            w_old = w; w = max(0.0, w_old - T_prev/(pump['I']*pump['w0'])*dt)
        CM = H[1] - B*Qo[1] + R*Qo[1]*abs(Qo[1])
        hv0 = z[0] + HV
        def pump_q(h):
            if pump and not pump['closed']:
                d = pump['Hsuc'] + pump['Hsh']*w*w - h
                if d > 0.0:
                    qp = math.sqrt(d/pump['k']); return qp, -0.5/(pump['k']*max(qp, 1e-6))
            return 0.0, 0.0
        def srv_q(h):
            if srv:
                p = h - z[0]; acc = max(srv.get('accum', 4.0), 1e-3); fr = (p - srv['Hset'])/acc
                if fr > 0.0:
                    s = math.sqrt(2*g*p); f1 = min(1.0, fr)
                    return srv['CdA']*f1*s, srv['CdA']*((1.0/acc if fr < 1.0 else 0.0)*s + f1*g/s)
            return 0.0, 0.0
        def solve_dec(fun, lo, hi, x):          # safeguarded Newton, fun decreasing, fun(lo) > 0 >= fun(hi)
            x = min(max(x, lo), hi)
            for _ in range(100):
                f, df = fun(x)
                if f > 0.0: lo = x
                else: hi = x
                xn = x - f/df if df < 0.0 else 0.5*(lo + hi)
                if not (lo < xn < hi): xn = 0.5*(lo + hi)
                if abs(xn - x) <= 1e-12*(1.0 + abs(x)): break
                x = xn
            return x
        def liquid_h(supply):                    # node head with a fixed vessel supply (none, or empty shell)
            def fun(h):
                qp, dqp = pump_q(h); qs, dqs = srv_q(h)
                return supply + qp - qs - (h - CM)/B, dqp - dqs - 1.0/B
            lo = min(CM, z[0] + srv['Hset'] if srv else CM) - 1.0
            hi = max(CM, pump['Hsuc'] + pump['Hsh']*w*w if pump else CM) + B*supply + 1.0
            return solve_dec(fun, lo, hi, H[0])
        if vessel:
            V_half = Vg + 0.5*Qv*dt
            q_lo = -2.0*V_half/dt + 1e-9                         # gas volume -> 0
            q_cap = max(0.0, 2.0*(Vtot - Vg)/dt - Qv)            # the water left in the shell
            def h_of(q):                                         # node head seen through the vessel
                Vn = max(V_half + 0.5*q*dt, 1e-9)
                Rv = Rv_out if q >= 0.0 else Rv_in
                return (Cg/Vn**nn - HBAR + z[0] + zl - Rv*q*abs(q), -0.5*dt*nn*Cg/Vn**(nn+1) - 2.0*Rv*abs(q))
            def node_q(q):                                       # decreasing in q; root = vessel flow
                h, dh = h_of(q); qp, dqp = pump_q(h); qs, dqs = srv_q(h)
                return h - CM - B*(q + qp - qs), dh*(1.0 - B*(dqp - dqs)) - B
            def vessel_at(h):                                    # vessel flow when the node head is h
                if h_of(q_cap)[0] >= h: return q_cap
                return solve_dec(lambda q: (h_of(q)[0] - h, h_of(q)[1]), q_lo, q_cap, Qv)
        def liquid():
            if not vessel:
                return liquid_h(0.0), 0.0
            H_top = h_of(0.0)[0]
            q_hi = max(0.0, (H_top - CM)/B + srv_q(H_top)[0]) + 1e-9
            if q_hi >= q_cap and node_q(q_cap)[0] > 0.0:
                return liquid_h(q_cap), q_cap                    # shell empty: node is a dead end
            qv = solve_dec(node_q, q_lo, min(q_hi, q_cap), Qv)
            return h_of(qv)[0], qv
        cavity = False
        if cav0 > 0.0:
            qv = vessel_at(hv0) if vessel else 0.0
            qp = pump_q(hv0)[0]
            c_new = cav0 + ((hv0 - CM)/B - qp - qv)*dt
            if c_new > 0.0:
                cavity = True; cav0 = c_new
            else:
                cav_lost += cav0
                cav0 = 0.0                                       # collapse: liquid solution this step
        if not cavity:
            h, qv = liquid()
            if h < hv0:                                          # a cavity forms
                qv = vessel_at(hv0) if vessel else 0.0
                qp = pump_q(hv0)[0]
                cav0 = max(0.0, ((hv0 - CM)/B - qp - qv)*dt)
                cavity = True
        if cavity:
            h = hv0; qs = 0.0
        else:
            qp = pump_q(h)[0]; qs = srv_q(h)[0]
        if not vessel: qv = 0.0
        parts = (qp, qv, qs)
        HP[0] = h; QP[0] = (h - CM)/B
        q_pump = qp
        if pump:
            I = pump['I']; P0 = pump['P0']; w0 = pump['w0']; H0 = pump['Hsh']; k = pump['k']
            if qp <= 0.0: pump['closed'] = True
            hp_rise = max(0.0, H0*w*w - k*qp*qp)
            omega = w*w0
            torque = 998*g*qp*hp_rise/max(pump['eta'],0.3)/max(omega,1e-3) if qp > 0 else 0.0
            torque += pump.get('T_loss',0.02)*P0/w0 * w*w
            if qp <= 0.0:
                torque += pump.get('T_shut',0.45)*P0/w0 * w*w
            w = max(0.0, w_old - 0.5*(T_prev + torque)/(I*w0)*dt)   # trapezoidal (Heun) rotor update
            T_prev = torque
        if vessel:
            Vnew = V_half + 0.5*qv*dt
            if Vnew >= Vtot:
                Vnew = Vtot; vessel['emptied'] = True             # reporting flag only
            Vg = Vnew; Qv = qv
            vessel['Vg_min'] = min(vessel['Vg_min'], Vg); vessel['Vg_max'] = max(vessel['Vg_max'], Vg)
        if srv and qs > 0.0:
            srv['q_peak'] = max(srv['q_peak'], qs)
        H, Q = HP, QP
        for i in range(N+1):
            c_ = cav0 if i == 0 else cav[i]
            if c_ > cav_max[i]: cav_max[i] = c_
        for i in range(N+1):
            if H[i] > Hmax[i]: Hmax[i] = H[i]
            if H[i] < Hmin[i]: Hmin[i] = H[i]
        if n % stride == 0:
            t_hist.append(round(t,3))
            for k in record: hist[k].append(round(H[k]-z[k],2))
            if vessel: extra['Vg'].append(round(Vg,3)); extra['Qv'].append(Qv)   # vessel outflow (+) / inflow (-), m3/s, unrounded
            if pump: extra['w'].append(round(w,4))
            if feed: extra['feed'].append(round(feed['vol_used'],2))
    x = [round(i*L.dx,1) for i in range(N+1)]
    return dict(t=t_hist, hist=hist, x=x,
                Hmax=[round(Hmax[i]-z[i],2) for i in range(N+1)],
                Hmin=[round(Hmin[i]-z[i],2) for i in range(N+1)],
                vessel=vessel, srv=srv, feed=feed, w_end=(w if pump else None), extra=extra,
                cav_lost=round(cav_lost, 3), cav_max=[round(v, 3) for v in cav_max],
                i_min=min(range(N+1), key=lambda i: Hmin[i]-z[i]), i_max=max(range(N+1), key=lambda i: Hmax[i]-z[i]))
