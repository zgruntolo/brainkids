from quizzes.lakeriversea import LakeRiverSea
from gui.renderer import Renderer
import unittest


class TestLakeRiverSea(unittest.TestCase):
    def test_lake_river_sea(self):
        renderer = Renderer(None, "Fiume lago o mare")
        LakeRiverSea(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
