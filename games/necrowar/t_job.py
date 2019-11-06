# tJob: Information about a tower's job/type.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.necrowar.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class tJob(GameObject):
    """The class representing the tJob in the Necrowar game.

    Information about a tower's job/type.
    """

    def __init__(self):
        """Initializes a tJob with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._all_units = False
        self._damage = 0
        self._gold_cost = 0
        self._health = 0
        self._mana_cost = 0
        self._range = 0
        self._title = ""
        self._turns_between_attacks = 0

    @property
    def all_units(self):
        """Whether this tower type hits all of the units on a tile (True) or one at a time (False).

        :rtype: bool
        """
        return self._all_units

    @property
    def damage(self):
        """How much damage this tower type does in a single turn of attack.

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
    def range(self):
        """The number of tiles this type can attack from.

        :rtype: int
        """
        return self._range

    @property
    def title(self):
        """The type title. 'arrow', 'aoe', 'ballista', or 'cleansing'.

        :rtype: str
        """
        return self._title

    @property
    def turns_between_attacks(self):
        """How many turns this tower type needs to take between attacks.

        :rtype: int
        """
        return self._turns_between_attacks



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
