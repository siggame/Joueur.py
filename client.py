from socketIO_client import SocketIO#, LoggingNamespace
import sys
import json
from serializer import serialize

class Client():
    def __init__(self, game, ai, server='localhost', port=3000):
        self.server = server
        self.port = port if port > 0 else 3000
        self.ai = ai
        self.game = game

        self.game.set_client(self)
        self.game.set_ai(self.ai)

        print("connecting to:", self.server, self.port)
        self.socket = SocketIO(self.server, self.port, wait_for_connection=False)
        self.socket.on('connected', self.on_connected)
        self.socket.on('delta', self.on_delta)
        self.socket.on('start', self.on_start)
        self.socket.on('awaiting', self.on_awaiting)
        self.socket.on('ignoring', self.on_ignoring)
        self.socket.on('over', self.on_over)
        self.socket.on('disconnect', self.on_disconnect)

    def on_connected(self, message):
        data = json.loads(message)
        self.ai.connected(data)
        self.game.connected(data)
        print("Connection successful to game '" + self.game.name + "' in session '" + self.game.session + "'.")

    def on_delta(self, message):
        print("got delta", message)
        self.game.apply_delta_state(json.loads(message))

    def on_start(self, message):
        self.ai.start(json.loads(message))

    def on_awaiting(self, message):
        self.ai.run()

    def on_ignoring(self, message):
        self.ai.ignoring()

    def on_over(self, message):
        self.ai.over()
        self.socket.disconnect()
        sys.exit()

    def on_disconnect(self, message):
        print("Disconnected from server...")
        sys.exit()

    def ready(self, player_name):
        self.socket.emit('play', json.dumps({
            'playerName': player_name or self.ai.get_name() or "Python Player",
            'gameName': self.game.name,
            'gameSession': self.game.session or "*"
        }))
        self.socket.wait()

    def send_command(self, caller, command, **kwargs):
        data = kwargs

        data['command'] = command
        data['caller'] = caller
        data = serialize(data)

        self.socket.emit("command", json.dumps(data))
