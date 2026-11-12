import re,sys
exec(open('maxc.py').read().split("for f,names")[0])
for f,rn,dn,fn,un in [('main_floor_h.scad','main_rooms','main_doors','main_fixtures','main_furniture'),('basement_h.scad','base_rooms','base_doors','base_fixtures','base_furniture')]:
    src,get=load(D+f)
    doors=get(dn); fx=get(fn)
    try: fx=fx+get(un)
    except Exception as e: pass
    print('==',f)
    for d in doors:
        x,y,ax,w,t=d[:5]
        if t=='garage': continue
        if ax=='x': zone=(x,y-0.7,x+w,y+0.7)
        else: zone=(x-0.7,y,x+0.7,y+w)
        for fxr in fx:
            if fxr[5]<=0.1: continue
            a,b,c,dd=fxr[:4]
            if a<zone[2] and c>zone[0] and b<zone[3] and dd>zone[1]:
                print('door',d[:5],'blocked/near by fixture',fxr[:6])
