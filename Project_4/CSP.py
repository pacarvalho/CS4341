# Contains all algorithms for solving the constraint 
# satisfaction problem.

from copy import deepcopy

class CSP:
	# Declare Variables
	counter = 0 # Keeps track of number of calls
	logger = 0

	# Constructor
	def __init__(self, logger):
		self.logger = logger


	# BackTrack algorithm
	def backtrackSearch(self, world):
		return self.backtrack(world)

	# Recursive portion of algorithm
	def backtrack(self, w):
		world = deepcopy(w)

		if world.isComplete():
			return world

		var = world.selectUnassignedVariable()

		if var not in world.var:
			return world

		for value in world.orderDomainValues():
			self.counter += 1 # Count!

			# Log state to log file
			self.logger.log(world, self.counter)

			world.addAssignment(var, value)
			inferences = w.inference(var, value) # Forward Checking

			for iVar,iValue in inferences:
				world.addAssignment(iVar, iValue)
			if world.isValid():
				result = self.backtrack(world)
				if result.isValid():
					return result

			world.removeAssignment(var)
			for iVar,iValue in inferences:
				world.removeAssignment(iVar)
			world.resetFailFlag() # Rests the fail flag

		return world.failFlag()



