import os
import re
import sys
import string
import sqlite3


def resource_path(relative_path):
    """Get the absolute path to a resource, accommodating both development and PyInstaller builds"""

    if hasattr(sys, '_MEIPASS'):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


class Database:
    """Database manipulation methods"""
    def __init__(self):
        self.SQL_FILEPATH = resource_path('db/db.sql')
        self.DB_FILEPATH = resource_path('db/db.db')

        self.conn = sqlite3.connect(self.DB_FILEPATH)
        self.cursor = self.conn.cursor()

    def create_db(self):
        """Create a new database using an .sql file"""
        with open(self.SQL_FILEPATH, "r", encoding='utf-8') as sql_file:
            sql_commands = sql_file.read()
        try:
            self.cursor.executescript(sql_commands)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def create_user(self, email, password):
        """Save user data to database"""
        insert_query = "INSERT INTO user_profile (email, password) VALUES (?, ?);"
        self.cursor.execute(insert_query, (email, password))
        self.conn.commit()

    def validate_user(self, email, password):
        """Validate user credentials"""
        select_query = "SELECT * FROM user_profile WHERE email = ? AND password = ?;"
        self.cursor.execute(select_query, (email, password))
        user_data = self.cursor.fetchone()
        if user_data:
            return True
        else:
            return False

    def close_db(self):
        """Close the database connection"""
        self.conn.close()


def center_window(window, width, height):
    """Center a window on the screen using the provided dimensions"""
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")
    window.update_idletasks()


def is_valid_email(email):
    """Check for a valid email address format"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)


def is_valid_password(password):
    """Check for valid password"""
    password_pattern = string.ascii_letters + string.digits + "!@#$&-_"
    for letter in password:
        if letter not in password_pattern:
            return False
    return True
