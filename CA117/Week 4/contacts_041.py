#!/usr/bin/env python3

import sys

phoneNums = {}
with open(sys.argv[1]) as f:
	data = f.readlines()

stdin = sys.stdin.readlines()

for info in data:
	info = info.strip().split()
	phoneNums[info[0]] = info[1]

for name in stdin:
	if name.strip() in phoneNums:
		print(f'Name: {name.strip()}')
		print(f'Phone: {phoneNums[name.strip()]}')
	else:
		print(f'Name: {name.strip()}')
		print("No such contact")