import os
import platform

class OSHelper:
    @staticmethod
    def get_os():
        return platform.system()

    @staticmethod
    def ensure_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def file_exists(path):
        return os.path.isfile(path)

    @staticmethod
    def delete_file(self, path):
        if self.file_exists(path):
            os.remove(path)

    @staticmethod
    def list_dir(path):
        return os.listdir(path)

    @staticmethod
    def get_current_directory():
        return os.getcwd()

    @staticmethod
    def change_directory(path):
        os.chdir(path)

    @staticmethod
    def get_file_size(self, path):
        if self.file_exists(path):
            return os.path.getsize(path)
        return None

    @staticmethod
    def join_paths(*paths):
        return os.path.join(*paths)


    @staticmethod
    def create_file(path, content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def create_directory(path):
        if not os.path.exists(path):
            os.makedirs(path)
    
