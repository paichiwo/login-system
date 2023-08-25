from src.helpers import create_database
from src.login_window import LoginApp

# finish login func
# fix id incrementation in db


def main():
    """Initialize database and create a login window"""

    create_database()

    login_app = LoginApp()
    login_app.mainloop()


if __name__ == "__main__":
    main()

