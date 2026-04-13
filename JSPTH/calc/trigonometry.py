from math import*
from .advanced_calculator import *
from .base_calculator import *


acalc = AdvancedCalculator()
bcalc = BaseCalculator()

class Trigonometry:

    def __init__(self, angle_rad, A, B, C, value, a, b, c, degrees, radians):
        if angle_rad and A and B and C and value and a and b and c and degrees and radians:
                    self.angle_rad = angle_rad
                    self.A = A
                    self.B = B
                    self.C = C
                    self.value = value
                    self.a = a
                    self.b = b
                    self.c = c
                    self.degrees = degrees
                    self.radians = radians

        if (angle_rad and A and B and C and value and a and b and c and degrees and radians) is None:
                    self.angle_rad = None
                    self.A = None
                    self.B = None
                    self.C = None
                    self.value = None
                    self.a = None
                    self.b = None
                    self.c = None
                    self.degrees = None
                    self.radians = None

    def sine(self, angle_rad):
        return acalc.sine(angle_rad)
    
    def cosine(self, angle_rad):
        return acalc.cosine(angle_rad)
    
    def tangent(self, angle_rad):
        return acalc.tangent(angle_rad)
    
    def cosecant(self, angle_rad):
        sin_value = acalc.sine(angle_rad)
        if sin_value == 0:
            raise ValueError("Cosecant undefined for angles where sine is zero.")
        return 1 / sin_value
    
    def secant(self, angle_rad):
        cos_value = acalc.cosine(angle_rad)
        if cos_value == 0:
            raise ValueError("Secant undefined for angles where cosine is zero.")
        return 1 / cos_value
    
    def cotangent(self, angle_rad):
        tan_value = acalc.tangent(angle_rad)
        if tan_value == 0:
            raise ValueError("Cotangent undefined for angles where tangent is zero.")
        return 1 / tan_value
    
    def arcsine(self, value):
        if value < -1 or value > 1:
            raise ValueError("Arcsine undefined for values outside the range [-1, 1].")
        return math.asin(value)
    
    def arccosine(self, value):
        if value < -1 or value > 1:
            raise ValueError("Arccosine undefined for values outside the range [-1, 1].")
        return math.acos(value)
    
    def arctangent(self, value):
        return math.atan(value)
    
    def arccosecant(self, value):
        if value == 0:
            raise ValueError("Arccosecant undefined for zero.")
        return math.asin(1 / value)
    
    def arcsecant(self, value):
        if value == 0:
            raise ValueError("Arcsecant undefined for zero.")
        return math.acos(1 / value)
    
    def arccotangent(self, value):
        if value == 0:
            raise ValueError("Arccotangent undefined for zero.")
        return math.atan(1 / value)
    
    def degrees_to_radians(self, degrees):
        return math.radians(degrees)
    
    def radians_to_degrees(self, radians):
        return math.degrees(radians)
    
    def law_of_sines(self, a, A, b, B, c, C):
        if A is not None and a is not None:
            if B is not None and b is None:
                return (b * math.sin(math.radians(B))) / math.sin(math.radians(A))
            elif C is not None and c is None:
                return (c * math.sin(math.radians(C))) / math.sin(math.radians(A))
        elif B is not None and b is not None:
            if A is not None and a is None:
                return (a * math.sin(math.radians(A))) / math.sin(math.radians(B))
            elif C is not None and c is None:
                return (c * math.sin(math.radians(C))) / math.sin(math.radians(B))
        elif C is not None and c is not None:
            if A is not None and a is None:
                return (a * math.sin(math.radians(A))) / math.sin(math.radians(C))
            elif B is not None and b is None:
                return (b * math.sin(math.radians(B))) / math.sin(math.radians(C))
        else:
            raise ValueError("Insufficient information to apply the law of sines.")