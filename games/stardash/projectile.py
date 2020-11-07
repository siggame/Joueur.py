# Projectile: Tracks any projectiles moving through space.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.stardash.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Projectile(GameObject):
    """The class representing the Projectile in the Stardash game.

    Tracks any projectiles moving through space.
    """

    def __init__(self):
        """Initializes a Projectile with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._energy = 0
        self._fuel = 0
        self._owner = None
        self._target = None
        self._x = 0
        self._y = 0

    @property
    def energy(self) -> int:
        """int: The remaining health of the projectile.
        """
        return self._energy

    @property
    def fuel(self) -> int:
        """int: The amount of remaining distance the projectile can move.
        """
        return self._fuel

    @property
    def owner(self) -> Optional['games.stardash.player.Player']:
        """games.stardash.player.Player or None: The Player that owns and can control this Projectile.
        """
        return self._owner

    @property
    def target(self) -> 'games.stardash.unit.Unit':
        """games.stardash.unit.Unit: The unit that is being attacked by this projectile.
        """
        return self._target

    @property
    def x(self) -> float:
        """float: The x value this projectile is on.
        """
        return self._x

    @property
    def y(self) -> float:
        """float: The y value this projectile is on.
        """
        return self._y

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
