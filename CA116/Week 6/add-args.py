#!/usr/bin/env python3

import sys

inputs = sys.argv[1:]

i = 0
total = 0

while i < len(inputs):
   number = int(inputs[i])
   total = total + number
   i += 1

print(total)
