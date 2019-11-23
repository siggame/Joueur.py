# Unit: A unit in the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.catastrophe.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Unit(GameObject):
    """The class representing the Unit in the Catastrophe game.

    A unit in the game.
    """

    def __init__(self):
        """Initializes a Unit with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._acted = False
        self._energy = 0
        self._food = 0
        self._job = None
        self._materials = 0
        self._movement_target = None
        self._moves = 0
        self._owner = None
        self._squad = []
        self._starving = False
        self._tile = None
        self._turns_to_die = 0

    @property
    def acted(self) -> bool:
        """bool: Whether this Unit has performed its action this turn.
        """
        return self._acted

    @property
    def energy(self) -> float:
        """float: The amount of energy this Unit has (from 0.0 to 100.0).
        """
        return self._energy

    @property
    def food(self) -> int:
        """int: The amount of food this Unit is holding.
        """
        return self._food

    @property
    def job(self) -> 'games.catastrophe.job.Job':
        """games.catastrophe.job.Job: The Job this Unit was recruited to do.
        """
        return self._job

    @property
    def materials(self) -> int:
        """int: The amount of materials this Unit is holding.
        """
        return self._materials

    @property
    def movement_target(self) -> Optional['games.catastrophe.tile.Tile']:
        """games.catastrophe.tile.Tile or None: The tile this Unit is moving to. This only applies to neutral fresh humans spawned on the road. Otherwise, the tile this Unit is on.
        """
        return self._movement_target

    @property
    def moves(self) -> int:
        """int: How many moves this Unit has left this turn.
        """
        return self._moves

    @property
    def owner(self) -> Optional['games.catastrophe.player.Player']:
        """games.catastrophe.player.Player or None: The Player that owns and can control this Unit, or None if the Unit is neutral.
        """
        return self._owner

    @property
    def squad(self) -> List['games.catastrophe.unit.Unit']:
        """list[games.catastrophe.unit.Unit]: The Units in the same squad as this Unit. Units in the same squad attack and defend together.
        """
        return self._squad

    @property
    def starving(self) -> bool:
        """bool: Whether this Unit is starving. Starving Units regenerate energy at half the rate they normally would while resting.
        """
        return self._starving

    @property
    def tile(self) -> Optional['games.catastrophe.tile.Tile']:
        """games.catastrophe.tile.Tile or None: The Tile this Unit is on.
        """
        return self._tile

    @property
    def turns_to_die(self) -> int:
        """int: The number of turns before this Unit dies. This only applies to neutral fresh humans created from combat. Otherwise, 0.
        """
        return self._turns_to_die

    def attack(self, tile: 'games.catastrophe.tile.Tile') -> bool:
        """Attacks an adjacent Tile. Costs an action for each Unit in this Unit's squad. Units in the squad without an action don't participate in combat. Units in combat cannot move afterwards. Attacking structures will not give materials.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile to attack.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', {
            'tile': tile
        })

    def change_job(self, job: str) -> bool:
        """Changes this Unit's Job. Must be at max energy (100.0) to change Jobs.

        Args:
            job ('soldier', 'gatherer', 'builder', or 'missionary'): The name of the Job to change to.

        Returns:
            bool: True if successfully changed Jobs, False otherwise.
        """
        return self._run_on_server('changeJob', {
            'job': job
        })

    def construct(self, tile: 'games.catastrophe.tile.Tile', type: str) -> bool:
        """Constructs a Structure on an adjacent Tile.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile to construct the Structure on. It must have enough materials on it for a Structure to be constructed.
            type ('neutral', 'shelter', 'monument', 'wall', or 'road'): The type of Structure to construct on that Tile.

        Returns:
            bool: True if successfully constructed a structure, False otherwise.
        """
        return self._run_on_server('construct', {
            'tile': tile,
            'type': type
        })

    def convert(self, tile: 'games.catastrophe.tile.Tile') -> bool:
        """Converts an adjacent Unit to your side.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile with the Unit to convert.

        Returns:
            bool: True if successfully converted, False otherwise.
        """
        return self._run_on_server('convert', {
            'tile': tile
        })

    def deconstruct(self, tile: 'games.catastrophe.tile.Tile') -> bool:
        """Removes materials from an adjacent Tile's Structure. You cannot deconstruct friendly structures (see Unit.attack).

        Args:
            tile (games.catastrophe.tile.Tile): The Tile to deconstruct. It must have a Structure on it.

        Returns:
            bool: True if successfully deconstructed, False otherwise.
        """
        return self._run_on_server('deconstruct', {
            'tile': tile
        })

    def drop(self, tile: 'games.catastrophe.tile.Tile', resource: str, amount: int = 0) -> bool:
        """Drops some of the given resource on or adjacent to the Unit's Tile. Does not count as an action.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile to drop materials/food on.
            resource ('materials' or 'food'): The type of resource to drop ('materials' or 'food').
            amount (int): The amount of the resource to drop. Amounts <= 0 will drop as much as possible.

        Returns:
            bool: True if successfully dropped the resource, False otherwise.
        """
        return self._run_on_server('drop', {
            'tile': tile,
            'resource': resource,
            'amount': amount
        })

    def harvest(self, tile: 'games.catastrophe.tile.Tile') -> bool:
        """Harvests the food on an adjacent Tile.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile you want to harvest.

        Returns:
            bool: True if successfully harvested, False otherwise.
        """
        return self._run_on_server('harvest', {
            'tile': tile
        })

    def move(self, tile: 'games.catastrophe.tile.Tile') -> bool:
        """Moves this Unit from its current Tile to an adjacent Tile.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile this Unit should move to.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('move', {
            'tile': tile
        })

    def pickup(self, tile: 'games.catastrophe.tile.Tile', resource: str, amount: int = 0) -> bool:
        """Picks up some materials or food on or adjacent to the Unit's Tile. Does not count as an action.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile to pickup materials/food from.
            resource ('materials' or 'food'): The type of resource to pickup ('materials' or 'food').
            amount (int): The amount of the resource to pickup. Amounts <= 0 will pickup as much as possible.

        Returns:
            bool: True if successfully picked up a resource, False otherwise.
        """
        return self._run_on_server('pickup', {
            'tile': tile,
            'resource': resource,
            'amount': amount
        })

    def rest(self) -> bool:
        """Regenerates energy. Must be in range of a friendly shelter to rest. Costs an action. Units cannot move after resting.

        Returns:
            bool: True if successfully rested, False otherwise.
        """
        return self._run_on_server('rest', {

        })


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
