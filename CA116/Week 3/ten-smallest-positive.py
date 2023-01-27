#!/usr/bin/env python3

i = 0

smallest = int(input())

while i < 9:

   n = int(input())

   if n < smallest and n > 0:
      smallest = n

   i = i + 1

print(smallest)
