# Machine: A machine on a tile.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.newtonian.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Machine(GameObject):
    """The class representing the Machine in the Newtonian game.

    A machine on a tile.
    """

    def __init__(self):
        """Initializes a Machine with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._input = 0
        self._ore_type = ""
        self._output = 0
        self._refine_input = 0
        self._refine_output = 0
        self._refine_time = 0
        self._tile = None
        self._time_left = 0
        self._worked = 0

    @property
    def input(self):
        """The amount of ore that is in the machine. Cannot be higher than the refineInput value.

        :rtype: int
        """
        return self._input

    @property
    def ore_type(self):
        """What type of ore the machine takes it, also determins the type of material it outputs.

        :rtype: str
        """
        return self._ore_type

    @property
    def output(self):
        """The amount of material that is waiting to be collected in the machine.

        :rtype: int
        """
        return self._output

    @property
    def refine_input(self):
        """The amount of ore that needs to be inputted into the machine.

        :rtype: int
        """
        return self._refine_input

    @property
    def refine_output(self):
        """The amount of material that out of the machine after running.

        :rtype: int
        """
        return self._refine_output

    @property
    def refine_time(self):
        """The amount of turns this machine takes to refine the ore.

        :rtype: int
        """
        return self._refine_time

    @property
    def tile(self):
        """The Tile this Machine is on.

        :rtype: games.newtonian.tile.Tile
        """
        return self._tile

    @property
    def time_left(self):
        """Time till the machine finishes running.

        :rtype: int
        """
        return self._time_left

    @property
    def worked(self):
        """Tracks how many times this machine has been worked.

        :rtype: int
        """
        return self._worked



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
