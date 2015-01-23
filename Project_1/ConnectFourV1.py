#!/usr/bin/env python

import sys
from time import sleep
from datetime import datetime
from copy import deepcopy
from timeit import default_timer
import random

# Define Constants DO NOT MODIFY
DROP = 1
POP = 0
MAX_DEPTH = 5

# Important Global Variables
numCols = 0
numRows = 0
nConnect = 0
playerTurn = 1
playerID = 0
timeLimit = 0
start_time = 0

# Create the Board
globalBoard = 0

# Sets up the Game
def setUp():
	# Recall Globals
	global globalBoard
	global numRows
	global numCols
	global nConnect
	global playerTurn
	global playerID
	global timeLimit
	global miniMaxAllotedTime
	# Print Name
	sys.stdout.write("The Winners\n")
	sys.stdout.flush()
	# Save Game Parameters Given by Referee
	gameSetUp = sys.stdin.readline().split()
	gameSetUp = [int(temp) for temp in gameSetUp]
	numRows = gameSetUp[0]
	numCols = gameSetUp[1]
	nConnect = gameSetUp[2]
	playerID = gameSetUp[3]
	timeLimit = gameSetUp[4]
	miniMaxAllotedTime = timeLimit * 0.9
	# Create Global Board
	globalBoard = [[0 for col in range(numCols)] \
		for row in range(numRows)]


# Updates the Board Based on Given Move
# Returns a Board in which the Given Move is Performed
def makeMove(player, col, type, tempTempBoard):
	tempBoard = deepcopy(tempTempBoard)
	if type is DROP:
		for row in range(numRows):
			if tempBoard[row][col] is not 0:
				if row is 0: # Not a Valid Move
					return None
				tempBoard[row-1][col] = player
				return tempBoard
			elif row is (numRows - 1):
				tempBoard[row][col] = player
				return tempBoard

	if type is POP:
		if tempBoard[numRows-1][col] is playerID:
			for i in range(1, numRows):
				tempBoard[-i][col] = tempBoard[-i-1][col]
			tempBoard[0][col] = 0
			return tempBoard
		return None
	return None

# Determines the Next Move Based on Current Board
def calculateMove():
	#DO SOMETHING HERE
	a = 3

# Creates a the exploration list
# Replaces each board with a list of boards upon expansion
def explorer(player, boardList, depth):
	currentBoard = deepcopy(boardList)

	#print "Depth: " + str(depth)

	if currentBoard == None:
		#print "IM HERE"
		return None

	#print "Time Elapsed: " + str(default_timer() - start_time)
	
	if (default_timer() - start_time) > miniMaxAllotedTime or \
			depth >= MAX_DEPTH:
		for i in range(numCols*2):
			a = [calculateHeuristic(currentBoard[i]) \
					 for i in range(numCols*2)]
			#print "Heurestic: " + str(a)
			return max(a) if player == 1 else \
						min(a)
	if depth < MAX_DEPTH:
		#print "Depth If"
		temp = [explorer(2 if player==1 else 1, \
			pseudoBoardGenerator(player, i), depth+1) for i in currentBoard]

		temp = (max(temp) if player == 1 else \
					min(filter(lambda a: a is not None, temp))) if \
					isinstance(temp, list) and depth>1 else temp

		return temp



# Return a list of Pseudo Board
# Pseudo board being all possible moves by the given player
# Given the current board
def pseudoBoardGenerator(player, startingBoard):
	pseudoBoardList = []

	if not isinstance(startingBoard, (list)):
		return None

	for col in range(numCols):
		pseudoBoardList.append(makeMove(player,col,DROP,startingBoard))
		pseudoBoardList.append(makeMove(player,col,POP,startingBoard))

	#pseudoBoardList = filter(lambda a: a is not None, pseudoBoardList)

	return pseudoBoardList


def calculateHeuristic(pseudoBoard):
	#DO SOMETHING HERE
	random.seed(default_timer())
	return random.randint(-100,100)

def calculateMiniMax(pseudoBoardList):
	#DO SOMETHING HERE
	a = 3

def pieceLocationWeightCalculator():
	a = 3

# Returns the 1 or 2 if either player won, 0 if there is no win
# or -1 if the game board is a draw
def hasWon(pseudoBoard):
	if pseudoBoard == None:
		return None

	consecutivePieceCount = 0
	for player in range(1,3):
		# Detect a Horizontal Win
		for row in range(numRows):
			consecutivePieceCount = 0
			for col in range(numCols):
				if pseudoBoard[row][col] == player:
					consecutivePieceCount += 1
					if consecutivePieceCount == nConnect:
						return player
				else: 
					consecutivePieceCount = 0
		# Detect a Vertical Win
		for col in range(numCols):
			consecutivePieceCount = 0
			for row in range(numRows):
				if pseudoBoard[row][col] == player:
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
				if pseudoBoard[row][col] is player:
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
				
				if pseudoBoard[row][col] is player:
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
				
				if pseudoBoard[row][col] == player:
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
				
				if pseudoBoard[numRows-k][col]:
					consecutivePieceCount += 1
					if consecutivePieceCount is nConnect:
						return player
				else:
					consecutivePieceCount = 0
				k = k+1 if k < numRows else k

		# Calculate if a Draw Took Place
		consecutivePieceCount = 0
		for col in range(numCols):
			if pseudoBoard[0][col]:
				consecutivePieceCount += 1
				if consecutivePieceCount == numCols:
					return 0 # TODO TAKE INTO ACCOUNT POP!!!


	return -1

#############################################################
################### Main Program ############################
#############################################################
setUp()
p = 1

f = open("locationWeights.kpa", 'w')
f.write("Start Of Writing: " + str(datetime.utcnow()) + "\n\n")

for z in range(3,8):
	nConnect = z
	for k in range(4,13):
		for j in range(4,13):
			numCols = k
			numRows = j

			result = [[0 for col in range(numCols)] \
					for row in range(numRows)]
			globalBoard = [[0 for col in range(numCols)] \
						for row in range(numRows)]

			i = 0

			startTime = default_timer()

			while i < 100000:
				i += 1
				
				globalBoard = makeMove(p, random.randint(0,numCols-1), 1, globalBoard) 
				
				p = 2 if p is 1 else 1
				winner = hasWon(globalBoard)
				#print globalBoard
				if winner is not -1:
					for col in range(numCols):
						for row in range(numRows):
							if winner is 1:
								result[row][col] += globalBoard[row][col] if globalBoard[row][col] is not 2 else -1  
							#if winner is 2:
							#	result[row][col] -= globalBoard[row][col] if globalBoard[row][col] is not 2 else -1 
					globalBoard = [[0 for col in range(numCols)] \
						for row in range(numRows)]

			compTime = default_timer() - startTime
			f.write("Col: " + str(k) + ", Row: " + str(j) + ", nConnect: " \
				+ str(nConnect) + " CompTime: " + str(compTime) + "\n")
			f.write(str(result) + "\n\n")
			print "RESULT: numCols: " + str(numCols) + " numRows: " \
				+ str(numRows) + " nConnect: " + str(nConnect) + " CompTime: " + str(compTime)
			print result 
f.close()

	#print sys.stdin.readline()
	#sys.stdout.write("1 1\n")
	#sys.stdout.flush()
	#sleep(0.5)
	


