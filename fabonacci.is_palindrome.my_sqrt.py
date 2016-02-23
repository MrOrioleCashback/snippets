def fabonacci(n):
	"""
	Return the n'th number of the fabonacci sequence
	"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fabonacci(n-1) + fabonacci(n-2)	

print(fabonacci(14))

def is_palindrome(sequence):
	"""
	Checks if sequence is a palindrome, returns true or false
	"""
	sequence = str(sequence).lower()
	for index, letter in enumerate(sequence):
		if letter != sequence[(index + 1) * -1]:
			return False
	return True    

print(is_palindrome('Racecar'))


def my_sqrt(a,x):
	"""
	Newton's method is a method for finding successively better
	approximations (x) to the roots (or zeroes) of a real-valued
	function (a)
	"""
	while True:
		print(x)
		y = (x + a / x) / 2
		if y == x:
			break
		x = y

my_sqrt(4, 2)  