# note: this file is not entirely accurate at cleaning the original location csv, sp I had to add some manual locations in addition, so the output will not exactly match the file 'geocoded_locations.csv'
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time

df = pd.read_csv("Greater Pittsburgh Food Bank\Pittsburgh Food Bank Distribution Locations.csv")
seen_streets = []

# removing duplicates
for i in range(df.shape[0]):
    row = df.iloc[i]
    street = row[1]
    print(street)
    seen_streets.append(street)
    if (street not in seen_streets):
        seen_streets.append(street)
print(len(seen_streets))

#Initialize geolocator
geolocator = Nominatim(user_agent="geoapi")

# Define geocoding function
def geocode_address(street, city, zipcode):
    address = {'street':street,'city':city, 'zipcode':zipcode}
    print(address)
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            return location.latitude, location.longitude
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding failed for {address}: {e}")
    return None, None

# Geocode each row 
latitudes = []
longitudes = []

for i in range(df.shape[0]):
    row = df.iloc[i]
    print(geocode_address(row[1], row[2], row[3]))
    lat, lon = geocode_address(row[1], row[2], row[3])
    latitudes.append(lat)
    longitudes.append(lon)
    print (lat,lon)
    time.sleep(1)

df['LAT'] = latitudes
df['LON'] = longitudes

df.to_csv("Greater Pittsburgh Food Bank\geocoded_locations.csv", index=False)


