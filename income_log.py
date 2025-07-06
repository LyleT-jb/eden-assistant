# income_log.py
import json
import datetime

LOG_FILE = "income_log.json"

def log_income(source, amount):
    today = datetime.date.today().isoformat()
    try:
        with open(LOG_FILE, "r") as f:
            log = json.load(f)
    except:
        log = {}
    if today not in log:
        log[today] = []
    log[today].append({"source": source, "amount": amount})
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

def save_daily_summary():
    print("📄 Daily income summary saved.")

# (other files remain unchanged)
