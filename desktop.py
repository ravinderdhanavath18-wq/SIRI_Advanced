import os
import subprocess
import platform
import webbrowser
import pyautogui
import requests
import psutil
from datetime import datetime

class DesktopController:
    def __init__(self):
        self.system = platform.system().lower()

    def open_app(self, app_name: str):
        app_name = app_name.lower().strip()

        if not app_name:
            return "Which app should I open?"

        if "notepad" in app_name:
            try:
                if self.system == "windows":
                    os.startfile("notepad.exe")
                else:
                    subprocess.Popen(["notepad"])
                return "Opening Notepad."
            except Exception:
                return "Notepad is not available."

        if "calculator" in app_name:
            try:
                if self.system == "windows":
                    os.startfile("calc.exe")
                else:
                    subprocess.Popen(["gnome-calculator"])
                return "Opening Calculator."
            except Exception:
                return "Calculator is not available."

        if "vscode" in app_name or "visual studio code" in app_name:
            try:
                if self.system == "windows":
                    os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
                else:
                    subprocess.Popen(["code"])
                return "Opening VS Code."
            except Exception:
                return "VS Code is not installed or not set in PATH."

        if "browser" in app_name or "chrome" in app_name:
            webbrowser.open("https://www.google.com")
            return "Opening your browser."

        if "whatsapp" in app_name:
            webbrowser.open("https://web.whatsapp.com")
            return "Opening WhatsApp Web."

        if "youtube" in app_name:
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube."

        return f"I cannot open '{app_name}' from this system."

    def take_screenshot(self):
        try:
            screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
            pyautogui.screenshot(screenshot_path)
            return f"Screenshot saved at: {screenshot_path}"
        except Exception:
            return "Screenshot failed."

    def lock_screen(self):
        if self.system == "windows":
            try:
                os.system("rundll32.exe user32.dll,LockWorkStation")
                return "Locking the screen."
            except Exception:
                return "Lock screen command failed."
        else:
            return "Lock screen command is not supported on this OS."

    def shutdown(self):
        if self.system == "windows":
            os.system("shutdown /s /t 1")
            return "Shutting down the system."
        else:
            return "Shutdown is not supported on this OS."

    def get_system_info(self):
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            data = {
                "cpu": cpu_percent,
                "memory_used": memory.used,
                "memory_total": memory.total,
                "memory_percent": memory.percent
            }
            return data
        except Exception:
            return {"cpu": "unknown", "memory_percent": "unknown"}

    def get_location(self):
        try:
            response = requests.get("https://ipapi.co/json/", timeout=8)
            if response.status_code == 200:
                data = response.json()
                city = data.get("city", "Unknown city")
                region = data.get("region", "Unknown region")
                country = data.get("country_name", "Unknown country")
                return f"Location: {city}, {region}, {country}"
            return "Location not available."
        except Exception:
            return "Unable to fetch location."

    def current_time(self):
        now = datetime.now()
        return now.strftime("%I:%M %p")

    def current_date(self):
        now = datetime.now()
        return now.strftime("%A, %d %B %Y")
