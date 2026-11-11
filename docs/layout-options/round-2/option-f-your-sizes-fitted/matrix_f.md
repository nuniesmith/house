## Layout matrix

Source files: main = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/main_floor_f.scad`; basement = `/home/user/house-review/docs/layout-options/round-2/option-f-your-sizes-fitted/basement_f.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 3,704 | 3704.1; excl. stair opening 3639.3 |
| Building area, centre lines (house + attached garage) | 397.1 m2 | 4275 sq ft |
| Building area, outside face | 417.8 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Heated main-floor footprint excl. garage, outside face | 3,910 sq ft | centre lines 3,704 sq ft; same 0.50 ft outward offset; round-2 target <= 3,000 sq ft |
| Basement footprint, outside face (excl. exit-stair areaway) | 3,917 sq ft | centre lines 3,711 sq ft |
| Circulation % (strict / with foyer) | 10.7% / 13.4% | 396 sq ft strict of 3704 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 19 | type `door` rows, by opening width |
| Double / open counts (main) | 2 / 0 | type `double` / type `open` |
| Minimum hall clear width | 5.00 ft ((short hall to the primary)) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 5.00 ft ((short hall to the primary)) |
| Wet-wall groups (main / basement) | 9 / 2 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 0 of 9 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 1017.1 ft | alternate exit (22.16, 38.9): 847.8 ft |
| Water heater -> furthest fixture (main / basement) | 114.8 ft (toilet/tub/wash basin (MASTER BATH)) / 62.4 ft (vanity (JACK & JILL BATH)) | water heater at (18.1, 31.5); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 29.6 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 1 | 1 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 4 of 6: CLOSET @86.6,25.8 [N(yard 5.4) W(yard 7.4)]; ELEVATOR (FUTURE) [N(yard 6.4)]; CLOSET @106.8,12.4 [S(yard 7.8)]; WIC @98.4,36.2 [N(yard 1.2) W(yard 8.4)] | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | PANTRY: 12.4 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(yard 12.4) E(yard 14.4) W(yard 6.4) ;; MASTER BEDROOM: N(yard 27.4) E(porch/patio 16.0, yard 6.4) W(yard 22.4) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(yard 28.6) E(porch/patio 16.0, yard 25.2) W(yard 30.8) | suite rooms: (short hall to the primary), WIC @98.4,36.2, WIC @104.8,36.2, (primary entry), MASTER BATH, MASTER BEDROOM |
| Living-kind rooms with S exposure | LIVING (24.4 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 5: KITCHEN (N/S); LIVING (N/S); OFFICE / LIBRARY (N/W); BEDROOM 2 (E/S); MASTER BEDROOM (E/N/W) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 86.6..92, y 20.4; basement foot room x 86.6..92, y 4.45; **moved** (x offset +0.00/+0.00 ft, run 15.950 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 20.0 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_f.scad (defaults): 30 rooms, 32 doors, 17 windows - OK ; basement_f.scad (defaults): 23 rooms, 22 doors, 6 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |
