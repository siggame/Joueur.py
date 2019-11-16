# This is where you build your AI for the Necrowar game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Necrowar. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.necrowar.game.Game
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.necrowar.player.Player
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Necrowar Python Player" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic

        # Set up varibales to track all relevant information
        self.spawnUnitTile = None
        self.spawnWorkerTile = None
        self.goldMines = []
        self.miners = []
        self.builders = []
        self.units = []
        self.grassByPath = []
        self.enemyCastle = self.player.opponent.towers[0]
        self.myCastle = self.player.towers[0]

        # Fill our variables with tile data
        for tile in self.player.side:
            if tile.is_unit_spawn:
                self.spawnUnitTile = tile
            elif tile.is_worker_spawn:
                self.spawnWorkerTile = tile
            elif tile.is_gold_mine:
                self.goldMines.append(tile)
            elif tile.is_grass:
                for neighbor in tile.get_neighbors():
                    if neighbor.is_path:
                        self.grassByPath.append(tile)

        # Now we should have our spawn tiles, mines, and tower building locations!

        # <<-- /Creer-Merge: start -->>

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are
        tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and
            dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won
            or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """

        # Remove any dead units from our personal tracking lists
        self.miners = [miner for miner in self.miners if miner.health]
        self.builders = [builder for builder in self.builders if builder.health]
        self.units = [unit for unit in self.units if unit.health]

        # Spawn all three of our chosen unit types if necessary
        if not self.miners:
            if self.spawnWorkerTile.spawn_worker():
                self.miners.append(self.player.units[-1])
        
        if not self.builders:
            if self.spawnWorkerTile.spawn_worker():
                self.builders.append(self.player.units[-1])

        if not self.units:
            if self.spawnUnitTile.spawn_unit("ghoul"):
                self.units.append(self.player.units[-1])

        # Activate all the different units in our lists
        for miner in self.miners:
            if miner.tile.is_gold_mine:
                miner.mine(miner.tile)
            else:
                path = self.find_path_worker(miner.tile, self.goldMines[0])
                for tile in path:
                    if miner.moves <= 0:
                        break
                    miner.move(tile)
        
        for builder in self.builders:
            path = self.find_path_worker(builder.tile, self.grassByPath[0])
            for tile in path:
                if builder.moves <= 0:
                    break
                builder.move(tile)
            if path == [] and builder.moves > 0:
                builder.build("arrow")
        
        for unit in self.units:
            path = self.find_path(unit.tile, self.enemyCastle.tile.tile_south)
            for tile in path:
                if unit.moves <= 0:
                    break
                unit.move(tile)
            if path == [] and unit.moves > 0:
                unit.attack(self.enemyCastle.tile)
        
        # Make towers attack anything adjacent to them
        # Note that they are not using their full range
        for tower in self.player.towers:
            adjacent = tower.tile.get_neighbors()
            for tile in adjacent:
                if tile.unit and tile.unit.owner == self.player.opponent:
                    tower.attack(tile)
        
        return True
        # <<-- /Creer-Merge: runTurn -->>

    def find_path(self, start, goal):
        """A very basic path finding algorithm (Breadth First Search) that when
            given a starting Tile, will return a valid path to the goal Tile.

        Args:
            start (games.necrowar.tile.Tile): the starting Tile
            goal (games.necrowar.tile.Tile): the goal Tile
        Returns:
            list[games.necrowar.tile.Tile]: A list of Tiles
            representing the path, the the first element being a valid adjacent
            Tile to the start, and the last element being the goal.
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
                    # Follow the path backward to the start from the goal and
                    # # return it.
                    path = [goal]

                    # Starting at the tile we are currently at, insert them
                    # retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.insert(0, inspect)
                        inspect = came_from[inspect.id]
                    return path
                # else we did not find the goal, so enqueue this tile's
                # neighbors to be inspected

                # if the tile exists, has not been explored or added to the
                # fringe yet, and it is pathable
                if neighbor and neighbor.id not in came_from and (
                    neighbor.is_pathable()
                ):
                    # add it to the tiles to be explored and add where it came
                    # from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

        # if you're here, that means that there was not a path to get to where
        # you want to go; in that case, we'll just return an empty path.
        return []

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here

    def find_path_worker(self, start, goal):
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
                    # Follow the path backward to the start from the goal and
                    # # return it.
                    path = [goal]

                    # Starting at the tile we are currently at, insert them
                    # retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.insert(0, inspect)
                        inspect = came_from[inspect.id]
                    return path
                # else we did not find the goal, so enqueue this tile's
                # neighbors to be inspected

                # if the tile exists, has not been explored or added to the
                # fringe yet, and it is pathable
                if neighbor and neighbor.id not in came_from and (
                    neighbor.isPathableWorker()
                ):
                    # add it to the tiles to be explored and add where it came
                    # from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

    # <<-- /Creer-Merge: functions -->>
