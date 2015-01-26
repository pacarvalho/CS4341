#!/usr/bin/env python
#####################################################################
# Main Script for Connect N Game
#####################################################################

# Import Our Classes
from Board import Board
from Communication import Communication
from Game import Game
from GamePar import GamePar
from Logger import Logger

#####################################################################
#####################################################################
#######################    MAIN LOOP   ##############################
#####################################################################
#####################################################################

# Instantiate Objects
comm = Communication()
gamePar = GamePar()
board = []
game = []
logger = []

# Declare Constants
playerName = "TheWinner2"

# Report Our Name
comm.write(playerName)

# Keeps Track of the Round
roundNum = 0

while 1:
	read = comm.read()

	# Set Up Message
	if len(read) is 5:
		logger.write("5: " + str(read))
		read = [int(temp) for temp in read]
		gamePar.setUp(read)
		logger.write("PlayerID: " + str(gamePar.playerID))
		board = Board(gamePar)
		game = Game(gamePar, board)

		# If we are player one, make first move (play at center)
		if gamePar.playerID == gamePar.playerTurn:
			#logger.write("First Move Start")
			comm.writeMove(gamePar.numCols/2, 1)
			#logger.write("Move Sent")
			board.makeMove(gamePar.playerID, gamePar.numCols/2, 1)
			logger.write("First Move End")

	# Our Turn, Make a move
	elif len(read) is 2:
		#logger.write("ListOfCreation: " + str(board.listOfCreation))
		logger.write("Board Before All: " + str(board.board))

		# Save Other Player's move
		read = [int(temp) for temp in read]
		logger.write("2: " + str(read))
		board.makeMove(1 if gamePar.playerID is 2 else 2, read[0], read[1])
		logger.write("Board After Other: " + str(board.board))

		# Perform Our Move
		tempMove = game.miniMax()
		#logger.write("My Move: " + str(tempMove))
		comm.writeMove(tempMove[1], tempMove[2])
		logger.write("Reported Move: " + str(tempMove[1]))
		board.makeMove(gamePar.playerID, tempMove[1], tempMove[2])
		logger.write("Board After Me: " + str(board.board))
		logger.write("***********************************")
		roundNum += 1
		logger.write("Round: " + str(roundNum))
		logger.write("CalcHeur: " + str(board.calcHeur()))
		logger.write("CalcLoc: " + str(board.calcLocationWeights()))
		logger.write("CalcNeigh: " + str(board.calculateNeighborWeights()))
		logger.write("***********************************")


	# Determine Which Player We Are
	elif len(read) is 4:
		if read[1] == playerName: gamePar.playerID = 1
		else: gamePar.playerID = 2

		# Set up logger and do first logging
		logger = Logger(gamePar)
		logger.write("4: " + str(read))

	# Game Ended
	elif len(read) is 1:
		logger.write("1: " + str(gamePar.playerID) + " " + str(read))
		if read[0] is "win":
			comm.write("Muahaha! I Won!")
		elif read[0] is "lose":
			comm.write("I Shall Have My Revange!")
		elif read[0] is "draw":
			comm.write(":(")
		logger.close()
		comm.close()
		break



