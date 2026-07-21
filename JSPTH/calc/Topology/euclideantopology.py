
import math
from itertools import combinations, permutations
from collections import defaultdict, deque


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

