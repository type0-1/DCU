#!/usr/bin/env python3

n = int(input())

x = 1

i = 0

while i < n:

   x = -x + (x % 2) * 2 - 1

   print(x)

   i = i + 1
