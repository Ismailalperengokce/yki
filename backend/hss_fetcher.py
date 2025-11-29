# import requests
# from .hss import HSSZone

# class HSSFetcher:
#     def __init__(self, url):
#         self.url = url

#     def fetch(self):
#         try:
#             r = requests.get(self.url, timeout=2)
#             data = r.json()

#             hss_list = []
#             for h in data.get("hss_koordinat_bilgileri", []):
#                 zone = HSSZone(
#                     zone_id=h["id"],
#                     lat=h["hssEnlem"],
#                     lon=h["hssBoylam"],
#                     radius_m=h["hssYaricap"]
#                 )
#                 hss_list.append(zone)

#             return hss_list

#         except Exception as e:
#             print("HSS Fetch error:", e)
#             return []
# from .hss import HSSZone   # ❌ bu yanlış
from hss import HSSZone       # ✅ bu doğru


class HSSFetcher:
    def fetch(self):
        print("Fake HSS data loaded.")
        return [
            HSSZone(zone_id=0, lat=41.5100, lon=36.1190, radius_m=80),
            HSSZone(zone_id=1, lat=41.5125, lon=36.1205, radius_m=100)
        ]
