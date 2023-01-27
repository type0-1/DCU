#!/usr/bin/env python3

import sys
numbers = sys.stdin.readlines()
buckets = 0

litersAvailable = int(numbers[0].strip())
capacity = numbers[1].strip().split()

for liter in capacity:
   if litersAvailable >= int(liter):
      litersAvailable -= int(liter)
      buckets += 1
   else:
      break
print(buckets)
