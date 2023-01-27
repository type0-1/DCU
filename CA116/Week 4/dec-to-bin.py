#!/usr/bin/env python3

n = int(input())
total = 0
i = 0
while n != 0:

   rem = n % 2
   total = (total * 10) + rem
   n = n // 2
   i = i + 1

s = str(total)
print(s[::-1])
