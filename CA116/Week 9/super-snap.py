#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
snap = {}
i = 0

while i < len(inputs):
   new_inputs = inputs[i].split()
   if new_inputs[0] not in snap:
      snap[new_inputs[0]] = True
   else:
      print("snap: " + new_inputs[0])
      i = len(inputs)
   i += 1
