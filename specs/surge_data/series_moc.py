"""
series_moc.py — numpy method-of-characteristics solver for a chain of pipes in series (same bore, each
pipe with its own length and wave speed), written for the surge-analysis practice articles.

Why it exists: Bentley HAMMER (and every MOC code) needs each pipe length to be a whole number of
reaches of length a*dt. With one time step for the whole model, a short pipe forces either a tiny
time step or an adjustment of that pipe's length or wave speed. This solver reproduces both
adjustment modes so their effect can be measured against a fine reference run.

  mode='length' : n_i = round(L_i/(a_i dt)) (at least 1); the pipe is modelled n_i*a_i*dt long (wave speed kept)
  mode='wave'   : same n_i; the wave speed becomes a_i' = L_i/(n_i dt) (length kept)
Friction is applied on the real length in both modes, so every run starts from the same steady state.

Boundaries: node 0 = stopped pump (ideal check valve) with an optional hydropneumatic vessel (same
trapezoidal gas-volume scheme and asymmetric connection loss as moc.py), or a constant-head reservoir;
node N = reservoir, optionally behind a valve closing linearly (the Joukowsky test).
No cavity model: the run reports `vapour=True` if any node falls below vapour, and such a run is not used.
"""
import math
import numpy as np
g = 9.81; HBAR = 10.33; HV = -9.8

def discretise(pipes, dt, mode):
    out = []
    for (L, a) in pipes:
        n = max(1, int(math.floor(L/(a*dt) + 0.5)))   # round half up, as JavaScript Math.round does
        if mode == 'length':
            out.append(dict(L=L, a=a, n=n, a_m=a, L_m=n*a*dt, adj=(n*a*dt - L)/L))
        else:
            a2 = L/(n*dt)
            out.append(dict(L=L, a=a, n=n, a_m=a2, L_m=L, adj=(a2 - a)/a))
    return out

def adjust_stats(pipes, dt, mode):
    d = discretise(pipes, dt, mode)
    adj = [abs(p['adj']) for p in d]
    return dict(max=max(adj), mean=sum(adj)/len(adj), rms=math.sqrt(sum(x*x for x in adj)/len(adj)),
                reaches=sum(p['n'] for p in d), worst=max(range(len(d)), key=lambda i: adj[i]))

def run(pipes, dt, mode='length', D=0.80, Q0=0.70, H_up=85.0, H_dn=44.8, T=150.0, vessel=None,
        up='pump', valve=None, record_x=(0.0,), stride=1):
    A = math.pi*D*D/4
    d = discretise(pipes, dt, mode)
    Ltot = sum(L for (L, a) in pipes)
    r_per_m = (H_up - H_dn - (valve['dH0'] if valve else 0.0))/(Q0*Q0)/Ltot   # friction per real metre
    Bs, Rs, xs = [], [], [0.0]
    for p in d:
        for k in range(p['n']):
            Bs.append(p['a_m']/(g*A)); Rs.append(r_per_m*p['L']/p['n'])
            xs.append(xs[-1] + p['L']/p['n'])
    Bs = np.array(Bs); Rs = np.array(Rs); xs = np.array(xs); N = len(Bs)
    H = H_up - r_per_m*Q0*Q0*xs
    Q = np.full(N+1, Q0)
    Bl = Bs[:-1]; Br = Bs[1:]; Rl = Rs[:-1]; Rr = Rs[1:]       # for interior nodes 1..N-1
    steps = int(round(T/dt))
    Hmax = H.copy(); Hmin = H.copy()
    rec_i = [int(np.argmin(np.abs(xs - x))) for x in record_x]
    t_hist = []; hist = {x: [] for x in record_x}; env_min = []; env_max = []
    if vessel:
        nn = vessel.get('n', 1.2); Vg = vessel['V0']; Cg = (H[0] + HBAR)*Vg**nn; Qv = 0.0
        Ro = vessel['R_out']; Ri = vessel['R_in']; vessel['Vg_max'] = Vg; vessel['Vg_min'] = Vg
    vapour = False
    for n in range(steps):
        t = (n+1)*dt
        HP = np.empty_like(H); QP = np.empty_like(Q)
        CP = H[:-2] + Bl*Q[:-2] - Rl*Q[:-2]*np.abs(Q[:-2])
        CM = H[2:] - Br*Q[2:] + Rr*Q[2:]*np.abs(Q[2:])
        QP[1:-1] = (CP - CM)/(Bl + Br); HP[1:-1] = CP - Bl*QP[1:-1]
        # downstream
        cp = H[-2] + Bs[-1]*Q[-2] - Rs[-1]*Q[-2]*abs(Q[-2])
        if valve:
            tau = max(0.0, 1.0 - t/valve['Tc']) if valve['Tc'] > 0 else 0.0
            # Q = tau*Q0*sqrt((h - H_dn)/dH0),  h = cp - B Q  -> quadratic in Q (forward flow)
            if tau <= 0.0:
                q = 0.0
            else:
                Cv = (tau*Q0)**2/valve['dH0']; b = Bs[-1]
                q = (-b*Cv + math.sqrt((b*Cv)**2 + 4*Cv*(cp - H_dn)))/2 if cp > H_dn else 0.0
            QP[-1] = q; HP[-1] = cp - Bs[-1]*q
        else:
            HP[-1] = H_dn; QP[-1] = (cp - H_dn)/Bs[-1]
        # upstream
        cm = H[1] - Bs[0]*Q[1] + Rs[0]*Q[1]*abs(Q[1])
        if up == 'reservoir':
            HP[0] = H_up; QP[0] = (H_up - cm)/Bs[0]
        elif vessel:
            Vh = Vg + 0.5*Qv*dt
            def f(q):
                V = max(Vh + 0.5*q*dt, 1e-9); R = Ro if q >= 0 else Ri
                h = Cg/V**nn - HBAR - R*q*abs(q)
                dh = -0.5*dt*nn*Cg/V**(nn+1) - 2*R*abs(q)
                return h - cm - Bs[0]*q, dh - Bs[0], h
            q = Qv
            for _ in range(60):
                F, dF, h = f(q); qn = q - F/dF
                if abs(qn - q) < 1e-12: q = qn; break
                q = qn
            h = f(q)[2]
            Vg = Vh + 0.5*q*dt; Qv = q
            vessel['Vg_max'] = max(vessel['Vg_max'], Vg); vessel['Vg_min'] = min(vessel['Vg_min'], Vg)
            HP[0] = h; QP[0] = q
        else:                       # stopped pump, nothing else: dead end
            QP[0] = 0.0; HP[0] = cm
        H, Q = HP, QP
        np.maximum(Hmax, H, out=Hmax); np.minimum(Hmin, H, out=Hmin)
        if H.min() < HV: vapour = True
        if n % stride == 0:
            t_hist.append(round(t, 4))
            for x, i in zip(record_x, rec_i): hist[x].append(float(H[i]))
            env_min.append(float(Hmin.min())); env_max.append(float(Hmax.max()))
    return dict(x=xs.tolist(), Hmax=Hmax.tolist(), Hmin=Hmin.tolist(), t=t_hist, hist=hist,
                env_min=env_min, env_max=env_max, vapour=vapour, N=N, disc=d, vessel=vessel,
                line_min=float(Hmin.min()), x_min=float(xs[int(np.argmin(Hmin))]), line_max=float(Hmax.max()),
                x_max=float(xs[int(np.argmax(Hmax))]))
