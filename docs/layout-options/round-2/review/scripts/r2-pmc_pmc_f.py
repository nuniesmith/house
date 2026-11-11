import ast, re, subprocess, sys, math
from shapely.geometry import box, Point, LineString
from shapely.ops import unary_union
O="/home/user/house-review/docs/layout-options/round-2/"
OPT={"D":(O+"option-d-compact-l/main_floor_d.scad",O+"option-d-compact-l/basement_d.scad"),
     "E":(O+"option-e-linear-ranch/main_floor_e.scad",O+"option-e-linear-ranch/basement_e.scad"),
     "F":(O+"option-f-your-sizes-fitted/main_floor_f.scad",O+"option-f-your-sizes-fitted/basement_f.scad"),
     "T":("/home/user/house-review/models/main_floor.scad","/home/user/house-review/models/basement.scad")}
def lit(s): return ast.literal_eval(s.replace("true","True").replace("false","False").replace("undef","None"))
def audit(f):
    r=subprocess.run(["openscad","-o","/dev/stdout","--export-format","echo","-D","audit=true",f],capture_output=True,text=True)
    m=re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$",r.stdout+r.stderr,re.M)
    return [lit(g) for g in m.groups()]
def rect(r): return min(r[1],r[3]),min(r[2],r[4]),max(r[1],r[3]),max(r[2],r[4])
def lab(r): return " ".join(r[0]) if isinstance(r[0],list) else r[0]
def un(rooms,keep): return unary_union([box(*rect(r)).buffer(0.01,join_style=2) for r in rooms if keep(r)]).buffer(-0.01,join_style=2)
tank=box(-3,52,3,64)
for k in ("F",):
    m,b=OPT[k]; R=audit(m)[0]; B=audit(b)[0]
    heated=un(R,lambda r:r[6] not in("porch","garage")).buffer(0.5,join_style=2)
    gar=un(R,lambda r:r[6]=="garage").buffer(0.5,join_style=2)
    porch=un(R,lambda r:r[6]=="porch" and "DRIVE" not in lab(r))
    base=un(B,lambda r:r[6]!="porch").buffer(0.5,join_style=2)
    print("==",k)
    print(" tank->heated(outside face) %.1f  ->garage %.1f  ->basement %.1f  ->porch/deck %.1f"%(tank.distance(heated),tank.distance(gar),tank.distance(base),tank.distance(porch)))
    # nearest heated point
    # ICF
    print(" basement perimeter %.1f  wall area at 10.125 ft: %.0f"%(base.exterior.length, base.exterior.length*10.125))
    # utility room exposure
    U=[r for r in B if lab(r)=="UTILITY"][0]; ux0,uy0,ux1,uy1=rect(U)
    edges={"W":LineString([(ux0,uy0),(ux0,uy1)]),"E":LineString([(ux1,uy0),(ux1,uy1)]),"S":LineString([(ux0,uy0),(ux1,uy0)]),"N":LineString([(ux0,uy1),(ux1,uy1)])}
    for n,e in edges.items():
        free=e.length - e.intersection(base.buffer(-0.0).exterior.buffer(0.6)).length
        onb=e.intersection(base.exterior.buffer(0.6)).length
        gnear=e.intersection(gar.buffer(0.6)).length
        # boundary length on basement outline that is within 0.6 of garage polygon (garage over/next to)
        print("  UTILITY %s wall len %.1f: on basement outline %.1f; of that touching garage footprint %.1f"%(n,e.length,onb,e.intersection(base.exterior.buffer(0.6)).intersection(gar.buffer(1.0)).length))
    # ejector pit and basement bath distances
    # dryer
    dry=None
    for f in audit(m)[3]:
        pass
    ex=heated.exterior
    # exterior boundary minus garage contact
    ext=ex.difference(gar.buffer(0.6))
    for name,pt in {"F":(107.0,31.1)}.items():
        if name==k:
            p=Point(pt); print(" dryer %s: euclid to exterior wall %.1f ft"%(pt,p.distance(ext)))
            # manhattan nearest: sample boundary points
            best=1e9
            L=ext.length if hasattr(ext,'length') else 0
            geoms=list(ext.geoms) if ext.geom_type.startswith("Multi") else [ext]
            for g in geoms:
                n=int(g.length*20)+1
                for i in range(n+1):
                    q=g.interpolate(i/n,normalized=True); d=abs(q.x-pt[0])+abs(q.y-pt[1]); best=min(best,d)
            print("   manhattan %.1f"%best)
