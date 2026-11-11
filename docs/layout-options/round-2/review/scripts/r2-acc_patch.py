import json,re
P='/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run/findings/r2-accessibility-kayla.md'
s=open(P).read(); o=json.load(open('out.json')); des=json.load(open('designer.json'))
s=s.replace("**Status:** D and E complete; **F pending** (option F is being redrawn; its column, findings and the three-way verdict will be added when it lands).","**Status:** D, E and F complete. F is Kayla's Nov 11 list drawn at her sizes with no footprint cap (3,910 sq ft at the outside face): the overage against 3,000 is context, not a defect in F's arrangement, and the cap comparison belongs in the decision pack. The `*_nov10.*` files were ignored.")
s=s.replace("| @x","")
# F rows by row-label prefix
Frows={
"| IN / MISSING / CONTRADICTED |":"%d / %d / %d"%tuple(o['cF']),
"| Designer's own score |":"108 / 56 / 0 (only 28 rows re-scored on F, the rest carried from E)",
"| Deal-breakers met (of 12) |":str(sum(o['dF'].values())),
"| Designer's deal-breaker score |":"11",
"| 1,700 mm circle, main floor":"kitchen 6.8, foyer 6.1, laundry 6.4, shared bath 6.0, ensuite 9.4 ft pass; powder 3.6 ft with door leaf fails: 6 of 7",
"| Basement baths |":"J&J 8.0 ft (leaf) pass: 1 of 1",
"| Step-free house to garage |":"Y (slab at house level, drive rises as drawn)",
"| House to deck |":"Y at house level, but the deck is 3 ft deep (48 sf)",
"| Single doors <32 in":"main 0 / 0 / 19; basement 0 / 1 / 14",
"| Minimum hall clear (ft) |":"5.00 (short hall to the primary; bedroom hall 5.0 x 28)",
"| Elevator stack |":"Y: x 92-98.4, y 25.8-33.2, offset 0.0",
"| 5 x 5 ft approach |":"junction hall 5.0 ft deep (5.4 CL) with the door leaf swinging into it, both levels: exactly 5.0",
"| Stair |":"straight, 19 risers, 5.4 ft wall to wall; top landing is the junction hall; foot landing 4.0 ft deep under the foyer",
"| Curbless showers |":"ensuite wet zone (tub + shower), shared bath, basement flush, recess flagged",
"| Garage to kitchen with groceries |":"Costco door to pantry then 3 ft door to the kitchen (garage to kitchen centre about 25 ft); or mudroom door; every route crosses the kitchen, with a clear 6 ft south lane outside the work zone",
"| Primary bed to toilet at night |":"through the bedroom to the open ensuite: about 25 ft",
"| Primary bed to laundry |":"29.6 ft via the walk-in (plan_facts)",
"| Entry to powder |":"powder 12 ft from the front door, door visible from the front door",
"| Kitchen to dining |":"14 ft opening",
"| Bedrooms and living rooms with exterior wall and window |":"all; kitchen, living, office and the primary have 2+ walls",
"| Dark interior living rooms |":"none on main; basement theatre and future room have no window (future uses)",
"| Depth at living rooms |":"20.4-22.4 ft; primary 27.4 x 22.4",
"| Bedroom vs living / theatre noise |":"main: 0 shared walls; basement BEDROOM 4 shares a 14.4 ft wall with the rec room; gym under bedroom 2; theatre under the suite wing",
"| Kitchen |":"345 (15 x 22, her size)",
"| Dining + nook |":"323 (14 x 22)",
"| Pantry |":"9 x 12 = 108 (her 12 x 8 = 96, turned)",
"| Living |":"24 x 20 = 480 (her size)",
"| Primary bedroom |":"27 x 22 = 594 (her size)",
"| Ensuite |":"10 x 18.4 = 184 (her 16 x 10 = 160, turned)",
"| Walk-ins (each 7 x 8) |":"6 x 8 each (her size)",
"| Laundry |":"9 x 10 (her size)",
"| Bedroom 2 |":"12 x 14 + closet (her size)",
"| Powder |":"6 x 7 (her size)",
"| Basement theatre / gym |":"theatre and future room drawn, windowless; gym 12 x 20",
"| Dropped |":"nothing; adds office/library 15 x 16 on the main floor",
}
out=[]
for line in s.split('\n'):
    if line.rstrip().endswith('| pending |'):
        for k,v in Frows.items():
            if line.startswith(k):
                line=line.rstrip()[:-len('pending |')]+v+' |'
                break
    out.append(line)
s='\n'.join(out)
# deal-breaker table
for k,v in o['dF'].items():
    s=s.replace("| %s | %s | %s | pending |"%(k,'met' if o['dD'][k] else 'NOT met','met' if o['dE'][k] else 'NOT met'),"| %s | %s | %s | %s |"%(k,'met' if o['dD'][k] else 'NOT met','met' if o['dE'][k] else 'NOT met','met' if v else 'NOT met'))
s=s.replace("Designers claimed 11 each.","F misses K-331/K-070, K-332, K-334 (basement bedroom against the rec room) and wide doors (one 34 in basement door). Designers claimed 11 each.")
# F disagreement table
rows=["\n**Option F** (designer 108 / 56 / 0, of which 136 rows carried from E and unmeasured on F; mine %d / %d / %d)\n\n| K-ID | Designer | Mine | Evidence |\n|---|---|---|---|"%tuple(o['cF'])]
n=0
for k,(v,e) in o['oF'].items():
    if des['F'][k][0]!=v:
        n+=1; rows.append("| %s | %s | %s | %s |"%(k,des['F'][k][0],v,e))
s=s.replace("\nEvery other item matches the designer's verdict after a check against the plan.","\n".join(rows)+"\n\nEvery other item matches the designer's verdict after a check against the plan.")
print('F disagreements',n)
# F findings
newf="""| ACC-19 | Should fix | F | Closets | 4 of 6 closets touch an exterior wall (junction CLOSET, ELEVATOR, BR 2 closet, WIC @98.4,36.2): K-070 and K-331 CONTRADICTED, K-071 MISSING. Designer scores K-331 MISSING but K-070 IN. | matrix_f.md "4 of 6"; main_floor_f.scad rooms | - | $ |
| ACC-20 | Should fix | F | Front door to kitchen | No vestibule (K-041). Just inside the front door the kitchen is 200/330 sf visible, dining 220/308, living 359/480; kitchen, dining and living are joined by two 14 ft openings (62 pct of the 22.4 ft wall) with no door. K-332 (deal-breaker), K-144, K-262 CONTRADICTED; K-062, K-324 MISSING. | los.py; main_floor_f.scad doors `[47.8,3,y,14,full]`, `[62.2,3,y,14,full]`, `[86.6,1.5,y,6.5,full]` | - | $ |
| ACC-21 | Should fix | F | Basement bedroom 4 and the rec room | BEDROOM 4 (x 53.2-65.6, y 0-14.4) shares a 14.4 ft wall with the basement LIVING ROOM (x 65.6-86.6): K-334 (deal-breaker) CONTRADICTED, K-325 MISSING. The matrix row counts main-floor rooms only. GYM / MUSIC sits under bedroom 2 and the future theatre under the laundry and ensuite: K-008. | basement_f.scad rooms; main_floor_f.scad BEDROOM 2 | - | $$ (sound assemblies; no repo price) |
| ACC-22 | Should fix | F | Powder and turning circles | Powder 6.0 x 7.0 ft clear: largest circle 4.6 ft (3.6 ft with its leaf); the drawn circle overlaps the toilet and vanity. 6 of 7 rooms pass. The drawn kitchen circle is a clipped 5.6 x 3.6 ft disc, though a 6.8 ft circle fits at (36, 3.7). | circ.py F; main_floor_f.scad fixture rows | ABC 3.8.4.3.(4) | $ |
| ACC-23 | Should fix | F | Entry and pantry fit-out | The only entry fixtures are a 5.2 x 1.2 ft coat cabinet and mudroom lockers and bench: no foyer bench, console, drop surface or mail point (K-043, K-044, K-140, K-143, K-151, K-153, K-320 MISSING). The pantry has a 0.6 ft shelf bank and a freezer, no counter (K-114). The designer carried these rows from E, which drew them. | main_floor_f.scad fixtures | - | $ |
| ACC-24 | Should fix | F | Primary suite and bedroom 2 | Ensuite has one door and an open toilet: no link to the laundry or walk-ins, no WC room (K-227, K-228, K-229 MISSING). Primary deck is 3.0 x 16 ft (K-191). Bedroom 2 is 24 ft from the primary bedroom, about 28 ft by door path (K-245). Window behind the bed head: bed x 110-116.3, north window x 114-120 (K-306). | main_floor_f.scad doors/windows/fixtures | - | $ |
| ACC-25 | Should fix | F | Dining and windows | 72 in table (x 48.5-54.5) is 0.5 ft from the kitchen/dining opening (K-128). Kitchen windows (south x 36-42, north x 35-43) and living windows (south x 68-80, north x 66-74) are directly across from each other (K-077). | main_floor_f.scad furniture/windows | - | $ |
| ACC-26 | Consider | F | Door, hall and stair numbers | Basement door (23.8, 24.8) is 2.8 ft (34 in): K-061 MISSING under the 36 in target. Halls are exactly 5.0 ft clear; the 5 x 5 ft elevator approach is exactly 5.0 ft deep with the door leaf swinging into it, on both levels; the stair foot landing is 4.0 ft deep. | misc.py F; PROS-CONS F s.6 | ABC 9.5.4.1. | none |
| ACC-27 | Consider | F | Circulation | 28 ft bedroom hall plus two short halls: 10.7 pct strict, 13.4 pct with foyer; K-316 and K-317 MISSING (round-1 midpoint between C and B). Primary is 70 ft from the kitchen. | matrix_f.md | - | none |
| ACC-28 | Consider | F | Drawing conflicts | Fireplace `[84.8,3,86.2,8]` stands in front of the 6.5 ft foyer/living opening (y 1.5-8); coffee counter `[60.4,15,62,21.4]` overlaps the dining/living opening (y 3-17) by 2 ft. | main_floor_f.scad | - | none |
"""
s=s.replace("\n(Stair headroom, window wells",newf.rstrip('\n')+"\n\n(Stair headroom, window wells",1)
# findings table order: new rows are after the table's last row; ensure blank-line separation fine
s=s.replace("| ACC-18 | Consider | D, E |","| ACC-18 | Consider | D, E |")
# verdict
vi=s.index("## 6. Verdict")
ci=s.index("## 7. Citation log")
verdict="""## 6. Verdict (D, E and F)

1. On my re-score D is strongest (%d IN, 10 of 12 deal-breakers), then E (%d, 11 of 12), then F (%d, 8 of 12). F's own 108 IN rests on 136 rows carried from E without re-measuring; measured on F it loses the vestibule, entry drop zones, pantry counter, a window-free bed head and the basement bedroom wall.
2. On accessibility: F's main-floor sizes are the roomiest (laundry 9 x 10, foyer 11.4 x 8, ensuite 10 x 18.4) and its doors and showers are sound, but halls and the elevator approach sit at exactly 5.0 ft, the powder fails the 1,700 mm circle, the deck is 3 ft deep and the stair foot landing is 4 ft. D has the widest halls (5.6 ft) and 5 of 5 main circles; E has the widest elevator approach clear of leaves in the basement.
3. Strongest on my criteria: D (flow, daylight and noise are cleanest; its misses are three 34 in doors, one basement bath circle, an open vestibule and the exterior closets). F is the honest size of the latest list, not a better arrangement; its Kayla gaps are mostly fit-out that can be drawn in, but the open public wing and the basement bedroom against the rec room are layout.

"""%(o['cD'][0],o['cE'][0],o['cF'][0])
s=s[:vi]+verdict+s[ci:]
s=s.replace("## 7. Citation log","## Citation log")
s=s.replace("ACC-03, ACC-04, ACC-14","ACC-03, ACC-04, ACC-14, ACC-22")
s=s.replace("| ACC-18 | `search.py --doc abc_2023 '\"9.5.4.1\"'`","| ACC-18, ACC-26 | `search.py --doc abc_2023 '\"9.5.4.1\"'`")
open(P,'w').write(s)
