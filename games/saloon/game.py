# Game: Use cowboys to have a good time and play some music on a Piano, while brawling with enemy Cowboys.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List, Optional
from joueur.base_game import BaseGame

# import game objects
from games.saloon.bottle import Bottle
from games.saloon.cowboy import Cowboy
from games.saloon.furnishing import Furnishing
from games.saloon.game_object import GameObject
from games.saloon.player import Player
from games.saloon.tile import Tile
from games.saloon.young_gun import YoungGun

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Saloon game.

    Use cowboys to have a good time and play some music on a Piano, while brawling with enemy Cowboys.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bartender_cooldown = 0
        self._bottles = []
        self._brawler_damage = 0
        self._cowboys = []
        self._current_player = None
        self._current_turn = 0
        self._furnishings = []
        self._game_objects = {}
        self._jobs = []
        self._map_height = 0
        self._map_width = 0
        self._max_cowboys_per_job = 0
        self._max_turns = 100
        self._players = []
        self._rowdiness_to_siesta = 0
        self._session = ""
        self._sharpshooter_damage = 0
        self._siesta_length = 0
        self._tiles = []
        self._time_added_per_turn = 0
        self._turns_drunk = 0

        self.name = "Saloon"

        self._game_object_classes = {
            'Bottle': Bottle,
            'Cowboy': Cowboy,
            'Furnishing': Furnishing,
            'GameObject': GameObject,
            'Player': Player,
            'Tile': Tile,
            'YoungGun': YoungGun
        }

    @property
    def bartender_cooldown(self) -> int:
        """int: How many turns a Bartender will be busy for after throwing a Bottle.
        """
        return self._bartender_cooldown

    @property
    def bottles(self) -> List['games.saloon.bottle.Bottle']:
        """list[games.saloon.bottle.Bottle]: All the beer Bottles currently flying across the saloon in the game.
        """
        return self._bottles

    @property
    def brawler_damage(self) -> int:
        """int: How much damage is applied to neighboring things bit by the Sharpshooter between turns.
        """
        return self._brawler_damage

    @property
    def cowboys(self) -> List['games.saloon.cowboy.Cowboy']:
        """list[games.saloon.cowboy.Cowboy]: Every Cowboy in the game.
        """
        return self._cowboys

    @property
    def current_player(self) -> 'games.saloon.player.Player':
        """games.saloon.player.Player: The player whose turn it is currently. That player can send commands. Other players cannot.
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """int: The current turn number, starting at 0 for the first player's turn.
        """
        return self._current_turn

    @property
    def furnishings(self) -> List['games.saloon.furnishing.Furnishing']:
        """list[games.saloon.furnishing.Furnishing]: Every furnishing in the game.
        """
        return self._furnishings

    @property
    def game_objects(self) -> Dict[str, 'games.saloon.game_object.GameObject']:
        """dict[str, games.saloon.game_object.GameObject]: A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        """
        return self._game_objects

    @property
    def jobs(self) -> List[str]:
        """list[str]: All the jobs that Cowboys can be called in with.
        """
        return self._jobs

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
    def max_cowboys_per_job(self) -> int:
        """int: The maximum number of Cowboys a Player can bring into the saloon of each specific job.
        """
        return self._max_cowboys_per_job

    @property
    def max_turns(self) -> int:
        """int: The maximum number of turns before the game will automatically end.
        """
        return self._max_turns

    @property
    def players(self) -> List['games.saloon.player.Player']:
        """list[games.saloon.player.Player]: List of all the players in the game.
        """
        return self._players

    @property
    def rowdiness_to_siesta(self) -> int:
        """int: When a player's rowdiness reaches or exceeds this number their Cowboys take a collective siesta.
        """
        return self._rowdiness_to_siesta

    @property
    def session(self) -> str:
        """str: A unique identifier for the game instance that is being played.
        """
        return self._session

    @property
    def sharpshooter_damage(self) -> int:
        """int: How much damage is applied to things hit by Sharpshooters when they act.
        """
        return self._sharpshooter_damage

    @property
    def siesta_length(self) -> int:
        """int: How long siestas are for a player's team.
        """
        return self._siesta_length

    @property
    def tiles(self) -> List['games.saloon.tile.Tile']:
        """list[games.saloon.tile.Tile]: All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.
        """
        return self._tiles

    @property
    def time_added_per_turn(self) -> int:
        """int: The amount of time (in nano-seconds) added after each player performs a turn.
        """
        return self._time_added_per_turn

    @property
    def turns_drunk(self) -> int:
        """int: How many turns a Cowboy will be drunk for if a bottle breaks on it.
        """
        return self._turns_drunk

    def get_tile_at(self, x: int, y: int) -> Optional['games.saloon.tile.Tile']:
        """Gets the Tile at a specified (x, y) position.

        Args:
            x (int): An integer between 0 and the map_width.
            y (int): An integer between 0 and the map_height.

        Returns:
            games.saloon.tile.Tile or None: The Tile at (x, y) or None if out of bounds.
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
