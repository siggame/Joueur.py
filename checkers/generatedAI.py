# NOTE: This file should never be modified after being spit out of the new CodeGen
from baseAI import BaseAI
idKey = "#"

# @class BaseCheckersAI: the base interface to command the Checkers game.
class GeneratedAI(BaseAI):
	def move(self, checker, x, y):
		return self.sendCommand("move", idKey + str(checker.id), x, y)

	def done(self):
		return self.sendCommand("done")
