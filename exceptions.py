# exceptions.py
class NavigationError(Exception): 
    """هذا هو الأب الكبير لكل أخطاء مشروعنا"""
    pass

class InvalidCoordinateError(NavigationError):
    """هذا الابن متخصص فقط في أخطاء الإحداثيات"""
    def __init__(self, coord_type, value):
        self.message = f"Invalid {coord_type}: {value} is out of range."
        super().__init__(self.message)