import math


class perimeterOf3DFigures:
    """Class to calculate perimeter of different 3D geometric figures."""
    
    @staticmethod
    def cube(side):
        """Calculate perimeter of a cube given its side length."""
        return 12 * side
    
    @staticmethod
    def rectangular_prism(length, width, height):
        """Calculate perimeter of a rectangular prism given its length, width, and height."""
        return 4 * (length + width + height)

    @staticmethod
    def sphere(radius):
        """Calculate perimeter of a sphere given its radius (circumference of great circle)."""
        return 2 * math.pi * radius
    
    @staticmethod
    def cylinder(radius, height):
        """Calculate perimeter of a cylinder given its radius and height (circumference of base)."""
        return 2 * math.pi * radius
    
    @staticmethod
    def cone(radius, slant_height):
        """Calculate perimeter of a cone given its radius and slant height (circumference of base)."""
        return 2 * math.pi * radius
    
    @staticmethod
    def rectangular_prism(length, width, height):
        """Calculate perimeter of a rectangular prism given its length, width, and height."""
        return 4 * (length + width + height)
    
    @staticmethod
    def triangular_prism(side1, side2, side3, height):
        """Calculate perimeter of a triangular prism given its three sides and height."""
        return 2 * (side1 + side2 + side3) + 3 * height

    @staticmethod
    def pyramid(base_length, base_width, height):
        """Calculate perimeter of a pyramid given its base length, base width, and height."""
        slant_height = math.sqrt((base_length / 2) ** 2 + height ** 2)
        return 2 * (base_length + base_width) + 4 * slant_height
    
    @staticmethod
    def ngon_prism(sides, height):
        """Calculate perimeter of a regular n-gon prism given the number of sides and height."""
        perimeter_base = sides * (2 * math.pi * (height / (2 * math.pi)))
        return 2 * perimeter_base + sides * height

    @staticmethod
    def ngon_pyramid(sides, height):
        """Calculate perimeter of a regular n-gon pyramid given the number of sides and height."""
        perimeter_base = sides * (2 * math.pi * (height / (2 * math.pi)))
        slant_height = math.sqrt((height ** 2) + ((1 / (2 * math.tan(math.pi / sides))) ** 2))
        return perimeter_base + sides * slant_height
    
    @staticmethod
    def sphere_cap(radius, height):
        """Calculate perimeter of a spherical cap given its radius and height (circumference of base)."""
        return 2 * math.pi * math.sqrt(radius ** 2 - (radius - height) ** 2)
    
    @staticmethod
    def regular_polygon(sides, length):
        """Calculate perimeter of a regular polygon given the number of sides and length of each side."""
        return sides * length

