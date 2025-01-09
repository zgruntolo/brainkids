from src.datamanager import DataManager
from src.state import State
import random


class RandomImageSelector:

    def __init__(self, filename):
        self.image = DataManager()
        self.image.load(filename)

    def select_image(self):
        session_state = State()
        category = random.choice(list(self.image.data.keys()))
        session_state.category = category
        session_state.counter += 1
        image = random.choice(self.image.data[category])
        self.image.data[category].remove(image)
        return image
