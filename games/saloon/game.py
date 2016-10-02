# This is a simple class to represent the Game object in the game. You can extend it by adding utility functions here in this file.

from joueur.base_game import BaseGame

# import game objects
from games.saloon.bottle import Bottle
from games.saloon.cowboy import Cowboy
from games.saloon.furnishing import Furnishing
from games.saloon.game_object import GameObject
from games.saloon.player import Player
from games.saloon.tile import Tile

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Saloon game.

    Use cowboys to have a good time and play some music on a Piano, while brawling with enemy Coyboys.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bottles = []
        self._cowboys = []
        self._current_player = None
        self._current_turn = 0
        self._furnishings = []
        self._game_objects = {}
        self._jobs = []
        self._map_height = 0
        self._map_width = 0
        self._max_cowboys = 0
        self._max_turns = 100
        self._players = []
        self._rowdyness_to_siesta = 0
        self._session = ""
        self._siesta_length = 0
        self._tiles = []

        self.name = "Saloon"

        self._game_object_classes = {
            'Bottle': Bottle,
            'Cowboy': Cowboy,
            'Furnishing': Furnishing,
            'GameObject': GameObject,
            'Player': Player,
            'Tile': Tile
        }


    @property
    def bottles(self):
        """All the beer Bottles currently flying across the saloon in the game.

        :rtype: list[Bottle]
        """
        return self._bottles


    @property
    def cowboys(self):
        """Every Cowboy in the game.

        :rtype: list[Cowboy]
        """
        return self._cowboys


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
    def furnishings(self):
        """Every furnishing in the game.

        :rtype: list[Furnishing]
        """
        return self._furnishings


    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, GameObject]
        """
        return self._game_objects


    @property
    def jobs(self):
        """All the jobs that Cowboys can be assigned within the saloon.

        :rtype: list[str]
        """
        return self._jobs


    @property
    def map_height(self):
        """The number of Tiles in the map along the y (vertical) axis.

        :rtype: int
        """
        return self._map_height


    @property
    def map_width(self):
        """The number of Tiles in the map along the x (horizontal) axis.

        :rtype: int
        """
        return self._map_width


    @property
    def max_cowboys(self):
        """The maximum number of Cowboys a Player can bring into the saloon.

        :rtype: int
        """
        return self._max_cowboys


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
    def rowdyness_to_siesta(self):
        """When a player's rowdyness reaches or exceeds this number their Cowboys take a collective siesta.

        :rtype: int
        """
        return self._rowdyness_to_siesta


    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session


    @property
    def siesta_length(self):
        """How long siestas are for a player's team.

        :rtype: int
        """
        return self._siesta_length


    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[Tile]
        """
        return self._tiles



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
