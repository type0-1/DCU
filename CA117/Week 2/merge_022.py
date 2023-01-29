import sys

n1 = []
n2 = []
with open(sys.argv[1]) as f:
	for line in f:
		line = line.strip()
		n1.append(int(line))
with open(sys.argv[2]) as f:
	for line in f:
		line = line.strip()
		n2.append(int(line))
i = 0
while i < len(n1) and i < len(n2):
	print(n1[i])
	print(n2[i])
	i += 1
