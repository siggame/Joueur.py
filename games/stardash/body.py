# Body: A celestial body located within the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.stardash.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Body(GameObject):
    """The class representing the Body in the Stardash game.

    A celestial body located within the game.
    """

    def __init__(self):
        """Initializes a Body with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._amount = 0
        self._body_type = ""
        self._material_type = ""
        self._owner = None
        self._radius = 0
        self._x = 0
        self._y = 0

    @property
    def amount(self):
        """The amount of material the object has.

        :rtype: int
        """
        return self._amount

    @property
    def body_type(self):
        """The type of celestial body it is.

        :rtype: str
        """
        return self._body_type

    @property
    def material_type(self):
        """The type of material the celestial body has.

        :rtype: str
        """
        return self._material_type

    @property
    def owner(self):
        """The Player that owns and can control this Unit.

        :rtype: games.stardash.player.Player
        """
        return self._owner

    @property
    def radius(self):
        """The radius of the circle that this body takes up.

        :rtype: float
        """
        return self._radius

    @property
    def x(self):
        """The x value this celestial body is on.

        :rtype: float
        """
        return self._x

    @property
    def y(self):
        """The y value this celestial body is on.

        :rtype: float
        """
        return self._y

    def spawn(self, x, y, title):
        """ Spawn a unit on some value of this celestial body.

        Args:
            x (float): The x value of the spawned unit.
            y (float): The y value of the spawned unit.
            title (str): The job title of the unit being spawned.

        Returns:
            bool: True if successfully taken, False otherwise.
        """
        return self._run_on_server('spawn', x=x, y=y, title=title)

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
