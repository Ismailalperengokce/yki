# YKI - Yer Kontrol İstasyonu
## TEKNOFEST Sunucu Sistemi Entegrasyonu



### Proje Yapısı
```
yki/
├── backend/
│   ├── main.py              # Ana program
│   ├── api_client.py        # TEKNOFEST API istemcisi (boş)
│   ├── telemetry_manager.py # Telemetri yöneticisi (boş)
│   └── requirements.txt      # Bağımlılıklar
│   │_  camera                # görüntü alımı ve işleme
├── config.py               # Konfigürasyon
└── README.md              # Bu dosya
```

### Kurulum
```bash
cd /home/alp/yki/backend
pip install -r requirements.txt
python main.py
```

### API Bağlantı Bilgileri
- Sunucu: http://127.0.0.25:5000 #örnek
- Takım Adı: config.py'de TEAM_USERNAME
- Takım Şifresi: config.py'de TEAM_PASSWORD

### Yapılacak İşler
- [ ] `api_client.py` fonksiyonlarını doldurmak
- [ ] `telemetry_manager.py` fonksiyonlarını doldurmak
- [ ] `main.py` fonksiyonlarını doldurmak
- [ ] Terminal arayüzünü test etmek
