from copy import deepcopy

class Importer:
	boards = []
	f = 0

	def __init__(self, filename):
		self.f = open(filename, 'r')

	def parser(self):
		tempBoard = [[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7]

		for line in self.f.readlines():
			line = line.split(',')
			line = map(int, line)
			for row in range(6):
				for col in range(7):
					tempBoard[5-row][col] = line[row+6*col]
			self.boards.append(deepcopy(tempBoard))

		return self.boards
