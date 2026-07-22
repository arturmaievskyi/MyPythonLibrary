from .topology_imports import*


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

