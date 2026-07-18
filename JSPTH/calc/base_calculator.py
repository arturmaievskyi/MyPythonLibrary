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

    def multiply_advenced(self, a, b):
        if a == 0 or b == 0:
            return 0
        elif a == 1:
            return b
        
        elif b == 1:
            return a
        
        elif a < 0 and b < 0:
            a = abs(a)
            b = abs(b)
                
            for i in range(a, b):
                a += a
            return a
    
    
        elif a<1:
            a = 1/a
            for i in range(1, b):
                a += a
            return 1/a
    
    def is_Odd(self, n):
        return n % 2 != 0
    
    def is_Even(self, n):
        return n % 2 == 0