#!/usr/bin/env python3

i = 0
total = 0

while i < 5:

   n = int(input())
   if n < 0:
      n = n * -1
      total = total + n
   else:
      total = total + n

   i = i + 1

print(total)
