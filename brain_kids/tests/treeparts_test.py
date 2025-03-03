import unittest
from src.quizzes.treeparts import TreeParts
from src.gui.renderer import Renderer


class TestLivingOrNot(unittest.TestCase):
    def test_treeparts(self):
        renderer = Renderer(None, "Parti dell'albero")
        TreeParts(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
