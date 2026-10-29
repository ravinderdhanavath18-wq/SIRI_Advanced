import webbrowser
from urllib.parse import quote

class BrowserController:
    def search_google(self, query: str):
        if not query:
            return "What should I search for?"
        search_url = "https://www.google.com/search?q=" + quote(query)
        webbrowser.open(search_url)
        return f"Searching Google for: {query}"

    def open_youtube(self, query: str = ""):
        if query:
            search_url = "https://www.youtube.com/results?search_query=" + quote(query)
            webbrowser.open(search_url)
            return f"Searching YouTube for: {query}"
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    def open_url(self, url: str):
        if not url:
            return "No URL provided."
        webbrowser.open(url)
        return f"Opening: {url}"

    def open_whatsapp_web(self):
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp Web."
