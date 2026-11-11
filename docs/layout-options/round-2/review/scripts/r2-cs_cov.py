import ast,re,subprocess
from pathlib import Path
O=Path("/home/user/house-review/docs/layout-options/round-2")
def fn(path,name):
    t=Path(path).read_text()
    tmp=Path("/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run/work/R2-CS/_t.scad"); tmp.write_text(t+f"\necho(X={name}());\n")
    r=subprocess.run(["openscad","-o","/dev/stdout","--export-format","echo",str(tmp)],capture_output=True,text=True,cwd=str(Path(path).parent))
    m=re.search(r"ECHO: X = (.*)$",r.stdout+r.stderr,re.M)
    return ast.literal_eval(m.group(1).replace("true","True").replace("false","False"))
from collections import defaultdict
for tag,d,k in (("D","option-d-compact-l","d"),("E","option-e-linear-ranch","e"),("F","option-f-your-sizes-fitted","f")):
    M=O/d/f"main_floor_{k}.scad"
    roof=fn(M,"main_roof"); rooms=fn(M,"main_rooms"); posts=fn(M,"main_posts")
    print("=====",tag)
    unc=0; tot=0
    for r in rooms:
        if r[6] in ("porch",): continue
        x=r[1]
        while x<r[3]:
            y=r[2]
            while y<r[4]:
                cx,cy=x+.25,y+.25; tot+=1
                if not any(b[0]-b[6]<=cx<=b[2]+b[6] and b[1]-b[6]<=cy<=b[3]+b[6] for b in roof): unc+=1
                y+=.5
            x+=.5
    print("uncovered heated area sq ft",unc*0.25,"of",tot*0.25)
    for b in roof:
        dx,dy=b[2]-b[0],b[3]-b[1]; print(" roof",b[:4],"short ft",round(min(dx,dy),1),"m",round(min(dx,dy)*.3048,2))
    byy=defaultdict(list); byx=defaultdict(list)
    for p in posts: byy[p[1]].append(p[0]); byx[p[0]].append(p[1])
    for y,xs in byy.items():
        xs=sorted(xs); print(" posts y",y,[round(b-a,1) for a,b in zip(xs,xs[1:])])
    por=[r for r in rooms if r[6]=="porch" and "DRIVE" not in str(r[0])]
    print(" porch sf",sum((r[3]-r[1])*(r[4]-r[2]) for r in por),[ (r[0],(r[3]-r[1])*(r[4]-r[2])) for r in por])
