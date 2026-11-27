#!/usr/bin/env python3
"""İstasyon dosyasındaki il ve ilçe adlarını resmi il/ilçe listesine göre düzeltir; aynı şarj ağının aynı noktadaki tekrar kayıtlarını teke indirir.
Kullanım: python3 temizle_ilce.py tum_istasyonlar_birlesik.json ilce.json il.json cikti.json
(ilce.json / il.json: github.com/cosmohacker/turkiye-iller-ve-ilceler-json)"""
import json,sys,collections,re
def fold(s):
    s=str(s).replace('İ','i').replace('I','i').replace('ı','i').lower()
    s=s.translate(str.maketrans('çğöşü','cgosu'))
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
def phpmyadmin(p):
    for o in json.load(open(p,encoding='utf-8')):
        if o.get('type')=='table': return o['data']
src,ilcep,ilp,out=sys.argv[1:5]
# Listede olmayan yaygın kısaltma / eski ad / yazım hataları
TAKMA={'eyup':'eyupsultan','dogubeyazit':'dogubayazit','s karahisar':'sebinkarahisar','m kemalpasa':'mustafakemalpasa','s kochisar':'sereflikochisar','konyaeregli':'eregli','ondokuzmayis':'ondokuz mayis','mayis':'ondokuz mayis'}
iller={x['id']:x['name'] for x in phpmyadmin(ilp)}
il_resmi={fold(v):v for v in iller.values()}
sozluk=collections.defaultdict(dict)   # il_fold -> ilce_fold -> resmi ad
for x in phpmyadmin(ilcep): sozluk[fold(iller[x['il_id']])][fold(x['name'])]=x['name']
d=json.load(open(src,encoding='utf-8'))
sayac=collections.Counter();bulunamayan=collections.Counter()
for x in d:
    ilf=fold(x['il'])
    if ilf in il_resmi: x['il']=il_resmi[ilf]
    ham=x.get('ic') or '';sz=sozluk.get(ilf,{})
    k=fold(re.sub(r'\(.*?\)','',ham))
    if not k: x['ic']='';sayac['bos']+=1;continue
    k=TAKMA.get(k,k)
    if k==ilf: x['ic']='MERKEZ';sayac['merkez']+=1;continue
    # il adını baştan/sondan at ("bodrum mugla" -> "bodrum", "adiyaman merkez" -> "merkez")
    t=k.split()
    if len(t)>1 and ' '.join(t[-len(ilf.split()):])==ilf: t=t[:-len(ilf.split())]
    if len(t)>1 and ' '.join(t[:len(ilf.split())])==ilf: t=t[len(ilf.split()):]
    bulundu=None
    for n in range(len(t),0,-1):          # en uzun eşleşmeyi tercih et
        for i in range(len(t)-n+1):
            g=' '.join(t[i:i+n])
            if g in sz: bulundu=sz[g];break
        if bulundu:break
    if not bulundu and 'merkez' in t: bulundu='MERKEZ'
    if bulundu: x['ic']=bulundu;sayac['eslesti']+=1
    else: x['ic']='';sayac['bulunamadi']+=1;bulunamayan[(x['il'],ham)]+=1
# Aynı şarj ağının aynı noktadaki (≈10 m) tekrar kayıtlarını teke indir
gor=set();yeni=[]
for x in d:
    if x.get('tur')=='sarj':
        k=(x['m'],round(x['e'],4),round(x['b'],4))
        if k in gor: sayac['tekrar_silindi']+=1;continue
        gor.add(k)
    yeni.append(x)
d=yeni
# Şüpheli koordinatlı şarj kayıtlarını ele: (1) en az 3 farklı ilde aynı noktaya düşenler (konum bulunamayınca düşen varsayılan nokta),
# (2) koordinatı kendi ilinin akaryakıt istasyonlarının sınırlarından ~45 km'den fazla dışarıda kalanlar
kutu={}
for x in d:
    if x.get('tur')=='yakit' and x['il']:
        b=kutu.setdefault(x['il'],[99,99,0,0]);b[0]=min(b[0],x['e']);b[1]=min(b[1],x['b']);b[2]=max(b[2],x['e']);b[3]=max(b[3],x['b'])
ilsay=collections.defaultdict(set)
for x in d:
    if x.get('tur')=='sarj': ilsay[(round(x['e'],5),round(x['b'],5))].add(x['il'])
M=0.4;yeni=[]
for x in d:
    if x.get('tur')=='sarj':
        b=kutu.get(x['il'])
        if len(ilsay[(round(x['e'],5),round(x['b'],5))])>=3 or (b and not(b[0]-M<=x['e']<=b[2]+M and b[1]-M<=x['b']<=b[3]+M)):
            sayac['supheli_koordinat_silindi']+=1;continue
    yeni.append(x)
d=yeni
json.dump(d,open(out,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(dict(sayac));print('eşleşmeyenler (ilk 40):',bulunamayan.most_common(40))
