# Almanca Fiil Çekim Testi

Kivy tabanlı, Android için Almanca fiil çekimi alıştırma uygulaması.
Uygulama rastgele bir fiil + özne (ich/du/er-sie-es/wir/ihr/sie-Sie) + kip/zaman
(İndikatif, Konjunktiv I, Konjunktiv II × Präsens, Präteritum, Perfekt,
Plusquamperfekt, Futur I/II) kombinasyonu sorar; siz çekimlenmiş fiili
yazıp gönderirsiniz, uygulama doğru/yanlış olduğunu söyler.

- 725 fiil, hepsinin Türkçe anlamı ve tam çekim tablosu `data/fiiller_duzeltilmis.json`
  içinde. Bu dosya `duzenli_dosyaniz.json` + `fiiller.txt` birleştirilip
  bazı fiillerde eksik/bozuk çıkan ö/ü harfleri düzeltilerek oluşturuldu.

## Dosyalar
- `main.py` – uygulama mantığı
- `quiz.kv` – arayüz
- `data/fiiller_duzeltilmis.json` – fiil + çekim + anlam verisi
- `buildozer.spec` – Android derleme ayarları (Redmi Note 9 için arm64-v8a/armeabi-v7a)

## GitHub'a yükleme

```bash
cd almanca_app
git init
git add .
git commit -m "İlk sürüm: Almanca çekim testi"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADIN/almanca-cekim-testi.git
git push -u origin main
```

## Google Colab ile APK derleme

Yeni bir Colab not defterinde:

```python
!git clone https://github.com/KULLANICI_ADIN/almanca-cekim-testi.git
%cd almanca-cekim-testi
!pip install buildozer cython==0.29.36
!apt update
!apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config \
    zlib1g-dev libncurses-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!buildozer android debug
```

Derleme bitince APK `bin/` klasöründe oluşur:

```python
from google.colab import files
files.download('bin/almancacekim-0.1-arm64-v8a_armeabi-v7a-debug.apk')
```

(Buildozer sürümüne göre dosya adı biraz farklı çıkabilir; tam adı görmek için
derleme bitince `!ls bin/` çalıştırın.) İndirilen `.apk` dosyasını Redmi Note 9'a
aktarıp yükleyin (bilinmeyen kaynaklardan yükleme izni gerekebilir).

## Notlar / bilinen sınırlamalar
- Kaynak `duzenli_dosyaniz.json` içinde "drücken" fiilinin kendi çekim kaydı
  hiç yoktu, o yüzden 725 fiil arasında değil.
- Cevap kontrolü büyük/küçük harf ve baş/son boşluğa duyarsız, ama Almanca
  özel harfler (ä ö ü ß) tam eşleşmeli.
