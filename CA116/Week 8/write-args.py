#!/usr/bin/env python3

import sys

file = sys.argv[1]
inputs = sys.argv[2:]

with open(file, "w") as f:
   i = 0
   while i < len(inputs):
      f.write(inputs[i] + "\n")
      i += 1
