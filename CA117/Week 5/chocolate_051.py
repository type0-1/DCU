import sys

lines = sys.stdin.readlines()

for n in lines:
	if int(n) < 400:
		print(400 // int(n))
	else:
		print(int(n) // 400)