# ${header}
# This is where you build your AI for the ${game_name} game.
<%include file="functions.noCreer" />
from joueur.base_ai import BaseAI

${merge("# ", "imports", "# you can add addtional import(s) here")}

class AI(BaseAI):
    """ the basic AI functions that are the same between games
    """


    def get_name(self):
        """ this is the name you send to the server to play as.

        Returns
            str: the name you want your player to have
        """
${merge("        # ", "get-name", '        return "' + game_name + ' Python Player" # REPLACE THIS WITH YOUR TEAM NAME')}



    def start(self):
        """ this is called once the game starts and your AI knows its player.id and game. You can initialize your AI here.
        """
${merge("        # ", "start", "        # replace with your start logic")}



    def game_updated(self):
        """ this is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
${merge("        # ", "game-updated", "        # replace with your game updated logic")}



    def end(self, won, reason):
        """ this is called when the game ends, you can clean up your data and dump files here if need be

        Args:
            won (bool): won == true means you won, won == false means you lost
            reason (str): the reason why you won or lost
        """
${merge("        # ", "end", "        # replace with your end logic")}
% for function_name in ai['function_names']:
<% function_parms = ai['functions'][function_name]
%>

    def ${underscore(function_name)}(self${", ".join([""] + function_parms['argument_names'])}):
        """ ${function_parms['description']}
% if len(function_parms['arguments']) > 0:

        Args:
% for arg_parms in function_parms['arguments']:
            ${underscore(arg_parms['name'])} (${shared['py']['type'](arg_parms['type'])}): ${arg_parms['description']}
% endfor
% endif
% if function_parms['returns']:

        Returns:
            ${shared['py']['type'](function_parms['returns']['type'])}: ${function_parms['returns']['description']}
% endif
        """
${merge("        # ", function_name,
"""        # Put your game logic here for {0}
        return {1}
""".format(function_name, shared['py']['default'](function_parms['returns']['type'], function_parms['returns']['default']) if function_parms['returns'] else "")
)}
% endfor


${merge("    # ", "functions", "    # if you need additional functions for your AI you can add them here")}
