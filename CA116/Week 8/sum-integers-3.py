#!/usr/bin/env python3

import sys

files = sys.argv[1:]

i = 0
total = 0

while i < len(files):
   with open(files[i]) as f:
      content = f.readlines()
      j = 0
      while j < len(content):
         new_content = content[j].strip()
         total = total + int(new_content)
         j += 1
   i += 1
print(total)
