import core.scoreboard as scoreboard
import random
from core.datamanager import DataManager
from core.gamestate import State
from core.imagemanager import ImageManager


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
        # Initialize game logic with difficulty levels, data directories, and image directories
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
        # Start the game by requesting the player's name
        self.game_ui_callback("request_player_name")

    def assign_player_name(self, player_name):
        # Set the player's name, assigning a default if none is provided
        if player_name == "":
            player_name = "Giocatore 1"
        self.game_state.player_name = player_name
        self.game_ui_callback("request_game_difficulty", self.difficulty_levels.keys())

    def set_game_difficulty(self, difficulty_name):
        # Set the chosen difficulty level, load game data, and display answer buttons
        self.selected_difficulty = self.difficulty_levels[difficulty_name]
        self.load_game_data()
        self.game_ui_callback(
            "display_answers_button", self.game_state.selected_categories.keys()
        )
        self.display_next_image()

    def load_game_data(self):
        # Load data and select images based on the chosen difficulty level
        data_manager = DataManager()
        data_manager.load(self.data_directory)

        image_manager = ImageManager(self.image_directory, data_manager)
        selected_images = image_manager.select_images(self.selected_difficulty)
        self.preloaded_images = image_manager.preload_images(selected_images)

        # Initialize the count of displayed images for each category
        self.game_state.selected_categories = {
            category: 0 for category in self.preloaded_images.keys()
        }
        scoreboard.load(self.default_chart_path, self.chart_save_path)

    def display_next_image(self):
        # Select and display the next image. If all images have been shown, end the game
        available_categories = [
            category
            for category, shown_count in self.game_state.selected_categories.items()
            if shown_count < self.selected_difficulty
        ]
        if not available_categories:
            self.end_game()
            return

        self.current_image_category = random.choice(available_categories)
        current_image_index = self.game_state.selected_categories[
            self.current_image_category
        ]

        next_image = self.preloaded_images[self.current_image_category][
            current_image_index
        ]
        self.game_ui_callback("display_image", next_image)

        # Update the count of displayed images for the selected category
        self.game_state.selected_categories[self.current_image_category] += 1

    def verify_player_answer(self, player_answer):
        # VCheck if the player's answer is correct and update the score accordingly
        if player_answer == self.current_image_category:
            self.game_state.player_score += 10
            self.game_ui_callback("show_correct_answer_message")
        else:
            self.game_ui_callback("show_wrong_answer_message")

        self.display_next_image()

    def save_player_score(self):
        # Save the player's score to the scoreboard
        scoreboard.update_scoreboard(
            self.game_state.player_name, self.game_state.player_score
        )
        scoreboard.save(self.chart_save_path)

    def end_game(self):
        # End the game, save the score if it's greater than zero, and display the final leaderboard
        if self.game_state.player_score > 0:
            self.save_player_score()
            self.game_ui_callback("display_game_results", self.game_state.scoreboard)
