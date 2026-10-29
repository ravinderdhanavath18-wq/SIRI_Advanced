import pyttsx3
import speech_recognition as sr

class VoiceEngine:
    def __init__(self):
        self.engine = None
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", 170)
            self.engine.setProperty("volume", 1.0)
            voices = self.engine.getProperty("voices")
            if voices:
                try:
                    self.engine.setProperty("voice", voices[0].id)
                except Exception:
                    pass
        except Exception as e:
            print("Voice engine failed to initialize:", e)

    def speak(self, text: str):
        if not text:
            return
        try:
            if self.engine:
                self.engine.say(text)
                self.engine.runAndWait()
        except Exception as e:
            print("Error speaking:", e)

    def listen_once(self, language="en-IN"):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            try:
                text = recognizer.recognize_google(audio, language=language)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                print("Could not understand voice.")
                return ""
            except sr.RequestError:
                print("Speech recognition service unavailable.")
                return ""
        except Exception as e:
            print("Microphone error:", e)
            return ""
