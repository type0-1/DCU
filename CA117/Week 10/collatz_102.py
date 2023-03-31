def collatz(n):
	print(n)
	if n == 1:
		return 1
	elif n % 2 == 0:
		return collatz(n // 2)
	else:
		return collatz(n * 3 + 1)

def main():
    collatz(5)

if __name__ == '__main__':
    main()