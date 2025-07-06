# goal_tracker.py
from settings import load_settings

def track_goals():
    goals = load_settings().get("income_goal")
    print(f"📊 Tracking progress: {goals}")
