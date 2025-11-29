"""
TEKNOFEST Sunucu API İstemcisi
Tüm API endpoints'e bağlantı sağlar
"""
import requests
import json
from typing import Dict, Any, Optional
import sys
sys.path.append('..')
from config import SERVER_URL, ENDPOINTS


class ApiClient:
    """TEKNOFEST Sunucu API İstemcisi"""
    
    def __init__(self):
        self.base_url = SERVER_URL
        self.team_id = None
        self.session = requests.Session()
        self.last_error = None
    
    def login(self, username: str, password: str) -> bool:
        """
        Sunucuya giriş yap
        POST /api/giris
        """
        # Endpoint'e POST isteği gönder
        # JSON: {"kadi": username, "sifre": password}
        # Başarılıysa team_id'yi kaydet ve True döndür
        # Başarısızsa hata mesajı kaydet ve False döndür
        pass
    
    def get_server_time(self) -> Optional[Dict[str, int]]:
        """
        Sunucu saatini al
        GET /api/sunucusaati
        """
        # Endpoint'e GET isteği gönder
        # Başarılıysa JSON cevapı döndür (gun, saat, dakika, saniye, milisaniye)
        # Başarısızsa None döndür
        pass
    
    def send_telemetry(self, telemetry_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Telemetri verisini gönder
        POST /api/telemetri_gonder
        """
        # Endpoint'e POST isteği gönder (telemetry_data)
        # Başarılıysa JSON cevapı döndür (diğer takımların konumları)
        # Başarısızsa None döndür
        pass
    
    def send_lock_info(self, lock_data: Dict[str, Any]) -> bool:
        """
        Kilitlenme bilgisini gönder
        POST /api/kilitlenme_bilgisi
        """
        # Endpoint'e POST isteği gönder (lock_data)
        # Başarılıysa True döndür, aksi halde False döndür
        pass
    
    def send_kamikaze_info(self, kamikaze_data: Dict[str, Any]) -> bool:
        """
        Kamikaze bilgisini gönder
        POST /api/kamikaze_bilgisi
        """
        # Endpoint'e POST isteği gönder (kamikaze_data)
        # Başarılıysa True döndür, aksi halde False döndür
        pass
    
    def get_qr_coordinates(self) -> Optional[Dict[str, float]]:
        """
        QR koordinatlarını al
        GET /api/qr_koordinati
        """
        # Endpoint'e GET isteği gönder
        # Başarılıysa JSON cevapı döndür (qrEnlem, qrBoylam)
        # Başarısızsa None döndür
        pass
    
    def get_hss_coordinates(self) -> Optional[Dict[str, Any]]:
        """
        HSS koordinatlarını al
        GET /api/hss_koordinatlari
        """
        # Endpoint'e GET isteği gönder
        # Başarılıysa JSON cevapı döndür (sunucusaati, hss_koordinat_bilgileri listesi)
        # Başarısızsa None döndür
        pass
