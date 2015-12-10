def sort(li):

    assert isinstance(li[0], int)

    largestNum = max(li)
    smallestNum = min(li)
    output = []
    frequencies = [0 for x in xrange(largestNum + 1)]

    for i in li:

        frequencies[i] += 1


    for i in xrange(smallestNum, (largestNum + 1)):

        for j in xrange(frequencies[i]):

            output.append(i)

    return output

print sort([5,4,3,2,1])
