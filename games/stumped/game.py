# Game: Gather branches and build up your lodge as beavers fight to survive.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List, Optional
from joueur.base_game import BaseGame

# import game objects
from games.stumped.beaver import Beaver
from games.stumped.game_object import GameObject
from games.stumped.job import Job
from games.stumped.player import Player
from games.stumped.spawner import Spawner
from games.stumped.tile import Tile

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Stumped game.

    Gather branches and build up your lodge as beavers fight to survive.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
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
        self._time_added_per_turn = 0

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
    def beavers(self) -> List['games.stumped.beaver.Beaver']:
        """list[games.stumped.beaver.Beaver]: Every Beaver in the game.
        """
        return self._beavers

    @property
    def current_player(self) -> 'games.stumped.player.Player':
        """games.stumped.player.Player: The player whose turn it is currently. That player can send commands. Other players cannot.
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """int: The current turn number, starting at 0 for the first player's turn.
        """
        return self._current_turn

    @property
    def free_beavers_count(self) -> int:
        """int: When a Player has less Beavers than this number, then recruiting other Beavers is free.
        """
        return self._free_beavers_count

    @property
    def game_objects(self) -> Dict[str, 'games.stumped.game_object.GameObject']:
        """dict[str, games.stumped.game_object.GameObject]: A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        """
        return self._game_objects

    @property
    def jobs(self) -> List['games.stumped.job.Job']:
        """list[games.stumped.job.Job]: All the Jobs that Beavers can have in the game.
        """
        return self._jobs

    @property
    def lodge_cost_constant(self) -> float:
        """float: Constant number used to calculate what it costs to spawn a new lodge.
        """
        return self._lodge_cost_constant

    @property
    def lodges_to_win(self) -> int:
        """int: How many lodges must be owned by a Player at once to win the game.
        """
        return self._lodges_to_win

    @property
    def map_height(self) -> int:
        """int: The number of Tiles in the map along the y (vertical) axis.
        """
        return self._map_height

    @property
    def map_width(self) -> int:
        """int: The number of Tiles in the map along the x (horizontal) axis.
        """
        return self._map_width

    @property
    def max_turns(self) -> int:
        """int: The maximum number of turns before the game will automatically end.
        """
        return self._max_turns

    @property
    def players(self) -> List['games.stumped.player.Player']:
        """list[games.stumped.player.Player]: List of all the players in the game.
        """
        return self._players

    @property
    def session(self) -> str:
        """str: A unique identifier for the game instance that is being played.
        """
        return self._session

    @property
    def spawner(self) -> List['games.stumped.spawner.Spawner']:
        """list[games.stumped.spawner.Spawner]: Every Spawner in the game.
        """
        return self._spawner

    @property
    def spawner_harvest_constant(self) -> float:
        """float: Constant number used to calculate how many branches/food Beavers harvest from Spawners.
        """
        return self._spawner_harvest_constant

    @property
    def spawner_types(self) -> List[str]:
        """list[str]: All the types of Spawners in the game.
        """
        return self._spawner_types

    @property
    def tiles(self) -> List['games.stumped.tile.Tile']:
        """list[games.stumped.tile.Tile]: All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.
        """
        return self._tiles

    @property
    def time_added_per_turn(self) -> int:
        """int: The amount of time (in nano-seconds) added after each player performs a turn.
        """
        return self._time_added_per_turn

    def get_tile_at(self, x: int, y: int) -> Optional['games.stumped.tile.Tile']:
        """Gets the Tile at a specified (x, y) position.

        Args:
            x (int): An integer between 0 and the map_width.
            y (int): An integer between 0 and the map_height.

        Returns:
            games.stumped.tile.Tile or None: The Tile at (x, y) or None if out of bounds.
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
