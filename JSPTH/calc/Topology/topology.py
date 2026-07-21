import math
from itertools import combinations, permutations
from collections import defaultdict, deque


class Topology:
    """
    Base class for defining and working with topological spaces.
    A topological space is a set X with a collection of subsets (open sets) that satisfy:
    1. Empty set and X are open
    2. Arbitrary unions of open sets are open
    3. Finite intersections of open sets are open
    """

    def __init__(self, base_set, open_sets):
        """
        Initialize a topological space.
        
        :param base_set: The underlying set (as a list or tuple)
        :param open_sets: A collection of open sets (as a list of lists/tuples)
        """
        self.base_set = set(base_set)
        self.open_sets = [set(s) for s in open_sets]
        self.closed_sets = []
        self._compute_closed_sets()

    def _compute_closed_sets(self):
        """Compute closed sets as complements of open sets."""
        self.closed_sets = []
        for open_set in self.open_sets:
            closed_set = self.base_set - open_set
            self.closed_sets.append(closed_set)

    def is_valid_topology(self):
        """
        Check if the collection of open sets forms a valid topology.
        
        :return: True if valid, False otherwise
        """
        # Check 1: Empty set and full set must be open
        if set() not in self.open_sets and set() not in [s for s in self.open_sets if len(s) == 0]:
            return False
        if self.base_set not in self.open_sets:
            return False

        # Check 2: Arbitrary unions of open sets are open
        for i, open_set1 in enumerate(self.open_sets):
            for open_set2 in self.open_sets[i+1:]:
                union = open_set1 | open_set2
                if union not in self.open_sets:
                    return False

        # Check 3: Finite intersections of open sets are open
        for i, open_set1 in enumerate(self.open_sets):
            for open_set2 in self.open_sets[i+1:]:
                intersection = open_set1 & open_set2
                if len(intersection) > 0 and intersection not in self.open_sets:
                    return False

        return True

    def is_open_set(self, subset):
        """Check if a subset is open."""
        return set(subset) in self.open_sets

    def is_closed_set(self, subset):
        """Check if a subset is closed."""
        return set(subset) in self.closed_sets

    def closure(self, subset):
        """
        Compute the closure of a set (smallest closed set containing it).
        
        :param subset: The subset to find closure of
        :return: The closure as a set
        """
        subset = set(subset)
        # Closure is complement of the interior of complement
        complement = self.base_set - subset
        interior = self.interior(complement)
        return self.base_set - interior

    def interior(self, subset):
        """
        Compute the interior of a set (largest open set contained in it).
        
        :param subset: The subset to find interior of
        :return: The interior as a set
        """
        subset = set(subset)
        interior = set()
        for open_set in self.open_sets:
            if open_set.issubset(subset):
                interior = interior | open_set
        return interior

    def boundary(self, subset):
        """
        Compute the boundary of a set (points in closure but not in interior).
        
        :param subset: The subset to find boundary of
        :return: The boundary as a set
        """
        subset = set(subset)
        closure_set = self.closure(subset)
        interior_set = self.interior(subset)
        return closure_set - interior_set

    def neighborhood(self, point):
        """
        Find all neighborhoods of a point.
        
        :param point: The point to find neighborhoods for
        :return: List of neighborhoods (open sets containing the point)
        """
        neighborhoods = []
        for open_set in self.open_sets:
            if point in open_set:
                neighborhoods.append(open_set)
        return neighborhoods

    def is_continuous(self, func, source_topology, target_topology):
        """
        Check if a function is continuous.
        
        :param func: Function mapping elements
        :param source_topology: Topology on the source space
        :param target_topology: Topology on the target space
        :return: True if continuous, False otherwise
        """
        # f is continuous if preimage of every open set in target is open in source
        for open_set in target_topology.open_sets:
            preimage = set()
            for x in source_topology.base_set:
                if func(x) in open_set:
                    preimage.add(x)
            if preimage not in source_topology.open_sets and len(preimage) > 0:
                return False
        return True

    def is_connected(self):
        """
        Check if the topological space is connected.
        A space is connected if it cannot be separated into two non-empty open sets.
        
        :return: True if connected, False otherwise
        """
        # Space is disconnected if it can be written as union of two non-empty disjoint open sets
        for open_set1 in self.open_sets:
            for open_set2 in self.open_sets:
                if (open_set1 | open_set2 == self.base_set and 
                    len(open_set1) > 0 and len(open_set2) > 0 and 
                    open_set1 & open_set2 == set()):
                    return False
        return True

    def is_compact(self):
        """
        Check if space is compact (every open cover has a finite subcover).
        Simplified check for finite spaces.
        
        :return: True if compact, False otherwise
        """
        # For finite spaces, check if open sets form a valid topology
        return self.is_valid_topology()

    def is_hausdorff(self):
        """
        Check if space is Hausdorff (T2 - any two points have disjoint neighborhoods).
        
        :return: True if Hausdorff, False otherwise
        """
        points = list(self.base_set)
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                if p1 == p2:
                    continue
                # Find neighborhoods of p1 and p2
                nbhd_p1 = self.neighborhood(p1)
                nbhd_p2 = self.neighborhood(p2)
                # Check if there exist disjoint neighborhoods
                found_disjoint = False
                for n1 in nbhd_p1:
                    for n2 in nbhd_p2:
                        if n1 & n2 == set():
                            found_disjoint = True
                            break
                    if found_disjoint:
                        break
                if not found_disjoint:
                    return False
        return True

class MetricSpace:
    """
    Enhanced MetricSpace class with comprehensive distance and topology operations.
    A metric space is a set with a distance function satisfying:
    1. d(x,y) ≥ 0 (non-negativity)
    2. d(x,y) = 0 ⟺ x = y (identity of indiscernibles)
    3. d(x,y) = d(y,x) (symmetry)
    4. d(x,z) ≤ d(x,y) + d(y,z) (triangle inequality)
    """

    def __init__(self, points, metric, name="MetricSpace"):
        """
        Initialize a metric space.
        
        :param points: Set of points (list, set, or tuple)
        :param metric: Function metric(p1, p2) returning distance
        :param name: Name for the space (optional)
        """
        self.points = set(points) if not isinstance(points, set) else points
        self.metric = metric
        self.name = name
        self._distance_cache = {}  # Cache distances for performance
        self._verify_metric()

    def _verify_metric(self):
        """Verify that the metric satisfies basic properties (partial check)."""
        if len(self.points) < 2:
            return True
        
        points_list = list(self.points)
        # Check symmetry and non-negativity
        for p1 in points_list[:min(3, len(points_list))]:  # Sample check
            for p2 in points_list[:min(3, len(points_list))]:
                d12 = self.metric(p1, p2)
                d21 = self.metric(p2, p1)
                
                if abs(d12 - d21) > 1e-10:
                    raise ValueError(f"Metric not symmetric: d({p1},{p2})={d12} ≠ d({p2},{p1})={d21}")
                
                if d12 < -1e-10:
                    raise ValueError(f"Metric returned negative distance: d({p1},{p2})={d12}")
        
        return True

    def distance(self, p1, p2):
        """
        Calculate distance between two points.
        Uses caching to avoid redundant calculations.
        """
        if p1 == p2:
            return 0
        
        # Use sorted tuple as cache key (exploits symmetry)
        key = tuple(sorted([str(p1), str(p2)]))
        
        if key in self._distance_cache:
            return self._distance_cache[key]
        
        dist = self.metric(p1, p2)
        self._distance_cache[key] = dist
        return dist

    def clear_cache(self):
        """Clear the distance cache."""
        self._distance_cache = {}

    # ===== BASIC BALL OPERATIONS =====

    def open_ball(self, center, radius):
        """
        Open ball: all points strictly within radius of center.
        B(c, r) = {x ∈ X : d(c, x) < r}
        """
        ball = set()
        for point in self.points:
            if self.distance(center, point) < radius:
                ball.add(point)
        return ball

    def closed_ball(self, center, radius):
        """
        Closed ball: all points within and on the radius.
        B̄(c, r) = {x ∈ X : d(c, x) ≤ r}
        """
        ball = set()
        for point in self.points:
            if self.distance(center, point) <= radius:
                ball.add(point)
        return ball

    def sphere(self, center, radius):
        """
        Sphere: all points exactly at distance radius from center.
        S(c, r) = {x ∈ X : d(c, x) = r}
        """
        sphere = set()
        for point in self.points:
            if abs(self.distance(center, point) - radius) < 1e-10:
                sphere.add(point)
        return sphere

    # ===== DIAMETER & RADIUS OPERATIONS =====

    def diameter(self, subset=None):
        """
        Diameter of space or subset: maximum distance between any two points.
        diam(X) = sup{d(x, y) : x, y ∈ X}
        """
        if subset is None:
            subset = self.points
        subset = list(subset)
        
        if len(subset) <= 1:
            return 0
        
        max_dist = 0
        for i, p1 in enumerate(subset):
            for p2 in subset[i+1:]:
                dist = self.distance(p1, p2)
                if dist > max_dist:
                    max_dist = dist
        
        return max_dist

    def radius(self, subset=None):
        """
        Radius of subset: minimum eccentricity of any point.
        Essentially, the smallest radius needed to cover the subset with a ball.
        """
        if subset is None:
            subset = self.points
        subset = list(subset)
        
        if len(subset) == 0:
            return 0
        
        # Find the point that minimizes maximum distance to all others
        min_eccentricity = float('inf')
        
        for center in subset:
            max_dist = 0
            for point in subset:
                dist = self.distance(center, point)
                if dist > max_dist:
                    max_dist = dist
            
            if max_dist < min_eccentricity:
                min_eccentricity = max_dist
        
        return min_eccentricity

    def center(self, subset=None):
        """
        Find the center point (or points) of a subset.
        Center point(s) minimize eccentricity: min max d(x, y).
        """
        if subset is None:
            subset = self.points
        subset = list(subset)
        
        if len(subset) == 0:
            return []
        
        # Find points with minimum eccentricity
        radius = self.radius(subset)
        centers = []
        
        for center_candidate in subset:
            max_dist = max(self.distance(center_candidate, p) for p in subset)
            if abs(max_dist - radius) < 1e-10:
                centers.append(center_candidate)
        
        return centers

    def eccentricity(self, point, subset=None):
        """
        Eccentricity of a point: maximum distance to any other point in subset.
        e(x) = max{d(x, y) : y ∈ X}
        """
        if subset is None:
            subset = self.points
        
        max_dist = 0
        for p in subset:
            if p != point:
                dist = self.distance(point, p)
                if dist > max_dist:
                    max_dist = dist
        
        return max_dist

    def is_bounded(self, subset=None):
        """Check if space/subset is bounded (finite diameter)."""
        return self.diameter(subset) < float('inf')

    # ===== NEAREST NEIGHBOR OPERATIONS =====

    def nearest_neighbor(self, point):
        """Find the nearest point to a given point."""
        if point not in self.points:
            raise ValueError(f"Point {point} not in metric space")
        
        nearest = None
        min_dist = float('inf')
        
        for p in self.points:
            if p != point:
                dist = self.distance(point, p)
                if dist < min_dist:
                    min_dist = dist
                    nearest = p
        
        return nearest, min_dist

    def k_nearest_neighbors(self, point, k=1):
        """
        Find k nearest neighbors to a point.
        
        :param point: Query point
        :param k: Number of neighbors to return
        :return: List of (neighbor, distance) tuples sorted by distance
        """
        if point not in self.points:
            raise ValueError(f"Point {point} not in metric space")
        
        if k < 1:
            raise ValueError("k must be at least 1")
        
        # Calculate distances to all other points
        distances = []
        for p in self.points:
            if p != point:
                dist = self.distance(point, p)
                distances.append((p, dist))
        
        # Sort by distance and return top k
        distances.sort(key=lambda x: x[1])
        return distances[:min(k, len(distances))]

    def radius_search(self, point, radius):
        """
        Find all points within radius of a point.
        Combines open ball concept with explicit listing.
        
        :param point: Query point
        :param radius: Search radius
        :return: List of (point, distance) tuples within radius
        """
        neighbors = []
        for p in self.points:
            if p != point:
                dist = self.distance(point, p)
                if dist <= radius:
                    neighbors.append((p, dist))
        
        neighbors.sort(key=lambda x: x[1])
        return neighbors

    # ===== CLUSTERING & CONNECTIVITY =====

    def connected_components(self, max_distance=None):
        """
        Find connected components using distance threshold.
        Two points are connected if distance ≤ max_distance.
        
        :param max_distance: Distance threshold for connectivity
        :return: List of sets (each set is a connected component)
        """
        if max_distance is None:
            max_distance = self.diameter() / 2
        
        visited = set()
        components = []
        
        for point in self.points:
            if point not in visited:
                # BFS to find component
                component = set()
                queue = deque([point])
                
                while queue:
                    current = queue.popleft()
                    if current in visited:
                        continue
                    
                    visited.add(current)
                    component.add(current)
                    
                    # Find neighbors within max_distance
                    for neighbor in self.points:
                        if neighbor not in visited:
                            if self.distance(current, neighbor) <= max_distance:
                                queue.append(neighbor)
                
                if component:
                    components.append(component)
        
        return components

    def single_linkage_clustering(self, n_clusters):
        """
        Simple single-linkage hierarchical clustering.
        
        :param n_clusters: Number of clusters to form
        :return: List of sets (each set is a cluster)
        """
        # Start with each point as its own cluster
        clusters = [{p} for p in self.points]
        
        # Merge closest clusters until reaching desired number
        while len(clusters) > n_clusters:
            min_dist = float('inf')
            merge_i, merge_j = 0, 1
            
            # Find two closest clusters
            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    # Single linkage: minimum distance between clusters
                    for p1 in clusters[i]:
                        for p2 in clusters[j]:
                            dist = self.distance(p1, p2)
                            if dist < min_dist:
                                min_dist = dist
                                merge_i, merge_j = i, j
            
            # Merge clusters
            clusters[merge_i] = clusters[merge_i] | clusters[merge_j]
            clusters.pop(merge_j)
        
        return clusters

    def complete_linkage_clustering(self, n_clusters):
        """
        Complete-linkage hierarchical clustering.
        Uses maximum distance between clusters (more conservative).
        
        :param n_clusters: Number of clusters to form
        :return: List of sets (each set is a cluster)
        """
        clusters = [{p} for p in self.points]
        
        while len(clusters) > n_clusters:
            min_dist = float('inf')
            merge_i, merge_j = 0, 1
            
            # Find two closest clusters (by maximum distance)
            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    # Complete linkage: maximum distance between clusters
                    max_dist = 0
                    for p1 in clusters[i]:
                        for p2 in clusters[j]:
                            dist = self.distance(p1, p2)
                            if dist > max_dist:
                                max_dist = dist
                    
                    if max_dist < min_dist:
                        min_dist = max_dist
                        merge_i, merge_j = i, j
            
            clusters[merge_i] = clusters[merge_i] | clusters[merge_j]
            clusters.pop(merge_j)
        
        return clusters

    # ===== STATISTICAL MEASURES =====

    def average_distance(self, subset=None):
        """
        Calculate average distance between all pairs in subset.
        """
        if subset is None:
            subset = self.points
        subset = list(subset)
        
        if len(subset) < 2:
            return 0
        
        total_dist = 0
        count = 0
        
        for i, p1 in enumerate(subset):
            for p2 in subset[i+1:]:
                total_dist += self.distance(p1, p2)
                count += 1
        
        return total_dist / count if count > 0 else 0

    def distance_variance(self, subset=None):
        """
        Calculate variance of distances between all pairs.
        Measures how spread out the distances are.
        """
        if subset is None:
            subset = self.points
        subset = list(subset)
        
        if len(subset) < 2:
            return 0
        
        distances = []
        for i, p1 in enumerate(subset):
            for p2 in subset[i+1:]:
                distances.append(self.distance(p1, p2))
        
        if not distances:
            return 0
        
        mean = sum(distances) / len(distances)
        variance = sum((d - mean) ** 2 for d in distances) / len(distances)
        return variance

    def distance_standard_deviation(self, subset=None):
        """Standard deviation of all pairwise distances."""
        return math.sqrt(self.distance_variance(subset))

    def pairwise_distances(self, subset=None):
        """
        Get all pairwise distances as a dictionary.
        
        :param subset: Optional subset of points
        :return: Dict mapping (p1, p2) -> distance
        """
        if subset is None:
            subset = self.points
        subset = list(subset)
        
        distances = {}
        for i, p1 in enumerate(subset):
            for j, p2 in enumerate(subset):
                if i < j:
                    distances[(p1, p2)] = self.distance(p1, p2)
        
        return distances

    def distance_matrix(self, subset=None, as_list=False):
        """
        Get distance matrix for subset.
        
        :param subset: Optional subset of points
        :param as_list: If True, return as list of lists; if False, return as dict
        :return: Distance matrix (N×N)
        """
        if subset is None:
            subset = list(self.points)
        else:
            subset = list(subset)
        
        n = len(subset)
        matrix = [[0] * n for _ in range(n)]
        
        for i, p1 in enumerate(subset):
            for j, p2 in enumerate(subset):
                matrix[i][j] = self.distance(p1, p2)
        
        return matrix

    # ===== GEOMETRIC OPERATIONS =====

    def midpoint(self, p1, p2):
        """
        Find the midpoint between two points.
        For discrete spaces, returns the point closest to the midpoint.
        Works best for continuous metrics like Euclidean.
        """
        # For actual coordinates (tuples)
        if isinstance(p1, tuple) and isinstance(p2, tuple):
            mid = tuple((a + b) / 2 for a, b in zip(p1, p2))
            return mid
        
        # For discrete spaces, find closest point to halfway distance
        half_dist = self.distance(p1, p2) / 2
        return self.radius_search(p1, half_dist + 0.1)

    def geodesic(self, p1, p2):
        """
        Find shortest path between two points in the metric space.
        Useful for understanding space structure.
        
        :param p1: Start point
        :param p2: End point
        :return: List of points forming shortest path
        """
        if p1 == p2:
            return [p1]
        
        # Dijkstra-like algorithm for shortest path
        distances = {p: float('inf') for p in self.points}
        distances[p1] = 0
        parent = {p: None for p in self.points}
        unvisited = set(self.points)
        
        while unvisited:
            # Find unvisited point with minimum distance
            current = min(unvisited, key=lambda p: distances[p])
            
            if distances[current] == float('inf') or current == p2:
                break
            
            unvisited.remove(current)
            
            # Update distances to neighbors
            for neighbor in unvisited:
                new_dist = distances[current] + self.distance(current, neighbor)
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = current
        
        # Reconstruct path
        path = []
        current = p2
        while current is not None:
            path.append(current)
            current = parent[current]
        
        return list(reversed(path))

    def geodesic_distance(self, p1, p2):
        """Distance along shortest path (may differ from direct metric distance)."""
        path = self.geodesic(p1, p2)
        total = 0
        for i in range(len(path) - 1):
            total += self.distance(path[i], path[i + 1])
        return total

    # ===== DENSITY & DISTRIBUTION =====

    def local_density(self, point, radius):
        """
        Calculate local density: number of points within radius.
        
        :param point: Query point
        :param radius: Search radius
        :return: Number of points within radius (including self)
        """
        return len(self.closed_ball(point, radius))

    def density_distribution(self, radii):
        """
        Get density distribution for each point across multiple radii.
        
        :param radii: List of radii to check
        :return: Dict mapping point -> dict of radius -> density
        """
        distribution = {}
        for point in self.points:
            distribution[point] = {}
            for radius in radii:
                distribution[point][radius] = self.local_density(point, radius)
        return distribution

    def outlier_score(self, point, k=5):
        """
        Calculate outlier score using k-distance.
        Higher score = more likely to be outlier.
        
        :param point: Query point
        :param k: Number of neighbors to consider
        :return: k-distance value
        """
        neighbors = self.k_nearest_neighbors(point, k)
        if neighbors:
            return neighbors[-1][1]  # Distance to kth neighbor
        return 0

    def detect_outliers(self, k=5, threshold=None):
        """
        Detect outliers using k-distance.
        
        :param k: Number of neighbors
        :param threshold: Distance threshold for outliers; if None, use mean + 2*std
        :return: List of potential outliers
        """
        outlier_scores = {}
        for point in self.points:
            outlier_scores[point] = self.outlier_score(point, k)
        
        if threshold is None:
            scores = list(outlier_scores.values())
            mean = sum(scores) / len(scores)
            variance = sum((s - mean) ** 2 for s in scores) / len(scores)
            std = math.sqrt(variance)
            threshold = mean + 2 * std
        
        outliers = [p for p, score in outlier_scores.items() if score > threshold]
        return outliers

    # ===== SPACE PROPERTIES =====

    def is_discrete(self, epsilon=1e-10):
        """
        Check if space is discrete (all points far apart).
        
        :param epsilon: Minimum distance threshold
        :return: True if all distances > epsilon
        """
        for i, p1 in enumerate(self.points):
            for p2 in list(self.points)[i+1:]:
                if self.distance(p1, p2) < epsilon:
                    return False
        return True

    def is_separable(self):
        """
        Check if metric space is separable (has countable dense subset).
        For finite spaces, always true.
        """
        return len(self.points) <= float('inf')

    def is_complete(self):
        """
        Simplified completeness check for finite metric spaces.
        Finite metric spaces are always complete.
        """
        return True if len(self.points) < float('inf') else None

    def is_connected(self, max_distance=None):
        """
        Check if space is connected (can reach any point from any other).
        
        :param max_distance: Optional distance threshold for connectivity
        :return: True if connected
        """
        components = self.connected_components(max_distance)
        return len(components) == 1

    # ===== UTILITY METHODS =====

    def get_statistics(self, subset=None):
        """
        Get comprehensive statistics about the space/subset.
        
        :return: Dictionary with various metrics
        """
        if subset is None:
            subset = self.points
        subset = list(subset)
        
        return {
            'num_points': len(subset),
            'diameter': self.diameter(subset),
            'radius': self.radius(subset),
            'center': self.center(subset),
            'avg_distance': self.average_distance(subset),
            'distance_std': self.distance_standard_deviation(subset),
            'is_bounded': self.is_bounded(subset),
            'is_discrete': self.is_discrete(),
            'is_connected': self.is_connected(),
        }

    def print_statistics(self, subset=None):
        """Print space statistics in readable format."""
        stats = self.get_statistics(subset)
        print(f"\n{'='*50}")
        print(f"Metric Space: {self.name}")
        print(f"{'='*50}")
        print(f"Number of points: {stats['num_points']}")
        print(f"Diameter: {stats['diameter']:.4f}")
        print(f"Radius: {stats['radius']:.4f}")
        print(f"Center points: {stats['center']}")
        print(f"Average distance: {stats['avg_distance']:.4f}")
        print(f"Distance std dev: {stats['distance_std']:.4f}")
        print(f"Bounded: {stats['is_bounded']}")
        print(f"Discrete: {stats['is_discrete']}")
        print(f"Connected: {stats['is_connected']}")
        print(f"{'='*50}\n")

    def summary(self):
        """Get a one-line summary of the space."""
        return f"{self.name}: {len(self.points)} points, diameter={self.diameter():.2f}"

class other_functions:
    def euclidean_metric(p1, p2):
        """Euclidean distance: √(Σ(xᵢ - yᵢ)²)"""
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


    def manhattan_metric(p1, p2):
        """Manhattan distance: Σ|xᵢ - yᵢ|"""
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        return sum(abs(a - b) for a, b in zip(p1, p2))


    def chebyshev_metric(p1, p2):
        """Chebyshev distance: max(|xᵢ - yᵢ|)"""
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        return max(abs(a - b) for a, b in zip(p1, p2))


    def minkowski_metric(p1, p2, p=2):
        """
        Minkowski distance: (Σ|xᵢ - yᵢ|^p)^(1/p)
        p=1 gives Manhattan, p=2 gives Euclidean, p=∞ gives Chebyshev
        """
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        if p == float('inf'):
            return other_functions.chebyshev_metric(p1, p2)
        return sum(abs(a - b) ** p for a, b in zip(p1, p2)) ** (1/p)


    def hamming_metric(s1, s2):
        """Hamming distance: number of differing positions (for strings/sequences)"""
        if len(s1) != len(s2):
            raise ValueError("Strings must have same length")
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))


    def cosine_metric(v1, v2):
        """
        Cosine distance: 1 - cosine_similarity
        For vectors/points representing similarity.
        """
        if len(v1) != len(v2):
            raise ValueError("Vectors must have same dimension")
        
        dot_product = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a ** 2 for a in v1))
        norm2 = math.sqrt(sum(b ** 2 for b in v2))
        
        if norm1 == 0 or norm2 == 0:
            return 1.0
        
        similarity = dot_product / (norm1 * norm2)
        return 1 - max(-1, min(1, similarity))  # Clamp to [0, 2]


    def jaccard_metric(set1, set2):
        """Jaccard distance: 1 - Jaccard_similarity"""
        if not isinstance(set1, set):
            set1 = set(set1)
        if not isinstance(set2, set):
            set2 = set(set2)
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        if union == 0:
            return 0
        
        return 1 - (intersection / union)


    def hausdorff_metric(set1, set2, metric=euclidean_metric):
        """Hausdorff distance between two sets."""
        set1 = list(set1)
        set2 = list(set2)
        
        if not set1 or not set2:
            return float('inf')
        
        max_dist = 0
        
        # Maximum of minimum distances from set1 to set2
        for p1 in set1:
            min_dist = min(metric(p1, p2) for p2 in set2)
            if min_dist > max_dist:
                max_dist = min_dist
        
        # Maximum of minimum distances from set2 to set1
        for p2 in set2:
            min_dist = min(metric(p1, p2) for p1 in set1)
            if min_dist > max_dist:
                max_dist = min_dist
        
        return max_dist
    
        
    def line_segment(p1, p2, steps=100):
        """Generate points along line segment from p1 to p2."""
        if isinstance(p1, (int, float)):
            p1 = (p1,)
        if isinstance(p2, (int, float)):
            p2 = (p2,)
        
        points = []
        for t in [i / (steps - 1) for i in range(steps)]:
            point = tuple(p1[i] * (1 - t) + p2[i] * t for i in range(len(p1)))
            points.append(point)
        
        return points


    def circle(center, radius, steps=100):
        """Generate points on circle."""
        if isinstance(center, (int, float)):
            center = (center, 0)
        
        points = []
        for angle in [i * 2 * math.pi / steps for i in range(steps)]:
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            points.append((x, y))
        
        return points


    def sphere_surface(center, radius, steps=20):
        """Generate points on sphere surface (3D)."""
        if not isinstance(center, tuple) or len(center) != 3:
            raise ValueError("Center must be 3D point")
        
        points = []
        for phi in [i * math.pi / steps for i in range(steps)]:
            for theta in [i * 2 * math.pi / steps for i in range(steps)]:
                x = center[0] + radius * math.sin(phi) * math.cos(theta)
                y = center[1] + radius * math.sin(phi) * math.sin(theta)
                z = center[2] + radius * math.cos(phi)
                points.append((x, y, z))
        
        return points
    
    def euclidean_metric(p1, p2):
        """
        Compute Euclidean distance between two points (tuples).
        
        :param p1: First point (tuple of coordinates)
        :param p2: Second point (tuple of coordinates)
        :return: Euclidean distance
        """
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


    def manhattan_metric(p1, p2):
        """
        Compute Manhattan distance between two points.
        
        :param p1: First point (tuple of coordinates)
        :param p2: Second point (tuple of coordinates)
        :return: Manhattan distance
        """
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        return sum(abs(a - b) for a, b in zip(p1, p2))


    def chebyshev_metric(p1, p2):
        """
        Compute Chebyshev (maximum) distance between two points.
        
        :param p1: First point (tuple of coordinates)
        :param p2: Second point (tuple of coordinates)
        :return: Chebyshev distance
        """
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        return max(abs(a - b) for a, b in zip(p1, p2))


    def hausdorff_distance(set1, set2, metric):
        """
        Compute the Hausdorff distance between two sets.
        
        :param set1: First set (list of points)
        :param set2: Second set (list of points)
        :param metric: Distance metric function
        :return: Hausdorff distance
        """
        max_dist = 0
        
        # Maximum of minimum distances from set1 to set2
        for p1 in set1:
            min_dist = float('inf')
            for p2 in set2:
                dist = metric(p1, p2)
                if dist < min_dist:
                    min_dist = dist
            if min_dist > max_dist:
                max_dist = min_dist
        
        # Maximum of minimum distances from set2 to set1
        for p2 in set2:
            min_dist = float('inf')
            for p1 in set1:
                dist = metric(p1, p2)
                if dist < min_dist:
                    min_dist = dist
            if min_dist > max_dist:
                max_dist = min_dist
        
        return max_dist


class IndiscreteTopology(Topology):
    """
    The indiscrete (trivial) topology where only the empty set and the whole space are open.
    """

    def __init__(self, base_set):
        """
        Initialize indiscrete topology.
        
        :param base_set: The underlying set
        """
        base_set = list(base_set)
        self.base_set = set(base_set)
        self.open_sets = [set(), self.base_set]  # Only empty set and full set
        self.closed_sets = []
        self._compute_closed_sets()


class CofiniteTopology(Topology):
    """
    Cofinite topology where open sets are complements of finite sets (plus empty set).
    """

    def __init__(self, base_set):
        """
        Initialize cofinite topology.
        
        :param base_set: The underlying set
        """
        base_set = list(base_set)
        self.base_set = set(base_set)
        self.open_sets = [set()]  # Start with empty set
        
        # Add all complements of finite sets
        elements = list(self.base_set)
        for r in range(1, len(elements)):
            for combo in combinations(elements, r):
                complement = self.base_set - set(combo)
                self.open_sets.append(complement)
        
        self.open_sets.append(self.base_set)  # Add full set
        self.closed_sets = []
        self._compute_closed_sets()


class SubspaceTopology(Topology):
    """
    Induced subspace topology on a subset of a topological space.
    """

    def __init__(self, parent_topology, subspace):
        """
        Initialize subspace topology.
        
        :param parent_topology: The parent topological space
        :param subspace: The subset with induced topology
        """
        self.parent_topology = parent_topology
        self.base_set = set(subspace)
        # Subspace topology: intersections of open sets in parent with subspace
        self.open_sets = []
        for open_set in parent_topology.open_sets:
            induced_open = open_set & self.base_set
            self.open_sets.append(induced_open)
        self.closed_sets = []
        self._compute_closed_sets()


class ProductTopology(Topology):
    """
    Product topology on the Cartesian product of topological spaces.
    """

    def __init__(self, topology1, topology2):
        """
        Initialize product topology.
        
        :param topology1: First topological space
        :param topology2: Second topological space
        """
        # Base set is Cartesian product
        self.base_set = set()
        for p1 in topology1.base_set:
            for p2 in topology2.base_set:
                self.base_set.add((p1, p2))
        
        # Open sets in product topology
        self.open_sets = []
        for open_set1 in topology1.open_sets:
            for open_set2 in topology2.open_sets:
                product_open = set()
                for p1 in open_set1:
                    for p2 in open_set2:
                        product_open.add((p1, p2))
                self.open_sets.append(product_open)
        
        self.closed_sets = []
        self._compute_closed_sets()


# Utility functions for topology operations

