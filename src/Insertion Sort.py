def sort(li):

	for i in xrange(1,len(li)):

		a = i

		while( (a > 0) and (li[a] < li[a-1]) ):

			swap(a, (a - 1), li)

			a -= 1

	return li

def swap(num1, num2, li):

	temp = li[num1]
	li[num1] = li[num2]
	li[num2] = temp
	

s = raw_input("Enter your array as N spaced numbers (x1 x2 x3...)")
s2 = [float(a) for a in s.split()]

print sort(s2)