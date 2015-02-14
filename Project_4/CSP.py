# Contains all algorithms for solving the constraint 
# satisfaction problem.

from copy import deepcopy

class CSP:
	# Constructor
	def __init__(self):
		pass

	# BackTrack algorithm
	def backtrackSearch(self, world):
		return self.backtrack(world)

	# Recursive portion of algorithm
	def backtrack(self, w):
		world = deepcopy(w)
		if world.isComplete():
			print "Im Complete"
			return world

		var = world.selectUnassignedVariable()

		print "******************************"
		print var
		print world.orderDomainValues(var)
		print w.assignment
		for value in world.orderDomainValues(var):
			world.addAssignment(var, value)
			print w.assignment
			if world.isValid():
				print "Is valid"
				result = self.backtrack(world)
				if result.isValid():
					print "Result Valid"
					return result
			world.removeAssignment(var)

		print "Failed!"
		return world.failFlag()