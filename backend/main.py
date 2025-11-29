"""
YKI - Yer Kontrol İstasyonu
Ana Program Dosyası

"""
import sys
import os

# map_core modüllerini import et
from map_manager import MapManager
from uav import UAVObject
from hss_fetcher import HSSFetcher

# diğer modüller
#from config import TEAM_USERNAME, TEAM_PASSWORD
#from api_client import ApiClient
#from telemetry_manager import TelemetryManager
from camera import CameraStream

import cv2
import time


def camera():
    # Bilgisayar kamerası için GStreamer pipeline
    pipeline = (
        "v4l2src device=/dev/video0 ! "
        "video/x-raw, width=640, height=480, framerate=30/1 ! "
        "videoconvert ! appsink"
    )

    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        raise RuntimeError("Kamera açılamadı! Pipeline yanlış olabilir.")

    print("Kamera başlatıldı...")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            # -----------------------------------------
            # YOLO MODELİ BURAYA GELECEK
            # ör:
            # results = model(frame)
            # boxes = results[0].boxes
            # -----------------------------------------
            pass  # şimdilik hiçbir şey yapmıyor

            # Test amacıyla görüntüyü göster
            cv2.imshow("Camera Test", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.01)

    except KeyboardInterrupt:
        print("Kamera kapatılıyor...")

    cap.release()
    cv2.destroyAllWindows()

def hss():
     # Harita yöneticisi
    manager = MapManager()

    # Sahte İHA ekleyelim
    manager.add_uav(UAVObject(1, 41.5100, 36.1180))
    manager.add_uav(UAVObject(2, 41.5120, 36.1190))

    # HSS verisini çek
   # hss_fetch = HSSFetcher("http://127.0.0.1:5001/hss")
    #zones = hss_fetch.fetch()
    #manager.set_hss_zones(zones)
    hss_fetch = HSSFetcher()
    zones = hss_fetch.fetch()
    manager.set_hss_zones(zones)


    # Sahte güncelleme (main döngüsünde olacak)
    manager.update_uav(1, 41.5105, 36.1185)
    manager.update_uav(2, 41.5125, 36.1195)

    # Haritayı oluştur
    output = manager.render("test_map.png")
    print("Map saved to:", output)

def main():
    #camera()
    """
    Ana program döngüsü
    
    İşleyiş:
    1. ApiClient örneği oluştur
    2. Sunucuya giriş yap (login)
    3. Sunucu saatini al ve senkronize et
    4. Telemetri ve görüntü göndermesini başlat 
    5. Görevleri (kilitlenme, kamikaze) işle
    6. İstatistikleri düzenli olarak göster
    7. Çıkış sinyaline kadar çalışmaya devam et
    """
    hss()


def display_menu():
    """
    Kullanıcı menüsünü göster
    
    Seçenekler:
    1. Sunucu saatini göster
    2. QR koordinatlarını göster
    3. HSS bölgelerini göster
    4. Kilitlenme bildirimi gönder
    5. Kamikaze bildirimi gönder
    6. Telemetri istatistiklerini göster
    7. Çıkış
    """
    pass


def handle_user_input(api_client, telemetry_manager):
    """
    Kullanıcı girdisini işle
    
    Parametreler:
    - api_client: ApiClient örneği
    - telemetry_manager: TelemetryManager örneği
    
    İşlem:
    - Kullanıcıdan seçim iste
    - Seçime göre ilgili işlemi yap
    """
    pass


def show_telemetry_stats(telemetry_manager):
    """
    Telemetri istatistiklerini göster
    
    Gösterilecek bilgiler:
    - Çalışıyor mu?
    - Gönderilen paket sayısı
    - Hata sayısı
    - Son telemetri verisi
    """
    pass


def show_server_time(api_client):
    """
    Sunucu saatini al ve göster
    
    İşlem:
    - get_server_time() çağır
    - Başarılıysa saat bilgilerini yazdır
    - Başarısızsa hata mesajı göster
    """
    pass


def show_qr_coordinates(api_client):
    """
    QR koordinatlarını al ve göster
    
    İşlem:
    - get_qr_coordinates() çağır
    - Başarılıysa enlem/boylam bilgilerini yazdır
    - Başarısızsa hata mesajı göster
    """
    pass


def show_hss_zones(api_client):
    """
    HSS bölgelerini al ve göster
    
    İşlem:
    - get_hss_coordinates() çağır
    - Başarılıysa her bölgenin bilgilerini tablosu şeklinde göster
    - Başarısızsa hata mesajı göster
    """
    pass


def send_lock_notification(api_client):
    """
    Kilitlenme bildirimi gönder
    
    İşlem:
    - Kullanıcıdan saati iste (veya şimdiki zamanı kullan)
    - Kilitlenme veri strukturunu oluştur
    - send_lock_info() çağır
    - Sonuç mesajını göster
    """
    pass


def send_kamikaze_notification(api_client):
    """
    Kamikaze bildirimi gönder
    
    İşlem:
    - Kullanıcıdan başlangıç ve bitiş saatlerini iste
    - Kamikaze veri strukturunu oluştur (qrMetni: "teknofest2025")
    - send_kamikaze_info() çağır
    - Sonuç mesajını göster
    """
    pass


def login(api_client):
    """
    Sunucuya giriş yap
    
    İşlem:
    - login() çağır
    - Başarılıysa takım numarasını göster
    - Başarısızsa hata mesajı göster ve False döndür
    """
    pass


if __name__ == "__main__":
    main()
