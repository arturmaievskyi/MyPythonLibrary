import math
from abc import ABC, abstractmethod


class Shape3D(ABC):
    """Abstract base class for 3D shapes."""
    
    @abstractmethod
    def volume(self):
        """Calculate the volume of the shape."""
        pass
    
    @abstractmethod
    def surface_area(self):
        """Calculate the surface area of the shape."""
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: Volume={self.volume():.2f}, Surface Area={self.surface_area():.2f}"


# ============================================================================
# PRISMS & BASIC SHAPES
# ============================================================================

class Cube(Shape3D):
    """
    Cube: Regular hexahedron with 6 square faces.
    
    Attributes:
        side (float): Length of each edge
    
    Formulas:
        Volume = s³
        Surface Area = 6s²
        Space Diagonal = s√3
        Face Diagonal = s√2
    """
    
    def __init__(self, side):
        """Initialize a cube."""
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side
    
    def volume(self):
        """Calculate volume: V = s³"""
        return self.side ** 3
    
    def surface_area(self):
        """Calculate surface area: A = 6s²"""
        return 6 * self.side ** 2
    
    def space_diagonal(self):
        """Calculate space diagonal: d = s√3"""
        return self.side * math.sqrt(3)
    
    def face_diagonal(self):
        """Calculate face diagonal: d = s√2"""
        return self.side * math.sqrt(2)
    
    def edge_length(self):
        """Get edge length."""
        return self.side


class RectangularPrism(Shape3D):
    """
    Rectangular Prism (Cuboid): Box shape with rectangular faces.
    
    Attributes:
        length (float): Length
        width (float): Width
        height (float): Height
    
    Formulas:
        Volume = l × w × h
        Surface Area = 2(lw + lh + wh)
        Space Diagonal = √(l² + w² + h²)
    """
    
    def __init__(self, length, width, height):
        """Initialize a rectangular prism."""
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.length = length
        self.width = width
        self.height = height
    
    def volume(self):
        """Calculate volume: V = l × w × h"""
        return self.length * self.width * self.height
    
    def surface_area(self):
        """Calculate surface area: A = 2(lw + lh + wh)"""
        lw = self.length * self.width
        lh = self.length * self.height
        wh = self.width * self.height
        return 2 * (lw + lh + wh)
    
    def space_diagonal(self):
        """Calculate space diagonal: d = √(l² + w² + h²)"""
        return math.sqrt(self.length**2 + self.width**2 + self.height**2)
    
    def face_diagonals(self):
        """Calculate all three face diagonals."""
        d1 = math.sqrt(self.length**2 + self.width**2)
        d2 = math.sqrt(self.length**2 + self.height**2)
        d3 = math.sqrt(self.width**2 + self.height**2)
        return {"length_width": d1, "length_height": d2, "width_height": d3}


class TriangularPrism(Shape3D):
    """
    Triangular Prism: Prism with triangular base.
    
    Attributes:
        base (float): Base of triangular face
        height_triangle (float): Height of triangular face
        prism_height (float): Height of prism
    
    Formulas:
        Volume = (1/2 × base × height_triangle) × prism_height
        Surface Area = 2 × (triangle area) + (perimeter × prism_height)
    """
    
    def __init__(self, base, height_triangle, prism_height):
        """Initialize a triangular prism."""
        if base <= 0 or height_triangle <= 0 or prism_height <= 0:
            raise ValueError("All dimensions must be positive")
        self.base = base
        self.height_triangle = height_triangle
        self.prism_height = prism_height
    
    def volume(self):
        """Calculate volume: V = (1/2 × b × h_tri) × h_prism"""
        triangle_area = 0.5 * self.base * self.height_triangle
        return triangle_area * self.prism_height
    
    def surface_area(self):
        """Calculate surface area: A = 2×A_tri + perimeter×h"""
        triangle_area = 0.5 * self.base * self.height_triangle
        # Assumes isosceles triangle for simplicity
        # For general case, need three side lengths
        return 2 * triangle_area + (self.base * 3 * self.prism_height)


class HexagonalPrism(Shape3D):
    """
    Hexagonal Prism: Prism with regular hexagonal base.
    
    Attributes:
        side (float): Side length of hexagonal base
        height (float): Height of prism
    
    Formulas:
        Volume = (3√3/2 × s²) × h
        Surface Area = 2×(hexagon area) + 6×(rectangle area)
    """
    
    def __init__(self, side, height):
        """Initialize a hexagonal prism."""
        if side <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.side = side
        self.height = height
    
    def volume(self):
        """Calculate volume: V = (3√3/2 × s²) × h"""
        hexagon_area = (3 * math.sqrt(3) / 2) * self.side ** 2
        return hexagon_area * self.height
    
    def surface_area(self):
        """Calculate surface area: A = 2×A_hex + 6×(s×h)"""
        hexagon_area = (3 * math.sqrt(3) / 2) * self.side ** 2
        rectangular_area = 6 * self.side * self.height
        return 2 * hexagon_area + rectangular_area


# ============================================================================
# PYRAMIDS
# ============================================================================

class SquarePyramid(Shape3D):
    """
    Square Pyramid: Pyramid with square base.
    
    Attributes:
        base_side (float): Side length of square base
        height (float): Height from base to apex
        slant_height (float, optional): Height of triangular faces
    
    Formulas:
        Volume = (1/3 × s² × h)
        Slant Height = √(h² + (s/2)²)
        Surface Area = s² + 2s√(h² + (s/2)²)
    """
    
    def __init__(self, base_side, height, slant_height=None):
        """Initialize a square pyramid."""
        if base_side <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.base_side = base_side
        self.height = height
        if slant_height is None:
            self.slant_height = math.sqrt(height**2 + (base_side/2)**2)
        else:
            self.slant_height = slant_height
    
    def volume(self):
        """Calculate volume: V = (1/3 × s² × h)"""
        return (1/3) * self.base_side ** 2 * self.height
    
    def surface_area(self):
        """Calculate surface area: A = s² + 2s × l"""
        base_area = self.base_side ** 2
        triangular_area = 2 * self.base_side * self.slant_height
        return base_area + triangular_area
    
    def lateral_area(self):
        """Calculate lateral (side) surface area."""
        return 2 * self.base_side * self.slant_height
    
    def space_diagonal(self):
        """Calculate space diagonal of base."""
        return self.base_side * math.sqrt(2)


class TriangularPyramid(Shape3D):
    """
    Triangular Pyramid (Tetrahedron): Pyramid with triangular base.
    
    Attributes:
        base (float): Base of triangular face
        height_triangle (float): Height of triangular base
        pyramid_height (float): Height from base to apex
    """
    
    def __init__(self, base, height_triangle, pyramid_height):
        """Initialize a triangular pyramid."""
        if base <= 0 or height_triangle <= 0 or pyramid_height <= 0:
            raise ValueError("All dimensions must be positive")
        self.base = base
        self.height_triangle = height_triangle
        self.pyramid_height = pyramid_height
    
    def volume(self):
        """Calculate volume: V = (1/3 × base_area × height)"""
        base_area = 0.5 * self.base * self.height_triangle
        return (1/3) * base_area * self.pyramid_height
    
    def surface_area(self):
        """Calculate surface area (approximate)."""
        # This is simplified - actual calculation needs all face areas
        base_area = 0.5 * self.base * self.height_triangle
        return base_area * 4  # Approximate for regular tetrahedron


class RegularTetrahedron(Shape3D):
    """
    Regular Tetrahedron: All edges equal length.
    
    Attributes:
        edge (float): Length of each edge
    
    Formulas:
        Volume = (a³) / (6√2)
        Surface Area = √3 × a²
        Height = √(2/3) × a
    """
    
    def __init__(self, edge):
        """Initialize a regular tetrahedron."""
        if edge <= 0:
            raise ValueError("Edge length must be positive")
        self.edge = edge
    
    def volume(self):
        """Calculate volume: V = a³/(6√2)"""
        return (self.edge ** 3) / (6 * math.sqrt(2))
    
    def surface_area(self):
        """Calculate surface area: A = √3 × a²"""
        return math.sqrt(3) * self.edge ** 2
    
    def height(self):
        """Calculate height: h = √(2/3) × a"""
        return math.sqrt(2/3) * self.edge


# ============================================================================
# CYLINDERS & CONES
# ============================================================================

class Cylinder(Shape3D):
    """
    Cylinder: Circular prism.
    
    Attributes:
        radius (float): Radius of circular base
        height (float): Height of cylinder
    
    Formulas:
        Volume = πr²h
        Surface Area = 2πr² + 2πrh = 2πr(r + h)
        Lateral Area = 2πrh
    """
    
    def __init__(self, radius, height):
        """Initialize a cylinder."""
        if radius <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.radius = radius
        self.height = height
    
    def volume(self):
        """Calculate volume: V = πr²h"""
        return math.pi * self.radius ** 2 * self.height
    
    def surface_area(self):
        """Calculate surface area: A = 2πr² + 2πrh"""
        base_area = 2 * math.pi * self.radius ** 2
        lateral_area = 2 * math.pi * self.radius * self.height
        return base_area + lateral_area
    
    def lateral_area(self):
        """Calculate lateral area: A = 2πrh"""
        return 2 * math.pi * self.radius * self.height
    
    def space_diagonal(self):
        """Calculate space diagonal: d = √(4r² + h²)"""
        return math.sqrt(4 * self.radius ** 2 + self.height ** 2)


class Cone(Shape3D):
    """
    Cone: Circular pyramid.
    
    Attributes:
        radius (float): Radius of circular base
        height (float): Height from base to apex
        slant_height (float, optional): Height along the side
    
    Formulas:
        Volume = (1/3)πr²h
        Slant Height = √(r² + h²)
        Surface Area = πr² + πrl
        Lateral Area = πrl
    """
    
    def __init__(self, radius, height, slant_height=None):
        """Initialize a cone."""
        if radius <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.radius = radius
        self.height = height
        if slant_height is None:
            self.slant_height = math.sqrt(radius**2 + height**2)
        else:
            self.slant_height = slant_height
    
    def volume(self):
        """Calculate volume: V = (1/3)πr²h"""
        return (1/3) * math.pi * self.radius ** 2 * self.height
    
    def surface_area(self):
        """Calculate surface area: A = πr² + πrl"""
        base_area = math.pi * self.radius ** 2
        lateral_area = math.pi * self.radius * self.slant_height
        return base_area + lateral_area
    
    def lateral_area(self):
        """Calculate lateral area: A = πrl"""
        return math.pi * self.radius * self.slant_height


class Frustum(Shape3D):
    """
    Frustum (Truncated Cone): Cone with top cut off.
    
    Attributes:
        radius1 (float): Radius of larger base
        radius2 (float): Radius of smaller base
        height (float): Height between bases
        slant_height (float, optional): Height along the side
    
    Formulas:
        Volume = (1/3)πh(r₁² + r₁r₂ + r₂²)
        Slant Height = √(h² + (r₁ - r₂)²)
        Surface Area = π(r₁² + r₂²) + π(r₁ + r₂)l
    """
    
    def __init__(self, radius1, radius2, height, slant_height=None):
        """Initialize a frustum."""
        if radius1 <= 0 or radius2 <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.radius1 = radius1
        self.radius2 = radius2
        self.height = height
        if slant_height is None:
            self.slant_height = math.sqrt(height**2 + (radius1 - radius2)**2)
        else:
            self.slant_height = slant_height
    
    def volume(self):
        """Calculate volume: V = (1/3)πh(r₁² + r₁r₂ + r₂²)"""
        r1, r2, h = self.radius1, self.radius2, self.height
        return (1/3) * math.pi * h * (r1**2 + r1*r2 + r2**2)
    
    def surface_area(self):
        """Calculate surface area: A = π(r₁² + r₂²) + π(r₁ + r₂)l"""
        base_area = math.pi * (self.radius1**2 + self.radius2**2)
        lateral_area = math.pi * (self.radius1 + self.radius2) * self.slant_height
        return base_area + lateral_area


# ============================================================================
# SPHERES
# ============================================================================

class Sphere(Shape3D):
    """
    Sphere: Perfect round 3D shape.
    
    Attributes:
        radius (float): Radius from center to surface
    
    Formulas:
        Volume = (4/3)πr³
        Surface Area = 4πr²
        Diameter = 2r
    """
    
    def __init__(self, radius):
        """Initialize a sphere."""
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def volume(self):
        """Calculate volume: V = (4/3)πr³"""
        return (4/3) * math.pi * self.radius ** 3
    
    def surface_area(self):
        """Calculate surface area: A = 4πr²"""
        return 4 * math.pi * self.radius ** 2
    
    def diameter(self):
        """Calculate diameter: d = 2r"""
        return 2 * self.radius
    
    def circumference(self):
        """Calculate circumference: C = 2πr"""
        return 2 * math.pi * self.radius


class SphericalCap(Shape3D):
    """
    Spherical Cap: Portion of sphere cut by a plane.
    
    Attributes:
        radius (float): Radius of sphere
        height (float): Height of the cap
    
    Formulas:
        Volume = (πh²/3)(3r - h)
        Curved Surface Area = 2πrh
        Base Area = π(2rh - h²)
    """
    
    def __init__(self, radius, height):
        """Initialize a spherical cap."""
        if radius <= 0 or height <= 0 or height > 2*radius:
            raise ValueError("Invalid dimensions for spherical cap")
        self.radius = radius
        self.height = height
    
    def volume(self):
        """Calculate volume: V = (πh²/3)(3r - h)"""
        return (math.pi * self.height**2 / 3) * (3*self.radius - self.height)
    
    def curved_surface_area(self):
        """Calculate curved surface area: A = 2πrh"""
        return 2 * math.pi * self.radius * self.height
    
    def base_area(self):
        """Calculate base area: A = π(2rh - h²)"""
        return math.pi * (2*self.radius*self.height - self.height**2)
    
    def surface_area(self):
        """Total surface area including base."""
        return self.curved_surface_area() + self.base_area()


class Ellipsoid(Shape3D):
    """
    Ellipsoid: 3D ellipse (stretched sphere).
    
    Attributes:
        a (float): Semi-axis a
        b (float): Semi-axis b
        c (float): Semi-axis c
    
    Formulas:
        Volume = (4/3)πabc
        Surface Area ≈ complex formula (Knud Thomsen's approximation)
    """
    
    def __init__(self, a, b, c):
        """Initialize an ellipsoid."""
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All semi-axes must be positive")
        self.a = a
        self.b = b
        self.c = c
    
    def volume(self):
        """Calculate volume: V = (4/3)πabc"""
        return (4/3) * math.pi * self.a * self.b * self.c
    
    def surface_area(self):
        """Calculate surface area (Knud Thomsen approximation)."""
        a, b, c = self.a, self.b, self.c
        p = 1.6075  # Knud Thomsen's power
        term = ((a**p * b**p + a**p * c**p + b**p * c**p) / 3) ** (1/p)
        return 4 * math.pi * term


class Torus(Shape3D):
    """
    Torus: Donut shape.
    
    Attributes:
        major_radius (float): Radius from center to center of tube
        minor_radius (float): Radius of the tube
    
    Formulas:
        Volume = (π²)(R + r)(R - r)² = (π² × Rr²) × 4
        Wait, correct: V = (π × R) × (π × r²) × 2 = 2π²Rr²
        Surface Area = (2π × R)(2π × r) = 4π²Rr
    """
    
    def __init__(self, major_radius, minor_radius):
        """Initialize a torus."""
        if major_radius <= 0 or minor_radius <= 0:
            raise ValueError("All radii must be positive")
        if major_radius < minor_radius:
            raise ValueError("Major radius must be >= minor radius")
        self.major_radius = major_radius
        self.minor_radius = minor_radius
    
    def volume(self):
        """Calculate volume: V = 2π²Rr²"""
        R = self.major_radius
        r = self.minor_radius
        return 2 * math.pi ** 2 * R * r ** 2
    
    def surface_area(self):
        """Calculate surface area: A = 4π²Rr"""
        R = self.major_radius
        r = self.minor_radius
        return 4 * math.pi ** 2 * R * r


# ============================================================================
# PLATONIC SOLIDS
# ============================================================================

class RegularOctahedron(Shape3D):
    """
    Regular Octahedron: 8 equilateral triangle faces.
    
    Attributes:
        edge (float): Length of each edge
    
    Formulas:
        Volume = (√2/3) × a³
        Surface Area = 2√3 × a²
    """
    
    def __init__(self, edge):
        """Initialize a regular octahedron."""
        if edge <= 0:
            raise ValueError("Edge length must be positive")
        self.edge = edge
    
    def volume(self):
        """Calculate volume: V = (√2/3)a³"""
        return (math.sqrt(2) / 3) * self.edge ** 3
    
    def surface_area(self):
        """Calculate surface area: A = 2√3 × a²"""
        return 2 * math.sqrt(3) * self.edge ** 2


class RegularDodecahedron(Shape3D):
    """
    Regular Dodecahedron: 12 pentagonal faces.
    
    Attributes:
        edge (float): Length of each edge
    
    Formulas:
        Volume = (15 + 7√5)/4 × a³
        Surface Area = 3√25 + 10√5 × a²
    """
    
    def __init__(self, edge):
        """Initialize a regular dodecahedron."""
        if edge <= 0:
            raise ValueError("Edge length must be positive")
        self.edge = edge
    
    def volume(self):
        """Calculate volume."""
        sqrt5 = math.sqrt(5)
        return ((15 + 7*sqrt5) / 4) * self.edge ** 3
    
    def surface_area(self):
        """Calculate surface area."""
        sqrt5 = math.sqrt(5)
        return 3 * math.sqrt(25 + 10*sqrt5) * self.edge ** 2


class RegularIcosahedron(Shape3D):
    """
    Regular Icosahedron: 20 equilateral triangle faces.
    
    Attributes:
        edge (float): Length of each edge
    
    Formulas:
        Volume = (5(3 + √5)/12) × a³
        Surface Area = 5√3 × a²
    """
    
    def __init__(self, edge):
        """Initialize a regular icosahedron."""
        if edge <= 0:
            raise ValueError("Edge length must be positive")
        self.edge = edge
    
    def volume(self):
        """Calculate volume: V = (5(3 + √5)/12)a³"""
        sqrt5 = math.sqrt(5)
        return (5 * (3 + sqrt5) / 12) * self.edge ** 3
    
    def surface_area(self):
        """Calculate surface area: A = 5√3 × a²"""
        return 5 * math.sqrt(3) * self.edge ** 2


# ============================================================================
# QUICK CALCULATION FUNCTIONS
# ============================================================================

class QuickVolume:

    def cube_volume(side):
        """Calculate cube volume quickly."""
        return side ** 3


    def cube_surface_area(side):
        """Calculate cube surface area quickly."""
        return 6 * side ** 2


    def rectangular_prism_volume(length, width, height):
        """Calculate rectangular prism volume."""
        return length * width * height


    def rectangular_prism_surface_area(length, width, height):
        """Calculate rectangular prism surface area."""
        return 2 * (length*width + length*height + width*height)


    def cylinder_volume(radius, height):
        """Calculate cylinder volume."""
        return math.pi * radius ** 2 * height


    def cylinder_surface_area(radius, height):
        """Calculate cylinder surface area."""
        return 2 * math.pi * radius * (radius + height)


    def sphere_volume(radius):
        """Calculate sphere volume."""
        return (4/3) * math.pi * radius ** 3


    def sphere_surface_area(radius):
        """Calculate sphere surface area."""
        return 4 * math.pi * radius ** 2


    def cone_volume(radius, height):
        """Calculate cone volume."""
        return (1/3) * math.pi * radius ** 2 * height


    def cone_surface_area(radius, height):
        """Calculate cone surface area."""
        slant = math.sqrt(radius**2 + height**2)
        return math.pi * radius * (radius + slant)


    def square_pyramid_volume(base_side, height):
        """Calculate square pyramid volume."""
        return (1/3) * base_side ** 2 * height


    def triangular_prism_volume(base, height_triangle, prism_height):
        """Calculate triangular prism volume."""
        return 0.5 * base * height_triangle * prism_height


    def ellipsoid_volume(a, b, c):
        """Calculate ellipsoid volume."""
        return (4/3) * math.pi * a * b * c


    def torus_volume(major_radius, minor_radius):
        """Calculate torus volume."""
        return 2 * math.pi ** 2 * major_radius * minor_radius ** 2


    def tetrahedron_volume(edge):
        """Calculate regular tetrahedron volume."""
        return edge ** 3 / (6 * math.sqrt(2))


    def octahedron_volume(edge):
        """Calculate regular octahedron volume."""
        return (math.sqrt(2) / 3) * edge ** 3


    def icosahedron_volume(edge):
        """Calculate regular icosahedron volume."""
        sqrt5 = math.sqrt(5)
        return (5 * (3 + sqrt5) / 12) * edge ** 3
