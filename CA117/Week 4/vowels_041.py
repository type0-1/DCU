#!/usr/bin/env python3

import sys

vowels = {}

lines = sys.stdin.read().strip()

new = [word.strip().lower() for word in lines]
lowerWords = "".join(new)
sort = []
sort.append((lowerWords.count("e"), "e"))
sort.append((lowerWords.count("a"), "a"))
sort.append((lowerWords.count("o"), "o"))
sort.append((lowerWords.count("i"), "i"))
sort.append((lowerWords.count("u"), "u"))
sort.sort(reverse=True)
pad = len(str(sort[0][0]))
for tup in sort:
	vowels[tup[1]] = tup[0]
for vowel in vowels:
	print(f'{vowel} : {vowels[vowel]:{pad}d}')