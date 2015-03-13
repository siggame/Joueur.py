# NOTE: this is where you code your gameplay logic!
from baseAI import BaseAI
from random import shuffle

# @class BaseAI: the basic AI functions that are the same between games
class AI(BaseAI):
    def get_name(self):
        return "Test Python Player"


    # this is called once the game starts and your ai knows its player.id and game. You can initialize your AI here.
    def game_initialized(self):
        self.checkers_map = [[False for y in range(self.game.board_width)] for x in range(self.game.board_height)]


        # this is called when the game's state updates, so if you are tracking anything you can update it here.
    def game_updated(self):
        game = self.game

        for x in range(game.board_width):
            for y in range(game.board_height):
                self.checkers_map[x][y] = None

        self.my_checkers = []
        self.force_checker = None
        self.cant_move = False
        for checker in game.checkers:
            self.checkers_map[checker.x][checker.y] = checker
            if checker.owner is self.player:
                self.my_checkers.append(checker)
                if checker is game.checker_moved:
                    if game.checker_moved_jumped:
                        self.force_checker = checker
                    else:
                        self.cant_move = True


    # this is called every time the server talls you that you can send a command. Once you send a command any you send will be disregarded, so return upon doing so
    def run(self):
        if self.cant_move:
            return self.player.end_turn()

        checkers = self.my_checkers

        if self.force_checker != None:
            checkers = [ self.force_checker ]

        shuffle(checkers)

        y_direction = 1 if self.player.id == 0 else -1 # the first player (id == 0) moves down, the second (id == 1) moves up, we need to know that so unkinged peices don't try to move in illegal directions

        for checker in checkers:
            neighbors = [ # valid move directions for all peices moving in the direction of their player's y (y_direction)
                {'x': checker.x + 1, 'y': checker.y + y_direction, 'requires jump': False},
                {'x': checker.x - 1, 'y': checker.y + y_direction, 'requires jump': False},
            ]

            if checker.kinged: # add the reversed y_direction neighbors to investigate moving to, because kinged peices can move in reverse
                neighbors.extend([
                    {'x': checker.x + 1, 'y': checker.y - y_direction, 'requires jump': False},
                    {'x': checker.x - 1, 'y': checker.y - y_direction, 'requires jump': False},
                ])

            shuffle(neighbors)

            while len(neighbors) > 0: # try to find a valid neighbor to move to
                neighbor = neighbors.pop()
                if neighbor['x'] >= self.game.board_width or neighbor['x'] < 0 or neighbor['y'] >= self.game.board_height or neighbor['y'] < 0:
                    continue # because we can't use this neighbor as it is out of bounds

                if self.force_checker != None: # then we must jump
                    if neighbor['requires jump']:
                        return checker.move(x=neighbor['x'], y=neighbor['y'])
                else:
                    jumping = self.checkers_map[neighbor['x']][neighbor['y']]
                    if jumping == None: # there's no checker there, so it's valid!
                        return checker.move(x=neighbor['x'], y=neighbor['y'])
                    elif jumping.owner != checker.owner: #there is one to jump so let's try to jump it
                        if not neighbor['requires jump']: # then we have not already jumped to get here, so let's try to jump it
                            dx = neighbor['x'] - checker.x
                            dy = neighbor['y'] - checker.y

                            neighbors.append({'x': neighbor['x'] + dx, 'y': neighbor['y'] + dy, 'requires jump': True})

        # if we got here we couldn't find a valid move for all our checkers :(
        return self.player.end_turn()



    # this is called when the server is no longer taking game commands from you, normally when you turn ends
    def ignoring(self):
        pass


    # this is called when the game closes (ends), you can clean up your data and dump files here if need be
    def close(self):
        pass
