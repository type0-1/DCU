#!/usr/bin/env python3

s = input()
i = 0
total = 0

while i < len(s):

   if ("a" <= s[i] and s[i] <= "z"):
      total = total + 1
   else:
      total = total + 0
   i = i + 1

print(total)
