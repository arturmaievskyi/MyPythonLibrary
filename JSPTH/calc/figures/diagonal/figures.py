
import math


class diagonalOfFigures:
    """Class to calculate diagonal of different geometric figures."""
    
    @staticmethod
    def rectangle(length, width):
        """Calculate diagonal of a rectangle given its length and width."""
        return math.sqrt(length ** 2 + width ** 2)
    
    @staticmethod
    def square(side):
        """Calculate diagonal of a square given its side length."""
        return side * math.sqrt(2)
    
    @staticmethod
    def cube(side):
        """Calculate diagonal of a cube given its side length."""
        return side * math.sqrt(3)
    
    @staticmethod
    def rectangular_prism(length, width, height):
        """Calculate diagonal of a rectangular prism given its length, width, and height."""
        return math.sqrt(length ** 2 + width ** 2 + height ** 2)
    
    @staticmethod
    def triangle(side1, side2, side3):
        """Calculate diagonal of a triangle given its three sides using Heron's formula."""
        import math
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return (side1 * side2 * side3) / (4 * area)

    