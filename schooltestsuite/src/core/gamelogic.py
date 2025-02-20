import random
import src.core.chart as chart
from src.core.datamanager import DataManager
from src.core.imagemanager import ImageManager
from src.core.state import State


class GameLogic:
    def __init__(
        self,
        difficulty_ranks,
        data_dir,
        image_dir,
        default_chart,
        chart_filename,
        ui_callback,
    ):
        # Initialize the game logic with preloaded images and difficulty level
        self.chart_filename = chart_filename
        self.current_category = None
        self.data_dir = data_dir
        self.default_chart = default_chart
        self.difficulty = 0
        self.difficulty_ranks = difficulty_ranks
        self.image_dir = image_dir
        self.preloaded_images = {}
        self.state = State()
        self.ui_callback = ui_callback

    def start_game(self):
        # Start the chosen game
        self.ui_callback("request_player_name")

    def assign_username(self, name):
        # Assign username
        if name == "":
            name = "Primaria Vamba"
        self.state.avatar_name = name
        self.ui_callback("request_game_difficulty", self.difficulty_ranks.keys())

    def assign_difficulty(self, difficulty):
        # Assign difficulty
        self.difficulty = self.difficulty_ranks[difficulty]
        self.load_game_data()
        self.ui_callback("display_answer_buttons", self.state.category.keys())
        self.show_next_image()

    def _initialize_state(self):
        # Initialize the player's state
        self.state.category = {category: 0 for category in self.preloaded_images.keys()}
        chart.load(self.default_chart, self.chart_filename)

    def load_game_data(self):
        # Select and import images based on difficulty level
        data = DataManager()
        data.load(self.data_dir)

        images = ImageManager(self.image_dir, data)
        selected_images = images.select_images(self.difficulty)
        self.preloaded_images = images.preload_images(selected_images)

        self._initialize_state()

    def show_next_image(self):
        # Choose the next image and handle if you finish all the image of a key
        available_categories = [
            cat for cat, count in self.state.category.items() if count < self.difficulty
        ]
        if not available_categories:
            self.end_game()
            return

        self.current_category = random.choice(available_categories)
        current_image_index = self.state.category[self.current_category]

        image = self.preloaded_images[self.current_category][current_image_index]
        self.ui_callback("display_image", image)

        self.state.category[self.current_category] += 1

    def check_answer(self, answer):
        # Check if the answer is right or wrong
        if answer == self.current_category:
            self.state.avatar_score += 10
            self.ui_callback("show_correct_answer")
        else:
            self.ui_callback("show_wrong_answer")

        self.show_next_image()

    def save_score(self):
        # Save the score of the player
        chart.update_chart(self.state.avatar_name, self.state.avatar_score)
        chart.save(self.chart_filename)

    def end_game(self):
        # End the game and show the final chart
        if self.state.avatar_score > 0:
            self.save_score()
            self.ui_callback("display_game_results", self.state.chart)