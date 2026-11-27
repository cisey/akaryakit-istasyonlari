// Yakınımdaki Akaryakıt — çevrimdışı önbellek
const V='akaryakit-v4';
const KABUK=['./','index.html','hakkinda.html','istasyonlar.json','manifest.webmanifest','icon-192.png','icon-512.png'];
const DIS=['https://unpkg.com/leaflet@1.9.4/dist/leaflet.js','https://unpkg.com/leaflet@1.9.4/dist/leaflet.css','https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js','https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.css','https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.Default.css'];
self.addEventListener('install',e=>{
  e.waitUntil(caches.open(V).then(c=>Promise.all([c.addAll(KABUK),...DIS.map(u=>c.add(u).catch(()=>{}))])).then(()=>self.skipWaiting()));
});
self.addEventListener('activate',e=>{
  e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim()));
});
// Önce önbellekten hızlıca ver, arkadan güncelle (veri değişince bir sonraki açılışta yeni hali gelir)
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;
  const u=new URL(r.url);
  const bizim=u.origin===location.origin, leaflet=u.href.startsWith('https://unpkg.com/leaflet');
  if(!bizim&&!leaflet)return;   // harita karoları, yazı tipi, analitik: önbelleğe alma
  e.respondWith(caches.open(V).then(async c=>{
    const eski=await c.match(r,{ignoreSearch:true});
    const ag=fetch(r).then(y=>{if(y&&y.ok)c.put(r,y.clone());return y}).catch(()=>null);
    return eski||(await ag)||new Response('Çevrimdışı',{status:503});
  }));
});
