# This is where you build your AI for the Stumped game.

from joueur.base_ai import BaseAI
from math import floor, ceil
from random import random

# these functions are used by the ShellAI, you can remove them if you wish with the ShellAI code in runTurn()

# Simply returns a random element of an array
def random_element(items):
    if items:
        return items[floor(random()*len(items))]

    return None

# Simply returns a shuffled copy of an array
def shuffled(a):
    if a:
        for i in range(len(a)-1, -1, -1):
            j = floor(random() * i)
            x = a[i - 1]
            a[i - 1] = a[j]
            a[j] = x
        return a

    return None

class AI(BaseAI):
    """ The basic AI functions that are the same between games. """

    def get_name(self):
        """ This is the name you send to the server so your AI will control the player named this string.

        Returns
            str: The name of your Player.
        """
        return "Stumped Python Player" # REPLACE THIS WITH YOUR TEAM NAME

    def start(self):
        """ This is called once the game starts and your AI knows its playerID and game. You can initialize your AI here.
        """
        # replace with your start logic

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # replace with your game updated logic

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why you won or lost.
        """
        # replace with your end logic
    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # This is your Stumped ShellAI
        # ShellAI is intended to be a simple AI that does everything possible in the game, but plays the game very poorly
        # This example code does the following:
        # 1. Grabs a single beaver
        # 2. tries to move the beaver
        # 3. tries to do one of the 5 actions on it
        # 4. Grabs a lodge and tries to recruit a new beaver

        # First let's do a simple print statement telling us what turn we are on
        print('My Turn {}'.format(self.game.current_turn))

        beaver = None
        # 1. get the first beaver to try to do things with
        if len(self.player.beavers) > 0:
            beaver = self.player.beavers[0]

        # if we have a beaver, and it's not distracted, and it is alive (health greater than 0)
        if beaver and beaver.turns_distracted == 0 and beaver.health > 0:
            # then let's try to do stuff with it

            # 2. Try to move the beaver
            if beaver.moves >= 3:
            # then it has enough moves to move in any direction, so let's move it

                # find a spawner to move to
                target = None
                for tile in self.game.tiles:
                    if tile.spawner and tile.spawner.health > 1:
                        # then we found a healthy spawner, let's target that tile to move to
                        target = tile
                        break

                if target:
                    # use the pathfinding algorithm below to make a path to the spawner's target tile
                    path = self.find_path(beaver.tile, target)

                    # if there is a path, move to it
                    #      length 0 means no path could be found to the tile
                    #      length 1 means the target is adjacent, and we can't move onto the same tile as the spawner
                    #      length 2+ means we have to move towards it
                    if len(path) > 1:
                        print('Moving {} towards {}'.format(beaver, target))
                        beaver.move(path[0])

            # 3. Try to do an action on the beaver
            if beaver.actions > 0:
                # then let's try to do an action!

                # Do a random action!
                action = random_element(['build_lodge', 'attack', 'pickup', 'drop', 'harvest'])

                # how much this beaver is carrying, used for calculations
                load = beaver.branches + beaver.food

                if action == 'build_lodge':
                    # if the beaver has enough branches to build a lodge
                    #   and the tile does not already have a lodge, then do so
                    if (beaver.branches + beaver.tile.branches) >= self.player.branches_to_build_lodge and not beaver.tile.lodge_owner:
                        print('{} building lodge'.format(beaver))
                        beaver.build_lodge()

                elif action == 'attack':
                    # look at all our neighbor tiles and if they have a beaver attack it!
                    for neighbor in shuffled(beaver.tile.get_neighbors()):
                        if neighbor.beaver:
                            print('{} attacking {}'.format(beaver, neighbor.beaver))
                            beaver.attack(neighbor.beaver)
                            break

                elif action == 'pickup':
                    # make an array of our neighboring tiles + our tile as all can be picked up from
                    neighbors = beaver.tile.get_neighbors()
                    neighbors.append(beaver.tile)
                    pickup_tiles = shuffled(neighbors)

                    # if the beaver can carry more resources, try to pick something up
                    if load < beaver.job.carry_limit:
                        for tile in pickup_tiles:
                            # try to pickup branches
                            if tile.branches > 0:
                                print('{} picking up branches'.format(beaver))
                                beaver.pickup(tile, 'branches', 1)
                                break
                            # try to pickup food
                            elif tile.food > 0:
                                print('{} picking up food'.format(beaver))
                                beaver.pickup(tile, 'food', 1)
                                break

                elif action == 'drop':
                    # choose a random tile from our neighbors + out tile to drop stuff on
                    neighbors = beaver.tile.get_neighbors()
                    neighbors.append(beaver.tile)
                    drop_tiles = shuffled(neighbors)

                    # find a valid tile to drop resources onto
                    tile_to_drop_on = None
                    for tile in drop_tiles:
                        if not tile.spawner:
                            tile_to_drop_on = tile
                            break

                    # if there is a tile that resources can be dropped on
                    if tile_to_drop_on:
                        # if we have branches to drop
                        if beaver.branches > 0:
                            print('{} dropping 1 branch'.format(beaver))
                            beaver.drop(tile_to_drop_on, 'branches', 1)
                        # or if we have food to drop
                        elif beaver.food > 0:
                            print('{} dropping 1 food'.format(beaver))
                            beaver.drop(tile_to_drop_on, 'food', 1)

                elif action == 'harvest':
                    # if we can carry more, try to harvest something
                    if load < beaver.job.carry_limit:
                        # try to find a neighboring tile with a spawner on it to harvest from
                        for neighbor in shuffled(beaver.tile.get_neighbors()):
                            # if it has a spawner on that tile, harvest from it
                            if neighbor.spawner:
                                print('{} harvesting {}'.format(beaver, neighbor.spawner))
                                beaver.harvest(neighbor.spawner)
                                break

        # now try to spawn a beaver if we have lodges

        # 4. Get a lodge to try to spawn something at

        lodge = random_element(self.player.lodges)

        # if we found a lodge and it has no beaver blocking it
        if lodge and not lodge.beaver:
            # then this lodge can have a new beaver appear here

            # We need to know how many beavers we have to see if they are free to spawn
            alive_beavers = len([beaver for beaver in self.player.beavers if beaver.health > 0])

            # and we need a Job to spawn
            job = random_element(self.game.jobs)

            # if we have less beavers than the freeBeavers count, it is free to spawn
            #    otherwise if that lodge has enough food on it to cover the job's cost
            if alive_beavers < self.game.free_beavers_count or lodge.food >= job.cost:
                # then spawn a new beaver of that job!
                print('Recruiting {} to {}'.format(job, lodge))
                job.recruit(lodge)
                alive_beavers += 1

        print('Done with our turn')
        return True # to signify that we are truly done with this turn


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
