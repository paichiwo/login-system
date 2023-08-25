import sqlite3

import customtkinter as ctk
from tkinter import BOTTOM
from src.app_window import AppWindow
from src.helpers import center_window, is_valid_email, create_user, is_valid_password


class LoginApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window setup

        self.title("Login Window")
        center_window(self, 300, 500)

        # UI elements

        self.root_label = ctk.CTkLabel(
            self,
            text="pyPETS",
            font=("Any", 26, "bold"))
        self.root_label.pack(pady=20)

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True)

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
            command=self.signup)
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
                app.mainloop()
            else:
                self.message_label.configure(text="Wrong credentials")
        else:
            self.message_label.configure(text="Enter valid email address and password", text_color="grey")

    def signup(self):
        """Sign Up button callback"""
        self.destroy()
        signup_window = SignUpWindow()
        signup_window.mainloop()


class SignUpWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window setup

        self.title("Sign Up Window")
        center_window(self, 300, 500)

        # UI Elements

        self.root_label = ctk.CTkLabel(
            self,
            text="pyPETS",
            font=("Any", 26, "bold"))
        self.root_label.pack(pady=20)

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True)

        self.frame_top_label = ctk.CTkLabel(
            master=self.frame,
            text='Sign up')
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

        self.signup_button = ctk.CTkButton(
            master=self.frame,
            text='Create Account',
            width=200,
            command=self.signup)
        self.signup_button.pack(pady=12, padx=10)

        self.message_label = ctk.CTkLabel(
            self.frame,
            text="Enter email and password",
            text_color="grey")
        self.message_label.pack(pady=12, padx=10)

        self.cancel_button = ctk.CTkButton(
            master=self.frame,
            text='Go Back',
            width=200,
            command=self.cancel)
        self.cancel_button.pack(pady=24, padx=10, side=BOTTOM)

    def signup(self):
        email = self.user_entry.get()
        password = self.user_pass.get()

        if is_valid_email(email):
            if len(password) >= 6:
                if is_valid_password(password):
                    try:
                        create_user(email, password)
                    except sqlite3.Error as error:
                        self.message_label.configure(text=f"SQLite Error: {error}")
                    self.message_label.configure(text="Account created\nYou can now log in")
                else:
                    specials = "!@#$%^&*()-_=+{}[]|:;<>,.?"
                    self.message_label.configure(text=f"Error\nAllowed characters:\n\n(A-Z) (a-z) (0-9)\n{specials}")
            else:
                self.message_label.configure(text="Password must be minimum 6 characters")
        else:
            self.message_label.configure(text="Please enter valid email address")

    def cancel(self):
        self.destroy()
        login_app = LoginApp()
        login_app.mainloop()

    def delete_invalid_password_character(self):
        pass
