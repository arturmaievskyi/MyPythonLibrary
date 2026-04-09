import math
import base64


class AdvancedCalculator:
    def modulo(a, b):
        return a % b
    def floor_divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a // b
    
    def absolute(a):
        return abs(a)
    
    def logarithm(a, base=10):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(a, base)
    
    def lagorithm_user_arg(a, base):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(a, base)
    
    def sine(angle_rad):
        return math.sin(angle_rad)
    
    def cosine(angle_rad):
        return math.cos(angle_rad)
    
    def tangent(angle_rad):
        return math.tan(angle_rad)
    
    def random_number(start, end):
        return math.floor(math.random() * (end - start + 1)) + start
    
    def root(a, n):
        if a < 0 and n % 2 == 0:
            raise ValueError("Cannot take even root of negative number.")
        return a ** (1/n)
    
    def exponential(a):
        return math.exp(a)
    
    def permutation(n, r):
        if n < 0 or r < 0 or r > n:
            raise ValueError("Invalid values for permutation.")
        return math.factorial(n) // math.factorial(n - r)
    
    def combination(n, r):
        if n < 0 or r < 0 or r > n:
            raise ValueError("Invalid values for combination.")
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    
    def hyperbolic_sine(x):
        return math.sinh(x)
    
    def hyperbolic_cosine(x):
        return math.cosh(x)
    
    def hyperbolic_tangent(x):
        return math.tanh(x)
    
    def sineh_inverse(x):
        return math.asinh(x)
    
    def cosineh_inverse(x):
        return math.acosh(x)
    
    def tangenth_inverse(x):
        return math.atanh(x)
    
    def pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
    
    def viniette_formula(a, b):
        return (a + b) * (a - b)
    
    def golden_ratio(n):
        phi = (1 + math.sqrt(5)) / 2
        return phi * n
    
    def silver_ratio(n):
        delta = 1 + math.sqrt(2)
        return delta * n
    
    def bronze_ratio(n):
        gamma = (3 + math.sqrt(13)) / 2
        return gamma * n
    
    def mean(values):
        if len(values) == 0:
            raise ValueError("Cannot compute mean of empty list.")
        return sum(values) / len(values)
    
    def median(values):
        if len(values) == 0:
            raise ValueError("Cannot compute median of empty list.")
        sorted_values = sorted(values)
        mid = len(sorted_values) // 2
        if len(sorted_values) % 2 == 0:
            return (sorted_values[mid - 1] + sorted_values[mid]) / 2
        else:
            return sorted_values[mid]
        
    def mode(values):
        if len(values) == 0:
            raise ValueError("Cannot compute mode of empty list.")
        frequency = {}
        for value in values:
            frequency[value] = frequency.get(value, 0) + 1
        max_freq = max(frequency.values())
        modes = [key for key, freq in frequency.items() if freq == max_freq]
        if len(modes) == len(frequency):
            raise ValueError("No mode found; all values are unique.")
        return modes
    
    def cosine_law(a, b, angle_C_rad):
        return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle_C_rad))
    
    def sine_law(a, A_rad, b):
        return (a * math.sin(A_rad)) / b
    
    def herons_formula(a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def circle_area(radius):
        return math.pi * radius**2
    
    def sphere_volume(radius):
        return (4/3) * math.pi * radius**3
    
    def cylinder_volume(radius, height):
        return math.pi * radius**2 * height
    
    def cone_volume(radius, height):
        return (1/3) * math.pi * radius**2 * height
    
    def trapezoid_area(a, b, height):
        return ((a + b) / 2) * height
    
    def ellipse_area(a, b):
        return math.pi * a * b
    
    def square_area(side):
        return side**2
    
    def rectangle_area(length, width):
        return length * width
    
    def triangle_area(base, height):
        return (1/2) * base * height
    
    def circle_radius(area):
        return math.sqrt(area / math.pi)
    
    def sphere_surface_area(radius):
        return 4 * math.pi * radius**2
    
    def cylinder_surface_area(radius, height):
        return 2 * math.pi * radius * (radius + height)
    
    def cone_surface_area(radius, slant_height):
        return math.pi * radius * (radius + slant_height)
    
    def trapezoid_perimeter(a, b, c, d):
        return a + b + c + d
    
    def ellipse_circumference(a, b):
        h = ((a - b)**2) / ((a + b)**2)
        return math.pi * (a + b) * (1 + (3*h) / (10 + math.sqrt(4 - 3*h)))
    
    def fibonacci(n):
        if not isinstance(n, int):
            raise ValueError("Fibonacci input must be an integer.")
        else:
            
            if n < 0:
                raise ValueError("Fibonacci not defined for negative numbers.")
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a
        
    def circle_circumference(radius):
        return 2 * math.pi * radius
    
    def quadratic_formula(a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("No real roots exist.")
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    
    def distance_between_points(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def midpoint(x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def julian_date(day, month, year):
        if month <= 2:
            month += 12
            year -= 1
        A = year // 100
        B = 2 - A + A // 4
        JD = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5
        return JD
    
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
    def lcm(a, b):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return abs(a * b) // gcd(a, b)
    
    def hcf(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    def product_of_list(values):
        result = 1
        for value in values:
            result *= value
        return result
    
    def sum_of_squares(values):
        return sum(x**2 for x in values)

    def product_of_squares(values):
        result = 1
        for x in values:
            result *= x**2
        return result
    
    def base64_encode(data):
        if isinstance(data, str):
            data = data.encode('utf-8')
        encoded_bytes = base64.b64encode(data)
        return encoded_bytes.decode('utf-8')
    
    def base64_decode(data):
        if isinstance(data, str):
            data = data.encode('utf-8')
        decoded_bytes = base64.b64decode(data)
        return decoded_bytes.decode('utf-8')
    
    def harmonic_mean(values):
        if len(values) == 0:
            raise ValueError("Cannot compute harmonic mean of empty list.")
        return len(values) / sum(1/x for x in values)
    
    def geometric_mean(values):
        if len(values) == 0:
            raise ValueError("Cannot compute geometric mean of empty list.")
        product = 1
        for x in values:
            product *= x
        return product ** (1/len(values))
    
    def quadratic_mean(values):
        if len(values) == 0:
            raise ValueError("Cannot compute quadratic mean of empty list.")
        return math.sqrt(sum(x**2 for x in values) / len(values))
    
    def cubic_mean(values):
        if len(values) == 0:
            raise ValueError("Cannot compute cubic mean of empty list.")
        return (sum(x**3 for x in values) / len(values)) ** (1/3)
    
    def weighted_mean(values, weights):
        if len(values) == 0 or len(values) != len(weights):
            raise ValueError("Values and weights must be of same non-zero length.")
        return sum(v * w for v, w in zip(values, weights)) / sum(weights)
    
    def root_mean_square(values):
        if len(values) == 0:
            raise ValueError("Cannot compute root mean square of empty list.")
        return math.sqrt(sum(x**2 for x in values) / len(values))

    def pythagorean_triple(a, b):
        c = math.sqrt(a**2 + b**2)
        return (a, b, c)

