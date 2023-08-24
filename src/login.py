import customtkinter as ctk
from tkinter import messagebox


def login_window():
    """Create a login window using CTK"""
    root = ctk.CTk()
    root.geometry("400x600+400+100")
    root.title("Login Page")

    def login():
        """Login button callback"""
        username = "admin"
        password = "123"

        if user_entry.get() == username and user_pass.get() == password:
            messagebox.showinfo(title="Login Successful", message="You have logged in")
        else:
            messagebox.showerror(title="Login Failed", message="Invalid credentials")

    # Create UI elements
    label = ctk.CTkLabel(root, text="Pet Health Tracker Logo")
    label.pack(pady=20)

    # Frame and its contents
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    label = ctk.CTkLabel(master=frame, text='Login frame')
    label.pack(pady=12, padx=10)

    user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
    user_entry.pack(pady=12, padx=10)

    user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    user_pass.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text='Login', command=login)
    button.pack(pady=12, padx=10)

    checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
    checkbox.pack(pady=12, padx=10)

    root.mainloop()
