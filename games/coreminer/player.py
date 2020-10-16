# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Coreminer game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator."""
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
    def base_tile(self):
        """The Tile this Player's base is on.

        :rtype: games.coreminer.tile.Tile
        """
        return self._base_tile

    @property
    def bombs(self):
        """Every Bomb owned by this Player.

        :rtype: list[games.coreminer.bomb.Bomb]
        """
        return self._bombs

    @property
    def client_type(self):
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.

        :rtype: str
        """
        return self._client_type

    @property
    def hopper_tiles(self):
        """The Tiles this Player's hoppers are on.

        :rtype: list[games.coreminer.tile.Tile]
        """
        return self._hopper_tiles

    @property
    def lost(self):
        """If the player lost the game or not.

        :rtype: bool
        """
        return self._lost

    @property
    def miners(self):
        """Every Miner owned by this Player.

        :rtype: list[games.coreminer.miner.Miner]
        """
        return self._miners

    @property
    def money(self):
        """The amount of money this Player currently has.

        :rtype: int
        """
        return self._money

    @property
    def name(self):
        """The name of the player.

        :rtype: str
        """
        return self._name

    @property
    def opponent(self):
        """This player's opponent in the game.

        :rtype: games.coreminer.player.Player
        """
        return self._opponent

    @property
    def reason_lost(self):
        """The reason why the player lost the game.

        :rtype: str
        """
        return self._reason_lost

    @property
    def reason_won(self):
        """The reason why the player won the game.

        :rtype: str
        """
        return self._reason_won

    @property
    def time_remaining(self):
        """The amount of time (in ns) remaining for this AI to send commands.

        :rtype: float
        """
        return self._time_remaining

    @property
    def value(self):
        """The amount of value (victory points) this Player has gained.

        :rtype: int
        """
        return self._value

    @property
    def won(self):
        """If the player won the game or not.

        :rtype: bool
        """
        return self._won

    def spawn_miner(self):
        """ Spawns a Miner on this Player's base Tile.

        Returns:
            bool: True if successfully spawned, False otherwise.
        """
        return self._run_on_server('spawnMiner')



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
