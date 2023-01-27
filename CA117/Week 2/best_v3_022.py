import sys

list = []
check = []
with open(sys.argv[1]) as f:
	for line in f:
		try:
			line = line.strip().split()
			name = " ".join(line[1:])
			num = int(line[0])
			result = str(num) + " " + name
			check.append(result)
			list.append(num)
		except ValueError:
			print(f'Invalid mark {line[0]} encountered. Skipping.')
list.sort(reverse=True)
hNum = list[0]
for data in check:
	data = data.strip().split()
	num = int(data[0])
	name = " ".join(data[1:])
	if hNum == num:
		print(f'Best student: {name}')
		print(f'Best mark: {num}')
		break