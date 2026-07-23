
import math


class volumeOf3DFigures:
    """Class to calculate volume of different 3D geometric figures."""
    
    @staticmethod
    def sphere(radius):
        """Calculate volume of a sphere given its radius."""
        return (4/3) * math.pi * radius ** 3
    
    @staticmethod
    def cylinder(radius, height):
        """Calculate volume of a cylinder given its radius and height."""
        return math.pi * radius ** 2 * height
    
    @staticmethod
    def cone(radius, height):
        """Calculate volume of a cone given its radius and height."""
        return (1/3) * math.pi * radius ** 2 * height
    
    @staticmethod
    def cube(side):
        """Calculate volume of a cube given its side length."""
        return side ** 3
    
    @staticmethod
    def rectangular_prism(length, width, height):
        """Calculate volume of a rectangular prism given its length, width, and height."""
        return length * width * height

    @staticmethod
    def pyramid(base_length, base_width, height):
        """Calculate volume of a pyramid given its base length, base width, and height."""
        return (1/3) * base_length * base_width * height
    
    @staticmethod
    def sphere_cap(radius, height):
        """Calculate volume of a spherical cap given its radius and height."""
        return (1/3) * math.pi * height ** 2 * (3 * radius - height)

