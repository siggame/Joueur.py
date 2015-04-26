# NOTE: this file should not be modified by competitors
from easydict import EasyDict
from utilities import camel_case_converter
import json

# @class BaseAI: the basic AI functions that are the same between games
class BaseAI:
    def __init__(self, game):
        self.game = game

    def set_player(self, player):
        self.player = player

    # intended to be overridden by the AI class
    def start(self):
        pass

    # intended to be overridden by the AI class
    def game_updated(self):
        pass

    # intended to be overridden by the AI class
    def respond_to(self, request, arguments):
        callback = getattr(self, camel_case_converter(request))

        if callback != None:
            return callback(*arguments)
        else:
            raise Exception("AI has no function '" + request + "' to respond with")

    # called when we (the client) send some invalid response to the server. It should be echoed back here
    def invalid(self, data):
        pass

    # intended to be overridden by the AI class
    def end(self):
        pass
