import json
import os

JSON_PATH = os.path.join(os.path.dirname(__file__), "save_convertions.json")

# Loads all conversion data from the JSON file
def load_convertions():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# Saves all conversion data to the JSON file
def save_convertions(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Returns the default conversion dictionary
def get_default_convertion():
    data = load_convertions()
    return data["default"]

# Returns the list of custom conversion dictionaries
def get_custom_convertions():
    data = load_convertions()
    return data["custom"]

# Adds a new custom conversion list with a name
def add_custom_convertion(name, items):
    data = load_convertions()
    data["custom"].append({"name": name, "items": items})
    save_convertions(data)

# Removes a custom conversion list by its index
def remove_custom_convertion(index):
    data = load_convertions()
    if 0 <= index < len(data["custom"]):
        del data["custom"][index]
        save_convertions(data)