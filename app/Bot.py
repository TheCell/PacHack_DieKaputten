from app.dto.ReturnDirections import ReturnDirections

class Bot:
    game_field = None
    my_player = None
    my_position = None
    players = None
    preference = ReturnDirections.EAST
    choice = ReturnDirections.EAST

    @staticmethod
    def updateValues(game_field, players, my_player, my_position):
        Bot.game_field = game_field
        Bot.players = players
        Bot.my_player = my_player
        Bot.my_position = my_position
