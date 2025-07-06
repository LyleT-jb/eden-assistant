import webbrowser

def search_web(cmd):
    try:
        query = cmd.split("search", 1)[1].strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching Google for: {query}"
    except:
        return "Sorry, I couldn't search that right now."
