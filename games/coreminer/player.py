# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List
from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Coreminer game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._base_tile = None
        self._bombs = []
        self._client_type = ""
        self._hopper_tiles = []
        self._lost = False
        self._miners = []
        self._money = 0
        self._name = "Anonymous"
        self._opponent = None
        self._reason_lost = ""
        self._reason_won = ""
        self._time_remaining = 0
        self._value = 0
        self._won = False

    @property
    def base_tile(self) -> 'games.coreminer.tile.Tile':
        """games.coreminer.tile.Tile: The Tile this Player's base is on.
        """
        return self._base_tile

    @property
    def bombs(self) -> List['games.coreminer.bomb.Bomb']:
        """list[games.coreminer.bomb.Bomb]: Every Bomb owned by this Player.
        """
        return self._bombs

    @property
    def client_type(self) -> str:
        """str: What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.
        """
        return self._client_type

    @property
    def hopper_tiles(self) -> List['games.coreminer.tile.Tile']:
        """list[games.coreminer.tile.Tile]: The Tiles this Player's hoppers are on.
        """
        return self._hopper_tiles

    @property
    def lost(self) -> bool:
        """bool: If the player lost the game or not.
        """
        return self._lost

    @property
    def miners(self) -> List['games.coreminer.miner.Miner']:
        """list[games.coreminer.miner.Miner]: Every Miner owned by this Player.
        """
        return self._miners

    @property
    def money(self) -> int:
        """int: The amount of money this Player currently has.
        """
        return self._money

    @property
    def name(self) -> str:
        """str: The name of the player.
        """
        return self._name

    @property
    def opponent(self) -> 'games.coreminer.player.Player':
        """games.coreminer.player.Player: This player's opponent in the game.
        """
        return self._opponent

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
    def time_remaining(self) -> float:
        """float: The amount of time (in ns) remaining for this AI to send commands.
        """
        return self._time_remaining

    @property
    def value(self) -> int:
        """int: The amount of value (victory points) this Player has gained.
        """
        return self._value

    @property
    def won(self) -> bool:
        """bool: If the player won the game or not.
        """
        return self._won

    def spawn_miner(self) -> bool:
        """Spawns a Miner on this Player's base Tile.

        Returns:
            bool: True if successfully spawned, False otherwise.
        """
        return self._run_on_server('spawnMiner', {

        })


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
