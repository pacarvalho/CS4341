# Creates the output file

from datetime import datetime

class Printer:
	f = 0

	# Constructor
	def __init__(self, filename):
		self.f = open(filename, 'w')

	# Write Output to file
	def write(self, w):
		cap = w.calcUsedCapacity()

		# Timestamp
		self.f.write(str(datetime.now()) + '\n\n')

		for value in w.value:
			if value in cap.keys(): 
				self.f.write(value + ' ') # Print Assignment (Line 1)
				count = 0
				for var in w.assignment:
					if w.assignment[var] == value:
						self.f.write(var + ' ')
						count += 1
				self.f.write('\n')
				# Number of Items (Line 2)
				self.f.write("Number of Items: " + str(count) + '\n') 
				# Total Weight (Line 3)
				self.f.write("Total Weight: " + str(cap[value]) + '/' + 
					str(w.value[value]) + '\n')
				# Wasted Capacity (Line 4)
				self.f.write("Waster Capacity: " + str(w.value[value]-cap[value]) + '\n\n')



