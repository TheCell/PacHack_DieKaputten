import random
import bottle
import os

from app import BringHomePointsStrategy
from app.dto.PublicGameState import PublicGameState
from app.dto.PublicPlayer import PublicPlayer
from app.dto.ReturnDirections import ReturnDirections
from app.eatEverythingStrategy import EatEverythingStrategy
from app.WalkAroundStrategy import WalkAroungStrategy
from app.Bot import Bot

@bottle.post('/start')
def start():
    return "DieKaputten"


@bottle.post('/chooseAction')
def move():
    data = PublicGameState(ext_dict=bottle.request.json)
    game_field = data.gameField
    players = data.publicPlayers
    my_player = data.agent_id
    my_position = players[my_player]['position']
    Bot.updateValues(game_field, players, my_player, my_position)

    print("I am player: "+str(my_player))
    print("My position is: "+str(my_position))
    #strategy = EatEverythingStrategy(game_field, my_player, my_position)
    #strategy = BringHomePointsStrategy(game_field, my_player, my_position)
    strategy = WalkAroungStrategy(game_field, my_player, my_position)
    return strategy.get_move()

application = bottle.default_app()
if __name__ == '__main__':
    idiotBot = Bot()

    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))

    #print("legal positions: " + str(StrategyHelper.get_legal_directions_yxpos(my_position, game_field)))
    #print(game_field)
    #def add_walls_to_enemy_places(playerindex, players, gamefield):
    #    own_player = players[playerindex]
    #    del players[playerindex]
    #    for player in players:
    #        # case we are weak ghost they are pacman
    #        if not player.isPacman and not own_player.isweakened:
    #            gamefield[player.position[1]][player.position[0]] = '%'
    #        # case We are pacman and they are weak ghost
    #        if not player.isweakened and not own_player.isPacman:
    #            gamefield[player.position[1]][player.position[0]] = '%'

    #add_walls_to_enemy_places(my_player, players, game_field)
    #print(game_field)
    #strategy = EatEverythingStrategy(game_field, my_player, my_position)
