from src.helpers import is_valid_password
import pytest


def test_valid_passwords():

    valid_passwords = [
        "PasswOrd!",
        "Secret123$",
        "MyP@55-",
        "S3cur3_p@ssw0rd"
    ]

    for password in valid_passwords:
        assert is_valid_password(password) is True


def test_invalid_passwords():
    invalid_passwords = [
        "password/",  # Not allowed characters
        "/|\\/|\\/"  # Only not allowed characters
    ]

    for password in invalid_passwords:
        assert is_valid_password(password) is False


def test_whitespace_password():
    whitespace_password = "   "
    assert is_valid_password(whitespace_password) is False


if __name__ == "__main__":
    pytest.main()
