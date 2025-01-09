class StateInstance:
    def __init__(self):
        self.category = []
        self.counter = 0
        self.chart = ()


class State:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Singleton pattern to ensure only one instance of State is created
        if not cls._instance:
            cls._instance = StateInstance()
        return cls._instance
