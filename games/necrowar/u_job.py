# uJob: Information about a unit's job/type.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.necrowar.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class uJob(GameObject):
    """The class representing the uJob in the Necrowar game.

    Information about a unit's job/type.
    """

    def __init__(self):
        """Initializes a uJob with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._damage = 0
        self._gold_cost = 0
        self._health = 0
        self._mana_cost = 0
        self._moves = 0
        self._per_tile = 0
        self._range = 0
        self._title = ""

    @property
    def damage(self):
        """The amount of damage this type does per attack.

        :rtype: int
        """
        return self._damage

    @property
    def gold_cost(self):
        """How much does this type cost in gold.

        :rtype: int
        """
        return self._gold_cost

    @property
    def health(self):
        """The amount of starting health this type has.

        :rtype: int
        """
        return self._health

    @property
    def mana_cost(self):
        """How much does this type cost in mana.

        :rtype: int
        """
        return self._mana_cost

    @property
    def moves(self):
        """The number of moves this type can make per turn.

        :rtype: int
        """
        return self._moves

    @property
    def per_tile(self):
        """How many of this type of unit can take up one tile.

        :rtype: int
        """
        return self._per_tile

    @property
    def range(self):
        """Amount of tiles away this type has to be in order to be effective.

        :rtype: int
        """
        return self._range

    @property
    def title(self):
        """The type title. 'worker', 'zombie', 'ghoul', 'hound', 'abomination', 'wraith' or 'horseman'.

        :rtype: str
        """
        return self._title



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
