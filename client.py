import socket
import sys
import json
import time
from serializer import serialize

EOT_CHAR = chr(4)

## @class Client: talks to the server recieving game information and sending commands to execute. Clients perform no game logic
class Client():
    def __init__(self, game, ai, server='localhost', port=3000):
        self.server = server
        self.port = port if port > 0 else 3000
        self.ai = ai
        self.game = game
        self.buffer_size = 1024

        self.game.set_client(self)
        self.game.set_ai(self.ai)

        print("connecting to:", self.server, ":", self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # stupid Windows
        self.socket.connect((self.server, self.port))



    ## loops to check the socket for incoming data and runs it when it gets.
    def run(self):
        self.running = True

        buffer = ""
        try:
            while self.running:
                self.socket.settimeout(1.0) # so the blocking on recv doesn't hang forever and other system interupts (e.g. keyboard) can be handled
                recieved = ""
                try:
                    recieved = self.socket.recv(self.buffer_size).decode("utf-8")
                except socket.timeout:
                    pass

                if not recieved:
                    continue

                split = (buffer + recieved).split(EOT_CHAR)
                buffer = split.pop() # the last item will either be "" if the last char was an EOT_CHAR, or a partial data we need to buffer anyways

                for json_str in split:
                    self.recieve_data(json.loads(json_str))
        except (KeyboardInterrupt, SystemExit):
            pass

        self.disconnect()

    ## disconnects from the server and ends the program
    def disconnect(self):
        print("Disconnected from server...")
        self.running = False
        self.socket.close()
        sys.exit()

    ## called via the client run loop when data is recieved
    def recieve_data(self, data):
        my_function = getattr(self, "on_" + data['event'])
        my_function(data['data'] if 'data' in data else None)


    ## sends the server an event via socket
    def send_event(self, event, data):
        self.socket.send((json.dumps(
            {
                'sentTime': int(time.time()),
                'event': event,
                'data': data
            }) + EOT_CHAR).encode('utf-8')
        )

    ## tells the server this player is ready to play a game
    def ready(self, player_name):
        self.send_event('play', {
            'clientType': 'Python',
            'playerName': player_name or self.ai.get_name() or "Python Player",
            'gameName': self.game.name,
            'gameSession': self.game.session or "*"
        })

    ## sends a command on behalf of a caller game object to the server
    def send_command(self, caller, command, **kwargs):
        data = kwargs

        data['command'] = command
        data['caller'] = caller
        data = serialize(data)

        self.send_event("command", data)


    # On Command functions #

    def on_playing(self, data):
        self.ai.connected(data)
        self.game.connected(data)
        print("Connection successful to game '" + self.game.name + "' in session '" + self.game.session + "'.")

    def on_delta(self, data):
        self.game.apply_delta_state(data)

    def on_start(self, data):
        self.ai.start(data)

    def on_awaiting(self, data):
        self.ai.run()

    def on_ignoring(self, data):
        self.ai.ignoring()

    def on_over(self, data):
        self.ai.over()
        self.disconnect()
