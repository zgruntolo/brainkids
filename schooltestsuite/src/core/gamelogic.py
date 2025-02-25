import random
import src.core.chart as chart
from src.core.datamanager import DataManager
from src.core.imagemanager import ImageManager
from src.core.state import State


class GameLogic:
    def __init__(
        self,
        difficulty_levels,
        data_directory,
        image_directory,
        default_chart_path,
        chart_save_path,
        game_ui_callback,
    ):
        # Initialize the game logic with preloaded images and difficulty level
        self.chart_save_path = chart_save_path
        self.current_image_category = None
        self.data_directory = data_directory
        self.default_chart_path = default_chart_path
        self.selected_difficulty = 0
        self.difficulty_levels = difficulty_levels
        self.image_directory = image_directory
        self.preloaded_images = {}
        self.game_state = State()
        self.game_ui_callback = game_ui_callback

    def start_game(self):
        # Start the chosen game
        self.game_ui_callback("request_player_name")

    def assign_player_name(self, player_name):
        # Assign username
        if player_name == "":
            player_name = "Primaria Vamba"
        self.game_state.avatar_name = player_name
        self.game_ui_callback("request_game_difficulty", self.difficulty_levels.keys())

    def set_game_difficulty(self, difficulty_name):
        # Assign difficulty
        self.selected_difficulty = self.difficulty_levels[difficulty_name]
        self.load_game_data()
        self.game_ui_callback("display_answers_button", self.game_state.category.keys())
        self.display_next_image()

    def load_game_data(self):
        # Select and import images based on difficulty level
        data_manager = DataManager()
        data_manager.load(self.data_directory)

        image_manager = ImageManager(self.image_directory, data_manager)
        selected_images = image_manager.select_images(self.selected_difficulty)
        self.preloaded_images = image_manager.preload_images(selected_images)

        self.game_state.category = {
            category: 0 for category in self.preloaded_images.keys()
        }
        chart.load(self.default_chart_path, self.chart_save_path)

    def display_next_image(self):
        # Choose the next image and handle if you finish all the image of a key
        available_categories = [
            category
            for category, shown_count in self.game_state.category.items()
            if shown_count < self.selected_difficulty
        ]
        if not available_categories:
            self.end_game()
            return

        self.current_image_category = random.choice(available_categories)
        current_image_index = self.game_state.category[self.current_image_category]

        next_image = self.preloaded_images[self.current_image_category][
            current_image_index
        ]
        self.game_ui_callback("display_image", next_image)

        self.game_state.category[self.current_image_category] += 1

    def verify_player_answer(self, player_answer):
        # Verify if the player's answer is correct or incorrect
        if player_answer == self.current_image_category:
            self.game_state.avatar_score += 10
            self.game_ui_callback("show_correct_answer_message")
        else:
            self.game_ui_callback("show_wrong_answer_message")

        self.display_next_image()

    def save_player_score(self):
        # Save the player's score to the leaderboard
        chart.update_chart(self.game_state.avatar_name, self.game_state.avatar_score)
        chart.save(self.chart_save_path)

    def end_game(self):
        # End the game and display the final results
        if self.game_state.avatar_score > 0:
            self.save_player_score()
            self.game_ui_callback("display_game_results", self.game_state.chart)
