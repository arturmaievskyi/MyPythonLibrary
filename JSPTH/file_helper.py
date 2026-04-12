import json
import os
import sys

class FileHelper:
    @staticmethod
    def read_json(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def write_json(path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def append_json(self, path, data):
        if os.path.exists(path):
            existing_data = self.read_json(path)
            if isinstance(existing_data, list):
                existing_data.append(data)
                self.write_json(path, existing_data)
            else:
                raise ValueError("Existing JSON data is not a list. Cannot append.")
        else:
            self.write_json(path, [data])


    @staticmethod
    def read_text(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def write_text(path, text):
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    @staticmethod
    def append_text(path, text):
        with open(path, "a", encoding="utf-8") as f:
            f.write(text)

