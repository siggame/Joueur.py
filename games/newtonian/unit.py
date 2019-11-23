# Unit: A unit in the game. May be a manager, intern, or physicist.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.newtonian.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Unit(GameObject):
    """The class representing the Unit in the Newtonian game.

    A unit in the game. May be a manager, intern, or physicist.
    """

    def __init__(self):
        """Initializes a Unit with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._acted = False
        self._blueium = 0
        self._blueium_ore = 0
        self._health = 0
        self._job = None
        self._moves = 0
        self._owner = None
        self._redium = 0
        self._redium_ore = 0
        self._stun_immune = 0
        self._stun_time = 0
        self._tile = None

    @property
    def acted(self) -> bool:
        """Whether or not this Unit has performed its action this turn.

        :rtype: bool
        """
        return self._acted

    @property
    def blueium(self) -> int:
        """The amount of blueium carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._blueium

    @property
    def blueium_ore(self) -> int:
        """The amount of blueium ore carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._blueium_ore

    @property
    def health(self) -> int:
        """The remaining health of a unit.

        :rtype: int
        """
        return self._health

    @property
    def job(self) -> 'games.newtonian.job.Job':
        """The Job this Unit has.

        :rtype: games.newtonian.job.Job
        """
        return self._job

    @property
    def moves(self) -> int:
        """The number of moves this unit has left this turn.

        :rtype: int
        """
        return self._moves

    @property
    def owner(self) -> Optional['games.newtonian.player.Player']:
        """The Player that owns and can control this Unit.

        :rtype: games.newtonian.player.Player or None
        """
        return self._owner

    @property
    def redium(self) -> int:
        """The amount of redium carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._redium

    @property
    def redium_ore(self) -> int:
        """The amount of redium ore carried by this unit. (0 to job carry capacity - other carried items).

        :rtype: int
        """
        return self._redium_ore

    @property
    def stun_immune(self) -> int:
        """Duration of stun immunity. (0 to timeImmune).

        :rtype: int
        """
        return self._stun_immune

    @property
    def stun_time(self) -> int:
        """Duration the unit is stunned. (0 to the game constant stunTime).

        :rtype: int
        """
        return self._stun_time

    @property
    def tile(self) -> Optional['games.newtonian.tile.Tile']:
        """The Tile this Unit is on.

        :rtype: games.newtonian.tile.Tile or None
        """
        return self._tile

    def act(self, tile: 'games.newtonian.tile.Tile') -> bool:
        """Makes the unit do something to a machine or unit adjacent to its tile. Interns sabotage, physicists work. Interns stun physicist, physicist stuns manager, manager stuns intern.

        Args:
            tile (games.newtonian.tile.Tile): The tile the unit acts on.

        Returns:
            bool: True if successfully acted, False otherwise.
        """
        return self._run_on_server('act', {
            'tile': tile
        })

    def attack(self, tile: 'games.newtonian.tile.Tile') -> bool:
        """Attacks a unit on an adjacent tile.

        Args:
            tile (games.newtonian.tile.Tile): The Tile to attack.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', {
            'tile': tile
        })

    def drop(self, tile: 'games.newtonian.tile.Tile', amount: int, material: str) -> bool:
        """Drops materials at the units feet or adjacent tile.

        Args:
            tile (games.newtonian.tile.Tile): The tile the materials will be dropped on.
            amount (int): The number of materials to dropped. Amounts <= 0 will drop all the materials.
            material ('redium ore', 'redium', 'blueium', or 'blueium ore'): The material the unit will drop. 'redium', 'blueium', 'redium ore', or 'blueium ore'.

        Returns:
            bool: True if successfully deposited, False otherwise.
        """
        return self._run_on_server('drop', {
            'tile': tile,
            'amount': amount,
            'material': material
        })

    def move(self, tile: 'games.newtonian.tile.Tile') -> bool:
        """Moves this Unit from its current Tile to an adjacent Tile.

        Args:
            tile (games.newtonian.tile.Tile): The Tile this Unit should move to.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('move', {
            'tile': tile
        })

    def pickup(self, tile: 'games.newtonian.tile.Tile', amount: int, material: str) -> bool:
        """Picks up material at the units feet or adjacent tile.

        Args:
            tile (games.newtonian.tile.Tile): The tile the materials will be picked up from.
            amount (int): The amount of materials to pick up. Amounts <= 0 will pick up all the materials that the unit can.
            material ('redium ore', 'redium', 'blueium', or 'blueium ore'): The material the unit will pick up. 'redium', 'blueium', 'redium ore', or 'blueium ore'.

        Returns:
            bool: True if successfully deposited, False otherwise.
        """
        return self._run_on_server('pickup', {
            'tile': tile,
            'amount': amount,
            'material': material
        })


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
