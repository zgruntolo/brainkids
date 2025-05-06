from quizzes.animals import Animals
from gui.renderer import Renderer
import unittest


class TestAnimals(unittest.TestCase):
    def test_animals(self):
        renderer = Renderer(None, "Egizi")
        Animals(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
