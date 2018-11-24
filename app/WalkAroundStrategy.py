from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy
from app.StrategyHelper import StrategyHelper
from app.Bot import Bot

import random

class WalkAroungStrategy(Strategy):
    preference = ReturnDirections.WEST
    choice = ReturnDirections.WEST
    previousmove = None
    preferedDirection = ReturnDirections.WEST

    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)

    def get_move(self):
        print(WalkAroungStrategy.preference)
        moves = []
        for move in StrategyHelper.get_legal_directions(self.my_position, self.game_field):
            moves.append(move)

        if WalkAroungStrategy.preference in moves:
            if (WalkAroungStrategy.previousmove is not ReturnDirections.WEST) and (ReturnDirections.EAST in moves):
                WalkAroungStrategy.preference = ReturnDirections.EAST

            WalkAroungStrategy.choice = WalkAroungStrategy.preference
            print("is in if " + str(WalkAroungStrategy.choice))
        else:
            if WalkAroungStrategy.previousmove is not None:
                if len(moves) > 1:
                    if WalkAroungStrategy.previousmove == ReturnDirections.NORTH:
                        moves.remove(ReturnDirections.SOUTH)
                    elif WalkAroungStrategy.previousmove == ReturnDirections.SOUTH:
                        moves.remove(ReturnDirections.NORTH)
                    elif WalkAroungStrategy.previousmove == ReturnDirections.EAST:
                        moves.remove(ReturnDirections.WEST)
                    elif WalkAroungStrategy.previousmove == ReturnDirections.WEST:
                        moves.remove(ReturnDirections.EAST)
                else:
                    print("moves length is not more then 1")
            if WalkAroungStrategy.preferedDirection in moves:
                WalkAroungStrategy.preference = WalkAroungStrategy.preferedDirection
            else:
                WalkAroungStrategy.preference = random.choice(moves)

            WalkAroungStrategy.choice = WalkAroungStrategy.preference
            print("is in else " + str(WalkAroungStrategy.choice))

        WalkAroungStrategy.previousmove = WalkAroungStrategy.choice
        return WalkAroungStrategy.choice
