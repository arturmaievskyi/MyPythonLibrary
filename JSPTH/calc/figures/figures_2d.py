
import math


"""
2D Figures Area Calculator
==========================

Comprehensive module for calculating areas of various 2D geometric figures.
Includes basic shapes, regular polygons, and composite shapes.

Author: JSPTH Project
Version: 1.0
"""

import math
from abc import ABC, abstractmethod


class Shape2D(ABC):
    """Abstract base class for 2D shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"


class Circle(Shape2D):
    """
    Circle: A round shape with all points equidistant from center.
    
    Attributes:
        radius (float): Distance from center to edge
    
    Formulas:
        Area = πr²
        Perimeter = 2πr
    """
    
    def __init__(self, radius):
        """
        Initialize a circle.
        
        Args:
            radius (float): Radius of the circle
            
        Raises:
            ValueError: If radius is negative or zero
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        """Calculate area of circle: A = πr²"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate perimeter (circumference): C = 2πr"""
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """Calculate diameter: D = 2r"""
        return 2 * self.radius


class Rectangle(Shape2D):
    """
    Rectangle: Four-sided shape with right angles and parallel opposite sides.
    
    Attributes:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    
    Formulas:
        Area = length × width
        Perimeter = 2(length + width)
    """
    
    def __init__(self, length, width):
        """
        Initialize a rectangle.
        
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
            
        Raises:
            ValueError: If dimensions are negative or zero
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area: A = l × w"""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate perimeter: P = 2(l + w)"""
        return 2 * (self.length + self.width)
    
    def diagonal(self):
        """Calculate diagonal: d = √(l² + w²)"""
        return math.sqrt(self.length ** 2 + self.width ** 2)


class Triangle(Shape2D):
    """
    Triangle: Three-sided polygon.
    
    Supports three methods of initialization:
    1. Base and height
    2. Three sides (Heron's formula)
    3. Two sides and included angle
    """
    
    def __init__(self, *args):
        """
        Initialize triangle with flexible parameters.
        
        Options:
            1. Triangle(base, height)
            2. Triangle(a, b, c)  # three sides
            3. Triangle(a, b, angle_C_rad)  # two sides and angle
        """
        if len(args) == 2:
            # Base and height
            self.base = args[0]
            self.height = args[1]
            if self.base <= 0 or self.height <= 0:
                raise ValueError("Base and height must be positive")
            self.mode = "base_height"
        elif len(args) == 3:
            a, b, c = args[0], args[1], args[2]
            
            # Check if it's three sides (Heron's) or two sides and angle
            if a > 0 and b > 0 and c > 0:
                # Check triangle inequality
                if a + b > c and b + c > a and a + c > b:
                    self.a, self.b, self.c = a, b, c
                    self.mode = "heron"
                else:
                    raise ValueError("Invalid triangle: violates triangle inequality")
            else:
                raise ValueError("All dimensions must be positive")
        else:
            raise ValueError("Triangle requires 2 or 3 arguments")
    
    def area(self):
        """Calculate area based on initialization mode."""
        if self.mode == "base_height":
            return 0.5 * self.base * self.height
        elif self.mode == "heron":
            # Heron's formula: A = √(s(s-a)(s-b)(s-c))
            s = (self.a + self.b + self.c) / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        """Calculate perimeter."""
        if self.mode == "base_height":
            # Need to calculate other sides (not ideal)
            return "Cannot calculate without side lengths"
        elif self.mode == "heron":
            return self.a + self.b + self.c


class Square(Shape2D):
    """
    Square: Rectangle with all sides equal.
    
    Attributes:
        side (float): Length of each side
    
    Formulas:
        Area = side²
        Perimeter = 4 × side
    """
    
    def __init__(self, side):
        """
        Initialize a square.
        
        Args:
            side (float): Length of each side
            
        Raises:
            ValueError: If side is negative or zero
        """
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side
    
    def area(self):
        """Calculate area: A = s²"""
        return self.side ** 2
    
    def perimeter(self):
        """Calculate perimeter: P = 4s"""
        return 4 * self.side
    
    def diagonal(self):
        """Calculate diagonal: d = s√2"""
        return self.side * math.sqrt(2)


class Trapezoid(Shape2D):
    """
    Trapezoid: Quadrilateral with one pair of parallel sides.
    
    Attributes:
        base1 (float): Length of first parallel base
        base2 (float): Length of second parallel base
        height (float): Perpendicular distance between bases
    
    Formulas:
        Area = ½(base1 + base2) × height
        Perimeter = base1 + base2 + side1 + side2
    """
    
    def __init__(self, base1, base2, height, side1=None, side2=None):
        """
        Initialize a trapezoid.
        
        Args:
            base1 (float): First base length
            base2 (float): Second base length
            height (float): Height between bases
            side1 (float, optional): Left side length
            side2 (float, optional): Right side length
        """
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Base lengths and height must be positive")
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        """Calculate area: A = ½(b1 + b2) × h"""
        return 0.5 * (self.base1 + self.base2) * self.height
    
    def perimeter(self):
        """Calculate perimeter: P = b1 + b2 + s1 + s2"""
        if self.side1 is None or self.side2 is None:
            return "Sides required for perimeter calculation"
        return self.base1 + self.base2 + self.side1 + self.side2
    
    def median(self):
        """Calculate median (midsegment): m = (b1 + b2) / 2"""
        return (self.base1 + self.base2) / 2


class Parallelogram(Shape2D):
    """
    Parallelogram: Quadrilateral with opposite sides parallel and equal.
    
    Attributes:
        base (float): Length of the base
        height (float): Perpendicular distance from base
    
    Formulas:
        Area = base × height
        Perimeter = 2(base + side)
    """
    
    def __init__(self, base, height, side=None):
        """
        Initialize a parallelogram.
        
        Args:
            base (float): Base length
            height (float): Height (perpendicular to base)
            side (float, optional): Length of adjacent side
        """
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive")
        self.base = base
        self.height = height
        self.side = side
    
    def area(self):
        """Calculate area: A = base × height"""
        return self.base * self.height
    
    def perimeter(self):
        """Calculate perimeter: P = 2(base + side)"""
        if self.side is None:
            return "Side length required for perimeter"
        return 2 * (self.base + self.side)


class Rhombus(Shape2D):
    """
    Rhombus: Parallelogram with all sides equal.
    
    Two methods:
    1. Using diagonals: A = ½(d1 × d2)
    2. Using side and height: A = side × height
    """
    
    def __init__(self, *args):
        """
        Initialize rhombus.
        
        Options:
            1. Rhombus(diagonal1, diagonal2)
            2. Rhombus(side, height)
        """
        if len(args) == 2:
            d1, d2 = args[0], args[1]
            if d1 <= 0 or d2 <= 0:
                raise ValueError("Diagonals must be positive")
            self.d1 = d1
            self.d2 = d2
            self.mode = "diagonal"
        else:
            raise ValueError("Rhombus requires 2 arguments (diagonals or side, height)")
    
    def area(self):
        """Calculate area using diagonals: A = ½(d1 × d2)"""
        if self.mode == "diagonal":
            return 0.5 * self.d1 * self.d2
    
    def perimeter(self):
        """Calculate perimeter from diagonals: P = 4√((d1/2)² + (d2/2)²)"""
        if self.mode == "diagonal":
            side = math.sqrt((self.d1/2) ** 2 + (self.d2/2) ** 2)
            return 4 * side
    
    def side_length(self):
        """Calculate side length from diagonals."""
        if self.mode == "diagonal":
            return math.sqrt((self.d1/2) ** 2 + (self.d2/2) ** 2)


class Kite(Shape2D):
    """
    Kite: Quadrilateral with two pairs of adjacent equal sides.
    
    Attributes:
        d1 (float): Length of one diagonal
        d2 (float): Length of other diagonal
    
    Formulas:
        Area = ½(d1 × d2)
    """
    
    def __init__(self, diagonal1, diagonal2):
        """
        Initialize a kite.
        
        Args:
            diagonal1 (float): Length of first diagonal
            diagonal2 (float): Length of second diagonal
        """
        if diagonal1 <= 0 or diagonal2 <= 0:
            raise ValueError("Diagonals must be positive")
        self.d1 = diagonal1
        self.d2 = diagonal2
    
    def area(self):
        """Calculate area: A = ½(d1 × d2)"""
        return 0.5 * self.d1 * self.d2
    
    def perimeter(self):
        """Perimeter requires side lengths (not derivable from diagonals alone)"""
        return "Side lengths required for perimeter"


class Ellipse(Shape2D):
    """
    Ellipse: Oval shape defined by two semi-axes.
    
    Attributes:
        semi_major (float): Length of major axis / 2
        semi_minor (float): Length of minor axis / 2
    
    Formulas:
        Area = π × a × b
        Perimeter ≈ π(a + b) [Ramanujan approximation]
    """
    
    def __init__(self, semi_major, semi_minor):
        """
        Initialize an ellipse.
        
        Args:
            semi_major (float): Semi-major axis (larger)
            semi_minor (float): Semi-minor axis (smaller)
        """
        if semi_major <= 0 or semi_minor <= 0:
            raise ValueError("Semi-axes must be positive")
        self.a = semi_major
        self.b = semi_minor
    
    def area(self):
        """Calculate area: A = π × a × b"""
        return math.pi * self.a * self.b
    
    def perimeter(self):
        """Calculate perimeter using Ramanujan approximation."""
        h = ((self.a - self.b) ** 2) / ((self.a + self.b) ** 2)
        return math.pi * (self.a + self.b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
    
    def eccentricity(self):
        """Calculate eccentricity: e = √(1 - (b/a)²)"""
        return math.sqrt(1 - (self.b / self.a) ** 2)


class RegularPolygon(Shape2D):
    """
    Regular Polygon: Polygon with all sides and angles equal.
    
    Attributes:
        sides (int): Number of sides
        side_length (float): Length of each side
    
    Formulas:
        Area = (n × s² × cot(π/n)) / 4
        Perimeter = n × s
    """
    
    def __init__(self, sides, side_length):
        """
        Initialize a regular polygon.
        
        Args:
            sides (int): Number of sides (must be ≥ 3)
            side_length (float): Length of each side
        """
        if sides < 3:
            raise ValueError("Polygon must have at least 3 sides")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.sides = sides
        self.side_length = side_length
    
    def area(self):
        """Calculate area: A = (n × s² × cot(π/n)) / 4"""
        n = self.sides
        s = self.side_length
        return (n * s ** 2) / (4 * math.tan(math.pi / n))
    
    def perimeter(self):
        """Calculate perimeter: P = n × s"""
        return self.sides * self.side_length
    
    def apothem(self):
        """Calculate apothem (distance from center to side)."""
        return self.side_length / (2 * math.tan(math.pi / self.sides))
    
    def circumradius(self):
        """Calculate circumradius (distance from center to vertex)."""
        return self.side_length / (2 * math.sin(math.pi / self.sides))
    
    def interior_angle(self):
        """Calculate interior angle in degrees."""
        return ((self.sides - 2) * 180) / self.sides


class CircularSector(Shape2D):
    """
    Circular Sector: Pie-slice shape cut from a circle.
    
    Attributes:
        radius (float): Radius of the circle
        angle (float): Central angle in radians
    
    Formulas:
        Area = (θ × r²) / 2
        Arc length = θ × r
        Perimeter = 2r + arc_length
    """
    
    def __init__(self, radius, angle_rad):
        """
        Initialize a circular sector.
        
        Args:
            radius (float): Radius of the circle
            angle_rad (float): Central angle in radians (0 to 2π)
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        if not (0 <= angle_rad <= 2 * math.pi):
            raise ValueError("Angle must be between 0 and 2π radians")
        self.radius = radius
        self.angle = angle_rad
    
    def area(self):
        """Calculate area: A = (θ × r²) / 2"""
        return (self.angle * self.radius ** 2) / 2
    
    def arc_length(self):
        """Calculate arc length: L = θ × r"""
        return self.angle * self.radius
    
    def perimeter(self):
        """Calculate perimeter: P = 2r + arc_length"""
        return 2 * self.radius + self.arc_length()
    
    def chord_length(self):
        """Calculate chord length: c = 2r × sin(θ/2)"""
        return 2 * self.radius * math.sin(self.angle / 2)


class CircularSegment(Shape2D):
    """
    Circular Segment: Region between chord and arc.
    
    Attributes:
        radius (float): Radius of the circle
        angle (float): Central angle in radians
    """
    
    def __init__(self, radius, angle_rad):
        """
        Initialize a circular segment.
        
        Args:
            radius (float): Radius of the circle
            angle_rad (float): Central angle in radians
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        self.angle = angle_rad
    
    def area(self):
        """Calculate area: A = (r²/2)(θ - sin(θ))"""
        return (self.radius ** 2 / 2) * (self.angle - math.sin(self.angle))
    
    def perimeter(self):
        """Calculate perimeter: P = arc_length + chord_length"""
        arc = self.angle * self.radius
        chord = 2 * self.radius * math.sin(self.angle / 2)
        return arc + chord


class Polygon(Shape2D):
    """
    Polygon: General polygon using coordinates.
    
    Uses the Shoelace formula (Gauss's area formula).
    """
    
    def __init__(self, vertices):
        """
        Initialize a polygon.
        
        Args:
            vertices (list): List of (x, y) tuples in order
        """
        if len(vertices) < 3:
            raise ValueError("Polygon must have at least 3 vertices")
        self.vertices = vertices
    
    def area(self):
        """Calculate area using Shoelace formula."""
        n = len(self.vertices)
        area = 0.0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2.0
    
    def perimeter(self):
        """Calculate perimeter by summing edge lengths."""
        n = len(self.vertices)
        perimeter = 0.0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return perimeter


class BearArea():
    """
    This is a class with bear bones functions for calculating areas of various 2D figures.
    It is not meant to be instantiated, but rather to provide quick access to area calculations.
    """

    def circle_area(radius):
        """Calculate circle area quickly."""
        return math.pi * radius ** 2


    def rectangle_area(length, width):
        """Calculate rectangle area quickly."""
        return length * width


    def triangle_area_base_height(base, height):
        """Calculate triangle area from base and height."""
        return 0.5 * base * height


    def triangle_area_heron(a, b, c):
        """Calculate triangle area using Heron's formula."""
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


    def square_area(side):
        """Calculate square area quickly."""
        return side ** 2


    def trapezoid_area(base1, base2, height):
        """Calculate trapezoid area quickly."""
        return 0.5 * (base1 + base2) * height


    def parallelogram_area(base, height):
        """Calculate parallelogram area quickly."""
        return base * height


    def ellipse_area(semi_major, semi_minor):
        """Calculate ellipse area quickly."""
        return math.pi * semi_major * semi_minor


    def rhombus_area(diagonal1, diagonal2):
        """Calculate rhombus area from diagonals."""
        return 0.5 * diagonal1 * diagonal2


    def kite_area(diagonal1, diagonal2):
        """Calculate kite area from diagonals."""
        return 0.5 * diagonal1 * diagonal2


    def regular_polygon_area(sides, side_length):
        """Calculate regular polygon area."""
        return (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))


    def sector_area(radius, angle_rad):
        """Calculate circular sector area."""
        return (angle_rad * radius ** 2) / 2


    def segment_area(radius, angle_rad):
        """Calculate circular segment area."""
        return (radius ** 2 / 2) * (angle_rad - math.sin(angle_rad))


