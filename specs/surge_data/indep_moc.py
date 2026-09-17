#!/usr/bin/env python3
"""
Independent (clean-room) transient model built only from MODEL_SPEC.md.

Method of characteristics (Courant = 1, friction lumped per reach, explicit in the
characteristics) with the discrete vapour cavity model (DVCM, Wylie & Streeter 1993;
Bergant, Simpson & Tijsseling 2006).

State per node i (0..N):
    H[i]   hydraulic grade line (m)
    QU[i]  flow on the UPSTREAM side of the node   (end of reach i-1 .. i)
    QD[i]  flow on the DOWNSTREAM side of the node (start of reach i .. i+1)
    cav[i] vapour cavity volume (m3)
At a normal node QU == QD. At a cavity node (or the feed-tank node while it supplies)
they differ.  The C+ characteristic arriving at node i leaves node i-1 on its
downstream side (uses QD[i-1]); the C- characteristic arriving at node i leaves
node i+1 on its upstream side (uses QU[i+1]).

At node 0, QU[0] is the flow delivered by the sources (pump / check valve / vessel /
relief valve) and QD[0] is the flow entering the pipe; they differ only while a
cavity sits between the sources and the pipe.
"""
import json
import math
import sys
import time

import numpy as np

G = 9.81
RHO = 998.0
H_ATM = 10.33
P_VAP = -9.8          # vapour pressure head, m gauge

import os
OUT_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "indep_results.json")


# --------------------------------------------------------------------------- numerics
def solve_increasing(g, lo, hi):
    """Bisection to floating-point exhaustion for g increasing with g(lo) < 0 < g(hi)."""
    glo = g(lo)
    ghi = g(hi)
    if glo > 0 or ghi < 0:
        raise ValueError("root not bracketed: g(lo)=%r g(hi)=%r" % (glo, ghi))
    if glo == 0:
        return lo
    if ghi == 0:
        return hi
    for _ in range(400):
        mid = 0.5 * (lo + hi)
        if mid <= lo or mid >= hi:
            break
        gm = g(mid)
        if gm == 0:
            return mid
        if gm < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --------------------------------------------------------------------------- pipeline
class Line:
    def __init__(self, L=12000.0, D=0.800, a=1050.0, N=120, Q0=0.70,
                 H_up=85.0, H_dn=44.8, profile="flat", R_per_reach=None):
        self.L, self.D, self.a, self.N, self.Q0 = L, D, a, N, Q0
        self.H_up, self.H_dn, self.profile = H_up, H_dn, profile
        self.A = math.pi * D * D / 4.0
        self.dx = L / N
        self.dt = self.dx / a
        self.B = a / (G * self.A)
        self.R = (H_up - H_dn) / Q0 ** 2 / N if R_per_reach is None else R_per_reach
        self.x = np.arange(N + 1) * self.dx
        if profile == "flat":
            self.z = np.zeros(N + 1)
        elif profile == "knee":
            self.z = np.where(self.x <= 300.0, 30.0 * self.x / 300.0, 30.0)
        else:
            raise ValueError(profile)
        # steady HGL: exactly steady for the lumped scheme, linear H_up -> H_dn
        self.H_steady = H_up - np.arange(N + 1) * self.R * Q0 * abs(Q0)

    def node_at(self, x):
        k = int(round(x / self.dx))
        assert abs(k * self.dx - x) < 1e-9, "no node at x=%g" % x
        return k


# --------------------------------------------------------------------------- node-0 DVCM
def dvcm_node0(bc, CM, Hv, cav_old, r_old, psi, B, dt):
    """Upstream boundary with a possible cavity between the sources and the pipe.
    Returns H, Q_sources (QU0), Q_pipe (QD0), cavity volume, branch."""
    H, q = bc.solve_free(CM)
    if cav_old > 0.0 or H < Hv:
        qc = bc.flow_at(Hv)             # sources see vapour head
        QD = (Hv - CM) / B              # pipe side from C-
        c = cav_old + dt * (psi * (QD - qc) + (1.0 - psi) * r_old)
        if c > 0.0:
            return Hv, qc, QD, c, "cav"
    return H, q, q, 0.0, "free"


class Node0BC:
    name = "base"

    def bind(self, line):
        self.B = line.B
        self.dt = line.dt
        self.z0 = float(line.z[0])
        self.line = line

    def solve_free(self, CM):          # no cavity: H = CM + B*q(H)
        raise NotImplementedError

    def flow_at(self, H):              # source flow for a prescribed node head
        raise NotImplementedError

    def commit(self, H, q_src, t, branch):
        pass

    def step(self, CM, Hv, cav_old, r_old, psi, t):
        H, q, QD, c, br = dvcm_node0(self, CM, Hv, cav_old, r_old, psi, self.B, self.dt)
        self.commit(H, q, t, br)
        return H, q, QD, c

    def report(self):
        return {}


class ReservoirUpBC(Node0BC):
    """Constant-head upstream reservoir (validation only)."""
    name = "reservoir"

    def __init__(self, H=None):
        self.Hres = H

    def bind(self, line):
        super().bind(line)
        if self.Hres is None:
            self.Hres = float(line.H_steady[0])

    def solve_free(self, CM):
        return self.Hres, (self.Hres - CM) / self.B

    def flow_at(self, H):
        return (self.Hres - H) / self.B   # never used: head is fixed above vapour


class ConstFlowBC(Node0BC):
    """Pump delivering a fixed flow (steady / no-event validation)."""
    name = "const_flow"

    def __init__(self, Q):
        self.Q = Q

    def solve_free(self, CM):
        return CM + self.B * self.Q, self.Q

    def flow_at(self, H):
        return self.Q


class StoppedPumpBC(ConstFlowBC):
    """(a) instant pump stop, ideal check valve: no inflow from the pump side."""
    name = "instant_stop"

    def __init__(self):
        super().__init__(0.0)


class VesselBC(Node0BC):
    """(b) hydropneumatic vessel at node 0 (+ optional constant pump flow for validation)."""
    name = "vessel"

    def __init__(self, V0, Vtot=math.inf, Kout=0.5, Kin=0.5, n=1.2, Dc=0.4, pump_flow=0.0):
        self.V0, self.Vtot, self.Kout, self.Kin, self.n, self.Dc = V0, Vtot, Kout, Kin, n, Dc
        self.P = pump_flow

    def bind(self, line):
        super().bind(line)
        Ac = math.pi * self.Dc ** 2 / 4.0
        self.Rout = self.Kout / (2.0 * G * Ac * Ac)
        self.Rin = self.Kin / (2.0 * G * Ac * Ac)
        H0g = float(line.H_steady[0]) - self.z0          # 85.0 m gauge
        self.Cgas = (H0g + H_ATM) * self.V0 ** self.n
        self.V = self.V0
        self.q = 0.0
        self.Vmin = self.Vmax = self.V0
        self.qmax = 0.0
        self.qmin = 0.0
        self.emptied = False
        self.t_empty = None
        self.delivered = 0.0          # trapezoidal integral of vessel outflow
        self.clamp_excess = 0.0       # volume "delivered" beyond the shell (empty clamp)

    def gas_head(self, V):
        return self.Cgas / V ** self.n - H_ATM

    def loss(self, q):
        return (self.Rout if q > 0.0 else self.Rin) * q * abs(q)

    def Vp(self, q):
        return self.V + 0.5 * (self.q + q) * self.dt

    def _bracket(self, g):
        lo = -self.q - 2.0 * self.V * (1.0 - 1e-9) / self.dt     # gas volume -> ~0
        hi = max(1.0, lo + 1.0)
        while g(hi) < 0:
            hi = lo + 2.0 * (hi - lo)
        return lo, hi

    def _cap(self, q):
        if math.isinf(self.Vtot):
            return q
        qcap = 2.0 * (self.Vtot - self.V) / self.dt - self.q     # flow that just empties it
        if q > qcap:
            return qcap if qcap >= 0.0 else min(q, 0.0)
        return q

    def solve_free(self, CM):
        B, P, z0 = self.B, self.P, self.z0

        def g(q):
            return CM + B * (P + q) - z0 - self.gas_head(self.Vp(q)) + self.loss(q)
        q = solve_increasing(g, *self._bracket(g))
        q = self._cap(q)
        return CM + B * (P + q), P + q

    def flow_at(self, H):
        z0 = self.z0

        def g(q):
            return H - z0 - self.gas_head(self.Vp(q)) + self.loss(q)
        q = solve_increasing(g, *self._bracket(g))
        return self.P + self._cap(q)

    def commit(self, H, q_src, t, branch):
        q = q_src - self.P
        dV = 0.5 * (self.q + q) * self.dt
        Vn = self.V + dV
        self.delivered += dV
        if not math.isinf(self.Vtot) and Vn >= self.Vtot - 1e-9:
            if Vn > self.Vtot:
                self.clamp_excess += Vn - self.Vtot
            Vn = self.Vtot
            if not self.emptied:
                self.emptied = True
                self.t_empty = t
        self.V = Vn
        self.q = q
        self.Vmin = min(self.Vmin, Vn)
        self.Vmax = max(self.Vmax, Vn)
        self.qmax = max(self.qmax, q)
        self.qmin = min(self.qmin, q)

    def report(self):
        return {"gas_volume_min_m3": self.Vmin, "gas_volume_max_m3": self.Vmax,
                "gas_volume_final_m3": self.V, "vessel_emptied": self.emptied,
                "time_emptied_s": self.t_empty, "vessel_outflow_max_m3s": self.qmax,
                "vessel_inflow_max_m3s": -self.qmin,
                "vessel_delivered_trapz_m3": self.delivered,
                "gas_volume_change_m3": self.V - self.V0,
                "empty_clamp_excess_m3": self.clamp_excess}


class ReliefBC(Node0BC):
    """(d) surge relief valve at node 0 discharging to atmosphere, pump stopped."""
    name = "relief"

    def __init__(self, Hset, CdAv=0.6 * math.pi * 0.25 ** 2 / 4.0, lift=4.0, pump_flow=0.0):
        self.Hset, self.CdAv, self.lift, self.P = Hset, CdAv, lift, pump_flow

    def bind(self, line):
        super().bind(line)
        self.qr_old = 0.0
        self.qr_peak = 0.0
        self.t_peak = None
        self.released = 0.0

    def qr(self, H):
        h = H - self.z0
        if h <= self.Hset:
            return 0.0
        f = min(1.0, (h - self.Hset) / self.lift)
        return self.CdAv * f * math.sqrt(2.0 * G * h)

    def solve_free(self, CM):
        CMp = CM + self.B * self.P
        Hs = self.z0 + self.Hset
        if CMp <= Hs:
            return CMp, self.P
        H = solve_increasing(lambda H: H - CMp + self.B * self.qr(H), Hs, CMp)
        return H, self.P - self.qr(H)

    def flow_at(self, H):
        return self.P - self.qr(H)

    def commit(self, H, q_src, t, branch):
        qr = self.P - q_src
        self.released += 0.5 * (self.qr_old + qr) * self.dt
        self.qr_old = qr
        if qr > self.qr_peak:
            self.qr_peak = qr
            self.t_peak = t

    def report(self):
        return {"relief_flow_peak_m3s": self.qr_peak, "relief_flow_peak_time_s": self.t_peak,
                "relief_volume_released_m3": self.released}


class PumpRundownBC(Node0BC):
    """(c) pump rundown with ideal check valve that closes permanently on reversal."""
    name = "pump_rundown"

    def __init__(self, I, fixed_speed=False):
        self.I = I
        self.fixed = fixed_speed
        self.hs = 5.0
        self.c0 = 100.0
        self.k = 20.0 / 0.49
        self.omega0 = 1480.0 * 2.0 * math.pi / 60.0
        self.P0 = 685e3
        self.Tr = self.P0 / self.omega0
        self.eta = 0.80
        self.wind = 0.02
        self.churn = 0.45

    def bind(self, line):
        super().bind(line)
        self.w = 1.0
        self.w_trial = 1.0
        self.closed = False
        self.t_close = None
        self._rev = False
        self.hist_t = [0.0]
        self.hist_w = [1.0]
        self.max_iter = 0
        self.max_iter_change = 0.0
        Q0 = line.Q0
        Hp0 = float(line.H_steady[0]) - self.hs
        self.T_old = self.torque(1.0, Q0, Hp0, False)      # motor torque gone at t = 0+
        self.T_initial = self.T_old

    def torque(self, w, Q, Hp, closed):
        T = 0.0
        om = w * self.omega0
        if Q > 0.0 and om > 1e-12:
            T += RHO * G * Q * Hp / (self.eta * om)
        T += self.wind * self.Tr * w * w
        if closed:
            T += self.churn * self.Tr * w * w
        return T

    def solve_free(self, CM):
        if self.closed:
            self._rev = True
            return CM, 0.0
        w = self.w_trial
        c = CM - self.hs - self.c0 * w * w
        if c > 0.0:                      # pump flow would reverse
            self._rev = True
            return CM, 0.0
        self._rev = False
        Q = -2.0 * c / (self.B + math.sqrt(self.B * self.B - 4.0 * self.k * c))
        return CM + self.B * Q, Q

    def flow_at(self, H):
        if self.closed:
            return 0.0
        w = self.w_trial
        arg = (self.hs + self.c0 * w * w - H) / self.k
        return math.sqrt(arg) if arg > 0.0 else 0.0

    def step(self, CM, Hv, cav_old, r_old, psi, t):
        B, dt = self.B, self.dt
        if self.fixed:
            self.w_trial = 1.0
            H, q, QD, c, br = dvcm_node0(self, CM, Hv, cav_old, r_old, psi, B, dt)
            self.closed = self.closed or (br == "free" and self._rev)
            return H, q, QD, c
        a = dt / (self.I * self.omega0)
        w_g = max(self.w - a * self.T_old, 0.0)
        it = 0
        last = 0.0
        for it in range(1, 201):
            self.w_trial = w_g
            H, q, QD, c, br = dvcm_node0(self, CM, Hv, cav_old, r_old, psi, B, dt)
            closed_t = self.closed or (br == "free" and self._rev)
            T_new = self.torque(w_g, q, H - self.hs, closed_t)
            w_new = max(self.w - 0.5 * a * (self.T_old + T_new), 0.0)
            last = abs(w_new - w_g)
            if last < 1e-15:
                w_g = w_new
                break
            w_g = w_new
        self.max_iter = max(self.max_iter, it)
        self.max_iter_change = max(self.max_iter_change, last)
        self.w_trial = w_g
        H, q, QD, c, br = dvcm_node0(self, CM, Hv, cav_old, r_old, psi, B, dt)
        closed_t = self.closed or (br == "free" and self._rev)
        self.T_old = self.torque(w_g, q, H - self.hs, closed_t)
        if closed_t and not self.closed:
            self.t_close = t
        self.closed = closed_t
        self.w = w_g
        self.hist_t.append(t)
        self.hist_w.append(w_g)
        return H, q, QD, c

    def speed_at(self, t):
        return float(np.interp(t, self.hist_t, self.hist_w))

    def report(self):
        return {"check_valve_close_time_s": self.t_close, "speed_ratio_final": self.w,
                "T_rated_Nm": self.Tr,
                "rotor_max_iterations_per_step": self.max_iter,
                "rotor_worst_final_iteration_change": self.max_iter_change}


class Tank:
    """(e) one-way feed tank at an interior node."""

    def __init__(self, x=300.0, level=8.0, volume=800.0):
        self.xpos, self.level, self.volume = x, level, volume


# --------------------------------------------------------------------------- simulation
def simulate(line, bc0, t_end=150.0, downstream="reservoir", tank=None, psi=1.0,
             track_steady=False):
    N, dt, B, R = line.N, line.dt, line.B, line.R
    z = line.z
    Hv = z + P_VAP
    H = line.H_steady.copy()
    QU = np.full(N + 1, line.Q0)
    QD = QU.copy()
    cav = np.zeros(N + 1)
    bc0.bind(line)
    H_init, Q_init = H.copy(), line.Q0

    nsteps = int(round(t_end / dt))
    p = H - z
    pmax, pmin = p.copy(), p.copy()
    tmax, tmin = np.zeros(N + 1), np.zeros(N + 1)
    pmax_tr = np.full(N + 1, -np.inf)        # envelope over t > 0 only
    tmax_tr = np.zeros(N + 1)
    cavmax = np.zeros(N + 1)
    cav_total_max = 0.0
    steady_dev_H = steady_dev_Q = 0.0

    k = None
    tank_empty = False
    tank_active_old = False
    tank_drawn = 0.0
    tank_supply_max = 0.0
    tank_hist = [0.0]
    if tank is not None:
        k = line.node_at(tank.xpos)
        assert 0 < k < N

    node0_p = [float(p[0])]

    # mass-balance tallies
    S0 = H[1:N].sum() + 0.5 * (H[0] + H[N])
    acc = dict(flux0_pipe=0.0, fluxN=0.0, cav_trapz_interior=0.0, cav_trapz_node0=0.0,
               tank_trapz=0.0, friction_artifact=0.0, src_in=0.0)
    ident_step_max = 0.0
    discarded = 0.0          # cavity volume thrown away at collapse (vol<=0 rule)
    n_collapse = 0

    for n in range(1, nsteps + 1):
        t = n * dt
        fD = QD * np.abs(QD)
        fU = QU * np.abs(QU)
        CP = np.empty(N + 1)
        CM = np.empty(N + 1)
        CP[1:] = H[:-1] + B * QD[:-1] - R * fD[:-1]
        CM[:-1] = H[1:] - B * QU[1:] + R * fU[1:]

        Hn = np.empty(N + 1)
        QUn = np.empty(N + 1)
        QDn = np.empty(N + 1)
        cavn = np.zeros(N + 1)

        # ---- interior nodes 1..N-1
        cp, cm, hv = CP[1:N], CM[1:N], Hv[1:N]
        c_old = cav[1:N]
        r_old = (QD - QU)[1:N]
        hs = 0.5 * (cp + cm)
        qs = (cp - cm) / (2.0 * B)
        h_i, qu_i, qd_i = hs.copy(), qs.copy(), qs.copy()
        c_i = np.zeros(N - 1)
        trial = (c_old > 0.0) | (hs < hv)
        if trial.any():
            qu_c = (cp - hv) / B
            qd_c = (hv - cm) / B
            c_try = c_old + dt * (psi * (qd_c - qu_c) + (1.0 - psi) * r_old)
            keep = trial & (c_try > 0.0)
            coll = trial & ~keep & (c_old > 0.0)
            if coll.any():
                discarded += float(c_old[coll].sum())
                n_collapse += int(np.count_nonzero(coll))
            h_i[keep] = hv[keep]
            qu_i[keep] = qu_c[keep]
            qd_i[keep] = qd_c[keep]
            c_i[keep] = c_try[keep]
        tank_active_new = False
        if k is not None and not tank_empty:
            j = k - 1
            htank = z[k] + tank.level
            if hs[j] < htank:                       # check valve opens, tank holds the head
                h_i[j] = htank
                qu_i[j] = (cp[j] - htank) / B
                qd_i[j] = (htank - cm[j]) / B
                c_i[j] = 0.0
                tank_active_new = True
        Hn[1:N], QUn[1:N], QDn[1:N], cavn[1:N] = h_i, qu_i, qd_i, c_i

        # ---- node 0
        H0, QU0, QD0, c0 = bc0.step(CM[0], Hv[0], cav[0], QD[0] - QU[0], psi, t)
        if cav[0] > 0.0 and c0 == 0.0:
            discarded += float(cav[0])
            n_collapse += 1
        Hn[0], QUn[0], QDn[0], cavn[0] = H0, QU0, QD0, c0

        # ---- node N
        if downstream == "reservoir":
            Hn[N] = line.H_dn
            QUn[N] = QDn[N] = (CP[N] - line.H_dn) / B
        elif downstream == "closed":
            hsN = CP[N]
            done = False
            if cav[N] > 0.0 or hsN < Hv[N]:
                quc = (CP[N] - Hv[N]) / B
                ct = cav[N] + dt * (psi * (0.0 - quc) + (1.0 - psi) * (QD[N] - QU[N]))
                if ct > 0.0:
                    Hn[N], QUn[N], QDn[N], cavn[N] = Hv[N], quc, 0.0, ct
                    done = True
            if not done:
                Hn[N], QUn[N], QDn[N] = hsN, 0.0, 0.0
        else:
            raise ValueError(downstream)

        # ---- mass-balance tallies (exact discrete identity of the scheme)
        r_new = QDn - QUn
        r_prev = QD - QU
        half = 0.5 * dt
        s_old = r_prev[k] if (k is not None and tank_active_old) else 0.0
        s_new = r_new[k] if (k is not None and tank_active_new) else 0.0
        step_flux0 = half * (QD[0] + QDn[0])
        step_fluxN = half * (QU[N] + QUn[N])
        step_int = half * (r_prev[1:N].sum() + r_new[1:N].sum())
        step_tank = half * (s_old + s_new)
        step_node0cav = half * (r_prev[0] + r_new[0])
        step_fric = (R * dt / (2.0 * B)) * (fD[0] - fU[N] + (fD[1:N] - fU[1:N]).sum())
        S1 = Hn[1:N].sum() + 0.5 * (Hn[0] + Hn[N])
        step_dS = (S1 - (H[1:N].sum() + 0.5 * (H[0] + H[N]))) * dt / B
        step_res = step_dS - (step_flux0 - step_fluxN + step_int - step_fric)
        ident_step_max = max(ident_step_max, abs(step_res))
        acc["flux0_pipe"] += step_flux0
        acc["fluxN"] += step_fluxN
        acc["cav_trapz_interior"] += step_int - step_tank
        acc["tank_trapz"] += step_tank
        acc["cav_trapz_node0"] += step_node0cav
        acc["friction_artifact"] += step_fric
        acc["src_in"] += half * (QU[0] + QUn[0])

        if k is not None:
            tank_drawn += step_tank
            tank_supply_max = max(tank_supply_max, s_new)
            tank_hist.append(tank_drawn)
            if tank_drawn >= tank.volume:
                tank_empty = True
            tank_active_old = tank_active_new

        # ---- advance
        H, QU, QD, cav = Hn, QUn, QDn, cavn
        p = H - z
        up = p > pmax
        pmax[up] = p[up]
        tmax[up] = t
        up2 = p > pmax_tr
        pmax_tr[up2] = p[up2]
        tmax_tr[up2] = t
        dn = p < pmin
        pmin[dn] = p[dn]
        tmin[dn] = t
        np.maximum(cavmax, cav, out=cavmax)
        cav_total_max = max(cav_total_max, float(cav.sum()))
        node0_p.append(float(p[0]))
        if track_steady:
            steady_dev_H = max(steady_dev_H, float(np.max(np.abs(H - H_init))))
            steady_dev_Q = max(steady_dev_Q, float(max(np.max(np.abs(QU - Q_init)),
                                                        np.max(np.abs(QD - Q_init)))))

    S_end = H[1:N].sum() + 0.5 * (H[0] + H[N])
    dS_total = (S_end - S0) * dt / B
    cav_final = float(cav.sum())
    ident_res = dS_total - (acc["flux0_pipe"] - acc["fluxN"] + acc["cav_trapz_interior"]
                            + acc["tank_trapz"] - acc["friction_artifact"])
    # physical balance with tracked (psi-integrated, collapse-clipped) cavity volumes
    phys_rhs = acc["src_in"] - acc["fluxN"] + tank_drawn + cav_final
    phys_res = dS_total - phys_rhs
    cav_integration_diff = (acc["cav_trapz_interior"] + acc["cav_trapz_node0"]) - cav_final
    r_end = QD - QU
    open_nodes = cav > 0.0
    half_r_open = 0.5 * dt * float(r_end[open_nodes].sum())
    # for psi = 1: trapz(QD-QU) - tracked volume = discarded at collapses - dt/2 * r(open cavities at end)
    cav_diff_explained = discarded - half_r_open
    phys_closure = phys_res - (cav_integration_diff - acc["friction_artifact"])

    mass = {
        "pipe_storage_change_m3": dS_total,
        "source_inflow_node0_m3": acc["src_in"],
        "pipe_inflow_node0_m3": acc["flux0_pipe"],
        "outflow_reservoir_m3": acc["fluxN"],
        "tank_drawn_m3": tank_drawn,
        "cavity_volume_final_tracked_m3": cav_final,
        "cavity_volume_trapz_of_flows_m3": acc["cav_trapz_interior"] + acc["cav_trapz_node0"],
        "friction_artifact_m3": acc["friction_artifact"],
        "scheme_identity_residual_m3": ident_res,
        "scheme_identity_max_step_residual_m3": ident_step_max,
        "physical_balance_error_m3": phys_res,
        "physical_error_from_cavity_integration_m3": cav_integration_diff,
        "physical_error_from_friction_artifact_m3": -acc["friction_artifact"],
        "physical_balance_closure_after_decomposition_m3": phys_closure,
        "cavity_collapse_count": n_collapse,
        "cavity_volume_discarded_at_collapse_m3": discarded,
        "cavity_integration_diff_unexplained_m3": (cav_integration_diff - cav_diff_explained) if psi == 1.0 else None,
    }

    return {
        "line": line, "pmax": pmax, "pmin": pmin, "tmax": tmax, "tmin": tmin,
        "pmax_tr": pmax_tr, "tmax_tr": tmax_tr,
        "cavmax": cavmax, "cav_total_max": cav_total_max, "bc": bc0,
        "tank_drawn": tank_drawn, "tank_hist": tank_hist, "tank_node": k,
        "tank_supply_max": tank_supply_max, "tank_empty": tank_empty,
        "node0_p": node0_p, "mass": mass, "nsteps": nsteps,
        "steady_dev_H": steady_dev_H, "steady_dev_Q": steady_dev_Q,
        "H_final": H, "QU_final": QU, "QD_final": QD,
    }


# --------------------------------------------------------------------------- reporting
def env_summary(res):
    line = res["line"]
    x = line.x
    pmax, pmin = res["pmax"], res["pmin"]
    imax = int(np.argmax(pmax))
    vmin = float(pmin.min())
    at_min = np.where(pmin <= vmin + 1e-6)[0]
    return {
        "line_max_pressure_head_m": float(pmax[imax]),
        "line_max_chainage_m": float(x[imax]),
        "line_max_time_s": float(res["tmax"][imax]),
        "line_min_pressure_head_m": vmin,
        "line_min_chainage_first_m": float(x[at_min[0]]),
        "line_min_chainage_last_m": float(x[at_min[-1]]),
        "line_min_node_count": int(at_min.size),
        "line_max_after_t0_pressure_head_m": float(res["pmax_tr"].max()),
        "line_max_after_t0_chainage_m": float(x[int(np.argmax(res["pmax_tr"]))]),
        "line_max_after_t0_time_s": float(res["tmax_tr"][int(np.argmax(res["pmax_tr"]))]),
        "node0_max_pressure_head_m": float(pmax[0]),
        "node0_max_after_t0_pressure_head_m": float(res["pmax_tr"][0]),
        "node0_min_pressure_head_m": float(pmin[0]),
        "cavitating_node_count": int(np.count_nonzero(res["cavmax"] > 0)),
        "cavity_volume_max_single_node_m3": float(res["cavmax"].max()),
        "cavity_volume_max_total_m3": float(res["cav_total_max"]),
    }


def pmax_at(res, xpos):
    return float(res["pmax"][res["line"].node_at(xpos)])


def pmin_at(res, xpos):
    return float(res["pmin"][res["line"].node_at(xpos)])


def jclean(o):
    if isinstance(o, dict):
        return {k: jclean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jclean(v) for v in o]
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, (np.floating,)):
        o = float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, float) and (math.isinf(o) or math.isnan(o)):
        return None
    return o


# --------------------------------------------------------------------------- validation
def validation():
    out = {}

    # (1) no event: steady state must stay steady
    cases = [
        ("upstream_reservoir_flat", Line(), ReservoirUpBC(), None),
        ("pump_fixed_speed_flat", Line(), PumpRundownBC(100.0, fixed_speed=True), None),
        ("vessel_with_pump_flow_flat", Line(),
         VesselBC(V0=3.5, Vtot=20.0, Kout=2.0, Kin=10.0, pump_flow=0.70), None),
        ("relief_Hset95_with_pump_flow_flat", Line(), ReliefBC(95.0, pump_flow=0.70), None),
        ("const_flow_tank8_knee", Line(profile="knee"), ConstFlowBC(0.70), Tank(level=8.0)),
        ("vessel_tank16_knee", Line(profile="knee"),
         VesselBC(V0=20.9, Vtot=125.4, Kout=2.0, Kin=10.0, pump_flow=0.70), Tank(level=16.0)),
    ]
    steady = {}
    ok = True
    for name, line, bc, tank in cases:
        r = simulate(line, bc, t_end=150.0, tank=tank, track_steady=True)
        d = {"max_abs_dH_m": r["steady_dev_H"], "max_abs_dQ_m3s": r["steady_dev_Q"],
             "max_cavity_m3": float(r["cavmax"].max()), "tank_drawn_m3": r["tank_drawn"]}
        d["pass"] = (d["max_abs_dH_m"] < 1e-6 and d["max_abs_dQ_m3s"] < 1e-6
                     and d["max_cavity_m3"] == 0.0 and d["tank_drawn_m3"] == 0.0)
        ok = ok and d["pass"]
        steady[name] = d
    steady["all_pass"] = ok
    out["V1_steady_no_event"] = steady

    # (2) Joukowsky on a short frictionless line (no cavitation: high static head)
    jl = {}
    lineA = Line(L=1000.0, N=10, H_up=300.0, H_dn=300.0, R_per_reach=0.0)
    v = lineA.Q0 / lineA.A
    joukowsky = lineA.a * v / G
    rA = simulate(lineA, StoppedPumpBC(), t_end=20.0)
    jl["joukowsky_a_v_over_g_m"] = joukowsky
    jl["upstream_instant_stop_node0_drop_m"] = 300.0 - float(rA["pmin"][0])
    jl["upstream_instant_stop_node0_rise_m"] = float(rA["pmax"][0]) - 300.0
    lineB = Line(L=1000.0, N=10, H_up=300.0, H_dn=300.0, R_per_reach=0.0)
    rB = simulate(lineB, ReservoirUpBC(300.0), t_end=20.0, downstream="closed")
    jl["downstream_instant_closure_nodeN_rise_m"] = float(rB["pmax"][-1]) - 300.0
    jl["downstream_instant_closure_nodeN_drop_m"] = 300.0 - float(rB["pmin"][-1])
    # time the drop first reaches mid-line (should be L/(2a))
    errs = [abs(jl[k] - joukowsky) for k in jl if k.endswith("_m") and k != "joukowsky_a_v_over_g_m"]
    jl["max_abs_error_m"] = max(errs)
    jl["pass"] = jl["max_abs_error_m"] < 1e-9
    out["V2_joukowsky"] = jl

    return out


def mass_record(res):
    m = dict(res["mass"])
    scale = max(abs(m["outflow_reservoir_m3"]), abs(m["pipe_storage_change_m3"]),
                m["cavity_volume_trapz_of_flows_m3"], 1.0)
    m["scheme_identity_pass"] = abs(m["scheme_identity_residual_m3"]) < 1e-9 * scale * 10
    m["physical_decomposition_closes"] = (
        abs(m["physical_balance_closure_after_decomposition_m3"]) < 1e-9 * scale * 10
        and abs(m["cavity_integration_diff_unexplained_m3"]) < 1e-9 * scale * 10)
    bcr = res["bc"].report()
    if "vessel_delivered_trapz_m3" in bcr:
        m["vessel_delivered_minus_gas_volume_change_m3"] = (bcr["vessel_delivered_trapz_m3"]
                                                          - bcr["gas_volume_change_m3"])
        m["vessel_empty_clamp_excess_m3"] = bcr["empty_clamp_excess_m3"]
    return m


# --------------------------------------------------------------------------- test matrix
def run_matrix():
    R = {}
    mass = {}

    # T1
    t1 = {}
    for N in (120, 240):
        r = simulate(Line(N=N), StoppedPumpBC())
        e = env_summary(r)
        e["max_pressure_head_at_x6000_m"] = pmax_at(r, 6000.0)
        e["min_pressure_head_at_x6000_m"] = pmin_at(r, 6000.0)
        t1["N%d" % N] = e
        if N == 120:
            mass["T1_N120"] = mass_record(r)
    R["T1"] = t1

    # T2
    t2 = {}
    for a in (700.0, 1300.0):
        r = simulate(Line(a=a), StoppedPumpBC())
        t2["a%d" % int(a)] = env_summary(r)
    R["T2"] = t2

    # T3
    r = simulate(Line(), VesselBC(V0=3.08, Vtot=math.inf, Kout=0.5, Kin=0.5))
    e = env_summary(r)
    e.update(r["bc"].report())
    R["T3"] = e
    mass["T3"] = mass_record(r)

    # T4
    r = simulate(Line(), VesselBC(V0=3.5, Vtot=20.0, Kout=2.0, Kin=10.0))
    e = env_summary(r)
    e.update(r["bc"].report())
    R["T4"] = e
    mass["T4"] = mass_record(r)

    # T5
    r = simulate(Line(), VesselBC(V0=4.0, Vtot=8.0, Kout=0.5, Kin=0.5))
    e = env_summary(r)
    e.update(r["bc"].report())
    R["T5"] = e
    mass["T5"] = mass_record(r)

    # T6
    t6 = {}
    for hset in (95.0, 120.0):
        r = simulate(Line(), ReliefBC(hset))
        e = env_summary(r)
        e.update(r["bc"].report())
        t6["Hset%d" % int(hset)] = e
        if hset == 95.0:
            mass["T6_Hset95"] = mass_record(r)
    R["T6"] = t6

    # T7
    t7 = {}
    for I in (100.0, 400.0):
        r = simulate(Line(), PumpRundownBC(I))
        e = env_summary(r)
        e["speed_ratio_at_10s"] = r["bc"].speed_at(10.0)
        e.update(r["bc"].report())
        t7["I%d" % int(I)] = e
        mass["T7_I%d" % int(I)] = mass_record(r)
    R["T7"] = t7

    # T8
    t8 = {}
    cases = [
        ("i_no_protection", StoppedPumpBC(), None),
        ("ii_tank8_only", StoppedPumpBC(), Tank(level=8.0)),
        ("iii_tank8_plus_vessel", VesselBC(V0=20.9, Vtot=125.4, Kout=2.0, Kin=10.0), Tank(level=8.0)),
        ("iv_vessel_only", VesselBC(V0=43.1, Vtot=258.6, Kout=2.0, Kin=10.0), None),
    ]
    for name, bc, tank in cases:
        r = simulate(Line(profile="knee"), bc, tank=tank)
        e = env_summary(r)
        e["min_pressure_head_at_x300_m"] = pmin_at(r, 300.0)
        e["tank_volume_drawn_m3"] = r["tank_drawn"] if tank is not None else None
        e["tank_supply_max_m3s"] = r["tank_supply_max"] if tank is not None else None
        rep = r["bc"].report()
        e["gas_volume_max_m3"] = rep.get("gas_volume_max_m3")
        e.update(rep)
        t8[name] = e
        mass["T8_" + name] = mass_record(r)
    R["T8"] = t8

    # T9
    line9 = Line(profile="knee")
    r = simulate(line9, StoppedPumpBC(), t_end=600.0, tank=Tank(level=16.0))
    hist = np.array(r["tank_hist"])
    tt = np.arange(hist.size) * line9.dt
    v500 = float(np.interp(500.0, tt, hist))
    v600 = float(np.interp(600.0, tt, hist))
    rate = (v600 - v500) / 100.0
    Rtot = (85.0 - 44.8) / 0.7 ** 2
    rigid = math.sqrt(1.2 / (Rtot * 11700.0 / 12000.0))
    # instantaneous supply over the last steps (should equal the rate if quasi-steady)
    e = env_summary(r)
    e.update({
        "tank_draw_rate_last100s_m3s": rate,
        "tank_drawn_at_500s_m3": v500,
        "tank_drawn_at_600s_m3": v600,
        "tank_flow_final_instantaneous_m3s": float(r["QD_final"][r["tank_node"]] - r["QU_final"][r["tank_node"]]),
        "rigid_column_estimate_m3s": rigid,
        "relative_difference": rate / rigid - 1.0,
    })
    R["T9"] = e
    mass["T9"] = mass_record(r)

    # extra: DVCM weighting sensitivity for T1 (psi = 0.5) -- informational
    r = simulate(Line(), StoppedPumpBC(), psi=0.5)
    e = env_summary(r)
    e["max_pressure_head_at_x6000_m"] = pmax_at(r, 6000.0)
    extras = {"T1_N120_psi0.5": e}

    # grid refinement (N = 240) for the non-T1 cases -- informational
    ref = {}
    specs = [
        ("T2_a700_N240", Line(a=700.0, N=240), StoppedPumpBC(), None, "flat"),
        ("T3_N240", Line(N=240), VesselBC(V0=3.08, Kout=0.5, Kin=0.5), None, "flat"),
        ("T4_N240", Line(N=240), VesselBC(V0=3.5, Vtot=20.0, Kout=2.0, Kin=10.0), None, "flat"),
        ("T5_N240", Line(N=240), VesselBC(V0=4.0, Vtot=8.0, Kout=0.5, Kin=0.5), None, "flat"),
        ("T6_Hset95_N240", Line(N=240), ReliefBC(95.0), None, "flat"),
        ("T7_I100_N240", Line(N=240), PumpRundownBC(100.0), None, "flat"),
        ("T8_iii_N240", Line(N=240, profile="knee"),
         VesselBC(V0=20.9, Vtot=125.4, Kout=2.0, Kin=10.0), Tank(level=8.0), "knee"),
        ("T8_iv_N240", Line(N=240, profile="knee"),
         VesselBC(V0=43.1, Vtot=258.6, Kout=2.0, Kin=10.0), None, "knee"),
    ]
    for name, line, bc, tank, _ in specs:
        rr = simulate(line, bc, tank=tank)
        ee = env_summary(rr)
        rep_ = rr["bc"].report()
        for key in ("gas_volume_min_m3", "gas_volume_max_m3", "vessel_emptied",
                    "relief_flow_peak_m3s"):
            if key in rep_:
                ee[key] = rep_[key]
        if isinstance(bc, PumpRundownBC):
            ee["speed_ratio_at_10s"] = bc.speed_at(10.0)
        if tank is not None:
            ee["tank_volume_drawn_m3"] = rr["tank_drawn"]
        if line.profile == "knee":
            ee["min_pressure_head_at_x300_m"] = pmin_at(rr, 300.0)
        ref[name] = ee
    extras["grid_refinement_N240"] = ref

    return R, mass, extras


def main():
    t0 = time.time()
    val = validation()
    R, mass, extras = run_matrix()
    val["V3_mass_balance"] = mass
    val["V3_all_scheme_identities_pass"] = all(m["scheme_identity_pass"] for m in mass.values())
    val["V3_all_decompositions_close"] = all(m["physical_decomposition_closes"] for m in mass.values())
    t9 = R["T9"]
    val["V4_T9_rigid_column"] = {
        "model_rate_m3s": t9["tank_draw_rate_last100s_m3s"],
        "rigid_column_m3s": t9["rigid_column_estimate_m3s"],
        "relative_difference": t9["relative_difference"],
        "pass_within_1pct": abs(t9["relative_difference"]) < 0.01,
    }
    long = {}
    for T in (1500.0, 3000.0):
        line = Line(profile="knee")
        rr = simulate(line, StoppedPumpBC(), t_end=T, tank=Tank(level=16.0))
        hist = np.array(rr["tank_hist"])
        tt = np.arange(hist.size) * line.dt
        rate = (np.interp(T, tt, hist) - np.interp(T - 100.0, tt, hist)) / 100.0
        long["run_%ds_rate_last100s_m3s" % int(T)] = float(rate)
        long["run_%ds_relative_difference" % int(T)] = float(rate) / t9["rigid_column_estimate_m3s"] - 1.0
    P = 4 * 12000.0 / 1050.0
    line = Line(profile="knee")
    rr = simulate(line, StoppedPumpBC(), t_end=600.0, tank=Tank(level=16.0))
    hist = np.array(rr["tank_hist"])
    tt = np.arange(hist.size) * line.dt
    long["run_600s_rate_over_last_4_wave_periods_m3s"] = float(
        (np.interp(600.0, tt, hist) - np.interp(600.0 - 4 * P, tt, hist)) / (4 * P))
    sel = tt > 500.0
    s_inst = np.gradient(hist, line.dt)
    long["run_600s_instantaneous_supply_last100s_min_m3s"] = float(s_inst[sel].min())
    long["run_600s_instantaneous_supply_last100s_max_m3s"] = float(s_inst[sel].max())
    val["V4_T9_rigid_column"]["long_run_convergence"] = long
    val["V4_T9_rigid_column"]["long_run_pass_within_0.1pct"] = abs(long["run_3000s_relative_difference"]) < 1e-3
    out = dict(R)
    out["validation"] = val
    out["extras"] = extras
    out["model_notes"] = {
        "scheme": "MOC Courant=1, lumped explicit friction R*Q|Q| per reach, DVCM psi=1 (new-time flows)",
        "cavity_rule": "head held at z-9.8; QU from C+ (uses left neighbour QD), QD from C- (uses right neighbour QU); vol += (QD-QU)dt; vol<=0 -> collapse to single-flow solution",
        "envelopes": "max/min pressure head over t in [0,T] including the initial steady state",
        "vessel_empty": "outflow capped so gas volume reaches V_tot exactly; afterwards no outflow unless node head exceeds gas head",
        "pump_rotor": "trapezoidal integration of I dw/dt = -T, iterated to convergence each step",
        "tank_volume": "trapezoidal integral of tank supply (QD-QU) at the tank node",
        "runtime_s": None,
    }
    out["model_notes"]["runtime_s"] = time.time() - t0
    with open(OUT_JSON, "w") as f:
        json.dump(jclean(out), f, indent=2)
    return out


if __name__ == "__main__":
    main()
    print("wrote", OUT_JSON)
