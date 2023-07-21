import sqlite3


def create_database(database_path, sql_file_path):
    """Create a new database using an .sql file"""
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    with open(sql_file_path, "r", encoding='utf-8') as sql_file:
        sql_commands = sql_file.read()

    cursor.executescript(sql_commands)
    conn.commit()
    conn.close()
    print("New database created successfully.")
