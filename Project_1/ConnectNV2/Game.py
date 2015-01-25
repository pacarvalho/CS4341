#####################################################################
# Game Class
# Contains the Following Methods:
#	Minimax with A-B Prunning
#	SetUp
#####################################################################
from timeit import default_timer
from copy import deepcopy

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
		self.depth = 0
		self.startTime = default_timer() # Save Start Time
		maxV = -self.inf
		for son in self.board.generateMoves():
			v = self.minValue(son, -self.inf, self.inf, 1)
			if v > maxV:
				maxV = v
				favoriteSon = deepcopy(son)
		return favoriteSon.listOfCreation[-1]

	def maxValue(self, state, a, b, depth):
		if self.isTerminal(state, depth):
			return state.calcHeur()
		v = -self.inf
		for son in state.generateMoves():
			v = max(v, self.minValue(son, a, b, depth+1))
			if v >= b: return v
			a = max(a, v)
		return v

	def minValue(self, state, a, b, depth):
		if self.isTerminal(state, depth):
			return state.calcHeur()
		v = self.inf
		for son in state.generateMoves():
			v = min(v, self.maxValue(son, a, b, depth+1))
			if v <= a: return v
			b = min(b, v)
		return v

	def isTerminal(self, state, depth):
		if default_timer() - self.startTime > self.gamePar.miniMaxAllotedTime:
			return True
		if depth > self.maxDepth:
			return True
		if state.hasWin() is not - 1:
			return True
		return False




		