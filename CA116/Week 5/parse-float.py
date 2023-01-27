#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and s[i] != ".":
   i = i + 1

if i < len(s):
   n1 = s[:i]
   n2 = s[i + 1:]

   print(n1)
   print(n2)
