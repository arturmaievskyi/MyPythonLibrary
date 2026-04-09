import math

class Expression:
    def __init__(self, expression: str):
        self.expression = expression

    def evaluate(self, context: dict = None) -> float:
        if context is None:
            context = {}
        try:
            result = eval(self.expression, {}, context)
            return float(result)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{self.expression}': {e}")
        
    def __str__(self):
        return self.expression
    
    def __repr__(self):
        return f"Expression('{self.expression}')"


class cubicExpression(Expression):
    def __init__(self, a: float, b: float, c: float, d: float):
        super().__init__(f"{a}*x**3 + {b}*x**2 + {c}*x + {d}")

    def evaluate(self, x: float) -> float:
        return super().evaluate({'x': x})
    
class quadraticExpression(Expression):
    def __init__(self, a: float, b: float, c: float):
        a = a if a != 0 else 1
        b = b if b != 0 else 1
        c = c if c != 0 else 1

    def evaluate(self, x: float) -> float:
        descriminant = self.b**2 - 4*self.a*self.c
        if descriminant < 0:
            raise ValueError("No real roots.")
        root1 = (-self.b + math.sqrt(descriminant)) / (2*self.a)
        root2 = (-self.b - math.sqrt(descriminant)) / (2*self.a)
        return root1, root2