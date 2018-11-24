from app.dto.ReturnDirections import ReturnDirections

class Strategy:
    def __init__(self):
        self.choice = ReturnDirections.random()

    def get_move(self):
        return self.choice
