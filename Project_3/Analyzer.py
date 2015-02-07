

class Analyzer:

	board = []

	def __init__(self, board):
		self.board = board

	def analyze(self):
		result = []
		
		result.append(self.hasConnect(4, 1)) # Player 1 won?
		result.append(self.hasConnect(4, 2)) # Player 2 won?
		result = result + self.calcRows() # Row Distribution
		result = result + self.calcCols() # Col Distribution
		result = result + self.calculateNeighborWeights() # Neighbor Weight

		for nConnect in range(2,4):
			result.append(self.hasConnect(nConnect, 1)) # Connect 2, 3? Player 1
			result.append(self.hasConnect(nConnect, 2)) # Connect 2, 3? Player 2

		return result

	def calcRows(self):
		results = []
		for player in range(1,3):
			for row in range(6):
				count = 0
				for col in range(7):
					if self.board[row][col] == player:
						count += 1
				results.append(count)
		return results

	def calcCols(self):
		results = []
		for player in range(1,3):
			for col in range(7):
				count = 0
				for row in range(6):
					if self.board[row][col] == player:
						count += 1
				results.append(count)
		return results

	def hasConnect(self, nConnect, player):
		numRows = 6
		numCols = 7

		consecutivePieceCount = 0
		
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

	def calculateNeighborWeights(self):
		results  = []
		player = 1

		value = [[0 for col in range(7)] \
			for row in range(6)]

		for neighborRadius in range(1,5):
			for row in range(6):
				for col in range(7):
					for k in range(1,neighborRadius+1):
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
			for row in range (6):
				for col in range(7):
					finalValue += value[row][col]

			results.append(finalValue)
		
		return results



