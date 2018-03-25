import datetime
import os
import os.path
import shutil
import subprocess
import re
import sys
import m2r

def run(*args, **kwargs):
    error_code = subprocess.call(*args, **kwargs)
    if error_code != 0: # an error happened
        sys.exit(error_code)

doc_string_re = re.compile('(?:""")([\S\s]*?)(?:""")')
def get_doc_string(s):
    first = s.find('"""')
    if first == -1:
        return
    second = s.find('"""', first + 1)
    if second == -1:
        return

    return s[(first+3):second]

temp_path = "./temp"

if os.path.isdir(temp_path):
    shutil.rmtree(temp_path)
os.makedirs(temp_path)

if os.path.isdir("./output"):
    shutil.rmtree("./output")

def camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

game_names = [f for f in os.listdir("../games") if os.path.isdir(os.path.join("../games", f))]

for game_name in game_names:
    lower_game_name = game_name.lower()
    game_path = os.path.join("../games", game_name)
    only_files = [f for f in os.listdir(game_path) if os.path.isfile(os.path.join(game_path, f))]
    game_classes = []

    game_rst_path = os.path.join(temp_path, game_name)
    if os.path.isdir(game_rst_path):
        shutil.rmtree(game_rst_path)
    os.makedirs(game_rst_path)

    for name in only_files:
        name = os.path.splitext(name)[0]
        cc = camelcase(name)
        not_inherit = (name == "game" or name == "game_object")

        if name == "__init__":
            continue
        elif name == "ai":
            cc = "AI"

        if name == "game":
            # get the description
            with open('../games/{}/game.py'.format(lower_game_name), 'r') as f:
                contents = f.read()
            summary = [s.strip() for s in get_doc_string(contents).splitlines() if s.strip()][-1]

        if not not_inherit and name != "player" and name != "ai":
            game_classes.append(name)

        with open(game_rst_path + "/" + name + ".rst", "w+") as f:
            f.write("""{cc}
{cc_underline}

.. currentmodule:: games.{lower_game_name}.{name}

.. automodule:: games.{lower_game_name}.{name}
   :members:
   :inherited-members:
   :show-inheritance:
""".format(
        cc=cc,
        cc_underline='='*len(cc),
        lower_game_name=lower_game_name,
        name=name,
    ))


    with open(os.path.join(game_rst_path, "index.rst"), "w+") as f:
        f.truncate()
        f.write("""{upper_game_name}
{game_name_underline}

*{summary}*

Rules
^^^^^

The full game rules for {game_name} can be found on `GitHub <https://github.com/siggame/Cadre/blob/master/Games/{upper_game_name}/rules.md>`_.

Additional materials, such as the `story <https://github.com/siggame/Cadre/blob/master/Games/{upper_game_name}/story.md>`_ and `game template <https://github.com/siggame/Cadre/blob/master/Games/{upper_game_name}/creer.yaml>`_ can be found on `GitHub as well <https://github.com/siggame/Cadre/blob/master/Games/{upper_game_name}/>`_.

Classes
^^^^^^^

.. toctree::
   :maxdepth: 3
   :name: {upper_game_name}

   ai.rst
   game.rst
   game_object.rst
   player.rst
{game_classes}

Other Notes
^^^^^^^^^^^

Modifying non AI files

Each class fle inside of ``games/GAME_NAME/``, except for your ``ai.py`` should ideally not be modified. They are intended
to be read only constructs that hold the state of that object at the point in time you are reading its properties.
That being is said, if you really wish to add functionality, such as helper functions, ensure they do not directly modify game state information.

Game Logic

If you are attempting to figure out how the logic is executed for a game, that code is **not** here.
All `Cadre <https://github.com/siggame/Cadre>`_ game clients are dumb state tracking programs that facilitate IO between a game server and your AI in whatever language you choose.
If you wish to get the actual code for a game check in the `game server <https://github.com/siggame/Cerveau>`_.
Its directory structure is similar to most clients (such as this one).

""".format(
        upper_game_name=game_name[0].upper()+game_name[1:],
        game_name=game_name,
        game_name_underline="="*len(game_name),
        summary=summary,
        game_classes="\n".join(
            "   {}.rst".format(game_class) for game_class in sorted(game_classes)
        )
    ))

rst_readme = m2r.parse_from_file("../README.md").replace(".. code-block::", ".. code-block:: bash")

index = rst_readme.find("How to Run")

readme = rst_readme[:index] + """
Games
-----

.. toctree::
   :maxdepth: 1
   :name: mastertoc

{games}

""".format(games=("\n".join(["   {}/index.rst".format(g.lower()) for g in game_names]))
) + rst_readme[index:]

with open(os.path.join(temp_path, "index.rst"), "w+") as f:
    f.write(readme)

# create the conf file for sphinx
with open("_conf.py", "r") as f:
    conf = f.read()

conf = conf.replace("###YEAR###", str(datetime.datetime.now().year))

with open(os.path.join(temp_path, "conf.py"), "w+") as f:
    f.write(conf)

# shutil.copytree("../games/", os.path.join(temp_path, "games"))
run(["sphinx-build -b html ./temp ./output"], shell=True)

# cleanup files we made
shutil.rmtree(temp_path)

print("Python docs generated!")
