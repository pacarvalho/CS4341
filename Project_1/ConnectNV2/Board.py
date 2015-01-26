#####################################################################
# Board Class
# Contains methods including:
#	calcHeuristic()
#	makeMove()
#	generateMoves()
#	hasWin()
#####################################################################
from copy import deepcopy
from random import randint

class Board:
	# Class Variables
	gamePar = 0
	board = [] # Stores the actual board
	listOfCreation = []
	hasPopped1 = 0
	hasPopped2 = 0

	# Type of Moves
	POP = 0
	DROP = 1

	def __init__(self, gamePar):
		self.gamePar = gamePar
		self.board = [[0 for col in range(self.gamePar.numCols)] \
			for row in range(self.gamePar.numRows)]
		self.listOfCreation = []
		self.hasPopped1 = 0
		self.hasPopped2 = 0
		self.POP = 0
		self.DROP = 1


	def calcHeur(self):
		value = 0
		# 1) Take wins, cut loses
		# Take win
		temp = self.hasWin() # Player who won (1,2) or 0 for draw else -1
		
		if temp == self.gamePar.playerID: 
			value += self.gamePar.KWin # Victory is best move

		# Cut Lose
		if temp == (1 if self.gamePar.playerID is 2 else 2):
			value -= self.gamePar.KLose # Loosing is worst move

		# Notice that Draws are not accounted for... TODO
		
		# 2) Take into account location values on board
		value += self.gamePar.KLocation * self.calcLocationWeights()
		
		# 3) Take into account neighbors
		value += self.gamePar.KNeighbor * self.calculateNeighborWeights()

		return value
	
	# Assigns a utility value for the given board based on
	# The sum of the location weights of each piece on the board
	def calcLocationWeights(self):
		# For Safety: In case matrix is not imported correcly
		if self.gamePar.locationWeightMatrix == []:
			return 0

		locationValueOfBoard = 0

		otherPlayer = 1 if self.gamePar.playerID == 2 else 2

		for col in range(self.gamePar.numCols):
			for row in range(self.gamePar.numRows):
				if self.board[row][col] == self.gamePar.playerID:
					locationValueOfBoard += self.gamePar.locationWeightMatrix[row][col]
				elif self.board[row][col] == otherPlayer:
					locationValueOfBoard -= self.gamePar.locationWeightMatrix[row][col]

		return locationValueOfBoard

	def calculateNeighborWeights(self):
		player = self.gamePar.playerID

		value = [[0 for col in range(self.gamePar.numCols)] \
			for row in range(self.gamePar.numRows)]

		for row in range(self.gamePar.numRows):
			for col in range(self.gamePar.numCols):
				for k in range(1,self.gamePar.neighborRadius+1):
					try:
						if self.board[row+k][col+k]: 
							value[row][col] += 1 if self.board[row+k][col+k] is player else -1
					except:
						pass
					try:
						if self.board[row-k if row-k>-1 else 100][col+k]:
							value[row][col] += 1 if self.board[row-k if row-k>-1 else 100][col+k] is player else -1
					except:
						pass
					try:
						if self.board[row+k][col-k if col-k>-1 else 100]:
							value[row][col] += 1 if self.board[row+k][col-k if col-k>-1 else 100] is player else -1
					except:
						pass
					try:
						if self.board[row-k if row-k>-1 else 100][col-k if col-k>-1 else 100]:
							value[row][col] += 1 if self.board[row-k if row-k>-1 else 100][col-k if col-k>-1 else 100] is player else -1
					except:
						pass
					try:
						if self.board[row][col+k]:
							value[row][col] += 1 if self.board[row][col+k] is player else -1
					except:
						pass
					try:
						if self.board[row][col-k if col-k>-1 else 100]:
							value[row][col] += 1 if self.board[row][col-k if col-k>-1 else 100] is player else -1
					except:
						pass
					try:
						if self.board[row-k if row-k>-1 else 100][col]:
							value[row][col] += 1 if self.board[row-k if row-k>-1 else 100][col] is player else -1
					except:
						pass
					try:
						if self.board[row+k][col]:
							value[row][col] += 1 if self.board[row+k][col] is player else -1
					except:
						pass

		finalValue = 0
		for row in range (self.gamePar.numRows):
			for col in range(self.gamePar.numCols):
				finalValue += value[row][col]
		return finalValue
					
	# Performs the given move with the class
	def makeMove(self, player, col, move):
		if move is self.DROP:
			for row in range(self.gamePar.numRows-1, -1, -1):
				if self.board[row][col] is 0:
					self.board[row][col] = player
					self.listOfCreation.append([player, col, move])
					return self
			return None
		if move is self.POP:
			if self.board[self.gamePar.numRows-1][col] is player:
				for i in range(1, self.gamePar.numRows):
					self.board[-i][col] = self.board[-i-1][col]
				self.board[0][col] = 0
				self.listOfCreation.append([player, col, move])
				return self
			return None
		return None

	def unmakeMove(self):
		[player, col, move] = deepcopy(self.listOfCreation[-1])
		del(self.listOfCreation[-1])
		if move is self.DROP:
			for row in range(self.gamePar.numRows):
				if self.board[row][col] is not 0:
					self.board[row][col] = 0
					return self
			return None
		elif move is self.POP:
			for row in range(self.gamePar.numRows-1):
				self.board[row][col] = self.board[row+1][col]
			self.board[self.gamePar.numRows-1][col] = player
			return self
		return None

	def generateMoves(self):
		pseudoBoardList = []

		for col in range(self.gamePar.numCols):

			player = 1 if self.listOfCreation[-1][0] is 2 else 2
			
			temp = deepcopy(self.makeMove(player,col,self.DROP))
			
			if temp is not None:
				pseudoBoardList.append(temp)
				self.unmakeMove()
			
			if self.hasPopped1 is 0 and self.gamePar.playerID is 1:
				temp = deepcopy(self.makeMove(player,col,self.POP))
				if temp is not None:
					pseudoBoardList.append(temp)
					self.unmakeMove()
					self.hasPopped1 = 1

			elif self.hasPopped2 is 0 and self.gamePar.playerID is 2:
				temp = deepcopy(self.makeMove(player,col,self.POP))
				if temp is not None:
					pseudoBoardList.append(temp)
					self.unmakeMove()
					self.hasPopped2 = 1

		#pseudoBoardList = filter(lambda a: a is not None, pseudoBoardList)
		return pseudoBoardList

	def hasWin(self):
		numRows = self.gamePar.numRows
		numCols = self.gamePar.numCols
		nConnect = self.gamePar.nConnect

		consecutivePieceCount = 0
		for player in range(1,3):
			# Detect a Horizontal Win
			for row in range(numRows):
				consecutivePieceCount = 0
				for col in range(numCols):
					if self.board[row][col] == player:
						consecutivePieceCount += 1
						if consecutivePieceCount == nConnect:
							return player
					else: 
						consecutivePieceCount = 0
			# Detect a Vertical Win
			for col in range(numCols):
				consecutivePieceCount = 0
				for row in range(numRows):
					if self.board[row][col] == player:
						consecutivePieceCount += 1
						if consecutivePieceCount == nConnect:
							return player
					else: 
						consecutivePieceCount = 0
			
			largestDimension = numCols if numCols > numRows else numRows
			# Detect Principal Diagonal Win
			# Top Half
			for col in range(largestDimension-1, -1, -1):
				consecutivePieceCount = 0
				for row in range(largestDimension):
					if row > numRows-1: break
					if col > numCols-1: break
					if self.board[row][col] is player:
						consecutivePieceCount += 1
						if consecutivePieceCount is nConnect:
							return player
					else: 
						consecutivePieceCount = 0
					col += 1
			
			# Bottom Half
			for row in range(1,largestDimension):
				consecutivePieceCount = 0
				for col in range(largestDimension):
					if col > numCols-1: break
					if row > numRows-1: break
					
					if self.board[row][col] is player:
						consecutivePieceCount += 1
						if consecutivePieceCount is nConnect:
							return player
					else:
						consecutivePieceCount = 0
					row += 1

			# Detect Non-Principal Diagonal Win
			# Top Half
			for row in range(largestDimension):
				consecutivePieceCount = 0
				for col in range(largestDimension):
					if col > numCols-1: break
					if row > numRows-1: break
					
					if self.board[row][col] == player:
						consecutivePieceCount += 1
						if consecutivePieceCount is nConnect:
							return player
					else: 
						consecutivePieceCount = 0
					row -= 1
					if row < 0: break

			# Bottom Half
			for row in range(largestDimension):
				consecutivePieceCount = 0
				k = 1
				for col in range(1,largestDimension):
					col += row
					if col > numCols-1: break
					if row > numRows-1: break
					
					if self.board[numRows-k][col]:
						consecutivePieceCount += 1
						if consecutivePieceCount is nConnect:
							return player
					else:
						consecutivePieceCount = 0
					k = k+1 if k < numRows else k

			# Calculate if a Draw Took Place
			consecutivePieceCount = 0
			for col in range(numCols):
				if self.board[0][col]:
					consecutivePieceCount += 1
					if consecutivePieceCount == numCols:
						return 0 # TODO TAKE INTO ACCOUNT POP!!!


		return -1





