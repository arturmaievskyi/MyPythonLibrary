from math import *

class NumericalDerivatives:
    """
    Comprehensive class for numerical differentiation methods.
    Includes various techniques for computing derivatives numerically.
    """
    
    # ==================== BASIC FINITE DIFFERENCE METHODS ====================
    
    @staticmethod
    def forward_difference(func, x, h=1e-5):
        """
        Forward difference approximation (first-order accurate).
        f'(x) ≈ (f(x+h) - f(x)) / h
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate derivative
        """
        return (func(x + h) - func(x)) / h
    
    @staticmethod
    def backward_difference(func, x, h=1e-5):
        """
        Backward difference approximation (first-order accurate).
        f'(x) ≈ (f(x) - f(x-h)) / h
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate derivative
        """
        return (func(x) - func(x - h)) / h
    
    @staticmethod
    def central_difference(func, x, h=1e-5):
        """
        Central difference approximation (second-order accurate).
        f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate derivative
        """
        return (func(x + h) - func(x - h)) / (2 * h)
    
    # ==================== HIGHER-ORDER DERIVATIVES ====================
    
    @staticmethod
    def second_derivative_central(func, x, h=1e-5):
        """
        Second derivative using central difference (second-order accurate).
        f''(x) ≈ (f(x+h) - 2*f(x) + f(x-h)) / h²
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate second derivative
        """
        return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)
    
    @staticmethod
    def second_derivative_forward(func, x, h=1e-5):
        """
        Second derivative using forward difference.
        f''(x) ≈ (f(x+2h) - 2*f(x+h) + f(x)) / h²
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate second derivative
        """
        return (func(x + 2*h) - 2*func(x + h) + func(x)) / (h ** 2)
    
    @staticmethod
    def second_derivative_backward(func, x, h=1e-5):
        """
        Second derivative using backward difference.
        f''(x) ≈ (f(x) - 2*f(x-h) + f(x-2h)) / h²
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate second derivative
        """
        return (func(x) - 2*func(x - h) + func(x - 2*h)) / (h ** 2)
    
    @staticmethod
    def third_derivative_central(func, x, h=1e-5):
        """
        Third derivative using central difference.
        f'''(x) ≈ (f(x+2h) - 2*f(x+h) + 2*f(x-h) - f(x-2h)) / (2h³)
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate third derivative
        """
        return (func(x + 2*h) - 2*func(x + h) + 2*func(x - h) - func(x - 2*h)) / (2 * h**3)
    
    @staticmethod
    def fourth_derivative_central(func, x, h=1e-5):
        """
        Fourth derivative using central difference.
        f''''(x) ≈ (f(x+2h) - 4*f(x+h) + 6*f(x) - 4*f(x-h) + f(x-2h)) / h⁴
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param h: Step size
        :return: Approximate fourth derivative
        """
        return (func(x + 2*h) - 4*func(x + h) + 6*func(x) - 4*func(x - h) + func(x - 2*h)) / (h ** 4)
    
    @staticmethod
    def nth_derivative_central(func, x, n, h=1e-5):
        """
        Compute nth derivative using finite differences.
        Uses binomial coefficients for the formula.
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param n: Order of derivative
        :param h: Step size
        :return: Approximate nth derivative
        """
        if n == 1:
            return NumericalDerivatives.central_difference(func, x, h)
        elif n == 2:
            return NumericalDerivatives.second_derivative_central(func, x, h)
        elif n == 3:
            return NumericalDerivatives.third_derivative_central(func, x, h)
        elif n == 4:
            return NumericalDerivatives.fourth_derivative_central(func, x, h)
        else:
            # General formula using binomial expansion
            from math import comb, factorial
            result = 0
            sign = (-1) ** n if n % 2 == 0 else 1
            
            for k in range(n + 1):
                coeff = comb(n, k) * ((-1) ** (n - k))
                result += coeff * func(x + (k - n/2) * h)
            
            return result / (h ** n)
    
    # ==================== RICHARDSON EXTRAPOLATION ====================
    
    @staticmethod
    def richardson_extrapolation(func, x, order=1, h=1e-3, levels=3):
        """
        Richardson extrapolation for improved derivative accuracy.
        Combines multiple finite difference estimates with different step sizes.
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate derivative
        :param order: Order of derivative (1 or 2)
        :param h: Initial step size
        :param levels: Number of extrapolation levels
        :return: Improved derivative estimate
        """
        if order == 1:
            diff_func = NumericalDerivatives.central_difference
        elif order == 2:
            diff_func = NumericalDerivatives.second_derivative_central
        else:
            raise ValueError("Richardson extrapolation supports order 1 or 2")
        
        # Initialize table for Richardson extrapolation
        table = [[0 for _ in range(levels)] for _ in range(levels)]
        
        # First column: finite difference estimates with different step sizes
        for i in range(levels):
            step = h / (2 ** i)
            table[i][0] = diff_func(func, x, step)
        
        # Fill in the extrapolation table
        for j in range(1, levels):
            for i in range(levels - j):
                p = 2 ** (2 * j)  # Power for convergence rate
                table[i][j] = (p * table[i + 1][j - 1] - table[i][j - 1]) / (p - 1)
        
        return table[0][levels - 1]
    
    # ==================== COMPLEX STEP DERIVATIVE ====================
    
    @staticmethod
    def complex_step_derivative(func, x, h=1e-30):
        """
        Complex step method for highly accurate first derivatives.
        f'(x) ≈ Im(f(x + i*h)) / h
        
        This method is very accurate and doesn't suffer from cancellation errors.
        Note: Function must be able to handle complex arguments.
        
        :param func: Function (must accept complex numbers)
        :param x: Point at which to evaluate derivative
        :param h: Step size (very small)
        :return: Approximate derivative
        """
        complex_step = complex(x, h)
        return func(complex_step).imag / h
    
    # ==================== PARTIAL DERIVATIVES ====================
    
    @staticmethod
    def partial_derivative(func, point, var_index, h=1e-5):
        """
        Compute partial derivative with respect to one variable.
        
        :param func: Multivariable function
        :param point: Point (tuple/list) at which to evaluate
        :param var_index: Index of variable to differentiate with respect to
        :param h: Step size
        :return: Partial derivative
        """
        point = list(point)
        point_plus = point.copy()
        point_minus = point.copy()
        
        point_plus[var_index] += h
        point_minus[var_index] -= h
        
        return (func(*point_plus) - func(*point_minus)) / (2 * h)
    
    @staticmethod
    def gradient(func, point, h=1e-5):
        """
        Compute the gradient vector (all first partial derivatives).
        
        :param func: Multivariable function
        :param point: Point (tuple/list) at which to evaluate
        :param h: Step size
        :return: Gradient vector (list)
        """
        gradient_vec = []
        for i in range(len(point)):
            partial = NumericalDerivatives.partial_derivative(func, point, i, h)
            gradient_vec.append(partial)
        return gradient_vec
    
    # ==================== DIRECTIONAL DERIVATIVE ====================
    
    @staticmethod
    def directional_derivative(func, point, direction, h=1e-5):
        """
        Compute the directional derivative in a given direction.
        D_u f = ∇f · u, where u is a unit direction vector.
        
        :param func: Multivariable function
        :param point: Point (tuple/list) at which to evaluate
        :param direction: Direction vector (will be normalized)
        :param h: Step size
        :return: Directional derivative
        """
        # Normalize direction
        direction = list(direction)
        magnitude = sqrt(sum(d**2 for d in direction))
        unit_direction = [d / magnitude for d in direction]
        
        # Get gradient
        grad = NumericalDerivatives.gradient(func, point, h)
        
        # Compute dot product
        return sum(g * u for g, u in zip(grad, unit_direction))
    
    # ==================== HESSIAN MATRIX ====================
    
    @staticmethod
    def hessian(func, point, h=1e-5):
        """
        Compute the Hessian matrix (matrix of all second partial derivatives).
        
        :param func: Multivariable function
        :param point: Point (tuple/list) at which to evaluate
        :param h: Step size
        :return: Hessian matrix (2D list)
        """
        n = len(point)
        hessian_matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                # Mixed partial derivative
                point_pp = list(point)
                point_pm = list(point)
                point_mp = list(point)
                point_mm = list(point)
                
                point_pp[i] += h
                point_pp[j] += h
                
                point_pm[i] += h
                point_pm[j] -= h
                
                point_mp[i] -= h
                point_mp[j] += h
                
                point_mm[i] -= h
                point_mm[j] -= h
                
                second_partial = (func(*point_pp) - func(*point_pm) - 
                                 func(*point_mp) + func(*point_mm)) / (4 * h**2)
                
                hessian_matrix[i][j] = second_partial
        
        return hessian_matrix
    
    # ==================== JACOBIAN MATRIX ====================
    
    @staticmethod
    def jacobian(func_vector, point, h=1e-5):
        """
        Compute the Jacobian matrix for a vector-valued function.
        
        :param func_vector: List of functions (vector field)
        :param point: Point (tuple/list) at which to evaluate
        :param h: Step size
        :return: Jacobian matrix (2D list)
        """
        m = len(func_vector)  # Number of functions
        n = len(point)        # Number of variables
        jacobian_matrix = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            gradient = NumericalDerivatives.gradient(func_vector[i], point, h)
            jacobian_matrix[i] = gradient
        
        return jacobian_matrix
    
    # ==================== NUMERICAL DIFFERENTIATION MATRICES ====================
    
    @staticmethod
    def finite_difference_matrix_1d(n, h=1, method='central'):
        """
        Generate finite difference matrix for 1D derivative.
        
        :param n: Size of matrix (number of grid points)
        :param h: Grid spacing
        :param method: 'forward', 'backward', or 'central'
        :return: Finite difference matrix (2D list)
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        if method == 'central':
            for i in range(1, n - 1):
                matrix[i][i - 1] = -1 / (2 * h)
                matrix[i][i + 1] = 1 / (2 * h)
        elif method == 'forward':
            for i in range(n - 1):
                matrix[i][i] = -1 / h
                matrix[i][i + 1] = 1 / h
        elif method == 'backward':
            for i in range(1, n):
                matrix[i][i - 1] = -1 / h
                matrix[i][i] = 1 / h
        
        return matrix
    
    @staticmethod
    def finite_difference_matrix_2d(n, m, h=1, method='central'):
        """
        Generate finite difference matrix for 2D Laplacian.
        
        :param n: Grid points in x-direction
        :param m: Grid points in y-direction
        :param h: Grid spacing
        :param method: 'central' (most common for Laplacian)
        :return: Finite difference matrix for 2D grid
        """
        size = n * m
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                idx = i * m + j
                
                # Laplacian stencil
                matrix[idx][idx] = -4 / (h ** 2)
                matrix[idx][idx - m] = 1 / (h ** 2)  # Up
                matrix[idx][idx + m] = 1 / (h ** 2)  # Down
                matrix[idx][idx - 1] = 1 / (h ** 2)  # Left
                matrix[idx][idx + 1] = 1 / (h ** 2)  # Right
        
        return matrix
    
    # ==================== OPTIMAL STEP SIZE SELECTION ====================
    
    @staticmethod
    def optimal_step_size(func, x, derivative_order=1, epsilon=1e-16):
        """
        Estimate optimal step size using error analysis.
        Balances truncation error and rounding error.
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate
        :param derivative_order: Order of derivative
        :param epsilon: Machine precision
        :return: Recommended step size
        """
        # Estimate second derivative for optimal step size
        h_test = 1e-3
        f2 = NumericalDerivatives.second_derivative_central(func, x, h_test)
        
        if abs(f2) < 1e-10:
            f2 = 1.0
        
        # Optimal h = (6 * epsilon / |f''(x)|)^(1/3) for first derivative
        if derivative_order == 1:
            h_opt = (6 * epsilon / abs(f2)) ** (1/3)
        elif derivative_order == 2:
            h_opt = (12 * epsilon / abs(f2)) ** (1/4)
        else:
            h_opt = 1e-5
        
        return max(h_opt, 1e-15)  # Don't go below machine precision
    
    # ==================== AUTOMATIC DERIVATIVE ESTIMATION ====================
    
    @staticmethod
    def adaptive_derivative(func, x, tolerance=1e-6):
        """
        Adaptively compute derivative using Richardson extrapolation.
        Continues until desired accuracy is reached.
        
        :param func: Function to differentiate
        :param x: Point at which to evaluate
        :param tolerance: Desired accuracy
        :return: Derivative and error estimate
        """
        h = 0.1
        prev_estimate = float('inf')
        
        for iteration in range(20):
            current_estimate = NumericalDerivatives.richardson_extrapolation(
                func, x, order=1, h=h, levels=3
            )
            
            error = abs(current_estimate - prev_estimate)
            
            if error < tolerance:
                return current_estimate, error
            
            prev_estimate = current_estimate
            h /= 2
        
        return current_estimate, error

    @staticmethod
    def numerical_derivative(func, x, h=1e-5):
        """
        Calculate the numerical derivative of a function at a point using central difference method.
        
        :param func: The function to differentiate
        :param x: The point at which to calculate the derivative
        :param h: Step size for approximation
        :return: The approximate derivative
        """
        return (func(x + h) - func(x - h)) / (2 * h)
    
    @staticmethod
    def forward_difference(func, x, h=1e-5):
        """
        Calculate derivative using forward difference method.
        
        :param func: The function to differentiate
        :param x: The point at which to calculate the derivative
        :param h: Step size
        :return: The approximate derivative
        """
        return (func(x + h) - func(x)) / h
    
    @staticmethod
    def backward_difference(func, x, h=1e-5):
        """
        Calculate derivative using backward difference method.
        
        :param func: The function to differentiate
        :param x: The point at which to calculate the derivative
        :param h: Step size
        :return: The approximate derivative
        """
        return (func(x) - func(x - h)) / h
    
    @staticmethod
    def second_derivative(func, x, h=1e-5):
        """
        Calculate the second derivative of a function at a point.
        
        :param func: The function to differentiate
        :param x: The point at which to calculate the derivative
        :param h: Step size
        :return: The approximate second derivative
        """
        return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)
    
    # ==================== NUMERICAL INTEGRATION ====================
    
    @staticmethod
    def trapezoidal_rule(func, a, b, n=1000):
        """
        Approximate the integral using the trapezoidal rule.
        
        :param func: The function to integrate
        :param a: Lower bound
        :param b: Upper bound
        :param n: Number of intervals
        :return: Approximate integral value
        """
        h = (b - a) / n
        result = (func(a) + func(b)) / 2
        for i in range(1, n):
            result += func(a + i * h)
        return result * h
    
    @staticmethod
    def simpsons_rule(func, a, b, n=1000):
        """
        Approximate the integral using Simpson's rule (1/3).
        
        :param func: The function to integrate
        :param a: Lower bound
        :param b: Upper bound
        :param n: Number of intervals (must be even)
        :return: Approximate integral value
        """
        if n % 2 != 0:
            n += 1
        h = (b - a) / n
        result = func(a) + func(b)
        
        for i in range(1, n, 2):
            result += 4 * func(a + i * h)
        for i in range(2, n - 1, 2):
            result += 2 * func(a + i * h)
        
        return result * h / 3
    
    @staticmethod
    def simpsons_38_rule(func, a, b, n=1000):
        """
        Approximate the integral using Simpson's 3/8 rule.
        
        :param func: The function to integrate
        :param a: Lower bound
        :param b: Upper bound
        :param n: Number of intervals (must be divisible by 3)
        :return: Approximate integral value
        """
        if n % 3 != 0:
            n = ((n // 3) + 1) * 3
        h = (b - a) / n
        result = func(a) + func(b)
        
        for i in range(1, n, 3):
            result += 3 * func(a + i * h)
        for i in range(2, n - 1, 3):
            result += 3 * func(a + i * h)
        for i in range(3, n - 2, 3):
            result += 2 * func(a + i * h)
        
        return result * 3 * h / 8
    
    @staticmethod
    def midpoint_rule(func, a, b, n=1000):
        """
        Approximate the integral using the midpoint rule.
        
        :param func: The function to integrate
        :param a: Lower bound
        :param b: Upper bound
        :param n: Number of intervals
        :return: Approximate integral value
        """
        h = (b - a) / n
        result = 0
        for i in range(n):
            midpoint = a + (i + 0.5) * h
            result += func(midpoint)
        return result * h
