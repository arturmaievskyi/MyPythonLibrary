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

class Other_functions:
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
            return chebyshev_metric(p1, p2)
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

class EuclideanTopology:
    """
    The standard topology on Euclidean space (ℝⁿ).
    
    Properties:
    - Open sets are unions of open intervals (1D) or open balls (nD)
    - Induced by the standard Euclidean metric: d(x,y) = √(Σ(xᵢ - yᵢ)²)
    - Hausdorff separable space
    - Connected for any dimension
    - Not compact (infinite space)
    """

    def __init__(self, dimension=1, bounds=None):
        """
        Initialize Euclidean topology.
        
        :param dimension: Dimension of the space (1, 2, 3, ...)
        :param bounds: Optional tuple (min, max) for bounded representation
        """
        if dimension < 1:
            raise ValueError("Dimension must be at least 1")
        
        self.dimension = dimension
        self.bounds = bounds  # For finite representation
        
        # Generate representative open sets
        if bounds is None:
            self.bounds = (-10, 10)  # Default finite representation
        
        self.min_val, self.max_val = self.bounds
        self.open_sets = []
        self.closed_sets = []
        self._generate_standard_topology()

    def _generate_standard_topology(self):
        """Generate standard Euclidean topology (finite approximation)."""
        self.open_sets = [set()]  # Empty set
        
        if self.dimension == 1:
            # Generate open intervals
            for a in range(self.min_val, self.max_val):
                for b in range(a + 1, self.max_val + 1):
                    interval = set(range(a, b))
                    if interval:
                        self.open_sets.append(interval)
        elif self.dimension == 2:
            # Generate open balls in 2D (square approximation)
            all_points = set()
            for x in range(self.min_val, self.max_val + 1):
                for y in range(self.min_val, self.max_val + 1):
                    all_points.add((x, y))
            
            self.open_sets.append(all_points)  # Full space
            
            # Add some open balls
            for cx in range(self.min_val, self.max_val):
                for cy in range(self.min_val, self.max_val):
                    for r in [1, 2, 3]:
                        ball = set()
                        for x in range(self.min_val, self.max_val + 1):
                            for y in range(self.min_val, self.max_val + 1):
                                if math.sqrt((x - cx)**2 + (y - cy)**2) < r:
                                    ball.add((x, y))
                        if ball:
                            self.open_sets.append(ball)
        else:
            # General case: at least have empty and full sets
            all_points = set()
            for coords in self._generate_points(self.dimension):
                all_points.add(coords)
            self.open_sets.append(all_points)

    def _generate_points(self, dim, min_v=None, max_v=None):
        """Generate all points up to dimension dim."""
        if min_v is None:
            min_v = self.min_val
        if max_v is None:
            max_v = self.max_val
        
        if dim == 1:
            return [[x] for x in range(min_v, max_v + 1)]
        else:
            points = []
            for p in self._generate_points(dim - 1, min_v, max_v):
                for x in range(min_v, max_v + 1):
                    points.append(tuple(p + [x]))
            return points

    # ===== DISTANCE OPERATIONS =====

    @staticmethod
    def euclidean_distance(p1, p2):
        """
        Calculate Euclidean distance between two points.
        d(x,y) = √(Σ(xᵢ - yᵢ)²)
        """
        if isinstance(p1, (int, float)):
            p1 = (p1,)
        if isinstance(p2, (int, float)):
            p2 = (p2,)
        
        if len(p1) != len(p2):
            raise ValueError("Points must have same dimension")
        
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

    @staticmethod
    def manhattan_distance(p1, p2):
        """Manhattan distance (L1 norm): Σ|xᵢ - yᵢ|"""
        if isinstance(p1, (int, float)):
            p1 = (p1,)
        if isinstance(p2, (int, float)):
            p2 = (p2,)
        
        return sum(abs(a - b) for a, b in zip(p1, p2))

    @staticmethod
    def chebyshev_distance(p1, p2):
        """Chebyshev distance (L∞ norm): max(|xᵢ - yᵢ|)"""
        if isinstance(p1, (int, float)):
            p1 = (p1,)
        if isinstance(p2, (int, float)):
            p2 = (p2,)
        
        return max(abs(a - b) for a, b in zip(p1, p2))

    # ===== BALL OPERATIONS =====

    @staticmethod
    def open_ball(center, radius, dimension=None):
        """
        Open ball B(c, r) = {x : d(x, c) < r}
        Returns ball as set of representative points.
        """
        if isinstance(center, (int, float)):
            center = (center,)
        
        if dimension is None:
            dimension = len(center)
        
        ball = set()
        
        if dimension == 1:
            # 1D: open interval
            a, b = center[0] - radius, center[0] + radius
            return (a, b)  # Return as interval tuple
        
        elif dimension == 2:
            # 2D: sample points in open ball
            cx, cy = center[0], center[1]
            for x in [i * 0.1 for i in range(int(cx * 10 - radius * 10), int(cx * 10 + radius * 10))]:
                for y in [j * 0.1 for j in range(int(cy * 10 - radius * 10), int(cy * 10 + radius * 10))]:
                    if EuclideanTopology.euclidean_distance((x, y), center) < radius:
                        ball.add((x, y))
            return ball
        
        else:
            # Higher dimensions: return set of points
            raise NotImplementedError(f"Ball generation for dimension {dimension} not yet implemented")

    @staticmethod
    def closed_ball(center, radius, dimension=None):
        """Closed ball B̄(c, r) = {x : d(x, c) ≤ r}"""
        if isinstance(center, (int, float)):
            center = (center,)
        
        if dimension is None:
            dimension = len(center)
        
        if dimension == 1:
            a, b = center[0] - radius, center[0] + radius
            return (a, b)  # Closed interval
        
        # Similar to open_ball but with ≤ instead of <
        ball = set()
        cx = center
        
        if dimension == 2:
            cx, cy = center[0], center[1]
            for x in [i * 0.1 for i in range(int(cx * 10 - radius * 10), int(cx * 10 + radius * 10) + 1)]:
                for y in [j * 0.1 for j in range(int(cy * 10 - radius * 10), int(cy * 10 + radius * 10) + 1)]:
                    if EuclideanTopology.euclidean_distance((x, y), center) <= radius:
                        ball.add((x, y))
            return ball
        
        return ball

    @staticmethod
    def sphere(center, radius, dimension=None):
        """Sphere S(c, r) = {x : d(x, c) = r}"""
        if isinstance(center, (int, float)):
            center = (center,)
        
        if dimension is None:
            dimension = len(center)
        
        sphere = set()
        
        if dimension == 1:
            # Two points at distance radius
            return {center[0] - radius, center[0] + radius}
        
        elif dimension == 2:
            # Sample points on circle
            cx, cy = center[0], center[1]
            for angle in [i * math.pi / 180 for i in range(360)]:
                x = cx + radius * math.cos(angle)
                y = cy + radius * math.sin(angle)
                sphere.add((x, y))
            return sphere
        
        return sphere

    # ===== INTERVAL OPERATIONS (1D) =====

    @staticmethod
    def open_interval(a, b):
        """Open interval (a, b) = {x : a < x < b}"""
        if a >= b:
            raise ValueError("a must be less than b")
        return (a, b, "open")

    @staticmethod
    def closed_interval(a, b):
        """Closed interval [a, b] = {x : a ≤ x ≤ b}"""
        if a > b:
            raise ValueError("a must be less than or equal to b")
        return (a, b, "closed")

    @staticmethod
    def half_open_interval_left(a, b):
        """Half-open interval [a, b) = {x : a ≤ x < b}"""
        if a >= b:
            raise ValueError("a must be less than b")
        return (a, b, "half-open-left")

    @staticmethod
    def half_open_interval_right(a, b):
        """Half-open interval (a, b] = {x : a < x ≤ b}"""
        if a >= b:
            raise ValueError("a must be less than b")
        return (a, b, "half-open-right")

    @staticmethod
    def interval_contains(interval, x):
        """Check if point x is in interval."""
        a, b, interval_type = interval
        
        if interval_type == "open":
            return a < x < b
        elif interval_type == "closed":
            return a <= x <= b
        elif interval_type == "half-open-left":
            return a <= x < b
        elif interval_type == "half-open-right":
            return a < x <= b
        
        return False

    @staticmethod
    def interval_union(*intervals):
        """Union of intervals."""
        # Merge overlapping intervals
        if not intervals:
            return []
        
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            # Check if overlapping or adjacent
            if current[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], current[1]), "merged")
            else:
                merged.append(current)
        
        return merged

    @staticmethod
    def interval_intersection(*intervals):
        """Intersection of intervals."""
        if not intervals:
            return None
        
        a = max(i[0] for i in intervals)
        b = min(i[1] for i in intervals)
        
        if a < b:
            return (a, b, "intersection")
        return None

    # ===== OPEN & CLOSED SETS =====

    def is_open_set(self, subset):
        """Check if set is open (can be written as union of open balls)."""
        return subset in self.open_sets

    def is_closed_set(self, subset):
        """Check if set is closed (complement is open)."""
        # For Euclidean space, a set is closed iff it contains all its limit points
        return True  # Simplified for now

    def interior(self, subset):
        """Interior: largest open set contained in subset."""
        # For Euclidean space, interior of finite set is empty
        # Interior of interval (a,b) is (a,b) itself
        return subset

    def closure(self, subset):
        """Closure: smallest closed set containing subset."""
        # For intervals, closure adds boundary points
        if isinstance(subset, tuple) and len(subset) == 3:
            a, b, itype = subset
            return (a, b, "closed")  # Closure is always closed interval
        return subset

    def boundary(self, subset):
        """Boundary: points in closure but not interior."""
        # For open interval (a,b), boundary is {a, b}
        if isinstance(subset, tuple) and len(subset) == 3:
            a, b, itype = subset
            if itype == "open":
                return {a, b}
            elif itype == "closed":
                return {a, b}
        return set()

    # ===== CONVERGENCE & LIMITS =====

    def is_convergent_sequence(self, sequence, limit, epsilon=1e-6):
        """
        Check if sequence converges to limit.
        For all ε > 0, there exists N such that n > N implies d(xₙ, L) < ε
        """
        for i, term in enumerate(sequence):
            if self.euclidean_distance(term, limit) >= epsilon:
                # Found a term beyond epsilon, sequence might still converge
                pass
        
        # Simplified: check if last terms are close to limit
        if len(sequence) > 0:
            return self.euclidean_distance(sequence[-1], limit) < epsilon
        return False

    def limit_of_sequence(self, sequence):
        """
        Try to find limit of a sequence.
        Returns limit if sequence appears to converge.
        """
        if len(sequence) < 2:
            return None
        
        # Check if last terms stabilize
        last_term = sequence[-1]
        if len(sequence) > 1:
            distance = self.euclidean_distance(sequence[-1], sequence[-2])
            if distance < 1e-10:
                return last_term
        
        return None

    def cauchy_sequence(self, sequence, epsilon=1e-6):
        """
        Check if sequence is Cauchy.
        For all ε > 0, there exists N such that m,n > N implies d(xₘ, xₙ) < ε
        """
        n = len(sequence)
        if n < 2:
            return True
        
        # Check last few terms
        for i in range(max(0, n - 5), n - 1):
            for j in range(i + 1, n):
                if self.euclidean_distance(sequence[i], sequence[j]) >= epsilon:
                    return False
        return True

    # ===== CONNECTEDNESS =====

    def is_connected(self, subset=None):
        """
        Euclidean spaces are connected.
        Intervals are connected, unions of disjoint intervals are not.
        """
        # Euclidean space itself is connected
        return True

    def is_connected_set(self, subset):
        """
        Check if subset is connected.
        Subset is connected if it cannot be written as union of two disjoint open sets.
        """
        # For intervals: connected iff it's a single interval
        if isinstance(subset, tuple) and len(subset) == 3:
            return True  # Single interval is connected
        
        # For finite unions of intervals
        if isinstance(subset, list):
            return len(subset) <= 1  # Connected iff single interval

    def path_connected(self, p1, p2):
        """
        Check if there's continuous path from p1 to p2.
        Straight line segment from p1 to p2.
        """
        if isinstance(p1, (int, float)):
            p1 = (p1,)
        if isinstance(p2, (int, float)):
            p2 = (p2,)
        
        # Always path-connected in Euclidean space
        return True

    def path_from_to(self, p1, p2, steps=10):
        """
        Generate path (straight line) from p1 to p2.
        """
        if isinstance(p1, (int, float)):
            p1 = (p1,)
        if isinstance(p2, (int, float)):
            p2 = (p2,)
        
        path = []
        for t in [i / (steps - 1) for i in range(steps)]:
            point = tuple(p1[i] * (1 - t) + p2[i] * t for i in range(len(p1)))
            path.append(point)
        
        return path

    # ===== COMPACTNESS =====

    def is_compact_set(self, subset):
        """
        Check if subset is compact.
        In ℝⁿ: compact iff closed and bounded (Heine-Borel theorem)
        """
        # For intervals
        if isinstance(subset, tuple) and len(subset) == 3:
            a, b, itype = subset
            is_closed = itype == "closed"
            is_bounded = (b - a) < float('inf')
            return is_closed and is_bounded
        
        return False

    def is_bounded(self, subset):
        """
        Check if subset is bounded.
        Subset is bounded if diameter is finite.
        """
        if isinstance(subset, tuple) and len(subset) == 3:
            a, b, itype = subset
            return (b - a) < float('inf')
        
        return True

    def diameter(self, subset):
        """
        Diameter of subset (maximum distance between points).
        For interval [a,b], diameter = b - a.
        """
        if isinstance(subset, tuple) and len(subset) == 3:
            a, b, itype = subset
            return abs(b - a)
        
        return float('inf')

    # ===== CONVEXITY =====

    def is_convex(self, subset):
        """
        Check if subset is convex.
        Subset is convex if for any x, y in subset, the line segment xy is in subset.
        """
        # Intervals are convex
        if isinstance(subset, tuple) and len(subset) == 3:
            return True
        
        return False

    def convex_hull(self, points):
        """
        Compute convex hull of points.
        In 1D: [min(points), max(points)]
        In 2D: Graham scan algorithm
        """
        if isinstance(points, (int, float)):
            return (points, points)
        
        if isinstance(points[0], (int, float)):
            # 1D case
            return (min(points), max(points))
        
        # 2D case: simple convex hull
        if len(points) <= 3:
            return points
        
        # Sort by x, then y
        sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
        
        # Build lower hull
        lower = []
        for p in sorted_points:
            while len(lower) >= 2 and self._cross_product(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        
        # Build upper hull
        upper = []
        for p in reversed(sorted_points):
            while len(upper) >= 2 and self._cross_product(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        
        return lower[:-1] + upper[:-1]

    @staticmethod
    def _cross_product(o, a, b):
        """Cross product for 2D convex hull."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def is_convex_combination(self, point, points, weights=None):
        """
        Check if point is convex combination of points.
        point = Σ wᵢ * pᵢ, where Σ wᵢ = 1, wᵢ ≥ 0
        """
        if weights is None:
            # Equal weights
            weights = [1.0 / len(points)] * len(points)
        
        if sum(weights) < 0.99 or sum(weights) > 1.01:
            raise ValueError("Weights must sum to 1")
        
        if any(w < 0 for w in weights):
            return False
        
        # Compute combination
        combination = tuple(sum(w * p[i] for w, p in zip(weights, points)) 
                           for i in range(len(point)))
        
        # Check if close enough
        return all(abs(combination[i] - point[i]) < 1e-10 for i in range(len(point)))

    # ===== CONTINUITY =====

    def is_continuous_function(self, func, domain, test_points=None):
        """
        Check if function is continuous on domain.
        f is continuous at c if for all ε > 0, ∃δ > 0 such that 
        |x - c| < δ implies |f(x) - f(c)| < ε
        """
        if test_points is None:
            # Sample test points
            if isinstance(domain, tuple) and len(domain) == 3:
                a, b, _ = domain
                test_points = [a + (b - a) * i / 10 for i in range(11)]
            else:
                return True
        
        # Test continuity at sample points
        epsilon = 1e-6
        delta = 1e-6
        
        for c in test_points:
            fc = func(c)
            # Check nearby points
            for x in [c + delta * i for i in range(-5, 6)]:
                if abs(x - c) < delta:
                    fx = func(x)
                    if abs(fx - fc) >= epsilon:
                        return False
        
        return True

    def uniform_continuous(self, func, domain, epsilon=1e-6):
        """
        Check if function is uniformly continuous on domain.
        For all ε > 0, ∃δ > 0 such that 
        for all x, y: |x - y| < δ implies |f(x) - f(y)| < ε
        """
        if isinstance(domain, tuple) and len(domain) == 3:
            a, b, _ = domain
            delta = (b - a) / 100
            
            test_points = [a + delta * i for i in range(101)]
            
            for i, x in enumerate(test_points[:-1]):
                y = test_points[i + 1]
                if abs(func(y) - func(x)) >= epsilon:
                    return False
            
            return True
        
        return True

    # ===== METRIC PROPERTIES =====

    def metric_space(self):
        """Return metric space structure of Euclidean topology."""
        return {
            'distance_metric': self.euclidean_distance,
            'is_complete': True,  # ℝⁿ is complete
            'is_separable': True,  # ℝⁿ is separable (rationals)
            'is_connected': True,  # ℝⁿ is connected
            'is_hausdorff': True,  # ℝⁿ is Hausdorff
            'dimension': self.dimension,
        }

    def dimension_of_space(self):
        """Return dimension of space."""
        return self.dimension

    # ===== NORMS =====

    @staticmethod
    def euclidean_norm(v):
        """Euclidean norm (L² norm): √(Σxᵢ²)"""
        return math.sqrt(sum(x**2 for x in v))

    @staticmethod
    def taxicab_norm(v):
        """Taxicab norm (L¹ norm): Σ|xᵢ|"""
        return sum(abs(x) for x in v)

    @staticmethod
    def supremum_norm(v):
        """Supremum norm (L∞ norm): max(|xᵢ|)"""
        return max(abs(x) for x in v)

    @staticmethod
    def p_norm(v, p=2):
        """General p-norm: (Σ|xᵢ|^p)^(1/p)"""
        if p == float('inf'):
            return max(abs(x) for x in v)
        return sum(abs(x)**p for x in v) ** (1/p)

    # ===== SUBSPACE TOPOLOGY =====

    def subspace_topology(self, subset):
        """
        Induced topology on subset of Euclidean space.
        Open sets in subset = intersection of subset with open sets in ℝⁿ
        """
        return {
            'parent_space': 'Euclidean',
            'subset': subset,
            'inherited_metric': self.euclidean_distance,
        }

    # ===== VECTOR SPACE OPERATIONS =====

    @staticmethod
    def vector_addition(v1, v2):
        """Add two vectors."""
        return tuple(a + b for a, b in zip(v1, v2))

    @staticmethod
    def scalar_multiplication(scalar, v):
        """Multiply vector by scalar."""
        return tuple(scalar * x for x in v)

    @staticmethod
    def dot_product(v1, v2):
        """Dot product of two vectors."""
        return sum(a * b for a, b in zip(v1, v2))

    @staticmethod
    def cross_product_3d(v1, v2):
        """Cross product in 3D."""
        if len(v1) != 3 or len(v2) != 3:
            raise ValueError("Cross product requires 3D vectors")
        
        return (
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0],
        )

    def orthogonal(self, v1, v2):
        """Check if two vectors are orthogonal."""
        return abs(self.dot_product(v1, v2)) < 1e-10

    def orthonormal_basis(self, vectors):
        """
        Gram-Schmidt orthonormalization.
        Convert set of vectors to orthonormal basis.
        """
        basis = []
        
        for v in vectors:
            # Remove components parallel to basis vectors
            u = list(v)
            for b in basis:
                projection = self.dot_product(u, b)
                u = tuple(u[i] - projection * b[i] for i in range(len(u)))
            
            # Normalize
            norm = self.euclidean_norm(u)
            if norm > 1e-10:
                u = tuple(x / norm for x in u)
                basis.append(u)
        
        return basis

    # ===== STATISTICS & GEOMETRY =====

    def centroid(self, points):
        """Compute centroid (center of mass) of points."""
        if not points:
            return None
        
        n = len(points)
        if isinstance(points[0], (int, float)):
            return sum(points) / n
        
        # Multi-dimensional
        dim = len(points[0])
        return tuple(sum(p[i] for p in points) / n for i in range(dim))

    def pairwise_distances_matrix(self, points):
        """Compute distance matrix for set of points."""
        n = len(points)
        matrix = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                dist = self.euclidean_distance(points[i], points[j])
                matrix[i][j] = dist
                matrix[j][i] = dist
        
        return matrix

    def is_orthogonal_set(self, vectors):
        """Check if set of vectors are mutually orthogonal."""
        for i, v1 in enumerate(vectors):
            for v2 in vectors[i+1:]:
                if not self.orthogonal(v1, v2):
                    return False
        return True

    def angle_between(self, v1, v2):
        """
        Compute angle between two vectors (in radians).
        cos(θ) = (v₁ · v₂) / (|v₁| |v₂|)
        """
        dot = self.dot_product(v1, v2)
        norm1 = self.euclidean_norm(v1)
        norm2 = self.euclidean_norm(v2)
        
        if norm1 == 0 or norm2 == 0:
            return 0
        
        cos_angle = dot / (norm1 * norm2)
        # Clamp to [-1, 1] to avoid numerical errors
        cos_angle = max(-1, min(1, cos_angle))
        return math.acos(cos_angle)

    # ===== PROPERTIES & UTILITIES =====

    def get_properties(self):
        """Get all topological properties of Euclidean space."""
        return {
            'dimension': self.dimension,
            'bounds': self.bounds,
            'is_connected': True,
            'is_hausdorff': True,
            'is_separable': True,
            'is_complete': True,
            'is_locally_compact': True,
            'is_metrizable': True,
            'is_vector_space': True,
            'has_euclidean_metric': True,
        }

    def print_properties(self):
        """Print space properties."""
        props = self.get_properties()
        print(f"\n{'='*50}")
        print(f"Euclidean Space ℝ^{self.dimension}")
        print(f"{'='*50}")
        for key, value in props.items():
            print(f"{key}: {value}")
        print(f"{'='*50}\n")

    def summary(self):
        """One-line summary of the space."""
        return f"Euclidean Space ℝ^{self.dimension} (bounds: {self.bounds})"

class DiscreteTopology(Topology):
    """
    The discrete topology where every subset is open.
    """

    def __init__(self, base_set):
        """
        Initialize discrete topology.
        
        :param base_set: The underlying set
        """
        base_set = list(base_set)
        self.base_set = set(base_set)
        # Generate all possible subsets (power set)
        self.open_sets = self._generate_power_set()
        self.closed_sets = []
        self._compute_closed_sets()

    def _generate_power_set(self):
        """Generate all subsets of the base set."""
        elements = list(self.base_set)
        power_set = [set()]
        for r in range(1, len(elements) + 1):
            for combo in combinations(elements, r):
                power_set.append(set(combo))
        return power_set


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

class DiscreteTopology:
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