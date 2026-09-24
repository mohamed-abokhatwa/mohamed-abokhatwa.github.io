"""
model.py — hour-by-hour chilled-water load model of a mixed-use Gulf megatall, for the article
"Chilled-water diversity in megatall towers".

It is a design-day model, not an annual simulation: one clear summer day, 24 hourly values, built up
from four load sources for every zone of every floor —

  envelope   solar through glazing (sun position computed for the latitude and date, a simple clear-sky
             model, a radiant time lag) plus conduction through glass and wall;
  internal   people, lights and equipment, on a use-specific hourly schedule;
  outdoor    ventilation air cooled from the outdoor enthalpy to the room enthalpy (the outdoor air
             follows the design-day temperature cycle at constant humidity ratio);
  process    constant 24/7 loads (IT, telecom, lift machine and electrical rooms).

Two kinds of diversity are kept separate because they behave differently:

  time diversity        deterministic — loads peak at different hours (orientation, use, climate).
                        It comes out of the hour-by-hour sum; no factor is assumed.
  usage (statistical)   random — not every room, apartment or tenancy is at its full internal gain at
                        the same moment. Modelled per group of n independent units as
                        f(n) = min(1, m + z*s/sqrt(n)) on the internal and occupancy-driven loads only.
                        Weather-driven loads (envelope, outdoor air at design flow) get none.

usage: python3 specs/diversity_data/model.py specs/diversity_data     (writes model.json)
All inputs are stated below; they are illustrative and must be replaced by project data.
"""
import sys, json, math

HOURS = list(range(24))           # hour h covers h:00-h+1:00; loads are reported at the end of the hour

# ---------------------------------------------------------------- climate (illustrative design days)
# ASHRAE-style fraction of the daily range below the maximum, hour ending 1..24 (Fundamentals, Ch. 14)
DR_FRAC = [0.88, 0.92, 0.95, 0.98, 1.00, 0.98, 0.91, 0.74, 0.55, 0.38, 0.23, 0.13,
           0.05, 0.00, 0.00, 0.06, 0.14, 0.24, 0.39, 0.50, 0.59, 0.68, 0.75, 0.82]
CLIMATES = {
    'coastal': dict(label='Coastal Gulf (humid)', tmax=42.0, rng=9.0, w=0.0205, lat=21.5),
    'inland':  dict(label='Inland Gulf (dry)',    tmax=45.5, rng=14.0, w=0.0080, lat=24.7),
}
T_ROOM, W_ROOM = 24.0, 0.0093      # 24 C, ~50 % RH
def enthalpy(t, w): return 1.006*t + w*(2501 + 1.86*t)          # kJ/kg dry air
H_ROOM = enthalpy(T_ROOM, W_ROOM)

def weather(cl):
    c = CLIMATES[cl]
    t = [c['tmax'] - c['rng']*DR_FRAC[h] for h in HOURS]
    h = [enthalpy(x, c['w']) for x in t]
    return t, h

# ---------------------------------------------------------------- sun on the four façades (21 July)
def solar(lat_deg, day=202):
    """incident W/m2 on N, E, S, W vertical façades, hour by hour (solar time, mid-hour)"""
    dec = math.radians(23.45*math.sin(math.radians(360*(284 + day)/365)))
    lat = math.radians(lat_deg)
    out = {k: [] for k in 'NESW'}
    az_face = {'N': 180.0, 'E': -90.0, 'S': 0.0, 'W': 90.0}     # façade azimuth from south, west positive
    for hr in HOURS:
        hs = math.radians(15*((hr + 0.5) - 12))
        sin_alt = math.sin(lat)*math.sin(dec) + math.cos(lat)*math.cos(dec)*math.cos(hs)
        if sin_alt <= 0.01:
            for k in out: out[k].append(0.0)
            continue
        alt = math.asin(sin_alt)
        az = math.atan2(math.sin(hs)*math.cos(dec), math.cos(hs)*math.cos(dec)*math.sin(lat) - math.sin(dec)*math.cos(lat))
        am = 1/sin_alt
        eb = 1000*0.7**(am**0.678)                       # beam normal, simple clear-sky model
        edh = 0.12*eb                                    # diffuse on the horizontal
        egh = eb*sin_alt + edh
        for k, fa in az_face.items():
            cos_i = math.cos(alt)*math.cos(az - math.radians(fa))
            out[k].append(max(0.0, eb*cos_i) + 0.5*edh + 0.5*0.3*egh)
    return out

def lag(series, w=(0.45, 0.25, 0.14, 0.09, 0.07)):
    """radiant time lag for solar gain (a simplified radiant time series, repeating day)"""
    n = len(series)
    return [sum(w[k]*series[(h - k) % n] for k in range(len(w))) for h in range(n)]

# ---------------------------------------------------------------- schedules (fraction of full internal gain)
def sched(pts):
    """piecewise-constant schedule from {start_hour: value}"""
    out, v = [], 0.0
    keys = sorted(pts)
    for h in HOURS:
        for k in keys:
            if h >= k: v = pts[k]
        out.append(v)
    return out
SCHED = {
    'office':      sched({0: 0.10, 7: 0.40, 8: 0.85, 9: 1.00, 17: 0.60, 18: 0.30, 20: 0.10}),
    'hotel_rooms': sched({0: 0.90, 8: 0.60, 10: 0.35, 16: 0.55, 18: 0.80, 20: 1.00, 23: 0.95}),
    'hotel_public':sched({0: 0.05, 7: 0.40, 9: 0.30, 12: 1.00, 15: 0.40, 18: 0.70, 19: 1.00, 23: 0.30}),
    'residential': sched({0: 0.85, 6: 0.75, 8: 0.45, 16: 0.60, 18: 0.85, 19: 1.00, 23: 0.90}),
    'retail':      sched({0: 0.05, 9: 0.20, 10: 0.55, 13: 0.70, 16: 0.85, 18: 1.00, 23: 0.30}),
    'observation': sched({0: 0.00, 9: 0.30, 10: 0.55, 14: 0.75, 16: 1.00, 20: 0.80, 23: 0.20}),
}
# ventilation runs 24 h for hotel rooms and residences (DOAS), during operating hours elsewhere
VENT_ON = {
    'office':      sched({0: 0.0, 7: 1.0, 20: 0.0}),
    'hotel_rooms': [1.0]*24,
    'residential': [1.0]*24,
    'retail':      sched({0: 0.0, 9: 1.0, 24: 0.0}),
}

# ---------------------------------------------------------------- the tower (illustrative programme)
# per function: floors, plate m2, side m, floor-to-floor m, window-to-wall, SHGC, internal W/m2 at full
# schedule, ventilation L/s per m2, usage statistics (mean m, spread s, units per floor)
U_GLASS, U_WALL = 1.8, 0.45
INFIL_ACH = 0.15                      # air changes per hour on the floor volume (stack and wind on a tall facade)
FUNCS = {
    'retail':      dict(label='Retail podium',          floors=4,  plate=7000, ftf=6.0, wwr=0.30, shgc=0.25,
                        internal=52,  vent=1.00, vent_occ=True,  m=0.90, s=0.20, units=40, perim=4.5),
    'hotel_public':dict(label='Hotel ballroom, meeting & dining', floors=2, plate=3000, ftf=6.0, wwr=0.25, shgc=0.25,
                        internal=103, vent=3.00, vent_occ=True,  m=1.00, s=0.00, units=1,  perim=4.5),
    'office':      dict(label='Offices',                floors=40, plate=2200, ftf=4.2, wwr=0.70, shgc=0.25,
                        internal=36,  vent=0.55, vent_occ=False, m=0.85, s=0.20, units=4,  perim=4.5),
    'hotel_rooms': dict(label='Hotel guest rooms',      floors=30, plate=1600, ftf=3.6, wwr=0.50, shgc=0.25,
                        internal=19,  vent=0.40, vent_occ=False, m=0.85, s=0.35, units=30, perim=8.0),
    'residential': dict(label='Residences',             floors=50, plate=1400, ftf=3.6, wwr=0.60, shgc=0.25,
                        internal=19,  vent=0.35, vent_occ=False, m=0.75, s=0.30, units=8,  perim=8.0),
    'observation': dict(label='Observation deck & entertainment', floors=2, plate=1750, ftf=6.0, wwr=0.90, shgc=0.22,
                        internal=89,  vent=2.50, vent_occ=True,  m=1.00, s=0.00, units=1,  perim=6.0),
}
PROCESS_KW = 900.0                    # IT, telecom, lift machine and electrical rooms, 24/7
Z_DESIGN = 1.65                        # one-sided 95 % for the statistical usage allowance
# hydraulic zoning: plant feeds zone 1 directly and a cascade of heat exchangers above
ZONES = [
    dict(key='Z1', label='Zone 1 · direct from plant (podium + offices)', parts=[('retail', 1.0), ('hotel_public', 1.0), ('office', 1.0)]),
    dict(key='Z2', label='Zone 2 · HX-A (hotel rooms)',                   parts=[('hotel_rooms', 1.0)]),
    dict(key='Z3', label='Zone 3 · HX-B (lower residences)',               parts=[('residential', 30/50)]),
    dict(key='Z4', label='Zone 4 · HX-C (upper residences + deck)',        parts=[('residential', 20/50), ('observation', 1.0)]),
]

def usage_factor(f, n):
    """statistical coincidence of internal/occupancy load across n independent units"""
    return 1.0 if n <= 1 else min(1.0, f['m'] + Z_DESIGN*f['s']/math.sqrt(n))

def floor_zones(key, cl):
    """hourly loads (kW) for each zone of ONE floor of a function, split into components"""
    f = FUNCS[key]; t, h = weather(cl); sun = solar(CLIMATES[cl]['lat'])
    side, depth = f['side'] if 'side' in f else math.sqrt(f['plate']), f['perim']
    fac = side*f['ftf']; glass = fac*f['wwr']; wall = fac - glass
    per_area = side*depth
    core_area = max(0.0, f['plate'] - 4*per_area)
    zones = {}
    for o in 'NESW':
        sol = lag([f['shgc']*glass*x/1000 for x in sun[o]])
        cond = [(U_GLASS*glass + U_WALL*wall)*(t[i] - T_ROOM)/1000 for i in HOURS]
        env = [sol[i] + cond[i] for i in HOURS]
        zones[o] = dict(area=per_area, env=env)
    zones['core'] = dict(area=core_area, env=[0.0]*24)
    for z in zones.values():
        z['int'] = [z['area']*f['internal']*SCHED[key][i]/1000 for i in HOURS]
    # ventilation handled at the floor or DOAS, apportioned for reporting only
    if f['vent_occ']:
        vflow = [f['vent']*f['plate']*SCHED[key][i] for i in HOURS]          # people-driven (DCV)
    else:
        vflow = [f['vent']*f['plate']*VENT_ON[key][i] for i in HOURS]        # design ventilation rate
    vent = [1.2*vflow[i]*(h[i] - H_ROOM)/1000 for i in HOURS]                # kW
    # infiltration enters through the perimeter: share it over the four facade zones as envelope load
    infil = [1.2*(INFIL_ACH*f['plate']*f['ftf']/3.6)*(h[i] - H_ROOM)/1000 for i in HOURS]   # L/s x kJ/kg -> kW
    for o in 'NESW':
        zones[o]['env'] = [zones[o]['env'][i] + infil[i]/4 for i in HOURS]
    return zones, vent

def build(cl):
    res = {}
    for key, f in FUNCS.items():
        zones, vent = floor_zones(key, cl)
        n_units_floor = f['units']; n_units_all = f['units']*f['floors']
        # terminal (room / zone) peaks: every zone at its own peak, full usage, no ventilation
        term_peaks = {zk: max(z['env'][i] + z['int'][i] for i in HOURS) for zk, z in zones.items()}
        vent_peak = max(vent)
        env_floor = [sum(z['env'][i] for z in zones.values()) for i in HOURS]
        int_floor = [sum(z['int'][i] for z in zones.values()) for i in HOURS]
        uf_floor = usage_factor(f, n_units_floor); uf_all = usage_factor(f, n_units_all)
        vent_occ_share = 1.0 if f['vent_occ'] else 0.0
        def total(uf):
            return [env_floor[i] + uf*int_floor[i] + (uf if vent_occ_share else 1.0)*vent[i] for i in HOURS]
        floor_block = total(uf_floor)                     # one floor / one AHU or floor riser branch
        func_block = [x*f['floors'] for x in total(uf_all)]   # every floor of the function, statistical diversity at n_all
        res[key] = dict(
            label=f['label'], floors=f['floors'], area=f['plate']*f['floors'],
            terminal_peaks_floor=term_peaks, terminal_sum_floor=sum(term_peaks.values()), vent_peak_floor=vent_peak,
            connected=(sum(term_peaks.values()) + vent_peak)*f['floors'],          # every terminal and ventilation unit at its own peak
            floor_block=floor_block, floor_block_peak=max(floor_block),
            func_block=func_block, func_block_peak=max(func_block), func_block_hour=func_block.index(max(func_block)),
            env=[x*f['floors'] for x in env_floor], internal=[x*f['floors']*uf_all for x in int_floor],
            vent=[x*f['floors']*(uf_all if vent_occ_share else 1.0) for x in vent],
            uf_floor=round(uf_floor, 3), uf_all=round(uf_all, 3), units=n_units_all,
            internal_full=[x*f['floors'] for x in int_floor], vent_full=[x*f['floors'] for x in vent])
    proc = [PROCESS_KW]*24
    tower = [sum(r['func_block'][i] for r in res.values()) + proc[i] for i in HOURS]
    connected = sum(r['connected'] for r in res.values()) + PROCESS_KW
    sum_func_peaks = sum(r['func_block_peak'] for r in res.values()) + PROCESS_KW
    zones = []
    for z in ZONES:
        series = [sum(res[k]['func_block'][i]*share for k, share in z['parts']) for i in HOURS]
        if z['key'] == 'Z1': series = [series[i] + PROCESS_KW for i in HOURS]
        conn = sum(res[k]['connected']*share for k, share in z['parts']) + (PROCESS_KW if z['key'] == 'Z1' else 0)
        zones.append(dict(key=z['key'], label=z['label'], series=series, peak=max(series), hour=series.index(max(series)), connected=conn))
    # cascade: each heat exchanger carries its own zone and every zone above it, at their COINCIDENT hour
    hx = []
    for j, name in ((1, 'HX-A'), (2, 'HX-B'), (3, 'HX-C')):
        above = [sum(zones[k]['series'][i] for k in range(j, 4)) for i in HOURS]
        hx.append(dict(name=name, serves=[zones[k]['key'] for k in range(j, 4)], block=max(above), hour=above.index(max(above)),
                       sum_zone_peaks=sum(zones[k]['peak'] for k in range(j, 4))))
    th = tower.index(max(tower))
    for k, v in res.items():
        v['at_tower_peak'] = v['func_block'][th]
        v['floor_blocks_sum'] = v['floor_block_peak']*v['floors']
    levels = [
        ('Every terminal and ventilation unit at its own peak', connected),
        ('Sum of floor blocks (one AHU or riser branch per floor)', sum(v['floor_blocks_sum'] for v in res.values()) + PROCESS_KW),
        ('Sum of use blocks (all floors of each use)', sum_func_peaks),
        ('Sum of hydraulic zone blocks (HX duties)', sum(z['peak'] for z in zones)),
        ('Tower block (the plant)', max(tower)),
    ]
    return dict(functions=res, process=PROCESS_KW, tower=tower, tower_peak=max(tower), tower_hour=th, levels=levels,
                tower_min=min(tower), tower_min_hour=tower.index(min(tower)),
                connected=connected, sum_function_peaks=sum_func_peaks, zones=zones, hx=hx,
                weather=dict(zip(('t', 'h'), weather(cl))), h_room=H_ROOM)

def r(x, n=1):
    if isinstance(x, list): return [r(v, n) for v in x]
    if isinstance(x, dict): return {k: r(v, n) for k, v in x.items()}
    if isinstance(x, float): return round(x, n)
    return x

if __name__ == '__main__':
    OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
    D = {}
    for cl in CLIMATES:
        b = build(cl)
        D[cl] = dict(
            label=CLIMATES[cl]['label'], tower=r(b['tower']), tower_peak=r(b['tower_peak']), tower_hour=b['tower_hour'],
            connected=r(b['connected']), sum_function_peaks=r(b['sum_function_peaks']), process=b['process'],
            levels=[[a, r(v)] for a, v in b['levels']], tower_min=r(b['tower_min']), tower_min_hour=b['tower_min_hour'],
            zones=[dict(key=z['key'], label=z['label'], series=r(z['series']), peak=r(z['peak']), hour=z['hour'], connected=r(z['connected'])) for z in b['zones']],
            hx=[r(x) for x in b['hx']],
            t_out=r(b['weather']['t']), h_out=r(b['weather']['h']),
            functions={k: dict(label=v['label'], floors=v['floors'], area=v['area'], units=v['units'],
                               uf_floor=v['uf_floor'], uf_all=v['uf_all'],
                               terminal_peaks_floor=r(v['terminal_peaks_floor']), terminal_sum_floor=r(v['terminal_sum_floor']),
                               vent_peak_floor=r(v['vent_peak_floor']), floor_block_peak=r(v['floor_block_peak']),
                               connected=r(v['connected']), func_block_peak=r(v['func_block_peak']), func_block_hour=v['func_block_hour'],
                               series=r(v['func_block']), env=r(v['env'], 3), internal=r(v['internal'], 3), vent=r(v['vent'], 3),
                               at_tower_peak=r(v['at_tower_peak']), floor_blocks_sum=r(v['floor_blocks_sum']),
                               internal_raw=r(v['internal_full'], 3), vent_raw=r(v['vent_full'], 3))
                       for k, v in b['functions'].items()})
    D['inputs'] = dict(funcs=FUNCS, sched=SCHED, vent_on=VENT_ON, process_kw=PROCESS_KW, z=Z_DESIGN,
                       climates=CLIMATES, t_room=T_ROOM, w_room=W_ROOM, h_room=round(H_ROOM, 2),
                       u_glass=U_GLASS, u_wall=U_WALL, zones=ZONES)
    json.dump(D, open(OUT + '/model.json', 'w'), separators=(',', ':'))
    for cl in CLIMATES:
        d = D[cl]
        print(f"== {d['label']}: tower block {d['tower_peak']:.0f} kW at {d['tower_hour']}:00-{d['tower_hour']+1}:00 | "
              f"connected {d['connected']:.0f} | sum of function peaks {d['sum_function_peaks']:.0f} | "
              f"block/connected {d['tower_peak']/d['connected']:.3f} | block/sum-func {d['tower_peak']/d['sum_function_peaks']:.3f}")
        for k, v in d['functions'].items():
            print(f"   {k:13s} conn {v['connected']:7.0f}  floorblk {v['floor_block_peak']*v['floors']:7.0f}  func {v['func_block_peak']:7.0f} @ {v['func_block_hour']:2d}h"
                  f"  W/m2 {1000*v['func_block_peak']/v['area']:5.0f}  uf {v['uf_floor']:.2f}/{v['uf_all']:.2f}  term/floor {v['terminal_sum_floor']:.0f}")
        for z in d['zones']: print(f"   {z['key']} peak {z['peak']:7.0f} @ {z['hour']:2d}h  conn {z['connected']:7.0f}")
        for x in d['hx']: print(f"   {x['name']} block {x['block']:7.0f} @ {x['hour']}h vs sum of zone peaks {x['sum_zone_peaks']:.0f}")
        for a, v in d['levels']: print(f"   level {v:8.0f}  {v/d['connected']:.3f}  {a}")
        print(f"   night minimum {d['tower_min']:.0f} kW at {d['tower_min_hour']}h = {d['tower_min']/d['tower_peak']:.2f} of peak")
        for k, v in d['functions'].items():
            print(f"   {k:13s} at tower peak {v['at_tower_peak']:7.0f}  / own connected {v['at_tower_peak']/v['connected']:.2f}  / own block {v['at_tower_peak']/v['func_block_peak']:.2f}")
        area = sum(v['area'] for v in d['functions'].values())
        print(f"   area {area:.0f} m2 -> connected {1000*d['connected']/area:.0f} W/m2, block {1000*d['tower_peak']/area:.0f} W/m2, {area/(d['tower_peak']/3.517):.1f} m2/TR")
