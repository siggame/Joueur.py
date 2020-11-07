# This is where you build your AI for the Saloon game.

from typing import List
from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
import random
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Saloon. """

    @property
    def game(self) -> 'games.saloon.game.Game':
        """games.saloon.game.Game: The reference to the Game instance this AI is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.saloon.player.Player':
        """games.saloon.player.Player: The reference to the Player this AI controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control the player named this string.

        Returns:
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Saloon Python ShellAI" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        # <<-- /Creer-Merge: start -->>

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def run_turn(self) -> bool:
        """This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """

        # This is "ShellAI", some basic code we've provided that does
        # everything in the game for demo purposed, but poorly so you
        # can get to optimizing or overwriting it ASAP
        #
        # ShellAI does a few things:
        # 1. Tries to spawn a new Cowboy
        # 2. Tries to move to a Piano
        # 3. Tries to play a Piano
        # 4. Tries to act

        print("Start of my turn: " + str(self.game.current_turn))

        # Find the active cowboy to try to do things with
        active_cowboy = None
        for cowboy in self.player.cowboys:
            if not cowboy.is_dead:
                active_cowboy = cowboy
                break

        # 1. Try to spawn a cowboy.

        # Randomly select a job.
        new_job = random.choice(self.game.jobs)

        # Count cowboys with selected job
        job_count = 0
        for cowboy in self.player.cowboys:
            if not cowboy.is_dead and cowboy.job == new_job:
                job_count += 1

        # Call in the new cowboy with that job if there aren't too many
        #   cowboys with that job already.
        if self.player.young_gun.can_call_in and job_count < self.game.max_cowboys_per_job:
            print("1. Calling in: " + new_job)
            self.player.young_gun.call_in(new_job)


        # Now lets use him
        if active_cowboy:
            # 2. Try to move to a piano.

            # Find a piano.
            piano = None
            for furnishing in self.game.furnishings:
                if furnishing.is_piano and not furnishing.is_destroyed:
                    piano = furnishing
                    break

            # There will always be pianos or the game will end. No need to check for existence.
            # Attempt to move toward the piano by finding a path.
            if active_cowboy.can_move and not active_cowboy.is_dead:
                print("Trying to use Cowboy #" + active_cowboy.id)

                # find a path from the Tile this cowboy is on to the tile the piano is on
                path = self.find_path(active_cowboy.tile, piano.tile)

                # if there is a path, move to it
                #      length 0 means no path could be found to the tile
                #      length 1 means the piano is adjacent, and we can't move onto the same tile as the piano
                if len(path) > 1:
                    print("2. Moving to Tile #" + path[0].id)
                    active_cowboy.move(path[0])


            # 3. Try to play a nearby piano.

            # make sure the cowboy is alive and is not busy
            if not active_cowboy.is_dead and active_cowboy.turns_busy == 0:
                # look at all the neighboring (adjacent) tiles, and if they have a piano, play it
                neighbors = active_cowboy.tile.get_neighbors()
                for tile in neighbors:
                    # if the neighboring tile has a piano
                    if tile.furnishing and tile.furnishing.is_piano:
                        # then play it
                        print("3. Playing piano (Furnishing) #" + tile.furnishing.id)
                        active_cowboy.play(tile.furnishing)
                        break


            # 4. Try to act with active cowboy
            if not active_cowboy.is_dead and active_cowboy.turns_busy == 0:
                # Get a random neighboring tile.
                neighbor = random.choice(active_cowboy.tile.get_neighbors())

                # Based on job, act accordingly.
                if active_cowboy.job == "Bartender":
                    # Bartenders dispense brews freely, but they still manage to get their due.
                    direction = random.choice(Tile.directions)
                    print("4. Bartender acting on Tile #" + neighbor.id + " with drunkDirection: " + direction)
                    active_cowboy.act(neighbor, direction)
                elif active_cowboy.job == "Brawler":
                    # Brawlers' brains are so pickled, they hardly know friend from foe.
                    # Probably don't ask them act on your behalf.
                    print("4. Brawlers cannot act")
                elif active_cowboy.job == "Sharpshooter":
                    # Sharpshooters aren't as quick as they used to be, and all that ruckus around them
                    # requires them to focus when taking aim.
                    if active_cowboy.focus > 0:
                        print("4. Sharpshooter acting on Tile #" + neighbor.id)
                        active_cowboy.act(neighbor)
                    else:
                        print("4. Sharpshooter doesn't have enough focus. (focus == " + str(active_cowboy.focus) + ")")

        print("Ending my turn.")
        return True # signifies we are done with our turn
        # <<-- /Creer-Merge: runTurn -->>

    def find_path(self, start: 'games.saloon.tile.Tile', goal: 'games.saloon.tile.Tile') -> List['games.saloon.tile.Tile']:
        """A very basic path finding algorithm (Breadth First Search) that when given a starting Tile, will return a valid path to the goal Tile.

        Args:
            start (games.saloon.tile.Tile): The starting Tile to find a path from.
            goal (games.saloon.tile.Tile): The goal (destination) Tile to find a path to.

        Returns:
            list[games.saloon.tile.Tile]: A list of Tiles representing the path, the the first element being a valid adjacent Tile to the start, and the last element being the goal.
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
