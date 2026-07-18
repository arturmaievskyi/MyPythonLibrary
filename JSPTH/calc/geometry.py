from .advanced_calculator import*
from .base_calculator import*

bcalc = BaseCalculator()
acalc = AdvancedCalculator()

class BaseGeometry:
    def __init__(self):
        pass

    def area_of_circle(self, radius):
        return acalc.circle_area(radius)
    
    def area_of_rectangle(self, length, width):
        return acalc.rectangle_area(length, width)
    
    def area_of_triangle(self, base, height):
        return acalc.triangle_area(base, height)
    
    def area_of_square(self, side):
        return acalc.square_area(side)
    
    def area_of_trapezoid(self, base1, base2, height):
        return acalc.trapezoid_area(base1, base2, height)
    
    def area_of_parallelogram(self, base, height):
        return acalc.parallelogram_area(base, height)
    
    def area_of_ellipse(self, major_axis, minor_axis):
        return acalc.ellipse_area(major_axis, minor_axis)
    
    def area_of_sector(self, radius, angle):
        return acalc.sector_area(radius, angle)
    

class AdvancedGeometry:
    pass