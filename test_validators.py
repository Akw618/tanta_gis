import pytest
from validators import validate_coordinates
from exceptions import InvalidCoordinateError

# 1. اختبار الحارس: هل يكتشف الأرقام الفضائية؟
def test_out_of_range_coordinates():
    with pytest.raises(InvalidCoordinateError):
        validate_coordinates(100, 30)  # خط عرض 100 مستحيل

# 2. اختبار الحارس: هل يكتشف النصوص؟
def test_string_coordinates():
    with pytest.raises(TypeError):
        validate_coordinates("Cairo", 30)

# 3. اختبار الحارس: هل يكتشف الثقوب السوداء (NaN)؟
def test_nan_coordinates():
    import math
    with pytest.raises(ValueError):
        validate_coordinates(math.nan, 30)

# 4. اختبار التسامح (Tolerance): هل هو "حليم" مع الأخطاء الصغيرة؟
def test_tolerance_acceptance():
    # 90.0000000001 يجب أن تمر لأنها ضمن الـ 1e-9
    lat, lon = validate_coordinates(90.0000000001, 30)
    assert lat == 90.0000000001