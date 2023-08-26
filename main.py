import os.path
from src.helpers import Database
from src.login_window import LoginApp


def main():
    """Initialize database and create a login window"""
    if not os.path.exists('./db/db.db'):
        Database().create_db()
        Database().close_db()
        print("database created")
    else:
        print("database exists, proceeding...")
    login_app = LoginApp()
    login_app.mainloop()


if __name__ == "__main__":
    main()

