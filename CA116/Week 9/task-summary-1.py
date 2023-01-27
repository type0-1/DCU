#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
i = 0
d = {}
newer_list = []
while i < len(inputs):
   list = inputs[i].strip()
   new_list = list.split(".")
   if new_list[0] not in d:
      d[new_list[0]] = new_list[2]
   else:
      d[new_list[0]] = new_list[2]
      newer_list.append(new_list[1])
   i += 1

for key in d:
   if d[key] == "correct":
      print(key + "." + newer_list[0])
