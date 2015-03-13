# NOTE: this file should not be modified by competitors
from easydict import EasyDict
from gameObject import GameObject
from serializer import serialize
import json

# @class BaseAI: the basic AI functions that are the same between games
class BaseAI:
    def __init__(self, game, socket):
        self.socket = socket
        self.game = game

    def start(self, data):
        self.player_id = data["playerID"]
        self.player_name = data["playerName"]

    def connected(self, data):
        self._server_constants = EasyDict(data["constants"])


    def connect_player(self):
        self.player = self.game.get_game_object(self.player_id)


    # intended to be overridden by the AI class
    def game_initialized(self):
        pass


    # intended to be overridden by the AI class
    def game_updated(self):
        pass


    #intended to be overridden by the AI class
    def run(self):
        pass


    #intended to be overridden by the AI class
    def ignoring(self):
        pass


    #intended to be overridden by the AI class
    def close(self):
        pass


    def over(self):
        self.close()


    #intended to be called by the GeneratedAI class to perform game commands.
    def send_command(self, caller, command, **kwargs):
        data = kwargs

        data['command'] = command
        data['caller'] = caller
        data = serialize(data)

        self.socket.emit("command", json.dumps(data))

    # recursively formats command data, transforming game objects to simple id holders.
    # @param data: dict/list of data for format. DO NOT HAVE CYCLES IN IT (cycles in game objects are fine) 
   


