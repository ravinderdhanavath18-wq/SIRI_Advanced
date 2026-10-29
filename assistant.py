import re
from app.voice import VoiceEngine
from app.desktop import DesktopController
from app.browser import BrowserController

class SiriAssistant:
    def __init__(self, on_response=None):
        self.voice = VoiceEngine()
        self.desktop = DesktopController()
        self.browser = BrowserController()
        self.on_response = on_response

    def notify(self, message: str):
        if self.on_response:
            self.on_response(message)

    def speak_and_reply(self, text: str):
        self.notify(text)
        self.voice.speak(text)

    def handle_command(self, text: str):
        command = text.strip().lower()

        if not command:
            return "I am ready. Tell me what you want."

        # Greetings
        if any(word in command for word in ["hello", "hi", "hey", "namaste", "hola"]):
            response = "Hello! I am SIRI, your AI assistant. How can I help you today?"
            self.speak_and_reply(response)
            return response

        # Hindi greeting
        if "नमस्ते" in command or "hello" in command or "hi" in command:
            response = "नमस्ते! मैं SIRI हूँ, आपका सहायक।"
            self.speak_and_reply(response)
            return response

        # Help
        if "help" in command or "what can you do" in command:
            response = (
                "I can open apps, search the web, open YouTube, open WhatsApp Web, "
                "lock the screen, take screenshots, tell time and date, "
                "check your location, and answer simple commands."
            )
            self.speak_and_reply(response)
            return response

        # Open apps
        if "open" in command:
            if "notepad" in command:
                response = self.desktop.open_app("notepad")
                self.speak_and_reply(response)
                return response

            if "calculator" in command:
                response = self.desktop.open_app("calculator")
                self.speak_and_reply(response)
                return response

            if "vscode" in command or "visual studio code" in command:
                response = self.desktop.open_app("vscode")
                self.speak_and_reply(response)
                return response

            if "browser" in command or "chrome" in command:
                response = self.desktop.open_app("browser")
                self.speak_and_reply(response)
                return response

            if "youtube" in command:
                response = self.browser.open_youtube()
                self.speak_and_reply(response)
                return response

            if "whatsapp" in command:
                response = self.browser.open_whatsapp_web()
                self.speak_and_reply(response)
                return response

        # Search
        if "search for" in command or "search" in command:
            query = command
            if "search for" in query:
                query = query.replace("search for", "", 1).strip()
            elif "search" in query:
                query = query.replace("search", "", 1).strip()

            if not query:
                response = "What do you want me to search for?"
                self.speak_and_reply(response)
                return response

            response = self.browser.search_google(query)
            self.speak_and_reply(response)
            return response

        # Direct URL open
        if "http://" in command or "https://" in command:
            url_match = re.search(r"https?://\\S+", command)
            if url_match:
                response = self.browser.open_url(url_match.group(0))
                self.speak_and_reply(response)
                return response

        # Screenshot
        if "screenshot" in command:
            response = self.desktop.take_screenshot()
            self.speak_and_reply(response)
            return response

        # Lock screen
        if "lock" in command and "screen" in command:
            response = self.desktop.lock_screen()
            self.speak_and_reply(response)
            return response

        # Shutdown
        if "shutdown" in command:
            response = self.desktop.shutdown()
            self.speak_and_reply(response)
            return response

        # Time
        if "time" in command:
            response = "The current time is " + self.desktop.current_time()
            self.speak_and_reply(response)
            return response

        # Date
        if "date" in command:
            response = "Today is " + self.desktop.current_date()
            self.speak_and_reply(response)
            return response

        # Location
        if "location" in command or "where am i" in command:
            response = self.desktop.get_location()
            self.speak_and_reply(response)
            return response

        # System info
        if "system info" in command or "cpu" in command or "memory" in command:
            info = self.desktop.get_system_info()
            response = (
                f"CPU usage: {info.get('cpu')}%, "
                f"Memory usage: {info.get('memory_percent')}%"
            )
            self.speak_and_reply(response)
            return response

        # General friendly answer
        response = (
            "I understand your request. I can help with app control, "
            "search, browser tasks, system actions, and friendly conversation."
        )
        self.speak_and_reply(response)
        return response
