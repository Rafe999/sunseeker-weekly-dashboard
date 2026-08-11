import json,re,urllib.request,pathlib,datetime
root=pathlib.Path('investment-dashboard/data')
F=json.loads((root/'forecast.json').read_text(encoding='utf-8'))
rows=[]
for f in F['funds']:
    code=f['code']
    u=f'https://fundgz.1234567.com.cn/js/{code}.js'
    req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Referer':'https://fund.eastmoney.com/'})
    txt=urllib.request.urlopen(req,timeout=20).read().decode('utf-8','ignore')
    m=re.search(r'jsonpgz\((\{.*\})\)',txt)
    if not m: continue
    e=json.loads(m.group(1)); nav=float(e['gsz']); prev=float(e['dwjz']); cp=float(e['gszzl'])
    rows.append({'date':e['gztime'][:10],'code':code,'name':f['name'],'estimatedNav':round(nav,4),'previousNav':round(prev,4),'dailyChangePct':round(cp,4),'dailyChangeValue':round(nav-prev,4),'holdingPnl':round(float(f['holding'])*cp/100,2),'asOf':e['gztime'],'source':'fundgz.1234567.com.cn'})
out={'updatedAt':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds'),'records':rows}
(root/'close-estimate.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')