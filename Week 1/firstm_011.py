#!/usr/bin/env python3

import sys

for lines in sys.stdin:
   total = 0
   words = lines.split()
   string = ""
   for word in words:
      if word[0] == "m" and total == 0:
         string += word.capitalize() + " "
         total += 1
      else:
         string += word + " "
   print(string.strip())
