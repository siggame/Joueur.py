# Miner: A Miner in the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Miner(GameObject):
    """The class representing the Miner in the Coreminer game.

    A Miner in the game.
    """

    def __init__(self):
        """Initializes a Miner with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bombs = 0
        self._building_materials = 0
        self._current_upgrade = None
        self._dirt = 0
        self._health = 0
        self._mining_power = 0
        self._moves = 0
        self._ore = 0
        self._owner = None
        self._tile = None
        self._upgrade_level = 0

    @property
    def bombs(self) -> int:
        """int: The number of bombs being carried by this Miner.
        """
        return self._bombs

    @property
    def building_materials(self) -> int:
        """int: The number of building materials carried by this Miner.
        """
        return self._building_materials

    @property
    def current_upgrade(self) -> 'games.coreminer.upgrade.Upgrade':
        """games.coreminer.upgrade.Upgrade: The Upgrade this Miner is on.
        """
        return self._current_upgrade

    @property
    def dirt(self) -> int:
        """int: The amount of dirt carried by this Miner.
        """
        return self._dirt

    @property
    def health(self) -> int:
        """int: The remaining health of this Miner.
        """
        return self._health

    @property
    def mining_power(self) -> int:
        """int: The remaining mining power this Miner has this turn.
        """
        return self._mining_power

    @property
    def moves(self) -> int:
        """int: The number of moves this Miner has left this turn.
        """
        return self._moves

    @property
    def ore(self) -> int:
        """int: The amount of ore carried by this Miner.
        """
        return self._ore

    @property
    def owner(self) -> 'games.coreminer.player.Player':
        """games.coreminer.player.Player: The Player that owns and can control this Miner.
        """
        return self._owner

    @property
    def tile(self) -> Optional['games.coreminer.tile.Tile']:
        """games.coreminer.tile.Tile or None: The Tile this Miner is on.
        """
        return self._tile

    @property
    def upgrade_level(self) -> int:
        """int: The upgrade level of this Miner. Starts at 0.
        """
        return self._upgrade_level

    def build(self, tile: 'games.coreminer.tile.Tile', type: str) -> bool:
        """Builds a support, shield, or ladder on Miner's Tile, or an adjacent Tile.

        Args:
            tile (games.coreminer.tile.Tile): The Tile to build on.
            type ('support', 'ladder', or 'shield'): The structure to build (support, ladder, or shield).

        Returns:
            bool: True if successfully built, False otherwise.
        """
        return self._run_on_server('build', {
            'tile': tile,
            'type': type
        })

    def buy(self, resource: str, amount: int) -> bool:
        """Purchase a resource from the Player's base or hopper.

        Args:
            resource ('dirt', 'ore', 'bomb', or 'buildingMaterials'): The type of resource to buy.
            amount (int): The amount of resource to buy. Amounts <= 0 will buy all of that material Player can.

        Returns:
            bool: True if successfully purchased, False otherwise.
        """
        return self._run_on_server('buy', {
            'resource': resource,
            'amount': amount
        })

    def dump(self, tile: 'games.coreminer.tile.Tile', material: str, amount: int) -> bool:
        """Dumps materials from cargo to an adjacent Tile. If the Tile is a base or a hopper Tile, materials are sold instead of placed.

        Args:
            tile (games.coreminer.tile.Tile): The Tile the materials will be dumped on.
            material ('dirt', 'ore', or 'bomb'): The material the Miner will drop. 'dirt', 'ore', or 'bomb'.
            amount (int): The number of materials to drop. Amounts <= 0 will drop all of the material.

        Returns:
            bool: True if successfully dumped materials, False otherwise.
        """
        return self._run_on_server('dump', {
            'tile': tile,
            'material': material,
            'amount': amount
        })

    def mine(self, tile: 'games.coreminer.tile.Tile', amount: int) -> bool:
        """Mines the Tile the Miner is on or an adjacent Tile.

        Args:
            tile (games.coreminer.tile.Tile): The Tile the materials will be mined from.
            amount (int): The amount of material to mine up. Amounts <= 0 will mine all the materials that the Miner can.

        Returns:
            bool: True if successfully mined, False otherwise.
        """
        return self._run_on_server('mine', {
            'tile': tile,
            'amount': amount
        })

    def move(self, tile: 'games.coreminer.tile.Tile') -> bool:
        """Moves this Miner from its current Tile to an adjacent Tile.

        Args:
            tile (games.coreminer.tile.Tile): The Tile this Miner should move to.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('move', {
            'tile': tile
        })

    def transfer(self, miner: 'games.coreminer.miner.Miner', resource: str, amount: int) -> bool:
        """Transfers a resource from the one Miner to another.

        Args:
            miner (games.coreminer.miner.Miner): The Miner to transfer materials to.
            resource ('dirt', 'ore', 'bomb', or 'buildingMaterials'): The type of resource to transfer.
            amount (int): The amount of resource to transfer. Amounts <= 0 will transfer all the of the material.

        Returns:
            bool: True if successfully transferred, False otherwise.
        """
        return self._run_on_server('transfer', {
            'miner': miner,
            'resource': resource,
            'amount': amount
        })

    def upgrade(self) -> bool:
        """Upgrade this Miner by installing an upgrade module.

        Returns:
            bool: True if successfully upgraded, False otherwise.
        """
        return self._run_on_server('upgrade', {

        })


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
