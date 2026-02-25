from validators import validate_coordinates
from geometry import haversine
from exceptions import NavigationError

def find_nearest_station(my_lat, my_lon, stations_list):
    """
    Orchestrates the search process: Validates input then finds the closest point.
    """
    try:
        # Guard the borders and transform input
        clean_lat, clean_lon = validate_coordinates(my_lat, my_lon)
        
        if not stations_list:
            return None
            
        min_dist = float('inf')
        closest_station = None
        
        for station in stations_list:
            d = haversine(clean_lat, clean_lon, station['lat'], station['lon'])
            if d < min_dist:
                min_dist = d
                closest_station = station
                
        return closest_station

    except NavigationError as e:
        print(f"🚨 Navigation Alert: {e}")
        return None
    except (ValueError, TypeError) as e:
        print(f"🚨 Data Integrity Alert: {e}")
        return None