from unittest.mock import MagicMock
from src.core.common_ui_callback import create_ui_callback
import unittest

chart = [["Ilary", 30], ["Tommaso", 20], ["Giovanni", 10]]


class TestUICallback(unittest.TestCase):
    def setUp(self):
        self.game_logic = MagicMock()
        self.renderer = MagicMock()
        self.ui_callback = create_ui_callback(self.game_logic, self.renderer)

    def test_get_name(self):
        self.ui_callback("get_name")
        self.renderer.get_name.assert_called_once()

    def test_assign_username(self):
        self.ui_callback("assign_username", "Tommaso")
        self.game_logic.assign_username.assert_called_once_with("Tommaso")

    def test_get_difficulty(self):
        self.ui_callback("get_difficulty", "Facile", "Medio", "Difficile")
        self.renderer.get_difficulty.assert_called_once_with(
            "Facile", "Medio", "Difficile"
        )

    def test_assign_difficulty(self):
        self.ui_callback("assign_difficulty", "Facile")
        self.game_logic.assign_difficulty.assert_called_once_with("Facile")

    def test_setup_ui(self):
        self.ui_callback("setup_ui", "Vivente", "Non Vivente")
        self.renderer.setup_gui_images.assert_called_once()
        self.renderer.create_buttons.assert_called_once_with("Vivente", "Non Vivente")

    def test_show_image(self):
        self.ui_callback(
            "show_image",
            "<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=300x300 at 0x103A05A70>",
        )
        self.renderer.next_image.assert_called_once_with(
            "<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=300x300 at 0x103A05A70>"
        )

    def test_check_answer(self):
        self.ui_callback("check_answer", "Vivente")
        self.game_logic.check_answer.assert_called_once_with("Vivente")

    def test_correct_answer(self):
        self.ui_callback("correct_answer")
        self.renderer.correct_answer.assert_called_once()

    def test_wrong_answer(self):
        self.ui_callback("wrong_answer")
        self.renderer.wrong_answer.assert_called_once()

    def test_end_game(self):
        self.ui_callback("end_game", chart)
        self.renderer.end_game.assert_called_once_with(chart)


if __name__ == "__main__":
    unittest.main()
