# ${header}
# This is where you build your AI for the ${game_name} game.
from baseAI import BaseAI

# @class BaseAI: the basic AI functions that are the same between games
class AI(BaseAI):
    # this is the name you send to the server to play as.
    def get_name(self):
        return "${game_name} Python Player"

    # this is called once the game starts and your AI knows its player.id and game. You can initialize your AI here.
    def game_initialized(self):
        pass

        # this is called when the game's state updates, so if you are tracking anything you can update it here.
    def game_updated(self):
        pass

    # this is called every time the server tells you that you can send a command. Once you send a command you must return. This is where most of your game logic will probably go
    def run(self):
        pass

    # this is called when the server is no longer taking game commands from you, normally when you turn ends and another players begins.
    def ignoring(self):
        pass

    # this is called when the game closes (ends), you can clean up your data and dump files here if need be
    def close(self):
        pass
