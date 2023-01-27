#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
prev = 0
for line in inputs:
   curr = len(line.strip())
   if prev < curr:
      prev = curr

for line in inputs:
   line = line.strip()
   print(f'{line:^{prev}}')
