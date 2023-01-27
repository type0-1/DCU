#!/usr/bin/env python3

s = input()
i = 0

while i < len(s):
   chr = s[i]
   if "a" <= chr and chr <= "g":
      s = chr
   i = i + 1

print(s)
