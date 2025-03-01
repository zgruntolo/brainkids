import json


class DataManager:
    def __init__(self):
        # Initialize an empty data dictionary
        self.data = {}

    def load(self, filepath):
        # Load data from a JSON file and update the internal dictionary
        with open(filepath, "r") as file:
            loaded_data = json.load(file)
        self.data.update(loaded_data)
