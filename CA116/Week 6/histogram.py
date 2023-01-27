#!/usr/bin/env python3

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

s = input()
while s != "end":
   s = int(s)
   i = 0
   while i < len(count):
      if s == i:
         count[i] = count[i] + 1
      i += 1
   s = input()

i = 0

while i < len(count):
   print(i, count[i] * "*")
   i += 1
