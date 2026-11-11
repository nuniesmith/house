import ast,re,subprocess
from pathlib import Path
O=Path("/home/user/house-review/docs/layout-options/round-2")
def fn(path,name):
    # evaluate OpenSCAD function table by echoing
    t=Path(path).read_text()
    tmp=Path("/tmp/claude-0/-home-user-house/6efebace-6ecc-5584-9c6f-b979c17b28d6/scratchpad/run/work/R2-CS/_t.scad")
    tmp.write_text(t+f"\necho(X={name}());\n")
    r=subprocess.run(["openscad","-o","/dev/stdout","--export-format","echo",str(tmp)],capture_output=True,text=True,cwd=str(Path(path).parent))
    m=re.search(r"ECHO: X = (.*)$",r.stdout+r.stderr,re.M)
    return ast.literal_eval(m.group(1).replace("true","True").replace("false","False"))
for tag,d,k in (("D","option-d-compact-l","d"),("E","option-e-linear-ranch","e")):
    M=O/d/f"main_floor_{k}.scad"
    roof=fn(M,"main_roof"); posts=fn(M,"main_posts"); rooms=fn(M,"main_rooms")
    print("=====",tag)
    for b in roof:
        dx,dy=b[2]-b[0],b[3]-b[1]
        print("roof block",b[:4],"short side ft",round(min(dx,dy),1),"m",round(min(dx,dy)*0.3048,2),"clear m",round((min(dx,dy)-0.4)*0.3048,2))
    # post spacing along same y or x
    import itertools
    ps=sorted(posts)
    from collections import defaultdict
    byy=defaultdict(list); byx=defaultdict(list)
    for p in posts: byy[p[1]].append(p[0]); byx[p[0]].append(p[1])
    for y,xs in byy.items():
        xs=sorted(xs); print(" posts y",y,"spans ft",[round(b-a,1) for a,b in zip(xs,xs[1:])],"m",[round((b-a)*0.3048,2) for a,b in zip(xs,xs[1:])])
    for x,ys in byx.items():
        ys=sorted(ys)
        if len(ys)>1: print(" posts x",x,"spans ft",[round(b-a,1) for a,b in zip(ys,ys[1:])])
    por=[r for r in rooms if r[6]=="porch" and not str(r[0]).startswith("DRIVE") and "DRIVE" not in str(r[0])]
    tot=0
    for r in por:
        a=(r[3]-r[1])*(r[4]-r[2]); tot+=a; print("  porch",r[0],round(a,1))
    print(" porch total sf",round(tot,1),"m2",round(tot*0.092903,1))
