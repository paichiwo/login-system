import customtkinter as ctk
from src.helpers import center_window


class SignUpWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window setup

        self.title("Sign Up Window")
        center_window(self, 400, 500)
