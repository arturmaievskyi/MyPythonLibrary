import os
def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def append_file(path, content):
    with open(path, 'a') as file:
        file.write(content)

def file_exists(path):
    return path.exists(path)

def delete_file(path):
    os.remove(path)

def list_files(directory):
    return os.listdir(directory)

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def delete_directory(path):
    os.rmdir(path)

def get_file_size(path):
    return os.path.getsize(path)

def get_file_extension(path):
    return os.path.splitext(path)[1]

def get_file_name(path):
    return os.path.basename(path)

def get_file_directory(path):
    return os.path.dirname(path)

def copy_file(src, dest):
    with open(src, 'rb') as source_file:
        with open(dest, 'wb') as dest_file:
            dest_file.write(source_file.read())

def move_file(src, dest):
    os.rename(src, dest)

def read_binary_file(path):
    with open(path, 'rb') as file:
        return file.read()

def write_binary_file(path, content):
    with open(path, 'wb') as file:
        file.write(content)

def append_binary_file(path, content):
    with open(path, 'ab') as file:
        file.write(content)

def get_absolute_path(path):
    return os.path.abspath(path)

def get_relative_path(path, start=os.curdir):
    return os.path.relpath(path, start)

def join_paths(*paths):
    return os.path.join(*paths)

def split_path(path):
    return os.path.split(path)

def split_extension(path):
    return os.path.splitext(path)

def normalize_path(path):
    return os.path.normpath(path)

def resolve_path(path):
    return os.path.realpath(path)

def is_file(path):
    return os.path.isfile(path)

def is_directory(path):
    return os.path.isdir(path)

def get_creation_time(path):
    return os.path.getctime(path)

def get_modification_time(path):
    return os.path.getmtime(path)

def get_access_time(path):
    return os.path.getatime(path)

def change_file_permissions(path, mode):
    os.chmod(path, mode)

def change_file_owner(path, uid, gid):
    os.chown(path, uid, gid)
