# Job: Information about a beaver's job.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.stumped.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Job(GameObject):
    """The class representing the Job in the Stumped game.

    Information about a beaver's job.
    """

    def __init__(self):
        """Initializes a Job with basic logic as provided by the Creer code generator.
        """
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
    def actions(self) -> int:
        """int: The number of actions this Job can make per turn.
        """
        return self._actions

    @property
    def carry_limit(self) -> int:
        """int: How many combined resources a beaver with this Job can hold at once.
        """
        return self._carry_limit

    @property
    def chopping(self) -> int:
        """int: Scalar for how many branches this Job harvests at once.
        """
        return self._chopping

    @property
    def cost(self) -> int:
        """int: How much food this Job costs to recruit.
        """
        return self._cost

    @property
    def damage(self) -> int:
        """int: The amount of damage this Job does per attack.
        """
        return self._damage

    @property
    def distraction_power(self) -> int:
        """int: How many turns a beaver attacked by this Job is distracted by.
        """
        return self._distraction_power

    @property
    def health(self) -> int:
        """int: The amount of starting health this Job has.
        """
        return self._health

    @property
    def moves(self) -> int:
        """int: The number of moves this Job can make per turn.
        """
        return self._moves

    @property
    def munching(self) -> int:
        """int: Scalar for how much food this Job harvests at once.
        """
        return self._munching

    @property
    def title(self) -> str:
        """str: The Job title.
        """
        return self._title

    def recruit(self, tile: 'games.stumped.tile.Tile') -> Optional['games.stumped.beaver.Beaver']:
        """Recruits a Beaver of this Job to a lodge.

        Args:
            tile (games.stumped.tile.Tile): The Tile that is a lodge owned by you that you wish to spawn the Beaver of this Job on.

        Returns:
            games.stumped.beaver.Beaver or None: The recruited Beaver if successful, None otherwise.
        """
        return self._run_on_server('recruit', {
            'tile': tile
        })


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
