#!/usr/bin/env python3

import sys

contact = {}
with open(sys.argv[1]) as f:
	info = f.readlines()

names = sys.stdin.readlines()

for data in info:
	data = data.strip().split()
	contact[data[0]] = (data[1], data[2])

for name in names:
	if name.strip() in contact:
		print(f'Name: {name.strip()}')
		print(f'Phone: {contact[name.strip()][0]}')
		print(f'Email: {contact[name.strip()][1]}')
	else:
		print(f'Name: {name.strip()}')
		print(f'No such contact')