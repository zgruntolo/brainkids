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

        self.difficulty_ranks = {"Facile": 5, "Medio": 10, "Difficile": 15}
        self.data_dir = "test_data"
        self.image_dir = "test_images"
        self.default_chart = {}
        self.chart_filename = Path(__file__).parent / "test_data" / "test_chart.json"

        self.game_logic = GameLogic(
            self.difficulty_ranks,
            self.data_dir,
            self.image_dir,
            self.default_chart,
            self.chart_filename,
            self.mock_ui_callback,
        )

    def test_start_game(self):
        self.game_logic.start_game()
        self.mock_ui_callback.assert_called_once_with("get_name")

    def test_assign_username(self):
        self.game_logic.assign_username("Tommaso")
        self.assertEqual(self.game_logic.state.avatar_name, "Tommaso")
        self.mock_ui_callback.assert_called_once_with(
            "get_difficulty", self.difficulty_ranks.keys()
        )

    def test_assign_difficulty(self):
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

            self.game_logic.assign_difficulty("Facile")

            self.assertEqual(self.game_logic.difficulty, 5)
            mock_image_manager.select_images.assert_called_once_with(5)
            mock_image_manager.preload_images.assert_called_once()
            self.mock_ui_callback.assert_called()

    def test_initialize_state(self):
        self.game_logic.preloaded_images = {
            "Vivente": ["pappagallo.png"],
            "Non Vivente": ["sasso.png"],
        }
        self.game_logic._initialize_state()
        self.assertEqual(
            self.game_logic.state.category, {"Vivente": 0, "Non Vivente": 0}
        )

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
            mock_data_manager.return_value.load.assert_called_once_with(self.data_dir)
            mock_image_manager.return_value.select_images.assert_called_once_with(
                self.game_logic.difficulty
            )
            mock_image_manager.return_value.preload_images.assert_called_once()

    def test_show_next_image(self):
        self.game_logic.state.category = {"Vivente": 0, "Non Vivente": 0}
        self.game_logic.difficulty = 1
        self.game_logic.preloaded_images = {
            "Vivente": ["pappagallo.png"],
            "Non Vivente": ["sasso.png"],
        }

        self.game_logic.show_next_image()
        calls = [
            call[0][1]
            for call in self.mock_ui_callback.call_args_list
            if call[0][0] == "show_image"
        ]
        self.assertIn(calls[0], ["pappagallo.png", "sasso.png"])
        self.game_logic.state.category = {"Vivente": 1, "Non Vivente": 1}
        self.mock_ui_callback.reset_mock()
        self.game_logic.show_next_image()
        self.mock_ui_callback.assert_called_with(
            "end_game", self.game_logic.state.chart
        )

    def test_check_answer_correct(self):
        self.game_logic.current_category = "Vivente"
        self.game_logic.state.avatar_score = 0
        self.game_logic.state.category = {"Vivente": 1, "Non Vivente": 0}
        self.game_logic.preloaded_images = {
            "Vivente": ["pappagallo.png"],
            "Non Vivente": ["sasso.png"],
        }
        self.game_logic.check_answer("Vivente")

        calls = [call[0][0] for call in self.mock_ui_callback.call_args_list]
        self.assertIn("correct_answer", calls)
        self.assertEqual(self.game_logic.state.avatar_score, 10)

    def test_check_answer_wrong(self):
        self.game_logic.current_category = "Non Vivente"
        self.game_logic.state.avatar_score = 0
        self.game_logic.state.category = {"Vivente": 1, "Non Vivente": 0}
        self.game_logic.preloaded_images = {
            "Vivente": ["pappagallo.png"],
            "Non Vivente": ["sasso.png"],
        }
        self.game_logic.check_answer("Vivente")

        calls = [call[0][0] for call in self.mock_ui_callback.call_args_list]
        self.assertIn("wrong_answer", calls)
        self.assertEqual(self.game_logic.state.avatar_score, 0)

    def test_save_score(self):
        with patch("src.core.gamelogic.chart") as mock_chart:
            self.game_logic.state.avatar_name = "Tommaso"
            self.game_logic.state.avatar_score = 50
            self.game_logic.save_score()

            mock_chart.update_chart.assert_called_with("Tommaso", 50)
            mock_chart.save.assert_called_with(self.chart_filename)

    def test_end_game(self):
        with patch("src.core.gamelogic.chart") as mock_chart:
            self.game_logic.end_game()
            mock_chart.update_chart.assert_called_with(
                self.game_logic.state.avatar_name, self.game_logic.state.avatar_score
            )
            mock_chart.save.assert_called_with(self.chart_filename)
            self.mock_ui_callback.assert_called_with(
                "end_game", self.game_logic.state.chart
            )
            APP_FOLDER = Path.home() / "Documents" / "Schooltestsuite"
            APP_FOLDER.rmdir()


if __name__ == "__main__":
    unittest.main()
