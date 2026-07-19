# Extrema and Critical Points - Comprehensive Guide

## Overview
The `Extrema` class provides methods for finding and analyzing critical points, local/global extrema, inflection points, and optimization. Essential for calculus and optimization problems.

---

## 1. Critical Points

Critical points occur where the derivative equals zero: **f'(x) = 0**

### Finding Critical Points
```python
def f(x):
    return x**3 - 3*x**2 + 2*x + 1

# Find all critical points in [-1, 4]
critical_points = Extrema.find_critical_points(f, search_range=(-1, 4), num_divisions=1000)
# Result: [x1, x2, ...] where f'(x_i) ≈ 0
```

**Why find critical points?**
- Maxima and minima occur here (in smooth functions)
- Needed for optimization problems
- Essential for sketching accurate graphs

---

## 2. First Derivative Test

**Purpose:** Classify critical point as max, min, or neither based on derivative sign changes.

**Test Logic:**
- f' changes from **+** to **−** → **LOCAL MAXIMUM** (peaks)
- f' changes from **−** to **+** → **LOCAL MINIMUM** (valleys)
- f' doesn't change sign → **Neither** (saddle point or inflection)

### Application

```python
def f(x):
    return x**3 - 3*x

# Find critical point
cp = 1.0

# Analyze using first derivative test
result = Extrema.first_derivative_test(f, critical_point=cp, delta=0.01)
# Returns:
# {
#   'critical_point': 1.0,
#   'function_value': -2.0,
#   'left_derivative': -2.71... (negative),
#   'right_derivative': 2.71... (positive),
#   'type': 'LOCAL MINIMUM',
#   'reason': 'Derivative changes from - to +'
# }
```

**Visual:**
```
   Local Min        Local Max
       ↓               ↓
    ___/               \___
   /                       \
---•-------•-------•-------•---
   f' > 0  f' = 0  f' < 0  f' = 0
```

---

## 3. Second Derivative Test

**Purpose:** Classify critical point using concavity information.

**Test Logic:**
- f''(c) > 0 → Concave up (∪) → **LOCAL MINIMUM**
- f''(c) < 0 → Concave down (∩) → **LOCAL MAXIMUM**
- f''(c) = 0 → **INCONCLUSIVE** (use first derivative test)

### Application

```python
def f(x):
    return x**2 - 4*x + 3

# Analyze critical point using second derivative test
cp = 2.0
result = Extrema.second_derivative_test(f, critical_point=cp)
# Returns:
# {
#   'critical_point': 2.0,
#   'function_value': -1.0,
#   'first_derivative': ≈0 (critical point check),
#   'second_derivative': 2.0 (> 0),
#   'type': 'LOCAL MINIMUM',
#   'concavity': 'Concave up (∪)'
# }
```

**Comparison:**

| Test | Advantage | Disadvantage |
|------|-----------|--------------|
| First Derivative | Works always | Need to evaluate derivative twice |
| Second Derivative | Direct, uses second derivative | Fails if f''(c) = 0 |

---

## 4. Higher-Order Derivative Test

**For harder cases** when both first and second derivative tests fail.

**Rule:** If f'(c) = f''(c) = ... = f^(n-1)(c) = 0 but f^(n)(c) ≠ 0:
- If **n is even**:
  - f^(n)(c) > 0 → LOCAL MINIMUM
  - f^(n)(c) < 0 → LOCAL MAXIMUM
- If **n is odd** → SADDLE POINT

### Example: f(x) = x⁴

```python
def f(x):
    return x**4

result = Extrema.higher_order_derivative_test(f, critical_point=0, max_order=4)
# At x=0:
# - f'(0) = 0
# - f''(0) = 0
# - f'''(0) = 0
# - f''''(0) = 24 > 0 (4th derivative, even)
# Result: LOCAL MINIMUM (correctly identified!)
```

---

## 5. Inflection Points

**Inflection points** are where **concavity changes**: f''(x) = 0 with sign change.

### Finding Inflection Points

```python
def f(x):
    return x**3 - 3*x**2 + 2

# Find inflection points in [0, 3]
inflection_points = Extrema.find_inflection_points(f, search_range=(0, 3), num_divisions=500)
# Result: [x1, x2, ...] where concavity changes
```

### Classifying Inflection Points

```python
# Confirm an inflection point
ip = 1.0
classification = Extrema.classify_inflection_point(f, inflection_point=ip)
# Returns:
# {
#   'inflection_point': 1.0,
#   'function_value': -0.0,
#   'left_second_deriv': -6.0 (concave down),
#   'right_second_deriv': 6.0 (concave up),
#   'is_inflection': True,
#   'concavity_change': 'Concave down (∩) to Concave up (∪)'
# }
```

**Visual Representation:**
```
        Inflection Point
               ↓
    ∩∩∩∩∩∩∩∩∪∪∪∪∪∪∪∪
        Changes curvature
```

---

## 6. Global vs Local Extrema

### Local Extrema
- Extrema within a small neighborhood
- Can have multiple local extrema in one function

### Global Extrema
- **Largest** and **smallest** values on entire closed interval [a, b]
- Occur at:
  - Critical points where f'(x) = 0
  - Endpoints x = a or x = b

### Finding Global Extrema

```python
def f(x):
    return x**3 - 3*x**2 + 2

# Find absolute max and min on [-1, 3]
result = Extrema.find_global_extrema(f, search_range=(-1, 3))
# Returns:
# {
#   'global_minimum': {'x': 2.0, 'y': -2.0},
#   'global_maximum': {'x': -1.0, 'y': 6.0},
#   'all_candidates': [...],
#   'critical_points_checked': [0, 2]
# }
```

**Important:** Global extrema are found by checking:
1. All critical points
2. Both endpoints

---

## 7. Optimization Algorithms

### Gradient Descent
Iteratively move downhill to find minimum.

**Algorithm:** x_{n+1} = x_n - learning_rate × f'(x_n)

```python
def f(x):
    return (x - 3)**2 + 2

# Find minimum starting from x = 0
result = Extrema.gradient_descent(f, start_x=0, learning_rate=0.1, num_iterations=1000)
# Returns:
# {
#   'algorithm': 'Gradient Descent',
#   'minimum': 3.0,
#   'function_value': 2.0,
#   'iterations': 47,
#   'converged': True,
#   'history': [last 10 steps]
# }
```

**Hyperparameters:**
- **learning_rate**: Too small = slow; Too large = overshoots
- **num_iterations**: Maximum steps to take

---

### Newton's Method
Faster convergence using second derivative information.

**Algorithm:** x_{n+1} = x_n - f'(x_n) / f''(x_n)

```python
def f(x):
    return x**2 - 4*x + 3

# Find critical point
result = Extrema.newton_method(f, start_x=0, num_iterations=100)
# Returns:
# {
#   'algorithm': 'Newton\'s Method',
#   'critical_point': 2.0,
#   'function_value': -1.0,
#   'first_derivative': ≈0,
#   'second_derivative': 2.0,
#   'iterations': 5,
#   'converged': True
# }
```

**Advantages:** Quadratic convergence (very fast)
**Disadvantages:** Needs second derivative; can diverge if f''(c) ≈ 0

---

### Bisection Search
Robust method for finding critical points in an interval.

```python
def f(x):
    return x**3 - 2*x

# Critical point known to be in [0, 2]
result = Extrema.bisection_search(f, a=0, b=2, num_iterations=100)
# Returns:
# {
#   'algorithm': 'Bisection Search',
#   'critical_point': 0.816...,
#   'iterations': 25,
#   'converged': True
# }
```

**Advantages:** Always works in interval
**Disadvantages:** Slower than Newton's method

---

## 8. Multivariable Optimization (2D)

### Finding Critical Points in 2D

Critical points where ∇f = 0, i.e., **∂f/∂x = 0** AND **∂f/∂y = 0**

```python
def f(x, y):
    return x**2 + y**2 - 4*x + 2*y + 5

# Find critical points in region
critical_points = Extrema.find_critical_points_2d(
    f, 
    x_range=(0, 5), 
    y_range=(-3, 2),
    x_divisions=50,
    y_divisions=50
)
# Result: [(2.0, -1.0)]  Critical point found
```

### Classifying 2D Critical Points (Hessian Test)

The **Hessian matrix** H contains all second partial derivatives:
```
H = [∂²f/∂x²    ∂²f/∂x∂y]
    [∂²f/∂x∂y   ∂²f/∂y² ]
```

**Classification** using determinant D = det(H):
- **D > 0 and f_xx > 0** → **LOCAL MINIMUM** (valley)
- **D > 0 and f_xx < 0** → **LOCAL MAXIMUM** (peak)
- **D < 0** → **SADDLE POINT** (mountain pass)
- **D = 0** → **INCONCLUSIVE**

```python
def f(x, y):
    return x**2 + y**2

# Classify critical point (0, 0)
classification = Extrema.classify_critical_point_2d(f, x=0, y=0)
# Returns:
# {
#   'critical_point': (0, 0),
#   'function_value': 0,
#   'gradient': (0, 0),
#   'hessian': [[2, 0], [0, 2]],
#   'hessian_determinant': 4 (> 0),
#   'fxx': 2 (> 0),
#   'type': 'LOCAL MINIMUM',
#   'reason': 'D > 0 and f_xx > 0'
# }
```

**Geometric Intuition:**
```
Minimum          Maximum         Saddle Point
    ∪              ∩              /  \
   / \            / \            /    \
  /   \          /   \          /      \
```

---

## 9. Constrained Optimization (Lagrange Multipliers)

Optimize **f(x, y)** subject to constraint **g(x, y) = 0**

**Method:** Find point where ∇f = λ∇g (gradients are parallel)

```python
# Maximize x² + y² subject to x + y = 1
def objective(x, y):
    return x**2 + y**2

def constraint(x, y):
    return x + y - 1  # = 0

result = Extrema.lagrange_multipliers_2var(
    objective, constraint, 
    x_init=0.5, y_init=0.5,
    num_iterations=100
)
# Returns:
# {
#   'algorithm': 'Lagrange Multipliers',
#   'optimal_point': (0.5, 0.5),
#   'function_value': 0.5,
#   'constraint_value': ≈0,
#   'lagrange_multiplier': 1.0,
#   'converged': True
# }
```

**Applications:**
- Minimize/maximize subject to restrictions
- Resource allocation problems
- Engineering design with constraints

---

## 10. Comprehensive Extrema Analysis

Run all tests at once for complete understanding:

```python
def f(x):
    return x**4 - 4*x**3 + 6*x**2 - 4*x + 1

# Complete analysis
analysis = Extrema.complete_extrema_analysis(f, search_range=(-1, 3))
# Returns:
# {
#   'interval': (-1, 3),
#   'critical_points': [
#     {
#       'point': 1.0,
#       'function_value': 0.0,
#       'first_derivative_test': {...},
#       'second_derivative_test': {...}
#     }
#   ],
#   'inflection_points': [...],
#   'global_extrema': {
#     'global_minimum': {...},
#     'global_maximum': {...}
#   },
#   'boundary': {...}
# }
```

---

## 11. Practical Workflow

### Step 1: Find Critical Points
```python
critical_points = Extrema.find_critical_points(f, search_range)
```

### Step 2: Classify Each Critical Point
```python
for cp in critical_points:
    classification = Extrema.second_derivative_test(f, cp)
    # or first_derivative_test if second fails
```

### Step 3: Find Global Extrema (on closed interval)
```python
global_extrema = Extrema.find_global_extrema(f, search_range)
```

### Step 4: Find Inflection Points
```python
inflection_points = Extrema.find_inflection_points(f, search_range)
```

### Step 5: Sketch Graph
- Plot critical points (maxima/minima)
- Plot inflection points (concavity changes)
- Show increasing/decreasing intervals
- Show concave up/down regions

---

## 12. Quick Reference Table

| Feature | Method | Returns |
|---------|--------|---------|
| Find critical points | `find_critical_points()` | List of x-values |
| Classify with 1st test | `first_derivative_test()` | min/max/neither |
| Classify with 2nd test | `second_derivative_test()` | min/max/inconclusive |
| Find inflection points | `find_inflection_points()` | List of x-values |
| Global extrema | `find_global_extrema()` | max and min values |
| Minimize function | `gradient_descent()` | Local minimum |
| Optimize faster | `newton_method()` | Critical point |
| 2D analysis | `find_critical_points_2d()` | Critical points (x,y) |
| 2D classification | `classify_critical_point_2d()` | min/max/saddle |
| With constraints | `lagrange_multipliers_2var()` | Constrained extremum |

---

## Common Examples

### Example 1: Polynomial
```python
def f(x):
    return x**3 - 3*x**2 - 9*x + 5

# Find critical points
cp = Extrema.find_critical_points(f, (-5, 5))
# Result: [-1, 3]

# Classify
for point in cp:
    test = Extrema.second_derivative_test(f, point)
    print(test['type'])
# Output: LOCAL MAXIMUM, LOCAL MINIMUM
```

### Example 2: Optimization Problem
"Minimize cost function: C(x) = x² - 10x + 30"

```python
def cost(x):
    return x**2 - 10*x + 30

result = Extrema.gradient_descent(cost, start_x=0)
# Result: Minimum at x = 5, cost = 5
```

### Example 3: 2D Surface
"Find extrema of f(x,y) = x² + 2xy + 3y²"

```python
def f(x, y):
    return x**2 + 2*x*y + 3*y**2

cp = Extrema.find_critical_points_2d(f, (-2, 2), (-2, 2))
# Result: [(0, 0)]

classification = Extrema.classify_critical_point_2d(f, 0, 0)
# Result: LOCAL MINIMUM (saddle-shaped paraboloid)
```

---

## Best Practices

✅ **DO:**
- Always verify critical points exist in your interval
- Use multiple tests (first AND second derivative) for confirmation
- Check endpoints for global extrema on closed intervals
- Use appropriate optimization algorithm for your problem
- Visualize results when possible

❌ **DON'T:**
- Forget to check endpoints for global extrema
- Rely on second derivative test alone if f''(c) ≈ 0
- Use gradient descent for functions with many local minima (try multiple starting points)
- Ignore constraint violations in Lagrange multipliers
- Trust optimization without verifying convergence

---

## Troubleshooting

**Problem:** "Can't find critical points"
- Solution: Increase `num_divisions` for finer sampling
- Check if function is differentiable in your interval
- Try different `h` value for derivatives

**Problem:** "Second derivative test says inconclusive"
- Solution: Use first derivative test instead
- Try higher-order derivative test
- Use graphical inspection

**Problem:** "Optimization doesn't converge"
- Solution: Adjust learning rate (smaller → slower, more stable)
- Increase `num_iterations`
- Try different starting point
- Consider Newton's method for faster convergence

**Problem:** "Different results from different methods"
- Solution: Some methods find local, others global extrema
- Always verify with graphing
- Check interval for multiple critical points