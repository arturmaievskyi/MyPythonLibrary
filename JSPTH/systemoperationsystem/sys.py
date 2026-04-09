import sys

def get_system_info():
    return {
        "platform": sys.platform,
        "version": sys.version,
        "executable": sys.executable,
        "path": sys.path,
        "modules": list(sys.modules.keys())
    }

def exit_program(code=0):
    sys.exit(code)

def get_python_version():
    return sys.version_info

def get_loaded_modules():
    return sys.modules

