# Game: Combine elements and be the first scientists to create fusion.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from joueur.base_game import BaseGame

# import game objects
from games.newtonian.game_object import GameObject
from games.newtonian.job import Job
from games.newtonian.machine import Machine
from games.newtonian.player import Player
from games.newtonian.tile import Tile
from games.newtonian.unit import Unit

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Newtonian game.

    Combine elements and be the first scientists to create fusion.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._current_player = None
        self._current_turn = 0
        self._degrade_rate = 0
        self._game_objects = {}
        self._intern_cap = 0
        self._jobs = []
        self._machines = []
        self._manager_cap = 0
        self._map_height = 0
        self._map_width = 0
        self._material_spawn = 0
        self._max_turns = 100
        self._physicist_cap = 0
        self._players = []
        self._refined_value = 0
        self._session = ""
        self._spawn_time = 0
        self._stun_time = 0
        self._tiles = []
        self._time_added_per_turn = 0
        self._time_immune = 0
        self._units = []
        self._victory_amount = 0

        self.name = "Newtonian"

        self._game_object_classes = {
            'GameObject': GameObject,
            'Job': Job,
            'Machine': Machine,
            'Player': Player,
            'Tile': Tile,
            'Unit': Unit
        }

    @property
    def current_player(self):
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.newtonian.player.Player
        """
        return self._current_player

    @property
    def current_turn(self):
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn

    @property
    def degrade_rate(self):
        """Percent loss from the difference of Heat and Pressure. (0 to 1).

        :rtype: float
        """
        return self._degrade_rate

    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, games.newtonian.game_object.GameObject]
        """
        return self._game_objects

    @property
    def intern_cap(self):
        """The maximum number of interns a player can have.

        :rtype: int
        """
        return self._intern_cap

    @property
    def jobs(self):
        """A list of all jobs. first item is intern, second is physicists, and third is manager.

        :rtype: list[games.newtonian.job.Job]
        """
        return self._jobs

    @property
    def machines(self):
        """Every Machine in the game.

        :rtype: list[games.newtonian.machine.Machine]
        """
        return self._machines

    @property
    def manager_cap(self):
        """The maximum number of managers a player can have.

        :rtype: int
        """
        return self._manager_cap

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
    def material_spawn(self):
        """The number of materials that spawn per spawn cycle.

        :rtype: int
        """
        return self._material_spawn

    @property
    def max_turns(self):
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns

    @property
    def physicist_cap(self):
        """The maximum number of physicists a player can have.

        :rtype: int
        """
        return self._physicist_cap

    @property
    def players(self):
        """List of all the players in the game.

        :rtype: list[games.newtonian.player.Player]
        """
        return self._players

    @property
    def refined_value(self):
        """The amount of victory points added when a refined ore is consumed by the generator.

        :rtype: int
        """
        return self._refined_value

    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def spawn_time(self):
        """The amount of turns it takes a unit to spawn.

        :rtype: int
        """
        return self._spawn_time

    @property
    def stun_time(self):
        """The amount of turns a unit cannot do anything when stunned.

        :rtype: int
        """
        return self._stun_time

    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[games.newtonian.tile.Tile]
        """
        return self._tiles

    @property
    def time_added_per_turn(self):
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn

    @property
    def time_immune(self):
        """The number turns a unit is immune to being stunned.

        :rtype: int
        """
        return self._time_immune

    @property
    def units(self):
        """Every Unit in the game.

        :rtype: list[games.newtonian.unit.Unit]
        """
        return self._units

    @property
    def victory_amount(self):
        """The amount of combined heat and pressure that you need to win.

        :rtype: int
        """
        return self._victory_amount


    def get_tile_at(self, x, y):
        """Gets the Tile at a specified (x, y) position
        Args:
            x (int): integer between 0 and the map_width
            y (int): integer between 0 and the map_height
        Returns:
            games.newtonian.tile.Tile: the Tile at (x, y) or None if out of bounds
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
