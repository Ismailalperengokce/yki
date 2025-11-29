# YKI Konfigürasyon Dosyası

# Sunucu Ayarları
SERVER_HOST = "127.0.0.25"
SERVER_PORT = 5000
SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"

# Takım Bilgileri
TEAM_USERNAME = "takimkadi"
TEAM_PASSWORD = "takimsifresi"
TEAM_ID = None  # Login sonrası doldurulur

# Telemetri Ayarları
TELEMETRY_FREQUENCY = 1  # Hz (saniye başına)
TELEMETRY_TIMEOUT = 2000  # ms

# API Endpoints
ENDPOINTS = {
    "login": "/api/giris",
    "server_time": "/api/sunucusaati",
    "telemetry": "/api/telemetri_gonder",
    "lock_info": "/api/kilitlenme_bilgisi",
    "kamikaze_info": "/api/kamikaze_bilgisi",
    "qr_coords": "/api/qr_koordinati",
    "hss_coords": "/api/hss_koordinatlari",
}

# UI Ayarları
UI_HOST = "localhost"
UI_PORT = 5001
UI_DEBUG = True
