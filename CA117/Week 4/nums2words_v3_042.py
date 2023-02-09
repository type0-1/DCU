#!/usr/bin/env python3

import sys
d = {}
nums = sys.stdin.readlines()
with open (sys.argv[1]) as f:
	tr = f.readlines()

count = 0
for line in tr:
	line = line.strip().split()
	d[str(count)] = (line[0], line[1])
	count += 1
for line in nums:
	line = line.strip().split()
	s = ""
	for n in line:
		if n in d:
			s += d[n][1] + " "
	print(s.strip())