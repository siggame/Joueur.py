# NOTE: this is where you code your gameplay logic!
from checkers.generatedAI import GeneratedAI
from random import shuffle

# @class BaseAI: the basic AI functions that are the same between games
class AI(GeneratedAI):
    # this is called once the game starts and your ai knows its playerID and game. You can initialize your AI here.
    def init(self):
        game = self.game.state
        self.checkersMap = [[False for y in range(game.boardWidth)] for x in range(game.boardHeight)]

    def getName(self):
        return "Test Python Player"

        # this is called when the game's state updates, so if you are tracking anything you can update it here.
    def gameUpdated(self):
        game = self.game.state

        for x in range(game.boardWidth):
            for y in range(game.boardHeight):
                self.checkersMap[x][y] = None

        self.myCheckers = []
        self.forceChecker = False
        self.cantMove = False
        for checker in game.checkers:
            self.checkersMap[checker.x][checker.y] = checker
            if checker.ownerID is self.playerID:
                self.myCheckers.append(checker)
                if checker.id is game.checkerMovedID:
                    if game.checkerMovedJumped:
                        self.forceChecker = checker
                    else:
                        self.cantMove = True


    # this is called every time the server talls you that you can send a command. Once you send a command any you send will be disregarded, so return upon doing so
    def run(self):
        if self.cantMove:
            return self.done()

        game = self.game.state
        checkers = self.myCheckers

        if self.forceChecker is not False:
            checkers = [ self.forceChecker ]

        shuffle(checkers)

        yDirection = 1 if self.playerID is 0 else -1 # the first player (id == 0) moves down, the second (id == 1) moves up, we need to know that so unkinged peices don't try to move in illegal directions

        for checker in checkers:
            neighbors = [ # valid move directions for all peices moving in the direction of their player's y (yDirection)
                {'x': checker.x + 1, 'y': checker.y + yDirection, 'requires jump': False},
                {'x': checker.x - 1, 'y': checker.y + yDirection, 'requires jump': False},
            ]

            if checker.kinged: # add the reversed yDirection neighbors to investigate moving to, because kinged peices can move in reverse
                neighbors.extend([
                    {'x': checker.x + 1, 'y': checker.y - yDirection, 'requires jump': False},
                    {'x': checker.x - 1, 'y': checker.y - yDirection, 'requires jump': False},
                ])

            shuffle(neighbors)

            while len(neighbors) > 0: # try to find a valid neighbor to move to
                neighbor = neighbors.pop()

                if neighbor['x'] >= game.boardWidth or neighbor['x'] < 0 or neighbor['y'] >= game.boardHeight or neighbor['y'] < 0:
                    continue # because we can't use this neighbor as it is out of bounds

                if self.forceChecker is not False: # then we must jump
                    if neighbor['requires jump']:
                        return self.move(checker, x=neighbor['x'], y=neighbor['y'])
                else:
                    jumpingChecker = self.checkersMap[neighbor['x']][neighbor['y']]
                    if jumpingChecker is None: # there's no checker there, so it's valid!
                        return self.move(checker, x=neighbor['x'], y=neighbor['y'])
                    elif jumpingChecker.ownerID is not checker.ownerID: #there is one to jump so let's try to jump it
                        if not neighbor['requires jump']: # then we have not already jumped to get here, so let's try to jump it
                            dx = neighbor['x'] - checker.x
                            dy = neighbor['y'] - checker.y

                            neighbors.append({'x': neighbor['x'] + dx, 'y': neighbor['y'] + dy, 'requires jump': True})

        # if we got here we couldn't find a valid move for all our checkers :(
        return self.done()




    # this is called when the server is no longer taking game commands from you, normally when you turn ends
    def ignoring(self):
        pass


    # this is called when the game closes (ends), you can clean up your data and dump files here if need be
    def close(self):
        pass
