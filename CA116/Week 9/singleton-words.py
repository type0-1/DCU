#!/usr/bin/env python3

import sys
inputs = sys.stdin.readlines()
d = {}

total = 0

i = 0
while i < len(inputs):
   word = inputs[i].strip()
   if word not in d:
      d[word] = 0
   else:
      d[word] = + 1
   i += 1

for key in d:
   if d[key] == 0:
      print(key)
