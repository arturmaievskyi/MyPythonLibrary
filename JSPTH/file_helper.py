import json
import os

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def append_json(path, data):
    if os.path.exists(path):
        existing_data = read_json(path)
        if isinstance(existing_data, list):
            existing_data.append(data)
            write_json(path, existing_data)
        else:
            raise ValueError("Existing JSON data is not a list. Cannot append.")
    else:
        write_json(path, [data])


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def append_text(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write(text)