# libraries
from socketIO_client import SocketIO#, LoggingNamespace
import json
import argparse
import importlib

parser = argparse.ArgumentParser(description='Runs the python client with options. must provide a server and game to connect to')

parser.add_argument('-g, --game', action='store', dest='game', required=True, help='the game name you want to play on the server')
parser.add_argument('-s, --server', action='store', dest='server', required=True, help='the url to the server you want to connect to e.g. locahost:3000')
parser.add_argument('-p, --port', action='store', dest='port', help='(optional) the port to connect to on the server. Can be defined on the server arg via server:port')
parser.add_argument('-n, --name', action='store', dest='name', help='(optional) the name you want to use as your AI\'s player name')
parser.add_argument('--session', action='store', dest='session', help='(optional) the game session you want to play on the server')

args = parser.parse_args()


serverSplit = args.server.split(":")
server = serverSplit[0]
port = int(args.port or serverSplit[1] or 3000)

gameModule = importlib.import_module(args.game) # should load Game and AI to load based on the game selected in args
socketIO = SocketIO(server, port)

game = gameModule.Game()
ai = gameModule.AI(game, socketIO)
game.setAI(ai)

#TODO: throw these in a dictionary of lambda functions or something, maybe a class?
def onConnected(message):
    data = json.loads(message)
    print("Connection successful to game '" + data["gameName"] + "' in session '" + str(data["gameSession"]) + "' as player named '" + data["playerName"] + "'.")
socketIO.on('connected', onConnected)

def onState(message):
    game.updateState(json.loads(message))
socketIO.on('state', onState)

def onStart(message):
    ai.start(json.loads(message))
socketIO.on('start', onStart)

def onAwaiting(message):
    ai.run()
socketIO.on('awaiting', onAwaiting)

def onIgnoring(message):
    ai.ignoring()
socketIO.on('ignoring', onIgnoring)

def onOver(message):
    ai.over()
    socketIO.disconnect()
socketIO.on('over', onOver)


socketIO.emit('play', "pythonPlayer checkers TestSession")
socketIO.wait()
