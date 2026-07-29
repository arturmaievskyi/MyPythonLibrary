# 3D Figures Calculator - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [Prisms & Basic Shapes](#prisms--basic-shapes)
3. [Pyramids](#pyramids)
4. [Cylinders & Cones](#cylinders--cones)
5. [Spheres](#spheres)
6. [Platonic Solids](#platonic-solids)
7. [Usage Examples](#usage-examples)
8. [Quick Reference Functions](#quick-reference-functions)
9. [Mathematical Formulas](#mathematical-formulas)

---

## Overview

The **3D Figures Calculator** provides comprehensive calculations for 3D geometric shapes including:

- **Volume** - Internal capacity
- **Surface Area** - External area coverage
- **Diagonals** - Space diagonals and face diagonals
- **Additional Properties** - Height, radius, slant height, etc.

### Key Features

✅ **30+ 3D Shapes** supported
✅ **OOP Design** with Shape3D base class
✅ **Multiple Calculation Methods** where applicable
✅ **Comprehensive Error Handling** for invalid inputs
✅ **Advanced Properties** (diagonals, slant heights, etc.)
✅ **Accurate Mathematical Formulas** for all shapes

---

## Prisms & Basic Shapes

### Cube

A regular hexahedron with 6 square faces and 12 equal edges.

```python
from areas_3d import Cube

# Create a cube with side length 5
cube = Cube(side=5)

# Calculate properties
volume = cube.volume()              # 125
surface_area = cube.surface_area()  # 150
space_diagonal = cube.space_diagonal()  # 8.66
face_diagonal = cube.face_diagonal()    # 7.07

print(f"Volume: {volume}")
print(f"Surface Area: {surface_area}")
print(f"Space Diagonal: {space_diagonal:.2f}")
print(f"Face Diagonal: {face_diagonal:.2f}")
```

**Formulas:**
- Volume = s³
- Surface Area = 6s²
- Space Diagonal = s√3
- Face Diagonal = s√2

**Properties:**
- 6 faces (all square)
- 12 edges (all equal)
- 8 vertices

**Use Cases:**
- Dice, storage boxes, room dimensions
- Packaging design, structural elements

---

### Rectangular Prism (Cuboid)

A 6-faced solid with rectangular faces and right angles.

```python
from areas_3d import RectangularPrism

# Create a rectangular prism (4 × 6 × 3)
prism = RectangularPrism(length=4, width=6, height=3)

# Calculate properties
volume = prism.volume()              # 72
surface_area = prism.surface_area()  # 108
space_diagonal = prism.space_diagonal()  # 7.81
face_diagonals = prism.face_diagonals()

print(f"Volume: {volume}")
print(f"Surface Area: {surface_area}")
print(f"Space Diagonal: {space_diagonal:.2f}")
print(f"Face Diagonals: {face_diagonals}")
```

**Formulas:**
- Volume = l × w × h
- Surface Area = 2(lw + lh + wh)
- Space Diagonal = √(l² + w² + h²)

**Use Cases:**
- Building dimensions, room volume
- Box dimensions, storage capacity
- Shipping containers

---

### Triangular Prism

A prism with triangular bases and three rectangular faces.

```python
from areas_3d import TriangularPrism

# Create a triangular prism
# Base: triangle with base=4 and height=3
# Prism height: 5
prism = TriangularPrism(base=4, height_triangle=3, prism_height=5)

# Calculate properties
volume = prism.volume()              # 30
surface_area = prism.surface_area()

print(f"Volume: {volume}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = (½ × b × h_tri) × h_prism
- Surface Area = 2×A_triangle + (perimeter × h_prism)

**Use Cases:**
- Tent design, roof structures
- Triangular duct systems
- Architectural elements

---

### Hexagonal Prism

A prism with regular hexagonal bases.

```python
from areas_3d import HexagonalPrism

# Create a hexagonal prism
# Side of hexagon: 2, Height: 5
prism = HexagonalPrism(side=2, height=5)

# Calculate properties
volume = prism.volume()              # 51.96
surface_area = prism.surface_area()

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = (3√3/2 × s²) × h
- Surface Area = 2×(hexagon area) + 6×(rectangle area)

**Use Cases:**
- Honeycomb structures, nuts and bolts
- Industrial pipes and containers
- Crystal structures

---

## Pyramids

### Square Pyramid

A pyramid with a square base and 4 triangular faces.

```python
from areas_3d import SquarePyramid

# Create a square pyramid
# Base side: 4, Height: 6
pyramid = SquarePyramid(base_side=4, height=6)

# Calculate properties
volume = pyramid.volume()              # 32
surface_area = pyramid.surface_area()  # 56.13
slant_height = pyramid.slant_height    # 6.32
lateral_area = pyramid.lateral_area()  # 50.56

print(f"Volume: {volume}")
print(f"Surface Area: {surface_area:.2f}")
print(f"Slant Height: {slant_height:.2f}")
print(f"Lateral Area: {lateral_area:.2f}")
```

**Formulas:**
- Volume = ⅓ × s² × h
- Slant Height = √(h² + (s/2)²)
- Surface Area = s² + 2s×l
- Lateral Area = 2s×l

**Use Cases:**
- Egyptian pyramids, monuments
- Roof designs, tent peaks
- Architecture, landscape features

---

### Triangular Pyramid

A pyramid with a triangular base (3 triangular side faces + triangular base).

```python
from areas_3d import TriangularPyramid

# Create a triangular pyramid
# Base: triangle with base=4 and height=3
# Pyramid height: 5
pyramid = TriangularPyramid(base=4, height_triangle=3, pyramid_height=5)

# Calculate properties
volume = pyramid.volume()        # 10
surface_area = pyramid.surface_area()

print(f"Volume: {volume}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = ⅓ × (½ × b × h_tri) × h

**Use Cases:**
- Tetrahedron shapes, molecular models
- Decorative objects, sculptures

---

### Regular Tetrahedron

All edges equal length; 4 equilateral triangle faces.

```python
from areas_3d import RegularTetrahedron

# Create a regular tetrahedron with edge length 5
tetrahedron = RegularTetrahedron(edge=5)

# Calculate properties
volume = tetrahedron.volume()              # 14.73
surface_area = tetrahedron.surface_area()  # 43.30
height = tetrahedron.height()              # 4.08

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
print(f"Height: {height:.2f}")
```

**Formulas:**
- Volume = a³/(6√2)
- Surface Area = √3 × a²
- Height = √(⅔) × a

**Use Cases:**
- Molecular structures, chemistry
- Structural engineering, design
- Crystallography

---

## Cylinders & Cones

### Cylinder

A prism with circular bases.

```python
from areas_3d import Cylinder

# Create a cylinder (radius=3, height=8)
cylinder = Cylinder(radius=3, height=8)

# Calculate properties
volume = cylinder.volume()              # 226.19
surface_area = cylinder.surface_area()  # 207.35
lateral_area = cylinder.lateral_area()  # 150.80
space_diagonal = cylinder.space_diagonal()  # 8.25

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
print(f"Lateral Area: {lateral_area:.2f}")
print(f"Space Diagonal: {space_diagonal:.2f}")
```

**Formulas:**
- Volume = πr²h
- Surface Area = 2πr² + 2πrh = 2πr(r + h)
- Lateral Area = 2πrh
- Space Diagonal = √(4r² + h²)

**Use Cases:**
- Pipes, tubes, containers
- Cans, drums, storage tanks
- Columns, pillars

---

### Cone

A circular pyramid.

```python
from areas_3d import Cone

# Create a cone (radius=3, height=5)
cone = Cone(radius=3, height=5)

# Calculate properties
volume = cone.volume()              # 47.12
surface_area = cone.surface_area()  # 64.41
slant_height = cone.slant_height    # 5.83
lateral_area = cone.lateral_area()  # 54.88

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
print(f"Slant Height: {slant_height:.2f}")
print(f"Lateral Area: {lateral_area:.2f}")
```

**Formulas:**
- Volume = ⅓πr²h
- Slant Height = √(r² + h²)
- Surface Area = πr² + πrl
- Lateral Area = πrl

**Use Cases:**
- Traffic cones, funnels
- Ice cream cones, party hats
- Rocket nosecones

---

### Frustum (Truncated Cone)

A cone with the top cut off.

```python
from areas_3d import Frustum

# Create a frustum
# Large radius: 5, Small radius: 3, Height: 4
frustum = Frustum(radius1=5, radius2=3, height=4)

# Calculate properties
volume = frustum.volume()              # 163.36
surface_area = frustum.surface_area()  # 186.90
slant_height = frustum.slant_height    # 4.47

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
print(f"Slant Height: {slant_height:.2f}")
```

**Formulas:**
- Volume = ⅓πh(r₁² + r₁r₂ + r₂²)
- Slant Height = √(h² + (r₁ - r₂)²)
- Surface Area = π(r₁² + r₂²) + π(r₁ + r₂)l

**Use Cases:**
- Bucket shapes, tapered containers
- Lamp shades, ventilation ducts
- Engineering components

---

## Spheres

### Sphere

Perfect round 3D shape.

```python
from areas_3d import Sphere

# Create a sphere with radius 5
sphere = Sphere(radius=5)

# Calculate properties
volume = sphere.volume()              # 523.60
surface_area = sphere.surface_area()  # 314.16
diameter = sphere.diameter()          # 10
circumference = sphere.circumference()  # 31.42

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference:.2f}")
```

**Formulas:**
- Volume = ⁴⁄₃πr³
- Surface Area = 4πr²
- Diameter = 2r
- Circumference = 2πr

**Use Cases:**
- Balls, balloons, planets
- Tank design, pressure vessels
- Spherical bearings

---

### Spherical Cap

Portion of sphere cut by a plane.

```python
from areas_3d import SphericalCap

# Create a spherical cap
# Sphere radius: 5, Cap height: 2
cap = SphericalCap(radius=5, height=2)

# Calculate properties
volume = cap.volume()              # 20.94
curved_area = cap.curved_surface_area()  # 62.83
base_area = cap.base_area()         # 28.27
total_area = cap.surface_area()     # 91.10

print(f"Volume: {volume:.2f}")
print(f"Curved Surface Area: {curved_area:.2f}")
print(f"Base Area: {base_area:.2f}")
print(f"Total Surface Area: {total_area:.2f}")
```

**Formulas:**
- Volume = (πh²/3)(3r - h)
- Curved Surface Area = 2πrh
- Base Area = π(2rh - h²)

**Use Cases:**
- Dome structures, hemispheres
- Tank bottoms, spacecraft design
- Liquid in spherical containers

---

### Ellipsoid

3D ellipse (stretched sphere).

```python
from areas_3d import Ellipsoid

# Create an ellipsoid
# Semi-axes: a=5, b=4, c=3
ellipsoid = Ellipsoid(a=5, b=4, c=3)

# Calculate properties
volume = ellipsoid.volume()              # 251.33
surface_area = ellipsoid.surface_area()  # 213.56

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = ⁴⁄₃πabc
- Surface Area ≈ 4π × ((aᵖbᵖ + aᵖcᵖ + bᵖcᵖ)/3)^(1/p)  [Knud Thomsen]

**Use Cases:**
- Planetary models (Earth is an oblate ellipsoid)
- Biological cells, egg shapes
- Engineering components

---

### Torus

Donut shape.

```python
from areas_3d import Torus

# Create a torus
# Major radius: 5, Minor radius: 2
torus = Torus(major_radius=5, minor_radius=2)

# Calculate properties
volume = torus.volume()              # 394.78
surface_area = torus.surface_area()  # 394.78

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = 2π²Rr²
- Surface Area = 4π²Rr

**Use Cases:**
- Donuts, tires, rings
- Magnetic field rings
- Industrial gaskets

---

## Platonic Solids

### Regular Octahedron

8 equilateral triangle faces.

```python
from areas_3d import RegularOctahedron

# Create a regular octahedron with edge 3
octahedron = RegularOctahedron(edge=3)

# Calculate properties
volume = octahedron.volume()              # 12.73
surface_area = octahedron.surface_area()  # 31.18

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = (√2/3) × a³
- Surface Area = 2√3 × a²

**Properties:**
- 8 faces (equilateral triangles)
- 12 edges (all equal)
- 6 vertices

---

### Regular Dodecahedron

12 pentagonal faces.

```python
from areas_3d import RegularDodecahedron

# Create a regular dodecahedron with edge 2
dodecahedron = RegularDodecahedron(edge=2)

# Calculate properties
volume = dodecahedron.volume()              # 61.61
surface_area = dodecahedron.surface_area()  # 82.23

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = ((15 + 7√5)/4) × a³
- Surface Area = 3√(25 + 10√5) × a²

**Properties:**
- 12 faces (regular pentagons)
- 30 edges (all equal)
- 20 vertices

---

### Regular Icosahedron

20 equilateral triangle faces.

```python
from areas_3d import RegularIcosahedron

# Create a regular icosahedron with edge 2
icosahedron = RegularIcosahedron(edge=2)

# Calculate properties
volume = icosahedron.volume()              # 18.51
surface_area = icosahedron.surface_area()  # 34.64

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")
```

**Formulas:**
- Volume = (5(3 + √5)/12) × a³
- Surface Area = 5√3 × a²

**Properties:**
- 20 faces (equilateral triangles)
- 30 edges (all equal)
- 12 vertices

---

## Usage Examples

### Example 1: Calculate Volume of a Water Tank

```python
from areas_3d import Cylinder

# Cylindrical tank with radius 2 meters, height 3 meters
tank = Cylinder(radius=2, height=3)

volume = tank.volume()  # m³
volume_liters = volume * 1000  # Convert to liters

print(f"Tank Volume: {volume:.2f} cubic meters")
print(f"Tank Capacity: {volume_liters:.0f} liters")

# Calculate surface area for painting
surface_area = tank.surface_area()
print(f"Surface Area to Paint: {surface_area:.2f} m²")
```

**Output:**
```
Tank Volume: 37.70 cubic meters
Tank Capacity: 37699 liters
Surface Area to Paint: 62.83 m²
```

---

### Example 2: Compare Storage Containers

```python
from areas_3d import Cube, RectangularPrism, Cylinder

print("Storage Container Comparison:")
print("=" * 60)

# Cube (6×6×6)
cube = Cube(side=6)
print(f"Cube (6×6×6):")
print(f"  Volume: {cube.volume():.2f} m³")
print(f"  Surface Area: {cube.surface_area():.2f} m²")

# Rectangular box (8×6×5)
box = RectangularPrism(length=8, width=6, height=5)
print(f"\nRectangular Box (8×6×5):")
print(f"  Volume: {box.volume():.2f} m³")
print(f"  Surface Area: {box.surface_area():.2f} m²")

# Cylindrical tank (radius=2, height=8)
cylinder = Cylinder(radius=2, height=8)
print(f"\nCylindrical Tank (r=2, h=8):")
print(f"  Volume: {cylinder.volume():.2f} m³")
print(f"  Surface Area: {cylinder.surface_area():.2f} m²")

# Find largest volume
volumes = {
    "Cube": cube.volume(),
    "Box": box.volume(),
    "Cylinder": cylinder.volume()
}
largest = max(volumes, key=volumes.get)
print(f"\nLargest Volume: {largest} ({volumes[largest]:.2f} m³)")
```

---

### Example 3: Ice Cream Cone Calculations

```python
from areas_3d import Cone, Sphere

# Cone (radius=2cm, height=8cm)
cone = Cone(radius=2, height=8)
cone_volume = cone.volume()

# Hemisphere (radius=2cm)
sphere = Sphere(radius=2)
hemisphere_volume = sphere.volume() / 2

print("Ice Cream Cone Capacity:")
print(f"Cone Volume: {cone_volume:.2f} cm³")
print(f"Hemisphere Volume: {hemisphere_volume:.2f} cm³")
print(f"Total Capacity: {cone_volume + hemisphere_volume:.2f} cm³")

# Surface area (cone lateral + hemisphere)
cone_lateral = cone.lateral_area()
hemisphere_surface = 2 * math.pi * 2**2
print(f"\nCone Lateral Area: {cone_lateral:.2f} cm²")
print(f"Hemisphere Area: {hemisphere_surface:.2f} cm²")
```

---

### Example 4: Construction - Concrete for Pool

```python
from areas_3d import Cylinder, RectangularPrism

# Concrete pool dimensions
# Inner dimensions: cylinder with radius 3m, depth 2m
# Wall thickness: 0.3m

# Outer cylinder
outer = Cylinder(radius=3.3, height=2.3)
# Inner cylinder
inner = Cylinder(radius=3, height=2)

concrete_volume = outer.volume() - inner.volume()
concrete_needed_m3 = concrete_volume
concrete_needed_kg = concrete_needed_m3 * 2400  # 2400 kg/m³

print("Swimming Pool Concrete Calculation:")
print(f"Outer Volume: {outer.volume():.2f} m³")
print(f"Inner Volume: {inner.volume():.2f} m³")
print(f"Concrete Volume: {concrete_volume:.2f} m³")
print(f"Concrete Weight: {concrete_needed_kg:.0f} kg")
print(f"Concrete Cost (at $150/m³): ${concrete_volume * 150:.2f}")
```

---

### Example 5: Rocket Design - Calculate Mass

```python
from areas_3d import Cylinder, Cone

# Rocket body (cylinder)
body = Cylinder(radius=1.5, height=10)
body_volume = body.volume()

# Nose cone (cone)
nose = Cone(radius=1.5, height=3)
nose_volume = nose.volume()

total_volume = body_volume + nose_volume

# Assuming fuel density = 800 kg/m³
fuel_density = 800
total_mass = total_volume * fuel_density

print("Rocket Specifications:")
print(f"Body Volume: {body_volume:.2f} m³")
print(f"Nose Cone Volume: {nose_volume:.2f} m³")
print(f"Total Volume: {total_volume:.2f} m³")
print(f"Total Fuel Mass: {total_mass:.0f} kg")

# Surface area for thermal protection
surface_area = body.lateral_area() + nose.lateral_area()
print(f"Surface Area (Heat Shield): {surface_area:.2f} m²")
```

---

### Example 6: Packaging Optimization

```python
from areas_3d import Cube, RectangularPrism, Cylinder

print("Packaging Options for 1000 cm³ Product Volume:")
print("=" * 60)

target_volume = 1000

# Option 1: Cube
cube_side = target_volume ** (1/3)
cube = Cube(side=cube_side)
print(f"Cube ({cube_side:.2f} × {cube_side:.2f} × {cube_side:.2f}):")
print(f"  Volume: {cube.volume():.2f} cm³")
print(f"  Material (Surface Area): {cube.surface_area():.2f} cm²")

# Option 2: Rectangular (2:1:1 ratio)
rect = RectangularPrism(length=12.6, width=6.3, height=12.6)
print(f"\nRectangular (12.6 × 6.3 × 12.6):")
print(f"  Volume: {rect.volume():.2f} cm³")
print(f"  Material (Surface Area): {rect.surface_area():.2f} cm²")

# Option 3: Cylinder
height_cyl = 20
radius_cyl = math.sqrt(target_volume / (math.pi * height_cyl))
cylinder = Cylinder(radius=radius_cyl, height=height_cyl)
print(f"\nCylinder (r={radius_cyl:.2f}, h={height_cyl}):")
print(f"  Volume: {cylinder.volume():.2f} cm³")
print(f"  Material (Surface Area): {cylinder.surface_area():.2f} cm²")

# Comparison
areas = {
    "Cube": cube.surface_area(),
    "Rectangular": rect.surface_area(),
    "Cylinder": cylinder.surface_area()
}
most_efficient = min(areas, key=areas.get)
print(f"\nMost Material Efficient: {most_efficient}")
```

---

## Quick Reference Functions

Fast calculation functions without object instantiation:

```python
from areas_3d import *

# Cube
cube_volume(5)              # 125
cube_surface_area(5)        # 150

# Rectangular Prism
rectangular_prism_volume(4, 6, 3)       # 72
rectangular_prism_surface_area(4, 6, 3) # 108

# Cylinder
cylinder_volume(3, 8)       # 226.19
cylinder_surface_area(3, 8) # 207.35

# Sphere
sphere_volume(5)            # 523.60
sphere_surface_area(5)      # 314.16

# Cone
cone_volume(3, 5)           # 47.12
cone_surface_area(3, 5)     # 64.41

# Square Pyramid
square_pyramid_volume(4, 6) # 32

# Ellipsoid
ellipsoid_volume(5, 4, 3)   # 251.33

# Torus
torus_volume(5, 2)          # 394.78

# Platonic Solids
tetrahedron_volume(5)       # 14.73
octahedron_volume(3)        # 12.73
icosahedron_volume(2)       # 18.51
```

---

## Mathematical Formulas

### Prisms

| Shape | Volume | Surface Area |
|-------|--------|---------------|
| Cube | s³ | 6s² |
| Rectangular | l×w×h | 2(lw+lh+wh) |
| Triangular | (½bh)×H | 2×(tri area)+(perimeter×H) |
| Hexagonal | (3√3/2×s²)×h | 2×(hex area)+6×(s×h) |

### Pyramids & Cones

| Shape | Volume | Surface Area |
|-------|--------|---------------|
| Square Pyramid | ⅓s²h | s²+2sl |
| Triangular Pyramid | ⅓×(½bh)×H | Sum of all 4 faces |
| Regular Tetrahedron | a³/(6√2) | √3×a² |
| Cone | ⅓πr²h | πr²+πrl |
| Frustum | ⅓πh(r₁²+r₁r₂+r₂²) | π(r₁²+r₂²)+π(r₁+r₂)l |

### Spheres

| Shape | Volume | Surface Area |
|-------|--------|---------------|
| Sphere | ⁴⁄₃πr³ | 4πr² |
| Spherical Cap | (πh²/3)(3r-h) | 2πrh+(base area) |
| Ellipsoid | ⁴⁄₃πabc | Thomsen approx. |
| Torus | 2π²Rr² | 4π²Rr |

### Platonic Solids

| Shape | Faces | Edges | Vertices | Volume | Surface Area |
|-------|-------|-------|----------|--------|--------------|
| Tetrahedron | 4 △ | 6 | 4 | a³/(6√2) | √3×a² |
| Octahedron | 8 △ | 12 | 6 | (√2/3)×a³ | 2√3×a² |
| Dodecahedron | 12 ⬠ | 30 | 20 | ((15+7√5)/4)×a³ | 3√(25+10√5)×a² |
| Icosahedron | 20 △ | 30 | 12 | (5(3+√5)/12)×a³ | 5√3×a² |

---

## Diagonals Reference

| Shape | Diagonal Type | Formula |
|-------|---------------|---------|
| Cube | Space | s√3 |
| Cube | Face | s√2 |
| Rectangular Prism | Space | √(l²+w²+h²) |
| Square Pyramid | Base | s√2 |
| Cylinder | Axial | √(4r²+h²) |

---

## Error Handling

All classes validate inputs:

```python
from areas_3d import Cube, Sphere, RectangularPrism

try:
    # Negative side
    cube = Cube(side=-5)
except ValueError as e:
    print(f"Error: {e}")  # "Side length must be positive"

try:
    # Zero radius
    sphere = Sphere(radius=0)
except ValueError as e:
    print(f"Error: {e}")  # "Radius must be positive"

try:
    # Invalid dimensions
    prism = RectangularPrism(length=-4, width=6, height=3)
except ValueError as e:
    print(f"Error: {e}")  # "All dimensions must be positive"
```

---

## Unit Conversion

```python
# Volume conversions
volume_m3 = 1.0
volume_cm3 = volume_m3 * 1e6
volume_mm3 = volume_m3 * 1e9
volume_liters = volume_m3 * 1000
volume_gallons = volume_liters * 0.264172

# Surface area conversions
area_m2 = 1.0
area_cm2 = area_m2 * 1e4
area_mm2 = area_m2 * 1e6
area_ft2 = area_m2 * 10.7639
```

---

## Applications by Field

| Field | Shapes Used | Purpose |
|-------|------------|---------|
| Architecture | All shapes | Building design, material calculation |
| Engineering | Cylinders, Cones, Prisms | Pipe sizing, tank design |
| Manufacturing | All shapes | Mold design, material optimization |
| Fluid Mechanics | Cylinders, Spheres | Tank design, pressure vessel calc |
| Packaging | All shapes | Box optimization, material reduction |
| Astronomy | Spheres, Ellipsoids | Planetary modeling, orbital mechanics |
| Chemistry | Tetrahedron, Octahedron | Molecular structures, crystal shapes |
| Food | Cone, Sphere, Cylinder | Recipe scaling, container sizing |

---

## Summary

The **3D Figures Calculator** provides:

✅ **Prisms** - Cube, Rectangular, Triangular, Hexagonal
✅ **Pyramids** - Square, Triangular, Regular Tetrahedron
✅ **Cylinders** - Cylinder, Cone, Frustum
✅ **Spheres** - Sphere, Cap, Ellipsoid, Torus
✅ **Platonic Solids** - Tetrahedron, Octahedron, Dodecahedron, Icosahedron
✅ **Complete Calculations** - Volume, Surface Area, Diagonals, Properties
✅ **Real-World Applications** - Practical examples for common scenarios
✅ **Flexible Interfaces** - Both OOP and functional approaches

Perfect for engineers, architects, students, and anyone working with 3D shapes!

---
