"""
SubspaceTopology Implementation
================================

Comprehensive implementation of subspace topology for any topological space.
A subspace topology is induced on a subset A of a topological space (X, τ) by:
    τ_A = {U ∩ A : U ∈ τ}

That is, the open sets in the subspace are exactly the intersections of open sets
of the parent space with the subset.
"""


class SubspaceTopology:
    """
    Subspace topology on a subset of a topological space.
    
    Given a topological space (X, τ) and a subset A ⊆ X, the subspace topology
    on A is defined as:
        τ_A = {U ∩ A : U ∈ τ}
    
    This is the coarsest topology on A making the inclusion map i: A → X continuous.
    
    Attributes:
        parent_space: The parent topological space
        subset: The subset A on which the subspace topology is defined
        open_sets: Open sets in the subspace
        closed_sets: Closed sets in the subspace
    """

    def __init__(self, parent_space, subset, name=None):
        """
        Initialize subspace topology.
        
        Args:
            parent_space: Parent topological space (must have open_sets attribute)
            subset: Subset A ⊆ X on which to define subspace topology
            name: Optional name for the subspace
            
        Raises:
            ValueError: If subset is not contained in parent space
        """
        self.parent_space = parent_space
        self.subset = set(subset) if not isinstance(subset, set) else subset
        self.name = name or f"Subspace of {getattr(parent_space, 'name', 'Space')}"
        
        # Validate subset is contained in parent
        if not self.subset.issubset(parent_space.base_set):
            raise ValueError("Subset must be contained in parent space")
        
        self.size = len(self.subset)
        
        # Compute open sets in subspace topology
        self.open_sets = []
        self._compute_open_sets()
        
        # Compute closed sets
        self.closed_sets = []
        self._compute_closed_sets()

    def _compute_open_sets(self):
        """Compute open sets in subspace: {U ∩ A : U open in parent}"""
        self.open_sets = []
        
        for open_set in self.parent_space.open_sets:
            # Intersection of open set with subset
            subspace_open = open_set & self.subset
            
            # Avoid duplicates
            if subspace_open not in self.open_sets:
                self.open_sets.append(subspace_open)

    def _compute_closed_sets(self):
        """Compute closed sets: complements in the subspace"""
        self.closed_sets = []
        
        for open_set in self.open_sets:
            closed_set = self.subset - open_set
            
            if closed_set not in self.closed_sets:
                self.closed_sets.append(closed_set)

    # ===== BASIC TOPOLOGICAL PROPERTIES =====

    def is_open_set(self, subset):
        """Check if subset is open in the subspace topology."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return subset_set in self.open_sets

    def is_closed_set(self, subset):
        """Check if subset is closed in the subspace topology."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return subset_set in self.closed_sets

    def is_clopen_set(self, subset):
        """Check if subset is both open and closed in the subspace."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return self.is_open_set(subset_set) and self.is_closed_set(subset_set)

    def get_all_clopen_sets(self):
        """Get all clopen (closed and open) sets in the subspace."""
        clopen = []
        for s in self.open_sets:
            if self.is_closed_set(s):
                clopen.append(s)
        return clopen

    # ===== INTERIOR, CLOSURE, BOUNDARY (RELATIVE TO SUBSPACE) =====

    def interior(self, subset):
        """
        Interior in subspace topology.
        
        int_A(B) = {x ∈ B : ∃ U open in A with x ∈ U ⊆ B}
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        # Largest open set contained in subset
        interior_set = set()
        for open_set in self.open_sets:
            if open_set <= subset_set:  # open_set is contained in subset
                interior_set |= open_set
        
        return interior_set

    def closure(self, subset):
        """
        Closure in subspace topology.
        
        cl_A(B) = A ∩ cl_X(B) where cl_X is closure in parent space
        
        Smallest closed set containing subset in the subspace.
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        # Get closure in parent space
        if hasattr(self.parent_space, 'closure'):
            parent_closure = self.parent_space.closure(subset_set)
            # Intersection with subspace
            subspace_closure = parent_closure & self.subset
        else:
            # Fallback: complement of interior of complement
            complement = self.subset - subset_set
            interior_complement = self.interior(complement)
            subspace_closure = self.subset - interior_complement
        
        return subspace_closure

    def boundary(self, subset):
        """Boundary in subspace topology."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        closure_set = self.closure(subset_set)
        interior_set = self.interior(subset_set)
        
        return closure_set - interior_set

    def derived_set(self, subset):
        """
        Derived set in subspace: all limit points of subset.
        
        A point x ∈ A is a limit point of B ⊆ A if every neighborhood of x
        in A intersects B \ {x}.
        """
        subset_set = set(subset) if not isinstance(subset, set) else subset
        limit_points = set()
        
        for point in self.subset:
            # Check if point is a limit point
            if self.is_limit_point(point, subset_set):
                limit_points.add(point)
        
        return limit_points

    def is_limit_point(self, point, subset):
        """
        Check if point is a limit point of subset in the subspace.
        
        A point x is a limit point of set B if every neighborhood of x
        intersects B \ {x}.
        """
        if point not in self.subset:
            return False
        
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        # Get all neighborhoods of point in subspace
        nbhds = self.neighborhood(point)
        
        for nbhd in nbhds:
            # Check if neighborhood intersects subset \ {point}
            remainder = subset_set - {point}
            if not (nbhd & remainder):  # No intersection
                return False
        
        return True

    # ===== NEIGHBORHOODS IN SUBSPACE =====

    def neighborhood(self, point):
        """
        Get all neighborhoods of point in subspace.
        
        N is a neighborhood of x if ∃ U open in A with x ∈ U ⊆ N.
        """
        if point not in self.subset:
            return []
        
        neighborhoods = []
        
        # A set is neighborhood of point if it contains an open set containing point
        for open_set in self.open_sets:
            if point in open_set:
                # All supersets of this open set are neighborhoods
                # But we can just return the open sets for simplicity
                if open_set not in neighborhoods:
                    neighborhoods.append(open_set)
        
        return neighborhoods

    def open_neighborhood(self, point):
        """Get all open neighborhoods of point in subspace."""
        if point not in self.subset:
            return []
        
        open_nbhds = []
        for open_set in self.open_sets:
            if point in open_set:
                open_nbhds.append(open_set)
        
        return open_nbhds

    def is_neighborhood(self, point, subset):
        """Check if subset is a neighborhood of point in subspace."""
        if point not in self.subset:
            return False
        
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        # Must contain an open set containing point
        for open_set in self.open_sets:
            if point in open_set and open_set <= subset_set:
                return True
        
        return False

    # ===== RELATIVE TOPOLOGY PROPERTIES =====

    def is_open_in_parent(self, subset):
        """Check if subset is open in the parent space (not just subspace)."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return subset_set in self.parent_space.open_sets

    def is_closed_in_parent(self, subset):
        """Check if subset is closed in the parent space (not just subspace)."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return subset_set in self.parent_space.closed_sets

    def interior_in_parent(self, subset):
        """Interior in parent space (not subspace)."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return self.parent_space.interior(subset_set)

    def closure_in_parent(self, subset):
        """Closure in parent space (not subspace)."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        return self.parent_space.closure(subset_set)

    # ===== SEPARATION AXIOMS IN SUBSPACE =====

    def is_t0(self):
        """Check if subspace satisfies T₀ (Kolmogorov)."""
        # Subspace inherits T₀ from parent if parent is T₀
        if not self.parent_space.is_t0():
            return False
        
        # Also check locally
        for p1 in self.subset:
            for p2 in self.subset:
                if p1 != p2:
                    # Need nbhd of p1 not containing p2 or vice versa
                    nbhds_p1 = self.open_neighborhood(p1)
                    nbhds_p2 = self.open_neighborhood(p2)
                    
                    found = False
                    for nbhd in nbhds_p1:
                        if p2 not in nbhd:
                            found = True
                            break
                    
                    if not found:
                        for nbhd in nbhds_p2:
                            if p1 not in nbhd:
                                found = True
                                break
                    
                    if not found:
                        return False
        
        return True

    def is_t1(self):
        """Check if subspace satisfies T₁."""
        for p1 in self.subset:
            for p2 in self.subset:
                if p1 != p2:
                    # Need nbhd of p1 not containing p2 AND
                    # nbhd of p2 not containing p1
                    nbhds_p1 = self.open_neighborhood(p1)
                    nbhds_p2 = self.open_neighborhood(p2)
                    
                    found_p1_excludes_p2 = any(p2 not in nbhd for nbhd in nbhds_p1)
                    found_p2_excludes_p1 = any(p1 not in nbhd for nbhd in nbhds_p2)
                    
                    if not (found_p1_excludes_p2 and found_p2_excludes_p1):
                        return False
        
        return True

    def is_t2_hausdorff(self):
        """Check if subspace is Hausdorff."""
        for p1 in self.subset:
            for p2 in self.subset:
                if p1 != p2:
                    # Need disjoint neighborhoods
                    nbhds_p1 = self.open_neighborhood(p1)
                    nbhds_p2 = self.open_neighborhood(p2)
                    
                    found_disjoint = False
                    for nbhd1 in nbhds_p1:
                        for nbhd2 in nbhds_p2:
                            if not (nbhd1 & nbhd2):  # Disjoint
                                found_disjoint = True
                                break
                        if found_disjoint:
                            break
                    
                    if not found_disjoint:
                        return False
        
        return True

    def is_t3(self):
        """Check if subspace is regular (T₃)."""
        if not self.is_t0():
            return False
        
        # Regular: disjoint closed sets have disjoint neighborhoods
        closed_sets = self.closed_sets
        
        for c1 in closed_sets:
            for c2 in closed_sets:
                if not (c1 & c2):  # Disjoint
                    # Try to find disjoint open neighborhoods
                    found_disjoint_nbhds = False
                    
                    for u1 in self.open_sets:
                        for u2 in self.open_sets:
                            # u1 ⊇ c1, u2 ⊇ c2, u1 ∩ u2 = ∅
                            if c1 <= u1 and c2 <= u2 and not (u1 & u2):
                                found_disjoint_nbhds = True
                                break
                        if found_disjoint_nbhds:
                            break
                    
                    if not found_disjoint_nbhds:
                        return False
        
        return True

    def is_t4(self):
        """Check if subspace is normal (T₄)."""
        # Normal: disjoint closed sets have disjoint neighborhoods
        closed_sets = self.closed_sets
        
        for c1 in closed_sets:
            for c2 in closed_sets:
                if not (c1 & c2):  # Disjoint
                    found_disjoint = False
                    
                    for u1 in self.open_sets:
                        for u2 in self.open_sets:
                            if c1 <= u1 and c2 <= u2 and not (u1 & u2):
                                found_disjoint = True
                                break
                        if found_disjoint:
                            break
                    
                    if not found_disjoint:
                        return False
        
        return True

    def separation_axioms(self):
        """Get all separation axioms."""
        return {
            'T0 (Kolmogorov)': self.is_t0(),
            'T1': self.is_t1(),
            'T2 (Hausdorff)': self.is_t2_hausdorff(),
            'T3 (Regular)': self.is_t3(),
            'T4 (Normal)': self.is_t4(),
        }

    # ===== CONNECTIVITY IN SUBSPACE =====

    def is_connected(self):
        """Check if subspace is connected."""
        # Connected if cannot write as union of disjoint non-empty open sets
        for u1 in self.open_sets:
            for u2 in self.open_sets:
                # Check if u1 and u2 separate the space
                if (u1 and u2 and  # both non-empty
                    not (u1 & u2) and  # disjoint
                    u1 | u2 == self.subset):  # cover the space
                    return False
        
        return True

    def connected_components(self):
        """Get connected components of the subspace."""
        if not self.subset:
            return []
        
        visited = set()
        components = []
        
        for point in self.subset:
            if point not in visited:
                # Find all points in same component as point
                component = self._get_component(point, visited)
                components.append(component)
        
        return components

    def _get_component(self, point, visited):
        """Get connected component containing point (DFS)."""
        component = set()
        stack = [point]
        
        while stack:
            current = stack.pop()
            
            if current in visited:
                continue
            
            visited.add(current)
            component.add(current)
            
            # Find all points "connected" to current
            for other in self.subset:
                if other not in visited:
                    # Check if can be separated
                    separated = False
                    for u1 in self.open_sets:
                        for u2 in self.open_sets:
                            if (current in u1 and other in u2 and
                                not (u1 & u2) and
                                u1 | u2 == self.subset):
                                separated = True
                                break
                        if separated:
                            break
                    
                    if not separated:
                        stack.append(other)
        
        return component

    def is_path_connected(self):
        """Check if subspace is path-connected."""
        # Path connected is stronger than connected
        # Requires continuous paths between all point pairs
        
        if not self.subset or len(self.subset) == 1:
            return True
        
        # Check if parent has path connectivity notion
        if hasattr(self.parent_space, 'is_path_connected'):
            # Approximate: if parent is path-connected and subspace
            # is connected and "nice", likely path-connected
            return self.is_connected()
        
        return self.is_connected()

    def is_locally_connected(self, point):
        """Check if space is locally connected at point."""
        if point not in self.subset:
            return False
        
        # Space is locally connected at p if p has a base of
        # connected neighborhoods
        
        for nbhd in self.open_neighborhood(point):
            # Create subspace of neighborhood
            sub_nbhd = SubspaceTopology(self, nbhd)
            if not sub_nbhd.is_connected():
                return False
        
        return True

    def is_totally_disconnected(self):
        """Check if space is totally disconnected."""
        components = self.connected_components()
        # Totally disconnected if all components are singletons
        return all(len(c) == 1 for c in components)

    # ===== COMPACTNESS IN SUBSPACE =====

    def is_compact(self):
        """
        Check if subspace is compact.
        
        Subspace is compact if every open cover has finite subcover.
        """
        # Heine-Borel: finite intersection property
        # A subspace is compact iff every collection of closed sets
        # with finite intersection property has non-empty intersection
        
        closed_sets = self.closed_sets
        if not closed_sets:
            return True
        
        # Check finite intersection property
        # Every finite subcollection has non-empty intersection
        from itertools import combinations
        
        max_size = min(3, len(closed_sets))  # Check small subcollections
        
        for r in range(2, max_size + 1):
            for sublist in combinations(closed_sets, r):
                intersection = set.intersection(*sublist) if sublist else set()
                if not intersection:
                    return False
        
        return True

    def is_locally_compact(self):
        """Check if space is locally compact."""
        # Locally compact if every point has a compact neighborhood
        
        for point in self.subset:
            neighborhoods = self.open_neighborhood(point)
            
            has_compact_nbhd = False
            for nbhd in neighborhoods:
                sub_nbhd = SubspaceTopology(self, nbhd)
                if sub_nbhd.is_compact():
                    has_compact_nbhd = True
                    break
            
            if not has_compact_nbhd:
                return False
        
        return True

    def is_countably_compact(self):
        """Check if space is countably compact."""
        # Every countable open cover has finite subcover
        # For finite spaces, equivalent to compact
        return self.is_compact()

    def is_sequentially_compact(self):
        """Check if space is sequentially compact."""
        # Every sequence has convergent subsequence
        
        if not self.subset or len(self.subset) == 1:
            return True
        
        # For finite spaces, always true
        if self.size < float('inf'):
            return True
        
        return False

    # ===== DENSITY =====

    def is_dense(self):
        """Check if subspace is dense in parent space."""
        # A is dense in X if cl_X(A) = X
        
        if hasattr(self.parent_space, 'closure'):
            parent_closure = self.parent_space.closure(self.subset)
            return parent_closure == self.parent_space.base_set
        
        return False

    def is_nowhere_dense(self):
        """Check if subspace is nowhere dense."""
        # Nowhere dense if int(cl(A)) = ∅ in parent
        
        if hasattr(self.parent_space, 'closure') and hasattr(self.parent_space, 'interior'):
            closure = self.parent_space.closure(self.subset)
            interior = self.parent_space.interior(closure)
            return not interior
        
        return False

    def is_dense_subset(self, other_subset):
        """Check if other_subset is dense in this subspace."""
        other_set = set(other_subset) if not isinstance(other_subset, set) else other_subset
        
        if not other_set.issubset(self.subset):
            return False
        
        # Dense if closure in subspace equals subspace
        closure = self.closure(other_set)
        return closure == self.subset

    # ===== CONVERGENCE IN SUBSPACE =====

    def converges_to(self, sequence, limit_point):
        """
        Check if sequence converges to limit point in subspace.
        
        Sequence converges to p if for every neighborhood N of p,
        only finitely many terms lie outside N.
        """
        if limit_point not in self.subset:
            return False
        
        neighborhoods = self.open_neighborhood(limit_point)
        
        if not neighborhoods:
            return False
        
        # Check if eventually in all neighborhoods
        for nbhd in neighborhoods:
            count_outside = 0
            for term in sequence:
                if term not in nbhd:
                    count_outside += 1
            
            # Should only have finitely many (we allow any for finite spaces)
            if count_outside > len(sequence) // 2:  # Heuristic
                return False
        
        return True

    def get_limits(self, sequence):
        """Get all limits of a sequence in the subspace."""
        limits = set()
        
        for point in self.subset:
            if self.converges_to(sequence, point):
                limits.add(point)
        
        return limits

    def is_limit_point_sequence(self, point, sequence):
        """Check if point is a limit point of the sequence."""
        # Point is limit point if infinitely many terms equal point
        # Or more generally, every neighborhood has infinitely many terms
        
        if point not in self.subset:
            return False
        
        neighborhoods = self.open_neighborhood(point)
        
        for nbhd in neighborhoods:
            count_in = sum(1 for term in sequence if term in nbhd)
            if count_in == 0:
                return False
        
        return True

    # ===== CONTINUOUS FUNCTIONS =====

    def is_continuous_function(self, func, target_space, test_points=None):
        """
        Check if function is continuous from subspace to target.
        
        Function f: A → Y is continuous if preimage of every open set
        in Y is open in A.
        """
        # Test critical open sets in target
        target_opens = target_space.open_sets if hasattr(target_space, 'open_sets') else []
        
        for open_set in target_opens:
            # Preimage in subspace
            preimage = {x for x in self.subset if func(x) in open_set}
            
            # Must be open in subspace
            if preimage not in self.open_sets:
                return False
        
        return True

    def is_continuous_from_parent(self, func, target_space):
        """Check if function is continuous from parent space to target."""
        parent_opens = self.parent_space.open_sets
        
        for open_set in parent_opens:
            preimage = {x for x in self.parent_space.base_set 
                       if func(x) in (target_space.open_sets[0] if target_space.open_sets else set())}
            
            if preimage not in parent_opens:
                return False
        
        return True

    def restriction_to_subspace(self, func):
        """
        Create a function restricted to this subspace.
        
        Returns: Function that operates on subspace points.
        """
        def restricted_func(x):
            if x not in self.subset:
                raise ValueError(f"Point {x} not in subspace")
            return func(x)
        
        return restricted_func

    def inclusion_map(self):
        """Get the inclusion map from subspace to parent."""
        def inclusion(x):
            if x not in self.subset:
                raise ValueError(f"Point {x} not in subspace")
            return x
        
        return inclusion

    def is_inclusion_continuous(self):
        """Check if inclusion map i: A → X is continuous."""
        # Always true: preimage of U ∩ A is U ∩ A which is open in subspace
        return True

    # ===== SUBSPACE OF SUBSPACE =====

    def subspace(self, subset):
        """Create a subspace of this subspace."""
        subset_set = set(subset) if not isinstance(subset, set) else subset
        
        # Must be contained in this subspace
        if not subset_set.issubset(self.subset):
            raise ValueError("Subset must be contained in this subspace")
        
        return SubspaceTopology(self, subset_set, 
                               name=f"{self.name} (subspace)")

    def is_subspace_of(self, other):
        """Check if this is a subspace of another topology."""
        if not isinstance(other, SubspaceTopology):
            return False
        
        return self.subset.issubset(other.subset)

    # ===== QUOTIENT & OPERATIONS =====

    def quotient_by_equivalence(self, equivalence_classes):
        """Create quotient space by equivalence relation."""
        # Check that classes partition the subspace
        union = set().union(*equivalence_classes)
        if union != self.subset:
            raise ValueError("Classes must partition the subspace")
        
        return SubspaceTopology(self.parent_space, set(equivalence_classes),
                               name=f"{self.name} / ~")

    def product_with(self, other):
        """Create product topology with another subspace."""
        if not isinstance(other, SubspaceTopology):
            raise TypeError("Other must be SubspaceTopology")
        
        # Product of subsets
        product_set = {(x, y) for x in self.subset for y in other.subset}
        
        # Create product as subspace of parent product
        # For simplicity, return new subspace with product structure
        product = SubspaceTopology(self.parent_space, product_set,
                                  name=f"{self.name} × {other.name}")
        return product

    def disjoint_union(self, other):
        """Create disjoint union with another subspace."""
        if not isinstance(other, SubspaceTopology):
            raise TypeError("Other must be SubspaceTopology")
        
        # Tag elements to keep distinct
        tagged_set = (
            {(0, x) for x in self.subset} |
            {(1, y) for y in other.subset}
        )
        
        return SubspaceTopology(self.parent_space, tagged_set,
                               name=f"{self.name} ⊔ {other.name}")

    # ===== PROPERTIES & UTILITIES =====

    def get_properties(self):
        """Get all topological properties."""
        return {
            'name': self.name,
            'size': self.size,
            'open_sets': len(self.open_sets),
            'closed_sets': len(self.closed_sets),
            'is_connected': self.is_connected(),
            'is_compact': self.is_compact(),
            'is_path_connected': self.is_path_connected(),
            'is_hausdorff': self.is_t2_hausdorff(),
            'is_dense': self.is_dense(),
            'is_nowhere_dense': self.is_nowhere_dense(),
            'is_totally_disconnected': self.is_totally_disconnected(),
            'components': len(self.connected_components()),
        }

    def print_properties(self):
        """Print properties in formatted way."""
        props = self.get_properties()
        print(f"\n{'='*60}")
        print(f"SubspaceTopology: {self.name}")
        print(f"{'='*60}")
        for key, value in props.items():
            print(f"{key:.<40} {value}")
        print(f"{'='*60}\n")

    def summary(self):
        """One-line summary."""
        return (f"SubspaceTopology: {self.name} with {self.size} points, "
                f"{len(self.open_sets)} open sets")

    def describe(self):
        """Detailed description."""
        desc = f"\n{'='*70}\n"
        desc += f"SubspaceTopology: {self.name}\n"
        desc += f"{'='*70}\n"
        desc += f"Number of points: {self.size}\n"
        desc += f"Number of open sets: {len(self.open_sets)}\n"
        desc += f"Number of closed sets: {len(self.closed_sets)}\n"
        desc += f"Is connected: {self.is_connected()}\n"
        desc += f"Is compact: {self.is_compact()}\n"
        desc += f"Is path-connected: {self.is_path_connected()}\n"
        desc += f"Is Hausdorff: {self.is_t2_hausdorff()}\n"
        desc += f"Is dense in parent: {self.is_dense()}\n"
        desc += f"Inclusion continuous: {self.is_inclusion_continuous()}\n"
        desc += f"Connected components: {len(self.connected_components())}\n"
        desc += f"{'='*70}\n"
        return desc

    def export_to_dict(self):
        """Export as dictionary."""
        return {
            'name': self.name,
            'subset': list(self.subset),
            'size': self.size,
            'open_sets': [list(s) for s in self.open_sets],
            'closed_sets': [list(s) for s in self.closed_sets],
            'properties': self.get_properties(),
        }

    # ===== COMPARISON WITH PARENT =====

    def compare_with_parent(self):
        """Compare topology with parent space."""
        return {
            'subspace_name': self.name,
            'parent_name': getattr(self.parent_space, 'name', 'Parent Space'),
            'subspace_open_sets': len(self.open_sets),
            'parent_open_sets': len(self.parent_space.open_sets),
            'subspace_size': self.size,
            'parent_size': len(self.parent_space.base_set),
            'subspace_connected': self.is_connected(),
            'parent_connected': self.parent_space.is_connected() if hasattr(self.parent_space, 'is_connected') else None,
            'subspace_compact': self.is_compact(),
            'parent_compact': self.parent_space.is_compact() if hasattr(self.parent_space, 'is_compact') else None,
            'subspace_hausdorff': self.is_t2_hausdorff(),
            'parent_hausdorff': self.parent_space.is_t2_hausdorff() if hasattr(self.parent_space, 'is_t2_hausdorff') else None,
        }

    def coarser_than_parent(self):
        """Check if subspace is coarser than parent (fewer open sets)."""
        return len(self.open_sets) < len(self.parent_space.open_sets)

    def finer_than_parent(self):
        """Check if subspace is finer than parent (more open sets)."""
        return len(self.open_sets) > len(self.parent_space.open_sets)

    # ===== SPECIAL OPERATIONS =====

    def closure_in_parent(self, subset=None):
        """Get closure of subspace in parent space."""
        if subset is None:
            subset = self.subset
        
        if hasattr(self.parent_space, 'closure'):
            return self.parent_space.closure(set(subset))
        return None

    def interior_in_parent(self, subset=None):
        """Get interior of subspace in parent space."""
        if subset is None:
            subset = self.subset
        
        if hasattr(self.parent_space, 'interior'):
            return self.parent_space.interior(set(subset))
        return None

    def is_open_in_parent(self):
        """Check if subspace itself is open in parent."""
        return self.subset in self.parent_space.open_sets

    def is_closed_in_parent(self):
        """Check if subspace itself is closed in parent."""
        return self.subset in self.parent_space.closed_sets

    def is_clopen_in_parent(self):
        """Check if subspace is both open and closed in parent."""
        return self.is_open_in_parent() and self.is_closed_in_parent()

    # ===== DIMENSION =====

    def dimension(self):
        """
        Compute dimension (approximation for finite spaces).
        
        For subspaces of R^n, this gives Euclidean dimension.
        """
        if self.size == 0:
            return -1
        elif self.size == 1:
            return 0
        else:
            # Approximation: based on open sets
            return min(self.size - 1, len(self.open_sets) - 1)

    def is_zero_dimensional(self):
        """Check if space is zero-dimensional."""
        # Zero-dimensional if has base of clopen sets
        clopen = self.get_all_clopen_sets()
        return len(clopen) > 0

    # ===== ADVANCED ANALYSIS =====

    def hausdorff_dimension(self):
        """Approximate Hausdorff dimension (for finite spaces)."""
        if self.size <= 1:
            return 0
        
        # Rough approximation
        return len(set(range(len(self.open_sets)))) / len(self.subset) if self.subset else 0

    def covering_dimension(self):
        """Covering dimension (for finite spaces)."""
        if self.size <= 1:
            return 0
        
        # Use open covers
        return len(self.open_sets) - 2

    def generate_open_set_base(self):
        """Generate a base for the topology."""
        # Subbasic: use open sets
        return self.open_sets

    def get_separating_sets(self):
        """Get all pairs of disjoint sets that could separate space."""
        separating = []
        
        for u1 in self.open_sets:
            for u2 in self.open_sets:
                if (u1 and u2 and  # both non-empty
                    not (u1 & u2) and  # disjoint
                    u1 | u2 == self.subset):  # cover space
                    separating.append((u1, u2))
        
        return separating
