import math
from exceptions import InvalidCoordinateError 

def validate_coordinates(lat, lon):
    """
    Ensures data integrity and prevents 'Numerical Evaporation'.
    Implements Tolerance based on Machine Epsilon (Sauer, Chapter 1).
    """
    TOLERANCE = 1e-9

    try:
        # Ensures compatibility and converts strings like "25.5" to float
        lat_f = float(lat)
        lon_f = float(lon)
    except (ValueError, TypeError):
        raise TypeError(f"Coordinates must be numbers, got {type(lat).__name__}")

    # Prevent crashes from NaN or Infinity
    if not math.isfinite(lat_f) or not math.isfinite(lon_f):
        raise ValueError("Digital Integrity Error: Coordinates cannot be NaN or Infinity.")

    # Planetary boundary check with Tolerance
    if not (-90 - TOLERANCE <= lat_f <= 90 + TOLERANCE):
        raise InvalidCoordinateError("Latitude", lat_f)
        
    if not (-180 - TOLERANCE <= lon_f <= 180 + TOLERANCE):
        raise InvalidCoordinateError("Longitude", lon_f)
    
    return lat_f, lon_f