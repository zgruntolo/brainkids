import sys
from pathlib import Path
from src.core.gamelogic import GameLogic
from src.core.common_ui_callback import create_ui_callback
from src.gui.renderer import Renderer

# Handle the Pyinstaller files path
if hasattr(sys, "_MEIPASS"):
    ABSOLUTE_PATH = Path(sys._MEIPASS) / "livingornot"
else:
    ABSOLUTE_PATH = Path(__file__).parent

DIFFICULTY_RANK = {"Facile": 10, "Medio": 15, "Difficile": 20}
DATA_FILE = ABSOLUTE_PATH / "data/files/images.json"
IMAGE_DIR = ABSOLUTE_PATH / "data/images"
DEFAULT_CHART = ABSOLUTE_PATH / "data/files/chart.json"
CHART_FILENAME = "livingornot.json"


def LivingOrNot():
    game_logic = GameLogic(
        DIFFICULTY_RANK,
        DATA_FILE,
        IMAGE_DIR,
        DEFAULT_CHART,
        CHART_FILENAME,
        ui_callback=None,
    )
    renderer = Renderer(ui_callback=None, title="Viventi o Non Viventi")
    ui_callback = create_ui_callback(game_logic, renderer)
    game_logic.ui_callback = ui_callback
    renderer.ui_callback = ui_callback
    game_logic.start_game()
