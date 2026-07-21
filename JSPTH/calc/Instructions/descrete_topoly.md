# DiscreteTopology - Comprehensive Documentation

## Overview

The **DiscreteTopology** class provides a complete implementation of the discrete topology on finite or countable sets. In the discrete topology, **every subset is open (and closed)**, making it the finest possible topology.

### Key Properties
- Every point is isolated
- All subsets are both open and closed
- Compact iff finite
- Not connected (unless single point)
- Hausdorff separable
- Metrizable by discrete metric

---

## Initialization

```python
from discrete_topology_extended import DiscreteTopology

# Create discrete topology on finite set
space = DiscreteTopology({1, 2, 3, 4, 5}, name="Numbers")

# Create on strings
space = DiscreteTopology(['a', 'b', 'c', 'd'])

# Custom metric (if desired)
def custom_metric(x, y):
    return 0 if x == y else 1

space = DiscreteTopology({1, 2, 3}, metric=custom_metric)
```

---

## Basic Properties

### Check Properties
```python
# All subsets are open and closed
is_open = space.is_open_set({1, 2})  # True
is_closed = space.is_closed_set({1, 2})  # True

# All points are isolated
is_isolated = space.is_isolated_point(1)  # True

# Get all properties
props = space.get_properties()
space.print_properties()
```

### Output
```
============================================================
Discrete Topology: Numbers
============================================================
name: Numbers
is_discrete: True
is_connected: False
is_hausdorff: True
is_metrizable: True
is_separable: True
is_compact: True
number_of_points: 5
number_of_open_sets: 32  (2^5 = 32)
all_sets_open_and_closed: True
============================================================
```

---

## Distance Operations

### Discrete Metric
```python
# Default: discrete metric
d = space.distance(1, 2)  # 1 (different points)
d = space.distance(1, 1)  # 0 (same point)
```

The discrete metric is:
```
d(x, y) = 0 if x = y
        = 1 if x ≠ y
```

### Distance Matrix
```python
matrix, elements = space.distance_matrix()
# Returns n×n matrix and ordered elements
```

### Distances from Point
```python
distances = space.distances_from(1)
# Returns {1: 0, 2: 1, 3: 1, 4: 1, 5: 1}
```

### Diameter & Radius
```python
d = space.diameter()  # 1 (max distance between any points)
r = space.radius()    # 1 (min radius needed to cover)

centers = space.center()  # Points minimizing eccentricity

ecc = space.eccentricity(1)  # Max distance from point 1 to others
```

---

## Neighborhood Operations

### Neighborhoods
```python
# All open sets containing a point
neighborhoods = space.neighborhood(1)
# Returns list of all open sets containing 1

# Singleton neighborhood (basic neighborhood)
singleton = space.singleton_neighborhood(1)  # {1}
```

### Nearest Neighbors
```python
# In discrete metric, all others are at distance 1
neighbors = space.nearest_neighbors(1, k=3)
# Returns 3 closest neighbors: [(2,1), (3,1), (4,1)]

# All neighbors within radius
nearby = space.radius_search(1, radius=1.0)
# With discrete metric, returns all other points
```

---

## Connectivity

### Connected Components
```python
# In discrete metric with threshold 1.0:
# With threshold < 1: each point is separate
components_sep = space.connected_components(max_distance=0.5)
# Returns: [{1}, {2}, {3}, {4}, {5}]

# With threshold >= 1: all points together
components_all = space.connected_components(max_distance=1.0)
# Returns: [{1, 2, 3, 4, 5}]
```

### Path Finding
```python
# Shortest path between points
path = space.shortest_path(1, 5)
# Returns [1, 2, 3, 4, 5] or some permutation

# Check path connectivity
connected = space.is_path_connected()  # False (unless single point)
```

---

## Compactness

### Compact Sets
```python
# All finite subsets are compact
is_compact = space.is_compact()  # True
is_compact_sub = space.is_compact({1, 2, 3})  # True

# Always bounded
is_bounded = space.is_bounded()  # True
```

---

## Open & Closed Sets

### Set Operations
```python
# Interior, closure, boundary in discrete topology
interior = space.interior({1, 2, 3})  # {1, 2, 3}
closure = space.closure({1, 2, 3})    # {1, 2, 3}
boundary = space.boundary({1, 2, 3})  # set() (empty)

# Derived set (limit points): always empty
derived = space.derived_set({1, 2, 3})  # set() (no limit points)
```

---

## Hausdorff & Separation

### Separation
```python
# Discrete topology is always Hausdorff
is_hausdorff = space.is_hausdorff()  # True

# Singleton neighborhoods separate points
nbhd_1, nbhd_2 = space.separating_neighborhoods(1, 2)
# Returns ({1}, {2}) - disjoint singleton neighborhoods
```

---

## Graph Structure

### Complete Graph
```python
# Discrete space viewed as complete graph
graph = space.as_complete_graph()
# Returns:
# {
#     'vertices': {1, 2, 3, 4, 5},
#     'edges': {(1,2), (1,3), ..., (4,5)},
#     'is_complete': True,
#     'number_of_edges': 10  (5 choose 2)
# }
```

### Graph with Distance Threshold
```python
# Points connected if within distance threshold
graph = space.as_graph_with_threshold(threshold=1.0)
# With discrete metric: complete graph

graph = space.as_graph_with_threshold(threshold=0.5)
# With threshold < 1: no edges (no points within distance)
```

### Adjacency Matrix
```python
matrix, elements = space.adjacency_matrix(threshold=1.0)
# Returns adjacency matrix and ordered elements
```

---

## Degree & Clustering

### Degree
```python
# Number of neighbors within threshold
degree = space.degree(1, threshold=1.0)  # 4 (all others)

# Average degree
avg_degree = space.average_degree(threshold=1.0)  # 4.0
```

### Clustering Coefficient
```python
# Local clustering: how many neighbors are connected
coeff = space.clustering_coefficient(1, threshold=1.0)
# With discrete metric and threshold 1: 1.0 (all neighbors connected)

# Average clustering
avg_coeff = space.average_clustering_coefficient(threshold=1.0)

# Global clustering (transitivity)
trans = space.transitivity(threshold=1.0)
# Proportion of triangles to connected triples
```

---

## Statistical Properties

### Distance Statistics
```python
# Average distance between all pairs
avg = space.average_distance()

# Distribution of distances
dist_dist = space.distance_distribution()
# With discrete metric: {0: 0, 1: n(n-1)/2}
# (0 distance only for same points, 1 for all pairs)

# All pairwise distances
distances = space.pairwise_distances()
# Returns dict: {(x,y): distance}
```

---

## Metric Properties

### Verify Metric
```python
# Check if metric satisfies axioms
is_metric = space.is_metric_space()  # True

# Get metric properties
props = space.metric_properties()
# {
#     'is_metric': True,
#     'is_complete': True,
#     'is_separable': True,
#     'is_totally_bounded': True,
# }
```

---

## Cardinality

### Size & Countability
```python
# Number of points
size = space.cardinality()  # 5

# Is finite?
is_finite = space.is_finite()  # True

# Is countable?
is_countable = space.is_countable()  # True

# Number of open sets (power set size)
num_opens = len(space.open_sets)  # 2^5 = 32
```

---

## Subspaces

### Create Subspace
```python
# Discrete subspace of discrete space
subspace = space.subspace({1, 2, 3})
# Is also discrete topology on {1, 2, 3}

# Check subspace relationship
is_sub = subspace.is_subspace_of(space)  # True
```

---

## Homeomorphism & Isometry

### Topological Equivalence
```python
other_space = DiscreteTopology({1, 2, 3, 4, 5})

# Same cardinality means homeomorphic
is_homeo = space.is_homeomorphic_to(other_space)  # True

# For discrete metric spaces: isometric iff same cardinality
is_iso = space.is_isometric_to(other_space)  # True
```

---

## Partitions

### Partition by Distance
```python
# Partition points based on distance threshold
# With threshold 0.5: each point separate
parts = space.partition_by_distance(0.5)
# Returns: [{1}, {2}, {3}, {4}, {5}]

# With threshold 1.0: all together
parts = space.partition_by_distance(1.0)
# Returns: [{1, 2, 3, 4, 5}]
```

---

## Output & Export

### Summary
```python
# One-line summary
summary = space.summary()
# "Discrete Topology: Numbers with 5 points"

# Detailed description
desc = space.describe()
# Formatted output with all properties

# Export to dictionary
data = space.export_to_dict()
```

---

## Complete Example

```python
from discrete_topology_extended import DiscreteTopology

# Create space
space = DiscreteTopology({1, 2, 3, 4}, name="Example")

print(space.describe())

# Graph structure
graph = space.as_complete_graph()
print(f"Complete graph: {len(graph['edges'])} edges")

# Clustering
for point in space.base_set:
    coeff = space.clustering_coefficient(point, threshold=1.0)
    print(f"Point {point}: clustering coefficient = {coeff:.2f}")

# Distance distribution
dist_dist = space.distance_distribution()
print(f"Distance distribution: {dist_dist}")

# Matrix representation
matrix, elements = space.distance_matrix()
print(f"Distance matrix:")
for row in matrix:
    print(f"  {row}")
```

---

## Method Count by Category

| Category | Methods | Count |
|----------|---------|-------|
| Basic Properties | is_open_set, is_closed_set, is_isolated_point, etc. | 4 |
| Distance Operations | distance, diameter, radius, center, eccentricity | 7 |
| Neighborhoods | neighborhood, nearest_neighbors, radius_search | 4 |
| Connectivity | connected_components, is_connected, shortest_path | 4 |
| Compactness | is_compact, is_bounded | 2 |
| Open & Closed Sets | interior, closure, boundary, derived_set | 4 |
| Hausdorff | is_hausdorff, separating_neighborhoods | 2 |
| Graph Structure | as_complete_graph, adjacency_matrix, degree | 4 |
| Clustering | clustering_coefficient, transitivity, average_degree | 5 |
| Statistics | average_distance, distance_distribution, pairwise_distances | 3 |
| Metric Properties | is_metric_space, metric_properties | 2 |
| Cardinality | cardinality, is_finite, is_countable | 3 |
| Subspaces | subspace, is_subspace_of | 2 |
| Equivalence | is_homeomorphic_to, is_isometric_to | 2 |
| Partitions | partition_by_distance | 1 |
| Export | summary, describe, export_to_dict | 3 |

**Total: 50+ Methods**

---

## Key Theorems

### Finite Discrete Topology
- Finite discrete spaces are **compact**
- Every point is **isolated**
- Space is **Hausdorff**
- Every subset is **open and closed**

### Metric
- Discrete metric: d(x,y) = 0 if x=y, else 1
- Induces discrete topology
- All finite metric spaces complete

### Connectivity
- Not connected (unless single point)
- Each point is connected component
- Totally disconnected

---

## Applications

| Domain | Use Case |
|--------|----------|
| **Graph Theory** | Represent as complete graph |
| **Data Science** | All points equally important |
| **Clustering** | Simplest case: no clustering |
| **Networks** | Fully connected network |
| **Computer Science** | Discrete state spaces |

---

# DiscreteTopology - Working Examples

Complete working examples demonstrating all features.

---

## Example 1: Basic Setup & Properties

```python
from discrete_topology_extended import DiscreteTopology

print("="*60)
print("Example 1: Basic Setup & Properties")
print("="*60)

# Create discrete topologies
space_numbers = DiscreteTopology({1, 2, 3, 4, 5}, name="Numbers")
space_letters = DiscreteTopology(['a', 'b', 'c', 'd'], name="Letters")

print(space_numbers.summary())
print(space_letters.summary())

# Print detailed properties
space_numbers.print_properties()

# Check basic properties
print(f"Is {1, 2, 3} open? {space_numbers.is_open_set({1, 2, 3})}")
print(f"Is {1, 2, 3} closed? {space_numbers.is_closed_set({1, 2, 3})}")
print(f"Is all subsets open and closed? True (discrete topology)")
print()
```

---

## Example 2: Distance Metrics

```python
print("="*60)
print("Example 2: Discrete Metric")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4})

# Distances
print("Distances from point 1:")
distances = space.distances_from(1)
for point, dist in sorted(distances.items()):
    print(f"  d(1, {point}) = {dist}")

print("\nDistance matrix:")
matrix, elements = space.distance_matrix()
print(f"Elements: {elements}")
for i, row in enumerate(matrix):
    print(f"  {elements[i]}: {row}")

# Diameter and radius
print(f"\nDiameter: {space.diameter()}")
print(f"Radius: {space.radius()}")
print(f"Center points: {space.center()}")
print()
```

---

## Example 3: Neighborhoods

```python
print("="*60)
print("Example 3: Neighborhoods")
print("="*60)

space = DiscreteTopology({1, 2, 3})

# Neighborhoods of point 1
neighborhoods = space.neighborhood(1)
print(f"Neighborhoods of 1: {len(neighborhoods)} total")
for nbhd in neighborhoods:
    print(f"  {nbhd}")

# Singleton neighborhood
singleton = space.singleton_neighborhood(1)
print(f"\nSingleton neighborhood of 1: {singleton}")

# Nearest neighbors
neighbors = space.nearest_neighbors(1, k=2)
print(f"\n2-nearest neighbors of 1: {neighbors}")

# Radius search
nearby = space.radius_search(1, radius=1.0)
print(f"\nPoints within radius 1.0 of 1: {nearby}")
print()
```

---

## Example 4: Connectivity & Components

```python
print("="*60)
print("Example 4: Connectivity & Connected Components")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4, 5})

# Overall connectivity
is_connected = space.is_connected()
print(f"Is entire space connected? {is_connected}")

# Connected components with different thresholds
print("\nConnected components with threshold = 0.5:")
components_sep = space.connected_components(max_distance=0.5)
for i, comp in enumerate(components_sep):
    print(f"  Component {i+1}: {comp}")

print("\nConnected components with threshold = 1.0:")
components_all = space.connected_components(max_distance=1.0)
for i, comp in enumerate(components_all):
    print(f"  Component {i+1}: {comp}")

# Shortest path
print("\nShortest paths:")
path = space.shortest_path(1, 5)
print(f"  From 1 to 5: {path}")
print()
```

---

## Example 5: Graph Structure

```python
print("="*60)
print("Example 5: Graph Representation")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4})

# As complete graph
graph = space.as_complete_graph()
print(f"Complete graph:")
print(f"  Vertices: {len(graph['vertices'])}")
print(f"  Edges: {len(graph['edges'])}")
print(f"  Is complete? {graph['is_complete']}")

# With distance threshold
graph_thresh = space.as_graph_with_threshold(threshold=1.0)
print(f"\nGraph with threshold 1.0:")
print(f"  Edges: {len(graph_thresh['edges'])}")

# Adjacency matrix
matrix, elements = space.adjacency_matrix(threshold=1.0)
print(f"\nAdjacency matrix:")
for i, row in enumerate(matrix):
    print(f"  {elements[i]}: {row}")
print()
```

---

## Example 6: Degree & Clustering

```python
print("="*60)
print("Example 6: Degree & Clustering Analysis")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4, 5})

# Degrees
print("Degrees (with threshold 1.0):")
for point in space.base_set:
    degree = space.degree(point, threshold=1.0)
    print(f"  Point {point}: degree = {degree}")

print(f"\nAverage degree: {space.average_degree(threshold=1.0):.2f}")

# Clustering coefficients
print("\nLocal clustering coefficients:")
for point in space.base_set:
    coeff = space.clustering_coefficient(point, threshold=1.0)
    print(f"  Point {point}: {coeff:.2f}")

print(f"\nAverage clustering coefficient: {space.average_clustering_coefficient(threshold=1.0):.2f}")
print(f"Transitivity (global clustering): {space.transitivity(threshold=1.0):.2f}")
print()
```

---

## Example 7: Statistical Properties

```python
print("="*60)
print("Example 7: Distance Statistics")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4, 5})

# Average distance
avg = space.average_distance()
print(f"Average pairwise distance: {avg:.2f}")

# Distance distribution
dist_dist = space.distance_distribution()
print(f"\nDistance distribution:")
for dist, count in sorted(dist_dist.items()):
    print(f"  Distance {dist}: {count} pairs")

# Pairwise distances
print(f"\nAll pairwise distances:")
pairwise = space.pairwise_distances()
for (x, y), dist in sorted(pairwise.items())[:5]:
    print(f"  d({x}, {y}) = {dist}")
print(f"  ... and {len(pairwise) - 5} more")
print()
```

---

## Example 8: Compactness & Boundedness

```python
print("="*60)
print("Example 8: Compactness & Boundedness")
print("="*60)

space_finite = DiscreteTopology({1, 2, 3, 4})

# Compactness
is_compact = space_finite.is_compact()
print(f"Is finite discrete space compact? {is_compact}")

# Bounded
is_bounded = space_finite.is_bounded()
print(f"Is space bounded? {is_bounded}")

# Subsets
subset = {1, 2}
is_compact_sub = space_finite.is_compact(subset)
print(f"Is {subset} compact? {is_compact_sub}")

print("\nKey fact: All finite discrete spaces are compact!")
print()
```

---

## Example 9: Hausdorff Separation

```python
print("="*60)
print("Example 9: Hausdorff Separation")
print("="*60)

space = DiscreteTopology({1, 2, 3})

# Hausdorff property
is_hausdorff = space.is_hausdorff()
print(f"Is space Hausdorff? {is_hausdorff}")

# Separating neighborhoods
nbhd_1, nbhd_2 = space.separating_neighborhoods(1, 2)
print(f"\nSeparating neighborhoods for 1 and 2:")
print(f"  For point 1: {nbhd_1}")
print(f"  For point 2: {nbhd_2}")
print(f"  Disjoint? {len(nbhd_1 & nbhd_2) == 0}")

for x in [1, 2]:
    for y in [2, 3]:
        if x != y:
            n1, n2 = space.separating_neighborhoods(x, y)
            print(f"  Points {x},{y}: {n1} and {n2} (disjoint: {len(n1 & n2) == 0})")
print()
```

---

## Example 10: Open & Closed Sets

```python
print("="*60)
print("Example 10: Open & Closed Sets in Discrete Topology")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4})

subset = {1, 2}

# Open and closed
is_open = space.is_open_set(subset)
is_closed = space.is_closed_set(subset)
print(f"Is {subset} open? {is_open}")
print(f"Is {subset} closed? {is_closed}")

# Interior, closure, boundary
interior = space.interior(subset)
closure = space.closure(subset)
boundary = space.boundary(subset)

print(f"\nSet operations for {subset}:")
print(f"  Interior: {interior}")
print(f"  Closure: {closure}")
print(f"  Boundary: {boundary}")

# Derived set (limit points)
derived = space.derived_set(subset)
print(f"  Derived set (limit points): {derived}")

print("\nKey fact: In discrete topology:")
print("  Interior = Closure = the set itself")
print("  Boundary = empty set")
print("  No limit points (every point is isolated)")
print()
```

---

## Example 11: Subspaces

```python
print("="*60)
print("Example 11: Subspaces")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4, 5})

# Create subspace
subspace = space.subspace({1, 2, 3})
print(f"Original space: {space.summary()}")
print(f"Subspace: {subspace.summary()}")

# Check subspace relationship
is_sub = subspace.is_subspace_of(space)
print(f"\nIs subspace of original? {is_sub}")

# Subspace is also discrete
print(f"Is subspace discrete? {subspace.get_properties()['is_discrete']}")
print()
```

---

## Example 12: Homeomorphism & Isometry

```python
print("="*60)
print("Example 12: Homeomorphism & Isometry")
print("="*60)

space1 = DiscreteTopology({1, 2, 3, 4})
space2 = DiscreteTopology(['a', 'b', 'c', 'd'])
space3 = DiscreteTopology({1, 2, 3})

# Homeomorphic (same cardinality)
homo_12 = space1.is_homeomorphic_to(space2)
homo_13 = space1.is_homeomorphic_to(space3)

print(f"Space1 (4 points) homeomorphic to Space2 (4 points)? {homo_12}")
print(f"Space1 (4 points) homeomorphic to Space3 (3 points)? {homo_13}")

# Isometric (same cardinality for discrete metric)
iso_12 = space1.is_isometric_to(space2)
iso_13 = space1.is_isometric_to(space3)

print(f"\nSpace1 isometric to Space2? {iso_12}")
print(f"Space1 isometric to Space3? {iso_13}")

print("\nKey fact: Discrete spaces are determined by cardinality")
print("  Same size → homeomorphic")
print("  Same size → isometric (for discrete metric)")
print()
```

---

## Example 13: Partitions

```python
print("="*60)
print("Example 13: Partitioning by Distance")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4, 5})

# With small threshold: each point separate
parts_small = space.partition_by_distance(0.5)
print(f"Partition with threshold 0.5:")
for i, part in enumerate(parts_small):
    print(f"  Partition {i+1}: {part}")

# With large threshold: all together
parts_large = space.partition_by_distance(1.5)
print(f"\nPartition with threshold 1.5:")
for i, part in enumerate(parts_large):
    print(f"  Partition {i+1}: {part}")
print()
```

---

## Example 14: Metric Verification

```python
print("="*60)
print("Example 14: Metric Properties")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4})

# Verify metric
is_metric = space.is_metric_space()
print(f"Is discrete metric a valid metric? {is_metric}")

# Metric properties
props = space.metric_properties()
print(f"\nMetric properties:")
for key, value in props.items():
    print(f"  {key}: {value}")

# Show metric axioms
print(f"\nDiscrete metric satisfies:")
print(f"  ✓ Non-negativity: d(x,y) ≥ 0")
print(f"  ✓ Identity: d(x,x) = 0, d(x,y) > 0 for x ≠ y")
print(f"  ✓ Symmetry: d(x,y) = d(y,x)")
print(f"  ✓ Triangle inequality: d(x,z) ≤ d(x,y) + d(y,z)")
print()
```

---

## Example 15: Complete Analysis

```python
print("="*60)
print("Example 15: Complete Space Analysis")
print("="*60)

space = DiscreteTopology({1, 2, 3, 4, 5}, name="Analysis Example")

# Full description
print(space.describe())

# Cardinality
print(f"Cardinality: {space.cardinality()}")
print(f"Is finite? {space.is_finite()}")
print(f"Is countable? {space.is_countable()}")
print(f"Number of open sets: {len(space.open_sets)} (2^{space.cardinality()})")

# Export
data = space.export_to_dict()
print(f"\nExported data:")
for key, value in data.items():
    if key != 'base_set':
        print(f"  {key}: {value}")
print()
```

---

## Running These Examples

```python
# Save as discrete_topology_examples.py
# python discrete_topology_examples.py

from discrete_topology_extended import DiscreteTopology
```

---

## Key Insights from Examples

1. **Every subset is open and closed** - fundamental property
2. **Distance is trivial** - only 0 and 1
3. **All points are isolated** - no limit points
4. **Finite implies compact** - always true
5. **Not connected** - unless single point
6. **Complete graph structure** - every point connects to every other
7. **Hausdorff separation** - always satisfies
8. **Cardinality determines everything** - homeomorphic iff same size
9. **Metric properties satisfied** - discrete metric is valid
10. **High clustering** - complete connectivity

---