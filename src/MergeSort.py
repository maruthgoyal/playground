
def merge(start, mid, end, numbers):

	"""

	Copy elements of left node into "left" array and right node into "right" array

	Replace appropriate index of original array with smaller number from left and right until both are empty

	O(N)

	"""

	left = []
	right = []

	leftIndex = 0
	rightIndex = 0

	for index in range(start, ( mid + 1 )):

		left.append(numbers[index])

	for index in range(( mid + 1 ), (end + 1)):

		right.append(numbers[index])


	for i in range(start, (end + 1)):

		if (rightIndex < len(right) or leftIndex < len(left)):

			if(leftIndex >= len(left) and rightIndex < len(right)):  # Left is empty. Copy over right

				for x in range(i,(end + 1)):
					
					numbers[x] = right[rightIndex]
					rightIndex += 1

				break

			elif(rightIndex >= len(right) and leftIndex < len(left)): # Right is empty. Copy over left

				for x in range(i, (end + 1)):

					numbers[x] = left[leftIndex]
					leftIndex += 1 

				break
			
			elif(left[leftIndex] < right[rightIndex]): # Left element is smaller than right

				numbers[i] = left[leftIndex]
				leftIndex += 1

			elif (right[rightIndex] <= left[leftIndex]): # Right element is smaller than left

				numbers[i] = right[rightIndex]
				rightIndex += 1

def sort(start, end, numbers):

	"""

	Recursively divide array into 2 halves until they are of length one

	Merge all subarrays using Merge proccedure

	O(n log_2 n)


	"""

	if(end - start == 0):
		return -1

	else:	

		mid = (start + end)/2

		sort(start, mid, numbers)

		sort( ( mid + 1 ), end, numbers )

		merge(start, mid, end, numbers)


numbers = raw_input("Please enter your numbers as N spaced numbers (x1 x2 x3...)")
s = [float(a) for a in numbers.split()]
sort(0, (len(s) - 1), s)

print s