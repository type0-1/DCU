import sys

for line in sys.stdin:
	digits = [int(n) for n in line.strip().split() if line.count(n) == 1]
	print(max(digits, default="none"))

