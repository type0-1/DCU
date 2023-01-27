#!/usr/bin/env python3

import sys

for word in sys.stdin:
   word = word.strip()
   cap1 = word[0].upper()
   cap2 = word[len(word) - 1].upper()
   print(cap1 + word[1:len(word) - 1] + cap2)
