import sys

words = sys.stdin.readlines()
vowels = ["a", "e", "i", "o", "u"]
tups = []
for word in words:
	vowel = ""
	count = 0
	for l in word.strip():
		if l in vowels:
			vowel += l
		else:
			count += len(vowel)
			vowel = ""
	tups.append((count, word.strip()))
tups = sorted(tups, reverse=True)
print(tups[0][1])
