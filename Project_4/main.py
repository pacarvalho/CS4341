#!/usr/bin/env python
# CS4341 Project 4 
# Main file
# By Paulo Carvalho and Alex Bennett

from Parser import Parser
from World import World
import sys

# Create World Class
world = World()

# Get User Input from Terminal
inputFileName = sys.argv[1]

# Read the input file
parser = Parser(inputFileName, world)
parser.read() 

# Print Output from World FOR DEBUGGING
world.logAll()

