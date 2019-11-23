# Job: Information about a Unit's job.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.catastrophe.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Job(GameObject):
    """The class representing the Job in the Catastrophe game.

    Information about a Unit's job.
    """

    def __init__(self):
        """Initializes a Job with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._action_cost = 0
        self._carry_limit = 0
        self._moves = 0
        self._regen_rate = 0
        self._title = ""
        self._upkeep = 0

    @property
    def action_cost(self) -> float:
        """The amount of energy this Job normally uses to perform its actions.

        :rtype: float
        """
        return self._action_cost

    @property
    def carry_limit(self) -> int:
        """How many combined resources a Unit with this Job can hold at once.

        :rtype: int
        """
        return self._carry_limit

    @property
    def moves(self) -> int:
        """The number of moves this Job can make per turn.

        :rtype: int
        """
        return self._moves

    @property
    def regen_rate(self) -> float:
        """The amount of energy normally regenerated when resting at a shelter.

        :rtype: float
        """
        return self._regen_rate

    @property
    def title(self) -> str:
        """The Job title.

        :rtype: 'fresh human', 'cat overlord', 'soldier', 'gatherer', 'builder', or missionary
        """
        return self._title

    @property
    def upkeep(self) -> int:
        """The amount of food per turn this Unit consumes. If there isn't enough food for every Unit, all Units become starved and do not consume food.

        :rtype: int
        """
        return self._upkeep


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
