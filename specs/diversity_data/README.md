# Chilled-water diversity — model data

Every number and chart in `specs/a25_chw_diversity.py` (chilled-water-diversity-megatall.html) comes
from `model.py`, an hour-by-hour design-day load model of an illustrative mixed-use Gulf megatall.

- Envelope: sun position for the site latitude on 21 July, a simple clear-sky model onto each façade,
  a radiant time lag, conduction through glass and wall, and infiltration.
- Internal gains on use-specific hourly schedules; ventilation cooled from outdoor to room enthalpy;
  900 kW of 24/7 process load.
- Two kinds of diversity kept apart: time diversity comes out of the hourly sum; statistical usage
  diversity f(n) = min(1, m + z·s/√n) applies to internal and occupancy-driven loads only.
- Coastal (42 °C, 20.5 g/kg) and inland (45.5 °C, 8 g/kg) design days, both illustrative.

    python3 specs/diversity_data/model.py specs/diversity_data     # writes model.json

All inputs are stated at the top of model.py and are illustrative; a project must use its own
climatic design data, schedules and usage statistics.
