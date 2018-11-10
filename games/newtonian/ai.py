# This is where you build your AI for the Newtonian game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here

# Un-comment this line if you would like to use the debug map, which requires the colorama package.
# from colorama import init, Fore, Back, Style

# <<-- /Creer-Merge: imports -->>


class AI(BaseAI):
    """ The AI you add and improve code inside to play Newtonian. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.newtonian.game.Game
        """
        return self._game  # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.newtonian.player.Player
        """
        return self._player  # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Newtonian Python Player"  # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic

        # Un-comment this line if you are using colorama for the debug map.
        # init()

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
        # Put your game logic here for runTurn

        """
        Please note: This code is intentionally bad. You should try to optimize everything here. THe code here is only to show you how to use the game's
                     mechanics with the MegaMinerAI server framework.
        """

        # Goes through all the units that you own.
        for unit in self.player.units:
            # Only tries to do something if the unit actually exists.
            if unit is not None and unit.tile is not None:
                if unit.job.title == 'physicist':
                    # If the unit is a physicist, tries to work on machines that are ready, but if there are none,
                    # it finds and attacks enemy managers.

                    # Tries to find a workable machine for blueium ore.
                    # Note: You need to get redium ore as well.
                    target = None

                    # Goes through all the machines in the game and picks one that is ready to process ore as its target.
                    for machine in self.game.machines:
                        if machine.tile.blueium_ore >= machine.refine_input:
                            target = machine.tile

                    if target is None:
                        # Chases down enemy managers if there are no machines that are ready to be worked.
                        for enemy in self.game.units:
                            # Only does anything if the unit that we found is a manager and belongs to our opponent.
                            if enemy.tile is not None and enemy.owner == self.player.opponent and enemy.job.title == 'manager':
                                # Moves towards the manager.
                                while unit.moves > 0 and len(self.find_path(unit.tile, enemy.tile)) > 0:
                                    # Moves until there are no moves left for the physicist.
                                    if not unit.move(self.find_path(unit.tile, enemy.tile)[0]):
                                        break

                                if unit.tile in enemy.tile.get_neighbors():
                                    if enemy.stun_time == 0 and enemy.stun_immune == 0:
                                        # Stuns the enemy manager if they are not stunned and not immune.
                                        unit.act(enemy.tile)
                                    else:
                                        # Attacks the manager otherwise.
                                        unit.attack(enemy.tile)
                                break

                    else:
                        # Gets the tile of the targeted machine if adjacent to it.
                        adjacent = False
                        for tile in target.get_neighbors():
                            if tile == unit.tile:
                                adjacent = True

                        # If there is a machine that is waiting to be worked on, go to it.
                        while unit.moves > 0 and len(self.find_path(unit.tile, target)) > 1 and not adjacent:
                            if not unit.move(self.find_path(unit.tile, target)[0]):
                                break

                        # Acts on the target machine to run it if the physicist is adjacent.
                        if adjacent and not unit.acted:
                            unit.act(target)

                elif unit.job.title == 'intern':
                    # If the unit is an intern, collects blueium ore.
                    # Note: You also need to collect redium ore.

                    # Goes to gather resources if currently carrying less than the carry limit.
                    if unit.blueium_ore < unit.job.carry_limit:
                        # Your intern's current target.
                        target = None

                        # Goes to collect blueium ore that isn't on a machine.
                        for tile in self.game.tiles:
                            if tile.blueium_ore > 0 and tile.machine is None:
                                target = tile
                                break

                        # Moves towards our target until at the target or out of moves.
                        if len(self.find_path(unit.tile, target)) > 0:
                            while unit.moves > 0 and len(self.find_path(unit.tile, target)) > 0:
                                if not unit.move(self.find_path(unit.tile, target)[0]):
                                    break

                        # Picks up the appropriate resource once we reach our target's tile.
                        if unit.tile == target and target.blueium_ore > 0:
                            unit.pickup(target, 0, 'blueium ore')

                    else:
                        # Deposits blueium ore in a machine for it if we have any.

                        # Finds a machine in the game's tiles that takes blueium ore.
                        for tile in self.game.tiles:
                            if tile.machine is not None and tile.machine.ore_type == 'blueium':
                                # Moves towards the found machine until we reach it or are out of moves.
                                while unit.moves > 0 and len(self.find_path(unit.tile, tile)) > 1:
                                    if not unit.move(self.find_path(unit.tile, tile)[0]):
                                        break

                                # Deposits blueium ore on the machine if we have reached it.
                                if len(self.find_path(unit.tile, tile)) <= 1:
                                    unit.drop(tile, 0, 'blueium ore')

                elif unit.job.title == 'manager':
                    # Finds enemy interns, stuns, and attacks them if there is no blueium to take to the generator.
                    target = None

                    for tile in self.game.tiles:
                        if tile.blueium > 1 and unit.blueium < unit.job.carry_limit:
                            target = tile

                    if target is None and unit.blueium == 0:
                        for enemy in self.game.units:
                            # Only does anything for an intern that is owned by your opponent.
                            if enemy.tile is not None and enemy.owner == self.player.opponent and enemy.job.title == 'intern':
                                # Moves towards the intern until reached or out of moves.
                                while unit.moves > 0 and len(self.find_path(unit.tile, enemy.tile)) > 0:
                                    if not unit.move(self.find_path(unit.tile, enemy.tile)[0]):
                                        break

                                # Either stuns or attacks the intern if we are within range.
                                if unit.tile in enemy.tile.get_neighbors():
                                    if enemy.stun_time == 0 and enemy.stun_immune == 0:
                                        # Stuns the enemy intern if they are not stunned and not immune.
                                        unit.act(enemy.tile)
                                    else:
                                        # Attacks the intern otherwise.
                                        unit.attack(enemy.tile)
                                break

                    elif target is not None:
                        # Moves towards our target until at the target or out of moves.
                        while unit.moves > 0 and len(self.find_path(unit.tile, target)) > 1:
                            if not unit.move(self.find_path(unit.tile, target)[0]):
                                break

                        # Picks up blueium once we reach our target's tile.
                        if len(self.find_path(unit.tile, target)) <= 1 and target.blueium > 0:
                            unit.pickup(target, 0, 'blueium')

                    elif target is None and unit.blueium > 0:
                        # Stores a tile that is part of your generator.
                        gen_tile = self.player.generator_tiles[0]

                        # Goes to your generator and drops blueium in.
                        while unit.moves > 0 and len(self.find_path(unit.tile, gen_tile)) > 0:
                            if not unit.move(self.find_path(unit.tile, gen_tile)[0]):
                                break

                        # Deposits blueium in our generator if we have reached it.
                        if len(self.find_path(unit.tile, gen_tile)) <= 1:
                            unit.drop(gen_tile, 0, 'blueium')


        return True
        # <<-- /Creer-Merge: runTurn -->>

    def find_path(self, start, goal):
        """A very basic path finding algorithm (Breadth First Search) that when
            given a starting Tile, will return a valid path to the goal Tile.

        Args:
            start (games.newtonian.tile.Tile): the starting Tile
            goal (games.newtonian.tile.Tile): the goal Tile
        Returns:
            list[games.newtonian.tile.Tile]: A list of Tiles
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
    def display_map(self):
        """A function to display the current state of the map, mainly used for
            debugging without the visualizer. Use this to see a live view of what
            is happening during a game, but the visualizer should be much clearer
            and more helpful. To use this, make sure to un-comment the import for
            colorama and download it with pip.
        """

        print('\033[0;0H', end='')

        for y in range(0, self.game.map_height):
            print(' ', end='')
            for x in range(0, self.game.map_width):
                t = self.game.tiles[y * self.game.map_width + x]

                if t.machine is not None:
                    if t.machine.ore_type == 'redium':
                        print(Back.RED, end='')
                    else:
                        print(Back.BLUE, end='')
                elif t.is_wall:
                    print(Back.BLACK, end='')
                else:
                    print(Back.WHITE, end='')

                foreground = ' '

                if t.machine is not None:
                    foreground = 'M'

                print(Fore.WHITE, end='')

                if t.unit is not None:
                    if t.unit.owner == self.player:
                        print(Fore.CYAN, end='')
                    else:
                        print(Fore.MAGENTA, end='')

                    foreground = t.unit.job.title[0].upper()
                elif t.blueium > 0 and t.blueium >= t.redium:
                    print(Fore.BLUE, end='')
                    if foreground == ' ':
                        foreground = 'R'
                elif t.redium > 0 and t.redium > t.blueium:
                    print(Fore.RED, end='')
                    if foreground == ' ':
                        foreground = 'R'
                elif t.blueium_ore > 0 and t.blueium_ore >= t.redium_ore:
                    print(Fore.BLUE, end='')
                    if foreground == ' ':
                        foreground = 'O'
                elif t.redium_ore > 0 and t.redium_ore > t.blueium_ore:
                    print(Fore.RED, end='')
                    if foreground == ' ':
                        foreground = 'O'
                elif t.owner is not None:
                    if t.type == 'spawn' or t.type == 'generator':
                        if t.owner == self.player:
                            print(Back.CYAN, end='')
                        else:
                            print(Back.MAGENTA, end='')

                print(foreground + Fore.RESET + Back.RESET, end='')

            if y < 10:
                print(' 0' + str(y))
            else:
                print(' ' + str(y))

        print('\nTurn: ' + str(self.game.current_turn) + ' / '
              + str(self.game.max_turns))
        print(Fore.CYAN + 'Heat: ' + str(self.player.heat)
              + '\tPressure: ' + str(self.player.pressure) + Fore.RESET)
        print(Fore.MAGENTA + 'Heat: ' + str(self.player.opponent.heat)
              + '\tPressure: ' + str(self.player.opponent.pressure) + Fore.RESET)

        return
    # <<-- /Creer-Merge: functions -->>
