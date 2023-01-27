#!/usr/bin/env python3

import sys

tickets = sys.argv[1:]
inputs = sys.stdin.readlines()

i = 0

while i < len(inputs):
   lottery = inputs[i].split(" ")
   j = 0
   nums = []
   while j < len(lottery):
      info = lottery[j].strip()
      nums.append(info)
      j += 1
   j = 0
   total = 0
   while j < len(tickets):
      p = 0
      while p < len(nums):
         if tickets[j] == nums[p]:
            total += 1
         p += 1
      j += 1
   if total == 1:
      print(total)
   elif total == 2:
      print("5")
   elif total == 3:
      print("100")
   else:
      print("0")
   i += 1
