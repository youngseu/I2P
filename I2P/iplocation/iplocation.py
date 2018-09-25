import geoip2.database


# # create a reader object
# reader = geoip2.database.Reader('/home/yang/pyproject/i2p/GeoLite2-City.mmdb')
# # give the ip address
# response = reader.city('223.3.68.179')
# # get the attribution of the ip
# print(response.country.iso_code)
#
# print(response.location.latitude)
#
# print(response.location.longitude)
#
# reader.close()
def lookup_lat_and_long(ip):
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
    try:
        response = reader.city(ip)
        lat = response.location.latitude
        lng = response.location.longitude
        reader.close()
        return {"lat": lat, "lng": lng}
    except geoip2.errors.AddressNotFoundError:
        return None


if __name__ == '__main__':
    result = lookup_lat_and_long('217.82.84.59')
    print(result['lat'])
