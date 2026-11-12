import subprocess,re,sys
Q=[
(852,"The vertical height of any flight of stairs shall not exceed 3.7 m."),
(852,"shall not be less than 1 950 mm"),
(852,"measured vertically, over the clear width of the stair, from a straight line tangent to the tread and landing nosings to the lowest point above"),
(853,"Private (1) 200 125"),(853,"Private (1) 355 255"),
(851,"at least one stair between each floor level within a dwelling unit"),
(856,"landings shall be at least as wide and as long as the width of the stair or ramp in which they occur"),
(856,"The slope of landings shall not exceed 1 in 50."),
(857,"Within a dwelling unit or a house with a secondary suite"),
(873,"provide an unobstructed opening of not less than 0.35 m2 in area with no dimension less than 380 mm"),
(873,"a clearance of not less than 760 mm shall be provided in front of the window"),
(873,"the enclosure shall be openable from the inside without the use of keys, tools or special knowledge"),
(1368,"It is recommended that the sills of windows intended for use as emergency exits be not higher than 1.5 m above the floor"),
(1369,"The window well should be designed to provide sufficient clear space for a person to get out the window and then out the well"),
(909,"at least one smoke alarm installed on each storey, including basements"),
(1049,"outside each bedroom, within 5 m of each bedroom door, measured following corridors and doorways"),
(40,"3 storeys or less in building height, having a building area not exceeding 600 m2"),
(43,"Building area means the greatest horizontal area of a building above grade within the outside surface of exterior walls"),
(927,"for walls not exceeding 3.0 m in unsupported height"),
(928,"300 1.5 2.3 2.6 2.85"),
(836,"Subject to the application limitations defined elsewhere in this Part, structural members and their connections shall"),
(837,"the clear span of any structural member does not exceed 12.2 m"),
(1338,"2-38×286 3.08 2.64 2.35 2.14 1.98 2.14"),
(1339,"Lintel spans are calculated based on a maximum floor joist, roof joist or rafter span of 4.9 m and a maximum roof truss span of 9.8 m"),
(1315,"38 × 286 5.21 4.95 4.71 5.49 5.16 4.85 5.66 5.28 4.92"),
(1317,"38 × 286 5.67 5.34 4.88 6.19 5.89 5.54 6.83 6.37 5.58"),
(1067,"the garage floor shall be sloped to the outdoors"),
(1067,"adjacent spaces in the building are less than 50 mm above the garage floor"),
(1453,"it must be raised at least 50 mm off the floor or be installed so it closes against the curb"),
(1067,"foundations conforming to Sections 9.12. and 9.15. shall be provided for the support of carport and garage super-structures, including that portion beneath garage doors"),
(894,"tight fitting and weather-stripped to provide an effective barrier against the passage of gas and exhaust fumes"),
(894,"shall not be located in a room intended for sleeping"),
(887,"an air barrier system conforming to Subsection 9.25.3. shall be installed between the garage and the remainder of the building"),
(859,"for the length where the difference in elevation is more than 600 mm between the walking surface and the adjacent surface within 1.2 m"),
(923,"Every window well shall be drained to the footing level or other suitable location."),
(287,"shall conform to the Elevating Devices Codes Regulation made pursuant to the Safety Codes Act"),
]
bad=0
for p,q in Q:
    t=subprocess.run(["python3",str(__import__('pathlib').Path.home()/"code-library/search.py"),"--page","abc_2023",str(p)],capture_output=True,text=True).stdout
    n=lambda s:re.sub(r"\s+"," ",s)
    ok=n(q) in n(t)
    if not ok: bad+=1; print("MISS",p,q)
print("bad",bad,"of",len(Q))
