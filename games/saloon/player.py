# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List
from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Saloon game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._client_type = ""
        self._cowboys = []
        self._kills = 0
        self._lost = False
        self._name = "Anonymous"
        self._opponent = None
        self._reason_lost = ""
        self._reason_won = ""
        self._rowdiness = 0
        self._score = 0
        self._siesta = 0
        self._time_remaining = 0
        self._won = False
        self._young_gun = None

    @property
    def client_type(self) -> str:
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.

        :rtype: str
        """
        return self._client_type

    @property
    def cowboys(self) -> List['games.saloon.cowboy.Cowboy']:
        """Every Cowboy owned by this Player.

        :rtype: list[games.saloon.cowboy.Cowboy]
        """
        return self._cowboys

    @property
    def kills(self) -> int:
        """How many enemy Cowboys this player's team has killed.

        :rtype: int
        """
        return self._kills

    @property
    def lost(self) -> bool:
        """If the player lost the game or not.

        :rtype: bool
        """
        return self._lost

    @property
    def name(self) -> str:
        """The name of the player.

        :rtype: str
        """
        return self._name

    @property
    def opponent(self) -> 'games.saloon.player.Player':
        """This player's opponent in the game.

        :rtype: games.saloon.player.Player
        """
        return self._opponent

    @property
    def reason_lost(self) -> str:
        """The reason why the player lost the game.

        :rtype: str
        """
        return self._reason_lost

    @property
    def reason_won(self) -> str:
        """The reason why the player won the game.

        :rtype: str
        """
        return self._reason_won

    @property
    def rowdiness(self) -> int:
        """How rowdy their team is. When it gets too high their team takes a collective siesta.

        :rtype: int
        """
        return self._rowdiness

    @property
    def score(self) -> int:
        """How many times their team has played a piano.

        :rtype: int
        """
        return self._score

    @property
    def siesta(self) -> int:
        """0 when not having a team siesta. When greater than 0 represents how many turns left for the team siesta to complete.

        :rtype: int
        """
        return self._siesta

    @property
    def time_remaining(self) -> float:
        """The amount of time (in ns) remaining for this AI to send commands.

        :rtype: float
        """
        return self._time_remaining

    @property
    def won(self) -> bool:
        """If the player won the game or not.

        :rtype: bool
        """
        return self._won

    @property
    def young_gun(self) -> 'games.saloon.young_gun.YoungGun':
        """The YoungGun this Player uses to call in new Cowboys.

        :rtype: games.saloon.young_gun.YoungGun
        """
        return self._young_gun


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
