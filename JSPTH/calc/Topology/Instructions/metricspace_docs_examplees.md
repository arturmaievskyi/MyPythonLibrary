# Extended MetricSpace Documentation

## Overview

The expanded `MetricSpace` class provides 50+ methods for working with metric spaces, including:

- **Ball Operations** - Open/closed balls, spheres
- **Diameter & Radius** - Space properties and eccentricity
- **Nearest Neighbors** - k-NN, radius search, neighbor finding
- **Clustering** - Single/complete linkage hierarchical clustering
- **Statistical Measures** - Distance statistics, distributions
- **Geometric Operations** - Geodesics, midpoints, paths
- **Density Analysis** - Local density, outlier detection
- **Space Properties** - Connectivity, completeness, discreteness
- **Multiple Metrics** - 8 built-in distance metrics

---

## Core Class Methods

### Initialization & Setup

```python
from metric_space_extended import MetricSpace, euclidean_metric

# Create metric space
points = [(0,0), (1,0), (0,1), (1,1), (2,2)]
space = MetricSpace(points, euclidean_metric, name="2D Points")
```

---

## SECTION 1: Ball Operations

### open_ball(center, radius)
Find all points strictly within radius.

```python
ball = space.open_ball((0, 0), 1.5)
# Returns points where distance < 1.5
```

### closed_ball(center, radius)
Find all points within and on radius boundary.

```python
ball = space.closed_ball((0, 0), 1.5)
# Returns points where distance ≤ 1.5
```

### sphere(center, radius)
Find points exactly at distance radius.

```python
sphere = space.sphere((0, 0), 1.0)
# Returns points at exactly distance 1.0
```

---

## SECTION 2: Diameter & Radius Operations

### diameter(subset=None)
Maximum distance between any two points in space/subset.

```python
d = space.diameter()  # Full space: 3.61
d = space.diameter({(0,0), (1,0), (0,1)})  # Subset: 1.41
```

### radius(subset=None)
Minimum radius needed to cover all points with a single ball.

```python
r = space.radius()  # ~1.41 for this space
```

### center(subset=None)
Find center point(s) - minimizes maximum distance to others.

```python
centers = space.center()  # Returns list of center points
```

### eccentricity(point, subset=None)
Maximum distance from a point to any other point.

```python
ecc = space.eccentricity((0, 0))  # How far is farthest point?
```

### is_bounded(subset=None)
Check if space has finite diameter.

```python
bounded = space.is_bounded()  # True for finite spaces
```

---

## SECTION 3: Nearest Neighbor Operations

### nearest_neighbor(point)
Find single nearest neighbor.

```python
neighbor, distance = space.nearest_neighbor((0, 0))
# Returns: ((1, 0), 1.0)
```

### k_nearest_neighbors(point, k=1)
Find k nearest neighbors.

```python
neighbors = space.k_nearest_neighbors((0, 0), k=3)
# Returns: [((1,0), 1.0), ((0,1), 1.0), ((1,1), 1.41)]
```

### radius_search(point, radius)
Find all neighbors within radius.

```python
neighbors = space.radius_search((0, 0), radius=1.5)
# Returns points and distances, sorted by distance
```

---

## SECTION 4: Clustering

### single_linkage_clustering(n_clusters)
Hierarchical clustering using minimum distance between clusters.

```python
clusters = space.single_linkage_clustering(n_clusters=2)
# Returns: [cluster1, cluster2] as sets of points
```

**Properties:**
- Tends to find elongated clusters
- Sensitive to outliers
- Produces chain-like structures

### complete_linkage_clustering(n_clusters)
Hierarchical clustering using maximum distance between clusters.

```python
clusters = space.complete_linkage_clustering(n_clusters=2)
# More compact clusters than single linkage
```

**Properties:**
- Finds compact, roughly spherical clusters
- Robust to outliers
- More balanced cluster sizes

---

## SECTION 5: Statistical Measures

### average_distance(subset=None)
Mean distance between all pairs.

```python
avg = space.average_distance()  # Mean pairwise distance
```

### distance_variance(subset=None)
Variance of all pairwise distances.

```python
var = space.distance_variance()  # Spread of distances
```

### distance_standard_deviation(subset=None)
Standard deviation of distances.

```python
std = space.distance_standard_deviation()  # √variance
```

### pairwise_distances(subset=None)
Dictionary of all pairwise distances.

```python
dists = space.pairwise_distances()
# Returns: {(p1,p2): distance, (p1,p3): distance, ...}
```

### distance_matrix(subset=None)
N×N matrix of all distances.

```python
matrix = space.distance_matrix()
# Returns 2D list: matrix[i][j] = distance(points[i], points[j])
```

---

## SECTION 6: Geometric Operations

### midpoint(p1, p2)
Find point roughly halfway between two points.

```python
mid = space.midpoint((0, 0), (2, 2))
# For continuous spaces, returns actual midpoint
# For discrete spaces, returns closest point
```

### geodesic(p1, p2)
Find shortest path between two points through the space.

```python
path = space.geodesic((0, 0), (2, 2))
# Returns: [(0,0), (1,0), (1,1), (2,2)] etc.
```

### geodesic_distance(p1, p2)
Distance traveled along shortest path.

```python
dist = space.geodesic_distance((0, 0), (2, 2))
# May differ from direct metric distance in discrete spaces
```

---

## SECTION 7: Density & Outlier Detection

### local_density(point, radius)
Number of points within radius of a point.

```python
density = space.local_density((0, 0), radius=1.5)
# Count of neighbors (including self)
```

### density_distribution(radii)
Density for each point across multiple radii.

```python
distribution = space.density_distribution([0.5, 1.0, 1.5, 2.0])
# Returns: {point1: {0.5: count, 1.0: count, ...}, ...}
```

### outlier_score(point, k=5)
Score indicating how outlier-like a point is.

```python
score = space.outlier_score((2, 2), k=5)
# Higher score = more likely to be outlier
```

### detect_outliers(k=5, threshold=None)
Find outlier points using k-distance.

```python
outliers = space.detect_outliers(k=5)
# Returns points that are statistical outliers
```

---

## SECTION 8: Space Properties

### is_discrete(epsilon=1e-10)
Check if all points are far apart.

```python
discrete = space.is_discrete()  # All distances > epsilon?
```

### is_separable()
Check if space has countable dense subset (always True for finite spaces).

```python
separable = space.is_separable()  # True
```

### is_complete()
Check completeness (always True for finite metric spaces).

```python
complete = space.is_complete()  # True
```

### is_connected(max_distance=None)
Check if all points reachable from any point.

```python
connected = space.is_connected()  # True if one component
```

---

## SECTION 9: Utility Methods

### get_statistics(subset=None)
Get comprehensive statistics dictionary.

```python
stats = space.get_statistics()
# Returns: {
#   'num_points': 5,
#   'diameter': 3.61,
#   'radius': 1.41,
#   'center': [...],
#   'avg_distance': ...,
#   'distance_std': ...,
#   'is_bounded': True,
#   'is_discrete': True,
#   'is_connected': True,
# }
```

### print_statistics(subset=None)
Print formatted statistics.

```python
space.print_statistics()
# ==================================================
# Metric Space: 2D Points
# ==================================================
# Number of points: 5
# Diameter: 3.6056
# ...
```

### summary()
One-line space summary.

```python
print(space.summary())
# "2D Points: 5 points, diameter=3.61"
```

### distance(p1, p2)
Calculate distance with automatic caching.

```python
dist = space.distance((0, 0), (1, 1))  # Uses cache
```

### clear_cache()
Clear cached distances.

```python
space.clear_cache()  # Free memory
```

---

## SECTION 10: Distance Metrics (8 Total)

### euclidean_metric(p1, p2)
Standard Euclidean distance: √(Σ(xᵢ - yᵢ)²)

```python
from metric_space_extended import euclidean_metric
d = euclidean_metric((0,0), (3,4))  # 5.0
```

### manhattan_metric(p1, p2)
City-block distance: Σ|xᵢ - yᵢ|

```python
from metric_space_extended import manhattan_metric
d = manhattan_metric((0,0), (3,4))  # 7
```

### chebyshev_metric(p1, p2)
Maximum coordinate distance: max(|xᵢ - yᵢ|)

```python
from metric_space_extended import chebyshev_metric
d = chebyshev_metric((0,0), (3,4))  # 4
```

### minkowski_metric(p1, p2, p=2)
Generalized distance: (Σ|xᵢ - yᵢ|^p)^(1/p)

```python
from metric_space_extended import minkowski_metric
d = minkowski_metric((0,0), (3,4), p=1)   # Manhattan
d = minkowski_metric((0,0), (3,4), p=2)   # Euclidean
d = minkowski_metric((0,0), (3,4), p=float('inf'))  # Chebyshev
```

### hamming_metric(s1, s2)
String/sequence distance: count of differing positions

```python
from metric_space_extended import hamming_metric
d = hamming_metric("hello", "hallo")  # 1 (one different position)
```

### cosine_metric(v1, v2)
Cosine distance: 1 - cosine_similarity

```python
from metric_space_extended import cosine_metric
d = cosine_metric((1,0,1), (1,1,0))  # ~0.42
```

### jaccard_metric(set1, set2)
Set distance: 1 - Jaccard_similarity

```python
from metric_space_extended import jaccard_metric
d = jaccard_metric({1,2,3}, {2,3,4})  # 0.6
# (1 intersection, 5 union, 1 - 1/5 = 0.8)
```

### hausdorff_metric(set1, set2, metric)
Distance between sets: max(min distances)

```python
from metric_space_extended import hausdorff_metric
d = hausdorff_metric({(0,0)}, {(1,0), (0,1)})  # ~1.0
```

---

## Complete Usage Example

```python
from metric_space_extended import MetricSpace, euclidean_metric

# Create space with 10 random 2D points
import random
points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(10)]
space = MetricSpace(points, euclidean_metric, name="Random 2D")

# Basic analysis
print(space.summary())
space.print_statistics()

# Neighborhood queries
neighbors_3nn = space.k_nearest_neighbors(points[0], k=3)
print(f"3 nearest neighbors: {neighbors_3nn}")

# Clustering
clusters = space.complete_linkage_clustering(n_clusters=3)
print(f"3 clusters found: {[len(c) for c in clusters]}")

# Outlier detection
outliers = space.detect_outliers(k=3, threshold=5.0)
print(f"Outliers: {outliers}")

# Geometric analysis
path = space.geodesic(points[0], points[9])
print(f"Shortest path from point 0 to 9: {path}")

# Statistical summary
print(f"Average distance: {space.average_distance():.2f}")
print(f"Distance std dev: {space.distance_standard_deviation():.2f}")
print(f"Is connected: {space.is_connected()}")
```

---

## Performance Notes

- **Distance Caching**: Automatic caching avoids redundant calculations
- **Clustering O(n³)**: Complete linkage slower than single linkage
- **Geodesic O(n²)**: Uses Dijkstra-like algorithm
- **Statistics O(n²)**: All pairwise distances required

For 1000+ points, consider:
1. Using simpler metrics (Chebyshev vs Euclidean)
2. Pre-computing distance matrix
3. Using space partitioning trees (k-d tree, ball tree)
4. Sampling for approximate statistics

---

## Real-World Applications

| Task | Methods |
|------|---------|
| **Recommendation** | k_nearest_neighbors, radius_search |
| **Clustering** | single_linkage_clustering, complete_linkage_clustering |
| **Outlier Detection** | detect_outliers, outlier_score, local_density |
| **Routing** | geodesic, geodesic_distance |
| **Classification** | k_nearest_neighbors, connected_components |
| **Similarity Search** | radius_search, distance_matrix |
| **Data Analysis** | get_statistics, density_distribution |
| **Topology** | is_connected, connected_components |

---



# Extended MetricSpace - Working Examples

This file contains complete working examples demonstrating all major features of the expanded MetricSpace class.

---

## Example 1: Basic Metric Space Creation & Analysis

```python
from metric_space_extended import MetricSpace, euclidean_metric

print("="*60)
print("Example 1: Basic Metric Space Creation & Analysis")
print("="*60)

# Create a 2D metric space
points_2d = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)]
space = MetricSpace(points_2d, euclidean_metric, name="2D Square")

# Print basic info
print(space.summary())
space.print_statistics()

# Get specific properties
print(f"Diameter: {space.diameter():.2f}")
print(f"Radius: {space.radius():.2f}")
print(f"Center: {space.center()}")
print(f"Is bounded: {space.is_bounded()}")
print()
```

---

## Example 2: Ball Operations

```python
print("="*60)
print("Example 2: Ball Operations")
print("="*60)

# Create metric space
points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5), (3, 3)]
space = MetricSpace(points, euclidean_metric, name="Points with Ball")

center = (0.5, 0.5)
radius = 1.0

# Open ball (strictly within radius)
open_b = space.open_ball(center, radius)
print(f"Open ball B({center}, {radius}):")
print(f"  Points: {open_b}")
print(f"  Count: {len(open_b)}")

# Closed ball (within and on boundary)
closed_b = space.closed_ball(center, radius)
print(f"\nClosed ball B̄({center}, {radius}):")
print(f"  Points: {closed_b}")
print(f"  Count: {len(closed_b)}")

# Sphere (exactly at distance)
sphere = space.sphere(center, 0.5)
print(f"\nSphere S({center}, 0.5):")
print(f"  Points: {sphere}")
print()
```

---

## Example 3: Nearest Neighbor Queries

```python
print("="*60)
print("Example 3: Nearest Neighbor Queries")
print("="*60)

points = [(0, 0), (1, 0), (2, 0), (1, 1), (2, 2), (0, 5)]
space = MetricSpace(points, euclidean_metric, name="NN Example")

query_point = (1, 0)

# Single nearest neighbor
nearest, dist = space.nearest_neighbor(query_point)
print(f"Query point: {query_point}")
print(f"Nearest neighbor: {nearest} at distance {dist:.2f}")

# k-nearest neighbors
k = 3
neighbors = space.k_nearest_neighbors(query_point, k=k)
print(f"\n{k}-Nearest Neighbors:")
for i, (neighbor, distance) in enumerate(neighbors, 1):
    print(f"  {i}. {neighbor} - distance {distance:.2f}")

# Radius search
radius = 2.0
neighbors_in_radius = space.radius_search(query_point, radius)
print(f"\nPoints within radius {radius}:")
for neighbor, distance in neighbors_in_radius:
    print(f"  {neighbor} - distance {distance:.2f}")
print()
```

---

## Example 4: Hierarchical Clustering

```python
print("="*60)
print("Example 4: Hierarchical Clustering")
print("="*60)

# Create two clusters separated in space
cluster1 = [(0, 0), (1, 0), (0, 1), (1, 1)]
cluster2 = [(5, 5), (6, 5), (5, 6), (6, 6)]
points = cluster1 + cluster2

space = MetricSpace(points, euclidean_metric, name="Two Clusters")

# Single linkage clustering (minimum distance)
print("Single Linkage Clustering (finds elongated clusters):")
sl_clusters = space.single_linkage_clustering(n_clusters=2)
for i, cluster in enumerate(sl_clusters):
    print(f"  Cluster {i+1}: {cluster}")

# Complete linkage clustering (maximum distance)
print("\nComplete Linkage Clustering (finds compact clusters):")
cl_clusters = space.complete_linkage_clustering(n_clusters=2)
for i, cluster in enumerate(cl_clusters):
    print(f"  Cluster {i+1}: {cluster}")
print()
```

---

## Example 5: Distance Statistics

```python
print("="*60)
print("Example 5: Distance Statistics")
print("="*60)

points = [(0, 0), (1, 1), (2, 0), (1, -1), (3, 3)]
space = MetricSpace(points, euclidean_metric, name="Statistics Example")

# Basic statistics
avg_dist = space.average_distance()
std_dist = space.distance_standard_deviation()
var_dist = space.distance_variance()

print(f"Average pairwise distance: {avg_dist:.4f}")
print(f"Standard deviation: {std_dist:.4f}")
print(f"Variance: {var_dist:.4f}")

# Pairwise distances
print("\nAll pairwise distances:")
pairwise = space.pairwise_distances()
for (p1, p2), distance in sorted(pairwise.items(), key=lambda x: x[1])[:5]:
    print(f"  d({p1}, {p2}) = {distance:.4f}")

# Distance matrix
print("\nDistance matrix (first 3x3):")
matrix = space.distance_matrix()
for i in range(min(3, len(matrix))):
    print(f"  {[f'{matrix[i][j]:.2f}' for j in range(min(3, len(matrix[i])))]}")
print()
```

---

## Example 6: Geodesics & Paths

```python
print("="*60)
print("Example 6: Geodesics & Shortest Paths")
print("="*60)

# Create a grid of points
points = [(i, j) for i in range(4) for j in range(4)]
space = MetricSpace(points, euclidean_metric, name="Grid")

start = (0, 0)
end = (3, 3)

# Find geodesic (shortest path)
path = space.geodesic(start, end)
print(f"Shortest path from {start} to {end}:")
print(f"  Path: {' → '.join(str(p) for p in path)}")
print(f"  Length: {len(path)} steps")

# Geodesic distance
geo_dist = space.geodesic_distance(start, end)
direct_dist = space.distance(start, end)

print(f"\nGeodesic distance: {geo_dist:.2f}")
print(f"Direct distance: {direct_dist:.2f}")
print()
```

---

## Example 7: Density & Outlier Detection

```python
print("="*60)
print("Example 7: Density Analysis & Outlier Detection")
print("="*60)

# Points with one outlier
normal_points = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5)]
outlier_point = [(10, 10)]
points = normal_points + outlier_point

space = MetricSpace(points, euclidean_metric, name="Outlier Detection")

# Local density for each point
print("Local density (within radius 2.0):")
for point in points:
    density = space.local_density(point, radius=2.0)
    print(f"  {point}: {density} neighbors")

# Outlier scores
print("\nOutlier scores (k=3):")
for point in points:
    score = space.outlier_score(point, k=3)
    print(f"  {point}: {score:.2f}")

# Detect outliers
outliers = space.detect_outliers(k=3)
print(f"\nDetected outliers: {outliers}")

# Density distribution
print("\nDensity distribution across radii:")
distribution = space.density_distribution([1.0, 1.5, 2.0, 2.5])
for point in normal_points[:2]:  # Show first 2 points
    print(f"  {point}: {distribution[point]}")
print()
```

---

## Example 8: Space Connectivity

```python
print("="*60)
print("Example 8: Connected Components & Connectivity")
print("="*60)

# Two separate clusters
cluster1 = [(0, 0), (1, 0), (0, 1), (1, 1)]
cluster2 = [(5, 5), (6, 5), (5, 6), (6, 6)]
points = cluster1 + cluster2

space = MetricSpace(points, euclidean_metric, name="Two Separate Clusters")

# Check connectivity
is_connected = space.is_connected()
print(f"Is space connected: {is_connected}")

# Find connected components
components = space.connected_components()
print(f"Number of components: {len(components)}")
for i, component in enumerate(components):
    print(f"  Component {i+1}: {component}")

# Try with larger distance threshold
is_connected_large = space.is_connected(max_distance=10)
print(f"\nIs connected with max_distance=10: {is_connected_large}")
print()
```

---

## Example 9: Different Metrics Comparison

```python
from metric_space_extended import (
    euclidean_metric, manhattan_metric, chebyshev_metric,
    hamming_metric, cosine_metric, jaccard_metric
)

print("="*60)
print("Example 9: Different Metrics Comparison")
print("="*60)

# Coordinate space
p1 = (0, 0)
p2 = (3, 4)

print("Coordinate metrics for p1=(0,0), p2=(3,4):")
print(f"  Euclidean: {euclidean_metric(p1, p2):.2f}")
print(f"  Manhattan: {manhattan_metric(p1, p2):.2f}")
print(f"  Chebyshev: {chebyshev_metric(p1, p2):.2f}")

# String metric
s1 = "kitten"
s2 = "sitting"
print(f"\nHamming distance between '{s1}' and '{s2}':")
# (Note: strings have same length, show concept)
s1_short = "cat"
s2_short = "hat"
print(f"  '{s1_short}' vs '{s2_short}': {hamming_metric(s1_short, s2_short)}")

# Set metric
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nJaccard distance between {set1} and {set2}:")
print(f"  {jaccard_metric(set1, set2):.2f}")

# Vector metric
v1 = (1, 0, 1)
v2 = (1, 1, 0)
print(f"\nCosine distance between {v1} and {v2}:")
print(f"  {cosine_metric(v1, v2):.2f}")
print()
```

---

## Example 10: Complete Space Analysis

```python
print("="*60)
print("Example 10: Complete Space Analysis")
print("="*60)

# Create a random 3D point cloud
import random
random.seed(42)
points = [(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10))
          for _ in range(20)]

space = MetricSpace(points, euclidean_metric, name="3D Point Cloud")

# Get all statistics at once
stats = space.get_statistics()

print("Comprehensive Space Statistics:")
print(f"  Number of points: {stats['num_points']}")
print(f"  Diameter: {stats['diameter']:.2f}")
print(f"  Radius: {stats['radius']:.2f}")
print(f"  Center points: {stats['center']}")
print(f"  Average distance: {stats['avg_distance']:.2f}")
print(f"  Distance std dev: {stats['distance_std']:.2f}")
print(f"  Is bounded: {stats['is_bounded']}")
print(f"  Is discrete: {stats['is_discrete']}")
print(f"  Is connected: {stats['is_connected']}")

# Find some interesting points
print(f"\nMost eccentric point (farthest from others):")
eccentricities = [(p, space.eccentricity(p)) for p in points]
most_ecc = max(eccentricities, key=lambda x: x[1])
print(f"  {most_ecc[0]}: eccentricity {most_ecc[1]:.2f}")

print(f"\nLeast eccentric point (closest to all others):")
least_ecc = min(eccentricities, key=lambda x: x[1])
print(f"  {least_ecc[0]}: eccentricity {least_ecc[1]:.2f}")

# Outlier detection
outliers = space.detect_outliers(k=5)
print(f"\nDetected outliers (k=5, threshold=mean+2*std): {len(outliers)} points")
print()
```

---

## Example 11: Using Different Metrics on Same Data

```python
print("="*60)
print("Example 11: Metric Comparison on Same Dataset")
print("="*60)

from metric_space_extended import (
    euclidean_metric, manhattan_metric, chebyshev_metric
)

points = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)]

# Create spaces with different metrics
space_euclidean = MetricSpace(points, euclidean_metric, name="Euclidean")
space_manhattan = MetricSpace(points, manhattan_metric, name="Manhattan")
space_chebyshev = MetricSpace(points, chebyshev_metric, name="Chebyshev")

spaces = [space_euclidean, space_manhattan, space_chebyshev]

print("Comparison of metrics on the same point set:")
print(f"{'Metric':<15} {'Diameter':<12} {'Avg Distance':<15} {'Radius':<10}")
print("-" * 52)

for space in spaces:
    name = space.name
    diameter = space.diameter()
    avg_dist = space.average_distance()
    radius = space.radius()
    print(f"{name:<15} {diameter:<12.2f} {avg_dist:<15.2f} {radius:<10.2f}")

# Clustering with different metrics
print("\nClustering results with different metrics:")
for space in spaces:
    clusters = space.complete_linkage_clustering(n_clusters=2)
    sizes = [len(c) for c in clusters]
    print(f"  {space.name}: {sizes}")
print()
```

---

## Example 12: Performance & Caching

```python
import time

print("="*60)
print("Example 12: Performance & Caching Demonstration")
print("="*60)

import random
random.seed(42)

# Create larger point set
points = [(random.uniform(0, 100), random.uniform(0, 100))
          for _ in range(50)]

space = MetricSpace(points, euclidean_metric, name="Performance Test")

# First call (cache miss)
start = time.time()
dist1 = space.distance(points[0], points[1])
time1 = time.time() - start

# Second call (cache hit)
start = time.time()
dist2 = space.distance(points[0], points[1])
time2 = time.time() - start

print(f"First distance calculation (cache miss): {time1*1000:.3f} ms")
print(f"Second distance calculation (cache hit): {time2*1000:.3f} ms")
print(f"Speedup: {time1/time2:.1f}x")

print(f"\nCache size: {len(space._distance_cache)} entries")

# Clear cache
space.clear_cache()
print(f"After clear_cache(): {len(space._distance_cache)} entries")
print()
```

---

## Running These Examples

```python
# Save as metric_space_examples.py
# Then run: python metric_space_examples.py

# Or run individual examples by copying/pasting
# Don't forget to import:
from metric_space_extended import MetricSpace, euclidean_metric
```

---

## Summary of Methods Demonstrated

- ✅ Ball operations (open_ball, closed_ball, sphere)
- ✅ Neighbor queries (nearest_neighbor, k_nearest_neighbors, radius_search)
- ✅ Clustering (single_linkage, complete_linkage)
- ✅ Statistics (average_distance, variance, std_dev)
- ✅ Paths (geodesic, geodesic_distance)
- ✅ Density (local_density, density_distribution)
- ✅ Outliers (outlier_score, detect_outliers)
- ✅ Connectivity (is_connected, connected_components)
- ✅ Multiple metrics (euclidean, manhattan, chebyshev, etc.)
- ✅ Space properties (diameter, radius, center, eccentricity)
- ✅ Statistics (get_statistics, print_statistics)

---