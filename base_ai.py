# NOTE: this file should not be modified by competitors
from utilities import camel_case_converter
from error_code import ErrorCode, handle_error
import sys
import client

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
    def _do_order(self, order, arguments):
        callback = getattr(self, camel_case_converter(order))

        if callback != None:
            try:
                return callback(*arguments)
            except:
                handle_error(ErrorCode.ai_errored, sys.exc_info()[0], "AI caused exception while trying to execute order '" + order + "'.")
        else:
            handle_error(ErrorCode.reflection_failed, message="AI has no function '" + order + "' to respond with")

    # called when we (the client) send some invalid response to the server. It should be echoed back here
    def invalid(self, data):
        pass

    # intended to be overridden by the AI class
    def end(self):
        pass
