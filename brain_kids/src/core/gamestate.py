class _GameState:
    # Class representing the internal game state
    def __init__(self):
        self.selected_categories = {}
        self.difficulty_level = 0
        self.player_name = ""
        self.player_score = 0
        self.scoreboard = []


class State:
    # Singleton class to manage the game state.
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = _GameState()
        return cls._instance
