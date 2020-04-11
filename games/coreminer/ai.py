# This is where you build your AI for the Coreminer game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Coreminer. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.coreminer.game.Game
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.coreminer.player.Player
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Coreminer Python Player" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        self.lastMined = None
        self.mineTiles = []
        self.supportTiles = []
        for tile in self.player.side:
            if (tile.x == 1):
                self.mineTiles.append(tile) # Tunnel downwards
            elif (tile.y % 6 == 0):
                self.mineTiles.append(tile) # Horizontal tunnels
                if (tile.x % 2 == 0):
                    self.supportTiles.append(tile) # Supports
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
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        if (self.player.units < 5):
            self.player.base_tile.spawn_miner()
        for unit in self.player.units:
            if unit.job == "miner":
                nearTiles = unit.tile.get_neighbors() # get nearby tiles and check for ore
                for tile in nearTiles:
                    if tile.ore > 0:
                        unit.mine(tile, -1) # mine as much as possible
                # Move to base if full
                if (unit.ore + unit.dirt + (unit.bombs * self.game.bomb_size) + unit.building_materials >= unit.max_cargo_capacity):
                    for position in self.find_path(unit.tile, self.player.base_tile):
                        if (unit.moves > 0):
                            unit.move(position)
                    if unit.tile.is_base:
                        # dump and gather building materials for two supports
                        unit.dump(unit.tile, "ore", -1)
                        unit.dump(unit.tile, "dirt", -1)
                        self.player.buy("buildingMaterial", self.game.support_cost * 2)
                        self.player.transfer(unit, "buildingMaterial", self.game.support_cost * 2)
                # Mine along paths and place supports
                if self.mineTiles:
                    target = self.mineTiles[0]
                    for position in self.find_path(unit.tile, target):
                        if (unit.moves > 0):
                            unit.move(position)
                            if position in self.supportTiles:
                                unit.build(position, "support")
                    unit.mine(target)

        return True
        # <<-- /Creer-Merge: runTurn -->>

    def find_path(self, start, goal):
        """A very basic path finding algorithm (Breadth First Search) that when
            given a starting Tile, will return a valid path to the goal Tile.

        Args:
            start (games.coreminer.tile.Tile): the starting Tile
            goal (games.coreminer.tile.Tile): the goal Tile
        Returns:
            list[games.coreminer.tile.Tile]: A list of Tiles
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
