import requests
from bs4 import BeautifulSoup

def find_properties():
    url = "https://www.property24.com/for-sale/western-cape/cape-town/432"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        listings = soup.select(".p24_content")[:3]
        results = []
        for item in listings:
            title = item.select_one(".p24_title").get_text(strip=True)
            price = item.select_one(".p24_price").get_text(strip=True)
            results.append(f"{title} — {price}")

        return "🏠 Top Cheap Listings:\n" + "\n".join(results)
    except:
        return "❌ Couldn't find listings now. Try again later."
