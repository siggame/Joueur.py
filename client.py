import socket
import sys
import json
import time
from serializer import serialize, deserialize 
EOT_CHAR = chr(4)

class _Client:
    pass

_client = _Client()

## Client: A singlton module that talks to the server receiving game information and sending commands to execute. Clients perform no game logic
def setup(game, ai, server='localhost', port=3000, print_io=False):
    _client.game = game
    _client.ai = ai
    _client.server = server
    _client.port = port

    _client._print_io = print_io
    _client._received_buffer = ""
    _client._events_stack = []
    _client._buffer_size = 1024
    _client._timeout_time = 1.0

    print("connecting to:", _client.server + ":" + str(_client.port))

    _client.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _client.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # stupid Windows
    _client.socket.settimeout(_client._timeout_time) # so the blocking on recv doesn't hang forever and other system interupts (e.g. keyboard) can be handled
    _client.socket.connect((_client.server, _client.port))


def _send_raw(string):
    if _client._print_io:
        print("TO SERVER -->", string)
    _client.socket.send(string)

 ## sends the server an event via socket
def send(event, data):
    _send_raw(
        (json.dumps({
            'sentTime': int(time.time()),
            'event': event,
            'data': serialize(data)
        })
        + EOT_CHAR).encode('utf-8')
    )

## disconnects from the server and ends the program
def disconnect():
    print("Disconnected from server...")
    _client.socket.close()
    sys.exit()



def run_on_server(caller, function_name, args=None):
    send("run", {
        'caller': caller,
        'functionName': function_name,
        'args': args
    })

    ran_data = wait_for_event("ran")
    return deserialize(ran_data, _client.game)

def wait_for_event(event):
    while True:
        wait_for_events()

        while len(_client._events_stack) > 0:
            sent = _client._events_stack.pop()
            if sent['event'] == event:
                return sent['data']
            else:
                _auto_handle(sent['event'], sent['data'] if 'data' in sent else None)

## loops to check the socket for incoming data and ends once some events get found
def wait_for_events():
    if len(_client._events_stack) > 0:
        return # as we already have events to handle, no need to wait for more

    try:
        while True:
            sent = ""
            try:
                sent = _client.socket.recv(_client._buffer_size).decode("utf-8")
            except socket.timeout:
                pass

            if not sent:
                continue
            elif _client._print_io:
                print("FROM SERVER <--", sent)

            split = (_client._received_buffer + sent).split(EOT_CHAR)
            _client._received_buffer = split.pop() # the last item will either be "" if the last char was an EOT_CHAR, or a partial data we need to buffer anyways

            for json_str in reversed(split):
                _client._events_stack.append(json.loads(json_str))

            if len(_client._events_stack) > 0:
                return
    except (KeyboardInterrupt, SystemExit):
        disconnect()



    ## called via the client run loop when data is sent
def _auto_handle(event, data=None):
    g = globals() # the current module, e.g. the Client module that acts as a singleton
    my_function = g["_auto_handle_" + event]
    return my_function(data)

def _auto_handle_delta(data):
    _client.game.apply_delta_state(data)

    if _client.ai.player: # then the AI is ready for updates
        _client.ai.game_updated()

def _auto_handle_invalid(data):
    _client.ai.invalid(data)
    print("received invalid data", data)
    disconnect()

def _auto_handle_over(data):
    won = _client.ai.player.won
    reason = _client.ai.player.reason_won if _client.ai.player.won else _client.ai.player.reason_lost

    print("Game is over.", "I Won!" if won else "I Lost :(", "because: " + reason)

    _client.ai.end(won, reason)
    disconnect()
