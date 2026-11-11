import re, ast
R='/home/user/house-review/docs/layout-options/round-2/'
P={'D':R+'option-d-compact-l/','E':R+'option-e-linear-ranch/','F':R+'option-f-your-sizes-fitted/'}
def load(opt, level):
    f=P[opt]+('main_floor_%s.scad'%opt.lower() if level=='main' else 'basement_%s.scad'%opt.lower())
    t=open(f).read()
    t=re.sub(r'//.*','',t); t=t.replace('basement_ceiling()','10'); t=re.sub(r'/\*.*?\*/','',t,flags=re.S)
    out={}
    for name in ['rooms','doors','windows','fixtures','furniture']:
        m=re.search(r'function\s+(\w*%s)\s*\(\)\s*=\s*\[(.*?)\n\];'%name,t,flags=re.S)
        if not m: out[name]=[];continue
        body='['+m.group(2)+']'
        body=re.sub(r'\b(?!true|false|None)([a-z_]\w*)\b(?!\s*")',lambda mm: '0' if mm.group(1) not in ('x','y') else '"%s"'%mm.group(1),body)
        body=body.replace('undef','None')
        try: out[name]=ast.literal_eval(body)
        except Exception as e:
            out[name]=[]; print('ERR',opt,level,name,e)
    return out
if __name__=='__main__':
    for o in 'DE':
        for l in ('main','base'):
            d=load(o,l); print(o,l,{k:len(v) for k,v in d.items()})
