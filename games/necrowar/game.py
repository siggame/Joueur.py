# Game: Send hordes of the undead at your opponent while defending yourself against theirs to win.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from joueur.base_game import BaseGame

# import game objects
from games.necrowar.game_object import GameObject
from games.necrowar.player import Player
from games.necrowar.tile import Tile
from games.necrowar.tower import Tower
from games.necrowar.unit import Unit
from games.necrowar.t_job import tJob
from games.necrowar.u_job import uJob

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Necrowar game.

    Send hordes of the undead at your opponent while defending yourself against theirs to win.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._current_player = None
        self._current_turn = 0
        self._game_objects = {}
        self._gold_income_per_unit = 0
        self._island_income_per_unit = 0
        self._mana_income_per_unit = 0
        self._map_height = 0
        self._map_width = 0
        self._max_turns = 100
        self._mine_unit_cap = 0
        self._players = []
        self._river_phase = 0
        self._session = ""
        self._t_jobs = []
        self._tiles = []
        self._time_added_per_turn = 0
        self._towers = []
        self._u_jobs = []
        self._units = []

        self.name = "Necrowar"

        self._game_object_classes = {
            'GameObject': GameObject,
            'Player': Player,
            'Tile': Tile,
            'Tower': Tower,
            'Unit': Unit,
            'tJob': tJob,
            'uJob': uJob
        }

    @property
    def current_player(self):
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.necrowar.player.Player
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

        :rtype: dict[str, games.necrowar.game_object.GameObject]
        """
        return self._game_objects

    @property
    def gold_income_per_unit(self):
        """The amount of gold income per turn per unit in a mine.

        :rtype: int
        """
        return self._gold_income_per_unit

    @property
    def island_income_per_unit(self):
        """The amount of gold income per turn per unit in the island mine.

        :rtype: int
        """
        return self._island_income_per_unit

    @property
    def mana_income_per_unit(self):
        """The Amount of gold income per turn per unit fishing on the river side.

        :rtype: int
        """
        return self._mana_income_per_unit

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
    def mine_unit_cap(self):
        """The maximum number of workers that can occupy a mine at a given time.

        :rtype: int
        """
        return self._mine_unit_cap

    @property
    def players(self):
        """List of all the players in the game.

        :rtype: list[games.necrowar.player.Player]
        """
        return self._players

    @property
    def river_phase(self):
        """The amount of turns it takes between the river changing phases.

        :rtype: int
        """
        return self._river_phase

    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def t_jobs(self):
        """A list of every tower type / job.

        :rtype: list[tJob]
        """
        return self._t_jobs

    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[games.necrowar.tile.Tile]
        """
        return self._tiles

    @property
    def time_added_per_turn(self):
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn

    @property
    def towers(self):
        """Every Tower in the game.

        :rtype: list[games.necrowar.tower.Tower]
        """
        return self._towers

    @property
    def u_jobs(self):
        """A list of every unit type / job.

        :rtype: list[uJob]
        """
        return self._u_jobs

    @property
    def units(self):
        """Every Unit in the game.

        :rtype: list[games.necrowar.unit.Unit]
        """
        return self._units


    def get_tile_at(self, x, y):
        """Gets the Tile at a specified (x, y) position
        Args:
            x (int): integer between 0 and the map_width
            y (int): integer between 0 and the map_height
        Returns:
            games.necrowar.tile.Tile: the Tile at (x, y) or None if out of bounds
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
