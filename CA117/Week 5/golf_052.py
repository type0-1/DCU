import sys

tuples = []
disqualified = []
lines = sys.stdin.readlines()

for line in lines:
	nums = [int(n) for n in line if n.isnumeric()]
	line = line.strip().split()
	if len(nums) != 3:
		disqualified.append(" ".join(line[:-3]))
	else:
		name = " ".join(line[:-3])
		both = (sum(nums), name)
		tuples.append(both)
tuples.sort()
for result in tuples:
	print(f'{result[1]}: {result[0]}')
s = ""
for i in range(len(disqualified)):
	s += " " + disqualified[i] + ",  "
	s = s.strip()
	if i + 1 == len(disqualified):
		print(f'Disqualified: {s[:len(s) - 1]}')
