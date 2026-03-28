class Memory:
    def __init__(self):
        self.keywords = []

    def update(self, text):
        for w in text.lower().split():
            if w not in self.keywords:
                self.keywords.append(w)

    def get(self):
        return self.keywords
