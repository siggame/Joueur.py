# Game: Mine resources to obtain more wealth than your opponent.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from joueur.base_game import BaseGame

# import game objects
from games.coreminer.game_object import GameObject
from games.coreminer.job import Job
from games.coreminer.player import Player
from games.coreminer.tile import Tile
from games.coreminer.unit import Unit

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Coreminer game.

    Mine resources to obtain more wealth than your opponent.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bomb_cost = 0
        self._bomb_size = 0
        self._building_material_cost = 0
        self._current_player = None
        self._current_turn = 0
        self._free_bomb_interval = 0
        self._game_objects = {}
        self._jobs = []
        self._ladder_cost = 0
        self._map_height = 0
        self._map_width = 0
        self._max_turns = 100
        self._ore_value = 0
        self._players = []
        self._session = ""
        self._shield_cost = 0
        self._support_cost = 0
        self._tiles = []
        self._time_added_per_turn = 0
        self._units = []
        self._upgrade_cargo_capacity_cost = 0
        self._upgrade_health_cost = 0
        self._upgrade_mining_power_cost = 0
        self._upgrade_moves_cost = 0
        self._victory_amount = 0

        self.name = "Coreminer"

        self._game_object_classes = {
            'GameObject': GameObject,
            'Job': Job,
            'Player': Player,
            'Tile': Tile,
            'Unit': Unit
        }

    @property
    def bomb_cost(self):
        """The price of buying a bomb.

        :rtype: int
        """
        return self._bomb_cost

    @property
    def bomb_size(self):
        """The amount of cargo space taken up by a bomb.

        :rtype: int
        """
        return self._bomb_size

    @property
    def building_material_cost(self):
        """The price of buying building materials.

        :rtype: int
        """
        return self._building_material_cost

    @property
    def current_player(self):
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.coreminer.player.Player
        """
        return self._current_player

    @property
    def current_turn(self):
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn

    @property
    def free_bomb_interval(self):
        """The amount of turns it takes to gain a free Bomb.

        :rtype: int
        """
        return self._free_bomb_interval

    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, games.coreminer.game_object.GameObject]
        """
        return self._game_objects

    @property
    def jobs(self):
        """A list of all jobs.

        :rtype: list[games.coreminer.job.Job]
        """
        return self._jobs

    @property
    def ladder_cost(self):
        """The amount of building material required to build a ladder.

        :rtype: int
        """
        return self._ladder_cost

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
    def ore_value(self):
        """The amount of victory points awarded when ore is deposited in the base.

        :rtype: int
        """
        return self._ore_value

    @property
    def players(self):
        """List of all the players in the game.

        :rtype: list[games.coreminer.player.Player]
        """
        return self._players

    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def shield_cost(self):
        """The amount of building material required to shield a Tile.

        :rtype: int
        """
        return self._shield_cost

    @property
    def support_cost(self):
        """The amount of building material required to build a support.

        :rtype: int
        """
        return self._support_cost

    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[games.coreminer.tile.Tile]
        """
        return self._tiles

    @property
    def time_added_per_turn(self):
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn

    @property
    def units(self):
        """Every Unit in the game.

        :rtype: list[games.coreminer.unit.Unit]
        """
        return self._units

    @property
    def upgrade_cargo_capacity_cost(self):
        """The cost to upgrade a Unit's cargo capacity.

        :rtype: int
        """
        return self._upgrade_cargo_capacity_cost

    @property
    def upgrade_health_cost(self):
        """The cost to upgrade a Unit's health.

        :rtype: int
        """
        return self._upgrade_health_cost

    @property
    def upgrade_mining_power_cost(self):
        """The cost to upgrade a Unit's mining power.

        :rtype: int
        """
        return self._upgrade_mining_power_cost

    @property
    def upgrade_moves_cost(self):
        """The cost to upgrade a Unit's movement speed.

        :rtype: int
        """
        return self._upgrade_moves_cost

    @property
    def victory_amount(self):
        """The amount of victory points required to win.

        :rtype: int
        """
        return self._victory_amount


    def get_tile_at(self, x, y):
        """Gets the Tile at a specified (x, y) position
        Args:
            x (int): integer between 0 and the map_width
            y (int): integer between 0 and the map_height
        Returns:
            games.coreminer.tile.Tile: the Tile at (x, y) or None if out of bounds
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
