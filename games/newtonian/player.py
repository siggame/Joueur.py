# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.newtonian.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Newtonian game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator."""
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
        self._time_remaining = 0
        self._units = []
        self._won = False

    @property
    def client_type(self):
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.

        :rtype: str
        """
        return self._client_type

    @property
    def generator_tiles(self):
        """Every generator tile owned by this Player.

        :rtype: list[games.newtonian.tile.Tile]
        """
        return self._generator_tiles

    @property
    def heat(self):
        """The amount of heat this Player has.

        :rtype: int
        """
        return self._heat

    @property
    def intern_spawn(self):
        """Time left till a intern spawns.

        :rtype: int
        """
        return self._intern_spawn

    @property
    def lost(self):
        """If the player lost the game or not.

        :rtype: bool
        """
        return self._lost

    @property
    def manager_spawn(self):
        """Time left till a manager spawns.

        :rtype: int
        """
        return self._manager_spawn

    @property
    def name(self):
        """The name of the player.

        :rtype: str
        """
        return self._name

    @property
    def opponent(self):
        """This player's opponent in the game.

        :rtype: games.newtonian.player.Player
        """
        return self._opponent

    @property
    def physicist_spawn(self):
        """Time left till a physicist spawns.

        :rtype: int
        """
        return self._physicist_spawn

    @property
    def pressure(self):
        """The amount of pressure this Player has.

        :rtype: int
        """
        return self._pressure

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
    def units(self):
        """Every Unit owned by this Player.

        :rtype: list[games.newtonian.unit.Unit]
        """
        return self._units

    @property
    def won(self):
        """If the player won the game or not.

        :rtype: bool
        """
        return self._won



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
