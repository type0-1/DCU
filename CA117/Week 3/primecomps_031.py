#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

for n in inputs:
	n = int(n.strip())
	primes = [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, i))]
	print(f'Primes: {primes}')