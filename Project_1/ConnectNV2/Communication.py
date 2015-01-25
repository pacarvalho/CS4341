#####################################################################
# Communication Class
# Deals with the Referee
#####################################################################

import sys
import io

class Communication:

	def __init__(self):
		pass

	def read(self):
		return sys.stdin.readline().split()
		#return raw_input().split()

	def writeMove(self, col, move):
		self.write(str(col) + " " + str(move))

	def write(self, data):
		sys.stdout.write(str(data) + "\n")
		sys.stdout.flush()
