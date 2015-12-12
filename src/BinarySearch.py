def binary_search(key, numbers):

	"""

	Assume input array is sorted (sort the array as a precaution in case user tries to mess with you)

	Look at middle of array for element

	if it is equal to the element, return the index

	if it is smaller look at the middle of the remaining array on the right

	if it is greater, look at the middle of the remaining array on the left

	repeat until element is found or index becomes invalid

	O(log_2 N)

	"""

	length = len(numbers)  # Number of elements in the list
	numbers = sorted(numbers) # Sorting it as a precaution in case user tries to crash us :|

	index = (length - 1) / 2 # Chosing the middle element as the index
	start = 0 # Starting at the initial position
	end = length - 1 # Last element of the list

	while (end - start) > -1: # Ensuring end is not less than start, they can be the same, pointing to 1 element, but if they end up crossing over, the element isn't in the list

		if numbers[index] == key: # If the element at position "index" is our number, return the index
			return index

		elif numbers[index] > key: # If the element at position "index" is > our number, search the elements to the left of it

			end = index - 1 # Changing end to be the element to the left of our current index
			index = (start + end) / 2 # setting index to be the middle of the new list


		else: # If the element at position "index" is < our number, search the elements to the right of it.
			start = index + 1 # Setting start to be the element to the right of our current index
			index = (start + end) / 2 # Setting index to be the middle of the new list

	return -1 # Returns -1 iff the element is not in our list

num = raw_input("Please enter the numbers to be searched as N spaced numbers (x1 x2 x3...) ")
nums = [float(a) for a in num.split()]
key = float(raw_input("Please enter the number to be searched "))

index = binary_search(key, nums)

if(index == -1):

	print "The key was not found in the array"

else:

	print "The key " + str(key) + " was found at index " + str(index) + " in the sorted array"
