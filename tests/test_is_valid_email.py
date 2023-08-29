from src.login_window import is_valid_email
import pytest


def test_valid_emails():

    valid_emails = [
        "test@example.com",
        "user.123@gmail.com",
        "rocky@hotmail.co.uk",
        "info+123@example-domain.net"
    ]

    for email in valid_emails:
        assert is_valid_email(email) is not None


def test_invalid_emails():

    invalid_emails = [
        "invalid_email",
        "user@.com",
        "user@example.",
        "user@domain",
        "user@domain.",
        "@example.com",
        "21343253234"
    ]

    for email in invalid_emails:
        assert is_valid_email(email) is None


def test_mixed_case_email():

    mixed_case_email = "MiXeDcAsE@ExAmPlE.cOm"
    assert is_valid_email(mixed_case_email) is not None


def test_empty_email():

    empty_email = ""
    assert is_valid_email(empty_email) is None


def test_whitespace_email():

    whitespace_email = " "
    assert is_valid_email(whitespace_email) is None


if __name__ == "__main__":
    pytest.main()
