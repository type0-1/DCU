#!/usr/bin/env python3

import sys

for word in sys.stdin:
   count = 0
   first, second  = word.split()
   first = first.strip()
   second = second.strip()
   for char in first:
      if char.lower() in second.lower():
         second = second.replace(char, "!")
         count += 1
      else:
         pass
   if count == len(first):
      print("True")
   else:
      print("False")
