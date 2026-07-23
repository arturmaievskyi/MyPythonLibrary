import math

    
class perimeterOfFigures:
    """Class to calculate perimeter of different geometric figures."""
    
    @staticmethod
    def circle(radius):
        """Calculate perimeter of a circle given its radius."""
        return 2 * math.pi * radius
    
    @staticmethod
    def rectangle(length, width):
        """Calculate perimeter of a rectangle given its length and width."""
        return 2 * (length + width)
    
    @staticmethod
    def triangle(side1, side2, side3):
        """Calculate perimeter of a triangle given its three sides."""
        return side1 + side2 + side3
    
    @staticmethod
    def square(side):
        """Calculate perimeter of a square given its side length."""
        return 4 * side
    
    @staticmethod
    def regular_polygon(sides, length):
        """Calculate perimeter of a regular polygon given the number of sides and length of each side."""
        return sides * length

    @staticmethod
    def parallelogram(base, side):
        """Calculate perimeter of a parallelogram given its base and side lengths."""
        return 2 * (base + side)

    @staticmethod
    def trapezoid(base1, base2, side1, side2):
        """Calculate perimeter of a trapezoid given its two bases and two sides."""
        return base1 + base2 + side1 + side2

    @staticmethod
    def rhombus(side):
        """Calculate perimeter of a rhombus given its side length."""
        return 4 * side

    @staticmethod
    def regular_polygon(sides, length):
        """Calculate perimeter of a regular polygon given the number of sides and length of each side."""
        return sides * length

