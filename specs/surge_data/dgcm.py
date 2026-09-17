"""dgcm.py — discrete GAS cavity model (DGCM; Wylie 1984, Wylie & Streeter 1993 s.8.x, Bergant-Simpson-Tijsseling 2006)
as a peak-uncertainty cross-check on the DVCM collapse peaks.  Same grid, friction, boundaries (clean-room BCs).
Free gas lumped at every node: V_g = C3 / (H - z - HV),  C3 = alpha0 * A dx * 10.33 (alpha0 at atmospheric);
continuity with psi = 1:  V_g_new = V_g_old + dt (Q_D - Q_U).  No collapse rule: mass is conserved."""
import math, sys, time
import numpy as np
import os, sys as _sys
_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep_moc as IM

P_VAP = IM.P_VAP


def dgcm(line, bc0, t_end=150.0, tank=None, alpha0=1e-7):
    N, dt, B, R = line.N, line.dt, line.B, line.R
    z = line.z; s = z + P_VAP
    C3 = alpha0 * line.A * line.dx * 10.33
    H = line.H_steady.copy()
    QU = np.full(N + 1, line.Q0); QD = QU.copy()
    Vg = C3 / (H - s)
    bc0.bind(line)
    k = line.node_at(tank.xpos) if tank is not None else None
    drawn = 0.0
    p = H - z; pmax = p.copy(); pmin = p.copy(); tmax = np.zeros(N + 1)
    S0 = (H[1:N].sum() + 0.5 * (H[0] + H[N])) * dt / B
    src_in = 0.0; out_N = 0.0; Vg0_sum = Vg.sum()
    for n in range(1, int(round(t_end / dt)) + 1):
        t = n * dt
        CP = np.empty(N + 1); CM = np.empty(N + 1)
        CP[1:] = H[:-1] + B * QD[:-1] - R * QD[:-1] * np.abs(QD[:-1])
        CM[:-1] = H[1:] - B * QU[1:] + R * QU[1:] * np.abs(QU[1:])
        Hn = np.empty(N + 1); QUn = np.empty(N + 1); QDn = np.empty(N + 1); Vn = Vg.copy()
        # interior: (2dt/B) y^2 + b y - C3 = 0
        cp, cm, si, vo = CP[1:N], CM[1:N], s[1:N], Vg[1:N]
        a2 = 2.0 * dt / B
        b = vo + dt * (2.0 * si - cp - cm) / B
        disc = np.sqrt(b * b + 4.0 * a2 * C3)
        y = np.where(b > 0, 2.0 * C3 / (b + disc), (-b + disc) / (2.0 * a2))
        h = y + si
        Hn[1:N] = h; QUn[1:N] = (cp - h) / B; QDn[1:N] = (h - cm) / B; Vn[1:N] = C3 / y
        if k is not None:
            htank = z[k] + tank.level
            if Hn[k] < htank:
                Hn[k] = htank; QUn[k] = (CP[k] - htank) / B; QDn[k] = (htank - CM[k]) / B
                Vn[k] = C3 / (htank - s[k])
                drawn += dt * (QDn[k] - QUn[k]) - (Vn[k] - Vg[k])   # tank supply = Q_D - Q_U - dV_gas/dt
        # node 0: C3/y - V_old - dt((y+s0-CM)/B - q_src(y+s0)) = 0, decreasing in y
        cm0, s0, v0 = CM[0], s[0], Vg[0]
        def F(yy):
            HH = yy + s0
            return C3 / yy - v0 - dt * ((HH - cm0) / B - bc0.flow_at(HH))
        lo, hi = 1e-12, 1.0
        while F(hi) > 0: hi *= 2.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if mid <= lo or mid >= hi: break
            if F(mid) > 0: lo = mid
            else: hi = mid
        y0 = 0.5 * (lo + hi); H0 = y0 + s0; q_src = bc0.flow_at(H0)
        bc0.commit(H0, q_src, t, 'dgcm')
        Hn[0] = H0; QUn[0] = q_src; QDn[0] = (H0 - cm0) / B; Vn[0] = C3 / y0
        # node N reservoir
        Hn[N] = line.H_dn; QUn[N] = QDn[N] = (CP[N] - line.H_dn) / B
        src_in += 0.5 * dt * (QU[0] + QUn[0]); out_N += 0.5 * dt * (QU[N] + QUn[N])
        H, QU, QD, Vg = Hn, QUn, QDn, Vn
        p = H - z
        up = p > pmax; pmax[up] = p[up]; tmax[up] = t
        pmin = np.minimum(pmin, p)
    S1 = (H[1:N].sum() + 0.5 * (H[0] + H[N])) * dt / B
    mass_res = (S1 - S0) - (src_in - out_N + drawn + (Vg.sum() - Vg0_sum))   # liquid storage + free-gas growth
    im = int(np.argmax(pmax))
    return dict(pmax=[float(v) for v in pmax], pmin=[float(v) for v in pmin], lmax=float(pmax[im]), at=float(line.x[im]), tmax=float(tmax[im]), lmin=float(pmin.min()),
                n0max=float(pmax[0]), x6000=(float(pmax[line.node_at(6000.0)]) if line.L >= 6000 else None),
                vmax_free_gas=float(Vg.max()), drawn=drawn, mass_res=mass_res)


CASES = {
    'T1':        (lambda N: IM.Line(N=N), lambda: IM.StoppedPumpBC(), None, 150.0),
    'T2 a700':   (lambda N: IM.Line(a=700.0, N=N), lambda: IM.StoppedPumpBC(), None, 150.0),
    'T2 a1300':  (lambda N: IM.Line(a=1300.0, N=N), lambda: IM.StoppedPumpBC(), None, 150.0),
    'T5':        (lambda N: IM.Line(N=N), lambda: IM.VesselBC(V0=4.0, Vtot=8.0, Kout=0.5, Kin=0.5), None, 150.0),
    'T6 Hset95': (lambda N: IM.Line(N=N), lambda: IM.ReliefBC(95.0), None, 150.0),
    'T6 Hset120': (lambda N: IM.Line(N=N), lambda: IM.ReliefBC(120.0), None, 150.0),
    'T8i':       (lambda N: IM.Line(N=N, profile='knee'), lambda: IM.StoppedPumpBC(), None, 150.0),
    'T8ii':      (lambda N: IM.Line(N=N, profile='knee'), lambda: IM.StoppedPumpBC(), lambda: IM.Tank(level=8.0), 150.0),
}

if __name__ == '__main__':
    which = sys.argv[1:] or list(CASES)
    for name in which:
        mkline, mkbc, mktank, T = CASES[name]
        for N in (120, 240):
            for a0 in ((1e-7, 1e-8, 1e-6) if N == 120 else (1e-7,)):
                t0 = time.time()
                r = dgcm(mkline(N), mkbc(), t_end=T, tank=(mktank() if mktank else None), alpha0=a0)
                print('%-10s N=%3d alpha0=%.0e  line max %7.2f @ %5.0f m (%.1f s)  node-0 max %7.2f  line min %6.2f'
                      '  x6000 max %s  tank %s  mass res %.1e m3  [%.0f s]' %
                      (name, N, a0, r['lmax'], r['at'], r['tmax'], r['n0max'], r['lmin'],
                       ('%.2f' % r['x6000']) if r['x6000'] else '-', ('%.2f' % r['drawn']) if mktank else '-',
                       r['mass_res'], time.time() - t0), flush=True)
