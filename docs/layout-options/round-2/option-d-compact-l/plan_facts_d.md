# Plan facts (variant mode)

main = `/home/user/house-review/docs/layout-options/round-2/option-d-compact-l/main_floor_d.scad`, basement = `/home/user/house-review/docs/layout-options/round-2/option-d-compact-l/basement_d.scad`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.

## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-2/option-d-compact-l/main_floor_d.scad`; basement = `/home/user/house-review/docs/layout-options/round-2/option-d-compact-l/basement_d.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 2,779 | 2778.7; excl. stair opening 2725.8 |
| Building area, centre lines (house + attached garage) | 313.5 m2 | 3374 sq ft |
| Building area, outside face | 330.4 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 2,934 sq ft | centre lines 2,779 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 2,934 sq ft | centre lines 2,779 sq ft |
| Circulation % (strict / with foyer) | 6.9% / 8.7% | 193 sq ft strict of 2779 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 1 / 12 | type `door` rows, by opening width |
| Double / open counts (main) | 4 / 10 | type `double` / type `open` |
| Minimum hall clear width | 5.60 ft (HALL) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 4.20 ft ((stair top landing)) |
| Wet-wall groups (main / basement) | 7 / 4 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 3 of 7 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 587.2 ft | alternate exit (22.16, 38.9): 557.3 ft |
| Water heater -> furthest fixture (main / basement) | 94.7 ft (shower (SHOWER)) / 94.4 ft (toilet/tub/wash basin (BATH @92.8,41.2)) | water heater at (32.0, 20.0); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 23.5 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 3 of 5: LINEN [W(yard 2.7)]; BR 2 CLOSET [S(yard 3.8) E(yard 7.4)]; WIC @96.4,41.2 [S(yard 4.8) E(yard 8.4)] | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 10.0 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: E(yard 12.2) ;; MASTER BEDROOM: N(yard 22.0) E(porch/patio 14.0, yard 5.9) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 31.0) S(yard 4.8) E(porch/patio 14.0, yard 14.3) W(yard 19.9) | suite rooms: (suite hall), WIC @88.4,41.2, WIC @96.4,41.2, MASTER BATH, WC, SHOWER, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING ROOM (20.0 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 3: KITCHEN (N/S); LIVING ROOM (N/S); MASTER BEDROOM (E/N) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 77.8..82.4, y 38.5; basement foot room x 77.8..82.4, y 27; **moved** (x offset +0.00/+0.00 ft, run 11.500 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 43.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_d.scad (defaults): 29 rooms, 31 doors, 16 windows - OK ; basement_d.scad (defaults): 28 rooms, 24 doors, 8 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |

## Section 1

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 2778.7 | computed: sum (x1-x0)*(y1-y0) over 23 rows, main_floor.scad:54-86 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 52.9 | option-d-compact-l/main_floor_d.scad:66 |
| Main-floor conditioned excluding the stair opening | 2725.8 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 2778.7 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 2834.7 | computed over basement.scad:46-77 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 595.4 | option-d-compact-l/main_floor_d.scad:54 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| DRIVE | 390.4 | option-d-compact-l/main_floor_d.scad:82 |
| MUD STOOP | 24.0 | option-d-compact-l/main_floor_d.scad:83 |
| FRONT PORCH | 102.4 | option-d-compact-l/main_floor_d.scad:84 |
| PATIO | 518.3 | option-d-compact-l/main_floor_d.scad:85 |
| DECK | 112.0 | option-d-compact-l/main_floor_d.scad:86 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 1147.1 sq ft. PATIO alone: 518.3; DECK alone: 112.0. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 307.8 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 203.8 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 82.4 ft | same |
|   facing garage | 21.6 ft | same (garage is unheated) |
| Outside (convex) corners | 9 | vertices of the union polygon after 0.02 ft simplify (14 vertices) |
| Inside (reflex) corners | 5 | same polygon |
| Bounding box, heated rooms | x 24.4..105 (80.6 ft), y 0..69.5 (69.5 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 0..113 (113 ft), y -16..69.5 (85.5 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 9 hip-roof blocks in main_roof (main_floor.scad:244); each hip block is 4 sloped facets, so 4 x 9 = 36 nominal facets before overlapping blocks merge; 5 blocks at 6/12 pitch, 4 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)

## Section 2

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| MUDROOM | S 4.8 (porch/patio (open)), 3.6 (yard/soil); W 11.6 (garage) | option-d-compact-l/main_floor_d.scad:55 |
| PANTRY | N 8.4 (yard/soil); W 10.0 (garage) | option-d-compact-l/main_floor_d.scad:56 |
| KITCHEN | N 12.2 (porch/patio (open)), 3.2 (yard/soil); S 15.4 (yard/soil) | option-d-compact-l/main_floor_d.scad:57 |
| DINING + NOOK | N 14.2 (porch/patio (open)); S 14.2 (yard/soil) | option-d-compact-l/main_floor_d.scad:58 |
| LIVING ROOM | N 15.4 (porch/patio (open)); S 3.4 (porch/patio (open)), 16.6 (yard/soil) | option-d-compact-l/main_floor_d.scad:59 |
| VESTIBULE | S 6.0 (porch/patio (open)); E 8.0 (yard/soil) | option-d-compact-l/main_floor_d.scad:60 |
| FOYER | E 3.6 (yard/soil) | option-d-compact-l/main_floor_d.scad:61 |
| BATH | S 8.0 (yard/soil); E 10.0 (yard/soil) | option-d-compact-l/main_floor_d.scad:62 |
| HALL | none | option-d-compact-l/main_floor_d.scad:64 |
| (stair top landing) | W 5.4 (porch/patio (open)) | option-d-compact-l/main_floor_d.scad:65 |
| STAIR DN | W 7.0 (porch/patio (open)), 4.5 (yard/soil) | option-d-compact-l/main_floor_d.scad:66 |
| LINEN | W 2.7 (yard/soil) | option-d-compact-l/main_floor_d.scad:67 |
| ELEVATOR (FUTURE) | none | option-d-compact-l/main_floor_d.scad:68 |
| BEDROOM 2 | E 12.2 (yard/soil) | option-d-compact-l/main_floor_d.scad:70 |
| BR 2 CLOSET | S 3.8 (yard/soil); E 7.4 (yard/soil) | option-d-compact-l/main_floor_d.scad:71 |
| LAUNDRY | S 3.8 (yard/soil); W 8.4 (yard/soil) | option-d-compact-l/main_floor_d.scad:73 |
| (suite hall) | none | option-d-compact-l/main_floor_d.scad:74 |
| WIC @88.4,41.2 | none | option-d-compact-l/main_floor_d.scad:75 |
| WIC @96.4,41.2 | S 4.8 (yard/soil); E 8.4 (yard/soil) | option-d-compact-l/main_floor_d.scad:76 |
| MASTER BATH | W 12.4 (yard/soil) | option-d-compact-l/main_floor_d.scad:77 |
| WC | N 4.6 (yard/soil); W 7.5 (yard/soil) | option-d-compact-l/main_floor_d.scad:78 |
| SHOWER | N 4.4 (yard/soil) | option-d-compact-l/main_floor_d.scad:79 |
| MASTER BEDROOM | N 22.0 (yard/soil); E 14.0 (porch/patio (open)), 5.9 (yard/soil) | option-d-compact-l/main_floor_d.scad:80 |

## Section 3

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MUDROOM | 24.4 | 0 | 32.8 | 11.6 | 8.40 x 11.60 | 8.0 x 11.2 | 97 | 90 | 1.38 | utility | 10 | option-d-compact-l/main_floor_d.scad:55 |
| PANTRY | 24.4 | 11.6 | 32.8 | 21.6 | 8.40 x 10.00 | 8.0 x 9.6 | 84 | 77 | 1.19 | utility | 10 | option-d-compact-l/main_floor_d.scad:56 |
| KITCHEN | 32.8 | 0 | 48.2 | 21.6 | 15.40 x 21.60 | 15.0 x 21.2 | 333 | 318 | 1.40 | kitchen | 12 | option-d-compact-l/main_floor_d.scad:57 |
| DINING + NOOK | 48.2 | 0 | 62.4 | 21.6 | 14.20 x 21.60 | 13.8 x 21.2 | 307 | 293 | 1.52 | dining | 12 | option-d-compact-l/main_floor_d.scad:58 |
| LIVING ROOM | 62.4 | 0 | 82.4 | 21.6 | 20.00 x 21.60 | 19.6 x 21.2 | 432 | 416 | 1.08 | living | 12 | option-d-compact-l/main_floor_d.scad:59 |
| VESTIBULE | 82.4 | 0 | 88.4 | 8 | 6.00 x 8.00 | 5.6 x 7.6 | 48 | 43 | 1.33 | hall | 10 | option-d-compact-l/main_floor_d.scad:60 |
| FOYER | 82.4 | 8 | 88.4 | 21.6 | 6.00 x 13.60 | 5.6 x 13.2 | 82 | 74 | 2.27 | hall | 12 | option-d-compact-l/main_floor_d.scad:61 |
| BATH | 88.4 | 11.6 | 96.4 | 21.6 | 8.00 x 10.00 | 7.6 x 9.6 | 80 | 73 | 1.25 | bath | 10 | option-d-compact-l/main_floor_d.scad:62 |
| HALL | 82.4 | 21.6 | 88.4 | 41.2 | 6.00 x 19.60 | 5.6 x 19.2 | 118 | 108 | 3.27 | hall | 10 | option-d-compact-l/main_floor_d.scad:64 |
| (stair top landing) | 77.8 | 21.6 | 82.4 | 27 | 4.60 x 5.40 | 4.2 x 5.0 | 25 | 21 | 1.17 | hall | 10 | option-d-compact-l/main_floor_d.scad:65 |
| STAIR DN | 77.8 | 27 | 82.4 | 38.5 | 4.60 x 11.50 | 4.2 x 11.1 | 53 | - | 2.50 | stairwell | 0 | option-d-compact-l/main_floor_d.scad:66 |
| LINEN | 77.8 | 38.5 | 82.4 | 41.2 | 4.60 x 2.70 | 4.2 x 2.3 | 12 | 10 | 1.70 | closet | 10 | option-d-compact-l/main_floor_d.scad:67 |
| ELEVATOR (FUTURE) | 88.4 | 21.6 | 94.4 | 29 | 6.00 x 7.40 | 5.6 x 7.0 | 44 | 39 | 1.23 | closet | 10 | option-d-compact-l/main_floor_d.scad:68 |
| BEDROOM 2 | 88.4 | 29 | 100.2 | 41.2 | 11.80 x 12.20 | 11.4 x 11.8 | 144 | 135 | 1.03 | bed | 10 | option-d-compact-l/main_floor_d.scad:70 |
| BR 2 CLOSET | 94.4 | 21.6 | 100.2 | 29 | 5.80 x 7.40 | 5.4 x 7.0 | 43 | 38 | 1.28 | closet | 10 | option-d-compact-l/main_floor_d.scad:71 |
| LAUNDRY | 74 | 41.2 | 82.4 | 49.6 | 8.40 x 8.40 | 8.0 x 8.0 | 71 | 64 | 1.00 | utility | 10 | option-d-compact-l/main_floor_d.scad:73 |
| (suite hall) | 82.4 | 41.2 | 88.4 | 49.6 | 6.00 x 8.40 | 5.6 x 8.0 | 50 | 45 | 1.40 | hall | 10 | option-d-compact-l/main_floor_d.scad:74 |
| WIC @88.4,41.2 | 88.4 | 41.2 | 96.4 | 49.6 | 8.00 x 8.40 | 7.6 x 8.0 | 67 | 61 | 1.05 | closet | 10 | option-d-compact-l/main_floor_d.scad:75 |
| WIC @96.4,41.2 | 96.4 | 41.2 | 105 | 49.6 | 8.60 x 8.40 | 8.2 x 8.0 | 72 | 66 | 1.02 | closet | 10 | option-d-compact-l/main_floor_d.scad:76 |
| MASTER BATH | 74 | 49.6 | 83 | 62 | 9.00 x 12.40 | 8.6 x 12.0 | 112 | 103 | 1.38 | bath | 10 | option-d-compact-l/main_floor_d.scad:77 |
| WC | 74 | 62 | 78.6 | 69.5 | 4.60 x 7.50 | 4.2 x 7.1 | 34 | 30 | 1.63 | bath | 10 | option-d-compact-l/main_floor_d.scad:78 |
| SHOWER | 78.6 | 62 | 83 | 69.5 | 4.40 x 7.50 | 4.0 x 7.1 | 33 | 28 | 1.70 | bath | 10 | option-d-compact-l/main_floor_d.scad:79 |
| MASTER BEDROOM | 83 | 49.6 | 105 | 69.5 | 22.00 x 19.90 | 21.6 x 19.5 | 438 | 421 | 1.11 | bed | 10 | option-d-compact-l/main_floor_d.scad:80 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 0 | 0 | 24.4 | 24.4 | 24.40 x 24.40 | 24.0 x 24.0 | 595 | 576 | 1.00 | garage | 10 | option-d-compact-l/main_floor_d.scad:54 |
| DRIVE | 0 | -16 | 24.4 | 0 | 24.40 x 16.00 | 24.4 x 16.0 (open) | 390 | - | 1.52 | porch | 0 | option-d-compact-l/main_floor_d.scad:82 |
| MUD STOOP | 28 | -5 | 32.8 | 0 | 4.80 x 5.00 | 4.8 x 5.0 (open) | 24 | - | 1.04 | porch | 0 | option-d-compact-l/main_floor_d.scad:83 |
| FRONT PORCH | 79 | -8 | 91.8 | 0 | 12.80 x 8.00 | 12.8 x 8.0 (open) | 102 | - | 1.60 | porch | 0 | option-d-compact-l/main_floor_d.scad:84 |
| PATIO | 36 | 21.6 | 77.8 | 34 | 41.80 x 12.40 | 41.8 x 12.4 (open) | 518 | - | 3.37 | porch | 0 | option-d-compact-l/main_floor_d.scad:85 |
| DECK | 105 | 54 | 113 | 68 | 8.00 x 14.00 | 8.0 x 14.0 (open) | 112 | - | 1.75 | porch | 0 | option-d-compact-l/main_floor_d.scad:86 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STORAGE @24.4,0 | 24.4 | 0 | 35 | 9.6 | 10.60 x 9.60 | 9.8 x 8.8 | 102 | 87 | 1.10 | closet | 10 | option-d-compact-l/basement_d.scad:46 |
| UTILITY | 24.4 | 9.6 | 35 | 21.6 | 10.60 x 12.00 | 9.8 x 11.2 | 127 | 111 | 1.13 | utility | 10 | option-d-compact-l/basement_d.scad:47 |
| OFFICE / LIBRARY | 35 | 0 | 51 | 13.6 | 16.00 x 13.60 | 15.6 x 12.8 | 218 | 200 | 1.18 | office | 10 | option-d-compact-l/basement_d.scad:49 |
| STORAGE @35,13.6 | 35 | 13.6 | 51 | 21.6 | 16.00 x 8.00 | 15.6 x 7.2 | 128 | 113 | 2.00 | closet | 10 | option-d-compact-l/basement_d.scad:50 |
| GYM / MUSIC | 51 | 0 | 64 | 13.6 | 13.00 x 13.60 | 12.6 x 12.8 | 177 | 162 | 1.05 | rec | 10 | option-d-compact-l/basement_d.scad:51 |
| STORAGE @51,13.6 | 51 | 13.6 | 64 | 21.6 | 13.00 x 8.00 | 12.6 x 7.2 | 104 | 91 | 1.62 | closet | 10 | option-d-compact-l/basement_d.scad:52 |
| LIVING ROOM | 64 | 0 | 82.4 | 21.6 | 18.40 x 21.60 | 18.0 x 20.5 | 397 | 369 | 1.17 | living | 10 | option-d-compact-l/basement_d.scad:53 |
| HALL @82.4,0 | 82.4 | 0 | 88.4 | 21.6 | 6.00 x 21.60 | 5.2 x 20.8 | 130 | 109 | 3.60 | hall | 10 | option-d-compact-l/basement_d.scad:54 |
| BATH @88.4,11.6 | 88.4 | 11.6 | 96.4 | 21.6 | 8.00 x 10.00 | 7.2 x 9.2 | 80 | 67 | 1.25 | bath | 10 | option-d-compact-l/basement_d.scad:55 |
| HALL @82.4,21.6 | 82.4 | 21.6 | 88.4 | 41.2 | 6.00 x 19.60 | 5.6 x 19.2 | 118 | 108 | 3.27 | hall | 10 | option-d-compact-l/basement_d.scad:57 |
| UNDER STAIR | 77.8 | 21.6 | 82.4 | 27 | 4.60 x 5.40 | 3.8 x 5.0 | 25 | 19 | 1.17 | closet | 10 | option-d-compact-l/basement_d.scad:58 |
| STAIR UP | 77.8 | 27 | 82.4 | 42.75 | 4.60 x 15.75 | 3.8 x 15.3 | 72 | 59 | 3.42 | stair | 10 | option-d-compact-l/basement_d.scad:59 |
| STAIR FOOT | 77.8 | 42.75 | 82.4 | 49.6 | 4.60 x 6.85 | 4.2 x 6.5 | 32 | 27 | 1.49 | hall | 10 | option-d-compact-l/basement_d.scad:60 |
| HALL @82.4,41.2 | 82.4 | 41.2 | 92.8 | 49.6 | 10.40 x 8.40 | 9.6 x 8.0 | 87 | 77 | 1.24 | hall | 10 | option-d-compact-l/basement_d.scad:61 |
| ELEVATOR (FUTURE) | 88.4 | 21.6 | 94.4 | 29 | 6.00 x 7.40 | 5.6 x 7.0 | 44 | 39 | 1.23 | closet | 10 | option-d-compact-l/basement_d.scad:62 |
| FLEX / CRAFT | 88.4 | 29 | 100.2 | 41.2 | 11.80 x 12.20 | 11.0 x 11.8 | 144 | 130 | 1.03 | bed | 10 | option-d-compact-l/basement_d.scad:64 |
| CLOSET @94.4,21.6 | 94.4 | 21.6 | 100.2 | 29 | 5.80 x 7.40 | 5.0 x 6.6 | 43 | 34 | 1.28 | closet | 10 | option-d-compact-l/basement_d.scad:65 |
| STORAGE @74,41.2 | 74 | 41.2 | 77.8 | 49.6 | 3.80 x 8.40 | 2.7 x 7.6 | 32 | 21 | 2.21 | closet | 10 | option-d-compact-l/basement_d.scad:66 |
| BATH @92.8,41.2 | 92.8 | 41.2 | 100.8 | 49.6 | 8.00 x 8.40 | 7.6 x 7.6 | 67 | 58 | 1.05 | bath | 10 | option-d-compact-l/basement_d.scad:67 |
| STORAGE @100.8,41.2 | 100.8 | 41.2 | 105 | 49.6 | 4.20 x 8.40 | 3.4 x 7.6 | 35 | 26 | 2.00 | closet | 10 | option-d-compact-l/basement_d.scad:68 |
| (unlabelled hall) | 86.2 | 49.6 | 92.8 | 69.5 | 6.60 x 19.90 | 6.2 x 19.1 | 131 | 119 | 3.02 | hall | 10 | option-d-compact-l/basement_d.scad:69 |
| BEDROOM 4 | 74 | 57 | 86.2 | 69.5 | 12.20 x 12.50 | 11.4 x 11.7 | 153 | 134 | 1.02 | bed | 10 | option-d-compact-l/basement_d.scad:70 |
| CLOSET @74,49.6 | 74 | 49.6 | 86.2 | 57 | 12.20 x 7.40 | 11.4 x 7.0 | 90 | 80 | 1.65 | closet | 10 | option-d-compact-l/basement_d.scad:71 |
| BEDROOM 3 | 92.8 | 57 | 105 | 69.5 | 12.20 x 12.50 | 11.4 x 11.7 | 153 | 134 | 1.02 | bed | 10 | option-d-compact-l/basement_d.scad:72 |
| CLOSET @92.8,49.6 | 92.8 | 49.6 | 105 | 57 | 12.20 x 7.40 | 11.4 x 7.0 | 90 | 80 | 1.65 | closet | 10 | option-d-compact-l/basement_d.scad:73 |
| WINDOW WELL @70.5,59.5 | 70.5 | 59.5 | 74 | 65 | 3.50 x 5.50 | 3.5 x 5.5 (open) | 19 | - | 1.57 | porch | 0 | option-d-compact-l/basement_d.scad:75 |
| WINDOW WELL @105,59.5 | 105 | 59.5 | 108.5 | 65 | 3.50 x 5.50 | 3.5 x 5.5 (open) | 19 | - | 1.57 | porch | 0 | option-d-compact-l/basement_d.scad:76 |
| WINDOW WELL @100.2,31.5 | 100.2 | 31.5 | 103.7 | 36.5 | 3.50 x 5.00 | 3.5 x 5.0 (open) | 18 | - | 1.43 | porch | 0 | option-d-compact-l/basement_d.scad:77 |

## Section 4

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (82.8, 0) x | 5 ft = 60 in | double | 1 | FRONT PORCH / VESTIBULE | option-d-compact-l/main_floor_d.scad:92 |
| M2 | (4, 0) x | 16 ft = 192 in | garage | - | DRIVE / GARAGE | option-d-compact-l/main_floor_d.scad:93 |
| M3 | (29.4, 0) x | 3 ft = 36 in | door | 1 | MUD STOOP / MUDROOM | option-d-compact-l/main_floor_d.scad:94 |
| M4 | (53, 21.6) x | 6 ft = 72 in | double | 1 | DINING + NOOK / PATIO | option-d-compact-l/main_floor_d.scad:95 |
| M5 | (69.5, 21.6) x | 6 ft = 72 in | double | 1 | LIVING ROOM / PATIO | option-d-compact-l/main_floor_d.scad:96 |
| M6 | (105, 56) y | 6 ft = 72 in | double | 1 | MASTER BEDROOM / DECK | option-d-compact-l/main_floor_d.scad:97 |
| M7 | (24.4, 3) y | 3 ft = 36 in | door | 1 | GARAGE / MUDROOM | option-d-compact-l/main_floor_d.scad:99 |
| M8 | (24.4, 14) y | 3 ft = 36 in | door | 1 | GARAGE / PANTRY | option-d-compact-l/main_floor_d.scad:100 |
| M9 | (32.8, 7.6) y | 4 ft = 48 in | open | - | MUDROOM / KITCHEN | option-d-compact-l/main_floor_d.scad:101 |
| M10 | (32.8, 14) y | 3 ft = 36 in | door | 1 | PANTRY / KITCHEN | option-d-compact-l/main_floor_d.scad:102 |
| M11 | (48.2, 11) y | 9 ft = 108 in | full | - | KITCHEN / DINING + NOOK | option-d-compact-l/main_floor_d.scad:103 |
| M12 | (62.4, 4) y | 6 ft = 72 in | open | - | DINING + NOOK / LIVING ROOM | option-d-compact-l/main_floor_d.scad:104 |
| M13 | (83.2, 8) x | 4.8 ft = 57.6 in | open | - | VESTIBULE / FOYER | option-d-compact-l/main_floor_d.scad:106 |
| M14 | (82.4, 10) y | 6 ft = 72 in | open | - | LIVING ROOM / FOYER | option-d-compact-l/main_floor_d.scad:107 |
| M15 | (88.4, 12.4) y | 3 ft = 36 in | door | 1 | FOYER / BATH | option-d-compact-l/main_floor_d.scad:108 |
| M16 | (82.6, 21.6) x | 5.6 ft = 67.2 in | full | - | FOYER / HALL | option-d-compact-l/main_floor_d.scad:109 |
| M17 | (82.4, 22) y | 4.8 ft = 57.6 in | open | - | (stair top landing) / HALL | option-d-compact-l/main_floor_d.scad:111 |
| M18 | (78, 27) x | 4.2 ft = 50.4 in | full | - | (stair top landing) / STAIR DN | option-d-compact-l/main_floor_d.scad:112 |
| M19 | (88.4, 22.4) y | 3 ft = 36 in | door | 1 | HALL / ELEVATOR (FUTURE) | option-d-compact-l/main_floor_d.scad:113 |
| M20 | (88.4, 30.5) y | 3 ft = 36 in | door | 1 | HALL / BEDROOM 2 | option-d-compact-l/main_floor_d.scad:114 |
| M21 | (95, 29) x | 3 ft = 36 in | open | - | BR 2 CLOSET / BEDROOM 2 | option-d-compact-l/main_floor_d.scad:115 |
| M22 | (82.4, 38.7) y | 2.4 ft = 28.8 in | open | - | LINEN / HALL | option-d-compact-l/main_floor_d.scad:116 |
| M23 | (84.4, 41.2) x | 3 ft = 36 in | door | 1 | HALL / (suite hall) | option-d-compact-l/main_floor_d.scad:118 |
| M24 | (82.4, 43) y | 3 ft = 36 in | door | -1 | LAUNDRY / (suite hall) | option-d-compact-l/main_floor_d.scad:119 |
| M25 | (83.4, 49.6) x | 3 ft = 36 in | door | 1 | (suite hall) / MASTER BEDROOM | option-d-compact-l/main_floor_d.scad:120 |
| M26 | (89.4, 49.6) x | 4 ft = 48 in | open | - | WIC @88.4,41.2 / MASTER BEDROOM | option-d-compact-l/main_floor_d.scad:121 |
| M27 | (98.4, 49.6) x | 4 ft = 48 in | open | - | WIC @96.4,41.2 / MASTER BEDROOM | option-d-compact-l/main_floor_d.scad:122 |
| M28 | (75.5, 49.6) x | 3 ft = 36 in | door | -1 | LAUNDRY / MASTER BATH | option-d-compact-l/main_floor_d.scad:123 |
| M29 | (83, 56) y | 3 ft = 36 in | door | 1 | MASTER BATH / MASTER BEDROOM | option-d-compact-l/main_floor_d.scad:124 |
| M30 | (75.5, 62) x | 2.8 ft = 33.6 in | door | 1 | MASTER BATH / WC | option-d-compact-l/main_floor_d.scad:125 |
| M31 | (79.4, 62) x | 3 ft = 36 in | open | - | MASTER BATH / SHOWER | option-d-compact-l/main_floor_d.scad:126 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (82.4, 8) y | 6 ft = 72 in | open | - | LIVING ROOM / HALL @82.4,0 | option-d-compact-l/basement_d.scad:82 |
| B2 | (82.6, 21.6) x | 5.6 ft = 67.2 in | full | - | HALL @82.4,0 / HALL @82.4,21.6 | option-d-compact-l/basement_d.scad:83 |
| B3 | (82.6, 41.2) x | 5.6 ft = 67.2 in | full | - | HALL @82.4,21.6 / HALL @82.4,41.2 | option-d-compact-l/basement_d.scad:84 |
| B4 | (88.4, 12.4) y | 3 ft = 36 in | door | 1 | HALL @82.4,0 / BATH @88.4,11.6 | option-d-compact-l/basement_d.scad:85 |
| B5 | (88.4, 22.4) y | 3 ft = 36 in | door | 1 | HALL @82.4,21.6 / ELEVATOR (FUTURE) | option-d-compact-l/basement_d.scad:86 |
| B6 | (88.4, 30.5) y | 3 ft = 36 in | door | 1 | HALL @82.4,21.6 / FLEX / CRAFT | option-d-compact-l/basement_d.scad:87 |
| B7 | (95, 29) x | 3 ft = 36 in | open | - | CLOSET @94.4,21.6 / FLEX / CRAFT | option-d-compact-l/basement_d.scad:88 |
| B8 | (82.4, 22) y | 3 ft = 36 in | door | -1 | UNDER STAIR / HALL @82.4,21.6 | option-d-compact-l/basement_d.scad:89 |
| B9 | (78, 42.75) x | 4.2 ft = 50.4 in | full | - | STAIR UP / STAIR FOOT | option-d-compact-l/basement_d.scad:90 |
| B10 | (82.4, 43.5) y | 4 ft = 48 in | full | - | STAIR FOOT / HALL @82.4,41.2 | option-d-compact-l/basement_d.scad:91 |
| B11 | (77.8, 44) y | 2.8 ft = 33.6 in | door | -1 | STORAGE @74,41.2 / STAIR FOOT | option-d-compact-l/basement_d.scad:92 |
| B12 | (92.8, 43.5) y | 3 ft = 36 in | door | 1 | HALL @82.4,41.2 / BATH @92.8,41.2 | option-d-compact-l/basement_d.scad:93 |
| B13 | (101, 49.6) x | 2.8 ft = 33.6 in | door | -1 | STORAGE @100.8,41.2 / CLOSET @92.8,49.6 | option-d-compact-l/basement_d.scad:94 |
| B14 | (86.7, 49.6) x | 5.6 ft = 67.2 in | full | - | HALL @82.4,41.2 / (unlabelled hall) | option-d-compact-l/basement_d.scad:95 |
| B15 | (86.2, 60) y | 3 ft = 36 in | door | -1 | BEDROOM 4 / (unlabelled hall) | option-d-compact-l/basement_d.scad:96 |
| B16 | (92.8, 60) y | 3 ft = 36 in | door | 1 | (unlabelled hall) / BEDROOM 3 | option-d-compact-l/basement_d.scad:97 |
| B17 | (77, 57) x | 4 ft = 48 in | open | - | CLOSET @74,49.6 / BEDROOM 4 | option-d-compact-l/basement_d.scad:98 |
| B18 | (96, 57) x | 4 ft = 48 in | open | - | CLOSET @92.8,49.6 / BEDROOM 3 | option-d-compact-l/basement_d.scad:99 |
| B19 | (64, 4) y | 3 ft = 36 in | door | -1 | GYM / MUSIC / LIVING ROOM | option-d-compact-l/basement_d.scad:100 |
| B20 | (51, 4) y | 3 ft = 36 in | door | -1 | OFFICE / LIBRARY / GYM / MUSIC | option-d-compact-l/basement_d.scad:101 |
| B21 | (57, 13.6) x | 3 ft = 36 in | door | 1 | GYM / MUSIC / STORAGE @51,13.6 | option-d-compact-l/basement_d.scad:102 |
| B22 | (41, 13.6) x | 3 ft = 36 in | door | 1 | OFFICE / LIBRARY / STORAGE @35,13.6 | option-d-compact-l/basement_d.scad:103 |
| B23 | (35, 14) y | 3 ft = 36 in | door | -1 | UTILITY / STORAGE @35,13.6 | option-d-compact-l/basement_d.scad:104 |
| B24 | (35, 3) y | 3 ft = 36 in | door | -1 | STORAGE @24.4,0 / OFFICE / LIBRARY | option-d-compact-l/basement_d.scad:105 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 1 | 12 | 13 |
| double | 0 | 0 | 4 | 4 |
| open | 1 | 0 | 9 | 10 |
| full | 0 | 0 | 3 | 3 |
| garage | 0 | 0 | 1 | 1 |
| ALL | 1 | 1 | 29 | 31 |
| passage (door+double+slider+open) | 1 | 1 | 25 | 27 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 2 | 13 | 15 |
| open | 0 | 0 | 4 | 4 |
| full | 0 | 0 | 5 | 5 |
| ALL | 0 | 2 | 22 | 24 |
| passage (door+double+slider+open) | 0 | 2 | 17 | 19 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-d-compact-l/main_floor_d.scad:97 | MASTER BEDROOM / DECK | double | 72 in | - |
| option-d-compact-l/main_floor_d.scad:108 | FOYER / BATH | door | 36 in | 34.5 |
| option-d-compact-l/main_floor_d.scad:113 | HALL / ELEVATOR (FUTURE) | door | 36 in | 34.5 |
| option-d-compact-l/main_floor_d.scad:114 | HALL / BEDROOM 2 | door | 36 in | 34.5 |
| option-d-compact-l/main_floor_d.scad:115 | BR 2 CLOSET / BEDROOM 2 | open | 36 in | - |
| option-d-compact-l/main_floor_d.scad:116 | LINEN / HALL | open | 28.8 in | - |
| option-d-compact-l/main_floor_d.scad:120 | (suite hall) / MASTER BEDROOM | door | 36 in | 34.5 |
| option-d-compact-l/main_floor_d.scad:121 | WIC @88.4,41.2 / MASTER BEDROOM | open | 48 in | - |
| option-d-compact-l/main_floor_d.scad:122 | WIC @96.4,41.2 / MASTER BEDROOM | open | 48 in | - |
| option-d-compact-l/main_floor_d.scad:123 | LAUNDRY / MASTER BATH | door | 36 in | 34.5 |
| option-d-compact-l/main_floor_d.scad:124 | MASTER BATH / MASTER BEDROOM | door | 36 in | 34.5 |
| option-d-compact-l/main_floor_d.scad:125 | MASTER BATH / WC | door | 33.6 in | 32.1 |
| option-d-compact-l/main_floor_d.scad:126 | MASTER BATH / SHOWER | open | 36 in | - |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-d-compact-l/basement_d.scad:85 | HALL @82.4,0 / BATH @88.4,11.6 | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:86 | HALL @82.4,21.6 / ELEVATOR (FUTURE) | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:87 | HALL @82.4,21.6 / FLEX / CRAFT | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:88 | CLOSET @94.4,21.6 / FLEX / CRAFT | open | 36 in | - |
| option-d-compact-l/basement_d.scad:89 | UNDER STAIR / HALL @82.4,21.6 | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:92 | STORAGE @74,41.2 / STAIR FOOT | door | 33.6 in | 32.1 |
| option-d-compact-l/basement_d.scad:93 | HALL @82.4,41.2 / BATH @92.8,41.2 | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:94 | STORAGE @100.8,41.2 / CLOSET @92.8,49.6 | door | 33.6 in | 32.1 |
| option-d-compact-l/basement_d.scad:96 | BEDROOM 4 / (unlabelled hall) | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:97 | (unlabelled hall) / BEDROOM 3 | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:98 | CLOSET @74,49.6 / BEDROOM 4 | open | 48 in | - |
| option-d-compact-l/basement_d.scad:99 | CLOSET @92.8,49.6 / BEDROOM 3 | open | 48 in | - |
| option-d-compact-l/basement_d.scad:102 | GYM / MUSIC / STORAGE @51,13.6 | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:103 | OFFICE / LIBRARY / STORAGE @35,13.6 | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:104 | UTILITY / STORAGE @35,13.6 | door | 36 in | 34.5 |
| option-d-compact-l/basement_d.scad:105 | STORAGE @24.4,0 / OFFICE / LIBRARY | door | 36 in | 34.5 |

## Section 5

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| MUDROOM | S | (26, 0, 'x') | 3 | 3 | 3.5 | 10.5 | option-d-compact-l/main_floor_d.scad:131 |
| KITCHEN | S | (34.5, 0, 'x') | 5 | 3.5 | 3.5 | 17.5 | option-d-compact-l/main_floor_d.scad:132 |
| KITCHEN | N | (43.5, 21.6, 'x') | 3.5 | 3.5 | 3.5 | 12.2 | option-d-compact-l/main_floor_d.scad:133 |
| DINING + NOOK | S | (50, 0, 'x') | 3 | 2 | 5 | 15.0 | option-d-compact-l/main_floor_d.scad:134 |
| DINING + NOOK | S | (55, 0, 'x') | 6 | 2.5 | 4.5 | 27.0 | option-d-compact-l/main_floor_d.scad:135 |
| LIVING ROOM | S | (70, 0, 'x') | 10 | 2 | 6 | 60.0 | option-d-compact-l/main_floor_d.scad:136 |
| LIVING ROOM | N | (63, 21.6, 'x') | 5 | 2.5 | 5 | 25.0 | option-d-compact-l/main_floor_d.scad:137 |
| BATH | E | (96.4, 13.5, 'y') | 2.5 | 4.5 | 2.5 | 6.2 | option-d-compact-l/main_floor_d.scad:138 |
| BEDROOM 2 | E | (100.2, 31.5, 'y') | 5 | 2.5 | 5 | 25.0 | option-d-compact-l/main_floor_d.scad:139 |
| LAUNDRY | W | (74, 43.5, 'y') | 3 | 3.5 | 3.5 | 10.5 | option-d-compact-l/main_floor_d.scad:140 |
| MASTER BATH | W | (74, 53, 'y') | 3 | 4 | 3 | 9.0 | option-d-compact-l/main_floor_d.scad:141 |
| WC | N | (75.5, 69.5, 'x') | 2 | 5 | 2 | 4.0 | option-d-compact-l/main_floor_d.scad:142 |
| SHOWER | N | (79.8, 69.5, 'x') | 2.4 | 5 | 2 | 4.8 | option-d-compact-l/main_floor_d.scad:143 |
| MASTER BEDROOM | N | (84.4, 69.5, 'x') | 5 | 2.5 | 5.5 | 27.5 | option-d-compact-l/main_floor_d.scad:144 |
| MASTER BEDROOM | N | (99, 69.5, 'x') | 5 | 2.5 | 5.5 | 27.5 | option-d-compact-l/main_floor_d.scad:145 |
| MASTER BEDROOM | E | (105, 64, 'y') | 4 | 2.5 | 5.5 | 22.0 | option-d-compact-l/main_floor_d.scad:146 |

Total main-floor window glass (width x height): 303.8 sq ft (16 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 6, S: 5, E: 3, W: 2

Rooms with windows on 2+ walls (main): KITCHEN (N/S); LIVING ROOM (N/S); MASTER BEDROOM (E/N)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| PANTRY | utility | 84 |
| VESTIBULE | hall | 48 |
| FOYER | hall | 82 |
| HALL | hall | 118 |
| (stair top landing) | hall | 25 |
| LINEN | closet | 12 |
| ELEVATOR (FUTURE) | closet | 44 |
| BR 2 CLOSET | closet | 43 |
| (suite hall) | hall | 50 |
| WIC @88.4,41.2 | closet | 67 |
| WIC @96.4,41.2 | closet | 72 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| BEDROOM 4 | W | (74, 61, 'y') | 2.5 | 3 | 4 | 10.0 | foundation.scad:160 |
| BEDROOM 4 | N | (78, 69.5, 'x') | 3 | 4 | 3 | 9.0 | foundation.scad:161 |
| BEDROOM 3 | E | (105, 61, 'y') | 2.5 | 3 | 4 | 10.0 | foundation.scad:0 |
| BEDROOM 3 | N | (97, 69.5, 'x') | 3 | 4 | 3 | 9.0 | foundation.scad:0 |
| FLEX / CRAFT | E | (100.2, 33, 'y') | 2.5 | 3 | 4 | 10.0 | foundation.scad:0 |
| LIVING ROOM | S | (68, 0, 'x') | 8 | 4 | 2.5 | 20.0 | foundation.scad:0 |
| GYM / MUSIC | S | (56, 0, 'x') | 5 | 4 | 2.5 | 12.5 | foundation.scad:0 |
| OFFICE / LIBRARY | S | (40, 0, 'x') | 5 | 4 | 2.5 | 12.5 | foundation.scad:0 |

Rooms with windows on 2+ walls (basement): BEDROOM 4; BEDROOM 3

Basement rooms with no window row: STORAGE @24.4,0 (closet, 102 sf); UTILITY (utility, 127 sf); STORAGE @35,13.6 (closet, 128 sf); STORAGE @51,13.6 (closet, 104 sf); HALL @82.4,0 (hall, 130 sf); BATH @88.4,11.6 (bath, 80 sf); HALL @82.4,21.6 (hall, 118 sf); UNDER STAIR (closet, 25 sf); STAIR UP (stair, 72 sf); STAIR FOOT (hall, 32 sf); HALL @82.4,41.2 (hall, 87 sf); ELEVATOR (FUTURE) (closet, 44 sf); CLOSET @94.4,21.6 (closet, 43 sf); STORAGE @74,41.2 (closet, 32 sf); BATH @92.8,41.2 (bath, 67 sf); STORAGE @100.8,41.2 (closet, 35 sf); (unlabelled hall) (hall, 131 sf); CLOSET @74,49.6 (closet, 90 sf); CLOSET @92.8,49.6 (closet, 90 sf); WINDOW WELL @70.5,59.5 (porch, 19 sf); WINDOW WELL @105,59.5 (porch, 19 sf); WINDOW WELL @100.2,31.5 (porch, 18 sf)

## Section 6

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| HALL | 82.4,21.6 to 88.4,41.2 | 118 | 5.6 ft clear width (67 in), length 19.2 | option-d-compact-l/main_floor_d.scad:64 |
| (stair top landing) | 77.8,21.6 to 82.4,27 | 25 | 4.2 ft clear width (50 in), length 5.0 | option-d-compact-l/main_floor_d.scad:65 |
| (suite hall) | 82.4,41.2 to 88.4,49.6 | 50 | 5.6 ft clear width (67 in), length 8.0 | option-d-compact-l/main_floor_d.scad:74 |

**Circulation total (halls only): 193 sq ft = 6.9% of 2779 sq ft conditioned** (7.1% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 48 | 5.6 ft | 8.7% | option-d-compact-l/main_floor_d.scad:60 |
| MUDROOM | 97 | 8.0 ft | 12.2% (halls+foyer+mudroom) | option-d-compact-l/main_floor_d.scad:55 |
| STAIR DN opening (stairwell) | 53 | 4.2 ft | 14.1% (all four) | option-d-compact-l/main_floor_d.scad:66 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| HALL @82.4,0 | 82.4,0 to 88.4,21.6 | 130 | 5.2 ft clear width (63 in), length 20.8 | option-d-compact-l/basement_d.scad:54 |
| HALL @82.4,21.6 | 82.4,21.6 to 88.4,41.2 | 118 | 5.6 ft clear width (67 in), length 19.2 | option-d-compact-l/basement_d.scad:57 |
| STAIR FOOT | 77.8,42.75 to 82.4,49.6 | 32 | 4.2 ft clear width (50 in), length 6.5 | option-d-compact-l/basement_d.scad:60 |
| HALL @82.4,41.2 | 82.4,41.2 to 92.8,49.6 | 87 | 8.0 ft clear width (96 in), length 9.6 | option-d-compact-l/basement_d.scad:61 |
| (unlabelled hall) | 86.2,49.6 to 92.8,69.5 | 131 | 6.2 ft clear width (74 in), length 19.1 | option-d-compact-l/basement_d.scad:69 |

**Circulation total (halls only): 497 sq ft = 17.5% of 2835 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 72 | 3.8 ft | 20.1% | option-d-compact-l/basement_d.scad:59 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.

## Section 7

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): none

Basement: none

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| GARAGE | garage | DRIVE; MUDROOM; PANTRY | - |
| MUDROOM | utility | GARAGE; KITCHEN; MUD STOOP | - |
| PANTRY | utility | GARAGE; KITCHEN | - |
| KITCHEN | kitchen | DINING + NOOK; MUDROOM; PANTRY | - |
| DINING + NOOK | dining | KITCHEN; LIVING ROOM; PATIO | - |
| LIVING ROOM | living | DINING + NOOK; FOYER; PATIO | - |
| VESTIBULE | hall | FOYER; FRONT PORCH | - |
| FOYER | hall | BATH; HALL; LIVING ROOM; VESTIBULE | - |
| BATH | bath | FOYER | - |
| HALL | hall | (stair top landing); (suite hall); BEDROOM 2; ELEVATOR (FUTURE); FOYER; LINEN | - |
| (stair top landing) | hall | HALL; STAIR DN | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (stair top landing) | - |
| LINEN | closet | HALL | - |
| ELEVATOR (FUTURE) | closet | HALL | - |
| BEDROOM 2 | bed | BR 2 CLOSET; HALL | - |
| BR 2 CLOSET | closet | BEDROOM 2 | - |
| LAUNDRY | utility | (suite hall); MASTER BATH | - |
| (suite hall) | hall | HALL; LAUNDRY; MASTER BEDROOM | - |
| WIC @88.4,41.2 | closet | MASTER BEDROOM | - |
| WIC @96.4,41.2 | closet | MASTER BEDROOM | - |
| MASTER BATH | bath | LAUNDRY; MASTER BEDROOM; SHOWER; WC | - |
| WC | bath | MASTER BATH | - |
| SHOWER | bath | MASTER BATH | - |
| MASTER BEDROOM | bed | (suite hall); DECK; MASTER BATH; WIC @88.4,41.2; WIC @96.4,41.2 | - |
| DRIVE | porch, ceiling 0 (open zone) | GARAGE | - |
| MUD STOOP | porch, ceiling 0 (open zone) | MUDROOM | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | VESTIBULE | - |
| PATIO | porch, ceiling 0 (open zone) | DINING + NOOK; LIVING ROOM | - |
| DECK | porch, ceiling 0 (open zone) | MASTER BEDROOM | - |

### 7.2 Basement adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| STORAGE @24.4,0 | closet | OFFICE / LIBRARY | - |
| UTILITY | utility | STORAGE @35,13.6 | - |
| OFFICE / LIBRARY | office | GYM / MUSIC; STORAGE @24.4,0; STORAGE @35,13.6 | - |
| STORAGE @35,13.6 | closet | OFFICE / LIBRARY; UTILITY | - |
| GYM / MUSIC | rec | LIVING ROOM; OFFICE / LIBRARY; STORAGE @51,13.6 | - |
| STORAGE @51,13.6 | closet | GYM / MUSIC | - |
| LIVING ROOM | living | GYM / MUSIC; HALL @82.4,0 | - |
| HALL @82.4,0 | hall | BATH @88.4,11.6; HALL @82.4,21.6; LIVING ROOM | - |
| BATH @88.4,11.6 | bath | HALL @82.4,0 | - |
| HALL @82.4,21.6 | hall | ELEVATOR (FUTURE); FLEX / CRAFT; HALL @82.4,0; HALL @82.4,41.2; UNDER STAIR | - |
| UNDER STAIR | closet | HALL @82.4,21.6 | - |
| STAIR UP | stair | STAIR FOOT | - |
| STAIR FOOT | hall | HALL @82.4,41.2; STAIR UP; STORAGE @74,41.2 | - |
| HALL @82.4,41.2 | hall | (unlabelled hall); BATH @92.8,41.2; HALL @82.4,21.6; STAIR FOOT | - |
| ELEVATOR (FUTURE) | closet | HALL @82.4,21.6 | - |
| FLEX / CRAFT | bed | CLOSET @94.4,21.6; HALL @82.4,21.6 | - |
| CLOSET @94.4,21.6 | closet | FLEX / CRAFT | - |
| STORAGE @74,41.2 | closet | STAIR FOOT | - |
| BATH @92.8,41.2 | bath | HALL @82.4,41.2 | - |
| STORAGE @100.8,41.2 | closet | CLOSET @92.8,49.6 | - |
| (unlabelled hall) | hall | BEDROOM 3; BEDROOM 4; HALL @82.4,41.2 | - |
| BEDROOM 4 | bed | (unlabelled hall); CLOSET @74,49.6 | - |
| CLOSET @74,49.6 | closet | BEDROOM 4 | - |
| BEDROOM 3 | bed | (unlabelled hall); CLOSET @92.8,49.6 | - |
| CLOSET @92.8,49.6 | closet | BEDROOM 3; STORAGE @100.8,41.2 | - |
| WINDOW WELL @70.5,59.5 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @105,59.5 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @100.2,31.5 | porch, ceiling 0 (open zone) | - | - |

### 7.3 Daily paths

**Method:** shortest route by Dijkstra over door midpoints; each leg is the straight (Euclidean) distance between consecutive points inside one room (door midpoint to door midpoint; the first/last point is the room centre, a fixture centre, or the door/stair point named). Legs ignore furniture, so real walking length is >= these numbers. Porches/outside are never crossed.

| Path | walk ft | room sequence (innermost room each side of each door crossed) |
|---|---|---|
| front door -> kitchen/dining room centre | 60.4 | VESTIBULE > FOYER > LIVING ROOM > DINING + NOOK > KITCHEN |
| front door -> range (option-d-compact-l/main_floor_d.scad:157) | 66.0 | VESTIBULE > FOYER > LIVING ROOM > DINING + NOOK > KITCHEN |
| garage (room centre) -> kitchen/dining room centre | 30.1 | GARAGE > PANTRY > KITCHEN |
| garage (room centre) -> range | 39.2 | GARAGE > MUDROOM > KITCHEN |
| garage (room centre) -> PANTRY centre | 17.0 | GARAGE > PANTRY |
| garage (room centre) -> tall pantry cabinets in kitchen (option-d-compact-l/main_floor_d.scad:159) | 27.6 | GARAGE > PANTRY > KITCHEN |
| master bedroom centre -> WIC @88.4,41.2 centre | 14.6 | MASTER BEDROOM > WIC @88.4,41.2 |
| master bedroom centre -> WIC @96.4,41.2 centre | 16.0 | MASTER BEDROOM > WIC @96.4,41.2 |
| master bedroom centre -> LAUNDRY centre | 23.5 | MASTER BEDROOM > (suite hall) > LAUNDRY |
| BEDROOM 2 centre -> hall BATH centre | 30.6 | BEDROOM 2 > HALL > FOYER > BATH |
| BEDROOM 2 centre -> MASTER BATH centre | 34.8 | BEDROOM 2 > HALL > (suite hall) > LAUNDRY > MASTER BATH |
| BEDROOM 2 centre -> LAUNDRY centre | 25.3 | BEDROOM 2 > HALL > (suite hall) > LAUNDRY |
| foyer centre -> hall BATH centre (no powder room in model; nearest toilet room reachable from the foyer side) | 15.4 | VESTIBULE > FOYER > BATH |
| front door -> top of main stair (top nosing, (80.10, 38.5)) | 42.8 | VESTIBULE > FOYER > HALL > LINEN |
| master bedroom centre -> top of main stair (top nosing, (80.10, 38.5)) | 28.4 | MASTER BEDROOM > (suite hall) > HALL > LINEN |
| BEDROOM 2 centre -> top of main stair (top nosing, (80.10, 38.5)) | 19.3 | BEDROOM 2 > HALL > LINEN |
| basement stair foot (80.10, 27) -> UTILITY centre | 75.7 | UNDER STAIR > HALL @82.4,21.6 > HALL @82.4,0 > LIVING ROOM > GYM / MUSIC > OFFICE / LIBRARY > STORAGE @35,13.6 > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC @88.4,41.2 centre: no (via MASTER BEDROOM > WIC @88.4,41.2); WIC @96.4,41.2 centre: no (via MASTER BEDROOM > WIC @96.4,41.2)

## Section 8

### 8.1 LIVING ROOM (main; option-d-compact-l/main_floor_d.scad:59) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| DINING + NOOK | dining | 21.6 | open 72 in |
| VESTIBULE | hall | 8.0 | - |
| FOYER | hall | 13.6 | open 72 in |
| (stair top landing) | hall | 4.6 | - |
| FRONT PORCH | porch (ceil 0) | 3.4 | - |
| PATIO | porch (ceil 0) | 15.4 | double 72 in |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are LIVING ROOM. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| GYM / MUSIC | rec | 13.6 | door 36 in |
| STORAGE @51,13.6 | closet | 8.0 | - |
| HALL @82.4,0 | hall | 21.6 | open 72 in |
| UNDER STAIR | closet | 4.6 | - |

### 8.2 FOYER (option-d-compact-l/main_floor_d.scad:60) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| LIVING ROOM | living | 8.0 | - |
| FOYER | hall | 6.0 | open 57.6 in |
| FRONT PORCH | porch (ceil 0) | 6.0 | double 60 in |

### 8.3 Closets, WICs, linen, scullery/pantry, storage: exterior exposure

Pantry-like rooms: PANTRY.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | PANTRY | option-d-compact-l/main_floor_d.scad:56 | N 8.4 (yard/soil); W 10.0 (garage) |
| main | LINEN | option-d-compact-l/main_floor_d.scad:67 | W 2.7 (yard/soil) |
| main | ELEVATOR (FUTURE) | option-d-compact-l/main_floor_d.scad:68 | none |
| main | BR 2 CLOSET | option-d-compact-l/main_floor_d.scad:71 | S 3.8 (yard/soil); E 7.4 (yard/soil) |
| main | WIC @88.4,41.2 | option-d-compact-l/main_floor_d.scad:75 | none |
| main | WIC @96.4,41.2 | option-d-compact-l/main_floor_d.scad:76 | S 4.8 (yard/soil); E 8.4 (yard/soil) |
| base | STORAGE @24.4,0 | option-d-compact-l/basement_d.scad:46 | S 10.6 (yard/soil); W 9.6 (yard/soil) |
| base | STORAGE @35,13.6 | option-d-compact-l/basement_d.scad:50 | N 16.0 (yard/soil) |
| base | STORAGE @51,13.6 | option-d-compact-l/basement_d.scad:52 | N 13.0 (yard/soil) |
| base | UNDER STAIR | option-d-compact-l/basement_d.scad:58 | W 5.4 (yard/soil) |
| base | ELEVATOR (FUTURE) | option-d-compact-l/basement_d.scad:62 | none |
| base | CLOSET @94.4,21.6 | option-d-compact-l/basement_d.scad:65 | S 3.8 (yard/soil); E 7.4 (yard/soil) |
| base | STORAGE @74,41.2 | option-d-compact-l/basement_d.scad:66 | S 3.8 (yard/soil); E 0.1 (yard/soil); W 8.4 (yard/soil) |
| base | STORAGE @100.8,41.2 | option-d-compact-l/basement_d.scad:68 | S 4.2 (yard/soil); E 8.4 (yard/soil) |
| base | CLOSET @74,49.6 | option-d-compact-l/basement_d.scad:71 | W 7.4 (yard/soil) |
| base | CLOSET @92.8,49.6 | option-d-compact-l/basement_d.scad:73 | E 7.4 (yard/soil) |

Pantry/garage: PANTRY shares 10.0 ft of wall with the garage; doors between PANTRY and GARAGE: 1. The garage's doors to the house are: option-d-compact-l/main_floor_d.scad:99 (GARAGE | MUDROOM, 36 in); option-d-compact-l/main_floor_d.scad:100 (GARAGE | PANTRY, 36 in). The tall pantry cabinets (x 35.7-38.7) are 11.3 ft east of the garage wall (x 24.4): no shared wall.

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN | sink (155); dishwasher (156); range (157); fridge (158); island, no seating (160) | front door -> kitchen/dining room centre; front door -> range (option-d-compact-l/main_floor_d.scad:157); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range; garage (room centre) -> tall pantry cabinets in kitchen (option-d-compact-l/main_floor_d.scad:159) |
| LAUNDRY | stacked washer + dryer (191) | master bedroom centre -> LAUNDRY centre; BEDROOM 2 centre -> MASTER BATH centre; BEDROOM 2 centre -> LAUNDRY centre |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| GARAGE | 2.0 | west driveway (site.scad:111) | N 24.4 (yard/soil); S 24.4 (porch/patio (open)); E 2.8 (yard/soil); W 24.4 (yard/soil) |
| MUDROOM | 14.0 | loop north leg (:114) | S 4.8 (porch/patio (open)), 3.6 (yard/soil); W 11.6 (garage) |
| KITCHEN | 14.0 | loop north leg (:114) | N 12.2 (porch/patio (open)), 3.2 (yard/soil); S 15.4 (yard/soil) |
| DINING + NOOK | 14.0 | loop north leg (:114) | N 14.2 (porch/patio (open)); S 14.2 (yard/soil) |
| LIVING ROOM | 14.0 | loop north leg (:114) | N 15.4 (porch/patio (open)); S 3.4 (porch/patio (open)), 16.6 (yard/soil) |
| VESTIBULE | 14.0 | loop north leg (:114) | S 6.0 (porch/patio (open)); E 8.0 (yard/soil) |
| FOYER | 22.0 | loop north leg (:114) | E 3.6 (yard/soil) |
| PANTRY | 25.6 | loop north leg (:114) | N 8.4 (yard/soil); W 10.0 (garage) |
| BATH | 25.6 | loop north leg (:114) | S 8.0 (yard/soil); E 10.0 (yard/soil) |
| HALL | 35.6 | loop north leg (:114) | none |
| (stair top landing) | 35.6 | loop north leg (:114) | W 5.4 (porch/patio (open)) |
| ELEVATOR (FUTURE) | 35.6 | loop north leg (:114) | none |
| BR 2 CLOSET | 35.6 | loop north leg (:114) | S 3.8 (yard/soil); E 7.4 (yard/soil) |

Other rooms are > 40 ft from any drive. Garage doors (rows option-d-compact-l/main_floor_d.scad:93) face S; garage rectangle to the nearest drive piece: 2.0 ft.

## Section 9

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| sink (KITCHEN) | KITCHEN | (35.7, 0.4, 38.7, 2) | (37.2, 1.2) | S wall y=0 | 0.40 | option-d-compact-l/main_floor_d.scad:155 |
| vanity (BATH) | BATH | (88.6, 19, 92.6, 21.2) | (90.6, 20.1) | W wall x=88.4 | 0.20 | option-d-compact-l/main_floor_d.scad:178 |
| sink (BATH) | BATH | (89.2, 19.5, 91, 20.9) | (90.1, 20.2) | N wall y=21.6 | 0.70 | option-d-compact-l/main_floor_d.scad:179 |
| toilet/tub/wash basin (BATH) | BATH | (94.4, 19, 96, 21) | (95.2, 20.0) | E wall x=96.4 | 0.40 | option-d-compact-l/main_floor_d.scad:180 |
| shower (BATH) | BATH | (93, 12, 96.2, 16.5) | (94.6, 14.2) | E wall x=96.4 | 0.20 | option-d-compact-l/main_floor_d.scad:181 |
| sink (LAUNDRY) | LAUNDRY | (74.4, 44.6, 75.8, 46) | (75.1, 45.3) | W wall x=74 | 0.40 | option-d-compact-l/main_floor_d.scad:193 |
| vanity (MASTER BATH) | MASTER BATH | (74.2, 52, 76.2, 58) | (75.2, 55.0) | W wall x=74 | 0.20 | option-d-compact-l/main_floor_d.scad:196 |
| sink (MASTER BATH) | MASTER BATH | (74.4, 52.6, 76, 54) | (75.2, 53.3) | W wall x=74 | 0.40 | option-d-compact-l/main_floor_d.scad:197 |
| sink (MASTER BATH) | MASTER BATH | (74.4, 56, 76, 57.4) | (75.2, 56.7) | W wall x=74 | 0.40 | option-d-compact-l/main_floor_d.scad:198 |
| toilet/tub/wash basin (WC) | WC | (76, 66.9, 77.8, 69.1) | (76.9, 68.0) | N wall y=69.5 | 0.40 | option-d-compact-l/main_floor_d.scad:200 |
| shower (SHOWER) | SHOWER | (79, 62.4, 82.8, 69.1) | (80.9, 65.8) | E wall x=83 | 0.20 | option-d-compact-l/main_floor_d.scad:201 |

(equipment list omitted in variant mode)

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| vanity (BATH @88.4,11.6) | BATH @88.4,11.6 | (88.6, 19, 92.6, 21.2) | (90.6, 20.1) | W wall x=88.4 | 0.20 | option-d-compact-l/basement_d.scad:130 |
| toilet/tub/wash basin (BATH @88.4,11.6) | BATH @88.4,11.6 | (94.4, 19, 96, 21) | (95.2, 20.0) | E wall x=96.4 | 0.40 | option-d-compact-l/basement_d.scad:131 |
| shower (BATH @88.4,11.6) | BATH @88.4,11.6 | (93, 12, 96.2, 16.5) | (94.6, 14.2) | E wall x=96.4 | 0.20 | option-d-compact-l/basement_d.scad:132 |
| shower (BATH @92.8,41.2) | BATH @92.8,41.2 | (93, 42.4, 96, 45.4) | (94.5, 43.9) | W wall x=92.8 | 0.20 | option-d-compact-l/basement_d.scad:134 |
| vanity (BATH @92.8,41.2) | BATH @92.8,41.2 | (97.4, 42, 100.6, 44) | (99.0, 43.0) | E wall x=100.8 | 0.20 | option-d-compact-l/basement_d.scad:135 |
| toilet/tub/wash basin (BATH @92.8,41.2) | BATH @92.8,41.2 | (98.4, 46.2, 100, 48.2) | (99.2, 47.2) | E wall x=100.8 | 0.80 | option-d-compact-l/basement_d.scad:136 |

(equipment list omitted in variant mode)

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | sink (KITCHEN) | KITCHEN | y=0 (horizontal wall) | (37.2, 1.2) |
| G2 | toilet/tub/wash basin (BATH); shower (BATH) | BATH | x=96.4 (vertical wall) | (94.9, 17.1) |
| G3 | vanity (BATH) | BATH | x=88.4 (vertical wall) | (90.6, 20.1) |
| G4 | sink (BATH) | BATH | y=21.6 (horizontal wall) | (90.1, 20.2) |
| G5 | sink (LAUNDRY); vanity (MASTER BATH); sink (MASTER BATH); sink (MASTER BATH) | LAUNDRY; MASTER BATH | x=74 (vertical wall) | (75.2, 52.6) |
| G6 | shower (SHOWER) | SHOWER | x=83 (vertical wall) | (80.9, 65.8) |
| G7 | toilet/tub/wash basin (WC) | WC | y=69.5 (horizontal wall) | (76.9, 68.0) |

**Main floor: 7 wet-wall groups** (3 back-to-back plumbing clusters of rooms: KITCHEN | BATH | LAUNDRY+MASTER BATH+WC+SHOWER)

Basement:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | toilet/tub/wash basin (BATH @88.4,11.6); shower (BATH @88.4,11.6) | BATH @88.4,11.6 | x=96.4 (vertical wall) | (94.9, 17.1) |
| G2 | vanity (BATH @88.4,11.6) | BATH @88.4,11.6 | x=88.4 (vertical wall) | (90.6, 20.1) |
| G3 | vanity (BATH @92.8,41.2); toilet/tub/wash basin (BATH @92.8,41.2) | BATH @92.8,41.2 | x=100.8 (vertical wall) | (99.1, 45.1) |
| G4 | shower (BATH @92.8,41.2) | BATH @92.8,41.2 | x=92.8 (vertical wall) | (94.5, 43.9) |

**Basement: 4 wet-wall groups** (2 clusters: BATH @88.4,11.6 | BATH @92.8,41.2)

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 8/4; 6 ft: 7/4; 8 ft: 7/4; 12 ft: 7/4; inf: 7/4

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | sink (KITCHEN) | (37.2,1.2) | B2 (BATH @88.4,11.6) | (90.6,20.1) | 53.4 | 18.9 | 72.3 |
| G2 | toilet/tub/wash basin (BATH); shower (BATH) | (94.9,17.1) | B1 (BATH @88.4,11.6) | (94.9,17.1) | 0.0 | 0.0 | 0.0 |
| G3 | vanity (BATH) | (90.6,20.1) | B2 (BATH @88.4,11.6) | (90.6,20.1) | 0.0 | 0.0 | 0.0 |
| G4 | sink (BATH) | (90.1,20.2) | B2 (BATH @88.4,11.6) | (90.6,20.1) | 0.5 | 0.1 | 0.6 |
| G5 | sink (LAUNDRY); vanity (MASTER BATH); sink (MASTER BATH)... | (75.2,52.6) | B4 (BATH @92.8,41.2) | (94.5,43.9) | 19.3 | 8.7 | 28.0 |
| G6 | shower (SHOWER) | (80.9,65.8) | B4 (BATH @92.8,41.2) | (94.5,43.9) | 13.6 | 21.9 | 35.4 |
| G7 | toilet/tub/wash basin (WC) | (76.9,68.0) | B4 (BATH @92.8,41.2) | (94.5,43.9) | 17.6 | 24.1 | 41.7 |

Main-floor groups with a basement group within 5 ft Manhattan: 3 of 7; within 10 ft: 3.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (37.2,1.2) | 71.8 | 52.7 |
| G2 | (94.9,17.1) | 113.6 | 94.5 |
| G3 | (90.6,20.1) | 106.3 | 87.2 |
| G4 | (90.1,20.2) | 105.7 | 86.6 |
| G5 | (75.2,52.6) | 58.4 | 66.7 |
| G6 | (80.9,65.8) | 66.5 | 85.6 |
| G7 | (76.9,68.0) | 64.7 | 83.8 |

**DRI (E = (22.16, 58)) = 587.2 ft over 7 groups; mean 83.9 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 557.3 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:125, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:124). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **shower (SHOWER), 94.7 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: shower (SHOWER), 96.7 ft.
- Furthest basement fixture: **toilet/tub/wash basin (BATH @92.8,41.2), 94.4 ft** from the water heater.
- Nearest main-floor fixture: sink (KITCHEN), 24.0 ft.

Per fixture (Manhattan plan ft from the water heater): sink (KITCHEN) 24; vanity (BATH) 59; sink (BATH) 58; toilet/tub/wash basin (BATH) 63; shower (BATH) 68; sink (LAUNDRY) 68; vanity (MASTER BATH) 78; sink (MASTER BATH) 76; sink (MASTER BATH) 80; toilet/tub/wash basin (WC) 93; shower (SHOWER) 95; vanity (BATH @88.4,11.6) 59; toilet/tub/wash basin (BATH @88.4,11.6) 63; shower (BATH @88.4,11.6) 68; shower (BATH @92.8,41.2) 86; vanity (BATH @92.8,41.2) 90; toilet/tub/wash basin (BATH @92.8,41.2) 94

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
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | option-d-compact-l/main_floor_d.scad:66 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | option-d-compact-l/basement_d.scad:59 |
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
| Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27) | 37.2 ft (11.3 m) |
| Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6) | 19.16 ft (5.8 m) / 18.61 ft |
| Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner | 21.3 ft (6.5 m) |
| Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour | 19.2 ft (5.8 m) |
| Septic tank to well | 147.4 ft (44.9 m) |
| Pump chamber to well | 147.2 ft (44.9 m) |
| Treatment field to well | 215.0 ft (65.5 m) |
| Reserve field to well | 217.8 ft (66.4 m) |
| Treatment field to the basement (outline polygon) | 87.2 ft (26.6 m) |
| Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27) | 92.4 ft (28.2 m) |
| Treatment field to the garage west wall (x=0, slab, no basement) | 65.7 ft (20.0 m) |
| Reserve field to basement | 87.2 ft (26.6 m) |
| Reserve field to the nearest heated wall | 89.4 ft (27.2 m) |
| Reserve field to the garage | 65.0 ft (19.8 m) |
| Treatment field to west driveway edge (x=-32) | 33.1 ft (10.1 m) |
| Reserve field to west driveway edge | 33.0 ft (10.1 m) |
| Treatment field to the service-line corridor (x=-47..-41) | 18.0 ft (5.5 m) |
| Reserve field to the service-line corridor | 18.0 ft (5.5 m) |
| Reserve field to propane pad (-68..-52, -48..-42) | 27.0 ft (8.2 m) |
| Well to heated main-floor wall (nearest) | 45.3 ft (13.8 m) |
| Well to side porch/deck edge (nearest unconditioned main-floor row) | 37.7 ft (11.5 m) |
| Well to basement outline | 57.4 ft (17.5 m) |
| House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130) | 60.5 ft (18.4 m) |
| House incl. porches/deck to future shop | 60.5 ft (18.4 m) |
| Basement exit areaway (y 67.75) to shop | 62.3 ft (19.0 m) |
| Garage to shop (garage north wall 35.46) | 94.5 ft (28.8 m) |

Corridor and drive lengths: power run road->meter wall 197.3 ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas 202.3 ft; fibre 192.3 ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: 53.0 ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).

West driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).

phase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.

Phase house: parents' house and geothermal loop field are not in site.scad (§13).

