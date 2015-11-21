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

	length = len(numbers)
	numbers = sorted(numbers)

	index = (length - 1) / 2
	start = 0
	end = length - 1

	while (end - start) > -1:
		
		if numbers[index] == key:
			return index

		elif numbers[index] > key:
			
			end = index - 1
			index = (start + end) / 2 
			

		else:
			start = index + 1
			index = (start + end) / 2	

	return -1

num = raw_input("Please enter the numbers to be searched as N spaced numbers (x1 x2 x3...) ")
nums = [float(a) for a in num.split()]
key = float(raw_input("Please enter the number to be searched "))

index = binary_search(key, nums)

if(index == -1):

	print "The key was not found in the array"

else:

	print "The key " + str(key) + " was found at index " + str(index) + " in the sorted array"




