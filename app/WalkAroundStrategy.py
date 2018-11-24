from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy
from app.StrategyHelper import StrategyHelper
from app.Bot import Bot

import random

class WalkAroungStrategy(Strategy):
    preference = ReturnDirections.WEST
    choice = ReturnDirections.WEST

    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)

    def get_move(self):
        print(WalkAroungStrategy.preference)
        moves = []
        for move in StrategyHelper.get_legal_directions(self.my_position, self.game_field):
            moves.append(move)

        if WalkAroungStrategy.preference in moves:
            WalkAroungStrategy.choice = WalkAroungStrategy.preference
            print("is in if " + str(WalkAroungStrategy.choice))
        else:
            WalkAroungStrategy.preference = random.choice(moves)
            WalkAroungStrategy.choice = WalkAroungStrategy.preference
            print("is in else " + str(WalkAroungStrategy.choice))
        return WalkAroungStrategy.choice
