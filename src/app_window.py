import customtkinter as ctk


class AppWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window setup

        self.title("App Window")
        self.geometry("800x600")

        # UI elements

        self.label = ctk.CTkLabel(self, text="Login Successful\nThis is main app window")
        self.label.pack()