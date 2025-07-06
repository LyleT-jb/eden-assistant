# command_handler.py
from income_engine import make_money
import webbrowser


def handle_command(cmd):
    cmd = cmd.lower()

    if "money" in cmd or "start money engine" in cmd:
        return make_money()

    elif "goal" in cmd:
        return "Your goal is to earn R70K before 13 July 2025. We are tracking your progress."

    elif "hello" in cmd:
        return "Hello! I'm here and ready."

    elif "search" in cmd:
        search_term = cmd.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        return f"🔍 Searching Google for: {search_term}"

    elif "get me free stuff" in cmd:
        from free_stuff_finder import get_real_free_items
        return get_real_free_items()

    elif "save" in cmd and "r" in cmd:
        amount = ''.join([c for c in cmd if c.isdigit()])
        from saver import save_money
        return save_money(int(amount))

    elif "report" in cmd:
        from report_sender import send_report
        return send_report()

    else:
        return "I heard you, Lyle. I'll learn more soon."






