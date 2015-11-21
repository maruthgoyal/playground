def fib(n, dic):

	"""
	Recursively calculates the nTH element of the Fibonacci series.

	Becomes O(1) as number of calls tends to infinity.

	Saves each encountered value in a Hash table (N --> F(n))

	"""

	if n < 1:
		return None

	elif n == 1 or n == 2:

		return 1

	else:

		if(n in dic):

			return dic[n]


		elif (((n - 1) in dic) and ((n - 2) not in dic)):

			dic[n - 2] = fib((n - 2), dic)


		elif (((n - 1) not in dic) and ((n - 2) in dic)):

			dic[n - 1] = fib((n - 1), dic)
			

		else:

			dic[n - 1] = fib((n - 1), dic)
			dic[n - 2] = fib((n - 2), dic)

		dic[n] = dic[n - 1] + dic[n - 2]

		return dic[n]

di = {}
while True:

	n = int(raw_input())

	if n < 0:
		break

	print fib(n, di)


