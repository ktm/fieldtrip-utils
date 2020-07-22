# http://www.movable-type.co.uk/scripts/latlong.html

import math

R = 6378.1  # Radius of the Earth


def get_destination(lat, lng, degrees, kilometers):
    bearing_radians = math.radians(degrees)
    lat_radians = math.radians(lat)
    lng_radians = math.radians(lng)
    dest_lat_radians = math.asin(math.sin(lat_radians) * math.cos(kilometers / R) +
                                 math.cos(lat_radians) * math.sin(kilometers / R) * math.cos(bearing_radians))
    dest_long_radians = \
        lng_radians + math.atan2(math.sin(bearing_radians) * math.sin(kilometers / R) * math.cos(lat_radians),
                                 math.cos(kilometers / R) - math.sin(lat_radians) * math.sin(dest_lat_radians))
    dest_lat = math.degrees(dest_lat_radians)
    dest_long = math.degrees(dest_long_radians)
    return dest_lat, dest_long
