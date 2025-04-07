import unittest
from quizzes.lakeriversea import LakeRiverSea
from gui.renderer import Renderer


class TestLivingOrNot(unittest.TestCase):
    def test_lake_river_sea(self):
        renderer = Renderer(None, "Fiume lago o mare")
        LakeRiverSea(renderer)
        renderer.run()


if __name__ == "__main__":
    unittest.main()
