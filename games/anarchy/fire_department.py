# FireDepartment: Can put out fires completely.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.anarchy.building import Building

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class FireDepartment(Building):
    """The class representing the FireDepartment in the Anarchy game.

    Can put out fires completely.
    """

    def __init__(self):
        """Initializes a FireDepartment with basic logic as provided by the Creer code generator.
        """
        Building.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._fire_extinguished = 0

    @property
    def fire_extinguished(self) -> int:
        """int: The amount of fire removed from a building when bribed to extinguish a building.
        """
        return self._fire_extinguished

    def extinguish(self, building: 'games.anarchy.building.Building') -> bool:
        """Bribes this FireDepartment to extinguish the some of the fire in a building.

        Args:
            building (games.anarchy.building.Building): The Building you want to extinguish.

        Returns:
            bool: True if the bribe worked, False otherwise.
        """
        return self._run_on_server('extinguish', {
            'building': building
        })

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
