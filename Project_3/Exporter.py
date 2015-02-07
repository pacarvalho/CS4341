class Exporter:
	fromFile = 0
	toFile = 0

	def __init__(self, fromFileName, toFileName):
		self.fromFile = open(fromFileName, 'r')
		self.toFile = open(toFileName, 'w')

	def write(self, results):
		i = 0
		self.toFile.write(
			"a1,a2,a3,a4,a5,a6,b1,b2,b3,b4,b5,b6,c1,c2,c3,c4,c5,c6,"+
			"d1,d2,d3,d4,d5,d6,e1,e2,e3,e4,e5,e6,f1,f2,f3,f4,f5,f6,"+
			"g1,g2,g3,g4,g5,g6,winner,win1,win2,r1p1,r2p1,r3p1,r4p1,"+
			"r5p1,r6p1,r1p2,r2p2,r3p2,r4p2,r5p2,r6p2,c1p1,c2p1,c3p1,"+
			"c4p1,c5p1,c6p1,c7p1,c1p2,c2p2,c3p2,c4p2,c5p2,c6p2,c7p2,"+
			"nbr1,nbr2,nbr3,nbr4,nc2p1,nc2p2,nc3p1,nc3p2\n")

		for line in self.fromFile.readlines():
			self.toFile.write(line[0:-1])
			self.toFile.write(',')
			self.toFile.write(str(results[i])[1:-1])
			self.toFile.write('\n')
			i += 1