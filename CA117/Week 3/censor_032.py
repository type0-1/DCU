#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
	censor = f.read().strip().split()
poem = sys.stdin.readlines()

for line in poem:
	line = line.strip()
	for cen in censor:
		if cen in line:
			line = line.replace(cen, "@"*len(cen))
	print(line)