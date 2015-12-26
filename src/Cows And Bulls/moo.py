from random import shuffle
from random import randint

def genNum(nDigits):

    nDigits -= 1

    start = 10**nDigits
    end = 10**(nDigits + 1)

    allNums = (str(x) for x in xrange(start, end))

    possible = []
    dead = False

    for x in allNums:

        for char in x:

            if x.count(char) > 1:

                dead = True
                break

        if dead == False:

            possible.append(int(x))

        dead = False

    shuffle(possible)

    return str(possible.pop())

def nBullsAndCows(secretNum, userGuess):

    nBulls = 0
    nCows = 0

    i = 0

    for x in userGuess:

        if x in secretNum:

            index = secretNum.index(x)

            if i == index:

                nBulls += 1

            else:

                nCows += 1
        i += 1

    return (nBulls, nCows)

def main():

    num = genNum(4)

    while True:

        userIn = raw_input("Please enter your 4-digit guess: ")

        if (len(userIn) != 4):

            print "Invalid guess. Try Again."


        else:
            if userIn == num:

                print "You got it right. " + "The number was %s" % (num)
                break

            elif userIn == "lolo":

                print num
                break

            else:

                nBnC = nBullsAndCows(num, userIn)

                print str(nBnC[0]) + " Bulls  " + str(nBnC[1]) + " Cows"

if __name__ == '__main__':
    main()
