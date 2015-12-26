import matplotlib.pyplot as plt
import numpy as np

def fib(x):

    olderEl = 0
    oldEl = 1
    currEl = 1

    for i in xrange(x):

        if i == 0:

            yield 0

        elif i == 1:

            yield 1

        else:

            currEl = oldEl + olderEl

            yield currEl

            olderEl = oldEl
            oldEl = currEl

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes


a = []

for i in fib(20):
    a.append(i)



c = primes_sieve(10**6)

slope = 17.3567274858
slopeLine = [(x*(slope - 6)) for x in xrange(len(c))]
b = [i for i in xrange(len(c))]

'''print c
print a


plt.plot(b, a, label="fib") '''
plt.plot(b, c, label="prime")
plt.plot(b, slopeLine)
plt.legend(loc='best')
plt.show()
