from math import*
from .advanced_calculator import *

class Computational:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

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