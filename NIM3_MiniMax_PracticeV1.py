#!/usr/bin/env python

# Create Board
board = [4,4]

# Create List of Pseudo Boards
def pseudoBoardCreator(board):
	pseudoBoardList = []

	for i in range(1,3):
		tempPseudoBoard = [board[0] - i, board[1]]
		if tempPseudoBoard[0] >= 0 and tempPseudoBoard[1] >= 0:
			pseudoBoardList.append(tempPseudoBoard)

		tempPseudoBoard = [board[0], board[1] - i]
		if tempPseudoBoard[0] >= 0 and tempPseudoBoard[1] >= 0:
			pseudoBoardList.append(tempPseudoBoard)

	return pseudoBoardList
		

# MiniMax Algorithm
def miniMax(pseudoBoard, player):
	#print pseudoBoardCreator(pseudoBoard)
	for tempBoard in pseudoBoardCreator(pseudoBoard):
		if tempBoard[0] == 0 and tempBoard[1] == 0:
			result = 1 if player == -1 else -1
			#print tempPlayer
			return result
		return miniMax(tempBoard, -1 if player == 1 else 1)

def firstRun():
	for tempBoard in pseudoBoardCreator(board):
		if miniMax(tempBoard, 1) == -1:
			return tempBoard

while 1:
	print board
	print "Your Move"
	board[0] = int(raw_input())
	board[1] = int(raw_input())
	print board
	board = firstRun()




