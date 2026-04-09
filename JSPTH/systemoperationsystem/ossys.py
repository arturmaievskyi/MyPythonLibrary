import os
import sys

def restart_program():
    """Restarts the current program."""
    python = sys.executable
    os.execl(python, python, *sys.argv)