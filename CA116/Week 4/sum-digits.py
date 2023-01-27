#!/usr/bin/env python3

s = input()
i = 0
total = 0

while i < len(s):

   n = s[i]
   n = int(n)
   total = total + n
   n = n // 10

   i = i + 1

print(total)
