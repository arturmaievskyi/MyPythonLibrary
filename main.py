from JSPTH import Console
from JSPTH import Calc

console = Console.console.Console()
calc = Calc.BaseCalculator()

result = calc.add(5, 3)
console.print(f"The result of adding 5 and 3 is: {result}")

