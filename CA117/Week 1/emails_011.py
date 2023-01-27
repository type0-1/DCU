#!/usr/bin/env python3

import sys

for email in sys.stdin:
   first, second, no1, no2 = email.split(".")
   string = ""
   i = 0
   while i < len(second) and not ("0" <= second[i] and second[i] <= "9"):
      string += second[i]
      i += 1
   if i < len(second):
      print(first.capitalize(), string.capitalize())
