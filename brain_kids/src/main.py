from gui.renderer import Renderer
from quizzes.lakeriversea import LakeRiverSea
from quizzes.livingornot import LivingOrNot
from quizzes.treeparts import TreeParts


games = {
    "Viventi e Non Viventi": LivingOrNot,
    "Parti dell'albero": TreeParts,
    "Lago Fiume o Mare": LakeRiverSea,
}

if __name__ == "__main__":
    renderer = Renderer(None, "BrainKids")
    renderer.show_game_selection_screen(games)
    renderer.run()
