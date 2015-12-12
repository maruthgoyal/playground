def sort(li):
    """
    Implements the counting sort algorithm. We count the frequency of each element and assign it to the resp. index.
    So int 'i' is assigned to A[i] in our array of frequencies. Then starting at the Smallest number, we add every num A[i] times

    IMP: All numbers must be integers
    
    O(N) worst case
    O(max) space
    """
    assert isinstance(li[0], int)

    largestNum = max(li) # Largest number in the list
    smallestNum = min(li) # Smallest number in the list
    output = [] # The list to be output
    frequencies = [0 for x in xrange(largestNum + 1)] # initialising a list of size largestNum

    for i in li: # Iterating over the list

        frequencies[i] += 1 # Incrementing the frequency of number 'i' at index 'i'


    for i in xrange(smallestNum, (largestNum + 1)): # Iterating from the smallest number to the largest number

        for j in xrange(frequencies[i]): # Adding the numbers

            output.append(i) # Append it based on the value of its frequency

    return output

print sort([5,4,3,2,1])
