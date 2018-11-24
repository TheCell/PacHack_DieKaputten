from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy

class EatEverythingStrategy(Strategy):
    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)
        self.name = ""
