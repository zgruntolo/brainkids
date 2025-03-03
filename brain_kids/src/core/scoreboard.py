import json
from bisect import insort
from pathlib import Path
from core.gamestate import State

SAVE_DIRECTORY = Path.home() / "Documents" / "BrainKids"
game_state = State()


def save(scoreboard_filename, save_directory=SAVE_DIRECTORY):
    # Create and save the scoreboard to a file
    SAVE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    save_path = save_directory / scoreboard_filename
    with open(save_path, "w") as file:
        json.dump(game_state.scoreboard, file)


def load(default_scoreboard_file, scoreboard_filename, save_directory=SAVE_DIRECTORY):
    # Load the scoreboard from a file if it exists, otherwise load the default
    save_path = save_directory / scoreboard_filename
    try:
        with open(save_path, "r") as file:
            game_state.scoreboard = json.load(file)
    except FileNotFoundError:
        default_path = Path(__file__).parent.parent / default_scoreboard_file
        with open(default_path, "r") as file:
            game_state.scoreboard = json.load(file)


def update_scoreboard(player_name, player_score):
    # Update the scoreboard with the player's name and score, keeping only the top 10 scores
    player_entry = [player_name, player_score]
    insort(game_state.scoreboard, player_entry, key=lambda x: -x[1])
    if len(game_state.scoreboard) > 10:
        game_state.scoreboard.pop()
