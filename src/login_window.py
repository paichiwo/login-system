import sqlite3

import customtkinter as ctk
from tkinter import BOTTOM
from src.app_window import AppWindow
from src.helpers import center_window, is_valid_email, is_valid_password
from src.helpers import Database


class LoginApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Login Window")
        center_window(self, 300, 500)

        self.frame = None
        self.frame_top_label = None
        self.user_entry = None
        self.user_pass = None
        self.confirm_user_pass = None
        self.login_button = None
        self.remember_me = None
        self.message_label = None
        self.signup_button = None
        self.cancel_button = None

        self.root_label = ctk.CTkLabel(self, text=".PETS", font=("Any", 26, "bold"))
        self.root_label.pack(pady=20)

        self.login_frame()

    def login_frame(self):
        """Create UI elements for the login page"""
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True)

        self.frame_top_label = ctk.CTkLabel(master=self.frame, text='Login')
        self.frame_top_label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Email", width=200)
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*", width=200)
        self.user_pass.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(master=self.frame, text='Login', width=200, command=self.login)
        self.login_button.pack(pady=12, padx=10)

        self.remember_me = ctk.CTkCheckBox(master=self.frame, text='Remember Me')
        self.remember_me.pack(pady=12, padx=10)

        self.message_label = ctk.CTkLabel(self.frame, text="")
        self.message_label.pack(pady=12, padx=10)

        self.signup_button = ctk.CTkButton(master=self.frame, text='Sign Up', width=200, command=self.signup)
        self.signup_button.pack(pady=24, padx=10, side=BOTTOM)

    def signup_frame(self):
        """Create UI elements for the user registration page"""
        if self.frame:
            self.frame.destroy()

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True)

        self.frame_top_label = ctk.CTkLabel(master=self.frame, text='Sign up')
        self.frame_top_label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Email", width=200)
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*", width=200)
        self.user_pass.pack(pady=12, padx=10)

        self.confirm_user_pass = ctk.CTkEntry(master=self.frame, placeholder_text="Confirm Password", show="*", width=200)
        self.confirm_user_pass.pack(pady=12, padx=10)

        self.signup_button = ctk.CTkButton(master=self.frame, text='Create Account', width=200, command=self.create_user)
        self.signup_button.pack(pady=12, padx=10)

        self.message_label = ctk.CTkLabel(self.frame, text="Enter email and password", text_color="grey")
        self.message_label.pack(pady=12, padx=10)

        self.cancel_button = ctk.CTkButton(master=self.frame, text='Go Back', width=200, command=self.cancel)
        self.cancel_button.pack(pady=24, padx=10, side=BOTTOM)

    def login(self):
        """Login button callback"""
        email = self.user_entry.get()
        password = self.user_pass.get()

        if is_valid_email(self.user_entry.get()):
            if Database().validate_user(email, password):
                self.destroy()
                app = AppWindow()
                app.mainloop()
            else:
                self.message_label.configure(text="Wrong credentials")
        else:
            self.message_label.configure(text="Enter valid email address and password", text_color="grey")

    def signup(self):
        """Sign Up button callback"""
        self.signup_frame()

    def create_user(self):
        """Create user in the database"""
        email = self.user_entry.get()
        password = self.user_pass.get()
        password_confirmation = self.confirm_user_pass.get()

        if password == password_confirmation:
            if is_valid_email(email):
                if len(password) >= 6:
                    if is_valid_password(password):
                        try:
                            Database().create_user(email, password)
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
        else:
            self.message_label.configure(text="Passwords don't match")

    def cancel(self):
        self.login_frame()
