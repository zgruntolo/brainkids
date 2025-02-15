from pathlib import Path
from src.core.state import State
import json
import src.core.chart as chart
import unittest


ABSOLUTE_PATH = Path(__file__).parent / "test_data/saves/"
DEFAULT_TEST_NAME = "state.json"
DEFAULT_TEST_PATH = ABSOLUTE_PATH / DEFAULT_TEST_NAME
TEST_SAVE_NAME = "tommaso.json"
TEST_SAVE_PATH = ABSOLUTE_PATH / TEST_SAVE_NAME


class TestChart(unittest.TestCase):

    def test_load(self):
        state = State()
        chart.load(None, DEFAULT_TEST_NAME, ABSOLUTE_PATH)
        self.assertEqual(state.chart, [["Ilary", 320]])
        state.chart = []

    def test_save(self):
        state = State()
        state.chart.append(["Tommaso", 260])
        chart.save(TEST_SAVE_NAME, ABSOLUTE_PATH)
        with open(TEST_SAVE_PATH, "r") as file:
            save_data = json.load(file)
        self.assertEqual(save_data, state.chart)
        TEST_SAVE_PATH.unlink()


if __name__ == "__main__":
    unittest.main()
