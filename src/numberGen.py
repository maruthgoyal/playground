from random import randint

def enterNumbers(n):

	"""

	Generates list of N psuedo-random numbers

	"""
	li = []
	for i in range(n):

		li.append(randint(0,n))

	return li

numbers = enterNumbers(10000000)

print numbers