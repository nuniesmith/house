import ast, re, subprocess, sys, math, json
from pathlib import Path
O = Path("/home/user/house-review/docs/layout-options/round-2")
OPT = {"D": ("option-d-compact-l", "d"), "E": ("option-e-linear-ranch", "e")}
if len(sys.argv) > 1 and sys.argv[1] == "F":
    pass
FT = 0.3048
def lit(s): return ast.literal_eval(s.replace("true","True").replace("false","False").replace("undef","None"))
def audit(scad):
    r = subprocess.run(["openscad","-o","/dev/stdout","--export-format","echo","-D","audit=true",str(scad)],capture_output=True,text=True)
    m = re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$", r.stdout+r.stderr, re.M)
    return [lit(g) for g in m.groups()]
def lab(r): 
    l = r[0]; return " ".join(l) if isinstance(l, list) else l
def overlap(a,b):
    return max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
def stairhead(top, opening_len, rise_in=None, ftf=11.75, depth=1.625, run_in=10.5):
    n = math.ceil(ftf*12/7.5); rise = ftf/n; run = run_in/12
    drop = opening_len/run*rise      # nosing-line drop (ft) at the far edge of the opening
    return n, rise*12, drop, drop-depth
def run(tag):
    d,k = OPT[tag]
    M = O/d/f"main_floor_{k}.scad"; B = O/d/f"basement_{k}.scad"
    mr,md,mw,mf = audit(M); br,bd,bw,bf = audit(B)
    return mr,md,mw,mf,br,bd,bw,bf
res = {}
for tag in "DE":
    mr,md,mw,mf,br,bd,bw,bf = run(tag)
    print("=====", tag)
    # stair
    n, rise_in, _, _ = stairhead(0, 1)
    print("risers", n, "rise in", round(rise_in,3), "mm", round(rise_in*25.4,1), "flight mm", round(11.75*304.8,0))
    sw = [r for r in mr if r[6]=="stairwell"][0]
    print("stairwell room", sw[:6])
    wt = 0.4
    if tag=="D":
        top = 27.0; far = sw[4]-wt/2+ -0.01   # opening cut: 27.01 .. 38.49
        open_len_cl = 11.5 - 0.02             # as cut in floor_assembly
        olen = (sw[2]-0.0) - (27.0)           # centre line
        olen_cut = 38.49 - 27.0
    else:
        top = 53.3; olen_cut = 53.3 - (42+0.2+0.01)
    n, ri, drop, head = stairhead(top, olen_cut)
    print("opening length from top nosing (as cut)", round(olen_cut,3), "nosing drop at far edge ft", round(drop,3), "headroom ft", round(head,3), "mm", round(head*304.8,0))
    need = (1.95/0.3048+1.625)/(11.75/n/(10.5/12))
    print("opening length needed for 1950 mm (ft)", round(need,3), "short by", round(need-olen_cut,3), "ft =", round((need-olen_cut)*12,2), "in")
    # with 13mm ceiling drywall
    print("headroom less 12.7 mm drywall:", round(head*304.8-12.7,0))
    # basement wall
    print("wall height ft", 11.75-1.625, "m", round((11.75-1.625)*FT,3), "| backfill m", round((11.75-2)*FT,3))
    # window wells vs main-floor porches/rooms
    wells = [r for r in br if r[6]=="porch" and "WELL" in lab(r)]
    for w in wells:
        wr = (w[1],w[2],w[3],w[4])
        hits=[]
        for r in mr:
            if r[6] in ("porch","garage") or r[6] in ("bed","living","kitchen","dining","bath","hall","utility","closet","stairwell"):
                a = overlap(wr,(r[1],r[2],r[3],r[4]))
                if a>0: hits.append((lab(r), r[6], round(a,1)))
        print("WELL", wr, "area", round((wr[2]-wr[0])*(wr[3]-wr[1]),1), "overlaps main:", hits)
    # basement windows: head height vs grade
    print("basement windows [x,y,axis,w,sill,h] -> head above slab; grade above slab = 9.75")
    for w in bw:
        print("  ", w, "head", w[4]+w[5], "below grade by", round(9.75-(w[4]+w[5]),2))
    # elevator stack
    em = [r for r in mr if "ELEVATOR" in lab(r)]; eb = [r for r in br if "ELEVATOR" in lab(r)]
    print("elev main", em[0][1:5], "base", eb[0][1:5])
    # areas
    # garage door header
    print("garage doors", [x for x in md if x[4]=="garage"])
    print("exterior windows >=8ft main:", [(w[0],w[1],w[3]) for w in mw if w[3]>=8])
