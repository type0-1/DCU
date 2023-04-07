import sys

lines = sys.stdin.readlines()

for line in lines:
	x, y = list(map(int, line.strip().split()))
	if x > 0 and y > 0:
		print(1)
	elif x > 0 and y < 0:
		print(2)
	elif x < 0 and y < 0:
		print(3)
	elif x < 0 and y > 0:
		print(4)