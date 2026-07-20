# EuclideanTopology - Comprehensive Documentation

## Overview

The **EuclideanTopology** class provides a complete implementation of the standard topology on Euclidean spaces (ℝⁿ). It includes:

- Distance metrics and norms
- Ball operations (open, closed, spheres)
- Interval operations (1D)
- Convergence and limits
- Connectedness and path connectivity
- Compactness analysis
- Convexity operations
- Continuity checking
- Vector space operations
- Gram-Schmidt orthonormalization

---

## Core Features

### 1. Initialization

```python
from euclidean_topology_extended import EuclideanTopology

# 1D Euclidean space
space_1d = EuclideanTopology(dimension=1)

# 2D Euclidean space
space_2d = EuclideanTopology(dimension=2, bounds=(-10, 10))

# 3D Euclidean space
space_3d = EuclideanTopology(dimension=3)
```

---

## Distance Metrics

### Euclidean Distance (L² norm)
```python
d = EuclideanTopology.euclidean_distance((0, 0), (3, 4))  # 5.0
# Formula: √(Σ(xᵢ - yᵢ)²)
```

### Manhattan Distance (L¹ norm)
```python
d = EuclideanTopology.manhattan_distance((0, 0), (3, 4))  # 7
# Formula: Σ|xᵢ - yᵢ|
```

### Chebyshev Distance (L∞ norm)
```python
d = EuclideanTopology.chebyshev_distance((0, 0), (3, 4))  # 4
# Formula: max(|xᵢ - yᵢ|)
```

---

## Ball Operations

### Open Ball
```python
# B(c, r) = {x : d(x, c) < r}
ball = EuclideanTopology.open_ball((0, 0), radius=1.5, dimension=2)
# Returns set of points strictly within radius
```

### Closed Ball
```python
# B̄(c, r) = {x : d(x, c) ≤ r}
ball = EuclideanTopology.closed_ball((0, 0), radius=1.5, dimension=2)
# Returns set of points within and on boundary
```

### Sphere
```python
# S(c, r) = {x : d(x, c) = r}
sphere = EuclideanTopology.sphere((0, 0), radius=1.0, dimension=2)
# Returns points exactly at distance radius
```

---

## Interval Operations (1D)

### Create Intervals
```python
open_int = EuclideanTopology.open_interval(0, 1)        # (0, 1)
closed_int = EuclideanTopology.closed_interval(0, 1)    # [0, 1]
half_left = EuclideanTopology.half_open_interval_left(0, 1)   # [0, 1)
half_right = EuclideanTopology.half_open_interval_right(0, 1) # (0, 1]
```

### Test Membership
```python
is_in = EuclideanTopology.interval_contains((0, 1, "open"), 0.5)  # True
is_in = EuclideanTopology.interval_contains((0, 1, "open"), 0)    # False
```

### Interval Operations
```python
# Union of intervals
merged = EuclideanTopology.interval_union((0, 1, "closed"), (1, 2, "closed"))

# Intersection of intervals
inter = EuclideanTopology.interval_intersection((0, 2, "closed"), (1, 3, "closed"))
# Returns (1, 2, "intersection")
```

---

## Convergence & Limits

### Check Convergence
```python
sequence = [1.0, 0.5, 0.25, 0.125, 0.0625]
is_convergent = space.is_convergent_sequence(sequence, limit=0, epsilon=0.1)
```

### Find Limit
```python
limit = space.limit_of_sequence(sequence)
# Returns limit point if sequence converges
```

### Cauchy Sequence
```python
is_cauchy = space.cauchy_sequence(sequence, epsilon=1e-6)
# Check if sequence is Cauchy (convergent)
```

---

## Connectedness

### Path Connectivity
```python
# Check if path exists between two points
is_path_connected = space.path_connected((0, 0), (3, 4))  # True

# Generate path
path = space.path_from_to((0, 0), (3, 4), steps=10)
# Returns straight line path with 10 points
```

### Connected Sets
```python
is_connected = space.is_connected_set(interval)
# Single interval is connected
```

---

## Compactness

### Check Compactness
```python
# Heine-Borel Theorem: Compact ⟺ Closed and Bounded
interval = (0, 1, "closed")
is_compact = space.is_compact_set(interval)  # True

open_interval = (0, 1, "open")
is_compact = space.is_compact_set(open_interval)  # False (not closed)
```

### Boundedness
```python
is_bounded = space.is_bounded(interval)
diameter = space.diameter(interval)  # 1.0 for [0, 1]
```

---

## Convexity

### Check Convexity
```python
interval = (0, 1, "closed")
is_convex = space.is_convex(interval)  # True
```

### Convex Hull
```python
points = [(0, 0), (1, 0), (0, 1), (1, 1)]
hull = space.convex_hull(points)
# Returns vertices of convex hull
```

### Convex Combination
```python
point = (0.5, 0.5)
points = [(0, 0), (1, 0), (0, 1), (1, 1)]
weights = [0.25, 0.25, 0.25, 0.25]

is_combo = space.is_convex_combination(point, points, weights)
# Check if point is weighted average of points
```

---

## Continuity

### Check Continuity
```python
def f(x):
    return x ** 2

domain = (0, 2, "closed")
is_continuous = space.is_continuous_function(f, domain)
```

### Uniform Continuity
```python
is_uniform = space.uniform_continuous(f, domain, epsilon=1e-6)
# More stringent than pointwise continuity
```

---

## Vector Space Operations

### Norms
```python
v = (3, 4)

euclidean = EuclideanTopology.euclidean_norm(v)  # 5.0 (√(9+16))
taxicab = EuclideanTopology.taxicab_norm(v)      # 7 (3+4)
supremum = EuclideanTopology.supremum_norm(v)    # 4 (max(3,4))
p_norm = EuclideanTopology.p_norm(v, p=3)        # Lp norm
```

### Vector Operations
```python
v1 = (1, 2, 3)
v2 = (4, 5, 6)

# Addition
sum_v = EuclideanTopology.vector_addition(v1, v2)  # (5, 7, 9)

# Scalar multiplication
scaled = EuclideanTopology.scalar_multiplication(2, v1)  # (2, 4, 6)

# Dot product
dot = EuclideanTopology.dot_product(v1, v2)  # 32 (1*4 + 2*5 + 3*6)

# Cross product (3D)
cross = EuclideanTopology.cross_product_3d(v1, v2)
```

### Orthogonality
```python
v1 = (1, 0)
v2 = (0, 1)

is_orthogonal = space.orthogonal(v1, v2)  # True (dot product = 0)

# Gram-Schmidt orthonormalization
vectors = [(1, 1), (1, -1), (0, 1)]
basis = space.orthonormal_basis(vectors)
# Returns orthonormal basis
```

### Angles
```python
v1 = (1, 0)
v2 = (0, 1)

angle = space.angle_between(v1, v2)  # π/2 (90 degrees)
angle_degrees = math.degrees(angle)   # 90.0
```

---

## Geometric Analysis

### Centroid
```python
points = [(0, 0), (1, 0), (0, 1), (1, 1)]
center = space.centroid(points)  # (0.5, 0.5)
```

### Distance Matrix
```python
points = [(0, 0), (1, 0), (0, 1)]
matrix = space.pairwise_distances_matrix(points)
# Returns 3x3 matrix of pairwise distances
```

### Orthogonal Sets
```python
vectors = [(1, 0), (0, 1)]
is_orthogonal_set = space.is_orthogonal_set(vectors)  # True
```

---

## Space Properties

### Get All Properties
```python
props = space.get_properties()
# Returns dictionary with:
# - dimension
# - is_connected (True)
# - is_hausdorff (True)
# - is_separable (True)
# - is_complete (True)
# - is_metrizable (True)
# - has_euclidean_metric (True)
```

### Print Properties
```python
space.print_properties()
# Formatted output of all properties
```

### Summary
```python
summary = space.summary()
# "Euclidean Space ℝ^2 (bounds: (-10, 10))"
```

---

## Utility Functions

### Line Segment
```python
from euclidean_topology_extended import line_segment

points = line_segment((0, 0), (1, 1), steps=11)
# 11 points along line from origin to (1,1)
```

### Circle
```python
from euclidean_topology_extended import circle

circle_points = circle(center=(0, 0), radius=1, steps=100)
# 100 points on unit circle
```

### Sphere Surface
```python
from euclidean_topology_extended import sphere_surface

sphere_points = sphere_surface(center=(0, 0, 0), radius=1, steps=20)
# Points on unit sphere in 3D
```

---

## Complete Example

```python
from euclidean_topology_extended import EuclideanTopology
import math

# Create 2D Euclidean space
space = EuclideanTopology(dimension=2, bounds=(-10, 10))

# Ball operations
open_ball = space.open_ball((0, 0), radius=2)
closed_ball = space.closed_ball((0, 0), radius=2)
print(f"Open ball size: {len(open_ball)}")
print(f"Closed ball size: {len(closed_ball)}")

# Path connectivity
p1 = (0, 0)
p2 = (3, 4)
path = space.path_from_to(p1, p2, steps=5)
print(f"Path from {p1} to {p2}: {path}")

# Vector operations
v1 = (3, 4)
v2 = (5, 12)
distance = space.euclidean_distance(v1, v2)
dot = space.dot_product(v1, v2)
angle = space.angle_between(v1, v2)

print(f"Distance: {distance:.2f}")
print(f"Dot product: {dot}")
print(f"Angle: {math.degrees(angle):.2f}°")

# Convexity
hull = space.convex_hull([(0, 0), (1, 0), (0, 1), (1, 1)])
print(f"Convex hull: {hull}")

# Space properties
space.print_properties()
```

---

## Mathematical Background

### Euclidean Space (ℝⁿ)
- **Dimension**: n (number of coordinates)
- **Metric**: d(x,y) = √(Σ(xᵢ - yᵢ)²)
- **Topology**: Induced by Euclidean metric

### Properties
- **Connected**: Cannot separate into disjoint open sets
- **Hausdorff**: Any two points have disjoint neighborhoods
- **Separable**: Has countable dense subset (rationals)
- **Complete**: Every Cauchy sequence converges
- **Metrizable**: Induced by Euclidean metric

### Compactness (Heine-Borel Theorem)
- In ℝⁿ: Compact ⟺ Closed and Bounded
- Open balls are not compact (not closed)
- Closed balls are compact

### Connectedness
- ℝⁿ is path-connected
- Any continuous path between two points exists
- Intervals in ℝ are connected

---

## Method Count by Category

| Category | Methods | Examples |
|----------|---------|----------|
| Distance Metrics | 3 | euclidean, manhattan, chebyshev |
| Ball Operations | 3 | open_ball, closed_ball, sphere |
| Interval Operations | 4 | open_interval, closed_interval, union, intersection |
| Convergence | 3 | is_convergent_sequence, limit_of_sequence, cauchy_sequence |
| Connectedness | 3 | is_connected, path_connected, path_from_to |
| Compactness | 3 | is_compact_set, is_bounded, diameter |
| Convexity | 3 | is_convex, convex_hull, is_convex_combination |
| Continuity | 2 | is_continuous_function, uniform_continuous |
| Norms | 4 | euclidean_norm, taxicab_norm, supremum_norm, p_norm |
| Vector Operations | 5 | vector_addition, scalar_multiplication, dot_product, cross_product_3d |
| Orthogonality | 3 | orthogonal, orthonormal_basis, is_orthogonal_set |
| Geometry | 4 | centroid, pairwise_distances_matrix, angle_between |
| Utilities | 3 | get_properties, print_properties, summary |

**Total: 45+ Methods**

---

## Performance Notes

- Distance calculations: O(n) where n = dimension
- Ball generation: O(m²) where m = resolution
- Convex hull (2D): O(n log n) using Graham scan
- Gram-Schmidt: O(n³) for n vectors in ℝⁿ

---

## Applications

- **Physics**: Particle systems, trajectories
- **Graphics**: 3D geometry, transformations
- **ML/Statistics**: Distance-based algorithms, clustering
- **Optimization**: Convex optimization, linear programming
- **Analysis**: Convergence, continuity properties

---

# EuclideanTopology - Working Examples

Complete working examples demonstrating all major features.

---

## Example 1: Basic Setup & Properties

```python
from euclidean_topology_extended import EuclideanTopology
import math

print("="*60)
print("Example 1: Basic Setup & Space Properties")
print("="*60)

# Create 1D space
space_1d = EuclideanTopology(dimension=1)
print(f"1D Space: {space_1d.summary()}")

# Create 2D space
space_2d = EuclideanTopology(dimension=2, bounds=(-10, 10))
print(f"2D Space: {space_2d.summary()}")

# Create 3D space
space_3d = EuclideanTopology(dimension=3)
print(f"3D Space: {space_3d.summary()}")

# Print all properties
space_2d.print_properties()
```

---

## Example 2: Distance Metrics

```python
print("="*60)
print("Example 2: Distance Metrics Comparison")
print("="*60)

p1 = (0, 0)
p2 = (3, 4)

euclidean = EuclideanTopology.euclidean_distance(p1, p2)
manhattan = EuclideanTopology.manhattan_distance(p1, p2)
chebyshev = EuclideanTopology.chebyshev_distance(p1, p2)

print(f"Distance from {p1} to {p2}:")
print(f"  Euclidean (L²): {euclidean:.2f}")
print(f"  Manhattan (L¹): {manhattan:.2f}")
print(f"  Chebyshev (L∞): {chebyshev:.2f}")

# Visualize
print("\nInterpretation:")
print(f"  Euclidean: straight line distance")
print(f"  Manhattan: sum of coordinate differences")
print(f"  Chebyshev: maximum coordinate difference")
print()
```

---

## Example 3: Ball Operations

```python
print("="*60)
print("Example 3: Ball Operations")
print("="*60)

space = EuclideanTopology(dimension=2)

center = (0, 0)
radius = 1.5

# Open ball
open_ball = space.open_ball(center, radius)
print(f"Open ball B({center}, {radius}):")
print(f"  Points in ball: {len(open_ball)}")

# Closed ball
closed_ball = space.closed_ball(center, radius)
print(f"Closed ball B̄({center}, {radius}):")
print(f"  Points in ball: {len(closed_ball)}")

# Sphere
sphere = space.sphere(center, 1.0)
print(f"Sphere S({center}, 1.0):")
print(f"  Points on sphere: {len(sphere)}")

# Verify inclusion
test_point = (0.5, 0.5)
dist = space.euclidean_distance(center, test_point)
print(f"\nTest point {test_point} at distance {dist:.2f}:")
print(f"  In open ball: {test_point in open_ball}")
print(f"  In closed ball: {test_point in closed_ball}")
print()
```

---

## Example 4: Interval Operations (1D)

```python
print("="*60)
print("Example 4: Interval Operations (1D)")
print("="*60)

# Create intervals
open_int = EuclideanTopology.open_interval(0, 1)
closed_int = EuclideanTopology.closed_interval(0, 1)
half_left = EuclideanTopology.half_open_interval_left(0, 1)
half_right = EuclideanTopology.half_open_interval_right(0, 1)

print("Different interval types from 0 to 1:")
print(f"  Open (0, 1):        {open_int}")
print(f"  Closed [0, 1]:      {closed_int}")
print(f"  Half-left [0, 1):   {half_left}")
print(f"  Half-right (0, 1]:  {half_right}")

# Test membership
test_points = [0, 0.5, 1]
print("\nMembership tests:")
for x in test_points:
    in_open = EuclideanTopology.interval_contains(open_int, x)
    in_closed = EuclideanTopology.interval_contains(closed_int, x)
    print(f"  {x}: in (0,1)? {in_open}, in [0,1]? {in_closed}")

# Union and intersection
int1 = (0, 1, "closed")
int2 = (0.5, 1.5, "closed")

union = EuclideanTopology.interval_union(int1, int2)
intersection = EuclideanTopology.interval_intersection(int1, int2)

print(f"\nUnion of [0,1] and [0.5,1.5]: {union}")
print(f"Intersection: {intersection}")
print()
```

---

## Example 5: Convergence & Limits

```python
print("="*60)
print("Example 5: Convergence & Limits")
print("="*60)

space = EuclideanTopology(dimension=1)

# Convergent sequence (decreasing to 0)
seq1 = [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125]
print(f"Sequence 1: {seq1}")
print(f"  Converges to 0? {space.is_convergent_sequence(seq1, limit=0, epsilon=0.05)}")
print(f"  Limit: {space.limit_of_sequence(seq1)}")

# Another sequence
seq2 = [1/n for n in range(1, 11)]
print(f"\nSequence 2 (1/n): {[f'{x:.2f}' for x in seq2]}")
print(f"  Is Cauchy? {space.cauchy_sequence(seq2)}")
print(f"  Limit: {space.limit_of_sequence(seq2)}")

# Divergent sequence
seq3 = [1, 2, 3, 4, 5]
print(f"\nSequence 3: {seq3}")
print(f"  Converges to 0? {space.is_convergent_sequence(seq3, limit=0)}")
print(f"  Limit: {space.limit_of_sequence(seq3)}")
print()
```

---

## Example 6: Path Connectivity

```python
print("="*60)
print("Example 6: Path Connectivity")
print("="*60)

space = EuclideanTopology(dimension=2)

p1 = (0, 0)
p2 = (3, 4)

# Check path connectivity
is_connected = space.path_connected(p1, p2)
print(f"Path from {p1} to {p2}: {is_connected}")

# Generate path
path = space.path_from_to(p1, p2, steps=5)
print(f"\nPath with 5 steps:")
for i, point in enumerate(path):
    print(f"  Step {i}: ({point[0]:.2f}, {point[1]:.2f})")

# More detailed path
path_detailed = space.path_from_to(p1, p2, steps=11)
print(f"\nPath length (straight line): {len(path_detailed)} points")
print(f"Total path distance: {sum(space.euclidean_distance(path_detailed[i], path_detailed[i+1]) for i in range(len(path_detailed)-1)):.2f}")
print()
```

---

## Example 7: Compactness & Boundedness

```python
print("="*60)
print("Example 7: Compactness & Boundedness (Heine-Borel)")
print("="*60)

space = EuclideanTopology(dimension=1)

# Test different sets
intervals = [
    ((0, 1, "open"), "Open interval (0, 1)"),
    ((0, 1, "closed"), "Closed interval [0, 1]"),
    ((0, 1, "half-open-left"), "Half-open [0, 1)"),
    ((-float('inf'), float('inf'), "open"), "Entire real line"),
]

print("Compactness Analysis (Heine-Borel: Compact ⟺ Closed & Bounded):\n")
print(f"{'Interval':<30} {'Closed':<10} {'Bounded':<10} {'Compact':<10}")
print("-" * 60)

for interval, name in intervals:
    # Simplified checks
    is_closed = interval[2] == "closed"
    is_bounded = abs(interval[1] - interval[0]) < float('inf')
    is_compact = space.is_compact_set(interval)
    
    print(f"{name:<30} {str(is_closed):<10} {str(is_bounded):<10} {str(is_compact):<10}")

print("\nInterpretation:")
print("  (0, 1): Not closed → Not compact")
print("  [0, 1]: Closed and bounded → Compact")
print("  ℝ: Not bounded → Not compact")
print()
```

---

## Example 8: Convexity

```python
print("="*60)
print("Example 8: Convexity")
print("="*60)

space = EuclideanTopology(dimension=2)

# Convex set (triangle)
triangle = [(0, 0), (1, 0), (0, 1)]
print(f"Triangle: {triangle}")
print(f"Is convex: {space.is_convex(triangle)}")

# Convex hull
points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
hull = space.convex_hull(points)
print(f"\nPoints: {points}")
print(f"Convex hull: {hull}")

# Centroid
centroid = space.centroid(points)
print(f"Centroid: {centroid}")

# Is centroid a convex combination?
is_combo = space.is_convex_combination(
    centroid, 
    points,
    weights=[0.2, 0.2, 0.2, 0.2, 0.2]
)
print(f"Centroid is convex combination: {is_combo}")
print()
```

---

## Example 9: Vector Operations

```python
print("="*60)
print("Example 9: Vector Operations & Norms")
print("="*60)

v1 = (3, 4)
v2 = (5, 12)

# Norms
euclidean_norm = EuclideanTopology.euclidean_norm(v1)
taxicab_norm = EuclideanTopology.taxicab_norm(v1)
supremum_norm = EuclideanTopology.supremum_norm(v1)

print(f"Vector v1 = {v1}")
print(f"  Euclidean norm (L²): {euclidean_norm:.2f}")
print(f"  Taxicab norm (L¹): {taxicab_norm:.2f}")
print(f"  Supremum norm (L∞): {supremum_norm:.2f}")

# Vector arithmetic
sum_v = EuclideanTopology.vector_addition(v1, v2)
scaled = EuclideanTopology.scalar_multiplication(2, v1)
print(f"\nArithmetic:")
print(f"  v1 + v2 = {sum_v}")
print(f"  2 * v1 = {scaled}")

# Dot product
dot = EuclideanTopology.dot_product(v1, v2)
print(f"  v1 · v2 = {dot}")

# 3D operations
v1_3d = (1, 0, 0)
v2_3d = (0, 1, 0)

cross = EuclideanTopology.cross_product_3d(v1_3d, v2_3d)
print(f"\n3D Cross Product:")
print(f"  (1,0,0) × (0,1,0) = {cross}")

# Angle between vectors
space = EuclideanTopology(dimension=2)
angle_rad = space.angle_between(v1, v2)
angle_deg = math.degrees(angle_rad)
print(f"\nAngle between {v1} and {v2}:")
print(f"  Radians: {angle_rad:.4f}")
print(f"  Degrees: {angle_deg:.2f}°")
print()
```

---

## Example 10: Orthogonality & Orthonormalization

```python
print("="*60)
print("Example 10: Orthogonality & Gram-Schmidt")
print("="*60)

space = EuclideanTopology(dimension=3)

# Test orthogonality
v1 = (1, 0, 0)
v2 = (0, 1, 0)
v3 = (1, 1, 0)

print("Orthogonality tests:")
print(f"  (1,0,0) ⊥ (0,1,0)? {space.orthogonal(v1, v2)}")
print(f"  (1,0,0) ⊥ (1,1,0)? {space.orthogonal(v1, v3)}")

# Gram-Schmidt orthonormalization
vectors = [(1, 1, 0), (1, -1, 0), (0, 0, 1)]
print(f"\nOriginal vectors: {vectors}")

basis = space.orthonormal_basis(vectors)
print(f"Orthonormal basis:")
for i, v in enumerate(basis):
    norm = space.euclidean_norm(v)
    print(f"  e{i} = ({v[0]:.4f}, {v[1]:.4f}, {v[2]:.4f}) with norm {norm:.4f}")

# Verify orthogonality
if len(basis) >= 2:
    dot_product = space.dot_product(basis[0], basis[1])
    print(f"\nVerification: e0 · e1 = {dot_product:.10f} (should be ~0)")
print()
```

---

## Example 11: Continuity Testing

```python
print("="*60)
print("Example 11: Continuity of Functions")
print("="*60)

space = EuclideanTopology(dimension=1)

# Continuous function
def f_continuous(x):
    return x ** 2

# Discontinuous function (step function)
def f_discontinuous(x):
    return 1 if x > 0 else 0

domain = (0, 2, "closed")

is_cont_1 = space.is_continuous_function(f_continuous, domain)
is_cont_2 = space.is_continuous_function(f_discontinuous, domain)

print(f"f(x) = x²:")
print(f"  Is continuous on [0, 2]? {is_cont_1}")

print(f"\nf(x) = step function (1 if x>0, 0 otherwise):")
print(f"  Is continuous on [0, 2]? {is_cont_2}")

# Uniform continuity
is_unif = space.uniform_continuous(f_continuous, domain)
print(f"\nf(x) = x² is uniformly continuous on [0, 2]? {is_unif}")
print()
```

---

## Example 12: Complete Spatial Analysis

```python
print("="*60)
print("Example 12: Complete 2D Spatial Analysis")
print("="*60)

space = EuclideanTopology(dimension=2, bounds=(-10, 10))

# Point set
points = [(0, 0), (3, 4), (6, 0), (3, -4), (0, 0.1)]

print(f"Point set: {points}")

# Basic metrics
centroid = space.centroid(points)
print(f"Centroid: ({centroid[0]:.2f}, {centroid[1]:.2f})")

# Distance matrix
matrix = space.pairwise_distances_matrix(points)
print(f"\nDistance matrix (3x3 sample):")
for i in range(min(3, len(matrix))):
    print(f"  {[f'{matrix[i][j]:.2f}' for j in range(min(3, len(matrix[i])))]}")

# Convex hull
hull = space.convex_hull(points)
print(f"\nConvex hull vertices: {hull}")

# Diameter of convex hull
diameter = space.diameter(hull)
print(f"Diameter of convex hull: {diameter:.2f}")

# Connectivity analysis
p1, p2 = points[0], points[1]
path = space.path_from_to(p1, p2, steps=5)
print(f"\nPath from {p1} to {p2}:")
for p in path:
    print(f"  ({p[0]:.2f}, {p[1]:.2f})")

# Properties
props = space.metric_space()
print(f"\nMetric space properties:")
for key, value in props.items():
    print(f"  {key}: {value}")
print()
```

---

## Running These Examples

```python
# Save as euclidean_examples.py
# python euclidean_examples.py

# Import required
from euclidean_topology_extended import EuclideanTopology
import math
```

---

## Key Concepts Demonstrated

✅ Space initialization (1D, 2D, 3D)
✅ Distance metrics (Euclidean, Manhattan, Chebyshev)
✅ Ball operations (open, closed, spheres)
✅ Interval operations (union, intersection, membership)
✅ Convergence analysis
✅ Path connectivity
✅ Compactness (Heine-Borel theorem)
✅ Convexity and convex hulls
✅ Vector operations and norms
✅ Orthogonality and orthonormalization
✅ Continuity testing
✅ Spatial analysis and geometry

---