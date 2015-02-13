# Takes in the raw representation of the constraints, variables
# etc and creates a more manageable and independent version
# of the world. Contains methods for detecting consistencies
# etc.

class World:
	var = {} # Dictionary of Variable names and value ITEMS!!!
	value = {} # Dictionary of values BAGS!!!!
	limits = [] # Limits Array
	unaryI = {} # Unary Inclusive Constraints
	unaryE = {} # Unary Exclusive Constraints
	binE = {} # Binary Equals Constraints
	binNE = {} # Binary NOT Equals Constraints
	binS = {} # Binary Simultaneuous NOT
	capacity = 0 # Minimum filling of the bag

	assignment = {} # Assignment Dictionary ITEM IS KEY

	# Constructor
	def __init__(self, capacity):
		self.capacity = capacity

	##### Adder Methods ####
	def addVar(self, var, x):
		self.var[var] = int(x)

	def addValue(self, value, x):
		self.value[value] = int(x)

	def addLimits(self, low, high):
		self.limits = [low,high]

	def addUnaryI(self, var, values):
		self.unaryI[var] = values

	def addUnaryE(self, var, values):
		self.unaryE[var] = values

	def addBinE(self, var, value):
		self.binE[var] = values;

	def addBinNE(self, var, value):
		self.binNE[var] = values;

	def addBinS(self, var1, var2, value1, value2):
		self.binS[[var1,var2]] = [value1,value2];

	##### Validation Methods #####
	# Returns if the world is valid. Fulffils all constraints
	def isValid(self):
		return self.checkTopLimit() and self.checkUnaryI() and \
			self.checkUnaryE() and self.checkBinE() and \
			self.checkBinNE() and self.checkBinS()

	# Check that the bags have the minimum filling required
	def checkCapacity(self):
		pass

	# Checks if the limits have been obeyed
	def checkTopLimit(self):
		check = {}

		if not self.assignment.keys(): # If empty
			return True

		for var in self.assignment:
			if self.assignment[var] in check:
				check[self.assignment[var]] += 1
			else:
				check[self.assignment[var]] = 1

		if max(check.values()) > self.limits[1]:
			return False
		return True

	# Checks if the bottom limit has been obeyed
	def checkBottomLimit(self):
		check = {}

		if not self.assignment.keys(): # If empty
			return False

		for var in self.assignment:
			if self.assignment[var] in check:
				check[self.assignment[var]] += 1
			else:
				check[self.assignment[var]] = 1

		if len(check.values()) is not len(self.values.keys()):
			return False # A bag has remained unassigned!

		if min(check.values()) < self.limits[0]:
			return False
		return True

	# Checks if Unary Inclusion Constraint is not violated
	def checkUnaryI(self):
		for var in self.unaryI:
			if var in self.assignment.keys():
				if self.assignment[var] not in self.unaryI[var]:
					return False
		return True

	# Checks if Unary Exclusion Constraint is not violated
	def checkUnaryE(self):
		for var in self.unaryE:
			if var in self.assignment.keys():
				if self.assignment[var] in self.unaryE[var]:
					return False
		return True

	# Checks if the binary exclusion has been violated
	def checkBinE(self):
		return True

	# Checks if the binary inequality has been violated
	def checkBinNE(self):
		return True

	# Checks if the binary mutua exclusivity has been violated
	def checkBinS(self):
		return True

	# Logs all variables for debugging
	def logAll(self):
		print self.var
		print self.value
		print self.limits
		print self.unaryI
		print self.unaryE
		print self.binE
		print self.binNE
		print self.binS


