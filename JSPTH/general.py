import os
import time
import sys
import abc

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def repeat_function(func, times, *args, **kwargs):
    """Repeats a function a specified number of times."""
    results = []
    for _ in range(times):
        results.append(func(*args, **kwargs))
    return results

def time_function(func, *args, **kwargs):
    """Times how long a function takes to execute."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

class Timer:
    """A simple timer class."""
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Starts the timer."""
        self.start_time = time.time()

    def stop(self):
        """Stops the timer."""
        self.end_time = time.time()

    def elapsed(self):
        """Returns the elapsed time."""
        if self.start_time is None or self.end_time is None:
            raise ValueError("Timer has not been started and stopped properly.")
        return self.end_time - self.start_time
    
def compilation_time(func, *args, **kwargs):
    """Measures the compilation time of a function."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

class RepeatFunction:
    """Class to repeat a function multiple times."""
    def __init__(self, func, times):
        self.func = func
        self.times = times

    def run(self, *args, **kwargs):
        """Runs the function the specified number of times."""
        results = []
        for _ in range(self.times):
            results.append(self.func(*args, **kwargs))
        return results
    
    def measure_time(func):
        """Decorator to measure the execution time of a function."""
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
            return result
        return wrapper
    
def initialize(func):
    """Initialize a function"""
    __init__ = func
    return __init__

def initialize(*funcs):
    """Initialize multiple functions"""
    __init__ = funcs
    return __init__

def initialize(cls):
    """Initialize a class"""
    __init__ = cls
    return __init__

def initialize(*cls):
    """Initialize multiple classes"""
    __init__ = cls
    return __init__

def system_info():
    """Prints system information."""
    print(f"Platform: {sys.platform}")
    print(f"Python Version: {sys.version}")
    print(f"Executable: {sys.executable}")
    print(f"Current Working Directory: {os.getcwd()}")

