from app.dto.HelperDTOs import PublicFields
from app.dto.ReturnDirections import ReturnDirections

class StrategyHelper:
    @staticmethod
    def get_legal_directions(position, gamefield):
        all_legal_directions = []
        neighbourhood = StrategyHelper.get_full_neighbourhood(position, gamefield)
        if neighbourhood[3] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.LEFT)
        if neighbourhood[1] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.NORTH)
        if neighbourhood[6] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.SOUTH)
        if neighbourhood[4] != PublicFields.WALL:
            all_legal_directions.append(ReturnDirections.RIGHT)
        return all_legal_directions

    @staticmethod
    def get_legal_directions_yxpos(position, gamefield):
        all_legal_directions = []
        neighbourhood = StrategyHelper.get_full_neighbourhood_yx(position)
        if gamefield[neighbourhood[0][1]][neighbourhood[0][1]] != PublicFields.WALL:
            all_legal_directions.append(neighbourhood[0])
        if gamefield[neighbourhood[1][0]][neighbourhood[1][1]] != PublicFields.WALL:
            all_legal_directions.append(neighbourhood[1])
        if gamefield[neighbourhood[2][0]][neighbourhood[2][1]] != PublicFields.WALL:
            all_legal_directions.append(neighbourhood[2])
        if gamefield[neighbourhood[3][0]][neighbourhood[3][1]] != PublicFields.WALL:
            all_legal_directions.append(neighbourhood[3])
        return all_legal_directions

    @staticmethod
    def get_full_neighbourhood(position, gamefield):
        neighbourhood_array = []
        player_x = position[0]
        player_y = position[1]
        neighbourhood_array = neighbourhood_array + gamefield[int(player_y - 1)][int(player_x - 1):int(player_x + 2)]
        neighbourhood_array = neighbourhood_array + gamefield[int(player_y)][int(player_x - 1):int(player_x + 2)]
        neighbourhood_array.pop(4)
        neighbourhood_array = neighbourhood_array + gamefield[int(player_y + 1)][int(player_x - 1):int(player_x + 2)]
        return neighbourhood_array

    @staticmethod
    def get_full_neighbourhood_yx(position):
        player_x = int(position[0])
        player_y = int(position[1])
        neighbourhood_array = [[player_y - 1,player_x],
                               [player_y, player_x - 1],
                               [player_y, player_x + 1],
                               [player_y + 1, player_x]]
        return neighbourhood_array
