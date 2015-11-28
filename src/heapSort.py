from minHeap import minHeap

def sort(li):

	"""

	Sorts a given array of numbers using min-heaps

	First, add all the numbers into a min-heap (see minHeap.py for my implementation)

	Then do the pop (or extract-min) operation N times for N numbers and add that to the new array

	Time complexity: O(N lg N)

	"""

	sortedList = []
	miHeap = minHeap()

	for i in li:
		miHeap.append(i)

	for i in xrange(len(li)):

		sortedList.append(miHeap.pop())

	return sortedList

nums = raw_input("Please enter the numbers you would like to sort as spaced numbers (x1 x2 x3 ...) ")
lis = [float(x) for x in nums.split()]
print sort(lis)

