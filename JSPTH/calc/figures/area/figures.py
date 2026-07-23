
import math


class areaOfFigures:
    """Class to calculate area of different geometric figures."""
    
    @staticmethod
    def circle(radius):
        """Calculate area of a circle given its radius."""
        return math.pi * radius ** 2
    
    @staticmethod
    def rectangle(length, width):
        """Calculate area of a rectangle given its length and width."""
        return length * width
    
    @staticmethod
    def triangle(base, height):
        """Calculate area of a triangle given its base and height."""
        return 0.5 * base * height
    
    @staticmethod
    def square(side):
        """Calculate area of a square given its side length."""
        return side ** 2

    @staticmethod
    def regular_polygon(sides, length):
        """Calculate area of a regular polygon given the number of sides and length of each side."""
        n = sides
        s = length
        return (n * s ** 2) / (4 * math.tan(math.pi / n))

