from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy

class EatEverythingStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.name = ""
