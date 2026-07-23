# SubspaceTopology Class - Complete Documentation & Examples

**Comprehensive Guide to Subspace Topologies in Python**

---

## Table of Contents

1. [Overview](#overview)
2. [Mathematical Background](#mathematical-background)
3. [Quick Start](#quick-start)
4. [Initialization](#initialization)
5. [Basic Topological Properties](#basic-topological-properties)
6. [Interior, Closure, Boundary](#interior-closure-boundary)
7. [Neighborhoods in Subspaces](#neighborhoods-in-subspaces)
8. [Separation Axioms](#separation-axioms)
9. [Connectivity](#connectivity)
10. [Compactness](#compactness)
11. [Density](#density)
12. [Convergence](#convergence)
13. [Continuous Functions](#continuous-functions)
14. [Subspaces of Subspaces](#subspaces-of-subspaces)
15. [Comparing with Parent Space](#comparing-with-parent-space)
16. [Practical Examples](#practical-examples)
17. [API Reference](#api-reference)
18. [Common Patterns](#common-patterns)
19. [Best Practices](#best-practices)

---

## Overview

### What is a Subspace Topology?

A **subspace topology** is a topology induced on a subset of a topological space. Given a topological space $(X, \tau)$ and a subset $A \subseteq X$, the subspace topology on $A$ is defined as:

$$\tau_A = \{U \cap A : U \in \tau\}$$

In other words, **open sets in the subspace are exactly the intersections of the parent's open sets with the subset**.

### Key Characteristics

| Property | Description |
|----------|-------------|
| **Definition** | $\tau_A = \{U \cap A : U \in \tau\}$ |
| **Open sets** | Intersections of parent's open sets with subset |
| **Closed sets** | Complements (in the subset) of open sets |
| **Inclusion map** | The map $i: A \to X$ defined by $i(a) = a$ is always continuous |
| **Initial topology** | Subspace topology is the coarsest making inclusion continuous |
| **Uniqueness** | For each subset, there's exactly one subspace topology |

### When to Use

✅ **Perfect for:**
- Studying restrictions of functions
- Understanding inherited properties
- Analyzing open/closed sets in restrictions
- Building complex spaces from simpler ones
- Approximating continuous deformations

❌ **Not ideal for:**
- High-dimensional numerical computations
- Large-scale data processing
- Real-time applications
- Spaces without clear parent structure

---

## Mathematical Background

### Fundamental Definition

For a topological space $(X, \tau)$ and subset $A \subseteq X$:

**Subspace Topology** = $\{U \cap A : U \in \tau\}$

### Examples

#### Example 1: Standard Subspace
```
Parent: X = {1, 2, 3, 4}, τ = {∅, {1}, {1,2}, {1,2,3}, X}
Subset: A = {1, 2, 3}

Subspace open sets:
  ∅ ∩ A = ∅
  {1} ∩ A = {1}
  {1,2} ∩ A = {1,2}
  {1,2,3} ∩ A = {1,2,3}
  X ∩ A = {1,2,3}

τ_A = {∅, {1}, {1,2}, {1,2,3}}
```

#### Example 2: Closed Subset
If $A$ is closed in $X$:
- The relative topology on $A$ inherits closure properties
- $A$ itself is closed in subspace topology

#### Example 3: Dense Subset
If $A$ is dense in $X$:
- $A$ itself equals its closure in the subspace
- The subspace may have different density properties

### Key Theorems

1. **Inclusion is Continuous**: The inclusion map $i: A \to X$ is always continuous
2. **Transitivity**: If $B \subseteq A \subseteq X$, then subspace topology on $B$ from $A$ equals subspace topology on $B$ from $X$
3. **Inherited Properties**: Hausdorff, regularity, and normality are inherited by subspaces
4. **Counterexample**: Compactness is NOT always inherited

---

## Quick Start

```python
from subspace_topology import SubspaceTopology
from indiscrete_topology import IndiscreteTopology

# Create parent space
parent = IndiscreteTopology({1, 2, 3, 4}, name="Parent")

# Create subspace
subspace = SubspaceTopology(parent, {1, 2, 3}, name="Subspace A")

# Basic queries
print(subspace.is_connected())        # True/False
print(subspace.is_compact())          # True/False
print(subspace.is_t2_hausdorff())     # True/False

# Topological operations
print(subspace.interior({1, 2}))      # Interior in subspace
print(subspace.closure({1, 2}))       # Closure in subspace
print(subspace.boundary({1, 2}))      # Boundary in subspace

# Properties
subspace.print_properties()
```

---

## Initialization

### Constructor

```python
SubspaceTopology(parent_space, subset, name=None)
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `parent_space` | Topological space | Must have `open_sets` and `base_set` attributes |
| `subset` | set/list/tuple | Subset $A \subseteq X$ |
| `name` | str | Optional name for the subspace |

### Creating Subspaces

```python
from subspace_topology import SubspaceTopology
from indiscrete_topology import IndiscreteTopology

# Parent space
parent = IndiscreteTopology({1, 2, 3, 4, 5}, name="Five Points")

# Create multiple subspaces
sub1 = SubspaceTopology(parent, {1, 2, 3})
sub2 = SubspaceTopology(parent, {1, 2}, name="Pair")
sub3 = SubspaceTopology(parent, {5}, name="Singleton")

# From different parent types
from discrete_topology import DiscreteTopology
parent2 = DiscreteTopology(range(10))
sub4 = SubspaceTopology(parent2, set(range(5)))
```

### Error Handling

```python
parent = IndiscreteTopology({1, 2, 3})

# This raises ValueError - subset not in parent
try:
    bad_subspace = SubspaceTopology(parent, {1, 2, 5})
except ValueError as e:
    print(e)  # "Subset must be contained in parent space"
```

---

## Basic Topological Properties

### Open Sets in Subspace

Open sets in the subspace are intersections of parent's open sets with the subset.

```python
from subspace_topology import SubspaceTopology
from indiscrete_topology import IndiscreteTopology

parent = IndiscreteTopology({1, 2, 3, 4}, name="Parent")
subspace = SubspaceTopology(parent, {1, 2, 3}, name="Subspace")

# View all open sets
print("Open sets in subspace:")
for s in subspace.open_sets:
    print(f"  {s if s else '∅'}")

# Check specific sets
print(subspace.is_open_set({1}))        # May be True/False depending on parent
print(subspace.is_open_set({1, 2}))     # May be True/False
print(subspace.is_open_set({1, 2, 3}))  # Usually True (whole subspace)
print(subspace.is_open_set(set()))      # Always True (empty set)
```

### Closed Sets in Subspace

Closed sets are complements of open sets within the subspace.

```python
# Check which sets are closed
print(subspace.is_closed_set({1}))       # May be True/False
print(subspace.is_closed_set({1, 2, 3})) # Usually True

# View all closed sets
print("Closed sets in subspace:")
for s in subspace.closed_sets:
    print(f"  {s if s else '∅'}")
```

### Clopen Sets

Sets that are both open and closed.

```python
# Get all clopen sets
clopen = subspace.get_all_clopen_sets()
print(f"Clopen sets: {clopen}")

# Check specific set
print(subspace.is_clopen_set({1, 2, 3}))  # Likely True (whole space)
```

---

## Interior, Closure, Boundary

### Interior in Subspace

Interior in subspace is different from interior in parent space!

```python
subspace = SubspaceTopology(parent, {1, 2, 3, 4})
subset = {1, 2}

# Interior in subspace (relative to subspace topology)
interior_sub = subspace.interior(subset)
print(f"Interior in subspace: {interior_sub}")

# Interior in parent space (for comparison)
interior_parent = subspace.interior_in_parent(subset)
print(f"Interior in parent: {interior_parent}")

# These can be different!
print(f"Are they equal? {interior_sub == interior_parent}")
```

**Example:**
```
Parent: Indiscrete on {1,2,3,4}, open sets: {∅, {1,2,3,4}}
Subspace: A = {1,2,3}

Interior({1,2}) in subspace: ∅ (no open set contains it)
Interior({1,2}) in parent: ∅ (same in parent)
```

### Closure in Subspace

Closure in subspace is computed as: $\text{cl}_A(B) = A \cap \text{cl}_X(B)$

```python
subset = {1, 2}

# Closure in subspace
closure_sub = subspace.closure(subset)
print(f"Closure in subspace: {closure_sub}")

# Closure in parent
closure_parent = subspace.closure_in_parent(subset)
print(f"Closure in parent: {closure_parent}")

# Intersection formula
intersection = closure_parent & subspace.subset
print(f"Parent closure ∩ subset: {intersection}")
print(f"Equals subspace closure? {intersection == closure_sub}")
```

### Boundary in Subspace

Boundary = closure - interior

```python
test_set = {1, 2}

closure = subspace.closure(test_set)
interior = subspace.interior(test_set)
boundary = subspace.boundary(test_set)

print(f"Closure: {closure}")
print(f"Interior: {interior}")
print(f"Boundary: {boundary}")
print(f"Boundary = Closure - Interior? {boundary == (closure - interior)}")
```

### Derived Set (Limit Points)

The derived set contains all limit points of a set.

```python
subset = {1, 2}

# Get derived set
derived = subspace.derived_set(subset)
print(f"Derived set of {subset}: {derived}")

# Individual limit points
for point in subspace.subset:
    is_limit = subspace.is_limit_point(point, subset)
    print(f"  {point} is limit point? {is_limit}")

# Closure = Set ∪ Derived Set
closure = subspace.closure(subset)
reconstructed_closure = subset | derived
print(f"Closure: {closure}")
print(f"Set ∪ Derived: {reconstructed_closure}")
print(f"Are equal? {closure == reconstructed_closure}")
```

---

## Neighborhoods in Subspaces

### Understanding Neighborhoods

A neighborhood of point $p$ in a subspace is a set containing an open set containing $p$.

```python
subspace = SubspaceTopology(parent, {1, 2, 3})

point = 1

# Get all neighborhoods
nbhds = subspace.neighborhood(point)
print(f"Neighborhoods of {point}: {nbhds}")

# Get open neighborhoods
open_nbhds = subspace.open_neighborhood(point)
print(f"Open neighborhoods of {point}: {open_nbhds}")

# Check if set is neighborhood
test_set = {1, 2, 3}
is_nbhd = subspace.is_neighborhood(point, test_set)
print(f"Is {test_set} a neighborhood? {is_nbhd}")
```

### Neighborhood Bases

Neighborhoods form a structure around each point:

```python
# Analyze neighborhoods for each point
for point in subspace.subset:
    nbhds = subspace.open_neighborhood(point)
    print(f"\nPoint {point}:")
    print(f"  Open neighborhoods: {nbhds}")
    print(f"  Number of neighborhoods: {len(nbhds)}")
```

---

## Separation Axioms

Separation axioms describe how well the topology distinguishes between points.

### T₀ (Kolmogorov Separation)

For any two distinct points, at least one has a neighborhood not containing the other.

```python
subspace = SubspaceTopology(parent, {1, 2, 3})

# Check T₀
is_t0 = subspace.is_t0()
print(f"Is T₀ (Kolmogorov)? {is_t0}")

# Example: for points 1, 2
p1, p2 = 1, 2
nbhds_p1 = subspace.open_neighborhood(p1)
nbhds_p2 = subspace.open_neighborhood(p2)

# T₀ satisfied if can separate
for nbhd in nbhds_p1:
    if p2 not in nbhd:
        print(f"  Separating neighborhood of {p1}: {nbhd}")
        break
```

### T₁ (Frechet Separation)

For any two distinct points, each has a neighborhood not containing the other.

```python
# Check T₁
is_t1 = subspace.is_t1()
print(f"Is T₁ (Frechet)? {is_t1}")

# T₁ requires: for each pair (p,q),
# ∃ U open with p∈U, q∉U AND ∃ V open with q∈V, p∉V
```

### T₂ (Hausdorff)

For any two distinct points, there exist disjoint neighborhoods.

```python
# Check Hausdorff
is_hausdorff = subspace.is_t2_hausdorff()
print(f"Is Hausdorff (T₂)? {is_hausdorff}")

# Check for specific pair
p1, p2 = 1, 2
nbhds_p1 = subspace.open_neighborhood(p1)
nbhds_p2 = subspace.open_neighborhood(p2)

found_disjoint = False
for n1 in nbhds_p1:
    for n2 in nbhds_p2:
        if not (n1 & n2):  # Disjoint
            print(f"  Disjoint neighborhoods: {n1} and {n2}")
            found_disjoint = True
            break
    if found_disjoint:
        break

print(f"  Found disjoint pair? {found_disjoint}")
```

### T₃ (Regular) and T₄ (Normal)

```python
is_regular = subspace.is_t3()
is_normal = subspace.is_t4()

print(f"Is T₃ (Regular)? {is_regular}")
print(f"Is T₄ (Normal)? {is_normal}")

# Get all separation properties
axioms = subspace.separation_axioms()
print("\nAll separation axioms:")
for axiom, value in axioms.items():
    print(f"  {axiom}: {value}")
```

### Complete Separation Analysis

```python
def analyze_separation(subspace):
    """Complete separation analysis."""
    print(f"\n{'='*50}")
    print(f"Separation Axioms for: {subspace.name}")
    print(f"{'='*50}")
    
    axioms = subspace.separation_axioms()
    for axiom, satisfied in axioms.items():
        symbol = "✓" if satisfied else "✗"
        print(f"  {symbol} {axiom}: {satisfied}")
    
    # Implication chain
    print("\nImplication chain:")
    if axioms['T4 (Normal)']:
        print("  T₄ ⟹ T₃ ⟹ T₁ ⟹ T₀")
    elif axioms['T3 (Regular)']:
        print("  T₃ ⟹ T₁ ⟹ T₀")
    elif axioms['T1']:
        print("  T₁ ⟹ T₀")
    elif axioms['T0 (Kolmogorov)']:
        print("  T₀ satisfied")

analyze_separation(subspace)
```

---

## Connectivity

### Is Connected?

A space is connected if it cannot be written as the union of two non-empty disjoint open sets.

```python
subspace = SubspaceTopology(parent, {1, 2, 3})

# Check connectivity
is_connected = subspace.is_connected()
print(f"Is connected? {is_connected}")

# Get separating sets (if disconnected)
separating = subspace.get_separating_sets()
if separating:
    print(f"Separating open sets: {separating}")
else:
    print("No separating sets - space is connected")
```

### Connected Components

Connected components partition the space into maximal connected subsets.

```python
# Get connected components
components = subspace.connected_components()
print(f"Connected components: {components}")
print(f"Number of components: {len(components)}")

# Each component should be connected
for i, component in enumerate(components):
    comp_subspace = subspace.subspace(component)
    is_connected = comp_subspace.is_connected()
    print(f"  Component {i}: {component}, connected? {is_connected}")
```

### Total Disconnection

A space is totally disconnected if all components are singletons.

```python
is_totally_disc = subspace.is_totally_disconnected()
print(f"Is totally disconnected? {is_totally_disc}")

# Verification
components = subspace.connected_components()
all_singletons = all(len(c) == 1 for c in components)
print(f"All singletons? {all_singletons}")
```

### Path Connectivity

Path-connected is stronger than connected.

```python
is_path_connected = subspace.is_path_connected()
print(f"Is path-connected? {is_path_connected}")

# Check local connectivity
point = list(subspace.subset)[0] if subspace.subset else None
if point:
    is_locally_conn = subspace.is_locally_connected(point)
    print(f"Is locally connected at {point}? {is_locally_conn}")
```

---

## Compactness

### Basic Compactness

A space is compact if every open cover has a finite subcover.

```python
subspace = SubspaceTopology(parent, {1, 2, 3})

# Check compactness
is_compact = subspace.is_compact()
print(f"Is compact? {is_compact}")

# For finite spaces, always compact
print(f"Size: {subspace.size}")
print(f"Finite implies compact: {is_compact if subspace.size < float('inf') else 'N/A'}")
```

### Local Compactness

A space is locally compact if every point has a compact neighborhood.

```python
is_locally_compact = subspace.is_locally_compact()
print(f"Is locally compact? {is_locally_compact}")

# Check for each point
for point in subspace.subset:
    nbhds = subspace.open_neighborhood(point)
    has_compact_nbhd = False
    
    for nbhd in nbhds:
        sub_nbhd = subspace.subspace(nbhd)
        if sub_nbhd.is_compact():
            has_compact_nbhd = True
            break
    
    print(f"  Point {point}: has compact neighborhood? {has_compact_nbhd}")
```

### Sequential Compactness

Every sequence has a convergent subsequence.

```python
is_seq_compact = subspace.is_sequentially_compact()
print(f"Is sequentially compact? {is_seq_compact}")
```

### Countable Compactness

Every countable open cover has finite subcover.

```python
is_countably_compact = subspace.is_countably_compact()
print(f"Is countably compact? {is_countably_compact}")
```

---

## Density

### Is Dense?

A subspace $A$ is dense in its parent $X$ if $\text{cl}_X(A) = X$.

```python
subspace = SubspaceTopology(parent, {1, 2, 3})

# Check density
is_dense = subspace.is_dense()
print(f"Is dense in parent space? {is_dense}")

# Manual check
if hasattr(parent, 'closure'):
    parent_closure = parent.closure(subspace.subset)
    manually_dense = parent_closure == parent.base_set
    print(f"Manual check: {manually_dense}")
```

### Dense Subset

Check if another subset is dense within this subspace.

```python
# Check if subset is dense in this subspace
test_set = {1, 2}
is_dense_here = subspace.is_dense_subset(test_set)
print(f"Is {test_set} dense in {subspace.name}? {is_dense_here}")

# Verification
closure = subspace.closure(test_set)
print(f"Closure of {test_set}: {closure}")
print(f"Equals subspace? {closure == subspace.subset}")
```

### Nowhere Dense

A space is nowhere dense if interior of its closure is empty.

```python
is_nowhere_dense = subspace.is_nowhere_dense()
print(f"Is nowhere dense? {is_nowhere_dense}")

# Manual check (in parent)
if hasattr(parent, 'closure') and hasattr(parent, 'interior'):
    closure_in_parent = parent.closure(subspace.subset)
    interior_of_closure = parent.interior(closure_in_parent)
    manually_nowhere_dense = not interior_of_closure
    print(f"Manual check: {manually_nowhere_dense}")
```

---

## Convergence

### Sequence Convergence

A sequence converges to a point if it eventually enters all neighborhoods.

```python
subspace = SubspaceTopology(parent, {1, 2, 3})

# Define a sequence
sequence = [1, 2, 1, 2, 1]

# Check convergence to each point
for point in subspace.subset:
    converges = subspace.converges_to(sequence, point)
    print(f"Sequence {sequence} converges to {point}? {converges}")

# Get all limits
limits = subspace.get_limits(sequence)
print(f"All limits: {limits}")
```

### Limit Points of Sequences

Check if a point is a limit point of a sequence (infinitely many terms equal it).

```python
sequence = [1, 2, 1, 2, 1, 3]
point = 1

is_limit_pt = subspace.is_limit_point_sequence(point, sequence)
print(f"Is {point} a limit point of sequence? {is_limit_pt}")

# Count occurrences
count = sum(1 for x in sequence if x == point)
print(f"  Point {point} appears {count} times")
```

### Convergence Analysis

```python
def analyze_convergence(subspace, sequences):
    """Analyze convergence of multiple sequences."""
    print(f"\n{'='*60}")
    print(f"Convergence Analysis for {subspace.name}")
    print(f"{'='*60}")
    
    for seq_name, sequence in sequences.items():
        print(f"\nSequence: {seq_name}")
        print(f"  Terms: {sequence}")
        
        limits = subspace.get_limits(sequence)
        print(f"  Limits: {limits}")
        print(f"  Number of limits: {len(limits)}")

# Example sequences
sequences = {
    "Constant": [1, 1, 1],
    "Alternating": [1, 2, 1, 2],
    "Converging": [1, 2, 3, 1],
}

analyze_convergence(subspace, sequences)
```

---

## Continuous Functions

### Checking Continuity

A function $f: A \to Y$ is continuous if preimages of open sets are open.

```python
subspace = SubspaceTopology(parent, {1, 2, 3})
target = IndiscreteTopology({2, 4, 6}, name="Target")

def f(x):
    """Example function"""
    return 2 * x

# Check continuity
is_continuous = subspace.is_continuous_function(f, target)
print(f"Is f(x) = 2x continuous? {is_continuous}")
```

### Restriction of Functions

Get a function restricted to the subspace.

```python
def original_func(x):
    return x**2

# Restrict to subspace
restricted = subspace.restriction_to_subspace(original_func)

# Use restricted function
for point in subspace.subset:
    result = restricted(point)
    print(f"  f({point}) = {result}")
```

### Inclusion Map

The inclusion map $i: A \to X$ is always continuous.

```python
# Get inclusion map
inclusion = subspace.inclusion_map()

# Check it's continuous
is_inclusion_cont = subspace.is_inclusion_continuous()
print(f"Is inclusion map continuous? {is_inclusion_cont}")

# Use inclusion map
for point in subspace.subset:
    image = inclusion(point)
    print(f"  i({point}) = {image}")
```

---

## Subspaces of Subspaces

### Creating Subspaces Hierarchically

```python
parent = IndiscreteTopology({1, 2, 3, 4, 5})
subspace1 = SubspaceTopology(parent, {1, 2, 3, 4}, name="First subspace")
subspace2 = subspace1.subspace({1, 2, 3}, name="Subspace of subspace")

print(f"Parent: {parent.name} with {len(parent.base_set)} points")
print(f"Subspace 1: {subspace1.name} with {subspace1.size} points")
print(f"Subspace 2: {subspace2.name} with {subspace2.size} points")
```

### Transitivity Property

The subspace topology on $C$ (from $A$ which is subspace of $X$) equals the subspace topology on $C$ (directly from $X$).

```python
# Create subspace two ways
sub_indirect = subspace1.subspace({1, 2})  # B ⊂ A ⊂ X
sub_direct = parent.subspace({1, 2})       # B ⊂ X

# They should have same open sets (up to interpretation)
print(f"Both have same size? {sub_indirect.size == sub_direct.size}")
print(f"Both connected? {sub_indirect.is_connected() == sub_direct.is_connected()}")
```

### Checking Subspace Relationships

```python
parent = IndiscreteTopology(range(5))
sub1 = SubspaceTopology(parent, {1, 2, 3})
sub2 = SubspaceTopology(parent, {1, 2})

# Is sub2 a subspace of sub1?
is_sub = sub2.is_subspace_of(sub1)
print(f"Is {sub2.name} a subspace of {sub1.name}? {is_sub}")
```

---

## Comparing with Parent Space

### Basic Comparison

```python
subspace = SubspaceTopology(parent, {1, 2, 3})

# Compare properties
comparison = subspace.compare_with_parent()

print(f"{'='*60}")
print("Comparison with Parent Space")
print(f"{'='*60}")

for key, value in comparison.items():
    print(f"{key:.<40} {value}")
```

### Coarseness Analysis

```python
is_coarser = subspace.coarser_than_parent()
is_finer = subspace.finer_than_parent()

print(f"Subspace is coarser (fewer opens)? {is_coarser}")
print(f"Subspace is finer (more opens)? {is_finer}")

print(f"\nSubspace open sets: {len(subspace.open_sets)}")
print(f"Parent open sets: {len(parent.open_sets)}")
```

### Open/Closed in Parent

```python
# Is the subspace itself open/closed in parent?
is_open_in_parent = subspace.is_open_in_parent()
is_closed_in_parent = subspace.is_closed_in_parent()
is_clopen_in_parent = subspace.is_clopen_in_parent()

print(f"Subspace is open in parent? {is_open_in_parent}")
print(f"Subspace is closed in parent? {is_closed_in_parent}")
print(f"Subspace is clopen in parent? {is_clopen_in_parent}")
```

### Property Inheritance

Properties that are inherited vs. those that may differ:

```python
def property_inheritance_summary(subspace):
    """Show which properties inherit from parent."""
    parent = subspace.parent_space
    
    print("INHERITED (or same):")
    print(f"  Connectedness: Parent={parent.is_connected()}, "
          f"Sub={subspace.is_connected()}")
    
    print("\nMAY DIFFER:")
    print(f"  Compactness: Parent={parent.is_compact()}, "
          f"Sub={subspace.is_compact()}")
    print(f"  Hausdorff: Parent={parent.is_t2_hausdorff() if hasattr(parent, 'is_t2_hausdorff') else 'N/A'}, "
          f"Sub={subspace.is_t2_hausdorff()}")

property_inheritance_summary(subspace)
```

---

## Practical Examples

### Example 1: Restricting from Real Line

```python
# Simulate real line subspace
class RealLineSubspace:
    """Simplified example: subspace of real line"""
    
    def __init__(self, interval_start, interval_end):
        self.start = interval_start
        self.end = interval_end
        self.name = f"[{interval_start}, {interval_end}]"
    
    def describe(self):
        print(f"\nSubspace: {self.name}")
        print(f"  Type: Closed interval subspace")
        print(f"  Connectedness: Always connected")
        print(f"  Compactness: Always compact (closed and bounded)")
        print(f"  Is Hausdorff: Yes (inherits from R)")

# Example
interval = RealLineSubspace(0, 1)
interval.describe()
```

### Example 2: Product Subspaces

```python
parent_space = IndiscreteTopology(range(4))
sub1 = SubspaceTopology(parent_space, {1, 2})
sub2 = SubspaceTopology(parent_space, {0, 1})

# Create product
product = sub1.product_with(sub2)
print(f"\n{sub1.name} × {sub2.name} = {product.name}")
print(f"  Original size: {sub1.size} × {sub2.size} = {sub1.size * sub2.size}")
print(f"  Product size: {product.size}")
```

### Example 3: Disjoint Union

```python
disjoint_union = sub1.disjoint_union(sub2)
print(f"\n{sub1.name} ⊔ {sub2.name} = {disjoint_union.name}")
print(f"  Original sizes: {sub1.size} + {sub2.size}")
print(f"  Union size: {disjoint_union.size}")
print(f"  Is connected? {disjoint_union.is_connected()}")
```

### Example 4: Quotient Spaces

```python
# Identify points 1 and 2
classes = [{0}, {1, 2}, {3}]
quotient = sub1.quotient_by_equivalence(classes)

print(f"\nQuotient space:")
print(f"  Original: {sub1.name} with {sub1.size} points")
print(f"  Quotient: {quotient.name} with {len(classes)} equivalence classes")
```

### Example 5: Dense Subspace

```python
# Create scenario where subspace might be dense
parent = IndiscreteTopology({1, 2, 3, 4, 5})
dense_subset = SubspaceTopology(parent, {1, 2, 3})

print(f"\nDensity Analysis:")
print(f"  Is {dense_subset.name} dense in parent? {dense_subset.is_dense()}")
print(f"  Is nowhere dense? {dense_subset.is_nowhere_dense()}")

# Check density of sub-subset
sub_subset = {1, 2}
is_dense_here = dense_subset.is_dense_subset(sub_subset)
print(f"  Is {sub_subset} dense in subspace? {is_dense_here}")
```

---

## API Reference

### Quick Method Reference

#### Topology Testing

```python
# Set properties
.is_open_set(subset)        # Check if open
.is_closed_set(subset)      # Check if closed
.is_clopen_set(subset)      # Check if both

# Basic operations
.interior(subset)           # Interior of set
.closure(subset)            # Closure of set
.boundary(subset)           # Boundary of set
.derived_set(subset)        # Limit points
.is_limit_point(point, set) # Check limit point

# Neighborhoods
.neighborhood(point)         # All neighborhoods
.open_neighborhood(point)    # Open neighborhoods
.is_neighborhood(point, set) # Is neighborhood?

# Separation
.is_t0()                     # Kolmogorov
.is_t1()                     # Frechet
.is_t2_hausdorff()          # Hausdorff
.is_t3()                     # Regular
.is_t4()                     # Normal
.separation_axioms()        # All axioms

# Connectivity
.is_connected()             # Connected?
.connected_components()     # Components
.is_path_connected()        # Path-connected?
.is_locally_connected(pt)  # Locally connected?
.is_totally_disconnected() # Totally disconnected?

# Compactness
.is_compact()              # Compact?
.is_locally_compact()      # Locally compact?
.is_sequentially_compact() # Sequentially compact?
.is_countably_compact()    # Countably compact?

# Density
.is_dense()                # Dense in parent?
.is_nowhere_dense()        # Nowhere dense?
.is_dense_subset(set)      # Set dense here?

# Convergence
.converges_to(seq, point)  # Convergence?
.get_limits(sequence)      # All limits
.is_limit_point_sequence(pt, seq) # Limit point of sequence?

# Functions
.is_continuous_function(f, target)    # Continuous?
.restriction_to_subspace(f)           # Restrict function
.inclusion_map()                       # Inclusion i: A→X
.is_inclusion_continuous()             # Always True

# Subspaces
.subspace(subset)           # Create subspace
.is_subspace_of(other)      # Is subspace?

# Comparison
.compare_with_parent()      # Compare properties
.is_open_in_parent()        # Open in parent?
.is_closed_in_parent()      # Closed in parent?
.interior_in_parent(set)    # Interior in parent
.closure_in_parent(set)     # Closure in parent

# Operations
.product_with(other)        # Create product
.disjoint_union(other)      # Disjoint union
.quotient_by_equivalence(classes) # Quotient space

# Utilities
.summary()                  # One-line summary
.describe()                 # Detailed description
.print_properties()         # Print formatted
.get_properties()          # Dictionary of properties
.export_to_dict()          # Full export
```

---

## Common Patterns

### Pattern 1: Complete Topological Analysis

```python
def full_analysis(subspace):
    """Complete analysis of a subspace."""
    print(f"\n{'='*70}")
    print(f"COMPLETE ANALYSIS: {subspace.name}")
    print(f"{'='*70}")
    
    print(f"\nBASIC INFORMATION:")
    print(f"  Size: {subspace.size}")
    print(f"  Open sets: {len(subspace.open_sets)}")
    print(f"  Closed sets: {len(subspace.closed_sets)}")
    
    print(f"\nCONNECTIVITY:")
    print(f"  Connected: {subspace.is_connected()}")
    print(f"  Components: {len(subspace.connected_components())}")
    print(f"  Path-connected: {subspace.is_path_connected()}")
    
    print(f"\nCOMPACTNESS:")
    print(f"  Compact: {subspace.is_compact()}")
    print(f"  Locally compact: {subspace.is_locally_compact()}")
    
    print(f"\nSEPARATION:")
    axioms = subspace.separation_axioms()
    for ax, val in axioms.items():
        print(f"  {ax}: {val}")
    
    print(f"\nDENSITY:")
    print(f"  Dense in parent: {subspace.is_dense()}")
    print(f"  Nowhere dense: {subspace.is_nowhere_dense()}")
    
    print(f"\nCONTINUITY:")
    print(f"  Inclusion continuous: {subspace.is_inclusion_continuous()}")

# Usage
full_analysis(subspace)
```

### Pattern 2: Comparing Multiple Subspaces

```python
def compare_subspaces(subspaces):
    """Compare multiple subspaces."""
    print(f"\n{'='*70}")
    print("SUBSPACE COMPARISON")
    print(f"{'='*70}\n")
    
    print(f"{'Name':<25} {'Size':<8} {'Open':<8} {'Connected':<12} {'Compact':<10}")
    print("-" * 70)
    
    for sub in subspaces:
        print(f"{sub.name:<25} {sub.size:<8} {len(sub.open_sets):<8} "
              f"{str(sub.is_connected()):<12} {str(sub.is_compact()):<10}")

# Usage
subspaces = [
    SubspaceTopology(parent, {1, 2}),
    SubspaceTopology(parent, {1, 2, 3}),
    SubspaceTopology(parent, {1}),
]
compare_subspaces(subspaces)
```

### Pattern 3: Testing Convergence

```python
def test_convergence(subspace, sequences):
    """Test convergence of multiple sequences."""
    print(f"\n{'='*70}")
    print(f"CONVERGENCE ANALYSIS: {subspace.name}")
    print(f"{'='*70}\n")
    
    for name, seq in sequences.items():
        print(f"{name}: {seq}")
        limits = subspace.get_limits(seq)
        if limits:
            print(f"  → Converges to: {limits}")
        else:
            print(f"  → No limits")

# Usage
seqs = {
    "Constant": [1, 1, 1],
    "Alternating": [1, 2, 1, 2],
    "Trivial": [1],
}
test_convergence(subspace, seqs)
```

### Pattern 4: Hierarchy Analysis

```python
def analyze_hierarchy(parent, subsets_dict):
    """Analyze subspace hierarchy."""
    print(f"\n{'='*70}")
    print("SUBSPACE HIERARCHY")
    print(f"{'='*70}\n")
    
    subspaces = {}
    for name, subset in subsets_dict.items():
        sub = SubspaceTopology(parent, subset, name=name)
        subspaces[name] = sub
        print(f"{name}:")
        print(f"  Size: {sub.size}")
        print(f"  Open sets: {len(sub.open_sets)}")
        print(f"  Connected: {sub.is_connected()}")
    
    return subspaces

# Usage
hierarchy = analyze_hierarchy(
    parent,
    {
        "Whole": {1, 2, 3, 4, 5},
        "Half": {1, 2, 3},
        "Quarter": {1, 2},
    }
)
```

---

## Best Practices

### ✅ DO

1. **Verify containment before creating subspace**
   ```python
   if subset.issubset(parent.base_set):
       subspace = SubspaceTopology(parent, subset)
   ```

2. **Use descriptive names**
   ```python
   sub = SubspaceTopology(parent, {1,2,3}, name="First Three Elements")
   ```

3. **Check parent properties first**
   ```python
   if parent.is_t2_hausdorff():
       print("Subspace inherits Hausdorff property")
   ```

4. **Compare with parent when needed**
   ```python
   parent_closure = parent.closure(subset)
   sub_closure = subspace.closure(subset)
   ```

5. **Document topology assumptions**
   ```python
   # Subspace inherits T₁ and T₃ from parent
   # But may not inherit compactness
   ```

### ❌ DON'T

1. **Don't assume inherited properties without checking**
   ```python
   # ❌ DON'T assume subspace is compact if parent is
   # Compactness may not be inherited
   ```

2. **Don't forget the intersection formula**
   ```python
   # ❌ DON'T use parent's open sets directly
   # Must intersect with subset: U ∩ A
   ```

3. **Don't confuse relative and absolute topology**
   ```python
   # ❌ DON'T forget these are different:
   # interior_subspace vs interior_in_parent
   ```

4. **Don't create redundant subspaces**
   ```python
   # ❌ DON'T do both:
   sub_way1 = parent.subspace(A).subspace(B)
   sub_way2 = parent.subspace(B)  # Same by transitivity
   ```

5. **Don't ignore density properties**
   ```python
   # ❌ Dense subset may have different properties
   # Check .is_dense() carefully
   ```

---

## Summary

**SubspaceTopology** is a fundamental concept in topology. Key takeaways:

- **Definition:** Open sets are intersections of parent's opens with subset
- **Inclusion:** The inclusion map is always continuous
- **Inheritance:** Separation axioms and regularity inherit; compactness may not
- **Transitivity:** Subspace of subspace can be created as direct subspace
- **Density:** Check if subset is dense in parent or subspace
- **Operations:** Supports product, quotient, and disjoint union

### Key Properties Table

| Property | Inherited | Notes |
|----------|-----------|-------|
| **Connectedness** | ✓ Often | Subspace of connected may be disconnected |
| **Compactness** | ✗ No | Closed subset of compact can be non-compact |
| **Hausdorff** | ✓ Yes | Inherited from parent |
| **Regularity** | ✓ Yes | Inherited from parent |
| **Normality** | ✓ Yes | Inherited from parent |
| **Countability** | ✓ Usually | Usually inherited |
| **Separability** | ✓ Usually | Usually inherited |

---

## Further Reading

### Related Concepts
- **Quotient Topology:** Opposite of subspace - formed by partitioning
- **Product Topology:** Combines multiple spaces
- **Induced Topology:** Same as subspace topology
- **Relative Topology:** Synonym for subspace topology

### Key Theorems
1. **Transitivity:** $(A \subset B \subset X)$ implies subspace topology on $A$ from $B$ equals subspace topology on $A$ from $X$
2. **Inclusion Continuity:** Inclusion map $i: A \to X$ is always continuous
3. **Infinite Product:** Subspace of product equals product of subspaces
4. **Closed Subset:** If $A$ is closed in $X$, subspace topology inherits compactness from $X$

---

**Last Updated:** 2024
**Version:** 1.0
**Status:** Complete Documentation
**Examples:** 100+