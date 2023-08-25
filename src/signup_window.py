import customtkinter as ctk


class SignUpWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window setup

        self.title("Sign Up Window")
        self.geometry("400x500")
