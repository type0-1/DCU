#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
list = []
i = 0

while i < len(inputs):
   split = inputs[i].split(" ")
   joined = split[2].strip()
   if int(joined) >= 40:
      content = " ".join(split[0:2])
      print(content)
   i += 1
