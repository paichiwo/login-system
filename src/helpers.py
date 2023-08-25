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


def create_database(database_path, sql_file_path):
    """Create a new database using an .sql file"""
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    with open(sql_file_path, "r", encoding='utf-8') as sql_file:
        sql_commands = sql_file.read()

    cursor.executescript(sql_commands)
    conn.commit()
    conn.close()


def is_valid_email(email):
    """Check for a valid email address format"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)
