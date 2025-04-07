from contextlib import contextmanager
from gui.renderer import Renderer
from quizzes.lakeriversea import LakeRiverSea
from quizzes.livingornot import LivingOrNot
from quizzes.treeparts import TreeParts
from quizzes.egyptians import Egyptians
from pathlib import Path
import sys
import subprocess
import time

games = {
    "Viventi e Non Viventi": LivingOrNot,
    "Parti dell'albero": TreeParts,
    "Lago Fiume o Mare": LakeRiverSea,
    "Egizi": Egyptians,
}

folder_path = Path(__file__).parent.parent / "temp"


def remove_dir(path):
    if path.exists() and path.is_dir():
        time.sleep(3)
        subprocess.Popen(f'cmd /c timeout 2 && rmdir /s /q "{folder_path}"', shell=True)
        sys.exit()


def start():
    renderer = Renderer(None, "BrainKids")
    renderer.show_game_selection_screen(games)
    renderer.run()


@contextmanager
def temp_dir_cleanup(path):
    try:
        yield
    finally:
        remove_dir(path)


if __name__ == "__main__":
    if "__compiled__" in globals():
        with temp_dir_cleanup(folder_path):
            start()
    else:
        start()
