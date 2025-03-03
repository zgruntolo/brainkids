from pathlib import Path
from src.core.gamestate import State
import json
import src.core.scoreboard as scoreboard
import unittest


ABSOLUTE_PATH = Path(__file__).parent / "test_data" / "saves"
DEFAULT_TEST_NAME = "state.json"
DEFAULT_TEST_PATH = ABSOLUTE_PATH / DEFAULT_TEST_NAME
TEST_SAVE_NAME = "tommaso.json"
TEST_SAVE_PATH = ABSOLUTE_PATH / TEST_SAVE_NAME


class TestScoreboard(unittest.TestCase):

    def test_load(self):
        state = State()
        scoreboard.load(None, DEFAULT_TEST_NAME, ABSOLUTE_PATH)
        self.assertEqual(state.scoreboard, [["Ilary", 320]])
        state.scoreboard = []

    def test_save(self):
        state = State()
        state.scoreboard.append(["Tommaso", 260])
        scoreboard.save(TEST_SAVE_NAME, ABSOLUTE_PATH)
        with open(TEST_SAVE_PATH, "r") as file:
            save_data = json.load(file)
        self.assertEqual(save_data, state.scoreboard)
        TEST_SAVE_PATH.unlink()


if __name__ == "__main__":
    unittest.main()
