# ${header}
# This is where you build your AI for the ${game_name} game.
<%include file="functions.noCreer" />
from baseAI import BaseAI

class AI(BaseAI):
    """ the basic AI functions that are the same between games
    """


    def get_name(self):
        """ this is the name you send to the server to play as.

        Returns
            str: the name you want your player to have
        """

        return "${game_name} Python Player"



    def start(self):
        """ this is called once the game starts and your AI knows its player.id and game. You can initialize your AI here.
        """
        pass



    def game_updated(self):
        """ this is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        pass



    def end(self, won, reason):
        """ this is called when the game ends, you can clean up your data and dump files here if need be

        Args:
            won (bool): won == true means you won, won == false means you lost
            reason (str): the reason why you won or lost
        """
        pass
% for function_name, function_parms in ai['functions'].items():


    def ${camel_case_to_underscore(function_name)}(self${", ".join([""] + function_parms['argument_names'])}):
        """ ${function_parms['description']}
% if len(function_parms['arguments']) > 0:

        Args:
% for arg_parms in function_parms['arguments']:
            ${camel_case_to_underscore(arg_parms['name'])} (${shared['py']['type'](arg_parms['type'])}): ${arg_parms['description']}
% endfor
% endif
% if function_parms['returns']:

        Returns:
            ${shared['py']['type'](function_parms['returns']['type'])}: ${shared['py']['type'](function_parms['returns']['description'])}
% endif
        """

        # Put your game logic here for ${function_name}

        return ${shared['py']['default'](function_parms['returns']['type'], function_parms['returns']['default'])}
% endfor
