# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List
from games.catastrophe.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Catastrophe game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._cat = None
        self._client_type = ""
        self._food = 0
        self._lost = False
        self._name = "Anonymous"
        self._opponent = None
        self._reason_lost = ""
        self._reason_won = ""
        self._structures = []
        self._time_remaining = 0
        self._units = []
        self._upkeep = 0
        self._won = False

    @property
    def cat(self) -> 'games.catastrophe.unit.Unit':
        """games.catastrophe.unit.Unit: The overlord cat Unit owned by this Player.
        """
        return self._cat

    @property
    def client_type(self) -> str:
        """str: What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.
        """
        return self._client_type

    @property
    def food(self) -> int:
        """int: The amount of food owned by this player.
        """
        return self._food

    @property
    def lost(self) -> bool:
        """bool: If the player lost the game or not.
        """
        return self._lost

    @property
    def name(self) -> str:
        """str: The name of the player.
        """
        return self._name

    @property
    def opponent(self) -> 'games.catastrophe.player.Player':
        """games.catastrophe.player.Player: This player's opponent in the game.
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
    def structures(self) -> List['games.catastrophe.structure.Structure']:
        """list[games.catastrophe.structure.Structure]: Every Structure owned by this Player.
        """
        return self._structures

    @property
    def time_remaining(self) -> float:
        """float: The amount of time (in ns) remaining for this AI to send commands.
        """
        return self._time_remaining

    @property
    def units(self) -> List['games.catastrophe.unit.Unit']:
        """list[games.catastrophe.unit.Unit]: Every Unit owned by this Player.
        """
        return self._units

    @property
    def upkeep(self) -> int:
        """int: The total upkeep of every Unit owned by this Player. If there isn't enough food for every Unit, all Units become starved and do not consume food.
        """
        return self._upkeep

    @property
    def won(self) -> bool:
        """bool: If the player won the game or not.
        """
        return self._won


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
