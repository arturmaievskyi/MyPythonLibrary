import os

class FileOperations:
    @staticmethod
    def read_file(path):
        with open(path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(path, content):
        with open(path, 'w') as file:
            file.write(content)

    @staticmethod
    def append_file(path, content):
        with open(path, 'a') as file:
            file.write(content)

    @staticmethod
    def file_exists(path):
        return os.path.exists(path)

    @staticmethod
    def delete_file(path):
        os.remove(path)

    @staticmethod
    def list_files(directory):
        return os.listdir(directory)

    @staticmethod
    def create_directory(path):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def delete_directory(path):
        os.rmdir(path)

    @staticmethod
    def get_file_size(path):
        return os.path.getsize(path)

    @staticmethod
    def get_file_extension(path):
        return os.path.splitext(path)[1]

    @staticmethod
    def get_file_name(path):
        return os.path.basename(path)

    @staticmethod
    def get_file_directory(path):
        return os.path.dirname(path)

    @staticmethod
    def copy_file(src, dest):
        with open(src, 'rb') as source_file:
            with open(dest, 'wb') as dest_file:
                dest_file.write(source_file.read())

    @staticmethod
    def move_file(src, dest):
        os.rename(src, dest)

    @staticmethod
    def read_binary_file(path):
        with open(path, 'rb') as file:
            return file.read()

    @staticmethod
    def write_binary_file(path, content):
        with open(path, 'wb') as file:
            file.write(content)

    @staticmethod
    def append_binary_file(path, content):
        with open(path, 'ab') as file:
            file.write(content)

    @staticmethod
    def get_absolute_path(path):
        return os.path.abspath(path)

    @staticmethod
    def get_relative_path(path, start=os.curdir):
        return os.path.relpath(path, start)

    @staticmethod
    def join_paths(*paths):
        return os.path.join(*paths)

    @staticmethod
    def split_path(path):
        return os.path.split(path)

    @staticmethod
    def split_extension(path):
        return os.path.splitext(path)

    @staticmethod
    def normalize_path(path):
        return os.path.normpath(path)

    @staticmethod
    def resolve_path(path):
        return os.path.realpath(path)

    @staticmethod
    def is_file(path):
        return os.path.isfile(path)

    @staticmethod
    def is_directory(path):
        return os.path.isdir(path)

    @staticmethod
    def get_creation_time(path):
        return os.path.getctime(path)

    @staticmethod
    def get_modification_time(path):
        return os.path.getmtime(path)

    @staticmethod
    def get_access_time(path):
        return os.path.getatime(path)

    @staticmethod
    def change_file_permissions(path, mode):
        os.chmod(path, mode)

    @staticmethod
    def change_file_owner(path, uid, gid):
            os.chown(path, uid, gid)
