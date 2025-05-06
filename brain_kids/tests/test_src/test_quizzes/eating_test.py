from quizzes.eating import Eating
from gui.renderer import Renderer
import unittest


class TestEating(unittest.TestCase):
    def test_eating(self):
        renderer = Renderer(None, "Egizi")
        Eating(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
