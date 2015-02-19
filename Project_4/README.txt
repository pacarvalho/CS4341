CS4341 Project 4 README
By Alex Bennett and Paulo Carvalho

The program can be run from the terminal of any computer that
has python installed. To run the program 'cd' into the file 
where the program is installed run the following command:
	
	./main.py inputFile outputFile logFile minCapacity

		Where:
			inputFile: File containing constraints in 
			appropriate format.

			outputFile: File to which the output will be
			written.

			logFile: File to which the logs will be written

			minCapacity: Value from 0 to 100 of the minimum
			capacity constraint.

For proper operation of the program the following files are 
required:
	CSP.py 
		Runs the backtracking algorithm

	Logger.py
		Generates the log file

	main.py
		Calls all required methods and creates objects

	Parser.py
		Reads the input file

	Printer.py
		Generates the output file

	World.py
		Keeps track of the state of the world and constraints

The file "test.py" was used for testing and is not required
for running of the program.

