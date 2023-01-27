#!/usr/bin/env python3

i = 0
pos = 0
neg = 0
while i < 5:
   n = int(input())
   if 0 < n:
      pos = n + pos
   elif n < 0:
      neg = n + neg

   i = i + 1

print(neg, pos)
