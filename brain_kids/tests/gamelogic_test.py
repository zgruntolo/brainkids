import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from src.core.gamelogic import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.mock_ui_callback = Mock()
        self.mock_data_manager = Mock()
        self.mock_image_manager = Mock()
        self.mock_chart = Mock()

        self.difficulty_levels = {"Facile": 5, "Medio": 10, "Difficile": 15}
        self.data_directory = "test_data"
        self.image_directory = "test_images"
        self.default_chart_path = {}
        self.chart_save_path = Path(__file__).parent / "test_data" / "test_chart.json"

        self.game_logic = GameLogic(
            self.difficulty_levels,
            self.data_directory,
            self.image_directory,
            self.default_chart_path,
            self.chart_save_path,
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
        with patch("src.core.gamelogic.DataManager") as MockDataManager, patch(
            "src.core.gamelogic.ImageManager"
        ) as MockImageManager:
            mock_data_manager = MockDataManager.return_value
            mock_image_manager = MockImageManager.return_value
            mock_data_manager.load.return_value = {
                "Vivente": ["pappagallo.png", "colomba.png"]
            }
            mock_image_manager.select_images.return_value = mock_data_manager
            mock_image_manager.preload_images.return_value = {
                "Vivente": ["pappagallo.png", "colomba.png"]
            }

            self.game_logic.set_game_difficulty("Facile")

            self.assertEqual(self.game_logic.selected_difficulty, 5)
            mock_image_manager.select_images.assert_called_once_with(5)
            mock_image_manager.preload_images.assert_called_once()
            self.mock_ui_callback.assert_called()

    def test_load_game_data(self):
        with patch("src.core.gamelogic.DataManager") as mock_data_manager, patch(
            "src.core.gamelogic.ImageManager"
        ) as mock_image_manager:
            mock_data_manager.return_value.load = Mock()
            mock_image_manager.return_value.select_images = Mock(
                return_value={"Vivente": ["pappagallo.png"]}
            )
            mock_image_manager.return_value.preload_images = Mock(
                return_value={"Vivente": ["pappagallo.png"]}
            )

            self.game_logic.load_game_data()
            mock_data_manager.return_value.load.assert_called_once_with(
                self.data_directory
            )
            mock_image_manager.return_value.select_images.assert_called_once_with(
                self.game_logic.selected_difficulty
            )
            mock_image_manager.return_value.preload_images.assert_called_once()

    def test_display_next_image(self):
        self.game_logic.game_state.selected_categories = {
            "Vivente": 0,
            "Non Vivente": 0,
        }
        self.game_logic.selected_difficulty = 1
        self.game_logic.preloaded_images = {
            "Vivente": ["pappagallo.png"],
            "Non Vivente": ["sasso.png"],
        }

        self.game_logic.display_next_image()
        calls = [
            call[0][1]
            for call in self.mock_ui_callback.call_args_list
            if call[0][0] == "display_image"
        ]
        self.assertIn(calls[0], ["pappagallo.png", "sasso.png"])
        self.game_logic.game_state.selected_categories = {
            "Vivente": 1,
            "Non Vivente": 1,
        }
        self.mock_ui_callback.reset_mock()

    def test_verify_player_answer(self):
        self.game_logic.current_image_category = "Vivente"
        self.game_logic.game_state.player_score = 0
        self.game_logic.game_state.selected_categories = {
            "Vivente": 1,
            "Non Vivente": 0,
        }
        self.game_logic.preloaded_images = {
            "Vivente": ["pappagallo.png"],
            "Non Vivente": ["sasso.png"],
        }
        self.game_logic.verify_player_answer("Vivente")

        calls = [call[0][0] for call in self.mock_ui_callback.call_args_list]
        self.assertIn("show_correct_answer_message", calls)
        self.assertEqual(self.game_logic.game_state.player_score, 10)

    def test_check_answer_wrong(self):
        self.game_logic.current_image_category = "Non Vivente"
        self.game_logic.game_state.player_score = 0
        self.game_logic.game_state.selected_categories = {
            "Vivente": 1,
            "Non Vivente": 0,
        }
        self.game_logic.preloaded_images = {
            "Vivente": ["pappagallo.png"],
            "Non Vivente": ["sasso.png"],
        }
        self.game_logic.verify_player_answer("Vivente")

        calls = [call[0][0] for call in self.mock_ui_callback.call_args_list]
        self.assertIn("show_wrong_answer_message", calls)
        self.assertEqual(self.game_logic.game_state.player_score, 0)

    def test_save_score(self):
        with patch("src.core.gamelogic.scoreboard") as mock_chart:
            self.game_logic.game_state.player_name = "Tommaso"
            self.game_logic.game_state.player_score = 50
            self.game_logic.save_player_score()

            mock_chart.update_scoreboard.assert_called_with("Tommaso", 50)
            mock_chart.save.assert_called_with(self.chart_save_path)

    def test_end_game(self):
        with patch("src.core.gamelogic.scoreboard") as mock_chart:
            self.game_logic.game_state.player_name = "Tommaso"
            self.game_logic.game_state.player_score = 50
            self.game_logic.end_game()
            mock_chart.update_scoreboard.assert_called_with("Tommaso", 50)
            self.mock_ui_callback.assert_called_with(
                "display_game_results", self.game_logic.game_state.scoreboard
            )
            APP_FOLDER = Path.home() / "Documents" / "BrainKids"
            APP_FOLDER.rmdir()


if __name__ == "__main__":
    unittest.main()
