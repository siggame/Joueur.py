# Body: A celestial body located within the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.stardash.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Body(GameObject):
    """The class representing the Body in the Stardash game.

    A celestial body located within the game.
    """

    def __init__(self):
        """Initializes a Body with basic logic as provided by the Creer code generator.
        """
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
    def amount(self) -> int:
        """The amount of material the object has, or energy if it is a planet.

        :rtype: int
        """
        return self._amount

    @property
    def body_type(self) -> str:
        """The type of celestial body it is. Either 'planet', 'asteroid', or 'sun'.

        :rtype: 'planet', 'asteroid', or 'sun'
        """
        return self._body_type

    @property
    def material_type(self) -> str:
        """The type of material the celestial body has. Either 'none', 'genarium', 'rarium', 'legendarium', or 'mythicite'.

        :rtype: 'none', 'genarium', 'rarium', 'legendarium', or 'mythicite'
        """
        return self._material_type

    @property
    def owner(self) -> Optional['games.stardash.player.Player']:
        """The Player that owns and can control this Body.

        :rtype: games.stardash.player.Player or None
        """
        return self._owner

    @property
    def radius(self) -> float:
        """The radius of the circle that this body takes up.

        :rtype: float
        """
        return self._radius

    @property
    def x(self) -> float:
        """The x value this celestial body is on.

        :rtype: float
        """
        return self._x

    @property
    def y(self) -> float:
        """The y value this celestial body is on.

        :rtype: float
        """
        return self._y

    def next_x(self, num: int) -> int:
        """The x value of this body a number of turns from now. (0-how many you want).

        Args:
            num (int): The number of turns in the future you wish to check.

        Returns:
            int: The x position of the body the input number of turns in the future.
        """
        return self._run_on_server('nextX', {
            'num': num
        })

    def next_y(self, num: int) -> int:
        """The x value of this body a number of turns from now. (0-how many you want).

        Args:
            num (int): The number of turns in the future you wish to check.

        Returns:
            int: The x position of the body the input number of turns in the future.
        """
        return self._run_on_server('nextY', {
            'num': num
        })

    def spawn(self, x: float, y: float, title: str) -> bool:
        """Spawn a unit on some value of this celestial body.

        Args:
            x (float): The x value of the spawned unit.
            y (float): The y value of the spawned unit.
            title (str): The job title of the unit being spawned.

        Returns:
            bool: True if successfully taken, False otherwise.
        """
        return self._run_on_server('spawn', {
            'x': x,
            'y': y,
            'title': title
        })

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
