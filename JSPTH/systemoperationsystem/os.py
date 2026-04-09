import os
import platform

def get_os():
    return platform.system()

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def file_exists(path):
    return os.path.isfile(path)

def delete_file(path):
    if file_exists(path):
        os.remove(path)

def list_dir(path):
    return os.listdir(path)

def get_current_directory():
    return os.getcwd()

def change_directory(path):
    os.chdir(path)

def get_file_size(path):
    if file_exists(path):
        return os.path.getsize(path)
    return None

def join_paths(*paths):
    return os.path.join(*paths)

