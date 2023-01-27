import sys
list = []
check = []
try:
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.strip().split()
			name = " ".join(line[1:])
			number = int(line[0])
			if str(number) not in list:
				list.append(str(number))
				list.append(name)
				result = str(number) + " " + name
				check.append(result)
			else:
				pass
	list.sort(reverse = True)
	hNum = list[len(list) // 2]
	for data in check:
		if str(hNum) in data:
			data = data.strip().split()
			number = int(data[0])
			name = " ".join(data[1:])
			print(f'Best student: {name}')
			print(f'Best mark: {number}')
			break
except FileNotFoundError:
	print(f'This file {sys.argv[1]} could not be opened.')