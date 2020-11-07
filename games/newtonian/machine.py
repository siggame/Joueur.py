# Machine: A machine in the game. Used to refine ore.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.newtonian.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Machine(GameObject):
    """The class representing the Machine in the Newtonian game.

    A machine in the game. Used to refine ore.
    """

    def __init__(self):
        """Initializes a Machine with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._ore_type = ""
        self._refine_input = 0
        self._refine_output = 0
        self._refine_time = 0
        self._tile = None
        self._worked = 0

    @property
    def ore_type(self) -> str:
        """'redium' or 'blueium': What type of ore the machine takes it. Also determines the type of material it outputs. (redium or blueium).
        """
        return self._ore_type

    @property
    def refine_input(self) -> int:
        """int: The amount of ore that needs to be inputted into the machine for it to be worked.
        """
        return self._refine_input

    @property
    def refine_output(self) -> int:
        """int: The amount of refined ore that is returned after the machine has been fully worked.
        """
        return self._refine_output

    @property
    def refine_time(self) -> int:
        """int: The number of times this machine needs to be worked to refine ore.
        """
        return self._refine_time

    @property
    def tile(self) -> 'games.newtonian.tile.Tile':
        """games.newtonian.tile.Tile: The Tile this Machine is on.
        """
        return self._tile

    @property
    def worked(self) -> int:
        """int: Tracks how many times this machine has been worked. (0 to refineTime).
        """
        return self._worked


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
