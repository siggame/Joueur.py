# Port: A port on a Tile.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.pirates.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Port(GameObject):
    """The class representing the Port in the Pirates game.

    A port on a Tile.
    """

    def __init__(self):
        """Initializes a Port with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._gold = 0
        self._investment = 0
        self._owner = None
        self._tile = None

    @property
    def gold(self):
        """For players, how much more gold this Port can spend this turn. For merchants, how much gold this Port has accumulated (it will spawn a ship when the Port can afford one).

        :rtype: int
        """
        return self._gold

    @property
    def investment(self):
        """(Merchants only) How much gold was invested into this Port. Investment determines the strength and value of the next ship.

        :rtype: int
        """
        return self._investment

    @property
    def owner(self):
        """The owner of this Port, or None if owned by merchants.

        :rtype: Player
        """
        return self._owner

    @property
    def tile(self):
        """The Tile this Port is on.

        :rtype: Tile
        """
        return self._tile

    def spawn(self, type):
        """ Spawn a Unit on this port.

        Args:
            type (str): What type of Unit to create ('crew' or 'ship').

        Returns:
            bool: True if Unit was created successfully, False otherwise.
        """
        return self._run_on_server('spawn', type=type)



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
