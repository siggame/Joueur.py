class AI:
	def __init__(self, game, socket):
		self.socket = socket
		self.game = game

	def start(self, data):
		self.playerID = data["playerID"]

	def makeCommand(self):
		print("I can make a command!")

	def ignoring(self):
		pass

	def close(self):
		pass

