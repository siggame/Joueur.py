# Job: Information about a unit's job.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.stardash.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Job(GameObject):
    """The class representing the Job in the Stardash game.

    Information about a unit's job.
    """

    def __init__(self):
        """Initializes a Job with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._carry_limit = 0
        self._damage = 0
        self._energy = 0
        self._moves = 0
        self._range = 0
        self._shield = 0
        self._title = ""
        self._unit_cost = 0

    @property
    def carry_limit(self) -> int:
        """How many combined resources a unit with this Job can hold at once.

        :rtype: int
        """
        return self._carry_limit

    @property
    def damage(self) -> int:
        """The amount of damage this Job does per attack.

        :rtype: int
        """
        return self._damage

    @property
    def energy(self) -> int:
        """The amount of starting health this Job has.

        :rtype: int
        """
        return self._energy

    @property
    def moves(self) -> int:
        """The distance this job can move per turn.

        :rtype: int
        """
        return self._moves

    @property
    def range(self) -> int:
        """The distance at which this job can effect things.

        :rtype: int
        """
        return self._range

    @property
    def shield(self) -> int:
        """The reserve the martyr use to protect allies.

        :rtype: int
        """
        return self._shield

    @property
    def title(self) -> str:
        """The Job title. 'corvette', 'missileboat', 'martyr', 'transport', or 'miner'. (in this order from 0-4).

        :rtype: 'corvette', 'missileboat', 'martyr', 'transport', or 'miner'
        """
        return self._title

    @property
    def unit_cost(self) -> int:
        """How much money it costs to spawn a unit.

        :rtype: int
        """
        return self._unit_cost

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
