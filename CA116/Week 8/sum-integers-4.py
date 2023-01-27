#!/usr/bin/env python3

import sys

inputs = sys.argv[1:]

i = 0
total = 0
while i < len(inputs):
   with open(inputs[i]) as f:
      content = f.readlines()
      j = 0
      while j < len(content):
         numbers = content[j].strip()
         new_numbers = numbers.split()
         p = 0
         while p < len(new_numbers):
            total = total + int(new_numbers[p])
            p += 1
         j += 1
   i += 1
print(total)
