# NOTE: this is where you code your game logic!
from checkers.generatedAI import GeneratedAI

# @class BaseAI: the basic AI functions that are the same between games
class AI(GeneratedAI):
	# this is called once the game starts and your ai knows its playerID and such
	def init(self):
		pass


	# this is called every time the server talls you that you can send a command. Once you send a command any you send will be disregarded, so return upon doing so
	def run(self):
		pass


	# this is called when the server is no longer taking game commands from you, normally when you turn ends
	def ignoring(self):
		pass


	# this is called when the game closes (ends), you can clean up your data and dump files here if need be
	def close(self):
		pass
