import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class MapManager:
    def __init__(self):
        self.uav_list = {}
        self.hss_zones = []

    def add_uav(self, uav_obj):
        self.uav_list[uav_obj.uav_id] = uav_obj

    def update_uav(self, uav_id, lat, lon, heading=None, altitude=None):
        if uav_id in self.uav_list:
            self.uav_list[uav_id].update(lat, lon, heading, altitude)

    def set_hss_zones(self, zones):
        self.hss_zones = zones

    def render(self, save_path="map_output.png"):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_facecolor("white")

        for uav in self.uav_list.values():
            ax.plot(uav.lon, uav.lat, marker="o", color="blue")
            ax.text(uav.lon, uav.lat, f"UAV {uav.uav_id}", fontsize=8)

        for zone in self.hss_zones:
            ax.plot(zone.lon, zone.lat, marker="x", color="red")
            c = Circle((zone.lon, zone.lat), zone.radius_m * 0.00001,
                       color="red", fill=True, alpha=0.2)
            ax.add_patch(c)
            ax.text(zone.lon, zone.lat, f"HSS {zone.zone_id}", fontsize=8)

        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.grid(True)
        ax.set_title("UAV & HSS Map")

        plt.savefig(save_path, dpi=150)
        plt.close(fig)

        return save_path
