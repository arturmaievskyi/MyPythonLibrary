import os
import sys

class Console:
    def log(message):
        print(message)

    def print(massage):
        print(massage)

    def input(prompt):
        return input(prompt)
    
    def convert_toINT(value):
        try:
            return int(value)
        except ValueError:
            Console.log("Conversion to INT failed.")
            return None
        
    def convert_toFLOAT(value):
        try:
            return float(value)
        except ValueError:
            Console.log("Conversion to FLOAT failed.")
            return None
        
    def convert_toSTRING(value):
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

    def convert_toCOMPLEX(value):
        try:
            return complex(value)
        except ValueError:
            Console.log("Conversion to COMPLEX failed.")
            return None
        
    def stop():
        sys.exit()

    def pause():
        os.system('pause')

    
    