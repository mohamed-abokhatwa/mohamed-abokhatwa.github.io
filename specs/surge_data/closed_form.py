import math, json, sys; sys.path.insert(0, sys.argv[1])
from moc import *
g=9.81; K=2.19e9; rho=998.0
out={}
def korteweg(D,e,E,c1): return math.sqrt((K/rho)/(1+(K*D)/(E*e)*c1))
# ---- A1: wave speed reference values
e_k9 = 9*(0.5+0.001*800)/1000       # ISO 2531 K-class nominal wall, DN800 K9
ref={}
for name,E,mu,D,e in (("Ductile iron DN800 K9",170e9,0.28,0.8,e_k9),("Steel DN800 e=10 mm",210e9,0.30,0.8,0.010),
                      ("Steel DN2000 e=20 mm",210e9,0.30,2.0,0.020),("GRP DN800 e=16 mm",11e9,0.25,0.8,0.016),
                      ("HDPE PE100 DN800 SDR17",1.1e9,0.45,0.8,0.8/17),("PVC DN300 e=11.7 mm",3.0e9,0.40,0.3,0.0117)):
    row={}
    for rest,c1 in (("anchored upstream",1-mu/2),("anchored throughout",1-mu*mu),("expansion joints",1.0)):
        row[rest]=round(korteweg(D,e,E,c1))
    ref[name]=dict(E_GPa=E/1e9,mu=mu,D_mm=D*1000,e_mm=round(e*1000,1),**row)
out['wave_speed_korteweg']=ref
def a_air(alpha,p_abs,a0,n=1.0):
    if alpha<=0: return a0
    return 1.0/math.sqrt(rho*(1.0/(rho*a0**2) + alpha/(n*p_abs)))
out['wave_speed_air_1050_isothermal']={f"{al*100:g}% @ {p} bar abs": round(a_air(al,p*1e5,1050.0)) for al in (0.001,0.005,0.01,0.02) for p in (2,5,10)}
# ---- A2: orifice loss (Idelchik thin sharp-edged orifice in a pipe, beta=d/D)
def K_orifice(beta):   # referred to the PIPE velocity
    return ((1 + 0.707*math.sqrt(1-beta**2) - beta**2)**2) / beta**4
out['orifice_K_pipe_velocity']={f"beta={b}": round(K_orifice(b),2) for b in (0.3,0.4,0.5,0.6,0.7,0.8)}
# peak vessel flows from the solver, free connection
A=math.pi*0.4**2/4; Rk=lambda Kk: Kk/(2*g*A*A)
ves=dict(V0=3.5,Vtot=20.0,n=1.2,R_out=Rk(0.5),R_in=Rk(0.5)); r=run(Line(),T=150,vessel=ves,record=(0,),stride=1)
q=r['extra']['Qv']                          # solver's vessel flow, unrounded
out['vessel_peak_flow_m3s']=dict(outflow=round(max(q),3), inflow=round(-min(q),3), DN400_velocity_out=round(max(q)/A,2))
# ---- A3: bladder vs air-over-water on the reference system
_DS=json.load(open(sys.argv[1]+'/datasets.json'))
_base=[c for c in _DS['wavespeed']['cases'] if c['a']==1050][0]
P_ss=85.0+10.33; P_min=3.0+10.33; gas_ss=_base['gas']; gas_min=_base['gas_max']; n=1.2   # MOC sizing, free DN400 connection
bl={}
# charging from pre-charge to the steady HGL is slow (isothermal); the transient discharge is fast (polytropic)
for f in (0.6,0.8,0.9,0.95):
    P_pre=f*P_min
    Vt=gas_ss*P_ss/P_pre                           # bladder shell: the pre-charge gas fills it, then is squeezed to 3.04 m3
    g_at_min=gas_ss*(P_ss/P_min)**(1/n)            # gas volume when the vessel is drawn down to the +3.0 m limit
    bl[f"precharge {f:.2f} x Pmin"]=dict(P_pre_m_abs=round(P_pre,2), total_m3=round(Vt,1), gas_at_min_m3=round(g_at_min,1),
                                         water_left_at_min_m3=round(Vt-g_at_min,1), ok=g_at_min<=Vt)
out['bladder_total_volume']=bl
out['air_over_water_total']=round(gas_min/0.8,1)
out['basis']=dict(gas_ss=gas_ss, gas_at_min_moc=gas_min, P_ss_m_abs=P_ss, P_min_m_abs=P_min, n=n)
for t_h in (1,2,4):
    out[f'compressor_FAD_recharge_{t_h}h_Nm3_per_min']=round(gas_ss*P_ss/10.33/(t_h*60),3)
# ---- A5: relief valve capacity checks
Qrel=[c for c in _DS['srv']['cases'] if c['set']==95.0][0]['q_peak']   # peak relief flow, DN250 set 95 m
ACC=4.0                                           # accumulation: the valve reaches full lift at Hset + 4 m
for dn in (100,150,200,250,300):
    A_=math.pi*(dn/1000)**2/4
    cap=0.6*A_*math.sqrt(2*g*(95.0+ACC))          # capacity at full lift, i.e. at the relieving head 99 m
    out[f'srv_DN{dn}_capacity_at_full_lift_set95_m3s']=round(cap,3)
Kv=Qrel*3600/math.sqrt(95.0*0.0981)
out['srv_required_Kv_m3h']=round(Kv); out['srv_required_Cv_US']=round(Kv*1.156)
# ---- A6: flywheel screening
w0=1480*2*math.pi/60; P=685e3; T_rated=P/w0
out['motor']=dict(w0_rad_s=round(w0,1),T_rated_Nm=round(T_rated))
for I in (25,100,400,800):
    out[f'accel_time_I{I}_at_50pct_rated_torque_s']=round(I*w0/(0.5*T_rated),1)
for r_,t_ in ((0.6,0.10),(0.8,0.12),(1.0,0.15)):
    m=7850*math.pi*r_*r_*t_; I=0.5*m*r_*r_
    out[f'steel_disc_r{r_}_t{t_}']=dict(mass_kg=round(m),I_kgm2=round(I),GD2=round(4*I))
json.dump(out, open(sys.argv[1]+'/closed_form_refs.json','w'), indent=1)
print(json.dumps(out, indent=1))
