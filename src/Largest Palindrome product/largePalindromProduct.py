"""
Find largest product of 2 3-digit numbers such that it is a palindrome

"""
from math import sqrt

def factorize(n):

	for i in xrange(2,int(sqrt(n)) + 1):

		if (n % i == 0):

			a = i
			b = n/i

			if((a > 99 and a < 1000) and (b > 99 and b < 1000)):

				return True

	return False

nTc = input()

for a in xrange(nTc):

	maxVal = str(int(raw_input()) - 1)

	while True:

		rev = maxVal[::-1]

		if (rev == maxVal):

			f = factorize(int(maxVal))

			if bool(f) == True:

				#print "Answers are " + str(f[0][0]) + " and " + str(f[0][1]) + " which is = " + str(maxVal)
				print maxVal
				break

		maxVal = str((int(maxVal) - 1))
