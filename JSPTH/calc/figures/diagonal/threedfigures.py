import math

class diagonalOf3DFigures():
    @staticmethod
    def diagonal_of_cube(side):
        """Calculate diagonal of a cube given its side length."""
        return side * math.sqrt(3)

    @staticmethod
    def diagonal_of_rectangular_prism(length, width, height):
        """Calculate diagonal of a rectangular prism given its length, width, and height."""
        return math.sqrt(length ** 2 + width ** 2 + height ** 2)

    @staticmethod
    def diagonal_of_pyramid(base_length, base_width, height):
        """Calculate diagonal of a pyramid given its base length, base width, and height."""
        return math.sqrt((base_length / 2) ** 2 + (base_width / 2) ** 2 + height ** 2)

    @staticmethod
    def diagonal_of_cone(radius, height):
        """Calculate diagonal of a cone given its radius and height."""
        return math.sqrt(radius ** 2 + height ** 2)

    