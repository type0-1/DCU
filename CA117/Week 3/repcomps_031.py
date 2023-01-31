#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

for num in inputs:
	num = int(num.strip())
	non = [0 if i % 3 != 0 else i for i in range(1, num + 1)]
	print(f'Non-multiples of 3 replaced: {non}')