# Cowboy: A person on the map that can move around and interact within the saloon.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Cowboy(GameObject):
    """The class representing the Cowboy in the Saloon game.

    A person on the map that can move around and interact within the saloon.
    """

    def __init__(self):
        """Initializes a Cowboy with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._can_move = False
        self._drunk_direction = ""
        self._focus = 0
        self._health = 0
        self._is_dead = False
        self._is_drunk = False
        self._job = ""
        self._owner = None
        self._tile = None
        self._tolerance = 0
        self._turns_busy = 0

    @property
    def can_move(self) -> bool:
        """If the Cowboy can be moved this turn via its owner.

        :rtype: bool
        """
        return self._can_move

    @property
    def drunk_direction(self) -> str:
        """The direction this Cowboy is moving while drunk. Will be 'North', 'East', 'South', or 'West' when drunk; or '' (empty string) when not drunk.

        :rtype: '', 'North', 'East', 'South', or 'West'
        """
        return self._drunk_direction

    @property
    def focus(self) -> int:
        """How much focus this Cowboy has. Different Jobs do different things with their Cowboy's focus.

        :rtype: int
        """
        return self._focus

    @property
    def health(self) -> int:
        """How much health this Cowboy currently has.

        :rtype: int
        """
        return self._health

    @property
    def is_dead(self) -> bool:
        """If this Cowboy is dead and has been removed from the game.

        :rtype: bool
        """
        return self._is_dead

    @property
    def is_drunk(self) -> bool:
        """If this Cowboy is drunk, and will automatically walk.

        :rtype: bool
        """
        return self._is_drunk

    @property
    def job(self) -> str:
        """The job that this Cowboy does, and dictates how they fight and interact within the Saloon.

        :rtype: 'Bartender', 'Brawler', or 'Sharpshooter'
        """
        return self._job

    @property
    def owner(self) -> 'games.saloon.player.Player':
        """The Player that owns and can control this Cowboy.

        :rtype: games.saloon.player.Player
        """
        return self._owner

    @property
    def tile(self) -> Optional['games.saloon.tile.Tile']:
        """The Tile that this Cowboy is located on.

        :rtype: games.saloon.tile.Tile or None
        """
        return self._tile

    @property
    def tolerance(self) -> int:
        """How many times this unit has been drunk before taking their siesta and reseting this to 0.

        :rtype: int
        """
        return self._tolerance

    @property
    def turns_busy(self) -> int:
        """How many turns this unit has remaining before it is no longer busy and can `act()` or `play()` again.

        :rtype: int
        """
        return self._turns_busy

    def act(self, tile: 'games.saloon.tile.Tile', drunk_direction: str = "") -> bool:
        """Does their job's action on a Tile.

        Args:
            tile (games.saloon.tile.Tile): The Tile you want this Cowboy to act on.
            drunk_direction ('', 'North', 'East', 'South', or 'West'): The direction the bottle will cause drunk cowboys to be in, can be 'North', 'East', 'South', or 'West'.

        Returns:
            bool: True if the act worked, False otherwise.
        """
        return self._run_on_server('act', {
            'tile': tile,
            'drunkDirection': drunk_direction
        })

    def move(self, tile: 'games.saloon.tile.Tile') -> bool:
        """Moves this Cowboy from its current Tile to an adjacent Tile.

        Args:
            tile (games.saloon.tile.Tile): The Tile you want to move this Cowboy to.

        Returns:
            bool: True if the move worked, False otherwise.
        """
        return self._run_on_server('move', {
            'tile': tile
        })

    def play(self, piano: 'games.saloon.furnishing.Furnishing') -> bool:
        """Sits down and plays a piano.

        Args:
            piano (games.saloon.furnishing.Furnishing): The Furnishing that is a piano you want to play.

        Returns:
            bool: True if the play worked, False otherwise.
        """
        return self._run_on_server('play', {
            'piano': piano
        })


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
