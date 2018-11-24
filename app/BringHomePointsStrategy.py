from app.dto.ReturnDirections import ReturnDirections
from app.strategy import Strategy
from app.dto.HelperDTOs import PublicFields

class BringHomePointsStrategy(Strategy):
    def __init__(self, game_field, my_player, my_position):
        super().__init__(game_field, my_player, my_position)
        self.name = ""

    def get_move(self):
        self.game_field
        self.my_player
        self.my_position
        self.optimum_position

        self.reached_goal()
        if self.reached_goal():
            self.choice = ReturnDirections.STOP
        else:
            self.choice = self.get_legal_directions()[0]

        #self.choice = self.get_legal_directions()[0]

        return self.choice

    def reached_goal(self):
        if self.my_position[0] < len(self.game_field[0]) / 2:
            self.optimum_position = True

        return self.optimum_position

    def get_legal_directions(self):
        all_legal_directions = []
        neighbourhood = self.get_full_neighbourhood()
        if neighbourhood[3] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.LEFT)
        if neighbourhood[1] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.NORTH)
        if neighbourhood[6] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.SOUTH)
        if neighbourhood[4] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.RIGHT)
        return all_legal_directions

    def get_full_neighbourhood(self):
        neighbourhood_array = []
        player_x = self.my_position[0]
        player_y = self.my_position[1]
        neighbourhood_array = neighbourhood_array + self.game_field[int(player_y - 1)][int(player_x - 1):int(player_x + 2)]
        neighbourhood_array = neighbourhood_array + self.game_field[int(player_y)][int(player_x - 1):int(player_x + 2)]
        neighbourhood_array.pop(4)
        neighbourhood_array = neighbourhood_array + self.game_field[int(player_y + 1)][int(player_x - 1):int(player_x + 2)]
        return neighbourhood_array
