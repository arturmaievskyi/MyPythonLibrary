from math import *
from advanced_calculator import *
import numpy as np
import sys
from .analytic import Analytic

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
