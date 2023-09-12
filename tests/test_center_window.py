import pytest
from unittest.mock import Mock
from src.helpers import center_window


class TestCenterWindow:
    @pytest.fixture
    def mock_window(self):
        return Mock()

    def test_center_window(self, mock_window):
        mock_window.winfo_screenwidth.return_value = 1920
        mock_window.winfo_screenheight.return_value = 1080

        center_window(mock_window, 800, 600)

        mock_window.geometry.assert_called_with("800x600+560+240")
        mock_window.update_idletasks.assert_called_once()

    def test_center_window_odd_dimensions(self, mock_window):
        mock_window.winfo_screenwidth.return_value = 1920
        mock_window.winfo_screenheight.return_value = 1080

        center_window(mock_window, 801, 601)

        mock_window.geometry.assert_called_with("801x601+559+239")
        mock_window.update_idletasks.assert_called_once()


if __name__ == "__main__":
    pytest.main()
