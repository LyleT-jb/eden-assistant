# income_engine.py
from dropshipping_bot import start_dropshipping
from content_bot import create_and_upload_video
from affiliate_engine import find_affiliate_opps
from free_stuff_finder import find_free_items
from freelance_finder import find_freelance_jobs

def make_money():
    print("💼 Eden is now making you money in every way (except trading).")
    start_dropshipping()
    create_and_upload_video()
    find_affiliate_opps()
    find_free_items()
    find_freelance_jobs()
    return "All systems activated. Money engines running."
