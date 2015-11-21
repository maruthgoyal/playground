from random import randint
import time

def binary_search(key, numbers):

	length = len(numbers)
	numbers.sort()

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

def search(num, li):
    
    for i in xrange(len(li)):
        
        if li[i] == num:
            
            return i
        
    return -1


def numGen(n):
	
	li = []
	
	for i in xrange(n):
		
		li.append(randint((-1 * n), n))
	
	li = sorted(li)
	
	return li		
				

a = numGen(9000000)
start_time = time.time()
result = binary_search(a[8999999], a)
total_time = time.time() - start_time


print "Found 0 at position ", result, " Time taken for Algorithm #1 is ", "{0:.2f}".format(total_time)

start_time = time.time()
result = search(a[8999999], a)
total_time = time.time() - start_time 

print "Found 0 at position ",result, " Time taken for Algorithm #2 is ", "{0:.2f}".format(total_time)

