#!/usr/bin/env python3

import sys
f = True
buckets = 0

for numbers in sys.stdin:
   if f:
      numbers = numbers.split()
      liters = int(numbers[0].strip())
      f = False
   else:
      listofLiters = numbers.split()
      buckets = 0
      for liter in listofLiters:
         if liters >= int(liter):
            liters = liters - int(liter)
            buckets += 1
         elif liters < int(liter):
              break
      print(buckets)
