# settings.py
import json

SETTINGS_FILE = "settings.json"

def load_settings():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)
