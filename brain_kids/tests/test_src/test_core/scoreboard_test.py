from pathlib import Path
from core.gamestate import State
import json
import core.scoreboard as scoreboard
import unittest


ABSOLUTE_PATH = Path(__file__).parent.parent.parent / "test_data" / "saves"
DEFAULT_TEST_NAME = "state.json"
DEFAULT_TEST_PATH = ABSOLUTE_PATH / DEFAULT_TEST_NAME
TEST_SAVE_NAME = "tommaso.json"
TEST_SAVE_PATH = ABSOLUTE_PATH / TEST_SAVE_NAME

game_state = State()


class TestScoreboard(unittest.TestCase):
    def test_save(self):
        game_state.scoreboard.append(["Tommaso", 260])
        scoreboard.save(TEST_SAVE_NAME, ABSOLUTE_PATH)
        with open(TEST_SAVE_PATH, "r") as file:
            save_data = json.load(file)
        self.assertEqual(save_data, game_state.scoreboard)
        TEST_SAVE_PATH.unlink()
        game_state.scoreboard.remove(["Tommaso", 260])
        save_path = Path.home() / "Documents" / "BrainKids"
        save_path.rmdir()

    def test_load(self):
        scoreboard.load(DEFAULT_TEST_PATH, DEFAULT_TEST_NAME, ABSOLUTE_PATH)
        self.assertEqual(game_state.scoreboard, [["Ilary", 320]])
        game_state.scoreboard.remove(["Ilary", 320])


if __name__ == "__main__":
    unittest.main()
