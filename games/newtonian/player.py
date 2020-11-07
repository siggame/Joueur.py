# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List
from games.newtonian.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Newtonian game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._client_type = ""
        self._generator_tiles = []
        self._heat = 0
        self._intern_spawn = 0
        self._lost = False
        self._manager_spawn = 0
        self._name = "Anonymous"
        self._opponent = None
        self._physicist_spawn = 0
        self._pressure = 0
        self._reason_lost = ""
        self._reason_won = ""
        self._spawn_tiles = []
        self._time_remaining = 0
        self._units = []
        self._won = False

    @property
    def client_type(self) -> str:
        """str: What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.
        """
        return self._client_type

    @property
    def generator_tiles(self) -> List['games.newtonian.tile.Tile']:
        """list[games.newtonian.tile.Tile]: Every generator Tile owned by this Player. (listed from the outer edges inward, from top to bottom).
        """
        return self._generator_tiles

    @property
    def heat(self) -> int:
        """int: The amount of heat this Player has.
        """
        return self._heat

    @property
    def intern_spawn(self) -> int:
        """int: The time left till a intern spawns. (0 to spawnTime).
        """
        return self._intern_spawn

    @property
    def lost(self) -> bool:
        """bool: If the player lost the game or not.
        """
        return self._lost

    @property
    def manager_spawn(self) -> int:
        """int: The time left till a manager spawns. (0 to spawnTime).
        """
        return self._manager_spawn

    @property
    def name(self) -> str:
        """str: The name of the player.
        """
        return self._name

    @property
    def opponent(self) -> 'games.newtonian.player.Player':
        """games.newtonian.player.Player: This player's opponent in the game.
        """
        return self._opponent

    @property
    def physicist_spawn(self) -> int:
        """int: The time left till a physicist spawns. (0 to spawnTime).
        """
        return self._physicist_spawn

    @property
    def pressure(self) -> int:
        """int: The amount of pressure this Player has.
        """
        return self._pressure

    @property
    def reason_lost(self) -> str:
        """str: The reason why the player lost the game.
        """
        return self._reason_lost

    @property
    def reason_won(self) -> str:
        """str: The reason why the player won the game.
        """
        return self._reason_won

    @property
    def spawn_tiles(self) -> List['games.newtonian.tile.Tile']:
        """list[games.newtonian.tile.Tile]: All the tiles this Player's units can spawn on. (listed from the outer edges inward, from top to bottom).
        """
        return self._spawn_tiles

    @property
    def time_remaining(self) -> float:
        """float: The amount of time (in ns) remaining for this AI to send commands.
        """
        return self._time_remaining

    @property
    def units(self) -> List['games.newtonian.unit.Unit']:
        """list[games.newtonian.unit.Unit]: Every Unit owned by this Player.
        """
        return self._units

    @property
    def won(self) -> bool:
        """bool: If the player won the game or not.
        """
        return self._won


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
