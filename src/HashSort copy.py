from random import randint
from collections import deque
import time

def enterNumbers(n):
    li = []
    for i in range((n)):
        li.append(randint((-1 * n), n))

    return li


def sort(numbers):

    numberDictoionary = {}

    for i in numbers:

        if abs(i) not in numberDictoionary:

            if i < 0:

                numberDictoionary[abs(i)] = [0,1]

            else:

                numberDictoionary[i] = [1,0]

        else:

            if i < 0:

                numberDictoionary[(-1 * i)][1] += 1

            else:

                numberDictoionary[i][0] += 1


    li = deque()

    for i in numberDictoionary:

        for a in range(numberDictoionary[i][0]):
            li.append(i)

        for a in range(numberDictoionary[i][1]):

            li.appendleft(-1 * i)


    return li

"""def checkIfSorted(numbers):

    for i in range(len(numbers)-1):

        if numbers[i] > numbers[i + 1]:

            return False

    return True"""

l = enterNumbers(100000)

start_time = time.time()

l = sort(l)

total_time = time.time() - start_time

print total_time