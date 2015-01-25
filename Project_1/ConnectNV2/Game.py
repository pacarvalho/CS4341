#####################################################################
# Game Class
# Contains the Following Methods:
#	Minimax with A-B Prunning
#	SetUp
#####################################################################
from timeit import default_timer

class Game:
	# Define Constants
	inf = float("inf")

	# Declare Variables
	startTime = 0
	board = 0
	maxDepth  = 0
	gamePar = 0

	def __init__(self, gamePar, board):
		self.board = board
		self.gamePar = gamePar
		self.maxDepth = gamePar.maxDepth

	def miniMax(self):
		startTime = default_timer() # Save Start Time
		listOfSonsAndValues = []
		maxV = -inf
		for son in board.generateMoves():
			v = minValue(son, -inf, inf)
			if v > maxV:
				maxV = v
				favoriteSon = son
		return favoriteSon.listOfCreation[-1]

	def maxValue(self, state, a, b):
		if self.isTerminal(state):
			return state.calcHeur()
		v = -inf
		else:
			for son in state.generateMoves():
				v = max(v, minValue(son, a, b))
				if v >= b: return v
				a = max(a, v)
			return v

	def minValue(self, state, a, b):
		if self.isTerminal(state):
			return state.calcHeur()
		v = inf
		else:
			for son in state.generateMoves():
				v = min(v, minValue(son, a, b))
				if v <= a: return v
				b = min(b, v)
			return v

	def isTerminal(self, state):
		if default_timer() - startTime > self.gamePar.miniMaxAllotedTime:
			return True
		if len(state.listOfCreation) - len(board.listOfCreation) > self.maxDepth:
			return True
		if state.hasWin() is not - 1:
			return True
		return False




		