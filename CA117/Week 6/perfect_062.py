def get_divisors(n):
	numbers = [i for i in range(1, n + 1) if n % i == 0]
	return numbers

def get_proper_divisors(n):
	numbers = get_divisors(n)[:-1]
	return numbers

def is_perfect(n):
	numbers = get_proper_divisors(n)
	if sum(numbers) == n:
		return True
	return False


