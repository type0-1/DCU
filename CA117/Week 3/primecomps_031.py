#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
for n in inputs:
	primes = []
	n = int(n.strip())
	for i in range(2, n + 1):
		count = 0
		for j in range(2, i):
			if i % j == 0:
				count += 1
			else:
				pass
		if count == 0:
			primes.append(i)
	print(f'Primes: {primes}')
