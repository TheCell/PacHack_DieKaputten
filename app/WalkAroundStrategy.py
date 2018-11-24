from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy
from app.StrategyHelper import StrategyHelper
import random

class WalkAroungStrategy(Strategy):
    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)
        if self.my_player == 1:
            self.preference = ReturnDirections.LEFT
        else:
            self.preference = ReturnDirections.RIGHT

    def get_move(self):
        moves = []
        for move in StrategyHelper.get_legal_directions(self.my_position, self.game_field):
            moves.append(move)
        if self.preference in moves:
            self.choice = self.preference
        else:
            self.preference = random.choice(moves)
            self.choice = self.preference
        return self.choice
