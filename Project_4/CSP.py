# Contains all algorithms for solving the constraint 
# satisfaction problem.

from copy import deepcopy

class CSP:
	# Constructor
	def __init__():
		pass

	# BackTrack algorithm
	def backtrackSearch(self, world):
		return backtrack(world)

	# Recursive portion of algorithm
	def backtrack(w):
		world = deepcopy(w)
		if world.isComplete():
			return world

		var = world.selectUnassignedVariable()

		for value in world.orderDomainValues(var):
			world.addAssignment(var, value)
			if world.isValid():
				result = backtrack(world)
				if result.isValid()
					return result
			world.removeAssignment(var,value)

		return world.flagFail()