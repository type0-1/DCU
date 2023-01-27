#!/usr/bin/env python3

import sys

command = sys.argv[1]
command = command.split("=")
inputs = sys.stdin.readlines()
i = 0

while i < len(inputs) - 1:
   location = inputs[0].strip()
   location = location.split(",")
   current = inputs[i].strip()
   current = current.split(",")
   j = 0
   while j < len(location):
      if location[j] == command[0]:
         if current[j] == command[1]:
            print(",".join(current))
      j += 1
   i += 1
