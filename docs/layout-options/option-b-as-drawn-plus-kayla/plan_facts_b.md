# Plan facts (variant mode)

main = `/home/user/house-layout/docs/layout-options/option-b-as-drawn-plus-kayla/main_floor_b.scad`, basement = `/home/user/house-layout/docs/layout-options/option-b-as-drawn-plus-kayla/basement_b.scad`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.

## Layout matrix

Source files: main = `/home/user/house-layout/docs/layout-options/option-b-as-drawn-plus-kayla/main_floor_b.scad`; basement = `/home/user/house-layout/docs/layout-options/option-b-as-drawn-plus-kayla/basement_b.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 5,417 | 5417.2; excl. stair opening 5346.3 |
| Building area, centre lines (house + attached garage) | 565.6 m2 | 6088 sq ft |
| Building area, outside face | 585.7 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Circulation % (strict / with foyer) | 13.6% / 14.8% | 737 sq ft strict of 5417 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 30 | type `door` rows, by opening width |
| Double / open counts (main) | 14 / 1 | type `double` / type `open` |
| Minimum hall clear width | 4.95 ft ((N-S hall, unlabelled)) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 1.15 ft ((suite entry, 2nd piece)) |
| Wet-wall groups (main / basement) | 16 / 8 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 2 of 16 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 1161.6 ft | alternate exit (22.16, 38.9): 1014.3 ft |
| Water heater -> furthest fixture (main / basement) | 114.8 ft (toilet/tub/wash basin (MASTER BATH)) / 84.8 ft (toilet/tub/wash basin (POOL BATH)) | water heater at (30.1, 36.8); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 99.3 ft, MASTER LAUNDRY: 31.5 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 2 | 2 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 0 of 5:  | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY / SCULLERY: 8.7 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(garage 14.8) W(porch/patio 3.1, yard 9.6) ;; BUNK ROOM: N(yard 4.6) W(yard 4.6) ;; (unlabelled bed): N(yard 10.5) E(yard 3.2) ;; MASTER BEDROOM: N(porch/patio 18.4) E(porch/patio 23.4) W(porch/patio 4.7) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(porch/patio 18.4) S(porch/patio 1.7, yard 26.7) E(porch/patio 23.4, yard 11.2) W(porch/patio 4.7) | suite rooms: MASTER BEDROOM, (master entry), WIC @95.95,20.56, (closet passage), WIC @112,20.56, MASTER BATH, WC @99.7,16.71, (linen between the WCs), WC @99.7,9.31 |
| Living-kind rooms with S exposure | LIBRARY (19.0 ft); DEN (14.8 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 5: SUN ROOM (E/N); MASTER BEDROOM (E/N); DEN (E/S); DINING ROOM (S/W); LIBRARY (S/W) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 42.65..47.27, y 50.825; basement foot room x 42.65..47.27, y 28.725; **moved** (x offset +0.00/+0.00 ft, run 22.100 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 9.3 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_b.scad (defaults): 61 rooms, 72 doors, 25 windows - OK ; basement_b.scad (defaults): 21 rooms, 21 doors, 2 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |

## Section 1

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 5417.2 | computed: sum (x1-x0)*(y1-y0) over 47 rows, main_floor.scad:80-147 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 71.0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:98 |
| Main-floor conditioned excluding the stair opening | 5346.3 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 5417.2 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 3475.0 | computed over basement.scad:74-95 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 670.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:80 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| SIDE ENTRY | 83.7 | option-b-as-drawn-plus-kayla/main_floor_b.scad:81 |
| PATIO | 185.1 | option-b-as-drawn-plus-kayla/main_floor_b.scad:106 |
| FRONT PORCH | 796.1 | option-b-as-drawn-plus-kayla/main_floor_b.scad:137 |
| (unlabelled porch) @49.24,2 | 22.9 | option-b-as-drawn-plus-kayla/main_floor_b.scad:138 |
| (unlabelled porch) @95.95,2 | 39.9 | option-b-as-drawn-plus-kayla/main_floor_b.scad:139 |
| (covered entry) | 35.9 | option-b-as-drawn-plus-kayla/main_floor_b.scad:140 |
| DECK | 322.4 | option-b-as-drawn-plus-kayla/main_floor_b.scad:141 |
| OFFICE PORCH | 146.9 | option-b-as-drawn-plus-kayla/main_floor_b.scad:142 |
| MASTER PORCH | 175.1 | option-b-as-drawn-plus-kayla/main_floor_b.scad:143 |
| SIDE PORCH | 320.3 | option-b-as-drawn-plus-kayla/main_floor_b.scad:144 |
| (unlabelled porch) @128.13,26.84 | 25.4 | option-b-as-drawn-plus-kayla/main_floor_b.scad:145 |
| (study stoop) | 14.6 | option-b-as-drawn-plus-kayla/main_floor_b.scad:146 |
| (garage side-door pad) | 17.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:147 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 2185.9 sq ft. PATIO alone: 185.1; DECK alone: 322.4. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 390.1 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 139.0 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 219.4 ft | same |
|   facing garage | 31.7 ft | same (garage is unheated) |
| Outside (convex) corners | 17 | vertices of the union polygon after 0.02 ft simplify (30 vertices) |
| Inside (reflex) corners | 13 | same polygon |
| Bounding box, heated rooms | x 7.27..128.13 (120.86 ft), y 2..66.64 (64.64 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 0..137.66 (137.66 ft), y -13.26..66.64 (79.9 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 17 hip-roof blocks in main_roof (main_floor.scad:377); each hip block is 4 sloped facets, so 4 x 17 = 68 nominal facets before overlapping blocks merge; 10 blocks at 6/12 pitch, 7 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)

## Section 2

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| PANTRY / SCULLERY | S 11.3 (porch/patio (open)); W 8.7 (garage) | option-b-as-drawn-plus-kayla/main_floor_b.scad:82 |
| MUDROOM | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:83 |
| WIC @22.1,35.46 | S 2.2 (garage) | option-b-as-drawn-plus-kayla/main_floor_b.scad:84 |
| LAUNDRY | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:85 |
| BEDROOM 2 | S 14.8 (garage); W 3.1 (porch/patio (open)), 9.6 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:87 |
| (suite entry) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:88 |
| (suite entry, 2nd piece) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:89 |
| WC @7.27,48.13 | W 7.2 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:90 |
| BATH 2 | N 10.2 (yard/soil); W 6.7 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:91 |
| BUNK ROOM | N 4.6 (yard/soil); W 4.6 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:92 |
| (unlabelled bed) | N 10.5 (yard/soil); E 3.2 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:93 |
| STUDY | N 4.6 (porch/patio (open)), 5.4 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:94 |
| HALL @22.1,49.64 | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:96 |
| (N-S hall, unlabelled) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:97 |
| STAIR DN | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:98 |
| (landing at the stair top) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:99 |
| HALL @24.34,29.51 | W 6.0 (garage) | option-b-as-drawn-plus-kayla/main_floor_b.scad:100 |
| BATH | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:101 |
| BROOM / LINEN | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:102 |
| SUN ROOM | N 7.3 (yard/soil); E 12.7 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:104 |
| (unlabelled living) | N 4.6 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:105 |
| LIBRARY | S 5.4 (porch/patio (open)), 13.6 (yard/soil); W 4.6 (porch/patio (open)), 7.1 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:108 |
| BREAKFAST | W 2.8 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:109 |
| DINING ROOM | S 14.5 (porch/patio (open)); E 3.0 (porch/patio (open)); W 4.3 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:110 |
| (dining room, north end) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:111 |
| BUTLER | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:112 |
| VESTIBULE | S 12.0 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:113 |
| FOYER @69.14,10.5 | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:114 |
| FOYER @69.14,22 | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:115 |
| POWDER | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:116 |
| DEN | S 14.8 (porch/patio (open)); E 7.3 (porch/patio (open)); W 3.0 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:117 |
| MEDIA | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:118 |
| KITCHEN | N 14.5 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:120 |
| GREAT ROOM | N 26.5 (porch/patio (open)); E 4.4 (porch/patio (open)); W 1.8 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:121 |
| HALL @69.14,29.51 | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:122 |
| OFFICE | N 13.0 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:124 |
| MASTER BEDROOM | N 18.4 (porch/patio (open)); E 23.4 (porch/patio (open)); W 4.7 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:125 |
| (master entry) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:126 |
| WIC @95.95,20.56 | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:127 |
| (closet passage) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:128 |
| WIC @112,20.56 | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:129 |
| MASTER LAUNDRY | N 1.2 (porch/patio (open)); E 2.7 (porch/patio (open)), 6.3 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:130 |
| MASTER BATH | S 21.6 (yard/soil); E 11.2 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:131 |
| MECH | S 3.8 (porch/patio (open)) | option-b-as-drawn-plus-kayla/main_floor_b.scad:132 |
| WC @99.7,16.71 | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:133 |
| (linen between the WCs) | none | option-b-as-drawn-plus-kayla/main_floor_b.scad:134 |
| WC @99.7,9.31 | S 1.7 (porch/patio (open)), 5.1 (yard/soil) | option-b-as-drawn-plus-kayla/main_floor_b.scad:135 |

## Section 3

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PANTRY / SCULLERY | 24.34 | 20.82 | 35.6 | 29.51 | 11.26 x 8.69 | 10.9 x 8.3 | 98 | 90 | 1.30 | utility | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:82 |
| MUDROOM | 28 | 35.46 | 37.3 | 40.56 | 9.30 x 5.10 | 8.9 x 4.7 | 47 | 42 | 1.82 | utility | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:83 |
| WIC @22.1,35.46 | 22.1 | 35.46 | 28 | 40.56 | 5.90 x 5.10 | 5.5 x 4.7 | 30 | 26 | 1.16 | closet | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:84 |
| LAUNDRY | 22.1 | 40.56 | 37.3 | 49.64 | 15.20 x 9.08 | 14.8 x 8.7 | 138 | 128 | 1.67 | utility | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:85 |
| BEDROOM 2 | 7.27 | 35.46 | 22.1 | 48.13 | 14.83 x 12.67 | 14.4 x 12.3 | 188 | 177 | 1.17 | bed | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:87 |
| (suite entry) | 13.78 | 48.13 | 22.1 | 53.75 | 8.32 x 5.62 | 7.9 x 5.2 | 47 | 41 | 1.48 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:88 |
| (suite entry, 2nd piece) | 13.78 | 53.75 | 17.5 | 55.3 | 3.72 x 1.55 | 3.3 x 1.1 | 6 | 4 | 2.40 | hall | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:89 |
| WC @7.27,48.13 | 7.27 | 48.13 | 13.78 | 55.3 | 6.51 x 7.17 | 6.1 x 6.8 | 47 | 41 | 1.10 | bath | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:90 |
| BATH 2 | 7.27 | 55.3 | 17.5 | 62.04 | 10.23 x 6.74 | 9.8 x 6.3 | 69 | 62 | 1.52 | bath | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:91 |
| BUNK ROOM | 17.5 | 53.75 | 22.1 | 66.64 | 4.60 x 12.89 | 4.2 x 12.5 | 59 | 52 | 2.80 | bed | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:92 |
| (unlabelled bed) | 22.1 | 55.6 | 32.6 | 66.64 | 10.50 x 11.04 | 10.1 x 10.6 | 116 | 107 | 1.05 | bed | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:93 |
| STUDY | 32.6 | 55.6 | 42.65 | 63.42 | 10.05 x 7.82 | 9.6 x 7.4 | 79 | 72 | 1.29 | office | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:94 |
| HALL @22.1,49.64 | 22.1 | 49.64 | 42.65 | 55.6 | 20.55 x 5.96 | 20.1 x 5.6 | 122 | 112 | 3.45 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:96 |
| (N-S hall, unlabelled) | 37.3 | 35.46 | 42.65 | 49.64 | 5.35 x 14.18 | 5.0 x 13.8 | 76 | 68 | 2.65 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:97 |
| STAIR DN | 42.65 | 35.46 | 47.27 | 50.825 | 4.62 x 15.37 | 4.2 x 15.0 | 71 | - | 3.33 | stairwell | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:98 |
| (landing at the stair top) | 42.65 | 50.825 | 47.27 | 55.6 | 4.62 x 4.77 | 4.2 x 4.4 | 22 | 18 | 1.03 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:99 |
| HALL @24.34,29.51 | 24.34 | 29.51 | 54.6 | 35.46 | 30.26 x 5.95 | 29.9 x 5.5 | 180 | 166 | 5.09 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:100 |
| BATH | 47.27 | 35.46 | 54.6 | 45.39 | 7.33 x 9.93 | 6.9 x 9.5 | 73 | 66 | 1.35 | bath | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:101 |
| BROOM / LINEN | 47.27 | 45.39 | 54.6 | 50.69 | 7.33 x 5.30 | 6.9 x 4.9 | 39 | 34 | 1.38 | closet | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:102 |
| SUN ROOM | 47.27 | 50.69 | 54.6 | 63.42 | 7.33 x 12.73 | 6.9 x 12.3 | 93 | 85 | 1.74 | living | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:104 |
| (unlabelled living) | 42.65 | 55.6 | 47.27 | 63.42 | 4.62 x 7.82 | 4.2 x 7.4 | 36 | 31 | 1.69 | living | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:105 |
| LIBRARY | 35.6 | 6.28 | 54.6 | 18 | 19.00 x 11.72 | 18.6 x 11.3 | 223 | 211 | 1.62 | living | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:108 |
| BREAKFAST | 35.6 | 18 | 54.6 | 29.51 | 19.00 x 11.51 | 18.6 x 11.1 | 219 | 207 | 1.65 | dining | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:109 |
| DINING ROOM | 54.6 | 2 | 69.14 | 22 | 14.54 x 20.00 | 14.1 x 19.6 | 291 | 277 | 1.38 | dining | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:110 |
| (dining room, north end) | 60.5 | 22 | 69.14 | 29.51 | 8.64 x 7.51 | 8.2 x 7.1 | 65 | 59 | 1.15 | dining | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:111 |
| BUTLER | 54.6 | 22 | 60.5 | 29.51 | 5.90 x 7.51 | 5.5 x 7.1 | 44 | 39 | 1.27 | utility | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:112 |
| VESTIBULE | 69.14 | 5 | 81.12 | 10.5 | 11.98 x 5.50 | 11.6 x 5.1 | 66 | 59 | 2.18 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:113 |
| FOYER @69.14,10.5 | 69.14 | 10.5 | 81.12 | 22 | 11.98 x 11.50 | 11.6 x 11.1 | 138 | 129 | 1.04 | hall | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:114 |
| FOYER @69.14,22 | 69.14 | 22 | 76 | 29.51 | 6.86 x 7.51 | 6.5 x 7.1 | 52 | 46 | 1.09 | hall | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:115 |
| POWDER | 76 | 22 | 81.12 | 29.51 | 5.12 x 7.51 | 4.7 x 7.1 | 38 | 34 | 1.47 | bath | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:116 |
| DEN | 81.12 | 2 | 95.95 | 17.5 | 14.83 x 15.50 | 14.4 x 15.1 | 230 | 218 | 1.05 | living | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:117 |
| MEDIA | 81.12 | 17.5 | 95.95 | 29.51 | 14.83 x 12.01 | 14.4 x 11.6 | 178 | 168 | 1.23 | living | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:118 |
| KITCHEN | 54.6 | 29.51 | 69.14 | 50.69 | 14.54 x 21.18 | 14.1 x 20.8 | 308 | 294 | 1.46 | kitchen | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:120 |
| GREAT ROOM | 69.14 | 35.46 | 95.63 | 52.53 | 26.49 x 17.07 | 26.1 x 16.7 | 452 | 435 | 1.55 | living | 12 | option-b-as-drawn-plus-kayla/main_floor_b.scad:121 |
| HALL @69.14,29.51 | 69.14 | 29.51 | 105.2 | 35.46 | 36.06 x 5.95 | 35.7 x 5.5 | 215 | 198 | 6.06 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:122 |
| OFFICE | 95.63 | 35.46 | 108.62 | 48.16 | 12.99 x 12.70 | 12.6 x 12.3 | 165 | 155 | 1.02 | office | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:124 |
| MASTER BEDROOM | 108.62 | 29.51 | 126.97 | 52.86 | 18.35 x 23.35 | 17.9 x 22.9 | 428 | 412 | 1.27 | bed | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:125 |
| (master entry) | 105.2 | 29.51 | 108.62 | 35.46 | 3.42 x 5.95 | 3.0 x 5.5 | 20 | 17 | 1.74 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:126 |
| WIC @95.95,20.56 | 95.95 | 20.56 | 106.51 | 29.51 | 10.56 x 8.95 | 10.2 x 8.6 | 95 | 87 | 1.18 | closet | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:127 |
| (closet passage) | 106.51 | 20.56 | 112 | 29.51 | 5.49 x 8.95 | 5.1 x 8.6 | 49 | 44 | 1.63 | hall | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:128 |
| WIC @112,20.56 | 112 | 20.56 | 121.94 | 29.51 | 9.94 x 8.95 | 9.5 x 8.6 | 89 | 82 | 1.11 | closet | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:129 |
| MASTER LAUNDRY | 121.94 | 20.56 | 128.13 | 29.51 | 6.19 x 8.95 | 5.8 x 8.6 | 55 | 50 | 1.45 | utility | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:130 |
| MASTER BATH | 106.51 | 9.31 | 128.13 | 20.56 | 21.62 x 11.25 | 21.2 x 10.8 | 243 | 230 | 1.92 | bath | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:131 |
| MECH | 95.95 | 9.31 | 99.7 | 20.56 | 3.75 x 11.25 | 3.4 x 10.8 | 42 | 36 | 3.00 | utility | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:132 |
| WC @99.7,16.71 | 99.7 | 16.71 | 106.51 | 20.56 | 6.81 x 3.85 | 6.4 x 3.4 | 26 | 22 | 1.77 | bath | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:133 |
| (linen between the WCs) | 99.7 | 13.09 | 106.51 | 16.71 | 6.81 x 3.62 | 6.4 x 3.2 | 25 | 21 | 1.88 | closet | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:134 |
| WC @99.7,9.31 | 99.7 | 9.31 | 106.51 | 13.09 | 6.81 x 3.78 | 6.4 x 3.4 | 26 | 22 | 1.80 | bath | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:135 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 0 | 7.9 | 24.34 | 35.46 | 24.34 x 27.56 | 23.9 x 27.2 | 671 | 650 | 1.13 | garage | 10 | option-b-as-drawn-plus-kayla/main_floor_b.scad:80 |
| SIDE ENTRY | 24.34 | 13.39 | 35.6 | 20.82 | 11.26 x 7.43 | 11.3 x 7.4 (open) | 84 | - | 1.52 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:81 |
| PATIO | 54.6 | 50.69 | 69.14 | 63.42 | 14.54 x 12.73 | 14.5 x 12.7 (open) | 185 | - | 1.14 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:106 |
| FRONT PORCH | 49.24 | -13.26 | 101.41 | 2 | 52.17 x 15.26 | 52.2 x 15.3 (open) | 796 | - | 3.42 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:137 |
| (unlabelled porch) @49.24,2 | 49.24 | 2 | 54.6 | 6.28 | 5.36 x 4.28 | 5.4 x 4.3 (open) | 23 | - | 1.25 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:138 |
| (unlabelled porch) @95.95,2 | 95.95 | 2 | 101.41 | 9.31 | 5.46 x 7.31 | 5.5 x 7.3 (open) | 40 | - | 1.34 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:139 |
| (covered entry) | 69.14 | 2 | 81.12 | 5 | 11.98 x 3.00 | 12.0 x 3.0 (open) | 36 | - | 3.99 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:140 |
| DECK | 69.14 | 52.53 | 95.63 | 64.7 | 26.49 x 12.17 | 26.5 x 12.2 (open) | 322 | - | 2.18 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:141 |
| OFFICE PORCH | 95.63 | 48.16 | 108.62 | 59.47 | 12.99 x 11.31 | 13.0 x 11.3 (open) | 147 | - | 1.15 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:142 |
| MASTER PORCH | 108.62 | 52.86 | 126.97 | 62.4 | 18.35 x 9.54 | 18.3 x 9.5 (open) | 175 | - | 1.92 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:143 |
| SIDE PORCH | 126.97 | 29.51 | 137.66 | 59.47 | 10.69 x 29.96 | 10.7 x 30.0 (open) | 320 | - | 2.80 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:144 |
| (unlabelled porch) @128.13,26.84 | 128.13 | 26.84 | 137.66 | 29.51 | 9.53 x 2.67 | 9.5 x 2.7 (open) | 25 | - | 3.57 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:145 |
| (study stoop) | 36.6 | 63.42 | 41.2 | 66.6 | 4.60 x 3.18 | 4.6 x 3.2 (open) | 15 | - | 1.45 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:146 |
| (garage side-door pad) | 1.7 | 35.46 | 7.27 | 38.6 | 5.57 x 3.14 | 5.6 x 3.1 (open) | 17 | - | 1.77 | porch | 0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:147 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MUSIC ROOM | 22.16 | 50.35 | 42.65 | 63.16 | 20.49 x 12.81 | 19.7 x 12.1 | 262 | 238 | 1.60 | living | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:74 |
| GYM | 42.65 | 50.825 | 54.14 | 63.16 | 11.49 x 12.33 | 10.7 x 11.6 | 142 | 124 | 1.07 | rec | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:75 |
| (unlabelled rec) | 47.27 | 45.34 | 54.14 | 50.825 | 6.87 x 5.48 | 6.1 x 5.1 | 38 | 31 | 1.25 | rec | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:76 |
| STORAGE | 22.16 | 42.77 | 37.37 | 50.35 | 15.21 x 7.58 | 14.5 x 7.2 | 115 | 104 | 2.01 | closet | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:77 |
| UTILITY | 22.16 | 35.08 | 37.37 | 42.77 | 15.21 x 7.69 | 14.5 x 6.9 | 117 | 100 | 1.98 | utility | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:78 |
| HALL @37.37,35.08 | 37.37 | 35.08 | 42.65 | 50.35 | 5.28 x 15.27 | 4.9 x 14.9 | 81 | 73 | 2.89 | hall | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:79 |
| STAIR UP | 42.65 | 28.725 | 47.27 | 50.825 | 4.62 x 22.10 | 4.2 x 21.7 | 102 | 92 | 4.78 | stair | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:80 |
| BATH @47.27,35.08 | 47.27 | 35.08 | 54.14 | 45.34 | 6.87 x 10.26 | 6.5 x 9.9 | 70 | 64 | 1.49 | bath | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:81 |
| HALLWAY | 35.27 | 27.6 | 54.14 | 28.725 | 18.87 x 1.12 | 18.1 x 0.7 | 21 | 13 | 16.77 | hall | 0 | option-b-as-drawn-plus-kayla/basement_b.scad:82 |
| (unlabelled hall) @35.27,28.725 | 35.27 | 28.725 | 42.65 | 35.08 | 7.38 x 6.35 | 6.6 x 6.0 | 47 | 39 | 1.16 | hall | 0 | option-b-as-drawn-plus-kayla/basement_b.scad:83 |
| (unlabelled hall) @47.27,28.725 | 47.27 | 28.725 | 54.14 | 35.08 | 6.87 x 6.35 | 6.5 x 6.0 | 44 | 39 | 1.08 | hall | 0 | option-b-as-drawn-plus-kayla/basement_b.scad:84 |
| LIVING ROOM | 35.27 | 5.79 | 54.14 | 27.6 | 18.87 x 21.81 | 18.1 x 21.1 | 412 | 382 | 1.16 | living | 10 | option-b-as-drawn-plus-kayla/basement_b.scad:85 |
| HOME THEATER | 54.14 | 29.12 | 69.38 | 50.35 | 15.24 x 21.23 | 14.8 x 20.5 | 324 | 304 | 1.39 | tiered | 13.25 | option-b-as-drawn-plus-kayla/basement_b.scad:86 |
| PET ROOM | 54.14 | 18.15 | 69.38 | 29.12 | 15.24 x 10.97 | 14.8 x 10.6 | 167 | 157 | 1.39 | utility | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:87 |
| POOL ROOM | 69.38 | 18.15 | 96.33 | 52.76 | 26.95 x 34.61 | 25.8 x 33.9 | 933 | 875 | 1.28 | pit | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:88 |
| POOL EQUIP. | 96.33 | 29.12 | 103.04 | 41.94 | 6.71 x 12.82 | 6.0 x 12.1 | 86 | 72 | 1.91 | utility | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:89 |
| POOL BATH | 96.33 | 18.15 | 103.04 | 29.12 | 6.71 x 10.97 | 6.0 x 10.6 | 74 | 63 | 1.63 | bath | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:90 |
| HALL @54.14,13.43 | 54.14 | 13.43 | 103.04 | 18.15 | 48.90 x 4.72 | 48.1 x 4.0 | 231 | 191 | 10.36 | hall | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:91 |
| BATH @54.14,5.79 | 54.14 | 5.79 | 67.4 | 13.43 | 13.26 x 7.64 | 12.9 x 6.9 | 101 | 89 | 1.74 | bath | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:92 |
| LAUNDRY | 67.4 | 5.79 | 81.68 | 13.43 | 14.28 x 7.64 | 13.5 x 6.9 | 109 | 93 | 1.87 | utility | 12 | option-b-as-drawn-plus-kayla/basement_b.scad:93 |
| EXIT STAIR | 45.6 | 63.16 | 66.8 | 67.75 | 21.20 x 4.59 | 20.1 x 3.5 | 97 | - | 4.62 | stairwell | 0 | option-b-as-drawn-plus-kayla/basement_b.scad:95 |

## Section 4

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (72, 5) x | 6.2 ft = 74.4 in | double | 1 | (covered entry) / VESTIBULE | option-b-as-drawn-plus-kayla/main_floor_b.scad:153 |
| M2 | (69.6, 5) x | 2 ft = 24 in | glass | - | (covered entry) / VESTIBULE | option-b-as-drawn-plus-kayla/main_floor_b.scad:154 |
| M3 | (78.6, 5) x | 2 ft = 24 in | glass | - | (covered entry) / VESTIBULE | option-b-as-drawn-plus-kayla/main_floor_b.scad:155 |
| M4 | (58.5, 2) x | 6 ft = 72 in | double | 1 | FRONT PORCH / DINING ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:156 |
| M5 | (37, 63.42) x | 3.75 ft = 45 in | double | 1 | STUDY / (study stoop) | option-b-as-drawn-plus-kayla/main_floor_b.scad:157 |
| M6 | (99, 48.16) x | 6.5 ft = 78 in | double | 1 | OFFICE / OFFICE PORCH | option-b-as-drawn-plus-kayla/main_floor_b.scad:158 |
| M7 | (114.1, 52.86) x | 6.05 ft = 72.6 in | double | 1 | MASTER BEDROOM / MASTER PORCH | option-b-as-drawn-plus-kayla/main_floor_b.scad:159 |
| M8 | (2, 7.9) x | 9 ft = 108 in | garage | - | OUTSIDE / GARAGE | option-b-as-drawn-plus-kayla/main_floor_b.scad:160 |
| M9 | (12.5, 7.9) x | 9 ft = 108 in | garage | - | OUTSIDE / GARAGE | option-b-as-drawn-plus-kayla/main_floor_b.scad:161 |
| M10 | (2.43, 35.46) x | 3 ft = 36 in | door | 1 | GARAGE / (garage side-door pad) | option-b-as-drawn-plus-kayla/main_floor_b.scad:162 |
| M11 | (24.34, 16.1) y | 3 ft = 36 in | door | -1 | GARAGE / SIDE ENTRY | option-b-as-drawn-plus-kayla/main_floor_b.scad:163 |
| M12 | (24.34, 22.3) y | 3 ft = 36 in | door | 1 | GARAGE / PANTRY / SCULLERY | option-b-as-drawn-plus-kayla/main_floor_b.scad:165 |
| M13 | (28.5, 20.82) x | 3 ft = 36 in | door | -1 | SIDE ENTRY / PANTRY / SCULLERY | option-b-as-drawn-plus-kayla/main_floor_b.scad:166 |
| M14 | (30.5, 29.51) x | 3 ft = 36 in | door | 1 | PANTRY / SCULLERY / HALL @24.34,29.51 | option-b-as-drawn-plus-kayla/main_floor_b.scad:167 |
| M15 | (35.6, 22.3) y | 3 ft = 36 in | door | 1 | PANTRY / SCULLERY / BREAKFAST | option-b-as-drawn-plus-kayla/main_floor_b.scad:168 |
| M16 | (24.34, 31.9) y | 3 ft = 36 in | door | 1 | GARAGE / HALL @24.34,29.51 | option-b-as-drawn-plus-kayla/main_floor_b.scad:169 |
| M17 | (28.2, 35.46) x | 8.8 ft = 105.6 in | full | - | HALL @24.34,29.51 / MUDROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:170 |
| M18 | (31, 40.56) x | 3 ft = 36 in | door | -1 | MUDROOM / LAUNDRY | option-b-as-drawn-plus-kayla/main_floor_b.scad:171 |
| M19 | (25, 49.64) x | 3 ft = 36 in | door | -1 | LAUNDRY / HALL @22.1,49.64 | option-b-as-drawn-plus-kayla/main_floor_b.scad:172 |
| M20 | (22.1, 36.6) y | 3 ft = 36 in | door | -1 | BEDROOM 2 / WIC @22.1,35.46 | option-b-as-drawn-plus-kayla/main_floor_b.scad:173 |
| M21 | (22.1, 50) y | 3 ft = 36 in | door | -1 | (suite entry) / HALL @22.1,49.64 | option-b-as-drawn-plus-kayla/main_floor_b.scad:175 |
| M22 | (14, 48.13) x | 7.9 ft = 94.8 in | full | - | BEDROOM 2 / (suite entry) | option-b-as-drawn-plus-kayla/main_floor_b.scad:176 |
| M23 | (13.9, 53.75) x | 3.5 ft = 42 in | full | - | (suite entry) / (suite entry, 2nd piece) | option-b-as-drawn-plus-kayla/main_floor_b.scad:177 |
| M24 | (14.2, 55.3) x | 3 ft = 36 in | door | 1 | (suite entry, 2nd piece) / BATH 2 | option-b-as-drawn-plus-kayla/main_floor_b.scad:178 |
| M25 | (8, 55.3) x | 3 ft = 36 in | door | -1 | WC @7.27,48.13 / BATH 2 | option-b-as-drawn-plus-kayla/main_floor_b.scad:179 |
| M26 | (8, 48.13) x | 3 ft = 36 in | door | -1 | BEDROOM 2 / WC @7.27,48.13 | option-b-as-drawn-plus-kayla/main_floor_b.scad:180 |
| M27 | (17.5, 56.8) y | 3 ft = 36 in | door | 1 | BATH 2 / BUNK ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:181 |
| M28 | (22.1, 57.2) y | 6 ft = 72 in | full | - | BUNK ROOM / (unlabelled bed) | option-b-as-drawn-plus-kayla/main_floor_b.scad:182 |
| M29 | (29.4, 55.6) x | 3 ft = 36 in | door | 1 | HALL @22.1,49.64 / (unlabelled bed) | option-b-as-drawn-plus-kayla/main_floor_b.scad:183 |
| M30 | (33, 55.6) x | 3 ft = 36 in | door | 1 | HALL @22.1,49.64 / STUDY | option-b-as-drawn-plus-kayla/main_floor_b.scad:184 |
| M31 | (37.5, 49.64) x | 5 ft = 60 in | full | - | (N-S hall, unlabelled) / HALL @22.1,49.64 | option-b-as-drawn-plus-kayla/main_floor_b.scad:185 |
| M32 | (37.6, 35.46) x | 4.8 ft = 57.6 in | full | - | HALL @24.34,29.51 / (N-S hall, unlabelled) | option-b-as-drawn-plus-kayla/main_floor_b.scad:186 |
| M33 | (42.9, 50.825) x | 4.1 ft = 49.2 in | full | - | STAIR DN / (landing at the stair top) | option-b-as-drawn-plus-kayla/main_floor_b.scad:188 |
| M34 | (42.65, 51.2) y | 4 ft = 48 in | full | - | HALL @22.1,49.64 / (landing at the stair top) | option-b-as-drawn-plus-kayla/main_floor_b.scad:189 |
| M35 | (47.27, 51.2) y | 4 ft = 48 in | double | 1 | (landing at the stair top) / SUN ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:190 |
| M36 | (47.27, 56.2) y | 5.5 ft = 66 in | full | - | (unlabelled living) / SUN ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:191 |
| M37 | (54.6, 53.9) y | 4.9 ft = 58.8 in | double | 1 | SUN ROOM / PATIO | option-b-as-drawn-plus-kayla/main_floor_b.scad:192 |
| M38 | (48.4, 50.69) x | 3 ft = 36 in | door | -1 | BROOM / LINEN / SUN ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:193 |
| M39 | (48.4, 35.46) x | 3 ft = 36 in | door | 1 | HALL @24.34,29.51 / BATH | option-b-as-drawn-plus-kayla/main_floor_b.scad:194 |
| M40 | (54.6, 29.8) y | 5.4 ft = 64.8 in | full | - | HALL @24.34,29.51 / KITCHEN | option-b-as-drawn-plus-kayla/main_floor_b.scad:196 |
| M41 | (55.4, 29.51) x | 4 ft = 48 in | full | - | BUTLER / KITCHEN | option-b-as-drawn-plus-kayla/main_floor_b.scad:197 |
| M42 | (61, 29.51) x | 6 ft = 72 in | full | - | (dining room, north end) / KITCHEN | option-b-as-drawn-plus-kayla/main_floor_b.scad:198 |
| M43 | (55.4, 22) x | 4 ft = 48 in | full | - | DINING ROOM / BUTLER | option-b-as-drawn-plus-kayla/main_floor_b.scad:199 |
| M44 | (54.6, 23.5) y | 5 ft = 60 in | full | - | BREAKFAST / BUTLER | option-b-as-drawn-plus-kayla/main_floor_b.scad:200 |
| M45 | (69.14, 24) y | 3 ft = 36 in | door | -1 | (dining room, north end) / FOYER @69.14,22 | option-b-as-drawn-plus-kayla/main_floor_b.scad:201 |
| M46 | (54.6, 8) y | 5 ft = 60 in | double | 1 | LIBRARY / DINING ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:202 |
| M47 | (38.5, 18) x | 6 ft = 72 in | full | - | LIBRARY / BREAKFAST | option-b-as-drawn-plus-kayla/main_floor_b.scad:203 |
| M48 | (64, 50.69) x | 4.6 ft = 55.2 in | double | -1 | KITCHEN / PATIO | option-b-as-drawn-plus-kayla/main_floor_b.scad:204 |
| M49 | (69.14, 38) y | 6 ft = 72 in | full | - | KITCHEN / GREAT ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:205 |
| M50 | (69.14, 29.8) y | 5.4 ft = 64.8 in | full | - | KITCHEN / HALL @69.14,29.51 | option-b-as-drawn-plus-kayla/main_floor_b.scad:206 |
| M51 | (71, 10.5) x | 5 ft = 60 in | double | 1 | VESTIBULE / FOYER @69.14,10.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:207 |
| M52 | (69.4, 22) x | 6.5 ft = 78 in | full | - | FOYER @69.14,10.5 / FOYER @69.14,22 | option-b-as-drawn-plus-kayla/main_floor_b.scad:208 |
| M53 | (77.4, 22) x | 3 ft = 36 in | door | -1 | FOYER @69.14,10.5 / POWDER | option-b-as-drawn-plus-kayla/main_floor_b.scad:209 |
| M54 | (69.4, 29.51) x | 6.5 ft = 78 in | full | - | FOYER @69.14,22 / HALL @69.14,29.51 | option-b-as-drawn-plus-kayla/main_floor_b.scad:210 |
| M55 | (69.4, 35.46) x | 26 ft = 312 in | full | - | HALL @69.14,29.51 / GREAT ROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:211 |
| M56 | (81.12, 11.8) y | 5 ft = 60 in | double | 1 | FOYER @69.14,10.5 / DEN | option-b-as-drawn-plus-kayla/main_floor_b.scad:212 |
| M57 | (84, 17.5) x | 8 ft = 96 in | full | - | DEN / MEDIA | option-b-as-drawn-plus-kayla/main_floor_b.scad:213 |
| M58 | (83, 29.51) x | 8 ft = 96 in | full | - | MEDIA / HALL @69.14,29.51 | option-b-as-drawn-plus-kayla/main_floor_b.scad:214 |
| M59 | (70.65, 52.53) x | 6 ft = 72 in | double | -1 | GREAT ROOM / DECK | option-b-as-drawn-plus-kayla/main_floor_b.scad:215 |
| M60 | (99.3, 35.46) x | 4.7 ft = 56.4 in | double | 1 | HALL @69.14,29.51 / OFFICE | option-b-as-drawn-plus-kayla/main_floor_b.scad:217 |
| M61 | (105.2, 29.95) y | 4.6 ft = 55.2 in | double | 1 | HALL @69.14,29.51 / (master entry) | option-b-as-drawn-plus-kayla/main_floor_b.scad:218 |
| M62 | (108.62, 29.8) y | 5.4 ft = 64.8 in | full | - | (master entry) / MASTER BEDROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:219 |
| M63 | (108.9, 29.51) x | 3 ft = 36 in | open | - | (closet passage) / MASTER BEDROOM | option-b-as-drawn-plus-kayla/main_floor_b.scad:220 |
| M64 | (106.51, 23.6) y | 3 ft = 36 in | door | -1 | WIC @95.95,20.56 / (closet passage) | option-b-as-drawn-plus-kayla/main_floor_b.scad:221 |
| M65 | (112, 23.6) y | 3 ft = 36 in | door | 1 | (closet passage) / WIC @112,20.56 | option-b-as-drawn-plus-kayla/main_floor_b.scad:222 |
| M66 | (107.1, 20.56) x | 3 ft = 36 in | door | -1 | MASTER BATH / (closet passage) | option-b-as-drawn-plus-kayla/main_floor_b.scad:223 |
| M67 | (122.6, 20.56) x | 3 ft = 36 in | door | 1 | MASTER BATH / MASTER LAUNDRY | option-b-as-drawn-plus-kayla/main_floor_b.scad:224 |
| M68 | (121.94, 23.6) y | 3 ft = 36 in | door | -1 | WIC @112,20.56 / MASTER LAUNDRY | option-b-as-drawn-plus-kayla/main_floor_b.scad:225 |
| M69 | (106.51, 17) y | 3 ft = 36 in | door | -1 | WC @99.7,16.71 / MASTER BATH | option-b-as-drawn-plus-kayla/main_floor_b.scad:226 |
| M70 | (106.51, 13.4) y | 3 ft = 36 in | door | -1 | (linen between the WCs) / MASTER BATH | option-b-as-drawn-plus-kayla/main_floor_b.scad:227 |
| M71 | (106.51, 9.8) y | 3 ft = 36 in | door | -1 | WC @99.7,9.31 / MASTER BATH | option-b-as-drawn-plus-kayla/main_floor_b.scad:228 |
| M72 | (95.95, 12) y | 3 ft = 36 in | door | -1 | DEN / MECH | option-b-as-drawn-plus-kayla/main_floor_b.scad:229 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (38.4, 50.35) x | 2.8 ft = 33.6 in | door | 1 | HALL @37.37,35.08 / MUSIC ROOM | option-b-as-drawn-plus-kayla/basement_b.scad:100 |
| B2 | (42.65, 52) y | 3 ft = 36 in | door | 1 | MUSIC ROOM / GYM | option-b-as-drawn-plus-kayla/basement_b.scad:101 |
| B3 | (47.5, 50.825) x | 6.4 ft = 76.8 in | full | - | (unlabelled rec) / GYM | option-b-as-drawn-plus-kayla/basement_b.scad:102 |
| B4 | (37.37, 45.6) y | 2.8 ft = 33.6 in | door | -1 | STORAGE / HALL @37.37,35.08 | option-b-as-drawn-plus-kayla/basement_b.scad:103 |
| B5 | (37.37, 38.4) y | 3 ft = 36 in | door | -1 | UTILITY / HALL @37.37,35.08 | option-b-as-drawn-plus-kayla/basement_b.scad:104 |
| B6 | (37.6, 35.08) x | 4.8 ft = 57.6 in | full | - | (unlabelled hall) @35.27,28.725 / HALL @37.37,35.08 | option-b-as-drawn-plus-kayla/basement_b.scad:105 |
| B7 | (42.9, 28.725) x | 4.1 ft = 49.2 in | full | - | HALLWAY / STAIR UP | option-b-as-drawn-plus-kayla/basement_b.scad:106 |
| B8 | (35.5, 28.725) x | 6.9 ft = 82.8 in | full | - | HALLWAY / (unlabelled hall) @35.27,28.725 | option-b-as-drawn-plus-kayla/basement_b.scad:107 |
| B9 | (47.5, 28.725) x | 6.4 ft = 76.8 in | full | - | HALLWAY / (unlabelled hall) @47.27,28.725 | option-b-as-drawn-plus-kayla/basement_b.scad:108 |
| B10 | (49.2, 35.08) x | 2.8 ft = 33.6 in | door | 1 | (unlabelled hall) @47.27,28.725 / BATH @47.27,35.08 | option-b-as-drawn-plus-kayla/basement_b.scad:109 |
| B11 | (54.14, 31.7) y | 3 ft = 36 in | door | -1 | (unlabelled hall) @47.27,28.725 / HOME THEATER | option-b-as-drawn-plus-kayla/basement_b.scad:110 |
| B12 | (40, 27.6) x | 8 ft = 96 in | open | - | LIVING ROOM / HALLWAY | option-b-as-drawn-plus-kayla/basement_b.scad:111 |
| B13 | (54.14, 13.8) y | 4 ft = 48 in | open | - | LIVING ROOM / HALL @54.14,13.43 | option-b-as-drawn-plus-kayla/basement_b.scad:112 |
| B14 | (56.5, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / PET ROOM | option-b-as-drawn-plus-kayla/basement_b.scad:113 |
| B15 | (71, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / POOL ROOM | option-b-as-drawn-plus-kayla/basement_b.scad:114 |
| B16 | (96.33, 20.5) y | 2.8 ft = 33.6 in | door | 1 | POOL ROOM / POOL BATH | option-b-as-drawn-plus-kayla/basement_b.scad:115 |
| B17 | (99, 18.15) x | 2.8 ft = 33.6 in | door | 1 | HALL @54.14,13.43 / POOL BATH | option-b-as-drawn-plus-kayla/basement_b.scad:116 |
| B18 | (96.33, 33.5) y | 3 ft = 36 in | door | 1 | POOL ROOM / POOL EQUIP. | option-b-as-drawn-plus-kayla/basement_b.scad:117 |
| B19 | (59, 13.43) x | 2.8 ft = 33.6 in | door | -1 | BATH @54.14,5.79 / HALL @54.14,13.43 | option-b-as-drawn-plus-kayla/basement_b.scad:118 |
| B20 | (73, 13.43) x | 3 ft = 36 in | door | -1 | LAUNDRY / HALL @54.14,13.43 | option-b-as-drawn-plus-kayla/basement_b.scad:119 |
| B21 | (46.2, 63.16) x | 3.5 ft = 42 in | door | -1 | GYM / EXIT STAIR | option-b-as-drawn-plus-kayla/basement_b.scad:120 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 30 | 30 |
| double | 0 | 0 | 14 | 14 |
| open | 0 | 0 | 1 | 1 |
| full | 0 | 0 | 23 | 23 |
| glass | 2 | 0 | 0 | 2 |
| garage | 0 | 0 | 2 | 2 |
| ALL | 2 | 0 | 70 | 72 |
| passage (door+double+slider+open) | 0 | 0 | 45 | 45 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 6 | 8 | 14 |
| open | 0 | 0 | 2 | 2 |
| full | 0 | 0 | 5 | 5 |
| ALL | 0 | 6 | 15 | 21 |
| passage (door+double+slider+open) | 0 | 6 | 10 | 16 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-b-as-drawn-plus-kayla/main_floor_b.scad:159 | MASTER BEDROOM / MASTER PORCH | double | 72.6 in | - |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:173 | BEDROOM 2 / WIC @22.1,35.46 | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:176 | BEDROOM 2 / (suite entry) | full | 94.8 in | - |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:178 | (suite entry, 2nd piece) / BATH 2 | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:179 | WC @7.27,48.13 / BATH 2 | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:180 | BEDROOM 2 / WC @7.27,48.13 | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:181 | BATH 2 / BUNK ROOM | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:182 | BUNK ROOM / (unlabelled bed) | full | 72 in | - |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:183 | HALL @22.1,49.64 / (unlabelled bed) | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:193 | BROOM / LINEN / SUN ROOM | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:194 | HALL @24.34,29.51 / BATH | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:209 | FOYER @69.14,10.5 / POWDER | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:219 | (master entry) / MASTER BEDROOM | full | 64.8 in | - |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:220 | (closet passage) / MASTER BEDROOM | open | 36 in | - |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:221 | WIC @95.95,20.56 / (closet passage) | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:222 | (closet passage) / WIC @112,20.56 | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:223 | MASTER BATH / (closet passage) | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:224 | MASTER BATH / MASTER LAUNDRY | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:225 | WIC @112,20.56 / MASTER LAUNDRY | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:226 | WC @99.7,16.71 / MASTER BATH | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:227 | (linen between the WCs) / MASTER BATH | door | 36 in | 34.5 |
| option-b-as-drawn-plus-kayla/main_floor_b.scad:228 | WC @99.7,9.31 / MASTER BATH | door | 36 in | 34.5 |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-b-as-drawn-plus-kayla/basement_b.scad:103 | STORAGE / HALL @37.37,35.08 | door | 33.6 in | 32.1 |
| option-b-as-drawn-plus-kayla/basement_b.scad:109 | (unlabelled hall) @47.27,28.725 / BATH @47.27,35.08 | door | 33.6 in | 32.1 |
| option-b-as-drawn-plus-kayla/basement_b.scad:115 | POOL ROOM / POOL BATH | door | 33.6 in | 32.1 |
| option-b-as-drawn-plus-kayla/basement_b.scad:116 | HALL @54.14,13.43 / POOL BATH | door | 33.6 in | 32.1 |
| option-b-as-drawn-plus-kayla/basement_b.scad:118 | BATH @54.14,5.79 / HALL @54.14,13.43 | door | 33.6 in | 32.1 |

## Section 5

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| STUDY | N | (33, 63.42, 'x') | 3 | 2.5 | 5 | 15.0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:234 |
| OFFICE | N | (96.4, 48.16, 'x') | 2.6 | 2.5 | 5 | 13.0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:235 |
| BUNK ROOM | W | (17.5, 63, 'y') | 3 | 2.5 | 5 | 15.0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:236 |
| (unlabelled bed) | N | (25, 66.64, 'x') | 3.5 | 2.5 | 5 | 17.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:237 |
| BEDROOM 2 | W | (7.27, 36.3, 'y') | 4 | 2.75 | 5 | 20.0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:238 |
| BEDROOM 2 | W | (7.27, 43.6, 'y') | 4 | 2.75 | 5 | 20.0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:239 |
| (unlabelled living) | N | (43, 63.42, 'x') | 3.5 | 1.5 | 6.5 | 22.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:240 |
| SUN ROOM | N | (48.5, 63.42, 'x') | 5 | 1.5 | 6.5 | 32.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:241 |
| SUN ROOM | E | (54.6, 59.3, 'y') | 3.6 | 1.5 | 6.5 | 23.4 | option-b-as-drawn-plus-kayla/main_floor_b.scad:242 |
| GREAT ROOM | N | (77.8, 52.53, 'x') | 3.6 | 2 | 6 | 21.6 | option-b-as-drawn-plus-kayla/main_floor_b.scad:243 |
| GREAT ROOM | N | (89.4, 52.53, 'x') | 4.3 | 2 | 6 | 25.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:244 |
| MASTER BEDROOM | N | (110, 52.86, 'x') | 2.5 | 2.5 | 5 | 12.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:245 |
| MASTER BEDROOM | E | (126.97, 46, 'y') | 4.7 | 2.5 | 5 | 23.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:246 |
| MASTER BEDROOM | E | (126.97, 31, 'y') | 4 | 2.5 | 5 | 20.0 | option-b-as-drawn-plus-kayla/main_floor_b.scad:247 |
| MASTER BATH | E | (128.13, 9.8, 'y') | 4.6 | 3.5 | 4 | 18.4 | option-b-as-drawn-plus-kayla/main_floor_b.scad:248 |
| MASTER LAUNDRY | E | (128.13, 21.3, 'y') | 3.6 | 4 | 3 | 10.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:249 |
| DEN | S | (82.5, 2, 'x') | 5 | 2.5 | 5.5 | 27.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:250 |
| DEN | E | (95.95, 3, 'y') | 5 | 2.5 | 5.5 | 27.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:251 |
| DINING ROOM | W | (54.6, 3, 'y') | 3 | 2.5 | 5.5 | 16.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:252 |
| DINING ROOM | S | (55.8, 2, 'x') | 2.5 | 2.5 | 5.5 | 13.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:253 |
| LIBRARY | S | (37.7, 6.28, 'x') | 5 | 2.5 | 5.5 | 27.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:254 |
| LIBRARY | S | (46, 6.28, 'x') | 5 | 2.5 | 5.5 | 27.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:255 |
| LIBRARY | W | (35.6, 8, 'y') | 5 | 2.5 | 5.5 | 27.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:256 |
| BREAKFAST | W | (35.6, 18.5, 'y') | 2.2 | 3 | 4 | 8.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:257 |
| KITCHEN | N | (57, 50.69, 'x') | 4.5 | 3 | 3.5 | 15.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:258 |

Total main-floor window glass (width x height): 504.1 sq ft (25 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 9, S: 4, E: 6, W: 6

Rooms with windows on 2+ walls (main): SUN ROOM (E/N); MASTER BEDROOM (E/N); DEN (E/S); DINING ROOM (S/W); LIBRARY (S/W)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| PANTRY / SCULLERY | utility | 98 |
| MUDROOM | utility | 47 |
| WIC @22.1,35.46 | closet | 30 |
| LAUNDRY | utility | 138 |
| (suite entry) | hall | 47 |
| (suite entry, 2nd piece) | hall | 6 |
| WC @7.27,48.13 | bath | 47 |
| BATH 2 | bath | 69 |
| HALL @22.1,49.64 | hall | 122 |
| (N-S hall, unlabelled) | hall | 76 |
| (landing at the stair top) | hall | 22 |
| HALL @24.34,29.51 | hall | 180 |
| BATH | bath | 73 |
| BROOM / LINEN | closet | 39 |
| (dining room, north end) | dining | 65 |
| BUTLER | utility | 44 |
| VESTIBULE | hall | 66 |
| FOYER @69.14,10.5 | hall | 138 |
| FOYER @69.14,22 | hall | 52 |
| POWDER | bath | 38 |
| MEDIA | living | 178 |
| HALL @69.14,29.51 | hall | 215 |
| (master entry) | hall | 20 |
| WIC @95.95,20.56 | closet | 95 |
| (closet passage) | hall | 49 |
| WIC @112,20.56 | closet | 89 |
| MECH | utility | 42 |
| WC @99.7,16.71 | bath | 26 |
| (linen between the WCs) | closet | 25 |
| WC @99.7,9.31 | bath | 26 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| LIVING ROOM | S | (40, 5.79, 'x') | 8 | 4.5 | 4 | 32.0 | foundation.scad:160 |
| MUSIC ROOM | N | (33.15, 63.16, 'x') | 3 | 4.5 | 4 | 12.0 | foundation.scad:161 |

Rooms with windows on 2+ walls (basement): none

Basement rooms with no window row: GYM (rec, 142 sf); (unlabelled rec) (rec, 38 sf); STORAGE (closet, 115 sf); UTILITY (utility, 117 sf); HALL @37.37,35.08 (hall, 81 sf); STAIR UP (stair, 102 sf); BATH @47.27,35.08 (bath, 70 sf); HALLWAY (hall, 21 sf); (unlabelled hall) @35.27,28.725 (hall, 47 sf); (unlabelled hall) @47.27,28.725 (hall, 44 sf); HOME THEATER (tiered, 324 sf); PET ROOM (utility, 167 sf); POOL ROOM (pit, 933 sf); POOL EQUIP. (utility, 86 sf); POOL BATH (bath, 74 sf); HALL @54.14,13.43 (hall, 231 sf); BATH @54.14,5.79 (bath, 101 sf); LAUNDRY (utility, 109 sf)

## Section 6

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (suite entry) | 13.78,48.13 to 22.1,53.75 | 47 | 5.2 ft clear width (63 in), length 7.9 | option-b-as-drawn-plus-kayla/main_floor_b.scad:88 |
| (suite entry, 2nd piece) | 13.78,53.75 to 17.5,55.3 | 6 | 1.1 ft clear width (14 in), length 3.3 | option-b-as-drawn-plus-kayla/main_floor_b.scad:89 |
| HALL @22.1,49.64 | 22.1,49.64 to 42.65,55.6 | 122 | 5.6 ft clear width (67 in), length 20.1 | option-b-as-drawn-plus-kayla/main_floor_b.scad:96 |
| (N-S hall, unlabelled) | 37.3,35.46 to 42.65,49.64 | 76 | 5.0 ft clear width (59 in), length 13.8 | option-b-as-drawn-plus-kayla/main_floor_b.scad:97 |
| (landing at the stair top) | 42.65,50.825 to 47.27,55.6 | 22 | 4.2 ft clear width (51 in), length 4.4 | option-b-as-drawn-plus-kayla/main_floor_b.scad:99 |
| HALL @24.34,29.51 | 24.34,29.51 to 54.6,35.46 | 180 | 5.5 ft clear width (67 in), length 29.9 | option-b-as-drawn-plus-kayla/main_floor_b.scad:100 |
| HALL @69.14,29.51 | 69.14,29.51 to 105.2,35.46 | 215 | 5.5 ft clear width (67 in), length 35.7 | option-b-as-drawn-plus-kayla/main_floor_b.scad:122 |
| (master entry) | 105.2,29.51 to 108.62,35.46 | 20 | 3.0 ft clear width (36 in), length 5.5 | option-b-as-drawn-plus-kayla/main_floor_b.scad:126 |
| (closet passage) | 106.51,20.56 to 112,29.51 | 49 | 5.1 ft clear width (61 in), length 8.6 | option-b-as-drawn-plus-kayla/main_floor_b.scad:128 |

**Circulation total (halls only): 737 sq ft = 13.6% of 5417 sq ft conditioned** (13.8% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 66 | 5.1 ft | 14.8% | option-b-as-drawn-plus-kayla/main_floor_b.scad:113 |
| MUDROOM | 47 | 4.7 ft | 15.7% (halls+foyer+mudroom) | option-b-as-drawn-plus-kayla/main_floor_b.scad:83 |
| STAIR DN opening (stairwell) | 71 | 4.2 ft | 17.0% (all four) | option-b-as-drawn-plus-kayla/main_floor_b.scad:98 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| HALL @37.37,35.08 | 37.37,35.08 to 42.65,50.35 | 81 | 4.9 ft clear width (59 in), length 14.9 | option-b-as-drawn-plus-kayla/basement_b.scad:79 |
| HALLWAY | 35.27,27.6 to 54.14,28.725 | 21 | 0.7 ft clear width (9 in), length 18.1 | option-b-as-drawn-plus-kayla/basement_b.scad:82 |
| (unlabelled hall) @35.27,28.725 | 35.27,28.725 to 42.65,35.08 | 47 | 6.0 ft clear width (71 in), length 6.6 | option-b-as-drawn-plus-kayla/basement_b.scad:83 |
| (unlabelled hall) @47.27,28.725 | 47.27,28.725 to 54.14,35.08 | 44 | 6.0 ft clear width (71 in), length 6.5 | option-b-as-drawn-plus-kayla/basement_b.scad:84 |
| HALL @54.14,13.43 | 54.14,13.43 to 103.04,18.15 | 231 | 4.0 ft clear width (48 in), length 48.1 | option-b-as-drawn-plus-kayla/basement_b.scad:91 |

**Circulation total (halls only): 423 sq ft = 12.2% of 3475 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 102 | 4.2 ft | 15.1% | option-b-as-drawn-plus-kayla/basement_b.scad:80 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.

## Section 7

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): PATIO <-> DECK (10.9 ft shared edge); FRONT PORCH <-> (unlabelled porch) @49.24,2 (5.4 ft shared edge); FRONT PORCH <-> (unlabelled porch) @95.95,2 (5.5 ft shared edge); FRONT PORCH <-> (covered entry) (12.0 ft shared edge); DECK <-> OFFICE PORCH (6.9 ft shared edge); OFFICE PORCH <-> MASTER PORCH (6.6 ft shared edge); MASTER PORCH <-> SIDE PORCH (6.6 ft shared edge); SIDE PORCH <-> (unlabelled porch) @128.13,26.84 (9.5 ft shared edge)

Basement: HALLWAY <-> (unlabelled hall) @35.27,28.725 (7.4 ft shared edge); HALLWAY <-> (unlabelled hall) @47.27,28.725 (6.9 ft shared edge)

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| GARAGE | garage | (garage side-door pad); HALL @24.34,29.51; PANTRY / SCULLERY; SIDE ENTRY | garage to outside (option-b-as-drawn-plus-kayla/main_floor_b.scad:160), garage to outside (option-b-as-drawn-plus-kayla/main_floor_b.scad:161) |
| SIDE ENTRY | porch, ceiling 0 (open zone) | GARAGE; PANTRY / SCULLERY | - |
| PANTRY / SCULLERY | utility | BREAKFAST; GARAGE; HALL @24.34,29.51; SIDE ENTRY | - |
| MUDROOM | utility | HALL @24.34,29.51; LAUNDRY | - |
| WIC @22.1,35.46 | closet | BEDROOM 2 | - |
| LAUNDRY | utility | HALL @22.1,49.64; MUDROOM | - |
| BEDROOM 2 | bed | (suite entry); WC @7.27,48.13; WIC @22.1,35.46 | - |
| (suite entry) | hall | (suite entry, 2nd piece); BEDROOM 2; HALL @22.1,49.64 | - |
| (suite entry, 2nd piece) | hall, ceiling 0 (open zone) | (suite entry); BATH 2 | - |
| WC @7.27,48.13 | bath | BATH 2; BEDROOM 2 | - |
| BATH 2 | bath | (suite entry, 2nd piece); BUNK ROOM; WC @7.27,48.13 | - |
| BUNK ROOM | bed | (unlabelled bed); BATH 2 | - |
| (unlabelled bed) | bed | BUNK ROOM; HALL @22.1,49.64 | - |
| STUDY | office | (study stoop); HALL @22.1,49.64 | - |
| HALL @22.1,49.64 | hall | (N-S hall, unlabelled); (landing at the stair top); (suite entry); (unlabelled bed); LAUNDRY; STUDY | - |
| (N-S hall, unlabelled) | hall | HALL @22.1,49.64; HALL @24.34,29.51 | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (landing at the stair top) | - |
| (landing at the stair top) | hall | HALL @22.1,49.64; STAIR DN; SUN ROOM | - |
| HALL @24.34,29.51 | hall | (N-S hall, unlabelled); BATH; GARAGE; KITCHEN; MUDROOM; PANTRY / SCULLERY | - |
| BATH | bath | HALL @24.34,29.51 | - |
| BROOM / LINEN | closet | SUN ROOM | - |
| SUN ROOM | living | (landing at the stair top); (unlabelled living); BROOM / LINEN; PATIO | - |
| (unlabelled living) | living | SUN ROOM | - |
| PATIO | porch, ceiling 0 (open zone) | DECK; KITCHEN; SUN ROOM | - |
| LIBRARY | living | BREAKFAST; DINING ROOM | - |
| BREAKFAST | dining | BUTLER; LIBRARY; PANTRY / SCULLERY | - |
| DINING ROOM | dining | BUTLER; FRONT PORCH; LIBRARY | - |
| (dining room, north end) | dining | FOYER @69.14,22; KITCHEN | - |
| BUTLER | utility | BREAKFAST; DINING ROOM; KITCHEN | - |
| VESTIBULE | hall | (covered entry); FOYER @69.14,10.5 | - |
| FOYER @69.14,10.5 | hall | DEN; FOYER @69.14,22; POWDER; VESTIBULE | - |
| FOYER @69.14,22 | hall | (dining room, north end); FOYER @69.14,10.5; HALL @69.14,29.51 | - |
| POWDER | bath | FOYER @69.14,10.5 | - |
| DEN | living | FOYER @69.14,10.5; MECH; MEDIA | - |
| MEDIA | living | DEN; HALL @69.14,29.51 | - |
| KITCHEN | kitchen | (dining room, north end); BUTLER; GREAT ROOM; HALL @24.34,29.51; HALL @69.14,29.51; PATIO | - |
| GREAT ROOM | living | DECK; HALL @69.14,29.51; KITCHEN | - |
| HALL @69.14,29.51 | hall | (master entry); FOYER @69.14,22; GREAT ROOM; KITCHEN; MEDIA; OFFICE | - |
| OFFICE | office | HALL @69.14,29.51; OFFICE PORCH | - |
| MASTER BEDROOM | bed | (closet passage); (master entry); MASTER PORCH | - |
| (master entry) | hall | HALL @69.14,29.51; MASTER BEDROOM | - |
| WIC @95.95,20.56 | closet | (closet passage) | - |
| (closet passage) | hall | MASTER BATH; MASTER BEDROOM; WIC @112,20.56; WIC @95.95,20.56 | - |
| WIC @112,20.56 | closet | (closet passage); MASTER LAUNDRY | - |
| MASTER LAUNDRY | utility | MASTER BATH; WIC @112,20.56 | - |
| MASTER BATH | bath | (closet passage); (linen between the WCs); MASTER LAUNDRY; WC @99.7,16.71; WC @99.7,9.31 | - |
| MECH | utility | DEN | - |
| WC @99.7,16.71 | bath | MASTER BATH | - |
| (linen between the WCs) | closet | MASTER BATH | - |
| WC @99.7,9.31 | bath | MASTER BATH | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | (covered entry); (unlabelled porch) @49.24,2; (unlabelled porch) @95.95,2; DINING ROOM | - |
| (unlabelled porch) @49.24,2 | porch, ceiling 0 (open zone) | FRONT PORCH | - |
| (unlabelled porch) @95.95,2 | porch, ceiling 0 (open zone) | FRONT PORCH | - |
| (covered entry) | porch, ceiling 0 (open zone) | FRONT PORCH; VESTIBULE | - |
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
| MUSIC ROOM | living | GYM; HALL @37.37,35.08 | - |
| GYM | rec | (unlabelled rec); EXIT STAIR; MUSIC ROOM | - |
| (unlabelled rec) | rec | GYM | - |
| STORAGE | closet | HALL @37.37,35.08 | - |
| UTILITY | utility | HALL @37.37,35.08 | - |
| HALL @37.37,35.08 | hall | (unlabelled hall) @35.27,28.725; MUSIC ROOM; STORAGE; UTILITY | - |
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
| front door -> kitchen/dining room centre | 39.5 | VESTIBULE > FOYER @69.14,10.5 > FOYER @69.14,22 > (dining room, north end) > KITCHEN |
| front door -> range (option-b-as-drawn-plus-kayla/main_floor_b.scad:267) | 44.0 | VESTIBULE > FOYER @69.14,10.5 > FOYER @69.14,22 > (dining room, north end) > KITCHEN |
| garage (room centre) -> kitchen/dining room centre | 55.2 | GARAGE > PANTRY / SCULLERY > HALL @24.34,29.51 > KITCHEN |
| garage (room centre) -> range | 54.8 | GARAGE > PANTRY / SCULLERY > HALL @24.34,29.51 > KITCHEN |
| garage (room centre) -> PANTRY / SCULLERY centre | 18.1 | GARAGE > PANTRY / SCULLERY |
| garage (room centre) -> tall pantry cabinets in kitchen (option-b-as-drawn-plus-kayla/main_floor_b.scad:265) | 49.4 | GARAGE > PANTRY / SCULLERY > HALL @24.34,29.51 > KITCHEN |
| master bedroom centre -> WIC @95.95,20.56 centre | 25.0 | MASTER BEDROOM > (closet passage) > WIC @95.95,20.56 |
| master bedroom centre -> WIC @112,20.56 centre | 23.5 | MASTER BEDROOM > (closet passage) > WIC @112,20.56 |
| master bedroom centre -> LAUNDRY centre | 99.3 | MASTER BEDROOM > (master entry) > HALL @69.14,29.51 > KITCHEN > HALL @24.34,29.51 > MUDROOM > LAUNDRY |
| master bedroom centre -> MASTER LAUNDRY centre | 31.5 | MASTER BEDROOM > (closet passage) > WIC @112,20.56 > MASTER LAUNDRY |
| BEDROOM 2 centre -> BATH 2 centre | 19.5 | BEDROOM 2 > (suite entry) > (suite entry, 2nd piece) > BATH 2 |
| BEDROOM 2 centre -> hall BATH centre | 55.6 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > LAUNDRY > MUDROOM > HALL @24.34,29.51 > BATH |
| BEDROOM 2 centre -> MASTER BATH centre | 132.4 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > LAUNDRY > MUDROOM > HALL @24.34,29.51 > KITCHEN > HALL @69.14,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH |
| BEDROOM 2 centre -> LAUNDRY centre | 22.8 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > LAUNDRY |
| BEDROOM 2 centre -> MASTER LAUNDRY centre | 130.7 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > LAUNDRY > MUDROOM > HALL @24.34,29.51 > KITCHEN > HALL @69.14,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > WIC @112,20.56 > MASTER LAUNDRY |
| BUNK ROOM centre -> BATH 2 centre | 8.1 | BUNK ROOM > BATH 2 |
| BUNK ROOM centre -> hall BATH centre | 52.3 | BUNK ROOM > (unlabelled bed) > HALL @22.1,49.64 > (N-S hall, unlabelled) > HALL @24.34,29.51 > BATH |
| BUNK ROOM centre -> MASTER BATH centre | 129.2 | BUNK ROOM > (unlabelled bed) > HALL @22.1,49.64 > (N-S hall, unlabelled) > HALL @24.34,29.51 > KITCHEN > HALL @69.14,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH |
| BUNK ROOM centre -> LAUNDRY centre | 25.2 | BUNK ROOM > BATH 2 > (suite entry, 2nd piece) > (suite entry) > HALL @22.1,49.64 > LAUNDRY |
| BUNK ROOM centre -> MASTER LAUNDRY centre | 127.4 | BUNK ROOM > (unlabelled bed) > HALL @22.1,49.64 > (N-S hall, unlabelled) > HALL @24.34,29.51 > KITCHEN > HALL @69.14,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > WIC @112,20.56 > MASTER LAUNDRY |
| (unlabelled bed) centre -> BATH 2 centre | 15.4 | (unlabelled bed) > BUNK ROOM > BATH 2 |
| (unlabelled bed) centre -> hall BATH centre | 46.6 | (unlabelled bed) > HALL @22.1,49.64 > (N-S hall, unlabelled) > HALL @24.34,29.51 > BATH |
| (unlabelled bed) centre -> MASTER BATH centre | 123.5 | (unlabelled bed) > HALL @22.1,49.64 > (N-S hall, unlabelled) > HALL @24.34,29.51 > KITCHEN > HALL @69.14,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > MASTER BATH |
| (unlabelled bed) centre -> LAUNDRY centre | 19.5 | (unlabelled bed) > HALL @22.1,49.64 > LAUNDRY |
| (unlabelled bed) centre -> MASTER LAUNDRY centre | 121.8 | (unlabelled bed) > HALL @22.1,49.64 > (N-S hall, unlabelled) > HALL @24.34,29.51 > KITCHEN > HALL @69.14,29.51 > (master entry) > MASTER BEDROOM > (closet passage) > WIC @112,20.56 > MASTER LAUNDRY |
| foyer centre -> POWDER centre (powder room) | 19.7 | VESTIBULE > FOYER @69.14,10.5 > POWDER |
| front door -> top of main stair (top nosing, (44.96, 50.825)) | 75.4 | VESTIBULE > FOYER @69.14,10.5 > FOYER @69.14,22 > (dining room, north end) > KITCHEN > HALL @24.34,29.51 > (N-S hall, unlabelled) > HALL @22.1,49.64 > (landing at the stair top) |
| garage mud-entry door -> top of main stair (top nosing, (44.96, 50.825)) | 37.7 | HALL @24.34,29.51 > (N-S hall, unlabelled) > HALL @22.1,49.64 > (landing at the stair top) |
| master bedroom centre -> top of main stair (top nosing, (44.96, 50.825)) | 103.5 | MASTER BEDROOM > (master entry) > HALL @69.14,29.51 > KITCHEN > HALL @24.34,29.51 > (N-S hall, unlabelled) > HALL @22.1,49.64 > (landing at the stair top) |
| BEDROOM 2 centre -> top of main stair (top nosing, (44.96, 50.825)) | 36.4 | BEDROOM 2 > (suite entry) > HALL @22.1,49.64 > (landing at the stair top) |
| BUNK ROOM centre -> top of main stair (top nosing, (44.96, 50.825)) | 27.5 | BUNK ROOM > (unlabelled bed) > HALL @22.1,49.64 > (landing at the stair top) |
| (unlabelled bed) centre -> top of main stair (top nosing, (44.96, 50.825)) | 21.9 | (unlabelled bed) > HALL @22.1,49.64 > (landing at the stair top) |
| basement stair foot (44.96, 28.725) -> UTILITY centre | 25.6 | HALLWAY > (unlabelled hall) @35.27,28.725 > HALL @37.37,35.08 > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC @95.95,20.56 centre: no (via MASTER BEDROOM > (closet passage) > WIC @95.95,20.56); WIC @112,20.56 centre: no (via MASTER BEDROOM > (closet passage) > WIC @112,20.56)

## Section 8

### 8.1 GREAT ROOM (main; option-b-as-drawn-plus-kayla/main_floor_b.scad:121) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| PATIO | porch (ceil 0) | 1.8 | - |
| KITCHEN | kitchen | 15.2 | full 72 in |
| HALL @69.14,29.51 | hall | 26.5 | full 312 in |
| OFFICE | office | 12.7 | - |
| DECK | porch (ceil 0) | 26.5 | double 72 in |
| OFFICE PORCH | porch (ceil 0) | 4.4 | - |

### 8.1 DEN (main; option-b-as-drawn-plus-kayla/main_floor_b.scad:117) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| VESTIBULE | hall | 5.5 | - |
| FOYER @69.14,10.5 | hall | 7.0 | double 60 in |
| MEDIA | living | 14.8 | full 96 in |
| MECH | utility | 8.2 | door 36 in |
| FRONT PORCH | porch (ceil 0) | 14.8 | - |
| (unlabelled porch) @95.95,2 | porch (ceil 0) | 7.3 | - |
| (covered entry) | porch (ceil 0) | 3.0 | - |

### 8.1 LIBRARY (main; option-b-as-drawn-plus-kayla/main_floor_b.scad:108) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| SIDE ENTRY | porch (ceil 0) | 4.6 | - |
| BREAKFAST | dining | 19.0 | full 72 in |
| DINING ROOM | dining | 11.7 | double 60 in |
| (unlabelled porch) @49.24,2 | porch (ceil 0) | 5.4 | - |

### 8.1 MEDIA (main; option-b-as-drawn-plus-kayla/main_floor_b.scad:118) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| FOYER @69.14,10.5 | hall | 4.5 | - |
| POWDER | bath | 7.5 | - |
| DEN | living | 14.8 | full 96 in |
| HALL @69.14,29.51 | hall | 14.8 | full 96 in |
| WIC @95.95,20.56 | closet | 9.0 | - |
| MECH | utility | 3.1 | - |

### 8.1 SUN ROOM (main; option-b-as-drawn-plus-kayla/main_floor_b.scad:104) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| STAIR DN | stairwell (ceil 0) | 0.1 | - |
| (landing at the stair top) | hall | 4.8 | double 48 in |
| BROOM / LINEN | closet | 7.3 | door 36 in |
| (unlabelled living) | living | 7.8 | full 66 in |
| PATIO | porch (ceil 0) | 12.7 | double 58.8 in |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are GREAT ROOM, DEN, LIBRARY, MEDIA, SUN ROOM. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| HALLWAY | hall (ceil 0) | 18.9 | open 96 in |
| PET ROOM | utility | 9.5 | - |
| HALL @54.14,13.43 | hall | 4.7 | open 48 in |
| BATH @54.14,5.79 | bath | 7.6 | - |

### 8.2 FOYER (option-b-as-drawn-plus-kayla/main_floor_b.scad:113) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| DINING ROOM | dining | 5.5 | - |
| FOYER @69.14,10.5 | hall | 12.0 | double 60 in |
| DEN | living | 5.5 | - |
| (covered entry) | porch (ceil 0) | 12.0 | double 74.4 in, glass 24 in, glass 24 in |

### 8.3 Closets, WICs, linen, scullery/pantry, storage: exterior exposure

Pantry-like rooms: PANTRY / SCULLERY.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | PANTRY / SCULLERY | option-b-as-drawn-plus-kayla/main_floor_b.scad:82 | S 11.3 (porch/patio (open)); W 8.7 (garage) |
| main | WIC @22.1,35.46 | option-b-as-drawn-plus-kayla/main_floor_b.scad:84 | S 2.2 (garage) |
| main | BROOM / LINEN | option-b-as-drawn-plus-kayla/main_floor_b.scad:102 | none |
| main | WIC @95.95,20.56 | option-b-as-drawn-plus-kayla/main_floor_b.scad:127 | none |
| main | WIC @112,20.56 | option-b-as-drawn-plus-kayla/main_floor_b.scad:129 | none |
| main | (linen between the WCs) | option-b-as-drawn-plus-kayla/main_floor_b.scad:134 | none |
| base | STORAGE | option-b-as-drawn-plus-kayla/basement_b.scad:77 | W 7.6 (yard/soil) |

Pantry/garage: PANTRY / SCULLERY shares 8.7 ft of wall with the garage; doors between PANTRY / SCULLERY and GARAGE: 1. The garage's doors to the house are: option-b-as-drawn-plus-kayla/main_floor_b.scad:162 (GARAGE | (garage side-door pad), 36 in); option-b-as-drawn-plus-kayla/main_floor_b.scad:163 (GARAGE | SIDE ENTRY, 36 in); option-b-as-drawn-plus-kayla/main_floor_b.scad:165 (GARAGE | PANTRY / SCULLERY, 36 in); option-b-as-drawn-plus-kayla/main_floor_b.scad:169 (GARAGE | HALL @24.34,29.51, 36 in). The tall pantry cabinets (x 54.8-57.3) are 30.5 ft east of the garage wall (x 24.34): no shared wall.

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN | range (267); fridge (268); dishwasher (270); sink (271); island (272) | front door -> kitchen/dining room centre; front door -> range (option-b-as-drawn-plus-kayla/main_floor_b.scad:267); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range; garage (room centre) -> tall pantry cabinets in kitchen (option-b-as-drawn-plus-kayla/main_floor_b.scad:265); master bedroom centre -> LAUNDRY centre; BEDROOM 2 centre -> MASTER BATH centre; BEDROOM 2 centre -> MASTER LAUNDRY centre; BUNK ROOM centre -> MASTER BATH centre; BUNK ROOM centre -> MASTER LAUNDRY centre; (unlabelled bed) centre -> MASTER BATH centre; (unlabelled bed) centre -> MASTER LAUNDRY centre; front door -> top of main stair (top nosing, (44.96, 50.825)); master bedroom centre -> top of main stair (top nosing, (44.96, 50.825)) |
| PANTRY / SCULLERY | scullery sink (281) | garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range; garage (room centre) -> PANTRY / SCULLERY centre; garage (room centre) -> tall pantry cabinets in kitchen (option-b-as-drawn-plus-kayla/main_floor_b.scad:265) |
| LAUNDRY | washer + dryer (282); laundry sink (284) | master bedroom centre -> LAUNDRY centre; BEDROOM 2 centre -> hall BATH centre; BEDROOM 2 centre -> MASTER BATH centre; BEDROOM 2 centre -> LAUNDRY centre; BEDROOM 2 centre -> MASTER LAUNDRY centre; BUNK ROOM centre -> LAUNDRY centre; (unlabelled bed) centre -> LAUNDRY centre |
| MASTER LAUNDRY | washer + dryer (304) | master bedroom centre -> MASTER LAUNDRY centre; BEDROOM 2 centre -> MASTER LAUNDRY centre; BUNK ROOM centre -> MASTER LAUNDRY centre; (unlabelled bed) centre -> MASTER LAUNDRY centre |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| GARAGE | 2.0 | west driveway (site.scad:111) | N 5.6 (porch/patio (open)), 1.7 (yard/soil); S 24.3 (yard/soil); E 7.4 (porch/patio (open)), 5.5 (yard/soil); W 27.6 (yard/soil) |
| BEDROOM 2 | 9.3 | west driveway (site.scad:111) | S 14.8 (garage); W 3.1 (porch/patio (open)), 9.6 (yard/soil) |
| WC @7.27,48.13 | 11.1 | west driveway (site.scad:111) | W 7.2 (yard/soil) |
| DINING ROOM | 16.0 | loop north leg (:114) | S 14.5 (porch/patio (open)); E 3.0 (porch/patio (open)); W 4.3 (porch/patio (open)) |
| DEN | 16.0 | loop north leg (:114) | S 14.8 (porch/patio (open)); E 7.3 (porch/patio (open)); W 3.0 (porch/patio (open)) |
| BATH 2 | 16.2 | west driveway (site.scad:111) | N 10.2 (yard/soil); W 6.7 (yard/soil) |
| (suite entry) | 16.9 | west driveway (site.scad:111) | none |
| VESTIBULE | 19.0 | loop north leg (:114) | S 12.0 (porch/patio (open)) |
| (suite entry, 2nd piece) | 19.7 | west driveway (site.scad:111) | none |
| LIBRARY | 20.3 | loop north leg (:114) | S 5.4 (porch/patio (open)), 13.6 (yard/soil); W 4.6 (porch/patio (open)), 7.1 (yard/soil) |
| BUNK ROOM | 22.8 | west driveway (site.scad:111) | N 4.6 (yard/soil); W 4.6 (yard/soil) |
| MASTER BATH | 23.3 | loop north leg (:114) | S 21.6 (yard/soil); E 11.2 (yard/soil) |
| MECH | 23.3 | loop north leg (:114) | S 3.8 (porch/patio (open)) |
| WC @99.7,9.31 | 23.3 | loop north leg (:114) | S 1.7 (porch/patio (open)), 5.1 (yard/soil) |
| WIC @22.1,35.46 | 24.1 | west driveway (site.scad:111) | S 2.2 (garage) |
| LAUNDRY | 24.1 | west driveway (site.scad:111) | none |
| FOYER @69.14,10.5 | 24.5 | loop north leg (:114) | none |
| HALL @22.1,49.64 | 25.3 | west driveway (site.scad:111) | none |
| PANTRY / SCULLERY | 26.3 | west driveway (site.scad:111) | S 11.3 (porch/patio (open)); W 8.7 (garage) |
| HALL @24.34,29.51 | 26.3 | west driveway (site.scad:111) | W 6.0 (garage) |
| (linen between the WCs) | 27.1 | loop north leg (:114) | none |
| (unlabelled bed) | 27.7 | west driveway (site.scad:111) | N 10.5 (yard/soil); E 3.2 (yard/soil) |
| MUDROOM | 30.0 | west driveway (site.scad:111) | none |
| WC @99.7,16.71 | 30.7 | loop north leg (:114) | none |
| MEDIA | 31.5 | loop north leg (:114) | none |
| BREAKFAST | 32.0 | loop north leg (:114) | W 2.8 (porch/patio (open)) |
| WIC @95.95,20.56 | 34.6 | loop north leg (:114) | none |
| (closet passage) | 34.6 | loop north leg (:114) | none |
| WIC @112,20.56 | 34.6 | loop north leg (:114) | none |
| MASTER LAUNDRY | 34.6 | loop north leg (:114) | N 1.2 (porch/patio (open)); E 2.7 (porch/patio (open)), 6.3 (yard/soil) |
| (dining room, north end) | 36.0 | loop north leg (:114) | none |
| BUTLER | 36.0 | loop north leg (:114) | none |
| FOYER @69.14,22 | 36.0 | loop north leg (:114) | none |
| POWDER | 36.0 | loop north leg (:114) | none |
| STUDY | 37.2 | west driveway (site.scad:111) | N 4.6 (porch/patio (open)), 5.4 (yard/soil) |
| (N-S hall, unlabelled) | 39.3 | west driveway (site.scad:111) | none |

Other rooms are > 40 ft from any drive. Garage doors (rows option-b-as-drawn-plus-kayla/main_floor_b.scad:160, option-b-as-drawn-plus-kayla/main_floor_b.scad:161) face S; garage rectangle to the nearest drive piece: 2.0 ft.

## Section 9

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| sink (KITCHEN) | KITCHEN | (59.6, 48.8, 62, 50.3) | (60.8, 49.5) | N wall y=50.69 | 0.39 | option-b-as-drawn-plus-kayla/main_floor_b.scad:271 |
| sink (PANTRY / SCULLERY) | PANTRY / SCULLERY | (32.8, 21.1, 34.6, 22.4) | (33.7, 21.8) | S wall y=20.82 | 0.28 | option-b-as-drawn-plus-kayla/main_floor_b.scad:281 |
| washer/dryer (LAUNDRY) | LAUNDRY | (28.09, 47.07, 34.01, 49.05) | (31.0, 48.1) | N wall y=49.64 | 0.59 | option-b-as-drawn-plus-kayla/main_floor_b.scad:282 |
| sink (LAUNDRY) | LAUNDRY | (33.22, 41.02, 35.1, 43.52) | (34.2, 42.3) | S wall y=40.56 | 0.46 | option-b-as-drawn-plus-kayla/main_floor_b.scad:284 |
| toilet/tub/wash basin (BATH 2) | BATH 2 | (8.3, 55.6, 14.1, 58.23) | (11.2, 56.9) | S wall y=55.3 | 0.30 | option-b-as-drawn-plus-kayla/main_floor_b.scad:290 |
| vanity (BATH 2) | BATH 2 | (10.99, 60.1, 16.9, 61.68) | (13.9, 60.9) | N wall y=62.04 | 0.36 | option-b-as-drawn-plus-kayla/main_floor_b.scad:291 |
| toilet/tub/wash basin (WC @7.27,48.13) | WC @7.27,48.13 | (11.2, 52, 13.5, 54.3) | (12.3, 53.1) | E wall x=13.78 | 0.28 | option-b-as-drawn-plus-kayla/main_floor_b.scad:292 |
| vanity (BATH) | BATH | (52, 36, 54.3, 38) | (53.1, 37.0) | E wall x=54.6 | 0.30 | option-b-as-drawn-plus-kayla/main_floor_b.scad:293 |
| toilet/tub/wash basin (BATH) | BATH | (52.3, 39.5, 54.1, 41.1) | (53.2, 40.3) | E wall x=54.6 | 0.50 | option-b-as-drawn-plus-kayla/main_floor_b.scad:294 |
| shower (BATH) | BATH | (49.6, 41.9, 54.3, 45.1) | (52.0, 43.5) | N wall y=45.39 | 0.29 | option-b-as-drawn-plus-kayla/main_floor_b.scad:295 |
| vanity (MASTER BATH) | MASTER BATH | (111.64, 17.86, 121.51, 19.64) | (116.6, 18.8) | N wall y=20.56 | 0.92 | option-b-as-drawn-plus-kayla/main_floor_b.scad:296 |
| shower (MASTER BATH) | MASTER BATH | (111.97, 9.55, 120.2, 14.05) | (116.1, 11.8) | S wall y=9.31 | 0.24 | option-b-as-drawn-plus-kayla/main_floor_b.scad:297 |
| toilet/tub/wash basin (MASTER BATH) | MASTER BATH | (121.2, 12.6, 125.7, 18) | (123.5, 15.3) | E wall x=128.13 | 2.43 | option-b-as-drawn-plus-kayla/main_floor_b.scad:298 |
| toilet/tub/wash basin (WC @99.7,16.71) | WC @99.7,16.71 | (100.79, 17.01, 103.42, 19.31) | (102.1, 18.2) | S wall y=16.71 | 0.30 | option-b-as-drawn-plus-kayla/main_floor_b.scad:299 |
| toilet/tub/wash basin (WC @99.7,9.31) | WC @99.7,9.31 | (100.79, 9.77, 103.42, 12.07) | (102.1, 10.9) | S wall y=9.31 | 0.46 | option-b-as-drawn-plus-kayla/main_floor_b.scad:300 |
| toilet/tub/wash basin (POWDER) | POWDER | (78.9, 26.9, 80.8, 28.9) | (79.8, 27.9) | E wall x=81.12 | 0.32 | option-b-as-drawn-plus-kayla/main_floor_b.scad:301 |
| vanity (POWDER) | POWDER | (79.6, 23.1, 80.9, 25.4) | (80.2, 24.2) | E wall x=81.12 | 0.22 | option-b-as-drawn-plus-kayla/main_floor_b.scad:302 |
| washer/dryer (MASTER LAUNDRY) | MASTER LAUNDRY | (122.4, 26, 127.5, 29) | (125.0, 27.5) | W wall x=121.94 | 0.46 | option-b-as-drawn-plus-kayla/main_floor_b.scad:304 |

(equipment list omitted in variant mode)

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| toilet/tub/wash basin (BATH @47.27,35.08) | BATH @47.27,35.08 | (52, 41.5, 53.8, 43.3) | (52.9, 42.4) | E wall x=54.14 | 0.34 | option-b-as-drawn-plus-kayla/basement_b.scad:144 |
| vanity (BATH @47.27,35.08) | BATH @47.27,35.08 | (52.1, 38.5, 53.9, 41) | (53.0, 39.8) | E wall x=54.14 | 0.24 | option-b-as-drawn-plus-kayla/basement_b.scad:145 |
| shower (BATH @47.27,35.08) | BATH @47.27,35.08 | (47.6, 42, 50.6, 45) | (49.1, 43.5) | W wall x=47.27 | 0.33 | option-b-as-drawn-plus-kayla/basement_b.scad:146 |
| toilet/tub/wash basin (POOL BATH) | POOL BATH | (100.6, 22.5, 102.4, 24.3) | (101.5, 23.4) | E wall x=103.04 | 0.64 | option-b-as-drawn-plus-kayla/basement_b.scad:147 |
| vanity (POOL BATH) | POOL BATH | (96.6, 25.5, 98.6, 28.8) | (97.6, 27.1) | W wall x=96.33 | 0.27 | option-b-as-drawn-plus-kayla/basement_b.scad:148 |
| shower (POOL BATH) | POOL BATH | (99.2, 25.4, 102.45, 28.9) | (100.8, 27.1) | N wall y=29.12 | 0.22 | option-b-as-drawn-plus-kayla/basement_b.scad:149 |
| toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | (54.4, 6.4, 59.4, 8.95) | (56.9, 7.7) | W wall x=54.14 | 0.26 | option-b-as-drawn-plus-kayla/basement_b.scad:150 |
| vanity (BATH @54.14,5.79) | BATH @54.14,5.79 | (62.5, 6.4, 67.1, 8.25) | (64.8, 7.3) | E wall x=67.4 | 0.30 | option-b-as-drawn-plus-kayla/basement_b.scad:151 |
| toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | (65.2, 9.5, 67.1, 11.3) | (66.2, 10.4) | E wall x=67.4 | 0.30 | option-b-as-drawn-plus-kayla/basement_b.scad:152 |
| washer/dryer (LAUNDRY) | LAUNDRY | (67.8, 6.4, 72.6, 8.75) | (70.2, 7.6) | W wall x=67.4 | 0.40 | option-b-as-drawn-plus-kayla/basement_b.scad:154 |
| toilet/tub/wash basin (PET ROOM) | PET ROOM | (65.5, 26.5, 69, 28.9) | (67.2, 27.7) | N wall y=29.12 | 0.22 | option-b-as-drawn-plus-kayla/basement_b.scad:156 |

(equipment list omitted in variant mode)

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | toilet/tub/wash basin (WC @99.7,9.31) | WC @99.7,9.31 | y=9.31 (horizontal wall) | (102.1, 10.9) |
| G2 | shower (MASTER BATH) | MASTER BATH | y=9.31 (horizontal wall) | (116.1, 11.8) |
| G3 | toilet/tub/wash basin (MASTER BATH) | MASTER BATH | x=128.13 (vertical wall) | (123.5, 15.3) |
| G4 | toilet/tub/wash basin (WC @99.7,16.71) | WC @99.7,16.71 | y=16.71 (horizontal wall) | (102.1, 18.2) |
| G5 | vanity (MASTER BATH) | MASTER BATH | y=20.56 (horizontal wall) | (116.6, 18.8) |
| G6 | sink (PANTRY / SCULLERY) | PANTRY / SCULLERY | y=20.82 (horizontal wall) | (33.7, 21.8) |
| G7 | washer/dryer (MASTER LAUNDRY) | MASTER LAUNDRY | x=121.94 (vertical wall) | (125.0, 27.5) |
| G8 | toilet/tub/wash basin (POWDER); vanity (POWDER) | POWDER | x=81.12 (vertical wall) | (80.0, 26.1) |
| G9 | vanity (BATH); toilet/tub/wash basin (BATH) | BATH | x=54.6 (vertical wall) | (53.2, 38.6) |
| G10 | sink (LAUNDRY) | LAUNDRY | y=40.56 (horizontal wall) | (34.2, 42.3) |
| G11 | shower (BATH) | BATH | y=45.39 (horizontal wall) | (52.0, 43.5) |
| G12 | washer/dryer (LAUNDRY) | LAUNDRY | y=49.64 (horizontal wall) | (31.0, 48.1) |
| G13 | sink (KITCHEN) | KITCHEN | y=50.69 (horizontal wall) | (60.8, 49.5) |
| G14 | toilet/tub/wash basin (WC @7.27,48.13) | WC @7.27,48.13 | x=13.78 (vertical wall) | (12.3, 53.1) |
| G15 | toilet/tub/wash basin (BATH 2) | BATH 2 | y=55.3 (horizontal wall) | (11.2, 56.9) |
| G16 | vanity (BATH 2) | BATH 2 | y=62.04 (horizontal wall) | (13.9, 60.9) |

**Main floor: 16 wet-wall groups** (6 back-to-back plumbing clusters of rooms: PANTRY / SCULLERY | LAUNDRY | WC @7.27,48.13+BATH 2 | BATH+KITCHEN | POWDER | MASTER LAUNDRY+MASTER BATH+WC @99.7,16.71+WC @99.7,9.31)

Basement:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | vanity (BATH @54.14,5.79); toilet/tub/wash basin (BATH @54.14,5.79); washer/dryer (LAUNDRY) | BATH @54.14,5.79; LAUNDRY | x=67.4 (vertical wall) | (67.0, 8.4) |
| G2 | toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | x=54.14 (vertical wall) | (56.9, 7.7) |
| G3 | toilet/tub/wash basin (POOL BATH) | POOL BATH | x=103.04 (vertical wall) | (101.5, 23.4) |
| G4 | vanity (POOL BATH) | POOL BATH | x=96.33 (vertical wall) | (97.6, 27.1) |
| G5 | shower (POOL BATH) | POOL BATH | y=29.12 (horizontal wall) | (100.8, 27.1) |
| G6 | toilet/tub/wash basin (PET ROOM) | PET ROOM | y=29.12 (horizontal wall) | (67.2, 27.7) |
| G7 | toilet/tub/wash basin (BATH @47.27,35.08); vanity (BATH @47.27,35.08) | BATH @47.27,35.08 | x=54.14 (vertical wall) | (53.0, 41.1) |
| G8 | shower (BATH @47.27,35.08) | BATH @47.27,35.08 | x=47.27 (vertical wall) | (49.1, 43.5) |

**Basement: 8 wet-wall groups** (4 clusters: BATH @47.27,35.08 | PET ROOM | POOL BATH | BATH @54.14,5.79+LAUNDRY)

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 16/8; 6 ft: 16/8; 8 ft: 16/8; 12 ft: 15/8; inf: 14/6

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | toilet/tub/wash basin (WC @99.7,9.31) | (102.1,10.9) | B3 (POOL BATH) | (101.5,23.4) | 0.6 | 12.5 | 13.1 |
| G2 | shower (MASTER BATH) | (116.1,11.8) | B3 (POOL BATH) | (101.5,23.4) | 14.6 | 11.6 | 26.2 |
| G3 | toilet/tub/wash basin (MASTER BATH) | (123.5,15.3) | B3 (POOL BATH) | (101.5,23.4) | 22.0 | 8.1 | 30.1 |
| G4 | toilet/tub/wash basin (WC @99.7,16.71) | (102.1,18.2) | B3 (POOL BATH) | (101.5,23.4) | 0.6 | 5.2 | 5.8 |
| G5 | vanity (MASTER BATH) | (116.6,18.8) | B3 (POOL BATH) | (101.5,23.4) | 15.1 | 4.6 | 19.7 |
| G6 | sink (PANTRY / SCULLERY) | (33.7,21.8) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 15.4 | 21.8 | 37.1 |
| G7 | washer/dryer (MASTER LAUNDRY) | (125.0,27.5) | B5 (POOL BATH) | (100.8,27.1) | 24.1 | 0.4 | 24.5 |
| G8 | toilet/tub/wash basin (POWDER); vanity (POWDER) | (80.0,26.1) | B6 (PET ROOM) | (67.2,27.7) | 12.8 | 1.6 | 14.4 |
| G9 | vanity (BATH); toilet/tub/wash basin (BATH) | (53.2,38.6) | B7 (BATH @47.27,35.08) | (53.0,41.1) | 0.2 | 2.4 | 2.6 |
| G10 | sink (LAUNDRY) | (34.2,42.3) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 14.9 | 1.2 | 16.2 |
| G11 | shower (BATH) | (52.0,43.5) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 2.9 | 0.0 | 2.9 |
| G12 | washer/dryer (LAUNDRY) | (31.0,48.1) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 18.1 | 4.6 | 22.6 |
| G13 | sink (KITCHEN) | (60.8,49.5) | B7 (BATH @47.27,35.08) | (53.0,41.1) | 7.8 | 8.5 | 16.3 |
| G14 | toilet/tub/wash basin (WC @7.27,48.13) | (12.3,53.1) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 36.8 | 9.6 | 46.4 |
| G15 | toilet/tub/wash basin (BATH 2) | (11.2,56.9) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 37.9 | 13.4 | 51.3 |
| G16 | vanity (BATH 2) | (13.9,60.9) | B8 (BATH @47.27,35.08) | (49.1,43.5) | 35.2 | 17.4 | 52.5 |

Main-floor groups with a basement group within 5 ft Manhattan: 2 of 16; within 10 ft: 3.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (102.1,10.9) | 127.0 | 107.9 |
| G2 | (116.1,11.8) | 140.1 | 121.0 |
| G3 | (123.5,15.3) | 144.0 | 124.9 |
| G4 | (102.1,18.2) | 119.8 | 100.7 |
| G5 | (116.6,18.8) | 133.7 | 114.6 |
| G6 | (33.7,21.8) | 47.8 | 28.7 |
| G7 | (125.0,27.5) | 133.3 | 114.2 |
| G8 | (80.0,26.1) | 89.8 | 70.7 |
| G9 | (53.2,38.6) | 50.4 | 31.3 |
| G10 | (34.2,42.3) | 27.7 | 15.4 |
| G11 | (52.0,43.5) | 44.3 | 34.4 |
| G12 | (31.0,48.1) | 18.8 | 18.1 |
| G13 | (60.8,49.5) | 47.1 | 49.3 |
| G14 | (12.3,53.1) | 14.7 | 24.1 |
| G15 | (11.2,56.9) | 12.0 | 29.0 |
| G16 | (13.9,60.9) | 11.1 | 30.2 |

**DRI (E = (22.16, 58)) = 1161.6 ft over 16 groups; mean 72.6 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 1014.3 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:160, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:159). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **toilet/tub/wash basin (MASTER BATH), 114.8 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: toilet/tub/wash basin (MASTER BATH), 117.5 ft.
- Furthest basement fixture: **toilet/tub/wash basin (POOL BATH), 84.8 ft** from the water heater.
- Nearest main-floor fixture: sink (LAUNDRY), 9.5 ft.

Per fixture (Manhattan plan ft from the water heater): sink (KITCHEN) 43; sink (PANTRY / SCULLERY) 19; washer/dryer (LAUNDRY) 12; sink (LAUNDRY) 10; toilet/tub/wash basin (BATH 2) 39; vanity (BATH 2) 40; toilet/tub/wash basin (WC @7.27,48.13) 34; vanity (BATH) 23; toilet/tub/wash basin (BATH) 27; shower (BATH) 29; vanity (MASTER BATH) 105; shower (MASTER BATH) 111; toilet/tub/wash basin (MASTER BATH) 115; toilet/tub/wash basin (WC @99.7,16.71) 91; toilet/tub/wash basin (WC @99.7,9.31) 98; toilet/tub/wash basin (POWDER) 59; vanity (POWDER) 63; washer/dryer (MASTER LAUNDRY) 104; toilet/tub/wash basin (BATH @47.27,35.08) 28; vanity (BATH @47.27,35.08) 26; shower (BATH @47.27,35.08) 26; toilet/tub/wash basin (POOL BATH) 85; vanity (POOL BATH) 77; shower (POOL BATH) 80; toilet/tub/wash basin (BATH @54.14,5.79) 56; vanity (BATH @54.14,5.79) 64; toilet/tub/wash basin (BATH @54.14,5.79) 62; washer/dryer (LAUNDRY) 69; toilet/tub/wash basin (PET ROOM) 46

## Section 10

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
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | option-b-as-drawn-plus-kayla/main_floor_b.scad:98 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | option-b-as-drawn-plus-kayla/basement_b.scad:80 |
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

## Section 12

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



## Option B additions (hand-written; the sections above are generated by plan_facts.py in variant mode)

**Reading note.** Prose lines above that quote `main_floor.scad:NNN`, `house_lib.scad:NNN` or the Redesign doc describe the CURRENT model (README-variant "Limits"). In particular, section 10.1 quotes the one-flight stair table from `house_lib.scad`; Option B's stair is the table below. The matrix row "Min distance bedroom -> drive" reads the unchanged `site.scad` and still says 9.3 ft; see "Site" below.

### Stair fit, two flights (CODE-01)

| Item | Value |
|---|---|
| Wall centre lines x | 42.65 to 47.27 (unchanged); clear width 4.22 ft = 1,286 mm |
| Risers | 22 x 7.5 in = 11 + 11, rise per flight 6.875 ft = 2.10 m (limit in CODE-01 is 3.7 m) |
| Treads | 20 x 10.5 in (10 + 10) |
| Landing | 4.6 ft long (y 37.475-42.075), 6.875 ft below the main floor, full stair width; CODE-07 asks for at least the stair width (4.22 ft) |
| Top nosing y / foot y | 50.825 / 28.725 (foot unchanged: same as the basement's HALLWAY archway) |
| Total run | 17.5 ft of treads + 4.6 ft landing = 22.1 ft |
| Main-floor opening (STAIR DN) | x 42.65-47.27, y 35.46-50.825: 4.2 x 15.0 ft clear, 71 sf (was 54 sf) |
| Headroom at the south end of the opening | stair underside z = -6.875 - 1.815 x (0.625/0.875) = -8.17 ft; floor underside z = -1.625; 6.55 ft = 1,996 mm against 1,950 mm: 46 mm margin (STR-08 had 43 mm). Computed from the stair table, engineer to confirm. |
| Top landing | the HALL at y 50.825-55.6: 4.575 ft clear in front of the top nosing (1,394 mm) |
| Basement stair room STAIR UP (`basement_b.scad`) | x 42.65-47.27, y 28.725-50.825; the gym loses its SW corner (x 42.65-47.27, y 45.34-50.825 = 25 sf); GYM is two rectangles joined by a 6.4 ft opening; gym door from the MUSIC ROOM at x 42.65, y 52.0 |
| Under the landing | basement x 42.65-47.27, y 37.5-42.1: 6.9 ft of space below the landing, enclosed with the stair box (not walkable) |

### Site and distance to the drive (hand-measured; `site.scad` not edited)

- Garage doors: two 9 ft doors in the south wall (y 7.9) at x 2.0-11.0 and 12.5-21.5.
- The apron lies south of y 7.9, so the distance from BEDROOM 2 (south wall y 35.46) to the nearest drive is at least 27.6 ft. Current: 9.3 ft. The 27.6 ft assumes the apron does not extend north of the garage's south wall.
- The meters under BEDROOM 2's west window (ELE-05, GAS-02) move to the garage west wall.

### Kitchen triangle (K-261), from fixture centres

Fridge (56.05, 47.6) to sink (60.8, 49.55): 5.1 ft. Sink to range (56.05, 42.5): 8.5 ft. Range to fridge: 5.1 ft. Total 18.7 ft. Island centre (63.8, 40.4): 8.0 ft to the range.

### Sheet calibration, residuals

In `README.md`.
