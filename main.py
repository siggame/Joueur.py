# libraries
from socketIO_client import SocketIO#, LoggingNamespace
import json
import argparse
import importlib
import sys

parser = argparse.ArgumentParser(description='Runs the python client with options. must provide a server and game to connect to')

parser.add_argument('-g, --game', action='store', dest='game', required=True, help='the game name you want to play on the server')
parser.add_argument('-s, --server', action='store', dest='server', required=True, help='the url to the server you want to connect to e.g. locahost:3000')
parser.add_argument('-p, --port', action='store', dest='port', help='(optional) the port to connect to on the server. Can be defined on the server arg via server:port')
parser.add_argument('-n, --name', action='store', dest='name', help='(optional) the name you want to use as your AI\'s player name')
parser.add_argument('--session', action='store', dest='session', help='(optional) the game session you want to play on the server', default='*')

args = parser.parse_args()

split = args.server.split(":")
server = split[0]
port = int(args.port or (len(split) == 2 and split[1]) or 3000)
game_name = args.game

module = importlib.import_module(game_name) # should load Game and AI to load based on the game selected in args

socket = SocketIO(server, port, wait_for_connection=False)

game = module.Game()
ai = module.AI(game, socket)
game.set_ai(ai)
player_name = args.name or ai.get_name() or "Python Player"

#TODO: throw these in a dictionary of lambda functions or something, maybe a class?
def on_connected(message):
    data = json.loads(message)
    print("Connection successful to game '" + data["gameName"] + "' in session '" + str(data["gameSession"]) + "'.")
    ai.connected(data)
    game.connected(data)
socket.on('connected', on_connected)

def on_state(message):
    game.set_state(json.loads(message))
socket.on('state', on_state)

def on_delta(message):
    game.apply_delta_state(json.loads(message))
socket.on('delta', on_delta)

def on_start(message):
    ai.start(json.loads(message))
socket.on('start', on_start)

def on_awaiting(message):
    ai.run()
socket.on('awaiting', on_awaiting)

def on_ignoring(message):
    ai.ignoring()
socket.on('ignoring', on_ignoring)

def on_over(message):
    ai.over()
    socket.disconnect()
    sys.exit()
socket.on('over', on_over)

def on_disconnect(message):
    print("Disconnected from server...")
    sys.exit()
socket.on('disconnect', on_disconnect)

socket.emit('play', json.dumps({
    'playerName': player_name,
    'gameName': game_name,
    'gameSession': args.session or "*"
}))
socket.wait()
