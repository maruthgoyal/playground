from random import randint

def search(num, li):
    
    """

    Goes through array and looks for element one by one

    O(n)

    """
    for i in xrange(len(li)):
        
        if li[i] == num:
            
            return i
        
    return -1

nums = [float(a) for a in (raw_input("Please enter your numbers as N spaced numbers (x1 x2 x3...) ")).split()]
key = float(raw_input("Please enter the number to be searched. "))
result = search(key, nums)

print "The number %d was found at index %d" %(key, result)
