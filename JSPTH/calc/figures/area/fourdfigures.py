import math

class areaOf4DFigures:
    """Class to calculate area of different 4D geometric figures."""
    
    @staticmethod
    def hypercube(side):
        """Calculate area of a hypercube given its side length."""
        return 8 * (side ** 3)
    
    @staticmethod
    def hyperrectangular_prism(length, width, height, depth):
        """Calculate area of a hyperrectangular prism given its length, width, height, and depth."""
        return 2 * (length * width * height + length * width * depth + length * height * depth + width * height * depth)
    
    @staticmethod
    def hyperpyramid(base_length, base_width, base_height, height):
        """Calculate area of a hyperpyramid given its base length, base width, base height, and height."""
        base_area = base_length * base_width * base_height
        lateral_area = (base_length + base_width + base_height) * height
        return base_area + lateral_area

    @staticmethod
    def hypersphere(radius):
        """Calculate area of a hypersphere given its radius."""
        return 2 * math.pi ** 2 * radius ** 3
    
    @staticmethod
    def hypersphere_cap(radius, height):
        """Calculate area of a hypersphere cap given its radius and height."""
        return 2 * math.pi * radius ** 2 * (1 - (radius - height) / radius)