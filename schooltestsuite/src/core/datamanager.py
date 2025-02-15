import json


class DataManager:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        # Load a JSON file and update the dict
        with open(filename, "r") as file:
            database = json.load(file)
        self.data.update(database)
