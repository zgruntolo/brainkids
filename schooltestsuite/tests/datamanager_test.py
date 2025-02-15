from pathlib import Path
from src.core.datamanager import DataManager
import unittest

ABSOLUTE_PATH = Path(__file__).parent
TEST_DATA = ABSOLUTE_PATH / "test_data/images.json"


class TestData(unittest.TestCase):

    def test_load(self):

        data = DataManager()
        data.load(TEST_DATA)
        self.assertEqual(
            data.data["Viventi"], ["pappagallo.jpg", "pesce.jpg", "quercia.jpg"]
        )


if __name__ == "__main__":
    unittest.main()
