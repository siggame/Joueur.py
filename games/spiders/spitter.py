# Spitter: A Spiderling that creates and spits new Webs from the Nest it is on to another Nest, connecting them.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.spiders.spiderling import Spiderling

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Spitter(Spiderling):
    """The class representing the Spitter in the Spiders game.

    A Spiderling that creates and spits new Webs from the Nest it is on to another Nest, connecting them.
    """

    def __init__(self):
        """Initializes a Spitter with basic logic as provided by the Creer code generator."""
        Spiderling.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._spitting_web_to_nest = None

    @property
    def spitting_web_to_nest(self):
        """The Nest that this Spitter is creating a Web to spit at, thus connecting them. None if not spitting.

        :rtype: games.spiders.nest.Nest
        """
        return self._spitting_web_to_nest

    def spit(self, nest):
        """ Creates and spits a new Web from the Nest the Spitter is on to another Nest, connecting them.

        Args:
            nest (games.spiders.nest.Nest): The Nest you want to spit a Web to, thus connecting that Nest and the one the Spitter is on.

        Returns:
            bool: True if the spit was successful, False otherwise.
        """
        return self._run_on_server('spit', nest=nest)

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
