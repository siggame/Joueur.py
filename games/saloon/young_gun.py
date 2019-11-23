# YoungGun: An eager young person that wants to join your gang, and will call in the veteran Cowboys you need to win the brawl in the saloon.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class YoungGun(GameObject):
    """The class representing the YoungGun in the Saloon game.

    An eager young person that wants to join your gang, and will call in the veteran Cowboys you need to win the brawl in the saloon.
    """

    def __init__(self):
        """Initializes a YoungGun with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._call_in_tile = None
        self._can_call_in = False
        self._owner = None
        self._tile = None

    @property
    def call_in_tile(self) -> 'games.saloon.tile.Tile':
        """games.saloon.tile.Tile: The Tile that a Cowboy will be called in on if this YoungGun calls in a Cowboy.
        """
        return self._call_in_tile

    @property
    def can_call_in(self) -> bool:
        """bool: True if the YoungGun can call in a Cowboy, False otherwise.
        """
        return self._can_call_in

    @property
    def owner(self) -> 'games.saloon.player.Player':
        """games.saloon.player.Player: The Player that owns and can control this YoungGun.
        """
        return self._owner

    @property
    def tile(self) -> 'games.saloon.tile.Tile':
        """games.saloon.tile.Tile: The Tile this YoungGun is currently on.
        """
        return self._tile

    def call_in(self, job: str) -> Optional['games.saloon.cowboy.Cowboy']:
        """Tells the YoungGun to call in a new Cowboy of the given job to the open Tile nearest to them.

        Args:
            job ('Bartender', 'Brawler', or 'Sharpshooter'): The job you want the Cowboy being brought to have.

        Returns:
            games.saloon.cowboy.Cowboy or None: The new Cowboy that was called in if valid. They will not be added to any `cowboys` lists until the turn ends. None otherwise.
        """
        return self._run_on_server('callIn', {
            'job': job
        })


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
