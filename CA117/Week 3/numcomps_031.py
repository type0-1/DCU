#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()

for num in input:
	num = int(num.strip())
	three = [i for i in range(1, num + 1) if not i % 3]
	squaredThree = [i ** 2 for i in range(1, num + 1) if not i % 3]
	doubleFour = [i * 2 for i in range(1, num + 1) if not i % 4]
	eitherThreeOrFour = [i for i in range(1, num + 1) if not i % 3 or not i % 4]
	ThreeFour = [i for i in range(1, num + 1) if not i % 3 and not i % 4]
	print(f'Multiples of 3: {three}')
	print(f'Multiples of 3 squared: {squaredThree}')
	print(f'Multiples of 4 doubled: {doubleFour}')
	print(f'Multiples of 3 or 4: {eitherThreeOrFour}')
	print(f'Multiples of 3 and 4: {ThreeFour}')