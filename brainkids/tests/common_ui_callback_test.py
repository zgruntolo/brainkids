from unittest.mock import MagicMock
from src.core.common_ui_callback import create_game_ui_callback
import unittest

chart = [["Ilary", 30], ["Tommaso", 20], ["Giovanni", 10]]


class TestUICallback(unittest.TestCase):
    def setUp(self):
        self.game_logic = MagicMock()
        self.renderer = MagicMock()
        self.ui_callback = create_game_ui_callback(self.game_logic, self.renderer)

    def test_request_name(self):
        self.ui_callback("request_player_name")
        self.renderer.request_player_name.assert_called_once()

    def test_assign_player_name(self):
        self.ui_callback("assign_player_name", "Tommaso")
        self.game_logic.assign_player_name.assert_called_once_with("Tommaso")

    def test_request_game_difficulty(self):
        self.ui_callback("request_game_difficulty", "Facile", "Medio", "Difficile")
        self.renderer.request_game_difficulty.assert_called_once_with(
            "Facile", "Medio", "Difficile"
        )

    def test_set_game_difficulty(self):
        self.ui_callback("set_game_difficulty", "Facile")
        self.game_logic.set_game_difficulty.assert_called_once_with("Facile")

    def test_display_answers_button(self):
        self.ui_callback("display_answers_button", ["Vivente", "Non Vivente"])
        self.renderer.display_answers_button.assert_called_once_with(
            ["Vivente", "Non Vivente"]
        )

    def test_display_image(self):
        self.ui_callback(
            "display_image",
            "<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=300x300 at 0x103A05A70>",
        )
        self.renderer.display_image.assert_called_once_with(
            "<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=300x300 at 0x103A05A70>"
        )

    def test_verify_player_answer(self):
        self.ui_callback("verify_player_answer", "Vivente")
        self.game_logic.verify_player_answer.assert_called_once_with("Vivente")

    def test_show_correct_answer_message(self):
        self.ui_callback("show_correct_answer_message")
        self.renderer.show_correct_answer_message.assert_called_once()

    def test_show_wrong_answer_message(self):
        self.ui_callback("show_wrong_answer_message")
        self.renderer.show_wrong_answer_message.assert_called_once()

    def test_display_game_results(self):
        self.ui_callback("display_game_results", chart)
        self.renderer.display_game_results.assert_called_once_with(chart)


if __name__ == "__main__":
    unittest.main()
