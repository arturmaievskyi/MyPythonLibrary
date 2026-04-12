import math


class BaseCalculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b  
    
    def power(self, a, b):
        return a ** b
    
    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        return a ** 0.5
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot take factorial of negative number.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def percentage(a, b):
        return (a / b) * 100
    
    