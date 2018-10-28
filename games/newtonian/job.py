# Job: Information about a unit's job.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.newtonian.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Job(GameObject):
    """The class representing the Job in the Newtonian game.

    Information about a unit's job.
    """

    def __init__(self):
        """Initializes a Job with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._carry_limit = 0
        self._damage = 0
        self._health = 0
        self._moves = 0
        self._title = ""

    @property
    def carry_limit(self):
        """How many combined resources a unit with this Job can hold at once.

        :rtype: int
        """
        return self._carry_limit

    @property
    def damage(self):
        """The amount of damage this Job does per attack.

        :rtype: int
        """
        return self._damage

    @property
    def health(self):
        """The amount of starting health this Job has.

        :rtype: int
        """
        return self._health

    @property
    def moves(self):
        """The number of moves this Job can make per turn.

        :rtype: int
        """
        return self._moves

    @property
    def title(self):
        """The Job title. 'intern', 'manager', or 'physicist'.

        :rtype: str
        """
        return self._title



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
