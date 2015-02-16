#!/usr/bin/env python
# CS4341 Project 4 
# Main file
# By Paulo Carvalho and Alex Bennett

from Parser import Parser
from World import World
from CSP import CSP
from Printer import Printer
import sys
from Logger import Logger

# Get User Input from Terminal
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
logFileName = sys.argv[3]
minCapacityConstraint = int(sys.argv[4])

# Create Classes
logger = Logger(logFileName)
world = World(minCapacityConstraint)
csp = CSP(logger)

# Read the input file
parser = Parser(inputFileName, world)
parser.read() 

# PERFORM CSP CALCULATION!!!
result = csp.backtrackSearch(world)

# Print Fail or Pass
print "******************************"
if not result.isComplete():
	print "Assignment not possible..."
else:
	print "Finished Assignment!"
print "Assigned: " + str(result.assignment)
print "With capacity: " + str(sum(result.calcUsedCapacity().values())) + \
	" of " + str(result.calcTotalCapacity())
print "In " + str(csp.counter) + " iterations."
print "******************************"

# Final Log to File
logger.finalLog(result)

# Print Final Result
printer = Printer(outputFileName)
printer.write(result)


