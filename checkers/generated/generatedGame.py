# NOTE: This file should never be modified after being spit out of the new CodeGen
from baseGame import BaseGame
from Checkers.player import Player
from Checkers.checker import Checker

class GeneratedGame(BaseGame):
    def __init__(self, *args, **kwargs):
        BaseGame.__init__(self, *args, **kwargs)

        self.board_width = 0
        self.board_height = 0
        self.checker_moved = None
        self.checker_moved_jumped = False
        self.checkers = []

        self._game_object_classes = {
            'Checker': Checker,
            'Player': Player
        }

