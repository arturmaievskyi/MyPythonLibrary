import math

class diagonalOf4DFigures:
    """Class to calculate diagonal of different 4D geometric figures."""
    
    @staticmethod
    def hypercube(side):
        """Calculate diagonal of a hypercube given its side length."""
        return side * math.sqrt(4)
    
    @staticmethod
    def hyperrectangular_prism(length, width, height, depth):
        """Calculate diagonal of a hyperrectangular prism given its length, width, height, and depth."""
        return math.sqrt(length ** 2 + width ** 2 + height ** 2 + depth ** 2)
    
    @staticmethod
    def hyperpyramid(base_length, base_width, base_height, height):
        """Calculate diagonal of a hyperpyramid given its base length, base width, base height, and height."""
        return math.sqrt(base_length ** 2 + base_width ** 2 + base_height ** 2 + height ** 2)

    @staticmethod
    def hypersphere(radius):
        """Calculate diagonal of a hypersphere given its radius (diameter)."""
        return 2 * radius
    
    @staticmethod
    def hypersphere_cap(radius, height):
        """Calculate diagonal of a hypersphere cap given its radius and height (diameter of the cap)."""
        return 2 * math.sqrt(radius ** 2 - (radius - height) ** 2)