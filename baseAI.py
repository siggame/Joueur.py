# NOTE: this file should not be modified by competitors
import json
idKey = "#"

# @class BaseAI: the basic AI functions that are the same between games
class BaseAI:
    def __init__(self, game, socket):
        self.socket = socket
        self.game = game

    def start(self, data):
        self.playerID = data["playerID"]


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

    #intended to be called by the BaseGameAI class
    def sendCommand(self, command, **kwargs):
        data = {'command': command}

        for key, value in kwargs.items():
            if isinstance(value, dict) and hasattr(value, "id") and value["id"] > -1:
                value = idKey + str(value["id"]) # TODO: get idKey from server
            data[key] = value

        self.socket.emit("command", json.dumps(data))
