# PF-ALT — Alternative (Remplanner project №1722010 "Alternate")

Conventions: page refs are `alt p.N`. Inches as printed (ceiling prints as H=106.3 in = 270 cm). Positions are on the sheet (top/bottom/left/right); no north arrow exists. "elev." = the per-room wall-elevation sheets p.6-p.38 (cleanest source for widths). "meas." = measured on the 150-dpi image. "inferred" = read from geometry or furniture, not printed. Room numbers are this set's own (circle numbers on p.2, descending by area).

**Scale check (done first, as required).** `scale.py` gives 11.82 px/ft for the Base plan p.1. Verified against printed chains: on p.1 the east terrace S=1129.14 prints 223.4 in wide and measures ~218 px (0.976 px/in = 11.7 px/ft; consistent with 11.82 within edge error). On the Rooms/Furniture/Plumbing sheets (p.2-p.4) the same terrace measures 213 px = 0.953 px/in = **11.44 px/ft**; the garage outer 384 in (p.1 bottom chain 12.0+223.4+48.0+88.7+12.0 = 384.1) measures 366 px on p.2 = 0.953 px/in. So p.2-p.4 are drawn at ~0.97 of the p.1 scale. All "meas." numbers on p.2 below use **11.44 px/ft** (1 px = 0.105 ft; 1 px on the 2000-px-wide displayed image = 0.108 ft). Measuring bias at wall edges: garage measured 356 px between dark wall lines = 372 in vs 384 in by chain (-12 in). Treat meas. as +/- 1 ft overall, +/- 2 ft on routes.

## §0 Set identity
- File: `Alternative.pdf`; sha256 `b962c1a42a4814c58e60d0d5fe927e9e24dd8e7a7e2abfe49abf1e6d88631baf`; 38 pages (A3 landscape).
- Project №1722010, title "Alternate" printed bottom-centre of every sheet.
- Sheet inventory (page -> title as printed): p1 Base plan; p2 Rooms; p3 Furniture; p4 Plumbing; p5 Wall elevations (key plan); p6 Garage (1-2); p7 Garage (3-4); p8 Living Room (1-5); p9 Living Room (6-7); p10 Kitchen (1-7); p11 Kitchen (8); p12 Foyer (1-8); p13 Foyer (9); p14 Master Bedroom (1-6); p15 Sunroom (1-4); p16 Dining Room (1-4); p17 Library (1-8); p18 Office (1-4); p19 Hall (1-5); p20 Hall (6-8); p21 Master Bathroom (1-14); p22 Laundry (1-4); p23 Mudroom (1-4); p24 Breakfast Room (1-4); p25 Bedroom 4 (1-6); p26 Hall (1-7); p27 Bedroom 3 (1-6); p28 Bedroom 2 (1-6); p29 Utility (1-7); p30 Bathroom 2 (1-6); p31 Pantry (1-4); p32 Bathroom 3 (1-4); p33 WIC (1-4); p34 WIC (1-4); p35 Powder Room (1-4); p36 Elevator Closet (1-4); p37 Water Closet (1-4); p38 Closet (1-4).
- Elevation-page to room mapping is printed in the sheet titles. The two "Hall" sets are different rooms: p19-p20 = Hall 10 (229.60 ft2), p26 = Hall 16 (137.99 ft2) (matched by wall lengths, e.g. p20 wall 6 540.0, p26 wall 1 360.0 on the bedroom wing). p33 = WIC 23 (walls 86.2 x 89.3 = 53.2 ft2), p34 = WIC 24 (85.2 x 89.3 = 52.8 ft2) (matched by product). p38 "Closet" 60.4 x 26.2 = 10.98 ft2 = room 28; **room 29 (Closet 10.76 ft2) has no elevation sheet** (not shown).
- Legend on p1: Existing wall, Material: drywall, Material: glass, Terrace.
- Not in this set (checked sheet titles and p1-p5 by eye): Partitions sheet (this set has none); basement plan; foundation plan; roof plan; building elevations; sections; electrical sheet; site plan; north arrow; scale bar; door/window schedule table; wall-type / insulation notes; overall envelope dimension string; any second-storey sheet; any room printed "Open to Basement" (the stair has no room number or S= label); driveway/road. One floor only (main floor).
- Differences between printed values on the Base plan (p1) and the Rooms sheet (p2), same set: Garage 1199.76 (p1) vs 1199.86 (p2); Foyer 380.18 vs 380.29; Living 789.86 vs 790.08; Kitchen 395.15 vs 395.36; Breakfast Room 144.02 vs 143.91; Laundry 157.15 vs 157.26; terraces 685.77 vs 685.56 and 567.69 vs 567.91. All other S= labels identical (checked every label). This sheet quotes the Rooms sheet (p2) and says so. p1 prints 28 room labels besides the garage, 29 in all.

## §1 Envelope
- Ceiling height: H=106.3 in (8 ft 10.3 in, 270 cm) in all 29 room labels (p1, p2 labels via labels.py); H=60.0 (x2) and H=82.7 (x1) on p1 are opening heights.
- Printed S= areas are NET INTERIOR (inside the walls). Wall thickness on the chains is about 12 in (garage inner 360.0 x 480.0 in, p6/p7, outer 384.1 x 504.0). Gross footprint is larger than any sum below.
- (a) Derived from printed chains:
  - Garage inner 360.0 x 480.0 in (elev. p6 wall 1 479.9, p7 wall 3 480.0 = 51.5+108.0+42.3+108.0+35.3+108.0+27.0; p6/p7 wall 2/4 360.0): 360.0 x 480.0/144 = 1200.0 ft2 = printed S=1199.86. Outer 384.1 x 504.0 in (p1 bottom chain 12.0+223.4+48.0+88.7+12.0 = 384.1; left chain 12.0+51.5+108.0+42.3+108.0+35.3+108.0+39.0?; outer taken as inner + 2 x 12 = 504.0).
  - Bedroom wing top wall, outer: 216.5 + 96.6 + 48.0 + 24.9 = **386.0 in (32.2 ft)** (p1 top chains; 96.6+48.0+24.9 = 169.5 = the printed width of the 115.61 ft2 terrace above the wing).
  - Heated block south wall inner chain (p1 row y=661.8 pt, mudroom west to living east): 86.7+42.0+34.2+25.3+48.0+22.8+105.4+120.0+59.0+64.7+48.0+123.1+48.0+65.8 = **893.0 in (74.4 ft)** (a sum of chain labels in one row; may include jamb overlaps).
  - East wall of sunroom+living: **727.1 in (60.6 ft)** (p1 chain on the 1129.14 ft2 terrace, 223.4 x 727.1).
  - Elevation inner dimensions of the main blocks: Sunroom 202.0 x 192.0 (p15); Library 240.1 x 144.0 (p17); Office 237.9 x 144.1 (p18); Dining 240.0 x 144.1 (p16); Breakfast 144.0 x 143.9 (p24); Laundry 156.4 x 144.8 (p22); Mudroom 163.0 x 128.2 (p23); Pantry 128.2 x 96.0 (p31). No single chain spans the whole building, so a printed overall length/width does not exist.
- (b) Measured on p.2 (11.44 px/ft, +/- 1 ft, outer wall lines): heated block west wall (foyer) to east wall (sunroom/living): about **85.9 ft (1030 in)**; top of bedroom wing to south wall of kitchen/living: about **101.6 ft (1219 in)**; bedroom wing width about 32.3 ft (387 in; chain gives 386.0, so (b) agrees); bedroom wing height (top to the foyer/hall-10 band) about 55 ft (meas. 631 px); with the garage: west edge of garage to east wall about 109 ft; garage bottom to wing top about 111.7 ft. Garage outer meas. 31.0 ft x 40.6 ft vs 32.0 x 42.0 ft by chain.
- Heated envelope outline (words, p1/p2): a "T/L" of two rectangles plus the garage. (1) North-south **bedroom wing** about 32 ft wide x 55 ft long at top-centre (master suite at its top, bedrooms/baths/laundry down its length, hall 16 as the spine); (2) east-west **main block** below it about 86 ft wide x 47 ft deep (foyer at left; office, hall 10, library, sunroom in the upper band; utility, breakfast room, dining room, kitchen, pantry, mudroom, living room in the lower band); (3) **garage** 32 x 42 ft attached at bottom-left, sharing its right wall with the mudroom and the stair/elevator zone and its top-right corner with the foyer. Outside corners of the heated envelope: not stated; tracing p.2 I count about 10-12 (inferred; V1-2 sheet counted about 28 by the same method). The bay/jogs that remain: a 12 in jog between sunroom and living-room east walls (p8 wall 1 = 12.0) and the garage/foyer step.
- Garage outline: simple rectangle, 3 bays side by side along the 480 in dimension, nose-in toward the house, three overhead doors on the left (outer, west) wall 108.0 in wide each, H=88.6 (p7 wall 3, p1). Touches the house at the mudroom wall (36.0 in door) and the stair/elevator wall (no door); the top-right corner of the garage abuts the foyer (no door printed).
- Terraces/porches as printed (legend "Terrace"), five areas, no roof/cover shown on any sheet:
  - Terrace A, 115.61 ft2, above the master wing top wall, 169.5 x 98.2 in (p1 chains 169.5 and 98.2).
  - Terrace B, 210.44 ft2, left of the foyer (front-door terrace), chain 268.7 (p1) and 152.0.
  - Terrace C, 685.56 ft2 (p1 685.77), above the library/office band, east of the bedroom wing, 585.9 x 168.4 in (p1).
  - Terrace D, 1129.14 ft2, east of sunroom and living room, 223.4 x 727.1 in (p1).
  - Terrace E, 567.91 ft2 (p1 567.69), south-east of the living room, 224.0 x 402.6 in (p1 chains 224.0, 402.6, 202.9/203.3).
  - Total terrace (p2 values) 115.61 + 210.44 + 685.56 + 1129.14 + 567.91 = **2708.66 ft2** (p1 values sum 2708.65).
- Totals (Rooms sheet p2, 29 numbered rooms): all numbered areas sum 6025.66 ft2 (rooms.py); minus garage 1199.86 = **net heated interior 4825.80 ft2** (p1 values: 4825.26). Garage 1199.86. Porches 2708.66. The set draws no "Open to Basement" area, so the stair area is inside a room (see §9).

## §2 Room table (Rooms sheet p.2; names/areas verified against the p.2 image)
Dimensions = elevation-sheet wall lengths (inside), inches. L-shapes list all walls in sheet order. Position on p.2.
| № | Name as printed | S ft2 | Inside dims (in) | Position | Use |
|---|---|---|---|---|---|
| 1 | Garage | 1199.86 | 360.0 x 480.0 (p6, p7) | bottom-left | printed; 3 cars drawn 195.7 x 88.2 (p3) |
| 2 | Living Room | 790.08 | 7 walls: 12.0, 204.0, 320.1, 349.6, 183.1, 149.1, 146.0 (p8, p9); L-shaped | bottom-right | printed |
| 3 | Kitchen | 395.36 | 8 walls: 183.1, 284.5, 128.2, 30.1, 7.0, 135.1, 48.0, 389.4 (p10, p11) | bottom-centre | printed |
| 4 | Foyer | 380.29 | 9 walls: 258.9, 196.8, 72.5, 30.7, 118.9 (stair), 59.9 (stair), 153.7 (stair), 96.0, 162.0 (p12, p13); includes the stair well (inferred, §9) | centre-left | printed |
| 5 | Master Bedroom | 300.64 | 6 walls: 249.0, 214.6, 67.9, 56.1, 181.4, 158.5 (p14) | top-right of wing | printed |
| 6 | Sunroom | 269.42 | 202.0 x 192.0 (p15) | right-centre | printed |
| 7 | Dining Room | 240.14 | 240.0 x 144.1 (p16) | centre-bottom band | printed |
| 8 | Library | 239.28 | 8 walls: 78.2, 20.7, 5.0, 20.7, 156.8, 143.9, 240.1, 144.0 (p17) (rectangle ~240 x 144 with a small jog) | centre-right | printed |
| 9 | Office | 237.99 | 237.9 x 144.1 (p18) | centre | printed |
| 10 | Hall | 229.60 | E-W band 540.0 long x 48.1 (p20 walls 6, 7) plus a N-S nook 149.0 x 48.0 between Office and Library (p19 walls 1-3, 5); 8 walls p19/p20 | centre band | printed |
| 11 | Master Bathroom | 164.26 | 14 walls p21: 181.4, 36.2, 67.9, 90.7, 79.4, 14.2, 7.0, 64.3, 84.1, 64.3, 7.0, 64.3, 72.0, 104.5 | top-left of wing | printed |
| 12 | Laundry | 157.26 | 156.4 x 144.8 (p22) | wing right-centre | printed |
| 13 | Mudroom | 145.10 | 163.0 x 128.2 (p23) | bottom, left of pantry | printed |
| 14 | Breakfast Room | 143.91 | 144.0 x 144.0 (p24; 143.9/144.1) | centre-bottom band | printed |
| 15 | Bedroom 4 | 142.62 | 6 walls: 144.1, 156.4, 79.1, 30.7, 65.0, 125.7 (p25) | wing right | printed |
| 16 | Hall | 137.99 | spine of the wing: 7 walls 360.0, 47.9, 400.6, 64.4, 40.6, 9.7, 7.0 (p26); about 47.9 wide | wing centre | printed |
| 17 | Bedroom 3 | 131.11 | 6 walls: 115.0, 144.0, 144.4, 78.8, 29.4, 65.1 (p27) | wing left | printed |
| 18 | Bedroom 2 | 129.92 | 6 walls: 144.1, 78.6, 31.2, 65.4, 112.9, 144.0 (p28) | wing left (upper) | printed (name "Bedroom 2"; rooms.py dropped the digit) |
| 19 | Utility | 129.17 | 7 walls p29: 89.7, 83.1, 8.6, 113.9, 25.7, 72.5, 197.0; about 89.7 wide x 197.0 long, L-shaped at the stair end | left of breakfast room, beside the garage | printed; no equipment symbol drawn (§6) |
| 20 | Bathroom 2 | 91.06 | 6 walls: 96.2, 144.0, 52.6, 16.7, 43.6, 127.4 (p30) | wing bottom-left | printed ("Bathroom 2") |
| 21 | Pantry | 85.47 | 128.2 x 96.0 (p31) | bottom, between mudroom and kitchen | printed |
| 22 | Bathroom 3 | 55.43 | 95.8 x 83.3 (p32) | wing bottom-right | printed (rooms.py merged text; on the sheet 22 = Bathroom 3) |
| 23 | WIC | 53.39 | 86.2 x 89.3 (p33) | top of wing, left of master bedroom | printed |
| 24 | WIC | 52.85 | 85.2 x 89.3 (p34) | below WIC 23 | printed |
| 25 | Powder Room | 43.92 | 95.8 x 66.1 (p35) | wing bottom, left of Bathroom 3 | printed (on the sheet 25 = Powder Room) |
| 26 | Elevator Closet | 34.12 | 75.1 x 65.5 (p36) | beside garage wall, below stair | printed |
| 27 | Water Closet | 23.68 | 79.4 x 43.0 (p37) | wing top-left, below master bath | printed |
| 28 | Closet | 10.98 | 60.4 x 26.2 (p38) | wing, between master bath zone and Bedroom 2 | printed |
| 29 | Closet | 10.76 | not shown (no elevation sheet); within Bedroom 4 at its east wall (p2 position 955,580 displayed) | wing right | printed |
Script corrections: `rooms.py` rows 22 and 25 printed "Powder Room Bathroom 3" - on p2 25 = Powder Room 43.92 and 22 = Bathroom 3 55.43 (the two labels sit side by side and the text merged); row 18 is "Bedroom 2" and row 20 is "Bathroom 2" (digit dropped by the script). No area was wrong. Numbering is descending by area (checked). The stair has no room number and no printed area. Hall 10 and Hall 16 are both named "Hall". Rooms 11, 23, 24, 27, 28 are partially or wholly open to each other (see §3).
Long narrow bedroom wing (rooms 5, 11, 12, 15-18, 20, 22-25, 27-29): inside widths: bedroom columns 144.0 wide (Bedroom 2/3 144.0-144.4; Bedroom 4 144.1; laundry 156.4), hall 16 about 47.9 wide (p26 wall 2 = 47.9), wing outer width 386.0 in (§1). Rooms stacked along the hall: left side Master zone / Bedroom 2 / Bedroom 3 / Bathroom 2; right side Master / Laundry / Bedroom 4 / Powder Room + Bathroom 3.

## §3 Door-type openings (ws=0)
Widths = chain labels at the opening on the elevation sheets (cross-checked on the room on the other side); H=82.7 unless stated. "open" = grey filled opening, no leaf; "double" = two leaves drawn. p1 prints 38 labels H=82.7 and 3 labels H=88.6 (openings.py); the elevations give 41 distinct H=82.7 openings listed below, so p1 has about 3 fewer labels than distinct openings (overlapping labels).
| # | Opening | Connects | Width in | Type | Source |
|---|---|---|---|---|---|
| 1 | Garage - Mudroom | garage / mudroom | 36.0 | single | p6 wall 1, p23 wall 1 |
| 2 | Garage side door | garage / outside (south yard) | 42.0 | single | p6 wall 1 |
| 3-5 | Garage overhead x3 | garage / outside (west) | 108.0 each, H=88.6 | overhead | p7 wall 3, p1 (three H=88.6 labels) |
| 6 | Mudroom - Utility | mudroom / utility | 66.0 | open | p23 wall 2, p29 wall 1 |
| 7 | Mudroom exterior | mudroom / outside (south) | 42.0 | single | p23 wall 4 |
| 8 | Utility - Elevator Closet | utility / elevator closet | 36.0 | single | p29 wall 2, p36 wall 3 |
| 9 | Utility - Hall 10 | utility / hall 10 | 42.0 | double | p29 wall 6 |
| 10 | Utility - Kitchen | utility / kitchen | 36.0 | single | p29 wall 7, p10 wall 7 |
| 11 | Pantry - Kitchen | pantry / kitchen | 36.0 | single | p31 wall 1, p10 wall 3 |
| 12 | Kitchen - Living | kitchen / living | 36.0 | single | p10 wall 1, p8 wall 5 |
| 13 | Kitchen - Breakfast Room | kitchen / breakfast | 60.0 | sliding panel run drawn | p11 wall 8, p24 wall 3 |
| 14 | Kitchen - Dining Room | kitchen / dining | 60.0 | sliding panel run drawn | p11 wall 8, p16 wall 3 |
| 15 | Breakfast Room - Hall 10 | breakfast / hall 10 | 60.0 | sliding panel run | p24 wall 1, p20 wall 6 |
| 16 | Dining Room - Hall 10 | dining / hall 10 | 60.0 | sliding panel run | p16 wall 1, p20 wall 6 |
| 17 | Dining Room - Living Room | dining / living | 36.0 | single | p16 wall 2, p9 wall 6 |
| 18 | Living Room - Hall 10 | living / hall 10 | 60.0 | sliding panel run | p9 wall 7, p20 wall 6 |
| 19 | Living Room - Terrace D | living / outside | 203.2 | wide glazed opening | p8 wall 3, p1 |
| 20 | Sunroom - Hall 10 | sunroom / hall 10 | 42.0 | single | p15 wall 3 |
| 21 | Sunroom north | sunroom / Terrace C | 126.0 | glazed | p15 wall 1 |
| 22 | Sunroom east | sunroom / Terrace D | 126.0 | glazed | p15 wall 4 |
| 23 | Foyer front door | foyer / Terrace B (outside) | 60.0 | double | p13 wall 9, p1 |
| 24 | Foyer second exterior | foyer / Terrace B (north side) | 42.0 | double, glazed sidelight 30.7 | p12 walls 3-4 (wall assignment inferred from p1 labels) |
| 25 | Foyer - Office | foyer / office | 42.0 | double | p12 wall 2, p18 |
| 26 | Foyer - Hall 10 | foyer / hall 10 | 40.1 | open | p12 wall 2, p20 wall 7 |
| 27 | Foyer - Hall 16 | foyer / hall 16 | 39.9 | open | p12 wall 1, p26 wall 4 |
| 28 | Office - Hall 10 nook | office / hall 10 | 42.0 | single/double symbol | p18 wall 2/4, p19 wall 1 |
| 29 | Library - Hall 10 nook | library / hall 10 | 42.0 | | p17 wall 8, p19 wall 3 |
| 30 | Hall 10 nook north | hall 10 / Terrace C | 42.0 | double | p19 wall 2 |
| 31 | Hall 10 nook south end | nook / hall 10 band | 42.0 | | p19 wall 5 |
| 32 | Hall 16 - Master Bedroom | hall 16 / master | 47.9 | double | p26 wall 2, p14 wall 2 |
| 33 | Hall 16 - Laundry | hall 16 / laundry | 48.0 | double | p26 wall 3, p22 wall 1 |
| 34 | Hall 16 - Bedroom 2 | hall 16 / bedroom 2 | 36.0 (p26 wall 1) but 34.4 on p28 wall 5 | single | p26, p28 |
| 35 | Hall 16 - Bedroom 3 | hall 16 / bedroom 3 | 36.0 | single | p26 wall 1, p27 wall 3 |
| 36 | Hall 16 - Bedroom 4 | hall 16 / bedroom 4 | 36.0 | single | p26 wall 3, p25 wall 1 |
| 37 | Hall 16 - Powder Room | hall 16 / powder room | 31.5 | single | p26 wall 3, p35 wall 1 |
| 38 | Master Bedroom - Laundry | master / laundry | 36.0 (dimensioned on p22 wall 2; the master wall 2 single door on p14 has no chain, scaled about 35) | single | p22, p14 |
| 39 | Master - WIC 23 | master / WIC | 31.5 | single | p14 wall 5, p33 wall 1 |
| 40 | Master - WIC 24 | master / WIC | 36.0 | single | p14 wall 4, p34 wall 2 (connection inferred from p2) |
| 41 | Master - Master Bathroom | master / bath | 36.0 | single | p14 wall 3, p21 wall 3 |
| 42 | Master Bathroom - Water Closet | bath / WC room | 36.0 | single | p21 wall 5, p37 wall 3 |
| 43 | Bedroom 3 - Bathroom 2 | bedroom 3 / bath 2 | 36.0 | single | p27 wall 4, p30 wall 2 |
| 44 | Bedroom 4 - Bathroom 3 | bedroom 4 / bath 3 | 36.0 | single | p25 wall 6, p32 wall 4 |
Closets 28 and 29, Bedroom 2's wardrobe niche, Bedroom 4's closet 29: no door label (open niches; p2). Elevator Closet has one door (36.0). Master Bathroom has two doors (36.0 to the bedroom side, 36.0 to the water closet).
Summary (distinct openings, H=82.7 unless stated): 36.0 in x 15 (rows 1, 8, 10, 11, 12, 17, 34/35/36 (34 as 36.0), 38, 40, 41, 42, 43, 44); 42.0 in x 10 (rows 2, 7, 9, 20, 24, 25, 28, 29, 30, 31); 60.0 in x 6 (rows 13-16, 18, 23); 66.0 in x 1; 126.0 in x 2; 203.2 in x 1; 39.9/40.1 in open x 2; 47.9/48.0 in doubles x 2; 31.5 in x 2; plus overhead 108.0 in x 3 (H=88.6). **Narrowest door-type opening: 31.5 in** (Powder Room p35 wall 1; WIC 23 / master wall 5 p14, p33). **Doors under 36 in: 31.5 in x 2** (powder room door, WIC 23 door) and Bedroom 2's door printed 34.4 in on p28 wall 5 (36.0 on the hall sheet p26 wall 1: printed discrepancy). Doors under 32 in: the two 31.5 in. No 30 in or smaller. Exterior openings: garage side 42.0; garage overhead x3; mudroom 42.0; foyer front 60.0 and foyer second 42.0; hall-nook north 42.0; sunroom 126.0 x2; living 203.2 = 11. Garage-to-house door width: **36.0 in** (to the mudroom only; no door garage-to-pantry, no door garage-to-utility, no door garage-to-foyer).
Door heights as printed: 82.7 except the garage overhead 88.6; sunroom/living glazed units also 82.7.

## §4 Window-type openings (ws>0)
p1 prints 18 window labels (openings.py): H=60 ws 24 x9; H=60 ws 33.5 x2; H=60 ws 36 x2; H=60 ws 42 x3; H=60 ws 46.5 x1; H=36 ws 46.5 x1; labels overlap on the dense wing so the elevations below are more complete. **Window widths are not dimensioned on the elevation sheets** (only H and ws, e.g. p14 prints 60.0 and 24.0 with no width chain); widths below are from p1 chain labels where one exists, else "not printed".
- Garage: 1 window north wall + 1 window south wall (p6 wall 2, p7 wall 4: H=60, ws 24); p1 chain 48.0 at the south wall (223.4+48.0+88.7); north wall chain 52.5/48.0. 2 walls.
- Master Bedroom: 2 windows on wall 1 (249.0) and 1 on wall 6 (158.5), all H=60 ws=24 (p14); p1 chains 48.0 beside the wing east wall (three 48.0 labels at 142.5/48.0) - widths 48.0 (p1), per-window assignment not printed. 2 walls (3 windows).
- Master Bathroom: 1 window on wall 9 (84.1), H=60 ws=46.5, two panes, above the tub (p21; p1 H=60 ws=46.5 label). 1 wall. WIC 23, WIC 24, Water Closet, Closet 28: no window on elevations (p33, p34, p37, p38).
- Bedroom 2: 1 window (wall 1, 144.1) H=60 ws=24 (p28). Bedroom 3: 1 window (wall 1, 115.0) H=60 ws=24 (p27). Bedroom 4: 1 window (wall 3, 79.1) H=60 ws=24 (p25). Each bedroom: windows on 1 wall.
- Bathroom 2: 1 window H=36 ws=46.5 (p30 wall 1 prints "36.0" as the height; p1 label H=36 ws=46.5). Bathroom 3 (p32), Powder Room (p35): no window.
- Laundry: 1 window wall 3 (144.8), H=60 ws=42 (p22). 1 wall.
- Office: 1 window wall 1 (237.9) H=60 ws=24 (p18). Library: 2 windows wall 5 (156.8) H=60 ws=36 (p17; p1 two H=60 ws=36 labels). Each room: 1 wall.
- Foyer: 2 windows H=60 ws=42 flanking the 60.0 front door on wall 9 (p13; p1 chains 48.0 each at the foyer left wall); plus a glazed full-height panel 30.7 wide on wall 4 (p12) beside the 42.0 double door. 2 walls.
- Living Room: 2 windows on wall 4 (349.6) H=60 ws=33.5 (p8; p1 chains 48.0 each); also the 203.2 in glazed opening on wall 3 (§3). 2 walls (windows + glazed opening).
- Kitchen: 2 windows on wall 2 (284.5) H=60 ws=42 (p10; p1 two H=60 ws=42 labels at the south wall with chains 48.0 and 120.0). 1 wall. Pantry: 1 window wall 2 (96.0) H=60 ws=42 (p31). Breakfast Room, Dining Room, Mudroom, Utility, Hall 10, Hall 16, Elevator Closet: no ws>0 opening on their elevations (p24, p16, p23, p29, p19, p20, p26, p36). Utility walls 4 (113.9) and 5 (25.7) are drawn as glass (blue panels, no ws label) on p29; Foyer walls 5-7 (stair) show a blue glass panel behind the stair on p12 wall 5.
- Sunroom: no ws>0 opening; glazing is two 126.0 in glazed doors (§3) and a 42.0 door (p15).
- Rooms with NO window-type opening: Breakfast Room, Dining Room, Mudroom, Utility (glass panels only), Pantry has one, Hall 10, Hall 16, Elevator Closet, WIC x2, Water Closet, Closets 28/29, Bathroom 3, Powder Room, Sunroom (glazed doors only).
- Windows directly across from each other: Bedroom 2 / Bedroom 3 west wall windows vs Laundry/Bedroom 4 east wall windows are across the 386.0 in wing (the hall 16 between): not on the same axis (hall has no window). Master Bedroom walls 1 and 6: perpendicular. The kitchen south windows face the north wall of the kitchen (60.0 slider openings), which look into the breakfast/dining rooms.

## §5 Halls and circulation
- Hall 10 (room 10): 229.60 ft2 (p2). Share of net heated interior 229.60 / 4825.80 = 4.8%. Narrowest printed width: 48.1 in (p20 wall 7); nook 48.0 (p19 walls 2, 5) with a 42.0 door at each end.
- Hall 16 (room 16): 137.99 ft2 (p2). 137.99 / 4825.80 = 2.9%. Narrowest printed width: 47.9 in (p26 wall 2); the foyer end opening is 39.9 in (open) (p26 wall 4, p12 wall 1).
- Foyer (room 4): 380.29 ft2 includes the stair well (inferred, §9). Foyer 380.29 / 4825.80 = 7.9%. No vestibule room exists.
- Total hall area (rooms 10 + 16) = 367.59 ft2 = 7.6% of net heated interior (p2). Foyer + halls = 747.88 ft2 = 15.5%.
- Printed clear widths on the routes: front door 60.0 (double); foyer open passages 40.1 and 39.9; hall 16 doors 36.0 (x3), 31.5, 48.0 (x2 doubles).
- Mudroom-utility passage 66.0 in open; utility-kitchen 36.0 in.

## §6 Plumbing fixtures (p4, p3, elevations)
- Master Bathroom (11): walk-in shower base 104.3 x 56.0 (p4); tub 84.3 x 40.2 (p4; p21 wall 9 84.1); double vanity with two basins on wall 4 (90.7 wide, p21); two "Mini cabinet for bathroom" labels and 21.0 / 21.0 clearance marks (p4); rain-shower/mixer fittings on wall 13 (p21). Water Closet (27): toilet 15.0 (p4). Both on the wing's left (west) exterior wall side.
- Bathroom 2 (20): toilet 15.0, tub 66.9 x 41.8, a shower base beside the tub (size not printed), lavatory with labels 52.8 / 16.1 / 18.1 (p4). Tub on the west exterior wall.
- Bathroom 3 (22): lavatory 16.1 x 24.0, tub/shower 59.1 x 35.4, toilet 15.0 (p4). Tub on the east exterior wall.
- Powder Room (25): lavatory 16.1 x 24.0, toilet 15.0 (red-printed dimension 42.6 beside it), and a **tub/shower-type fixture drawn in green along the north wall across the room width (66.1 in; size not printed)** (p4 crop). The Powder Room therefore draws a tub/shower fixture.
- Laundry (12): washer + dryer drawn as two 36.0 in wide units with 30.0 in depth marks on the east wall (p4: 36.0, 36.0, 30.0, 30.0); laundry sink: not drawn.
- Kitchen (3): sink 36.0 in (p4) in the south wall run under the windows (p4 label 36.0"); cooktop/range symbols on the east wall run (p3); refrigerator/oven units not labelled; dishwasher: not labelled. Breakfast Room (14): one round basin in the west cabinet run (p4/p3). Mudroom (13): sink with tap on the east wall (p23 wall 3) plus a hatched floor-grate fixture 47.2 x 31.5 beside it (unlabelled; dog wash not named; p4). Garage: two tap/sink symbols on the north wall (grey, unlabelled). Pantry: no sink drawn (cabinets only).
- Outdoor tap: not shown. Dog wash: not labelled. Mop sink: not shown. Hose bib: not shown.
- Wet-wall map (meas. on p2, 11.44 px/ft, +/- 2 ft, centre to centre): Powder Room 25 and Bathroom 3 share a wall (adjacent, about 8 ft apart); Bathroom 2 to Powder Room about 14 ft (hall 16 between); Master Bathroom to Water Closet 27 adjacent (shared wall); Master Bathroom tub to Laundry washer about 30 ft; Laundry to Bathroom 3 about 14 ft (Bedroom 4 between); Laundry to Powder Room about 24 ft; Master Bathroom to Bathroom 2 about 37 ft; Kitchen sink to Mudroom sink about 22 ft; Kitchen sink to Breakfast Room sink about 29 ft; Mudroom sink to Breakfast sink about 15 ft (utility between); Kitchen sink to Laundry about 72 ft; Kitchen sink to Powder Room about 50 ft; Kitchen sink to Master Bathroom about 80+ ft. No wet room shares a wall with the kitchen except none: kitchen / pantry / mudroom are the lower wet cluster; bath groups are in the wing; laundry is in the wing next to the master bedroom.
- Basement plumbing: nothing drawn. Mechanical/utility room: Utility 19 (129.17 ft2) is named; p29 shows built-in cabinetry (154.4 in run on wall 7), a console unit on wall 4 and glass panels; no furnace, water heater, softener or floor drain symbol on any sheet.

## §7 Kitchen, pantry, dining
- Kitchen (3) is a separate room: S=395.36 ft2, 8 walls (§2). Kitchen / breakfast room (14) / dining room (7) are three rooms separated by walls; the kitchen north wall (389.4 in, p11 wall 8) carries two 60.0 in openings (p11: 42.2 | 60.0 | 141.1 | 60.0 | 86.2), one to the breakfast room and one to the dining room, drawn as sliding panel runs on p2/p3.
- Island 120.0 x 60.0 in (p3/p4, labels 120.0 and 60.0). Aisle widths: not printed as chains between island and runs; meas. on p3: south run to island about 6.5 ft, island to the east appliance wall about 8 ft (+/- 1 ft).
- Sink: south wall run (36.0 in sink, p4), under the two windows (§4). Range/cooktop: east wall (kitchen/living wall), p3 shows a 48.0 in wide run with burners, plus a 24.0 in unit. Refrigerator and ovens: not labelled; tall cabinet/appliance blocks on the north-west alcove (24.0 / 30.0 / 48.0 labels, p3). Dishwasher: not labelled.
- Pantry (21): 85.47 ft2, 128.2 x 96.0 in; one door, 36.0 in to the kitchen (p31 wall 1); window on its south wall (p31 wall 2). **Pantry shares no wall with the garage** (mudroom 13 is between; p2). **No door pantry-garage ("Costco door" absent).** Garage-to-kitchen route (§10): garage - mudroom 36.0 - utility via 66.0 open - kitchen 36.0.
- Kitchen as a through route: kitchen has doors to utility (36.0, west side), pantry (36.0), living room (36.0, east side), and two 60.0 openings to breakfast/dining on the north side. Yes, through routes exist between west (utility) and east (living) and between north (dining/breakfast) and the pantry.
- Dining (7): 240.0 x 144.1 in; table 96.0 x 42.0 in with 8 chairs (p3). Openings: 60.0 north to Hall 10, 60.0 south to Kitchen, 36.0 east to Living Room. No window (§4). Breakfast Room (14): 144.0 x 144.0, round table (35.4/35.4 dia labels) with chairs; 60.0 north and 60.0 south; no window; basin on west cabinet run.
- Kitchen to dining: direct 60.0 opening; to breakfast: direct 60.0 opening. Breakfast and dining are not connected to each other (no opening between them on p16, p24).
- "Walled off vs V1-2": not applicable (different plan).

## §8 Furniture sheet facts (p3)
- Master bed: labels 82.0 and 86.0 (and 70.1), nightstands 19.7 each side, desk/dresser at the bottom, armchair at top corner; bed about 82.0 x 86.0 as labelled (orientation head to the east wall). Bedroom 2: bed 63.0 x 78.7 (p3). Bedroom 3: bed 63.0 x 78.7. Bedroom 4: bed 59.4 x 79.9 with a desk and a 78.7 in item; closet 29 drawn at its east wall.
- Office: two desks 78.7 x 39.4 with chairs, wall shelves 40.0 at each end and 47.2 shelving (p3). Library: bookcases 47.2 / 23.0 around three walls, a reading chair and sofa group (58.7, 55.1, 54.6 labels). Sunroom: two sofas (27.6 arm), armchair 35.0, side tables (p3).
- Living room: L-shaped sectional (84.0 + 31.5 x3 + 39.4 modules, 72.8 depth) with 48.0 x 36.0 coffee table, two armchairs (36.6), desk/sofa table 51.2 x 87.2 at the west wall, shelves 47.2 x2 on the north wall, 74.0 unit on the south wall (p3).
- Dining table 96.0 x 42.0, 8 chairs; breakfast round table ~35.4 dia, 4 chairs; kitchen island 120.0 x 60.0. Garage: 3 vehicles 195.7 x 88.2 each, workbench 83.1 x 42.9 and a 76.4 x 40.2 item (p3).
- Master WICs: hanging rails (21.7 / 31.5 / 48.4 labels), dresser 55.9 x 15.7. Library and office both drawn; screened porch: not shown. No furniture is drawn on the terraces (p3).

## §9 Stair and elevator space
- The stair has no room number, no S= and no "Open to Basement" label. Drawn at p2 position (716-760, 840-955 displayed): a straight run with an arrow, at the west end of the foyer/hall zone, against the garage wall. It appears in the Foyer's elevation sheet (p12 walls 5-7: stair profile 118.9 and 153.7 in with a glass panel behind it, wall 6 = 59.9 in) so it is inside the Foyer room (inferred from the wall list; S=380.29 includes it).
- Stair width: 59.9 in (p12 wall 6; meas. on p2 about 57 in, +/- 6 in). Run: wall lengths 118.9 / 153.7 in on the profile sheets; the number of treads is not printed.
- Elevator Closet (room 26): 34.12 ft2, 75.1 x 65.5 in (p36), one 36.0 in door to the Utility (p36 wall 3, p29 wall 2). Sits immediately below (south of) the stair and beside the garage wall, west of the Utility. Not entered from the foyer or hall. The word "Future" does not appear (printed "Elevator Closet").
- Relative to the halls: stair at the foyer's south-west corner; Utility to the east; Hall 10 (band) is about 9 ft to the east at the stair's north end (p2).

## §10 Daily routes (p2 straight segments through doorways, 11.44 px/ft, +/- 2 ft; rooms passed THROUGH)
| Route | Length ft | Rooms passed through |
|---|---|---|
| garage door -> kitchen (door threshold) | about 19 | mudroom, utility |
| garage door -> kitchen island centre | about 44 | mudroom, utility, (kitchen) |
| garage door -> pantry | about 32 | mudroom, utility, kitchen |
| front door -> kitchen (via utility double door) | about 46 | foyer, hall 10 (corner), utility |
| front door -> kitchen (via hall 10 and the breakfast room 60.0 sliders) | about 44 | foyer, hall 10, breakfast room |
| front door -> powder room | about 28 | foyer, hall 16 |
| front door -> primary bedroom door (hall 16 double) | about 56 | foyer, hall 16 |
| primary bedroom door -> laundry | about 6 (direct 36.0 door from the bedroom; about 6 via hall 16 double) | none (master bedroom only) |
| primary bedroom (bed) -> kitchen | about 82 | master bedroom, hall 16, foyer, hall 10, utility |
| Bedroom 2 -> nearest bath (Powder Room 25) | about 20 | hall 16 |
| Bedroom 2 -> Bathroom 2 | about 18 | hall 16, bedroom 3 |
| Bedroom 3 -> Bathroom 2 (ensuite door) | about 5 | none |
| Bedroom 4 -> Bathroom 3 (ensuite door) | about 6 | none |
| kitchen -> dining | about 8 | none (60.0 opening) |
| dining -> living | about 10 to the 36.0 door, about 27 to the living centre | none |
| living -> sunroom | about 24 to the sunroom door (about 34 to its centre) | hall 10 |
Notes: (1) The kitchen is not on the foyer/hall axis: every route from the front door to the kitchen passes the utility or breakfast room. (2) The living room has no door to the sunroom (p8, p15). (3) Kitchen threshold to powder room about 36 ft (utility - hall 10 - foyer - hall 16). (4) Route lengths are straight door-to-door segments, drawn on p2 where Hall 10 is open to the foyer at its west end (no door symbol, p12 wall 2 grey 40.1).

## §11 Kayla-relevant adjacency facts
- Laundry adjacent to master suite, connected through bath or closet: laundry (12) shares a wall with the Master Bedroom (north) and has a direct 36.0 door into it (p22 wall 2); not through the bath or a closet (p22, p14). Also 48.0 double to hall 16.
- Pantry shares a wall with the garage: no; garage-pantry door: no (mudroom between, p2). Pantry reached only from the kitchen (36.0, p31).
- Powder room near the front entry: about 28 ft via foyer and hall 16 (p2); door 31.5 in; fixtures include a tub/shower-type fixture (§6).
- Vestibule at the front door: no; the front door (60.0 double, p13) opens directly into the foyer (380.29 ft2).
- Any bedroom sharing a wall with the living room: no (wing is at the top of the plan, living room at bottom-right; p2).
- Any bedroom adjacent to the foyer: no bedroom; Bathroom 2 shares the foyer's north wall, and the bedroom wing's hall 16 opens into the foyer by a 39.9 in open passage (p12, p26).
- Closets on exterior walls: WIC 23 (north exterior wall, p2), Closet 29 (Bedroom 4 east exterior wall, p2). Others interior: WIC 24, Closet 28, Elevator Closet (shares the garage wall).
- Tubs on exterior walls: Master tub (west exterior wall, window above, p21/p4); Bathroom 2 tub (west exterior wall); Bathroom 3 tub/shower (east exterior wall); Powder Room tub/shower-type fixture on its north wall (interior side of the wing/top; not on an outer wall per p2).
- Master closet reachable without passing through the master bath: yes, both WICs open off the Master Bedroom (31.5 and 36.0, p14).
- Bathroom reachable from every living zone without crossing the house: Powder Room is off hall 16 (west end of the main block). From the kitchen threshold about 36 ft; from the living-room centre about 76 ft (living - hall 10 - foyer - hall 16); no bath is on the kitchen/living side of the plan (p2).
- Sunroom / screened porch: sunroom yes (269.42 ft2, p15); screened porch: not shown. Library: yes (239.28 ft2). Office: yes (237.99 ft2).
- Number of bedrooms: 4 (Master Bedroom, Bedroom 2, Bedroom 3, Bedroom 4; all printed). Guest room with ensuite: Bedroom 3 has Bathroom 2 by a 36.0 door; Bedroom 4 has Bathroom 3 by a 36.0 door; Bedroom 2 has no bath door.
- Dog bath / pet area: not labelled; mudroom has a sink and an unlabelled hatched grate 47.2 x 31.5 (p3/p4).
- Covered outdoor cooking area: not shown (terraces carry no roof or furniture).
- Sight line from the front door straight into the kitchen or living room: no; the line east from the front door crosses the foyer to the Office double door (p12 wall 2) and the 40.1 open passage to hall 10; kitchen and living room are south of the hall 10 band behind sliding panels and the utility (p2).
- Toilet visible from a bathroom door when open: not determinable from the sheets.
- Second laundry in the master suite: no. A washer/dryer pair is drawn only in room 12.
- Garage position: bottom-left of the plan; its right wall touches the mudroom and stair/elevator zone; the top-right corner touches the foyer; bedrooms are at the top (north wing); no drive is drawn (not shown). Overhead doors face the left edge of the sheet.

## §12 Unreadable / not done
- Window widths are not dimensioned on the elevation sheets (only H and ws). Widths cited from p1 chains only where a chain sits beside the window label (kitchen 48.0 and 120.0; living 48.0 x2; garage 48.0; foyer flanking 48.0; wing 48.0 labels). p1 window labels are only 18, fewer than the elevation sheets show.
- Foyer walls 1-4 (p12) were not matched one by one to p2 geometry: openings 24-27 in §3 use p1/p2 position reasoning, not a printed wall-to-room label.
- Master Bedroom wall 2 single door (p14) has no chain label; its width is from the laundry-side sheet (p22) and a scaled estimate (~35 in).
- Master WIC 24 door: master wall 4 (56.1) and WIC 24 wall 2 (89.3) chains do not match, so the pairing of "master - WIC 24" rests on p2 geometry.
- Bedroom 2 door width: 34.4 (p28) vs 36.0 (p26) - not reconciled.
- Closet 29 (room 29) has no elevation sheet; the plumbing-sheet fixtures in Bathroom 2 (shower base size) and Powder Room (tub/shower fixture size) are not printed.
- Scale: scale.py gives 11.82 px/ft for p1; p2-p4 measure ~11.44 px/ft (§ header). p1 measures were not re-done; envelope (b) is from p2.
- Outside-corner count (about 10-12) is an eyeball tracing; no printed value.
- The South chain sum 893.0 in may double count jamb overlaps.
- The rooms.py total (6025.66) was not re-summed on the image beyond confirming every printed label.
- Routes are by eye on p2 (+/- 2 ft or worse); Hall 10 to foyer is open without a door symbol, so route lengths through it are approximate.
- Per-wall window counts for the dining/breakfast sliding panel runs (p2 shows panels on the 60.0 openings) were not resolved beyond "sliding panel run drawn".
