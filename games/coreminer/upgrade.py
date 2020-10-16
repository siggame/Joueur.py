# Upgrade: Information about a Miner's Upgrade module.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Upgrade(GameObject):
    """The class representing the Upgrade in the Coreminer game.

    Information about a Miner's Upgrade module.
    """

    def __init__(self):
        """Initializes a Upgrade with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._cargo_capacity = 0
        self._health = 0
        self._mining_power = 0
        self._moves = 0
        self._title = ""

    @property
    def cargo_capacity(self):
        """The amount of cargo capacity this Upgrade has.

        :rtype: int
        """
        return self._cargo_capacity

    @property
    def health(self):
        """The maximum amount of health this Upgrade has.

        :rtype: int
        """
        return self._health

    @property
    def mining_power(self):
        """The amount of mining power this Upgrade has per turn.

        :rtype: int
        """
        return self._mining_power

    @property
    def moves(self):
        """The number of moves this Upgrade can make per turn.

        :rtype: int
        """
        return self._moves

    @property
    def title(self):
        """The Upgrade title.

        :rtype: str
        """
        return self._title



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
