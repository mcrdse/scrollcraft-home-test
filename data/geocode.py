# ponytail: Nominatim at 1 req/s with a cache; ~13 min for 783 rows, runs in background.
import json, time, urllib.request, urllib.parse, os
rows=json.load(open('data/geo-raw.json'))
cache_p='data/geo-cache.json'
cache=json.load(open(cache_p)) if os.path.exists(cache_p) else {}
ST={'CALIFORNIA':'CA','FLORIDA':'FL','COLORADO':'CO','FL':'FL'}
def key(r): return f"{r['city']}|{ST.get(r['st'],r['st'])}|{r['co']}"
for i,r in enumerate(rows):
    k=key(r)
    if k in cache: continue
    st=ST.get(r['st'],r['st']); co=r['co'] if r['co'] not in ('NONE','') else 'US'
    q=f"{r['city'].title()}, {st}, {co}" if co=='US' else f"{r['city'].title()}, {co}"
    url='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({'q':q,'format':'json','limit':1})
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'mcrdse-globe-build/1.0 (kchosd@gmail.com)'})
        j=json.load(urllib.request.urlopen(req,timeout=20))
        cache[k]=[float(j[0]['lat']),float(j[0]['lon'])] if j else None
    except Exception as e:
        cache[k]=None
    if i%25==0: json.dump(cache,open(cache_p,'w'))
    time.sleep(1.05)
json.dump(cache,open(cache_p,'w'))
out=[]
for r in rows:
    ll=cache.get(key(r))
    if ll: out.append({'lat':round(ll[0],3),'lng':round(ll[1],3),'n':r['n'],'city':r['city'].title(),'st':ST.get(r['st'],r['st']),'co':r['co']})
json.dump(out,open('data/geo.json','w'))
print('geocoded',len(out),'of',len(rows),'rows;',sum(o['n'] for o in out),'orders')
