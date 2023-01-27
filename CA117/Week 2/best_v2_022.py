import sys
list = []
check = []
try:
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.strip().split()
			name = " ".join(line[1:])
			num = int(line[0])
			result = str(num) + " " + name
			list.append(num)
			check.append(result)
	list.sort(reverse = True)
	hNum = list[0]
	for data in check:
		data = data.strip().split()
		if hNum == int(data[0]):
			name = " ".join(data[1:])
			num = int(data[0])
			print(f'Best student: {name}')
			print(f'Best mark: {num}')
			break
except ValueError:
	print(f'Invalid mark {line[0]} encountered. Exiting.')