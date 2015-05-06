# NOTE: this file should not be modified by competitors
from utilities import camel_case_converter

# @class BaseAI: the basic AI functions that are the same between games
class BaseAI:
    def __init__(self, game):
        self.game = game
        self.player = None

    def set_player(self, player):
        self.player = player

    # intended to be overridden by the AI class
    def start(self):
        pass

    # intended to be overridden by the AI class
    def game_updated(self):
        pass

    # intended to be overridden by the AI class
    def do_order(self, order, arguments):
        callback = getattr(self, camel_case_converter(order))

        if callback != None:
            return callback(*arguments)
        else:
            raise Exception("AI has no function '" + order + "' to respond with")

    # called when we (the client) send some invalid response to the server. It should be echoed back here
    def invalid(self, data):
        pass

    # intended to be overridden by the AI class
    def end(self):
        pass
