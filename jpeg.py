#!/usr/bin/env python
from fractions import Fraction

import piexif
from PIL import Image, ImageDraw, ImageFont
from geo import get_destination

# exif decimal to DMS conversion courtesy of c060604:
# https://gist.github.com/c060604/8a51f8999be12fc2be498e9ca56adc72

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)

def to_deg(value, loc):
    if value < 0:
        loc_value = loc[0]
    elif value > 0:
        loc_value = loc[1]
    else:
        loc_value = ""
    abs_value = abs(value)
    degrees = int(abs_value)
    t1 = (abs_value - degrees) * 60
    minutes = int(t1)
    seconds = round((t1 - minutes) * 60, 5)
    return degrees, minutes, seconds, loc_value


def change_to_rational(number):
    """convert a number to rantional

    Keyword arguments: number
    return: tuple like (1, 2), (numerator, denominator)
    """
    f = Fraction(str(number))
    return f.numerator, f.denominator


def create_exif(file, lat, lng, altitude):
    lat_deg = to_deg(lat, ["S", "N"])
    lng_deg = to_deg(lng, ["W", "E"])
    exiv_lat = (change_to_rational(lat_deg[0]), change_to_rational(lat_deg[1]), change_to_rational(lat_deg[2]))
    exiv_lng = (change_to_rational(lng_deg[0]), change_to_rational(lng_deg[1]), change_to_rational(lng_deg[2]))

    zeroth_ifd = {piexif.ImageIFD.Make: "Canon",  # ASCII, count any
                  piexif.ImageIFD.XResolution: (96, 1),  # RATIONAL, count 1
                  piexif.ImageIFD.YResolution: (96, 1),  # RATIONAL, count 1
                  piexif.ImageIFD.Software: "piexif"  # ASCII, count any
                  }
    exif_ifd = {piexif.ExifIFD.ExifVersion: b"\x02\x00\x00\x00",  # UNDEFINED, count 4
                piexif.ExifIFD.LensMake: "LensMake",  # ASCII, count any
                piexif.ExifIFD.Sharpness: 65535,  # SHORT, count 1 ... also be accepted '(65535,)'
                piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1)),  # Rational, count 4
                }
    gps_ifd = {piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),  # BYTE, count 4
               piexif.GPSIFD.GPSLatitudeRef: lat_deg[3],
               piexif.GPSIFD.GPSLatitude: exiv_lat,
               piexif.GPSIFD.GPSLongitudeRef: lng_deg[3],
               piexif.GPSIFD.GPSLongitude: exiv_lng,
               piexif.GPSIFD.GPSAltitude: change_to_rational(round(altitude)),
               }
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd}
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, file)

def createImage(file, label, lat, lng, altitude):
    img = Image.new('RGB', (300, 100), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 10), label, fill=(255, 255, 0), font=fnt)
    img.save(file + '.jpg')
    create_exif(file + '.jpg', lat, lng, altitude)



#createImage('test', 'ktm6', 34.0846312, -84.4785201, 800)
