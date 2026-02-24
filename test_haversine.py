from geometry import haversine


def test_same_point_should_return_zero():
    dist = haversine(30.0444, 31.2357, 30.0444, 31.2357)
    assert abs(dist) < 0.001


def test_cairo_to_alex_approximate_air_distance():
    dist = haversine(30.0444, 31.2357, 31.2001, 29.9187)
    assert 175 <= dist <= 185, f"Expected ~180 km, got {dist:.2f}"


def test_small_distance_north_of_cairo():
    dist = haversine(30.0444, 31.2357, 30.0534, 31.2357)
    assert 0.9 <= dist <= 1.1, f"Expected ~1 km, got {dist:.2f}"


def test_sydney_to_brisbane():
    dist = haversine(-33.8688, 151.2093, -27.4698, 153.0251)
    assert 700 <= dist <= 800, f"Expected ~730 km, got {dist:.2f}"


def test_pole_to_pole():
    dist = haversine(90.0, 0.0, -90.0, 0.0)
    assert 19900 <= dist <= 20100, f"Expected ~20000 km, got {dist:.2f}"


def test_distance_is_symmetric():
    d1 = haversine(30.0, 31.0, 32.0, 33.0)
    d2 = haversine(32.0, 33.0, 30.0, 31.0)
    assert abs(d1 - d2) < 1e-10
