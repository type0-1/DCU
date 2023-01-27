#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

i = 0
total = 0

while i < len(inputs):
   numbers = inputs[i].strip()
   total = total + int(numbers)
   i += 1
print(total)
