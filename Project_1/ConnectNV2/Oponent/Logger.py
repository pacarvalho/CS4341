#####################################################################
# Logs Events for Easier Debugging
#####################################################################
from datetime import datetime

class Logger:
	f = 0
	
	def __init__(self, gamePar):
		if gamePar.playerID == 1:
			self.f = open("log1.txt", 'w')
		else:
			self.f = open("log2.txt", 'w')

		self.f.write("Start Of Writing: " + str(datetime.utcnow()) + "\n\n")
		self.f.flush()
		

	def write(self, data):
		self.f.write(str(data) + "\n")
		self.f.flush()
	def close(self):
		self.f.close()