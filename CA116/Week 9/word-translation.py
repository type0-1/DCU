#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
translation = {}

with open("translation.txt") as f:
   content = f.readlines()
   i = 0
   while i < len(content):
      new_content = content[i].strip()
      newer_content = new_content.split(" ")
      if newer_content[0] not in translation:
         translation[newer_content[0]] = newer_content[1]
      i += 1

i = 0
while i < len(inputs):
   numbers = inputs[i].strip()
   if numbers in translation:
      print(translation[numbers])
   i += 1
