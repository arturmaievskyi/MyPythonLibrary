# Numerical Derivatives Guide

## Overview
The `NumericalDerivatives` class provides comprehensive methods for computing derivatives numerically without analytical formulas. This is essential for complex functions, empirical data, and optimization algorithms.

---

## 1. Basic Finite Difference Methods

### Forward Difference
**Formula:** f'(x) ≈ (f(x+h) - f(x)) / h
- First-order accurate
- Good for one-sided approximations
- Less accurate than central difference

```python
def f(x):
    return x**2

derivative = NumericalDerivatives.forward_difference(f, x=2.0, h=1e-5)
# Result: ≈ 4.0
```

### Backward Difference
**Formula:** f'(x) ≈ (f(x) - f(x-h)) / h
- First-order accurate
- Useful when only previous values available
- Similar accuracy to forward difference

```python
derivative = NumericalDerivatives.backward_difference(f, x=2.0, h=1e-5)
# Result: ≈ 4.0
```

### Central Difference
**Formula:** f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
- Second-order accurate
- Best balance between accuracy and efficiency
- Requires function evaluation at both sides

```python
derivative = NumericalDerivatives.central_difference(f, x=2.0, h=1e-5)
# Result: ≈ 4.0 (most accurate)
```

---

## 2. Higher-Order Derivatives

### Second Derivative (Central)
**Formula:** f''(x) ≈ (f(x+h) - 2f(x) + f(x-h)) / h²

```python
def f(x):
    return x**3

second_deriv = NumericalDerivatives.second_derivative_central(f, x=1.0)
# Result: ≈ 6.0 (since d²/dx²(x³) = 6x)
```

### Third Derivative
**Formula:** f'''(x) ≈ (f(x+2h) - 2f(x+h) + 2f(x-h) - f(x-2h)) / (2h³)

```python
third_deriv = NumericalDerivatives.third_derivative_central(f, x=1.0)
# Result: ≈ 6.0 (since d³/dx³(x³) = 6)
```

### Fourth Derivative
**Formula:** f''''(x) ≈ (f(x+2h) - 4f(x+h) + 6f(x) - 4f(x-h) + f(x-2h)) / h⁴

```python
fourth_deriv = NumericalDerivatives.fourth_derivative_central(f, x=1.0)
# Result: ≈ 0.0 (since d⁴/dx⁴(x³) = 0)
```

### N-th Derivative
Compute any order of derivative numerically

```python
# 5th derivative
deriv_5 = NumericalDerivatives.nth_derivative_central(f, x=1.0, n=5)
```

---

## 3. Richardson Extrapolation

**Purpose:** Improve accuracy by combining multiple finite difference estimates

**Principle:** Uses estimates at different step sizes to cancel lower-order error terms

```python
def f(x):
    return sin(x)

# Much more accurate than single finite difference
derivative = NumericalDerivatives.richardson_extrapolation(
    f, x=pi/4, order=1, h=1e-3, levels=3
)
# Result: ≈ cos(π/4) ≈ 0.707 (very accurate)
```

**Advantages:**
- Higher accuracy with same computational cost
- Reduces round-off and truncation errors
- Scalable to multiple extrapolation levels

---

## 4. Complex Step Derivative

**Formula:** f'(x) ≈ Im(f(x + ih)) / h

**Advantages:**
- Machine precision accuracy (no cancellation errors)
- Doesn't require step size optimization
- Very stable

**Requirements:** Function must handle complex numbers

```python
def f(x):
    return sin(x) + x**2

# Extremely accurate derivative
derivative = NumericalDerivatives.complex_step_derivative(f, x=1.0)
# Note: h is extremely small (1e-30)
```

---

## 5. Partial Derivatives (Multivariable Functions)

### Single Partial Derivative
Derivative with respect to one variable, holding others constant

```python
def f(x, y, z):
    return x**2 + y*z + x*y

# Partial derivative with respect to x
df_dx = NumericalDerivatives.partial_derivative(f, point=(1, 2, 3), var_index=0)
# Result: ≈ 2x + y = 4

# Partial derivative with respect to y
df_dy = NumericalDerivatives.partial_derivative(f, point=(1, 2, 3), var_index=1)
# Result: ≈ z + x = 4
```

### Gradient Vector
All first partial derivatives in one vector

```python
def f(x, y):
    return x**2 + y**2

gradient = NumericalDerivatives.gradient(f, point=(1, 2))
# Result: [∂f/∂x, ∂f/∂y] = [2, 4]
```

**Gradient points in direction of steepest increase**

---

## 6. Directional Derivative

**Purpose:** Rate of change in a specified direction

**Formula:** D_u f = ∇f · u (dot product of gradient and unit direction)

```python
def f(x, y):
    return x**2 + y**2

# Directional derivative in direction (1, 1)
dir_deriv = NumericalDerivatives.directional_derivative(
    f, point=(1, 2), direction=[1, 1]
)
# Result: gradient · unit_direction = [2,4] · (1/√2, 1/√2) ≈ 4.24
```

---

## 7. Hessian Matrix

**Purpose:** All second partial derivatives (curvature information)

**Formula:** H[i][j] = ∂²f/∂x_i∂x_j

```python
def f(x, y):
    return x**2 + 2*x*y + 3*y**2

hessian = NumericalDerivatives.hessian(f, point=(1, 1))
# Result: [[2, 2],
#          [2, 6]]
```

**Uses:**
- Newton's optimization method
- Classify critical points (maximum, minimum, saddle)
- Curvature analysis

---

## 8. Jacobian Matrix

**Purpose:** Derivative matrix for vector-valued functions

**Formula:** J[i][j] = ∂f_i/∂x_j

```python
# Vector-valued function: R² → R²
def f1(x, y):
    return x**2 + y
def f2(x, y):
    return x + y**2

func_vector = [f1, f2]
jacobian = NumericalDerivatives.jacobian(func_vector, point=(1, 2))
# Result: [[2, 1],   # [∂f1/∂x, ∂f1/∂y]
#          [1, 4]]   # [∂f2/∂x, ∂f2/∂y]
```

---

## 9. Finite Difference Matrices

### 1D Derivative Matrix
Convert finite differences into matrix form for solving PDEs

```python
# 5x5 central difference matrix with h=0.1
D = NumericalDerivatives.finite_difference_matrix_1d(n=5, h=0.1, method='central')
# Apply to array of function values to get derivatives
```

### 2D Laplacian Matrix
Used for solving 2D partial differential equations

```python
# 3x3 grid points in each direction
L = NumericalDerivatives.finite_difference_matrix_2d(n=3, m=3, h=0.1)
```

---

## 10. Optimal Step Size Selection

**Problem:** Choosing h is critical - too large (truncation error), too small (rounding error)

**Solution:** Automatic optimal step size

```python
def f(x):
    return sin(x) + x**3

optimal_h = NumericalDerivatives.optimal_step_size(f, x=1.0, derivative_order=1)
# Returns recommended step size balancing errors
```

---

## 11. Adaptive Derivative Computation

**Purpose:** Automatically compute derivative to desired accuracy

**Method:** Iteratively refines step size and uses Richardson extrapolation

```python
def f(x):
    return exp(x) * sin(x)

derivative, error = NumericalDerivatives.adaptive_derivative(
    f, x=1.0, tolerance=1e-8
)
# Automatically finds correct h and returns derivative with error estimate
```

---

## 12. Error Analysis

### Derivative Error Estimate
Compare multiple methods and see their discrepancies

```python
def f(x):
    return x**4

errors = NumericalDerivatives.derivative_error_estimate(
    f, x=2.0, true_derivative=32.0, h=1e-5
)
# Returns: {
#   'forward': ...,
#   'central': ...,
#   'richardson': ...,
#   'forward_error': ...,
#   'central_error': ...,
#   'richardson_error': ...
# }
```

### Test Derivative
Verify if numerical derivative matches expected

```python
result = NumericalDerivatives.test_derivative(
    f, x=2.0, expected_derivative=32.0
)
# {'numerical': ..., 'absolute_error': ..., 'passed': True/False}
```

---

## Comparison of Methods

| Method | Accuracy | Stability | Speed | Uses |
|--------|----------|-----------|-------|------|
| Forward Diff | O(h) | Good | Fast | One-sided cases |
| Backward Diff | O(h) | Good | Fast | One-sided cases |
| Central Diff | O(h²) | Good | Fast | General purpose |
| Richardson | O(h⁴) | Excellent | Moderate | High accuracy needed |
| Complex Step | O(h²) | Excellent | Moderate | Very high accuracy |

---

## Best Practices

1. **Start with Central Difference** - Best balance for most applications
2. **Use Richardson Extrapolation** - When higher accuracy needed without complex setup
3. **Complex Step for Maximum Accuracy** - When function accepts complex input
4. **Check with Multiple Methods** - Verify results using different techniques
5. **Adaptive Step Size** - Let the algorithm choose optimal h when uncertain
6. **Error Analysis** - Always quantify uncertainty in your derivatives

---

## Common Pitfalls

❌ **Too large step size** → Large truncation error
❌ **Too small step size** → Large rounding error (cancellation)
❌ **Ignoring function smoothness** → Unreliable results for discontinuous functions
❌ **Using forward/backward when central available** → Unnecessary accuracy loss
❌ **No validation** → Always verify with analytical derivatives if possible

---

## Example: Full Derivative Analysis

```python
def f(x):
    return x**3 - 2*x**2 + x - 5

x_test = 2.0

# Get derivative using multiple methods
forward = NumericalDerivatives.forward_difference(f, x_test)
central = NumericalDerivatives.central_difference(f, x_test)
richardson = NumericalDerivatives.richardson_extrapolation(f, x_test)
adaptive, error = NumericalDerivatives.adaptive_derivative(f, x_test)

# Check errors
errors = NumericalDerivatives.derivative_error_estimate(
    f, x_test, true_derivative=7.0  # 3x² - 4x + 1 = 7 at x=2
)

print(f"Forward: {forward:.8f}")
print(f"Central: {central:.8f}")
print(f"Richardson: {richardson:.8f}")
print(f"Adaptive: {adaptive:.8f} (error: {error:.2e})")
print(f"Expected: 7.0")
```

---

## References

- Finite Difference Formulas: Standard numerical analysis textbooks
- Richardson Extrapolation: Numerical Recipes in C
- Complex Step Derivative: Squire & Trapp (1998)
- Optimal Step Size: Numerical Methods for Unconstrained Optimization