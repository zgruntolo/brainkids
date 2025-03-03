import sys
from pathlib import Path
from core.gamelogic import GameLogic
from core.common_ui_callback import create_game_ui_callback

# Handle the Pyinstaller files path
if hasattr(sys, "_MEIPASS"):
    ABSOLUTE_PATH = Path(sys._MEIPASS)
else:
    ABSOLUTE_PATH = Path(__file__).parent.parent.parent

DIFFICULTY_RANK = {"Facile": 10, "Medio": 15, "Difficile": 20}
DATA_FILE = ABSOLUTE_PATH / "data" / "livingornot" / "files/images.json"
IMAGE_DIR = ABSOLUTE_PATH / "data" / "livingornot" / "images"
DEFAULT_CHART = ABSOLUTE_PATH / "data" / "livingornot" / "files/chart.json"
CHART_FILENAME = "livingornot.json"


def LivingOrNot(renderer):
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
