from src.helpers import Database
from src.login_window import LoginApp


def main():
    """Initialize database and create a login window"""

    Database().create_db()

    login_app = LoginApp()
    login_app.mainloop()


if __name__ == "__main__":
    main()

