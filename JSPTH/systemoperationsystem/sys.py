import sys

class SystemHelper:
    @staticmethod
    def get_system_info():
        return {
            "platform": sys.platform,
            "version": sys.version,
            "executable": sys.executable,
            "path": sys.path,
            "modules": list(sys.modules.keys())
        }

    @staticmethod
    def exit_program(code=0):
        sys.exit(code)

    @staticmethod
    def get_python_version():
        return sys.version_info

    @staticmethod
    def get_loaded_modules():
        return sys.modules
    
    @staticmethod
    def get_command_line_args():
        return sys.argv
    
    @staticmethod
    def get_max_recursion_depth():
        return sys.getrecursionlimit()
    
    @staticmethod
    def set_max_recursion_depth(limit):
        return sys.setrecursionlimit(limit)
    
    