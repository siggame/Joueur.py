# This is a simple class to represent the Game object in the game. You can extend it by adding utility functions here in this file.

from joueur.base_game import BaseGame

# import game objects
from games.checkers.checker import Checker
from games.checkers.game_object import GameObject
from games.checkers.player import Player

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Checkers game.

    The simple version of American Checkers. An 8x8 board with 12 checkers on each side that must move diagonally to the opposing side until kinged.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._board_height = 8
        self._board_width = 8
        self._checker_moved = None
        self._checker_moved_jumped = False
        self._checkers = []
        self._current_player = None
        self._current_turn = 0
        self._game_objects = {}
        self._max_turns = 100
        self._players = []
        self._session = ""

        self.name = "Checkers"

        self._game_object_classes = {
            'Checker': Checker,
            'GameObject': GameObject,
            'Player': Player
        }


    @property
    def board_height(self):
        """The height of the board for the Y component of a checker.

        :rtype: int
        """
        return self._board_height


    @property
    def board_width(self):
        """The width of the board for X component of a checker.

        :rtype: int
        """
        return self._board_width


    @property
    def checker_moved(self):
        """The checker that last moved and must be moved because only one checker can move during each players turn.

        :rtype: Checker
        """
        return self._checker_moved


    @property
    def checker_moved_jumped(self):
        """If the last checker that moved jumped, meaning it can move again.

        :rtype: bool
        """
        return self._checker_moved_jumped


    @property
    def checkers(self):
        """All the checkers currently in the game.

        :rtype: list[Checker]
        """
        return self._checkers


    @property
    def current_player(self):
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: Player
        """
        return self._current_player


    @property
    def current_turn(self):
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn


    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, GameObject]
        """
        return self._game_objects


    @property
    def max_turns(self):
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns


    @property
    def players(self):
        """List of all the players in the game.

        :rtype: list[Player]
        """
        return self._players


    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
