# ${header}
# This is where you build your AI for the ${game_name} game.
from baseAI import BaseAI

# @class BaseAI: the basic AI functions that are the same between games
class AI(BaseAI):
    # this is the name you send to the server to play as.
    def get_name(self):
        return "${game_name} Python Player"

    # this is called once the game starts and your AI knows its player.id and game. You can initialize your AI here.
    def start(self):
        pass

        # this is called every time the game's state updates, so if you are tracking anything you can update it here.
    def game_updated(self):
        pass

    # this is called when the game ends, you can clean up your data and dump files here if need be
    # @param {boolean} won == true means you won, won == false means you lost
    # @param {string} reason you won or lost
    def end(self, won, reason):
        pass


    #${"##"} Response Functions: functions you must fill out to send data to the game server to actually play the game! #${"##"}

% for function_name, function_parms in ai['functions'].items():
<%
    argument_string = ""
    argument_names = ['self']
    if 'arguments' in function_parms:
        for arg_parms in function_parms['arguments']:
            argument_names.append(camel_case_to_underscore(arg_parms['name']))

    argument_string = ", ".join(argument_names)
%>    #${'#'} ${function_parms['description']}
% if 'arguments' in function_parms:
% for arg_parms in function_parms['arguments']:
    # @param <${arg_parms['type']}> ${arg_parms['name']}: ${arg_parms['description']}
% endfor
% endif
    # @returns <${function_parms['return']['type']}> ${function_parms['return']['description']}
    def ${camel_case_to_underscore(function_name)}(${argument_string}):
        # Put your game logic here for ${function_name}

% endfor
