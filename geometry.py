from math import atan2, cos, radians, sin, sqrt

EARTH_RADIUS_KM = 6371.0
    
def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    # تحويل الدرجات إلى راديان
    φ1 = radians(lat1)
    λ1 = radians(lon1)
    φ2 = radians(lat2)
    λ2 = radians(lon2)

    # فرق الاحداثيات
    Δφ = φ2 - φ1
    Δλ = λ2 - λ1

    a = sin(Δφ / 2) ** 2 + cos(φ1) * cos(φ2) * sin(Δλ / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_KM * c
