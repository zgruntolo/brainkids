from quizzes.egyptians import Egyptians
from gui.renderer import Renderer
import unittest


class TestEgyptians(unittest.TestCase):
    def test_egyptians(self):
        renderer = Renderer(None, "Egizi")
        Egyptians(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
