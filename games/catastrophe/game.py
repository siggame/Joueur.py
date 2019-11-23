# Game: Convert as many humans to as you can to survive in this post-apocalyptic wasteland.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List, Optional
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
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._cat_energy_mult = 0
        self._current_player = None
        self._current_turn = 0
        self._game_objects = {}
        self._harvest_cooldown = 0
        self._jobs = []
        self._lower_harvest_amount = 0
        self._map_height = 0
        self._map_width = 0
        self._max_turns = 100
        self._monument_cost_mult = 0
        self._monument_materials = 0
        self._neutral_materials = 0
        self._players = []
        self._session = ""
        self._shelter_materials = 0
        self._starting_food = 0
        self._starving_energy_mult = 0
        self._structures = []
        self._tiles = []
        self._time_added_per_turn = 0
        self._turns_between_harvests = 0
        self._turns_to_create_human = 0
        self._turns_to_lower_harvest = 0
        self._units = []
        self._wall_materials = 0

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
    def cat_energy_mult(self) -> float:
        """The multiplier for the amount of energy regenerated when resting in a shelter with the cat overlord.

        :rtype: float
        """
        return self._cat_energy_mult

    @property
    def current_player(self) -> 'games.catastrophe.player.Player':
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.catastrophe.player.Player
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn

    @property
    def game_objects(self) -> Dict[str, 'games.catastrophe.game_object.GameObject']:
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, games.catastrophe.game_object.GameObject]
        """
        return self._game_objects

    @property
    def harvest_cooldown(self) -> int:
        """The amount of turns it takes for a Tile that was just harvested to grow food again.

        :rtype: int
        """
        return self._harvest_cooldown

    @property
    def jobs(self) -> List['games.catastrophe.job.Job']:
        """All the Jobs that Units can have in the game.

        :rtype: list[games.catastrophe.job.Job]
        """
        return self._jobs

    @property
    def lower_harvest_amount(self) -> int:
        """The amount that the harvest rate is lowered each season.

        :rtype: int
        """
        return self._lower_harvest_amount

    @property
    def map_height(self) -> int:
        """The number of Tiles in the map along the y (vertical) axis.

        :rtype: int
        """
        return self._map_height

    @property
    def map_width(self) -> int:
        """The number of Tiles in the map along the x (horizontal) axis.

        :rtype: int
        """
        return self._map_width

    @property
    def max_turns(self) -> int:
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns

    @property
    def monument_cost_mult(self) -> float:
        """The multiplier for the cost of actions when performing them in range of a monument. Does not effect pickup cost.

        :rtype: float
        """
        return self._monument_cost_mult

    @property
    def monument_materials(self) -> int:
        """The number of materials in a monument.

        :rtype: int
        """
        return self._monument_materials

    @property
    def neutral_materials(self) -> int:
        """The number of materials in a neutral Structure.

        :rtype: int
        """
        return self._neutral_materials

    @property
    def players(self) -> List['games.catastrophe.player.Player']:
        """List of all the players in the game.

        :rtype: list[games.catastrophe.player.Player]
        """
        return self._players

    @property
    def session(self) -> str:
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def shelter_materials(self) -> int:
        """The number of materials in a shelter.

        :rtype: int
        """
        return self._shelter_materials

    @property
    def starting_food(self) -> int:
        """The amount of food Players start with.

        :rtype: int
        """
        return self._starting_food

    @property
    def starving_energy_mult(self) -> float:
        """The multiplier for the amount of energy regenerated when resting while starving.

        :rtype: float
        """
        return self._starving_energy_mult

    @property
    def structures(self) -> List['games.catastrophe.structure.Structure']:
        """Every Structure in the game.

        :rtype: list[games.catastrophe.structure.Structure]
        """
        return self._structures

    @property
    def tiles(self) -> List['games.catastrophe.tile.Tile']:
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[games.catastrophe.tile.Tile]
        """
        return self._tiles

    @property
    def time_added_per_turn(self) -> int:
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn

    @property
    def turns_between_harvests(self) -> int:
        """After a food tile is harvested, the number of turns before it can be harvested again.

        :rtype: int
        """
        return self._turns_between_harvests

    @property
    def turns_to_create_human(self) -> int:
        """The number of turns between fresh humans being spawned on the road.

        :rtype: int
        """
        return self._turns_to_create_human

    @property
    def turns_to_lower_harvest(self) -> int:
        """The number of turns before the harvest rate is lowered (length of each season basically).

        :rtype: int
        """
        return self._turns_to_lower_harvest

    @property
    def units(self) -> List['games.catastrophe.unit.Unit']:
        """Every Unit in the game.

        :rtype: list[games.catastrophe.unit.Unit]
        """
        return self._units

    @property
    def wall_materials(self) -> int:
        """The number of materials in a wall.

        :rtype: int
        """
        return self._wall_materials

    def get_tile_at(self, x: int, y: int) -> Optional['games.catastrophe.tile.Tile']:
        """Gets the Tile at a specified (x, y) position.

        Args:
            x (int): An integer between 0 and the map_width.
            y (int): An integer between 0 and the map_height.

        Returns:
            games.catastrophe.tile.Tile or None: The Tile at (x, y) or None if out of bounds.
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
