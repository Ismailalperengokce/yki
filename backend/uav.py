# map_core/uav.py
class UAVObject:
    def __init__(self, uav_id, lat, lon, heading=0, altitude=0):
        self.uav_id = uav_id
        self.lat = lat
        self.lon = lon
        self.heading = heading
        self.altitude = altitude

    def update(self, lat, lon, heading=None, altitude=None):
        self.lat = lat
        self.lon = lon
        if heading is not None:
            self.heading = heading
        if altitude is not None:
            self.altitude = altitude