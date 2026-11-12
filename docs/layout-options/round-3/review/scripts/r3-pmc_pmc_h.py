import ast, re, subprocess, math
from shapely.geometry import box, Point, LineString
from shapely.ops import unary_union
H="/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub/"
def lit(s): return ast.literal_eval(s.replace("true","True").replace("false","False").replace("undef","None"))
def audit(f):
    r=subprocess.run(["openscad","-o","/dev/stdout","--export-format","echo","-D","audit=true",f],capture_output=True,text=True)
    m=re.search(r"ECHO: rooms = (.*?), doors = (.*?), windows = (.*?), fixtures = (.*)$",r.stdout+r.stderr,re.M)
    return [lit(g) for g in m.groups()]
def rect(r): return min(r[1],r[3]),min(r[2],r[4]),max(r[1],r[3]),max(r[2],r[4])
def lab(r): return " ".join(r[0]) if isinstance(r[0],list) else r[0]
def un(rooms,keep): return unary_union([box(*rect(r)).buffer(0.01,join_style=2) for r in rooms if keep(r)]).buffer(-0.01,join_style=2)
R=audit(H+"main_floor_h.scad"); B=audit(H+"basement_h.scad")
tank=box(-3,52,3,64)
heated=un(R[0],lambda r:r[6] not in("porch","garage")).buffer(0.5,join_style=2)
gar=un(R[0],lambda r:r[6]=="garage").buffer(0.5,join_style=2)
porch=un(R[0],lambda r:r[6]=="porch" and "DRIVE" not in lab(r))
base=un(B[0],lambda r:r[6]!="porch").buffer(0.5,join_style=2)
print("tank->heated %.1f garage %.1f basement %.1f porch/deck %.1f"%(tank.distance(heated),tank.distance(gar),tank.distance(base),tank.distance(porch)))
print("heated area %.0f perim %.1f; base area %.0f perim %.1f"%(heated.area,heated.exterior.length,base.area,base.exterior.length))
for h in (10.125,12.125): print("ICF at",h, base.exterior.length*h)
# porch areas
for r in R[0]:
    if r[6]=="porch": x0,y0,x1,y1=rect(r); print(" porch",lab(r),(x1-x0)*(y1-y0))
# utility exposure
U=[r for r in B[0] if lab(r)=="UTILITY"][0]; ux0,uy0,ux1,uy1=rect(U); print("UTILITY",U[1:5])
edges={"W":LineString([(ux0,uy0),(ux0,uy1)]),"E":LineString([(ux1,uy0),(ux1,uy1)]),"S":LineString([(ux0,uy0),(ux1,uy0)]),"N":LineString([(ux0,uy1),(ux1,uy1)])}
for n,e in edges.items():
    onb=e.intersection(base.exterior.buffer(0.6)).length
    print("  %s len %.1f on exterior ICF %.1f; touching garage %.1f"%(n,e.length,onb,e.intersection(gar.buffer(1.0)).length))
# is utility under ensuite?
E=[r for r in R[0] if lab(r)=="ENSUITE"][0]; print("ENSUITE",E[1:5])
# wet groups from plan_facts
groups={"G1":(60.6,1.2),"G2":(64.9,1.7),"G3":(86.9,20.4),"G4":(29.0,42.2),"G5":(31.2,38.7),"G6":(57.4,41.2),"G7":(37.0,42.8),"G8":(74.6,44.6),"G9":(53.5,46.1),"G10":(69.0,47.0)}
basepoly=un(B[0],lambda r:r[6]!="porch")
for nm,(xx,yy) in groups.items(): print(nm,"over basement" if basepoly.buffer(0.2).contains(Point(xx,yy)) else "NOT over basement")
for ex in [(22.16,58),(26,42)]:
    d={k:abs(v[0]-ex[0])+abs(v[1]-ex[1]) for k,v in groups.items()}
    print("exit",ex,"DRI %.1f"%sum(d.values()),"max %.1f"%max(d.values()),"over98.4:",[k for k,v in d.items() if v>98.4], {k:round(v,1) for k,v in d.items()})
# ejector
pit=(36.5,45.2)
for nm,(xx,yy) in {"B1":(68.2,19.5),"B2":(67.2,22.2),"B3":(71.0,25.0)}.items():
    d=abs(xx-pit[0])+abs(yy-pit[1]); print("pit->",nm,"%.1f ft = %.1f m"%(d,d*0.3048))
# pit to tank
print("pit to tank edge (3,58) Manhattan %.1f"%(abs(pit[0]-3)+abs(pit[1]-58)))
# dryer
ext=heated.exterior.difference(gar.buffer(0.6))
dry=(74.6,44.6); p=Point(dry); print("dryer euclid to ext non-garage %.1f"%p.distance(ext))
best=1e9
for g in ([ext] if ext.geom_type!="MultiLineString" else list(ext.geoms)):
    n=int(g.length*20)+1
    for i in range(n+1):
        q=g.interpolate(i/n,normalized=True); best=min(best,abs(q.x-dry[0])+abs(q.y-dry[1]))
print("dryer manhattan %.1f"%best)
# laundry window is on E wall x=75.5 at y43: dryer 74.6..: wall gap
# services: west landing (7.27,48) to utility W wall (26,42) and (26,44)
for t in [(26,42.4)]: print("services (7.27,48)->",t,"%.1f"%(abs(7.27-t[0])+abs(48-t[1])))
# utility intake/exhaust distance to garage
print("utility W wall to garage %.1f"%box(ux0,uy0,ux0,uy1).distance(gar))
# louvre heads vs windows above: ensuite windows (26,40,y,3,4,3),(28,36.4,x,...)
# unexcavated area
unex=un(R[0],lambda r:r[6] not in("porch","garage","stairwell")).difference(basepoly.buffer(0.01))
print("main heated not over basement (centre lines) %.0f"%unex.area)
# basement windows & wells counts
print("basement window rows",len(B[2]),"main window rows",len(R[2]))
