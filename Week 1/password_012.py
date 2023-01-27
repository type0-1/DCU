#!/usr/bin/env python3

import sys

for input in sys.stdin:
   n = 0
   lc = 0
   uc = 0
   spc = 0
   input = input.strip()
   for char in input:
      check1 = ("a" <= char and char <= "z")
      check2 = ("A" <= char and char <= "Z")
      check3 = ("0" <= char and char <= "9")
      if check1 and lc < 1:
         lc += 1
      elif check2 and uc < 1:
         uc += 1
      elif check3 and n < 1:
         n += 1
      elif (not check1 and not check2 and not check3) and spc < 1:
         spc += 1
   print(lc + uc + spc + n)
