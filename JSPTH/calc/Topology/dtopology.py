from .topology_imports import *

class DiscreteTopology(Topology):
    """
    The discrete topology on a finite or countable set.
    
    Properties:
    - Every subset is open (and closed)
    - Finest possible topology
    - Every point is isolated
    - Separable (every point is a neighborhood of itself)
    - Metrizable by the discrete metric
    - Hausdorff (T2 separation)
    - Not connected (unless single point)
    - Compact iff finite
    
    Discrete Metric:
    d(x, y) = 0 if x = y, else 1
    """

    def __init__(self, base_set, metric=None, name="DiscreteTopology"):
        """
        Initialize discrete topology.
        
        :param base_set: The underlying set (finite or countable)
        :param metric: Optional custom metric (defaults to discrete metric)
        :param name: Name for the space
        """
        self.base_set = set(base_set) if not isinstance(base_set, set) else base_set
        self.name = name
        self.size = len(self.base_set)
        
        # Use discrete metric by default
        if metric is None:
            self.metric = self._discrete_metric
        else:
            self.metric = metric
        
        # Generate all open sets (power set)
        self.open_sets = self._generate_power_set()
        self.closed_sets = self.open_sets.copy()  # In discrete topology, every set is both open and closed

    def _discrete_metric(self, x, y):
        """The discrete metric: d(x,y) = 0 if x=y, else 1"""
        return 0 if x == y else 1

    def _generate_power_set(self):
        """Generate all subsets of the base set (power set)."""
        elements = list(self.base_set)
        power_set = [set()]  # Empty set
        
        for r in range(1, len(elements) + 1):
            for combo in combinations(elements, r):
                power_set.append(set(combo))
        
        return power_set

    # ===== BASIC PROPERTIES =====

    def is_open_set(self, subset):
        """Check if subset is open (all subsets are open in discrete topology)."""
        return set(subset) in self.open_sets

    def is_closed_set(self, subset):
        """Check if subset is closed (all subsets are closed in discrete topology)."""
        return set(subset) in self.closed_sets

    def is_isolated_point(self, point):
        """Check if point is isolated (all points are isolated in discrete topology)."""
        return point in self.base_set

    def isolated_points(self):
        """Get all isolated points (all points in discrete topology)."""
        return list(self.base_set)

    def get_properties(self):
        """Get all topological properties of discrete topology."""
        return {
            'name': self.name,
            'is_discrete': True,
            'is_connected': self.size <= 1,  # Only single point is connected
            'is_hausdorff': True,  # Every point has disjoint neighborhood
            'is_metrizable': True,  # By discrete metric
            'is_separable': True,  # Every singleton is open
            'is_compact': self.size < float('inf'),  # Finite spaces are compact
            'number_of_points': self.size,
            'number_of_open_sets': len(self.open_sets),
            'all_sets_open_and_closed': True,
        }

    def print_properties(self):
        """Print space properties."""
        props = self.get_properties()
        print(f"\n{'='*60}")
        print(f"Discrete Topology: {self.name}")
        print(f"{'='*60}")
        for key, value in props.items():
            print(f"{key}: {value}")
        print(f"{'='*60}\n")

    # ===== DISTANCE OPERATIONS =====

    def distance(self, x, y):
        """Calculate distance between two points."""
        if x not in self.base_set or y not in self.base_set:
            raise ValueError(f"Points must be in base set")
        return self.metric(x, y)

    def distances_from(self, point):
        """Get distances from a point to all others."""
        distances = {}
        for other in self.base_set:
            distances[other] = self.distance(point, other)
        return distances

    def distance_matrix(self):
        """Get complete distance matrix."""
        elements = sorted(self.base_set, key=str)
        n = len(elements)
        matrix = [[0] * n for _ in range(n)]
        
        for i, x in enumerate(elements):
            for j, y in enumerate(elements):
                matrix[i][j] = self.distance(x, y)
        
        return matrix, elements

    def diameter(self, subset=None):
        """Diameter: maximum distance between any two points."""
        if subset is None:
            subset = self.base_set
        
        subset = set(subset)
        if len(subset) <= 1:
            return 0
        
        max_dist = 0
        for x in subset:
            for y in subset:
                dist = self.distance(x, y)
                if dist > max_dist:
                    max_dist = dist
        
        return max_dist

    def radius(self, subset=None):
        """Radius: minimum eccentricity of any point."""
        if subset is None:
            subset = self.base_set
        
        subset = set(subset)
        if len(subset) == 0:
            return 0
        
        min_ecc = float('inf')
        for center in subset:
            max_dist = 0
            for point in subset:
                dist = self.distance(center, point)
                if dist > max_dist:
                    max_dist = dist
            if max_dist < min_ecc:
                min_ecc = max_dist
        
        return min_ecc

    def center(self, subset=None):
        """Find center point(s) minimizing eccentricity."""
        if subset is None:
            subset = self.base_set
        
        subset = set(subset)
        if len(subset) == 0:
            return []
        
        rad = self.radius(subset)
        centers = []
        
        for point in subset:
            max_dist = max(self.distance(point, other) for other in subset)
            if abs(max_dist - rad) < 1e-10:
                centers.append(point)
        
        return centers

    def eccentricity(self, point, subset=None):
        """Maximum distance from point to any other point."""
        if subset is None:
            subset = self.base_set
        
        subset = set(subset)
        max_dist = 0
        
        for other in subset:
            if other != point:
                dist = self.distance(point, other)
                if dist > max_dist:
                    max_dist = dist
        
        return max_dist

    # ===== NEIGHBORHOOD OPERATIONS =====

    def neighborhood(self, point):
        """Get all neighborhoods (open sets containing point)."""
        neighborhoods = []
        for open_set in self.open_sets:
            if point in open_set:
                neighborhoods.append(open_set)
        return neighborhoods

    def singleton_neighborhood(self, point):
        """Singleton neighborhood: {point}."""
        return {point}

    def nearest_neighbors(self, point, k=1):
        """Find k nearest neighbors."""
        if point not in self.base_set:
            raise ValueError(f"Point {point} not in base set")
        
        distances = []
        for other in self.base_set:
            if other != point:
                dist = self.distance(point, other)
                distances.append((other, dist))
        
        distances.sort(key=lambda x: x[1])
        return distances[:min(k, len(distances))]

    def radius_search(self, point, radius):
        """Find all points within radius."""
        neighbors = []
        for other in self.base_set:
            if other != point:
                if self.distance(point, other) <= radius:
                    neighbors.append((other, self.distance(point, other)))
        
        neighbors.sort(key=lambda x: x[1])
        return neighbors

    # ===== CONNECTIVITY & COMPONENTS =====

    def is_connected(self):
        """Check if space is connected."""
        # Discrete topology: only single point is connected
        return self.size <= 1

    def connected_components(self, max_distance=None):
        """
        Find connected components.
        In discrete topology with discrete metric: each point is a component.
        """
        if max_distance is None:
            # With discrete metric, only connected if max_distance >= 1
            max_distance = 1.0
        
        if max_distance < 1.0:
            # Each point is its own component
            return [{point} for point in self.base_set]
        else:
            # All points in single component
            return [self.base_set]

    def is_path_connected(self):
        """Check if space is path-connected."""
        # Discrete space: not path-connected unless single point
        return self.size <= 1

    def shortest_path(self, start, end):
        """Find shortest path between two points (in graph sense)."""
        if start == end:
            return [start]
        
        if start not in self.base_set or end not in self.base_set:
            raise ValueError("Points must be in base set")
        
        # BFS to find shortest path
        visited = {start}
        queue = deque([(start, [start])])
        
        while queue:
            current, path = queue.popleft()
            
            if current == end:
                return path
            
            # In discrete topology, neighbors are all other points
            for neighbor in self.base_set:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None

    # ===== COMPACTNESS =====

    def is_compact(self, subset=None):
        """Check if space/subset is compact."""
        # Finite spaces are always compact
        if subset is None:
            return self.size < float('inf')
        
        return len(set(subset)) < float('inf')

    def is_bounded(self, subset=None):
        """Check if space/subset is bounded."""
        # Always bounded (finite)
        return True

    # ===== OPEN & CLOSED SETS =====

    def interior(self, subset):
        """Interior: largest open set contained in subset."""
        return set(subset)  # In discrete topology, interior is the set itself

    def closure(self, subset):
        """Closure: smallest closed set containing subset."""
        return set(subset)  # In discrete topology, closure is the set itself

    def boundary(self, subset):
        """Boundary: points in closure but not interior."""
        # In discrete topology: boundary is empty
        return set()

    def derived_set(self, subset):
        """Derived set: all limit points of subset."""
        # In discrete topology: no limit points (every point is isolated)
        return set()

    # ===== HAUSDORFF & SEPARATION =====

    def is_hausdorff(self):
        """Check if space is Hausdorff (T2)."""
        return True  # Discrete topology is always Hausdorff

    def separating_neighborhoods(self, x, y):
        """Find disjoint neighborhoods separating x and y."""
        if x == y:
            return None
        
        # Singleton neighborhoods work: {x} and {y}
        return {x}, {y}

    # ===== CLUSTERING & GRAPHS =====

    def as_complete_graph(self):
        """
        Represent discrete space as complete graph.
        Every point connected to every other point.
        """
        edges = set()
        points = list(self.base_set)
        
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                edges.add((p1, p2))
        
        return {
            'vertices': self.base_set,
            'edges': edges,
            'is_complete': True,
            'number_of_edges': len(edges),
        }

    def as_graph_with_threshold(self, threshold=1.0):
        """
        Represent as graph where edge exists if distance <= threshold.
        """
        edges = set()
        points = list(self.base_set)
        
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                if self.distance(p1, p2) <= threshold:
                    edges.add((p1, p2))
        
        return {
            'vertices': self.base_set,
            'edges': edges,
            'threshold': threshold,
            'number_of_edges': len(edges),
        }

    def adjacency_matrix(self, threshold=1.0):
        """Get adjacency matrix where edge exists if distance <= threshold."""
        elements = sorted(self.base_set, key=str)
        n = len(elements)
        matrix = [[0] * n for _ in range(n)]
        
        for i, x in enumerate(elements):
            for j, y in enumerate(elements):
                if i != j and self.distance(x, y) <= threshold:
                    matrix[i][j] = 1
        
        return matrix, elements

    def degree(self, point, threshold=1.0):
        """Degree of point (number of neighbors within threshold)."""
        count = 0
        for other in self.base_set:
            if other != point and self.distance(point, other) <= threshold:
                count += 1
        return count

    def average_degree(self, threshold=1.0):
        """Average degree of all points."""
        if self.size == 0:
            return 0
        
        total = sum(self.degree(p, threshold) for p in self.base_set)
        return total / self.size

    # ===== CLUSTERING ANALYSIS =====

    def clustering_coefficient(self, point, threshold=1.0):
        """
        Local clustering coefficient: proportion of neighbors that are connected.
        """
        neighbors = set()
        for other in self.base_set:
            if other != point and self.distance(point, other) <= threshold:
                neighbors.add(other)
        
        if len(neighbors) <= 1:
            return 0
        
        # Count edges among neighbors
        edges = 0
        neighbors_list = list(neighbors)
        for i, n1 in enumerate(neighbors_list):
            for n2 in neighbors_list[i+1:]:
                if self.distance(n1, n2) <= threshold:
                    edges += 1
        
        # Maximum possible edges
        max_edges = len(neighbors) * (len(neighbors) - 1) / 2
        
        return edges / max_edges if max_edges > 0 else 0

    def average_clustering_coefficient(self, threshold=1.0):
        """Average clustering coefficient over all points."""
        if self.size == 0:
            return 0
        
        coefficients = [self.clustering_coefficient(p, threshold) for p in self.base_set]
        return sum(coefficients) / len(coefficients)

    def transitivity(self, threshold=1.0):
        """Global clustering coefficient (transitivity)."""
        # Count triangles
        triangles = 0
        points = list(self.base_set)
        
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[i+1:], i+1):
                for p3 in points[j+1:]:
                    d12 = self.distance(p1, p2) <= threshold
                    d23 = self.distance(p2, p3) <= threshold
                    d13 = self.distance(p1, p3) <= threshold
                    
                    if d12 and d23 and d13:
                        triangles += 1
        
        # Count connected triples
        triples = 0
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[i+1:], i+1):
                for p3 in points[j+1:]:
                    d12 = self.distance(p1, p2) <= threshold
                    d23 = self.distance(p2, p3) <= threshold
                    d13 = self.distance(p1, p3) <= threshold
                    
                    if (d12 and d23) or (d23 and d13) or (d12 and d13):
                        triples += 1
        
        return 3 * triangles / triples if triples > 0 else 0

    # ===== STATISTICAL PROPERTIES =====

    def average_distance(self, subset=None):
        """Average pairwise distance."""
        if subset is None:
            subset = self.base_set
        
        subset = list(subset)
        if len(subset) < 2:
            return 0
        
        total = 0
        count = 0
        
        for i, x in enumerate(subset):
            for y in subset[i+1:]:
                total += self.distance(x, y)
                count += 1
        
        return total / count if count > 0 else 0

    def distance_distribution(self, subset=None):
        """Get distribution of distances."""
        if subset is None:
            subset = self.base_set
        
        subset = list(subset)
        distances = defaultdict(int)
        
        for i, x in enumerate(subset):
            for y in subset[i+1:]:
                dist = self.distance(x, y)
                distances[dist] += 1
        
        return dict(sorted(distances.items()))

    def pairwise_distances(self, subset=None):
        """Get all pairwise distances as dictionary."""
        if subset is None:
            subset = self.base_set
        
        subset = list(subset)
        distances = {}
        
        for i, x in enumerate(subset):
            for j, y in enumerate(subset):
                if i < j:
                    distances[(x, y)] = self.distance(x, y)
        
        return distances

    # ===== METRIC PROPERTIES =====

    def is_metric_space(self):
        """Check if metric satisfies metric axioms."""
        # Sample check on subset of points
        points = list(self.base_set)[:min(3, len(self.base_set))]
        
        for i, x in enumerate(points):
            for j, y in enumerate(points):
                d_xy = self.distance(x, y)
                d_yx = self.distance(y, x)
                
                # Symmetry
                if abs(d_xy - d_yx) > 1e-10:
                    return False
                
                # Non-negativity
                if d_xy < -1e-10:
                    return False
                
                # Identity
                if x == y and d_xy != 0:
                    return False
                if x != y and d_xy == 0:
                    return False
        
        return True

    def metric_properties(self):
        """Get metric space properties."""
        return {
            'is_metric': self.is_metric_space(),
            'is_complete': True,  # Finite metric spaces are complete
            'is_separable': True,
            'is_totally_bounded': True,
        }

    # ===== CARDINALITY =====

    def cardinality(self):
        """Get cardinality (number of points)."""
        return self.size

    def is_finite(self):
        """Check if space is finite."""
        return self.size < float('inf')

    def is_countable(self):
        """Check if space is countable."""
        # Always true for our implementation
        return True

    # ===== SUBSPACES =====

    def subspace(self, subset):
        """Get subspace topology."""
        return DiscreteTopology(subset, metric=self.metric, name=f"{self.name} (subspace)")

    def is_subspace_of(self, other):
        """Check if this is subspace of other."""
        if not isinstance(other, DiscreteTopology):
            return False
        
        return self.base_set.issubset(other.base_set)

    # ===== HOMEOMORPHISM & ISOMETRY =====

    def is_homeomorphic_to(self, other):
        """Check if homeomorphic to another discrete topology."""
        if not isinstance(other, DiscreteTopology):
            return False
        
        # Two discrete topologies are homeomorphic iff same cardinality
        return len(self.base_set) == len(other.base_set)

    def is_isometric_to(self, other):
        """Check if isometric to another metric space."""
        if not isinstance(other, DiscreteTopology):
            return False
        
        # Discrete metric spaces are isometric iff same cardinality
        return len(self.base_set) == len(other.base_set)

    # ===== PARTITIONS =====

    def partition_by_distance(self, distance_threshold):
        """Partition points based on distance threshold."""
        visited = set()
        partitions = []
        
        for point in self.base_set:
            if point not in visited:
                partition = set()
                queue = deque([point])
                
                while queue:
                    current = queue.popleft()
                    if current in visited:
                        continue
                    
                    visited.add(current)
                    partition.add(current)
                    
                    for other in self.base_set:
                        if other not in visited and self.distance(current, other) <= distance_threshold:
                            queue.append(other)
                
                partitions.append(partition)
        
        return partitions

    # ===== VISUALIZATION & EXPORT =====

    def summary(self):
        """One-line summary."""
        return f"Discrete Topology: {self.name} with {self.size} points"

    def describe(self):
        """Detailed description."""
        desc = f"\n{'='*60}\n"
        desc += f"Discrete Topology: {self.name}\n"
        desc += f"{'='*60}\n"
        desc += f"Number of points: {self.size}\n"
        desc += f"Number of open sets: {len(self.open_sets)}\n"
        desc += f"Diameter: {self.diameter()}\n"
        desc += f"Radius: {self.radius()}\n"
        desc += f"Average distance: {self.average_distance():.2f}\n"
        desc += f"Is connected: {self.is_connected()}\n"
        desc += f"Is compact: {self.is_compact()}\n"
        desc += f"Is Hausdorff: {self.is_hausdorff()}\n"
        desc += f"{'='*60}\n"
        return desc

    def export_to_dict(self):
        """Export space as dictionary."""
        return {
            'name': self.name,
            'base_set': list(self.base_set),
            'cardinality': self.size,
            'diameter': self.diameter(),
            'radius': self.radius(),
            'is_connected': self.is_connected(),
            'is_compact': self.is_compact(),
            'properties': self.get_properties(),
        }

