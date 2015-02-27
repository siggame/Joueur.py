from socketIO_client import SocketIO#, LoggingNamespace
import json
from game import Game
from ai import AI

def on_aaa_response(*args):
    print('connected', args)

socketIO = SocketIO('localhost', 3000)#, LoggingNamespace)
socketIO.on('connected', on_aaa_response)
socketIO.emit('play', "pythonPlayer checkers TestSession")

game = Game()
ai = AI(game, socketIO)

#TODO: throw these in a dictionary of lambda functions or something, maybe a class?
def onConnected(message):
    data = json.loads(message)
    print("Connection successful to game '" + data["gameName"] + "' in session '" + str(data["gameSession"]) + "' as player named '" + data["playerName"] + "'.")
socketIO.on('connected', onConnected)

def onState(message):
    game.updateState(json.loads(message))
socketIO.on('state', onState)

def onStart(message):
    print("onStart!")
    ai.start(json.loads(message))
socketIO.on('start', onStart)

def onAwaiting(message):
    ai.makeCommand()
socketIO.on('awaiting', onAwaiting)

def onIgnoring(message):
    ai.ignoring()
socketIO.on('ignoring', onIgnoring)

def onOver(message):
    ai.over()
    socketIO.disconnect()
socketIO.on('over', onOver)


socketIO.wait()
