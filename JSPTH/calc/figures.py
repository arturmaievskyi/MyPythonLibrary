import math

class angleOfFigures:
    """Class to calculate angles of different geometric figures."""
    
    @staticmethod
    def triangle(side1, side2, side3):
        """Calculate angles of a triangle given its three sides using the Law of Cosines."""
        angle1 = math.acos((side2 ** 2 + side3 ** 2 - side1 ** 2) / (2 * side2 * side3))
        angle2 = math.acos((side1 ** 2 + side3 ** 2 - side2 ** 2) / (2 * side1 * side3))
        angle3 = math.acos((side1 ** 2 + side2 ** 2 - side3 ** 2) / (2 * side1 * side2))
        return math.degrees(angle1), math.degrees(angle2), math.degrees(angle3)
    
    @staticmethod
    def rectangle(length, width):
        """Calculate angles of a rectangle given its length and width (all angles are 90 degrees)."""
        return 90, 90, 90, 90
    
    @staticmethod
    def ngon(sides):
        """Calculate angles of a regular n-gon given the number of sides."""
        n = sides
        angle = (n - 2) * 180 / n
        return [angle] * n

    @staticmethod
    def parallelogram(base, side):
        """Calculate angles of a parallelogram given its base and side lengths."""
        angle = math.acos((base ** 2 + side ** 2 - (base * side)) / (2 * base * side))
        return math.degrees(angle), 180 - math.degrees(angle), math.degrees(angle), 180 - math.degrees(angle)
    
    @staticmethod
    def trapezoid(base1, base2, side1, side2):
        """Calculate angles of a trapezoid given its two bases and two sides."""
        angle1 = math.acos((side1 ** 2 + base1 ** 2 - base2 ** 2) / (2 * side1 * base1))
        angle2 = math.acos((side2 ** 2 + base1 ** 2 - base2 ** 2) / (2 * side2 * base1))
        angle3 = math.acos((side1 ** 2 + base2 ** 2 - base1 ** 2) / (2 * side1 * base2))
        angle4 = math.acos((side2 ** 2 + base2 ** 2 - base1 ** 2) / (2 * side2 * base2))
        return math.degrees(angle1), math.degrees(angle2), math.degrees(angle3), math.degrees(angle4)

    def rhombus(diagonal1, diagonal2):
        """Calculate angles of a rhombus given its two diagonals."""
        angle1 = math.acos((diagonal1 ** 2 + diagonal2 ** 2) / (2 * diagonal1 * diagonal2))
        angle2 = math.acos((diagonal1 ** 2 + diagonal2 ** 2) / (2 * diagonal1 * diagonal2))
        return math.degrees(angle1), math.degrees(angle2), math.degrees(angle1), math.degrees(angle2)

    def kite(diagonal1, diagonal2):
        """Calculate angles of a kite given its two diagonals."""
        angle1 = math.acos((diagonal1 ** 2 + diagonal2 ** 2) / (2 * diagonal1 * diagonal2))
        angle2 = math.acos((diagonal1 ** 2 + diagonal2 ** 2) / (2 * diagonal1 * diagonal2))
        return math.degrees(angle1), math.degrees(angle2), math.degrees(angle1), math.degrees(angle2)

class angel_of_3d_figures:
    """Class to calculate angles of different 3D geometric figures."""
    
    @staticmethod
    def cube():
        """Calculate angles of a cube (all angles are 90 degrees)."""
        return 90, 90, 90, 90, 90, 90
    
    @staticmethod
    def rectangular_prism():
        """Calculate angles of a rectangular prism (all angles are 90 degrees)."""
        return 90, 90, 90, 90, 90, 90
    
    @staticmethod
    def pyramid(base_length, base_width, height):
        """Calculate angles of a pyramid given its base length, base width, and height."""
        slant_height = math.sqrt((base_length / 2) ** 2 + height ** 2)
        angle1 = math.acos(height / slant_height)
        angle2 = math.acos((base_length / 2) / slant_height)
        return math.degrees(angle1), math.degrees(angle2), math.degrees(angle1), math.degrees(angle2)

    @staticmethod
    def cone(radius, height):
        """Calculate angles of a cone given its radius and height."""
        slant_height = math.sqrt(radius ** 2 + height ** 2)
        angle1 = math.acos(height / slant_height)
        angle2 = math.acos(radius / slant_height)
        return math.degrees(angle1), math.degrees(angle2), math.degrees(angle1), math.degrees(angle2)
    
    @staticmethod
    def sphere():
        """Calculate angles of a sphere (all angles are 90 degrees)."""
        return 90, 90, 90, 90, 90, 90
    
    def tetrahedron(side):
        """Calculate angles of a regular tetrahedron given its side length."""
        angle = math.acos(-1/3)
        return math.degrees(angle), math.degrees(angle), math.degrees(angle), math.degrees(angle)
    
    def ngon_prism(sides, height):
        """Calculate angles of a regular n-gon prism given the number of sides and height."""
        n = sides
        angle = (n - 2) * 180 / n
        return [angle] * n + [90] * n

    def ngon_pyramid(sides, height):
        """Calculate angles of a regular n-gon pyramid given the number of sides and height."""
        n = sides
        angle = (n - 2) * 180 / n
        slant_height = math.sqrt((height ** 2) + ((1 / (2 * math.tan(math.radians(angle / 2)))) ** 2))
        angle1 = math.acos(height / slant_height)
        return [angle1] * n + [math.degrees(angle1)] * n

    def sphere_cap(radius, height):
        """Calculate angles of a spherical cap given its radius and height."""
        angle = math.acos((radius - height) / radius)
        return math.degrees(angle), math.degrees(angle)
    
    