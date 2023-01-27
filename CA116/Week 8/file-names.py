#!/usr/bin/env python3

import sys

files = sys.stdin.readlines()

i = 0

while i < len(files):
   content = files[i].strip()
   new_files = content.split("/")
   print(new_files[-1])
   i += 1
