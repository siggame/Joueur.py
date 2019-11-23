# Weaver: A Spiderling that can alter existing Webs by weaving to add or remove silk from the Webs, thus altering its strength.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.spiders.spiderling import Spiderling

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Weaver(Spiderling):
    """The class representing the Weaver in the Spiders game.

    A Spiderling that can alter existing Webs by weaving to add or remove silk from the Webs, thus altering its strength.
    """

    def __init__(self):
        """Initializes a Weaver with basic logic as provided by the Creer code generator.
        """
        Spiderling.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._strengthening_web = None
        self._weakening_web = None

    @property
    def strengthening_web(self) -> Optional['games.spiders.web.Web']:
        """games.spiders.web.Web or None: The Web that this Weaver is strengthening. None if not strengthening.
        """
        return self._strengthening_web

    @property
    def weakening_web(self) -> Optional['games.spiders.web.Web']:
        """games.spiders.web.Web or None: The Web that this Weaver is weakening. None if not weakening.
        """
        return self._weakening_web

    def strengthen(self, web: 'games.spiders.web.Web') -> bool:
        """Weaves more silk into an existing Web to strengthen it.

        Args:
            web (games.spiders.web.Web): The web you want to strengthen. Must be connected to the Nest this Weaver is currently on.

        Returns:
            bool: True if the strengthen was successfully started, False otherwise.
        """
        return self._run_on_server('strengthen', {
            'web': web
        })

    def weaken(self, web: 'games.spiders.web.Web') -> bool:
        """Weaves more silk into an existing Web to strengthen it.

        Args:
            web (games.spiders.web.Web): The web you want to weaken. Must be connected to the Nest this Weaver is currently on.

        Returns:
            bool: True if the weaken was successfully started, False otherwise.
        """
        return self._run_on_server('weaken', {
            'web': web
        })

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
