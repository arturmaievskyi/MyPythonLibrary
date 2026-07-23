import math

class perimeterOf4DFigures:
    @staticmethod
    def perimeter_of_hypercube(side):
        """Calculate perimeter of a hypercube given its side length."""
        return 32 * side
    
    @staticmethod
    def perimeter_of_hyperrectangular_prism(length, width, height, depth):
        """Calculate perimeter of a hyperrectangular prism given its length, width, height, and depth."""
        return 8 * (length + width + height + depth)
    
    @staticmethod
    def perimeter_of_hyperpyramid(base_length, base_width, base_height, height):
        """Calculate perimeter of a hyperpyramid given its base length, base width, base height, and height."""
        return 4 * (base_length + base_width + base_height) + 4 * height

    def perimeter_of_hypersphere(radius):
        """Calculate perimeter of a hypersphere given its radius (circumference of great circle)."""
        return 2 * math.pi * radius
    
    def perimeter_of_hypersphere_cap(radius, height):
        """Calculate perimeter of a hypersphere cap given its radius and height (circumference of base)."""
        return 2 * math.pi * math.sqrt(radius ** 2 - (radius - height) ** 2)
