from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy

class BringHomePointsStrategy(Strategy):
    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)
        self.name = ""

    def get_move(self):
        self.game_field
        self.my_player
        self.my_position
        self.choice = ReturnDirections.random()
        return self.choice
