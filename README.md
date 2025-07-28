### 😎 WhatsApp PFP Otomasyonu: Çalıştırma Macerası\! 😎

Selam Kaptan\! Dijital kimliğini her gün tazeleyecek bu efsane otomasyonu çalıştırmaya hazır mısın? O zaman kemerleri bağla, çünkü adım adım zafere ulaşıyoruz\!

-----

#### Adım 1: Cephaneliği Dolduruyoruz\! 🔫 (Gerekli Kütüphaneler)

Öncelikle bu operasyon için bize lazım olan tek bir sihirli değnek var: `selenium`. Gel onu terminalden veya komut istemcisinden hemen indirelim.

```bash
pip install selenium
```

Bunu yazdığında, Python bizim için gerekli olan bu kütüphaneyi indirip kuracak. Artık tarayıcıyı uzaktan kontrol etme gücüne sahibiz\! 💪

#### Adım 2: Arabanın Anahtarı: ChromeDriver 🔑

Selenium, tarayıcıyı kontrol etmek için bir "anahtar"a ihtiyaç duyar. Bu anahtarın adı `ChromeDriver`.

1.  **Versiyon Kontrolü:** Önce bilgisayarındaki Google Chrome tarayıcısının versiyonunu öğren.

      * Chrome'u aç, sağ üstteki üç noktaya tıkla.
      * `Yardım` \> `Google Chrome hakkında` yolunu izle.
      * Orada yazan versiyon numarasını (örneğin `127.0.589.34`) bir kenara not et. 📝

2.  **Doğru Anahtarı İndir:** Google'a "ChromeDriver download" yazarak resmi indirme sitesine git. Oradan, kendi Chrome versiyonunla **birebir aynı olan** ChromeDriver'ı indir. Bu çok önemli, yoksa araba çalışmaz\! 🚗💨

3.  **Anahtarı Doğru Yere Koy:** İndirdiğin `.zip` dosyasını aç. İçinden çıkan `chromedriver.exe` dosyasını, projenin ana klasöründe (`whatsapp-pfp-automation`) yeni bir klasör oluşturup içine at. Klasörün adı `chromedriver-win64` olmalı.

      * Yani dosya yolun şöyle gözükecek: `.../whatsapp-pfp-automation/chromedriver-win64/chromedriver.exe`

#### Adım 3: Sanat Galerimizi Oluşturuyoruz\! 🖼️

Şimdi en eğlenceli kısım\! Programın her gün seçeceği o havalı profil fotoğraflarını hazırlama zamanı.

1.  Projenin ana klasöründe `images` adında bir klasör oluştur.
2.  İçine istediğin kadar fotoğraf at\! Ama bir kural var: Fotoğrafların isimleri `1.jpg`, `2.jpg`, `3.jpg`... şeklinde sayılarla gitmeli.
3.  Kod şu an 1 ile 48 arasında rastgele bir sayı seçiyor. İstersen koddaki `random.randint(1, 48)` satırını değiştirerek bu aralığı kendi fotoğraf sayına göre ayarlayabilirsin. 😉

#### Adım 4: Motoru Çalıştırıyoruz\! 🔥

Her şey hazır olduğuna göre, artık marşa basabiliriz\! Terminali veya komut istemcisini aç ve projenin ana klasörüne git. Sonra şu sihirli komutu yaz:

```bash
python main.py
```

Enter'a bastığın an... BOOM\! 💥 Yeni bir Chrome penceresi açılacak ve içinde WhatsApp Web yüklenecek.

#### Adım 5: Olay Yeri Devir Teslimi 🤝

Otomasyon henüz kontrolü ele almadı. Önce senin küçük bir dokunuş yapman gerekiyor.

1.  Açılan WhatsApp Web ekranındaki QR kodu, telefonundaki WhatsApp uygulamasıyla okut.
2.  Giriş yapıp sohbetlerinin yüklenmesini bekle.
3.  Her şey tamamlandığında, programı başlattığın o siyah terminal ekranına geri dön. Orada seni bekleyen bir soru olacak: `Did you login? (yes/no):`
4.  Buraya kahramanca `yes` yaz ve Enter tuşuna bas\!

#### Adım 6: Arkana Yaslan ve Şovu İzle\! 🍿

İşte bu kadar\! `yes` dedikten sonra otomasyon gücü ele alır. Gözlerinin önünde ilk profil fotoğrafını şak diye değiştirecek. Ardından, 24 saatlik derin bir uykuya dalacak ve ertesi gün aynı saatte uyanıp yeni bir fotoğrafla dijital kimliğini tekrar tazeleyecek.

Artık sen de her gün farklı bir yüze sahip, gizemli ve havalı bir dijital ajansın\! 😎 Görev başarıyla tamamlandı\! ✅
