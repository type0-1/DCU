#!/usr/bin/env python3

import sys

for word in sys.stdin:
   chopped = word.strip()[1:len(word) - 2]
   if len(chopped) > 0:
      print(chopped)
