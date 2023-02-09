#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
d = {
    0: "zero",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
   10: "ten"
}

for line in lines:
	line = line.strip().split()
	s = ""
	for n in line:
		if int(n) in d:
			s += d[int(n)] + " "
	print(s.strip())