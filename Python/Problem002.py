'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

# Determine if number is even
# Runtime O(1)
def is_even(number):
	return number % 2

# Find the sum of even Fibonacci numbers up to the maximum Fibonacci term not exceeding the given limit
def sum_even_fibs(limit):
	sum = 0			# Store sum of even-valued Fibonacci numbers
	fib_a = 1		# Store first fibonacci number
	fib_b = 2		# Store second fibonacci number
	fib_c = fib_a + fib_b	# Store current Fibonacci number where C = A + B
	
	while (fib_c < limit):
		# GET CURRENT SUM
		if is_even(fib_c):
			sum += fib_c

		# GET NEXT FIBONACCI NUMBER
		# fib_c will be used only if it passes loop condition
		fib_a = fib_b
		fib_b = fib_c
		fib_c = fib_a + fib_b

	return sum


# TEST CODE
max_value = 4000000		# 4 million
print("{:,}".format( sum_even_fibs(max_value) ) )