import sys

lines = sys.stdin.readlines()
first = lines[0].strip()
second = lines[1].strip()
s = "" 
for i in range(len(first)):
	if first[i] == second[i]:
		s += "-"
	else:
		s += "*"
print(first)
print(second)
print(s)
