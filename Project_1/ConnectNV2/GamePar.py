#####################################################################
# Game Parameters Class
# Contains methods including:
#	Nothing at all...
#####################################################################

class GamePar:
	playerID = 0
	playerTurn = 0
	numCols = 0
	numRows = 0
	nConnect = 0
	timeLimit = 0
	miniMaxAllotedTime = 0.0

	def __init__(self):
		pass

	def setUp(self, array):
		self.numRows = array[0]
		self.numCols = array[1]
		self.nConnect = array[2]
		self.playerTurn = array[3]
		self.timeLimit = array[4]
		self.miniMaxAllotedTime = self.timeLimit * 0.7