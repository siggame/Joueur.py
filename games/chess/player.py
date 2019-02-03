# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.chess.game_object import GameObject

class Player(GameObject):
    """The class representing the Player in the Chess game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._client_type = ""
        self._color = ""
        self._lost = False
        self._name = "Anonymous"
        self._opponent = None
        self._reason_lost = ""
        self._reason_won = ""
        self._time_remaining = 0
        self._won = False

    @property
    def client_type(self):
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.

        :rtype: str
        """
        return self._client_type

    @property
    def color(self):
        """The color (side) of this player. Either 'white' or 'black', with the 'white' player having the first move.

        :rtype: str
        """
        return self._color

    @property
    def lost(self):
        """If the player lost the game or not.

        :rtype: bool
        """
        return self._lost

    @property
    def name(self):
        """The name of the player.

        :rtype: str
        """
        return self._name

    @property
    def opponent(self):
        """This player's opponent in the game.

        :rtype: games.chess.player.Player
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
    def won(self):
        """If the player won the game or not.

        :rtype: bool
        """
        return self._won
