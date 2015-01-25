#####################################################################
# Game Class
# Contains the Following Methods:
#	Minimax with A-B Prunning
#	SetUp
#####################################################################

class Game:
	board = 0

	def __init__(self, gamePar):
		self.board = Board(gamePar)

	def miniMax(self):
		v = maxValue()

	def maxValue(self, state, a, b):
		pass

	def minValue(self, state, a, b):
		pass