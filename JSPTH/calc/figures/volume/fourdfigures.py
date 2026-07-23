import math


class volumeOf4DFigures:
    """Class to calculate volume of different 4D geometric figures."""
    
    @staticmethod
    def hypersphere(radius):
        """Calculate volume of a hypersphere given its radius."""
        return (math.pi ** 2 / 2) * radius ** 4
    
    @staticmethod
    def hypercube(side):
        """Calculate volume of a hypercube given its side length."""
        return side ** 4
    
    @staticmethod
    def hyperrectangular_prism(length, width, height, depth):
        """Calculate volume of a hyperrectangular prism given its length, width, height, and depth."""
        return length * width * height * depth
    
    @staticmethod
    def hyperpyramid(base_length, base_width, base_height, height):
        """Calculate volume of a hyperpyramid given its base length, base width, base height, and height."""
        return (1/4) * base_length * base_width * base_height * height
    
    @staticmethod
    def hypersphere_cap(radius, height):
        """Calculate volume of a hypersphere cap given its radius and height."""
        return (math.pi ** 2 / 2) * height ** 4 * (1 - (height / radius) ** 4)
    
    @staticmethod
    def regular_polygon(sides, length):
        """Calculate area of a regular polygon given the number of sides and length of each side."""
        n = sides
        s = length
        return (n * s ** 2) / (4 * math.tan(math.pi / n))

