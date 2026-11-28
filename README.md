# ⛽ Yakıt & Şarj Radarı

Türkiye'deki akaryakıt ve şarj istasyonlarını konumuna göre listeleyen, tek sayfalık bir web uygulaması. Yolda giderken "bana en yakın istasyon hangisi, hangisi önümde, yolumda şarj noktası var mı?" sorularının cevabını verir.

**Canlı site:** https://cisey.github.io/akaryakit-istasyonlari/

## Ne yapar?

- **Canlı konum takibi:** Konumun sürekli izlenir, liste ilerledikçe kendini günceller.
- **📍 Yakın:** İstasyonları mesafeye göre, en yakından başlayarak sıralar.
- **🧭 Önümde:** Gittiğin yönü algılar, sadece önünde kalan istasyonları gösterir. Yön, yaklaşık 30 metre ilerleyince bulunur.
- **🛣️ Güzergâh (yol üstü radar):** Nereye gideceğini yaz, yolun ±1/2/3 km'sindeki istasyonları sırayla ve "kaç km ileride" bilgisiyle listeler. Yolun sağında mı solunda mı olduğunu da yazar. Marka veya özellik seçersen (örneğin sadece LPG), o özelliğin 60 km'den uzun süre bulunmadığı yerleri ⚠️ ile uyarır. Konum açıksa geçtiğin istasyonlar listeden düşer.
- **🔍 Keşfet:** Konumdan bağımsız arama. İl ve ilçe seç, istasyon adı/il/ilçe/marka yaz; marka ve özellik filtreleriyle birlikte çalışır. Seçime uyan LPG / şarj / market / yıkama sayısını gösterir. Harita görünümü istasyonları kümeleyerek (yakınlaştırdıkça açılır) tüm Türkiye'yi gösterir.
- **Yön oku:** Her istasyonun yanındaki ok, istasyonun sana göre nerede kaldığını gösterir (önünde, sağında, solunda, arkanda).
- **Tahmini varış:** Hızın 10 km/s'in üzerindeyse istasyona kaç dakikada varacağını yazar.
- **Yol tarifi:** Tek dokunuşla Google Haritalar'da navigasyon başlatır.
- **⚡ Şarj istasyonları:** Akaryakıt istasyonlarının yanında 170 şarj ağının (ZES, Eşarj, Trugo, WAT, Voltrun…) yaklaşık 8.500 şarj noktası da var. Filtrelerdeki "⛽ Akaryakıt / ⚡ Şarj istasyonları / Hepsi" seçimiyle hangisini görmek istediğini seçersin (varsayılan akaryakıt). Şarj seçilince "şarj ağı" listesinden tek bir ağı süzebilirsin. Veride varsa DC / AC, kW bilgisi ve ağın ücret sayfasına bağlantı görünür. Şarj seçiliyken filtrelerde **DC hızlı** ve **AC** çipleri çıkar. Bu bilgi şu an sadece yaklaşık 350 noktada bulunduğu için, bu filtreleri açınca bilgisi olmayan noktalar listeden düşer. Seçtiğin şarj ağı bir sonraki açılışta hatırlanır. Güzergâh modunda da çalışır: örneğin "Ankara'ya kadar şarj yok" uyarısı alırsın.
- **Filtreler:** Marka, LPG, ⚡ şarj, 🛒 market, 🚿 yıkama ve mesafe (2 km'den "Tümü"ne). Seçimlerin sonraki açılışta hatırlanır.
- **Harita görünümü:** İstasyonları marka renkleriyle haritada gösterir. Haritadan bir nokta seçerek o bölgenin çevresine de bakabilirsin.
- **Çevrimdışı çalışır ve ana ekrana eklenir (PWA):** Bir kez internetle açtıktan sonra istasyon listesi telefonda saklanır. İnternet çekmeyen yerde de konumuna en yakın istasyonlar listelenir. Sayfanın üstündeki "📲 Ana ekrana ekle" düğmesiyle uygulama gibi kurulur.
- **Açık / koyu tema.**

## Kapsanan markalar

Akaryakıt: Opet, Petrol Ofisi, Shell, TotalEnergies, Aytemiz, Alpet, Sunpet, M Oil, TPPD, Kadoil — **8.461 istasyon**.

Şarj: 170 şarj ağı (ZES, Eşarj, Trugo, WAT, Voltrun, Sharz.net, Astor ve diğerleri) — **8.536 şarj noktası**.

## Nasıl kullanılır?

1. Siteyi aç, **"📍 Canlı Konumumu Kullan"** düğmesine dokun.
2. Tarayıcı konum izni isterse **izin ver**.
3. Liste otomatik gelir. Yol tarifi için istasyonun yanındaki **"Yol tarifi"** düğmesine dokun.
4. Marka veya özellik seçmek için **"⚙️ Filtreler"** düğmesini kullan.

Konum izni vermek istemezsen **"🗺️ Haritadan Nokta Seç"** ile haritada bir yere dokunarak da bakabilirsin.

> 💡 En doğru sonuç telefondadır. Bilgisayar tarayıcıları konumu Wi-Fi üzerinden tahmin eder, bu yüzden yaklaşık bir nokta verir ve "Önümde" modu çalışmaz (hareket algılanamaz).

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `index.html` | Uygulamanın kendisi. Açılışta `tum_istasyonlar_birlesik.json` dosyasını okur. |
| `sw.js`, `manifest.webmanifest`, `icon-*.png` | Çevrimdışı çalışma ve ana ekrana ekleme için gerekli dosyalar. |
| `tum_istasyonlar_birlesik.json` | Akaryakıt ve şarj istasyonlarının tek dosyada birleşik listesi (tür, marka/ağ, isim, il, ilçe, koordinat, LPG / şarj / market / yıkama / DC / AC bilgisi, varsa ücret bağlantısı). |
| `istasyonlar.json` | Eski, yalnızca akaryakıt içeren liste. Artık kullanılmıyor, silinebilir. |

## Gizlilik

Konum bilgin yalnızca kendi tarayıcında işlenir, hiçbir sunucuya gönderilmez ve kaydedilmez. Tarayıcıda sadece tema, seçili marka ve mesafe tercihin saklanır.

## Bilinen sınırlar

- **Şarj verisi eksik olabilir.** Şarj noktalarının bir kısmında güç (kW) ve soket tipi bilinmiyor. Aynı yerdeki tekrar kayıtlar teke indirildi, hatalı koordinatlı kayıtlar silindi.
- **Fiyat bilgisi yok.** Veride akaryakıt fiyatı bulunmadığı için sıralama sadece konuma göre yapılır.
- **Veri sabittir.** Yeni açılan veya kapanan istasyonlar otomatik yansımaz. Veriyi güncellemek için sadece `tum_istasyonlar_birlesik.json` dosyasını değiştirmen yeterli, `index.html`'e dokunmak gerekmez.
- **Çalışma saatleri yok.** İstasyonun açık olup olmadığı bilinmez.
- **Çevrimdışıyken harita karoları gelmez.** Liste çalışır, harita görünümünde zemin görüntüsü olmaz (nokta ve istasyonlar yine de görünür).
- **Güzergâh için internet gerekir.** Yol çizgisi OSRM, yer arama OpenStreetMap Nominatim servisinden alınır. İkisi de ücretsiz ve kişisel kullanıma uygundur, ama çok yoğun kullanımda sınır koyabilirler.
- **İlk açılış internet ister.** Liste telefona ilk açılışta indirilir.
- Konum özelliği sadece güvenli bağlantıda (`https`) çalışır; GitHub Pages bunu sağlar.

## Teknik not

Tek dosyalık, bağımlılıksız bir HTML/JavaScript uygulamasıdır. Harita için [Leaflet](https://leafletjs.com/) ve [OpenStreetMap](https://www.openstreetmap.org/) kullanılır. Mesafeler kuş uçuşu (haversine) hesaplanır, yani gerçek yol mesafesinden kısa çıkabilir.
