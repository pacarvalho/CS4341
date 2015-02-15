#!/usr/bin/env python
# CS4341 Project 4 
# Main file
# By Paulo Carvalho and Alex Bennett

from Parser import Parser
from World import World
from CSP import CSP
from Printer import Printer
import sys

# Get User Input from Terminal
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
minCapacityConstraint = int(sys.argv[3])

# Create Classes
world = World(minCapacityConstraint)
csp = CSP()

# Read the input file
parser = Parser(inputFileName, world)
parser.read() 

# PERFORM CSP CALCULATION!!!
result = csp.backtrackSearch(world)

# Print Fail or Pass
if not result.isComplete():
	print "Assignment not possible..."
else:
	print "Finished Assignment!"
print "Assigned: " + str(result.assignment)
print "With unused capacity of: " + str(result.calcTotalUnusedCapacity())
print "In " + str(csp.counter) + " iterations."

# Print Final Result
printer = Printer(outputFileName)
printer.write(result)


