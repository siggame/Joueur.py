# @class BaseGame: the basics of any game, basically state management. Do not modify
class BaseGame:
	def __init__(self):
		self.state = {}

	def updateState(self, newState):
		self.state = newState

	def setAI(self, ai):
		self.ai = ai
