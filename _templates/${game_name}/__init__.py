from ${game_name}.ai import AI
from ${game_name}.game import Game
% for game_obj_key, game_obj in game_objs.items():
from ${game_name}.${uncapitalize(game_obj_key)} import ${game_obj_key}
% endfor

${merge("# ", "init", "# if you need to initialize this module with custom logic do so here")}
