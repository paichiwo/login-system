import customtkinter as ctk
from tkinter import BOTTOM
from src.app_window import AppWindow
from src.helpers import is_valid_email


class LoginWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window setup

        self.title("Login Window")
        self.geometry("400x500")

        # UI elements

        self.root_label = ctk.CTkLabel(
            self,
            text="pyPETS",
            font=("Any", 26, "bold"))
        self.root_label.pack(pady=20)

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.frame_top_label = ctk.CTkLabel(
            master=self.frame,
            text='Login')
        self.frame_top_label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(
            master=self.frame,
            placeholder_text="Email",
            width=200)
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(
            master=self.frame,
            placeholder_text="Password",
            show="*",
            width=200)
        self.user_pass.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(
            master=self.frame,
            text='Login',
            width=200,
            command=self.login)
        self.login_button.pack(pady=12, padx=10)

        self.remember_me = ctk.CTkCheckBox(
            master=self.frame,
            text='Remember Me')
        self.remember_me.pack(pady=12, padx=10)

        self.message_label = ctk.CTkLabel(self.frame, text="")
        self.message_label.pack(pady=12, padx=10)

        self.signup_button = ctk.CTkButton(
            master=self.frame,
            text='Sign Up',
            width=200,
            command=self.login)
        self.signup_button.pack(pady=24, padx=10, side=BOTTOM)

    def login(self):
        """Login button callback"""

        username = "admin@test.com"
        password = "123"

        # Check if valid email
        if is_valid_email(self.user_entry.get()):

            # If credentials ok destroy login_window and open the app
            if self.user_entry.get() == username and self.user_pass.get() == password:
                self.destroy()
                app = AppWindow()
                app.eval('tk::PlaceWindow . center')
                app.mainloop()
            else:
                self.message_label.configure(text="Wrong credentials")
        else:
            self.message_label.configure(text="Enter valid email address and password", text_color="grey")

    def signup(self):
        """Sign Up button callback"""


