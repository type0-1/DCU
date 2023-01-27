#!/usr/bin/env python3

i = 0

while i < 10:

   num = int(input())
   if i == 0 or largest < num:
      largest = num

   i = i + 1

print(largest)
