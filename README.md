# ⛽ Yakınımdaki Akaryakıt İstasyonları

Türkiye'deki akaryakıt istasyonlarını konumuna göre listeleyen, tek sayfalık bir web uygulaması. Yolda giderken "bana en yakın istasyon hangisi, hangisi önümde?" sorusunun cevabını verir.

**Canlı site:** https://cisey.github.io/akaryakit-istasyonlari/

## Ne yapar?

- **Canlı konum takibi:** Konumun sürekli izlenir, liste ilerledikçe kendini günceller.
- **📍 Çevremde:** İstasyonları mesafeye göre, en yakından başlayarak sıralar.
- **🧭 Önümde:** Gittiğin yönü algılar, sadece önünde kalan istasyonları gösterir. Yön, yaklaşık 30 metre ilerleyince bulunur.
- **🛣️ Güzergâh (yol üstü radar):** Nereye gideceğini yaz, yolun ±1/2/3 km'sindeki istasyonları sırayla ve "kaç km ileride" bilgisiyle listeler. Yolun sağında mı solunda mı olduğunu da yazar. Marka veya özellik seçersen (örneğin sadece LPG), o özelliğin 60 km'den uzun süre bulunmadığı yerleri ⚠️ ile uyarır. Konum açıksa geçtiğin istasyonlar listeden düşer.
- **Yön oku:** Her istasyonun yanındaki ok, istasyonun sana göre nerede kaldığını gösterir (önünde, sağında, solunda, arkanda).
- **Tahmini varış:** Hızın 10 km/s'in üzerindeyse istasyona kaç dakikada varacağını yazar.
- **Yol tarifi:** Tek dokunuşla Google Haritalar'da navigasyon başlatır.
- **Filtreler:** Marka, LPG, ⚡ şarj, 🛒 market, 🚿 yıkama ve mesafe (2 km'den "Tümü"ne). Seçimlerin sonraki açılışta hatırlanır.
- **Harita görünümü:** İstasyonları marka renkleriyle haritada gösterir. Haritadan bir nokta seçerek o bölgenin çevresine de bakabilirsin.
- **Çevrimdışı çalışır ve ana ekrana eklenir (PWA):** Bir kez internetle açtıktan sonra istasyon listesi telefonda saklanır. İnternet çekmeyen yerde de konumuna en yakın istasyonlar listelenir. Sayfanın üstündeki "📲 Ana ekrana ekle" düğmesiyle uygulama gibi kurulur.
- **Açık / koyu tema.**

## Kapsanan markalar

Opet, Petrol Ofisi, Shell, TotalEnergies, Aytemiz, Alpet, Sunpet, M Oil, TPPD, Kadoil — toplam **8.461 istasyon**.

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
| `index.html` | Uygulamanın kendisi. Açılışta `istasyonlar.json` dosyasını okur. |
| `sw.js`, `manifest.webmanifest`, `icon-*.png` | Çevrimdışı çalışma ve ana ekrana ekleme için gerekli dosyalar. |
| `istasyonlar.json` | Tüm markaların tek dosyada birleşik istasyon listesi (marka kodu, isim, il, ilçe, koordinat, LPG / şarj / market / yıkama bilgisi). |

## Gizlilik

Konum bilgin yalnızca kendi tarayıcında işlenir, hiçbir sunucuya gönderilmez ve kaydedilmez. Tarayıcıda sadece tema, seçili marka ve mesafe tercihin saklanır.

## Bilinen sınırlar

- **Fiyat bilgisi yok.** Veride akaryakıt fiyatı bulunmadığı için sıralama sadece konuma göre yapılır.
- **Veri sabittir.** Yeni açılan veya kapanan istasyonlar otomatik yansımaz. Veriyi güncellemek için sadece `istasyonlar.json` dosyasını değiştirmen yeterli, `index.html`'e dokunmak gerekmez.
- **Çalışma saatleri yok.** İstasyonun açık olup olmadığı bilinmez.
- **Çevrimdışıyken harita karoları gelmez.** Liste çalışır, harita görünümünde zemin görüntüsü olmaz (nokta ve istasyonlar yine de görünür).
- **Güzergâh için internet gerekir.** Yol çizgisi OSRM, yer arama OpenStreetMap Nominatim servisinden alınır. İkisi de ücretsiz ve kişisel kullanıma uygundur, ama çok yoğun kullanımda sınır koyabilirler.
- **İlk açılış internet ister.** Liste telefona ilk açılışta indirilir.
- Konum özelliği sadece güvenli bağlantıda (`https`) çalışır; GitHub Pages bunu sağlar.

## Teknik not

Tek dosyalık, bağımlılıksız bir HTML/JavaScript uygulamasıdır. Harita için [Leaflet](https://leafletjs.com/) ve [OpenStreetMap](https://www.openstreetmap.org/) kullanılır. Mesafeler kuş uçuşu (haversine) hesaplanır, yani gerçek yol mesafesinden kısa çıkabilir.
