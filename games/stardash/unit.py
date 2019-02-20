# Unit: A unit in the game. May be a corvette, missleboat, martyr, transport, miner.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.stardash.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Unit(GameObject):
    """The class representing the Unit in the Stardash game.

    A unit in the game. May be a corvette, missleboat, martyr, transport, miner.
    """

    def __init__(self):
        """Initializes a Unit with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._acted = False
        self._dash_x = 0
        self._dash_y = 0
        self._energy = 0
        self._genarium = 0
        self._is_dashing = False
        self._job = None
        self._legendarium = 0
        self._moves = 0
        self._mythicite = 0
        self._owner = None
        self._protector = None
        self._radius = 0
        self._rarium = 0
        self._x = 0
        self._y = 0

    @property
    def acted(self):
        """Whether or not this Unit has performed its action this turn.

        :rtype: bool
        """
        return self._acted

    @property
    def dash_x(self):
        """The x value this unit is dashing to.

        :rtype: float
        """
        return self._dash_x

    @property
    def dash_y(self):
        """The y value this unit is dashing to.

        :rtype: float
        """
        return self._dash_y

    @property
    def energy(self):
        """The remaining health of a unit.

        :rtype: int
        """
        return self._energy

    @property
    def genarium(self):
        """The amount of Generium ore carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._genarium

    @property
    def is_dashing(self):
        """Tracks wheither or not the ship is dashing.

        :rtype: bool
        """
        return self._is_dashing

    @property
    def job(self):
        """The Job this Unit has.

        :rtype: games.stardash.job.Job
        """
        return self._job

    @property
    def legendarium(self):
        """The amount of Legendarium ore carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._legendarium

    @property
    def moves(self):
        """The distance this unit can still move.

        :rtype: float
        """
        return self._moves

    @property
    def mythicite(self):
        """The amount of Mythicite carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._mythicite

    @property
    def owner(self):
        """The Player that owns and can control this Unit.

        :rtype: games.stardash.player.Player
        """
        return self._owner

    @property
    def protector(self):
        """The martyr ship that is currently shielding this ship if any.

        :rtype: games.stardash.unit.Unit
        """
        return self._protector

    @property
    def radius(self):
        """The radius of the circle this unit occupies.

        :rtype: float
        """
        return self._radius

    @property
    def rarium(self):
        """The amount of Rarium carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._rarium

    @property
    def x(self):
        """The x value this unit is on.

        :rtype: float
        """
        return self._x

    @property
    def y(self):
        """The y value this unit is on.

        :rtype: float
        """
        return self._y

    def attack(self, enemy):
        """ Attacks the specified unit.

        Args:
            enemy (games.stardash.unit.Unit): The Unit being attacked.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', enemy=enemy)

    def mine(self, body):
        """ allows a miner to mine a asteroid

        Args:
            body (games.stardash.body.Body): The object to be mined.

        Returns:
            bool: True if successfully acted, False otherwise.
        """
        return self._run_on_server('mine', body=body)

    def move(self, x, y):
        """ Moves this Unit from its current location to the new location specified.

        Args:
            x (float): The x value of the destination's coordinates.
            y (float): The y value of the destination's coordinates.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('move', x=x, y=y)

    def open(self, x, y):
        """ tells you if your ship can dash to that location.

        Args:
            x (float): The x position of the location you wish to check.
            y (float): The y position of the location you wish to check.

        Returns:
            bool: True if pathable by this unit, False otherwise.
        """
        return self._run_on_server('open', x=x, y=y)

    def shoot_down(self, missile):
        """ Attacks the specified projectile.

        Args:
            missile (games.stardash.projectile.Projectile): The projectile being shot down.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('shootDown', missile=missile)

    def transfer(self, unit, amount, material):
        """ Grab materials from a friendly unit. Doesn't use a action.

        Args:
            unit (games.stardash.unit.Unit): The unit you are grabbing the resources from.
            amount (int): The amount of materials to you with to grab. Amounts <= 0 will pick up all the materials that the unit can.
            material (str): The material the unit will pick up. 'resource1', 'resource2', or 'resource3'.

        Returns:
            bool: True if successfully taken, False otherwise.
        """
        return self._run_on_server('transfer', unit=unit, amount=amount, material=material)

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
