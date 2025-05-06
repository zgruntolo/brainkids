from quizzes.rocks import Rocks
from gui.renderer import Renderer
import unittest


class TestRocks(unittest.TestCase):
    def test_rocks(self):
        renderer = Renderer(None, "Egizi")
        Rocks(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
