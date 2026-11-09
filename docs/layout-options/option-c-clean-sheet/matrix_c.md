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
