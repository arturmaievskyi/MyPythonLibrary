from math import *
from advanced_calculator import *
import numpy as np
import sys
from .analytic import Analytic

class Extrema:
    """
    Comprehensive class for finding and analyzing extrema and critical points.
    Includes methods for optimization, critical point detection, and classification.
    """
    
    # ==================== NUMERICAL DERIVATIVES (HELPER) ====================
    
    @staticmethod
    def numerical_derivative(func, x, h=1e-5):
        """Helper: Compute numerical derivative using central difference."""
        return (func(x + h) - func(x - h)) / (2 * h)
    
    @staticmethod
    def second_derivative(func, x, h=1e-5):
        """Helper: Compute second derivative numerically."""
        return (func(x + h) - 2 * func(x) + func(x - h)) / (h ** 2)
    
    @staticmethod
    def third_derivative(func, x, h=1e-5):
        """Helper: Compute third derivative numerically."""
        return (func(x + 2*h) - 2*func(x + h) + 2*func(x - h) - func(x - 2*h)) / (2 * h**3)
    
    # ==================== CRITICAL POINTS ====================
    
    @staticmethod
    def find_critical_points(func, search_range, num_divisions=1000, h=1e-5):
        """
        Find critical points where f'(x) = 0 in a given range.
        
        :param func: Function to analyze
        :param search_range: Tuple (a, b) defining search interval
        :param num_divisions: Number of points to sample
        :param h: Step size for derivative calculation
        :return: List of critical points
        """
        a, b = search_range
        critical_points = []
        step = (b - a) / num_divisions
        
        # Sample derivative at multiple points
        for i in range(num_divisions):
            x = a + i * step
            try:
                derivative = Extrema.numerical_derivative(func, x, h)
                
                # Look for sign changes in derivative
                if i > 0:
                    prev_x = a + (i - 1) * step
                    prev_derivative = Extrema.numerical_derivative(func, prev_x, h)
                    
                    # Sign change indicates critical point
                    if derivative * prev_derivative < 0:
                        # Refine using bisection
                        refined = Extrema._bisection_critical_point(func, prev_x, x, h)
                        if refined not in critical_points:
                            critical_points.append(refined)
                
                # Direct check: derivative very close to zero
                elif abs(derivative) < 1e-6:
                    if not critical_points or abs(x - critical_points[-1]) > step:
                        critical_points.append(x)
            except:
                continue
        
        return sorted(set([round(cp, 10) for cp in critical_points]))
    
    @staticmethod
    def _bisection_critical_point(func, a, b, h, tolerance=1e-8):
        """Helper: Refine critical point using bisection on derivative."""
        for _ in range(50):
            mid = (a + b) / 2
            deriv_mid = Extrema.numerical_derivative(func, mid, h)
            deriv_a = Extrema.numerical_derivative(func, a, h)
            
            if abs(deriv_mid) < tolerance:
                return mid
            
            if deriv_a * deriv_mid < 0:
                b = mid
            else:
                a = mid
            
            if abs(b - a) < tolerance:
                return mid
        
        return (a + b) / 2
    
    # ==================== FIRST DERIVATIVE TEST ====================
    
    @staticmethod
    def first_derivative_test(func, critical_point, h=1e-5, delta=0.01):
        """
        Classify critical point using first derivative test.
        Checks sign of derivative before and after critical point.
        
        :param func: Function to analyze
        :param critical_point: x-value of critical point
        :param h: Step size for derivative
        :param delta: Distance to check before/after
        :return: Classification dictionary
        """
        left_deriv = Extrema.numerical_derivative(func, critical_point - delta, h)
        right_deriv = Extrema.numerical_derivative(func, critical_point + delta, h)
        
        classification = {
            'critical_point': critical_point,
            'function_value': func(critical_point),
            'left_derivative': left_deriv,
            'right_derivative': right_deriv
        }
        
        # Classify based on sign changes
        if left_deriv > 0 and right_deriv < 0:
            classification['type'] = 'LOCAL MAXIMUM'
            classification['reason'] = 'Derivative changes from + to -'
        elif left_deriv < 0 and right_deriv > 0:
            classification['type'] = 'LOCAL MINIMUM'
            classification['reason'] = 'Derivative changes from - to +'
        elif left_deriv > 0 and right_deriv > 0:
            classification['type'] = 'NEITHER (Increasing through point)'
            classification['reason'] = 'Derivative positive on both sides'
        elif left_deriv < 0 and right_deriv < 0:
            classification['type'] = 'NEITHER (Decreasing through point)'
            classification['reason'] = 'Derivative negative on both sides'
        else:
            classification['type'] = 'INCONCLUSIVE'
            classification['reason'] = 'Derivatives near zero'
        
        return classification
    
    # ==================== SECOND DERIVATIVE TEST ====================
    
    @staticmethod
    def second_derivative_test(func, critical_point, h=1e-5):
        """
        Classify critical point using second derivative test.
        
        Test:
        - f''(c) > 0 → LOCAL MINIMUM (concave up)
        - f''(c) < 0 → LOCAL MAXIMUM (concave down)
        - f''(c) = 0 → INCONCLUSIVE (need further tests)
        
        :param func: Function to analyze
        :param critical_point: x-value of critical point
        :param h: Step size for derivative
        :return: Classification dictionary
        """
        first_deriv = Extrema.numerical_derivative(func, critical_point, h)
        second_deriv = Extrema.second_derivative(func, critical_point, h)
        
        classification = {
            'critical_point': critical_point,
            'function_value': func(critical_point),
            'first_derivative': first_deriv,
            'second_derivative': second_deriv
        }
        
        if abs(second_deriv) < 1e-8:
            classification['type'] = 'INCONCLUSIVE'
            classification['reason'] = 'Second derivative ≈ 0'
            classification['recommendation'] = 'Use first derivative test or higher-order tests'
        elif second_deriv > 0:
            classification['type'] = 'LOCAL MINIMUM'
            classification['reason'] = f'f\'\'(c) = {second_deriv:.6f} > 0'
            classification['concavity'] = 'Concave up (∪)'
        else:
            classification['type'] = 'LOCAL MAXIMUM'
            classification['reason'] = f'f\'\'(c) = {second_deriv:.6f} < 0'
            classification['concavity'] = 'Concave down (∩)'
        
        return classification
    
    # ==================== HIGHER-ORDER DERIVATIVE TEST ====================
    
    @staticmethod
    def higher_order_derivative_test(func, critical_point, h=1e-5, max_order=4):
        """
        Classify critical point using higher-order derivatives.
        Uses the first non-zero derivative to classify.
        
        If f'(c) = f''(c) = ... = f^(n-1)(c) = 0 and f^(n)(c) ≠ 0:
        - If n is even and f^(n)(c) > 0: LOCAL MINIMUM
        - If n is even and f^(n)(c) < 0: LOCAL MAXIMUM
        - If n is odd: SADDLE POINT (neither max nor min)
        
        :param func: Function to analyze
        :param critical_point: x-value of critical point
        :param h: Step size for derivatives
        :param max_order: Maximum derivative order to check
        :return: Classification dictionary
        """
        derivatives = [func(critical_point)]  # 0th derivative
        
        # Compute derivatives
        for n in range(1, max_order + 1):
            if n == 1:
                deriv = Extrema.numerical_derivative(func, critical_point, h)
            elif n == 2:
                deriv = Extrema.second_derivative(func, critical_point, h)
            elif n == 3:
                deriv = Extrema.third_derivative(func, critical_point, h)
            else:
                # Higher-order derivative
                deriv = Extrema.numerical_derivative(
                    lambda x: Extrema.third_derivative(func, x, h), critical_point, h
                )
            
            derivatives.append(deriv)
        
        # Find first non-zero derivative after f'
        first_nonzero_order = None
        for n in range(1, len(derivatives)):
            if abs(derivatives[n]) > 1e-8:
                first_nonzero_order = n
                break
        
        classification = {
            'critical_point': critical_point,
            'function_value': func(critical_point),
            'derivatives': derivatives
        }
        
        if first_nonzero_order is None:
            classification['type'] = 'INCONCLUSIVE'
            classification['reason'] = 'All derivatives near zero'
        elif first_nonzero_order == 1:
            classification['type'] = 'NOT A CRITICAL POINT'
            classification['reason'] = f'First derivative = {derivatives[1]:.6f} ≠ 0'
        else:
            derivative_value = derivatives[first_nonzero_order]
            if first_nonzero_order % 2 == 0:  # Even derivative
                if derivative_value > 0:
                    classification['type'] = 'LOCAL MINIMUM'
                else:
                    classification['type'] = 'LOCAL MAXIMUM'
                classification['reason'] = f'f^({first_nonzero_order})(c) = {derivative_value:.6f}'
            else:  # Odd derivative
                classification['type'] = 'SADDLE POINT / INFLECTION'
                classification['reason'] = f'First non-zero derivative is odd: f^({first_nonzero_order})'
        
        return classification
    
    # ==================== INFLECTION POINTS ====================
    
    @staticmethod
    def find_inflection_points(func, search_range, num_divisions=500, h=1e-5):
        """
        Find inflection points where f''(x) = 0 and concavity changes.
        
        :param func: Function to analyze
        :param search_range: Tuple (a, b)
        :param num_divisions: Number of sample points
        :param h: Step size for derivatives
        :return: List of inflection points
        """
        a, b = search_range
        inflection_points = []
        step = (b - a) / num_divisions
        
        for i in range(num_divisions):
            x = a + i * step
            try:
                second_deriv = Extrema.second_derivative(func, x, h)
                
                # Look for sign changes in second derivative
                if i > 0:
                    prev_x = a + (i - 1) * step
                    prev_second_deriv = Extrema.second_derivative(func, prev_x, h)
                    
                    # Sign change indicates inflection point
                    if second_deriv * prev_second_deriv < 0:
                        # Refine with bisection
                        refined = Extrema._bisection_inflection(func, prev_x, x, h)
                        if refined not in inflection_points:
                            inflection_points.append(refined)
            except:
                continue
        
        return sorted(set([round(ip, 10) for ip in inflection_points]))
    
    @staticmethod
    def _bisection_inflection(func, a, b, h, tolerance=1e-8):
        """Helper: Refine inflection point using bisection on second derivative."""
        for _ in range(50):
            mid = (a + b) / 2
            f2_mid = Extrema.second_derivative(func, mid, h)
            f2_a = Extrema.second_derivative(func, a, h)
            
            if abs(f2_mid) < tolerance:
                return mid
            
            if f2_a * f2_mid < 0:
                b = mid
            else:
                a = mid
            
            if abs(b - a) < tolerance:
                return mid
        
        return (a + b) / 2
    
    @staticmethod
    def classify_inflection_point(func, inflection_point, h=1e-5, delta=0.01):
        """
        Classify an inflection point based on concavity change.
        
        :param func: Function to analyze
        :param inflection_point: x-value of potential inflection point
        :param h: Step size
        :param delta: Distance to check
        :return: Classification dictionary
        """
        left_f2 = Extrema.second_derivative(func, inflection_point - delta, h)
        right_f2 = Extrema.second_derivative(func, inflection_point + delta, h)
        
        classification = {
            'inflection_point': inflection_point,
            'function_value': func(inflection_point),
            'left_second_deriv': left_f2,
            'right_second_deriv': right_f2
        }
        
        if left_f2 * right_f2 < 0:
            classification['is_inflection'] = True
            classification['type'] = 'TRUE INFLECTION POINT'
            
            if left_f2 > 0 and right_f2 < 0:
                classification['concavity_change'] = 'Concave up (∪) to Concave down (∩)'
            else:
                classification['concavity_change'] = 'Concave down (∩) to Concave up (∪)'
        else:
            classification['is_inflection'] = False
            classification['type'] = 'NOT AN INFLECTION POINT'
            classification['reason'] = 'No concavity change'
        
        return classification
    
    # ==================== GLOBAL VS LOCAL EXTREMA ====================
    
    @staticmethod
    def find_global_extrema(func, search_range, num_divisions=1000, h=1e-5):
        """
        Find global maximum and minimum on a closed interval.
        Must check critical points AND endpoints.
        
        :param func: Function to analyze
        :param search_range: Tuple (a, b)
        :param num_divisions: Number of divisions for critical point search
        :param h: Step size for derivatives
        :return: Global extrema dictionary
        """
        a, b = search_range
        
        # Find critical points
        critical_points = Extrema.find_critical_points(func, search_range, num_divisions, h)
        
        # Candidates are critical points + endpoints
        candidates = [a, b] + critical_points
        
        # Evaluate function at all candidates
        values = []
        for x in candidates:
            try:
                y = func(x)
                if not isnan(y) and not isinf(y):
                    values.append({'x': x, 'y': y})
            except:
                continue
        
        if not values:
            return {'error': 'Cannot find extrema'}
        
        # Sort by function value
        values.sort(key=lambda v: v['y'])
        
        return {
            'global_minimum': values[0],
            'global_maximum': values[-1],
            'all_candidates': values,
            'critical_points_checked': critical_points,
            'interval': search_range
        }
    
    # ==================== OPTIMIZATION ALGORITHMS ====================
    
    @staticmethod
    def gradient_descent(func, start_x, learning_rate=0.01, num_iterations=1000, 
                        tolerance=1e-6, h=1e-5):
        """
        Find local minimum using gradient descent algorithm.
        x_{n+1} = x_n - learning_rate * f'(x_n)
        
        :param func: Function to minimize
        :param start_x: Starting point
        :param learning_rate: Step size (learning rate)
        :param num_iterations: Maximum iterations
        :param tolerance: Convergence criterion
        :param h: Step size for derivative
        :return: Optimization history and result
        """
        x = start_x
        history = [{'iteration': 0, 'x': x, 'f(x)': func(x), 'gradient': 0}]
        
        for iteration in range(1, num_iterations + 1):
            gradient = Extrema.numerical_derivative(func, x, h)
            x_new = x - learning_rate * gradient
            
            history.append({
                'iteration': iteration,
                'x': x_new,
                'f(x)': func(x_new),
                'gradient': gradient
            })
            
            # Check convergence
            if abs(x_new - x) < tolerance or abs(gradient) < tolerance:
                break
            
            x = x_new
        
        return {
            'algorithm': 'Gradient Descent',
            'minimum': x,
            'function_value': func(x),
            'iterations': len(history),
            'converged': abs(gradient) < tolerance,
            'history': history[-10:]  # Last 10 iterations
        }
    
    @staticmethod
    def newton_method(func, start_x, num_iterations=100, tolerance=1e-8, h=1e-5):
        """
        Find critical point using Newton's method.
        Solves f'(x) = 0 using Newton's method for root finding.
        x_{n+1} = x_n - f'(x_n) / f''(x_n)
        
        :param func: Function whose critical point to find
        :param start_x: Starting point
        :param num_iterations: Maximum iterations
        :param tolerance: Convergence criterion
        :param h: Step size for derivatives
        :return: Result dictionary
        """
        x = start_x
        history = [{'iteration': 0, 'x': x, 'f\'(x)': 0, 'f\'\'(x)': 0}]
        
        for iteration in range(1, num_iterations + 1):
            f_prime = Extrema.numerical_derivative(func, x, h)
            f_double_prime = Extrema.second_derivative(func, x, h)
            
            if abs(f_double_prime) < 1e-15:
                return {
                    'error': 'Second derivative too close to zero',
                    'last_x': x,
                    'iterations': iteration
                }
            
            x_new = x - f_prime / f_double_prime
            
            history.append({
                'iteration': iteration,
                'x': x_new,
                'f\'(x)': f_prime,
                'f\'\'(x)': f_double_prime
            })
            
            # Check convergence
            if abs(x_new - x) < tolerance or abs(f_prime) < tolerance:
                break
            
            x = x_new
        
        return {
            'algorithm': 'Newton\'s Method',
            'critical_point': x,
            'function_value': func(x),
            'first_derivative': Extrema.numerical_derivative(func, x, h),
            'second_derivative': Extrema.second_derivative(func, x, h),
            'iterations': len(history),
            'converged': abs(Extrema.numerical_derivative(func, x, h)) < tolerance,
            'history': history[-10:]
        }
    
    @staticmethod
    def bisection_search(func, a, b, num_iterations=100, tolerance=1e-8, h=1e-5):
        """
        Find critical point using bisection on the derivative.
        
        :param func: Function to analyze
        :param a, b: Interval containing critical point
        :param num_iterations: Maximum iterations
        :param tolerance: Convergence criterion
        :param h: Step size for derivative
        :return: Result dictionary
        """
        history = []
        
        for iteration in range(num_iterations):
            mid = (a + b) / 2
            f_prime_a = Extrema.numerical_derivative(func, a, h)
            f_prime_mid = Extrema.numerical_derivative(func, mid, h)
            
            history.append({
                'iteration': iteration,
                'interval': (a, b),
                'midpoint': mid,
                'f\'(mid)': f_prime_mid
            })
            
            if abs(f_prime_mid) < tolerance or (b - a) < tolerance:
                break
            
            if f_prime_a * f_prime_mid < 0:
                b = mid
            else:
                a = mid
        
        critical_point = (a + b) / 2
        
        return {
            'algorithm': 'Bisection Search',
            'critical_point': critical_point,
            'function_value': func(critical_point),
            'first_derivative': Extrema.numerical_derivative(func, critical_point, h),
            'second_derivative': Extrema.second_derivative(func, critical_point, h),
            'iterations': len(history),
            'final_interval': (a, b),
            'history': history[-10:]
        }
    
    # ==================== MULTIVARIABLE OPTIMIZATION ====================
    
    @staticmethod
    def find_critical_points_2d(func, x_range, y_range, 
                                x_divisions=50, y_divisions=50, h=1e-5):
        """
        Find critical points of f(x, y) where ∇f = 0.
        
        :param func: Function of two variables: func(x, y)
        :param x_range: Tuple (x_min, x_max)
        :param y_range: Tuple (y_min, y_max)
        :param x_divisions: Grid divisions in x
        :param y_divisions: Grid divisions in y
        :param h: Step size for partial derivatives
        :return: List of critical points
        """
        x_min, x_max = x_range
        y_min, y_max = y_range
        x_step = (x_max - x_min) / x_divisions
        y_step = (y_max - y_min) / y_divisions
        
        critical_points = []
        
        for i in range(x_divisions):
            for j in range(y_divisions):
                x = x_min + i * x_step
                y = y_min + j * y_step
                
                try:
                    # Compute partial derivatives
                    fx = (func(x + h, y) - func(x - h, y)) / (2 * h)
                    fy = (func(x, y + h) - func(x, y - h)) / (2 * h)
                    
                    # Check if both partials near zero
                    if abs(fx) < 0.1 and abs(fy) < 0.1:
                        # Refine using Newton's method (2D)
                        refined = Extrema._refine_critical_point_2d(func, x, y, h)
                        
                        # Check if not duplicate
                        is_duplicate = False
                        for cp in critical_points:
                            if abs(cp[0] - refined[0]) < x_step and \
                               abs(cp[1] - refined[1]) < y_step:
                                is_duplicate = True
                                break
                        
                        if not is_duplicate:
                            critical_points.append(refined)
                except:
                    continue
        
        return critical_points
    
    @staticmethod
    def _refine_critical_point_2d(func, x0, y0, h, num_iter=10):
        """Helper: Refine 2D critical point using Newton's method."""
        x, y = x0, y0
        
        for _ in range(num_iter):
            # Partial derivatives
            fx = (func(x + h, y) - func(x - h, y)) / (2 * h)
            fy = (func(x, y + h) - func(x, y - h)) / (2 * h)
            
            # Second partial derivatives (Hessian)
            fxx = (func(x + h, y) - 2*func(x, y) + func(x - h, y)) / (h**2)
            fyy = (func(x, y + h) - 2*func(x, y) + func(x, y - h)) / (h**2)
            fxy = (func(x + h, y + h) - func(x + h, y - h) - 
                   func(x - h, y + h) + func(x - h, y - h)) / (4 * h**2)
            
            # Hessian determinant
            det = fxx * fyy - fxy**2
            
            if abs(det) < 1e-15:
                break
            
            # Newton update
            dx = (fy * fxy - fx * fyy) / det
            dy = (fx * fxy - fy * fxx) / det
            
            x -= dx
            y -= dy
            
            if abs(dx) < h and abs(dy) < h:
                break
        
        return (x, y)
    
    @staticmethod
    def classify_critical_point_2d(func, x, y, h=1e-5):
        """
        Classify 2D critical point using Hessian matrix.
        
        Let H = [[f_xx, f_xy], [f_xy, f_yy]] (Hessian)
        Let D = det(H) = f_xx*f_yy - f_xy²
        
        Classification:
        - D > 0 and f_xx > 0: LOCAL MINIMUM
        - D > 0 and f_xx < 0: LOCAL MAXIMUM
        - D < 0: SADDLE POINT
        - D = 0: INCONCLUSIVE
        
        :param func: Function of two variables
        :param x, y: Point to classify
        :param h: Step size for derivatives
        :return: Classification dictionary
        """
        # Partial derivatives
        fx = (func(x + h, y) - func(x - h, y)) / (2 * h)
        fy = (func(x, y + h) - func(x, y - h)) / (2 * h)
        
        # Second partial derivatives
        fxx = (func(x + h, y) - 2*func(x, y) + func(x - h, y)) / (h**2)
        fyy = (func(x, y + h) - 2*func(x, y) + func(x, y - h)) / (h**2)
        fxy = (func(x + h, y + h) - func(x + h, y - h) - 
               func(x - h, y + h) + func(x - h, y - h)) / (4 * h**2)
        
        # Hessian
        hessian = [[fxx, fxy], [fxy, fyy]]
        det_h = fxx * fyy - fxy**2
        
        classification = {
            'critical_point': (x, y),
            'function_value': func(x, y),
            'gradient': (fx, fy),
            'hessian': hessian,
            'hessian_determinant': det_h,
            'fxx': fxx,
            'fyy': fyy,
            'fxy': fxy
        }
        
        if abs(det_h) < 1e-10:
            classification['type'] = 'INCONCLUSIVE'
            classification['reason'] = 'Hessian determinant ≈ 0'
        elif det_h > 0:
            if fxx > 0:
                classification['type'] = 'LOCAL MINIMUM'
                classification['reason'] = 'D > 0 and f_xx > 0'
            else:
                classification['type'] = 'LOCAL MAXIMUM'
                classification['reason'] = 'D > 0 and f_xx < 0'
        else:
            classification['type'] = 'SADDLE POINT'
            classification['reason'] = 'D < 0'
        
        return classification
    
    # ==================== LAGRANGE MULTIPLIERS ====================
    
    @staticmethod
    def lagrange_multipliers_2var(func, constraint, x_init, y_init, 
                                  num_iterations=100, tolerance=1e-6, h=1e-5):
        """
        Find extrema of f(x,y) subject to constraint g(x,y) = 0
        Using Lagrange multipliers: ∇f = λ∇g
        
        :param func: Objective function f(x, y)
        :param constraint: Constraint function g(x, y) = 0
        :param x_init, y_init: Initial point
        :param num_iterations: Maximum iterations
        :param tolerance: Convergence criterion
        :param h: Step size for derivatives
        :return: Result dictionary
        """
        x, y, lam = x_init, y_init, 1.0  # lambda multiplier
        history = []
        
        for iteration in range(num_iterations):
            # Gradients
            fx = (func(x + h, y) - func(x - h, y)) / (2 * h)
            fy = (func(x, y + h) - func(x, y - h)) / (2 * h)
            gx = (constraint(x + h, y) - constraint(x - h, y)) / (2 * h)
            gy = (constraint(x, y + h) - constraint(x, y - h)) / (2 * h)
            
            # Lagrangian conditions: ∇f - λ∇g = 0 and g(x,y) = 0
            residual1 = fx - lam * gx
            residual2 = fy - lam * gy
            residual3 = constraint(x, y)
            
            history.append({
                'iteration': iteration,
                'x': x,
                'y': y,
                'lambda': lam,
                'constraint_value': residual3
            })
            
            # Check convergence
            if abs(residual1) < tolerance and abs(residual2) < tolerance and \
               abs(residual3) < tolerance:
                break
            
            # Update using gradient of Lagrangian
            x -= 0.01 * residual1
            y -= 0.01 * residual2
            lam -= 0.01 * residual3
        
        return {
            'algorithm': 'Lagrange Multipliers',
            'optimal_point': (x, y),
            'function_value': func(x, y),
            'constraint_value': constraint(x, y),
            'lagrange_multiplier': lam,
            'iterations': len(history),
            'converged': abs(constraint(x, y)) < tolerance,
            'history': history[-10:]
        }
    
    # ==================== BOUNDARY ANALYSIS ====================
    
    @staticmethod
    def analyze_boundary(func, search_range, num_points=100, h=1e-5):
        """
        Analyze function behavior at boundaries of interval.
        
        :param func: Function to analyze
        :param search_range: Tuple (a, b)
        :param num_points: Number of boundary points
        :param h: Step size
        :return: Boundary analysis dictionary
        """
        a, b = search_range
        
        # Sample points near boundaries
        boundary_points = []
        for delta in [1e-3, 1e-4, 1e-5]:
            try:
                boundary_points.append({
                    'location': 'left boundary',
                    'x': a + delta,
                    'f(x)': func(a + delta),
                    'f\'(x)': Extrema.numerical_derivative(func, a + delta, h)
                })
                boundary_points.append({
                    'location': 'right boundary',
                    'x': b - delta,
                    'f(x)': func(b - delta),
                    'f\'(x)': Extrema.numerical_derivative(func, b - delta, h)
                })
            except:
                continue
        
        return {
            'interval': search_range,
            'boundary_analysis': boundary_points,
            'endpoint_values': {
                'f(a)': func(a) if not isnan(func(a)) else 'undefined',
                'f(b)': func(b) if not isnan(func(b)) else 'undefined'
            }
        }
    
    # ==================== COMPREHENSIVE EXTREMA ANALYSIS ====================
    
    @staticmethod
    def complete_extrema_analysis(func, search_range, num_divisions=500, h=1e-5):
        """
        Perform comprehensive analysis of all critical points and extrema.
        
        :param func: Function to analyze
        :param search_range: Tuple (a, b)
        :param num_divisions: Number of sample points
        :param h: Step size for derivatives
        :return: Complete analysis dictionary
        """
        a, b = search_range
        
        analysis = {
            'interval': search_range,
            'critical_points': [],
            'inflection_points': [],
            'global_extrema': None,
            'boundary': None
        }
        
        # Find critical points
        critical_points = Extrema.find_critical_points(func, search_range, num_divisions, h)
        analysis['critical_points'] = []
        
        for cp in critical_points:
            cp_analysis = {
                'point': cp,
                'function_value': func(cp),
                'first_derivative_test': Extrema.first_derivative_test(func, cp, h),
                'second_derivative_test': Extrema.second_derivative_test(func, cp, h)
            }
            analysis['critical_points'].append(cp_analysis)
        
        # Find inflection points
        inflection_points = Extrema.find_inflection_points(func, search_range, num_divisions, h)
        analysis['inflection_points'] = []
        
        for ip in inflection_points:
            ip_analysis = Extrema.classify_inflection_point(func, ip, h)
            analysis['inflection_points'].append(ip_analysis)
        
        # Global extrema
        analysis['global_extrema'] = Extrema.find_global_extrema(func, search_range, 
                                                                 num_divisions, h)
        
        # Boundary analysis
        analysis['boundary'] = Extrema.analyze_boundary(func, search_range, num_divisions, h)
        
        return analysis

    @staticmethod
    def find_critical_points(func, a, b, step=0.01, derivative_h=1e-5):
        """
        Find approximate critical points (where derivative = 0).
        
        :param func: The function
        :param a: Lower bound
        :param b: Upper bound
        :param step: Step size for scanning
        :param derivative_h: Step size for derivative calculation
        :return: List of critical points
        """
        critical_points = []
        x = a
        
        while x < b:
            derivative = Analytic.numerical_derivative(func, x, derivative_h)
            if abs(derivative) < 0.1:  # Near zero
                critical_points.append(x)
                x += step * 10  # Skip ahead to avoid duplicates
            else:
                x += step
        
        return critical_points
    
    @staticmethod
    def local_extrema(func, critical_point, h=1e-5):
        """
        Determine if a critical point is a local maximum or minimum.
        
        :param func: The function
        :param critical_point: The critical point to test
        :param h: Step size
        :return: 'maximum', 'minimum', or 'saddle'
        """
        second_deriv = Analytic.second_derivative(func, critical_point, h)
        
        if second_deriv > 0:
            return 'minimum'
        elif second_deriv < 0:
            return 'maximum'
        else:
            return 'saddle'
    
    # ==================== CONTINUITY ====================
    
    @staticmethod
    def is_continuous(func, x_val, tolerance=1e-5):
        """
        Check if a function appears to be continuous at a point.
        
        :param func: The function
        :param x_val: The point to test
        :param tolerance: Tolerance for convergence
        :return: True if likely continuous
        """
        try:
            left_limit = func(x_val - tolerance)
            right_limit = func(x_val + tolerance)
            func_value = func(x_val)
            
            return (abs(left_limit - func_value) < tolerance and 
                    abs(right_limit - func_value) < tolerance)
        except:
            return False
