from operations import find_nearest_station


egypt_stations = [
    {"name": "Port Said", "lat": 31.2653, "lon": 32.3019},
    {"name": "Damietta", "lat": 31.4392, "lon": 31.7483},
    {"name": "Alexandria", "lat": 31.2001, "lon": 29.9187},
]

my_location = (30.7865, 31.0004) 

result = find_nearest_station(my_location[0], my_location[1], egypt_stations)

print(f"The nearest station to Tanta is: {result['name']} at {result['lat']}, {result['lon']}")