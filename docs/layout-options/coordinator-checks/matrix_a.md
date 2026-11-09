## Layout matrix

Source files: main = `/home/user/house-layout/docs/layout-options/option-a-evolve-current/main_floor_a.scad`; basement = `/home/user/house-layout/docs/layout-options/option-a-evolve-current/basement_a.scad`.

| Measure | Value | Note |
|---|---|---|
| Main-floor conditioned sq ft | 5,486 | 5486.2; excl. stair opening 5432.4 |
| Building area, centre lines (house + attached garage) | 564.4 m2 | 6075 sq ft |
| Building area, outside face | 584.5 m2 | offset 0.5000 ft outward on every wall, calibrated so the CURRENT model = 608 m2 (permit README:41); same offset for all variants |
| Circulation % (strict / with foyer) | 16.6% / 22.2% | 909 sq ft strict of 5486 |
| Single doors <32 in / 32-35 in / 36 in+ (main) | 0 / 0 / 23 | type `door` rows, by opening width |
| Double / open counts (main) | 12 / 2 | type `double` / type `open` |
| Minimum hall clear width | 4.71 ft (HALL @22.1,48.64) | halls = circulation rooms with longer clear side >= 6 ft; raw min incl. entries/slivers 1.15 ft ((suite entry, 2nd piece)) |
| Wet-wall groups (main / basement) | 15 / 8 | 8 ft along-wall chaining, same-line within 1 ft |
| Main groups within 5 ft of a basement group | 1 of 15 | Manhattan between centroids |
| Drain-run index, E = (22.16, 58) | 1019.2 ft | alternate exit (22.16, 38.9): 866.1 ft |
| Water heater -> furthest fixture (main / basement) | 119.8 ft (toilet/tub/wash basin (MASTER BATH)) / 84.8 ft (toilet/tub/wash basin (POOL BATH)) | water heater at (30.1, 36.8); plan Manhattan |
| Bedrooms sharing a wall with a living-kind room | 0 | shared length > 1 ft; living-kind rooms with walls |
| A bedroom shares a wall with the foyer | N | foyer/vestibule label |
| Master bed -> laundry path | LAUNDRY: 102.6 ft, MASTER LAUNDRY: 42.9 ft | walk ft, Dijkstra over door midpoints (Phase 0 method) |
| Laundry count | 2 | 2 LAUNDRY room(s) |
| Closets/WICs touching an exterior wall (not garage) | 0 of 4:  | kind closet; yard / porch faces count, garage does not |
| Pantry/scullery shares a wall with the garage AND has a door to it | Y | SCULLERY: 8.7 ft shared, 1 door(s) |
| Each bedroom's exterior sides | BEDROOM 2: S(garage 11.2) W(porch/patio 3.1, yard 9.6) ;; BUNK ROOM: N(yard 15.1) E(yard 3.2) W(yard 4.6) ;; MASTER BEDROOM: N(porch/patio 18.4) E(porch/patio 23.4) W(porch/patio 4.7) | N/S/E/W with the length (ft) facing yard / porch / garage |
| Master suite exterior sides | N(porch/patio 18.4) S(porch/patio 1.7, yard 26.7) E(porch/patio 23.4, yard 11.2) W(porch/patio 4.7) | suite rooms: MASTER BEDROOM, (master entry), WIC @95.95,20.56, (closet passage), WIC @111.8,20.56, MASTER BATH, WC @99.7,16.71, (linen between the WCs), WC @99.7,9.31 |
| Living-kind rooms with S exposure | DEN (14.8 ft); (den alcove) (3.8 ft) | S edge facing yard/porch |
| Rooms with windows on 2+ walls | 4: SUN ROOM (E/N); MASTER BEDROOM (E/N); DEN (E/S); BREAKFAST (S/W) | window rows, facade per Phase 0 rule |
| Main stair top/foot vs the basement stair | top (nosing) at x 42.65..47.27, y 47.1; basement foot room x 42.65..47.27, y 27.6; **moved** (x offset +0.00/+0.00 ft, run 19.500 ft vs flight 18.375 ft); vs Phase 0 stair top y 47.1, foot y 28.725 |  |
| Min distance bedroom -> drive (house phase) | 9.3 ft (BEDROOM 2) | centre-line rectangle to nearest drive piece, site.scad:108-118 |
| check_layout.py | main_floor_a.scad (defaults): 52 rooms, 56 doors, 17 windows - OK ; basement_a.scad (defaults): 19 rooms, 19 doors, 2 windows - OK (exit 0) | python3 tools/check_layout.py on the variant file(s) |
