from livingornot.livingornot import LivingOrNot
from src.gui.renderer import Renderer
from treeparts.treeparts import TreeParts


games = {"Viventi e Non Viventi": LivingOrNot, "Parti dell'albero": TreeParts}

if __name__ == "__main__":
    renderer = Renderer(None, "School Test Suite")
    renderer.selection_screen(games)
    renderer.run()
