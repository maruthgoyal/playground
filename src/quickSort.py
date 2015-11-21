from random import randint
import time

def swap(index1, index2, numbers):

	if(index1 < len(numbers) and index2 < len(numbers) and ((index1 - index2) != 0)):

		temp = numbers[index1]
		numbers[index1] = numbers[index2]
		numbers[index2] = temp

def enterNumbers(n):
    li = []
    for i in range((n)):
        li.append(randint(0, n))

    return li


def sort(start, end, numbers):

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

l = enterNumbers(2000000)

start_time = time.time()

sort(0,(len(l) - 1),l)

total_time = time.time() - start_time

print total_time










