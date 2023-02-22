import sys

lines = sys.stdin.readlines()
maximum = 0
count = 0
entries = lines[1:]
denied = 0

try:
	maximum = int(lines[0].strip())
	for i in range(len(entries)):
		perm, num = entries[i].strip().split()
		try:
			num = int(num)
			if count + num <= maximum and perm == "enter":
				count += num
			elif perm == "enter" and count + num > maximum:
				denied += 1
			elif perm == "leave" and count - num >= 0:
				count -= num
			else:
				pass
		except ValueError:
			print(f'{num} is not a number.')
	print(denied)
except ValueError:
	print(f'{lines[0].strip()} is not a number.')




