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

	fFlag = False # Fail Flag!

	###### WEIGHTS!!
	binWeightE = 5 # Weight for a Binary Constraint when Counting
	binWeightNE = 5 # Weight for a Binary Constraint when Counting
	binWeightS = 5 # Weight for a Binary Constraint when Counting

	# Constructor
	def __init__(self, capacity):
		self.capacity = capacity

	#######################################################
	################### Adder Methods #####################
	#######################################################

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
		self.binE[var] = value

	def addBinNE(self, var, value):
		self.binNE[var] = value

	def addBinS(self, var1, var2, value1, value2):
		self.binS[var1] = [var2,value1,value2]

	def addAssignment(self, var, value):
		self.assignment[var] = value

	#######################################################
	################### Other Methods #####################
	#######################################################

	# Removes a previously made assignment
	def removeAssignment(self, var):
		del self.assignment[var]

	# Sets fail flag and return world
	def failFlag(self):
		self.fFlag = True
		return self

	#######################################################
	################# Validation Methods ##################
	#######################################################

	###### Higher Level Checking
	# Returns if the world is valid. Fulffils all constraints
	def isValid(self):
		
		print "All Checks:"
		print "L Bot: " + str(self.checkBottomLimit())
		print "L Top: " + str(self.checkTopLimit())
		print "UnaryI: " + str(self.checkUnaryI())
		print "UnaryE: " + str(self.checkUnaryE())
		print "BinE: " + str(self.checkBinE())
		print "BinNE: " + str(self.checkBinNE())
		print "BinS: " + str(self.checkBinS())
		print "Max: " + str(self.checkMaxCapacity())
		print "Min: " + str(self.checkMinCapacity())
		print "Flag: " + str(self.fFlag)

		return self.checkTopLimit() and self.checkUnaryI() and \
			self.checkUnaryE() and self.checkBinE() and \
			self.checkBinNE() and self.checkBinS() and \
			self.checkMaxCapacity() and not self.fFlag

	def isComplete(self):
		return self.isValid() and self.checkMinCapacity()

	# Calculates the weight of var current in value
	def calcUsedCapacity(self):
		cap = {}

		for var in self.assignment:
			if self.assignment[var] in cap:
				cap[self.assignment[var]] += self.var[var]
			else:
				cap[self.assignment[var]] = self.var[var]

		return cap

	###### Individual Checking
	# Check that the bags have the minimum filling required
	def checkMinCapacity(self):
		if not self.assignment.keys():
			return False

		cap = self.calcUsedCapacity()

		for value in cap:
			if cap[value] < self.capacity*self.value[value]/100:
				return False
		return True

	# Checks to ensure that the maximum capacity has not been
	# exceeded
	def checkMaxCapacity(self):
		if not self.assignment.keys():
			return True

		cap = self.calcUsedCapacity()

		for value in cap:
			if cap[value] > self.value[value]:
				return False
		return True

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

		if len(check.values()) is not len(self.value.keys()):
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

	# Checks if the binary equality has been violated
	def checkBinE(self):
		for var in self.binE:
			if var in self.assignment.keys():
				if self.binE[var] in self.assignment.keys():
					if self.assignment[var] is not \
							self.assignment[self.binE[var]]:
						return False
		return True


	# Checks if the binary inequality has been violated
	def checkBinNE(self):
		for var in self.binNE:
			if var in self.assignment.keys():
				if self.binNE[var] in self.assignment.keys():
					if self.assignment[var] is \
							self.assignment[self.binNE[var]]:
						return False
		return True

	# Checks if the binary mutua exclusivity has been violated
	def checkBinS(self):
		for var in self.binS:
			if var in self.assignment.keys():
				if self.binS[var][0] in self.assignment.keys():
					if (self.assignment[var] is self.binS[var][1] and \
							self.assignment[self.binS[var][0]] is self.binS[var][2]) or \
							(self.assignment[var] is self.binS[var][2] and \
							self.assignment[self.binS[var][0]] is self.binS[var][1]):
						return False 
		return True

	#######################################################
	############# Algorithm Related Methods ###############
	#######################################################

	# Returns a list with the unassigned variables
	def findUnassignedVar(self):
		unassigned = []
		for var in self.var:
			if var not in self.assignment.keys():
				unassigned += var
		return unassigned

	# Returns a list with the unfilled bag
	def findUnassignedValue(self):
		if not self.assignment.keys(): # If nothing is assigned
			return self.value.keys()

		unassigned = []

		lightestWeight = min(self.var.values())

		cap = self.calcUsedCapacity()

		for value in self.value:
			if value in cap.keys():
				if cap[value] < self.value[value] - lightestWeight:
					unassigned += [value]
		return unassigned


	# Count Constraints per Variables
	# Returns dictionary of var and constraints
	def countConstraints(self):
		count = {}
		for var in self.var:
			tempCount = 0
			if var in self.unaryI.keys():
				tempCount -= len(self.unaryI[var])
			if var in self.unaryE.keys():
				tempCount += len(self.unaryE[var])
			if var in self.binE.keys() or var in self.binE.values():
				tempCount += self.binWeightE
			if var in self.binNE.keys() or var in self.binNE.values():
				tempCount += self.binWeightNE
			if var in self.binS.keys() or var in [a[0] for a in self.binS.values()]:
				tempCount += self.binWeightS 
			count[var] = tempCount
		return count

	# Selects the next variables to expand
	def selectUnassignedVariable(self):
		tempMaxVar = 0
		tempMaxCount = -1

		unassigned = self.findUnassignedVar()
		constraints = self.countConstraints()

		for var in unassigned:
			if constraints[var] >= tempMaxCount:
				tempMaxCount = constraints[var]
				tempMaxVar = var

		return tempMaxVar # Return Variables with Most Constraints

	# Returns the next value to use
	def orderDomainValues(self, var):
		unassigned = self.findUnassignedValue()

		return unassigned







