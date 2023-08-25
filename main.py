from src.helpers import create_database
from src.login_window import LoginWindow


def main():
    """Initialize database and create a login window"""

    create_database()

    login_window = LoginWindow()
    login_window.mainloop()


if __name__ == "__main__":
    main()

