# Plan facts (variant mode)

main = `/home/user/house-review/docs/layout-options/round-2/option-e-linear-ranch/main_floor_e.scad`, basement = `/home/user/house-review/docs/layout-options/round-2/option-e-linear-ranch/basement_e.scad`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.

## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-2/option-e-linear-ranch/main_floor_e.scad`; basement = `/home/user/house-review/docs/layout-options/round-2/option-e-linear-ranch/basement_e.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 2,828 | 2827.5; excl. stair opening 2774.6 |
| Building area, centre lines (house + attached garage) | 322.9 m2 | 3476 sq ft |
| Building area, outside face | 335.6 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 2,940 sq ft | centre lines 2,828 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 2,940 sq ft | centre lines 2,828 sq ft |
| Circulation % (strict / with foyer) | 10.1% / 11.9% | 284 sq ft strict of 2828 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 19 | type `door` rows, by opening width |
| Double / open counts (main) | 2 / 0 | type `double` / type `open` |
| Minimum hall clear width | 5.10 ft ((private hall)) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 4.20 ft ((stair-top landing)) |
| Wet-wall groups (main / basement) | 8 / 3 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 1 of 8 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 667.1 ft | alternate exit (22.16, 38.9): 514.3 ft |
| Water heater -> furthest fixture (main / basement) | 83.9 ft (shower (BATH)) / 51.3 ft (shower (JACK & JILL BATH)) | water heater at (25.7, 29.6); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 30.0 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 0 of 3:  | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 9.0 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(yard 14.5) E(yard 11.5) ;; MASTER BEDROOM: N(yard 20.0) E(porch/patio 16.0, yard 3.5) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 38.0) E(porch/patio 16.0, yard 3.5) | suite rooms: WIC @61.5,19.5, WIC @69,19.5, WC, MASTER BATH, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING (18.5 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 3: BEDROOM 2 (E/S); KITCHEN (N/W); MASTER BEDROOM (E/N) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 42..53.5, y 39; basement foot room x 37.5..53.5, y 34.4; **moved** (x offset +4.50/+0.00 ft, run 4.600 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 14.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_e.scad (defaults): 28 rooms, 33 doors, 16 windows - OK ; basement_e.scad (defaults): 22 rooms, 18 doors, 7 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |

## Section 1

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 2827.5 | computed: sum (x1-x0)*(y1-y0) over 23 rows, main_floor.scad:41-71 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 52.9 | option-e-linear-ranch/main_floor_e.scad:57 |
| Main-floor conditioned excluding the stair opening | 2774.6 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 2827.5 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 2955.2 | computed over basement.scad:38-63 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 648.0 | option-e-linear-ranch/main_floor_e.scad:41 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| PATIO | 168.0 | option-e-linear-ranch/main_floor_e.scad:68 |
| FRONT PORCH | 420.0 | option-e-linear-ranch/main_floor_e.scad:69 |
| DRIVE (SLOPES UP TO GARAGE) | 384.0 | option-e-linear-ranch/main_floor_e.scad:70 |
| DECK | 184.0 | option-e-linear-ranch/main_floor_e.scad:71 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 1156.0 sq ft. PATIO alone: 168.0; DECK alone: 184.0. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 223.0 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 131.0 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 65.0 ft | same |
|   facing garage | 27.0 ft | same (garage is unheated) |
| Outside (convex) corners | 4 | vertices of the union polygon after 0.02 ft simplify (4 vertices) |
| Inside (reflex) corners | 0 | same polygon |
| Bounding box, heated rooms | x 24..96.5 (72.5 ft), y 0..39 (39 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 0..108 (108 ft), y -16..39 (55 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 4 hip-roof blocks in main_roof (main_floor.scad:225); each hip block is 4 sloped facets, so 4 x 4 = 16 nominal facets before overlapping blocks merge; 0 blocks at 6/12 pitch, 4 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)

## Section 2

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| MUDROOM | S 9.0 (yard/soil); W 10.5 (garage) | option-e-linear-ranch/main_floor_e.scad:43 |
| PANTRY | W 9.0 (garage) | option-e-linear-ranch/main_floor_e.scad:44 |
| DINING / NOOK | S 14.0 (porch/patio (open)) | option-e-linear-ranch/main_floor_e.scad:45 |
| LIVING | S 18.5 (porch/patio (open)) | option-e-linear-ranch/main_floor_e.scad:46 |
| VESTIBULE | S 6.5 (porch/patio (open)) | option-e-linear-ranch/main_floor_e.scad:47 |
| POWDER | S 4.5 (porch/patio (open)) | option-e-linear-ranch/main_floor_e.scad:48 |
| FOYER | none | option-e-linear-ranch/main_floor_e.scad:49 |
| (private hall) | S 5.5 (porch/patio (open)) | option-e-linear-ranch/main_floor_e.scad:50 |
| BEDROOM 2 | S 14.5 (yard/soil); E 11.5 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:51 |
| BATH | E 8.0 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:52 |
| KITCHEN | N 18.0 (yard/soil); W 7.5 (garage), 12.0 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:54 |
| (kitchen to hub passage) | none | option-e-linear-ranch/main_floor_e.scad:55 |
| ELEVATOR (FUTURE) | none | option-e-linear-ranch/main_floor_e.scad:56 |
| STAIR DN | N 11.5 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:57 |
| (gallery) | none | option-e-linear-ranch/main_floor_e.scad:58 |
| (gallery, east) | none | option-e-linear-ranch/main_floor_e.scad:59 |
| (stair-top landing) | N 5.0 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:60 |
| LAUNDRY | none | option-e-linear-ranch/main_floor_e.scad:61 |
| WIC @61.5,19.5 | none | option-e-linear-ranch/main_floor_e.scad:62 |
| WIC @69,19.5 | none | option-e-linear-ranch/main_floor_e.scad:63 |
| WC | N 5.5 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:64 |
| MASTER BATH | N 12.5 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:65 |
| MASTER BEDROOM | N 20.0 (yard/soil); E 16.0 (porch/patio (open)), 3.5 (yard/soil) | option-e-linear-ranch/main_floor_e.scad:66 |

## Section 3

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MUDROOM | 24 | 0 | 33 | 10.5 | 9.00 x 10.50 | 8.6 x 10.1 | 94 | 87 | 1.17 | utility | 10 | option-e-linear-ranch/main_floor_e.scad:43 |
| PANTRY | 24 | 10.5 | 33 | 19.5 | 9.00 x 9.00 | 8.6 x 8.6 | 81 | 74 | 1.00 | utility | 10 | option-e-linear-ranch/main_floor_e.scad:44 |
| DINING / NOOK | 33 | 0 | 47 | 19.5 | 14.00 x 19.50 | 13.6 x 19.1 | 273 | 260 | 1.39 | dining | 10 | option-e-linear-ranch/main_floor_e.scad:45 |
| LIVING | 47 | 0 | 65.5 | 19.5 | 18.50 x 19.50 | 18.1 x 19.1 | 361 | 346 | 1.05 | living | 10 | option-e-linear-ranch/main_floor_e.scad:46 |
| VESTIBULE | 65.5 | 0 | 72 | 8 | 6.50 x 8.00 | 6.1 x 7.6 | 52 | 46 | 1.23 | hall | 10 | option-e-linear-ranch/main_floor_e.scad:47 |
| POWDER | 72 | 0 | 76.5 | 8 | 4.50 x 8.00 | 4.1 x 7.6 | 36 | 31 | 1.78 | bath | 10 | option-e-linear-ranch/main_floor_e.scad:48 |
| FOYER | 65.5 | 8 | 76.5 | 19.5 | 11.00 x 11.50 | 10.6 x 11.1 | 126 | 118 | 1.05 | hall | 10 | option-e-linear-ranch/main_floor_e.scad:49 |
| (private hall) | 76.5 | 0 | 82 | 19.5 | 5.50 x 19.50 | 5.1 x 19.1 | 107 | 97 | 3.55 | hall | 10 | option-e-linear-ranch/main_floor_e.scad:50 |
| BEDROOM 2 | 82 | 0 | 96.5 | 11.5 | 14.50 x 11.50 | 14.1 x 11.1 | 167 | 157 | 1.26 | bed | 10 | option-e-linear-ranch/main_floor_e.scad:51 |
| BATH | 82 | 11.5 | 96.5 | 19.5 | 14.50 x 8.00 | 14.1 x 7.6 | 116 | 107 | 1.81 | bath | 10 | option-e-linear-ranch/main_floor_e.scad:52 |
| KITCHEN | 24 | 19.5 | 42 | 39 | 18.00 x 19.50 | 17.6 x 19.1 | 351 | 336 | 1.08 | kitchen | 10 | option-e-linear-ranch/main_floor_e.scad:54 |
| (kitchen to hub passage) | 42 | 19.5 | 48 | 27 | 6.00 x 7.50 | 5.6 x 7.1 | 45 | 40 | 1.25 | hall | 10 | option-e-linear-ranch/main_floor_e.scad:55 |
| ELEVATOR (FUTURE) | 42 | 27 | 48 | 34.4 | 6.00 x 7.40 | 5.6 x 7.0 | 44 | 39 | 1.23 | closet | 10 | option-e-linear-ranch/main_floor_e.scad:56 |
| STAIR DN | 42 | 34.4 | 53.5 | 39 | 11.50 x 4.60 | 11.1 x 4.2 | 53 | - | 2.50 | stairwell | 0 | option-e-linear-ranch/main_floor_e.scad:57 |
| (gallery) | 48 | 19.5 | 53.5 | 34.4 | 5.50 x 14.90 | 5.1 x 14.5 | 82 | 74 | 2.71 | hall | 10 | option-e-linear-ranch/main_floor_e.scad:58 |
| (gallery, east) | 53.5 | 29 | 58.5 | 34.4 | 5.00 x 5.40 | 4.6 x 5.0 | 27 | 23 | 1.08 | hall | 10 | option-e-linear-ranch/main_floor_e.scad:59 |
| (stair-top landing) | 53.5 | 34.4 | 58.5 | 39 | 5.00 x 4.60 | 4.6 x 4.2 | 23 | 19 | 1.09 | hall | 10 | option-e-linear-ranch/main_floor_e.scad:60 |
| LAUNDRY | 53.5 | 19.5 | 61.5 | 29 | 8.00 x 9.50 | 7.6 x 9.1 | 76 | 69 | 1.19 | utility | 10 | option-e-linear-ranch/main_floor_e.scad:61 |
| WIC @61.5,19.5 | 61.5 | 19.5 | 69 | 29 | 7.50 x 9.50 | 7.1 x 9.1 | 71 | 65 | 1.27 | closet | 10 | option-e-linear-ranch/main_floor_e.scad:62 |
| WIC @69,19.5 | 69 | 19.5 | 76.5 | 29 | 7.50 x 9.50 | 7.1 x 9.1 | 71 | 65 | 1.27 | closet | 10 | option-e-linear-ranch/main_floor_e.scad:63 |
| WC | 58.5 | 29 | 64 | 39 | 5.50 x 10.00 | 5.1 x 9.6 | 55 | 49 | 1.82 | bath | 10 | option-e-linear-ranch/main_floor_e.scad:64 |
| MASTER BATH | 64 | 29 | 76.5 | 39 | 12.50 x 10.00 | 12.1 x 9.6 | 125 | 116 | 1.25 | bath | 10 | option-e-linear-ranch/main_floor_e.scad:65 |
| MASTER BEDROOM | 76.5 | 19.5 | 96.5 | 39 | 20.00 x 19.50 | 19.6 x 19.1 | 390 | 374 | 1.03 | bed | 10 | option-e-linear-ranch/main_floor_e.scad:66 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 0 | 0 | 24 | 27 | 24.00 x 27.00 | 23.6 x 26.6 | 648 | 628 | 1.12 | garage | 10 | option-e-linear-ranch/main_floor_e.scad:41 |
| PATIO | 33 | -12 | 47 | 0 | 14.00 x 12.00 | 14.0 x 12.0 (open) | 168 | - | 1.17 | porch | 0 | option-e-linear-ranch/main_floor_e.scad:68 |
| FRONT PORCH | 47 | -12 | 82 | 0 | 35.00 x 12.00 | 35.0 x 12.0 (open) | 420 | - | 2.92 | porch | 0 | option-e-linear-ranch/main_floor_e.scad:69 |
| DRIVE (SLOPES UP TO GARAGE) | 0 | -16 | 24 | 0 | 24.00 x 16.00 | 24.0 x 16.0 (open) | 384 | - | 1.50 | porch | 0 | option-e-linear-ranch/main_floor_e.scad:70 |
| DECK | 96.5 | 21 | 108 | 37 | 11.50 x 16.00 | 11.5 x 16.0 (open) | 184 | - | 1.39 | porch | 0 | option-e-linear-ranch/main_floor_e.scad:71 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STORAGE @24,0 | 24 | 0 | 37.5 | 19.5 | 13.50 x 19.50 | 12.7 x 18.7 | 263 | 239 | 1.44 | closet | 10 | option-e-linear-ranch/basement_e.scad:38 |
| UTILITY | 24 | 19.5 | 32 | 39 | 8.00 x 19.50 | 7.2 x 18.7 | 156 | 136 | 2.44 | utility | 10 | option-e-linear-ranch/basement_e.scad:39 |
| (landing at the stair foot) | 32 | 19.5 | 37.5 | 39 | 5.50 x 19.50 | 5.1 x 18.7 | 107 | 96 | 3.55 | hall | 10 | option-e-linear-ranch/basement_e.scad:40 |
| (hall, elevator approach) | 37.5 | 19.5 | 53.5 | 27 | 16.00 x 7.50 | 15.6 x 7.1 | 120 | 111 | 2.13 | hall | 10 | option-e-linear-ranch/basement_e.scad:42 |
| STORAGE @37.5,27 | 37.5 | 27 | 42 | 34.4 | 4.50 x 7.40 | 4.1 x 7.0 | 33 | 29 | 1.64 | closet | 10 | option-e-linear-ranch/basement_e.scad:43 |
| ELEVATOR (FUTURE) | 42 | 27 | 48 | 34.4 | 6.00 x 7.40 | 5.6 x 7.0 | 44 | 39 | 1.23 | closet | 10 | option-e-linear-ranch/basement_e.scad:44 |
| STORAGE @48,27 | 48 | 27 | 53.5 | 34.4 | 5.50 x 7.40 | 5.1 x 7.0 | 41 | 36 | 1.35 | closet | 10 | option-e-linear-ranch/basement_e.scad:45 |
| STAIR UP | 37.5 | 34.4 | 53.5 | 39 | 16.00 x 4.60 | 15.6 x 3.8 | 74 | 60 | 3.48 | stair | 10 | option-e-linear-ranch/basement_e.scad:46 |
| (east hall) | 53.5 | 19.5 | 96.5 | 25 | 43.00 x 5.50 | 42.2 x 5.1 | 236 | 215 | 7.82 | hall | 10 | option-e-linear-ranch/basement_e.scad:47 |
| BEDROOM 3 | 53.5 | 25 | 65.5 | 39 | 12.00 x 14.00 | 11.6 x 13.2 | 168 | 154 | 1.17 | bed | 10 | option-e-linear-ranch/basement_e.scad:49 |
| JACK & JILL BATH | 65.5 | 25 | 73.5 | 39 | 8.00 x 14.00 | 7.6 x 13.2 | 112 | 101 | 1.75 | bath | 10 | option-e-linear-ranch/basement_e.scad:50 |
| BEDROOM 4 | 73.5 | 25 | 85.5 | 39 | 12.00 x 14.00 | 11.6 x 13.2 | 168 | 154 | 1.17 | bed | 10 | option-e-linear-ranch/basement_e.scad:51 |
| FLEX / CRAFT | 85.5 | 25 | 96.5 | 39 | 11.00 x 14.00 | 10.2 x 13.2 | 154 | 136 | 1.27 | office | 10 | option-e-linear-ranch/basement_e.scad:52 |
| OFFICE | 37.5 | 0 | 49.5 | 19.5 | 12.00 x 19.50 | 11.6 x 18.7 | 234 | 217 | 1.62 | office | 10 | option-e-linear-ranch/basement_e.scad:54 |
| LIVING ROOM | 49.5 | 0 | 69.5 | 19.5 | 20.00 x 19.50 | 19.6 x 18.7 | 390 | 367 | 1.03 | living | 10 | option-e-linear-ranch/basement_e.scad:55 |
| THEATRE | 69.5 | 0 | 83.5 | 19.5 | 14.00 x 19.50 | 13.6 x 18.7 | 273 | 255 | 1.39 | rec | 10 | option-e-linear-ranch/basement_e.scad:56 |
| GYM / MUSIC | 83.5 | 0 | 96.5 | 19.5 | 13.00 x 19.50 | 12.2 x 18.7 | 254 | 230 | 1.50 | rec | 10 | option-e-linear-ranch/basement_e.scad:57 |
| WINDOW WELL @55,39 | 55 | 39 | 61.5 | 42.5 | 6.50 x 3.50 | 6.5 x 3.5 (open) | 23 | - | 1.86 | porch | 0 | option-e-linear-ranch/basement_e.scad:59 |
| WINDOW WELL @75,39 | 75 | 39 | 81.5 | 42.5 | 6.50 x 3.50 | 6.5 x 3.5 (open) | 23 | - | 1.86 | porch | 0 | option-e-linear-ranch/basement_e.scad:60 |
| WINDOW WELL @88,39 | 88 | 39 | 94.5 | 42.5 | 6.50 x 3.50 | 6.5 x 3.5 (open) | 23 | - | 1.86 | porch | 0 | option-e-linear-ranch/basement_e.scad:61 |
| WINDOW WELL @40,-3.5 | 40 | -3.5 | 46.5 | 0 | 6.50 x 3.50 | 6.5 x 3.5 (open) | 23 | - | 1.86 | porch | 0 | option-e-linear-ranch/basement_e.scad:62 |
| WINDOW WELL @54,-3.5 | 54 | -3.5 | 64.5 | 0 | 10.50 x 3.50 | 10.5 x 3.5 (open) | 37 | - | 3.00 | porch | 0 | option-e-linear-ranch/basement_e.scad:63 |

## Section 4

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (1.5, 0) x | 9 ft = 108 in | garage | - | DRIVE (SLOPES UP TO GARAGE) / GARAGE | option-e-linear-ranch/main_floor_e.scad:77 |
| M2 | (12.5, 0) x | 9 ft = 108 in | garage | - | DRIVE (SLOPES UP TO GARAGE) / GARAGE | option-e-linear-ranch/main_floor_e.scad:78 |
| M3 | (67, 0) x | 3.5 ft = 42 in | door | 1 | FRONT PORCH / VESTIBULE | option-e-linear-ranch/main_floor_e.scad:79 |
| M4 | (40.5, 0) x | 6 ft = 72 in | double | -1 | PATIO / DINING / NOOK | option-e-linear-ranch/main_floor_e.scad:80 |
| M5 | (96.5, 27) y | 6 ft = 72 in | double | 1 | MASTER BEDROOM / DECK | option-e-linear-ranch/main_floor_e.scad:81 |
| M6 | (24, 3) y | 3 ft = 36 in | door | 1 | GARAGE / MUDROOM | option-e-linear-ranch/main_floor_e.scad:83 |
| M7 | (24, 12.5) y | 3 ft = 36 in | door | 1 | GARAGE / PANTRY | option-e-linear-ranch/main_floor_e.scad:84 |
| M8 | (26, 10.5) x | 3 ft = 36 in | door | -1 | MUDROOM / PANTRY | option-e-linear-ranch/main_floor_e.scad:85 |
| M9 | (29, 19.5) x | 3 ft = 36 in | door | 1 | PANTRY / KITCHEN | option-e-linear-ranch/main_floor_e.scad:86 |
| M10 | (33, 3) y | 3 ft = 36 in | door | 1 | MUDROOM / DINING / NOOK | option-e-linear-ranch/main_floor_e.scad:87 |
| M11 | (34, 19.5) x | 8 ft = 96 in | full | - | DINING / NOOK / KITCHEN | option-e-linear-ranch/main_floor_e.scad:89 |
| M12 | (47, 2) y | 15 ft = 180 in | full | - | DINING / NOOK / LIVING | option-e-linear-ranch/main_floor_e.scad:90 |
| M13 | (42, 20.5) y | 5.5 ft = 66 in | full | - | KITCHEN / (kitchen to hub passage) | option-e-linear-ranch/main_floor_e.scad:91 |
| M14 | (48, 19.8) y | 6.5 ft = 78 in | full | - | (kitchen to hub passage) / (gallery) | option-e-linear-ranch/main_floor_e.scad:92 |
| M15 | (48.2, 19.5) x | 5.1 ft = 61.2 in | full | - | LIVING / (gallery) | option-e-linear-ranch/main_floor_e.scad:93 |
| M16 | (48, 28.2) y | 3 ft = 36 in | door | 1 | ELEVATOR (FUTURE) / (gallery) | option-e-linear-ranch/main_floor_e.scad:95 |
| M17 | (53.5, 34.7) y | 4.3 ft = 51.6 in | full | - | STAIR DN / (stair-top landing) | option-e-linear-ranch/main_floor_e.scad:96 |
| M18 | (53.5, 29.3) y | 4.8 ft = 57.6 in | full | - | (gallery) / (gallery, east) | option-e-linear-ranch/main_floor_e.scad:97 |
| M19 | (53.5, 34.4) x | 5 ft = 60 in | full | - | (gallery, east) / (stair-top landing) | option-e-linear-ranch/main_floor_e.scad:98 |
| M20 | (54.5, 29) x | 3 ft = 36 in | door | -1 | LAUNDRY / (gallery, east) | option-e-linear-ranch/main_floor_e.scad:99 |
| M21 | (67.5, 8) x | 3 ft = 36 in | door | 1 | VESTIBULE / FOYER | option-e-linear-ranch/main_floor_e.scad:101 |
| M22 | (72.8, 8) x | 3 ft = 36 in | door | 1 | POWDER / FOYER | option-e-linear-ranch/main_floor_e.scad:102 |
| M23 | (65.5, 10) y | 6 ft = 72 in | full | - | LIVING / FOYER | option-e-linear-ranch/main_floor_e.scad:103 |
| M24 | (76.5, 9) y | 5 ft = 60 in | full | - | FOYER / (private hall) | option-e-linear-ranch/main_floor_e.scad:104 |
| M25 | (82, 3) y | 3 ft = 36 in | door | 1 | (private hall) / BEDROOM 2 | option-e-linear-ranch/main_floor_e.scad:106 |
| M26 | (82, 14) y | 3 ft = 36 in | door | 1 | (private hall) / BATH | option-e-linear-ranch/main_floor_e.scad:107 |
| M27 | (78.5, 19.5) x | 3 ft = 36 in | door | 1 | (private hall) / MASTER BEDROOM | option-e-linear-ranch/main_floor_e.scad:108 |
| M28 | (61.5, 22) y | 3 ft = 36 in | door | -1 | LAUNDRY / WIC @61.5,19.5 | option-e-linear-ranch/main_floor_e.scad:110 |
| M29 | (69, 22) y | 3 ft = 36 in | door | 1 | WIC @61.5,19.5 / WIC @69,19.5 | option-e-linear-ranch/main_floor_e.scad:111 |
| M30 | (76.5, 24) y | 3 ft = 36 in | door | 1 | WIC @69,19.5 / MASTER BEDROOM | option-e-linear-ranch/main_floor_e.scad:112 |
| M31 | (64.5, 29) x | 3 ft = 36 in | door | -1 | WIC @61.5,19.5 / MASTER BATH | option-e-linear-ranch/main_floor_e.scad:113 |
| M32 | (64, 33) y | 3 ft = 36 in | door | -1 | WC / MASTER BATH | option-e-linear-ranch/main_floor_e.scad:114 |
| M33 | (76.5, 31) y | 3 ft = 36 in | door | 1 | MASTER BATH / MASTER BEDROOM | option-e-linear-ranch/main_floor_e.scad:115 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (33.5, 19.5) x | 3 ft = 36 in | door | -1 | STORAGE @24,0 / (landing at the stair foot) | option-e-linear-ranch/basement_e.scad:68 |
| B2 | (32, 22) y | 3 ft = 36 in | door | -1 | UTILITY / (landing at the stair foot) | option-e-linear-ranch/basement_e.scad:69 |
| B3 | (37.5, 20) y | 6.5 ft = 78 in | full | - | (landing at the stair foot) / (hall, elevator approach) | option-e-linear-ranch/basement_e.scad:70 |
| B4 | (37.5, 34.7) y | 4.3 ft = 51.6 in | full | - | (landing at the stair foot) / STAIR UP | option-e-linear-ranch/basement_e.scad:71 |
| B5 | (38, 27) x | 3 ft = 36 in | door | -1 | (hall, elevator approach) / STORAGE @37.5,27 | option-e-linear-ranch/basement_e.scad:72 |
| B6 | (42.5, 27) x | 3 ft = 36 in | door | -1 | (hall, elevator approach) / ELEVATOR (FUTURE) | option-e-linear-ranch/basement_e.scad:73 |
| B7 | (49, 27) x | 3 ft = 36 in | door | -1 | (hall, elevator approach) / STORAGE @48,27 | option-e-linear-ranch/basement_e.scad:74 |
| B8 | (53.5, 19.8) y | 5 ft = 60 in | full | - | (hall, elevator approach) / (east hall) | option-e-linear-ranch/basement_e.scad:75 |
| B9 | (38.5, 19.5) x | 3 ft = 36 in | door | -1 | OFFICE / (hall, elevator approach) | option-e-linear-ranch/basement_e.scad:76 |
| B10 | (56, 19.5) x | 8 ft = 96 in | open | - | LIVING ROOM / (east hall) | option-e-linear-ranch/basement_e.scad:77 |
| B11 | (72, 19.5) x | 3 ft = 36 in | door | -1 | THEATRE / (east hall) | option-e-linear-ranch/basement_e.scad:78 |
| B12 | (86, 19.5) x | 3 ft = 36 in | door | -1 | GYM / MUSIC / (east hall) | option-e-linear-ranch/basement_e.scad:79 |
| B13 | (54.5, 25) x | 3 ft = 36 in | door | 1 | (east hall) / BEDROOM 3 | option-e-linear-ranch/basement_e.scad:80 |
| B14 | (67, 25) x | 3 ft = 36 in | door | 1 | (east hall) / JACK & JILL BATH | option-e-linear-ranch/basement_e.scad:81 |
| B15 | (65.5, 28) y | 3 ft = 36 in | door | 1 | BEDROOM 3 / JACK & JILL BATH | option-e-linear-ranch/basement_e.scad:82 |
| B16 | (73.5, 28) y | 3 ft = 36 in | door | -1 | JACK & JILL BATH / BEDROOM 4 | option-e-linear-ranch/basement_e.scad:83 |
| B17 | (75, 25) x | 3 ft = 36 in | door | 1 | (east hall) / BEDROOM 4 | option-e-linear-ranch/basement_e.scad:84 |
| B18 | (87, 25) x | 3 ft = 36 in | door | 1 | (east hall) / FLEX / CRAFT | option-e-linear-ranch/basement_e.scad:85 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 19 | 19 |
| double | 0 | 0 | 2 | 2 |
| full | 0 | 0 | 10 | 10 |
| garage | 0 | 0 | 2 | 2 |
| ALL | 0 | 0 | 33 | 33 |
| passage (door+double+slider+open) | 0 | 0 | 21 | 21 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 14 | 14 |
| open | 0 | 0 | 1 | 1 |
| full | 0 | 0 | 3 | 3 |
| ALL | 0 | 0 | 18 | 18 |
| passage (door+double+slider+open) | 0 | 0 | 15 | 15 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-e-linear-ranch/main_floor_e.scad:81 | MASTER BEDROOM / DECK | double | 72 in | - |
| option-e-linear-ranch/main_floor_e.scad:95 | ELEVATOR (FUTURE) / (gallery) | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:102 | POWDER / FOYER | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:106 | (private hall) / BEDROOM 2 | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:107 | (private hall) / BATH | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:108 | (private hall) / MASTER BEDROOM | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:110 | LAUNDRY / WIC @61.5,19.5 | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:111 | WIC @61.5,19.5 / WIC @69,19.5 | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:112 | WIC @69,19.5 / MASTER BEDROOM | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:113 | WIC @61.5,19.5 / MASTER BATH | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:114 | WC / MASTER BATH | door | 36 in | 34.5 |
| option-e-linear-ranch/main_floor_e.scad:115 | MASTER BATH / MASTER BEDROOM | door | 36 in | 34.5 |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-e-linear-ranch/basement_e.scad:68 | STORAGE @24,0 / (landing at the stair foot) | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:72 | (hall, elevator approach) / STORAGE @37.5,27 | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:73 | (hall, elevator approach) / ELEVATOR (FUTURE) | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:74 | (hall, elevator approach) / STORAGE @48,27 | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:80 | (east hall) / BEDROOM 3 | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:81 | (east hall) / JACK & JILL BATH | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:82 | BEDROOM 3 / JACK & JILL BATH | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:83 | JACK & JILL BATH / BEDROOM 4 | door | 36 in | 34.5 |
| option-e-linear-ranch/basement_e.scad:84 | (east hall) / BEDROOM 4 | door | 36 in | 34.5 |

## Section 5

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| DINING / NOOK | S | (34, 0, 'x') | 5.5 | 2.5 | 5.5 | 30.2 | option-e-linear-ranch/main_floor_e.scad:120 |
| LIVING | S | (50, 0, 'x') | 12 | 2 | 6 | 72.0 | option-e-linear-ranch/main_floor_e.scad:121 |
| POWDER | S | (73.2, 0, 'x') | 2 | 4 | 2 | 4.0 | option-e-linear-ranch/main_floor_e.scad:122 |
| (private hall) | S | (78, 0, 'x') | 3.5 | 2 | 5 | 17.5 | option-e-linear-ranch/main_floor_e.scad:123 |
| BEDROOM 2 | S | (86, 0, 'x') | 6 | 2.5 | 5 | 30.0 | option-e-linear-ranch/main_floor_e.scad:124 |
| BEDROOM 2 | E | (96.5, 3, 'y') | 5 | 2.5 | 5 | 25.0 | option-e-linear-ranch/main_floor_e.scad:125 |
| BATH | E | (96.5, 14, 'y') | 3 | 4 | 3 | 9.0 | option-e-linear-ranch/main_floor_e.scad:126 |
| KITCHEN | W | (24, 29, 'y') | 5 | 3.5 | 4 | 20.0 | option-e-linear-ranch/main_floor_e.scad:127 |
| KITCHEN | N | (28, 39, 'x') | 8 | 3.5 | 4 | 32.0 | option-e-linear-ranch/main_floor_e.scad:128 |
| KITCHEN | N | (36, 39, 'x') | 4 | 3.5 | 4 | 16.0 | option-e-linear-ranch/main_floor_e.scad:129 |
| WC | N | (59.5, 39, 'x') | 2.5 | 4 | 3 | 7.5 | option-e-linear-ranch/main_floor_e.scad:130 |
| MASTER BATH | N | (71, 39, 'x') | 4 | 4 | 3 | 12.0 | option-e-linear-ranch/main_floor_e.scad:131 |
| MASTER BEDROOM | N | (79, 39, 'x') | 4.5 | 2.5 | 5 | 22.5 | option-e-linear-ranch/main_floor_e.scad:132 |
| MASTER BEDROOM | N | (92, 39, 'x') | 4 | 2.5 | 5 | 20.0 | option-e-linear-ranch/main_floor_e.scad:133 |
| MASTER BEDROOM | E | (96.5, 21, 'y') | 4 | 2.5 | 5 | 20.0 | option-e-linear-ranch/main_floor_e.scad:134 |
| MASTER BEDROOM | E | (96.5, 34.5, 'y') | 3.5 | 2.5 | 5 | 17.5 | option-e-linear-ranch/main_floor_e.scad:135 |

Total main-floor window glass (width x height): 355.2 sq ft (16 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 6, S: 5, E: 4, W: 1

Rooms with windows on 2+ walls (main): BEDROOM 2 (E/S); KITCHEN (N/W); MASTER BEDROOM (E/N)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| MUDROOM | utility | 94 |
| PANTRY | utility | 81 |
| VESTIBULE | hall | 52 |
| FOYER | hall | 126 |
| (kitchen to hub passage) | hall | 45 |
| ELEVATOR (FUTURE) | closet | 44 |
| (gallery) | hall | 82 |
| (gallery, east) | hall | 27 |
| (stair-top landing) | hall | 23 |
| LAUNDRY | utility | 76 |
| WIC @61.5,19.5 | closet | 71 |
| WIC @69,19.5 | closet | 71 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| BEDROOM 3 | N | (56.5, 39, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:160 |
| BEDROOM 4 | N | (76.5, 39, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:161 |
| FLEX / CRAFT | N | (89.5, 39, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:0 |
| OFFICE | S | (41.5, 0, 'x') | 4 | 3.5 | 3 | 12.0 | foundation.scad:0 |
| LIVING ROOM | S | (55, 0, 'x') | 8 | 3.5 | 3 | 24.0 | foundation.scad:0 |
| UTILITY | W | (24, 22, 'y') | 3 | 4 | 2 | 6.0 | foundation.scad:0 |
| UTILITY | W | (24, 27, 'y') | 3 | 4 | 2 | 6.0 | foundation.scad:0 |

Rooms with windows on 2+ walls (basement): none

Basement rooms with no window row: STORAGE @24,0 (closet, 263 sf); (landing at the stair foot) (hall, 107 sf); (hall, elevator approach) (hall, 120 sf); STORAGE @37.5,27 (closet, 33 sf); ELEVATOR (FUTURE) (closet, 44 sf); STORAGE @48,27 (closet, 41 sf); STAIR UP (stair, 74 sf); (east hall) (hall, 236 sf); JACK & JILL BATH (bath, 112 sf); THEATRE (rec, 273 sf); GYM / MUSIC (rec, 254 sf); WINDOW WELL @55,39 (porch, 23 sf); WINDOW WELL @75,39 (porch, 23 sf); WINDOW WELL @88,39 (porch, 23 sf); WINDOW WELL @40,-3.5 (porch, 23 sf); WINDOW WELL @54,-3.5 (porch, 37 sf)

## Section 6

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (private hall) | 76.5,0 to 82,19.5 | 107 | 5.1 ft clear width (61 in), length 19.1 | option-e-linear-ranch/main_floor_e.scad:50 |
| (kitchen to hub passage) | 42,19.5 to 48,27 | 45 | 5.6 ft clear width (67 in), length 7.1 | option-e-linear-ranch/main_floor_e.scad:55 |
| (gallery) | 48,19.5 to 53.5,34.4 | 82 | 5.1 ft clear width (61 in), length 14.5 | option-e-linear-ranch/main_floor_e.scad:58 |
| (gallery, east) | 53.5,29 to 58.5,34.4 | 27 | 4.6 ft clear width (55 in), length 5.0 | option-e-linear-ranch/main_floor_e.scad:59 |
| (stair-top landing) | 53.5,34.4 to 58.5,39 | 23 | 4.2 ft clear width (50 in), length 4.6 | option-e-linear-ranch/main_floor_e.scad:60 |

**Circulation total (halls only): 284 sq ft = 10.1% of 2828 sq ft conditioned** (10.2% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 52 | 6.1 ft | 11.9% | option-e-linear-ranch/main_floor_e.scad:47 |
| MUDROOM | 94 | 8.6 ft | 15.2% (halls+foyer+mudroom) | option-e-linear-ranch/main_floor_e.scad:43 |
| STAIR DN opening (stairwell) | 53 | 4.2 ft | 17.1% (all four) | option-e-linear-ranch/main_floor_e.scad:57 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| (landing at the stair foot) | 32,19.5 to 37.5,39 | 107 | 5.1 ft clear width (61 in), length 18.7 | option-e-linear-ranch/basement_e.scad:40 |
| (hall, elevator approach) | 37.5,19.5 to 53.5,27 | 120 | 7.1 ft clear width (85 in), length 15.6 | option-e-linear-ranch/basement_e.scad:42 |
| (east hall) | 53.5,19.5 to 96.5,25 | 236 | 5.1 ft clear width (61 in), length 42.2 | option-e-linear-ranch/basement_e.scad:47 |

**Circulation total (halls only): 464 sq ft = 15.7% of 2955 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 74 | 3.8 ft | 18.2% | option-e-linear-ranch/basement_e.scad:46 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.

## Section 7

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): PATIO <-> FRONT PORCH (12.0 ft shared edge)

Basement: none

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| GARAGE | garage | DRIVE (SLOPES UP TO GARAGE); MUDROOM; PANTRY | - |
| MUDROOM | utility | DINING / NOOK; GARAGE; PANTRY | - |
| PANTRY | utility | GARAGE; KITCHEN; MUDROOM | - |
| DINING / NOOK | dining | KITCHEN; LIVING; MUDROOM; PATIO | - |
| LIVING | living | (gallery); DINING / NOOK; FOYER | - |
| VESTIBULE | hall | FOYER; FRONT PORCH | - |
| POWDER | bath | FOYER | - |
| FOYER | hall | (private hall); LIVING; POWDER; VESTIBULE | - |
| (private hall) | hall | BATH; BEDROOM 2; FOYER; MASTER BEDROOM | - |
| BEDROOM 2 | bed | (private hall) | - |
| BATH | bath | (private hall) | - |
| KITCHEN | kitchen | (kitchen to hub passage); DINING / NOOK; PANTRY | - |
| (kitchen to hub passage) | hall | (gallery); KITCHEN | - |
| ELEVATOR (FUTURE) | closet | (gallery) | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (stair-top landing) | - |
| (gallery) | hall | (gallery, east); (kitchen to hub passage); ELEVATOR (FUTURE); LIVING | - |
| (gallery, east) | hall | (gallery); (stair-top landing); LAUNDRY | - |
| (stair-top landing) | hall | (gallery, east); STAIR DN | - |
| LAUNDRY | utility | (gallery, east); WIC @61.5,19.5 | - |
| WIC @61.5,19.5 | closet | LAUNDRY; MASTER BATH; WIC @69,19.5 | - |
| WIC @69,19.5 | closet | MASTER BEDROOM; WIC @61.5,19.5 | - |
| WC | bath | MASTER BATH | - |
| MASTER BATH | bath | MASTER BEDROOM; WC; WIC @61.5,19.5 | - |
| MASTER BEDROOM | bed | (private hall); DECK; MASTER BATH; WIC @69,19.5 | - |
| PATIO | porch, ceiling 0 (open zone) | DINING / NOOK; FRONT PORCH | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | PATIO; VESTIBULE | - |
| DRIVE (SLOPES UP TO GARAGE) | porch, ceiling 0 (open zone) | GARAGE | - |
| DECK | porch, ceiling 0 (open zone) | MASTER BEDROOM | - |

### 7.2 Basement adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| STORAGE @24,0 | closet | (landing at the stair foot) | - |
| UTILITY | utility | (landing at the stair foot) | - |
| (landing at the stair foot) | hall | (hall, elevator approach); STAIR UP; STORAGE @24,0; UTILITY | - |
| (hall, elevator approach) | hall | (east hall); (landing at the stair foot); ELEVATOR (FUTURE); OFFICE; STORAGE @37.5,27; STORAGE @48,27 | - |
| STORAGE @37.5,27 | closet | (hall, elevator approach) | - |
| ELEVATOR (FUTURE) | closet | (hall, elevator approach) | - |
| STORAGE @48,27 | closet | (hall, elevator approach) | - |
| STAIR UP | stair | (landing at the stair foot) | - |
| (east hall) | hall | (hall, elevator approach); BEDROOM 3; BEDROOM 4; FLEX / CRAFT; GYM / MUSIC; JACK & JILL BATH; LIVING ROOM; THEATRE | - |
| BEDROOM 3 | bed | (east hall); JACK & JILL BATH | - |
| JACK & JILL BATH | bath | (east hall); BEDROOM 3; BEDROOM 4 | - |
| BEDROOM 4 | bed | (east hall); JACK & JILL BATH | - |
| FLEX / CRAFT | office | (east hall) | - |
| OFFICE | office | (hall, elevator approach) | - |
| LIVING ROOM | living | (east hall) | - |
| THEATRE | rec | (east hall) | - |
| GYM / MUSIC | rec | (east hall) | - |
| WINDOW WELL @55,39 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @75,39 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @88,39 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @40,-3.5 | porch, ceiling 0 (open zone) | - | - |
| WINDOW WELL @54,-3.5 | porch, ceiling 0 (open zone) | - | - |

### 7.3 Daily paths

**Method:** shortest route by Dijkstra over door midpoints; each leg is the straight (Euclidean) distance between consecutive points inside one room (door midpoint to door midpoint; the first/last point is the room centre, a fixture centre, or the door/stair point named). Legs ignore furniture, so real walking length is >= these numbers. Porches/outside are never crossed.

| Path | walk ft | room sequence (innermost room each side of each door crossed) |
|---|---|---|
| front door -> kitchen/dining room centre | 51.5 | VESTIBULE > FOYER > LIVING > (gallery) > (kitchen to hub passage) > KITCHEN |
| front door -> range (option-e-linear-ranch/main_floor_e.scad:144) | 59.3 | VESTIBULE > FOYER > LIVING > (gallery) > (kitchen to hub passage) > KITCHEN |
| garage (room centre) -> kitchen/dining room centre | 30.6 | GARAGE > PANTRY > KITCHEN |
| garage (room centre) -> range | 33.8 | GARAGE > PANTRY > KITCHEN |
| garage (room centre) -> PANTRY centre | 16.6 | GARAGE > PANTRY |
| master bedroom centre -> WIC @61.5,19.5 centre | 22.3 | MASTER BEDROOM > WIC @69,19.5 > WIC @61.5,19.5 |
| master bedroom centre -> WIC @69,19.5 centre | 14.6 | MASTER BEDROOM > WIC @69,19.5 |
| master bedroom centre -> LAUNDRY centre | 30.0 | MASTER BEDROOM > WIC @69,19.5 > WIC @61.5,19.5 > LAUNDRY |
| BEDROOM 2 centre -> hall BATH centre | 25.6 | BEDROOM 2 > (private hall) > BATH |
| BEDROOM 2 centre -> MASTER BATH centre | 42.4 | BEDROOM 2 > (private hall) > MASTER BEDROOM > MASTER BATH |
| BEDROOM 2 centre -> LAUNDRY centre | 48.8 | BEDROOM 2 > (private hall) > MASTER BEDROOM > WIC @69,19.5 > WIC @61.5,19.5 > LAUNDRY |
| foyer centre -> POWDER centre (powder room) | 13.3 | VESTIBULE > FOYER > POWDER |
| front door -> top of main stair (top nosing, (47.75, 39)) | 56.1 | VESTIBULE > FOYER > LIVING > (gallery) > (gallery, east) > (stair-top landing) > STAIR DN |
| master bedroom centre -> top of main stair (top nosing, (47.75, 39)) | 48.8 | MASTER BEDROOM > WIC @69,19.5 > WIC @61.5,19.5 > LAUNDRY > (gallery, east) > (stair-top landing) > STAIR DN |
| BEDROOM 2 centre -> top of main stair (top nosing, (47.75, 39)) | 67.5 | BEDROOM 2 > (private hall) > MASTER BEDROOM > WIC @69,19.5 > WIC @61.5,19.5 > LAUNDRY > (gallery, east) > (stair-top landing) > STAIR DN |
| basement stair foot (45.50, 34.4) -> UTILITY centre | 27.6 | ELEVATOR (FUTURE) > (hall, elevator approach) > (landing at the stair foot) > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC @61.5,19.5 centre: no (via MASTER BEDROOM > WIC @69,19.5 > WIC @61.5,19.5); WIC @69,19.5 centre: no (via MASTER BEDROOM > WIC @69,19.5)

## Section 8

### 8.1 LIVING (main; option-e-linear-ranch/main_floor_e.scad:46) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| DINING / NOOK | dining | 19.5 | full 180 in |
| VESTIBULE | hall | 8.0 | - |
| FOYER | hall | 11.5 | full 72 in |
| (kitchen to hub passage) | hall | 1.0 | - |
| (gallery) | hall | 5.5 | full 61.2 in |
| LAUNDRY | utility | 8.0 | - |
| WIC @61.5,19.5 | closet | 4.0 | - |
| FRONT PORCH | porch (ceil 0) | 18.5 | - |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are LIVING. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| (hall, elevator approach) | hall | 4.0 | - |
| (east hall) | hall | 16.0 | open 96 in |
| OFFICE | office | 19.5 | - |
| THEATRE | rec | 19.5 | - |
| WINDOW WELL @54,-3.5 | porch (ceil 0) | 10.5 | - |

### 8.2 FOYER (option-e-linear-ranch/main_floor_e.scad:47) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| LIVING | living | 8.0 | - |
| POWDER | bath | 8.0 | - |
| FOYER | hall | 6.5 | door 36 in |
| FRONT PORCH | porch (ceil 0) | 6.5 | door 42 in |

### 8.3 Closets, WICs, linen, scullery/pantry, storage: exterior exposure

Pantry-like rooms: PANTRY.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | PANTRY | option-e-linear-ranch/main_floor_e.scad:44 | W 9.0 (garage) |
| main | ELEVATOR (FUTURE) | option-e-linear-ranch/main_floor_e.scad:56 | none |
| main | WIC @61.5,19.5 | option-e-linear-ranch/main_floor_e.scad:62 | none |
| main | WIC @69,19.5 | option-e-linear-ranch/main_floor_e.scad:63 | none |
| base | STORAGE @24,0 | option-e-linear-ranch/basement_e.scad:38 | S 13.5 (yard/soil); W 19.5 (yard/soil) |
| base | STORAGE @37.5,27 | option-e-linear-ranch/basement_e.scad:43 | none |
| base | ELEVATOR (FUTURE) | option-e-linear-ranch/basement_e.scad:44 | none |
| base | STORAGE @48,27 | option-e-linear-ranch/basement_e.scad:45 | none |

Pantry/garage: PANTRY shares 9.0 ft of wall with the garage; doors between PANTRY and GARAGE: 1. The garage's doors to the house are: option-e-linear-ranch/main_floor_e.scad:83 (GARAGE | MUDROOM, 36 in); option-e-linear-ranch/main_floor_e.scad:84 (GARAGE | PANTRY, 36 in).

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN | sink (142); range (144); fridge, by the pantry door (145); island, no seating, nothing in it (146); dishwasher (54 in aisle to the island) (147) | front door -> kitchen/dining room centre; front door -> range (option-e-linear-ranch/main_floor_e.scad:144); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range |
| LAUNDRY | laundry sink (173) | master bedroom centre -> LAUNDRY centre; BEDROOM 2 centre -> LAUNDRY centre; master bedroom centre -> top of main stair (top nosing, (47.75, 39)); BEDROOM 2 centre -> top of main stair (top nosing, (47.75, 39)) |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| GARAGE | 2.0 | west driveway (site.scad:111) | N 24.0 (yard/soil); S 24.0 (porch/patio (open)); W 27.0 (yard/soil) |
| MUDROOM | 14.0 | loop north leg (:114) | S 9.0 (yard/soil); W 10.5 (garage) |
| DINING / NOOK | 14.0 | loop north leg (:114) | S 14.0 (porch/patio (open)) |
| LIVING | 14.0 | loop north leg (:114) | S 18.5 (porch/patio (open)) |
| VESTIBULE | 14.0 | loop north leg (:114) | S 6.5 (porch/patio (open)) |
| POWDER | 14.0 | loop north leg (:114) | S 4.5 (porch/patio (open)) |
| (private hall) | 14.0 | loop north leg (:114) | S 5.5 (porch/patio (open)) |
| BEDROOM 2 | 14.0 | loop north leg (:114) | S 14.5 (yard/soil); E 11.5 (yard/soil) |
| FOYER | 22.0 | loop north leg (:114) | none |
| PANTRY | 24.5 | loop north leg (:114) | W 9.0 (garage) |
| BATH | 25.5 | loop north leg (:114) | E 8.0 (yard/soil) |
| KITCHEN | 26.0 | west driveway (site.scad:111) | N 18.0 (yard/soil); W 7.5 (garage), 12.0 (yard/soil) |
| (kitchen to hub passage) | 33.5 | loop north leg (:114) | none |
| (gallery) | 33.5 | loop north leg (:114) | none |
| LAUNDRY | 33.5 | loop north leg (:114) | none |
| WIC @61.5,19.5 | 33.5 | loop north leg (:114) | none |
| WIC @69,19.5 | 33.5 | loop north leg (:114) | none |
| MASTER BEDROOM | 33.5 | loop north leg (:114) | N 20.0 (yard/soil); E 16.0 (porch/patio (open)), 3.5 (yard/soil) |

Other rooms are > 40 ft from any drive. Garage doors (rows option-e-linear-ranch/main_floor_e.scad:77, option-e-linear-ranch/main_floor_e.scad:78) face S; garage rectangle to the nearest drive piece: 2.0 ft.

## Section 9

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| sink (KITCHEN) | KITCHEN | (30, 37.5, 33, 38.5) | (31.5, 38.0) | N wall y=39 | 0.50 | option-e-linear-ranch/main_floor_e.scad:142 |
| toilet/tub/wash basin (POWDER) | POWDER | (73.4, 0.8, 75.4, 2.4) | (74.4, 1.6) | S wall y=0 | 0.80 | option-e-linear-ranch/main_floor_e.scad:158 |
| vanity (POWDER) | POWDER | (72.3, 3.4, 73.3, 6.2) | (72.8, 4.8) | W wall x=72 | 0.30 | option-e-linear-ranch/main_floor_e.scad:159 |
| shower (BATH) | BATH | (91.2, 11.9, 96.3, 15.6) | (93.8, 13.8) | E wall x=96.5 | 0.20 | option-e-linear-ranch/main_floor_e.scad:167 |
| vanity (BATH) | BATH | (86, 17.8, 93, 19.3) | (89.5, 18.6) | N wall y=19.5 | 0.20 | option-e-linear-ranch/main_floor_e.scad:168 |
| toilet/tub/wash basin (BATH) | BATH | (94, 17.4, 95.8, 19.1) | (94.9, 18.2) | N wall y=19.5 | 0.40 | option-e-linear-ranch/main_floor_e.scad:169 |
| washer/dryer (LAUNDRY) | LAUNDRY | (53.7, 19.7, 58, 22.2) | (55.9, 20.9) | S wall y=19.5 | 0.20 | option-e-linear-ranch/main_floor_e.scad:172 |
| sink (LAUNDRY) | LAUNDRY | (59, 20.2, 60.7, 21.4) | (59.9, 20.8) | S wall y=19.5 | 0.70 | option-e-linear-ranch/main_floor_e.scad:174 |
| shower (MASTER BATH) | MASTER BATH | (64.4, 34.5, 69.4, 38.8) | (66.9, 36.6) | N wall y=39 | 0.20 | option-e-linear-ranch/main_floor_e.scad:179 |
| vanity (MASTER BATH) | MASTER BATH | (70, 37.4, 76.3, 38.8) | (73.2, 38.1) | N wall y=39 | 0.20 | option-e-linear-ranch/main_floor_e.scad:180 |
| toilet/tub/wash basin (WC) | WC | (59, 36.5, 61, 38.2) | (60.0, 37.4) | W wall x=58.5 | 0.50 | option-e-linear-ranch/main_floor_e.scad:182 |

(equipment list omitted in variant mode)

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| shower (JACK & JILL BATH) | JACK & JILL BATH | (66.8, 35.5, 72.4, 38.6) | (69.6, 37.0) | N wall y=39 | 0.40 | option-e-linear-ranch/basement_e.scad:110 |
| toilet/tub/wash basin (JACK & JILL BATH) | JACK & JILL BATH | (66.8, 32.2, 68.6, 34) | (67.7, 33.1) | W wall x=65.5 | 1.30 | option-e-linear-ranch/basement_e.scad:111 |
| vanity (JACK & JILL BATH) | JACK & JILL BATH | (71.4, 32, 73.1, 35.5) | (72.2, 33.8) | E wall x=73.5 | 0.40 | option-e-linear-ranch/basement_e.scad:112 |

(equipment list omitted in variant mode)

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | toilet/tub/wash basin (POWDER) | POWDER | y=0 (horizontal wall) | (74.4, 1.6) |
| G2 | vanity (POWDER) | POWDER | x=72 (vertical wall) | (72.8, 4.8) |
| G3 | shower (BATH) | BATH | x=96.5 (vertical wall) | (93.8, 13.8) |
| G4 | vanity (BATH); toilet/tub/wash basin (BATH) | BATH | y=19.5 (horizontal wall) | (92.2, 18.4) |
| G5 | washer/dryer (LAUNDRY); sink (LAUNDRY) | LAUNDRY | y=19.5 (horizontal wall) | (57.9, 20.9) |
| G6 | shower (MASTER BATH); vanity (MASTER BATH) | MASTER BATH | y=39 (horizontal wall) | (70.0, 37.4) |
| G7 | toilet/tub/wash basin (WC) | WC | x=58.5 (vertical wall) | (60.0, 37.4) |
| G8 | sink (KITCHEN) | KITCHEN | y=39 (horizontal wall) | (31.5, 38.0) |

**Main floor: 8 wet-wall groups** (4 back-to-back plumbing clusters of rooms: POWDER | BATH | KITCHEN | LAUNDRY+WC+MASTER BATH)

Basement:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | toilet/tub/wash basin (JACK & JILL BATH) | JACK & JILL BATH | x=65.5 (vertical wall) | (67.7, 33.1) |
| G2 | vanity (JACK & JILL BATH) | JACK & JILL BATH | x=73.5 (vertical wall) | (72.2, 33.8) |
| G3 | shower (JACK & JILL BATH) | JACK & JILL BATH | y=39 (horizontal wall) | (69.6, 37.0) |

**Basement: 3 wet-wall groups** (1 clusters: JACK & JILL BATH)

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 8/3; 6 ft: 8/3; 8 ft: 8/3; 12 ft: 8/3; inf: 6/3

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | toilet/tub/wash basin (POWDER) | (74.4,1.6) | B2 (JACK & JILL BATH) | (72.2,33.8) | 2.2 | 32.1 | 34.3 |
| G2 | vanity (POWDER) | (72.8,4.8) | B2 (JACK & JILL BATH) | (72.2,33.8) | 0.5 | 28.9 | 29.5 |
| G3 | shower (BATH) | (93.8,13.8) | B2 (JACK & JILL BATH) | (72.2,33.8) | 21.5 | 20.0 | 41.5 |
| G4 | vanity (BATH); toilet/tub/wash basin (BATH) | (92.2,18.4) | B2 (JACK & JILL BATH) | (72.2,33.8) | 20.0 | 15.4 | 35.3 |
| G5 | washer/dryer (LAUNDRY); sink (LAUNDRY) | (57.9,20.9) | B1 (JACK & JILL BATH) | (67.7,33.1) | 9.8 | 12.2 | 22.1 |
| G6 | shower (MASTER BATH); vanity (MASTER BATH) | (70.0,37.4) | B3 (JACK & JILL BATH) | (69.6,37.0) | 0.4 | 0.3 | 0.8 |
| G7 | toilet/tub/wash basin (WC) | (60.0,37.4) | B3 (JACK & JILL BATH) | (69.6,37.0) | 9.6 | 0.3 | 9.9 |
| G8 | sink (KITCHEN) | (31.5,38.0) | B3 (JACK & JILL BATH) | (69.6,37.0) | 38.1 | 1.0 | 39.0 |

Main-floor groups with a basement group within 5 ft Manhattan: 1 of 8; within 10 ft: 2.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (74.4,1.6) | 108.6 | 89.5 |
| G2 | (72.8,4.8) | 103.8 | 84.7 |
| G3 | (93.8,13.8) | 115.8 | 96.7 |
| G4 | (92.2,18.4) | 109.6 | 90.5 |
| G5 | (57.9,20.9) | 72.8 | 53.7 |
| G6 | (70.0,37.4) | 68.5 | 49.4 |
| G7 | (60.0,37.4) | 58.5 | 39.4 |
| G8 | (31.5,38.0) | 29.3 | 10.2 |

**DRI (E = (22.16, 58)) = 667.1 ft over 8 groups; mean 83.4 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 514.3 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:104, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:103). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **shower (BATH), 83.9 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: shower (BATH), 80.3 ft.
- Furthest basement fixture: **shower (JACK & JILL BATH), 51.3 ft** from the water heater.
- Nearest main-floor fixture: sink (KITCHEN), 14.2 ft.

Per fixture (Manhattan plan ft from the water heater): sink (KITCHEN) 14; toilet/tub/wash basin (POWDER) 77; vanity (POWDER) 72; shower (BATH) 84; vanity (BATH) 75; toilet/tub/wash basin (BATH) 81; washer/dryer (LAUNDRY) 39; sink (LAUNDRY) 43; shower (MASTER BATH) 48; vanity (MASTER BATH) 56; toilet/tub/wash basin (WC) 42; shower (JACK & JILL BATH) 51; toilet/tub/wash basin (JACK & JILL BATH) 45; vanity (JACK & JILL BATH) 51

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
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | option-e-linear-ranch/main_floor_e.scad:57 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | option-e-linear-ranch/basement_e.scad:46 |
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
| Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27) | 24.7 ft (7.5 m) |
| Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6) | 19.16 ft (5.8 m) / 18.61 ft |
| Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner | 21.3 ft (6.5 m) |
| Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour | 19.2 ft (5.8 m) |
| Septic tank to well | 147.4 ft (44.9 m) |
| Pump chamber to well | 147.2 ft (44.9 m) |
| Treatment field to well | 215.0 ft (65.5 m) |
| Reserve field to well | 217.8 ft (66.4 m) |
| Treatment field to the basement (outline polygon) | 87.2 ft (26.6 m) |
| Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27) | 89.2 ft (27.2 m) |
| Treatment field to the garage west wall (x=0, slab, no basement) | 65.7 ft (20.0 m) |
| Reserve field to basement | 87.2 ft (26.6 m) |
| Reserve field to the nearest heated wall | 89.0 ft (27.1 m) |
| Reserve field to the garage | 65.0 ft (19.8 m) |
| Treatment field to west driveway edge (x=-32) | 33.1 ft (10.1 m) |
| Reserve field to west driveway edge | 33.0 ft (10.1 m) |
| Treatment field to the service-line corridor (x=-47..-41) | 18.0 ft (5.5 m) |
| Reserve field to the service-line corridor | 18.0 ft (5.5 m) |
| Reserve field to propane pad (-68..-52, -48..-42) | 27.0 ft (8.2 m) |
| Well to heated main-floor wall (nearest) | 64.5 ft (19.7 m) |
| Well to side porch/deck edge (nearest unconditioned main-floor row) | 56.6 ft (17.3 m) |
| Well to basement outline | 57.4 ft (17.5 m) |
| House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130) | 91.0 ft (27.7 m) |
| House incl. porches/deck to future shop | 91.0 ft (27.7 m) |
| Basement exit areaway (y 67.75) to shop | 62.3 ft (19.0 m) |
| Garage to shop (garage north wall 35.46) | 94.5 ft (28.8 m) |

Corridor and drive lengths: power run road->meter wall 197.3 ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas 202.3 ft; fibre 192.3 ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: 53.0 ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).

West driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).

phase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.

Phase house: parents' house and geothermal loop field are not in site.scad (§13).

