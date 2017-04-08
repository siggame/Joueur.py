# Game: Gather branches and build up your lodge as beavers fight to survive.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from joueur.base_game import BaseGame

# import game objects
from games.stumped.beaver import Beaver
from games.stumped.game_object import GameObject
from games.stumped.job import Job
from games.stumped.player import Player
from games.stumped.spawner import Spawner
from games.stumped.tile import Tile



class Game(BaseGame):
    """The class representing the Game in the Stumped game.

    Gather branches and build up your lodge as beavers fight to survive.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._beavers = []
        self._current_player = None
        self._current_turn = 0
        self._free_beavers_count = 0
        self._game_objects = {}
        self._jobs = []
        self._lodge_cost_constant = 0
        self._lodges_to_win = 0
        self._map_height = 0
        self._map_width = 0
        self._max_turns = 100
        self._players = []
        self._session = ""
        self._spawner = []
        self._spawner_harvest_constant = 0
        self._spawner_types = []
        self._tiles = []

        self.name = "Stumped"

        self._game_object_classes = {
            'Beaver': Beaver,
            'GameObject': GameObject,
            'Job': Job,
            'Player': Player,
            'Spawner': Spawner,
            'Tile': Tile
        }

    @property
    def beavers(self):
        """Every Beaver in the game.

        :rtype: list[Beaver]
        """
        return self._beavers

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
    def free_beavers_count(self):
        """When a Player has less Beavers than this number, then recruiting other Beavers is free.

        :rtype: int
        """
        return self._free_beavers_count

    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, GameObject]
        """
        return self._game_objects

    @property
    def jobs(self):
        """All the Jobs that Beavers can have in the game.

        :rtype: list[Job]
        """
        return self._jobs

    @property
    def lodge_cost_constant(self):
        """Constant number used to calculate what it costs to spawn a new lodge.

        :rtype: float
        """
        return self._lodge_cost_constant

    @property
    def lodges_to_win(self):
        """How many lodges must be owned by a Player at once to win the game.

        :rtype: int
        """
        return self._lodges_to_win

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

    @property
    def spawner(self):
        """Every Spawner in the game.

        :rtype: list[Spawner]
        """
        return self._spawner

    @property
    def spawner_harvest_constant(self):
        """Constant number used to calculate how many branches/food Beavers harvest from Spawners.

        :rtype: float
        """
        return self._spawner_harvest_constant

    @property
    def spawner_types(self):
        """All the types of Spawners in the game.

        :rtype: list[str]
        """
        return self._spawner_types

    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[Tile]
        """
        return self._tiles


    def get_tile_at(self, x, y):
        """Gets the Tile at a specified (x, y) position
        Args:
            x (int): integer between 0 and the mapWidth
            y (int): integer between 0 and the mapHeight
        Returns:
            Tile: the Tile at (x, y) or None if out of bounds
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.mapWidth]
