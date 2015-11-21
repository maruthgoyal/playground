from random import randint
import time


def enterNumbers(n):
    li = []
    for i in range((n)):
        li.append(randint((-1 * n), n))

    return li


def sort(numbers):
    numberDictoionary = {}

    for i in numbers:

        if i not in numberDictoionary:
            numberDictoionary[i] = 1


        else:
            numberDictoionary[i] += 1

    li = []

    for i in numberDictoionary:

        for a in range(numberDictoionary[i]):
            li.append(i)

    return li

time_list = []

for i in range(100000):

    start_time = time.time()

    l = enterNumbers(i)

    l = sort(l)

    total_time = time.time() - start_time

    time_list.append(total_time)


