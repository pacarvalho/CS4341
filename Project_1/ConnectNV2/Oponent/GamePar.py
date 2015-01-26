#####################################################################
# Game Parameters Class
# Contains methods including:
#	Nothing at all...
#####################################################################

from math import log10
from ast import literal_eval
from copy import deepcopy
from LocationWeights import allWeights

class GamePar:
	playerID = 0
	playerTurn = 0
	numCols = 0
	numRows = 0
	nConnect = 0
	timeLimit = 0
	miniMaxAllotedTime = 0.0
	maxDepth = 0
	locationWeightMatrix = []

	# Constants for Calculating Heuristic
	# Oponent
	KLocation = 50
	KNeighbor = 1000
	KWin = 10000000
	KLose = 0
	neighborRadius = 0

	def __init__(self):
		pass

	def setUp(self, array):
		self.numRows = array[0]
		self.numCols = array[1]
		self.nConnect = array[2]
		self.playerTurn = array[3]
		self.timeLimit = array[4]
		self.miniMaxAllotedTime = self.timeLimit * 0.6
		self.maxDepth = 20 * self.timeLimit 

		self.neighborRadius = self.nConnect # TAKE NOTICE!!

		if self.numRows > 12 or self.numCols > 12 or self.nConnect > 7 \
			or self.numRows < 4 or self.numCols < 4 or self.nConnect < 3:
			self.locationWeightMatrix = [[0 for col in range(self.numCols)] \
			for row in range(self.numRows)]
		else:
			self.locationWeightMatrix = \
				allWeights[(self.numRows-4) + 9*(self.numCols-4) + 81*(self.nConnect-3)]


		