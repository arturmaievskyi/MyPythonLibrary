import os
import sys

class Console:
    def __init__(self):
        pass

    def log(self, message):
        print(message)

    def print(self, massage):
        print(massage)

    def input(self, prompt):
        return input(prompt)
    
    def convert_toINT(self, value):
        try:
            return int(value)
        except ValueError:
            Console.log("Conversion to INT failed.")
            return None
        
    def convert_toFLOAT(self, value):
        try:
            return float(value)
        except ValueError:
            Console.log("Conversion to FLOAT failed.")
            return None
        
    def convert_toSTRING(self, value):
        try:
            return str(value)
        except ValueError:
            Console.log("Conversion to STRING failed.")
            return None
        
    def convert_toBOOL(value):
        try:
            return bool(value)
        except ValueError:
            Console.log("Conversion to BOOL failed.")
            return None
        
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def convert_toCOMPLEX(self, value):
        try:
            return complex(value)
        except ValueError:
            Console.log("Conversion to COMPLEX failed.")
            return None
        
    def stop():
        sys.exit()

    def pause():
        os.system('pause')

    
    