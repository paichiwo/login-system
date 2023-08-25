import customtkinter as ctk
from src.helpers import center_window


class AppWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window setup

        self.title("App Window")
        center_window(self, 800, 600)

        # UI elements

        self.label = ctk.CTkLabel(self, text="Login Successful\nThis is main app window")
        self.label.pack(pady=12, padx=10)
