# memory.py
import json

MEMORY_FILE = "memory.json"

def remember(command):
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append(command)
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def recall():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []