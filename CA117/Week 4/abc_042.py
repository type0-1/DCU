#!/usr/bin/env python3

import sys

d = {}
lines = sys.stdin.readlines()
nums = lines[0].strip().split()
letters = lines[1].strip()
order = sorted(lines[1].strip())
nums = sorted([int(n) for n in nums])
zipped = zip(order, nums)

for tup in zipped:
	d[tup[0]] = tup[1]
s = ""
for c in letters:
	if c in d:
		s += str(d[c])+ " "
print(s.strip())