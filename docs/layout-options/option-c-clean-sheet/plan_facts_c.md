# Option C notes (added by the layout designer; tool output follows unchanged)

- Stair fit: top nosing x 42.65-47.27, y 47.1 (unchanged); flight 1 = 18 risers, 17 treads, to y 32.225; landing y 27.8-32.225 (4.4 ft; stair width 4.22 ft clear) at 11.25 ft below the main floor; flight 2 = 4 risers turning east to x 49.7. Stair-top landing on the main floor 4.62 x 5.00 ft (CODE-07). The matrix line "moved" for the foot room (y 27.6 vs 28.725) is expected: same fix as Option A.
- Building area to the outside face: 575.3 m2 against 600 (24.7 under); centre lines 559.3 m2. Method: 0.5 ft offset, attached garage counted, porches not (matrix_c.md).
- Prose lines in sections 8, 10 and 12 below that quote `main_floor.scad:NNN` / `site.scad:NNN` are the CURRENT models' references (README-variant limits); tables point at main_floor_c.scad. Section 2.2 / 8.5 distances to the drive still use the west drive of site.scad (42.0 ft); with the south drive, bedroom 3 is more than 60 ft from the apron (hand measurement).
- Changes in basement / shop / site: basement_c.scad (stair foot only); shop none; site: south drive replaces the west drive (not drawn in site.scad); foundation crawl wings W and E mostly not needed.

# Plan facts (variant mode)

main = `/home/user/house-layout/docs/layout-options/option-c-clean-sheet/main_floor_c.scad`, basement = `/home/user/house-layout/docs/layout-options/option-c-clean-sheet/basement_c.scad`. Computed sections of Phase 0 plan_facts.md, regenerated for this variant. Table `source` columns point at the variant files; hard-coded line references in prose (e.g. main_floor.scad:NNN, site.scad:NNN) are the CURRENT models'. Section 11 and 13-15 of Phase 0 are about the current repo and are not repeated.

## Layout matrix

Source files: main = `/home/user/house-layout/docs/layout-options/option-c-clean-sheet/main_floor_c.scad`; basement = `/home/user/house-layout/docs/layout-options/option-c-clean-sheet/basement_c.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 5,444 | 5444.0; excl. stair opening 5390.2 |
| Building area, centre lines (house + attached garage) | 559.3 m2 | 6020 sq ft |
| Building area, outside face | 575.3 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Circulation % (strict / with foyer) | 8.7% / 10.2% | 474 sq ft strict of 5444 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 30 | type `door` rows, by opening width |
| Double / open counts (main) | 5 / 0 | type `double` / type `open` |
| Minimum hall clear width | 4.60 ft ((gallery, west)) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 4.22 ft ((stair-top landing)) |
| Wet-wall groups (main / basement) | 12 / 8 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 1 of 12 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 951.3 ft | alternate exit (22.16, 38.9): 845.8 ft |
| Water heater -> furthest fixture (main / basement) | 87.3 ft (shower (BATH 2)) / 84.8 ft (toilet/tub/wash basin (POOL BATH)) | water heater at (30.1, 36.8); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | MASTER LAUNDRY: 24.9 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 0 of 6:  | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | SCULLERY / PANTRY: 13.0 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 3: N(yard 12.0) ;; BEDROOM 2: E(porch/patio 14.0) ;; MASTER BEDROOM: N(yard 20.0) E(porch/patio 14.0, yard 7.4) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 36.0) E(porch/patio 14.0, yard 7.4) | suite rooms: MASTER BEDROOM, WIC, MASTER BATH |
| Living-kind rooms with S exposure | LIVING ROOM (16.0 ft); SUN ROOM (14.0 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 3: SUN ROOM (E/S); LIBRARY (N/W); MASTER BEDROOM (E/N) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 42.65..47.27, y 47.1; basement foot room x 42.65..47.27, y 27.6; **moved** (x offset +0.00/+0.00 ft, run 19.500 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 42.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_c.scad (defaults): 38 rooms, 49 doors, 18 windows - OK ; basement_c.scad (defaults): 19 rooms, 19 doors, 2 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |

## Section 1

### 1.1 Areas (centre-line W x D, sq ft; ceiling-0 open zones included where heated)

| Item | sq ft | Source / formula |
|---|---|---|
| Main-floor conditioned, sum of heated room rows (kind not porch/garage; includes STAIR DN stairwell footprint) | 5444.0 | computed: sum (x1-x0)*(y1-y0) over 32 rows, main_floor.scad:50-92 |
|   of which STAIR DN stairwell footprint (opening: no floor on this level) | 53.8 | option-c-clean-sheet/main_floor_c.scad:62 |
| Main-floor conditioned excluding the stair opening | 5390.2 | difference |
| Main-floor heated union polygon (shapely check, should equal row sum) | 5444.0 | unary_union of heated rects; holes=0 |
| Basement, sum of rooms (excl. EXIT STAIR areaway; includes pool-room 'pit', theatre 'tiered', stair) | 3475.0 | computed over basement.scad:62-81 |
| Basement outline polygon (centre lines) | 3475.0 | foundation.scad:40-45 basement_outline(), shoelace |
| Garage (GARAGE row, slab 1.5 ft below house floor) | 576.2 | option-c-clean-sheet/main_floor_c.scad:50 |

Unconditioned, listed separately (main_floor.scad rows; kind porch = ceiling 0, no walls):

| Porch / patio / deck row | sq ft | Source |
|---|---|---|
| FRONT PORCH | 740.0 | option-c-clean-sheet/main_floor_c.scad:88 |
| MUD STOOP | 71.0 | option-c-clean-sheet/main_floor_c.scad:89 |
| PATIO | 264.0 | option-c-clean-sheet/main_floor_c.scad:90 |
| MASTER PORCH | 120.0 | option-c-clean-sheet/main_floor_c.scad:91 |
| DECK | 220.0 | option-c-clean-sheet/main_floor_c.scad:92 |

Porch/patio/deck rows total (sum of rows; PATIO and DECK etc. are separate rows; unlabelled pieces are small porch extensions): 1415.0 sq ft. PATIO alone: 264.0; DECK alone: 220.0. Note that SIDE ENTRY (kind porch, 11.26 x 7.43) sits east of the garage and south of the scullery.

### 1.2 Envelope of the heated main floor (centre-line polygon)

| Measure | Value | How |
|---|---|---|
| Perimeter of heated union, centre line | 298.5 ft | shapely union of heated rects; this includes walls facing the garage and porches |
|   facing yard/soil | 130.8 ft | sum of room edges whose outside point is in no room |
|   facing porch/patio (open) | 141.8 ft | same |
|   facing garage | 26.0 ft | same (garage is unheated) |
| Outside (convex) corners | 4 | vertices of the union polygon after 0.02 ft simplify (4 vertices) |
| Inside (reflex) corners | 0 | same polygon |
| Bounding box, heated rooms | x 22.16..108 (85.84 ft), y 0..63.42 (63.42 ft) | min/max of heated room rects |
| Bounding box, everything on the main floor incl. garage, porches, deck | x 0..120 (120 ft), y -10..63.42 (73.42 ft) | all main_rooms rows |
| Basement outline | x 22.16..103.04, y 5.79..63.16; perimeter 281.3 ft; 9 outside / 5 inside corners (14 vertices) | foundation.scad:40-45 |
| Roof | 6 hip-roof blocks in main_roof (main_floor.scad:287); each hip block is 4 sloped facets, so 4 x 6 = 24 nominal facets before overlapping blocks merge; 2 blocks at 6/12 pitch, 4 porch blocks at 4/12 | house_lib.scad:hip_roof; the model draws overlapping blocks, so true merged facet count is not in model |

(Rooms with wall_t 0.4 ft: exterior and interior walls are drawn at the same thickness on the main floor, house_lib.scad:40; basement outside walls are ICF 13.25 in, foundation.scad:37.)

## Section 2

### 2.2 Exterior sides per main-floor room (length in ft of that room's wall facing outdoors / porch / garage)

Heated rooms only (porches and garage excluded). 'porch/patio (open)' = covered but unconditioned; 'garage' = the unheated attached garage; 'yard/soil' = open air.

| Room | Exterior sides touched (length ft) | Source |
|---|---|---|
| MUDROOM | S 11.8 (porch/patio (open)); W 13.0 (garage) | option-c-clean-sheet/main_floor_c.scad:51 |
| SCULLERY / PANTRY | W 13.0 (garage) | option-c-clean-sheet/main_floor_c.scad:52 |
| KITCHEN | N 0.1 (yard/soil); S 20.0 (porch/patio (open)) | option-c-clean-sheet/main_floor_c.scad:53 |
| DINING | S 12.0 (porch/patio (open)) | option-c-clean-sheet/main_floor_c.scad:54 |
| VESTIBULE | S 12.0 (porch/patio (open)) | option-c-clean-sheet/main_floor_c.scad:55 |
| FOYER | none | option-c-clean-sheet/main_floor_c.scad:56 |
| LIVING ROOM | S 16.0 (porch/patio (open)) | option-c-clean-sheet/main_floor_c.scad:57 |
| SUN ROOM | S 14.0 (porch/patio (open)); E 22.0 (porch/patio (open)) | option-c-clean-sheet/main_floor_c.scad:58 |
| DEN | W 21.1 (yard/soil) | option-c-clean-sheet/main_floor_c.scad:60 |
| BUTLER | none | option-c-clean-sheet/main_floor_c.scad:61 |
| STAIR DN | none | option-c-clean-sheet/main_floor_c.scad:62 |
| STORAGE | none | option-c-clean-sheet/main_floor_c.scad:63 |
| POWDER | none | option-c-clean-sheet/main_floor_c.scad:64 |
| COATS | none | option-c-clean-sheet/main_floor_c.scad:65 |
| BROOM | none | option-c-clean-sheet/main_floor_c.scad:66 |
| H1 | none | option-c-clean-sheet/main_floor_c.scad:68 |
| (gallery, west) | W 5.0 (yard/soil) | option-c-clean-sheet/main_floor_c.scad:69 |
| (stair-top landing) | none | option-c-clean-sheet/main_floor_c.scad:70 |
| GALLERY | none | option-c-clean-sheet/main_floor_c.scad:71 |
| H4 | none | option-c-clean-sheet/main_floor_c.scad:72 |
| LIBRARY | N 20.5 (yard/soil); W 11.3 (yard/soil) | option-c-clean-sheet/main_floor_c.scad:74 |
| OFFICE | N 17.4 (yard/soil) | option-c-clean-sheet/main_floor_c.scad:75 |
| BEDROOM 3 | N 12.0 (yard/soil) | option-c-clean-sheet/main_floor_c.scad:77 |
| LINEN | none | option-c-clean-sheet/main_floor_c.scad:78 |
| BATH | none | option-c-clean-sheet/main_floor_c.scad:79 |
| CLOSET | none | option-c-clean-sheet/main_floor_c.scad:80 |
| BEDROOM 2 | E 14.0 (porch/patio (open)) | option-c-clean-sheet/main_floor_c.scad:81 |
| BATH 2 | E 6.0 (porch/patio (open)) | option-c-clean-sheet/main_floor_c.scad:82 |
| MASTER BEDROOM | N 20.0 (yard/soil); E 14.0 (porch/patio (open)), 7.4 (yard/soil) | option-c-clean-sheet/main_floor_c.scad:83 |
| MASTER LAUNDRY | none | option-c-clean-sheet/main_floor_c.scad:84 |
| WIC | none | option-c-clean-sheet/main_floor_c.scad:85 |
| MASTER BATH | N 16.0 (yard/soil) | option-c-clean-sheet/main_floor_c.scad:86 |

## Section 3

Clear dimensions = centre-line size minus half of each bounding wall's thickness (0.4 ft each wall on the main floor; 13.25 in on basement outside walls). For ceiling-0 open zones the same rule is applied for the kinds that are bounded by neighbours' walls (halls); porches are shown nominal.

### 3.1 Main floor (heated rooms, then unconditioned rows)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MUDROOM | 22.16 | 0 | 34 | 13 | 11.84 x 13.00 | 11.4 x 12.6 | 154 | 144 | 1.10 | utility | 10 | option-c-clean-sheet/main_floor_c.scad:51 |
| SCULLERY / PANTRY | 22.16 | 13 | 34 | 26 | 11.84 x 13.00 | 11.4 x 12.6 | 154 | 144 | 1.10 | utility | 10 | option-c-clean-sheet/main_floor_c.scad:52 |
| KITCHEN | 34 | 0 | 54 | 26 | 20.00 x 26.00 | 19.6 x 25.6 | 520 | 502 | 1.30 | kitchen | 12 | option-c-clean-sheet/main_floor_c.scad:53 |
| DINING | 54 | 0 | 66 | 26 | 12.00 x 26.00 | 11.6 x 25.6 | 312 | 297 | 2.17 | dining | 12 | option-c-clean-sheet/main_floor_c.scad:54 |
| VESTIBULE | 66 | 0 | 78 | 7 | 12.00 x 7.00 | 11.6 x 6.6 | 84 | 77 | 1.71 | hall | 10 | option-c-clean-sheet/main_floor_c.scad:55 |
| FOYER | 66 | 7 | 78 | 28 | 12.00 x 21.00 | 11.6 x 20.6 | 252 | 239 | 1.75 | hall | 12 | option-c-clean-sheet/main_floor_c.scad:56 |
| LIVING ROOM | 78 | 0 | 94 | 28 | 16.00 x 28.00 | 15.6 x 27.6 | 448 | 431 | 1.75 | living | 12 | option-c-clean-sheet/main_floor_c.scad:57 |
| SUN ROOM | 94 | 0 | 108 | 22 | 14.00 x 22.00 | 13.6 x 21.6 | 308 | 294 | 1.57 | living | 10 | option-c-clean-sheet/main_floor_c.scad:58 |
| DEN | 22.16 | 26 | 42.65 | 47.1 | 20.49 x 21.10 | 20.1 x 20.7 | 432 | 416 | 1.03 | living | 10 | option-c-clean-sheet/main_floor_c.scad:60 |
| BUTLER | 42.65 | 26 | 60 | 35.46 | 17.35 x 9.46 | 17.0 x 9.1 | 164 | 154 | 1.83 | utility | 10 | option-c-clean-sheet/main_floor_c.scad:61 |
| STAIR DN | 42.65 | 35.46 | 47.27 | 47.1 | 4.62 x 11.64 | 4.2 x 11.2 | 54 | - | 2.52 | stairwell | 0 | option-c-clean-sheet/main_floor_c.scad:62 |
| STORAGE | 47.27 | 35.46 | 60 | 47.1 | 12.73 x 11.64 | 12.3 x 11.2 | 148 | 139 | 1.09 | closet | 10 | option-c-clean-sheet/main_floor_c.scad:63 |
| POWDER | 60 | 26 | 66 | 33 | 6.00 x 7.00 | 5.6 x 6.6 | 42 | 37 | 1.17 | bath | 10 | option-c-clean-sheet/main_floor_c.scad:64 |
| COATS | 60 | 33 | 66 | 40 | 6.00 x 7.00 | 5.6 x 6.6 | 42 | 37 | 1.17 | closet | 10 | option-c-clean-sheet/main_floor_c.scad:65 |
| BROOM | 60 | 40 | 66 | 47.1 | 6.00 x 7.10 | 5.6 x 6.7 | 43 | 38 | 1.18 | closet | 10 | option-c-clean-sheet/main_floor_c.scad:66 |
| H1 | 66 | 28 | 72 | 52.1 | 6.00 x 24.10 | 5.6 x 23.7 | 145 | 133 | 4.02 | hall | 10 | option-c-clean-sheet/main_floor_c.scad:68 |
| (gallery, west) | 22.16 | 47.1 | 42.65 | 52.1 | 20.49 x 5.00 | 20.1 x 4.6 | 102 | 92 | 4.10 | hall | 10 | option-c-clean-sheet/main_floor_c.scad:69 |
| (stair-top landing) | 42.65 | 47.1 | 47.27 | 52.1 | 4.62 x 5.00 | 4.2 x 4.6 | 23 | 19 | 1.08 | hall | 10 | option-c-clean-sheet/main_floor_c.scad:70 |
| GALLERY | 47.27 | 47.1 | 66 | 52.1 | 18.73 x 5.00 | 18.3 x 4.6 | 94 | 84 | 3.75 | hall | 10 | option-c-clean-sheet/main_floor_c.scad:71 |
| H4 | 72 | 37 | 94 | 42 | 22.00 x 5.00 | 21.6 x 4.6 | 110 | 99 | 4.40 | hall | 10 | option-c-clean-sheet/main_floor_c.scad:72 |
| LIBRARY | 22.16 | 52.1 | 42.65 | 63.42 | 20.49 x 11.32 | 20.1 x 10.9 | 232 | 219 | 1.81 | office | 10 | option-c-clean-sheet/main_floor_c.scad:74 |
| OFFICE | 42.65 | 52.1 | 60 | 63.42 | 17.35 x 11.32 | 17.0 x 10.9 | 196 | 185 | 1.53 | office | 10 | option-c-clean-sheet/main_floor_c.scad:75 |
| BEDROOM 3 | 60 | 52.1 | 72 | 63.42 | 12.00 x 11.32 | 11.6 x 10.9 | 136 | 127 | 1.06 | bed | 10 | option-c-clean-sheet/main_floor_c.scad:77 |
| LINEN | 72 | 28 | 78 | 37 | 6.00 x 9.00 | 5.6 x 8.6 | 54 | 48 | 1.50 | closet | 10 | option-c-clean-sheet/main_floor_c.scad:78 |
| BATH | 78 | 28 | 88 | 37 | 10.00 x 9.00 | 9.6 x 8.6 | 90 | 83 | 1.11 | bath | 10 | option-c-clean-sheet/main_floor_c.scad:79 |
| CLOSET | 88 | 28 | 94 | 37 | 6.00 x 9.00 | 5.6 x 8.6 | 54 | 48 | 1.50 | closet | 10 | option-c-clean-sheet/main_floor_c.scad:80 |
| BEDROOM 2 | 94 | 28 | 108 | 42 | 14.00 x 14.00 | 13.6 x 13.6 | 196 | 185 | 1.00 | bed | 10 | option-c-clean-sheet/main_floor_c.scad:81 |
| BATH 2 | 94 | 22 | 108 | 28 | 14.00 x 6.00 | 13.6 x 5.6 | 84 | 76 | 2.33 | bath | 10 | option-c-clean-sheet/main_floor_c.scad:82 |
| MASTER BEDROOM | 88 | 42 | 108 | 63.42 | 20.00 x 21.42 | 19.6 x 21.0 | 428 | 412 | 1.07 | bed | 10 | option-c-clean-sheet/main_floor_c.scad:83 |
| MASTER LAUNDRY | 72 | 42 | 80 | 52 | 8.00 x 10.00 | 7.6 x 9.6 | 80 | 73 | 1.25 | utility | 10 | option-c-clean-sheet/main_floor_c.scad:84 |
| WIC | 80 | 42 | 88 | 52 | 8.00 x 10.00 | 7.6 x 9.6 | 80 | 73 | 1.25 | closet | 10 | option-c-clean-sheet/main_floor_c.scad:85 |
| MASTER BATH | 72 | 52 | 88 | 63.42 | 16.00 x 11.42 | 15.6 x 11.0 | 183 | 172 | 1.40 | bath | 10 | option-c-clean-sheet/main_floor_c.scad:86 |

#### Garage and porches (not conditioned)

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GARAGE | 0 | 0 | 22.16 | 26 | 22.16 x 26.00 | 21.8 x 25.6 | 576 | 557 | 1.17 | garage | 10 | option-c-clean-sheet/main_floor_c.scad:50 |
| FRONT PORCH | 34 | -10 | 108 | 0 | 74.00 x 10.00 | 74.0 x 10.0 (open) | 740 | - | 7.40 | porch | 0 | option-c-clean-sheet/main_floor_c.scad:88 |
| MUD STOOP | 22.16 | -6 | 34 | 0 | 11.84 x 6.00 | 11.8 x 6.0 (open) | 71 | - | 1.97 | porch | 0 | option-c-clean-sheet/main_floor_c.scad:89 |
| PATIO | 108 | 0 | 120 | 22 | 12.00 x 22.00 | 12.0 x 22.0 (open) | 264 | - | 1.83 | porch | 0 | option-c-clean-sheet/main_floor_c.scad:90 |
| MASTER PORCH | 108 | 44 | 118 | 56 | 10.00 x 12.00 | 10.0 x 12.0 (open) | 120 | - | 1.20 | porch | 0 | option-c-clean-sheet/main_floor_c.scad:91 |
| DECK | 108 | 22 | 118 | 44 | 10.00 x 22.00 | 10.0 x 22.0 (open) | 220 | - | 2.20 | porch | 0 | option-c-clean-sheet/main_floor_c.scad:92 |

### 3.2 Basement

| Room | x0 | y0 | x1 | y1 | W x D (c/l) | approx clear | area c/l sf | area clear sf | long:short | kind | ceil | source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MUSIC ROOM | 22.16 | 50.35 | 42.65 | 63.16 | 20.49 x 12.81 | 19.7 x 12.1 | 262 | 238 | 1.60 | living | 12 | option-c-clean-sheet/basement_c.scad:62 |
| GYM | 42.65 | 45.34 | 54.14 | 63.16 | 11.49 x 17.82 | 10.7 x 17.1 | 205 | 183 | 1.55 | rec | 12 | option-c-clean-sheet/basement_c.scad:63 |
| STORAGE | 22.16 | 42.77 | 37.37 | 50.35 | 15.21 x 7.58 | 14.5 x 7.2 | 115 | 104 | 2.01 | closet | 12 | option-c-clean-sheet/basement_c.scad:64 |
| UTILITY | 22.16 | 35.08 | 37.37 | 42.77 | 15.21 x 7.69 | 14.5 x 6.9 | 117 | 100 | 1.98 | utility | 12 | option-c-clean-sheet/basement_c.scad:65 |
| HALL @37.37,35.08 | 37.37 | 35.08 | 42.65 | 50.35 | 5.28 x 15.27 | 4.9 x 14.9 | 81 | 73 | 2.89 | hall | 12 | option-c-clean-sheet/basement_c.scad:66 |
| STAIR UP | 42.65 | 27.6 | 47.27 | 45.34 | 4.62 x 17.74 | 4.2 x 17.3 | 82 | 73 | 3.84 | stair | 12 | option-c-clean-sheet/basement_c.scad:67 |
| BATH @47.27,35.08 | 47.27 | 35.08 | 54.14 | 45.34 | 6.87 x 10.26 | 6.5 x 9.9 | 70 | 64 | 1.49 | bath | 12 | option-c-clean-sheet/basement_c.scad:68 |
| HALLWAY | 35.27 | 27.6 | 42.65 | 35.08 | 7.38 x 7.48 | 6.6 x 7.1 | 55 | 47 | 1.01 | hall | 0 | option-c-clean-sheet/basement_c.scad:69 |
| STAIR FOOT | 47.27 | 27.6 | 54.14 | 35.08 | 6.87 x 7.48 | 6.5 x 7.1 | 51 | 46 | 1.09 | hall | 0 | option-c-clean-sheet/basement_c.scad:70 |
| LIVING ROOM | 35.27 | 5.79 | 54.14 | 27.6 | 18.87 x 21.81 | 18.1 x 21.1 | 412 | 382 | 1.16 | living | 10 | option-c-clean-sheet/basement_c.scad:71 |
| HOME THEATER | 54.14 | 29.12 | 69.38 | 50.35 | 15.24 x 21.23 | 14.8 x 20.5 | 324 | 304 | 1.39 | tiered | 13.25 | option-c-clean-sheet/basement_c.scad:72 |
| PET ROOM | 54.14 | 18.15 | 69.38 | 29.12 | 15.24 x 10.97 | 14.8 x 10.6 | 167 | 157 | 1.39 | utility | 12 | option-c-clean-sheet/basement_c.scad:73 |
| POOL ROOM | 69.38 | 18.15 | 96.33 | 52.76 | 26.95 x 34.61 | 25.8 x 33.9 | 933 | 875 | 1.28 | pit | 12 | option-c-clean-sheet/basement_c.scad:74 |
| POOL EQUIP. | 96.33 | 29.12 | 103.04 | 41.94 | 6.71 x 12.82 | 6.0 x 12.1 | 86 | 72 | 1.91 | utility | 12 | option-c-clean-sheet/basement_c.scad:75 |
| POOL BATH | 96.33 | 18.15 | 103.04 | 29.12 | 6.71 x 10.97 | 6.0 x 10.6 | 74 | 63 | 1.63 | bath | 12 | option-c-clean-sheet/basement_c.scad:76 |
| HALL @54.14,13.43 | 54.14 | 13.43 | 103.04 | 18.15 | 48.90 x 4.72 | 48.1 x 4.0 | 231 | 191 | 10.36 | hall | 12 | option-c-clean-sheet/basement_c.scad:77 |
| BATH @54.14,5.79 | 54.14 | 5.79 | 67.4 | 13.43 | 13.26 x 7.64 | 12.9 x 6.9 | 101 | 89 | 1.74 | bath | 12 | option-c-clean-sheet/basement_c.scad:78 |
| LAUNDRY | 67.4 | 5.79 | 81.68 | 13.43 | 14.28 x 7.64 | 13.5 x 6.9 | 109 | 93 | 1.87 | utility | 12 | option-c-clean-sheet/basement_c.scad:79 |
| EXIT STAIR | 45.6 | 63.16 | 66.8 | 67.75 | 21.20 x 4.59 | 20.1 x 3.5 | 97 | - | 4.62 | stairwell | 0 | option-c-clean-sheet/basement_c.scad:81 |

## Section 4

Door rows: `[x, y, axis, width, type, swing, tag]`; x,y is the LOW end. The model draws the leaf at the full opening width (house_lib.scad leaf()), so 'opening width' = the model's leaf width; 'approx clear' for a single swing door subtracts 1.5 in for the leaf and stop (a convention, not in model). Rooms on each side = innermost room at +/-0.8 ft from the opening midpoint (as tools/check_layout.py sides()).

### 4.1 Main floor schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| M1 | (4, 0) x | 16 ft = 192 in | garage | - | OUTSIDE / GARAGE | option-c-clean-sheet/main_floor_c.scad:98 |
| M2 | (27, 0) x | 3 ft = 36 in | door | 1 | MUD STOOP / MUDROOM | option-c-clean-sheet/main_floor_c.scad:99 |
| M3 | (70.5, 0) x | 3 ft = 36 in | door | 1 | FRONT PORCH / VESTIBULE | option-c-clean-sheet/main_floor_c.scad:100 |
| M4 | (68.3, 0) x | 2 ft = 24 in | glass | - | FRONT PORCH / VESTIBULE | option-c-clean-sheet/main_floor_c.scad:101 |
| M5 | (73.5, 0) x | 2 ft = 24 in | glass | - | FRONT PORCH / VESTIBULE | option-c-clean-sheet/main_floor_c.scad:102 |
| M6 | (57, 0) x | 6 ft = 72 in | double | 1 | FRONT PORCH / DINING | option-c-clean-sheet/main_floor_c.scad:103 |
| M7 | (49, 0) x | 3 ft = 36 in | door | 1 | FRONT PORCH / KITCHEN | option-c-clean-sheet/main_floor_c.scad:104 |
| M8 | (82, 0) x | 6 ft = 72 in | double | 1 | FRONT PORCH / LIVING ROOM | option-c-clean-sheet/main_floor_c.scad:105 |
| M9 | (108, 8) y | 5 ft = 60 in | double | 1 | SUN ROOM / PATIO | option-c-clean-sheet/main_floor_c.scad:106 |
| M10 | (108, 47) y | 5 ft = 60 in | double | 1 | MASTER BEDROOM / MASTER PORCH | option-c-clean-sheet/main_floor_c.scad:107 |
| M11 | (108, 38) y | 3 ft = 36 in | door | 1 | BEDROOM 2 / DECK | option-c-clean-sheet/main_floor_c.scad:108 |
| M12 | (22.16, 4) y | 3 ft = 36 in | door | 1 | GARAGE / MUDROOM | option-c-clean-sheet/main_floor_c.scad:110 |
| M13 | (22.16, 17) y | 3 ft = 36 in | door | 1 | GARAGE / SCULLERY / PANTRY | option-c-clean-sheet/main_floor_c.scad:111 |
| M14 | (29, 13) x | 3 ft = 36 in | door | -1 | MUDROOM / SCULLERY / PANTRY | option-c-clean-sheet/main_floor_c.scad:112 |
| M15 | (34, 2) y | 3 ft = 36 in | door | 1 | MUDROOM / KITCHEN | option-c-clean-sheet/main_floor_c.scad:113 |
| M16 | (34, 16) y | 3 ft = 36 in | door | 1 | SCULLERY / PANTRY / KITCHEN | option-c-clean-sheet/main_floor_c.scad:114 |
| M17 | (27, 26) x | 3 ft = 36 in | door | 1 | SCULLERY / PANTRY / DEN | option-c-clean-sheet/main_floor_c.scad:115 |
| M18 | (54, 6) y | 14 ft = 168 in | full | - | KITCHEN / DINING | option-c-clean-sheet/main_floor_c.scad:116 |
| M19 | (36, 26) x | 6 ft = 72 in | full | - | KITCHEN / DEN | option-c-clean-sheet/main_floor_c.scad:117 |
| M20 | (44, 26) x | 3 ft = 36 in | door | 1 | KITCHEN / BUTLER | option-c-clean-sheet/main_floor_c.scad:118 |
| M21 | (66, 10) y | 8 ft = 96 in | full | - | DINING / FOYER | option-c-clean-sheet/main_floor_c.scad:119 |
| M22 | (69, 7) x | 6 ft = 72 in | double | 1 | VESTIBULE / FOYER | option-c-clean-sheet/main_floor_c.scad:120 |
| M23 | (78, 10) y | 10 ft = 120 in | full | - | FOYER / LIVING ROOM | option-c-clean-sheet/main_floor_c.scad:121 |
| M24 | (94, 6) y | 12 ft = 144 in | full | - | LIVING ROOM / SUN ROOM | option-c-clean-sheet/main_floor_c.scad:122 |
| M25 | (66, 28) x | 6 ft = 72 in | full | - | FOYER / H1 | option-c-clean-sheet/main_floor_c.scad:124 |
| M26 | (66, 28.5) y | 3 ft = 36 in | door | -1 | POWDER / H1 | option-c-clean-sheet/main_floor_c.scad:125 |
| M27 | (66, 34) y | 3 ft = 36 in | door | -1 | COATS / H1 | option-c-clean-sheet/main_floor_c.scad:126 |
| M28 | (66, 41) y | 3 ft = 36 in | door | -1 | BROOM / H1 | option-c-clean-sheet/main_floor_c.scad:127 |
| M29 | (66, 47.6) y | 4 ft = 48 in | full | - | GALLERY / H1 | option-c-clean-sheet/main_floor_c.scad:128 |
| M30 | (47.27, 47.4) y | 4.4 ft = 52.8 in | full | - | (stair-top landing) / GALLERY | option-c-clean-sheet/main_floor_c.scad:129 |
| M31 | (42.65, 47.4) y | 4.4 ft = 52.8 in | full | - | (gallery, west) / (stair-top landing) | option-c-clean-sheet/main_floor_c.scad:130 |
| M32 | (42.9, 47.1) x | 4.1 ft = 49.2 in | full | - | STAIR DN / (stair-top landing) | option-c-clean-sheet/main_floor_c.scad:131 |
| M33 | (49, 47.1) x | 3 ft = 36 in | door | -1 | STORAGE / GALLERY | option-c-clean-sheet/main_floor_c.scad:132 |
| M34 | (30, 47.1) x | 3 ft = 36 in | door | -1 | DEN / (gallery, west) | option-c-clean-sheet/main_floor_c.scad:133 |
| M35 | (30, 52.1) x | 3 ft = 36 in | door | 1 | (gallery, west) / LIBRARY | option-c-clean-sheet/main_floor_c.scad:134 |
| M36 | (50, 52.1) x | 3 ft = 36 in | door | 1 | GALLERY / OFFICE | option-c-clean-sheet/main_floor_c.scad:135 |
| M37 | (61, 52.1) x | 3 ft = 36 in | door | 1 | GALLERY / BEDROOM 3 | option-c-clean-sheet/main_floor_c.scad:136 |
| M38 | (72, 37.5) y | 4 ft = 48 in | full | - | H1 / H4 | option-c-clean-sheet/main_floor_c.scad:138 |
| M39 | (79, 37) x | 3 ft = 36 in | door | -1 | BATH / H4 | option-c-clean-sheet/main_floor_c.scad:139 |
| M40 | (73, 37) x | 3 ft = 36 in | door | -1 | LINEN / H4 | option-c-clean-sheet/main_floor_c.scad:140 |
| M41 | (89, 37) x | 3 ft = 36 in | door | -1 | CLOSET / H4 | option-c-clean-sheet/main_floor_c.scad:141 |
| M42 | (94, 38.5) y | 3 ft = 36 in | door | 1 | H4 / BEDROOM 2 | option-c-clean-sheet/main_floor_c.scad:142 |
| M43 | (97, 28) x | 3 ft = 36 in | door | -1 | BATH 2 / BEDROOM 2 | option-c-clean-sheet/main_floor_c.scad:143 |
| M44 | (73, 42) x | 3 ft = 36 in | door | 1 | H4 / MASTER LAUNDRY | option-c-clean-sheet/main_floor_c.scad:144 |
| M45 | (89.5, 42) x | 3 ft = 36 in | door | 1 | H4 / MASTER BEDROOM | option-c-clean-sheet/main_floor_c.scad:145 |
| M46 | (80, 44) y | 3 ft = 36 in | door | -1 | MASTER LAUNDRY / WIC | option-c-clean-sheet/main_floor_c.scad:146 |
| M47 | (88, 43.5) y | 3 ft = 36 in | door | -1 | WIC / MASTER BEDROOM | option-c-clean-sheet/main_floor_c.scad:147 |
| M48 | (81, 52) x | 3 ft = 36 in | door | 1 | WIC / MASTER BATH | option-c-clean-sheet/main_floor_c.scad:148 |
| M49 | (88, 55) y | 3 ft = 36 in | door | -1 | MASTER BATH / MASTER BEDROOM | option-c-clean-sheet/main_floor_c.scad:149 |

### 4.2 Basement schedule

| # | pos (x,y) axis | opening width | type | swing | joins (low-side room / high-side room) | source |
|---|---|---|---|---|---|---|
| B1 | (38.4, 50.35) x | 2.8 ft = 33.6 in | door | 1 | HALL @37.37,35.08 / MUSIC ROOM | option-c-clean-sheet/basement_c.scad:86 |
| B2 | (42.65, 46.2) y | 2.8 ft = 33.6 in | door | 1 | HALL @37.37,35.08 / GYM | option-c-clean-sheet/basement_c.scad:87 |
| B3 | (37.37, 45.6) y | 2.8 ft = 33.6 in | door | -1 | STORAGE / HALL @37.37,35.08 | option-c-clean-sheet/basement_c.scad:88 |
| B4 | (37.37, 38.4) y | 3 ft = 36 in | door | -1 | UTILITY / HALL @37.37,35.08 | option-c-clean-sheet/basement_c.scad:89 |
| B5 | (37.6, 35.08) x | 4.8 ft = 57.6 in | full | - | HALLWAY / HALL @37.37,35.08 | option-c-clean-sheet/basement_c.scad:90 |
| B6 | (47.27, 28) y | 4.2 ft = 50.4 in | full | - | STAIR UP / STAIR FOOT | option-c-clean-sheet/basement_c.scad:91 |
| B7 | (49.2, 35.08) x | 2.8 ft = 33.6 in | door | 1 | STAIR FOOT / BATH @47.27,35.08 | option-c-clean-sheet/basement_c.scad:92 |
| B8 | (54.14, 31.7) y | 3 ft = 36 in | door | -1 | STAIR FOOT / HOME THEATER | option-c-clean-sheet/basement_c.scad:93 |
| B9 | (36, 27.6) x | 6.4 ft = 76.8 in | open | - | LIVING ROOM / HALLWAY | option-c-clean-sheet/basement_c.scad:94 |
| B10 | (50, 27.6) x | 4 ft = 48 in | open | - | LIVING ROOM / STAIR FOOT | option-c-clean-sheet/basement_c.scad:95 |
| B11 | (54.14, 13.8) y | 4 ft = 48 in | open | - | LIVING ROOM / HALL @54.14,13.43 | option-c-clean-sheet/basement_c.scad:96 |
| B12 | (56.5, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / PET ROOM | option-c-clean-sheet/basement_c.scad:97 |
| B13 | (71, 18.15) x | 3 ft = 36 in | door | 1 | HALL @54.14,13.43 / POOL ROOM | option-c-clean-sheet/basement_c.scad:98 |
| B14 | (96.33, 20.5) y | 2.8 ft = 33.6 in | door | 1 | POOL ROOM / POOL BATH | option-c-clean-sheet/basement_c.scad:99 |
| B15 | (99, 18.15) x | 2.8 ft = 33.6 in | door | 1 | HALL @54.14,13.43 / POOL BATH | option-c-clean-sheet/basement_c.scad:100 |
| B16 | (96.33, 33.5) y | 3 ft = 36 in | door | 1 | POOL ROOM / POOL EQUIP. | option-c-clean-sheet/basement_c.scad:101 |
| B17 | (59, 13.43) x | 2.8 ft = 33.6 in | door | -1 | BATH @54.14,5.79 / HALL @54.14,13.43 | option-c-clean-sheet/basement_c.scad:102 |
| B18 | (73, 13.43) x | 3 ft = 36 in | door | -1 | LAUNDRY / HALL @54.14,13.43 | option-c-clean-sheet/basement_c.scad:103 |
| B19 | (46.2, 63.16) x | 3.5 ft = 42 in | door | -1 | GYM / EXIT STAIR | option-c-clean-sheet/basement_c.scad:104 |

### 4.3 Width statistics

Main floor:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 0 | 30 | 30 |
| double | 0 | 0 | 5 | 5 |
| full | 0 | 0 | 11 | 11 |
| glass | 2 | 0 | 0 | 2 |
| garage | 0 | 0 | 1 | 1 |
| ALL | 2 | 0 | 47 | 49 |
| passage (door+double+slider+open) | 0 | 0 | 35 | 35 |

Basement:

| type | <32 in | 32-35 in | >=36 in | total |
|---|---|---|---|---|
| door | 0 | 7 | 7 | 14 |
| open | 0 | 0 | 3 | 3 |
| full | 0 | 0 | 2 | 2 |
| ALL | 0 | 7 | 12 | 19 |
| passage (door+double+slider+open) | 0 | 7 | 10 | 17 |

### 4.4 Every bedroom, bath, WC, closet/WIC/linen door (either side is kind bed/bath/closet)

Main:

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-c-clean-sheet/main_floor_c.scad:107 | MASTER BEDROOM / MASTER PORCH | double | 60 in | - |
| option-c-clean-sheet/main_floor_c.scad:108 | BEDROOM 2 / DECK | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:125 | POWDER / H1 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:126 | COATS / H1 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:127 | BROOM / H1 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:132 | STORAGE / GALLERY | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:136 | GALLERY / BEDROOM 3 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:139 | BATH / H4 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:140 | LINEN / H4 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:141 | CLOSET / H4 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:142 | H4 / BEDROOM 2 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:143 | BATH 2 / BEDROOM 2 | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:145 | H4 / MASTER BEDROOM | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:146 | MASTER LAUNDRY / WIC | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:147 | WIC / MASTER BEDROOM | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:148 | WIC / MASTER BATH | door | 36 in | 34.5 |
| option-c-clean-sheet/main_floor_c.scad:149 | MASTER BATH / MASTER BEDROOM | door | 36 in | 34.5 |

Basement (baths only; the basement has no bedrooms or closets except STORAGE kind closet):

| source | joins | type | opening width | approx clear (door: opening - 1.5 in) |
|---|---|---|---|---|
| option-c-clean-sheet/basement_c.scad:88 | STORAGE / HALL @37.37,35.08 | door | 33.6 in | 32.1 |
| option-c-clean-sheet/basement_c.scad:92 | STAIR FOOT / BATH @47.27,35.08 | door | 33.6 in | 32.1 |
| option-c-clean-sheet/basement_c.scad:99 | POOL ROOM / POOL BATH | door | 33.6 in | 32.1 |
| option-c-clean-sheet/basement_c.scad:100 | HALL @54.14,13.43 / POOL BATH | door | 33.6 in | 32.1 |
| option-c-clean-sheet/basement_c.scad:102 | BATH @54.14,5.79 / HALL @54.14,13.43 | door | 33.6 in | 32.1 |

## Section 5

Window rows: `[x, y, axis, width, sill, height]` (same low-end convention). Facade = the outdoor side of the wall (the side with no walled heated room).

### 5.1 Main floor

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| KITCHEN | S | (38.5, 0, 'x') | 7 | 3.5 | 4 | 28.0 | option-c-clean-sheet/main_floor_c.scad:154 |
| LIVING ROOM | S | (89.5, 0, 'x') | 3.9 | 2 | 6 | 23.4 | option-c-clean-sheet/main_floor_c.scad:155 |
| SUN ROOM | S | (95.5, 0, 'x') | 5 | 1.5 | 6.5 | 32.5 | option-c-clean-sheet/main_floor_c.scad:156 |
| SUN ROOM | S | (102.5, 0, 'x') | 4.5 | 1.5 | 6.5 | 29.2 | option-c-clean-sheet/main_floor_c.scad:157 |
| SUN ROOM | E | (108, 1.5, 'y') | 5 | 1.5 | 6.5 | 32.5 | option-c-clean-sheet/main_floor_c.scad:158 |
| SUN ROOM | E | (108, 15, 'y') | 5 | 1.5 | 6.5 | 32.5 | option-c-clean-sheet/main_floor_c.scad:159 |
| DEN | W | (22.16, 29, 'y') | 6 | 2.5 | 5 | 30.0 | option-c-clean-sheet/main_floor_c.scad:160 |
| LIBRARY | W | (22.16, 55, 'y') | 5 | 2.5 | 5 | 25.0 | option-c-clean-sheet/main_floor_c.scad:161 |
| LIBRARY | N | (28, 63.42, 'x') | 6 | 2.5 | 5 | 30.0 | option-c-clean-sheet/main_floor_c.scad:162 |
| OFFICE | N | (46, 63.42, 'x') | 6 | 2.5 | 5 | 30.0 | option-c-clean-sheet/main_floor_c.scad:163 |
| BEDROOM 3 | N | (67.4, 63.42, 'x') | 3.6 | 2.5 | 5 | 18.0 | option-c-clean-sheet/main_floor_c.scad:164 |
| MASTER BATH | N | (74, 63.42, 'x') | 3.5 | 4 | 3 | 10.5 | option-c-clean-sheet/main_floor_c.scad:165 |
| MASTER BEDROOM | N | (92, 63.42, 'x') | 5 | 2.5 | 5 | 25.0 | option-c-clean-sheet/main_floor_c.scad:166 |
| MASTER BEDROOM | N | (101, 63.42, 'x') | 5 | 2.5 | 5 | 25.0 | option-c-clean-sheet/main_floor_c.scad:167 |
| MASTER BEDROOM | E | (108, 58, 'y') | 4 | 2.5 | 5 | 20.0 | option-c-clean-sheet/main_floor_c.scad:168 |
| BEDROOM 2 | E | (108, 29, 'y') | 4.5 | 2.5 | 5 | 22.5 | option-c-clean-sheet/main_floor_c.scad:169 |
| BEDROOM 2 | E | (108, 33.8, 'y') | 3 | 2.5 | 5 | 15.0 | option-c-clean-sheet/main_floor_c.scad:170 |
| BATH 2 | E | (108, 23.5, 'y') | 3 | 4 | 3 | 9.0 | option-c-clean-sheet/main_floor_c.scad:171 |

Total main-floor window glass (width x height): 438.1 sq ft (18 windows; sliders/French doors/glass doors in main_doors are not included).

Facade counts: N: 6, S: 4, E: 6, W: 2

Rooms with windows on 2+ walls (main): SUN ROOM (E/S); LIBRARY (N/W); MASTER BEDROOM (E/N)

Heated main-floor rooms with NO window row (all kinds; baths, closets and halls included): 

| room | kind | area sf |
|---|---|---|
| MUDROOM | utility | 154 |
| SCULLERY / PANTRY | utility | 154 |
| DINING | dining | 312 |
| VESTIBULE | hall | 84 |
| FOYER | hall | 252 |
| BUTLER | utility | 164 |
| STORAGE | closet | 148 |
| POWDER | bath | 42 |
| COATS | closet | 42 |
| BROOM | closet | 43 |
| H1 | hall | 145 |
| (gallery, west) | hall | 102 |
| (stair-top landing) | hall | 23 |
| GALLERY | hall | 94 |
| H4 | hall | 110 |
| LINEN | closet | 54 |
| BATH | bath | 90 |
| CLOSET | closet | 54 |
| MASTER LAUNDRY | utility | 80 |
| WIC | closet | 80 |

### 5.2 Basement

| room | facade | pos (x,y,axis) | width ft | sill ft | height ft | glass sf | source |
|---|---|---|---|---|---|---|---|
| LIVING ROOM | S | (40, 5.79, 'x') | 8 | 4.5 | 4 | 32.0 | foundation.scad:160 |
| MUSIC ROOM | N | (33.15, 63.16, 'x') | 3 | 4.5 | 4 | 12.0 | foundation.scad:161 |

Rooms with windows on 2+ walls (basement): none

Basement rooms with no window row: GYM (rec, 205 sf); STORAGE (closet, 115 sf); UTILITY (utility, 117 sf); HALL @37.37,35.08 (hall, 81 sf); STAIR UP (stair, 82 sf); BATH @47.27,35.08 (bath, 70 sf); HALLWAY (hall, 55 sf); STAIR FOOT (hall, 51 sf); HOME THEATER (tiered, 324 sf); PET ROOM (utility, 167 sf); POOL ROOM (pit, 933 sf); POOL EQUIP. (utility, 86 sf); POOL BATH (bath, 74 sf); HALL @54.14,13.43 (hall, 231 sf); BATH @54.14,5.79 (bath, 101 sf); LAUNDRY (utility, 109 sf)

## Section 6

**Definition.** Circulation = rooms of kind `hall` (halls, corridors, galleries, vestibules, landings) in the model's own classification, excluding the foyer (also kind hall) which is shown on its own line. The mudroom (kind utility), the stair flight/opening, porches and the garage are never in the total. Percent = circulation sq ft / conditioned sq ft (the §1.1 row sums, main incl. stairwell footprint).

### 6.1 Main floor

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| H1 | 66,28 to 72,52.1 | 145 | 5.6 ft clear width (67 in), length 23.7 | option-c-clean-sheet/main_floor_c.scad:68 |
| (gallery, west) | 22.16,47.1 to 42.65,52.1 | 102 | 4.6 ft clear width (55 in), length 20.1 | option-c-clean-sheet/main_floor_c.scad:69 |
| (stair-top landing) | 42.65,47.1 to 47.27,52.1 | 23 | 4.2 ft clear width (51 in), length 4.6 | option-c-clean-sheet/main_floor_c.scad:70 |
| GALLERY | 47.27,47.1 to 66,52.1 | 94 | 4.6 ft clear width (55 in), length 18.3 | option-c-clean-sheet/main_floor_c.scad:71 |
| H4 | 72,37 to 94,42 | 110 | 4.6 ft clear width (55 in), length 21.6 | option-c-clean-sheet/main_floor_c.scad:72 |

**Circulation total (halls only): 474 sq ft = 8.7% of 5444 sq ft conditioned** (8.8% if the stair opening is excluded from the denominator).

| Separate lines (not in total) | area c/l sf | clear width | % of conditioned if added | source |
|---|---|---|---|---|
| FOYER | 84 | 6.6 ft | 10.2% | option-c-clean-sheet/main_floor_c.scad:55 |
| MUDROOM | 154 | 11.4 ft | 13.1% (halls+foyer+mudroom) | option-c-clean-sheet/main_floor_c.scad:51 |
| STAIR DN opening (stairwell) | 54 | 4.2 ft | 14.1% (all four) | option-c-clean-sheet/main_floor_c.scad:62 |

### 6.2 Basement

| Circulation room | rect | area c/l sf | clear width, length | source |
|---|---|---|---|---|
| HALL @37.37,35.08 | 37.37,35.08 to 42.65,50.35 | 81 | 4.9 ft clear width (59 in), length 14.9 | option-c-clean-sheet/basement_c.scad:66 |
| HALLWAY | 35.27,27.6 to 42.65,35.08 | 55 | 6.6 ft clear width (80 in), length 7.1 | option-c-clean-sheet/basement_c.scad:69 |
| STAIR FOOT | 47.27,27.6 to 54.14,35.08 | 51 | 6.5 ft clear width (78 in), length 7.1 | option-c-clean-sheet/basement_c.scad:70 |
| HALL @54.14,13.43 | 54.14,13.43 to 103.04,18.15 | 231 | 4.0 ft clear width (48 in), length 48.1 | option-c-clean-sheet/basement_c.scad:77 |

**Circulation total (halls only): 418 sq ft = 12.0% of 3475 sq ft** (rooms sum, excl. EXIT STAIR areaway).

| Separate line (not in total) | area c/l sf | clear width | % if added | source |
|---|---|---|---|---|
| STAIR UP (stair flight room, y 28.725..45.34) | 82 | 4.2 ft | 14.4% | option-c-clean-sheet/basement_c.scad:67 |

Note: the basement's long HALL (y 13.43..18.15) and HALLWAY pieces are kind `hall`; theatre and pool-room 'pit/tiered' rooms are rooms, not circulation.

## Section 7

Adjacency = rooms joined by a door row of any type (door, double, open, full, slider, glass); a `full` row is a wall-free opening. **Open zones:** a ceiling-0 non-porch room (stair landing, STAIR DN, basement HALLWAY) is treated as connected to another ceiling-0 room it physically abuts (no wall on either side). A ceiling-0 room abutting a walled room is NOT connected unless a door row is there (the neighbour's wall is on the shared edge). Porch rows (kind porch) are outside nodes: listed but never walked through.

Virtual connectors (open-zone abutments, main): FRONT PORCH <-> MUD STOOP (6.0 ft shared edge); PATIO <-> DECK (10.0 ft shared edge); MASTER PORCH <-> DECK (10.0 ft shared edge)

Basement: none

### 7.1 Main-floor adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| GARAGE | garage | MUDROOM; SCULLERY / PANTRY | garage to outside (option-c-clean-sheet/main_floor_c.scad:98) |
| MUDROOM | utility | GARAGE; KITCHEN; MUD STOOP; SCULLERY / PANTRY | - |
| SCULLERY / PANTRY | utility | DEN; GARAGE; KITCHEN; MUDROOM | - |
| KITCHEN | kitchen | BUTLER; DEN; DINING; FRONT PORCH; MUDROOM; SCULLERY / PANTRY | - |
| DINING | dining | FOYER; FRONT PORCH; KITCHEN | - |
| VESTIBULE | hall | FOYER; FRONT PORCH | - |
| FOYER | hall | DINING; H1; LIVING ROOM; VESTIBULE | - |
| LIVING ROOM | living | FOYER; FRONT PORCH; SUN ROOM | - |
| SUN ROOM | living | LIVING ROOM; PATIO | - |
| DEN | living | (gallery, west); KITCHEN; SCULLERY / PANTRY | - |
| BUTLER | utility | KITCHEN | - |
| STAIR DN | stairwell, ceiling 0 (open zone) | (stair-top landing) | - |
| STORAGE | closet | GALLERY | - |
| POWDER | bath | H1 | - |
| COATS | closet | H1 | - |
| BROOM | closet | H1 | - |
| H1 | hall | BROOM; COATS; FOYER; GALLERY; H4; POWDER | - |
| (gallery, west) | hall | (stair-top landing); DEN; LIBRARY | - |
| (stair-top landing) | hall | (gallery, west); GALLERY; STAIR DN | - |
| GALLERY | hall | (stair-top landing); BEDROOM 3; H1; OFFICE; STORAGE | - |
| H4 | hall | BATH; BEDROOM 2; CLOSET; H1; LINEN; MASTER BEDROOM; MASTER LAUNDRY | - |
| LIBRARY | office | (gallery, west) | - |
| OFFICE | office | GALLERY | - |
| BEDROOM 3 | bed | GALLERY | - |
| LINEN | closet | H4 | - |
| BATH | bath | H4 | - |
| CLOSET | closet | H4 | - |
| BEDROOM 2 | bed | BATH 2; DECK; H4 | - |
| BATH 2 | bath | BEDROOM 2 | - |
| MASTER BEDROOM | bed | H4; MASTER BATH; MASTER PORCH; WIC | - |
| MASTER LAUNDRY | utility | H4; WIC | - |
| WIC | closet | MASTER BATH; MASTER BEDROOM; MASTER LAUNDRY | - |
| MASTER BATH | bath | MASTER BEDROOM; WIC | - |
| FRONT PORCH | porch, ceiling 0 (open zone) | DINING; KITCHEN; LIVING ROOM; MUD STOOP; VESTIBULE | - |
| MUD STOOP | porch, ceiling 0 (open zone) | FRONT PORCH; MUDROOM | - |
| PATIO | porch, ceiling 0 (open zone) | DECK; SUN ROOM | - |
| MASTER PORCH | porch, ceiling 0 (open zone) | DECK; MASTER BEDROOM | - |
| DECK | porch, ceiling 0 (open zone) | BEDROOM 2; MASTER PORCH; PATIO | - |

### 7.2 Basement adjacency

| Room | kind | rooms reachable through one door/opening | exterior doors |
|---|---|---|---|
| MUSIC ROOM | living | HALL @37.37,35.08 | - |
| GYM | rec | EXIT STAIR; HALL @37.37,35.08 | - |
| STORAGE | closet | HALL @37.37,35.08 | - |
| UTILITY | utility | HALL @37.37,35.08 | - |
| HALL @37.37,35.08 | hall | GYM; HALLWAY; MUSIC ROOM; STORAGE; UTILITY | - |
| STAIR UP | stair | STAIR FOOT | - |
| BATH @47.27,35.08 | bath | STAIR FOOT | - |
| HALLWAY | hall, ceiling 0 (open zone) | HALL @37.37,35.08; LIVING ROOM | - |
| STAIR FOOT | hall, ceiling 0 (open zone) | BATH @47.27,35.08; HOME THEATER; LIVING ROOM; STAIR UP | - |
| LIVING ROOM | living | HALL @54.14,13.43; HALLWAY; STAIR FOOT | - |
| HOME THEATER | tiered | STAIR FOOT | - |
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
| front door -> kitchen/dining room centre | 38.3 | VESTIBULE > FOYER > DINING > KITCHEN |
| front door -> range (option-c-clean-sheet/main_floor_c.scad:181) | 47.2 | VESTIBULE > FOYER > DINING > KITCHEN |
| garage (room centre) -> kitchen/dining room centre | 35.2 | GARAGE > SCULLERY / PANTRY > KITCHEN |
| garage (room centre) -> range | 31.9 | GARAGE > SCULLERY / PANTRY > KITCHEN |
| garage (room centre) -> SCULLERY / PANTRY centre | 18.4 | GARAGE > SCULLERY / PANTRY |
| garage (room centre) -> tall pantry cabinets in kitchen (option-c-clean-sheet/main_floor_c.scad:185) | 31.8 | GARAGE > SCULLERY / PANTRY > KITCHEN |
| master bedroom centre -> WIC centre | 17.1 | MASTER BEDROOM > WIC |
| master bedroom centre -> MASTER LAUNDRY centre | 24.9 | MASTER BEDROOM > WIC > MASTER LAUNDRY |
| BEDROOM 3 centre -> hall BATH centre | 36.7 | BEDROOM 3 > GALLERY > H1 > H4 > BATH |
| BEDROOM 3 centre -> BATH 2 centre | 61.4 | BEDROOM 3 > GALLERY > H1 > H4 > BEDROOM 2 > BATH 2 |
| BEDROOM 3 centre -> MASTER BATH centre | 46.0 | BEDROOM 3 > GALLERY > H1 > H4 > MASTER LAUNDRY > WIC > MASTER BATH |
| BEDROOM 3 centre -> MASTER LAUNDRY centre | 31.5 | BEDROOM 3 > GALLERY > H1 > H4 > MASTER LAUNDRY |
| BEDROOM 2 centre -> hall BATH centre | 27.6 | BEDROOM 2 > H4 > BATH |
| BEDROOM 2 centre -> BATH 2 centre | 11.3 | BEDROOM 2 > BATH 2 |
| BEDROOM 2 centre -> MASTER BATH centre | 31.6 | BEDROOM 2 > H4 > MASTER BEDROOM > WIC > MASTER BATH |
| BEDROOM 2 centre -> MASTER LAUNDRY centre | 28.7 | BEDROOM 2 > H4 > MASTER BEDROOM > WIC > MASTER LAUNDRY |
| foyer centre -> POWDER centre (powder room) | 31.4 | VESTIBULE > FOYER > H1 > POWDER |
| front door -> top of main stair (top nosing, (44.96, 47.1)) | 72.2 | VESTIBULE > FOYER > H1 > GALLERY > (stair-top landing) |
| master bedroom centre -> top of main stair (top nosing, (44.96, 47.1)) | 64.6 | MASTER BEDROOM > WIC > MASTER LAUNDRY > H4 > H1 > GALLERY > (stair-top landing) |
| BEDROOM 3 centre -> top of main stair (top nosing, (44.96, 47.1)) | 25.5 | BEDROOM 3 > GALLERY > (stair-top landing) |
| BEDROOM 2 centre -> top of main stair (top nosing, (44.96, 47.1)) | 64.5 | BEDROOM 2 > H4 > H1 > GALLERY > (stair-top landing) |
| basement stair foot (44.96, 27.6) -> UTILITY centre | 26.4 | LIVING ROOM > HALLWAY > HALL @37.37,35.08 > UTILITY |

Main stair flight itself: 18.38 ft of plan run between top nosing y=47.1 and foot y=28.725 (model.json stair).

Master bed to WIC passes through the master bath? WIC centre: no (via MASTER BEDROOM > WIC)

## Section 8

### 8.1 LIVING ROOM (main; option-c-clean-sheet/main_floor_c.scad:57) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| VESTIBULE | hall | 7.0 | - |
| FOYER | hall | 21.0 | full 120 in |
| SUN ROOM | living | 22.0 | full 144 in |
| BATH | bath | 10.0 | - |
| CLOSET | closet | 6.0 | - |
| BATH 2 | bath | 6.0 | - |
| FRONT PORCH | porch (ceil 0) | 16.0 | double 72 in |

### 8.1 DEN (main; option-c-clean-sheet/main_floor_c.scad:60) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| SCULLERY / PANTRY | utility | 11.8 | door 36 in |
| KITCHEN | kitchen | 8.6 | full 72 in |
| BUTLER | utility | 9.5 | - |
| STAIR DN | stairwell (ceil 0) | 11.6 | - |
| (gallery, west) | hall | 20.5 | door 36 in |

### 8.1 SUN ROOM (main; option-c-clean-sheet/main_floor_c.scad:58) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| LIVING ROOM | living | 22.0 | full 144 in |
| BATH 2 | bath | 14.0 | - |
| FRONT PORCH | porch (ceil 0) | 14.0 | - |
| PATIO | porch (ceil 0) | 22.0 | double 60 in |

The model has no room labelled 'family room'; the main-floor living-type rooms (kind living) are LIVING ROOM, DEN, SUN ROOM. Basement LIVING ROOM:

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| STAIR UP | stair | 4.6 | - |
| HALLWAY | hall (ceil 0) | 7.4 | open 76.8 in |
| STAIR FOOT | hall (ceil 0) | 6.9 | open 48 in |
| PET ROOM | utility | 9.5 | - |
| HALL @54.14,13.43 | hall | 4.7 | open 48 in |
| BATH @54.14,5.79 | bath | 7.6 | - |

### 8.2 FOYER (option-c-clean-sheet/main_floor_c.scad:55) shares walls with

| shares a wall with | kind | shared length ft | door/opening between |
|---|---|---|---|
| DINING | dining | 7.0 | - |
| FOYER | hall | 12.0 | double 72 in |
| LIVING ROOM | living | 7.0 | - |
| FRONT PORCH | porch (ceil 0) | 12.0 | door 36 in, glass 24 in, glass 24 in |

### 8.3 Closets, WICs, linen, scullery/pantry, storage: exterior exposure

Pantry-like rooms: SCULLERY / PANTRY.

| level | room | source | sides touching outside/porch/garage/soil (ft) |
|---|---|---|---|
| main | SCULLERY / PANTRY | option-c-clean-sheet/main_floor_c.scad:52 | W 13.0 (garage) |
| main | STORAGE | option-c-clean-sheet/main_floor_c.scad:63 | none |
| main | COATS | option-c-clean-sheet/main_floor_c.scad:65 | none |
| main | BROOM | option-c-clean-sheet/main_floor_c.scad:66 | none |
| main | LINEN | option-c-clean-sheet/main_floor_c.scad:78 | none |
| main | CLOSET | option-c-clean-sheet/main_floor_c.scad:80 | none |
| main | WIC | option-c-clean-sheet/main_floor_c.scad:85 | none |
| base | STORAGE | option-c-clean-sheet/basement_c.scad:64 | W 7.6 (yard/soil) |

Pantry/garage: SCULLERY / PANTRY shares 13.0 ft of wall with the garage; doors between SCULLERY / PANTRY and GARAGE: 1. The garage's doors to the house are: option-c-clean-sheet/main_floor_c.scad:110 (GARAGE | MUDROOM, 36 in); option-c-clean-sheet/main_floor_c.scad:111 (GARAGE | SCULLERY / PANTRY, 36 in). The tall pantry cabinets (x 34.4-36.9) are 12.2 ft east of the garage wall (x 22.16): no shared wall.

### 8.4 Rooms containing kitchen-type fixtures (comment keywords range/sink/island/fridge/washer/dryer/prep) and which §7 paths cross them

| room | fixtures (source line) | §7 paths passing through (as a room walked through or ending in) |
|---|---|---|
| KITCHEN | sink (178); dishwasher beside the sink (179); range (181); fridge (at a run end, by the pantry) (182); island (184) | front door -> kitchen/dining room centre; front door -> range (option-c-clean-sheet/main_floor_c.scad:181); garage (room centre) -> kitchen/dining room centre; garage (room centre) -> range; garage (room centre) -> tall pantry cabinets in kitchen (option-c-clean-sheet/main_floor_c.scad:185) |

No dishwasher row exists in main_fixtures (not in model).

### 8.5 Rooms within 40 ft of a drive edge (phase house, site.scad:108-118; distance from the room's centre-line rectangle to the nearest drive rectangle edge)

| room | distance ft | nearest drive piece | exterior sides |
|---|---|---|---|
| GARAGE | 2.0 | west driveway (site.scad:111) | N 22.2 (yard/soil); S 22.2 (yard/soil); W 26.0 (yard/soil) |
| MUDROOM | 14.0 | loop north leg (:114) | S 11.8 (porch/patio (open)); W 13.0 (garage) |
| KITCHEN | 14.0 | loop north leg (:114) | N 0.1 (yard/soil); S 20.0 (porch/patio (open)) |
| DINING | 14.0 | loop north leg (:114) | S 12.0 (porch/patio (open)) |
| VESTIBULE | 14.0 | loop north leg (:114) | S 12.0 (porch/patio (open)) |
| LIVING ROOM | 14.0 | loop north leg (:114) | S 16.0 (porch/patio (open)) |
| SUN ROOM | 14.0 | loop north leg (:114) | S 14.0 (porch/patio (open)); E 22.0 (porch/patio (open)) |
| FOYER | 21.0 | loop north leg (:114) | none |
| SCULLERY / PANTRY | 24.2 | west driveway (site.scad:111) | W 13.0 (garage) |
| DEN | 24.2 | west driveway (site.scad:111) | W 21.1 (yard/soil) |
| (gallery, west) | 24.7 | west driveway (site.scad:111) | W 5.0 (yard/soil) |
| LIBRARY | 26.2 | west driveway (site.scad:111) | N 20.5 (yard/soil); W 11.3 (yard/soil) |
| BATH 2 | 36.0 | loop north leg (:114) | E 6.0 (porch/patio (open)) |
| BUTLER | 40.0 | loop north leg (:114) | none |
| POWDER | 40.0 | loop north leg (:114) | none |

Other rooms are > 40 ft from any drive. Garage doors (rows option-c-clean-sheet/main_floor_c.scad:98) face S; garage rectangle to the nearest drive piece: 2.0 ft.

## Section 9

Wet fixtures = sinks, vanities, toilets, tubs, showers, washers, dog wash (those with water + drain). Identified by hand from the box coordinates and source comments (the tables carry no type field): boxes are listed exactly so the mapping can be checked. Range, fridge and the basement equipment are in the second list (supply/fuel not stated in model).

### 9.1 Main floor wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| sink (KITCHEN) | KITCHEN | (40, 0.6, 43, 2.2) | (41.5, 1.4) | S wall y=0 | 0.60 | option-c-clean-sheet/main_floor_c.scad:178 |
| toilet/tub/wash basin (POWDER) | POWDER | (60.5, 29.5, 62.3, 31.5) | (61.4, 30.5) | W wall x=60 | 0.50 | option-c-clean-sheet/main_floor_c.scad:199 |
| vanity (POWDER) | POWDER | (60.4, 26.4, 62.4, 28) | (61.4, 27.2) | S wall y=26 | 0.40 | option-c-clean-sheet/main_floor_c.scad:200 |
| toilet/tub/wash basin (BATH) | BATH | (86, 30, 87.8, 32) | (86.9, 31.0) | E wall x=88 | 0.20 | option-c-clean-sheet/main_floor_c.scad:216 |
| shower (BATH) | BATH | (78.4, 28.4, 83, 30.4) | (80.7, 29.4) | S wall y=28 | 0.40 | option-c-clean-sheet/main_floor_c.scad:217 |
| vanity (BATH) | BATH | (84, 35, 87.6, 36.6) | (85.8, 35.8) | N wall y=37 | 0.40 | option-c-clean-sheet/main_floor_c.scad:218 |
| toilet/tub/wash basin (BATH 2) | BATH 2 | (94.4, 23, 96.4, 25) | (95.4, 24.0) | W wall x=94 | 0.40 | option-c-clean-sheet/main_floor_c.scad:219 |
| vanity (BATH 2) | BATH 2 | (97.4, 22.4, 101, 24) | (99.2, 23.2) | S wall y=22 | 0.40 | option-c-clean-sheet/main_floor_c.scad:220 |
| shower (BATH 2) | BATH 2 | (102, 22.4, 107.6, 26) | (104.8, 24.2) | S wall y=22 | 0.40 | option-c-clean-sheet/main_floor_c.scad:221 |
| washer/dryer (MASTER LAUNDRY) | MASTER LAUNDRY | (74.6, 49.6, 79.6, 51.6) | (77.1, 50.6) | N wall y=52 | 0.40 | option-c-clean-sheet/main_floor_c.scad:229 |
| sink (MASTER LAUNDRY) | MASTER LAUNDRY | (72.5, 47, 74.1, 48.6) | (73.3, 47.8) | W wall x=72 | 0.50 | option-c-clean-sheet/main_floor_c.scad:231 |
| shower (MASTER BATH) | MASTER BATH | (72.4, 53, 78.4, 58) | (75.4, 55.5) | W wall x=72 | 0.40 | option-c-clean-sheet/main_floor_c.scad:237 |
| toilet/tub/wash basin (MASTER BATH) | MASTER BATH | (72.4, 59, 78, 63) | (75.2, 61.0) | W wall x=72 | 0.40 | option-c-clean-sheet/main_floor_c.scad:238 |
| vanity (MASTER BATH) | MASTER BATH | (80, 61.6, 86.8, 63.1) | (83.4, 62.4) | N wall y=63.42 | 0.32 | option-c-clean-sheet/main_floor_c.scad:239 |
| toilet/tub/wash basin (MASTER BATH) | MASTER BATH | (86.6, 53.2, 87.6, 55) | (87.1, 54.1) | E wall x=88 | 0.40 | option-c-clean-sheet/main_floor_c.scad:240 |

(equipment list omitted in variant mode)

### 9.2 Basement wet fixtures

| fixture | room | box (x0,y0,x1,y1) | centre | nearest wall | gap ft | source |
|---|---|---|---|---|---|---|
| toilet/tub/wash basin (BATH @47.27,35.08) | BATH @47.27,35.08 | (52, 41.5, 53.8, 43.3) | (52.9, 42.4) | E wall x=54.14 | 0.34 | option-c-clean-sheet/basement_c.scad:128 |
| vanity (BATH @47.27,35.08) | BATH @47.27,35.08 | (52.1, 38.5, 53.9, 41) | (53.0, 39.8) | E wall x=54.14 | 0.24 | option-c-clean-sheet/basement_c.scad:129 |
| shower (BATH @47.27,35.08) | BATH @47.27,35.08 | (47.6, 42, 50.6, 45) | (49.1, 43.5) | W wall x=47.27 | 0.33 | option-c-clean-sheet/basement_c.scad:130 |
| toilet/tub/wash basin (POOL BATH) | POOL BATH | (100.6, 22.5, 102.4, 24.3) | (101.5, 23.4) | E wall x=103.04 | 0.64 | option-c-clean-sheet/basement_c.scad:131 |
| vanity (POOL BATH) | POOL BATH | (96.6, 25.5, 98.6, 28.8) | (97.6, 27.1) | W wall x=96.33 | 0.27 | option-c-clean-sheet/basement_c.scad:132 |
| shower (POOL BATH) | POOL BATH | (99.2, 25.4, 102.45, 28.9) | (100.8, 27.1) | N wall y=29.12 | 0.22 | option-c-clean-sheet/basement_c.scad:133 |
| toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | (54.4, 6.4, 59.4, 8.95) | (56.9, 7.7) | W wall x=54.14 | 0.26 | option-c-clean-sheet/basement_c.scad:134 |
| vanity (BATH @54.14,5.79) | BATH @54.14,5.79 | (62.5, 6.4, 67.1, 8.25) | (64.8, 7.3) | E wall x=67.4 | 0.30 | option-c-clean-sheet/basement_c.scad:135 |
| toilet/tub/wash basin (BATH @54.14,5.79) | BATH @54.14,5.79 | (65.2, 9.5, 67.1, 11.3) | (66.2, 10.4) | E wall x=67.4 | 0.30 | option-c-clean-sheet/basement_c.scad:136 |
| washer/dryer (LAUNDRY) | LAUNDRY | (67.8, 6.4, 72.6, 8.75) | (70.2, 7.6) | W wall x=67.4 | 0.40 | option-c-clean-sheet/basement_c.scad:138 |
| toilet/tub/wash basin (PET ROOM) | PET ROOM | (65.5, 26.5, 69, 28.9) | (67.2, 27.7) | N wall y=29.12 | 0.22 | option-c-clean-sheet/basement_c.scad:140 |

(equipment list omitted in variant mode)

Pool shell: x 75.07-90.04, y 32.66-47.7 (15 x 15) and spa x 82.07-90.04, y 23.77-31.91 (foundation.scad:57-58); floor drains, sump, pool drains and the main drain are NOT in the room/fixture tables (Redesign doc mentions a main-drain sump, lines 345, 497; no location in model).

### 9.3 Wet walls (definition and result)

**Definition.** For each wet fixture, the wall = the nearest centre line of its room (gap <= 3 ft; farther = free-standing island, its own group). Fixtures are in the same group if their walls are parallel, the same line within 1.0 ft, and their extents along the wall are <= 8 ft apart (chaining limit, my assumption). Back-to-back fixtures on opposite faces of one wall share a coordinate, so group together.

Main floor:

| wet group | fixtures | rooms | wall line(s) | centroid (x,y) |
|---|---|---|---|---|
| G1 | sink (KITCHEN) | KITCHEN | y=0 (horizontal wall) | (41.5, 1.4) |
| G2 | vanity (BATH 2); shower (BATH 2) | BATH 2 | y=22 (horizontal wall) | (102.0, 23.7) |
| G3 | toilet/tub/wash basin (BATH 2) | BATH 2 | x=94 (vertical wall) | (95.4, 24.0) |
| G4 | vanity (POWDER) | POWDER | y=26 (horizontal wall) | (61.4, 27.2) |
| G5 | shower (BATH) | BATH | y=28 (horizontal wall) | (80.7, 29.4) |
| G6 | toilet/tub/wash basin (POWDER) | POWDER | x=60 (vertical wall) | (61.4, 30.5) |
| G7 | toilet/tub/wash basin (BATH) | BATH | x=88 (vertical wall) | (86.9, 31.0) |
| G8 | vanity (BATH) | BATH | y=37 (horizontal wall) | (85.8, 35.8) |
| G9 | sink (MASTER LAUNDRY); shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | MASTER BATH; MASTER LAUNDRY | x=72 (vertical wall) | (74.6, 54.8) |
| G10 | washer/dryer (MASTER LAUNDRY) | MASTER LAUNDRY | y=52 (horizontal wall) | (77.1, 50.6) |
| G11 | toilet/tub/wash basin (MASTER BATH) | MASTER BATH | x=88 (vertical wall) | (87.1, 54.1) |
| G12 | vanity (MASTER BATH) | MASTER BATH | y=63.42 (horizontal wall) | (83.4, 62.4) |

**Main floor: 12 wet-wall groups** (5 back-to-back plumbing clusters of rooms: KITCHEN | POWDER | BATH | BATH 2 | MASTER LAUNDRY+MASTER BATH)

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

Sensitivity of the group count to the along-wall chaining limit (main / basement): 4 ft: 13/8; 6 ft: 12/8; 8 ft: 12/8; 12 ft: 12/8; inf: 11/6

### 9.4 Stacking: horizontal offset from each main-floor group to the nearest basement group

There is no plumbing chase modelled (not in model). Offset = |dx|,|dy| between centroids; Manhattan = sum. The basement UTILITY room (water heater at (30.1,36.8)) is 'basement mechanical', not a wet wall.

| main group | members | centroid | nearest basement group | its centroid | dx | dy | Manhattan ft |
|---|---|---|---|---|---|---|---|
| G1 | sink (KITCHEN) | (41.5,1.4) | B2 (BATH @54.14,5.79) | (56.9,7.7) | 15.4 | 6.3 | 21.7 |
| G2 | vanity (BATH 2); shower (BATH 2) | (102.0,23.7) | B3 (POOL BATH) | (101.5,23.4) | 0.5 | 0.3 | 0.8 |
| G3 | toilet/tub/wash basin (BATH 2) | (95.4,24.0) | B4 (POOL BATH) | (97.6,27.1) | 2.2 | 3.1 | 5.3 |
| G4 | vanity (POWDER) | (61.4,27.2) | B6 (PET ROOM) | (67.2,27.7) | 5.9 | 0.5 | 6.4 |
| G5 | shower (BATH) | (80.7,29.4) | B6 (PET ROOM) | (67.2,27.7) | 13.5 | 1.7 | 15.2 |
| G6 | toilet/tub/wash basin (POWDER) | (61.4,30.5) | B6 (PET ROOM) | (67.2,27.7) | 5.9 | 2.8 | 8.7 |
| G7 | toilet/tub/wash basin (BATH) | (86.9,31.0) | B4 (POOL BATH) | (97.6,27.1) | 10.7 | 3.9 | 14.5 |
| G8 | vanity (BATH) | (85.8,35.8) | B4 (POOL BATH) | (97.6,27.1) | 11.8 | 8.6 | 20.4 |
| G9 | sink (MASTER LAUNDRY); shower (MASTER BATH); toilet/tub/wash basin (MASTER BATH) | (74.6,54.8) | B6 (PET ROOM) | (67.2,27.7) | 7.4 | 27.1 | 34.5 |
| G10 | washer/dryer (MASTER LAUNDRY) | (77.1,50.6) | B6 (PET ROOM) | (67.2,27.7) | 9.8 | 22.9 | 32.8 |
| G11 | toilet/tub/wash basin (MASTER BATH) | (87.1,54.1) | B4 (POOL BATH) | (97.6,27.1) | 10.5 | 27.0 | 37.5 |
| G12 | vanity (MASTER BATH) | (83.4,62.4) | B4 (POOL BATH) | (97.6,27.1) | 14.2 | 35.2 | 49.4 |

Main-floor groups with a basement group within 5 ft Manhattan: 1 of 12; within 10 ft: 4.

### 9.5 Drain-run index (used for all layout options)

**DRI = sum over main-floor wet groups of the Manhattan distance (ft, plan) from the group centroid to the building-drain exit point E.** E is not stated as a number in any doc; the model draws the building sewer leaving the basement west wall at (22.16, 58) toward the tank (site.scad:188 `dashed([[22.16, 58], [t[2], 58]])`, tank face x=3). E = (22.16, 58.0). (Note site.scad:185-187 and the Redesign/permit text say 'by the UTILITY room', which is at y 35.08-42.77; see §15.)

| group | centroid | Manhattan to E | to alt E (22.16, 38.9) UTILITY west wall |
|---|---|---|---|
| G1 | (41.5,1.4) | 75.9 | 56.8 |
| G2 | (102.0,23.7) | 114.1 | 95.0 |
| G3 | (95.4,24.0) | 107.2 | 88.1 |
| G4 | (61.4,27.2) | 70.0 | 50.9 |
| G5 | (80.7,29.4) | 87.1 | 68.0 |
| G6 | (61.4,30.5) | 66.7 | 47.6 |
| G7 | (86.9,31.0) | 91.7 | 72.6 |
| G8 | (85.8,35.8) | 85.8 | 66.7 |
| G9 | (74.6,54.8) | 55.7 | 68.3 |
| G10 | (77.1,50.6) | 62.3 | 66.6 |
| G11 | (87.1,54.1) | 68.8 | 80.1 |
| G12 | (83.4,62.4) | 65.6 | 84.7 |

**DRI (E = (22.16, 58)) = 951.3 ft over 12 groups; mean 79.3 ft.** Sensitivity: with E at the UTILITY west wall (22.16, 38.9) the same sum is 845.8 ft.

### 9.6 Water heater / boiler to the furthest fixture

Water heater centre (30.1, 36.8) (basement.scad:144, identified as the third equipment box in the comment list at basement.scad:135); boiler centre (27.4, 36.7) (basement.scad:143). The model has ONE boiler and ONE water heater, both in the basement UTILITY room; no recirculation loop or other heater is modelled.

- Furthest main-floor fixture from the water heater (plan Manhattan): **shower (BATH 2), 87.3 ft** (plus ~13.75 ft vertical floor-to-floor; the runs go under the main floor). From the boiler: shower (BATH 2), 89.9 ft.
- Furthest basement fixture: **toilet/tub/wash basin (POOL BATH), 84.8 ft** from the water heater.
- Nearest main-floor fixture: toilet/tub/wash basin (POWDER), 37.6 ft.

Per fixture (Manhattan plan ft from the water heater): sink (KITCHEN) 47; toilet/tub/wash basin (POWDER) 38; vanity (POWDER) 41; toilet/tub/wash basin (BATH) 63; shower (BATH) 58; vanity (BATH) 57; toilet/tub/wash basin (BATH 2) 78; vanity (BATH 2) 83; shower (BATH 2) 87; washer/dryer (MASTER LAUNDRY) 61; sink (MASTER LAUNDRY) 54; shower (MASTER BATH) 64; toilet/tub/wash basin (MASTER BATH) 69; vanity (MASTER BATH) 79; toilet/tub/wash basin (MASTER BATH) 74; toilet/tub/wash basin (BATH @47.27,35.08) 28; vanity (BATH @47.27,35.08) 26; shower (BATH @47.27,35.08) 26; toilet/tub/wash basin (POOL BATH) 85; vanity (POOL BATH) 77; shower (POOL BATH) 80; toilet/tub/wash basin (BATH @54.14,5.79) 56; vanity (BATH @54.14,5.79) 64; toilet/tub/wash basin (BATH @54.14,5.79) 62; washer/dryer (LAUNDRY) 69; toilet/tub/wash basin (PET ROOM) 46

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
| Main-floor stairwell room STAIR DN | x 42.65-47.27, y 35.46-47.1 (ceiling 0) | option-c-clean-sheet/main_floor_c.scad:62 |
| Floor opening in the main floor assembly | 4.20 x 11.43 ft (11'-5" per Redesign line 165) | computed from main_floor.scad:337-338 floor_assembly() cut |
| Basement stair room STAIR UP | x 42.65-47.27, y 28.725-45.34 | option-c-clean-sheet/basement_c.scad:67 |
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
| Septic tank to nearest heated main-floor wall (bedroom wing, x=7.27) | 19.2 ft (5.8 m) |
| Septic tank to the basement west wall c/l (x=22.16) / outer ICF face (x=21.6) | 19.16 ft (5.8 m) / 18.61 ft |
| Septic tank to basement UTILITY room (x 22.16..37.37, y 35.08..42.77), nearest corner | 21.3 ft (6.5 m) |
| Septic tank to MUSIC ROOM west wall (22.16, y 50.35..63.16) - the tank's actual neighbour | 19.2 ft (5.8 m) |
| Septic tank to well | 147.4 ft (44.9 m) |
| Pump chamber to well | 147.2 ft (44.9 m) |
| Treatment field to well | 215.0 ft (65.5 m) |
| Reserve field to well | 217.8 ft (66.4 m) |
| Treatment field to the basement (outline polygon) | 87.2 ft (26.6 m) |
| Treatment field to the nearest heated crawl-space/main wall (bedroom wing x=7.27) | 87.2 ft (26.6 m) |
| Treatment field to the garage west wall (x=0, slab, no basement) | 65.7 ft (20.0 m) |
| Reserve field to basement | 87.2 ft (26.6 m) |
| Reserve field to the nearest heated wall | 87.2 ft (26.6 m) |
| Reserve field to the garage | 65.0 ft (19.8 m) |
| Treatment field to west driveway edge (x=-32) | 33.1 ft (10.1 m) |
| Reserve field to west driveway edge | 33.0 ft (10.1 m) |
| Treatment field to the service-line corridor (x=-47..-41) | 18.0 ft (5.5 m) |
| Reserve field to the service-line corridor | 18.0 ft (5.5 m) |
| Reserve field to propane pad (-68..-52, -48..-42) | 27.0 ft (8.2 m) |
| Well to heated main-floor wall (nearest) | 43.6 ft (13.3 m) |
| Well to side porch/deck edge (nearest unconditioned main-floor row) | 37.2 ft (11.3 m) |
| Well to basement outline | 57.4 ft (17.5 m) |
| House (heated) to future shop, closest walls (bunk-room north wall y=66.64 vs shop south wall y=130) | 66.6 ft (20.3 m) |
| House incl. porches/deck to future shop | 66.6 ft (20.3 m) |
| Basement exit areaway (y 67.75) to shop | 62.3 ft (19.0 m) |
| Garage to shop (garage north wall 35.46) | 94.5 ft (28.8 m) |

Corridor and drive lengths: power run road->meter wall 197.3 ft (road edge y=-100 up x=-44 to y=46, then east to x=7.27); gas 202.3 ft; fibre 192.3 ft; the three lines stop at the bedroom wing's west wall x=7.27 (crawl-space wing), 14.9 ft short of the basement west wall x=22.16 where the UTILITY room/panel are. Water line well->east wall x=126.97: 53.0 ft; it stops at the master-bedroom east wall (x=126.97), 24 ft east of the pool equipment room's east wall (x=103.04) where the doc says it enters (permit README:164-166).

West driveway: 142 ft long x 30 ft wide (site.scad:111), its east edge x=-2 is 2.0 ft from the garage's west wall (x=0). Garage door facade: WEST (axis y at x=0; main_floor.scad:117-118; two doors 16 ft + 9 ft wide, y 4.97-20.97 and 22.86-31.86; side-load relative to the south road). Connector to the front loop: x -2..25, y -50..-36 (14 ft wide).

phase = full additions (site.scad:122-131, 196-197, 245): the drive continues north x -38..-8, y 36..230 (30 x 194); shop apron x -72..-2, y 130..230 (70 ft deep, 100 long); north leg x -72..160, y 230..262 (32 wide); east apron x 100..160, y 126..262 (60 deep, 136 long); buried service lines (-50,50) -> (-50,126) -> (80,126) -> (80,130) = 210 ft from the house's west side to the shop's south wall (site.scad:197). Shop footprint x 0..100, y 130..230 (shop.scad / site.scad:218). In phase full the effluent line (y=66, x -65..-3) and the septic-tank neighbourhood sit 5 ft (tank x=-3 to drive x=-8) from the extended drive.

Phase house: parents' house and geothermal loop field are not in site.scad (§13).

