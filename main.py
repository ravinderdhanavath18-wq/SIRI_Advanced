import customtkinter as ctk
from app.assistant import SiriAssistant

class SiriWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SIRI Advanced")
        self.geometry("450x700")
        self.configure(fg_color="#0d1220")
        self.minsize(420, 600)

        # Make it always on top
        self.attributes("-topmost", True)

        # Top title
        self.title_label = ctk.CTkLabel(
            self,
            text="SIRI",
            font=("Segoe UI", 30, "bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(pady=(20, 5))

        # Anime-style circle avatar
        self.avatar_frame = ctk.CTkFrame(
            self,
            width=220,
            height=220,
            corner_radius=110,
            fg_color="#1e2a3a"
        )
        self.avatar_frame.pack(pady=10)

        # Use a simple face-like drawing with labels
        self.face = ctk.CTkLabel(
            self.avatar_frame,
            text="◕‿◕",
            font=("Segoe UI Emoji", 42, "bold"),
            text_color="#f8d7da"
        )
        self.face.place(relx=0.5, rely=0.5, anchor="center")

        # Text area
        self.chat_box = ctk.CTkTextbox(
            self,
            width=380,
            height=180,
            fg_color="#101827",
            text_color="#f3f4f6",
            border_color="#2f4961",
            corner_radius=18,
            font=("Segoe UI", 13)
        )
        self.chat_box.pack(pady=10)
        self.chat_box.insert("0.0", "Hi! I am SIRI.\n")
        self.chat_box.configure(state="disabled")

        # Input box
        self.command_entry = ctk.CTkEntry(
            self,
            width=340,
            height=40,
            placeholder_text="Type your command here...",
            border_color="#5eead4",
            font=("Segoe UI", 14)
        )
        self.command_entry.pack(pady=(5, 10))

        # Buttons
        self.ask_button = ctk.CTkButton(
            self,
            text="Ask SIRI",
            width=180,
            height=42,
            command=self.ask_command,
            fg_color="#10b981",
            hover_color="#059669",
            font=("Segoe UI", 14, "bold"),
            corner_radius=14
        )
        self.ask_button.pack(pady=(5, 8))

        self.listen_button = ctk.CTkButton(
            self,
            text="Listen",
            width=180,
            height=42,
            command=self.listen_and_run,
            fg_color="#3b82f6",
            hover_color="#2563eb",
            font=("Segoe UI", 14, "bold"),
            corner_radius=14
        )
        self.listen_button.pack(pady=(0, 10))

        self.assistant = SiriAssistant(self.update_chat)

    def update_chat(self, message: str):
        self.chat_box.configure(state="normal")
        self.chat_box.insert("0.0", message + "\n")
        self.chat_box.configure(state="disabled")

    def ask_command(self):
        text = self.command_entry.get().strip()
        if not text:
            return
        self.command_entry.delete(0, "end")
        self.update_chat("You: " + text)
        response = self.assistant.handle_command(text)
        self.update_chat("SIRI: " + response)

    def listen_and_run(self):
        try:
            from app.voice import VoiceEngine
            voice = VoiceEngine()
            command = voice.listen_once("en-IN")
            if not command:
                self.update_chat("SIRI: I could not hear you clearly.")
                return
            self.command_entry.delete(0, "end")
            self.command_entry.insert(0, command)
            self.ask_command()
        except Exception as e:
            self.update_chat("SIRI: Voice input failed. " + str(e))

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = SiriWindow()
    app.mainloop()
