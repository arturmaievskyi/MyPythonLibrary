from .topology_imports import *

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
            return Other_functions.chebyshev_metric(p1, p2)
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

