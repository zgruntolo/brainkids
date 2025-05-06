from quizzes.treeparts import TreeParts
from gui.renderer import Renderer
import unittest


class TestTreeParts(unittest.TestCase):
    def test_treeparts(self):
        renderer = Renderer(None, "Parti dell'albero")
        TreeParts(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
