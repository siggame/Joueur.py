import argparse
import importlib
from client import Client

parser = argparse.ArgumentParser(description='Runs the python client with options. must provide a server and game to connect to')

parser.add_argument('-g, --game', action='store', dest='game', required=True, help='the game name you want to play on the server')
parser.add_argument('-s, --server', action='store', dest='server', default='localhost', help='the url to the server you want to connect to e.g. locahost:3000')
parser.add_argument('-p, --port', action='store', dest='port', help='(optional) the port to connect to on the server. Can be defined on the server arg via server:port')
parser.add_argument('-n, --name', action='store', dest='name', help='(optional) the name you want to use as your AI\'s player name')
parser.add_argument('--session', action='store', dest='session', help='(optional) the game session you want to play on the server', default='*')

args = parser.parse_args()

split = args.server.split(":")
server = split[0]
port = int(args.port or (len(split) == 2 and split[1]))

module = importlib.import_module(args.game) # should load Game and AI to load based on the game selected in args

game = module.Game(args.session)
ai = module.AI(game)

client = Client(game, ai, server, port)

client.ready(args.name)
