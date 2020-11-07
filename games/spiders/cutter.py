# Cutter: A Spiderling that can cut existing Webs.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.spiders.spiderling import Spiderling

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Cutter(Spiderling):
    """The class representing the Cutter in the Spiders game.

    A Spiderling that can cut existing Webs.
    """

    def __init__(self):
        """Initializes a Cutter with basic logic as provided by the Creer code generator.
        """
        Spiderling.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._cutting_web = None

    @property
    def cutting_web(self) -> Optional['games.spiders.web.Web']:
        """games.spiders.web.Web or None: The Web that this Cutter is trying to cut. None if not cutting.
        """
        return self._cutting_web

    def cut(self, web: 'games.spiders.web.Web') -> bool:
        """Cuts a web, destroying it, and any Spiderlings on it.

        Args:
            web (games.spiders.web.Web): The web you want to Cut. Must be connected to the Nest this Cutter is currently on.

        Returns:
            bool: True if the cut was successfully started, False otherwise.
        """
        return self._run_on_server('cut', {
            'web': web
        })

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
