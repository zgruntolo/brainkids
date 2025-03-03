import sys
from pathlib import Path
from core.gamelogic import GameLogic
from core.common_ui_callback import create_game_ui_callback

# Handle the Pyinstaller files path
if hasattr(sys, "_MEIPASS"):
    ABSOLUTE_PATH = Path(sys._MEIPASS)
else:
    ABSOLUTE_PATH = Path(__file__).parent.parent.parent

DIFFICULTY_RANK = {"Facile": 5, "Medio": 10, "Difficile": 15}
DATA_FILE = ABSOLUTE_PATH / "data" / "lakeriversea" / "files/images.json"
IMAGE_DIR = ABSOLUTE_PATH / "data" / "lakeriversea" / "images"
DEFAULT_CHART = ABSOLUTE_PATH / "data" / "lakeriversea" / "files/chart.json"
CHART_FILENAME = "lakeriversea.json"


def LakeRiverSea(renderer):
    game_logic = GameLogic(
        DIFFICULTY_RANK,
        DATA_FILE,
        IMAGE_DIR,
        DEFAULT_CHART,
        CHART_FILENAME,
        game_ui_callback=None,
    )

    ui_callback = create_game_ui_callback(game_logic, renderer)
    game_logic.game_ui_callback = ui_callback
    renderer.game_callback = ui_callback
    game_logic.start_game()
