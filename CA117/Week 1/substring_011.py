#!/usr/bin/env python3

import sys

for word in sys.stdin:
   check = word.split(" ")
   if check[0].lower() in check[1].strip().lower():
      print("True")
   else:
      print("False")
