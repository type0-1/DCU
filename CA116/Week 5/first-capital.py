#!/usr/bin/env python3

i = 0
s = input()

while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
   i += 1

if i < len(s):
   print(s[i], i)
