# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List
from games.spiders.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Spiders game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._brood_mother = None
        self._client_type = ""
        self._lost = False
        self._max_spiderlings = 0
        self._name = "Anonymous"
        self._number_of_nests_controlled = 0
        self._opponent = None
        self._reason_lost = ""
        self._reason_won = ""
        self._spiders = []
        self._time_remaining = 0
        self._won = False

    @property
    def brood_mother(self) -> 'games.spiders.brood_mother.BroodMother':
        """games.spiders.brood_mother.BroodMother: This player's BroodMother. If it dies they lose the game.
        """
        return self._brood_mother

    @property
    def client_type(self) -> str:
        """str: What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.
        """
        return self._client_type

    @property
    def lost(self) -> bool:
        """bool: If the player lost the game or not.
        """
        return self._lost

    @property
    def max_spiderlings(self) -> int:
        """int: The max number of Spiderlings players can spawn.
        """
        return self._max_spiderlings

    @property
    def name(self) -> str:
        """str: The name of the player.
        """
        return self._name

    @property
    def number_of_nests_controlled(self) -> int:
        """int: The number of nests this player controls.
        """
        return self._number_of_nests_controlled

    @property
    def opponent(self) -> 'games.spiders.player.Player':
        """games.spiders.player.Player: This player's opponent in the game.
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
    def spiders(self) -> List['games.spiders.spider.Spider']:
        """list[games.spiders.spider.Spider]: All the Spiders owned by this player.
        """
        return self._spiders

    @property
    def time_remaining(self) -> float:
        """float: The amount of time (in ns) remaining for this AI to send commands.
        """
        return self._time_remaining

    @property
    def won(self) -> bool:
        """bool: If the player won the game or not.
        """
        return self._won

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
