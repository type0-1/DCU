#!/usr/bin/env python3

import sys
import string

punc = string.punctuation
letterCount = {}
lines = sys.stdin.read().split()
new_words = []

for word in lines:
	s = ""
	for c in word:
		if c not in punc or c in punc and word[len(word) - 1] not in punc:
			s += c.lower()
		else:
			break
	new_words.append(s)
new_words.sort()
for word in new_words:
	if word not in letterCount:
		letterCount[word] = 1
	else:
		letterCount[word] += 1
for entry in letterCount:
	print(f'{entry} : {letterCount[entry]}')
