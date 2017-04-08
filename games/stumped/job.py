# Job: Information about a beaver's job.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.stumped.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Job(GameObject):
    """The class representing the Job in the Stumped game.

    Information about a beaver's job.
    """

    def __init__(self):
        """Initializes a Job with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._actions = 0
        self._carry_limit = 0
        self._chopping = 0
        self._cost = 0
        self._damage = 0
        self._distraction_power = 0
        self._health = 0
        self._moves = 0
        self._munching = 0
        self._title = ""

    @property
    def actions(self):
        """The number of actions this Job can make per turn.

        :rtype: int
        """
        return self._actions

    @property
    def carry_limit(self):
        """How many combined resources a beaver with this Job can hold at once.

        :rtype: int
        """
        return self._carry_limit

    @property
    def chopping(self):
        """Scalar for how many branches this Job harvests at once.

        :rtype: int
        """
        return self._chopping

    @property
    def cost(self):
        """How much food this Job costs to recruit.

        :rtype: int
        """
        return self._cost

    @property
    def damage(self):
        """The amount of damage this Job does per attack.

        :rtype: int
        """
        return self._damage

    @property
    def distraction_power(self):
        """How many turns a beaver attacked by this Job is distracted by.

        :rtype: int
        """
        return self._distraction_power

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
    def munching(self):
        """Scalar for how much food this Job harvests at once.

        :rtype: int
        """
        return self._munching

    @property
    def title(self):
        """The Job title.

        :rtype: str
        """
        return self._title

    def recruit(self, tile):
        """ Recruits a Beaver of this Job to a lodge

        Args:
            tile (Tile): The Tile that is a lodge owned by you that you wish to spawn the Beaver of this Job on.

        Returns:
            Beaver: The recruited Beaver if successful, None otherwise.
        """
        return self._run_on_server('recruit', tile=tile)



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
