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
