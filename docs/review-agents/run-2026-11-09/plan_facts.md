# Plan facts: house design, rural Alberta (Phase 0)

Facts only. No judgements, recommendations or severities. Every number carries a source: `file:line` (repo `/home/user/house`), "computed" with the formula (all computed tables are produced by `scripts/plan_facts.py` and pasted below), or a render measurement.

## 0. Header

- **Commit:** `d20a2fa` on `main` (repo read-only; `tools/make_drawings.py` not run). **OpenSCAD:** 2021.01. `python3 tools/check_layout.py`: main_floor.scad 52 rooms / 56 doors / 17 windows OK; basement.scad 20 rooms / 20 doors / 2 windows OK.
- **Method:** room, door, window and fixture tables come from `openscad -D audit=true` on `models/main_floor.scad` and `models/basement.scad` (same tables check_layout.py reads); other values from `models/export.scad` via `tools/model_data.py` (saved as `model.json`) and from reading the SCAD and docs. Source line numbers are mapped from each table row. Geometry (areas, unions, distances, routes) is computed with shapely/numpy in `scripts/plan_facts.py`; renders by `scripts/plot_plan.py`.
- **Coordinates:** feet; x = east, y = north; x = 0 is the garage's west wall; y = 0 is the front wall of the den and breakfast bay (main_floor.scad:5-8, house_lib.scad:1-5). Both levels share the frame.
- **Definitions used.**
  - *Room rectangle* = wall centre lines (house_lib.scad:19-24). "W x D c/l" = centre-line size; "clear" = c/l minus half of each bounding wall's thickness. Main floor: every wall is `wall_t` = 0.4 ft (house_lib.scad:40), exterior and interior alike (the model draws no thicker exterior wall). Basement outside walls: ICF 13.25 in = 1.104 ft (foundation.scad:37).
  - *Conditioned main floor* = main_rooms rows whose kind is not `porch` or `garage` (includes ceiling-0 hall zones and the STAIR DN stairwell footprint). *Basement* = all base_rooms rows except the EXIT STAIR areaway.
  - *Opening width* = the `width` field of a door row; the model draws the leaf at that full width (house_lib.scad:leaf()). "Approx clear" for a single swing door = opening - 1.5 in (a convention, not in the model).
  - *Exterior wall* = a room edge whose point 0.55 ft outside lies in no heated room; the outside is classed yard/soil, porch/patio (open, unconditioned), garage, or areaway.
  - *Circulation* = rooms of kind `hall` (halls, corridors, vestibules, landings), foyer excluded; foyer, mudroom and the stair are separate lines (§6).
  - *Outside corner* = convex vertex of the heated-envelope polygon; inside corner = reflex vertex.
- **Source caveat:** the audit tables carry no fixture-type field; wet fixtures and appliances are identified by hand from box coordinates and the source-line comments (boxes are listed in §9 so the mapping can be checked).

## 1. Envelope and areas

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 5486.2 | computed: sum (x1-x0)*(y1-y0) over 38 rows, main_floor.scad:47-104 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 53.8 | main_floor.scad:64 |
| Main-floor conditioned excluding the stair opening | 5432.4 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 5486.2 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 3475.0 | computed over basement.scad:54-74 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 832.7 | main_floor.scad:47 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| SIDE ENTRY | 83.7 | main_floor.scad:48 |
| PATIO | 193.4 | main_floor.scad:72 |
| FRONT PORCH | 796.1 | main_floor.scad:94 |
| (unlabelled porch) @49.24,0 | 30.5 | main_floor.scad:95 |
| (unlabelled porch) @95.95,0 | 50.8 | main_floor.scad:96 |
| (covered entry) | 44.6 | main_floor.scad:97 |
| DECK | 322.4 | main_floor.scad:98 |
| OFFICE PORCH | 146.9 | main_floor.scad:99 |
| MASTER PORCH | 175.1 | main_floor.scad:100 |
| SIDE PORCH | 320.3 | main_floor.scad:101 |
| (unlabelled porch) @128.13,26.84 | 25.4 | main_floor.scad:102 |
| (study stoop) | 14.6 | main_floor.scad:103 |
| (garage side-door pad) | 17.5 | main_floor.scad:104 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 2221.3 sq ft. PATIO alone: 193.4; DECK alone: 322.4. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 395.5 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 138.3 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 225.4 ft | same |
|   facing garage | 31.7 ft | same (garage is unheated) |
| Outside (convex) corners | 17 | vertices of the union polygon after 0.02 ft simplify (30 vertices) |
| Inside (reflex) corners | 13 | same polygon |
| Bounding box, heated rooms | x 7.27..128.13 (120.86 ft), y 0..66.64 (66.64 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 0..137.66 (137.66 ft), y -15.26..66.64 (81.9 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 16 hip-roof blocks in main_roof (main_floor.scad:305); each hip block is 4 sloped facets, so 4 x 16 = 64 nominal facets before overlapping blocks merge; 9 blocks at 6/12 pitch, 7 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)


## 2. Orientation

### 2.1 Compass, road and driveway

- **North = +y.** main_floor.scad:5-8 ("x = east, y = north"); house_lib.scad:1. The front porch is at y < 0 (south): FRONT PORCH y -15.26..0 (main_floor.scad:94); the great-room deck and office/master porches are at y > 52 (north) (main_floor.scad:98-100); the side porch is on the east (main_floor.scad:101).
- **Road: south.** "The road is assumed along the south side" (site.scad:8); road north edge y = -100 (site.scad:74). Land is not chosen; positions are relative to the house (site.scad:6-8).
- **Driveway: west side.** Drive from the road up the west side to the garage's west-facing doors (site.scad:11-12; rectangle x -32..-2, y -100..42, site.scad:111) plus a front loop south of the house (x 25..130, y -72..-14, site.scad:113-117). Garage doors: west facade, axis y at x = 0 (main_floor.scad:117-118). Services corridor on the west side of the drive (site.scad:14-17, 162-164). Septic tank and field west; well east (site.scad:63, 70-73). Shop (later) north at x 0..100, y 130..230 (site.scad:56-60).
- **Facade summary:** garage W (doors), front porch/foyer/den/breakfast/kitchen S, great room/deck/sun room/office/master N, master suite and side porch E (computed in §2.2 and §5).

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| SCULLERY | S 11.3 (porch/patio (open)); W 8.7 (garage) | main_floor.scad:49 |
| MUDROOM | S 2.2 (garage) | main_floor.scad:50 |
| LAUNDRY | none | main_floor.scad:51 |
| BEDROOM 2 | S 14.8 (garage); W 3.1 (porch/patio (open)), 9.6 (yard/soil) | main_floor.scad:53 |
| (suite entry) | none | main_floor.scad:54 |
| (suite entry, 2nd piece) | none | main_floor.scad:55 |
| WIC @7.27,48.13 | W 3.0 (yard/soil) | main_floor.scad:56 |
| WC @7.27,51.15 | W 4.2 (yard/soil) | main_floor.scad:57 |
| BATH 2 | N 10.2 (yard/soil); W 6.7 (yard/soil) | main_floor.scad:58 |
| BUNK ROOM | N 15.1 (yard/soil); E 3.2 (yard/soil); W 4.6 (yard/soil) | main_floor.scad:59 |
| STUDY | N 4.6 (porch/patio (open)), 5.4 (yard/soil) | main_floor.scad:60 |
| HALL @22.1,49.64 | none | main_floor.scad:62 |
| (N-S hall, unlabelled) | none | main_floor.scad:63 |
| STAIR DN | none | main_floor.scad:64 |
| (landing at the stair top) | none | main_floor.scad:65 |
| (upper hall, west of its door) | none | main_floor.scad:66 |
| HALL @53.95,45.39 | N 15.2 (porch/patio (open)) | main_floor.scad:67 |
| BATH | none | main_floor.scad:68 |
| FLEX ROOM | none | main_floor.scad:69 |
| SUN ROOM | N 11.3 (yard/soil); E 12.7 (porch/patio (open)) | main_floor.scad:70 |
| HALL @24.34,29.51 | W 6.0 (garage) | main_floor.scad:73 |
| GREAT ROOM | N 26.5 (porch/patio (open)); E 4.4 (porch/patio (open)); W 1.8 (porch/patio (open)) | main_floor.scad:75 |
| KITCHEN / DINING | S 4.9 (porch/patio (open)), 13.6 (yard/soil); W 7.4 (porch/patio (open)), 7.1 (yard/soil) | main_floor.scad:76 |
| BREAKFAST | S 15.0 (porch/patio (open)); E 3.7 (porch/patio (open)); W 6.3 (porch/patio (open)) | main_floor.scad:77 |
| FOYER | S 12.0 (porch/patio (open)) | main_floor.scad:78 |
| DEN | S 14.8 (porch/patio (open)); E 9.3 (porch/patio (open)); W 3.7 (porch/patio (open)) | main_floor.scad:79 |
| (den alcove) | S 3.8 (porch/patio (open)) | main_floor.scad:80 |
| OFFICE | N 13.0 (porch/patio (open)) | main_floor.scad:82 |
| MASTER BEDROOM | N 18.4 (porch/patio (open)); E 23.4 (porch/patio (open)); W 4.7 (porch/patio (open)) | main_floor.scad:83 |
| (master entry) | none | main_floor.scad:84 |
| WIC @95.95,20.56 | none | main_floor.scad:85 |
| (closet passage) | none | main_floor.scad:86 |
| WIC @111.41,20.56 | none | main_floor.scad:87 |
| LINEN | N 1.2 (porch/patio (open)); E 2.7 (porch/patio (open)), 6.3 (yard/soil) | main_floor.scad:88 |
| MASTER BATH | S 21.6 (yard/soil); E 11.2 (yard/soil) | main_floor.scad:89 |
| WC @99.7,16.71 | none | main_floor.scad:90 |
| (linen between the WCs) | none | main_floor.scad:91 |
| WC @99.7,9.31 | S 1.7 (porch/patio (open)), 5.1 (yard/soil) | main_floor.scad:92 |


## 3. Room tables

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SCULLERY | 24.34 | 20.82 | 35.6 | 29.51 | 11.26 x 8.69 | 10.9 x 8.3 | 98 | 90 | 1.30 | utility | 12 | main_floor.scad:49 |
| MUDROOM | 22.1 | 35.46 | 37.3 | 40.56 | 15.20 x 5.10 | 14.8 x 4.7 | 78 | 70 | 2.98 | utility | 10 | main_floor.scad:50 |
| LAUNDRY | 22.1 | 40.56 | 37.3 | 49.64 | 15.20 x 9.08 | 14.8 x 8.7 | 138 | 128 | 1.67 | utility | 10 | main_floor.scad:51 |
| BEDROOM 2 | 7.27 | 35.46 | 22.1 | 48.13 | 14.83 x 12.67 | 14.4 x 12.3 | 188 | 177 | 1.17 | bed | 10 | main_floor.scad:53 |
| (suite entry) | 13.78 | 48.13 | 22.1 | 53.75 | 8.32 x 5.62 | 7.9 x 5.2 | 47 | 41 | 1.48 | hall | 10 | main_floor.scad:54 |
| (suite entry, 2nd piece) | 13.78 | 53.75 | 17.5 | 55.3 | 3.72 x 1.55 | 3.3 x 1.1 | 6 | 4 | 2.40 | hall | 0 | main_floor.scad:55 |
| WIC @7.27,48.13 | 7.27 | 48.13 | 13.78 | 51.15 | 6.51 x 3.02 | 6.1 x 2.6 | 20 | 16 | 2.16 | closet | 10 | main_floor.scad:56 |
| WC @7.27,51.15 | 7.27 | 51.15 | 13.78 | 55.3 | 6.51 x 4.15 | 6.1 x 3.7 | 27 | 23 | 1.57 | bath | 10 | main_floor.scad:57 |
| BATH 2 | 7.27 | 55.3 | 17.5 | 62.04 | 10.23 x 6.74 | 9.8 x 6.3 | 69 | 62 | 1.52 | bath | 10 | main_floor.scad:58 |
| BUNK ROOM | 17.5 | 53.75 | 32.6 | 66.64 | 15.10 x 12.89 | 14.7 x 12.5 | 195 | 184 | 1.17 | bed | 10 | main_floor.scad:59 |
| STUDY | 32.6 | 53.75 | 42.65 | 63.42 | 10.05 x 9.67 | 9.6 x 9.3 | 97 | 89 | 1.04 | office | 10 | main_floor.scad:60 |
| HALL @22.1,49.64 | 22.1 | 49.64 | 42.65 | 53.75 | 20.55 x 4.11 | 20.1 x 3.7 | 84 | 75 | 5.00 | hall | 10 | main_floor.scad:62 |
| (N-S hall, unlabelled) | 37.3 | 35.46 | 42.65 | 49.64 | 5.35 x 14.18 | 5.0 x 13.8 | 76 | 68 | 2.65 | hall | 10 | main_floor.scad:63 |
| STAIR DN | 42.65 | 35.46 | 47.27 | 47.1 | 4.62 x 11.64 | 4.2 x 11.2 | 54 | - | 2.52 | stairwell | 0 | main_floor.scad:64 |
| (landing at the stair top) | 42.65 | 47.1 | 47.27 | 50.69 | 4.62 x 3.59 | 4.2 x 3.2 | 17 | 13 | 1.29 | hall | 0 | main_floor.scad:65 |
| (upper hall, west of its door) | 47.27 | 45.39 | 53.95 | 50.69 | 6.68 x 5.30 | 6.3 x 4.9 | 35 | 31 | 1.26 | hall | 10 | main_floor.scad:66 |
| HALL @53.95,45.39 | 53.95 | 45.39 | 69.14 | 50.69 | 15.19 x 5.30 | 14.8 x 4.9 | 81 | 72 | 2.87 | hall | 10 | main_floor.scad:67 |
| BATH | 47.27 | 35.46 | 53.95 | 45.39 | 6.68 x 9.93 | 6.3 x 9.5 | 66 | 60 | 1.49 | bath | 10 | main_floor.scad:68 |
| FLEX ROOM | 53.95 | 35.46 | 69.14 | 45.39 | 15.19 x 9.93 | 14.8 x 9.5 | 151 | 141 | 1.53 | office | 10 | main_floor.scad:69 |
| SUN ROOM | 42.65 | 50.69 | 53.95 | 63.42 | 11.30 x 12.73 | 10.9 x 12.3 | 144 | 134 | 1.13 | living | 10 | main_floor.scad:70 |
| HALL @24.34,29.51 | 24.34 | 29.51 | 105.2 | 35.46 | 80.86 x 5.95 | 80.5 x 5.5 | 481 | 447 | 13.59 | hall | 10 | main_floor.scad:73 |
| GREAT ROOM | 69.14 | 35.46 | 95.63 | 52.53 | 26.49 x 17.07 | 26.1 x 16.7 | 452 | 435 | 1.55 | living | 12 | main_floor.scad:75 |
| KITCHEN / DINING | 35.6 | 6.28 | 69.14 | 29.51 | 33.54 x 23.23 | 33.1 x 22.8 | 779 | 757 | 1.44 | kitchen | 12 | main_floor.scad:76 |
| BREAKFAST | 54.1 | 0 | 69.14 | 6.28 | 15.04 x 6.28 | 14.6 x 5.9 | 94 | 86 | 2.39 | dining | 10 | main_floor.scad:77 |
| FOYER | 69.14 | 3.72 | 81.12 | 29.51 | 11.98 x 25.79 | 11.6 x 25.4 | 309 | 294 | 2.15 | hall | 12 | main_floor.scad:78 |
| DEN | 81.12 | 0 | 95.95 | 29.51 | 14.83 x 29.51 | 14.4 x 29.1 | 438 | 420 | 1.99 | living | 12 | main_floor.scad:79 |
| (den alcove) | 95.95 | 9.31 | 99.7 | 20.56 | 3.75 x 11.25 | 3.4 x 10.8 | 42 | 36 | 3.00 | living | 10 | main_floor.scad:80 |
| OFFICE | 95.63 | 35.46 | 108.62 | 48.16 | 12.99 x 12.70 | 12.6 x 12.3 | 165 | 155 | 1.02 | office | 10 | main_floor.scad:82 |
| MASTER BEDROOM | 108.62 | 29.51 | 126.97 | 52.86 | 18.35 x 23.35 | 17.9 x 22.9 | 428 | 412 | 1.27 | bed | 10 | main_floor.scad:83 |
| (master entry) | 105.2 | 29.51 | 108.62 | 35.46 | 3.42 x 5.95 | 3.0 x 5.5 | 20 | 17 | 1.74 | hall | 10 | main_floor.scad:84 |
| WIC @95.95,20.56 | 95.95 | 20.56 | 106.51 | 29.51 | 10.56 x 8.95 | 10.2 x 8.6 | 95 | 87 | 1.18 | closet | 10 | main_floor.scad:85 |
| (closet passage) | 106.51 | 20.56 | 111.41 | 29.51 | 4.90 x 8.95 | 4.5 x 8.6 | 44 | 38 | 1.83 | hall | 10 | main_floor.scad:86 |
| WIC @111.41,20.56 | 111.41 | 20.56 | 121.94 | 29.51 | 10.53 x 8.95 | 10.1 x 8.6 | 94 | 87 | 1.18 | closet | 10 | main_floor.scad:87 |
| LINEN | 121.94 | 20.56 | 128.13 | 29.51 | 6.19 x 8.95 | 5.8 x 8.6 | 55 | 50 | 1.45 | closet | 10 | main_floor.scad:88 |
| MASTER BATH | 106.51 | 9.31 | 128.13 | 20.56 | 21.62 x 11.25 | 21.2 x 10.8 | 243 | 230 | 1.92 | bath | 10 | main_floor.scad:89 |
| WC @99.7,16.71 | 99.7 | 16.71 | 106.51 | 20.56 | 6.81 x 3.85 | 6.4 x 3.4 | 26 | 22 | 1.77 | bath | 10 | main_floor.scad:90 |
| (linen between the WCs) | 99.7 | 13.09 | 106.51 | 16.71 | 6.81 x 3.62 | 6.4 x 3.2 | 25 | 21 | 1.88 | closet | 10 | main_floor.scad:91 |
| WC @99.7,9.31 | 99.7 | 9.31 | 106.51 | 13.09 | 6.81 x 3.78 | 6.4 x 3.4 | 26 | 22 | 1.80 | bath | 10 | main_floor.scad:92 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 0 | 1.25 | 24.34 | 35.46 | 24.34 x 34.21 | 23.9 x 33.8 | 833 | 809 | 1.41 | garage | 10 | main_floor.scad:47 |
| SIDE ENTRY | 24.34 | 13.39 | 35.6 | 20.82 | 11.26 x 7.43 | 11.3 x 7.4 (open) | 84 | - | 1.52 | porch | 0 | main_floor.scad:48 |
| PATIO | 53.95 | 50.69 | 69.14 | 63.42 | 15.19 x 12.73 | 15.2 x 12.7 (open) | 193 | - | 1.19 | porch | 0 | main_floor.scad:72 |
| FRONT PORCH | 49.24 | -15.26 | 101.41 | 0 | 52.17 x 15.26 | 52.2 x 15.3 (open) | 796 | - | 3.42 | porch | 0 | main_floor.scad:94 |
| (unlabelled porch) @49.24,0 | 49.24 | 0 | 54.1 | 6.28 | 4.86 x 6.28 | 4.9 x 6.3 (open) | 31 | - | 1.29 | porch | 0 | main_floor.scad:95 |
| (unlabelled porch) @95.95,0 | 95.95 | 0 | 101.41 | 9.31 | 5.46 x 9.31 | 5.5 x 9.3 (open) | 51 | - | 1.71 | porch | 0 | main_floor.scad:96 |
| (covered entry) | 69.14 | 0 | 81.12 | 3.72 | 11.98 x 3.72 | 12.0 x 3.7 (open) | 45 | - | 3.22 | porch | 0 | main_floor.scad:97 |
| DECK | 69.14 | 52.53 | 95.63 | 64.7 | 26.49 x 12.17 | 26.5 x 12.2 (open) | 322 | - | 2.18 | porch | 0 | main_floor.scad:98 |
| OFFICE PORCH | 95.63 | 48.16 | 108.62 | 59.47 | 12.99 x 11.31 | 13.0 x 11.3 (open) | 147 | - | 1.15 | porch | 0 | main_floor.scad:99 |
| MASTER PORCH | 108.62 | 52.86 | 126.97 | 62.4 | 18.35 x 9.54 | 18.3 x 9.5 (open) | 175 | - | 1.92 | porch | 0 | main_floor.scad:100 |
| SIDE PORCH | 126.97 | 29.51 | 137.66 | 59.47 | 10.69 x 29.96 | 10.7 x 30.0 (open) | 320 | - | 2.80 | porch | 0 | main_floor.scad:101 |
| (unlabelled porch) @128.13,26.84 | 128.13 | 26.84 | 137.66 | 29.51 | 9.53 x 2.67 | 9.5 x 2.7 (open) | 25 | - | 3.57 | porch | 0 | main_floor.scad:102 |
| (study stoop) | 36.6 | 63.42 | 41.2 | 66.6 | 4.60 x 3.18 | 4.6 x 3.2 (open) | 15 | - | 1.45 | porch | 0 | main_floor.scad:103 |
| (garage side-door pad) | 1.7 | 35.46 | 7.27 | 38.6 | 5.57 x 3.14 | 5.6 x 3.1 (open) | 17 | - | 1.77 | porch | 0 | main_floor.scad:104 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MUSIC ROOM | 22.16 | 50.35 | 42.65 | 63.16 | 20.49 x 12.81 | 19.7 x 12.1 | 262 | 238 | 1.60 | living | 12 | basement.scad:54 |
| GYM | 42.65 | 45.34 | 54.14 | 63.16 | 11.49 x 17.82 | 10.7 x 17.1 | 205 | 183 | 1.55 | rec | 12 | basement.scad:55 |
| STORAGE | 22.16 | 42.77 | 37.37 | 50.35 | 15.21 x 7.58 | 14.5 x 7.2 | 115 | 104 | 2.01 | closet | 12 | basement.scad:56 |
| UTILITY | 22.16 | 35.08 | 37.37 | 42.77 | 15.21 x 7.69 | 14.5 x 6.9 | 117 | 100 | 1.98 | utility | 12 | basement.scad:57 |
| HALL @37.37,35.08 | 37.37 | 35.08 | 42.65 | 50.35 | 5.28 x 15.27 | 4.9 x 14.9 | 81 | 73 | 2.89 | hall | 12 | basement.scad:58 |
| STAIR UP | 42.65 | 28.725 | 47.27 | 45.34 | 4.62 x 16.62 | 4.2 x 16.2 | 77 | 68 | 3.60 | stair | 12 | basement.scad:59 |
| BATH @47.27,35.08 | 47.27 | 35.08 | 54.14 | 45.34 | 6.87 x 10.26 | 6.5 x 9.9 | 70 | 64 | 1.49 | bath | 12 | basement.scad:60 |
| HALLWAY | 35.27 | 27.6 | 54.14 | 28.725 | 18.87 x 1.12 | 18.1 x 0.7 | 21 | 13 | 16.77 | hall | 0 | basement.scad:61 |
| (unlabelled hall) @35.27,28.725 | 35.27 | 28.725 | 42.65 | 35.08 | 7.38 x 6.35 | 6.6 x 6.0 | 47 | 39 | 1.16 | hall | 0 | basement.scad:62 |
| (unlabelled hall) @47.27,28.725 | 47.27 | 28.725 | 54.14 | 35.08 | 6.87 x 6.35 | 6.5 x 6.0 | 44 | 39 | 1.08 | hall | 0 | basement.scad:63 |
| LIVING ROOM | 35.27 | 5.79 | 54.14 | 27.6 | 18.87 x 21.81 | 18.1 x 21.1 | 412 | 382 | 1.16 | living | 10 | basement.scad:64 |
| HOME THEATER | 54.14 | 29.12 | 69.38 | 50.35 | 15.24 x 21.23 | 14.8 x 20.5 | 324 | 304 | 1.39 | tiered | 13.25 | basement.scad:65 |
| PET ROOM | 54.14 | 18.15 | 69.38 | 29.12 | 15.24 x 10.97 | 14.8 x 10.6 | 167 | 157 | 1.39 | utility | 12 | basement.scad:66 |
| POOL ROOM | 69.38 | 18.15 | 96.33 | 52.76 | 26.95 x 34.61 | 25.8 x 33.9 | 933 | 875 | 1.28 | pit | 12 | basement.scad:67 |
| POOL EQUIP. | 96.33 | 29.12 | 103.04 | 41.94 | 6.71 x 12.82 | 6.0 x 12.1 | 86 | 72 | 1.91 | utility | 12 | basement.scad:68 |
| POOL BATH | 96.33 | 18.15 | 103.04 | 29.12 | 6.71 x 10.97 | 6.0 x 10.6 | 74 | 63 | 1.63 | bath | 12 | basement.scad:69 |
| HALL @54.14,13.43 | 54.14 | 13.43 | 103.04 | 18.15 | 48.90 x 4.72 | 48.1 x 4.0 | 231 | 191 | 10.36 | hall | 12 | basement.scad:70 |
| BATH @54.14,5.79 | 54.14 | 5.79 | 67.4 | 13.43 | 13.26 x 7.64 | 12.9 x 6.9 | 101 | 89 | 1.74 | bath | 12 | basement.scad:71 |
| LAUNDRY | 67.4 | 5.79 | 81.68 | 13.43 | 14.28 x 7.64 | 13.5 x 6.9 | 109 | 93 | 1.87 | utility | 12 | basement.scad:72 |
| EXIT STAIR | 45.6 | 63.16 | 66.8 | 67.75 | 21.20 x 4.59 | 20.1 x 3.5 | 97 | - | 4.62 | stairwell | 0 | basement.scad:74 |


Sliver fragments, so per-row statistics mislead: "(suite entry, 2nd piece)" 3.72 x 1.55 ft (main_floor.scad:55); basement "HALLWAY" row 18.87 x 1.125 ft (basement.scad:61), which is the south strip of a 3-row hallway (rows basement.scad:61-63, x 35.27..54.14, y 27.6..35.08, with the STAIR UP flight room between its two arms).

## 4. Door schedule

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (72, 3.72) x | 6.2 ft = 74.4 in | double | 1 | (covered entry) / FOYER | main_floor.scad:110 |
| M2 | (69.6, 3.72) x | 2 ft = 24 in | glass | - | (covered entry) / FOYER | main_floor.scad:111 |
| M3 | (78.6, 3.72) x | 2 ft = 24 in | glass | - | (covered entry) / FOYER | main_floor.scad:112 |
| M4 | (63.8, 0) x | 5 ft = 60 in | double | 1 | FRONT PORCH / BREAKFAST | main_floor.scad:113 |
| M5 | (37, 63.42) x | 3.75 ft = 45 in | double | 1 | STUDY / (study stoop) | main_floor.scad:114 |
| M6 | (99, 48.16) x | 6.5 ft = 78 in | double | 1 | OFFICE / OFFICE PORCH | main_floor.scad:115 |
| M7 | (114.1, 52.86) x | 6.05 ft = 72.6 in | double | 1 | MASTER BEDROOM / MASTER PORCH | main_floor.scad:116 |
| M8 | (0, 4.97) y | 16 ft = 192 in | garage | - | OUTSIDE / GARAGE | main_floor.scad:117 |
| M9 | (0, 22.86) y | 9 ft = 108 in | garage | - | OUTSIDE / GARAGE | main_floor.scad:118 |
| M10 | (2.43, 35.46) x | 2.8 ft = 33.6 in | door | 1 | GARAGE / (garage side-door pad) | main_floor.scad:119 |
| M11 | (24.34, 16.1) y | 3 ft = 36 in | door | -1 | GARAGE / SIDE ENTRY | main_floor.scad:120 |
| M12 | (24.34, 31.9) y | 3 ft = 36 in | door | 1 | GARAGE / HALL @24.34,29.51 | main_floor.scad:122 |
| M13 | (35.6, 23.3) y | 3 ft = 36 in | door | -1 | SCULLERY / KITCHEN / DINING | main_floor.scad:123 |
| M14 | (24.6, 35.46) x | 12.4 ft = 148.8 in | full | - | HALL @24.34,29.51 / MUDROOM | main_floor.scad:124 |
| M15 | (24.8, 40.56) x | 2.8 ft = 33.6 in | door | -1 | MUDROOM / LAUNDRY | main_floor.scad:125 |
| M16 | (25, 49.64) x | 2.7 ft = 32.4 in | door | -1 | LAUNDRY / HALL @22.1,49.64 | main_floor.scad:126 |
| M17 | (22.1, 50) y | 2.8 ft = 33.6 in | door | -1 | (suite entry) / HALL @22.1,49.64 | main_floor.scad:128 |
| M18 | (14, 48.13) x | 7.9 ft = 94.8 in | full | - | BEDROOM 2 / (suite entry) | main_floor.scad:129 |
| M19 | (13.9, 53.75) x | 3.5 ft = 42 in | full | - | (suite entry) / (suite entry, 2nd piece) | main_floor.scad:130 |
| M20 | (14.3, 55.3) x | 2.6 ft = 31.2 in | door | -1 | (suite entry, 2nd piece) / BATH 2 | main_floor.scad:131 |
| M21 | (13.78, 51.35) y | 2.35 ft = 28.2 in | door | -1 | WC @7.27,51.15 / (suite entry) | main_floor.scad:132 |
| M22 | (7.6, 48.13) x | 5.9 ft = 70.8 in | open | - | BEDROOM 2 / WIC @7.27,48.13 | main_floor.scad:133 |
| M23 | (17.5, 56.2) y | 2.4 ft = 28.8 in | door | -1 | BATH 2 / BUNK ROOM | main_floor.scad:134 |
| M24 | (29.4, 53.75) x | 2.8 ft = 33.6 in | door | 1 | HALL @22.1,49.64 / BUNK ROOM | main_floor.scad:135 |
| M25 | (33, 53.75) x | 2.7 ft = 32.4 in | door | 1 | HALL @22.1,49.64 / STUDY | main_floor.scad:136 |
| M26 | (37.5, 49.64) x | 5 ft = 60 in | full | - | (N-S hall, unlabelled) / HALL @22.1,49.64 | main_floor.scad:137 |
| M27 | (37.6, 35.46) x | 4.8 ft = 57.6 in | full | - | HALL @24.34,29.51 / (N-S hall, unlabelled) | main_floor.scad:138 |
| M28 | (42.65, 47.15) y | 2.4 ft = 28.8 in | door | 1 | (N-S hall, unlabelled) / (landing at the stair top) | main_floor.scad:140 |
| M29 | (42.9, 47.1) x | 4.1 ft = 49.2 in | full | - | STAIR DN / (landing at the stair top) | main_floor.scad:141 |
| M30 | (47.27, 47.3) y | 3.2 ft = 38.4 in | full | - | (landing at the stair top) / (upper hall, west of its door) | main_floor.scad:142 |
| M31 | (53.95, 45.75) y | 2.7 ft = 32.4 in | door | -1 | (upper hall, west of its door) / HALL @53.95,45.39 | main_floor.scad:143 |
| M32 | (69.14, 45.6) y | 4.9 ft = 58.8 in | full | - | HALL @53.95,45.39 / GREAT ROOM | main_floor.scad:144 |
| M33 | (70.65, 52.53) x | 6 ft = 72 in | double | -1 | GREAT ROOM / DECK | main_floor.scad:145 |
| M34 | (47.8, 45.39) x | 2.9 ft = 34.8 in | door | -1 | BATH / (upper hall, west of its door) | main_floor.scad:146 |
| M35 | (58.3, 45.39) x | 6.5 ft = 78 in | slider | - | FLEX ROOM / HALL @53.95,45.39 | main_floor.scad:147 |
| M36 | (47.5, 50.69) x | 5.9 ft = 70.8 in | double | 1 | (upper hall, west of its door) / SUN ROOM | main_floor.scad:148 |
| M37 | (53.95, 53.9) y | 4.9 ft = 58.8 in | double | 1 | SUN ROOM / PATIO | main_floor.scad:149 |
| M38 | (58.55, 50.69) x | 6 ft = 72 in | double | -1 | HALL @53.95,45.39 / PATIO | main_floor.scad:150 |
| M39 | (38.2, 29.51) x | 4 ft = 48 in | full | - | KITCHEN / DINING / HALL @24.34,29.51 | main_floor.scad:152 |
| M40 | (48.9, 29.51) x | 5.9 ft = 70.8 in | full | - | KITCHEN / DINING / HALL @24.34,29.51 | main_floor.scad:153 |
| M41 | (54.4, 6.28) x | 14.5 ft = 174 in | full | - | BREAKFAST / KITCHEN / DINING | main_floor.scad:154 |
| M42 | (71.4, 29.51) x | 7.9 ft = 94.8 in | full | - | FOYER / HALL @24.34,29.51 | main_floor.scad:155 |
| M43 | (69.4, 35.46) x | 26 ft = 312 in | full | - | HALL @24.34,29.51 / GREAT ROOM | main_floor.scad:156 |
| M44 | (81.12, 12.66) y | 5 ft = 60 in | double | 1 | FOYER / DEN | main_floor.scad:157 |
| M45 | (95.95, 9.6) y | 10.7 ft = 128.4 in | full | - | DEN / (den alcove) | main_floor.scad:158 |
| M46 | (99.3, 35.46) x | 4.7 ft = 56.4 in | double | 1 | HALL @24.34,29.51 / OFFICE | main_floor.scad:160 |
| M47 | (105.2, 29.95) y | 4.6 ft = 55.2 in | double | 1 | HALL @24.34,29.51 / (master entry) | main_floor.scad:161 |
| M48 | (108.62, 29.8) y | 5.4 ft = 64.8 in | full | - | (master entry) / MASTER BEDROOM | main_floor.scad:162 |
| M49 | (108.9, 29.51) x | 2.3 ft = 27.6 in | open | - | (closet passage) / MASTER BEDROOM | main_floor.scad:163 |
| M50 | (106.51, 23.6) y | 2.9 ft = 34.8 in | door | -1 | WIC @95.95,20.56 / (closet passage) | main_floor.scad:164 |
| M51 | (111.41, 23.6) y | 2.9 ft = 34.8 in | door | 1 | (closet passage) / WIC @111.41,20.56 | main_floor.scad:165 |
| M52 | (107.1, 20.56) x | 2.7 ft = 32.4 in | door | -1 | MASTER BATH / (closet passage) | main_floor.scad:166 |
| M53 | (122.6, 20.56) x | 3 ft = 36 in | door | 1 | MASTER BATH / LINEN | main_floor.scad:167 |
| M54 | (106.51, 17) y | 2.6 ft = 31.2 in | door | -1 | WC @99.7,16.71 / MASTER BATH | main_floor.scad:168 |
| M55 | (106.51, 13.4) y | 2.4 ft = 28.8 in | door | -1 | (linen between the WCs) / MASTER BATH | main_floor.scad:169 |
| M56 | (106.51, 9.8) y | 2.6 ft = 31.2 in | door | -1 | WC @99.7,9.31 / MASTER BATH | main_floor.scad:170 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (38.4, 50.35) x | 2.8 ft = 33.6 in | door | 1 | HALL @37.37,35.08 / MUSIC ROOM | basement.scad:79 |
| B2 | (42.65, 46.2) y | 2.8 ft = 33.6 in | door | 1 | HALL @37.37,35.08 / GYM | basement.scad:80 |
| B3 | (37.37, 45.6) y | 2.8 ft = 33.6 in | door | -1 | STORAGE / HALL @37.37,35.08 | basement.scad:81 |
| B4 | (37.37, 38.4) y | 3 ft = 36 in | door | -1 | UTILITY / HALL @37.37,35.08 | basement.scad:82 |
| B5 | (37.6, 35.08) x | 4.8 ft = 57.6 in | full | - | (unlabelled hall) @35.27,28.725 / HALL @37.37,35.08 | basement.scad:83 |
| B6 | (42.9, 28.725) x | 4.1 ft = 49.2 in | full | - | HALLWAY / STAIR UP | basement.scad:84 |
| B7 | (35.5, 28.725) x | 6.9 ft = 82.8 in | full | - | HALLWAY / (unlabelled hall) @35.27,28.725 | basement.scad:85 |
| B8 | (47.5, 28.725) x | 6.4 ft = 76.8 in | full | - | HALLWAY / (unlabelled hall) @47.27,28.725 | basement.scad:86 |
| B9 | (49.2, 35.08) x | 2.8 ft = 33.6 in | door | 1 | (unlabelled hall) @47.27,28.725 / BATH @47.27,35.08 | basement.scad:87 |
| B10 | (54.14, 31.7) y | 3 ft = 36 in | door | -1 | (unlabelled hall) @47.27,28.725 / HOME THEATER | basement.scad:88 |
| B11 | (40, 27.6) x | 8 ft = 96 in | open | - | LIVING ROOM / HALLWAY | basement.scad:89 |
| B12 | (54.14, 13.8) y | 4 ft = 48 in | open | - | LIVING ROOM / HALL @54.14,13.43 | basement.scad:90 |
| B13 | (56.5, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / PET ROOM | basement.scad:91 |
| B14 | (71, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / POOL ROOM | basement.scad:92 |
| B15 | (96.33, 20.5) y | 2.8 ft = 33.6 in | door | 1 | POOL ROOM / POOL BATH | basement.scad:93 |
| B16 | (99, 18.15) x | 2.8 ft = 33.6 in | door | 1 | HALL @54.14,13.43 / POOL BATH | basement.scad:94 |
| B17 | (96.33, 33.5) y | 3 ft = 36 in | door | 1 | POOL ROOM / POOL EQUIP. | basement.scad:95 |
| B18 | (59, 13.43) x | 2.8 ft = 33.6 in | door | -1 | BATH @54.14,5.79 / HALL @54.14,13.43 | basement.scad:96 |
| B19 | (73, 13.43) x | 3 ft = 36 in | door | -1 | LAUNDRY / HALL @54.14,13.43 | basement.scad:97 |
| B20 | (46.2, 63.16) x | 3.5 ft = 42 in | door | -1 | GYM / EXIT STAIR | basement.scad:98 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 7 | 11 | 4 | 22 |
| double | 0 | 0 | 12 | 12 |
| open | 1 | 0 | 1 | 2 |
| full | 0 | 0 | 15 | 15 |
| slider | 0 | 0 | 1 | 1 |
| glass | 2 | 0 | 0 | 2 |
| garage | 0 | 0 | 2 | 2 |
| ALL | 10 | 11 | 35 | 56 |
| passage (door+double+slider+open) | 8 | 11 | 18 | 37 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 7 | 7 | 14 |
| open | 0 | 0 | 2 | 2 |
| full | 0 | 0 | 4 | 4 |
| ALL | 0 | 7 | 13 | 20 |
| passage (door+double+slider+open) | 0 | 7 | 9 | 16 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| main_floor.scad:116 | MASTER BEDROOM / MASTER PORCH | double | 72.6 in | - |
| main_floor.scad:129 | BEDROOM 2 / (suite entry) | full | 94.8 in | - |
| main_floor.scad:131 | (suite entry, 2nd piece) / BATH 2 | door | 31.2 in | 29.7 |
| main_floor.scad:132 | WC @7.27,51.15 / (suite entry) | door | 28.2 in | 26.7 |
| main_floor.scad:133 | BEDROOM 2 / WIC @7.27,48.13 | open | 70.8 in | - |
| main_floor.scad:134 | BATH 2 / BUNK ROOM | door | 28.8 in | 27.3 |
| main_floor.scad:135 | HALL @22.1,49.64 / BUNK ROOM | door | 33.6 in | 32.1 |
| main_floor.scad:146 | BATH / (upper hall, west of its door) | door | 34.8 in | 33.3 |
| main_floor.scad:162 | (master entry) / MASTER BEDROOM | full | 64.8 in | - |
| main_floor.scad:163 | (closet passage) / MASTER BEDROOM | open | 27.6 in | - |
| main_floor.scad:164 | WIC @95.95,20.56 / (closet passage) | door | 34.8 in | 33.3 |
| main_floor.scad:165 | (closet passage) / WIC @111.41,20.56 | door | 34.8 in | 33.3 |
| main_floor.scad:166 | MASTER BATH / (closet passage) | door | 32.4 in | 30.9 |
| main_floor.scad:167 | MASTER BATH / LINEN | door | 36 in | 34.5 |
| main_floor.scad:168 | WC @99.7,16.71 / MASTER BATH | door | 31.2 in | 29.7 |
| main_floor.scad:169 | (linen between the WCs) / MASTER BATH | door | 28.8 in | 27.3 |
| main_floor.scad:170 | WC @99.7,9.31 / MASTER BATH | door | 31.2 in | 29.7 |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| basement.scad:81 | STORAGE / HALL @37.37,35.08 | door | 33.6 in | 32.1 |
| basement.scad:87 | (unlabelled hall) @47.27,28.725 / BATH @47.27,35.08 | door | 33.6 in | 32.1 |
| basement.scad:93 | POOL ROOM / POOL BATH | door | 33.6 in | 32.1 |
| basement.scad:94 | HALL @54.14,13.43 / POOL BATH | door | 33.6 in | 32.1 |
| basement.scad:96 | BATH @54.14,5.79 / HALL @54.14,13.43 | door | 33.6 in | 32.1 |


## 5. Window schedule

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| BUNK ROOM | N | (21.45, 66.64, 'x') | 3.5 | 2.5 | 5 | 17.5 | main_floor.scad:175 |
| BEDROOM 2 | W | (7.27, 36.3, 'y') | 5.4 | 2.75 | 5 | 27.0 | main_floor.scad:176 |
| BEDROOM 2 | W | (7.27, 42.3, 'y') | 5.4 | 2.75 | 5 | 27.0 | main_floor.scad:177 |
| SUN ROOM | N | (44.3, 63.42, 'x') | 7.4 | 1.5 | 6.5 | 48.1 | main_floor.scad:178 |
| SUN ROOM | E | (53.95, 59.3, 'y') | 3.6 | 1.5 | 6.5 | 23.4 | main_floor.scad:179 |
| GREAT ROOM | N | (77.8, 52.53, 'x') | 3.6 | 2 | 6 | 21.6 | main_floor.scad:180 |
| GREAT ROOM | N | (89.4, 52.53, 'x') | 4.3 | 2 | 6 | 25.8 | main_floor.scad:181 |
| MASTER BEDROOM | N | (110, 52.86, 'x') | 2.5 | 2.5 | 5 | 12.5 | main_floor.scad:182 |
| MASTER BEDROOM | E | (126.97, 46, 'y') | 4.7 | 2.5 | 5 | 23.5 | main_floor.scad:183 |
| MASTER BEDROOM | E | (126.97, 31, 'y') | 4 | 2.5 | 5 | 20.0 | main_floor.scad:184 |
| MASTER BATH | E | (128.13, 9.8, 'y') | 4.6 | 3.5 | 4 | 18.4 | main_floor.scad:185 |
| LINEN | E | (128.13, 21.3, 'y') | 3.6 | 4 | 3 | 10.8 | main_floor.scad:186 |
| DEN | S | (84, 0, 'x') | 8 | 2.5 | 5.5 | 44.0 | main_floor.scad:187 |
| DEN | E | (95.95, 1.8, 'y') | 5.8 | 2.5 | 5.5 | 31.9 | main_floor.scad:188 |
| BREAKFAST | W | (54.1, 0.7, 'y') | 4.8 | 2 | 6 | 28.8 | main_floor.scad:189 |
| BREAKFAST | S | (54.6, 0, 'x') | 5.6 | 2 | 6 | 33.6 | main_floor.scad:190 |
| KITCHEN / DINING | S | (37.7, 6.28, 'x') | 7.5 | 3.5 | 4 | 30.0 | main_floor.scad:191 |

Total main-floor window glass (width x height): 443.9 sq ft (17 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 5, S: 3, E: 6, W: 3

Rooms with windows on 2+ walls (main): SUN ROOM (E/N); MASTER BEDROOM (E/N); DEN (E/S); BREAKFAST (S/W)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| SCULLERY | utility | 98 |
| MUDROOM | utility | 78 |
| LAUNDRY | utility | 138 |
| (suite entry) | hall | 47 |
| (suite entry, 2nd piece) | hall | 6 |
| WIC @7.27,48.13 | closet | 20 |
| WC @7.27,51.15 | bath | 27 |
| BATH 2 | bath | 69 |
| STUDY | office | 97 |
| HALL @22.1,49.64 | hall | 84 |
| (N-S hall, unlabelled) | hall | 76 |
| (landing at the stair top) | hall | 17 |
| (upper hall, west of its door) | hall | 35 |
| HALL @53.95,45.39 | hall | 81 |
| BATH | bath | 66 |
| FLEX ROOM | office | 151 |
| HALL @24.34,29.51 | hall | 481 |
| FOYER | hall | 309 |
| (den alcove) | living | 42 |
| OFFICE | office | 165 |
| (master entry) | hall | 20 |
| WIC @95.95,20.56 | closet | 95 |
| (closet passage) | hall | 44 |
| WIC @111.41,20.56 | closet | 94 |
| WC @99.7,16.71 | bath | 26 |
| (linen between the WCs) | closet | 25 |
| WC @99.7,9.31 | bath | 26 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| LIVING ROOM | S | (40, 5.79, 'x') | 8 | 4.5 | 4 | 32.0 | foundation.scad:160 |
| MUSIC ROOM | N | (33.15, 63.16, 'x') | 3 | 4.5 | 4 | 12.0 | foundation.scad:161 |

Rooms with windows on 2+ walls (basement): none

Basement rooms with no window row: GYM (rec, 205 sf); STORAGE (closet, 115 sf); UTILITY (utility, 117 sf); HALL @37.37,35.08 (hall, 81 sf); STAIR UP (stair, 77 sf); BATH @47.27,35.08 (bath, 70 sf); HALLWAY (hall, 21 sf); (unlabelled hall) @35.27,28.725 (hall, 47 sf); (unlabelled hall) @47.27,28.725 (hall, 44 sf); HOME THEATER (tiered, 324 sf); PET ROOM (utility, 167 sf); POOL ROOM (pit, 933 sf); POOL EQUIP. (utility, 86 sf); POOL BATH (bath, 74 sf); HALL @54.14,13.43 (hall, 231 sf); BATH @54.14,5.79 (bath, 101 sf); LAUNDRY (utility, 109 sf)


## 6. Circulation

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (suite entry) | 13.78,48.13 to 22.1,53.75 | 47 | 5.2 ft clear width (63 in), length 7.9 | main_floor.scad:54 |
| (suite entry, 2nd piece) | 13.78,53.75 to 17.5,55.3 | 6 | 1.1 ft clear width (14 in), length 3.3 | main_floor.scad:55 |
| HALL @22.1,49.64 | 22.1,49.64 to 42.65,53.75 | 84 | 3.7 ft clear width (45 in), length 20.1 | main_floor.scad:62 |
| (N-S hall, unlabelled) | 37.3,35.46 to 42.65,49.64 | 76 | 5.0 ft clear width (59 in), length 13.8 | main_floor.scad:63 |
| (landing at the stair top) | 42.65,47.1 to 47.27,50.69 | 17 | 3.2 ft clear width (38 in), length 4.2 | main_floor.scad:65 |
| (upper hall, west of its door) | 47.27,45.39 to 53.95,50.69 | 35 | 4.9 ft clear width (59 in), length 6.3 | main_floor.scad:66 |
| HALL @53.95,45.39 | 53.95,45.39 to 69.14,50.69 | 81 | 4.9 ft clear width (59 in), length 14.8 | main_floor.scad:67 |
| HALL @24.34,29.51 | 24.34,29.51 to 105.2,35.46 | 481 | 5.5 ft clear width (67 in), length 80.5 | main_floor.scad:73 |
| (master entry) | 105.2,29.51 to 108.62,35.46 | 20 | 3.0 ft clear width (36 in), length 5.5 | main_floor.scad:84 |
| (closet passage) | 106.51,20.56 to 111.41,29.51 | 44 | 4.5 ft clear width (54 in), length 8.6 | main_floor.scad:86 |

**Circulation total (halls only): 891 sq ft = 16.2% of 5486 sq ft conditioned** (16.4% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 309 | 11.6 ft | 21.9% | main_floor.scad:78 |
| MUDROOM | 78 | 4.7 ft | 23.3% (halls+foyer+mudroom) | main_floor.scad:50 |
| STAIR DN opening (stairwell) | 54 | 4.2 ft | 24.3% (all four) | main_floor.scad:64 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| HALL @37.37,35.08 | 37.37,35.08 to 42.65,50.35 | 81 | 4.9 ft clear width (59 in), length 14.9 | basement.scad:58 |
| HALLWAY | 35.27,27.6 to 54.14,28.725 | 21 | 0.7 ft clear width (9 in), length 18.1 | basement.scad:61 |
| (unlabelled hall) @35.27,28.725 | 35.27,28.725 to 42.65,35.08 | 47 | 6.0 ft clear width (71 in), length 6.6 | basement.scad:62 |
| (unlabelled hall) @47.27,28.725 | 47.27,28.725 to 54.14,35.08 | 44 | 6.0 ft clear width (71 in), length 6.5 | basement.scad:63 |
| HALL @54.14,13.43 | 54.14,13.43 to 103.04,18.15 | 231 | 4.0 ft clear width (48 in), length 48.1 | basement.scad:70 |

**Circulation total (halls only): 423 sq ft = 12.2% of 3475 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 77 | 4.2 ft | 14.4% | basement.scad:59 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.


Merged basement hallway zone (rows basement.scad:61-63, plus the stair foot between): the zone is 18.87 ft wide (x 35.27..54.14) by 7.48 ft (y 27.6..35.08); its two arms on either side of the stair foot are about 6 ft wide.

## 7. Door-graph facts for flow

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): STAIR DN <-> (landing at the stair top) (4.6 ft shared edge); PATIO <-> DECK (10.9 ft shared edge); FRONT PORCH <-> (unlabelled porch) @49.24,0 (4.9 ft shared edge); FRONT PORCH <-> (unlabelled porch) @95.95,0 (5.5 ft shared edge); FRONT PORCH <-> (covered entry) (12.0 ft shared edge); DECK <-> OFFICE PORCH (6.9 ft shared edge); OFFICE PORCH <-> MASTER PORCH (6.6 ft shared edge); MASTER PORCH <-> SIDE PORCH (6.6 ft shared edge); SIDE PORCH <-> (unlabelled porch) @128.13,26.84 (9.5 ft shared edge)

Basement: HALLWAY <-> (unlabelled hall) @35.27,28.725 (7.4 ft shared edge); HALLWAY <-> (unlabelled hall) @47.27,28.725 (6.9 ft shared edge)

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| GARAGE | garage | (garage side-door pad); HALL @24.34,29.51; SIDE ENTRY | garage to outside (main_floor.scad:117), garage to outside (main_floor.scad:118) |
| SIDE ENTRY | porch, ceiling 0 (open zone) | GARAGE | - |
| SCULLERY | utility | KITCHEN / DINING | - |
| MUDROOM | utility | HALL @24.34,29.51; LAUNDRY | - |
| LAUNDRY | utility | HALL @22.1,49.64; MUDROOM | - |
| BEDROOM 2 | bed | (suite entry); WIC @7.27,48.13 | - |
| (suite entry) | hall | (suite entry, 2nd piece); BEDROOM 2; HALL @22.1,49.64; WC @7.27,51.15 | - |
| (suite entry, 2nd piece) | hall, ceiling 0 (open zone) | (suite entry); BATH 2 | - |
| WIC @7.27,48.13 | closet | BEDROOM 2 | - |
| WC @7.27,51.15 | bath | (suite entry) | - |
| BATH 2 | bath | (suite entry, 2nd piece); BUNK ROOM | - |
| BUNK ROOM | bed | BATH 2; HALL @22.1,49.64 | - |
| STUDY | office | (study stoop); HALL @22.1,49.64 | - |
| HALL @22.1,49.64 | hall | (N-S hall, unlabelled); (suite entry); BUNK ROOM; LAUNDRY; STUDY | - |
| (N-S hall, unlabelled) | hall | (landing at the stair top); HALL @22.1,49.64; HALL @24.34,29.51 | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (landing at the stair top) | - |
| (landing at the stair top) | hall, ceiling 0 (open zone) | (N-S hall, unlabelled); (upper hall, west of its door); STAIR DN | - |
| (upper hall, west of its door) | hall | (landing at the stair top); BATH; HALL @53.95,45.39; SUN ROOM | - |
| HALL @53.95,45.39 | hall | (upper hall, west of its door); FLEX ROOM; GREAT ROOM; PATIO | - |
| BATH | bath | (upper hall, west of its door) | - |
| FLEX ROOM | office | HALL @53.95,45.39 | - |
| SUN ROOM | living | (upper hall, west of its door); PATIO | - |
| PATIO | porch, ceiling 0 (open zone) | DECK; HALL @53.95,45.39; SUN ROOM | - |
| HALL @24.34,29.51 | hall | (N-S hall, unlabelled); (master entry); FOYER; GARAGE; GREAT ROOM; KITCHEN / DINING; MUDROOM; OFFICE | - |
| GREAT ROOM | living | DECK; HALL @24.34,29.51; HALL @53.95,45.39 | - |
| KITCHEN / DINING | kitchen | BREAKFAST; HALL @24.34,29.51; SCULLERY | - |
| BREAKFAST | dining | FRONT PORCH; KITCHEN / DINING | - |
| FOYER | hall | (covered entry); DEN; HALL @24.34,29.51 | - |
| DEN | living | (den alcove); FOYER | - |
| (den alcove) | living | DEN | - |
| OFFICE | office | HALL @24.34,29.51; OFFICE PORCH | - |
| MASTER BEDROOM | bed | (closet passage); (master entry); MASTER PORCH | - |
| (master entry) | hall | HALL @24.34,29.51; MASTER BEDROOM | - |
| WIC @95.95,20.56 | closet | (closet passage) | - |
| (closet passage) | hall | MASTER BATH; MASTER BEDROOM; WIC @111.41,20.56; WIC @95.95,20.56 | - |
| WIC @111.41,20.56 | closet | (closet passage) | - |
| LINEN | closet | MASTER BATH | - |
| MASTER BATH | bath | (closet passage); (linen between the WCs); LINEN; WC @99.7,16.71; WC @99.7,9.31 | - |
| WC @99.7,16.71 | bath | MASTER BATH | - |
| (linen between the WCs) | closet | MASTER BATH | - |
| WC @99.7,9.31 | bath | MASTER BATH | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | (covered entry); (unlabelled porch) @49.24,0; (unlabelled porch) @95.95,0; BREAKFAST | - |
| (unlabelled porch) @49.24,0 | porch, ceiling 0 (open zone) | FRONT PORCH | - |
| (unlabelled porch) @95.95,0 | porch, ceiling 0 (open zone) | FRONT PORCH | - |
| (covered entry) | porch, ceiling 0 (open zone) | FOYER; FRONT PORCH | - |
| DECK | porch, ceiling 0 (open zone) | GREAT ROOM; OFFICE PORCH; PATIO | - |
| OFFICE PORCH | porch, ceiling 0 (open zone) | DECK; MASTER PORCH; OFFICE | - |
| MASTER PORCH | porch, ceiling 0 (open zone) | MASTER BEDROOM; OFFICE PORCH; SIDE PORCH | - |
| SIDE PORCH | porch, ceiling 0 (open zone) | (unlabelled porch) @128.13,26.84; MASTER PORCH | - |
| (unlabelled porch) @128.13,26.84 | porch, ceiling 0 (open zone) | SIDE PORCH | - |
| (study stoop) | porch, ceiling 0 (open zone) | STUDY | - |
| (garage side-door pad) | porch, ceiling 0 (open zone) | GARAGE | - |

### 7.2 Basement adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| MUSIC ROOM | living | HALL @37.37,35.08 | - |
| GYM | rec | EXIT STAIR; HALL @37.37,35.08 | - |
| STORAGE | closet | HALL @37.37,35.08 | - |
| UTILITY | utility | HALL @37.37,35.08 | - |
| HALL @37.37,35.08 | hall | (unlabelled hall) @35.27,28.725; GYM; MUSIC ROOM; STORAGE; UTILITY | - |
| STAIR UP | stair | HALLWAY | - |
| BATH @47.27,35.08 | bath | (unlabelled hall) @47.27,28.725 | - |
| HALLWAY | hall, ceiling 0 (open zone) | (unlabelled hall) @35.27,28.725; (unlabelled hall) @47.27,28.725; LIVING ROOM; STAIR UP | - |
| (unlabelled hall) @35.27,28.725 | hall, ceiling 0 (open zone) | HALL @37.37,35.08; HALLWAY | - |
| (unlabelled hall) @47.27,28.725 | hall, ceiling 0 (open zone) | BATH @47.27,35.08; HALLWAY; HOME THEATER | - |
| LIVING ROOM | living | HALL @54.14,13.43; HALLWAY | - |
| HOME THEATER | tiered | (unlabelled hall) @47.27,28.725 | - |
| PET ROOM | utility | HALL @54.14,13.43 | - |
| POOL ROOM | pit | HALL @54.14,13.43; POOL BATH; POOL EQUIP. | - |
| POOL EQUIP. | utility | POOL ROOM | - |
| POOL BATH | bath | HALL @54.14,13.43; POOL ROOM | - |
| HALL @54.14,13.43 | hall | BATH @54.14,5.79; LAUNDRY; LIVING ROOM; PET ROOM; POOL BATH; POOL ROOM | - |
| BATH @54.14,5.79 | bath | HALL @54.14,13.43 | - |
| LAUNDRY | utility | HALL @54.14,13.43 | - |
| EXIT STAIR | stairwell, ceiling 0 (open zone) | GYM | - |

### 7.3 Daily paths

**Method:** shortest route by Dijkstra over door midpoints; each leg is the straight (Euclidean) distance between consecutive points inside one room (door midpoint to door midpoint; the first/last point is the room centre, a fixture centre, or the door/stair point named). Legs ignore furniture, so real walking length is >= these numbers. Porches/outside are never crossed.

| Path | walk ft | room sequence (innermost room each side of each door crossed) |
|---|---|---|
| front door -> kitchen/dining room centre | 60.9 | FOYER > HALL @24.34,29.51 > KITCHEN / DINING |
| front door -> range (main_floor.scad:198) | 69.2 | FOYER > HALL @24.34,29.51 > KITCHEN / DINING |
| garage (room centre) -> kitchen/dining room centre | 52.5 | GARAGE > HALL @24.34,29.51 > KITCHEN / DINING |
| garage (room centre) -> range | 49.4 | GARAGE > HALL @24.34,29.51 > KITCHEN / DINING |
| garage (room centre) -> SCULLERY centre (no pantry room in model) | 47.9 | GARAGE > HALL @24.34,29.51 > KITCHEN / DINING > SCULLERY |
| garage (room centre) -> tall pantry cabinets in kitchen (main_floor.scad:202) | 41.3 | GARAGE > HALL @24.34,29.51 > KITCHEN / DINING |
| master bedroom centre -> WIC @95.95,20.56 centre | 25.0 | MASTER BEDROOM > (closet passage) > WIC @95.95,20.56 |
| master bedroom centre -> WIC @111.41,20.56 centre | 23.9 | MASTER BEDROOM > (closet passage) > WIC @111.41,20.56 |
| master bedroom centre -> LAUNDRY centre | 103.1 | MASTER BEDROOM > (master entry) > HALL @24.34,29.51 > MUDROOM > LAUNDRY |
| BEDROOM 2 centre -> BATH 2 centre | 19.4 | BEDROOM 2 > (suite entry) > (suite entry, 2nd piece) > BATH 2 |
| BEDROOM 2 centre -> hall BATH centre | 47.2 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > BATH |
| BEDROOM 2 centre -> MASTER BATH centre | 127.8 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > HALL @53.95,45.39 > GREAT ROOM > HALL @24.34,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH |
| BEDROOM 2 centre -> LAUNDRY centre | 22.7 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > LAUNDRY |
| BUNK ROOM centre -> BATH 2 centre | 13.3 | BUNK ROOM > BATH 2 |
| BUNK ROOM centre -> hall BATH centre | 35.5 | BUNK ROOM > HALL @22.1,49.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > BATH |
| BUNK ROOM centre -> MASTER BATH centre | 116.1 | BUNK ROOM > HALL @22.1,49.64 > (N-S hall, unlabelled) > (landing at the stair top) > (upper hall, west of its door) > HALL @53.95,45.39 > GREAT ROOM > HALL @24.34,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH |
| BUNK ROOM centre -> LAUNDRY centre | 20.3 | BUNK ROOM > HALL @22.1,49.64 > LAUNDRY |
| foyer centre -> hall BATH centre (no powder room in model; nearest toilet room reachable from the foyer side) | 65.8 | FOYER > HALL @24.34,29.51 > GREAT ROOM > HALL @53.95,45.39 > (upper hall, west of its door) > BATH |
| front door -> top of main stair (top nosing, (44.96, 47.1)) | 77.4 | FOYER > HALL @24.34,29.51 > (N-S hall, unlabelled) > (landing at the stair top) |
| garage mud-entry door -> top of main stair (top nosing, (44.96, 47.1)) | 31.6 | HALL @24.34,29.51 > (N-S hall, unlabelled) > (landing at the stair top) |
| master bedroom centre -> top of main stair (top nosing, (44.96, 47.1)) | 82.4 | MASTER BEDROOM > (master entry) > HALL @24.34,29.51 > GREAT ROOM > HALL @53.95,45.39 > (upper hall, west of its door) > (landing at the stair top) |
| BEDROOM 2 centre -> top of main stair (top nosing, (44.96, 47.1)) | 36.0 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > (N-S hall, unlabelled) > (landing at the stair top) |
| basement stair foot (44.96, 28.725) -> UTILITY centre | 25.6 | HALLWAY > (unlabelled hall) @35.27,28.725 > HALL @37.37,35.08 > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC @95.95,20.56 centre: no (via MASTER BEDROOM > (closet passage) > WIC @95.95,20.56); WIC @111.41,20.56 centre: no (via MASTER BEDROOM > (closet passage) > WIC @111.41,20.56)


## 8. Adjacency facts

### 8.1 GREAT ROOM (main; main_floor.scad:75) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALL @53.95,45.39 | hall | 5.3 | full 58.8 in |
| FLEX ROOM | office | 9.9 | - |
| PATIO | porch (ceil 0) | 1.8 | - |
| HALL @24.34,29.51 | hall | 26.5 | full 312 in |
| OFFICE | office | 12.7 | - |
| DECK | porch (ceil 0) | 26.5 | double 72 in |
| OFFICE PORCH | porch (ceil 0) | 4.4 | - |

### 8.1 DEN (main; main_floor.scad:79) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALL @24.34,29.51 | hall | 14.8 | - |
| FOYER | hall | 25.8 | double 60 in |
| (den alcove) | living | 11.2 | full 128.4 in |
| WIC @95.95,20.56 | closet | 9.0 | - |
| FRONT PORCH | porch (ceil 0) | 14.8 | - |
| (unlabelled porch) @95.95,0 | porch (ceil 0) | 9.3 | - |
| (covered entry) | porch (ceil 0) | 3.7 | - |

### 8.1 SUN ROOM (main; main_floor.scad:70) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| STUDY | office | 9.7 | - |
| HALL @22.1,49.64 | hall | 3.1 | - |
| (landing at the stair top) | hall (ceil 0) | 4.6 | - |
| (upper hall, west of its door) | hall | 6.7 | double 70.8 in |
| PATIO | porch (ceil 0) | 12.7 | double 58.8 in |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are GREAT ROOM, DEN, SUN ROOM. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALLWAY | hall (ceil 0) | 18.9 | open 96 in |
| PET ROOM | utility | 9.5 | - |
| HALL @54.14,13.43 | hall | 4.7 | open 48 in |
| BATH @54.14,5.79 | bath | 7.6 | - |

### 8.2 FOYER (main_floor.scad:78) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALL @24.34,29.51 | hall | 12.0 | full 94.8 in |
| KITCHEN / DINING | kitchen | 23.2 | - |
| BREAKFAST | dining | 2.6 | - |
| DEN | living | 25.8 | double 60 in |
| (covered entry) | porch (ceil 0) | 12.0 | double 74.4 in, glass 24 in, glass 24 in |

### 8.3 Closets, WICs, linen, scullery, storage: exterior exposure

No room is labelled PANTRY in the model. SCULLERY (kind utility) and the 'tall pantry cabinets' fixture row (main_floor.scad:202, inside KITCHEN/DINING) are the pantry-like items.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | SCULLERY | main_floor.scad:49 | S 11.3 (porch/patio (open)); W 8.7 (garage) |
| main | WIC @7.27,48.13 | main_floor.scad:56 | W 3.0 (yard/soil) |
| main | WIC @95.95,20.56 | main_floor.scad:85 | none |
| main | WIC @111.41,20.56 | main_floor.scad:87 | none |
| main | LINEN | main_floor.scad:88 | N 1.2 (porch/patio (open)); E 2.7 (porch/patio (open)), 6.3 (yard/soil) |
| main | (linen between the WCs) | main_floor.scad:91 | none |
| base | STORAGE | basement.scad:56 | W 7.6 (yard/soil) |

Pantry/garage: SCULLERY shares 8.7 ft of wall with the garage; doors between SCULLERY and GARAGE: 0. The garage's doors to the house are: main_floor.scad:119 (GARAGE | (garage side-door pad), 33.6 in); main_floor.scad:120 (GARAGE | SIDE ENTRY, 36 in); main_floor.scad:122 (GARAGE | HALL @24.34,29.51, 36 in). The tall pantry cabinets (x 42.24-49.14) are 17.9 ft east of the garage wall (x 24.34): no shared wall.

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN / DINING | range (198); sink (200); fridge (201); double island (203); prep sink (204) | front door -> kitchen/dining room centre; front door -> range (main_floor.scad:198); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range; garage (room centre) -> SCULLERY centre (no pantry room in model); garage (room centre) -> tall pantry cabinets in kitchen (main_floor.scad:202) |
| LAUNDRY | washer + dryer (210); laundry sink (212) | master bedroom centre -> LAUNDRY centre; BEDROOM 2 centre -> LAUNDRY centre; BUNK ROOM centre -> LAUNDRY centre |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| GARAGE | 2.0 | west driveway (site.scad:111) | N 5.6 (porch/patio (open)), 1.7 (yard/soil); S 24.3 (yard/soil); E 7.5 (porch/patio (open)), 12.1 (yard/soil); W 34.2 (yard/soil) |
| BEDROOM 2 | 9.3 | west driveway (site.scad:111) | S 14.8 (garage); W 3.1 (porch/patio (open)), 9.6 (yard/soil) |
| WIC @7.27,48.13 | 11.1 | west driveway (site.scad:111) | W 3.0 (yard/soil) |
| WC @7.27,51.15 | 13.0 | west driveway (site.scad:111) | W 4.2 (yard/soil) |
| BREAKFAST | 14.0 | loop north leg (:114) | S 15.0 (porch/patio (open)); E 3.7 (porch/patio (open)); W 6.3 (porch/patio (open)) |
| DEN | 14.0 | loop north leg (:114) | S 14.8 (porch/patio (open)); E 9.3 (porch/patio (open)); W 3.7 (porch/patio (open)) |
| BATH 2 | 16.2 | west driveway (site.scad:111) | N 10.2 (yard/soil); W 6.7 (yard/soil) |
| (suite entry) | 16.9 | west driveway (site.scad:111) | none |
| FOYER | 17.7 | loop north leg (:114) | S 12.0 (porch/patio (open)) |
| (suite entry, 2nd piece) | 19.7 | west driveway (site.scad:111) | none |
| KITCHEN / DINING | 20.3 | loop north leg (:114) | S 4.9 (porch/patio (open)), 13.6 (yard/soil); W 7.4 (porch/patio (open)), 7.1 (yard/soil) |
| BUNK ROOM | 22.8 | west driveway (site.scad:111) | N 15.1 (yard/soil); E 3.2 (yard/soil); W 4.6 (yard/soil) |
| (den alcove) | 23.3 | loop north leg (:114) | S 3.8 (porch/patio (open)) |
| MASTER BATH | 23.3 | loop north leg (:114) | S 21.6 (yard/soil); E 11.2 (yard/soil) |
| WC @99.7,9.31 | 23.3 | loop north leg (:114) | S 1.7 (porch/patio (open)), 5.1 (yard/soil) |
| MUDROOM | 24.1 | west driveway (site.scad:111) | S 2.2 (garage) |
| LAUNDRY | 24.1 | west driveway (site.scad:111) | none |
| HALL @22.1,49.64 | 25.3 | west driveway (site.scad:111) | none |
| SCULLERY | 26.3 | west driveway (site.scad:111) | S 11.3 (porch/patio (open)); W 8.7 (garage) |
| HALL @24.34,29.51 | 26.3 | west driveway (site.scad:111) | W 6.0 (garage) |
| (linen between the WCs) | 27.1 | loop north leg (:114) | none |
| WC @99.7,16.71 | 30.7 | loop north leg (:114) | none |
| WIC @95.95,20.56 | 34.6 | loop north leg (:114) | none |
| (closet passage) | 34.6 | loop north leg (:114) | none |
| WIC @111.41,20.56 | 34.6 | loop north leg (:114) | none |
| LINEN | 34.6 | loop north leg (:114) | N 1.2 (porch/patio (open)); E 2.7 (porch/patio (open)), 6.3 (yard/soil) |
| STUDY | 36.5 | west driveway (site.scad:111) | N 4.6 (porch/patio (open)), 5.4 (yard/soil) |
| (N-S hall, unlabelled) | 39.3 | west driveway (site.scad:111) | none |

Other rooms are > 40 ft from any drive. Garage doors face west (axis y, x=0: main_floor.scad:117-118) onto the west driveway; the drive's east edge is x=-2, i.e. 2.0 ft off the garage's west wall.


## 9. Plumbing

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| kitchen sink | KITCHEN / DINING | (39.93, 6.68, 42.57, 8.26) | (41.2, 7.5) | S wall y=6.28 | 0.40 | main_floor.scad:200 |
| prep sink (island) | KITCHEN / DINING | (43.22, 16.68, 44.87, 18.65) | (44.0, 17.7) | island | 7.62 | main_floor.scad:204 |
| scullery sink | SCULLERY | (28.09, 27.34, 31.71, 28.91) | (29.9, 28.1) | N wall y=29.51 | 0.60 | main_floor.scad:208 |
| washer + dryer | LAUNDRY | (28.09, 47.07, 34.01, 49.05) | (31.0, 48.1) | N wall y=49.64 | 0.59 | main_floor.scad:210 |
| laundry sink | LAUNDRY | (33.22, 41.02, 35.1, 43.52) | (34.2, 42.3) | S wall y=40.56 | 0.46 | main_floor.scad:212 |
| Bath 2 tub | BATH 2 | (7.7, 55.55, 10.33, 61.41) | (9.0, 58.5) | S wall y=55.3 | 0.25 | main_floor.scad:219 |
| Bath 2 double vanity | BATH 2 | (10.99, 60.1, 17.3, 61.68) | (14.1, 60.9) | E wall x=17.5 | 0.20 | main_floor.scad:220 |
| Bath 2 suite WC | WC @7.27,51.15 | (8.03, 51.55, 10.33, 53.85) | (9.2, 52.7) | S wall y=51.15 | 0.40 | main_floor.scad:221 |
| hall bath vanity | BATH | (51.78, 42.34, 53.42, 44.31) | (52.6, 43.3) | E wall x=53.95 | 0.53 | main_floor.scad:222 |
| hall bath toilet | BATH | (51.12, 39.7, 53.09, 41.35) | (52.1, 40.5) | E wall x=53.95 | 0.86 | main_floor.scad:223 |
| hall bath shower | BATH | (47.83, 35.89, 53.42, 38.39) | (50.6, 37.1) | S wall y=35.46 | 0.43 | main_floor.scad:224 |
| master double vanity | MASTER BATH | (111.64, 17.86, 121.51, 19.64) | (116.6, 18.8) | N wall y=20.56 | 0.92 | main_floor.scad:225 |
| master shower | MASTER BATH | (111.97, 9.55, 120.2, 14.05) | (116.1, 11.8) | S wall y=9.31 | 0.24 | main_floor.scad:226 |
| master tub | MASTER BATH | (123.16, 9.55, 127.63, 15.03) | (125.4, 12.3) | S wall y=9.31 | 0.24 | main_floor.scad:227 |
| master WC (north) | WC @99.7,16.71 | (100.79, 17.01, 103.42, 19.31) | (102.1, 18.2) | S wall y=16.71 | 0.30 | main_floor.scad:228 |
| master WC (south) | WC @99.7,9.31 | (100.79, 9.77, 103.42, 12.07) | (102.1, 10.9) | S wall y=9.31 | 0.46 | main_floor.scad:229 |

| equipment (non-wet-wall list) | room | centre | source |
|---|---|---|---|
| range (fuel not stated) | KITCHEN / DINING | (37.0, 16.2) | main_floor.scad:198 |
| fridge (water supply not stated) | KITCHEN / DINING | (37.0, 27.5) | main_floor.scad:201 |

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| bath-by-stair WC | BATH @47.27,35.08 | (52.0, 41.5, 53.8, 43.3) | (52.9, 42.4) | E wall x=54.14 | 0.34 | basement.scad:122 |
| bath-by-stair vanity | BATH @47.27,35.08 | (52.1, 38.5, 53.9, 41.0) | (53.0, 39.8) | E wall x=54.14 | 0.24 | basement.scad:123 |
| bath-by-stair shower | BATH @47.27,35.08 | (47.6, 42.0, 50.6, 45.0) | (49.1, 43.5) | W wall x=47.27 | 0.33 | basement.scad:124 |
| pool bath WC | POOL BATH | (100.6, 22.5, 102.4, 24.3) | (101.5, 23.4) | E wall x=103.04 | 0.64 | basement.scad:125 |
| pool bath vanity | POOL BATH | (96.6, 25.5, 98.6, 28.8) | (97.6, 27.1) | W wall x=96.33 | 0.27 | basement.scad:126 |
| pool bath shower | POOL BATH | (99.2, 25.4, 102.45, 28.9) | (100.8, 27.1) | N wall y=29.12 | 0.22 | basement.scad:127 |
| south bath tub | BATH @54.14,5.79 | (54.4, 6.4, 59.4, 8.95) | (56.9, 7.7) | W wall x=54.14 | 0.26 | basement.scad:128 |
| south bath vanity | BATH @54.14,5.79 | (62.5, 6.4, 67.1, 8.25) | (64.8, 7.3) | E wall x=67.4 | 0.30 | basement.scad:129 |
| south bath WC | BATH @54.14,5.79 | (65.2, 9.5, 67.1, 11.3) | (66.2, 10.4) | E wall x=67.4 | 0.30 | basement.scad:130 |
| laundry washer + dryer | LAUNDRY | (67.8, 6.4, 72.6, 8.75) | (70.2, 7.6) | W wall x=67.4 | 0.40 | basement.scad:132 |
| dog wash (pet room) | PET ROOM | (65.5, 26.5, 69.0, 28.9) | (67.2, 27.7) | N wall y=29.12 | 0.22 | basement.scad:134 |

| equipment (non-wet-wall list) | room | centre | source |
|---|---|---|---|
| air handler | UTILITY | (24.3, 37.2) | basement.scad:136 |
| boiler | UTILITY | (27.4, 36.7) | basement.scad:137 |
| water heater | UTILITY | (30.1, 36.8) | basement.scad:138 |
| well-water treatment | UTILITY | (35.2, 36.7) | basement.scad:139 |
| HRV (wall-mounted, z 5.5-7) | UTILITY | (24.3, 41.3) | basement.scad:140 |
| pool filter (round) | POOL EQUIP. | (101.1, 39.9) | basement.scad:142 |
| pool pump | POOL EQUIP. | (98.0, 40.1) | basement.scad:143 |
| pool heater | POOL EQUIP. | (101.0, 34.5) | basement.scad:144 |
| pool dehumidifier | POOL EQUIP. | (100.8, 31.0) | basement.scad:145 |
| pool chemicals | POOL EQUIP. | (97.8, 30.4) | basement.scad:146 |
| laundry counter (sink not stated) | LAUNDRY | (79.0, 7.4) | basement.scad:133 |

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | kitchen sink | KITCHEN / DINING | y=6.28 (horizontal wall) | (41.2, 7.5) |
| G2 | master WC (south) | WC @99.7,9.31 | y=9.31 (horizontal wall) | (102.1, 10.9) |
| G3 | master shower; master tub | MASTER BATH | y=9.31 (horizontal wall) | (120.7, 12.0) |
| G4 | prep sink (island) | KITCHEN / DINING | free-standing island (>3 ft from any wall) | (44.0, 17.7) |
| G5 | master WC (north) | WC @99.7,16.71 | y=16.71 (horizontal wall) | (102.1, 18.2) |
| G6 | master double vanity | MASTER BATH | y=20.56 (horizontal wall) | (116.6, 18.8) |
| G7 | scullery sink | SCULLERY | y=29.51 (horizontal wall) | (29.9, 28.1) |
| G8 | hall bath shower | BATH | y=35.46 (horizontal wall) | (50.6, 37.1) |
| G9 | laundry sink | LAUNDRY | y=40.56 (horizontal wall) | (34.2, 42.3) |
| G10 | hall bath vanity; hall bath toilet | BATH | x=53.95 (vertical wall) | (52.4, 41.9) |
| G11 | washer + dryer | LAUNDRY | y=49.64 (horizontal wall) | (31.0, 48.1) |
| G12 | Bath 2 suite WC | WC @7.27,51.15 | y=51.15 (horizontal wall) | (9.2, 52.7) |
| G13 | Bath 2 tub | BATH 2 | y=55.3 (horizontal wall) | (9.0, 58.5) |
| G14 | Bath 2 double vanity | BATH 2 | x=17.5 (vertical wall) | (14.1, 60.9) |

**Main floor: 14 wet-wall groups** (5 back-to-back plumbing clusters of rooms: SCULLERY+KITCHEN / DINING | LAUNDRY | WC @7.27,51.15+BATH 2 | BATH | MASTER BATH+WC @99.7,16.71+WC @99.7,9.31)

Basement:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | south bath vanity; south bath WC; laundry washer + dryer | BATH @54.14,5.79; LAUNDRY | x=67.4 (vertical wall) | (67.0, 8.4) |
| G2 | south bath tub | BATH @54.14,5.79 | x=54.14 (vertical wall) | (56.9, 7.7) |
| G3 | pool bath WC | POOL BATH | x=103.04 (vertical wall) | (101.5, 23.4) |
| G4 | pool bath vanity | POOL BATH | x=96.33 (vertical wall) | (97.6, 27.1) |
| G5 | pool bath shower | POOL BATH | y=29.12 (horizontal wall) | (100.8, 27.1) |
| G6 | dog wash (pet room) | PET ROOM | y=29.12 (horizontal wall) | (67.2, 27.7) |
| G7 | bath-by-stair WC; bath-by-stair vanity | BATH @47.27,35.08 | x=54.14 (vertical wall) | (53.0, 41.1) |
| G8 | bath-by-stair shower | BATH @47.27,35.08 | x=47.27 (vertical wall) | (49.1, 43.5) |

**Basement: 8 wet-wall groups** (4 clusters: BATH @47.27,35.08 | PET ROOM | POOL BATH | BATH @54.14,5.79+LAUNDRY)

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 14/8; 6 ft: 14/8; 8 ft: 14/8; 12 ft: 13/8; inf: 13/6

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | kitchen sink | (41.2,7.5) | B2 (BATH @54.14,5.79) | (56.9,7.7) | 15.6 | 0.2 | 15.9 |
| G2 | master WC (south) | (102.1,10.9) | B3 (POOL BATH) | (101.5,23.4) | 0.6 | 12.5 | 13.1 |
| G3 | master shower; master tub | (120.7,12.0) | B3 (POOL BATH) | (101.5,23.4) | 19.2 | 11.4 | 30.6 |
| G4 | prep sink (island) | (44.0,17.7) | B2 (BATH @54.14,5.79) | (56.9,7.7) | 12.9 | 10.0 | 22.8 |
| G5 | master WC (north) | (102.1,18.2) | B3 (POOL BATH) | (101.5,23.4) | 0.6 | 5.2 | 5.8 |
| G6 | master double vanity | (116.6,18.8) | B3 (POOL BATH) | (101.5,23.4) | 15.1 | 4.6 | 19.7 |
| G7 | scullery sink | (29.9,28.1) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 19.2 | 15.4 | 34.6 |
| G8 | hall bath shower | (50.6,37.1) | B7 (BATH @47.27,35.08) | (53.0,41.1) | 2.3 | 3.9 | 6.3 |
| G9 | laundry sink | (34.2,42.3) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 14.9 | 1.2 | 16.2 |
| G10 | hall bath vanity; hall bath toilet | (52.4,41.9) | B7 (BATH @47.27,35.08) | (53.0,41.1) | 0.6 | 0.9 | 1.4 |
| G11 | washer + dryer | (31.0,48.1) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 18.1 | 4.6 | 22.6 |
| G12 | Bath 2 suite WC | (9.2,52.7) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 39.9 | 9.2 | 49.1 |
| G13 | Bath 2 tub | (9.0,58.5) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 40.1 | 15.0 | 55.1 |
| G14 | Bath 2 double vanity | (14.1,60.9) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 35.0 | 17.4 | 52.3 |

Main-floor groups with a basement group within 5 ft Manhattan: 1 of 14; within 10 ft: 3.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (41.2,7.5) | 69.6 | 50.5 |
| G2 | (102.1,10.9) | 127.0 | 107.9 |
| G3 | (120.7,12.0) | 144.5 | 125.4 |
| G4 | (44.0,17.7) | 62.2 | 43.1 |
| G5 | (102.1,18.2) | 119.8 | 100.7 |
| G6 | (116.6,18.8) | 133.7 | 114.6 |
| G7 | (29.9,28.1) | 37.6 | 18.5 |
| G8 | (50.6,37.1) | 49.3 | 30.2 |
| G9 | (34.2,42.3) | 27.7 | 15.4 |
| G10 | (52.4,41.9) | 46.3 | 33.2 |
| G11 | (31.0,48.1) | 18.8 | 18.1 |
| G12 | (9.2,52.7) | 18.3 | 26.8 |
| G13 | (9.0,58.5) | 13.6 | 32.7 |
| G14 | (14.1,60.9) | 10.9 | 30.0 |

**DRI (E = (22.16, 58)) = 879.4 ft over 14 groups; mean 62.8 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 747.1 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:138, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:137). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **master tub, 119.8 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: master tub, 122.4 ft.
- Furthest basement fixture: **pool bath WC, 84.8 ft** from the water heater.
- Nearest main-floor fixture: scullery sink, 8.9 ft.

Per fixture (Manhattan plan ft from the water heater): kitchen sink 40; prep sink (island) 33; scullery sink 9; washer + dryer 12; laundry sink 10; Bath 2 tub 43; Bath 2 double vanity 40; Bath 2 suite WC 37; hall bath vanity 29; hall bath toilet 26; hall bath shower 21; master double vanity 105; master shower 111; master tub 120; master WC (north) 91; master WC (south) 98; bath-by-stair WC 28; bath-by-stair vanity 26; bath-by-stair shower 26; pool bath WC 85; pool bath vanity 77; pool bath shower 80; south bath tub 56; south bath vanity 64; south bath WC 62; laundry washer + dryer 69; dog wash (pet room) 46


## 10. Stairs

### 10.1 Main to basement stair (house_lib.scad:107-125, values via model.json `stair`)

| Item | Value | Source / formula |
|---|---|---|
| Wall centre lines x | 42.65 to 47.27 | house_lib.scad:120 stair_x() |
| Clear width between walls | 4.22 ft = 50.6 in | x range minus wall_t 0.4 (Redesign doc line 157 says 4'-2 1/2") |
| Floor to floor | 13.75 ft | house_lib.scad:107 |
| Risers / rise each | 22 x 7.500 in | house_lib.scad:121-122 ceil(floor_to_floor*12/7.5) |
| Treads / run each | 21 x 10.5 in | house_lib.scad:123 stair_run=10.5/12; treads = risers-1 |
| Total run | 18.375 ft (220.5 in) | 21 x 10.5 in |
| Top nosing y / foot y | 47.1 / 28.725 | house_lib.scad:124-125; foot = top - 21*run |
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | main_floor.scad:64 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | basement.scad:59 |
| Headroom | Redesign doc: >= 1 993 mm at the tightest point vs 1 950 mm required; the floor opening was sized for it (house_lib.scad:112-119 comment) | Redesign-and-Spec-2026-11-02.md:158, 162-167; not recomputed here |
| Handrails | both sides in the model (house_lib.scad main_stair rail=true) | house_lib.scad:324-340 main_stair(); Redesign doc:159 |
| Landings | top: the stair landing/upper hall; bottom: HALLWAY at the 8 ft archway (basement.scad:89 'open' 8 ft) into the living room | Redesign doc:160 |

### 10.2 Basement exit stair (foundation.scad:134-142, model.json `exit_stair`)

| Item | Value | Source |
|---|---|---|
| Door | x 46.2, 3.5 ft wide (42 in) in the gym's north wall y=63.16, opens in | basement.scad:98; foundation.scad:134 |
| Rise to grade | 11.75 ft; 19 risers x 7.42 in | foundation.scad:135-136 |
| Run | 11 in treads; flight length 16.50 ft | foundation.scad:137, 139 |
| Landing x range | [45.6, 50.3] | foundation.scad:138 |
| Areaway clear inside | x 45.6-66.80, y 63.75-67.75 (4.0 ft wide) | foundation.scad:139 |
| Top landing at grade | 2.2 ft past the top step | foundation.scad:141 |
| Footprint with walls | [44.93, 63.09, 69, 68.42] | foundation.scad:144 |
| Direction | rises east along the house's north side, ending beside the deck steps (Redesign doc:473-480) | Redesign doc |

The exit stair comes up beside the PATIO, whose north edge has a guard (main_floor.scad:345-354 patio_guard). Basement windows: 2 wells (foundation.scad:159-162).


## 11. Electrical and mechanical facts

| Item | As stated | Source |
|---|---|---|
| Electric service entrance | Underground from the road to a meter on the **west wall**; the house's own service (not fed from the shop) | permit README:152-153; make_drawings.py:1488-1491; site.scad:10-17 |
| Service route in the model | three dashed lines (fibre y=44, power y=46, gas y=48) run east from x = -41/-44/-47 to x = 7.27 (the bedroom wing's west wall, a crawl-space wing) | site.scad:162-164 |
| Meters | two boxes on the west wall at x = 6.6, y = 45 and 47.5, 3 ft above grade (not labelled which is which) | site.scad:175 |
| Panel | in the basement UTILITY room (x 22.16..37.37, y 35.08..42.77); no position or box in the fixture tables | permit README:144-145, 153; make_drawings.py:1491, 2254 |
| Panel size / service amperage | **not in model** for the house as built-first. "200 A panel fed from the shop" appears only in the Shop-Base-Plan (lines 84, 234, 323, 364), whose Nov 3 update says the house has its own services from the road (Shop-Base-Plan:9-11) | Shop-Base-Plan.md |
| Generator, batteries, switchgear | in the model only in the shop (Bay 1: shop.scad:145-151); none in the house model | shop.scad |
| Heating plant | basement UTILITY room: five boxes listed in the order of the comment "air handler, boiler, water heater, well-water treatment, HRV" (basement.scad:135): air handler (22.8..25.8, 35.7..38.7, 6 ft high, basement.scad:136), boiler (26.3..28.5 x 35.7..37.7, 3.5 ft, :137), water heater (round 29.0..31.2 x 35.7..37.9, 5.5 ft, :138), well-water treatment (33.8..36.6 x 35.7..37.7, :139), HRV (22.8..25.8 x 40.4..42.3, z 5.5-7, :140). The mapping is by comment order. Permit README says "furnace or boiler" (make_drawings.py:2254) and "heating, HRV, water heater, water treatment, the electrical panel and the sump pump" (permit README:144-145) | basement.scad:135-140 |
| Boiler / heat output, fuel, heat-loss calc | **not in model**; Oct 28 decision #21 (a/b/c) is open (House-Review-and-Research:1043-1047) | |
| Water heater | one, in the UTILITY room (above); no recirculation, no second heater modelled | basement.scad:138 |
| Gas / propane | Natural gas from the road if served, else 1 000 US gal propane tank at (-60, -45) (pad 16 x 6 ft) with a line east along y = -45 to x = -47, then north along the gas line (x = -47) to the house (y = 48) | site.scad:64, 164, 170-173; permit README:154-156 |
| Gas appliances | range (fuel not stated, main_floor.scad:198); great-room fireplace box (gas or wood undecided, main_floor.scad:241; permit README:108-109) | |
| Internet | fibre (x = -41 line) or a Starlink dish at (12, 80) with a drop to (12, 62.04) | site.scad:65, 162, 181-183; permit README:168-172 |
| Pool plant | pool equipment room x 96.33..103.04, y 29.12..41.94: filter (round), pump, heater, dehumidifier, chemicals (basement.scad:141-146); pool dehumidifier row at basement.scad:145 (comment order); pool/spa water: foundation.scad:57-58, 63-65 | basement.scad |
| Sump, floor drains, radon | Redesign/permit text only (sump "utility room is suggested", permit README:476-477; Redesign:224, 345, 497); no location or box in the models | |
| Well water | well (150, 75), line to (150, 45) then (126.97, 45); water treatment in UTILITY (basement.scad:139) | site.scad:63, 167 |

## 12. Site distances

Read with `phase = "house"` (site.scad:47, the default) for everything except the shop rows, which are the `phase = "full"` geometry (site.scad:122-131, 196-197, 245) and the future-shop dashed rectangle (site.scad:217-221, shop_origin() = [0,130], site.scad:60). Land is not chosen: positions are relative to the house (site.scad:6-8). Road assumed on the south (site.scad:8, 74: road north edge y = -100).

### 12.1 Coordinates (site.scad)

| Item | Coordinates [x0,y0,x1,y1] or point | Source |
|---|---|---|
| Septic tank | [-3, 52, 3, 64]  (6 x 12 ft) | site.scad:70 |
| Pump chamber | [-3, 64, 3, 68] | site.scad:71 |
| Treatment field | [-120, 45, -65, 100]  (55 x 55 ft) | site.scad:72 |
| Reserve field | [-120, -15, -65, 40] | site.scad:73 |
| Well | (150, 75) | site.scad:63 |
| Propane tank | (-60, -45) centre; pad 16 x 6 ft | site.scad:64, 170 |
| Starlink dish | (12, 80) | site.scad:65 |
| West driveway | x -32..-2 (30 ft wide), y -100..42 (142 ft long) | site.scad:111 |
| Front loop | ring x 25..130, y -72..-14, 14 ft wide legs; connector x -2..25, y -50..-36 | site.scad:113-117 |
| Future shop (house phase) | dashed [0,130]-[100,230] | site.scad:60, 218 |
| Service lines | fibre x=-41, power x=-44, gas x=-47, from y=-100 north to y=44/46/48 then east to x=7.27 (bedroom-wing west wall) | site.scad:162-164 |
| Meters | two boxes on x=6.6, y 45 and 47.5 | site.scad:175 |
| Water line | well (150,75) -> (150,45) -> (126.97,45) | site.scad:167 |
| Building sewer | (22.16,58) -> (3,58) (tank east face); effluent line (-3,66) -> (-65,66) | site.scad:188, 191 |

### 12.2 Distances (computed with shapely from those rectangles; ft and m)

| Pair | Distance |
|---|---|
| Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27) | 4.3 ft (1.3 m) |
| Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6) | 19.16 ft (5.8 m) / 18.61 ft |
| Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner | 21.3 ft (6.5 m) |
| Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour | 19.2 ft (5.8 m) |
| Septic tank to well | 147.4 ft (44.9 m) |
| Pump chamber to well | 147.2 ft (44.9 m) |
| Treatment field to well | 215.0 ft (65.5 m) |
| Reserve field to well | 217.8 ft (66.4 m) |
| Treatment field to the basement (outline polygon) | 87.2 ft (26.6 m) |
| Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27) | 72.3 ft (22.0 m) |
| Treatment field to the garage west wall (x=0, slab, no basement) | 65.7 ft (20.0 m) |
| Reserve field to basement | 87.2 ft (26.6 m) |
| Reserve field to the nearest heated wall | 72.3 ft (22.0 m) |
| Reserve field to the garage | 65.0 ft (19.8 m) |
| Treatment field to west driveway edge (x=-32) | 33.1 ft (10.1 m) |
| Reserve field to west driveway edge | 33.0 ft (10.1 m) |
| Treatment field to the service-line corridor (x=-47..-41) | 18.0 ft (5.5 m) |
| Reserve field to the service-line corridor | 18.0 ft (5.5 m) |
| Reserve field to propane pad (-68..-52, -48..-42) | 27.0 ft (8.2 m) |
| Well to heated main-floor wall (nearest) | 31.9 ft (9.7 m) |
| Well to side porch/deck edge (nearest unconditioned main-floor row) | 19.8 ft (6.0 m) |
| Well to basement outline | 57.4 ft (17.5 m) |
| House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130) | 63.4 ft (19.3 m) |
| House incl. porches/deck to future shop | 63.4 ft (19.3 m) |
| Basement exit areaway (y 67.75) to shop | 62.3 ft (19.0 m) |
| Garage to shop (garage north wall 35.46) | 94.5 ft (28.8 m) |

Corridor and drive lengths: power run road->meter wall 197.3 ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas 202.3 ft; fibre 192.3 ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: 53.0 ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).

West driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).

phase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.

Phase house: parents' house and geothermal loop field are not in site.scad (§13).


## 13. Run-document premises vs the model on main

Status key: PRESENT = in the model/docs on main as the run brief states; ABSENT = not in the models or docs; CHANGED = exists in a different form.

| # | Premise | Status | Evidence |
|---|---|---|---|
| a | ~70 ft heated, walkable utility tunnel house-shop, floor at basement level | **ABSENT (dropped)** | "No tunnel": site.scad:33-35; Redesign:22-23, 39-40, 559-566; permit README:121-124, 520; Shop-Base-Plan.md:15-19 (its §5, §6 and the tunnel drawing are kept "for reference only"). No tunnel geometry in site.scad. Leftovers: shop.scad:19-23 comment, "TUNNEL PORTAL" room (shop.scad:62) and its stair well (shop.scad:158-161) are still drawn in the shop. The old landing room (UTILITIES x 60.1..100.1, Shop-Base-Plan:96) is not in the basement: UTILITY is x 22.16..37.37 (basement.scad:57). Shop to house gap in the model is 63 ft of yard (§12) and a 210 ft buried-service route (site.scad:197) |
| b | Shop is the electrical service point; house has a 200 A panel fed from the shop | **CHANGED** | Described in Shop-Base-Plan.md:81-86, 226-236, 323; replaced by the Nov 3 update at :9-11 (house has its own services from the road) and permit README:152-153 (power from the road to a west-wall meter, panel in the basement UTILITY room); site.scad:10-17, 162-175. No panel size for the house anywhere except the superseded 200 A |
| c | Heating plant (boiler for pool + DHW + snow melt + house heat; geothermal backup) in shop Bay 1 | **CHANGED** | Shop boiler drawn in Bay 1 "WATER + HEAT" (shop.scad:152, room shop.scad:61) and described as the hub (Shop-Base-Plan.md:101, 289-298); but the house also has its own boiler and water heater in the basement UTILITY room (basement.scad:135-138) and the Nov 3 update retires the hub idea (Shop-Base-Plan.md:12-13). Geothermal: see (d) |
| d | Geothermal loop field | **ABSENT** from models and from the house/permit docs. Only: research (House-Review-and-Research §2, lines 757-855; decision #21 at 1043-1047, "GSHP" option) and one phrase "a future ground-source unit fits beside" the shop boiler (Shop-Base-Plan.md:296-298). No loop-field rectangle in site.scad |
| e | Heated driveway / walkways (snow melt) | **ABSENT** from models and Redesign/permit docs. Documented only as research (House-Review-and-Research §3 lines 855-925, decision #23 at 1050-1054) and as a shop-boiler load (Shop-Base-Plan.md:101, 289-295). Exit-stair treads "heated or heat-traced... worth considering" (Redesign:500). Drives in site.scad:108-132 are plain slabs |
| f | "U-stair in the former bar area" of the basement | **CHANGED** | Oct 28/29: option A decided (House-Review-and-Research:979-982, 1085-1086, 1131, 1171). Nov redesign model: one straight 22-riser stair, x 42.65..47.27, top y 47.1, foot y 28.725 (house_lib.scad:120-125; basement.scad:59; Redesign:117-121, 150-170); no "bar" room or U-stair anywhere in basement.scad |
| g | 80 ft truck apron; turning room for a Volvo VNL with trailer | **CHANGED / ABSENT** | Apron is **70 ft** deep in both docs and model: Shop-Base-Plan.md:112 (x -72..0) and site.scad:125 (x -72..-2, y 130..230), plus a 60 ft deep east apron (site.scad:130; Shop-Base-Plan.md:59) and a 32 ft north leg (site.scad:129). No 80 ft dimension and no "VNL" in models or docs. Only "tractor-trailer's ~50 ft outside turning radius" (Shop-Base-Plan.md:71; site.scad:127-128 comment). All of this exists only with `phase = "full"` |
| h | Shared drive | **PRESENT** | "A shared driveway runs up the west side" (Shop-Base-Plan.md:42, 113-116); site.scad:111 (house drive) and 124 (continues north at x -38..-8 in full phase). In the house phase the drive ends at y = 42 (site.scad:111) |
| i | Parents' house (no basement, crawl space, floor 2'-4" up, porch roof posts, 500 lb egg-chair hook) | **ABSENT from the SCAD models; PRESENT as drawings only** | Not in any `.scad`. Plan images `docs/small_house/IMG_0415..0420.PNG` (read by me): "PARENTS' HOUSE - FLOOR PLAN v1", 32' x 21' = 672 SF, 1 bed / 1 bath, "CRAWL SPACE (NO BASEMENT) - SERVICES: FROM MAIN HOUSE (TBD)", 7'-0" x 32'-0" porch, mech closet, W/D, an "EGG CHAIR HOOK: doubled joist + blocking, rated eye-bolt (500 lb design)" on the plan, porch posts in the elevations. The 2'-4" floor height is not readable in the images (an unmeasured base band is drawn). Text mentions: permit README:212-215 ("a future house for the parents is planned"); make_drawings.py:1503. Position on the lot, distance to the main house and foundation type in a model: **not in model** |
| j | 100 x 100 ft shop, 4 bays with wash bay, Bay 1 bathroom draining west by gravity | **PRESENT / CHANGED** | 100 x 100 (site.scad:218; shop.scad:46), four bays Bay 1 utilities / Bay 2 truck / Bay 3 truck + pit / Bay 4 wash (shop.scad:47-52; roof 100 x 100 at shop.scad:165); "NETWORK + BATH" room in Bay 1 (shop.scad:60). Gravity west then north: Shop-Base-Plan.md:300-306, 416-417; the Nov 3 update says instead the shop bathroom "pumps to the house tank through a small lift station in Bay 1" (Shop-Base-Plan.md:28-29). Also Shop-Base-Plan.md:404-412 has the house pumping to a shop tank. Drain direction is not in shop.scad |
| k | Septic on the west by the utility room; well on the east | **PRESENT, with a note** | Tank [-3,52,3,64], field [-120,45,-65,100], reserve [-120,-15,-65,40], well (150,75) (site.scad:63, 70-73); permit README:157-166. The tank sits at y 52..64, beside the bedroom wing and MUSIC ROOM; the UTILITY room is y 35.08..42.77 (9-17 ft south of the tank's south edge (y 52); §12). Shop-Base-Plan.md:9-11 header bullets state the reverse (well west, septic east), contradicted at :20-21 |
| l | Basement pool and spa | **PRESENT** | POOL ROOM row (basement.scad:67), pool 15 x 15 ft and spa 8 x 8.2 ft (foundation.scad:57-58), water depth 4.5 ft / 3.5 ft (foundation.scad:61-65), equipment room and pool bath (basement.scad:68-69); Redesign §4 |
| m | Main-floor baseline: model traced from `main_floor.jpg` (Nov redesign); run doc says `floor_plan.JPEG` "geometry matches the current model" | **CHANGED** (matches `main_floor.jpg`; `floor_plan.JPEG` matches in footprint only) | main_floor.scad:4-8; Redesign:3-5 calls floor_plan.JPEG "the version before them" |

**(m) image comparison (viewed at a glance, both sheets: front porch at the bottom, garage at the left).** Shared: the same overall footprint and wing pattern: garage on the west edge, a bedroom wing at the north-west, a large central block, two side wings with a covered porch/deck on the north and the master wing on the east, a front porch along the south. Different: in `floor_plan.JPEG` the big central room with the island and sink is in the upper middle (where `main_floor.jpg` has the GREAT ROOM), the south-centre holds two dining/study rooms, hallways and a patio, there is a stair/utility cluster at the garage corner and a row of pantries and storage rooms in the middle-east; in `main_floor.jpg` (and the model) the KITCHEN / DINING (35.6..69.14, y 6.28..29.51), BREAKFAST bay, FOYER and DEN are at the south-centre, the GREAT ROOM is north-centre, and the garage-side cluster is mudroom/laundry/scullery with a single stair at x 42.65..47.27. The two sheets agree on the footprint and the position of the garage and master wing, not on where the kitchen, great room and stair sit. The model's room layout matches `main_floor.jpg` (main_floor.scad:4-8), so the run document's claim that `floor_plan.JPEG`'s "geometry matches the current model" holds for the footprint only; Redesign:3-5 calls `floor_plan.JPEG` the earlier version.

## 14. Oct 28 decision list status (23 items, House-Review-and-Research-2026-10-28.md:977-1054)

| # | Item (doc lines) | Status | Evidence |
|---|---|---|---|
| 1 | Basement stair A/B/C (979-982) | superseded | Decided A (U-stair in the bar) Oct 29, lines 1085-1086, 1131; replaced by the Nov redesign's straight stair (Redesign:117-121, 150-170; basement.scad:1-21) |
| 2 | One interior stair or two (983-984) | decided | No second stair (1132); main stair + exit stair only (Redesign:140) |
| 3 | Basement bathroom by the pool (985-986) | decided | Pool bath added (1124, 1132); basement has POOL BATH + 2 BATH rows (basement.scad:60, 69, 71); under-slab rough-in listed (permit README:466-475) |
| 4 | Basement outline (987-989) | superseded | Oct 29 kept a 100 x 60 rectangle (1133); Nov outline is a 14-vertex 3,475 sq ft polygon with crawl space/frost walls elsewhere (foundation.scad:40-45, 90-105; Redesign:238-252) |
| 5 | Theater sound/vibration package (990-992) | decided (spec) | "Still open" Oct 29 (1136-1137); room-within-a-room spec in Redesign:434-436 |
| 6 | Exit stair vs side porch (993-994) | superseded | Moved Oct 29 (1134), then redone: areaway off the gym's north wall, patio guard (Redesign:446-480; foundation.scad:134-145; main_floor.scad:345-354) |
| 7 | Ask architect: garage-corner stair, side-load garage doors (995-997) | open | No later doc records an answer; model draws side-load (west) garage doors (main_floor.scad:117-118) and no garage-corner stair |
| 8 | Gas service (1001-1002) | open | Propane fallback in the model (site.scad:64, 170-173; permit README:154-156); land not chosen |
| 9 | Well prospects (1003-1005) | open | Land not chosen (site.scad:6-8); well drawn at (150,75) |
| 10 | Climate zone (1006-1008) | open | "7A or 7B... from the location" (permit README:77, 295 blank) |
| 11 | Geotechnical report (1009-1010) | open | Redesign:559-575 open questions ("Geotech first") |
| 12 | ICF core 8 in (1014) | decided | 13 1/4 in wall (foundation.scad:37; House-Review:1125) |
| 13 | Waterproofing in writing (1016-1017) | open (spec'd) | Waterproofing spec in Redesign:218-228; contract-scope wording not in repo |
| 14 | ICF above grade? (1018) | decided | Basement-only ICF; main floor on frost walls/crawl space (foundation.scad:90-105; Redesign:238-252) |
| 15 | Wall assembly (1019-1020) | open | No wall assembly in Redesign/permit docs; models draw 0.4 ft walls |
| 16 | Window spec (1021-1024) | open | No window spec in the later docs; window rows are geometry only (main_floor.scad:174-192) |
| 17 | Pool room = natatorium spec (1025-1028) | decided (input) | Dehumidification and the room around the pool in Redesign:358-373; pool dehumidifier in the model (basement.scad:145); permit README:395, 460 |
| 18 | Roof package (1029-1031) | open | Roof "product parked until land"; model has 16 hip blocks, 6/12 (main_floor.scad:305-322) |
| 19 | Before-the-pour checklist (1032-1034) | decided (listed) | Phase 1 rough-ins checklist, permit README:466-480 (under-slab drains, sump, radon, pool); well/septic/service entries in README:149-172 |
| 20 | Well contract (1038-1042) | open | No contract terms in repo; land not chosen |
| 21 | Heating plant architecture (1043-1047) | open | House has air handler + boiler + water heater boxes (basement.scad:135-138), fuel and type not chosen; the shop-hub version is superseded (Shop-Base-Plan.md:12-13) |
| 22 | Distribution: radiant (1048-1049) | open | Only "essential if the slab carries in-floor heat" (Redesign:211); no distribution in models |
| 23 | Snow-melt scope (1050-1054) | open | Not in models; shop-boiler tie superseded (Shop-Base-Plan.md:101) |

Count: decided 7 (2, 3, 12, 14, 17, 19 and 5 as spec), superseded 3 (1, 4, 6), open 13 (7-11, 13, 15, 16, 18, 20-23).

## 15. Model inconsistencies noticed (facts only)

1. **Stair length, comments vs table.** main_floor.scad:13-14 and basement.scad:12 say the stair "runs 15 3/4 ft"; the table gives 21 treads x 10.5 in = 18.375 ft (house_lib.scad:121-125), and Redesign:120, 155 say 18'-4 1/2".
2. **Basement door count.** Redesign:125 says 19 doors were added; basement.scad:79-98 has 20 door rows (14 swing doors, 2 "open", 4 "full").
3. **"By the UTILITY room" vs the drawn sewer and tank.** site.scad:22, 185-186, permit README:157, Redesign:564 place the septic tank / sewer at the UTILITY room (y 35.08..42.77); the model draws the tank at y 52..64 (site.scad:70) and the building sewer leaving at (22.16, 58) (site.scad:188), which is the MUSIC ROOM's west wall (y 50.35..63.16, basement.scad:54).
4. **Service lines stop at the crawl-space wing.** Power/gas/fibre end at x = 7.27 (site.scad:162-164, 175), the bedroom wing's west wall; the UTILITY room and panel are at x 22.16..37.37 (basement.scad:57), 14.9 ft further east, and the lines are at y 44..48, i.e. beside STORAGE (y 42.77..50.35), not UTILITY (y 35.08..42.77).
5. **Well water line stops at the master bedroom.** site.scad:167 ends at (126.97, 45); the docs say it enters at the pool equipment room (permit README:164-166), whose east wall is x = 103.04 (basement.scad:68), 24 ft west.
6. **Shop-Base-Plan contradicts itself and the model.** Header bullets at lines 9-11 (well west, septic east) vs lines 20-21, permit README:157-166 and site.scad:63, 70 (septic west, well east); body: well at (140, 110) (lines 72, 126) vs site.scad:63 (150, 75); septic zone around (-89, 212) (line 131) vs site.scad:70; "tunnel ~70 ft" and 200 A feeder through it (lines 96, 234) vs lines 15-19; title line 1 "utility hub + tunnel to house".
7. **Shop still draws the tunnel.** shop.scad:19-23, 62, 158-160 (portal room and stair well) while site.scad:33-35 says the tunnel is gone.
8. **Shop bathroom drainage.** Gravity west (Shop-Base-Plan.md:300-306, 416-417) vs pumped to the house tank (Shop-Base-Plan.md:28-29) vs house pumps to a shop tank (lines 404-412).
9. **Basement size across docs.** Oct 28 doc: 6,000 sq ft, 100 x 60 ft (House-Review:28, 275, 638-639); Redesign:523 "3,000 ft2 basement"; model polygon 3,475 sq ft, bbox 80.9 x 57.4 ft (foundation.scad:40-45; §1).
10. **Building area vs the Part 9 limit.** Redesign:574 says about 626 m2 to the outside face of the walls (house with attached garage); model heated + garage footprint = 6,319 sq ft = 587 m2 at wall centre lines, 595 m2 with 0.2 ft added each side (house_lib wall_t/2), 604 m2 with 0.4 ft; porches excluded in all three (computed from main_floor.scad:47-104 rows, kind not porch). The 626 m2 is not reproduced.
11. **Gym exit door.** Redesign:543 says a "full-glass 3'-6" exit door"; basement.scad:98 draws type "door" (opaque leaf), width 3.5 ft.
12. **Unnamed rows.** 9 main-floor and 2 basement hall/closet rows have an empty label and are identified here only from source-line comments (main_floor.scad:54-55, 63, 65-66, 80, 84, 86, 91; basement.scad:62-63).
13. **Pantry.** No PANTRY room exists in the main-floor table; floor_plan.JPEG labels several pantries, and main_floor.scad:202 has "tall pantry cabinets" inside the kitchen; SCULLERY is the nearest room (§8.3).
14. **Powder room.** No half bath on the main floor; the only toilets are in the bedroom-2 suite WC, the hall BATH and the master WCs (§9).
