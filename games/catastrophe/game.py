# Game: Convert as many humans to as you can to survive in this post-apocalyptic wasteland.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from joueur.base_game import BaseGame

# import game objects
from games.catastrophe.game_object import GameObject
from games.catastrophe.job import Job
from games.catastrophe.player import Player
from games.catastrophe.structure import Structure
from games.catastrophe.tile import Tile
from games.catastrophe.unit import Unit

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Catastrophe game.

    Convert as many humans to as you can to survive in this post-apocalyptic wasteland.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._cat_energy_mult = 0
        self._current_player = None
        self._current_turn = 0
        self._game_objects = {}
        self._harvest_cooldown = 0
        self._jobs = []
        self._map_height = 0
        self._map_width = 0
        self._max_turns = 100
        self._players = []
        self._session = ""
        self._starving_energy_mult = 0
        self._structures = []
        self._tiles = []
        self._units = []

        self.name = "Catastrophe"

        self._game_object_classes = {
            'GameObject': GameObject,
            'Job': Job,
            'Player': Player,
            'Structure': Structure,
            'Tile': Tile,
            'Unit': Unit
        }

    @property
    def cat_energy_mult(self):
        """The multiplier for the amount of energy regenerated when resting in a shelter with the cat overlord.

        :rtype: float
        """
        return self._cat_energy_mult

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
    def harvest_cooldown(self):
        """The amount of turns it takes for a Tile that was just harvested to grow food again.

        :rtype: int
        """
        return self._harvest_cooldown

    @property
    def jobs(self):
        """All the Jobs that Units can have in the game.

        :rtype: list[Job]
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
    def starving_energy_mult(self):
        """The multiplier for the amount of energy regenerated when resting while starving.

        :rtype: float
        """
        return self._starving_energy_mult

    @property
    def structures(self):
        """Every Structure in the game.

        :rtype: list[Structure]
        """
        return self._structures

    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[Tile]
        """
        return self._tiles

    @property
    def units(self):
        """Every Unit in the game.

        :rtype: list[Unit]
        """
        return self._units


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

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
