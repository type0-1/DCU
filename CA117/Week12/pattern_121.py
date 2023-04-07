import sys

pattern = sys.stdin.readline().strip()

output = []
s = ""

for word in sys.stdin:
	word = word.strip()
	if len(pattern) == len(word):
		s = ""
		for i, l in enumerate(word):
			if pattern[i] == word[i] and l.isalpha():
				s += l
			elif pattern[i] == "-" and word[i].isalpha():
				s += l
		if word == s:
			output.append(s)
if len(output):
	print(", ".join(output))
