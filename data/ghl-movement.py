# ponytail: one pass over the Movement location's contacts; counts, tags, states. Read-only.
import json, os, sys, time, urllib.request, urllib.parse, collections
key=os.environ['GHL_KEY']; loc=os.environ['GHL_LOC']
H={'Authorization':'Bearer '+key,'Version':'2021-07-28','Accept':'application/json','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36'}
def get(url):
    req=urllib.request.Request(url,headers=H); return json.load(urllib.request.urlopen(req,timeout=60))
total=0; tags=collections.Counter(); states=collections.Counter(); emails=0; dnd=0; start_after=None; start_id=None; pages=0
while True:
    q={'locationId':loc,'limit':100}
    if start_after: q['startAfter']=start_after; q['startAfterId']=start_id
    j=get('https://services.leadconnectorhq.com/contacts/?'+urllib.parse.urlencode(q))
    cs=j.get('contacts',[]); pages+=1
    for c in cs:
        total+=1
        if c.get('email'): emails+=1
        if c.get('dnd'): dnd+=1
        for t in c.get('tags',[]) or []: tags[t]+=1
        st=(c.get('state') or '').strip().upper()
        if st: states[st]+=1
    m=j.get('meta',{})
    if not cs or not m.get('startAfterId'): break
    start_after=m.get('startAfter'); start_id=m.get('startAfterId')
    if pages%20==0: print('pages',pages,'total',total,flush=True)
    time.sleep(0.15)
out={'total':total,'with_email':emails,'dnd':dnd,'pages':pages,'tags':tags.most_common(60),'states':dict(states.most_common())}
json.dump(out,open('data/movement.json','w'),indent=1); print('done',total,'contacts;',emails,'emails; top tags',tags.most_common(12))
