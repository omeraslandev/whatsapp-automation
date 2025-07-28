-----

### 🚀 Projenin Ruhu: WhatsApp Profil Fotoğrafı Otomasyonu

Sosyal medyada sürekli aynı yüzle var olmaktan sıkıldın mı? Her gün yeni bir mod, yeni bir enerji, yeni bir "sen" var. Peki dijital yansıman neden buna ayak uydurmasın?

Bu otomasyon, tam da bu noktada devreye giriyor. Senin için tasarladığımız bu akıllı sistem:

  * **Dinamik Kimlik 🎨:** Belirlediğin görsel koleksiyonundan her 24 saatte bir rastgele bir fotoğraf seçer ve WhatsApp profil fotoğrafın olarak ayarlar. Her güne yeni bir başlangıç\!
  * **Tam Otomasyon ⏰:** Bir kere kur, ve unut. Program, sen hayatına devam ederken arka planda sessizce çalışır. Manuel olarak profil fotoğrafı değiştirme derdine son. Biz buna "akıllı tembellik" diyoruz.
  * **Sonsuz Kişiselleştirme ✨:** Koleksiyon tamamen sana ait. İster en sevdiğin film karakterleri, ister doğa manzaraları, ister kendi çizimlerin... Tarzını sen belirlersin, gerisini teknoloji halleder.

Bu proje, **Selenium**'un gücünü kullanarak web otomasyonunun sınırlarını zorluyor ve sana zaman kazandırıyor. Çünkü en değerli kaynağımız zamandır ve biz onu boşa harcamana asla izin vermeyiz.

-----

### 🛠️ Kurulum ve Çalıştırma Rehberi: Adım Adım Mars'a... Pardon, WhatsApp'a\!

Projemizi hayata geçirmek, roket bilimi değil. Sadece aşağıdaki adımları takip et ve sihri izle\!

**1. Gereksinimler ✅**
Öncelikle bilgisayarında iki şeyin kurulu olması gerekiyor:

  * **Python:** Eğer yüklü değilse, [python.org](https://www.python.org/downloads/) adresinden indirebilirsin.
  * **Google Chrome:** Otomasyon Chrome tarayıcısı üzerinden çalışıyor.

**2. Proje Dosyalarını İndir 📂**

  * [GitHub proje sayfasına git](https://github.com/omeraslandev/whatsapp-pfp-automation).
  * Yeşil renkli **"\<\> Code"** butonuna tıkla ve **"Download ZIP"** seçeneği ile tüm dosyaları bilgisayarına indir.
  * İndirdiğin ZIP dosyasını klasöre çıkart.

**3. Görsellerini Hazırla 🖼️**

  * Proje klasörünün içinde **`images`** adında bir klasör oluştur.
  * Profil fotoğrafı olarak kullanmak istediğin tüm görselleri bu klasörün içine at.
  * **ÇOK ÖNEMLİ:** Fotoğraflarını `1.jpg`, `2.jpg`, `3.jpg`... şeklinde numaralandırmalısın. Kod, şu anki haliyle 1'den 48'e kadar olan fotoğraflar arasından rastgele seçim yapıyor. Eğer daha az veya daha çok fotoğrafın varsa, `main.py` dosyasındaki `pfp = random.randint(1, 48)` satırındaki `48` sayısını kendi fotoğraf adedinle değiştirmelisin.

**4. Gerekli Kütüphaneyi Yükle 📦**
Otomasyonun beyni olan Selenium kütüphanesini yüklememiz gerek. Bilgisayarında Komut İstemi'ni (CMD) veya Terminal'i aç ve şu komutu yazıp Enter'a bas:

```bash
pip install selenium
```

**5. Sürücüyü (ChromeDriver) Ayarla 🚗**
Bu, otomasyonun tarayıcını kontrol etmesini sağlayan köprüdür.

  * Önce Chrome tarayıcının sürümünü öğren. Chrome'da `Ayarlar > Chrome hakkında` kısmından sürüm numaranı (örneğin: `127.0.6533.72`) öğrenebilirsin.
  * [ChromeDriver indirme sayfasına git](https://googlechromelabs.github.io/chrome-for-testing/).
  * Kendi tarayıcı sürümüne **en uygun** ChromeDriver'ı bul ve `chromedriver-win64.zip` dosyasını indir.
  * İndirdiğin ZIP'ten çıkan `chromedriver.exe` dosyasını, projenin ana klasöründeki (`whatsapp-pfp-automation`) `chromedriver-win64` klasörünün içine at. Kodun yolu oraya ayarlı\!

**6. Otomasyonu Ateşle\! ▶️**
Her şey hazır\! Şimdi motorları çalıştırma zamanı.

  * Komut İstemi'ni (CMD) veya Terminal'i projenin ana klasöründe aç.
  * Aşağıdaki komutu yaz ve Enter'a basarak script'i başlat:
    ```bash
    python main.py
    ```
  * Script otomatik olarak bir Chrome penceresi açacak ve `web.whatsapp.com` adresine gidecek.
  * Telefonundan **QR kodu okutarak** WhatsApp Web'e giriş yap.
  * Giriş yaptıktan sonra, script'i çalıştırdığın terminal ekranına dön ve **"Did you login? (yes/no):"** sorusuna `yes` yazıp Enter'a bas.

İşte bu kadar\! Arkana yaslan ve script'in ilk profil fotoğrafını değiştirmesini izle. Artık o senin için her 24 saatte bir bu işlemi tekrarlayacak. Dijital kimliğin artık hiç olmadığı kadar canlı\! 😉
