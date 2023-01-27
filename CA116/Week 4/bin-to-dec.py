#!/usr/bin/env python3

n = int(input())
s = str(n)
i = 0
total = 0

while i < len(s):

   remain = n % 2
   n = n // 10
   result = (remain * (2 ** i))

   if result != 0:
      total = total + result
   i = i + 1
print(total)
