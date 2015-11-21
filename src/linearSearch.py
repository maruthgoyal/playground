from random import randint
import time
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
result = search(0, a)
total_time = time.time() - start_time
print result, " Time taken is ", "{0:.2f}".format(total_time)