# ${header}
# This is a simple class to represent the ${obj_key} object in the game. You can extend it by adding utility functions here in this file.
<% parent_classes = obj['parentClasses'] %>
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

# @class ${obj_key}: ${obj['description']}
class ${obj_key}(${", ".join(parent_classes)}):
    #${'#'} initializes a ${obj_key} with basic logic as provided by the Creer code generator
    # @param <dict> data: initialization data
    def __init__(self, data):
% for parent_class in reversed(parent_classes):
        ${parent_class}.__init__(self, data)
% endfor

% for attr_name, attr_parms in obj['attributes'].items():
<%
    attr_default = attr_parms["default"] if 'default' in attr_parms else None
    attr_type = attr_parms["type"]
    attr_cast = ""

    if attr_type == "string":
        attr_default = '"' + (attr_default if attr_default != None else '') + '"'
        attr_cast = "str"
    elif attr_type == "array":
        attr_default = '[]'
    elif attr_type == "int":
        attr_default = attr_default or 0
        attr_cast = "int"
    elif attr_type == "float":
        attr_default = attr_default or 0
        attr_cast = "float"
    elif attr_type == "dictionary":
        attr_default = '{}'
    elif attr_type == "boolean":
        attr_default = 'False'
        attr_cast = "bool"
    else:
        attr_default = "None"
%>        self.${camel_case_to_underscore(attr_name)} = ${attr_cast}(data['${attr_name}'] if '${attr_name}' in data else ${attr_default})
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
<%
    argument_string = ""
    argument_names = []
    kwargs_string = ""
    kwargs_keys = []
    if 'arguments' in function_parms:
        for arg_parms in function_parms['arguments']:
            var = camel_case_to_underscore(arg_parms['name'])
            argument_names.append(var)
            kwargs_keys.append(var + "=" + var)
        argument_string = ", " + ", ".join(argument_names)
        kwargs_string = ", " + ", ".join(kwargs_keys)
%>
    #${'#'} ${function_parms['description']}
% if 'arguments' in function_parms:
% for arg_parms in function_parms['arguments']:
    # @param <${arg_parms['type']}> ${camel_case_to_underscore(arg_parms['name'])}: ${arg_parms['description']}
% endfor
% endif
    def ${camel_case_to_underscore(function_name)}(self${argument_string}):
        return self.client.send_command(self, '${function_name}'${kwargs_string})
% endfor
