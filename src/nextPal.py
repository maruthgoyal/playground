nTc = int(raw_input())

def checkPal(s):

	for i in xrange(int((len(s)/2))):

		if(s[i] != s[(len(s) - 1) - i]):

			return False

	return True

for i in xrange(nTc):

	k = int(raw_input())

	a = k + 1

	while True:

		aS = str(a)
		pal = checkPal(aS)

		if pal:
			print aS
			break

		else:
			a += 1
