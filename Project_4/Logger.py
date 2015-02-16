# Creates the log file based on a passed instance of the world.

class Logger:
	# Class Variables
	f = 0

	# Constructor
	def __init__(self, logFileName):
		self.f = open(logFileName, 'w')

	# Log to file
	def log(self, world, iteration = 0):
		self.f.write("****************** - Iteration: " + str(iteration) +'\n')
		self.f.write('Assignment: ' + str(world.assignment) + '\n')

	# Final Log
	def finalLog(self, world):
		self.f.write("********************************\n")
		self.f.write("********* FINAL RESULT *********\n")
		self.f.write("********************************\n")

