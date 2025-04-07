import unittest
from quizzes.egyptians import Egyptians
from gui.renderer import Renderer


class TestLivingOrNot(unittest.TestCase):
    def test_egyptians(self):
        renderer = Renderer(None, "Egizi")
        Egyptians(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
