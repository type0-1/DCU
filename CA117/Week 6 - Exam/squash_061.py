import sys

lines = sys.stdin.readlines()
for line in lines:
	letters = []
	line = line.strip()
	s = ""
	for i in range(1, len(line)):
		if line[i - 1] == line[i]:
			s += line[i - 1]
		else:
			s += line[i - 1]
			letters.append(s)
			s = ""
			pass
	i = len(line) - 1
	rest = ""
	while i > 0 and line[i] == line[-1]:
		rest += line[i]
		i -= 1
	letters.append(rest)
	finalString = ""
	for word in letters:
		finalString += str(word.count(word[0])) + word[0]
	print(finalString)


		