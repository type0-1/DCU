#!/usr/bin/env python3

import sys
import math

pi = math.pi

for nums in sys.stdin:
   n = int(nums)
   print(f'{pi:.{n}f}')
