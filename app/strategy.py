from app.dto.ReturnDirections import ReturnDirections

class Strategy:
    def __init__(self, game_field, my_player, my_position):
        self.game_field = game_field
        self.my_player = my_player
        self.my_position = my_position
        self.optimum_position = False
        self.choice = ReturnDirections.STOP

    def get_move(self):
        return self.choice
