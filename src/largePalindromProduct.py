"""
Find largest product of 2 3-digit numbers such that it is a palindrome

"""
from math import sqrt

def factorize(n):

	factors = []
	
	for i in xrange(100, ((n/2) + 1)):

		if (n % i == 0):
			
			a = i
			b = n/a

			if(len(str(a)) == 3) and (len(str(b)) == 3):

				c = (a,b)

				factors.append(c)

	return factors


maxVal = "998001"

while True:
	
	rev = maxVal[::-1]
	
	if (rev == maxVal):

		f = factorize(int(maxVal))

		if bool(f) == True:

			print "Answers are " + str(f[0][0]) + " and " + str(f[0][1]) + " which is = " + str(maxVal)
			break



	maxVal = str((int(maxVal) - 1))





