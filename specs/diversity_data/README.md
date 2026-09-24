# Chilled-water diversity — model data

Every number and chart in `specs/a25_chw_diversity.py` (chilled-water-diversity-megatall.html) comes
from `model.py`, an hour-by-hour design-day load model of an illustrative mixed-use Gulf megatall.

- Envelope: sun position for the site latitude on 21 July, a simple clear-sky model onto each façade
  (set for Gulf summer haze, about 690 W/m² direct normal at noon), a radiant time lag, conduction
  through glass and wall, and infiltration. Each floor is a core and four perimeter zones whose strips
  meet at 45° corners, so no floor area is counted twice.
- Internal gains on use-specific hourly schedules; ventilation cooled from outdoor to room enthalpy;
  900 kW of 24/7 process load.
- Two kinds of diversity kept apart: time diversity comes out of the hourly sum; statistical usage
  diversity f(n) = min(1, m + z·s/√n) applies to internal and occupancy-driven loads only.
- Coastal (42 °C, 20.5 g/kg) and inland (45.5 °C, 8 g/kg) design days, both illustrative.

    python3 specs/diversity_data/model.py specs/diversity_data     # writes model.json

All inputs are stated at the top of model.py and are illustrative; a project must use its own
climatic design data, schedules and usage statistics.


Correction, September 2026: the first version gave each perimeter zone the full façade length times
the perimeter depth, which counted the four corners twice and shrank the core. The tower block was
unchanged (21,043 kW coastal); the connected load rose from 24,346 to 24,538 kW and the coastal tower
coincidence moved from 0.864 to 0.858.
