import json
from bisect import insort
from pathlib import Path
from src.core.state import State

APP_FOLDER = Path.home() / "Documents" / "Schooltestsuite"


@staticmethod
def save(filename, folder_path=APP_FOLDER):
    # Create a save file
    chart = State()
    APP_FOLDER.mkdir(parents=True, exist_ok=True)
    save_path = folder_path / filename
    with open(save_path, "w") as file:
        json.dump(chart.chart, file)


@staticmethod
def load(default, filename, folder_path=APP_FOLDER):
    # Check if a save file exist and load it
    chart = State()
    save_path = folder_path / filename
    try:
        with open(save_path, "r") as file:
            chart.chart = json.load(file)
    except FileNotFoundError:
        with open(Path(__file__).parent.parent / default, "r") as file:
            chart.chart = json.load(file)


@staticmethod
def update_chart(name, score):
    # Update the chart with the player's stats
    chart = State()
    chart.avatar = [name, score]
    insort(chart.chart, chart.avatar, key=lambda x: -x[1])
    if len(chart.chart) > 10:
        chart.chart.pop()
