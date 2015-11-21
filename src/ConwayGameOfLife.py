import time
from random import randint

"""

A version of Conway's game of life.

Check for validity at random nodes because pattern was a bit boring when it was done in a linear manner :P

"""

def update():

	"""

	Print out the current grid

	"""
	
	for a in grid:
		
		b = str(a)
		b = b.replace("[", " ")
		b = b.replace("]", " ")
		b = b.replace(",", " ")
		b = b.replace("'", " ")
		
		print b
	print ""
	print ""

def nDeadAndAliveNeighbors(li, x, y):

	"""

	Returns number of Dead neighbours and Alive neighbours as a tuple

	"""

	node = li[x][y]

	above = "-1"
	below = "-1"
	right = "-1"
	left = "-1"
	diagonalRightUp = "-1"
	diagonalLeftUp = "-1"
	diagonalRightBottom = "-1"
	diagonalLeftBottom = "-1"

	if((x > -1 and x < len(li)) and (y > -1 and y < len(li[0]))):
		if (x > 0):

			above = li[x-1][y]

			if(y < (len(li[0]) - 1)):
				diagonalRightUp = li[x-1][y + 1]

			if(y > 0):
				diagonalLeftUp = li[x-1][y - 1]

		if (x < (len(li) - 1)):

			below = li[x+1][y]

			if(y < (len(li[0]) - 1)):
				diagonalRightBottom = li[x+1][y+1]
			
			if(y > 0):
				diagonalLeftBottom = li[x+1][y-1]

		if (y > 0):
			left = li[x][y - 1]

		if(y < (len(li[0]) - 1)):
			right = li[x][y + 1]

	nDead = 0
	nAlive = 0

	a = [above, below, right, left, diagonalLeftBottom, diagonalRightBottom, diagonalLeftUp, diagonalRightUp]

	for s in a:

		if(s == "#"):

			nAlive += 1

		elif(s == "."):

			nDead += 1

	return(nAlive, nDead)

def checkNode(li, x, y):

	"""

	Decides death or life of a node based on Conway's rules

	1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.

	2. Any live cell with two or three live neighbours lives on to the next generation.

	3. Any live cell with more than three live neighbours dies, as if by over-population.

	4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

	"""

	if( (x > -1 and x < len(li)) and ( y > -1 and y < len(li[0]))):

		node = li[x][y]

		nAlive = nDeadAndAliveNeighbors(li, x, y)[0]
		nDead = nDeadAndAliveNeighbors(li, x, y)[1]

		if (node == "#" and ((nAlive in (0,1)) or (nAlive > 3))):

			li[x][y] = "."

			update()
			#time.sleep(1)


		elif(node == "." and (nAlive == 3)):

			li[x][y] = "#"
			update()
			#time.sleep(1)

def getNeighbors(li, x, y):

	"""

	Returns indices of all neighbours of a node as a list of 2 element lists if the neighbour exists
	Otherwise the default value of the neighbour is [-1, -1] (invalid index)

	"""

	above = [-1,-1]
	below = [-1,-1]
	right = [-1,-1]
	left = [-1,-1]
	diagoyalRightUp = [-1,-1]
	diagoyalLeftUp = [-1,-1]
	diagoyalRightBottox = [-1,-1]
	diagoyalLeftBottox = [-1,-1]

	if (x > 0):

		above = [(x-1),y]

		if(y < (len(li[0]) - 1)):
			diagoyalRightUp = [(x-1), (y + 1)]

		if(y > 0):
			diagoyalLeftUp = [(x-1),(y - 1)]

	if (x < len(li)):

		below = [(x+1),(y)]

		if(y < (len(li[0]) - 1)):
			diagoyalRightBottox = [(x+1),(y+1)]
			
		if(y > 0):
			diagoyalLeftBottox = [(x+1),(y-1)]

	if (y > 0):
		left = [x,(y - 1)]

	if(y < (len(li[0]) - 1)):
		right = [x,(y + 1)]

	return [above, below, right, left, diagoyalLeftBottox, diagoyalRightBottox, diagoyalLeftUp, diagoyalRightUp]





grid = [["#" for i in xrange(5)] for j in xrange(5)]

m = randint(0,4)
n = randint(0,4)

grid[m][n] = "."

update()
#time.sleep(1)

while True:
	
	time.sleep(0.3)
	checkNode(grid, m, n)

	a = getNeighbors(grid, m, n)
	s = a[randint(0,7)]
	m = s[0]
	n = s[1]