import sys

words = []
for line in sys.stdin:
	line = line.strip().split()
	s = ""
	for word in line:
		if not word[-1].isalpha():
			if word[:-1].lower() not in words and word[:-1].title() not in words:
				s += word + " "
				words.append(word[:-1])
			else:
				s += ". "
		else:
			if word.title() not in words and word.lower() not in words:
				s += word + " "
				words.append(word)
			else:
				s += ". "
	print(s.strip())
