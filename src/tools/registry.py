class Tools:
    def __init__(self):
        self.map = {}

    def add(self, name, tool):
        self.map[name] = tool

    def get(self, name):
        return self.map[name]
