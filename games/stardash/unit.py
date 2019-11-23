# Unit: A unit in the game. May be a corvette, missleboat, martyr, transport, miner.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.stardash.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Unit(GameObject):
    """The class representing the Unit in the Stardash game.

    A unit in the game. May be a corvette, missleboat, martyr, transport, miner.
    """

    def __init__(self):
        """Initializes a Unit with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._acted = False
        self._dash_x = 0
        self._dash_y = 0
        self._energy = 0
        self._genarium = 0
        self._is_busy = False
        self._job = None
        self._legendarium = 0
        self._moves = 0
        self._mythicite = 0
        self._owner = None
        self._protector = None
        self._rarium = 0
        self._shield = 0
        self._x = 0
        self._y = 0

    @property
    def acted(self) -> bool:
        """Whether or not this Unit has performed its action this turn.

        :rtype: bool
        """
        return self._acted

    @property
    def dash_x(self) -> float:
        """The x value this unit is dashing to.

        :rtype: float
        """
        return self._dash_x

    @property
    def dash_y(self) -> float:
        """The y value this unit is dashing to.

        :rtype: float
        """
        return self._dash_y

    @property
    def energy(self) -> int:
        """The remaining health of the unit.

        :rtype: int
        """
        return self._energy

    @property
    def genarium(self) -> int:
        """The amount of Genarium ore carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._genarium

    @property
    def is_busy(self) -> bool:
        """Tracks wheither or not the ship is dashing or Mining. If True, it cannot do anything else.

        :rtype: bool
        """
        return self._is_busy

    @property
    def job(self) -> 'games.stardash.job.Job':
        """The Job this Unit has.

        :rtype: games.stardash.job.Job
        """
        return self._job

    @property
    def legendarium(self) -> int:
        """The amount of Legendarium ore carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._legendarium

    @property
    def moves(self) -> float:
        """The distance this unit can still move.

        :rtype: float
        """
        return self._moves

    @property
    def mythicite(self) -> int:
        """The amount of Mythicite carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._mythicite

    @property
    def owner(self) -> Optional['games.stardash.player.Player']:
        """The Player that owns and can control this Unit.

        :rtype: games.stardash.player.Player or None
        """
        return self._owner

    @property
    def protector(self) -> Optional['games.stardash.unit.Unit']:
        """The martyr ship that is currently shielding this ship if any.

        :rtype: games.stardash.unit.Unit or None
        """
        return self._protector

    @property
    def rarium(self) -> int:
        """The amount of Rarium carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._rarium

    @property
    def shield(self) -> int:
        """The sheild that a martyr ship has.

        :rtype: int
        """
        return self._shield

    @property
    def x(self) -> float:
        """The x value this unit is on.

        :rtype: float
        """
        return self._x

    @property
    def y(self) -> float:
        """The y value this unit is on.

        :rtype: float
        """
        return self._y

    def attack(self, enemy: 'games.stardash.unit.Unit') -> bool:
        """Attacks the specified unit.

        Args:
            enemy (games.stardash.unit.Unit): The Unit being attacked.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', {
            'enemy': enemy
        })

    def dash(self, x: float, y: float) -> bool:
        """Causes the unit to dash towards the designated destination.

        Args:
            x (float): The x value of the destination's coordinates.
            y (float): The y value of the destination's coordinates.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('dash', {
            'x': x,
            'y': y
        })

    def mine(self, body: 'games.stardash.body.Body') -> bool:
        """allows a miner to mine a asteroid

        Args:
            body (games.stardash.body.Body): The object to be mined.

        Returns:
            bool: True if successfully acted, False otherwise.
        """
        return self._run_on_server('mine', {
            'body': body
        })

    def move(self, x: float, y: float) -> bool:
        """Moves this Unit from its current location to the new location specified.

        Args:
            x (float): The x value of the destination's coordinates.
            y (float): The y value of the destination's coordinates.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('move', {
            'x': x,
            'y': y
        })

    def safe(self, x: float, y: float) -> bool:
        """tells you if your ship can move to that location from were it is without clipping the sun.

        Args:
            x (float): The x position of the location you wish to arrive.
            y (float): The y position of the location you wish to arrive.

        Returns:
            bool: True if pathable by this unit, False otherwise.
        """
        return self._run_on_server('safe', {
            'x': x,
            'y': y
        })

    def shootdown(self, missile: 'games.stardash.projectile.Projectile') -> bool:
        """Attacks the specified projectile.

        Args:
            missile (games.stardash.projectile.Projectile): The projectile being shot down.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('shootdown', {
            'missile': missile
        })

    def transfer(self, unit: 'games.stardash.unit.Unit', amount: int, material: str) -> bool:
        """Grab materials from a friendly unit. Doesn't use a action.

        Args:
            unit (games.stardash.unit.Unit): The unit you are grabbing the resources from.
            amount (int): The amount of materials to you with to grab. Amounts <= 0 will pick up all the materials that the unit can.
            material ('genarium', 'rarium', 'legendarium', or 'mythicite'): The material the unit will pick up. 'genarium', 'rarium', 'legendarium', or 'mythicite'.

        Returns:
            bool: True if successfully taken, False otherwise.
        """
        return self._run_on_server('transfer', {
            'unit': unit,
            'amount': amount,
            'material': material
        })

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
