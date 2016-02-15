import socket, errno
import sys
import os
import json
import time
from joueur.serializer import serialize, deserialize
import joueur.error_code as error_code
from joueur.game_manager import GameManager
import joueur.ansi_color_coder as color

EOT_CHAR = chr(4)

class _Client:
    socket = None

_client = _Client()

## Client: A singlton module that talks to the server receiving game information and sending commands to execute. Clients perform no game logic
def setup(game, ai, manager, server='localhost', port=3000, print_io=False):
    _client.game = game
    _client.ai = ai
    _client.server = server
    _client.port = port
    _client.manager = manager

    _client._print_io = print_io
    _client._received_buffer = ""
    _client._events_stack = []
    _client._buffer_size = 1024
    _client._timeout_time = 1.0

    print(color.text("cyan") + "Connecting to:", _client.server + ":" + str(_client.port) + color.reset())

    try:
        _client.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _client.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # stupid Windows
        _client.socket.settimeout(_client._timeout_time) # so the blocking on recv doesn't hang forever and other system interupts (e.g. keyboard) can be handled
        _client.socket.connect((_client.server, _client.port))
    except socket.error as e:
        error_code.handle_error(error_code.COULD_NOT_CONNECT, e, "Could not connect to " + _client.server + ":" + str(_client.port))


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

def disconnect(exit_code=None):
    if _client.socket:
        _client.socket.close()

def run_on_server(caller, function_name, args=None):
    send("run", {
        'caller': caller,
        'functionName': function_name,
        'args': args
    })

    ran_data = wait_for_event("ran")
    return deserialize(ran_data, _client.game)

def play():
    wait_for_event(None)

def wait_for_event(event):
    while True:
        wait_for_events()

        while len(_client._events_stack) > 0:
            sent = _client._events_stack.pop()
            if event != None and sent['event'] == event:
                return sent['data']
            else:
                _auto_handle(sent['event'], sent['data'] if 'data' in sent else None)

## loops to check the socket for incoming data and ends once some events get found
def wait_for_events():
    if len(_client._events_stack) > 0:
        return # as we already have events to handle, no need to wait for more

    try:
        while True:
            sent = None
            try:
                sent = _client.socket.recv(_client._buffer_size).decode("utf-8")
            except socket.timeout:
                pass # timed out so keyboard/system interupts can be handled, hence the while true loop above
            except socket.error as e:
                error_code.handle_error(error_code.CANNOT_READ_SOCKET, e, "Error reading socket while waiting for events")

            if not sent:
                continue
            elif _client._print_io:
                print("FROM SERVER <--", sent)

            split = (_client._received_buffer + sent).split(EOT_CHAR)
            _client._received_buffer = split.pop() # the last item will either be "" if the last char was an EOT_CHAR, or a partial data we need to buffer anyways

            for json_str in reversed(split):
                try:
                    parsed = json.loads(json_str)
                except ValueError as e:
                    error_code.handle_error(error_code.MALFORMED_JSON, e, "Could not parse json '" + json_str + "'")

                _client._events_stack.append(parsed)

            if len(_client._events_stack) > 0:
                return
    except (KeyboardInterrupt, SystemExit):
        disconnect()

    ## called via the client run loop when data is sent
def _auto_handle(event, data=None):
    g = globals() # the current module, e.g. the Client module that acts as a singleton
    auto_handle_function = g["_auto_handle_" + event]

    if auto_handle_function:
        return auto_handle_function(data)
    else:
        error_code.handle_error(error_code.UNKNOWN_EVENT_FROM_SERVER, message=("Could not auto handle event '" + event + "'."))

def _auto_handle_delta(data):
    try:
        _client.manager.apply_delta_state(data)
    except:
        error_code.handle_error(error_code.DELTA_MERGE_FAILURE, sys.exc_info(), "Error merging delta")

    if _client.ai.player: # then the AI is ready for updates
        _client.ai.game_updated()

def _auto_handle_order(data):
    try:
        returned = _client.ai._do_order(data['name'], data['args'])
    except:
        print("esc info", type(sys.exc_info()))
        error_code.handle_error(error_code.AI_ERRORED, sys.exc_info(), "AI errored executing order '" + data['name'] + "'.")

    send("finished", {
        'orderIndex': data['index'],
        'returned': returned
    })

def _auto_handle_invalid(data):
    try:
        _client.ai.invalid(data['message'])
    except:
        error_code.handle_error(error_code.AI_ERRORED, sys.exc_info(), "AI errored while handling invalid data.")

def _auto_handle_fatal(data):
    error_code.handle_error(error_code.FATAL_EVENT, message="Got a fatal event from the server: " + data['message'])

def _auto_handle_over(data):
    won = _client.ai.player.won
    reason = _client.ai.player.reason_won if _client.ai.player.won else _client.ai.player.reason_lost

    print(color.text("green") + "Game is over.", "I Won!" if won else "I Lost :(", "because: " + reason + color.reset())

    try:
        _client.ai.end(won, reason)
    except:
        error_code.handle_error(error_code.AI_ERRORED, sys.exc_info(), "AI errored during end.")

    if 'message' in data:
        print(color.text("cyan") + data['message'] + color.reset())

    disconnect()
    os._exit(0)

