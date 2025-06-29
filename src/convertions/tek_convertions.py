import json
import os

JSON_PATH = os.path.join(os.path.dirname(__file__), "save_convertions.json")

def load_convertions():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_convertions(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_default_convertion():
    data = load_convertions()
    return data["default"]

def get_custom_convertions():
    data = load_convertions()
    return data["custom"]

def add_custom_convertion(name, items):
    data = load_convertions()
    data["custom"].append({"name": name, "items": items})
    save_convertions(data)

def remove_custom_convertion(index):
    data = load_convertions()
    if 0 <= index < len(data["custom"]):
        del data["custom"][index]
        save_convertions(data)