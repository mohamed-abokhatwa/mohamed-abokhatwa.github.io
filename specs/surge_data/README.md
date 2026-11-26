# Surge series — verified data

Every chart and figure in the seven surge-protection articles (`specs/s0*_*.py`) and in the
corrected `surge-vessel.html` and `pre-charge-pressure.html` is drawn from the files in this
folder, so the numbers on the pages can be reproduced.

- `moc.py` — method-of-characteristics transient solver with the discrete vapour cavity
  model (DVCM), upstream- and downstream-side flows kept distinct at cavity nodes.
  Boundaries: pump trip (instant, or a simplified homologous rundown with inertia, an ideal
  check valve, trapezoidal speed integration and a churning torque once the valve has closed),
  hydropneumatic vessel with asymmetric connection loss and a shell cap, spring relief valve
  opening in proportion to the actual head above its set point — all solved together at the
  pump node with a vapour cavity between the sources and the pipe — one-way feed tank at an
  interior node, downstream reservoir.
- `indep_moc.py` — an independent clean-room implementation written from the model
  specification only. On the audit test matrix it agrees with `moc.py` to 0.01 m on 89 of 92
  values; the other three differ because `moc.py` does not let the pump's hydraulic torque go
  negative.
- `dgcm.py` — discrete gas cavity model built on `indep_moc.py`. Collapse-governed peaks are
  model-sensitive, so every such peak is also computed with this model and the articles quote
  the range.
- `gen_datasets.py` — every scenario of the seven articles at 150 s; writes `datasets.json`.
- `closed_form.py` — Korteweg wave speed, air entrainment, orifice loss, bladder pre-charge
  (isothermal charging, polytropic discharge), compressor duty, relief valve capacity, flywheel
  inertia and motor acceleration time; writes `closed_form_refs.json` (reads `datasets.json`).
- `vessel_articles.py` — the sizing, iteration, sensitivity, pre-charge and gas-setting runs
  behind the two corrected vessel articles; writes `vessel_articles.json` (reads `datasets.json`).

Reference system: 12 km, DN800 ductile iron, Q = 2,520 m³/h (v = 1.39 m/s), a = 1,050 m/s,
HGL 85.0 m at the pump and 44.8 m at delivery, PN16 with 136 m allowable, +3.0 m minimum.

Run in this order (needs numpy for the two independent codes):

    python3 specs/surge_data/gen_datasets.py    specs/surge_data
    python3 specs/surge_data/closed_form.py     specs/surge_data
    python3 specs/surge_data/vessel_articles.py specs/surge_data

## Surge-analysis practice articles (s08–s11)

- `series_moc.py` — numpy MOC solver for pipes in series, each with its own length and wave speed,
  reproducing HAMMER's length and wave-speed adjustment; agrees with `moc.py` to 0.01 m on the uniform main.
- `gen_analyst.py` — every dataset behind `specs/s08_model_check.py`, `s09_pump_data.py`,
  `s10_pressure_limits.py` and `s11_surge_report.py`; writes `analyst.json`
  (`gen_datasets_helpers.py` holds the decimation helpers shared with `gen_datasets.py`).

    python3 specs/surge_data/gen_analyst.py specs/surge_data

## Surge-analysis practice articles, second set (s12–s19)

- `net_moc.py` — MOC solver for small networks: junction demands (fixed or orifice), branches,
  dead ends, vessels at junctions, pumps with a prescribed speed, a valve opening or a rundown, and
  in-line boosters with a bypass. It reproduces `moc.py` to 0.01 m on the reference main
  (unprotected trip, pump rundown, vessel); the check is stored under `checks` in `practice2.json`.
- `gen_practice2.py` — every dataset behind `specs/s12_*.py` to `specs/s19_*.py`; writes `practice2.json`.
  The filling article (s17) uses closed forms and a rigid-column ODE computed in the page itself.

    python3 specs/surge_data/gen_practice2.py specs/surge_data            # all sections
    python3 specs/surge_data/gen_practice2.py specs/surge_data s15 s19    # selected sections
