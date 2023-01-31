#!/usr/bin/env python3

# Explation on code:
# "i for i in range(2, n + 1)" will iterate from numbers 2 to n + 1, (2 to n is also acceptable.)
# "if all(i % j != 0 for j in range(2, i) works as follows:

# 1: for j in range(2, i) means j will iterate through numbers 2 to number "i".
# 2: The "all()" method is a method that returns "True" if all conditions are met, False otherwise.
# In this task, the conditions we want to me is for all numbers between 2 to i - 1 to all have remainders when divisble.
# This is in order to check for a prime number, and that is displayed with "i % j != 0"
# So, if all(i % j != 0 for j in range(2, i)) will only append i to the list if all numbers that j iterates have remainders. 

import sys

inputs = sys.stdin.readlines()

for n in inputs:
	n = int(n.strip())
	primes = [i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, i))]
	print(f'Primes: {primes}')
