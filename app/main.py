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
    temp_position = players[my_player]['position']
    my_position = [temp_position[1], temp_position[0]]
    print("I am player: "+str(my_player))
    print("My position is: "+str(my_position))
    strategy = EatEverythingStrategy(game_field, my_player, my_position)
    return strategy.get_move()

application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
