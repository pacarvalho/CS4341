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

	assignment = {} # Saves the current assignment!!!

	# Constructor
	def __init__(self):
		pass

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
		return self.checkLimits() and self.checkUnaryI() and \
			self.checkUnaryE() and self.checkBinE() and \
			self.checkBinNE() and self.checkBinS()

	# Checks if the limits have been obeyed
	def checkLimits(self):
		for value in self.assignment:
			length = len(self.assignment[value])
			if length > self.limits[1] or length < self.limits[0]:
				return False
		return True

	# Checks if Unary Inclusion Constraint is not violated
	def checkUnaryI(self):
		pass
		

	# Checks if Unary Exclusion Constraint is not violated
	def checkUnaryE(self):
		for value in self.assignment:
			for var in self.unaryE:
				if value in self.unaryE[var]:
					return False
		return True

	# Checks if the binary exclusion has been violated
	def checkBinE(self):
		return True

	# Checks if the binary inequality has been violated
	def checkBinNE(self):
		for value in self.assignment:
			for var in self.assignment[value]:
				if var in self.binNE.keys():
					if self.binNE[var] in self.assignment[value].index():
						return False
		return True

	# Checks if the binary mutua exclusivity has been violated
	def checkBinS(self):
		pass



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


