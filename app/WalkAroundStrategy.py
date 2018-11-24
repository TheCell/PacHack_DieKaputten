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
    hit_right_side = False

    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)

    def get_move(self):
        print(WalkAroungStrategy.preference)
        moves = []
        for move in StrategyHelper.get_legal_directions(self.my_position, self.game_field):
            moves.append(move)

        self.remove_origin_position_if_more_avail(moves)

        if WalkAroungStrategy.preference in moves:
            if (WalkAroungStrategy.previousmove is not ReturnDirections.WEST) and (ReturnDirections.EAST in moves):
                WalkAroungStrategy.preference = ReturnDirections.EAST
            elif len(moves) > 2:
                self.remove_origin_position_if_more_avail(moves)
                WalkAroungStrategy.preference = random.choice(moves)
            WalkAroungStrategy.choice = WalkAroungStrategy.preference
            print("is in if " + str(WalkAroungStrategy.choice))
        else:
            WalkAroungStrategy.remove_origin_position_if_more_avail(self, moves)

            if WalkAroungStrategy.preferedDirection in moves:
                WalkAroungStrategy.preference = WalkAroungStrategy.preferedDirection
            else:
                WalkAroungStrategy.preference = random.choice(moves)

            WalkAroungStrategy.choice = WalkAroungStrategy.preference
            print("is in else " + str(WalkAroungStrategy.choice))

        WalkAroungStrategy.previousmove = WalkAroungStrategy.choice
        return WalkAroungStrategy.choice

    def remove_origin_position_if_more_avail(self, moves):
        if WalkAroungStrategy.previousmove is not None:
            if len(moves) > 1:
                if WalkAroungStrategy.previousmove == ReturnDirections.NORTH:
                    if ReturnDirections.SOUTH in moves:
                        moves.remove(ReturnDirections.SOUTH)
                elif WalkAroungStrategy.previousmove == ReturnDirections.SOUTH:
                    if ReturnDirections.NORTH in moves:
                        moves.remove(ReturnDirections.NORTH)
                elif WalkAroungStrategy.previousmove == ReturnDirections.EAST:
                    if ReturnDirections.WEST in moves:
                        moves.remove(ReturnDirections.WEST)
                elif WalkAroungStrategy.previousmove == ReturnDirections.WEST:
                    if ReturnDirections.EAST in moves:
                        moves.remove(ReturnDirections.EAST)
            else:
                print("moves length is not more then 1")
