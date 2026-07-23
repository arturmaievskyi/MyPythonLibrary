

import math


class areaOf3DFigures:
    """Class to calculate surface area of different 3D geometric figures."""
    
    @staticmethod
    def sphere(radius):
        """Calculate surface area of a sphere given its radius."""
        return 4 * math.pi * radius ** 2
    
    @staticmethod
    def cylinder(radius, height):
        """Calculate surface area of a cylinder given its radius and height."""
        return 2 * math.pi * radius * (radius + height)
    
    @staticmethod
    def cone(radius, slant_height):
        """Calculate surface area of a cone given its radius and slant height."""
        return math.pi * radius * (radius + slant_height)
    
    @staticmethod
    def cube(side):
        """Calculate surface area of a cube given its side length."""
        return 6 * side ** 2
    
    @staticmethod
    def regular_polyron(sides, length):
        """Calculate surface area of a regular polyron given the number of sides and length of each side."""
        n = sides
        s = length
        return (n * s ** 2) / (4 * math.tan(math.pi / n)) + (n * s * math.sqrt((s ** 2) - ((s / (2 * math.tan(math.pi / n))) ** 2))) / 2

