import uuid
import datetime

class Tracker:
    def __init__(self):
        self.events = []

    def track_click(self, product):
        event = {
            "id": str(uuid.uuid4()),
            "type": "click",
            "product": product["title"],
            "timestamp": str(datetime.datetime.utcnow())
        }
        self.events.append(event)
        return event

    def track_conversion(self, product):
        event = {
            "id": str(uuid.uuid4()),
            "type": "conversion",
            "product": product["title"],
            "timestamp": str(datetime.datetime.utcnow())
        }
        self.events.append(event)
        return event
