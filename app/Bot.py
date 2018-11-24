from app.dto.ReturnDirections import ReturnDirections

class Bot:
    @staticmethod
    def __init__(self, game_field, my_player, my_position):
        self.game_field = game_field
        self.my_player = my_player
        self.my_position = my_position
        self.preference = ReturnDirections.EAST
        self.choice = self.preference
