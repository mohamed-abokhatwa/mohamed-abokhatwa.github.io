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
