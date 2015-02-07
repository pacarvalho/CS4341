#!/usr/bin/env python

from Importer import *
from Exporter import *
from Analyzer import *
import sys

# Take Files Given By User
dataSetFileName = sys.argv[1]
outputFileName = sys.argv[2]

print sys.argv

# Import the Training Data Set and Parse It
trainFile = Importer(dataSetFileName)
boards = trainFile.parser()

# Analyze All Boards
results = []
for i in range(1000):
	analyzer = Analyzer(boards[i])
	results.append(analyzer.analyze())

# Save to God File
exporter = Exporter(dataSetFileName, outputFileName)
exporter.write(results)
print "I am done :)"


