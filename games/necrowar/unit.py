# Unit: A unit in the game. May be a worker, zombie, ghoul, hound, abomination, wraith or horseman.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.necrowar.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Unit(GameObject):
    """The class representing the Unit in the Necrowar game.

    A unit in the game. May be a worker, zombie, ghoul, hound, abomination, wraith or horseman.
    """

    def __init__(self):
        """Initializes a Unit with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._acted = False
        self._health = 0
        self._moves = 0
        self._owner = None
        self._tile = None
        self._u_job = None

    @property
    def acted(self):
        """Whether or not this Unit has performed its action this turn (attack or build).

        :rtype: bool
        """
        return self._acted

    @property
    def health(self):
        """The remaining health of a unit.

        :rtype: int
        """
        return self._health

    @property
    def moves(self):
        """The number of moves this unit has left this turn.

        :rtype: int
        """
        return self._moves

    @property
    def owner(self):
        """The Player that owns and can control this Unit.

        :rtype: games.necrowar.player.Player
        """
        return self._owner

    @property
    def tile(self):
        """The Tile this Unit is on.

        :rtype: games.necrowar.tile.Tile
        """
        return self._tile

    @property
    def u_job(self):
        """The type of unit this is.

        :rtype: uJob
        """
        return self._u_job

    def attack(self, tile):
        """ Attacks an enemy tower on an adjacent tile.

        Args:
            tile (games.necrowar.tile.Tile): The Tile to attack.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', tile=tile)

    def build(self, tile, tJob):
        """ Unit, if it is a worker, builds a tower on the tile it is on, only workers can do this.

        Args:
            tile (games.necrowar.tile.Tile): The tile the unit is on/builds on.
            t_job (tJob): The type of tower that is being built. 'arrow', 'aoe', 'ballista', or 'cleansing'.

        Returns:
            bool: True if successfully built, False otherwise.
        """
        return self._run_on_server('build', tile=tile, tJob=tJob)

    def fish(self, tile):
        """ Stops adjacent to a river tile and begins fishing for mana.

        Args:
            tile (games.necrowar.tile.Tile): The tile the unit will stand on as it fishes.

        Returns:
            bool: True if successfully began fishing for mana, False otherwise.
        """
        return self._run_on_server('fish', tile=tile)

    def mine(self, tile):
        """ Enters an empty mine tile and is put to work gathering resources.

        Args:
            tile (games.necrowar.tile.Tile): The tile the mine is located on.

        Returns:
            bool: True if successfully entered mine and began mining, False otherwise.
        """
        return self._run_on_server('mine', tile=tile)

    def move(self, tile):
        """ Moves this Unit from its current Tile to an adjacent Tile.

        Args:
            tile (games.necrowar.tile.Tile): The Tile this Unit should move to.

        Returns:
            bool: True if it moved, False otherwise.
        """
        return self._run_on_server('move', tile=tile)



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
