def sort(li):

	"""
	Find the minimum of the array in each iteration.

	Swap it with the ith element from the left

	O(n^2)

	"""

	for i in xrange(len(li)):

		minIndex = i

		for a in xrange((i + 1), len(li)):

			if(li[a] < li[minIndex]):

				minIndex = a

		li[minIndex], li[i] = li[i], li[minIndex]

	return li

s = raw_input("Please enter your array as N spaced numbers (x1 x2 x3...)")
s2 = [float(a) for a in s.split()]
print sort(s2)

