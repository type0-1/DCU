import sys

num = int(sys.stdin.read().strip())

s = str(num)

while len(s) != 1:
	total = 1
	for n in s:
		if int(n) != 0:
			total *= int(n)
	s = str(total)
print(s)
