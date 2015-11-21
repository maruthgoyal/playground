from random import randint


def swap(index1, index2, numbers):

	"""

	Given two indexes and an array, checks if the indices are valid and swaps their values if so 

	"""

	if(index1 < len(numbers) and index2 < len(numbers) and ((index1 - index2) != 0)):

		temp = numbers[index1]
		numbers[index1] = numbers[index2]
		numbers[index2] = temp


def sort(start, end, numbers):

	"""

	Sort by partitioning around the pivot. 

	partitioning: Put all numbers less than our pivot behind it and those greater than it ahead of it

	recurse on both sides of the pivot. 

	Pivot can be the first element or a randomly chosen one. (Randomly chosen one provides better efficiency.)

	Average case: O(n log_2 n)
	Worst case: O(n)


	"""

	if ((end - start) > 0):

		pivot = randint(start, end)

		swap(start, pivot, numbers)

		wall = start

		for index in range((start + 1), (end + 1)):

			if(numbers[index] <= numbers[start]):

				swap(index, (wall + 1), numbers)

				wall += 1

		swap(start, wall, numbers)

		sort((wall + 1), end, numbers)

		sort(start, (wall - 1), numbers)


l = [float(a) for a in (raw_input("Please enter your numbers as N spaced numbers (x1 x2 x3...) ").split()]

sort(0,(len(l) - 1),l)

print l