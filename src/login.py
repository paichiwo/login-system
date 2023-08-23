import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

root = ctk.CTk()
root.geometry("400x600")
root.title("Login Page")


def login():
    username = "admin"
    password = "123"
    new_window = ctk.CTkToplevel(root)
    new_window.title("New window")
    new_window.geometry("350x150")

    if user_entry.get() == username and user_pass.get() == password:
        messagebox.showinfo(title="Login Successful", message="You have logged in")


user_entry = ctk.CTkEntry(root, border_width=0)
user_entry.pack()



root.mainloop()