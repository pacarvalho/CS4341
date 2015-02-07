from Importer import *
from Exporter import *
from Analyzer import *

# Take Files Given By User
# TODO!!!

# Import the Training Data Set and Parse It
trainFile = Importer("trainDataSet.csv")
boards = trainFile.parser()

# Analyze All Boards
results = []
for i in range(1000):
	analyzer = Analyzer(boards[i])
	results.append(analyzer.analyze())

# Save to God File
print results
exporter = Exporter("trainDataSet.csv", "trainDataSetResults.csv")
exporter.write(results)


