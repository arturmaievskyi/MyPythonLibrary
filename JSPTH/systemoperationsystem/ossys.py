import os
import sys


class OSSys:
    @staticmethod
    def restart_program():
        """Restarts the current program."""
        python = sys.executable
        os.execl(python, python, *sys.argv)

    @staticmethod
    def clear_console():
        """Clears the console screen."""
        if os.name == 'nt':  # For Windows
            os.system('cls')

    @staticmethod
    def clear_full_command_history():
        """Clears the command history (only works in interactive mode)."""
        if os.name == 'nt':  # For Windows
            os.system('cmd cls')
            os.system('cls')

    