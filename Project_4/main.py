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

# Create Classes
world = World(90)
csp = CSP()

# Read the input file
parser = Parser(inputFileName, world)
parser.read() 

# PERFORM CSP CALCULATION!!!
result = csp.backtrackSearch(world)

# Print Final Result
printer = Printer(outputFileName)
printer.write(result)


