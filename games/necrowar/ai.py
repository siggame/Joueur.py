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
        spawnWorkerTiles = []
        spawnUnitTiles = []
        for tile in self.player.side:
            if tile.owner == this.player:
                if tile.isWorkerSpawn:
                    spawnWorkerTiles.append(tile)
                elif tile.isUnitSpawn:
                    spawnUnitTiles.append(tile)

        gold = self.player.gold
        mana = self.player.man
        numWorkers = 0
        numUnits = 0
        for unit in self.player.units:
            if unit.job.title == "worker":
                numWorkers+=1
            else:
                numUnits+=1

        if (numWorkers < 5):
            spawnWorkerTiles[0].spawnWorker()

        if (numUnits < 3):
            spawnUnitTiles[0].spawnUnit("ghoul")

        enemy = None;
        if (self.player == self.game.players.get[0]):
            enemy = self.game.players.get(1)
        else:
            enemy = self.game.players.get(0)

        # Go through all the units that you own.
        target = None;
        for unit in self.player.units:
            # Only tries to do something if the unit actually exists.
            # if a unit does not have a tile, then they are dead.
            if not (unit == None) and not (unit.tile == None):
                if unit.job.title.equals("worker"):
                    # if the unit is a worker, go to mine and collect gold
                    target = None

                    # Goes through all tiles in the game and finds a mine.
                    # Should only have four workers over at the mine.
                    for tile in self.game.tiles:
                        # If that mine is on my side, is a gold mine, and have no units on it
                        if tile.isGoldMine and self.player.side.contains(tile) and tile.unit == None:
                            # Send it to that tile
                            target = tile
                        # If the tile is a tower and on my side, and has no other units on it.
                        elif tile.isTower and self.player.side.contains(tile) and tile.unit == None:
                            # Send it to that tile
                            target = tile
                    # Else, try fishing
                    if target == None:
                        # All river spots
                        riverSpots = []
                        for tile in game.tiles:
                            # Gathers all river spots
                            if tile.isRiver and self.player.side.contains(tile):
                                riverSpots.add(tile)
                        # Go through all game titles and find all adjacent spots to the river
                        for tile in game.tiles:
                            foundRiverSpot = False;
                            for spot in riverSpots:
                                foundRiverSpot = tile.getNeighbors().contains(spot);
                            # Only does anything if tile is adjacent to river
                            if foundRiverSpot and player.side.contains(tile):
                                while unit.moves > 0 and not findPath(unit.tile, tile).isEmpty():
                                    # Moves unit until there are no moves left for the worker or at the tile
                                    if not unit.move(findPath(unit.tile, tile)[0]):
                                        unit.move(target)
                                # Fish
                                if not unit.acted:
                                    unit.fish(tile)
                                break
                    else:
                        # Move to the target, whether that be mine or tower
                        while unit.moves > 0 and not findPath(unit.tile, target).isEmpty():
                            if not unit.move(findPath(unit.tile, target)[0]):
                                unit.move(target)
                        # Checks whether the target is a mine or tower. Acts accordingly
                        if not unit.acted:
                            if target.isGoldMine:
                                unit.acted = True
                                unit.mine(target.tile)
                            elif (target.isTower):
                                unit.acted = true
                                unit.build("arrow")
                elif unit.job.title.equals("ghoul"):
                    # Finds enemy towers
                    target = None

                    for tile in game.tiles:
                        if tile.isTower and enemy.side.contains(tile) and not tile.unit == None:
                            target = tile
                            # Moves towards our target until at the target or out of moves.
                            while unit.moves > 0 and len(findPath(unit.tile, target)) > 1):
                                if not unit.move(findPath(unit.tile, target)[0]):
                                    unit.move(target)
                                if not unit.acted:
                                       unit.attack(target)
                        elif target == None
                            target = None
                            for tileTarget in game.tiles:
                                if tileTarget.isCastle and enemy.side.contains(tileTarget) and not tileTarget.unit == null:
                                    target = tileTarget
                                    # Moves towards our target until at the target or out of moves.
                                    while unit.moves > 0 and len(findPath(unit.tile, target)) > 1:
                                        if not unit.move(findPath(unit.tile, target)[0]):
                                            unit.move(target)
                                        if not unit.acted:
                                                unit.attack(target)
                                                unit.acted = True
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
    # <<-- /Creer-Merge: functions -->>
