# ${header}
# This is a simple class to represent the ${obj_key} object in the game. You can extend it by adding utility functions here in this file.
<%include file="functions.noCreer" /><% parent_classes = obj['parentClasses'] %>
% if len(parent_classes) > 0:
% for parent_class in parent_classes:
from games.${underscore(game_name)}.${underscore(parent_class)} import ${parent_class}
% endfor
% else:
<% if obj_key == "Game":
    parent_classes = [ 'BaseGame' ]
else:
    parent_classes = [ 'BaseGameObject' ]
%>from joueur.${underscore(parent_classes[0])} import ${parent_classes[0]}
% endif

% if obj_key == "Game":
# import game objects
% for game_obj_key in sort_dict_keys(game_objs):
from games.${underscore(game_name)}.${underscore(game_obj_key)} import ${game_obj_key}
% endfor

% endif
${merge("# ", "imports", "# you can add addtional import(s) here")}

class ${obj_key}(${", ".join(parent_classes)}):
    """The class representing the ${obj_key} in the ${game_name} game.

    ${obj['description']}
    """

    def __init__(self):
        """Initializes a ${obj_key} with basic logic as provided by the Creer code generator."""
% for parent_class in reversed(parent_classes):
        ${parent_class}.__init__(self)
% endfor

        # private attributes to hold the properties so they appear read only
% for attr_name in obj['attribute_names']:
<% attr_parms = obj['attributes'][attr_name]
%>        self._${underscore(attr_name)} = ${shared['py']['default'](attr_parms['type'], attr_parms['default'])}
% endfor

% if obj_key == "Game":
        self.name = "${game_name}"

        self._game_object_classes = {<% c = len(game_objs) %>
% for game_obj_key in sort_dict_keys(game_objs):
<% c -= 1
%>            '${game_obj_key}': ${game_obj_key}${',' if c != 0 else ''}
% endfor
        }
% endif

% for attr_name in obj['attribute_names']:
<% attr_parms = obj['attributes'][attr_name] %>
    @property
    def ${underscore(attr_name)}(self):
        """${attr_parms['description']}

        :rtype: ${shared['py']['type'](attr_parms['type'])}
        """
        return self._${underscore(attr_name)}

% endfor
% for function_name in obj['function_names']:
<% function_parms = obj['functions'][function_name]
%>

    def ${underscore(function_name)}(self${shared['py']['args'](function_parms['arguments'])}):
        """ ${function_parms['description']}
% if len(function_parms['arguments']) > 0:

        Args:
% for arg_parms in function_parms['arguments']:
            ${underscore(arg_parms['name'])} (${"Optional[" if arg_parms['optional'] else ""}${shared['py']['type'](arg_parms['type'])}${"]" if arg_parms['optional'] else ""}): ${arg_parms['description']}
% endfor
% endif
% if function_parms['returns']:

        Returns:
            ${shared['py']['type'](function_parms['returns']['type'])}: ${function_parms['returns']['description']}
% endif
        """
        return self._run_on_server('${function_name}'${shared['py']['kwargs'](function_parms['argument_names'])})
% endfor


${merge("    # ", "functions", "    # if you want to add any client side logic (such as state checking functions) this is where you can add them")}
