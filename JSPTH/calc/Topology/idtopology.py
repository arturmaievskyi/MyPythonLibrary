from .topology_imports import *

class IndiscreteTopology(Topology):
    """
    The indiscrete (trivial) topology on a set.
    
    Properties:
    - Only empty set and whole space are open
    - Coarsest possible topology
    - Every point is a limit point (except in single-point space)
    - NOT Hausdorff (unless single point)
    - Connected (always)
    - Compact (always)
    - Separable (always)
    - NOT metrizable (unless finite)
    
    Applications:
    - Theoretical foundation for topology
    - Baseline for convergence studies
    - Teaching topology concepts
    - Comparison with other topologies
    """

    def __init__(self, base_set, name="IndiscreteTopology"):
        """
        Initialize indiscrete topology.
        
        :param base_set: The underlying set (finite or countable)
        :param name: Name for the space
        """
        self.base_set = set(base_set) if not isinstance(base_set, set) else base_set
        self.name = name
        self.size = len(self.base_set)
        
        # In indiscrete topology: only empty set and full set are open
        self.open_sets = [set(), self.base_set]
        
        # Compute closed sets (complements of open sets)
        self.closed_sets = []
        self._compute_closed_sets()

    def _compute_closed_sets(self):
        """Compute closed sets as complements of open sets."""
        self.closed_sets = []
        for open_set in self.open_sets:
            closed_set = self.base_set - open_set
            self.closed_sets.append(closed_set)

    # ===== BASIC TOPOLOGICAL PROPERTIES =====

    def is_open_set(self, subset):
        """Check if subset is open (must be ∅ or X)."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return subset_set == set() or subset_set == self.base_set

    def is_closed_set(self, subset):
        """Check if subset is closed (must be X or ∅)."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return subset_set == self.base_set or subset_set == set()

    def is_clopen_set(self, subset):
        """Check if subset is both open and closed."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return (subset_set == set() or subset_set == self.base_set)

    def get_all_clopen_sets(self):
        """Get all sets that are both open and closed."""
        return [set(), self.base_set]

    # ===== INTERIOR, CLOSURE, BOUNDARY =====

    def interior(self, subset):
        """
        Interior: largest open set contained in subset.
        In indiscrete topology:
        - interior(X) = X
        - interior(∅) = ∅
        - interior(any proper subset) = ∅
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        if subset_set == self.base_set:
            return self.base_set
        elif len(subset_set) == 0:
            return set()
        else:
            return set()  # No proper subset is open

    def closure(self, subset):
        """
        Closure: smallest closed set containing subset.
        In indiscrete topology:
        - closure(∅) = ∅
        - closure(any non-empty set) = X
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        if len(subset_set) == 0:
            return set()
        else:
            return self.base_set  # Closure of any non-empty set is X

    def boundary(self, subset):
        """
        Boundary: points in closure but not interior.
        In indiscrete topology:
        - boundary(∅) = ∅
        - boundary(X) = ∅
        - boundary(any proper non-empty subset) = X
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        closure_set = self.closure(subset_set)
        interior_set = self.interior(subset_set)
        
        return closure_set - interior_set

    def derived_set(self, subset):
        """
        Derived set: all limit points of subset.
        In indiscrete topology:
        - derived_set(∅) = ∅
        - derived_set(any non-empty set) = X \ {that single point if singleton}
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        if len(subset_set) == 0:
            return set()
        elif len(subset_set) == 1:
            # For singleton: limit point is the whole space minus the point
            # (unless space is single point)
            if self.size == 1:
                return set()
            else:
                return self.base_set
        else:
            # For non-singleton subset: all points are limit points
            return self.base_set

    # ===== LIMIT POINTS & CONVERGENCE =====

    def is_limit_point(self, point, subset):
        """
        Check if point is a limit point of subset.
        Point p is limit point of A if every neighborhood of p intersects A\{p}
        
        In indiscrete topology: only neighborhood is X
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        if self.size == 1:
            return False
        
        # X always intersects A\{p} for any non-empty A
        if len(subset_set) <= 1:
            return False
        else:
            return True

    def get_limit_points(self, subset):
        """Get all limit points of a subset."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        limit_points = set()
        
        for point in self.base_set:
            if self.is_limit_point(point, subset_set):
                limit_points.add(point)
        
        return limit_points

    def converges_to(self, sequence, limit_point):
        """
        Check if sequence converges to limit point.
        In indiscrete topology: every sequence converges to every point!
        """
        return True  # This is a key property of indiscrete topology

    def get_limits(self, sequence):
        """Get all possible limits of a sequence (all points in X)."""
        return self.base_set

    # ===== NEIGHBORHOODS =====

    def neighborhood(self, point):
        """
        Get all neighborhoods of a point.
        In indiscrete topology: only neighborhood is X
        """
        return [self.base_set]

    def open_neighborhood(self, point):
        """Get all open neighborhoods (only X)."""
        return [self.base_set]

    def is_neighborhood(self, point, subset):
        """Check if subset is neighborhood (must contain X)."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return subset_set == self.base_set

    # ===== SEPARATION AXIOMS =====

    def is_t0(self):
        """T0 (Kolmogorov): For any two distinct points, one has neighborhood not containing the other."""
        return self.size <= 1  # Only true for single point

    def is_t1(self):
        """T1: For any two distinct points, each has neighborhood not containing the other."""
        return self.size <= 1

    def is_t2_hausdorff(self):
        """T2 (Hausdorff): Any two distinct points have disjoint neighborhoods."""
        return self.size <= 1

    def is_t3(self):
        """T3 (Regular): Disjoint closed sets have disjoint neighborhoods."""
        return self.size <= 1

    def is_t4(self):
        """T4 (Normal): Disjoint closed sets have disjoint neighborhoods."""
        return self.size <= 1

    def separation_axioms(self):
        """Get all separation properties."""
        return {
            'T0 (Kolmogorov)': self.is_t0(),
            'T1': self.is_t1(),
            'T2 (Hausdorff)': self.is_t2_hausdorff(),
            'T3 (Regular)': self.is_t3(),
            'T4 (Normal)': self.is_t4(),
        }

    # ===== CONNECTIVITY =====

    def is_connected(self):
        """Check if space is connected (always true for indiscrete)."""
        return True

    def is_path_connected(self):
        """Check if space is path-connected (always true)."""
        return True

    def connected_components(self):
        """Get connected components (only one: the whole space)."""
        if self.size == 0:
            return []
        return [self.base_set]

    def is_locally_connected(self, point):
        """Check if space is locally connected at point."""
        return True

    def is_totally_disconnected(self):
        """Check if space is totally disconnected."""
        return self.size <= 1

    # ===== COMPACTNESS =====

    def is_compact(self):
        """Check if space is compact (always true)."""
        return True

    def is_locally_compact(self):
        """Check if space is locally compact."""
        return True

    def is_countably_compact(self):
        """Check if space is countably compact (always true)."""
        return True

    def is_sequentially_compact(self):
        """Check if space is sequentially compact (always true)."""
        return True

    def is_bounded(self):
        """Check if space is bounded (always true for finite spaces)."""
        return self.size < float('inf')

    # ===== SEPARABILITY & COUNTABILITY =====

    def is_separable(self):
        """Has countable dense subset (always true for countable spaces)."""
        return True

    def is_countable(self):
        """Check if space is countable."""
        return True

    def has_countable_base(self):
        """Has countable base for topology (only 2 sets, so yes)."""
        return True

    def density(self):
        """Smallest cardinality of dense subset (1 if non-empty)."""
        if self.size == 0:
            return 0
        return 1  # Single point is dense in indiscrete topology

    # ===== SUBSPACE TOPOLOGY =====

    def subspace(self, subset):
        """
        Get subspace topology on subset.
        Indiscrete topology induces indiscrete topology on subsets.
        """
        return IndiscreteTopology(subset, name=f"{self.name} (subspace)")

    def is_subspace_of(self, other):
        """Check if this is a subspace of another."""
        if not isinstance(other, IndiscreteTopology):
            return False
        return self.base_set.issubset(other.base_set)

    def is_dense_in(self, other):
        """Check if this is dense in another space."""
        if not isinstance(other, IndiscreteTopology):
            return False
        if len(self.base_set) == 0:
            return False
        # In indiscrete topology, any non-empty subset is dense
        return self.base_set.issubset(other.base_set)

    # ===== CONTINUOUS FUNCTIONS =====

    def is_continuous_function(self, func, target_space, test_points=None):
        """
        Check if function is continuous to target space.
        f: X → Y is continuous if preimage of every open set in Y is open in X.
        
        Since only ∅ and X are open in indiscrete space:
        - Preimage of ∅ = ∅ (open in X)
        - Preimage of Y = X (open in X)
        All functions FROM indiscrete space are continuous!
        """
        return True  # All functions from indiscrete space are continuous

    def is_continuous_into_indiscrete(self, func):
        """
        Check if function is continuous into indiscrete space.
        All functions are continuous into indiscrete space!
        """
        return True

    def is_homeomorphic_to(self, other):
        """
        Check if homeomorphic to another space.
        Two indiscrete spaces homeomorphic iff same cardinality.
        """
        if not isinstance(other, IndiscreteTopology):
            return False
        return self.size == other.size

    # ===== METRICS & UNIFORMITY =====

    def is_metrizable(self):
        """Check if space is metrizable."""
        # Indiscrete spaces are not metrizable if size > 1
        return self.size <= 1

    def is_uniformizable(self):
        """Check if space has uniform structure."""
        return True  # All indiscrete spaces are uniformizable

    def is_pseudometrizable(self):
        """Check if space is pseudometrizable."""
        return True

    # ===== HOMOTOPY & FUNDAMENTAL GROUP =====

    def is_simply_connected(self):
        """Check if space is simply connected."""
        return True  # Indiscrete spaces are contractible

    def is_contractible(self):
        """Check if space is contractible."""
        return True

    def fundamental_group_trivial(self):
        """Check if fundamental group is trivial."""
        return True

    # ===== DIMENSION =====

    def dimension(self):
        """
        Topological dimension.
        Indiscrete space (n points) has dimension 0 (if n > 0).
        """
        if self.size == 0:
            return -1
        elif self.size == 1:
            return 0
        else:
            return 0  # No proper separation possible

    def is_zero_dimensional(self):
        """Check if space is zero-dimensional."""
        return True

    # ===== CONVERGENCE FILTERS & NETS =====

    def filter_converges_to(self, filter_base, point):
        """
        Check if filter converges to point.
        In indiscrete topology: every filter converges to every point!
        """
        return True

    def net_converges_to(self, net, point):
        """
        Check if net converges to point.
        In indiscrete topology: every net converges to every point!
        """
        return True

    def all_filter_limits(self, filter_base):
        """Get all limits of a filter (all points in X)."""
        return self.base_set

    def all_net_limits(self, net):
        """Get all limits of a net (all points in X)."""
        return self.base_set

    # ===== UNIFORM STRUCTURES =====

    def uniform_distance(self, p1, p2):
        """Uniform distance (0 if same, ∞ otherwise, but we use 1 and 0)."""
        return 0 if p1 == p2 else 1

    def uniform_structure(self):
        """Get uniform structure."""
        return {
            'type': 'indiscrete_uniform',
            'entourage_zero': [(p, p) for p in self.base_set],
            'entourage_full': [(p, q) for p in self.base_set for q in self.base_set],
        }

    # ===== PROPERTIES & UTILITIES =====

    def get_properties(self):
        """Get all topological properties."""
        return {
            'name': self.name,
            'is_indiscrete': True,
            'cardinality': self.size,
            'is_connected': True,
            'is_compact': True,
            'is_path_connected': True,
            'is_separable': True,
            'is_t0': self.is_t0(),
            'is_t1': self.is_t1(),
            'is_hausdorff': self.is_t2_hausdorff(),
            'is_metrizable': self.is_metrizable(),
            'is_contractible': True,
            'is_simply_connected': True,
            'is_zero_dimensional': True,
            'dimension': self.dimension(),
            'all_functions_continuous': True,
            'every_sequence_converges_everywhere': True,
        }

    def print_properties(self):
        """Print all properties in readable format."""
        props = self.get_properties()
        print(f"\n{'='*60}")
        print(f"Indiscrete Topology: {self.name}")
        print(f"{'='*60}")
        for key, value in props.items():
            print(f"{key}: {value}")
        print(f"{'='*60}\n")

    def describe(self):
        """Detailed description of the space."""
        desc = f"\n{'='*60}\n"
        desc += f"Indiscrete Topology: {self.name}\n"
        desc += f"{'='*60}\n"
        desc += f"Number of points: {self.size}\n"
        desc += f"Number of open sets: {len(self.open_sets)}\n"
        desc += f"Number of closed sets: {len(self.closed_sets)}\n"
        desc += f"Is connected: True\n"
        desc += f"Is compact: True\n"
        desc += f"Is Hausdorff: {self.is_t2_hausdorff()}\n"
        desc += f"Is metrizable: {self.is_metrizable()}\n"
        desc += f"All functions from X are continuous: True\n"
        desc += f"All functions to X are continuous: True\n"
        desc += f"Every sequence converges to every point: True\n"
        desc += f"{'='*60}\n"
        return desc

    def summary(self):
        """One-line summary."""
        return f"Indiscrete Topology: {self.name} with {self.size} points"

    def export_to_dict(self):
        """Export space as dictionary."""
        return {
            'name': self.name,
            'base_set': list(self.base_set),
            'cardinality': self.size,
            'open_sets': [list(s) for s in self.open_sets],
            'closed_sets': [list(s) for s in self.closed_sets],
            'properties': self.get_properties(),
        }

    # ===== COMPARISON WITH OTHER TOPOLOGIES =====

    def compare_with_discrete(self):
        """Compare with discrete topology on same set."""
        
        discrete = DiscreteTopology(self.base_set)
        
        return {
            'name': self.name,
            'indiscrete_open_sets': len(self.open_sets),
            'discrete_open_sets': len(discrete.open_sets),
            'indiscrete_is_coarser': len(self.open_sets) < len(discrete.open_sets),
            'all_indiscrete_open_are_discrete_open': all(
                s in discrete.open_sets for s in self.open_sets
            ),
        }

    def coarser_than(self, other):
        """Check if this topology is coarser (fewer open sets) than other."""
        if not hasattr(other, 'open_sets'):
            return False
        return len(self.open_sets) < len(other.open_sets)

    def finer_than(self, other):
        """Check if this topology is finer (more open sets) than other."""
        if not hasattr(other, 'open_sets'):
            return False
        return len(self.open_sets) > len(other.open_sets)

    # ===== SPECIAL OPERATIONS =====

    def identify_points(self, p1, p2):
        """
        Create quotient space by identifying two points.
        Result still has indiscrete topology.
        """
        new_set = self.base_set - {p1, p2}
        new_set.add(f"({p1},{p2})")  # Identified point
        return IndiscreteTopology(new_set, name=f"{self.name} (quotient)")

    def coproduct_with(self, other):
        """
        Create coproduct (disjoint union) with another space.
        Result is indiscrete topology on union.
        """
        if not isinstance(other, IndiscreteTopology):
            raise TypeError("Both spaces must be IndiscreteTopology")
        
        # Tag points to keep them distinct
        tagged_base = (
            {f"X:{p}" for p in self.base_set} |
            {f"Y:{p}" for p in other.base_set}
        )
        return IndiscreteTopology(tagged_base, name=f"{self.name} ⊔ {other.name}")

    def product_with(self, other):
        """
        Create product topology with another space.
        Product of indiscrete spaces is indiscrete.
        """
        if not isinstance(other, IndiscreteTopology):
            raise TypeError("Both spaces must be IndiscreteTopology")
        
        product_set = {(p, q) for p in self.base_set for q in other.base_set}
        return IndiscreteTopology(product_set, name=f"{self.name} × {other.name}")

    # ===== QUOTIENT SPACES =====

    def quotient_by_equivalence(self, equivalence_classes):
        """
        Create quotient space by equivalence relation.
        Result is indiscrete (if had indiscrete before).
        """
        return IndiscreteTopology(
            equivalence_classes,
            name=f"{self.name} / ~"
        )
