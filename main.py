import os
from src.helpers import create_database
from src.config import SQL_FILEPATH, DB_FILEPATH
from src.login_window import LoginWindow


def main():
    """Initialize database and create a login window"""

    # Initialize database
    if not os.path.exists(DB_FILEPATH) and os.path.exists(SQL_FILEPATH):
        create_database(DB_FILEPATH, SQL_FILEPATH)
        print("New database successfully created")
    else:
        print("Database exists")

    # Create a login window
    login_window = LoginWindow()
    login_window.eval('tk::PlaceWindow . center')
    login_window.mainloop()


if __name__ == "__main__":
    main()

