#####################################################################
# Communication Class
# Deals with the Referee
#####################################################################

from sys import stdin
from sys import stdout

class Communication:
	def __init__:
		pass

	def read(self):
		return stdin.readline().split()

	def writeMove(self, col, move):
		self.write(str(col) + " " + str(move))

	def write(self, data):
		stdout.write(str(data) + "\n")
		stdout.flush()