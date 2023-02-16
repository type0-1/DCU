import sys

inputs = sys.stdin.readlines()
pos = int(inputs[0])
letters = inputs[1].strip()

def a(prize):
	if prize == 1:
		prize = 2
	elif prize == 2:
		prize = 1
	return prize

def b(prize):
	if prize == 2:
		prize = 3
	elif prize == 3:
		prize = 2
	return prize

def c(prize):
	if prize == 3:
		prize = 1
	elif prize == 1:
		prize = 3
	return prize
	
for l in letters:
	if l == "A":
		pos = a(pos)
	elif l == "B":
		pos = b(pos)
	else:
		pos = c(pos)
print(pos)
