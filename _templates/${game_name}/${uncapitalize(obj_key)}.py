# ${header}
# This is a simple class to represent the ${obj_key} object in the game. You can extend it by adding utility functions here in this file.
<%include file="functions.noCreer" /><% parent_classes = obj['parentClasses'] %>
% if len(parent_classes) > 0:
% for parent_class in parent_classes:
from ${game_name}.${uncapitalize(parent_class)} import ${parent_class}
% endfor
% else:
<% if obj_key == "Game":
    parent_classes = [ 'BaseGame' ]
else:
    parent_classes = [ 'BaseGameObject' ]
%>from ${uncapitalize(parent_classes[0])} import ${parent_classes[0]}
% endif

% if obj_key == "Game":
# import game objects
% for game_obj_key, game_obj in game_objs.items():
from ${game_name}.${uncapitalize(game_obj_key)} import ${game_obj_key}
% endfor

% endif
${merge("# ", "imports", "# you can add addtional require(s) here")}

class ${obj_key}(${", ".join(parent_classes)}):
    """ The class representing the ${obj_key} in the ${game_name} game.

    ${obj['description']}
    """

    def __init__(self, data):
        """ initializes a ${obj_key} with basic logic as provided by the Creer code generator

        Args:
            data (dict): initialization data
        """
% for parent_class in reversed(parent_classes):
        ${parent_class}.__init__(self, data)
% endfor

        # The following values should get overridden when delta states are merged, but we set them here as a reference for you to see what variables this class has.

% for attr_name, attr_parms in obj['attributes'].items():
        # ${attr_parms['description']}
        self.${camel_case_to_underscore(attr_name)} = ${shared['py']['default'](attr_parms['type'], attr_parms['default'])}
% endfor

% if obj_key == "Game":
        self.name = "${game_name}"

        self._game_object_classes = {<% c = len(game_objs) %>
% for game_obj_key, game_obj in game_objs.items():
<% c -= 1
%>            '${game_obj_key}': ${game_obj_key}${',' if c != 0 else ''}
% endfor
        }
% endif
% for function_name, function_parms in obj['functions'].items():


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
        return self._run_on_server('${function_name}'${shared['py']['kwargs'](function_parms['argument_names'])})
% endfor


${merge("# ", "functions", "# if you want to add any client side logic (such as state checking functions) this is where you can add them")}
