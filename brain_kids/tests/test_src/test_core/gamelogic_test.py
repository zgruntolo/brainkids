import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from core.gamelogic import GameLogic
from PIL import Image


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        ABSOLUTE_PATH = Path(__file__).parent.parent.parent / "test_data" / "test"
        self.difficulty_levels = {"Facile": 1}
        self.data_directory = ABSOLUTE_PATH / "files" / "images.json"
        self.image_directory = ABSOLUTE_PATH / "images"
        self.default_chart_path = ABSOLUTE_PATH / "files" / "chart.json"
        self.default_chart_filename = "chart.json"

        self.mock_ui_callback = Mock()
        self.mock_chart = Mock()

        self.game_logic = GameLogic(
            self.difficulty_levels,
            self.data_directory,
            self.image_directory,
            self.default_chart_path,
            self.default_chart_filename,
            self.mock_ui_callback,
        )

    def test_start_game(self):
        self.game_logic.start_game()
        self.mock_ui_callback.assert_called_once_with("request_player_name")

    def test_assign_player_name(self):
        self.game_logic.assign_player_name("Tommaso")
        self.assertEqual(self.game_logic.game_state.player_name, "Tommaso")
        self.mock_ui_callback.assert_called_once_with(
            "request_game_difficulty", self.difficulty_levels.keys()
        )

    def test_set_game_difficulty(self):
        self.game_logic.set_game_difficulty("Facile")
        self.assertEqual(self.game_logic.selected_difficulty, 1)
        self.assertEqual(
            self.game_logic.game_state.selected_categories.keys(),
            {"Viventi", "Non Viventi"},
        )
        called_images = [
            call[0][1]
            for call in self.mock_ui_callback.call_args_list
            if call[0][0] == "display_image"
        ]
        expected_images = [
            self.game_logic.preloaded_images["Viventi"][0],
            self.game_logic.preloaded_images["Non Viventi"][0],
        ]
        self.assertTrue(any(img in expected_images for img in called_images))

    def test_load_game_data(self):
        self.game_logic.load_game_data()
        self.assertEqual(len(self.game_logic.preloaded_images), 2)
        for img in self.game_logic.preloaded_images.get("Viventi", "Non Viventi"):
            self.assertIsInstance(img, Image.Image)
        self.assertEqual(self.game_logic.game_state.scoreboard, [["Tommaso", 10]])

    def test_display_next_image(self):
        self.game_logic.set_game_difficulty("Facile")
        self.game_logic.display_next_image()
        self.assertIn(
            "display_image",
            [call[0][0] for call in self.mock_ui_callback.call_args_list],
        )
        self.game_logic.game_state.selected_categories = {
            "Vivente": 1,
            "Non Vivente": 1,
        }

    def test_verify_player_answer(self):
        self.game_logic.set_game_difficulty("Facile")
        self.game_logic.current_image_category = "Vivente"

        self.game_logic.game_state.player_score = 0
        self.game_logic.verify_player_answer("Vivente")
        self.mock_ui_callback.assert_any_call("show_correct_answer_message")
        self.assertEqual(self.game_logic.game_state.player_score, 10)

        self.game_logic.game_state.player_score = 0
        self.game_logic.verify_player_answer("Non Vivente")
        self.mock_ui_callback.assert_any_call("show_wrong_answer_message")
        self.assertEqual(self.game_logic.game_state.player_score, 0)

    def test_save_score(self):
        with patch("core.gamelogic.scoreboard") as mock_chart:
            self.game_logic.game_state.player_name = "Tommaso"
            self.game_logic.game_state.player_score = 50
            self.game_logic.save_player_score()

            mock_chart.update_scoreboard.assert_called_with("Tommaso", 50)
            mock_chart.save.assert_called_with(self.default_chart_filename)
            self.game_logic.game_state.scoreboard = []

    def test_end_game(self):
        self.game_logic.game_state.player_name = "Tommaso"
        self.game_logic.game_state.player_score = 50
        self.game_logic.end_game()
        self.mock_ui_callback.assert_called_with(
            "display_game_results", self.game_logic.game_state.scoreboard
        )
        self.game_logic.game_state.scoreboard = []
        save_path = Path.home() / "Documents" / "BrainKids"
        for file in save_path.iterdir():
            file.unlink()
        save_path.rmdir()


if __name__ == "__main__":
    unittest.main()
