from math import *
from advanced_calculator import *
import numpy as np
import sys


class Limits:
    """
    Comprehensive class for computing and analyzing limits in calculus.
    Includes methods for finite limits, infinite limits, and indeterminate forms.
    """
    
    # ==================== BASIC LIMIT COMPUTATION ====================
    
    @staticmethod
    def limit_from_right(func, x_val, epsilon=1e-8, num_points=10):
        """
        Compute limit from the right: lim f(x) as x → x_val⁺
        
        :param func: Function to evaluate
        :param x_val: Point approaching from right
        :param epsilon: Distance from point (must be small)
        :param num_points: Number of points to sample
        :return: Approximate limit value
        """
        values = []
        for i in range(1, num_points + 1):
            delta = epsilon / (2 ** i)
            try:
                value = func(x_val + delta)
                if not isnan(value) and not isinf(value):
                    values.append(value)
            except:
                continue
        
        if not values:
            raise ValueError("Cannot compute limit from right")
        
        return sum(values) / len(values)
    
    @staticmethod
    def limit_from_left(func, x_val, epsilon=1e-8, num_points=10):
        """
        Compute limit from the left: lim f(x) as x → x_val⁻
        
        :param func: Function to evaluate
        :param x_val: Point approaching from left
        :param epsilon: Distance from point (must be small)
        :param num_points: Number of points to sample
        :return: Approximate limit value
        """
        values = []
        for i in range(1, num_points + 1):
            delta = epsilon / (2 ** i)
            try:
                value = func(x_val - delta)
                if not isnan(value) and not isinf(value):
                    values.append(value)
            except:
                continue
        
        if not values:
            raise ValueError("Cannot compute limit from left")
        
        return sum(values) / len(values)
    
    @staticmethod
    def limit_two_sided(func, x_val, epsilon=1e-8, num_points=10):
        """
        Compute two-sided limit: lim f(x) as x → x_val
        Verifies that left and right limits agree.
        
        :param func: Function to evaluate
        :param x_val: Point at which limit is taken
        :param epsilon: Distance from point
        :param num_points: Number of points to sample
        :return: Limit value if it exists
        :raises ValueError: If left and right limits don't match
        """
        left_limit = Limits.limit_from_left(func, x_val, epsilon, num_points)
        right_limit = Limits.limit_from_right(func, x_val, epsilon, num_points)
        
        # Check if limits agree within tolerance
        if abs(left_limit - right_limit) < 1e-5:
            return (left_limit + right_limit) / 2
        else:
            raise ValueError(
                f"Limit does not exist. Left: {left_limit}, Right: {right_limit}"
            )
    
    # ==================== LIMITS AT INFINITY ====================
    
    @staticmethod
    def limit_at_infinity(func, direction='positive', num_points=10):
        """
        Compute limit as x → ±∞
        
        :param func: Function to evaluate
        :param direction: 'positive' for x→+∞, 'negative' for x→-∞
        :param num_points: Number of points to evaluate
        :return: Approximate limit
        """
        values = []
        
        for i in range(1, num_points + 1):
            if direction == 'positive':
                x = 10 ** i
            else:  # negative
                x = -(10 ** i)
            
            try:
                value = func(x)
                if not isnan(value) and not isinf(value):
                    values.append(value)
            except:
                continue
        
        if not values:
            raise ValueError("Cannot compute limit at infinity")
        
        return sum(values) / len(values)
    
    @staticmethod
    def limit_to_positive_infinity(func, num_points=10):
        """Compute lim f(x) as x → +∞"""
        return Limits.limit_at_infinity(func, direction='positive', num_points=num_points)
    
    @staticmethod
    def limit_to_negative_infinity(func, num_points=10):
        """Compute lim f(x) as x → -∞"""
        return Limits.limit_at_infinity(func, direction='negative', num_points=num_points)
    
    # ==================== SEQUENCE LIMITS ====================
    
    @staticmethod
    def sequence_limit(sequence, tolerance=1e-10, max_iterations=1000):
        """
        Determine if sequence converges and find its limit.
        
        :param sequence: List of sequence terms or generator
        :param tolerance: Convergence criterion
        :param max_iterations: Maximum terms to check
        :return: Limit value and convergence info
        """
        if not isinstance(sequence, list):
            sequence = list(sequence)
        
        if len(sequence) == 0:
            raise ValueError("Empty sequence")
        
        # Check last differences
        for i in range(max(1, len(sequence) - max_iterations), len(sequence)):
            if i > 0:
                diff = abs(sequence[i] - sequence[i-1])
                if diff < tolerance:
                    return {
                        'converged': True,
                        'limit': sequence[-1],
                        'convergence_rate': diff,
                        'num_terms': len(sequence)
                    }
        
        return {
            'converged': False,
            'last_value': sequence[-1],
            'num_terms': len(sequence)
        }
    
    @staticmethod
    def sequence_convergence_analysis(sequence, num_terms_analyze=10):
        """
        Detailed analysis of sequence convergence behavior.
        
        :param sequence: List of sequence terms
        :param num_terms_analyze: Last n terms to analyze
        :return: Dictionary with convergence metrics
        """
        if len(sequence) < 2:
            raise ValueError("Need at least 2 terms")
        
        last_terms = sequence[-num_terms_analyze:]
        differences = [abs(last_terms[i+1] - last_terms[i]) 
                      for i in range(len(last_terms)-1)]
        
        if len(differences) > 1:
            ratios = [differences[i+1] / (differences[i] + 1e-15) 
                     for i in range(len(differences)-1)]
        else:
            ratios = []
        
        return {
            'last_term': sequence[-1],
            'differences': differences,
            'difference_trend': 'decreasing' if all(differences[i] >= differences[i+1] 
                                                   for i in range(len(differences)-1)) else 'irregular',
            'convergence_ratios': ratios,
            'linear_convergence': all(0 < r < 1 for r in ratios) if ratios else False,
            'quadratic_convergence': all(r < 0.5 for r in ratios) if ratios else False
        }
    
    # ==================== SERIES CONVERGENCE ====================
    
    @staticmethod
    def series_partial_sums(terms, num_terms=None):
        """
        Compute partial sums of a series to analyze convergence.
        
        :param terms: List of series terms or generator
        :param num_terms: Number of terms to sum (None = all)
        :return: List of partial sums
        """
        partial_sums = []
        current_sum = 0
        
        count = 0
        for term in terms:
            current_sum += term
            partial_sums.append(current_sum)
            count += 1
            if num_terms and count >= num_terms:
                break
        
        return partial_sums
    
    @staticmethod
    def series_limit(terms, num_terms=1000, tolerance=1e-10):
        """
        Compute limit of a series (sum of infinite series).
        
        :param terms: Generator or list of series terms
        :param num_terms: Maximum terms to use
        :param tolerance: Convergence criterion
        :return: Series sum (limit) and convergence info
        """
        partial_sums = Limits.series_partial_sums(terms, num_terms)
        
        # Check for convergence
        converged = False
        for i in range(1, len(partial_sums)):
            if abs(partial_sums[i] - partial_sums[i-1]) < tolerance:
                converged = True
                break
        
        return {
            'sum': partial_sums[-1],
            'converged': converged,
            'num_terms_used': len(partial_sums),
            'final_term_change': abs(partial_sums[-1] - partial_sums[-2]) if len(partial_sums) > 1 else 0
        }
    
    # ==================== INDETERMINATE FORMS ====================
    
    @staticmethod
    def is_indeterminate_form(func, x_val, epsilon=1e-8):
        """
        Detect if function exhibits indeterminate form at point.
        
        :param func: Function to test
        :param x_val: Point to test
        :param epsilon: Tolerance
        :return: Type of indeterminate form or None
        """
        try:
            left = Limits.limit_from_left(func, x_val, epsilon)
            right = Limits.limit_from_right(func, x_val, epsilon)
            
            # Check for 0/0
            if abs(left) < epsilon and abs(right) < epsilon:
                return "0/0"
            
            # Check for ∞/∞
            if abs(left) > 1e10 and abs(right) > 1e10:
                return "∞/∞"
            
            # Check for 0·∞
            if (abs(left) < epsilon and abs(right) > 1e10) or \
               (abs(left) > 1e10 and abs(right) < epsilon):
                return "0·∞"
            
            return None
        except:
            return None
    
    # ==================== LHÔPITAL'S RULE ====================
    
    @staticmethod
    def lhopital_rule(func, x_val, numerator_deriv, denominator_deriv, h=1e-5):
        """
        Apply L'Hôpital's rule to resolve indeterminate form 0/0 or ∞/∞.
        lim f(x)/g(x) = lim f'(x)/g'(x) as x → x_val
        
        :param func: Original function (ratio)
        :param x_val: Point of indeterminate form
        :param numerator_deriv: Derivative of numerator
        :param denominator_deriv: Derivative of denominator
        :param h: Step size for numerical derivative
        :return: Limit after applying L'Hôpital's rule
        """
        # Evaluate derivatives at x_val
        num_deriv_val = numerator_deriv(x_val)
        denom_deriv_val = denominator_deriv(x_val)
        
        if abs(denom_deriv_val) < 1e-15:
            raise ValueError("Denominator derivative is zero, cannot apply L'Hôpital's rule")
        
        return num_deriv_val / denom_deriv_val
    
    # ==================== SQUEEZE THEOREM ====================
    
    @staticmethod
    def squeeze_theorem(func_lower, func_middle, func_upper, x_val, epsilon=1e-8):
        """
        Apply squeeze theorem: if f(x) ≤ g(x) ≤ h(x) and lim f = lim h = L,
        then lim g = L
        
        :param func_lower: Lower bound function
        :param func_middle: Middle function
        :param func_upper: Upper bound function
        :param x_val: Point at which limits are taken
        :param epsilon: Tolerance
        :return: Limit of middle function
        """
        lower_limit = Limits.limit_two_sided(func_lower, x_val, epsilon)
        upper_limit = Limits.limit_two_sided(func_upper, x_val, epsilon)
        
        if abs(lower_limit - upper_limit) > 1e-5:
            raise ValueError("Lower and upper bounds don't converge to same limit")
        
        middle_limit = Limits.limit_two_sided(func_middle, x_val, epsilon)
        
        # Verify squeeze condition holds approximately
        test_point = x_val + epsilon
        if func_lower(test_point) > func_middle(test_point) or \
           func_middle(test_point) > func_upper(test_point):
            raise ValueError("Squeeze condition not satisfied: f(x) ≤ g(x) ≤ h(x)")
        
        return middle_limit
    
    # ==================== LIMIT THEOREMS ====================
    
    @staticmethod
    def limit_of_sum(func1, func2, x_val, epsilon=1e-8):
        """
        Limit of sum: lim [f(x) + g(x)] = lim f(x) + lim g(x)
        
        :param func1: First function
        :param func2: Second function
        :param x_val: Point at which limit is taken
        :param epsilon: Tolerance
        :return: Limit of sum
        """
        limit1 = Limits.limit_two_sided(func1, x_val, epsilon)
        limit2 = Limits.limit_two_sided(func2, x_val, epsilon)
        return limit1 + limit2
    
    @staticmethod
    def limit_of_product(func1, func2, x_val, epsilon=1e-8):
        """
        Limit of product: lim [f(x)·g(x)] = lim f(x) · lim g(x)
        
        :param func1: First function
        :param func2: Second function
        :param x_val: Point at which limit is taken
        :param epsilon: Tolerance
        :return: Limit of product
        """
        limit1 = Limits.limit_two_sided(func1, x_val, epsilon)
        limit2 = Limits.limit_two_sided(func2, x_val, epsilon)
        return limit1 * limit2
    
    @staticmethod
    def limit_of_quotient(func1, func2, x_val, epsilon=1e-8):
        """
        Limit of quotient: lim [f(x)/g(x)] = lim f(x) / lim g(x)
        (if lim g(x) ≠ 0)
        
        :param func1: Numerator function
        :param func2: Denominator function
        :param x_val: Point at which limit is taken
        :param epsilon: Tolerance
        :return: Limit of quotient
        """
        limit1 = Limits.limit_two_sided(func1, x_val, epsilon)
        limit2 = Limits.limit_two_sided(func2, x_val, epsilon)
        
        if abs(limit2) < 1e-15:
            raise ValueError("Denominator limit is zero, quotient rule doesn't apply")
        
        return limit1 / limit2
    
    @staticmethod
    def limit_of_power(func, x_val, exponent, epsilon=1e-8):
        """
        Limit of power: lim [f(x)^n] = [lim f(x)]^n
        
        :param func: Base function
        :param x_val: Point at which limit is taken
        :param exponent: Power/exponent
        :param epsilon: Tolerance
        :return: Limit of power
        """
        base_limit = Limits.limit_two_sided(func, x_val, epsilon)
        return base_limit ** exponent
    
    @staticmethod
    def limit_of_composition(outer_func, inner_func, x_val, epsilon=1e-8):
        """
        Limit of composition: lim f(g(x)) = f(lim g(x)) (if f is continuous)
        
        :param outer_func: Outer function f
        :param inner_func: Inner function g
        :param x_val: Point at which limit is taken
        :param epsilon: Tolerance
        :return: Limit of composition
        """
        inner_limit = Limits.limit_two_sided(inner_func, x_val, epsilon)
        try:
            return outer_func(inner_limit)
        except:
            raise ValueError("Cannot evaluate outer function at inner limit")
    
    # ==================== ASYMPTOTIC BEHAVIOR ====================
    
    @staticmethod
    def horizontal_asymptote(func, tolerance=1e-6, num_points=20):
        """
        Find horizontal asymptotes: values that function approaches at ±∞
        
        :param func: Function to analyze
        :param tolerance: Convergence criterion
        :param num_points: Number of points to evaluate
        :return: Dictionary with asymptote information
        """
        asymptotes = {}
        
        # Check positive infinity
        try:
            positive_limit = Limits.limit_to_positive_infinity(func, num_points)
            asymptotes['positive_infinity'] = positive_limit
        except:
            asymptotes['positive_infinity'] = None
        
        # Check negative infinity
        try:
            negative_limit = Limits.limit_to_negative_infinity(func, num_points)
            asymptotes['negative_infinity'] = negative_limit
        except:
            asymptotes['negative_infinity'] = None
        
        return asymptotes
    
    @staticmethod
    def vertical_asymptote_search(func, search_range, num_divisions=100):
        """
        Search for vertical asymptotes in a range.
        
        :param func: Function to analyze
        :param search_range: Tuple (a, b) for search interval
        :param num_divisions: Number of points to check
        :return: List of suspected asymptote locations
        """
        a, b = search_range
        asymptotes = []
        step = (b - a) / num_divisions
        
        for i in range(num_divisions):
            x = a + i * step
            try:
                # Try to evaluate function
                left_val = func(x - 1e-6)
                right_val = func(x + 1e-6)
                
                # Check if values explode
                if abs(left_val) > 1e10 or abs(right_val) > 1e10:
                    asymptotes.append(x)
            except:
                # Function likely undefined at this point
                asymptotes.append(x)
        
        return asymptotes
    
    @staticmethod
    def oblique_asymptote(func, x_range, tolerance=0.01):
        """
        Find oblique (slant) asymptote y = mx + b
        
        :param func: Rational function
        :param x_range: Tuple (x_min, x_max) for large x values
        :param tolerance: Allowed deviation from asymptote
        :return: (slope, intercept) or None
        """
        x_min, x_max = x_range
        
        # Sample points at large x values
        large_x_values = [x_min * 10**i for i in range(1, 4)]
        
        # Estimate slope by finite differences at large x
        x1 = large_x_values[0]
        x2 = large_x_values[1]
        
        try:
            slope = (func(x2) - func(x1)) / (x2 - x1)
            intercept = func(x1) - slope * x1
            
            return {'slope': slope, 'intercept': intercept}
        except:
            return None
    
    # ==================== CONTINUITY ANALYSIS ====================
    
    @staticmethod
    def is_continuous_at(func, x_val, epsilon=1e-8, tolerance=1e-5):
        """
        Check if function is continuous at a point.
        Requires: lim f(x) = f(x_val) as x → x_val
        
        :param func: Function to test
        :param x_val: Point to test continuity
        :param epsilon: Tolerance for limit calculation
        :param tolerance: Acceptable difference between limit and function value
        :return: True if continuous, False otherwise
        """
        try:
            func_value = func(x_val)
        except:
            return False
        
        try:
            limit_value = Limits.limit_two_sided(func, x_val, epsilon)
        except:
            return False
        
        return abs(limit_value - func_value) < tolerance
    
    @staticmethod
    def find_discontinuities(func, search_range, num_points=100):
        """
        Search for points of discontinuity in a range.
        
        :param func: Function to analyze
        :param search_range: Tuple (a, b) for search interval
        :param num_points: Number of points to check
        :return: List of suspected discontinuity locations
        """
        a, b = search_range
        discontinuities = []
        step = (b - a) / num_points
        
        for i in range(num_points):
            x = a + i * step
            if not Limits.is_continuous_at(func, x):
                discontinuities.append(x)
        
        return discontinuities
    
    @staticmethod
    def removable_discontinuity(func, x_val, epsilon=1e-8):
        """
        Check if discontinuity at x_val is removable.
        Discontinuity is removable if lim f(x) exists but ≠ f(x_val)
        
        :param func: Function to analyze
        :param x_val: Point of discontinuity
        :param epsilon: Tolerance
        :return: True if removable, False otherwise
        """
        try:
            limit_val = Limits.limit_two_sided(func, x_val, epsilon)
            func_val = func(x_val)
            
            # Removable if limit exists but differs from function value
            return not isnan(limit_val) and not isinf(limit_val) and \
                   abs(limit_val - func_val) > 1e-5
        except:
            return False
    
    
    # ==================== RATE OF CONVERGENCE ====================
    
    @staticmethod
    def convergence_rate(sequence):
        """
        Analyze convergence rate of sequence.
        Returns order of convergence (linear, quadratic, etc.)
        
        :param sequence: List of sequence terms
        :return: Convergence rate analysis
        """
        if len(sequence) < 5:
            raise ValueError("Need at least 5 terms")
        
        # Get last several terms
        tail = sequence[-5:]
        limit = tail[-1]  # Approximate limit as last term
        
        # Compute errors: e_n = |a_n - L|
        errors = [abs(tail[i] - limit) for i in range(len(tail))]
        
        # Compute ratios: e_{n+1} / e_n
        ratios = []
        for i in range(len(errors) - 1):
            if errors[i] > 1e-15:
                ratio = errors[i + 1] / errors[i]
                ratios.append(ratio)
        
        if not ratios:
            return {'type': 'unknown', 'ratios': []}
        
        avg_ratio = sum(ratios) / len(ratios)
        
        if avg_ratio > 0.9:
            return {'type': 'sublinear', 'rate': avg_ratio}
        elif avg_ratio > 0.1 and avg_ratio <= 0.9:
            return {'type': 'linear', 'rate': avg_ratio}
        elif avg_ratio > 0.01 and avg_ratio <= 0.1:
            return {'type': 'superlinear', 'rate': avg_ratio}
        elif avg_ratio <= 0.01:
            return {'type': 'quadratic_or_higher', 'rate': avg_ratio}
        
        return {'type': 'unknown', 'rate': avg_ratio, 'ratios': ratios}
    
    # ==================== SANDWICH/SQUEEZE MULTIPLE FUNCTIONS ====================
    
    @staticmethod
    def generalized_squeeze(functions, x_val, epsilon=1e-8):
        """
        Generalized squeeze theorem for multiple bounding functions.
        
        :param functions: List of functions [lower1, lower2, ..., target, ..., upper1, upper2]
        :param x_val: Point at which limits are taken
        :param epsilon: Tolerance
        :return: Limit if functions are properly ordered
        """
        limits = []
        for func in functions:
            try:
                lim = Limits.limit_two_sided(func, x_val, epsilon)
                limits.append(lim)
            except:
                return None
        
        # Check if all limits are the same
        if all(abs(lim - limits[0]) < 1e-5 for lim in limits):
            return limits[0]
        else:
            return None
    
    # ==================== UTILITY FUNCTIONS ====================
    
    @staticmethod
    def limit_summary(func, x_val, epsilon=1e-8):
        """
        Comprehensive limit analysis at a point.
        
        :param func: Function to analyze
        :param x_val: Point of interest
        :param epsilon: Tolerance
        :return: Dictionary with complete limit information
        """
        summary = {
            'point': x_val,
            'function_value': None,
            'left_limit': None,
            'right_limit': None,
            'two_sided_limit': None,
            'is_continuous': False,
            'discontinuity_type': None
        }
        
        # Get function value
        try:
            summary['function_value'] = func(x_val)
        except:
            summary['discontinuity_type'] = 'undefined'
        
        # Get limits
        try:
            summary['left_limit'] = Limits.limit_from_left(func, x_val, epsilon)
        except:
            pass
        
        try:
            summary['right_limit'] = Limits.limit_from_right(func, x_val, epsilon)
        except:
            pass
        
        try:
            summary['two_sided_limit'] = Limits.limit_two_sided(func, x_val, epsilon)
        except:
            pass
        
        # Check continuity
        summary['is_continuous'] = Limits.is_continuous_at(func, x_val, epsilon)
        
        # Determine discontinuity type
        if not summary['is_continuous']:
            if summary['left_limit'] is not None and summary['right_limit'] is not None:
                if abs(summary['left_limit'] - summary['right_limit']) < 1e-5:
                    summary['discontinuity_type'] = 'removable'
                else:
                    summary['discontinuity_type'] = 'jump'
            else:
                summary['discontinuity_type'] = 'essential'
        
        return summary
     
    @staticmethod
    def limit(func, x_val, direction='both', epsilon=1e-7):
        """
        Calculate the limit of a function at a point.
        
        :param func: The function
        :param x_val: The point at which to calculate the limit
        :param direction: 'left', 'right', or 'both'
        :param epsilon: Tolerance for calculation
        :return: The approximate limit value
        """
        if direction == 'left':
            return func(x_val - epsilon)
        elif direction == 'right':
            return func(x_val + epsilon)
        elif direction == 'both':
            left_limit = func(x_val - epsilon)
            right_limit = func(x_val + epsilon)
            if abs(left_limit - right_limit) < 1e-5:
                return (left_limit + right_limit) / 2
            else:
                raise ValueError("Left and right limits do not converge.")
        else:
            raise ValueError("Direction must be 'left', 'right', or 'both'.")
    
    # ==================== SEQUENCES ====================
    
    @staticmethod
    def arithmetic_sequence(a1, d, n):
        """
        Generate an arithmetic sequence.
        
        :param a1: First term
        :param d: Common difference
        :param n: Number of terms
        :return: List of terms
        """
        return [a1 + i * d for i in range(n)]
    
    @staticmethod
    def geometric_sequence(a1, r, n):
        """
        Generate a geometric sequence.
        
        :param a1: First term
        :param r: Common ratio
        :param n: Number of terms
        :return: List of terms
        """
        return [a1 * (r ** i) for i in range(n)]
    
    @staticmethod
    def arithmetic_sum(a1, d, n):
        """Calculate the sum of an arithmetic sequence."""
        return n * (2 * a1 + (n - 1) * d) / 2
    
    @staticmethod
    def geometric_sum(a1, r, n):
        """Calculate the sum of a geometric sequence."""
        if r == 1:
            return a1 * n
        return a1 * (1 - r ** n) / (1 - r)
    
    @staticmethod
    def infinite_geometric_sum(a1, r):
        """
        Calculate the sum of an infinite geometric series.
        
        :param a1: First term
        :param r: Common ratio (must be |r| < 1)
        :return: Sum of the series
        """
        if abs(r) >= 1:
            raise ValueError("Common ratio must satisfy |r| < 1 for convergence.")
        return a1 / (1 - r)

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

class Series:
    """
    Comprehensive class for series analysis in calculus.
    Includes convergence tests, special series, and series computations.
    """
    
    # ==================== SERIES REPRESENTATIONS ====================
    
    @staticmethod
    def arithmetic_series_sum(first_term, common_diff, num_terms):
        """
        Sum of arithmetic series: a + (a+d) + (a+2d) + ... + (a+(n-1)d)
        Formula: S_n = n/2 * (2a + (n-1)d) = n/2 * (first + last)
        
        :param first_term: First term (a)
        :param common_diff: Common difference (d)
        :param num_terms: Number of terms (n)
        :return: Sum of series
        """
        return num_terms * (2 * first_term + (num_terms - 1) * common_diff) / 2
    
    @staticmethod
    def geometric_series_sum(first_term, common_ratio, num_terms):
        """
        Sum of geometric series: a + ar + ar² + ... + ar^(n-1)
        Formula: S_n = a(1 - r^n) / (1 - r) if r ≠ 1, else S_n = na
        
        :param first_term: First term (a)
        :param common_ratio: Common ratio (r)
        :param num_terms: Number of terms (n)
        :return: Sum of series
        """
        if abs(common_ratio - 1) < 1e-15:
            return first_term * num_terms
        return first_term * (1 - common_ratio ** num_terms) / (1 - common_ratio)
    
    @staticmethod
    def infinite_geometric_series(first_term, common_ratio):
        """
        Sum of infinite geometric series: a + ar + ar² + ...
        Formula: S = a / (1 - r) if |r| < 1
        
        :param first_term: First term (a)
        :param common_ratio: Common ratio (r), must satisfy |r| < 1
        :return: Infinite sum
        :raises ValueError: If |r| >= 1 (series diverges)
        """
        if abs(common_ratio) >= 1:
            raise ValueError(f"Series diverges: |r| = {abs(common_ratio)} >= 1")
        return first_term / (1 - common_ratio)
    
    @staticmethod
    def harmonic_series_partial_sum(num_terms):
        """
        Sum of harmonic series: 1 + 1/2 + 1/3 + ... + 1/n
        Note: Infinite harmonic series diverges
        
        :param num_terms: Number of terms to sum
        :return: Approximate harmonic series sum
        """
        return sum(1/i for i in range(1, num_terms + 1))
    
    @staticmethod
    def p_series_convergence(p):
        """
        Determine convergence of p-series: Σ(1/n^p)
        Converges if p > 1, diverges if p ≤ 1
        
        :param p: Exponent value
        :return: 'converges' or 'diverges'
        """
        if p > 1:
            return 'converges'
        else:
            return 'diverges'
    
    @staticmethod
    def telescoping_series_sum(terms, num_terms=None):
        """
        Sum telescoping series where consecutive terms cancel.
        Example: Σ(1/(n(n+1))) = Σ(1/n - 1/(n+1))
        
        :param terms: List or generator of series terms
        :param num_terms: Number of terms to include
        :return: Partial sum (shows cancellation)
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        if num_terms:
            terms = terms[:num_terms]
        
        partial_sum = sum(terms)
        return partial_sum
    
    # ==================== CONVERGENCE TESTS ====================
    
    @staticmethod
    def nth_term_test(terms, num_check=100, tolerance=1e-10):
        """
        Divergence Test (nth Term Test for Divergence):
        If lim a_n ≠ 0, then series diverges.
        
        :param terms: List or generator of series terms
        :param num_check: Number of terms to check
        :param tolerance: Tolerance for checking if limit is zero
        :return: 'diverges', 'possibly_converges', or 'inconclusive'
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        terms_to_check = terms[-num_check:] if len(terms) > num_check else terms
        
        # Check if terms approach zero
        if abs(terms_to_check[-1]) > tolerance:
            return 'diverges'
        
        # Check if terms are consistently approaching zero
        last_few = terms_to_check[-5:] if len(terms_to_check) >= 5 else terms_to_check
        if all(abs(t) < tolerance for t in last_few):
            return 'possibly_converges'
        
        return 'inconclusive'
    
    @staticmethod
    def ratio_test(terms, num_check=None):
        """
        Ratio Test: Compute L = lim |a_{n+1} / a_n|
        - If L < 1: series converges absolutely
        - If L > 1: series diverges
        - If L = 1: inconclusive
        
        :param terms: List of series terms
        :param num_check: Number of ratios to examine
        :return: Dictionary with L value and conclusion
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        if len(terms) < 2:
            raise ValueError("Need at least 2 terms")
        
        # Compute ratios |a_{n+1} / a_n|
        ratios = []
        for i in range(len(terms) - 1):
            if abs(terms[i]) > 1e-15:
                ratio = abs(terms[i + 1] / terms[i])
                ratios.append(ratio)
        
        if not ratios:
            return {'L': None, 'conclusion': 'inconclusive'}
        
        # Use last few ratios to estimate L
        last_ratios = ratios[-min(num_check or 10, len(ratios)):]
        L = sum(last_ratios) / len(last_ratios)
        
        if L < 1:
            conclusion = 'converges_absolutely'
        elif L > 1:
            conclusion = 'diverges'
        else:
            conclusion = 'inconclusive'
        
        return {
            'L': L,
            'ratios': ratios,
            'conclusion': conclusion
        }
    
    @staticmethod
    def root_test(terms, num_check=None):
        """
        Root Test: Compute L = lim |a_n|^(1/n)
        - If L < 1: series converges absolutely
        - If L > 1: series diverges
        - If L = 1: inconclusive
        
        :param terms: List of series terms
        :param num_check: Number of terms to examine
        :return: Dictionary with L value and conclusion
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        # Compute nth roots
        roots = []
        for i, term in enumerate(terms):
            if i > 0:  # Start from index 1
                nth_root = abs(term) ** (1 / (i + 1))
                roots.append(nth_root)
        
        if not roots:
            return {'L': None, 'conclusion': 'inconclusive'}
        
        # Use last few roots to estimate L
        last_roots = roots[-min(num_check or 10, len(roots)):]
        L = sum(last_roots) / len(last_roots)
        
        if L < 1:
            conclusion = 'converges_absolutely'
        elif L > 1:
            conclusion = 'diverges'
        else:
            conclusion = 'inconclusive'
        
        return {
            'L': L,
            'roots': roots,
            'conclusion': conclusion
        }
    
    @staticmethod
    def integral_test(func, start=1, end=1000, num_steps=1000):
        """
        Integral Test: If f is positive, continuous, decreasing:
        Σ f(n) converges ⟺ ∫f(x)dx converges
        
        Uses numerical integration (trapezoidal rule)
        
        :param func: Function to integrate
        :param start: Starting point
        :param end: Ending point
        :param num_steps: Number of steps for integration
        :return: Dictionary with integral value and conclusion
        """
        # Numerical integration using trapezoidal rule
        h = (end - start) / num_steps
        integral = (func(start) + func(end)) / 2
        
        for i in range(1, num_steps):
            integral += func(start + i * h)
        
        integral *= h
        
        # Check if integral converges
        if integral < 1e10:  # Converges if finite
            conclusion = 'converges'
        else:
            conclusion = 'diverges'
        
        return {
            'integral_value': integral,
            'conclusion': conclusion
        }
    
    @staticmethod
    def comparison_test(series_a, series_b, num_terms=100):
        """
        Comparison Test: If 0 ≤ a_n ≤ b_n:
        - If Σ b_n converges, then Σ a_n converges
        - If Σ a_n diverges, then Σ b_n diverges
        
        :param series_a: Terms of first series (candidate)
        :param series_b: Terms of comparison series (known convergence)
        :param num_terms: Number of terms to check
        :return: Dictionary with conclusion
        """
        if not isinstance(series_a, list):
            series_a = list(series_a)
        if not isinstance(series_b, list):
            series_b = list(series_b)
        
        # Check comparison
        check_terms = min(num_terms, len(series_a), len(series_b))
        
        for i in range(check_terms):
            if series_a[i] > series_b[i] + 1e-10:
                return {
                    'valid': False,
                    'reason': 'Comparison not satisfied: a_n > b_n'
                }
        
        # Assume series_b convergence is known
        return {
            'valid': True,
            'reason': 'Comparison satisfied: a_n ≤ b_n',
            'conclusion': 'Convergence of series_b implies convergence of series_a'
        }
    
    @staticmethod
    def limit_comparison_test(series_a, series_b, num_terms=100):
        """
        Limit Comparison Test: If lim (a_n / b_n) = c > 0:
        Σ a_n and Σ b_n both converge or both diverge
        
        :param series_a: Terms of first series
        :param series_b: Terms of comparison series
        :param num_terms: Number of terms to examine
        :return: Dictionary with limit and conclusion
        """
        if not isinstance(series_a, list):
            series_a = list(series_a)
        if not isinstance(series_b, list):
            series_b = list(series_b)
        
        # Compute ratios
        ratios = []
        for i in range(min(num_terms, len(series_a), len(series_b))):
            if abs(series_b[i]) > 1e-15:
                ratio = series_a[i] / series_b[i]
                ratios.append(ratio)
        
        if not ratios:
            return {'limit': None, 'conclusion': 'inconclusive'}
        
        # Limit is average of last few ratios
        limit = sum(ratios[-10:]) / len(ratios[-10:])
        
        if limit > 1e-10 and limit < 1e10:  # Finite positive limit
            conclusion = 'Series have same convergence'
        else:
            conclusion = 'inconclusive'
        
        return {
            'limit': limit,
            'ratios': ratios,
            'conclusion': conclusion
        }
    
    @staticmethod
    def alternating_series_test(terms, num_check=100):
        """
        Alternating Series Test: For series Σ(-1)^n * b_n where b_n > 0:
        Converges if:
        1. b_n is decreasing
        2. lim b_n = 0
        
        :param terms: Terms of alternating series (including signs)
        :param num_check: Number of terms to check
        :return: Dictionary with test results
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        # Get absolute values
        abs_terms = [abs(t) for t in terms]
        
        # Check if decreasing
        decreasing = all(abs_terms[i] >= abs_terms[i+1] 
                        for i in range(len(abs_terms)-1))
        
        # Check if limit is zero
        limit_zero = abs(abs_terms[-1]) < 1e-10
        
        if decreasing and limit_zero:
            conclusion = 'converges'
        else:
            conclusion = 'diverges'
        
        return {
            'decreasing': decreasing,
            'limit_zero': limit_zero,
            'conclusion': conclusion,
            'num_terms_checked': len(abs_terms)
        }
    
    # ==================== POWER SERIES ====================
    
    @staticmethod
    def power_series_at_point(coefficients, x, center=0):
        """
        Evaluate power series: Σ c_n(x - a)^n
        
        :param coefficients: List of coefficients [c_0, c_1, c_2, ...]
        :param x: Point at which to evaluate
        :param center: Center of series (a)
        :return: Sum of power series
        """
        result = 0
        for n, c in enumerate(coefficients):
            result += c * ((x - center) ** n)
        return result
    
    @staticmethod
    def radius_of_convergence_ratio(coefficients, num_check=None):
        """
        Find radius of convergence using Ratio Test.
        R = lim |c_n / c_{n+1}|
        
        :param coefficients: List of series coefficients
        :param num_check: Number of ratios to check
        :return: Radius of convergence
        """
        ratios = []
        for i in range(len(coefficients) - 1):
            if abs(coefficients[i+1]) > 1e-15:
                ratio = abs(coefficients[i] / coefficients[i+1])
                ratios.append(ratio)
        
        if not ratios:
            return float('inf')
        
        # Use last several ratios
        last_ratios = ratios[-min(num_check or 10, len(ratios)):]
        R = sum(last_ratios) / len(last_ratios)
        
        return R
    
    @staticmethod
    def radius_of_convergence_root(coefficients, num_check=None):
        """
        Find radius of convergence using Root Test.
        R = lim 1 / |c_n|^(1/n)
        
        :param coefficients: List of series coefficients
        :param num_check: Number of roots to check
        :return: Radius of convergence
        """
        roots = []
        for n, c in enumerate(coefficients):
            if n > 0 and c != 0:
                root = abs(c) ** (1/n)
                roots.append(root)
        
        if not roots:
            return float('inf')
        
        # Use last several roots
        last_roots = roots[-min(num_check or 10, len(roots)):]
        L = sum(last_roots) / len(last_roots)
        
        if L < 1e-15:
            return float('inf')
        
        R = 1 / L
        return R
    
    @staticmethod
    def interval_of_convergence(coefficients, center=0, num_check=None):
        """
        Find interval of convergence for power series Σ c_n(x - a)^n
        
        :param coefficients: List of coefficients
        :param center: Center of series
        :param num_check: Number of terms to check
        :return: Dictionary with interval information
        """
        R = Series.radius_of_convergence_ratio(coefficients, num_check)
        
        if R == float('inf'):
            return {
                'radius': float('inf'),
                'interval': '(-∞, ∞)',
                'converges_everywhere': True
            }
        
        left = center - R
        right = center + R
        
        return {
            'radius': R,
            'center': center,
            'interval': f'({left}, {right})',
            'left_endpoint': left,
            'right_endpoint': right
        }
    
    # ==================== TAYLOR AND MACLAURIN SERIES ====================
    
    @staticmethod
    def taylor_series_approximation(func, center, x, num_terms, h=1e-5):
        """
        Approximate function using Taylor series around center point.
        f(x) ≈ f(c) + f'(c)(x-c) + f''(c)(x-c)²/2! + ...
        
        :param func: Function to approximate
        :param center: Center point (c)
        :param x: Point at which to evaluate
        :param num_terms: Number of terms to use
        :param h: Step size for numerical derivatives
        :return: Taylor series approximation
        """
        result = func(center)
        factorial = 1
        
        # Approximate derivatives using finite differences
        current_func = func
        
        for n in range(1, num_terms):
            factorial *= n
            
            # Approximate nth derivative
            deriv_val = Series._approximate_derivative(current_func, center, h)
            
            result += (deriv_val / factorial) * ((x - center) ** n)
            
            # For next iteration (approximate derivative of derivative)
            current_func = lambda t, f=current_func, s=h: \
                (f(t + s) - f(t - s)) / (2 * s)
        
        return result
    
    @staticmethod
    def _approximate_derivative(func, x, h=1e-5):
        """Helper function to compute numerical derivative"""
        return (func(x + h) - func(x - h)) / (2 * h)
    
    @staticmethod
    def maclaurin_series_sin(x, num_terms=10):
        """
        Maclaurin series for sin(x):
        sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...
        
        :param x: Point at which to evaluate
        :param num_terms: Number of terms to use
        :return: Approximation of sin(x)
        """
        result = 0
        for n in range(num_terms):
            sign = (-1) ** n
            factorial = 1
            for i in range(1, 2*n + 2):
                factorial *= i
            result += sign * (x ** (2*n + 1)) / factorial
        return result
    
    @staticmethod
    def maclaurin_series_cos(x, num_terms=10):
        """
        Maclaurin series for cos(x):
        cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...
        
        :param x: Point at which to evaluate
        :param num_terms: Number of terms to use
        :return: Approximation of cos(x)
        """
        result = 0
        for n in range(num_terms):
            sign = (-1) ** n
            factorial = 1
            for i in range(1, 2*n + 1):
                factorial *= i
            result += sign * (x ** (2*n)) / factorial
        return result
    
    @staticmethod
    def maclaurin_series_exp(x, num_terms=10):
        """
        Maclaurin series for e^x:
        e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
        
        :param x: Point at which to evaluate
        :param num_terms: Number of terms to use
        :return: Approximation of e^x
        """
        result = 0
        factorial = 1
        for n in range(num_terms):
            if n > 0:
                factorial *= n
            result += (x ** n) / factorial
        return result
    
    @staticmethod
    def maclaurin_series_ln(x, num_terms=10):
        """
        Maclaurin series for ln(1 + x):
        ln(1 + x) = x - x²/2 + x³/3 - x⁴/4 + ...
        Valid for -1 < x ≤ 1
        
        :param x: Point at which to evaluate (must satisfy -1 < x ≤ 1)
        :param num_terms: Number of terms to use
        :return: Approximation of ln(1 + x)
        """
        if x <= -1 or x > 1:
            raise ValueError("x must satisfy -1 < x ≤ 1")
        
        result = 0
        for n in range(1, num_terms + 1):
            sign = (-1) ** (n + 1)
            result += sign * (x ** n) / n
        return result
    
    @staticmethod
    def maclaurin_series_geometric(x, num_terms=10):
        """
        Maclaurin series for 1/(1-x):
        1/(1-x) = 1 + x + x² + x³ + ...
        Valid for |x| < 1
        
        :param x: Point at which to evaluate (must satisfy |x| < 1)
        :param num_terms: Number of terms to use
        :return: Approximation of 1/(1-x)
        """
        if abs(x) >= 1:
            raise ValueError("x must satisfy |x| < 1")
        
        result = sum(x ** n for n in range(num_terms))
        return result
    
    # ==================== FOURIER SERIES ====================
    
    @staticmethod
    def fourier_series_approximation(func, L, num_terms, x):
        """
        Approximate periodic function with period 2L using Fourier series.
        f(x) ≈ a₀/2 + Σ[a_n*cos(nπx/L) + b_n*sin(nπx/L)]
        
        :param func: Function defined on [-L, L]
        :param L: Half-period
        :param num_terms: Number of terms in series
        :param x: Point at which to evaluate
        :return: Fourier approximation
        """
        # Compute Fourier coefficients numerically
        # a_n = (1/L) ∫_{-L}^{L} f(x)cos(nπx/L) dx
        # b_n = (1/L) ∫_{-L}^{L} f(x)sin(nπx/L) dx
        
        # Numerical integration (trapezoidal rule)
        num_points = 1000
        h = 2 * L / num_points
        
        # Compute a_0
        a0 = 0
        for i in range(num_points):
            a0 += func(-L + i * h)
        a0 = a0 * h / L
        
        result = a0 / 2
        
        # Compute a_n and b_n
        for n in range(1, num_terms + 1):
            # a_n
            an = 0
            for i in range(num_points):
                xi = -L + i * h
                an += func(xi) * cos(n * pi * xi / L)
            an = an * h / L
            
            # b_n
            bn = 0
            for i in range(num_points):
                xi = -L + i * h
                bn += func(xi) * sin(n * pi * xi / L)
            bn = bn * h / L
            
            result += an * cos(n * pi * x / L) + bn * sin(n * pi * x / L)
        
        return result
    
    # ==================== SERIES OPERATIONS ====================
    
    @staticmethod
    def series_sum_limit(terms, num_terms=1000, tolerance=1e-10):
        """
        Compute sum of series and check for convergence.
        
        :param terms: Generator or list of terms
        :param num_terms: Maximum terms to sum
        :param tolerance: Convergence criterion
        :return: Dictionary with sum and convergence info
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        if num_terms:
            terms = terms[:num_terms]
        
        # Compute partial sums
        current_sum = 0
        converged = False
        
        for i, term in enumerate(terms):
            prev_sum = current_sum
            current_sum += term
            
            # Check for convergence
            if i > 0 and abs(current_sum - prev_sum) < tolerance:
                converged = True
                break
        
        return {
            'sum': current_sum,
            'converged': converged,
            'num_terms_used': len(terms),
            'last_term_added': terms[-1] if terms else 0
        }
    
    @staticmethod
    def series_remainder_estimate(terms, num_terms_used):
        """
        Estimate the error (remainder) when truncating series.
        R_n ≈ last few terms
        
        :param terms: All terms of the series
        :param num_terms_used: Number of terms already summed
        :return: Remainder estimate
        """
        if len(terms) <= num_terms_used:
            return 0
        
        remaining_terms = terms[num_terms_used:]
        remainder = sum(remaining_terms[:min(10, len(remaining_terms))])
        
        return abs(remainder)
    
    @staticmethod
    def series_acceleration(terms, num_terms=100):
        """
        Apply Shanks transformation to accelerate series convergence.
        Useful for slowly converging series.
        
        :param terms: List of partial sums or terms
        :param num_terms: Number of terms to use
        :return: Accelerated approximation
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        terms = terms[:num_terms]
        
        if len(terms) < 3:
            return sum(terms)
        
        # Compute partial sums if given terms
        partial_sums = []
        current = 0
        for term in terms:
            current += term
            partial_sums.append(current)
        
        # Apply Shanks transformation
        accelerated = []
        for i in range(len(partial_sums) - 2):
            s0, s1, s2 = partial_sums[i], partial_sums[i+1], partial_sums[i+2]
            
            denom = s2 - 2*s1 + s0
            if abs(denom) > 1e-15:
                accel = s2 - (s2 - s1)**2 / denom
                accelerated.append(accel)
        
        return sum(accelerated) / len(accelerated) if accelerated else partial_sums[-1]
    
    # ==================== SERIES ANALYSIS ====================
    
    @staticmethod
    def series_analysis_summary(terms, center=0, num_convergence_checks=50):
        """
        Comprehensive analysis of series convergence.
        
        :param terms: List of series terms
        :param center: Center point for power series
        :param num_convergence_checks: Number of terms to use in tests
        :return: Dictionary with all convergence test results
        """
        if not isinstance(terms, list):
            terms = list(terms)
        
        summary = {
            'num_terms': len(terms),
            'nth_term_test': Series.nth_term_test(terms, num_convergence_checks),
            'ratio_test': Series.ratio_test(terms, num_convergence_checks),
            'root_test': Series.root_test(terms, num_convergence_checks),
            'alternating_test': Series.alternating_series_test(terms, num_convergence_checks)
        }
        
        return summary
    
    @staticmethod
    def series_comparison_chart(terms_a, terms_b, labels=('Series A', 'Series B'), num_terms=100):
        """
        Compare two series term by term.
        
        :param terms_a: First series terms
        :param terms_b: Second series terms
        :param labels: Labels for series
        :param num_terms: Number of terms to display
        :return: Comparison data
        """
        if not isinstance(terms_a, list):
            terms_a = list(terms_a)
        if not isinstance(terms_b, list):
            terms_b = list(terms_b)
        
        terms_a = terms_a[:num_terms]
        terms_b = terms_b[:num_terms]
        
        comparison = []
        for i in range(min(len(terms_a), len(terms_b))):
            comparison.append({
                'n': i + 1,
                labels[0]: terms_a[i],
                labels[1]: terms_b[i],
                'ratio_a_b': terms_a[i] / terms_b[i] if abs(terms_b[i]) > 1e-15 else float('inf')
            })
        
        return comparison
    @staticmethod
    def taylor_series(func, x0, x, n_terms=10, h=1e-5):
        """
        Approximate a function using Taylor series expansion around x0.
        
        :param func: The function to approximate
        :param x0: Point around which to expand
        :param x: Point at which to evaluate
        :param n_terms: Number of terms to use
        :param h: Step size for derivative calculation
        :return: Taylor series approximation
        """
        result = func(x0)
        factorial = 1
        derivative = func(x0)
        
        for n in range(1, n_terms):
            factorial *= n
            derivative = Analytic.numerical_derivative(
                lambda t: Analytic.numerical_derivative(func, t, h), x0, h
            )
            result += (derivative / factorial) * ((x - x0) ** n)
        
        return result
    
    @staticmethod
    def taylor_polynomial_sine(x, n_terms=10):
        """Taylor series for sine function."""
        result = 0
        for n in range(n_terms):
            result += ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        return result
    
    @staticmethod
    def taylor_polynomial_cosine(x, n_terms=10):
        """Taylor series for cosine function."""
        result = 0
        for n in range(n_terms):
            result += ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        return result
    
    @staticmethod
    def taylor_polynomial_exponential(x, n_terms=10):
        """Taylor series for exponential function."""
        return sum((x ** n) / factorial(n) for n in range(n_terms))
    
    @staticmethod
    def taylor_polynomial_logarithm(x, n_terms=10):
        """
        Taylor series for natural logarithm around x=1.
        Valid for 0 < x <= 2
        """
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        result = 0
        for n in range(1, n_terms + 1):
            result += ((-1) ** (n + 1)) * ((x - 1) ** n) / n
        return result
    
    @staticmethod
    def power_series(coefficients, x):
        """
        Evaluate a power series given coefficients.
        
        :param coefficients: List of coefficients [a0, a1, a2, ...]
        :param x: Value at which to evaluate
        :return: Sum of a0 + a1*x + a2*x^2 + ...
        """
        return sum(coeff * (x ** i) for i, coeff in enumerate(coefficients))

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
    

class Analytic:
    """
    A comprehensive class for mathematical analysis including calculus, limits, series, and sequences.
    """
    
    # ==================== CONVERGENCE TESTS ====================
    
    @staticmethod
    def ratio_test(sequence, start_index=0):
        """
        Ratio test for convergence of series.
        
        :param sequence: List of terms in the series
        :param start_index: Starting index for calculation
        :return: Limit of ratio (if < 1, series converges)
        """
        ratios = []
        for i in range(start_index, len(sequence) - 1):
            if sequence[i] != 0:
                ratios.append(abs(sequence[i + 1] / sequence[i]))
        
        if ratios:
            return ratios[-1]  # Return the last ratio
        return 0
    
    @staticmethod
    def root_test(sequence, start_index=0):
        """
        Root test for convergence of series.
        
        :param sequence: List of terms in the series
        :param start_index: Starting index
        :return: Limit of nth root (if < 1, series converges)
        """
        roots = []
        for i in range(start_index, len(sequence)):
            roots.append(abs(sequence[i]) ** (1 / (i + 1)))
        
        if roots:
            return roots[-1]
        return 0
    
    @staticmethod
    def alternating_series_test(sequence):
        """
        Test for convergence of alternating series.
        Checks if terms decrease and approach zero.
        
        :param sequence: List of absolute values of terms
        :return: True if series likely converges
        """
        # Check if terms are decreasing
        decreasing = all(sequence[i] >= sequence[i + 1] for i in range(len(sequence) - 1))
        
        # Check if limit approaches zero
        limit_zero = sequence[-1] < 1e-10
        
        return decreasing and limit_zero
    
    # ==================== EXTREMA AND CRITICAL POINTS ====================
    
    
    # ==================== UTILITY FUNCTIONS ====================
    
    @staticmethod
    def verify_limit_behavior(func, x_val, num_points=100):
        """
        Verify limit behavior by sampling points approaching x_val.
        
        :param func: The function
        :param x_val: The limit point
        :param num_points: Number of sample points
        :return: List of function values at points approaching x_val
        """
        values = []
        for i in range(1, num_points + 1):
            delta = 1 / (i ** 2)
            try:
                values.append(func(x_val + delta))
            except:
                continue
        return values