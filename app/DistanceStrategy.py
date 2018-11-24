from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy
from app.StrategyHelper import StrategyHelper
import random

class DistanceStrategy(Strategy):
    moves = []

    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)
        self.food_positions = []
        self.find_all_food()

    def get_move(self):
        pos = self.get_food_position()
        distance = self.calculate_distance(pos, self.my_position)
        for position in StrategyHelper.get_legal_directions_yxpos(self.my_position, self.game_field):
            if distance > self.calculate_distance(pos, position):
                move = StrategyHelper.get_direction_from_positions(self.my_position, position)
                if len(DistanceStrategy.moves) > 2:
                    if DistanceStrategy.moves[-2] != DistanceStrategy.moves[-1] and DistanceStrategy.moves[-2] == move:
                        self.choice = ReturnDirections.random()
                    else:
                        self.choice = move
                else:
                    self.choice = move
            else:
                self.choice = ReturnDirections.random()
        DistanceStrategy.moves.append(self.choice)
        return self.choice

    def calculate_distance(self, pos1, pos2):
        dis1 = pos1[0] - pos2[0]
        dis2 = pos1[1] - pos2[1]
        return dis1 + dis2

    def find_all_food(self):
        for j in range(0, len(self.game_field)):
            self.food_positions.append(
                [index for index, x in enumerate(self.game_field[j]) if x == "\u00b0" and not self.index_on_my_side(index)])

    def index_on_my_side(self, index):
        if self.my_player == 0 and index < len(self.game_field[0]) / 2:
            return True
        else:
            return False

    def get_food_position(self):
        for j in range(0, 18):
            if self.food_positions[j]:
                return [j, self.food_positions[j][0]]