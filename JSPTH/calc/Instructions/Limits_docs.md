# Limits in Calculus - Comprehensive Guide

## Overview
The `Limits` class provides numerical methods for computing and analyzing limits, a fundamental concept in calculus. This module covers finite limits, infinite limits, sequences, series, and indeterminate forms.

---

## 1. Basic Limit Computation

### Limit from the Right
**Notation:** lim f(x) as x → a⁺
Approaches point from positive side.

```python
def f(x):
    return (x**2 - 1) / (x - 1)

# Limit as x → 1 from the right
limit_right = Limits.limit_from_right(f, x_val=1.0, epsilon=1e-8)
# Result: ≈ 2.0
```

**Usage:** When function is only defined on one side of a point.

### Limit from the Left
**Notation:** lim f(x) as x → a⁻
Approaches point from negative side.

```python
limit_left = Limits.limit_from_left(f, x_val=1.0, epsilon=1e-8)
# Result: ≈ 2.0
```

### Two-Sided Limit
**Notation:** lim f(x) as x → a
Approaches from both sides - limits must agree!

```python
limit = Limits.limit_two_sided(f, x_val=1.0, epsilon=1e-8)
# Result: ≈ 2.0 (if left and right limits match)
# Raises error if they differ
```

**Key Point:** Two-sided limit exists only if left and right limits are equal.

---

## 2. Limits at Infinity

### Positive Infinity
**Notation:** lim f(x) as x → +∞

```python
def f(x):
    return (2*x**2 + 3*x + 1) / (x**2 + 5)

limit_pos_inf = Limits.limit_to_positive_infinity(f)
# Result: ≈ 2.0
# (Leading coefficients: 2x²/x² = 2)
```

### Negative Infinity
**Notation:** lim f(x) as x → -∞

```python
limit_neg_inf = Limits.limit_to_negative_infinity(f)
# Result: ≈ 2.0
```

**Finding Horizontal Asymptotes:**
```python
asymptotes = Limits.horizontal_asymptote(f)
# Returns: {'positive_infinity': 2.0, 'negative_infinity': 2.0}
# Horizontal asymptote: y = 2
```

---

## 3. Sequence Limits

### Basic Sequence Convergence
Does a sequence converge? To what value?

```python
# Sequence: 1/n converging to 0
sequence = [1/n for n in range(1, 1001)]

result = Limits.sequence_limit(sequence, tolerance=1e-10)
# Returns: {
#   'converged': True,
#   'limit': 0.001,  # Last term ≈ 1/1000
#   'convergence_rate': < 1e-10,
#   'num_terms': 1000
# }
```

### Convergence Analysis
Detailed study of how sequence approaches limit.

```python
# Sequence: (-1/2)^n converging to 0
sequence = [((-1/2)**n) for n in range(100)]

analysis = Limits.sequence_convergence_analysis(sequence, num_terms_analyze=10)
# Returns: {
#   'last_term': ...,
#   'differences': [differences between consecutive terms],
#   'difference_trend': 'decreasing',
#   'convergence_ratios': [...],
#   'linear_convergence': True,
#   'quadratic_convergence': False
# }
```

### Convergence Rate Classification

**Sublinear:** Very slow convergence (ratio → 1)
```python
# Example: 1/√n sequence
sequence = [1/sqrt(n) for n in range(1, 1001)]
rate = Limits.convergence_rate(sequence)
# Result: {'type': 'sublinear', 'rate': 0.9...}
```

**Linear:** Geometric convergence (fixed ratio < 1)
```python
# Example: (1/2)^n
sequence = [(0.5)**n for n in range(100)]
rate = Limits.convergence_rate(sequence)
# Result: {'type': 'linear', 'rate': 0.5}
```

**Quadratic:** Very fast convergence (ratio → 0)
```python
# Example: (1/2)^(2^n)
sequence = [(0.5)**(2**n) for n in range(10)]
rate = Limits.convergence_rate(sequence)
# Result: {'type': 'quadratic_or_higher', 'rate': tiny}
```

---

## 4. Series Convergence

### Partial Sums
Compute running totals of series terms.

```python
# Harmonic series: 1 + 1/2 + 1/3 + ...
def harmonic_terms():
    n = 1
    while True:
        yield 1/n
        n += 1

partial_sums = Limits.series_partial_sums(harmonic_terms(), num_terms=100)
# Result: [1.0, 1.5, 1.833..., 2.083..., ...]
# Shows series grows without bound
```

### Series Limit (Infinite Sum)
Does series converge? What's its sum?

```python
# Geometric series: 1 + 1/2 + 1/4 + 1/8 + ...
def geometric_series():
    n = 0
    while True:
        yield (0.5)**n
        n += 1

result = Limits.series_limit(geometric_series(), num_terms=100)
# Returns: {
#   'sum': 1.999...,  # True sum is 2
#   'converged': True,
#   'num_terms_used': 100,
#   'final_term_change': very small
# }
```

**Key Insight:** Geometric series 1 + r + r² + ... = 1/(1-r) if |r| < 1

---

## 5. Indeterminate Forms

### Detection
Identify indeterminate forms that need special handling.

```python
def f(x):
    return (x**2 - 1) / (x - 1)  # 0/0 form at x=1

form = Limits.is_indeterminate_form(f, x_val=1.0)
# Result: "0/0"
```

**Common Indeterminate Forms:**
- **0/0:** Numerator and denominator both → 0
- **∞/∞:** Both → infinity
- **0·∞:** Product of vanishing and infinite quantities
- **1^∞:** One to infinite power
- **∞ - ∞:** Difference of infinities
- **0^0:** Zero to zero power

---

## 6. L'Hôpital's Rule

Resolves 0/0 and ∞/∞ indeterminate forms.

**Rule:** If f(a) = 0 and g(a) = 0, then
lim f(x)/g(x) = lim f'(x)/g'(x) as x → a

### Application

```python
# Problem: lim (x² - 1)/(x - 1) as x → 1
# This is 0/0 form

def numerator(x):
    return x**2 - 1

def denominator(x):
    return x - 1

def numerator_derivative(x):
    return 2*x  # d/dx(x² - 1) = 2x

def denominator_derivative(x):
    return 1   # d/dx(x - 1) = 1

limit = Limits.lhopital_rule(None, x_val=1.0, 
                             numerator_deriv=numerator_derivative,
                             denominator_deriv=denominator_derivative)
# Result: 2*1 / 1 = 2.0
```

**When to use:**
- Form is definitely 0/0 or ∞/∞
- Derivatives exist
- Direct evaluation fails

**Common Example:**
```python
# lim sin(x)/x as x → 0
def num(x):
    return sin(x)

def denom(x):
    return x

def num_deriv(x):
    return cos(x)

def denom_deriv(x):
    return 1

limit = Limits.lhopital_rule(None, 0, num_deriv, denom_deriv)
# Result: cos(0)/1 = 1
```

---

## 7. Squeeze Theorem

**Statement:** If f(x) ≤ g(x) ≤ h(x) near a, and lim f(x) = lim h(x) = L,
then lim g(x) = L

### Application

```python
# Example: lim x·sin(1/x) as x → 0
# Squeeze: -|x| ≤ x·sin(1/x) ≤ |x|
# Both bounds → 0

def lower_bound(x):
    return -abs(x)

def target_func(x):
    return x * sin(1/x) if x != 0 else 0

def upper_bound(x):
    return abs(x)

limit = Limits.squeeze_theorem(lower_bound, target_func, upper_bound, x_val=0.0)
# Result: 0 (because bounds converge to 0)
```

**Key Insight:** Even if you can't evaluate limit directly, bounding functions can help!

---

## 8. Limit Theorems

**Rules that make limit computation easier:**

### Sum Rule
lim [f(x) + g(x)] = lim f(x) + lim g(x)

```python
def f(x):
    return x**2

def g(x):
    return 3*x + 1

limit_sum = Limits.limit_of_sum(f, g, x_val=2.0)
# = lim(x²) + lim(3x+1) = 4 + 7 = 11
```

### Product Rule
lim [f(x)·g(x)] = lim f(x) · lim g(x)

```python
limit_product = Limits.limit_of_product(f, g, x_val=2.0)
# = 4 · 7 = 28
```

### Quotient Rule
lim [f(x)/g(x)] = lim f(x) / lim g(x) (if denominator ≠ 0)

```python
limit_quotient = Limits.limit_of_quotient(f, g, x_val=2.0)
# = 4 / 7 ≈ 0.571
```

### Power Rule
lim [f(x)]^n = [lim f(x)]^n

```python
limit_power = Limits.limit_of_power(f, x_val=2.0, exponent=3)
# = 4³ = 64
```

### Composition Rule
lim f(g(x)) = f(lim g(x)) (if f is continuous)

```python
def outer(x):
    return sqrt(x)

def inner(x):
    return x**2 + 3

limit_comp = Limits.limit_of_composition(outer, inner, x_val=2.0)
# = √(4 + 3) = √7 ≈ 2.646
```

---

## 9. Asymptotes

### Horizontal Asymptotes
Lines that function approaches as x → ±∞

```python
def f(x):
    return (2*x + 1) / (x - 3)

asymptotes = Limits.horizontal_asymptote(f)
# Both limits → 2, so y = 2 is horizontal asymptote
```

### Vertical Asymptotes
Lines where function "blows up"

```python
def f(x):
    return 1 / (x - 2)

asymptotes = Limits.vertical_asymptote_search(f, search_range=(-10, 10), num_divisions=100)
# Result: [≈2.0]  (division by zero)
```

### Oblique (Slant) Asymptotes
Linear asymptotes for rational functions

```python
def f(x):
    return (x**2 + 2*x) / (x - 1)  # Degree numerator > denominator

oblique = Limits.oblique_asymptote(f, x_range=(-100, 100))
# Result: {'slope': 1.0, 'intercept': 3.0}
# Asymptote: y = x + 3
```

---

## 10. Continuity Analysis

### Check Continuity at a Point
Is function continuous at x = a?

```python
def f(x):
    return x**2 if x != 1 else 0  # Discontinuous at x=1

is_cont = Limits.is_continuous_at(f, x_val=1.0)
# Result: False
# (limit = 1, but f(1) = 0)
```

### Find Discontinuities
Locate problematic points in interval.

```python
def f(x):
    return 1/(x-1) if x != 1 else 0

discontinuities = Limits.find_discontinuities(f, search_range=(-5, 5), num_points=100)
# Result: [points near 1.0]
```

### Classify Discontinuities

**Removable Discontinuity:** Limit exists but ≠ function value
- Can be "fixed" by redefining function at one point
```python
def f(x):
    return (x**2 - 1)/(x - 1)  # Undefined at x=1
    # But lim f(x) = 2 as x→1, so removable
```

**Jump Discontinuity:** Left and right limits exist but differ
```python
def f(x):
    return -1 if x < 0 else 1  # Jump at x=0
    # Left limit: -1, Right limit: 1
```

**Essential Discontinuity:** One or both limits don't exist
```python
def f(x):
    return sin(1/x) if x != 0 else 0  # Oscillates wildly near 0
```

### Classify Discontinuity Type

```python
summary = Limits.limit_summary(f, x_val=1.0)
# Returns comprehensive analysis including:
# - Function value
# - Left/right limits
# - Continuity status
# - Discontinuity type (removable/jump/essential)
```

---

## 11. Limit Verification

**Epsilon-Delta Definition:**
lim f(x) = L as x → a means:
For any ε > 0, there exists δ > 0 such that
if 0 < |x - a| < δ, then |f(x) - L| < ε

### Verify a Limit

```python
def f(x):
    return x**2

# Verify: lim x² = 4 as x → 2
verification = Limits.verify_limit(f, x_val=2.0, suspected_limit=4.0,
                                   epsilon_x=1e-8, epsilon_y=1e-6)
# Result: {
#   'verified': True,
#   'satisfaction_rate': 0.95+,
#   'test_points': [...],
#   'suspected_limit': 4.0
# }
```

---

## 12. Comprehensive Limit Summary

Analyze everything about a limit at once:

```python
def f(x):
    return (x**3 - 8) / (x - 2)

summary = Limits.limit_summary(f, x_val=2.0)
# Returns: {
#   'point': 2.0,
#   'function_value': undefined (division by 0),
#   'left_limit': 12.0,
#   'right_limit': 12.0,
#   'two_sided_limit': 12.0,
#   'is_continuous': False,
#   'discontinuity_type': 'removable'
# }
```

---

## Practical Workflow

### Finding a Limit

**Step 1: Try Direct Substitution**
```python
def f(x):
    return x**2 + 3*x + 2

limit = f(5)  # Works if no division by zero
```

**Step 2: Check for Indeterminate Form**
```python
form = Limits.is_indeterminate_form(f, x_val=a)
```

**Step 3: Choose Method**
- If 0/0 → Use L'Hôpital's rule or factor
- If ∞/∞ → Use L'Hôpital's rule or divide by leading term
- If removable → Redefine function
- If jump → Left and right limits differ

**Step 4: Verify Result**
```python
result = Limits.verify_limit(f, x_val=a, suspected_limit=L)
```

---

## Common Limits to Know

```python
# sin(x)/x → 1 as x → 0
# (1 + x)^(1/x) → e as x → 0
# (1 + 1/x)^x → e as x → ∞
# ln(1 + x)/x → 1 as x → 0
# (e^x - 1)/x → 1 as x → 0
# (a^x - 1)/x → ln(a) as x → 0
```

---

## Best Practices

✅ **DO:**
- Start with direct substitution
- Check left/right limits separately
- Verify limits with multiple methods
- Use asymptotic analysis for infinity limits
- Classify discontinuities when finding limits

❌ **DON'T:**
- Apply L'Hôpital repeatedly without checking
- Assume left limit = right limit without verifying
- Neglect domain restrictions
- Use indeterminate forms without resolving
- Trust single method - verify with another

---

## Troubleshooting

**Issue:** "Cannot compute limit"
- Function may have essential discontinuity
- Try smaller epsilon value
- Check if function is defined near point
- Use asymptotic methods for infinity

**Issue:** "Left and right limits don't match"
- Function has jump discontinuity
- Two-sided limit doesn't exist
- Report left and right separately

**Issue:** L'Hôpital not converging
- May not be 0/0 or ∞/∞ form
- Derivatives may be complicated
- Try other methods (factoring, rationalization)