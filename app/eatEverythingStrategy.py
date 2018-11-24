from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy
from app.StrategyHelper import StrategyHelper

class EatEverythingStrategy(Strategy):
    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)
        self.food_positions = []
        self.path = []
        self.debug()

    def get_shortest_path(self):
        #for wanted_position in self.food_positions:
            wanted_position=self.get_food_position()
            self.path = self.get_path_to_position(self.my_position, wanted_position, self.path)
            print("done")

    def get_path_to_position(self, current_position, wanted_position, path):
        print(current_position)
        print(wanted_position)
        if current_position != wanted_position:
            for position in StrategyHelper.get_legal_directions_xypos(current_position, self.game_field):
                new_position = position
                if new_position not in path:
                    path.append(new_position)
                    print(path)
                    return self.get_path_to_position(new_position, wanted_position, path)
        else:
            return self.path

    def countElement(a):
        g = {}
        for i in a:
            if i in g:
                g[i] += 1
            else:
                g[i] = 1
        return g

    def get_food_position(self):
        for j in range(0, 18):
            if self.food_positions[j]:
                return [j, self.food_positions[j][0]]

    def find_all_food(self):
        for j in range(0, len(self.game_field)):
            self.food_positions.append(
                [index for index, x in enumerate(self.game_field[j]) if x == "\u00b0" and not self.index_on_my_side(index)])

    def index_on_my_side(self, index):
        if self.my_player == 0 and index < len(self.game_field[0]) / 2:
            return True
        else:
            return False

    def debug(self):
        self.find_all_food()
        #pos = self.get_food_position()
        #self.get_path_to_position(self.my_position, pos, [])
        self.get_shortest_path()
        #print(self.food_positions)
