from quizzes.livingornot import LivingOrNot
from gui.renderer import Renderer
import unittest


class TestLivingOrNot(unittest.TestCase):
    def test_living_or_not(self):
        renderer = Renderer(None, "Vivente o non Vivente")
        LivingOrNot(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
