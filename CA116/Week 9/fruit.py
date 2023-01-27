#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

i = 0
while i < len(inputs):
   content = inputs[i].strip()
   if content in fruit:
      print(content)
   i += 1
