#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):

        self.dic = {}

        for i in pairs:

            if i[0] not in self.dic:

                self.dic[i[0]] = [i[1]]

            else:

                self.dic[i[0]].append(i[1])

    # Associates the value v with the key k.
    def put(self, k, v):

        if k in self.dic:

            self.dic[k].append(v)

        else:

            self.dic[k] = [v]

    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):

        if k in self.dic:

            return self.dic[k]

        else:

            return []

    def values(self):

        return self.dic.values()

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):

    i = 0
    currentString = ''

    for a in xrange(k):

        currentString += next(seq)

    hashGen = RollingHash(currentString)

    while True:

        yield  (i, currentString, hashGen.current_hash()) # Starting position of current string, Current string and its hash

        i += 1

        prev = currentString[0] # First character of previous string
        nex = next(seq, None) # Last character of next string

        if nex == None:

            break

        hashGen.slide(prev, nex)

        currentString = currentString[1:] + nex


# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):

    i = 0
    currentString = ''

    for a in xrange(k):

        currentString += next(seq)

    hashGen = RollingHash(currentString)

    while True:

        if (i + 1) % m == 0 or i==0:
            yield  (i, currentString, hashGen.current_hash()) # Starting position of current string, Current string and its hash

        i += 1

        prev = currentString[0] # First character of previous string
        nex = next(seq, None) # Last character of next string

        if nex == None:

            break

        if (i + 1) % m == 0 or i==0:
            hashGen = RollingHash(currentString)

        currentString = currentString[1:] + nex


# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):

    table = Multidict()
    matches = ()

    for i in intervalSubsequenceHashes(a, k, m):
        table.put(i[2], (i[0], "a"))

    for i in subsequenceHashes(b, k):
        table.put(i[2], (i[0], "b"))

    for i in table.values():

        if len(i) > 1:

            for a in xrange(len(i)):

                for b in xrange(1, (len(i) - a)):

                    if i[a][1] != i[a + b][1]:

                        yield (i[a][0], i[a + b][0])


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
