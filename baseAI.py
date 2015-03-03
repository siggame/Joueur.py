# NOTE: this file should not be modified by competitors
from easydict import EasyDict
import json

# @class BaseAI: the basic AI functions that are the same between games
class BaseAI:
    def __init__(self, game, socket):
        self.socket = socket
        self.game = game

    def start(self, data):
        self.playerID = data["playerID"]

    def _connected(self, data):
        self.playerName = data["playerName"]
        self._serverConstants = EasyDict(data["constants"])


    # intended to be overridden by the AI class
    def gameUpdated(self):
        pass


    # intended to be overridden by the AI class
    def init(self):
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
    def sendCommand(self, command, **kwargs):
        data = kwargs

        self._formatCommandData(data)
        data['command'] = command

        self.socket.emit("command", json.dumps(data))

    # recursively formats command data, transforming game objects to simple id holders.
    # @param data: dict/list of data for format. DO NOT HAVE CYCLES IN IT (cycles in game objects are fine) 
    def _formatCommandData(self, data):
        for key in data:
            value = data[key]
            if isinstance(value, dict) and 'id' in value and value['id'] > -1:
                data[key] =  {'id': value['id']}
            elif isinstance(value, dict) or isinstance(value, list):
                self._formatCommandData(value)


