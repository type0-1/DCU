import sys

list = []
check = []
with open(sys.argv[1]) as f:
	for line in f:
		line = line.strip().split()
		num = int(line[0])
		name = " ".join(line[1:])
		result = str(num) + " " + name
		list.append(num)
		check.append(result)
list.sort(reverse=True)
hNum = list[0]
count = 0
s = ""
for data in check:
	data = data.strip().split()
	num = int(data[0])
	name = " ".join(data[1:])
	if hNum == num and count == 0:
		s += name + ", "
		count += 1 
	elif hNum == num and count != 0:
		s += name + ", "
s = s[:len(s) - 2].strip()
print(f'Best student(s): {s}')
print(f'Best mark: {hNum}')