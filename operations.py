from geometry import haversine

def find_nearest_station(my_lat, my_lon, stations_list):
    if not stations_list:
        return None
        
    min_dist = float('inf')
    closest_station = None
    
    for station in stations_list:
        d = haversine(my_lat, my_lon, station['lat'], station['lon'])
        if d < min_dist:
            min_dist = d
            closest_station = station
            
    return closest_station