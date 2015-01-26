 #!/usr/bin/env python

depth = 1

board = [[0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 1, 0, 0, 0]]

def heuristicCalculator():
	value = [[0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0]]
	
	valueOfBoard = 0
	
	for j in range (7):
		for i in range(6):
			for k in range(1,depth+1):
				try:
					value[i][j] += board[i+k][j+k]
				except:
					value[i][j]
				try:
					value[i][j] += board[i-k if i-k>-1 else 100][j+k]
				except:
					value[i][j]
				try:
					value[i][j] += board[i+k][j-k if j-k>-1 else 100]
				except:
					value[i][j]
				try:
					value[i][j] += board[i-k if i-k>-1 else 100][j-k if j-k>-1 else 100]
				except:
					value[i][j]
				try:
					value[i][j] += board[i][j+k]
				except:
					value[i][j]
				try:
					value[i][j] += board[i][j-k if j-k>-1 else 100]
				except:
					value[i][j]
				try:
					value[i][j] += board[i-k if i-k>-1 else 100][j]
				except:
					value[i][j]
				try:
					value[i][j] += board[i+k][j]
				except:
					value[i][j]
				#try:
				#	value[i][j] += board[i][j]
				#except:
				#	value[i][j]

			valueOfBoard += value[i][j]
	return valueOfBoard

def Move():
	previousValue = 0
	previousValueAt = [0, 0]

	for i in range(0,7):
		for j in [5,4,3,2,1,0]:
			if not board[j][i]:
				board[j][i] = 1
				x = heuristicCalculator()
				board[j][i] = 0
				if x > previousValue:
					previousValue = x
					previousValueAt = [i, j]
				break

	board[previousValueAt[1]][previousValueAt[0]] = 1

#Move()
print "Heuristic Value: " + str(heuristicCalculator())
for i in range(6):
	print board[i]



