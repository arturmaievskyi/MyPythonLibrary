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
