def sort(li):

	"""

	Sort using pairwise swaps.

	For all numbers in the list, if it is larger than its neighbour, swap it with the neighbour

	After i iterations, the last i numbers will be in place

	Do the pairwise swap routine N times to sort completely

	O(N^2)

	"""

	for i in xrange(len(li)): # Since after 'a' iterations, a numbers are sorted, we need len(li) iterations to sort len(li) numbers

		for j in xrange((len(li) - 1)): # len(li) - 1 because we don't want li[j + 1] to become an invalid index at any point

			if li[j] > li[j + 1]:

				li[j], li[j + 1] = li[j + 1], li[j] # Swapping the elements. ("pythonista" way of doing it)

	return li


nums = raw_input("Please enter the numbers as spaced numbers (x1 x2 x3 ...): ")
num = [float(x) for x in nums.split()]

print sort(num)
