import ast,re,subprocess,math
from pathlib import Path
from shapely.geometry import box
from shapely.ops import unary_union
H=Path("/home/user/house-review/docs/layout-options/round-3/option-h-knuckle-hub")
def fn(path,name):
    t=Path(path).read_text()
    tmp=Path("/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run/work/R3-CS/_t.scad"); tmp.write_text(t+f"\necho(X={name}());\n")
    r=subprocess.run(["openscad","-o","/dev/stdout","--export-format","echo",str(tmp)],capture_output=True,text=True,cwd=str(H))
    m=re.search(r"ECHO: X = (.*)$",r.stdout+r.stderr,re.M)
    return ast.literal_eval(m.group(1).replace("true","True").replace("false","False").replace("undef","None"))
M=H/"main_floor_h.scad"; B=H/"basement_h.scad"
mr=fn(M,"main_rooms"); md=fn(M,"main_doors"); mw=fn(M,"main_windows"); roof=fn(M,"main_roof")
br=fn(B,"base_rooms"); bd=fn(B,"base_doors"); bw=fn(B,"base_windows")
def lab(r):
    l=r[0]; return " ".join(l) if isinstance(l,list) else l
# ---- stair
n=19; rise=11.75/n; run=10.5/12
for name,top,far in (("as cut",26.2,14.4+0.2+0.01),("wall c/l",26.2,14.4),("wall face",26.2,14.6)):
    L=top-far; drop=L/run*rise; head=drop-1.625
    print("stair",name,"len",round(L,2),"drop",round(drop,3),"head ft",round(head,3),"mm",round(head*304.8),"less 12.7:",round(head*304.8-12.7))
print("opening needed ft", round((1.95/0.3048+1.625)/(rise/run),3))
print("rise mm",rise*304.8,"flight mm",11.75*304.8, "foot y", 26.2-18*run)
# ---- building area
# ---- basement vs main
heated=[r for r in mr if r[6] not in ("porch","garage","stairwell")]
mu=unary_union([box(r[1]-.2,r[2]-.2,r[3]+.2,r[4]+.2) for r in mr if r[6] not in("porch","garage")])
bu=unary_union([box(r[1]-.2,r[2]-.2,r[3]+.2,r[4]+.2) for r in br if r[6] not in("porch",)])
print("main union area",mu.area,"basement union",bu.area, "bu holes", len(getattr(bu,'interiors',[])))
print("basement outside main:",bu.difference(mu).area)
d=mu.difference(bu); print("main not over basement area",round(d.area,1))
# elevator
el=[r for r in br if "ELEVATOR" in lab(r)][0]; elb=box(el[1],el[2],el[3],el[4])
print("elevator basement",el[1:5],"dist to basement exterior",elb.distance(bu.exterior), "to main exterior", box(*[r for r in mr if 'ELEVATOR' in lab(r)][0][1:5]).distance(mu.exterior))
# which side
ext=bu.exterior
from shapely.ops import nearest_points
print(nearest_points(elb,ext))
# ---- roof coverage
unc=0;tot=0;unl=[]
for r in mr:
    if r[6] in("porch",): continue
    x=r[1]
    while x<r[3]:
        y=r[2]
        while y<r[4]:
            cx,cy=x+.25,y+.25;tot+=1
            if not any(b[0]-b[6]<=cx<=b[2]+b[6] and b[1]-b[6]<=cy<=b[3]+b[6] for b in roof[:]): unc+=1; unl.append((lab(r),cx,cy))
            y+=.5
        x+=.5
print("uncovered",unc*.25,"of",tot*.25, set(u[0] for u in unl))
# spans
for b in roof:
    dx,dy=b[2]-b[0],b[3]-b[1]; print("roof",b[:4],"short",round(min(dx,dy),1),"m",round(min(dx,dy)*.3048,2))
# clerestory vs hub core
def hip(b):
    x0,y0,x1,y1,eave,p,ov=b; a=x0-ov;bb=y0-ov;c=x1+ov;e=y1+ov
    r=min(c-a,e-bb)/2*0.999; top=eave+p*r
    def z(x,y):
        if not(a<=x<=c and bb<=y<=e): return None
        d=min(x-a,c-x,y-bb,e-y)   # hip: distance from nearest edge
        return eave+p*min(d,r)
    return z,top,(a,bb,c,e)
core=hip(roof[1]); cl=hip(roof[-1])
print("core top",core[1],"clerestory top",cl[1])
mx=-9;mn=9
import itertools
for i in range(0,200):
    for j in range(0,300):
        x=cl[2][0]+(cl[2][2]-cl[2][0])*i/199; y=cl[2][1]+(cl[2][3]-cl[2][1])*j/299
        zc=cl[0](x,y); zr=core[0](x,y)
        if zc is None or zr is None: continue
        mx=max(mx,zc-zr)
print("max height of raised block above hub core roof surface, ft:",round(mx,3))
# ---- wells vs main rooms/porches
wells=[r for r in br if r[6]=="porch"]
def ov(a,b): return max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
for w in wells:
    wr=(w[1],w[2],w[3],w[4]); hits=[]
    for r in mr:
        if r[6]!="stairwell" and ov(wr,(r[1]-.2,r[2]-.2,r[3]+.2,r[4]+.2))>0: hits.append((lab(r),r[6],round(ov(wr,(r[1]-.2,r[2]-.2,r[3]+.2,r[4]+.2)),1)))
    rf=[b[:4] for b in roof if ov(wr,(b[0]-b[6],b[1]-b[6],b[2]+b[6],b[3]+b[6]))>0]
    print("WELL",wr,"area",(wr[2]-wr[0])*(wr[3]-wr[1]),"main hits",hits,"roof overhang over:",rf)
print("basement windows vs grade 9.75 above slab")
for w in bw: print(w,"head",w[4]+w[5],"below grade",round(9.75-w[4]-w[5],2))
print("garage doors",[x for x in md if x[4]=="garage"])
print("-----")
mx_=mu.exterior; bx_=bu.exterior
print("main ext len",mx_.length,"basement ext len",bx_.length)
fr=mx_.difference(bx_.buffer(0.6)); print("main exterior wall NOT over basement wall (frost wall/grade beam), ft:",round(fr.length,1))
ret=bx_.difference(mx_.buffer(0.6)); print("basement wall retaining unexcavated ground (inside main footprint), ft:",round(ret.length,1))
ov_=bx_.intersection(mx_.buffer(0.6)); print("basement wall under main exterior wall ft",round(ov_.length,1))
# garage pier/door
print("garage slab area", 24*24)
# egress windows vs wells alignment
