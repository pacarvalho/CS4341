#####################################################################
# Board Class
# Contains methods including:
#	calcHeuristic()
#	makeMove()
#	generateMoves()
#	hasWin()
#####################################################################
from copy import deepcopy

class Board:
	# Class Variables
	gamePar = 0
	board = [] # Stores the actual board
	hasPopped1 = 0
	hasPopped2 = 0
	listOfCreation = []

	# Type of Moves
	POP = 0
	DROP = 1

	def __init__(self, gamePar):
		self.gamePar = gamePar
		self.board = [[0 for col in range(self.gamePar.numCols)] \
			for row in range(self.gamePar.numRows)]


	def calcHeur(self):
		pass

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

	def unmakeMove(self, player, col, move):
		del(listOfCreation[-1])
		if move is self.DROP:
			for row in range(self.gamePar.numRows):
				if self.board[row][col] is not 0:
					self.board[row][col] = 0
					return self
			return None
		elif move is self.POP:
			if self.board[numRows-1][col] is player:
				for row in range(numRows-1):
					self.board[row][col] = self.board[row+1][col]
				self.board[self.gamePar.numRows-1][col] = player
				return self
			return None
		return None

	def generateMoves(self):
		pseudoBoardList = []

		for col in range(self.gamePar.numCols):
			temp = deepcopy(self.makeMove(player,col,self.DROP))
			if temp is not None:
				pseudoBoardList.append(temp)
				self.unmakeMove(player, col, self.DROP)
			
			if self.hasPopped1 is 0 and self.gamePar.playerID is 1:
				temp = deepcopy(self.makeMove(player,col,self.POP))
				if temp is not None:
					pseudoBoardList.append(temp)
					self.unmakeMove(player, col, self.POP)
			elif self.hasPopped2 is 0 and self.gamePar.playerID is 2:
				temp = deepcopy(self.makeMove(player,col,self.POP))
				if temp is not None:
					pseudoBoardList.append(temp)
					self.unmakeMove(player, col, self.POP)

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
					#print str(col) + " " + str(row)
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





