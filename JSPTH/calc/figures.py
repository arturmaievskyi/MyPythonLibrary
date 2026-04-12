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

class volumeOfFigures:
    """Class to calculate volume of different geometric figures."""
    
    @staticmethod
    def sphere(radius):
        """Calculate volume of a sphere given its radius."""
        import math
        return (4/3) * math.pi * radius ** 3
    
    @staticmethod
    def cylinder(radius, height):
        """Calculate volume of a cylinder given its radius and height."""
        return math.pi * radius ** 2 * height
    
    @staticmethod
    def cone(radius, height):
        """Calculate volume of a cone given its radius and height."""
        return (1/3) * math.pi * radius ** 2 * height
    
    @staticmethod
    def cube(side):
        """Calculate volume of a cube given its side length."""
        return side ** 3
    
class areaOf3DFigures:
    """Class to calculate surface area of different 3D geometric figures."""
    
    @staticmethod
    def sphere(radius):
        """Calculate surface area of a sphere given its radius."""
        return 4 * math.pi * radius ** 2
    
    @staticmethod
    def cylinder(radius, height):
        """Calculate surface area of a cylinder given its radius and height."""
        return 2 * math.pi * radius * (radius + height)
    
    @staticmethod
    def cone(radius, slant_height):
        """Calculate surface area of a cone given its radius and slant height."""
        return math.pi * radius * (radius + slant_height)
    
    @staticmethod
    def cube(side):
        """Calculate surface area of a cube given its side length."""
        return 6 * side ** 2

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

class volumeOf3DFigures:
    """Class to calculate volume of different 3D geometric figures."""
    
    @staticmethod
    def sphere(radius):
        """Calculate volume of a sphere given its radius."""
        return (4/3) * math.pi * radius ** 3
    
    @staticmethod
    def cylinder(radius, height):
        """Calculate volume of a cylinder given its radius and height."""
        return math.pi * radius ** 2 * height
    
    @staticmethod
    def cone(radius, height):
        """Calculate volume of a cone given its radius and height."""
        return (1/3) * math.pi * radius ** 2 * height
    
    @staticmethod
    def cube(side):
        """Calculate volume of a cube given its side length."""
        return side ** 3
    
    @staticmethod
    def rectangular_prism(length, width, height):
        """Calculate volume of a rectangular prism given its length, width, and height."""
        return length * width * height

    @staticmethod
    def pyramid(base_length, base_width, height):
        """Calculate volume of a pyramid given its base length, base width, and height."""
        return (1/3) * base_length * base_width * height
    
    @staticmethod
    def sphere_cap(radius, height):
        """Calculate volume of a spherical cap given its radius and height."""
        return (1/3) * math.pi * height ** 2 * (3 * radius - height)
