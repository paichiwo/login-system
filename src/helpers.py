import os
import re
import sys
import sqlite3


def resource_path(relative_path):
    """Get the absolute path to a resource, accommodating both development and PyInstaller builds"""

    if hasattr(sys, '_MEIPASS'):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


SQL_FILEPATH = resource_path('db\\db.sql')
DB_FILEPATH = resource_path('db\\db.db')


def create_database():
    """Create a new database using an .sql file"""

    if not os.path.exists(DB_FILEPATH) and os.path.exists(SQL_FILEPATH):
        conn = sqlite3.connect(DB_FILEPATH)
        cursor = conn.cursor()

        with open(SQL_FILEPATH, "r", encoding='utf-8') as sql_file:
            sql_commands = sql_file.read()

        cursor.executescript(sql_commands)
        conn.commit()
        conn.close()


def create_user(email, password):
    """Save user data to database"""

    conn = sqlite3.connect(DB_FILEPATH)
    cursor = conn.cursor()

    # SQL INSERT statement
    insert_query = "INSERT INTO user_profile (email, password) VALUES (?, ?);"

    # Execute the INSERT statement
    cursor.execute(insert_query, (email, password))

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()


def center_window(window, width, height):
    """Center a window on the screen using the provided dimensions"""

    # Get the center position
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2

    # Set the window in the center
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.update_idletasks()


def is_valid_email(email):
    """Check for a valid email address format"""

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)


def is_valid_password(password):
    """Check for valid password"""

    password_pattern = re.compile(r'^[a-zA-Z0-9!@#$%^&*()[-]_=+{}|:;<>,.?]+$')
    return re.match(password_pattern, password)
