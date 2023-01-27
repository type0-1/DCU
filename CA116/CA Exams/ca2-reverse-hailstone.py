#!/usr/bin/env python3

import sys

input = sys.argv[1]

nums = []
i = 0

while i < 9 + 1:
   input = int(input)
   if input % 2 == 0:
      nums.append(input)
      input = input // 2
   else:
      nums.append(input)
      input = input * 3 + 1
   i += 1

i = 0

while i < len(nums):
   print(nums[len(nums) - i - 1])
   i += 1
