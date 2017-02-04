# Web: A connection (edge) to a Nest (node) in the game that Spiders can converge on (regardless of owner). Spiders can travel in either direction on Webs.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.spiders.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Web(GameObject):
    """The class representing the Web in the Spiders game.

    A connection (edge) to a Nest (node) in the game that Spiders can converge on (regardless of owner). Spiders can travel in either direction on Webs.
    """

    def __init__(self):
        """Initializes a Web with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._length = 0
        self._load = 0
        self._nest_a = None
        self._nest_b = None
        self._spiderlings = []
        self._strength = 0



    @property
    def length(self):
        """How long this Web is, i.e., the distance between its nestA and nestB.

        :rtype: float
        """
        return self._length


    @property
    def load(self):
        """How much weight this Web currently has on it, which is the sum of all its Spiderlings weight.

        :rtype: int
        """
        return self._load


    @property
    def nest_a(self):
        """The first Nest this Web is connected to.

        :rtype: Nest
        """
        return self._nest_a


    @property
    def nest_b(self):
        """The second Nest this Web is connected to.

        :rtype: Nest
        """
        return self._nest_b


    @property
    def spiderlings(self):
        """All the Spiderlings currently moving along this Web.

        :rtype: list[Spiderling]
        """
        return self._spiderlings


    @property
    def strength(self):
        """How much weight this Web can take before snapping and destroying itself and all the Spiders on it.

        :rtype: int
        """
        return self._strength



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
