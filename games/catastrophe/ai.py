# This is where you build your AI for the Catastrophe game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
import random
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The basic AI functions that are the same between games. """

    def get_name(self):
        """ This is the name you send to the server so your AI will control the player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Catastrophe Python Player" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its playerID and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        random.seed()
        # <<-- /Creer-Merge: start -->>

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why you won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for runTurn

        # Output the current turn of the game
        print("TURN #{}".format(self.game.current_turn))

        # Grab one of your shelters
        my_shelter = None
        for structure in self.player.structures:
            if structure.type == "shelter":
                my_shelter = structure
                break

        # Loop through all of your units & define what to do for each of the different unit types
        for my_unit in self.player.units:
            # Display info about current unit
            print("Current Unit {} , Job Title {}".format(my_unit.id, my_unit.job.title))

            if my_unit.job.title == "fresh human":
                # Check if the Unit can move to its shelter
                if my_shelter and my_unit.moves > 0:
                    # Try to find a path to shelter
                    path = self.find_path(my_unit.tile, my_shelter.tile)

                    # if there is a path, move along it
                    #   - length 0 means no path could be found to the tile or the unit is
                    #     top of the shelther
                    #   - length 1 means the unit is adjacent to the shelter
                    if len(path) > 1:
                        if my_unit.move(path[0]):
                            print("Moving Unit {} to Tile {}".format(my_unit.id, path[0].id))

                # Create a job list that doesn't include the cat overlord or fresh human
                my_jobs = []
                for job in self.game.jobs:
                    if job.title != "cat overlord" and job.title != "fresh human":
                        my_jobs.append(job.title)

                # Grab the neighbors of the current Unit
                my_neighbors = my_unit.tile.get_neighbors()
                # Add the tile that the unit is standing on in case it is on top of a shelter
                my_neighbors.append(my_unit.tile)

                # Check for a shelter in my_neighbors
                if self.check_for_shelter(my_neighbors):
                    # Try to change the job of the fresh human to a random job from my_jobs
                    if my_unit.change_job(my_jobs[random.randint(0,(len(my_jobs)-1))]):
                        print("Successfully changed Unit {} to Job \'{}\'".format(my_unit.id, my_unit.job.title))

            elif my_unit.job.title == "soldier":
                # Grab the enemy Units
                enemy_units = self.player.opponent.units

                # Create a path variable for use below
                path = None

                # Check if the Unit has enough energy to attack
                if my_unit.energy > my_unit.job.action_cost:
                    # Define a path to the first enemy unit
                    if len(enemy_units) > 0:
                        path = self.find_path(my_unit.tile, enemy_units[0].tile)

                    # Try to move the soldier towards the enemy
                    if len(path) > 1:
                        if my_unit.move(path[0]):
                            print("Moving Unit {} to Tile {}".format(my_unit.id, path[0].id))

                    # If the soldier is right next to the enemy
                    elif len(path) == 1:
                        # Make sure the unit hasn't already acted
                        if my_unit.acted == False:
                            if my_unit.attack(path[0]):
                                print("Unit {} is attacking Unit {}".format(my_unit.id, enemy_units[0].id))

                # Move the unit back to a shelter to recharge
                else:
                    # Make sure a shelter exists
                    if my_shelter:
                        # Create a path to the shelter
                        path = self.find_path(my_unit.tile, my_shelter.tile)

                        # Try to move the soldier towards the shelter
                        if len(path) > 1:
                            if my_unit.move(path[0]):
                                print("Moving Unit {} to Tile {}".format(my_unit.id, path[0].id))

                        # If the unit isn't trying to move to the shelter, have it try to recharge (rest)
                        else:
                            # Grab the neighbors of the current Unit
                            my_neighbors = my_unit.tile.get_neighbors()
                            # Add the tile that the unit is standing on in case it is on top of a shelter
                            my_neighbors.append(my_unit.tile)

                            # Check for a shelter in the units neighbors
                            if self.check_for_shelter(my_neighbors):
                                # Try to recharge (rest)
                                if my_unit.rest():
                                    print("Unit {} is resting".format(my_unit.id))

            elif my_unit.job.title == "gatherer":
                # Grab the neighbors of the current Unit
                my_neighbors = my_unit.tile.get_neighbors()
                # Add the tile that the unit is standing on in case it is on top of a food resource
                my_neighbors.append(my_unit.tile)

                # Loop through the neighboring tiles
                for neighbor in my_neighbors:
                    # Check if food can be harvested from the neighboring tile
                    if neighbor.harvest_rate > 0 and neighbor.turns_to_harvest == 0:
                        # Attempt to harvest food
                        if my_unit.harvest(neighbor):
                            print("Unit {} harvested food from Tile {}".format(my_unit.id, neighbor.id))
                            break

                # Check if the unit has any food
                if my_unit.food > 0:
                    # Try to drop all your food because, you know, who needs it? Why did you even harvest it?
                    if my_unit.drop(my_unit.tile, "food", 0):
                        print("Unit {} dropped their food on Tile {}".format(my_unit.id, my_unit.tile.id))

            elif my_unit.job.title == "builder":

                # Grab the neighbors of the current Unit
                my_neighbors = my_unit.tile.get_neighbors()

                # Loop through the neighboring tiles
                for neighbor in my_neighbors:
                    # Check for materials on a neighboring tile
                    if neighbor.materials > 0:
                        # Try to pickup as many materials as possible
                        if my_unit.pickup(neighbor, "materials", 0):
                            print("Unit {} is picking up materials on Tile {}".format(my_unit.id, neighbor.id))

                # Loop through the neighboring tiles
                for neighbor in my_neighbors:
                    # Check for a neutral structure nearby
                    if neighbor.structure and neighbor.structure.type == "neutral":
                        # Attempt to deconstruct the neutral structure
                        if my_unit.deconstruct(neighbor):
                            print("Unit {} deconstructed a Structure on Tile {}".format(my_unit.id, neighbor.id))

                # See if the builder can build a wall
                if my_unit.materials >= 50:
                    # Loop through the neighboring tiles
                    for neighbor in neighbors:
                        # Check if any of the surrounding tiles are open to build something on
                        if neighbor.structure == None and neighbor.unit == None:
                            # Attempt to contruct wall
                            if my_unit.construct(neighbor, "wall"):
                                print("Unit {} constructed a wall on Tile {}".format(my_unit.id, neighbor.id))

            elif my_unit.job.title == "missionary":
                # Grab the neighbors of the current Unit
                my_neighbors = my_unit.tile.get_neighbors()

                # Loop through neighboring tiles
                for neighbor in my_neighbors:
                    # Find a neutral fresh human
                    if neighbor.unit and neighbor.unit.job.title == "fresh human" and neighbor.unit.owner == None:
                        # Attempts to convert neutral fresh human
                        if my_unit.convert(neighbor):
                            print("Unit {} converted Unit {} to a friendly fresh human".format(my_unit.id, neighbor.unit.id))

            else: # my_unit.job.title == "cat overlord":
                pass
                # stand there and look pretty?

            # Used for spacing between unit output
            print("")

        # Used for spacing between output for each turn
        print("\n\n")

        return True
        # <<-- /Creer-Merge: runTurn -->>

    def find_path(self, start, goal):
        """A very basic path finding algorithm (Breadth First Search) that when given a starting Tile, will return a valid path to the goal Tile.
        Args:
            start (Tile): the starting Tile
            goal (Tile): the goal Tile
        Returns:
            list[Tile]: A list of Tiles representing the path, the the first element being a valid adjacent Tile to the start, and the last element being the goal.
        """

        if start == goal:
            # no need to make a path to here...
            return []

        # queue of the tiles that will have their neighbors searched for 'goal'
        fringe = []

        # How we got to each tile that went into the fringe.
        came_from = {}

        # Enqueue start as the first tile to have its neighbors searched.
        fringe.append(start)

        # keep exploring neighbors of neighbors... until there are no more.
        while len(fringe) > 0:
            # the tile we are currently exploring.
            inspect = fringe.pop(0)

            # cycle through the tile's neighbors.
            for neighbor in inspect.get_neighbors():
                # if we found the goal, we have the path!
                if neighbor == goal:
                    # Follow the path backward to the start from the goal and return it.
                    path = [goal]

                    # Starting at the tile we are currently at, insert them retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.insert(0, inspect)
                        inspect = came_from[inspect.id]
                    return path
                # else we did not find the goal, so enqueue this tile's neighbors to be inspected

                # if the tile exists, has not been explored or added to the fringe yet, and it is pathable
                if neighbor and neighbor.id not in came_from and neighbor.is_pathable():
                    # add it to the tiles to be explored and add where it came from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

        # if you're here, that means that there was not a path to get to where you want to go.
        #   in that case, we'll just return an empty path.
        return []

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    def check_for_shelter(self, my_neighbors):
        # Loop through neighbors of the unit
        for neighbor in my_neighbors:
            # Check and see if the unit is next to one of its shelters
            if neighbor.structure and neighbor.structure.type == "shelter" and neighbor.structure.owner == self.player:
                return True # Shelter found

        return False # No shelter found

    # <<-- /Creer-Merge: functions -->>
